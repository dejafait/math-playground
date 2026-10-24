# Run from any directory with: make -f /path/to/scripts/maintenance/Makefile help
ROOT := $(abspath $(dir $(lastword $(MAKEFILE_LIST)))/../..)
PYTHON ?= python3

.PHONY: help check test

help:
	@echo "check  Validate all notebook links, DAGs and startup byte/line budgets (no inference)"
	@echo "test   Run offline supervisor and documentation regressions (no inference)"

check:
	$(PYTHON) -B "$(ROOT)/scripts/docs/check_structure.py"

test:
	$(PYTHON) -B -m unittest discover -s "$(ROOT)/scripts/docs" -p 'test_*.py' -q
	$(PYTHON) -B -m unittest discover -s "$(ROOT)/scripts/loop" -p 'test_*.py' -q
