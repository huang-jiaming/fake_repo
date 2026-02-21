#!/bin/bash
# Cleanup old report files - Run weekly
# FICTIONAL DEMO - Do not use in production

REPORT_DIR="/var/reports/insurance"
RETENTION_DAYS=90

find "$REPORT_DIR" -name "*.csv" -mtime +$RETENTION_DAYS -delete
# No error handling if find fails
