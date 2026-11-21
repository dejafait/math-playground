# Corollary C028a: variance-matched Hermite Schmeisser budget stop

## Hypotheses

Use the actual completion Xi of L018 and moments M_(2j) of L021. Set

    gamma_j=j! M_(2j)/(2j)!,    b_j=gamma_j/gamma_0,
    R_d(x)=sum_(j=0)^d binom(d,j) gamma_j x^(d-j),
    P_d(x)=R_d(x)/gamma_0,

for integers d>=3. Let S_k be the absolutely convergent real reciprocal
zero sums of L025. L027 gives S_2>0 and S_3>0 unconditionally. No RH,
Laguerre-Polya membership or root-reality hypothesis is imposed.

Put v=b_1^2-b_2. Use the monic Hermite orthogonal system H_n for the
Gaussian probability measure of mean -b_1 and variance v, and write

    P_d=sum_(nu=0)^d a_nu H_nu,    h_nu=integral H_nu(x)^2 dmu(x).

Define the source statistic

    kappa=Im(a_(d-1)/a_d),
    I(P_d)^2=kappa^2+sum_(nu=0)^(d-2)
                       (h_nu/h_(d-1)) |a_nu/a_d|^2.

This is Schmeisser's coefficient statistic for this specified basis,
not an actual root-height statistic or an infimum over reference measures.

## Conclusion

The measure is well defined: v=S_2>0. Its monic Hermite basis matches
the first two coefficients below the leading term of P_d. Precisely,

    a_d=1,    a_(d-1)=a_(d-2)=0,
    a_(d-3)=2 binom(d,3) S_3,
    h_n=n! S_2^n.

Consequently, for every integer d>=3,

    I(P_d)^2 >= (S_3^2/(9S_2^2)) d^2(d-1)(d-2),
    I(P_d)/d >= (S_3/(3S_2)) sqrt((d-1)(d-2)) -> infinity.

In particular I(P_d) is not o(d); it is bounded below by a positive
constant times d^2 for all sufficiently large d. This stops the proposed
sublinear Schmeisser budget in this mean- and variance-matched Hermite
basis. It does not lower-bound actual imaginary root heights, produce
a nonreal actual root, or decide hyperbolicity or RH. Other reference
measures and other methods are outside the conclusion.

## Proof

### Imported coefficient-height interface

Gerhard Schmeisser, *Estimates for the Imaginary Parts of the Zeros of
a Polynomial*, Mathematica Balkanica **16** (2002), 203-217,
[definitions pp.203-204 and Theorem 1, (2.1)-(2.2), pp.205-206](https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf),
defines I exactly as above for a monic orthogonal basis of a positive
real measure with all moments, and a degree-d polynomial with a_d!=0.
The source denotes the norm squares by gamma_nu; h_nu here avoids
confusion with the actual xi coefficients. For a nondecreasing convex
function phi on [0,infinity) with phi(0)=0, and c=-t*kappa with
0<=t<=1/2, its (2.2) bounds the sum of the k largest
phi(|Im z_j-c|), for 2<=k<=d, by

    phi((I+|kappa+2c|)/2)+phi((I-|kappa+2c|)/2)
        +(k-2)phi(|c|).

Roots count multiplicities. Here all expansion coefficients are real,
kappa=0, and c=0 is admissible. With k=d and phi(u)=u the imported
theorem yields sum_j |Im z_j|<=I(P_d). The Gaussian measure below has
positive density on R and all moments, so all orthogonal norms are
positive. No root hypotheses are needed for this application.

The theorem and its complete relevant proof, pp.211-214, were inspected
in source review1493 and reused in review1496. No part of that theorem
is reproved here. What needs checking is its actual-series coefficient
and norm specialization; these determine whether the resulting upper
bound can have the proposed size. A large upper bound does not force
large actual heights.

### Actual cubic mismatch

By L021 and gamma_0=M_0>0, the entire even expansion defines

    F(w)=sum_(j>=0) b_j w^j/j!,    F(-z^2)=Xi(z)/M_0.

L025 proves, on a zero-free disk about zero, an absolutely locally
uniformly convergent normalized logarithm

    log(Xi(z)/M_0)=-sum_(k>=1) S_k z^(2k)/k.

Substituting z^2=-w into these convergent even series gives, on a
sufficiently small w-disk, the normalized logarithm of F:

    log F(w)=S_1 w-S_2 w^2/2+S_3 w^3/3+O(w^4).

The substitution uses the even series, hence no square-root branch or
global logarithm assumption. Direct expansion at F(0)=1 also gives

    log F(w)=b_1 w+(b_2-b_1^2)w^2/2
               +(b_3-3b_1 b_2+2b_1^3)w^3/6+O(w^4).

Thus

    v=b_1^2-b_2=S_2>0,
    b_3-3b_1 b_2+2b_1^3=2S_3>0,

where the strict signs are L027, not numerical approximations or an
RH premise. This extracts only the cubic coefficient of L025's existing
logarithm, rather than introducing a new logarithmic representation.

### Gaussian normalization and triangular matching

Let mu have density

    (2 pi v)^(-1/2) exp(-(x+b_1)^2/(2v)).

Specify the monic Hermite normalization by

    exp((x+b_1)t-vt^2/2)=sum_(n>=0) H_n(x)t^n/n!.

The following short generating-function check fixes all translation,
variance and norm factors; it is not a new general orthogonal-polynomial
theorem. Completing the Gaussian square gives

    integral exp(u(x+b_1)) dmu(x)=exp(vu^2/2).

