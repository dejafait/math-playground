# 2026-09-26 — Literature assessment of the paired-state target

Step `collatz-2026-09-26-012-paired-state-literature` completed one
LITERATURE step with outcome EXPLORATION and classification
NOVELTY_UNCHECKED. The exact saved target was preserved in the
[assessment](../drafts/literature/2026-09-26-current-target.md), whose
decision is now SPECIALIZE. This replaces the incomplete migration
screen with theorem-level comparisons and a bounded continuation test.

The sources inspected cover the inverse-word machinery and the familiar
coalescence mechanism. Their hypotheses and time conventions do not
supply the simultaneous original-start inequalities sought here. Known
parts are recorded by precise citations; no new mathematical result or
claim beyond the checked literature is made. The assessment records
which sources were actually read and which remain unread leads.

The main gap is unchanged: the forced contractions in L011 might be
compensated by earlier growth. Restricted rigidity at every depth, a
fixed-start depth estimate, and treatment of other blocks remain missing.
The reason to retain the direction is the specific coupling of the two
thresholds with the offset, which is absent from the inspected results.
Reproducing a coalescence identity alone would not justify continuing.
The continuation/abandonment test is recorded in the assessment; the
single current Next action remains in PROGRESS.md.

One consecutive exploration turn has been used. No candidate proof or
disproof appeared. The active notebook had no pre-existing changes at
turn start; changes in other notebooks were left intact. This turn
changes only the assessment, checkpoint, and this history entry.
PROOF.md, DAG.md, lemmas/, and scripts/ remain unchanged because the
mathematical argument and its inputs have not changed. Mathlib coverage
is not checked. No mathematical computation was run.

Validation: `python3 ../scripts/docs/check_structure.py --problem collatz`
passed with 11 nodes, 10 unique edges, complete coverage, valid links,
and compact overviews. The assessment's required single-line fields,
review paths, and exact target match passed a separate read-only check.
`git diff --check -- .` passed, and the protected mathematical files
have no changes. These checks validate documentation, not mathematics.
