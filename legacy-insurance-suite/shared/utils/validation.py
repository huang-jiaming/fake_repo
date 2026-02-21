# -*- coding: utf-8 -*-
"""
Validation utilities - Yet another copy of policy number validation.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

def is_valid_policy_number(pn):
    """Validate policy number. Fifth copy in codebase."""
    return pn and len(pn) >= 5 and (pn.isdigit() or (pn.startswith('POL-') and len(pn) == 9))
