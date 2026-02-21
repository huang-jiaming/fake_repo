# Operations Runbook

> Last updated: 2017 - may be outdated

## Common Issues

### Batch job fails
1. Check /var/log/insurance/batch.log
2. Verify DB connectivity: `python scripts/health_check.py`
3. Manually re-run: `./batch/jobs/run_daily.sh`
4. No automated retry - contact on-call if persists

### ETL pipeline intermittent failures
- Known issue per CHANGELOG. Restart pipeline manually.
- Check disk space in /var/reports/

### Policy creation slow
- Check policy_engine logs
- May need to increase DB connection pool (see config.ini)

### Claims stuck in PENDING
- Manual review required for claims > $25,000
- Use admin UI (if available) or direct DB update

## Restart Procedures

```bash
# Policy Admin
sudo systemctl restart policy-admin  # or init script

# Claims
sudo systemctl restart claims-service

# Billing
sudo systemctl restart billing-service
```

## Contacts

- Escalation: [fictional - not real]
- DBA: [fictional - not real]
