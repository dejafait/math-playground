.PHONY: evidence check test
evidence:
	$(PYTHON) -B "$(ROOT)/scripts/maintenance/materialize_evidence.py"
check: evidence
	$(PYTHON) -B "$(ROOT)/scripts/docs/check_structure.py"
test:
	$(PYTHON) -B -m unittest discover -s "$(ROOT)/scripts/maintenance" -p 'test_*.py' -q
	$(PYTHON) -B -m unittest discover -s "$(ROOT)/scripts/docs" -p 'test_*.py' -q
	$(PYTHON) -B -m unittest discover -s "$(ROOT)/scripts/loop" -p 'test_*.py' -q
