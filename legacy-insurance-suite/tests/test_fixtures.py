# -*- coding: utf-8 -*-
"""
Fixture loading tests.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import unittest
import os

class TestFixtures(unittest.TestCase):
    
    def test_fixtures_exist(self):
        fixtures_dir = os.path.join(os.path.dirname(__file__), '..', 'fixtures')
        self.assertTrue(os.path.exists(os.path.join(fixtures_dir, 'policies.csv')))
        self.assertTrue(os.path.exists(os.path.join(fixtures_dir, 'claims.csv')))
