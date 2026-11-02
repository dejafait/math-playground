# One-sided Hankel bound — bounded mathematical attempt

Started 2026-11-01 under the unchanged EXPLORE assessment
`drafts/literature/2026-11-01-one-sided-pole-hankel-census.md`, exact
COVERED_TARGET matching the invocation's Next action. This is unfinished
reasoning, not a theorem or an RH candidate.

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
the exact C645g symbol with Re(a)<=x, positive integer residues,
|a|<=R-eta, anchor x, and M<=C*n for arbitrary fixed C. Seek
||H_q||>=c_(delta,eta,C) exp(-delta*n/8), uniformly for large n,
or an admissible fixed-parameter asymptotic counterfamily. C645h gives
the possible boundary-detector use, subject to actual-Xi selection,
census, clearance, realization and an independently smaller upper bound.

Reused literature: one-sided comparison supplied verbatim, and the
saved full-pole operator comparison. Read C645g's exact normalization
and quantitative proof, C645h's full principal-part and norm transfer,
C645d's exact scalar cancellation construction and recorded stop,
C645b's envelope conclusion, and L645's conditional Pick statement.
No additional literature is essential for the approved bounded test.
No cross-notebook input or modification of existing unfinished work.

Mechanism to test: the half-plane to the right of x contains no poles.
Look for an analytic directional multiplier/contour functional that
restores positive original residues while using less than the full
grid exponential. Retain B_n(a), not its modulus, and the factor 1/R.
Compare with a pole family on a circle tangent to the line Re(a)=x
as a possible cancellation model. These are alternatives within the
same approved bound test, not asserted estimates.

Continuation/abandonment threshold: a complete uniform lower bound or
a rigorous asymptotic upper bound violating it decides the target.
Failure of one multiplier, scalar cancellation, a small least singular
value, or a finite numerical sample does not. If incomplete, preserve
the calculations and require a specific refined mechanism before
repeating. No mathematical script has been run at this checkpoint.

## Saved partial mechanism

Candidate counterfamily: delta=2/5, eta=1/100, d=11/10, R=13/10,
x=-11/10. Put u=239/200, c=-u, r=19/200, and m=10*n.
Take a_k=c+r*exp(2*pi*i*k/m), 0<=k<m, each of residue one.
Then a_0=x, Re(a_k)<=x, and |a_k|<=129/100=R-eta.

For boundary z, apply the roots-of-unity average to the holomorphic
function of w, 1/[B_n(c+w)*(z-c-w)], on |w|<=s=1/10.
The constant Taylor coefficient is 1/[B_n(c)*(z-c)]. The other
surviving coefficients have degrees divisible by m. On |w|=s,
|z-c-w|>=1/200 and a factorwise bound should give
|B_n(c)/B_n(c+w)|<=exp(n/5). Since r/s=19/20,
the remaining sum has relative bound
200*exp(n/5)*(19/20)^(10*n)/(1-(19/20)^(10*n)).
This would be exponentially small relative to B_n(x)/B_n(c).

Required product check: for v in [d,u], the derivative of the log
modulus of one factor at -v is
D(v,t)=v/(v*v+t*t)-v*t*t/(R^4+v*v*t*t).
It decreases with v on this range and D(u,t) decreases with t.
Thus the logarithmic product ratio is at least
n*(u-d)*(1/8)*sum_(k=1)^8 D(u,k/8).
The pending exact rational test is whether that last average exceeds
27/50. If so the product gain is at least 513*n/10000, exceeding
the required delta*n/8=n/20 by 13*n/10000. Full analytic and
arithmetic checks remain before any result is stated canonically.

## Completed bounded attempt

The circle mechanism succeeded as a counterfamily. The full canonical
proof and all hypotheses are now in C645i; the partial reasoning above
is retained as the checkpoint. The exact rational check passed all
fourteen conditions and its full table/cross-products were inspected.
The proof uses the residue theorem on an explicit finite quadrature
kernel, rather than an unproved approximation heuristic.

For the fixed parameters above it proves
||H_q||<=||q||_infinity<4100*n*exp(-513*n/10000), so multiplying by
exp(delta*n/8) gives a quantity tending to zero. This is a negative
answer to the arbitrary-fixed-C synthetic claim, subject to the
separate conceptual audit nominated in PROGRESS.md. It is not an
actual-Xi construction or a disproof of RH. No attempt to solve the
independent actual-Xi gaps followed this one bounded test.
