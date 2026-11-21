# Corollary C035a: inverse Euler weights do not preserve a fixed cone

## Hypotheses

Fix a real angle 0<theta<pi/2 and the closed cone

    K_theta={0} union {w!=0: |arg(w)|<=theta},

where arg is the principal argument. On real polynomials define the
diagonal operator V by

    V(sum_j a_j w^j)=sum_j v_j a_j w^j,
    v_j=1/[2(2j+3)]    (j>=0).

The variable is w, and the weights act on its ordinary coefficients.
The same diagonal definition applies if the coefficients are written
with factorial denominators. All scalar normalizations below are
nonzero.

## Conclusion

The real polynomial

    p_theta(w)=w^2-2 cos(theta) w+1

has unit-modulus roots exp(+i theta), exp(-i theta), both on the
boundary of K_theta. However, both roots of V(p_theta) are outside
K_theta. More precisely, writing c=cos(theta), they are

    z_+=7c/5+i sqrt(7/3-49c^2/25),
    z_-=7c/5-i sqrt(7/3-49c^2/25),

with modulus sqrt(7/3) and principal arguments +phi,-phi, where

    phi=arccos((sqrt(21)/5) cos(theta)),
    theta<phi<pi/2.

Thus V does not preserve K_theta on all real polynomials whose zeros
lie there, for any of the stated fixed angles. This is a specialization
of the known three-term coefficient-ratio diagnostic, not a claimed
new general preserver theorem or a counterexample to RH.

## Proof

### Known diagnostic and the required specialization

David A. Cardon, Tamas Forgacs, Andrzej Piotrowski, Evan Sorensen and
Jason C. White, *On Zero-Sector Reducing Operators*,
[arXiv:1802.02641v1](https://arxiv.org/pdf/1802.02641v1#page=8),
7 February 2018, Section 4.2, p. 8, studies the real polynomial
x^n(x^2-bx+c) through the ratio v_n v_(n+2)/v_(n+1)^2.
The closed cone convention is on p. 1. Only the three-term mechanism
is used here; no complex-input characterization or transcendental
extension is imported. We compute the prescribed rational weights
and solve the weighted quadratic directly to retain its leading
coefficient. Strict sector reduction and preservation in the same
fixed cone are different assertions; the root calculation below
tests the latter exactly.

For the present n=0 specialization, the source's linear parameter
is b=2 cos(theta)>0 and its constant parameter is 1. The input roots
are exp(+i theta) and exp(-i theta); hence they are nonzero and in
the right half-plane as required for this diagnostic. These facts
also prove the input assertion, including the closed boundary.

### Weighted polynomial, normalization and both output roots

The three weights and their ratio are exactly

    v_0=1/6,  v_1=1/10,  v_2=1/14,
    v_0 v_2/v_1^2=25/21>1.

Applying V coefficient by coefficient gives

    V(p_theta)(w)=w^2/14-cw/5+1/6.

Multiplication by 14, a nonzero common scalar, gives the monic
polynomial with exactly the same roots and multiplicities,

    q_theta(w)=14 V(p_theta)(w)=w^2-(14c/5)w+7/3.

In particular, normalization multiplies every coefficient; it does
not drop the original leading factor selectively. Completing the
square gives

    q_theta(w)=(w-7c/5)^2+(7/3-49c^2/25).

Since 0<c<1,

    7/3-49c^2/25 > 7/3-49/25 = 28/75 > 0.

The two distinct conjugate roots are therefore exactly z_+,z_-
in the conclusion. Their real parts are positive, and direct
squaring of the real and imaginary parts gives |z_+|^2=|z_-|^2=7/3.
Thus their arguments are +phi,-phi with 0<phi<pi/2, and

    cos(phi)=(7c/5)/sqrt(7/3)=(sqrt(21)/5)c.

Because 0<sqrt(21)/5<1 and c>0, cos(phi)<c=cos(theta).
Cosine is strictly decreasing on [0,pi], so phi>theta.
Both output roots are nonzero and strictly outside the original
closed cone. This proves the universal real-polynomial obstruction
for each fixed theta in the specified open interval. No limiting
argument at theta=0 or theta=pi/2 is used.

### Scope relative to the actual-Xi interface

The displayed operator in C034z is B'=2(3+2w d/dw)A''.
Since w d/dw acts on w^j by j, its coefficientwise inverse has
exactly the weights defined here. This is only the operator
identification motivating the diagnostic; no conclusion or proof
of C034z is needed for the counterexample above.

The actual A'' is a particular transcendental real entire function,
with order and gamma coefficients specified in C034z. The polynomial
p_theta is not substituted for that actual function. The calculation
does not decide a restricted inverse theorem for those coefficients,
or for transcendental inputs of order at most 1/2. It does not refute
Kim--Lee, GORRTTW Theorem 1.2, or an actual-Xi sector statement.
It only rules out obtaining the missing inverse step from a universal
real-polynomial preservation assertion of this form. RH_2(T), actual
transformed-sector membership, all-degree control, unshifted descent
and the mixed positivity in L030/L032/C032a remain unresolved.

## Mathlib

Full matching Mathlib coverage for this exact diagonal operator and
fixed-angle counterexample has not been checked. No absence claim is
made. The proof is exact elementary algebra and an argument comparison;
no numerical evidence, mathematical script or Lean verification is used.