For bounded complex u, the integrands and their derivatives are dominated
by a polynomial times exp(C|x+b_1|) times the Gaussian density, which is
integrable. Coefficient comparison under these integrals is therefore
justified. In particular, multiplying the two generating functions and
integrating gives

    integral exp((x+b_1)s-vs^2/2)
             exp((x+b_1)t-vt^2/2) dmu(x)=exp(vst).

Comparing s^n t^m coefficients proves orthogonality for n!=m and
h_n=n!v^n. The generating function also gives the finite formula

    H_n(x)=n! sum_(r=0)^floor(n/2)
                 (-v/2)^r (x+b_1)^(n-2r)/(r!(n-2r)!).

For n>=3 its top four terms are

    x^n+n b_1 x^(n-1)+binom(n,2)(b_1^2-v)x^(n-2)
       +binom(n,3)(b_1^3-3b_1 v)x^(n-3).

Terms of lower degree, if any, are irrelevant to this coefficient check.
For d=3 there are no omitted lower terms in this formula. Since the
top terms of P_d are

    x^d+d b_1 x^(d-1)+binom(d,2)b_2 x^(d-2)
       +binom(d,3)b_3 x^(d-3),

triangular expansion in the monic H_n gives a_d=1 and
a_(d-1)=a_(d-2)=0. At the next degree it gives

    a_(d-3)=binom(d,3)(b_3-b_1^3+3b_1 v)
            =binom(d,3)(b_3-3b_1 b_2+2b_1^3)
            =2 binom(d,3)S_3.

Within translated/scaled Gaussian monic Hermite systems, the first
coefficient forces the mean -b_1 and the second forces variance v.
Thus there is no unused Gaussian mean or variance parameter in this
specified matching procedure.

### Retained nonnegative term and stopping threshold

Here kappa=0. The nu=d-3 term is present even at d=3, and every summand
in I^2 is nonnegative. The exact norm ratio is

    h_(d-3)/h_(d-1)=1/((d-1)(d-2)v^2).

Consequently

    I(P_d)^2 >= [4 binom(d,3)^2 S_3^2]
                    /[(d-1)(d-2)S_2^2]
              = (S_3^2/(9S_2^2))d^2(d-1)(d-2).

Taking nonnegative square roots and dividing by d proves the claim.
The factor S_3/(3S_2) is a fixed strictly positive actual-Xi constant,
independent of d; its numerical size is immaterial to divergence.
No higher coefficient can cancel this squared summand. The stipulated
abandonment test is met, so no full-norm or higher-order sweep is needed.

This concerns the unchanged actual R_d. L763 instead changes the input
series by a Gaussian product and tests a sufficient Turan criterion;
L764 tests signs at a prescribed grid for that changed series. Neither
is an input to the argument above. Inverting the roots to the ordinary
Jensen plane and obtaining all-degree signs remain independent gaps.

### Independent finite audit1499 (2026-11-18)

Under assessment1497, the normalization, local logarithm, norm factors
and inequality direction were independently replayed. No correction to
the statement or its mathematical inputs was needed. In moment notation,

    b_1=M_2/(2M_0), b_2=M_4/(12M_0), b_3=M_6/(120M_0).

Thus b_1^2-b_2 agrees exactly with L025's S_2, rather than twice S_2
or a raw-moment variance. In the locally convergent logarithm, replacing
z^(2k) by (-w)^k gives signs +,-,+ for k=1,2,3. In particular the cubic
exponential-series coefficient is
(b_3-3b_1*b_2+2b_1^3)/6=S_3/3. L027 supplies strict positivity
of both S_2 and S_3 without RH; its argument uses the elementary
rectangle and strip localization, not a real-zero assumption.

For the Gaussian integral above, the coefficient of s^n*t^m in
exp(v*s*t) vanishes unless n=m and is v^n/n! when n=m. Multiplication
by n!*m! therefore gives h_n=n!*v^n. Since the two preceding residual
coefficients vanish, no H_(d-1) or H_(d-2) term contributes to the
coefficient of x^(d-3). Division of (d-3)!*v^(d-3) by
(d-1)!*v^(d-1) gives precisely the norm ratio in the proof. The index
d-3 lies in [0,d-2] for every d>=3, so the retained square is present
throughout the stated range.

At the endpoint d=3 the complete expansion, with no lower residuals, is

    P_3=H_3+2S_3*H_0,  h_0=1, h_2=2v^2,
    I(P_3)^2=2S_3^2/v^2.

This equals the displayed general lower bound at d=3. For larger d,
additional summands are nonnegative and cannot decrease it. Since v
and S_3 are fixed positive constants, the displayed lower bound gives
I(P_d)/d tending to infinity, whereas the proposed budget requires
I(P_d)/d tending to zero. Schmeisser's Corollary 1, p.206 (or the
stated Theorem 1 specialization), supplies only
sum_j |Im z_j|<=I(P_d). A lower bound on its right side supplies no
lower bound on its left side. The bound-only stop survives the audit;
no actual root-height, hyperbolicity or reciprocal-transfer claim is
established. This is verification of the existing specialization,
not a stronger theorem or a new discovery beyond the cited method.

## Mathlib

Not checked. Availability of a full matching theorem in Mathlib is
unknown. No formal verification is claimed. The complete elementary
specialization and analytic interchange justification are given above;
Schmeisser's general theorem is imported by its precise citation.
