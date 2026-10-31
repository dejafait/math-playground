# Corollary 571a: real tilt misses negative first signs in a finite strip family

## Hypotheses

Let 0<=a<=4 and lambda be real, and define

    P_a(z)=(1+4*z^2)*(1-a*z^2),
    F_(a,lambda)(z)=exp(lambda*z)*P_a(z),
    N(F)=(1/(2*pi)) integral_0^(2*pi) |F(exp(i*theta))|^2 dtheta,
    D_1(F;0)=F'(0)^2-F(0)*F''(0).

Use L571 with r=1/2 and m=1. Its strict sufficient certificate for
D_1(F;0)<0 is N(F)<N_1, with exact designated zeros at +/-i/2;
other zeros are allowed. Put alpha=(4+sqrt(1767))/17.

## Conclusion

Each F_(a,lambda) is entire, real symmetric, normalized by F(0)=1,
and has zeros of exact order one at +/-i/2. All its zeros lie in
|Im z|<=1/2. For every a in the stated interval,

    min_(lambda real) N(F_(a,lambda))=17*a^2-8*a+17,

and the minimum is attained uniquely at lambda=0. L571's threshold
is N_1=120. Consequently

    exists real lambda with N(F_(a,lambda))<120
        if and only if 0<=a<alpha,
    D_1(F_(a,lambda);0)=2*a-8<0
        if and only if 0<=a<4, independently of lambda.

Thus [alpha,4) is a nonempty interval of negative first signs missed
by the strict norm certificate for **every** real exponential tilt.
At a=alpha the optimal norm is exactly 120, with negative first sign;
every nonzero tilt has norm greater than 120. At a=4 the first sign
is zero and the optimal norm is 257. No equivalence of the norm test
and negativity holds even in this finite strip-polynomial family.
This does not assert any actual-Xi realization or bound, nor any
failure of the sufficient implication in L571.

## Proof

### Source scope and specialization

