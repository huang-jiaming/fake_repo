# -*- coding: utf-8 -*-
"""
Logging utilities - Inconsistent logging across codebase.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import logging

# Many modules use print() instead of this
def get_logger(name):
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        logger.addHandler(handler)
    return logger
