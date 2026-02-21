# -*- coding: utf-8 -*-
"""
Legacy SOAP Client - For deprecated SOAP endpoints.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

# SOAP endpoint removed 2018 but client code remains
SOAP_ENDPOINT = 'http://localhost:5000/soap/PolicyLookup'

def lookup_policy_soap(policy_number):
    """SOAP lookup - endpoint no longer exists."""
    try:
        import suds
        client = suds.Client(SOAP_ENDPOINT)
        return client.service.LookupPolicy(policy_number)
    except Exception, e:
        print("SOAP lookup failed: %s" % str(e))
        return None