Use L571's already audited threshold, and the standard H2
boundary/coefficient norm identity, in the form recorded there from
G. J. Groenewald, S. ter Horst and H. J. Woerdeman, *Optimal
interpolation in Hardy and Bergman spaces: a reproducing kernel Banach
space approach*, [arXiv:2412.11473v1](https://arxiv.org/pdf/2412.11473v1),
Section 4.1, PDF p.13. Only a finite polynomial's coefficient norm is
needed; no new general Hardy theorem or interpolation theorem is proved.

For the first-sign convention and finite-product class, use George
Csordas, *Fourier transforms of positive definite kernels and the
Riemann xi-Function*, [arXiv:1309.0055v2](https://arxiv.org/pdf/1309.0055v2),
Definition 1.1/(1.3), printed p.2, and generating identity (2.11), p.4.
These sources supply tools, not this family's optimal tilted norm or
certification interval. The prior SPECIALIZE assessment identified
that explicit comparison as the calculation still needed. No novelty
beyond the sources checked is claimed.

### Admissibility and exact orders

The exponential is entire and nowhere zero. The factor 1+4*z^2 has
simple roots +/-i/2, and the other factor equals 1+a/4>0 there.
Hence their exact order remains one for every allowed parameter,
including a=0 and a=4. If a>0 the remaining roots are the two simple
real roots +/-1/sqrt(a); if a=0 this factor is constant and there
are no remaining roots. The two root sets cannot coincide. This
proves the strip statement and checks the degree drop at a=0.
Real a and lambda give real symmetry, and F(0)=1.

In Csordas's finite-product terminology this is also a valid
strip-class example with Gaussian parameter zero: arrange each
opposite root pair together in (1.3). For a pair {w,-w}, the
canonical exponential corrections exp(z/w) and exp(-z/w) cancel,
and the product is 1-z^2/w^2. The finite reciprocal-square sum
converges automatically, the remaining real linear exponent is
lambda*z, and there is no root at zero. No infinite product limit,
zero-free quotient, or membership of Xi in this model is assumed.

### Optimization over all real tilts

Set W_a(theta)=|P_a(exp(i*theta))|^2. Since P_a is even,
W_a(theta+pi)=W_a(theta). Also

    |exp(lambda*exp(i*theta))|^2=exp(2*lambda*cos(theta)).

Changing theta to theta+pi in the continuous periodic boundary
integral, then averaging the two equal integrals, gives exactly

    N(F_(a,lambda))
      =(1/(2*pi)) integral_0^(2*pi)
          W_a(theta)*cosh(2*lambda*cos(theta)) dtheta
      >=(1/(2*pi)) integral_0^(2*pi) W_a(theta) dtheta
      =N(P_a).

There is no infinite series or limit exchange here. The inequality
uses W_a>=0 and cosh(x)>=1 for real x. If lambda!=0, at theta=pi/4
one has cos(theta)!=0 and

    W_a(pi/4)=|1+4*i|^2*|1-a*i|^2=17*(1+a^2)>0.

Thus the integrand difference is strictly positive there and, by
continuity, on a nonempty open interval. Its integral is positive.
For lambda=0 equality holds, proving uniqueness of the global minimum,
without differentiating the norm or assuming coercivity.

Now P_a(z)=1+(4-a)*z^2-4*a*z^4. The finite coefficient-norm identity
gives

    N(P_a)=1+(4-a)^2+(-4*a)^2=17*a^2-8*a+17.

This step is an application of orthogonality of the three distinct
circle monomials, not an approximate norm evaluation.

### Threshold, actual sign, and all parameter endpoints

Substituting r=1/2,m=1 into L571 gives q=1/4,b=1/4,c=15/4>1,
phi(c)=2*c-1=13/2, and

    N_1=b^(-2)*(1+phi(c))=16*(15/2)=120.

By the proved minimum, some real tilt meets the strict budget
exactly when

    17*a^2-8*a-103<0.

The two roots of this quadratic are (4-sqrt(1767))/17<0 and alpha.
The leading coefficient is positive, so on 0<=a<=4 its strict
negative range is exactly [0,alpha). Its values at a=2 and a=3
are -51 and 26, respectively, proving 2<alpha<3<4 and hence that
the missed interval is nonempty. At a=alpha equality in the
threshold occurs only at the unique optimal tilt; equality is not
L571's strict certificate.

The source generating identity (2.11), evaluated at center zero,
identifies D_1 with the coefficient of y^2 in F(iy)*F(-iy).
The real linear exponential factors cancel at that center, and

    F(iy)*F(-iy)=(1-4*y^2)^2*(1+a*y^2)^2
                =1+(2*a-8)*y^2+O(y^4).

Therefore D_1=2*a-8. Equivalently, the derivatives are F'(0)=lambda
and F''(0)=lambda^2+8-2*a, verifying the same convention directly.
This is a family-specific application, not a reproof of the general
generating identity. At a=0 the norm is 17<120 and the sign is -8;
at a=alpha the sign is negative because alpha<4; at a=4 it is zero
and the minimum norm is 17*16-8*4+17=257. For alpha<a<4 the minimum
norm exceeds 120 while the sign remains negative. These observations
establish the asserted missed interval including its left endpoint
and excluding its right endpoint. Other boundary roots, for example
the real unit-circle roots at a=1, are allowed by L571 and do not
affect the integral or designated orders.

### Relevance and limits

The new local evidence is that real linear tilt cannot repair this
certificate's lost first-sign information even when the extra zeros
are real and all nonreal zeros are the designated simple pair.
No negative sign in the family occurs with a successful tilt outside
the computed interval, since the global minimum rules out every real
lambda. This refutes a proposed blanket equivalence, not RH.
An actual-Xi use still requires independent amplitude or boundary-norm
control, a legitimate nonzero-center normalization and its height
uniformity. Central zeros and higher signs are untouched. No new
zero-free estimate, aggregate moment or numerical evidence is used.

### Independent bounded audit, 31 October 2026

Replayed the whole stated parameter range, using L571 only for its
strict sufficient threshold. At either designated root z=+/-i/2,
P_a'(z)=8*z*(1+a/4)!=0. The remaining roots are real when a>0
and absent when a=0. The nonvanishing exponential preserves these
orders, real symmetry and normalization. Boundary zeros at a=1
are permitted: L571 neither divides by boundary values nor requires
the absence of other zeros. No L018 premise is needed here.

For the norm, write I(lambda)=integral W_a(theta)*exp(2*lambda*cos(theta))
dtheta over one complete period. Substitution by pi, periodicity and
evenness of P_a give I(lambda)=I(-lambda). Averaging these two exact
integrals gives the displayed cosh integral. For lambda!=0 its excess
over I(0) is continuous and nonnegative everywhere, and at theta=pi/4
it equals 17*(1+a^2)*(cosh(sqrt(2)*lambda)-1)>0. Thus the excess
integral is strictly positive, including a=0,1,alpha,4. This proves
the global minimum and uniqueness without a local-extremum argument.
At zero tilt, integrating the cross terms between exponents 0,2,4
gives zero since each nonzero integer Fourier mode has integral zero;
the three squared coefficients give 1+(4-a)^2+16*a^2 exactly.

Independently, q=b=1/4 and c=15/4>1 in L571, so
N_1=16*(1+2*(15/4)-1)=120. Subtracting this threshold yields
17*a^2-8*a-103, with discriminant 7068=4*1767 and roots
(4+/-sqrt(1767))/17. The lower root is negative; the upper is alpha.
The values -51 at a=2 and 26 at a=3 establish 2<alpha<3.
Hence the strict-budget range on [0,4] is [0,alpha), with equality
at alpha only for zero tilt. Separately, direct differentiation gives
F(0)=1, F'(0)=lambda, F''(0)=lambda^2+2*(4-a), and therefore
D_1=2*a-8. In particular all a in [alpha,4) have negative defect
and every tilt misses the strict budget; a=4 has zero defect and
norm minimum 257, whereas a=0 has defect -8 and norm minimum 17.
These checks include both excluded strict endpoints and the degree
drop. No error in the claimed finite obstruction was found. This
validates a local classical specialization, with no new source-level
novelty, actual-Xi estimate, central-zero case or higher-sign claim.

## Mathlib

Full matching theorem and supporting coverage not checked; availability
is unknown. The calculation needs only finite polynomial coefficients,
circle orthogonality, real cosh positivity and a quadratic inequality.
General Hardy support would not by itself establish this exact
family's optimized interval. [Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
