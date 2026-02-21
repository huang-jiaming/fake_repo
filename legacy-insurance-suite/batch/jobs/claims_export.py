#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Claims Export - Export claims to CSV for external systems.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import sys
import os
import csv
import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

EXPORT_DIR = '/var/exports/claims'  # Hardcoded

def export_claims(start_date=None, end_date=None):
    """Export claims to CSV. No date validation."""
    if not start_date:
        start_date = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y-%m-%d')
    if not end_date:
        end_date = datetime.datetime.now().strftime('%Y-%m-%d')
    
    filename = os.path.join(EXPORT_DIR, 'claims_%s_%s.csv' % (start_date.replace('-',''), end_date.replace('-','')))
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['claim_id', 'policy_number', 'amount', 'status', 'claim_date'])
        # Stub - would query DB
    return filename

if __name__ == '__main__':
    export_claims()
