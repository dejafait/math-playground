# Fourth-order comparison conceptual audit — step401

Approved target: Test the r=4 full-B cumulant comparison uniformly for all integers m>=M4 and u>=0, seeking explicit M4>=7, a positive signed base and relative complete-theta error below 1/2.

Reuse the unchanged step398 EXPLORE assessment. This invocation audits
L769/L770, not a different parameter range or an all-order extension.
Main gap: actual-Xi all-degree positivity. Downstream use: a verified
fixed-order smoothing input; general-order cost and exceptional-index
transfer remain independent. Accept only if the signed integral,
complete theta C^3 bound, conditional localization and all-m onset
survive; isolate any failure without discarding the valid base.

Initial independent checks, saved before replay: L019 gives exactly
B=H(x-3/2). Integration by parts in L769 has no endpoint term for
m>=7, and both four-row reversals have sign +1. The q_j recurrence,
Vandermonde minors and shifted positive polynomial are consistent.
In L770 the reciprocal scaling has six sign changes, hence positive
sign. Newton divided differences require only the stated C^3 norms;
no separation hypothesis is hidden. The theta majorant controls all
n, including derivative convergence at y=0. The transformed measure
has x^(5/4), not x^(9/4), because dt=dx/(2x).

The conditional comparison is plausible for all fixed other coordinates:
four disjoint expanded intervals and three coordinates leave a free
interval, even if the coordinates are very large or coincide. Pairwise
distance and logarithmic ratios, small-x0 and endpoint cases, and the
exact finite constants still need final verification. No audit verdict
is asserted in this checkpoint. Existing scripts will be replayed,
with their historical unresolved-scope labels preserved.

Source/duplicate limits reused: step398 supplies exact-scope coverage;
the recorded Conrey–Ghosh direct-transfer stop remains a different-kernel
obstruction. No external theorem is newly imported and no originality
claim is made. No cross-notebook input, source refresh or delegation.

Completed audit: accepted L769/L770 at their stated scopes; detailed
analytic checks are in the canonical critical-review sections. No
mathematical error or weakening was needed. The complete C^3 series,
reciprocal scaling, conditional integral inequality and all-m strictness
were checked. Both scripts replayed: the polynomial factor reproduced
and 112 finite constants passed. Actual bound: 2^-117; required: 1/2.
The finite checks support, but do not replace, the analytic audit.

The provisional reasoning above is preserved. ADVANCE means acceptance
of an existing local input; REPRODUCTION makes no originality claim.
No new lemma, mathematical script or DAG edge was created. The changed
all-order continuation is only a REVIEW_REQUIRED nomination in
`drafts/literature/2026-11-04-all-order-full-base-localization-review.md`.
No uncovered mathematics or exceptional-index transfer was attempted.
