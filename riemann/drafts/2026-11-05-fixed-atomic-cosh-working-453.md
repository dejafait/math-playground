# Fixed atomic diagnostic — preserved working reasoning, step453

The approved target is unchanged. The elementary identities in the ready
assessment give G_*(w)=cosh(2y)(cosh(y)+2), y^2=w. The first root family
is w=-pi^2(2n+1)^2/16; the second is w=(+/-log(2+sqrt(3))+(2n+1)i*pi)^2.
The even y identification must remove duplicate roots and retain simplicity.
At R=8 the interior nodes are alpha_1=-t, alpha_2=-9t,
t=pi^2/128. All remaining roots have modulus greater than9 in w,
so sigma=9/8 is available. Full details still to be written canonically.

An exact complete-tail alternative avoids unstable Taylor division past
the first removed root. Write B(z)=P(z)^2/G_*(8z), b=z^-2 B and
T(z)=sum_(m=-2)^3 beta_m z^m. Then h_3(z)=z^-3(b(z)-T(z)).
At each simple removed root b(alpha)=0 and b'(alpha)=1/d.
Consequently the positive-diagonal congruence
M=E^-1(J-Q)E^-1=diag(J_i/E_i^2)+K has entries

    M_ii=3 T(alpha_i)/alpha_i^4-T'(alpha_i)/alpha_i^3,
    M_12=(-T(alpha_1)/alpha_1^3+T(alpha_2)/alpha_2^3)/(alpha_1-alpha_2).

The residue term cancels exactly on the diagonal; it has not been dropped
from K. This is an exact analytic expression for the whole series, not
an inferred zero tail. Analyticity and the Laurent Cauchy theorem must
justify it before using node values and derivative limits. The six
coefficients beta_-2,...,beta_3 need only the first six Taylor coefficients
of 1/G_*(8z) locally at0; no reciprocal expansion outside its original
radius is used. A preliminary noncertifying rational substitution gives
M_11 about5063.009, M_12 about.06251, M_22 about-.45307, det about-2293.90.
This suggests the indices match, not a counterexample. Certify with rational
intervals for pi, complete residue signs/weights and a nonzero determinant;
retain any failed checks. Do not tune the model or claim a generic bound.

Completion: the exact rational-interval calculation passed all22 checks.
The full proof, bounds and qualifications are now canonical in
[L784](../lemmas/L784-fixed-positive-atomic-cosh-residual-inertia.md),
with evidence under `scripts/fixed-atomic-cosh/`. The indices match for
this model only. The diagnostic is closed without tuning. The reasoning
above is preserved as the original working record, not an independent
proof or a still-pending model calculation.
