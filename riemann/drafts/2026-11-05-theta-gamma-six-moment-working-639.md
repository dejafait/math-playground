# Step639 — approved six-moment calculation, working record

The approved target is exactly the TARGET in
`drafts/literature/2026-11-05-theta-gamma-six-moment-test.md` (SPECIALIZE,
saved and separately approved before invocation). Main gap: actual-Xi
all-degree mixed positivity. Intermediate target: finite positive
[0,infinity)-representability for the six compensated reciprocal moments.
Downstream use: a necessary consistency premise of the conditional
actual Mellin/Bernstein construction, not a sufficient sign transfer.

Read L778's complete evaluator/error argument and contracts, L791's
normalization and audit, L795's moment definition, L019/L021, and the
completed step637 source/duplicate/failure comparison. No new source
coverage or enlarged mathematical target is needed. Existing notebook
changes are preserved. No cross-notebook mathematical input is used.

For j<=5, m_j=8*4^j*(2j)!*a_j and
gamma(j)=8*4^j*j!*a_j, so s_j=gamma(0)/gamma(j), with s_0=1 exactly.
Extract P_0 coefficients 0..5, add the full complex Cauchy coefficient
error E_G/1600^j, then use exact rational interval arithmetic. Check
provenance against L791 and L778's audit before trusting the data.
Test both 3-by-3 real Hankel matrices. Strictly positive leading minors
give positive definiteness by Sylvester and automatic range compatibility
for H_0. A negative principal minor/direction ends the premise; a zero
interval is inconclusive. A singular exact case requires the complete
Curto–Fialkow Theorem5.1 range condition. No higher-degree test is planned.

Continuation inputs: L018/L019/L021/L795, finite evaluator L778 and
normalization L791. Inherited analytic/Decimal/provenance contracts remain
explicit assumptions. Infinite representation, actual Bernstein membership,
lower oscillation, uniform degree control and mixed/shifted transfer are
unresolved. Save full program/evidence in `scripts/theta-gamma-moments/`.

Initial save: no matrix test had yet been run.

Completed calculation: both Hankel matrices are positive definite, with
all three leading minors strictly positive for each. The range condition
is automatic. The known criterion gives a positive probability measure
matching indices0..5 only. Full proof, bounds and qualifications are in
L827; evidence is `scripts/theta-gamma-moments/six-moment-certificate-639.json`,
FINITE_STIELTJES_FEASIBLE, no failures. Full selected coefficient, error,
moment, minor and provenance values were inspected. No infinite law,
new RH sign mechanism or candidate is claimed. The new audit continuation
is separately nominated with REVIEW_REQUIRED; it is not self-approved.
