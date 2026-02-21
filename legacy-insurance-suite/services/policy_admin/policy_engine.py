# -*- coding: utf-8 -*-
"""
Policy Engine - Core business logic for policy administration.
WARNING: This class has grown to 500+ lines. Consider splitting.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import re
import datetime
from decimal import Decimal

# Duplicate: Same validation logic exists in services/claims/claim_validator.py
def validate_policy_number(policy_num):
    """Validate policy number format. Duplicated in claims service."""
    if not policy_num or len(policy_num) < 5:
        return False
    # Legacy format: POL-XXXXX or just XXXXX
    if policy_num.startswith('POL-'):
        return len(policy_num) == 9 and policy_num[4:].isdigit()
    return policy_num.isdigit() and len(policy_num) <= 12


# Duplicate: Premium calculation also in services/billing/premium_calc.py and shared/utils/
def calculate_premium(base_rate, coverage_amount, risk_factor, discount=0):
    """Calculate premium. DUPLICATED in billing and shared utils - keep in sync!"""
    if base_rate <= 0 or coverage_amount <= 0:
        return Decimal('0')
    premium = Decimal(str(base_rate)) * Decimal(str(coverage_amount)) * Decimal(str(risk_factor))
    if discount > 0:
        premium = premium * (1 - Decimal(str(discount)) / 100)
    return premium.quantize(Decimal('0.01'))


class PolicyEngine:
    """
    Monolithic policy engine. Handles validation, creation, renewal, endorsement.
    Known issues: Too many responsibilities, hard to test, mixed concerns.
    """
    
    def __init__(self, config=None):
        self.config = config or {}
        self.db_conn = None
        # Hardcoded - should come from config
        self.max_coverage = 10000000
        self.min_coverage = 1000
        self.supported_states = ['CA', 'NY', 'TX', 'FL', 'IL', 'OH', 'PA', 'GA', 'NC', 'MI']
        self._init_db()
    
    def _init_db(self):
        """Initialize database connection. Fragile - no connection pooling."""
        try:
            import MySQLdb
            self.db_conn = MySQLdb.connect(
                host=self.config.get('db_host', 'localhost'),
                port=self.config.get('db_port', 3306),
                user=self.config.get('db_user', 'policy_admin'),
                passwd=self.config.get('db_pass', 'changeme'),
                db=self.config.get('db_name', 'insurance_db'),
                charset='utf8'
            )
        except ImportError:
            # Fallback for environments without MySQLdb
            self.db_conn = None
            print("Warning: MySQLdb not available, running in stub mode")
    
    def validate_policy(self, policy_data):
        """Validate policy data before creation/update. Long method - consider splitting."""
        errors = []
        
        # Policy number
        if not validate_policy_number(policy_data.get('policy_number', '')):
            errors.append('Invalid policy number format')
        
        # Coverage amount - magic numbers
        coverage = policy_data.get('coverage_amount', 0)
        try:
            coverage = float(coverage)
        except (ValueError, TypeError):
            errors.append('Invalid coverage amount')
            return errors
        
        if coverage < self.min_coverage:
            errors.append('Coverage below minimum %s' % self.min_coverage)
        if coverage > self.max_coverage:
            errors.append('Coverage above maximum %s' % self.max_coverage)
        
        # State validation
        state = policy_data.get('state', '').upper()
        if state not in self.supported_states:
            errors.append('Unsupported state: %s' % state)
        
        # Effective date
        eff_date = policy_data.get('effective_date')
        if eff_date:
            try:
                if isinstance(eff_date, basestring):
                    dt = datetime.datetime.strptime(eff_date, '%Y-%m-%d')
                else:
                    dt = eff_date
                if dt.date() < datetime.date.today():
                    errors.append('Effective date cannot be in the past')
            except Exception, e:
                errors.append('Invalid effective date: %s' % str(e))
        
        # Insured name
        name = policy_data.get('insured_name', '')
        if not name or len(name) < 2:
            errors.append('Invalid insured name')
        
        return errors
    
    def create_policy(self, policy_data):
        """Create new policy. Returns policy_id or raises."""
        errors = self.validate_policy(policy_data)
        if errors:
            raise ValueError('Validation failed: %s' % '; '.join(errors))
        
        base_rate = 0.0025  # Hardcoded rate - should be from rate table
        risk_factor = policy_data.get('risk_factor', 1.0)
        discount = policy_data.get('discount', 0)
        
        premium = calculate_premium(
            base_rate,
            policy_data['coverage_amount'],
            risk_factor,
            discount
        )
        
        policy_data['premium'] = float(premium)
        policy_data['status'] = 'ACTIVE'
        policy_data['created_at'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        if self.db_conn:
            cursor = self.db_conn.cursor()
            cursor.execute("""
                INSERT INTO policies (policy_number, insured_name, coverage_amount, 
                premium, state, effective_date, status, created_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                policy_data['policy_number'],
                policy_data['insured_name'],
                policy_data['coverage_amount'],
                policy_data['premium'],
                policy_data.get('state', 'CA'),
                policy_data.get('effective_date'),
                policy_data['status'],
                policy_data['created_at']
            ))
            policy_id = cursor.lastrowid
            self.db_conn.commit()
            cursor.close()
            return policy_id
        
        return 99999  # Stub return
    
    def renew_policy(self, policy_id):
        """Renew policy for another term. Duplicates some create logic."""
        if not self.db_conn:
            return False
        
        cursor = self.db_conn.cursor()
        cursor.execute("SELECT * FROM policies WHERE id = %s", (policy_id,))
        row = cursor.fetchone()
        cursor.close()
        
        if not row:
            return False
        
        # Hardcoded renewal period - 365 days
        new_expiry = datetime.datetime.now() + datetime.timedelta(days=365)
        cursor = self.db_conn.cursor()
        cursor.execute(
            "UPDATE policies SET expiry_date = %s, status = 'RENEWED' WHERE id = %s",
            (new_expiry.strftime('%Y-%m-%d'), policy_id)
        )
        self.db_conn.commit()
        cursor.close()
        return True
    
    def get_policy(self, policy_id):
        """Fetch policy by ID."""
        if not self.db_conn:
            return None
        
        cursor = self.db_conn.cursor()
        cursor.execute("SELECT * FROM policies WHERE id = %s", (policy_id,))
        row = cursor.fetchone()
        cursor.close()
        return row
    
    def start(self):
        """Start the policy engine (stub for service mode)."""
        print("Policy engine started (stub mode)")
