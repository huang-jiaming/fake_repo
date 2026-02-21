# -*- coding: utf-8 -*-
"""
Billing Tests - Partial coverage. Critical reconciliation path untested.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

class TestBillingPremiumCalc(unittest.TestCase):
    """Tests for premium calculation. Billing reconciliation has NO tests."""
    
    def test_premium_calculation(self):
        from services.billing.premium_calc import calculate_premium
        result = calculate_premium(0.0025, 100000, 1.0, 10)
        self.assertAlmostEqual(float(result), 225.0, places=2)
    
    def test_prorated_premium(self):
        from services.billing.premium_calc import calculate_prorated_premium
        result = calculate_prorated_premium(365, 30, 365)
        self.assertAlmostEqual(float(result), 30.0, places=2)
