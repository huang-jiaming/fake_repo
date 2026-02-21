# -*- coding: utf-8 -*-
"""
Claim Validator - Validates claims before processing.
DUPLICATE: Policy number validation duplicated from services/policy_admin/policy_engine.py
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import datetime

# DUPLICATE - Same function in policy_admin/policy_engine.py - keep in sync!
def validate_policy_number(policy_num):
    """Validate policy number. Duplicated from policy_admin - slight variation in format check."""
    if not policy_num or len(policy_num) < 5:
        return False
    if policy_num.startswith('POL-'):
        return len(policy_num) == 9 and policy_num[4:].isdigit()
    return policy_num.isdigit() and len(policy_num) <= 12


def validate_claim_amount(amount, max_claim=5000000):
    """Validate claim amount. Magic number - should be configurable."""
    try:
        amt = float(amount)
        return amt > 0 and amt <= max_claim
    except (ValueError, TypeError):
        return False


def validate_claim_date(claim_date):
    """Validate claim date is not in future."""
    try:
        if isinstance(claim_date, basestring):
            dt = datetime.datetime.strptime(claim_date, '%Y-%m-%d')
        else:
            dt = claim_date
        return dt.date() <= datetime.date.today()
    except Exception, e:
        print("Date validation error: %s" % str(e))
        return False
