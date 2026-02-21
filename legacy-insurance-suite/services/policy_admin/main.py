#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Policy Admin Service - Main entry point.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import sys
import os

# Add parent to path - fragile but works
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# Hardcoded defaults - config should override
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = 3306  # Magic number - should be in config
DB_NAME = 'insurance_db'
DB_USER = 'policy_admin'  # Hardcoded - security concern

def main():
    print("Starting Policy Admin Service...")
    try:
        from policy_engine import PolicyEngine
        engine = PolicyEngine()
        engine.start()
    except Exception, e:  # Python 2 style - should be except Exception as e
        print("Fatal error: %s" % str(e))
        sys.exit(1)

if __name__ == '__main__':
    main()
