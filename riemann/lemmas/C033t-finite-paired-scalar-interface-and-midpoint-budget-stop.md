# Corollary C033t: finite paired scalar interface and a midpoint-budget stop

## Hypotheses

Retain C033s's exact objects, cuts a=2^-256, b=2^256, order128,
n=1, delta=1/16, and real signed width measures eta of mass one and
TV at most2 on [1,2]. In particular retain the actual positive-ordinate
divisor with conjugation and multiplicity, excluded ordinate zero,
strict strip, gamma>14, explicit counting, verified real zeros through100,
retained real zero in(14,15), reciprocal-square tail, heat positivity,
separate fixed-j errors through j=2, Gaussian half-variance convention
and both fixed-v1 preprint qualifications. Neither the preprints nor
their zero data are independently certified here. C033s's conditional
bounds passed audit1787; all their qualifications remain in force.

Write T(z)=sum_(j=0)^128 z^j/j!, and use C033s's measures Qc_sigma,P
and masses Mc_sigma,m. For s>0 define

    q_sigma(s)=integral_[a,b] exp(-s*t)D_sigma(t)dt,
    p(s)=integral_[1,3/2] exp(-s*t)ell_1(t)dt.

No positivity of Qc_sigma, R_sigma or eta, moment condition, positive
separator at these fixed parameters, or actual-Xi realization is assumed.
The cost test below concerns one explicitly specified real-midpoint
certification scheme, not all quadrature or all error analyses.

## Conclusion

The exact finite-approximant samples are

    Rtildehat_sigma(s)=exp(-Mc_sigma)*T(q_sigma(s)),
    lambdatildehat(s)=exp(m)*T(-p(s)).                    (1)

Their paired observable uses the four indexed nodes a_-,2*a_-,a_+,2*a_+,
where a_-=16*log(2)/15 and a_+=16*log(2)/17, with coefficients

    v=(2*a_-,-2*a_-,-2*a_+,2*a_+),
    sum_i |v_i|=4*(a_-+a_+)<2048/255<9.                 (2)

Here each sample in the observable is lambdatildehat minus the signed
width integral of Rtildehat. In particular the normalization factors,
finite polynomial and j=0 terms have not been replaced by their infinite
resummations or omitted.

Put epsilon=2^-112. Suppose every scalar input m,Mc_sigma,p(s_i),
q_sigma(s_i) has absolute error at most epsilon, uniformly in sigma,
with bounded Borel approximate width data. If the final finite expression
formed from those data, including nodes, coefficients, polynomials and
exponentials, is evaluated with an additional absolute error at most
2^-25, then its error against the full paired observable is at most

    E_lambda+2*(E_cut+E_series)+2^-25+2^-25 <2^-20.       (3)

The first three quantities are C033s's omitted-part allowances. This is
a conditional error allocation, not an established512-bit arithmetic
implementation. Errors in rounded nodes must be included in the stated
scalar-input or final-expression allowances; exact nodes are used in(1).

For a concrete certification branch, compute the normalization m by
composite midpoint quadrature in y=log(t), and certify its quadrature
error using the uniform second-derivative bound proved below. Reserve
epsilon/2=2^-113 for this quadrature, and the other half for all its
profile and arithmetic errors. The displayed rational error certificate
with N equal cells is

    E_mid(N)=1021/(384*N^2).                            (4)

Thus the least N accepted by THIS certificate is the smallest integer
with

    384*N^2 >= 1021*2^113.                              (5)

It exceeds10^17, and in particular exceeds the entire declared10^7-term
budget. This failure already counts m only once. All other integrals,
nested profile quadrature, prime powers, width work and polynomial
arithmetic would add nonnegative cost. No numerical observable is
evaluated and no full512-bit or10^7-term preflight passes.

This is a quantitative specialization and a failed sufficient-error
scheme, not progress beyond the source theorems checked. It does not
lower-bound the actual midpoint error, the minimal accuracy required
of m under a sharper correlated analysis, or the cost of analytic,
adaptive, resummed or otherwise improved evaluators. Enlarged-width
Gaussian bounds remain unpaid in this result. The conditional interface
and specified failure pass conceptual audit1789 below, including complex
approximate scalar data; no evaluator or source-wide certification follows.
RH remains open.

## Proof

