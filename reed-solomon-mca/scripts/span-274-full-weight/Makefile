.PHONY: help check
help:
	@echo 'check: certify and independently check the saved-kernel row-0 scalar identities'

# Reuses saved completeness; no rank test, search, or cover mutation.
check:
	python3 calculate.py
	python3 verify.py
