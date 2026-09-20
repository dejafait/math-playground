# Archived formalization handoff

Formalization is paused by user instruction. Do not run Lake, repair proofs, or process this handoff unless the user explicitly resumes that phase.

This file is an archived handoff, not a second live status or next-action record. Use root PROGRESS.md for the current checkpoint, GOAL.md and PROMPT.md for the active workflow, and each lemma Markdown file for validation evidence.

Before the workflow change, full local proofs were added for L031 and L034, and a conditional quadratic-root proof was added for L028. L028 still requires formalized moment inputs. Subsequent interrupted work created Rh/L012.lean; its full statement has not passed validation. No claim in this handoff clears the current backlog.

The formatting helper `python3 scripts/lean/sync_lemma_docs.py` checks section order and synchronizes embedded source. It cannot establish proof validity or promote an unfinished entry to validated. Only embed source as validated after checking the intended full statement and obtaining a successful local Lake build and axiom audit.
