#!/bin/bash
# Daily backup script - Run from cron
# Fragile: No retry, hardcoded paths, assumes pg_dump/mysqldump in PATH
# FICTIONAL DEMO - Do not use in production

BACKUP_DIR="/var/backups/insurance"
DATE=$(date +%Y%m%d)
DB_NAME="insurance_db"

mkdir -p "$BACKUP_DIR"
# No check if mkdir fails

mysqldump -u root -pchangeme "$DB_NAME" > "$BACKUP_DIR/backup_$DATE.sql"
# Password in command line - visible in process list
# No verification of backup success

echo "Backup complete: $BACKUP_DIR/backup_$DATE.sql"
