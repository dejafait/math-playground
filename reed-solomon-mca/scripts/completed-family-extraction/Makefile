.PHONY: help construct verify check audit

help:
	@echo "construct  Generate the explicit sixteen-row witness and full certificate"
	@echo "verify     Independently replay an existing certificate from the proof table"
	@echo "check      Construct, then independently verify the entire witness"
	@echo "audit      Critically audit canonical tables and existing certificates without regenerating them"

construct:
	python3 construct.py

verify:
	python3 verify.py

check: construct
	python3 verify.py

audit:
	python3 audit_l167.py
