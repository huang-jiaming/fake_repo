#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Invoice Batch Job - Generate monthly invoices.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

def run():
    """Generate invoices for all active policies. Duplicate invoice bug per CHANGELOG 2.3.2."""
    print("Generating invoices...")
    return 0

if __name__ == '__main__':
    sys.exit(run())
