# Periodic full-jet truncation: bounded attempt

Approved target: Test a periodic k=2 Whitney truncation of L582 under explicit paired bad-set energy budgets O(1) and O(ell^3), including C2 smoothing and six-jet support at most ell^2.

Prior gate: `literature/2026-10-31-periodic-whitney-weighted-reduction.md`
(EXPLORE), reused unchanged, with its parent source comparison. Read
L582's full proof/audit, L473 (1)--(2),(6),(9)--(10), and the relevant
C582a hypotheses and recorded scalar stop. No new source review or
cross-notebook input. Preserve all existing unfinished work.

Main gap: actual-Xi all-degree positivity. Intermediate target: a
period-independent full-jet extension followed by finite-p smoothing
and a complete paired-moment comparison. Downstream use: isolate
sufficient actual-Hardy exceptional-energy estimates for hard support;
these estimates, positive clipping and Xi transfer remain unproved.
Continue if all derivatives through two, the assessed bad set, all 147
tolerances and exact odd cancellations are controlled; stop on a
specific compatibility or uniform-bound failure.

Checkpoint before proof completion: let K={M_P a<=lambda}. At each
good endpoint, |g|,|g'|,|g''|<=lambda. On a complementary gap of length
d<=1, the endpoint-centered maximal bound gives integral |g''|<=2d lambda.
Cubic Hermite interpolation then has every derivative through two
bounded by 52 lambda. For a gap d>1, multiply each endpoint affine
jet by a fixed C1 cutoff of width 1/2 and set the middle to zero;
the candidate full-jet bound there is 42 lambda. This avoids a factor
of P in the function or first derivative. These are pending proof
details, not yet a completed result.

Still to verify: stitching at accumulation points; weak second-jet
agreement on K; normalized finite-L4 periodic smoothing and lagged
polynomial losses; support margin and one common eventual ray.
No unconditional bad-set estimate is being derived or assumed known.

Completion: those pending details are now proved in the canonical
`../lemmas/L583-periodic-whitney-weighted-moment-reduction.md`.
The proof supplies all three weak bounds <=52 lambda, a smooth
paired bound <128 lambda=ell^2/2 at A=256, and every L473 tolerance
under the two assumed budgets. Smoothing adds at most one to each
quadratic/quartic moment error; the odd entries vanish by periodicity.
The initial scratch reasoning above is preserved. No mathematical
script was used. The proof is a local conditional specialization and
awaits a separate conceptual audit; the actual-g budgets, clipping
and Xi-sign questions are untouched.
