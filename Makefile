# Reusable maintenance commands; research is started separately with loop-codex.sh.
.DEFAULT_GOAL := help
ROOT := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
PYTHON ?= python3
include mk/help.mk
include mk/diagnostics.mk
include mk/verification.mk
include mk/archive.mk
