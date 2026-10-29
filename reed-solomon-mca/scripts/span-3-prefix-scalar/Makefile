.PHONY: help check audit
help:
	@echo "check: verify span-3 coefficients and saved input bindings; no ranks or cover mutation"
	@echo "audit: separately audit complete selected provenance and coefficients; reuse saved completeness"
check:
	python3 check.py
audit:
	python3 audit.py
