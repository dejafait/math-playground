# Step 336 — L092 conditional critical audit

The prior SPECIALIZE assessment is
`literature/2026-10-19-zero-block-plus-3-4-witness-critical-audit.md`.
Main gap: arbitrary-center 67/68-agreement safety, bracket 955–957.
Intermediate target: independently reconstruct L092's frozen subsystem,
verify its entire original/raw witness and replay only its saved 277 pivots.
Downstream use: a trustworthy necessary-subsystem pass before a separately
assessed stronger test. Continue on complete agreement; preserve the first
discrepancy and distinguish mathematical correctness from provenance.
Missing evidence is inconclusive, never subsystem infeasibility.

Inputs: L021,L053,L073,L075,L076,L078,L082,L083,L084,L086,L090,L091,L092.
Retain foundations/04,09,10,12's ancestral PSD, uniqueness, whole-kernel
and normalization qualifications. Canonical L092 and its step-334 record
defer this audit; L090's earlier witness and L091's rejection are distinct.
ATTEMPTS/071 and /076 preserve the stopped full solve and single-row
nonexclusion. Reuse the supplied primary-source assessment; no new
literature review or general theorem reproof is needed.

Plan: reuse the inspected independent source reconstruction at the OLD
L086 moments as regression controls, redirecting its output to a fresh
audit artifact. Reconstruct all 81 coefficient rows and membership
decisions, all 43 zero cross vectors, the complete added block and its
range/cost; verify both full equality lifts and every retained witness
row. Replay saved events against independently reconstructed standard
rows, with no constructor, optimizer, retuning or omitted-mode test.
The other 29 complementary modes at L092's witness, scalar upper rows,
other anchors/columns/base/pairs, global moments and RS realization remain
outside scope. Historical elapsed time cannot be independently verified.

Before computation, source scripts and arithmetic helpers were inspected.
An inspector invocation hit Python's integer-string display limit; use
PYTHONINTMAXSTRDIGITS=0 for bounded inspection. No mathematical data or
comparison changed, and no computation was restarted.

## Preserved audit tooling failure

The first audit invocation completed 7993 independent source checks and
421 original/raw witness checks without failures, then raised
`KeyError: 'original_row'` before any saved pivot replay. L091's critical
certificate stores full block/cross/energy/normalization data, not its
original coefficient row in that schema. The first audit script and
exception are preserved under `scripts/finite-support/` as
`critical_audit_zero_block_plus_3_4_initial.py` and
`zero-block-plus-3-4-critical-audit-schema-failure.json`.
The correction compares all four available frozen block fields; every
original coefficient and bound is still independently reconstructed and
compared against the source and original model. No mathematical condition
was dropped. The corrected audit repeats validation, not construction or
optimization, and begins the saved-trace replay for the first time.

## Completed audit

The corrected invocation of

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_zero_block_plus_3_4.py

passes 7993 source, 421 independent original/raw and 2437 additional
checks. It replays exactly 277 saved pivots, compares complete initial/
terminal tableaux, bases and row transformations, and checks every
retained witness residual. All 28 original/raw equalities vanish; all
44 mode rows and 45 signs pass, with 11/33 positive/zero mode slacks
and 35/10 positive/zero moments. Both minima are exactly zero, meeting
the required zero bound. The added remainder is zero; all 15 principal
minors of its complete block and its exact determinant-one Schur
congruence pass. Full proof and artifact paths are canonical in L092.

The original arrays and mathematical comparisons were preserved through
the schema repair. The corrected reconstruction also passes the same
source/verifier checks; no optimizer or constructor was run.
Historical time is recorded provenance only. The other 29 modes at the
new witness remain untested. PROOF.md and DAG.md remain unchanged because
the argument and direct inputs are unchanged. The newly recorded
complementary-mode continuation is REVIEW_REQUIRED, for a separate
source-approval turn; this completed audit does not approve it.
