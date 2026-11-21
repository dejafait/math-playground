# Signed rank-two calculation — step435

The pre-existing SPECIALIZE assessment is
`literature/2026-11-04-signed-rank-two-fredholm-diagnostic.md`.
Its exact target is the saved Next action at (r,R)=(3,2048).
Main gap: actual-Xi all-degree mixed positivity. This one-pair test asks
whether a positive signed determinant survives original norm >=1;
that separation could motivate growing-order signed interaction bounds.
Stop this pair if a required contour count differs from 2; stop finite-pair
escalation if the norm upper endpoint is <1. Crossing intervals are
inconclusive. No radius/precision sweep or assumed zero list.

Startup supplied in full; existing notebook changes preserved. Read
L017/L018/L021/L776/L777/L778 and the old interval implementation,
the step433 audit working note, and the named shifted-boundary/q-Pascal
failure records. Reuse ready primary-source and Decimal assessments;
no source query or cross-notebook input. The existing certificate is
only at (2,1024), not this pair. No novelty claim or RH candidate.

Checkpoint before implementation: build a separate evaluator on
|w|<=4096 with 128 moments (rather than reusing radius1600's tail),
128 integration cells/order24, theta indices 1..8 and u<=2. The omitted
theta bound uses exp64; the u-tail is 2 exp(-97)/291.5; the cosh tail
starts at degree256. Fixed contour mesh256/quarter and Taylor degree16,
Cauchy radius1024; no automatic subdivision. Only after both counts=2
certify grouping/root/residue data. Fixed DFT L=2048, N=512 is planned.
All uncompleted reasoning remains provisional until canonical proof and
complete evidence are saved. Full Mathlib matching remains unchecked.

Both fixed contours completed with count=2 and strictly positive boundary
lower bounds (inner >8.419e-7, outer >2.090e-7). The first root pass hit
an unnecessary width assertion: the second strict bracket has width
2.776e-17, above the implementation's 1e-17 goal. No mathematical grouping
failure follows: two disjoint strict real brackets plus total count2 prove
both roots simple. Retained the failure record and repeated only the same
unchanged bisection/evaluator with that assertion removed, accepting the
wider enclosure. No precision, mesh, radius or iteration cap increased.
All trials and complete root/residue uncertainty are saved in the final
certificate. The signed/finite norm phase is now running at the fixed
L=2048,N=512; no result is yet accepted.

Completed: full saved-data checks passed. Canonical reasoning and precise
qualifications are now in L779; error evidence is in the three step435
JSON artifacts under scripts/actual-fredholm. The requested comparison
is inconclusive because high-mode recursive rectangular Fourier powers
dominate the trace error (E>35377031), while the infinite tail HS bound
is <1.722e-17. Stop this implementation without automatic refinement.
The independent-phase change is only nominated, REVIEW_REQUIRED; it was
neither assessed nor executed. Finite hats are not actual sign/norm claims.
