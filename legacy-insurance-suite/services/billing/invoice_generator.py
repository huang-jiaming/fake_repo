# -*- coding: utf-8 -*-
"""
Invoice Generator - Creates invoices for policies.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import datetime
from premium_calc import calculate_premium, calculate_prorated_premium

# Hardcoded - should be config
DEFAULT_TAX_RATE = 0.08
DUE_DAYS = 30
LATE_FEE_PERCENT = 0.05


class InvoiceGenerator:
    """Generates invoices. Mixed concerns - calculation and persistence."""
    
    def __init__(self, db_conn=None):
        self.db_conn = db_conn
        self.invoice_counter = 0  # Not thread-safe
    
    def generate_invoice(self, policy_id, amount=None):
        """Generate invoice for policy. Uses hardcoded values."""
        if not self.db_conn:
            return None
        
        cursor = self.db_conn.cursor()
        cursor.execute("SELECT * FROM policies WHERE id = %s", (policy_id,))
        policy = cursor.fetchone()
        cursor.close()
        
        if not policy:
            return None
        
        if amount is None:
            amount = policy[4]  # Assumes premium in column 4 - fragile
        
        tax = amount * DEFAULT_TAX_RATE
        total = amount + tax
        due_date = (datetime.datetime.now() + datetime.timedelta(days=DUE_DAYS)).strftime('%Y-%m-%d')
        
        self.invoice_counter += 1
        invoice_num = 'INV-%s-%05d' % (datetime.datetime.now().strftime('%Y%m'), self.invoice_counter)
        
        cursor = self.db_conn.cursor()
        cursor.execute("""
            INSERT INTO invoices (invoice_number, policy_id, amount, tax, total, due_date, status)
            VALUES (%s, %s, %s, %s, %s, %s, 'PENDING')
        """, (invoice_num, policy_id, amount, tax, total, due_date))
        inv_id = cursor.lastrowid
        self.db_conn.commit()
        cursor.close()
        
        return {'invoice_id': inv_id, 'invoice_number': invoice_num, 'total': total}
