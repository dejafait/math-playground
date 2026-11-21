.PHONY: quota-history review math-processes inventory math-save-diagnostics math-push
DAYS ?= 14
quota-history:
	$(PYTHON) -B "$(ROOT)/scripts/maintenance/quota_history.py"
review:
	$(PYTHON) -B "$(ROOT)/scripts/maintenance/loop_review.py" --days "$(DAYS)"
math-processes:
	ps -axo pid,ppid,etime,%cpu,command | awk 'NR==1 || /[s]cripts\/loop\/runner[.]py/ || /[c]odex.* exec --sandbox/'
inventory:
	mkdir -p "$(ROOT)/.generated/maintenance"
	git -C "$(ROOT)" ls-files --others --exclude-standard -z > "$(ROOT)/.generated/maintenance/untracked.nul"
	$(PYTHON) -B "$(ROOT)/scripts/maintenance/loop_review.py" --inventory "$(ROOT)/.generated/maintenance/untracked.nul"
math-save-diagnostics:
	git -C "$(ROOT)" diff --cached --quiet
	git -C "$(ROOT)" add -- Makefile mk scripts/maintenance/Makefile scripts/maintenance/archive_project.py scripts/maintenance/test_archive_project.py
	git -C "$(ROOT)" diff --cached --check
	git -C "$(ROOT)" commit -m "Add lossless research retirement archives and reusable maintenance commands"
math-push:
	git -C "$(ROOT)" push origin main
