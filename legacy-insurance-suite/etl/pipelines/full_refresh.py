#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Full Refresh ETL - Full data warehouse refresh. No incremental.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

def run_full_refresh():
    """Full refresh - truncates and reloads. No backup."""
    print("Running full refresh - WARNING: destructive")
    return 0
