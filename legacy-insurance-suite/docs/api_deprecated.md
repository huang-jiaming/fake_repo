# Deprecated API Endpoints

These endpoints are deprecated but still in use by 3 clients as of 2020.

## SOAP PolicyLookup (removed 2018)
- Was: /soap/PolicyLookup
- Replacement: GET /api/v1/policies?policy_number={id}

## Legacy batch format (removed 2014)
- Old batch job output format no longer supported
- Use new CSV format from batch/jobs/
