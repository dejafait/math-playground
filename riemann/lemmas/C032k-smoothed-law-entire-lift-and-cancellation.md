# Corollary C032k: entire lifts and the full finite-law cancellation condition

## Hypotheses

Use the actual-zero normalization, Gaussian half-variance sigma>0,
profile p_sigma, heat sums H and H_sigma, exponent B_sigma and
probability measure nu_sigma on [0,infinity) of C032j. In particular,
p_sigma is even entire, real on R, has logarithmic growth on R, and
p_sigma(0)>0. These are cited preprint inputs, not assumptions of RH
or of p_sigma>=0. Retain the source's finite-zero and counting inputs:
the first positive ordinate is greater than 14, |delta_rho|<1/2,
and N(T)=O(T log(T+2)), counting multiplicity.

Fix a finite r>=2, distinct sigma_1,...,sigma_r>0, and real
a_1,...,a_r with sum a_j=1. Write nu=sum a_j nu_sigma_j. This is
initially only a finite signed measure of total mass one. Whenever a
conclusion below invokes nonnegativity, it explicitly assumes nu>=0;
no positivity of this combination is proved here.

## Conclusion

For each sigma define, with removable values in the integrand,

    R_sigma(w) = integral_0^infinity
                  (p_sigma(x)-p_sigma(iw))/(x^2+w^2) dx,
    O_sigma(w) = 2*pi*integral_0^w p_sigma(it) dt,
    E_sigma(w) = 4*integral_0^w t R_sigma(t) dt,
    b_sigma(w) = E_sigma(w)+O_sigma(w).

The integrals defining the primitives are path independent. R_sigma
and E_sigma are entire even functions, O_sigma is entire odd, and
b_sigma(0)=0. For real w>0,

    b_sigma(w)=B_sigma(w^2).

Thus F(w)=sum_j a_j exp(-b_sigma_j(w)) is an entire lift of the
positive-real Laplace transform of nu. If nu>=0, the following are
equivalent:

1. integral exp(cu) dnu(u)<infinity for some c>0.
2. F is even on C.
3. J(w):=sum_j a_j exp(-E_sigma_j(w))*sinh(O_sigma_j(w)) is
   identically zero on C.
4. integral exp(cu) dnu(u)<infinity for every c>0.

This treats every order of cancellation, including cancellation of
the leading square-root term. For example, set

    c_sigma = 2*pi*p_sigma(0),
    e_sigma = 2*integral_0^infinity
                  (p_sigma(x)-p_sigma(0))/x^2 dx,
    d_sigma = -pi*p_sigma''(0)/3.

The integrals are absolutely convergent. The first two necessary
odd-coefficient identities are

    sum_j a_j c_sigma_j = 0,
    sum_j a_j (d_sigma_j+c_sigma_j^3/6-e_sigma_j*c_sigma_j) = 0.

Neither identity, nor any finite truncation of J, is claimed to be
sufficient. No independence of these first two scalar constraints
as functions of the widths is asserted.

In addition, the 2r zero-free entire functions
exp(-b_sigma_j(w)) and exp(-b_sigma_j(-w)) are pairwise
nonproportional. This is pairwise separation only: this corollary
does **not** infer their linear independence, exclude J identically
zero, construct a positive combination, or settle the finite-law
question. It establishes no actual-Xi all-degree sign or transfer.

## Proof

### Source inputs and the difference that needs proof

