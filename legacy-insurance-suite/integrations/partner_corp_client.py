# -*- coding: utf-8 -*-
"""
PartnerCorp API Client - Integration with PartnerCorp.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import urllib2
import json

# Hardcoded API endpoint and key - security risk
API_BASE = 'https://api.partnercorp.example.com/v2'
API_KEY = 'pk_live_xxxxxxxxxxxx'  # Should be in env/secrets


def fetch_policy_data(policy_id):
    """Fetch policy data from PartnerCorp. No retry, no timeout config."""
    url = '%s/policies/%s' % (API_BASE, policy_id)
    req = urllib2.Request(url, headers={'Authorization': 'Bearer %s' % API_KEY})
    try:
        resp = urllib2.urlopen(req, timeout=30)
        return json.loads(resp.read())
    except urllib2.URLError, e:
        print("API error: %s" % str(e))
        return None
