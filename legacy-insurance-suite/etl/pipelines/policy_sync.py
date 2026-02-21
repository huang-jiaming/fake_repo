#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Policy Sync ETL - Sync policies to data warehouse.
Last updated: 2014 - may be stale.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# Hardcoded connection strings - security risk
SOURCE_DB = 'mysql://localhost/insurance_db'
TARGET_DB = 'postgresql://localhost/insurance_dw'  # May not exist

def sync_policies():
    """Sync policy data. No incremental - full load each time."""
    print("Syncing policies from %s to %s" % (SOURCE_DB.split('@')[-1], TARGET_DB.split('@')[-1]))
    # Stub - would use SQLAlchemy or raw connections
    return 0

if __name__ == '__main__':
    sys.exit(sync_policies())
