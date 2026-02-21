# -*- coding: utf-8 -*-
"""
Mainframe Screen Scraper - Integration with legacy mainframe.
Fragile: Fails when mainframe format changes. Per CHANGELOG 2012.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

# Hardcoded screen positions - breaks when mainframe UI changes
POLICY_NUM_START = 10
POLICY_NUM_END = 19
AMOUNT_START = 45
AMOUNT_END = 55

def parse_mainframe_screen(screen_text):
    """Parse mainframe screen. Assumes fixed column positions."""
    if not screen_text or len(screen_text) < AMOUNT_END:
        return None
    return {
        'policy_number': screen_text[POLICY_NUM_START:POLICY_NUM_END].strip(),
        'amount': screen_text[AMOUNT_START:AMOUNT_END].strip()
    }