C032j imports the laws and H(t)>0. The additional analytic formulas
used here are from Suvrit Sra, *Some positivity properties of Riemann
Xi under smoothing*, fixed [2611.00345v1, 11 November 2026](https://hexagonmath.org/pdf/2611.00345v1):
Lemma A.4 and its proof, printed p.13, give the entire profile and
real-axis growth; the proof of Proposition A.8, printed p.17, gives

    B_sigma'(s)=2*integral_0^infinity p_sigma(x)/(s+x^2) dx,
    s>0,

absolutely convergently. Proposition 3.1, (3.2), printed pp.5-6
(proof p.21), gives

    H_sigma(t)=H(t/(1+4*sigma*t))/sqrt(1+4*sigma*t).

The finite-zero inputs and normal convergence for H are recorded in
Sra, *On some positivity properties of the Riemann Xi function*,
fixed [2610.00584v1, 20 October 2026](https://hexagonmath.org/pdf/2610.00584v1),
Section 2.1/(2.3), printed p.3, and Lemma 2.1 with proof, printed p.4.
The positivity theorem is Theorem 1.1, printed p.2, already imported
in C032j. The first-zero enclosure and counting inputs remain source
imports; this is not an independent numerical verification.

The source's leading cusp alone does not cover signed cancellation.
We therefore prove the entire lift and full cancellation condition,
rather than reprove the individual-law moment obstruction.

### 1. Removal of all apparent singularities in R_sigma

Temporarily write p=p_sigma. Since p is even entire, there is an
entire h with p(z)=h(z^2). For x>=0 the integrand is

    (h(x^2)-h(-w^2))/(x^2-(-w^2)).

At x^2=-w^2 it has its removable value h'(x^2). More explicitly it
equals

    integral_0^1 h'(-w^2+v*(x^2+w^2)) dv.

This expression is entire in w and continuous jointly in x,w.
For w in a compact disk |w|<=M and x in a bounded interval it is
uniformly bounded, including x=w=0. For x>=2M+1 the denominator has
modulus at least 3*x^2/4. Logarithmic growth of p(x), together with
boundedness of p(iw) on that compact disk, bounds the integrand by

    C_M*(1+log(x+2))/x^2.

This bound is integrable on the tail. Consequently the defining
integral converges absolutely and locally uniformly in w. The
holomorphic-parameter integral theorem (equivalently, dominated
Morera followed by continuity) makes R_sigma entire. Its expression
is unchanged under w -> -w, so it is even. The entire primitives
defining E_sigma and O_sigma exist on the simply connected plane.
Their derivatives and their values at zero give the stated parities.

For real w>0 the cited Stieltjes formula and the elementary integral
integral_0^infinity dx/(x^2+w^2)=pi/(2w) give

    d/dw B_sigma(w^2)
      =4w*integral_0^infinity p_sigma(x)/(x^2+w^2) dx
      =4w R_sigma(w)+2*pi*p_sigma(iw)
      =b_sigma'(w).

All terms are absolutely integrable; subtracting the constant
p_sigma(iw) is legitimate here. Both B_sigma(w^2) and b_sigma(w)
tend to zero as w decreases to zero, so their equality follows.
Only this positive-ray identity is needed; no unproved branch
choice for B_sigma off that ray is assumed.

### 2. Exact cancellation and positive moments

The finite signed measure has finite total variation, at most
sum_j |a_j|. Thus for s>0 its bounded Laplace integrals give

    integral exp(-su) dnu(u)=F(sqrt(s)).

Assume first nu>=0 and condition 1. It is a probability measure by
its mass. The exponential-moment holomorphy theorem applies: see
Jean-Baptiste Boyer, *The speed of convergence in the renewal
theorem*, [19 June 2015 manuscript](https://maths.jbboyer.fr/documents/articles/renewal.pdf),
Definition 2.1 and Lemma 2.2 with proof, printed p.6. Since the
support is nonnegative, the positive exponential moment is the
absolute exponential moment in that lemma. With Fourier-Laplace
variable chosen as -s it gives a holomorphic f(s) near zero that
agrees with the displayed Laplace transform for positive s. There
are no renewal or drift hypotheses in that lemma.

For small positive w, F(w)=f(w^2). Both sides are holomorphic on a
disk about zero, so the identity theorem gives equality throughout
that disk. Hence F is even there and, being entire, even everywhere.
This proves 1 implies 2. Direct subtraction gives

    F(w)-F(-w)=-2*J(w),

so 2 and 3 are equivalent.

Conversely assume nu>=0 and F even. Its entire Taylor series has
only even coefficients. Replacing w^(2n) by s^n defines an entire
function f(s): for any radius A, Cauchy's bounds for F on a circle
of radius greater than sqrt(A) give convergence on |s|<=A. This f
agrees with the Laplace transform of nu for s>0.

For each integer n>=0 and real s>0 differentiation under that
Laplace integral is justified by bounding u^n exp(-s*u) on a
smaller positive-s neighborhood. Therefore

    (-1)^n f^(n)(s)=integral u^n exp(-s*u) dnu(u).

Let s decrease to zero. Positivity of nu and monotone convergence,
and continuity of f^(n) at zero, show

    m_n:=integral u^n dnu(u)=(-1)^n f^(n)(0)<infinity.

For any c>0 the entire Taylor series at -c and monotone convergence
of the nonnegative exponential series then give

    integral exp(cu) dnu(u)
      =sum_(n>=0) c^n*m_n/n!
      =f(-c)<infinity.

Thus 2 implies 4; 4 implies 1 immediately. This argument never
subtracts divergent moments of the separate nu_sigma. Positivity
is essential to the two monotone-convergence steps; the assertion
is not being extended to arbitrary signed measures.

To check the displayed finite-order conditions, entire Taylor
expansion yields

    O_sigma(w)=c_sigma*w+d_sigma*w^3+O(w^5),
    E_sigma(w)=e_sigma*w^2+O(w^4),
    exp(-E_sigma(w))*sinh(O_sigma(w))
      =c_sigma*w+(d_sigma+c_sigma^3/6-e_sigma*c_sigma)*w^3+O(w^5).

The integral for e_sigma is R_sigma(0) times two. Its convergence
also follows directly from p_sigma(x)-p_sigma(0)=O(x^2) at zero
and logarithmic growth at infinity. Vanishing of J forces both
coefficients to vanish, and similarly every subsequent odd
coefficient. This includes, rather than discards, the case in
which the first coefficient is zero.

### 3. Distinct widths give distinct normalized exponentials

First prove p_sigma and p_tau cannot be identical when 0<sigma<tau.
Otherwise their absolutely convergent heat integrals coincide for
every t>0. Put d=tau-sigma>0 and substitute
u=t/(1+4*sigma*t) in the cited exact transformation. Cancelling
the common factor sqrt(1-4*sigma*u) gives

    H(u)=H(u/(1+4*d*u))/sqrt(1+4*d*u),
    0<u<1/(4*sigma).

H is holomorphic on Re(u)>0 by the cited normal convergence.
The map u/(1+4*d*u) preserves that half-plane, since its real
part is (Re(u)+4*d*|u|^2)/|1+4*d*u|^2>0. The square root has its
holomorphic branch positive on the positive real axis. Both sides
are therefore holomorphic on the connected right half-plane; the
identity theorem extends this equality to every real u>0.

Write a_rho=Re(z_rho^2)=gamma_rho^2-delta_rho^2. The imported
first-zero enclosure and strip give a_rho>195. Let
C=sum_rho exp(-a_rho)<infinity, by zero counting. For u>=1,

    |H(u)|<=sum_rho exp(-u*a_rho)<=C*exp(-195*(u-1)).

After multiplying the preceding identity by sqrt(1+4*d*u), its
left side tends to zero as u tends to infinity, whereas its right
side tends to H(1/(4*d))>0 by C032j's positivity input. This is a
contradiction. Thus distinct widths have distinct entire profiles.

If b_sigma(w)=b_tau(w), taking odd parts and differentiating gives
p_sigma(iw)=p_tau(iw), contradicting what was just proved.
If b_sigma(w)=b_tau(-w), derivatives at zero would instead give
2*pi*p_sigma(0)=-2*pi*p_tau(0), impossible because both values
are positive. Reflection handles the two negative-argument cases.
Consequently the 2r normalized exponents b_sigma_j(plus-or-minus w)
are pairwise distinct. All vanish at zero.

Finally, if two of their exponentials were proportional, evaluating
at zero would make the proportionality constant one. The difference
of their exponents would then take values in the discrete set
2*pi*i*Z; continuity on C makes it constant, and its value at zero
makes it zero. This contradicts their pairwise distinction.

At completion of step1300, the remaining question was a finite linear relation among these
zero-free entire functions, namely F(w)-F(-w)=0. Pairwise
nonproportionality alone is not used as a linear-independence
theorem here. At that step, a general theorem on such relations had not
been source-assessed or imported. The finite-mixture exclusion was
therefore left open, correctly. No RH criterion has been proved. The
source preprints retain the qualifications in C032j.

### Critical audit1302, 17 November 2026

The three analytic claims above survive a conceptual audit under the
stated source inputs. This audit is not a manuscript-wide verification
of either preprint. The full difference quotient is used, including
the removable points w=+/-ix and x=w=0. Its compact-interval bound
comes from h' on a compact set; its separate tail bound comes from
|x^2+w^2|>=x^2-|w|^2>=3*x^2/4 for x>=2M+1. Thus the locally
uniform absolute convergence is valid on every complex compact set,
not just near the positive ray. Both primitives are globally entire.
The constant in the positive-ray identity is fixed by B_sigma(0)=0,
which is part of the source probability-law construction.

In the converse moment argument, differentiation is on s>0, where
u^n exp(-s*u) is bounded uniformly on a smaller real neighborhood.
For n=0 as well as n>0, monotone convergence at s=0 uses nu>=0.
Cauchy's estimate for an even entire F at a radius R>sqrt(A) bounds
its coefficient of w^(2n) by M_R/R^(2n), so the substituted series
for f has infinite radius. Its Taylor series at -c really converges
for every c>0. The signs (-1)^n in the derivative formula then give
the nonnegative moment series. There is no signed-moment subtraction
and no implication from mere smoothness at zero.

For clarity, the half-plane normal convergence needed in the
separation argument also follows directly from the retained zero
inputs. Write u=v+iy with v>=epsilon>0, v<=V and |y|<=M on a compact
subset of Re(u)>0, and z_rho=gamma_rho-i*delta_rho. Then

    |exp(-u*z_rho^2)|
      <=exp(-epsilon*gamma_rho^2+V/4+M*gamma_rho).

Zero counting, including multiplicity, makes this majorant summable.
The transformed argument u/(1+4d*u) stays in that half-plane, and
1+4d*u has real part greater than one, fixing the positive-real
square-root branch without a cut crossing. The identity theorem
therefore does extend the equality from the original real interval
to every positive u. The bound a_rho>195 is weaker than the actual
consequence gamma_rho^2-delta_rho^2>196-1/4; C is finite by the same
counting bound. Exponential decay times sqrt(1+4d*u) tends to zero,
whereas continuity at 1/(4d) and the imported strict H positivity
give a strictly positive other limit. Every sigma<tau is covered.

Same-orientation pairs are separated by this argument; opposite
orientations, including the same width, are separated by the strict
sign of b_sigma'(0). Reflection covers the remaining same-orientation
case. Normalization at zero eliminates nonzero constant exponent
differences and proportional exponential pairs. Pairwise distinction
is still not itself used as linear independence in this proof.
The separate classical-theorem application is C032l; it is not an
input to this audit or to any assertion proved in C032k.

## Mathlib

Full matching coverage has not been checked and is unknown. No
Mathlib theorem is imported. General entire-function, dominated
integral and probability APIs are not asserted to cover the complete
lift, distinct-width separation, or the general dependence theorem.
