#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Policy Expiry Notifications - Send notices for expiring policies.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import sys
import os
import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# Magic number - policies expiring in next 30 days
DAYS_AHEAD = 30

def run():
    cutoff = datetime.datetime.now() + datetime.timedelta(days=DAYS_AHEAD)
    print("Checking policies expiring before %s" % cutoff.date())
    # Would query DB and send emails
    return 0

if __name__ == '__main__':
    sys.exit(run())
