# Run from any directory with: make -f /path/to/scripts/maintenance/Makefile help
ROOT := $(abspath $(dir $(lastword $(MAKEFILE_LIST)))/../..)
PYTHON ?= python3

.PHONY: help evidence check test

help:
	@echo "evidence  Restore exact certificate bytes from tracked lossless archives (no regeneration)"
	@echo "check  Validate all notebook links, DAGs and startup byte/line budgets (no inference)"
	@echo "test   Run offline supervisor and documentation regressions (no inference)"

evidence:
	$(PYTHON) -B "$(ROOT)/scripts/maintenance/materialize_evidence.py"

check: evidence
	$(PYTHON) -B "$(ROOT)/scripts/docs/check_structure.py"

test:
	$(PYTHON) -B -m unittest discover -s "$(ROOT)/scripts/maintenance" -p 'test_*.py' -q
	$(PYTHON) -B -m unittest discover -s "$(ROOT)/scripts/docs" -p 'test_*.py' -q
	$(PYTHON) -B -m unittest discover -s "$(ROOT)/scripts/loop" -p 'test_*.py' -q
