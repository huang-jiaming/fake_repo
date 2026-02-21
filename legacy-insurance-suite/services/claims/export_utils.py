# -*- coding: utf-8 -*-
"""
Claim Export Utilities - CSV export for claims.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import csv

def export_claims_to_csv(claims, filepath):
    """Export claims to CSV. Encoding issues with special chars per CHANGELOG."""
    with open(filepath, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['claim_id', 'policy_number', 'amount', 'status'])
        for c in claims:
            writer.writerow(c)
    return filepath
