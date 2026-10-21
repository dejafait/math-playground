# 2026-10-08 — Anchored neighborhood graph is sharp

STEP_ID: rsld-2026-10-08-084-affine-neighborhood-sharpness

Completed the preapproved 56-slope mathematical test in
[L035](../lemmas/L035-affine-fixed-block-neighborhood-sharpness.md).
The exact ordinary bound and the construction both equal 10696, for
every actual core, distinguished block and outside bijection. All
anchored forbidden incidences are avoided before any label-rank test.
The complete certificate at `scripts/finite-support/affine-neighborhood-results.json`
covers 57196860 unordered pairs by full same-slope enumeration and
294140 translation-reduced distinct-slope offset cases; all 15 checks pass.
Full benchmark, aggregate histogram, checks and failures were inspected.

NEGATIVE records new stopping evidence for this graph relaxation,
classified RESEARCH/REPRODUCTION of assessed methods, not progress
beyond the checked literature or an RS boundary improvement. The
canonical failed-route record is
[ATTEMPTS/024](../ATTEMPTS/024-anchored-fixed-block-graph-improvement.md).
The 955–957 bracket and full-neighborhood/family-conversion gaps remain.
Earlier stops and unfinished work are preserved; PROOF.md and DAG.md
now include the new local sharpness input.

The sole continuation is a separate critical audit of L035. Its newly
written [ready coverage](../drafts/literature/2026-10-08-affine-neighborhood-critical-audit.md)
requires separate supervisor approval next turn. This does not reopen
the exhausted cardinality mechanism; any later mathematical route must
add a materially different restriction or test an independent target.
