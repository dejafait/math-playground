# Resolvent-ratio attempt — step 181

The invocation-start EXPLORE assessment is
`literature/2026-11-03-resolvent-polynomial-ratio.md`; the supervisor
explicitly approves a mathematical attempt on its unchanged TARGET.
Existing work is preserved. Main gap: actual-Xi all-degree positivity
and the unpaid complementary spatial Jensen defect. This finite ratio
could isolate the resolvent's effect before the fixed signed bump
integral; L714's inverse-density application still needs its own audit.

Inputs read: L714's exact coefficients and audited root factorization;
L715's audited normalized logarithm, including its reciprocal-root
measure; L703/L713's original interval definitions. Reused the exact
source assessment and checked the three recorded signed-bump,
absolute-contour and positive-blend failures. None settles this ratio.
No boundary law, bump analyticity or signed lower bound is presumed.

Bounded test: prove a continuous nonzero uniform limit on the entire
closed interval, including its endpoints, or exhibit an actual zero,
nonconvergent subsequence or competing tail. A failed majorant is only
an inconclusive certificate. Retain every original finite-family
parameter, both endpoints and all moments.

Working direction: express the coefficient resolvent by an exact
Laplace integral and use L715 for the local relative polynomial ratio.
The essential unpaid step is a uniform integrable bound on the whole
tail, not a formal local expansion. A radial integration parameter
is also available because Re((d+c_0)/u)>0; its possible root-product
bound will be tested before any general saddle argument is attempted.

Pending: choose and justify the exact integral, control its entire
tail uniformly in n and v, identify the limit and bound its modulus
away from zero. No conclusion is asserted at this checkpoint.

Refinement: the finite numerical diagnostic (not a proof) shows why
the radial path is unsuitable for a simple absolute majorant: its
sampled normalized phase initially increases. This does not obstruct
the ratio. The original real Laplace parameter instead follows
z(x)=exp(-u*x), x=v/A+t/n. Test a strict upper bound below alpha=11/8
for G(x)=-Re[u*z(x)*F'(z(x))], uniformly for x>=2/5. Such a bound,
with L715's derivative convergence on a compact subdisk and the
root-product bound for large x, would give full-tail domination.
The exact moment coefficients of L715's reciprocal-root measure can
be obtained by the local inverse relation; use finite power series
with a rigorous remainder and rational interval arithmetic if needed.
This remains the same approved quotient target, not a new route.

The initial diagnostic invocation lacked mpmath. It was replaced by
a self-contained Decimal calculation; its output remains explicitly
nonrigorous. No finite ratios are used as evidence for convergence.

Completed: L716 contains the full proof of the uniform nonzero ratio
limit. The exact rational/interval certificate passes all nine checks;
its complete checks, analytic error bounds and worst cell were inspected
with the bounded JSON inspector, using full selected values. The proof
and code account for every moment and grid row, the unbounded tail,
and one uniform existential finite-n onset. The diagnostic is unused.
The bound 4/3 is strictly below the required damping 11/8, leaving
the eventual integrable majorant exp(-t/48). No effective onset is
claimed. Canonical proof, not this working record, holds all details.

Outcome: ADVANCE / POTENTIALLY_NEW, with originality unverified and
the result awaiting a separate conceptual audit. The only continuation
is that audit, with REVIEW_REQUIRED coverage in
literature/2026-11-03-resolvent-ratio-conceptual-audit.md. Outer signed
bump cancellation and L714's inversion audit remain independent.
