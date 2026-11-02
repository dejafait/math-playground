# Discrete parameter quadrature — bounded attempt, step 66

Invocation-start gate: the supplied unchanged EXPLORE assessment
`drafts/literature/2026-11-02-discrete-parameter-positive-quadrature.md`.
Only its exact full-kernel residual on L673's prescribed nodes is tested.
The main gap is actual-Xi mixed positivity; successful positive quadrature
would be an intermediate cone input, with H/support/realization unresolved.

Read L666 (6), L673's exact nodes, signs and audited rate, L680's audited
parameter-point attenuation, and the local fixed-gauge/continuum/polar
stop records. No new source theorem is needed at this stage. The bounded
new mechanism is a direct Cauchy-residue sampling formula based on the
exact nodal equation, rather than a rerun of the stopped finite-product
gauge contour. Its positivity, anchor, complement and exponential rate
are unproved at this checkpoint. No numerical evidence is a premise.

Put z=a-x, lambda=pi/h, rho=h/10. L673's nonzero nodes are among
the imaginary zeros of D(z)=z*cosh(lambda*z)+rho*sinh(lambda*z).
Investigate a meromorphic sampling kernel with these poles, including
the zero at z=0, whose residues have one sign after phase alignment.
The issue is whether its exact contour identity gives the fixed unit
anchor and the required full continuous L2 remainder at rate >1/100.
Continue only with a quantified identity/bound or informative intermediate
estimate; a finite fit or generic theorem inapplicability is inconclusive.

This file saves unfinished reasoning before the extended calculation.

## Direct sampling-kernel calculation (not yet a rate certificate)

Let C=(1+rho*lambda)/rho and
K(z)=C*(rho-z)*exp(-lambda*z)/D(z).
The residue at zero is one. At each nonzero imaginary root z=i*y,
the nodal equation gives the positive real residue

    b(y)=C*(rho^2+y^2)/(rho+lambda*(rho^2+y^2)).

It is less than C/lambda=1+10/pi; the full lower bound and the
complete contour identity still need checking. The meromorphic kernel
has no nonimaginary poles: the zero equation has incompatible moduli
on either open half-plane. A rectangle with top Y=2*q*h contains
exactly the required finite nodes. The kernel is O(n) on a fixed
left side and is O(n)*exp(-2*lambda*s) on a right side Re z=s>0.
At Y the hyperbolic functions have real phase, allowing a direct
top-edge bound. The continuum right-edge exponent to test is
F(s+i*y,u)-20*pi*s/27, with the complete product F from L673.
The floating design screen is explicitly uncertified and saved at
`scripts/one-sided-hankel/discrete-robin-quadrature-screen.json`.
No prescribed-weight optimality or arbitrary-weight obstruction follows
from failure of this single residue kernel.

The screen's best sampled right-edge exponent is about -0.006234,
short of -0.01. It is not a lower bound or an impossibility result.
The same coherent attempt now certifies the potentially useful partial
rate 3/500 with right side 7/100, left side -1/8, and top Y=2*q*h.
Its exact mesh certificate is running separately. All nonanchor weights
obey 1<b(y)<1+10/pi, since b(y)-1 has numerator y^2 and positive
denominator. On each edge, |K(z)| is bounded by
12*n*exp(-2*lambda*max(Re z,0)).

Left-edge |x+z|>=R gives |W|<=P_n by the exact disk-factor identity.
For the right and top, use the full continuum F and its proved
finite-product error <9 from the same denominator bounds as L672.
At the top, b-Y=27/(20*n) and |F_y|<9; replacing Y by b therefore
adds less than 243/20 to the finite exponent, for total cost <22.
The inherited F second-derivative bounds apply because throughout the
rectangle 29/25<|x+z|<3/2. Right/top continuous coverage and every
rational sample remain to be verified before the partial bound is claimed.

## Completed bounded attempt

The exact run passed all 117462 samples in 262 rows and all auxiliary
checks. Its continuous upper bound is -546306841/90000000000, below
-3/500 by 6306841/90000000000. The finished proof, precise weights,
constants and qualifications are now canonical in L681. Earlier
unfinished statements above are retained as the working history, not
additional hypotheses or a second proof. The resulting bound is
6*exp(22)*n*exp(-3*n/500), weaker than the approved rate >1/100.
No arbitrary-weight obstruction or complete RH candidate was found.
A separate conceptual audit is nominated REVIEW_REQUIRED; no new
continuation mathematics was derived or approved in this turn.
