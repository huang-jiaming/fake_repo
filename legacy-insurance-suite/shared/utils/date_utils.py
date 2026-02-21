# -*- coding: utf-8 -*-
"""
Date Utilities - Date handling. Inconsistent with datetime usage elsewhere.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import datetime

def parse_date(date_str, fmt='%Y-%m-%d'):
    """Parse date string. Doesn't handle timezone."""
    try:
        return datetime.datetime.strptime(date_str, fmt).date()
    except Exception, e:
        return None

def add_days(dt, days):
    """Add days to date. Doesn't handle month/year rollover edge cases."""
    if hasattr(dt, 'date'):
        dt = dt.date()
    return dt + datetime.timedelta(days=days)
