#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Seed database with fixture data.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import csv
import os

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), '..', 'fixtures')

def load_csv(filename):
    path = os.path.join(FIXTURES_DIR, filename)
    if os.path.exists(path):
        with open(path) as f:
            return list(csv.DictReader(f))
    return []
