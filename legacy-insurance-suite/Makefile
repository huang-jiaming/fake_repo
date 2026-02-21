# Legacy Insurance Suite - Makefile
# FICTIONAL DEMO - Do not use in production

.PHONY: test install

install:
	pip install -r requirements.txt

test:
	python -m pytest tests/ -v
	# Note: Some tests may fail intermittently (test_claims_integration)

lint:
	flake8 services/ batch/ etl/ shared/ 2>/dev/null || echo "flake8 not installed"
