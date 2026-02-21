# -*- coding: utf-8 -*-
"""
Acme Reinsurance Integration - Cede policies to reinsurer.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

# Hardcoded
ACME_API_URL = 'https://reinsurance.acme.example.com/api'
ACME_USER = 'legacy_insurance'
ACME_PASS = 'changeme'  # Should never be in code

def cede_policy(policy_data):
    """Send policy to reinsurer. No validation of response."""
    import urllib2
    import base64
    import json
    
    auth = base64.b64encode('%s:%s' % (ACME_USER, ACME_PASS))
    req = urllib2.Request(ACME_API_URL + '/cede', 
                         data=json.dumps(policy_data),
                         headers={'Authorization': 'Basic %s' % auth, 'Content-Type': 'application/json'})
    try:
        resp = urllib2.urlopen(req)
        return json.loads(resp.read())
    except Exception, e:
        print("Cede failed: %s" % str(e))
        return None
