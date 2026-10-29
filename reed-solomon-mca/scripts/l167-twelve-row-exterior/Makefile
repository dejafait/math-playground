.PHONY: help produce verify check audit

help:
	@echo "produce  Save the complete fixed twelve-row exterior rank/kernel certificate"
	@echo "verify   Reconstruct every block independently and certify the saved rank"
	@echo "check    Produce, then independently verify the fixed stack"
	@echo "audit    Audit both saved certificates without regenerating them"

produce:
	python3 produce.py

verify:
	python3 verify.py

check: produce
	python3 verify.py

audit:
	python3 audit_l168.py
