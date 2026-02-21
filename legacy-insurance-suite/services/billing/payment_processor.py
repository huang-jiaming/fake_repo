# -*- coding: utf-8 -*-
"""
Payment Processor - Process payments for invoices.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import datetime

class PaymentProcessor:
    def __init__(self, db_conn=None):
        self.db_conn = db_conn
    
    def record_payment(self, invoice_id, amount, method='CHECK'):
        """Record payment. No idempotency - duplicate submissions create duplicates."""
        if not self.db_conn:
            return False
        cursor = self.db_conn.cursor()
        cursor.execute("""
            INSERT INTO payments (invoice_id, amount, method, paid_at)
            VALUES (%s, %s, %s, %s)
        """, (invoice_id, amount, method, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        self.db_conn.commit()
        cursor.close()
        return True
