#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Claims Service - Main entry point.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# Hardcoded config
DB_HOST = os.environ.get('CLAIMS_DB_HOST', 'localhost')
QUEUE_HOST = 'localhost'  # Should be config
QUEUE_PORT = 5672

def main():
    print("Starting Claims Service...")
    try:
        from claims_processor import ClaimsProcessor
        processor = ClaimsProcessor()
        # In real service would connect to message queue
        print("Claims processor initialized (stub mode)")
    except Exception, e:
        print("Fatal error: %s" % str(e))
        sys.exit(1)

if __name__ == '__main__':
    main()
