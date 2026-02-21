#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Validate config files - Basic config check.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import os

def validate():
    config_files = ['config.ini', 'config.yml']
    for f in config_files:
        if os.path.exists(f):
            print("OK: %s" % f)
        else:
            print("MISSING: %s" % f)

if __name__ == '__main__':
    validate()
