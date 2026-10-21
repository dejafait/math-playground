# Step 308 — exact zero-plane sign/equality Phase I

IN_PROGRESS checkpoint before calculation. The pre-invocation SPECIALIZE
assessment is `literature/2026-10-18-zero-plane-affine-sign-feasibility.md`.
The sole target is its exact TARGET: selected L084 equalities, all 85
original plane-domain rows, and all 45 nonnegative moments. Main gap:
arbitrary-center safety at 67/68 agreements; bracket 955–957 unchanged.

Use L076,L078,L082,L083 and reviewed L084/L085, retaining original
rho,p8,pairs, seven-column dictionary/RREF/completion, whole-kernel and
source-normalization qualifications. Step 306 supplies the complete
affine lift and reverse, which must be checked before any pivots.
ATTEMPTS/052–053,060–068 preserve different fixed-point, equality-only
and conic failures; none decides this subsystem.

Reconstruct all original selected coefficients and absent quadratic
terms. Check both lift directions, original/raw scaling and every
domain row before converting the 130 pulled-back inequalities to
standard form. The 21 coordinates remain free and are split into
positive/negative parts. Retain every row, including duplicates/zeros.
Orient each equality to nonnegative right side and initialize one
artificial variable per row. Minimize the artificial sum with least-index
negative reduced cost, exact ratio test and least-index basic-variable
tie breaking. Fixed column order: positive coordinates, negative
coordinates, slacks, artificials. One run only, at most 10000 pivots
or 300 seconds. Save original rows, conversions, tableau, basis and
row transformation before iteration and at termination/interruption.

Acceptance requires exact original/raw substitution for a witness, or
a strict original-coordinate Farkas certificate with nonnegative
inequality weights and free equality multipliers cancelling all 48
coefficients. A limit/failure is inconclusive. Downstream: a witness
parks signs alone; a separator rejects this fixed family. The other
53 modes, scalar upper rows, other anchors, global moments and RS
realization remain open. Reuse the precise LP/Farkas/Phase I sources
in the approved assessment; no new external research or general
theorem reproof. Mathlib full matching coverage remains not checked.

## Completed calculation

[L086](../lemmas/L086-zero-plane-sign-equality-subsystem-is-feasible.md)
is the canonical result, proof and precise method-citation record. The
original affine model, all six vanishing quadratic terms in each selected
row and both equality-lift directions passed before iteration. All 130
rows were retained. One exact Phase I reached zero after 230 pivots,
within its declared limits; no point scan, second run or conic iteration
was used. Full matrices, conversions and rational witness are in
`scripts/finite-support/affine-sign-phase-one-results.json`; complete
initial/final tableaux, bases and row transformations have the corresponding
`affine-sign-phase-one-initial-state.json` and `affine-sign-phase-one-state.json`
names in that directory. The constructor passes 776 exact checks.

Independent original/raw reconstruction passes 139 checks with no
failures, saved in `scripts/finite-support/affine-sign-phase-one-verification.json`.
All 85 domain rows and 45 moment signs pass: 82 and 27 respectively are
positive. The minima are exactly zero against required zero. Every one
of the 28 selected original and 28 raw equality residuals is exactly
zero. The verifier was run again only to add zero-index lists to its
report, without another LP. The exact witness is retained without
rounding. Full proof and limitations are canonical in L086.

Outcome NEGATIVE / RESEARCH / REPRODUCTION / calculation. Sign-only
exclusion is parked; this useful finite result does not resolve the
other 53 modes or independent global/RS gaps. A separate critical audit
is proposed under a new REVIEW_REQUIRED assessment, with no approval
or new mathematical attempt on that continuation this turn. The
955–957 boundary is unchanged and STATUS remains IN_PROGRESS.
