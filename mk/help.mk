.PHONY: help
help:
	@echo "review DAYS=14 / math-processes / inventory  Read-only loop diagnostics"
	@echo "quota-history  Rebuild historical subscription observations"
	@echo "evidence / check / test  Restore certificates and run offline verification"
	@echo "math-stop  Gracefully stop this repository's loop before a final snapshot"
	@echo "math-plan-progress / math-save-progress  Review and commit mathematical files up to 1 MiB"
	@echo "math-save-diagnostics  Commit reusable maintenance tools separately"
	@echo "math-archive / math-archive-check  Preserve and verify the full research workspace"
	@echo "math-save-archive  Commit the archive inventory and closure documentation"
	@echo "math-push  Push committed main to origin (never stages files)"
	@echo "math-archive-upload / math-archive-remote-check  Publish and verify GitHub release assets"
