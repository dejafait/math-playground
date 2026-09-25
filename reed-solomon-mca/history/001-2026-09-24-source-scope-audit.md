# 001 — 2026-09-24 — Initial source and scope audit

Read shared GOAL/PROMPT, local GOAL/PROGRESS, the complete PROOF overview, and
the empty DAG. There were no local unfinished changes, lemmas, or previous
failures. Changes in other notebooks were inspected by git status and preserved.

The gap was the unaudited target definition. The intermediate target was a
version-specific scope and error definition, needed before a support-counting
bound could be tested against the actual MCA error and the 2^-128 benchmark.
The discriminating test was to recover the primary quantifiers and compare any
candidate error bound with that benchmark; failure to read them rules out
selecting a route by guessing the error event.

The [source audit](../foundations/01-target-and-source-audit.md) records the
official rates and threshold target, the preliminary status of the page, and
the paper's July 6 revision. The main gap is not reduced mathematically:
smoothness, the full MCA event, quantifier order, endpoint conventions, and
current upper/lower bounds remain unverified. The official PDF was inaccessible;
an April third-party reconstruction is not evidence of the current definition.
[Saved working notes](../drafts/2026-09-24-source-and-scope-audit.md) preserve the
failed retrieval assessment without treating it as a mathematical obstruction.

Outcome: EXPLORATION; one exploration turn used, zero mathematical advances.
The assessment is complete for this turn. The reason for the next direction is
to finish primary-source verification through a readable copy before testing a
mathematical mechanism. Repeating failed URL variants is not a useful route.
No new lemma, candidate resolution, or DAG change is warranted. No bound was
achieved, and none is represented as meeting the required error.

Validation: `python3 ../scripts/docs/check_structure.py --problem reed-solomon-mca`
is the sole required check for this documentation-only step; no numerical or
theorem-proving test can validate definitions that have not been read.
