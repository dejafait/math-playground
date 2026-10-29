.PHONY: help check
help:
	@echo 'check: construct and independently verify one saved-history geometric survivor'

# No stack/extension rank tests, traversal, or saved-cover mutation.
check:
	python3 calculate.py
	python3 verify.py
