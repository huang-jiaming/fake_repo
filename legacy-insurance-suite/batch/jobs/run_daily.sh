#!/bin/bash
# Daily batch job runner - Run from cron
# Fragile: No error handling, continues on failure
# FICTIONAL DEMO - Do not use in production

set -e  # Exit on first error - but no retry or alerting

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON=${PYTHON:-python}  # Assumes python in PATH

echo "Starting daily batch jobs..."

# Hardcoded paths
$PYTHON "$SCRIPT_DIR/daily_reconciliation.py" || echo "Reconciliation failed"
$PYTHON "$SCRIPT_DIR/claims_export.py" || echo "Claims export failed"
$PYTHON "$SCRIPT_DIR/policy_expiry_notifications.py" || echo "Expiry notifications failed"

echo "Daily batch complete"
