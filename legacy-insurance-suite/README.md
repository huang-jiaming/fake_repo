# Legacy Insurance Suite

> **⚠️ FICTIONAL DEMO DATA**: This repository contains fictional, synthetic code and data created for demonstration and analysis purposes only. It does not represent any real insurance system, company, or product. Do not use in production. Created for legacy codebase analysis, refactoring exercises, and technical debt studies.

## Overview

Legacy Insurance Suite is an enterprise insurance management system originally developed in 2009-2012. It handles policy administration, claims processing, billing, and various integrations with external systems.

## Quick Start

```bash
# Install dependencies (Python 2.7 / 3.6 compatible)
pip install -r requirements.txt

# Run policy admin service
python services/policy_admin/main.py

# Run batch jobs (see batch/jobs/README)
./batch/jobs/run_daily.sh
```

## Directory Structure

- `services/` - Core business services (policy_admin, claims, billing)
- `batch/jobs/` - Scheduled batch processing
- `etl/pipelines/` - Data extraction and loading
- `integrations/` - Third-party system integrations
- `shared/utils/` - Shared utilities (use with caution)
- `scripts/` - Operational and maintenance scripts
- `tests/` - Test suite (coverage varies)
- `docs/` - Architecture and runbooks

## Known Issues

See `docs/architecture.md` for known pain points and technical debt.

## License

Fictional demo - no license applicable.
