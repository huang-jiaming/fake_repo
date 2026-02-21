# -*- coding: utf-8 -*-
"""
Policy Admin REST API - Flask-based.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

try:
    from flask import Flask, request, jsonify
    FLASK_AVAILABLE = True
except ImportError:
    FLASK_AVAILABLE = False

# Hardcoded - should be in config
API_PORT = 5000
DEBUG_MODE = True  # Never use True in production!

app = Flask(__name__) if FLASK_AVAILABLE else None

if app:
    @app.route('/api/v1/policies', methods=['GET'])
    def list_policies():
        """List policies. No pagination - returns up to 10000. Performance risk."""
        try:
            from .policy_engine import PolicyEngine
            engine = PolicyEngine()
            # Direct DB access - bypasses repository
            if engine.db_conn:
                cursor = engine.db_conn.cursor()
                cursor.execute("SELECT id, policy_number, insured_name, status FROM policies LIMIT 10000")
                rows = cursor.fetchall()
                cursor.close()
                return jsonify([dict(zip(['id','policy_number','insured_name','status'], r)) for r in rows])
            return jsonify([])
        except Exception, e:
            return jsonify({'error': str(e)}), 500
    
    @app.route('/api/v1/policies', methods=['POST'])
    def create_policy():
        """Create policy. No rate limiting."""
        data = request.get_json() or {}
        try:
            from .policy_engine import PolicyEngine
            engine = PolicyEngine()
            policy_id = engine.create_policy(data)
            return jsonify({'policy_id': policy_id}), 201
        except ValueError, e:
            return jsonify({'error': str(e)}), 400
        except Exception, e:
            return jsonify({'error': str(e)}), 500

def run_api():
    if app:
        app.run(host='0.0.0.0', port=API_PORT, debug=DEBUG_MODE)
    else:
        print("Flask not available - API disabled")
