# Step472 — approved all-degree Taylor audit, working record

The supplied SPECIALIZE assessment for Proposition3.7 is unchanged and
was read before work. Target: its exact all-degree bound for integer
k>=10^9 and d>=3, including the L787/L788/L789 assembly. Main gap is
actual-Xi all-degree mixed positivity; possible use is far-tail coefficient
comparison, with central signs and other wedge gates independent.
Continue only if complete branches, circles and all-degree constants
give normalized total<=3; stop propagation at an unpaid premise.

Read all three canonical proofs and L786's normalization; reused the
prior duplicate/failure comparison and step470/471 records. Existing
unfinished notebook changes are preserved. Primary v1 Section3's full
saddle-action case and Proposition3.7 proof/Remark3.8 retrieved; no
ancillary enclosure is an input.

Working argument (not yet a completed certificate): L789 supplies the
restricted tubes, real initialization and analytic full saddle; these
match L788's antecedents, whose bounds in turn match L787. Use the full
phase with the real-normalized logarithm, including its log(pi) constant.
Stationarity yields S'=2 Log(u_s), S''=-4/(u_s^2 Psi_uu); the drift and
Re(A)>=6 suffice for |S''|<5/k, without sharper source decimals.
Construct the curvature principal log on Re(C)>0, the power-series
log(1+epsilon), and real-normalized log Gamma. Their sum defines f
and equals the real logarithm at k. All radius k/40 circles are strictly
inside the radius k/20 analytic disk; sigma and k stay fixed.

For d>=3, divide by 40^d*k^(1-d). Candidate component budgets are
5/[1600*d*(d-1)], 1/2, (19/1000)/k, and
40^(-d)*(1/(d*k)+2/[d*(d-1)]). The Gamma expression follows from
DLMF25.11.12/25.11.1 and the positive decreasing series/integral bound
at x=2k+1. Prove monotonicity in d and k; do not replace the universal
claim by a finite scan. Remaining work: write the complete branch and
factorial argument, verify its rational sum, then record honest scope.

Completed: the full proof and scope are canonical in
`lemmas/L790-uniform-all-degree-moment-taylor-audit.md`. All 11 exact
scalar checks pass in `scripts/complex-moment-audit/taylor-472.json`;
the normalized upper bound is 32033666667883/64000000000000<0.5006<3.
No source intermediate estimate needed repair within the approved
scope; sharper ancillary constants remain unused. The result is a
REPRODUCTION, not mathematics beyond the inspected source.

For the continuation, step465 explicitly flags an unread polynomial
Jensen-wedge lead. Its exact source identity, theorem range and possible
central signed input remain uncovered. Selected step385 and the
prescribed-primitive stop were consulted only to nominate a separate
source review, not to reopen or calculate that route in this turn.
