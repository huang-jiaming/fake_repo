# -*- coding: utf-8 -*-
"""
Database Utilities - Connection handling.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

# Hardcoded defaults
DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 3306
DEFAULT_DB = 'insurance_db'

def get_connection(host=None, port=None, db=None, user='root', password=''):
    """Get database connection. No connection pooling."""
    try:
        import MySQLdb
        return MySQLdb.connect(
            host=host or DEFAULT_HOST,
            port=port or DEFAULT_PORT,
            user=user,
            passwd=password,
            db=db or DEFAULT_DB
        )
    except Exception, e:
        print("DB connection failed: %s" % str(e))
        return None
