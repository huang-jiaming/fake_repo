#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Billing Export ETL - Export billing data.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

def export_billing():
    print("Exporting billing data...")
    return 0

if __name__ == '__main__':
    sys.exit(export_billing())
