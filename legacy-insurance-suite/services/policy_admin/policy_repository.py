# -*- coding: utf-8 -*-
"""
Policy Repository - Data access layer.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import datetime

class PolicyRepository:
    """Repository for policy CRUD. Uses raw SQL - no ORM."""
    
    def __init__(self, db_conn):
        self.conn = db_conn
    
    def find_by_policy_number(self, policy_number):
        """Find policy by policy number. SQL injection risk if not parameterized."""
        if not self.conn:
            return None
        cursor = self.conn.cursor()
        # Note: Using %s is correct for MySQLdb, but ensure caller validates
        cursor.execute("SELECT * FROM policies WHERE policy_number = %s", (policy_number,))
        row = cursor.fetchone()
        cursor.close()
        return row
    
    def find_active_policies(self, state=None, limit=1000):
        """Find active policies. Magic number 1000 - should be configurable."""
        if not self.conn:
            return []
        cursor = self.conn.cursor()
        if state:
            cursor.execute(
                "SELECT * FROM policies WHERE status = 'ACTIVE' AND state = %s LIMIT %s",
                (state, limit)
            )
        else:
            cursor.execute(
                "SELECT * FROM policies WHERE status = 'ACTIVE' LIMIT %s",
                (limit,)
            )
        rows = cursor.fetchall()
        cursor.close()
        return rows
    
    def update_status(self, policy_id, new_status):
        """Update policy status."""
        if not self.conn:
            return False
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "UPDATE policies SET status = %s, updated_at = %s WHERE id = %s",
                (new_status, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), policy_id)
            )
            self.conn.commit()
            cursor.close()
            return True
        except Exception, e:
            print("Update failed: %s" % str(e))
            return False
