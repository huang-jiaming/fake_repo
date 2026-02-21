# Changelog

All notable changes to the Legacy Insurance Suite. Format based on Keep a Changelog.

## [2.4.1] - 2021-03-15
### Fixed
- Patch for premium calculation rounding in edge cases (POL-8923)
- Claims status update race condition (CLAIM-4451)

### Known Issues
- ETL pipeline for Q4 reports still failing intermittently

## [2.4.0] - 2020-11-20
### Added
- New integration endpoint for PartnerCorp API v2
- Batch job for monthly reconciliation report

### Changed
- Updated claims adjudication timeout from 30s to 60s
- Deprecated legacy policy lookup endpoint (still in use by 3 clients)

### Deprecated
- Python 2.7 support - target removal Q2 2021

## [2.3.2] - 2019-08-12
### Fixed
- Billing cycle calculation for leap year (BILL-2234)
- Duplicate invoice generation in batch job

### Security
- Rotated database credentials (manual process)

## [2.3.1] - 2019-04-22
### Fixed
- Policy renewal date off-by-one in certain timezones
- Claims export CSV encoding for special characters

## [2.3.0] - 2018-09-10
### Added
- ETL pipeline for claims analytics
- New config option for batch job concurrency

### Changed
- Migrated from MySQL 5.5 to 5.7 (incomplete)
- Increased default connection pool size

### Removed
- Legacy SOAP endpoint for PolicyLookup (replaced 2016, finally removed)

## [2.2.0] - 2017-06-15
### Added
- Integration with AcmeReinsurance API
- Batch job for policy expiration notifications

### Fixed
- Memory leak in long-running claims processor
- Timeout handling in billing service

## [2.1.0] - 2016-02-29
### Added
- REST API for policy admin (alongside existing SOAP)
- Basic audit logging (partial implementation)

### Changed
- Refactored shared utils (introduced new bugs, see POL-1234)
- Updated requirements.txt

## [2.0.0] - 2014-11-01
### Added
- Billing service split from monolith
- New ETL pipelines for data warehouse

### Changed
- Major database schema migration
- All services now use shared connection pool

### Breaking
- Old batch job format no longer supported
- Config file format changed (legacy.ini deprecated)

## [1.5.0] - 2013-05-20
### Added
- Claims service extraction from monolith
- Integration with external payment gateway

### Fixed
- Policy validation for international addresses
- Various null pointer exceptions

## [1.4.0] - 2012-08-14
### Added
- Batch job framework
- Initial ETL scripts

### Changed
- Upgraded to Python 2.7 (from 2.5)
- Improved error messages in policy engine

## [1.3.0] - 2012-01-10
### Added
- Policy endorsement workflow
- Basic unit tests (policy_admin only)

### Fixed
- Premium calculation for multi-policy discounts
- Date handling in claims processing

## [1.2.0] - 2011-06-01
### Added
- Claims processing automation
- Integration with legacy mainframe (screen scraping)

### Known Issues
- Mainframe integration fragile, fails on format changes

## [1.1.0] - 2010-09-15
### Added
- Billing module
- Monthly report generation

### Changed
- Database connection handling
- Config loading (now supports .ini files)

## [1.0.0] - 2009-12-01
### Added
- Initial release
- Policy administration
- Basic claims entry
- Manual billing process
- Shared utilities
