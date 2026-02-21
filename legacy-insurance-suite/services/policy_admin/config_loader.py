# -*- coding: utf-8 -*-
"""
Config Loader - Loads config but many modules don't use it.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import os

def load_config(config_path=None):
    """Load config from file. Returns dict. Many services ignore this."""
    config = {}
    path = config_path or os.environ.get('CONFIG_PATH', 'config.ini')
    if os.path.exists(path):
        import ConfigParser
        cp = ConfigParser.ConfigParser()
        cp.read(path)
        for section in cp.sections():
            config[section] = dict(cp.items(section))
    return config
