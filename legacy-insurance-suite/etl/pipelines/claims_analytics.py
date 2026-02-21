#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Claims Analytics ETL - Load claims data for analytics.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

def run():
    """Run claims analytics pipeline. Fails intermittently per CHANGELOG."""
    print("Running claims analytics ETL...")
    return 0

if __name__ == '__main__':
    sys.exit(run())
