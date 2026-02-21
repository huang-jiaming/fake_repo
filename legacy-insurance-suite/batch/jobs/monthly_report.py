#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Monthly Report Job - Run 1st of each month.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import sys
import os
import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# Hardcoded - same as daily_reconciliation
OUTPUT_DIR = '/var/reports/insurance'

def main():
    month = datetime.datetime.now().strftime('%Y-%m')
    print("Generating monthly report for %s" % month)
    # Stub - real implementation would aggregate data
    return 0

if __name__ == '__main__':
    sys.exit(main())
