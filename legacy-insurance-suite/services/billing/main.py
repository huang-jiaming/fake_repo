#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Billing Service - Main entry point.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

def main():
    print("Starting Billing Service...")
    # Hardcoded - no config loading
    db_host = os.environ.get('BILLING_DB_HOST', 'localhost')
    print("DB host: %s" % db_host)

if __name__ == '__main__':
    main()
