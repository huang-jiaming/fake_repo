#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Database migration script - One-off migrations.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import sys

# No migration framework - raw SQL
MIGRATIONS = [
    "ALTER TABLE policies ADD COLUMN IF NOT EXISTS risk_score DECIMAL(5,2) DEFAULT 1.0",
    "CREATE INDEX IF NOT EXISTS idx_claims_status ON claims(status)",
]

def run_migrations(conn):
    for sql in MIGRATIONS:
        try:
            conn.cursor().execute(sql)
            conn.commit()
        except Exception, e:
            print("Migration failed: %s" % str(e))
            return 1
    return 0
