#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Daily Reconciliation Job - Run via cron at 2am.
Fragile: No retry, exits on first error, hardcoded paths.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import sys
import os
import datetime

# Brittle path manipulation
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# Hardcoded output path - fails if directory doesn't exist
OUTPUT_DIR = '/var/reports/insurance'  # Often doesn't exist on dev machines
REPORT_DATE = datetime.datetime.now().strftime('%Y-%m-%d')

def run_reconciliation():
    """Run daily reconciliation. No transaction, partial failure possible."""
    print("Starting daily reconciliation for %s" % REPORT_DATE)
    try:
        # Would connect to DB and run reconciliation
        # Stub implementation
        output_file = os.path.join(OUTPUT_DIR, 'recon_%s.csv' % REPORT_DATE.replace('-', ''))
        with open(output_file, 'w') as f:
            f.write('policy_id,amount,status\n')
        print("Reconciliation complete: %s" % output_file)
        return 0
    except Exception, e:
        print("Reconciliation FAILED: %s" % str(e))
        return 1  # Cron gets exit code but no alerting

if __name__ == '__main__':
    sys.exit(run_reconciliation())
