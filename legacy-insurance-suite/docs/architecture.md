# Legacy Insurance Suite - Architecture Notes

> Last updated: 2018 (notes may be stale)

## System Overview

The Legacy Insurance Suite consists of three main services that share a common database and messaging layer. Data flows from policy creation through claims and billing.

```
[Policy Admin] --> [Claims] --> [Billing]
       |               |             |
       v               v             v
   [Shared DB]    [Message Queue]  [External APIs]
```

## Components

### Policy Admin Service
- Handles policy CRUD, renewals, endorsements
- Located in `services/policy_admin/`
- Uses `policy_engine.py` for business rules (complex, hard to maintain)

### Claims Service
- Processes claims, adjudication, payouts
- Located in `services/claims/`
- Duplicates some validation logic from policy_admin (known issue)

### Billing Service
- Premium calculation, invoicing, payment processing
- Located in `services/billing/`
- Has its own copy of premium calculation (should be shared)

### Batch Jobs
- Daily/monthly reconciliation, report generation
- Cron-driven, fragile error handling
- See `batch/jobs/`

### ETL Pipelines
- Data sync to data warehouse
- Some pipelines have not been updated since 2014

## Known Pain Points

1. **Duplicate Business Logic**: Premium calculation exists in 3 places. Policy validation in 2. Risk of divergence.

2. **Python 2 Compatibility**: Many modules use `print` statements, `except Exception, e`, and `unicode` handling. Migration to Python 3 incomplete.

3. **Monolithic Classes**: `PolicyEngine` (policy_admin) is 2000+ lines. `ClaimsProcessor` similarly large.

4. **Hardcoded Values**: Database hosts, API keys, magic numbers scattered throughout. Config management inconsistent.

5. **Flaky Tests**: `tests/test_claims_integration.py` fails intermittently (timing). Several tests marked xfail but never fixed.

6. **Missing Tests**: Critical paths in billing reconciliation and ETL have no automated tests.

7. **Cron Scripts**: `scripts/daily_backup.sh` and batch jobs use brittle error handling. No retry logic.

8. **Outdated Dependencies**: requirements.txt has packages from 2015. Some have known CVEs.

9. **Tight Coupling**: Services share database tables directly. No clear API boundaries.

10. **Documentation Drift**: This document and runbooks may not reflect current state.

## Database Schema (Partial)

- `policies` - Policy records
- `claims` - Claims records
- `invoices` - Billing invoices
- `payments` - Payment history
- `audit_log` - Audit trail (rarely used)

## Deployment

Historically deployed on bare metal. Migration to containers planned but not executed.
