# Approved finite tilt test: working record

31 October 2026. Research under the pre-existing SPECIALIZE assessment
`literature/2026-10-31-tilted-strip-polynomial-budget-test.md`.
Only its fixed family and parameter interval are being tested.

Main gap: actual-Xi all-degree positivity and initial signs at unbounded
heights. Intermediate target: optimize the normalized squared circle
norm of exp(lambda*z)*(1+4*z^2)*(1-a*z^2), real lambda, 0<=a<=4,
and compare L571's strict certificate with D_1<0. Downstream use:
determine whether linear tilt alone repairs loss of first-sign information
before seeking any actual-Xi bound. Stop a blanket equivalence if a
negative-sign interval misses the strict budget for every real tilt.

## Saved calculation to finish checking

The even polynomial gives |P(exp(i*(theta+pi)))|^2=|P(exp(i*theta))|^2.
Pairing antipodal boundary points replaces exp(2*lambda*cos(theta)) by
cosh(2*lambda*cos(theta))>=1. Strictness for lambda!=0 should follow
from positivity away from finitely many zeros and cos(theta)=0. Hence
the unique optimum should be lambda=0, with squared norm
1+(4-a)^2+16*a^2=17*a^2-8*a+17.

For L571 at r=1/2,m=1, q=1/4,b=1/4,c=15/4, the strict threshold
should be N_1=120. Its positive parameter root is
alpha=(4+sqrt(1767))/17. D_1=2*a-8 independently of lambda, so the
candidate missed interval is [alpha,4). Check exact zero orders,
strip/product class, all endpoints, and uniqueness before finalizing.
No Xi application or complete candidate follows from this model.

## Completed result

The calculation above is now fully justified, with all parameter and
strict-budget endpoints, in canonical C571a. The norm pairing is exact;
strictness at theta=pi/4 proves uniqueness for every parameter. The
additional roots are real and the designated pair stays simple,
including the degree drop at a=0. No mathematical script was needed.
The exact missed interval supplies an informative NEGATIVE outcome
for the blanket equivalence claim. The sufficient implication in L571
survives. Independent audit is the next bounded action, not another
optimization scan or a purported actual-Xi estimate.
