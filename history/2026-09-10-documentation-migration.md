# Documentation migration — 2026-09-10

Split 57 lemmas and Corollary 32a out of PROOF.md, preserving their mathematical text and numbering. Moved shared starting inputs and the existing formalization inventory to foundations/. Reconstructed direct dependencies in root DAG.md, the sole graph source, including the later results missing from the former overview.

Condensed dated research entries into six history files, retaining outcomes, failures, and historical direction changes. Removed repeated proof and validation summaries; the canonical proofs retain those details. Attempt files retain their dated outcome and WHY IT FAILS paragraphs, with links replacing repeated derivations. The original versions remain available in Git history.

Removed the stale determinant-expansion next step from PROOF.md. PROGRESS.md retains the previously active heat-deformation task. No new mathematical result or verification is claimed by this migration.

The initial run was recorded as taking about two minutes; the recurrent run ran about fifty minutes before reaching a five-hour limit. The old prompt text was replaced by the current workflow in README.md and GOAL.md.
