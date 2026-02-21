# Developer Onboarding

> Last updated: 2016

## Setup

1. Clone repository
2. `pip install -r requirements.txt`
3. Create database: `mysql < schema.sql`
4. Copy config.ini: `cp config.ini.example config.ini` (if exists)
5. Run tests: `make test` (expect some failures)

## Key Files

- `services/policy_admin/policy_engine.py` - Core policy logic
- `services/claims/claims_processor.py` - Claims logic
- `config.ini` - Main config (some services ignore it)

## Known Gotchas

- Python 2 and 3 compatibility issues
- Some tests are flaky - run multiple times
- ETL pipelines require data warehouse (may not exist locally)
