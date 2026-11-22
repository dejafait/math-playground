ARCHIVE_TAG ?= research-snapshot-2026-11-22
.PHONY: math-stop math-plan-progress math-save-progress math-archive math-archive-check math-save-archive math-archive-upload math-archive-remote-check
.PHONY: math-save-storage-policy
math-save-storage-policy:
	git -C "$(ROOT)" diff --cached --quiet
	git -C "$(ROOT)" add -- .gitignore riemann/scripts/.gitignore README.md scripts/maintenance/research-archive.md mk/archive.mk
	git -C "$(ROOT)" diff --cached --check
	git -C "$(ROOT)" commit -m "Keep bulky generated research results local and cancel GitHub archive publication"
math-stop:
	$(PYTHON) -B "$(ROOT)/scripts/maintenance/archive_project.py" stop
math-plan-progress:
	$(PYTHON) -B "$(ROOT)/scripts/maintenance/archive_project.py" plan
math-save-progress:
	$(PYTHON) -B "$(ROOT)/scripts/maintenance/archive_project.py" validate-staging
	git -C "$(ROOT)" add --pathspec-from-file="$(ROOT)/.generated/maintenance/progress.nul" --pathspec-file-nul
	git -C "$(ROOT)" -c core.whitespace=-blank-at-eof,-blank-at-eol diff --cached --check
	git -C "$(ROOT)" commit -m "Record final Riemann hypothesis research progress through November 22" -m "Preserve notebook checkpoints, source reviews, audits, scripts and compact evidence. Large evidence remains byte-for-byte in the separately inventoried research snapshot release. This records exploratory work, not a proof of RH."
math-archive:
	$(PYTHON) -B "$(ROOT)/scripts/maintenance/archive_project.py" prepare --tag "$(ARCHIVE_TAG)"
math-archive-check:
	$(PYTHON) -B "$(ROOT)/scripts/maintenance/archive_project.py" verify --tag "$(ARCHIVE_TAG)"
math-save-archive:
	git -C "$(ROOT)" diff --cached --quiet
	git -C "$(ROOT)" add -- README.md scripts/maintenance/research-archive.md scripts/maintenance/research-snapshot-manifest.json
	git -C "$(ROOT)" diff --cached --check
	git -C "$(ROOT)" commit -m "Document independently verified RH result and inventory the final research archive"
math-archive-upload:
	$(PYTHON) -B "$(ROOT)/scripts/maintenance/archive_project.py" upload --tag "$(ARCHIVE_TAG)"
math-archive-remote-check:
	$(PYTHON) -B "$(ROOT)/scripts/maintenance/archive_project.py" remote-check --tag "$(ARCHIVE_TAG)"
