# Three-factor compatibility attempt — step606

Approved target: the unchanged TARGET of
`literature/2026-11-05-three-factor-unit-gap-feasibility.md` (SPECIALIZE,
saved before invocation). This is one conventional algebraic feasibility
attempt, not a new root theorem or a signed-positivity mechanism.

Main gap: actual-Xi all-degree mixed positivity. Intermediate test:
positive exact solutions with two unit gaps and an unbounded third gap.
A positive unbounded family could evade the audited two-factor degree
caps, leaving normalization, separation, signed payment and mixed
assembly unresolved. An all-tuples bound on the third gap would stop
this precise regime. Finite scans or approximate limiting roots cannot
decide the test.

Read L791 in full, including its step478 audit and inherited
L018/L021/L776/L778 contracts; read L819's setup/elimination and the
step602/604 working notes and regime stop. The supplied step605 source
review covers this target, but supplies no feasibility conclusion.
Existing notebook changes are extensive and will be preserved.

Initial reduction: write x=B1+1>1, y=B2+1>1. Each unit-gap quotient is
u_x(k)=(x+k)^2/((x+k)^2-1). With t=1/(A3+1), the third factor is
[(1+(k-1)t)/(1+kt)]*[(B3+k+1)/(B3+k)]. The possible t=0 boundary
removes A3 and leaves three equations in x,y,B3. A nondegenerate positive
solution there, with a uniform existence certificate for the exact q
box and small t>=0, would produce arbitrarily large third gaps. No
boundary feasibility or continuation is yet claimed; if this limit
fails, escaping unit-factor parameters must still be treated.

## Completed attempt

Nonvalidated boundary diagnostics first tried Newton's method from
(x,y,B3)=(5,10,30),(6,15,20),(4,20,100),(7,9,50),(5,50,20),(10,30,14),
where these initial x,y were B1+1,B2+1. Four line searches stalled near
x=y, with maximum log-residuals respectively .0025521,.0037038,.0026531,
.00094824; two Jacobians became numerically singular while a denominator
escaped (residuals .014084 and .014323). These failures are diagnostic
only, not evidence of infeasibility. A one-dimensional boundary diagnostic
eliminating B3 by q0 and approximately matching q1 at reciprocal x in
{0,.02,.04,.06,.08,.10,.12,.14} found q2 above its target by approximately
.00055651,.00056192,.00055345,.00050956,.00042583,.00031257,.00019473,
.00011481 respectively. These finite checks suggested an obstruction;
they are not premises of the result and do not cover the boundary.

The final argument changed to a uniform compactification, rather than
inferring anything from the failed solver. In canonical L820, x,y now
denote reciprocal unit-gap denominators, b is eliminated exactly and
0<=t<=10^(-6) is covered together with the entire exact q enclosure box.
The exhaustive interval certificate passed with 727 nodes, 364 excluded
leaves and no unresolved rectangle. The full proof, arithmetic contracts,
all escaping cases, and d<=1000000 conclusion are canonical in L820.
The exact rational consistency check read all leaves and the full path
cover; it is not an independent interval replay. Programs and full
certificates are under scripts/central-jacobi/three_factor_606.py and
consistency_606.py with their named JSON outputs. No numerical evaluator
or inherited binary was revalidated. Independent audit is the next gate;
the unbounded-degree regime is provisionally stopped, with no Xi sign
gain. Existing two-factor stops are preserved.
