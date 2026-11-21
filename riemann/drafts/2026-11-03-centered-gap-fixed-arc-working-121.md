# Fixed angular arc attempt — step 121, 3 November 2026

Invocation-start EXPLORE assessment:
`literature/2026-11-03-centered-gap-fixed-angular-arc.md`.
The target is unchanged. Essential inputs are L666 and the audited L696;
L694/L693 enter through L696's existing centered-profile construction.
All pre-existing changes are preserved. No external retrieval is needed.

Main gap: actual-Xi mixed positivity. Intermediate test: fixed positive
delta,c and finite C,N for the unfiltered finite scalar on |theta|<=delta,
with the fixed real l1 profile, cap 1/8, anchor, unit masses, j=0 and
both endpoints unchanged. This could support later logarithmic tests;
moments, the rest of the circle, complete logarithms, H/support and Xi
realization remain independent. A shrinking arc fails the test.

Partial derivation, not yet a completed result:
For u=exp(i theta), t in [0,1], put lambda=d+t*u,
alpha=t/(U*u+d*t), r=alpha*lambda and a=Re(lambda).
The exact factor is Q(y)=r+(1-r)*lambda/(lambda-i*y).
Its complex measure is r*delta_0+(1-r)*lambda*exp(-lambda*v)dv
on v>=0. For cos(theta)>=0, a>=d; its positive variation majorant
has mass z=|r|+|1-r|*|lambda|/a. The normalized majorant is a
zero/exponential mixture of rate a, mean |1-r|*|lambda|/(a^2*z).
At theta=0, z=1 and this mean is L696's f(t). Compact continuity
should allow log z<=epsilon and mean drift<=g/(4*A) on a fixed arc.
Its centered psi1 norm is <=4, so the scalar Bernstein rate b survives
while the variation cost exp(epsilon*n) must be paid explicitly.

The j=0 factor remains the real exponential of rate d. It should give
the same positive-comb density bound after the exp(epsilon*n) cost;
the zero one-sided density is (d/h)*product_(j>=1)r_j and must remain.
Use L696's real signed-interval primitive and reflected H, with Fubini
against product variation. No reality of the complex kernel is assumed.

Endpoint plan: uniform contraction |Q_t(y,u)|<=kappa_1<1 on
|y|>=2/5 follows by continuity from L696 on the compactified real line.
Pair W(y,u)+W(-y,u) directly. The leading term is product r_j times
Q_0(y)+Q_0(-y)=2*d^2/(d^2+y^2); all telescoping remainders are
O(n*kappa_1^(n-2)/y^2). This replaces scalar conjugacy. Derivatives
and l1 segment lengths should pay both displaced tails with an
exponential rate. All uniformity, comb limits and constants still need
checking in the canonical proof before an ADVANCE is recorded.

Comparisons reused from the ready assessment: C672a has auxiliary
multipliers; L688 has an n-dependent Taylor filter near -1; L695's
absolute angular/spatial stop is not a signed fixed-arc obstruction.
The parked step-105 screen is not repeated. No general convolution,
Bernstein or Poisson theorem is to be reproved.

Completion: the full derivation is now canonical in
`lemmas/L697-centered-fourier-gap-fixed-angular-arc.md` (from the notebook
root). Its (24) retains all five costs, with positive rates after
epsilon=min(b/4,1/40) and fixed kappa_1<1. Both finite endpoints and
the zero half-density are paid. This working note is preserved as the
pre-completion checkpoint, not a second canonical proof. L697 remains
unaudited; its next conceptual audit can reuse the unchanged fixed-arc
assessment because the target and hypotheses have not changed.
