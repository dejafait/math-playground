# Corollary C030k: scalar theta sign from the positive heat trace

## Hypotheses

Use the actual completed zeta function
xi(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)/2 and set
F(r)=xi(1/2+r). Count all nontrivial zeros with multiplicity, including
any off the critical line. Write

    lambda(rho)=-(rho-1/2)^2,
    W(t)=sum_(Im(rho)>0) m(rho) exp(-lambda(rho)*t), t>0.

Import the following precise preprint results, without independently
certifying their analytic estimates or finite zero verification:

- Nicholas G. Polson, *On Hilbert's 8th Problem*,
  [arXiv:1708.02653v24, 11 September 2026](https://arxiv.org/pdf/1708.02653v24):
  Section3/(2), p6, and Definition5.1/(4), p8, specify one factor per
  reflection pair with multiplicity; Theorem5.3/(5)-(6) and its proof,
  p9, give the logarithmic-derivative representation and absolute
  integrability below. TheoremA, p3, proved in Section6.3, p15, gives
  W(t)>0 for every t>0. Only this sign, not W'<0, is needed.
- Agum Abdillah, *A Theta-Geometric Framework for the Hankel Positivity
  Problem in the Riemann Hypothesis*,
  [viXra:2609.0027v1, September 2026](https://vixra.org/pdf/2609.0027v1.pdf):
  (5.3)-(5.5), p16, (5.11)-(5.16), p17, and Section5.5, p18, give
  the actual theta density, its convergent transform and normalization.
  Equations(6.11)-(6.12), pp20-21, (7.17)-(7.21), pp24-25, and
  (7.43)-(7.44), pp27-28, identify the variance/kernel observable.
  The scalar question being compared is (8.16)/Section8.7, p30.

Explicitly, on u>=0 use the source's normalization

    Phi(u)=sum_(n>=1) pi*n^2*exp(5u/2)
             *(2*pi*n^2*exp(2u)-3)*exp(-pi*n^2*exp(2u)),
    A(r)=integral_0^infinity Phi(u)cosh(ru)du, F(r)=4A(r).

Here Phi>0 and A(r) is finite and positive for every real r. For r>0
put x=r^2 and define

    S(x)=F'(sqrt(x))/(2*sqrt(x)*F(sqrt(x))),
    dP_r(u)=Phi(u)cosh(ru)du/A(r),
    d omega_r(y)=Phi(y/r)cosh(y)dy/(r*A(r)),
    a(y)=y*tanh(y)-y^2*sech(y)^2, b(y)=y*tanh(y).

Thus omega_r is the law of Y=rU when U has law P_r. The prime on
S always means differentiation in x, whereas F' and A' mean r.
No r=0 assertion, generic density replacement, or RH assumption is made.

## Conclusion

For every r>0, all expressions below are finite and

    -S'(r^2)=integral_0^infinity t*exp(-r^2*t)*W(t)dt
             =(E_(omega_r) a(Y)-Var_(omega_r) b(Y))/(4*r^4)>0.  (1)

In particular the strict inequality

    Var_(omega_r) b(Y)<E_(omega_r) a(Y)                       (2)

holds relative to the imported positive-W theorem. The double integral
of K(y,z)=a(y)+a(z)-(b(y)-b(z))^2 against omega_r times itself is
strictly positive as well. This settles the scalar sign in (8.16)
under these imports; it supplies no all-degree mixed-Hankel positivity,
fixed reciprocal-zero Stieltjes measure, or common-graph realization.

## Proof

### Normalization and spectral convention

Let G_P(x)=F(sqrt(x))/F(0), Polson's Section3 function. The chain rule
and the theta normalization give, for x=r^2>0,

    G_P'(x)/G_P(x)=F'(r)/(2*r*F(r))=A'(r)/(2*r*A(r))=S(x).   (3)

The factor4 in F=4A and the constant F(0) both cancel. Abdillah's
sign-reversed fold is K_fold(w)=F(i*sqrt(w)); hence
K_fold(-x)=F(sqrt(x)) and -K_fold'(-x)/K_fold(-x)=S(x).
This checks the orientation, rather than identifying opposite derivatives.

Both sources square a centered zero and choose one representative of
each pair under negation. For an actual zeta zero this is the pair
{rho,1-rho}, and its exponent is lambda=-(rho-1/2)^2. C030g gives
the absolutely convergent identity between this trace and the
positive-ordinate trace above, including multiplicities. An off-line
quartet contributes two conjugate exponents; it is not collapsed to
one real exponent. There is no remaining factor2. C030b's finite-block
specialization is a consistency comparison, not a premise of this proof.

Theorem5.3 applies at every x>0: its proof supplies min Re(lambda)>0
using already published low-height verification. We import this source
hypothesis verification, not a stronger zero-free assertion. Together
with (3) it gives

    S(x)=integral_0^infinity exp(-x*t)W(t)dt,
    integral_0^infinity min(1,t)*|W(t)|/t dt<infinity.        (4)

### Differentiated Laplace integral, including both endpoints

Fix x0>0. The second assertion in (4) says separately

    integral_0^1 |W(t)|dt<infinity,
    integral_1^infinity |W(t)|/t dt<infinity.

For x in [x0/2,3*x0/2], the absolute value of the derivative of the
integrand in (4) is t*exp(-x*t)|W(t)|. On 0<t<1 this is at most
|W(t)|. On t>=1 it is at most C*|W(t)|/t, where
C=sup_(t>=1) t^2*exp(-x0*t/2)<infinity. This last supremum is finite
by elementary exponential decay. The undifferentiated integrand is
also dominated: near zero by |W| and at infinity by D*|W|/t with
D=sup_(t>=1)t*exp(-x0*t/2)<infinity.

For the difference quotient at x0, the real mean value theorem bounds
its absolute value by the same derivative majorant whenever |h|<x0/2.
Dominated convergence therefore proves

    -S'(x0)=integral_0^infinity t*exp(-x0*t)W(t)dt.         (5)

This checks the required endpoint domination; compact-time convergence
alone would not do so. C030g gives continuity of W on positive time.
By the imported W(1)>0, a neighborhood of 1 has a positive lower bound
for W. Since the other factors in (5) are positive, its integral is
strictly positive. No limit x0->0 or differentiation of W is needed.

### Exact theta variance and the factor 4r^4

The necessary theta differentiations can be justified without new
theta-tail estimates. On a compact interval |r|<=R0 choose R>R0.
For k=0,1,2, u^k*exp(R0*u)<=C_k*exp(R*u) on u>=0, and

    integral_0^infinity Phi(u)exp(R*u)du<=2*A(R)<infinity.

This dominates the integrands and their first two r derivatives.
Consequently A'=integral u*Phi*sinh(ru)du and
A''=integral u^2*Phi*cosh(ru)du, with finite second moments under P_r.
The moments of a(Y) and b(Y)^2 are finite since
|a(y)|<=y+y^2 and b(y)^2<=y^2 for y>=0.

Writing M=E_(omega_r)b(Y), these formulas give exactly

    M=r*A'(r)/A(r), E_(omega_r)Y^2=r^2*A''(r)/A(r).

Since a(y)=b(y)+b(y)^2-y^2,

    E a-Var b=M+M^2-E Y^2
             =r*A'/A+r^2*(A'/A)^2-r^2*A''/A.              (6)

Differentiate S(r^2)=A'/(2rA), using d/dx=(2r)^(-1)d/dr.
The negative derivative is

    -S'(r^2)=A'/(4*r^3*A)+(A'/A)^2/(4*r^2)
                              -A''/(4*r^2*A).

Multiplying by 4r^4 yields precisely (6), proving (1)-(2). In
particular the measure's r dependence has not been frozen. Finally
product integration of K is justified by its finite second-moment
majorants. Independence gives
integral integral (b(y)-b(z))^2=2*Var b, hence integral integral K
=2*(E a-Var b)=8*r^4*(-S'(r^2))>0, agreeing with (7.19)-(7.20).
This is an integrated sign, not pointwise positivity of K.

The reproduction passes its normalization, domination and strictness
tests. The scalar sign is already covered by Polson's positive-W
representation; its theta variance form is a specialization. No
novelty claim follows from Abdillah's first-order discussion. Neither
this calculation nor positive W establishes the missing all-degree
signs or a Stieltjes representation with fixed spectral support.
The finite-height/all-degree and heat-block propagation stops are
unchanged. There is no RH candidate here.

## Mathlib

Full matching coverage of this actual-theta specialization and of the
two preprint theorem inputs is unchecked, not asserted absent. The
chain rule, dominated convergence and variance algebra are ordinary
supporting mathematics, not a checked formalization of this result.
Reference: [Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