### Imported tools and why there is application work

Use the pre-existing SPECIALIZE assessment1780. For the product of
Laplace transforms import Ante Mimica, *Laplace transform*, Dresden
course27 April-1 May2015,
[Proposition1.4(iv), pp.6-7](https://web.math.pmf.unizg.hr/~amimica/lt.pdf).
Its positive-measure statement extends here by the finite-signed Fubini
argument already proved in C033j after(9): exp(-s*(x+y)) has modulus
at most one on X times X, and the product variation measure is finite.
Finite polynomial sums therefore require no interchange of infinite
series. The known theorem is imported, not reproved.

For real C^2 composite midpoint quadrature import Erik Talvila and
Matthew Wiersma, *Simple derivation of basic quadrature formulas*,
[arXiv:1202.0249v1, Section1/(1.1) and composite rule p.2;
Section4 proof p.8](https://arxiv.org/pdf/1202.0249v1), already used in
C033m. The error is at most interval_length^3*sup|f''|/(24*N^2).
This is a real smooth direct quadrature case of the assessed interface;
no analyticity callback or complex-width estimate is assumed.

The Gaussian identity and profile derivatives needed for m are imported
locally from C033m(3)-(4), whose source specialization and application
audit remain qualified there. In particular F(w)=p_w(0) is real C^2 on
[1,2], and

    |F|<21, |F'|<200, |F''|<2400.                      (6)

The primary Gaussian input is S. Sra, *Some positivity properties of
Riemann Xi under smoothing*,
[fixed2611.00345v1, Proposition3.1/(3.2)-(3.3), pp.5-6,
proof C.1 p.21](https://hexagonmath.org/pdf/2611.00345v1).
The bounds in(6) are C033m's application of C032w, not assertions of
that source. C032w imports the unconditional complex-zero explicit
formula from A. Connes, *Heat Expansion and Zeta*,
[arXiv:2402.13082v1, Section2/(4)-(9), p.4](https://alainconnes.org/wp-content/uploads/heat-zeta.pdf).
No RH-dependent real-spectrum formula is used. Neither the source nor
the midpoint theorem supplies the scalar error allocation or cost count
below; only these application details are derived here.

### Finite scalar reduction and logarithmic-time interface

Applying the cited product rule to each finite convolution power gives
q_sigma(s)^j and (-p(s))^j. Multiplying by the existing normalizations
proves(1), including T's constant term. The kernels vanish at zero
only after the exact paired combination; the atoms have not been deleted
from any individual transform. C033r(10), or C033s's explicit n=1
kernel, gives(2). Since log(2)<1,
4*(a_-+a_+)<4*(16/15+16/17)=2048/255<9.

For clarity the proposed direct jump integrals can be written exactly
in logarithmic time. For y in [-256*log(2),256*log(2)] put

    u_sigma(y)=exp(y)/(1+4*sigma*exp(y)),
    d_sigma(y)=exp(-y/2)*[K(u_sigma(y))-K(u_1(y))].

C033s's density identity and the ordinary finite-interval change of
variables give

    Mc_sigma=integral d_sigma(y)dy,
    q_sigma(s)=integral exp(-s*exp(y))*d_sigma(y)dy.      (7)

No quantitative enlarged-width profile or quadrature bound for(7)
is asserted. The preflight stops on the independent m certificate first.

### Uniform scalar error allocation

C033s gives |Mc_sigma|,|q_sigma(s)|<=24 and 0<=p(s)<=m<21.
Every line segment between exact and epsilon-approximate inputs lies
in the square of absolute coordinate bounds25 for Rtilde, and22 for
lambdatilde. For real z,

    |T(z)|<=exp(|z|), |T'(z)|<=exp(|z|).

Therefore both partial derivatives of exp(-M)*T(q) have absolute
value at most exp(50)<3^50<2^80. Both partial derivatives of
exp(m)*T(-p) have absolute value at most exp(44)<3^45<2^72.
The last integer inequalities follow from 3^5=243<256=2^8;
e<3 suffices for the exponential comparisons. Integrating derivatives
along the real input segment yields per-sample errors

    error_R <=2^81*epsilon,
    error_lambda <=2^73*epsilon.                       (8)

There is no positivity estimate for the signed mixture. Integrating
the first bound in(8) against |eta| uses its TV cap2. Equation(2)
then bounds the whole paired input error by

    9*(2^73+2^82)*epsilon
       <2^87*epsilon=2^-25.                           (9)

The Borel assumption makes those approximate integrals defined.
Adding the separately reserved final-expression error and C033s's
omission error below2^-44 proves(3). In fact
2^-44+2*2^-25<2^-23<2^-20. This proves sufficiency of the allocation;
it does not prove that these scalar tolerances are necessary, that the
unspecified finite arithmetic can meet them at512 bits, or that the
input integrals have been evaluated.

### Logarithmic normalization bound and decisive cost test

Set L=log(3/2), z(y)=exp(-y)/4 and w(y)=1+z(y). C033m(3)
and t=exp(y) give

    m=integral_0^L f(y)dy,
    f(y)=sqrt(pi)*exp(-y/2)*F(w(y)).                    (10)

Throughout this interval, 1/6<=z<=1/4 and 7/6<=w<=5/4.
These widths are inside [1,2], so every use of(6) is within its
proved numerical scope. C033m's real C^2 result and elementary chain
rules make f real C^2 including both endpoints. Since z'=-z,z''=z,

    f''(y)=sqrt(pi)*exp(-y/2)
             *[F(w)/4+2*z*F'(w)+z^2*F''(w)].

Using sqrt(pi)<2, exp(-y/2)<=1 and(6) yields

    |f''|<2*(21/4+200/2+2400/16)=1021/2.              (11)

Also 0<L<1/2, by log(1+x)<x at x=1/2. The imported midpoint
rule now gives an error bounded by
L^3*(1021/2)/(24*N^2)<1021/(384*N^2), proving(4).
The declared branch accepts only when this displayed allowance is
at most2^-113. Its algebraic acceptance condition is exactly(5).

Integer comparison at N=10^17 gives

    384*10^34 < 1021*2^113.

Hence even that many cells do not pass this certificate. At the actual
budget N=10^7, its bound is 1021/(384*10^14), about2.659e-14,
whereas its quadrature allocation2^-113 is about9.630e-35.
These are a bound and an allocation, not observed numerical errors.
No smaller N can pass this monotone rational acceptance test. One
midpoint value requires at least one outer integrand term, so m alone
exceeds the aggregate10^7-term budget, even granting free nested
profile evaluations and arithmetic. It is unnecessary to estimate the
remaining positive costs or prove a512-bit implementation after this
failure. Even relaxing the scalar tolerance by a factor32 leaves the
same displayed node test above10^16; this does not repair the scheme.

All rational comparisons, the exact least accepted integer, conditional
combined allowance, and the budget failure are recorded by

    python3 scripts/smoothed-law/paired_scalar_preflight_1781.py

in scripts/smoothed-law/paired_scalar_preflight_1781.json. The script
performs integer/rational preflight only, without any quadrature,
divisor approximation or evaluation of the observable. The certificate
verifies these comparisons, not the analytic hypotheses or C033s.

### Scope of the stop

The norm-based scalar propagation and uniform second-derivative
midpoint allowance fail together. This supplies a specific cost reason
to abandon their literal numerical implementation. It does not exhaust
the direct transform interface: cancellation-aware scalar bounds or
high-order analytic quadrature could change the certificate. They must
retain or pay changes to the order128 polynomial, verify their enlarged-
width domains and count all costs before any implementation. This
failure is distinct from stop1576's expanding spatial-disk enumeration
and stop1571's independent divisor boxes. None is a global prohibition.

### Conceptual audit1789 — 19 November 2026

**Verdict.** Claims (1)-(11) pass under the stated conditional inputs.
The prior SPECIALIZE assessment1787 and source comparison1788 cover
this application audit. The scalar proof's real-segment wording is
incomplete for potentially complex approximate data; point3 below
explicitly verifies that stated scope with the same constants. No
real-data restriction, new bound, positivity assumption or mathematical
input is added. The imported tools remain Mimica Proposition1.4(iv),
with C033j's finite-signed justification, and Talvila-Wiersma's real
closed-interval composite midpoint theorem cited above. Their general
theorems are not reproved. The validation is local, not mathematics
beyond the checked sources or a recertification of the two preprints.

1. **Finite signed transforms and zero atoms.** C033s's restrictions
   Qc_sigma and P are finite measures on X, the former signed. For
   s>0 the convolution kernel has modulus at most one, so C033j's
   finite-signed product rule applies at every one of the129 orders.
   The transform of Qc_sigma^{*j} is q_sigma(s)^j; the transform of
   (-1)^j P^{*j} is (-p(s))^j. The j=0 transform is1 in both cases,
   proving (1) with precisely exp(-Mc_sigma) and exp(m). This uses
   neither an infinite resummation nor positivity of Qc_sigma.
   At n=1 the binomial coefficients in C033r(10) give
   2*a_x*(thetahat(a_x)-thetahat(2*a_x)). Subtracting the two centers
   gives the signs and node order in (2). Each center's two
   coefficients sum to zero, so a zero atom cancels in the exact
   observable, while remaining present in every individual sample
   and in its perturbation bound. The coefficient sum is exactly
   4*(16/15+16/17)*log(2)<2048/255<9.

2. **Logarithmic substitution.** On the compact interval [a,b],
   t=exp(y) has Jacobian exp(y). Multiplying C033s's density
   t^(-3/2)*(K(u_sigma(t))-K(u_1(t))) by that Jacobian gives
   exp(-y/2)*(K(u_sigma(y))-K(u_1(y))). Thus both formulas (7)
   have the stated exponent, endpoints and optional Laplace factor.
   Only exact finite-interval substitution is asserted; no estimate
   of the small difference by two separately evaluated large terms,
   or enlarged-width profile computation, enters the proof.

3. **Full scalar domain and signed-width amplification.** The exact
   inputs are real with |Mc_sigma|,|q_sigma|<=24 and 0<=p<=m<21.
   If approximate inputs are complex, let DeltaM,Deltaq denote
   their differences, of modulus at most epsilon. On the path
   (M_r,q_r)=(M+r*DeltaM,q+r*Deltaq), 0<=r<=1, both moduli are
   at most25. For every complex z, the finite triangle inequalities

       |T(z)|<=sum_(j=0)^128 |z|^j/j!<=exp(|z|),
       |T'(z)|<=sum_(j=0)^127 |z|^j/j!<=exp(|z|)

   hold. Also |exp(-M_r)|=exp(-Re M_r)<=exp(|M_r|).
   Differentiating this finite expression in the real parameter r,

       d/dr [exp(-M_r)*T(q_r)]
        =exp(-M_r)*[-DeltaM*T(q_r)+Deltaq*T'(q_r)].

   Its integral has modulus at most2*exp(50)*epsilon, hence at
   most2^81*epsilon. The same real-parameter calculation for
   exp(m_r)*T(-p_r), on |m_r|,|p_r|<=22, gives the bound
   2*exp(44)*epsilon<=2^73*epsilon. The fundamental theorem of
   calculus is applied componentwise to real and imaginary parts;
   no complex mean-value theorem or complex-width profile is needed.
   The displayed strict integer majorants justify both binary bounds.
   This verifies (8) over the entire stated approximation domain.

   Bounded Borel approximate width data remain bounded Borel after
   a finite polynomial and exponential. Their real and imaginary
   parts are integrable against the finite signed eta, and
   |integral error_R deta|<=integral |error_R| d|eta|
   costs exactly its cap2. Summing the four indexed samples gives
   at most(2048/255)*(2^73+2^82)*epsilon, strictly below (9).
   No positivity of eta, Q_sigma or R_sigma, finite-width support,
   independence of errors or correlation cancellation is used.

4. **Exact versus rounded nodes and the final allowance.** Define
   the reference approximate expression using the exact four nodes
   and coefficients, the hypothesized scalar approximations to the
   exact-node values, and the exact signed width integrals. Point3
   bounds its difference from the exact finite approximant. A value
   computed at a rounded node qualifies as such a scalar input only
   when its error relative to that exact-node value is <=epsilon;
   alternatively the resulting discrepancy must be paid in the
   separate final-expression allowance. Coefficient rounding,
   polynomial/exponential arithmetic and numerical width integration
   likewise belong to that additional2^-25 allowance. They are not
   free, nor certified merely by bounded Borel dependence. The
   conditional hypothesis explicitly includes these errors; no
   implemented continuum integral or512-bit arithmetic follows.

   C033s/audit1787 gives E_lambda+2*(E_cut+E_series)<2^-44.
   Adding that allowance, the scalar reserve2^-25 and the distinct
   final-expression reserve2^-25 gives (3), since
   2^-44+2^-24<2^-23<2^-20. The mass-one requirement on eta is
   retained but is not used in this sufficient absolute-error bound.

5. **Real midpoint hypotheses, endpoints and curvature.** C033m(3)
   gives ell_1(t)=sqrt(pi)*t^(-3/2)*F(1+1/(4t)). Its change of
   variables yields exactly (10); no Gaussian factor two is lost.
   On the whole closed interval 0<=y<=log(3/2), z ranges from1/4
   to1/6 and w ranges from5/4 to7/6, inside C033m's audited real
   C^2 width domain. Conjugation of the actual divisor makes F real.
   With h=exp(-y/2), h'=-h/2, h''=h/4, w'=-z and w''=z,
   the product and chain rules give

       (h*F(w))''=h*[F(w)/4+2*z*F'(w)+z^2*F''(w)].

   The cross term contributes z*F', and w'' supplies the other
   z*F'. Applying |F|<21,|F'|<200,|F''|<2400, sqrt(pi)<2
   and h<=1 gives precisely1021/2 in (11). The real closed-interval
   midpoint theorem therefore applies to every cell, including both
   endpoints. The strict length bound log(3/2)<1/2 supplies the
   rational allowance1021/(384*N^2). The other half of epsilon
   remains reserved for profile and arithmetic errors, including
   rounded logarithmic endpoints and nodes; it is not verified here.

6. **Independent certificate comparison and exact stopping scope.**
   The separate script

       python3 scripts/smoothed-law/paired_scalar_audit_1789.py

   reconstructs the order129 terms by rational recurrence, the four
   coefficient bound by summation, and the midpoint coefficient from
   the chain-rule terms. It independently finds the least acceptable
   cell count by integer bisection, not the original square-root
   calculation, and compares every saved error/midpoint field and
   assertion with its reconstruction. All54 checks passed. The full
   evidence is scripts/smoothed-law/paired_scalar_audit_1789.json;
   the original preflight1781 certificate was not overwritten.

   Let A=1021*2^113 and N=166165941979008264. Complete inspected
   integer comparisons are

       A-384*(N-1)^2 = 67456785815713003136 >0,
       384*N^2-A     = 60158657624165343232 >0.

   Monotonicity for positive integer N proves that this is exactly
   the least count accepted by (5), exceeding10^17 and10^7.
   At the declared budget the displayed allowance is exactly
   1021/38400000000000000, about2.65885416667e-14; the required
   quadrature allowance is2^-113, about9.62964972194e-35. Relaxing
   that allowance by32 gives least count29374266093901787>10^16.
   The conditional total in (3) is about5.96046729049e-8, below
   2^-20, about9.53674316406e-7; all comparisons use exact rationals.

   This counts the specified normalization once, with at least one
   outer integrand term for each cell of this direct rule. Granting
   free nested work only makes its failure stronger. It does not
   lower-bound actual midpoint error, certify a minimum necessary
   scalar tolerance, or rule out other cost mechanisms. No quadrature
   or observable was evaluated. Stops1781/1782 stay parked.

The finite scalar interface is conditionally validated. Positive
separation at n=1,delta=1/16, source-wide and zero-data correctness,
continuum evaluation and512-bit realization remain unpaid. Retain the
full divisor, conjugation/multiplicity, excluded ordinate zero, strict
strip, gamma>14, counting, real zeros through100, retained real zero,
reciprocal-square tail, heat positivity, separate j<=2 heat errors,
Gaussian half-variance and both fixed-v1 qualifications. The main
all-degree positivity, signed-height, unrestricted-variation and actual-Xi
realization gaps are unchanged. No DAG edge or main argument changes.

## Mathlib

Full matching coverage for this qualified actual-zero scalar interface
and numerical certification stop is unchecked/unknown. Standard finite
sum, signed integration, convolution, differentiation and quadrature
facts would support pieces; no matching theorem or Lean verification
is claimed. Audit1789 is an informal conditional application audit;
its exact arithmetic certificate is not Lean verification.
