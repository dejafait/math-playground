# Repeated-pole rational action — bounded attempt, step 56

Invocation-start gate: EXPLORE in
`drafts/literature/2026-11-02-repeated-exterior-pole-rational-separator.md`.
This is one attempt at its exact saved target, not a fresh approval.

Main gap: actual-Xi mixed positivity; the immediate missing input is a
segment-positive angular separator with inverse cost at most
exp(n/100) times one fixed power of n. H/support/Xi realization remain
independent. Retain L666's full product, the audited factorization and
arbitrary-preimage moments of L675 Sections 2--3, and L677's polynomial
stop as a comparison. No nonzero-beta assumption or restricted inverse
is used.

The allowed actions are P(w)=N(w)/(1-r*w)^n, deg N<=n,
0<r<4*(n-1)/(5*n), with P(0)=0, P(1)=1, P(10/11)=0,
Re P(x/(x+i*y))>=0 for all |y|<=9/20, and the full exact action on
|a|>(n-1)/n. Continue if one uniform full inverse meets the budget;
park this ansatz if every eligible pair exceeds it for every fixed
polynomial factor. An incomplete estimate does not decide this test.

## Reasoning saved before the analytic attempt

Possible mechanism: the change z=(1-r)*w/(1-r*w) removes the sole
repeated pole. With inverse w=z/(1-r+r*z), the rational action becomes
a polynomial of degree at most n. The prescribed point and positive
arc move with r. Need derive the transformed constraints and, crucially,
an arbitrary-preimage norm estimate that retains the infinite Taylor
tail. L677's coefficient cutoff cannot simply be transferred.

An alternative necessary bound is the full-action norm on circles in
w: the L675 moment expansion is analytic on |w|<|x|/tau. Parseval may
control every mode there, but no useful exponent has yet been shown.
Cancellation at the apparent repeated pole, zero beta coefficients,
and the uniform r,n quantifiers must remain explicit.

No result, inverse, class obstruction or numerical certificate is
claimed in this checkpoint. No new external theorem has been used.

## Candidate route saved before checking constants

For z=(1-r)*w/(1-r*w), T(z)=P(z/(1-r+r*z)) is a real
polynomial of degree at most n. Its segment parameter is
z=1/(1-i*t/(1-r)), |t|<=9/25. Its zero occurs at
z0=10*(1-r)/(11-10*r); the corresponding Poisson point is
alpha=2*z0-1=(9-10*r)/(11-10*r), between 1/3 and 9/11.
This suggests a uniform positive-arc mass of order 1/n, using the
finite-polynomial argument in L677 with the changed arc endpoint.

The proposed full-tail estimate uses the original product directly.
For a=-d+i*y, d=5/4, y0=9/20, U=121/64, Delta=U-d^2=21/64,
write u=c+i*s and t=t_j. The squared modulus of each nonzero-grid
ratio is

    A*(B+t^2*y^2-2*U*t*y*s)/(B*(A+y^2-2*t*y*s)),
    A=d^2+t^2+2*d*t*c, B=U^2+d^2*t^2+2*U*d*t*c.

Its numerator minus denominator is

    -(U-t^2)*[y^2*(U+t^2+2*d*t*c)-2*t*y*s*Delta].

Cauchy--Schwarz bounds the bracket below by
y^2*(U+t^2-2*t*K), where
K=sqrt(d^2+Delta^2/y0^2)<29/20 for |y|>=y0.
For g(t)=U+t^2-(29/10)*t>=0, a proposed uniform contraction is

    delta(t)=y0^2*(U-t^2)*g(t)/((U+d*t)^2*(133/100+t)^2),

using sqrt(d^2+y0^2)<133/100 and monotonicity of
|y|/(sqrt(d^2+y^2)+t). For g<0, a separate small excess bound
is needed. Negative excess can occur only for |a|<R; hence y^2<Delta.
The denominator is bounded below by
(U-d*t)^2*(53/40-t)^2, since sqrt(d^2+y0^2)>53/40.

An exact rational partition of t in [0,1] will test whether the sum
of these contraction and excess bounds gives gamma>1/100 in
|W_a(u)|<=C0*exp(-gamma*n), uniformly in the full complementary
rays |y|>=9/20. If it does not, the present coarse bound is
inconclusive, not an obstruction. Every partition and rounding error
must be charged uniformly in n. No constants are yet certified.

## Completed attempt

The candidate mechanism succeeds as a proposed class obstruction.
The full proof, qualifications and source citation are canonical in
[L678](../lemmas/L678-repeated-exterior-pole-rational-cost-obstruction.md).
The exact 200-interval certificate gives
gamma=94502611/8000000000>1/100 and B=19680067/8000000 in the
uniform complementary-ray bound. The pole-removing map and positive
mass then give ||psi||_2>=exp(gamma*n-B)/(300*(2*n+3)).

All eight arithmetic checks pass; all interval data and the full
aggregate are in
`scripts/one-sided-hankel/repeated-pole-rational-cost-check.json`.
The script checks exact constants, not the analytic proof. A separate
conceptual audit remains necessary before treating the rational stop
as verified. The unchanged invocation-start assessment covers the same
target and hypotheses; no new source gate was written or approved.
The pre-calculation reasoning above is retained as a working record,
not an additional canonical proof. General cone/H/support/Xi gaps
remain open.
