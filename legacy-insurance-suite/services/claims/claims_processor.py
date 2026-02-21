# -*- coding: utf-8 -*-
"""
Claims Processor - Core claims adjudication logic.
WARNING: 400+ line class. Known to have timing-sensitive behavior (flaky tests).
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import datetime
import time
from decimal import Decimal

# Duplicate: Premium calculation also in policy_admin and billing
def calculate_premium(base_rate, coverage_amount, risk_factor, discount=0):
    """Calculate premium. DUPLICATED - differs slightly in rounding from policy_admin!"""
    if base_rate <= 0 or coverage_amount <= 0:
        return Decimal('0')
    premium = Decimal(str(base_rate)) * Decimal(str(coverage_amount)) * Decimal(str(risk_factor))
    if discount > 0:
        premium = premium * (1 - Decimal(str(discount)) / 100)
    # Different rounding than policy_admin - potential bug
    return round(premium, 2)


try:
    from .claim_validator import validate_policy_number, validate_claim_amount, validate_claim_date
except ImportError:
    from claim_validator import validate_policy_number, validate_claim_amount, validate_claim_date


class ClaimsProcessor:
    """
    Monolithic claims processor. Handles validation, adjudication, payout.
    Known issues: Race conditions in status updates, no idempotency.
    """
    
    # Hardcoded thresholds - should be in config
    AUTO_APPROVE_LIMIT = 5000
    FRAUD_CHECK_THRESHOLD = 25000
    DEFAULT_DEDUCTIBLE = 500
    
    def __init__(self, db_conn=None):
        self.db_conn = db_conn
        self.processing_delay = 0.1  # Simulated processing - causes flaky tests
    
    def validate_claim(self, claim_data):
        """Validate claim before processing."""
        errors = []
        
        if not validate_policy_number(claim_data.get('policy_number', '')):
            errors.append('Invalid policy number')
        
        if not validate_claim_amount(claim_data.get('amount', 0)):
            errors.append('Invalid claim amount')
        
        if not validate_claim_date(claim_data.get('claim_date')):
            errors.append('Invalid claim date')
        
        claim_type = claim_data.get('claim_type', '')
        if claim_type not in ['AUTO', 'HOME', 'MEDICAL', 'OTHER']:
            errors.append('Invalid claim type')
        
        return errors
    
    def process_claim(self, claim_id):
        """
        Process a claim. Timing-sensitive - uses sleep which causes flaky tests.
        """
        if not self.db_conn:
            return {'status': 'ERROR', 'message': 'No database connection'}
        
        time.sleep(self.processing_delay)  # Simulated - causes test flakiness
        
        cursor = self.db_conn.cursor()
        cursor.execute("SELECT * FROM claims WHERE id = %s", (claim_id,))
        claim = cursor.fetchone()
        cursor.close()
        
        if not claim:
            return {'status': 'ERROR', 'message': 'Claim not found'}
        
        amount = claim[3]  # Assumes column order - fragile
        if amount <= self.AUTO_APPROVE_LIMIT:
            status = 'APPROVED'
        elif amount >= self.FRAUD_CHECK_THRESHOLD:
            status = 'PENDING_REVIEW'
        else:
            status = 'APPROVED'  # Simplified - real logic would be more complex
        
        # Race condition: Two concurrent calls could both update
        cursor = self.db_conn.cursor()
        cursor.execute(
            "UPDATE claims SET status = %s, processed_at = %s WHERE id = %s",
            (status, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), claim_id)
        )
        self.db_conn.commit()
        cursor.close()
        
        return {'status': status, 'claim_id': claim_id}
    
    def adjudicate_batch(self, claim_ids):
        """Process multiple claims. No transaction - partial failure leaves inconsistent state."""
        results = []
        for cid in claim_ids:
            try:
                result = self.process_claim(cid)
                results.append(result)
            except Exception, e:
                results.append({'status': 'ERROR', 'claim_id': cid, 'message': str(e)})
        return results
