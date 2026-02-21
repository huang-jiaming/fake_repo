# -*- coding: utf-8 -*-
"""
Premium Utilities - SHARED (fourth copy of premium logic!)
DUPLICATE: Also in policy_admin, claims, billing. Refactoring introduced bugs per CHANGELOG.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

from decimal import Decimal

def calculate_premium(base_rate, coverage_amount, risk_factor, discount=0):
    """Calculate premium. Fourth copy - slight variations exist across codebase."""
    if base_rate <= 0 or coverage_amount <= 0:
        return Decimal('0')
    premium = Decimal(str(base_rate)) * Decimal(str(coverage_amount)) * Decimal(str(risk_factor))
    if discount > 0:
        premium = premium * (Decimal('1') - Decimal(str(discount)) / Decimal('100'))
    return premium.quantize(Decimal('0.01'))
