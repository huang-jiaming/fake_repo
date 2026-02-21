# Batch Jobs

Run via cron. See crontab.example. No retry logic - failures require manual intervention.

## Jobs

- daily_reconciliation.py - Daily reconciliation (run at 2am)
- monthly_report.py - Monthly report generation (run 1st of month)
- policy_expiry_notifications.py - Send expiry notices
- claims_export.py - Export claims to CSV
