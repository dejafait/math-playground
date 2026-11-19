# Run from any directory with: make -f /path/to/scripts/maintenance/Makefile help
ROOT := $(abspath $(dir $(lastword $(MAKEFILE_LIST)))/../..)
PYTHON ?= python3

.PHONY: help evidence check test quota-history review math-processes inventory math-save-diagnostics math-push

help:
	@echo "review     Summarize recent loop activity, models, quota observations and checkpoints (read-only)"
	@echo "math-processes  Inspect live loop supervisor/worker processes (read-only)"
	@echo "inventory  Measure untracked files before preserving research progress"
	@echo "math-save-diagnostics  Commit only the reusable diagnostic commands (requires an empty staging area)"
	@echo "math-push  Push committed main to origin; never stages working files"
	@echo "quota-history  Rebuild observed subscription allowance history from local logs (no API calls)"
	@echo "evidence  Restore exact certificate bytes from tracked lossless archives (no regeneration)"
	@echo "check  Validate all notebook links, DAGs and startup byte/line budgets (no inference)"
	@echo "test   Run offline supervisor and documentation regressions (no inference)"

evidence:
	$(PYTHON) -B "$(ROOT)/scripts/maintenance/materialize_evidence.py"

quota-history:
	$(PYTHON) -B "$(ROOT)/scripts/maintenance/quota_history.py"

# DAYS can be overridden, for example: make review DAYS=7.
DAYS ?= 14
review:
	$(PYTHON) -B "$(ROOT)/scripts/maintenance/loop_review.py" --days "$(DAYS)"

# Kept separate because operating-system process inspection needs extra permission.
math-processes:
	ps -axo pid,ppid,etime,%cpu,command | awk 'NR==1 || /[s]cripts\/loop\/runner[.]py/ || /[c]odex.* exec --sandbox/'

math-save-diagnostics:
	git -C "$(ROOT)" diff --cached --quiet
	git -C "$(ROOT)" add -- Makefile scripts/maintenance/Makefile scripts/maintenance/loop_review.py scripts/maintenance/test_loop_review.py
	git -C "$(ROOT)" diff --cached --check
	git -C "$(ROOT)" commit -m "Maintain reusable mathematical loop diagnostics"

math-push:
	git -C "$(ROOT)" push origin main

inventory:
	mkdir -p "$(ROOT)/.generated/maintenance"
	git -C "$(ROOT)" ls-files --others --exclude-standard -z > "$(ROOT)/.generated/maintenance/untracked.nul"
	$(PYTHON) -B "$(ROOT)/scripts/maintenance/loop_review.py" --inventory "$(ROOT)/.generated/maintenance/untracked.nul"

check: evidence
	$(PYTHON) -B "$(ROOT)/scripts/docs/check_structure.py"

test:
	$(PYTHON) -B -m unittest discover -s "$(ROOT)/scripts/maintenance" -p 'test_*.py' -q
	$(PYTHON) -B -m unittest discover -s "$(ROOT)/scripts/docs" -p 'test_*.py' -q
	$(PYTHON) -B -m unittest discover -s "$(ROOT)/scripts/loop" -p 'test_*.py' -q
