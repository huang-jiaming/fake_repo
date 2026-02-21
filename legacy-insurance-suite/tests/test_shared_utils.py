# -*- coding: utf-8 -*-
"""
Shared Utils Tests - Basic tests.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

class TestSharedUtils(unittest.TestCase):
    
    def test_premium_utils(self):
        from shared.utils.premium_utils import calculate_premium
        result = calculate_premium(0.01, 1000, 1.0)
        self.assertEqual(float(result), 10.0)
    
    def test_validation(self):
        from shared.utils.validation import is_valid_policy_number
        self.assertTrue(is_valid_policy_number('POL-12345'))
        self.assertFalse(is_valid_policy_number('x'))
