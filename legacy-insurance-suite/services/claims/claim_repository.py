# -*- coding: utf-8 -*-
"""
Claim Repository - Data access for claims.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

class ClaimRepository:
    def __init__(self, db_conn):
        self.conn = db_conn
    
    def find_by_id(self, claim_id):
        if not self.conn:
            return None
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM claims WHERE id = %s", (claim_id,))
        row = cursor.fetchone()
        cursor.close()
        return row
    
    def find_pending(self, limit=100):
        if not self.conn:
            return []
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM claims WHERE status = 'PENDING' LIMIT %s", (limit,))
        rows = cursor.fetchall()
        cursor.close()
        return rows
