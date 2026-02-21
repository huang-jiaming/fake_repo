#!/bin/bash
# Deployment script - Outdated, references deprecated paths
# FICTIONAL DEMO - Do not use in production

echo "Deploying Legacy Insurance Suite..."
# References old directory structure
cd /opt/legacy-insurance 2>/dev/null || cd "$(dirname "$0")/.."

# No version check, no rollback capability
pip install -r requirements.txt
python -m py_compile services/policy_admin/*.py 2>/dev/null || true

echo "Deploy complete. Restart services manually."
