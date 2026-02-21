# -*- coding: utf-8 -*-
"""
Premium Calculator - Billing service premium calculation.
DUPLICATE: Same logic in policy_admin/policy_engine.py and claims/claims_processor.py
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

from decimal import Decimal

# Third copy of premium calculation - risk of divergence
def calculate_premium(base_rate, coverage_amount, risk_factor, discount=0):
    """Calculate premium. DUPLICATED in policy_admin and claims - sync required!"""
    if base_rate <= 0 or coverage_amount <= 0:
        return Decimal('0')
    premium = Decimal(str(base_rate)) * Decimal(str(coverage_amount)) * Decimal(str(risk_factor))
    if discount > 0:
        premium = premium * (Decimal('1') - Decimal(str(discount)) / Decimal('100'))
    return premium.quantize(Decimal('0.01'))


def calculate_prorated_premium(full_premium, days_elapsed, total_days=365):
    """Prorate premium. Magic number 365 - doesn't handle leap year consistently."""
    if total_days <= 0:
        return Decimal('0')
    return (Decimal(str(full_premium)) * Decimal(str(days_elapsed)) / Decimal(str(total_days))).quantize(Decimal('0.01'))
