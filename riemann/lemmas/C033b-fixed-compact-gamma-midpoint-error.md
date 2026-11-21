# Corollary C033b: fixed compact gamma midpoint error

## Hypotheses

Let sigma be real in [1,2] and w complex with |w|<=2. Use C033a's
ordinary gamma integrand, including its endpoint value:

    I(v)=exp(-sigma*v^2-v/2)*(cosh(w*v)-1)
                       /[v*(1-exp(-2*v))], v>0,
    I(0)=w^2/4.                                           (1)

Fix n=4096, h=16/n=1/256 and v_j=(j+1/2)*h, j=0,...,4095.
All function values in the midpoint sum below are exact complex values.
The parameter set, interval [0,16] and panel count are not adjustable.

The compact analytic assertion needs no RH or zero coordinates. Its
use for the gamma term of the actual-divisor formula retains C032z's
normalization, multiplicities, no-ordinate-zero, strip and counting
qualifications as carried by C033a. Probability-law use also retains
C032j/m/q's finite-zero, heat and fixed-v1 qualifications. None of those
external source data is independently verified here.

Import the composite midpoint remainder from Erik Talvila and Matthew
Wiersma, *Simple derivation of basic quadrature formulas*,
[arXiv:1202.0249v1](https://arxiv.org/pdf/1202.0249v1), 1 February 2012,
Section 1, printed p.2, equation (1.1) and following composite formula;
Section 4, printed p.8, supplies its proof. For f in C^2([a,b]),

    |integral_a^b f(t)dt - (b-a)/n*sum_j f(midpoint_j)|
             <= (b-a)^3*sup_[a,b]|f''|/(24*n^2).          (2)

For the precise complex-valued applicability use Douglas N. Arnold,
*A Concise Introduction to Numerical Analysis*, copyright 1999-2001,
[author's notes](https://www-users.cse.umn.edu/~arnold/597.00-01/nabook.pdf),
Chapter 2, Section 2, printed pp.58-59 (PDF pp.64-65), equations
(2.3)-(2.5) and their integral-kernel proof. On each panel [l,r], its
nonnegative kernel is (t-l)^2/2 on the left half and (r-t)^2/2 on the
right half. Its integral is (r-l)^3/24. The error identity integrates
f'' against that kernel. Apply the identity to the real and imaginary
parts and take the complex modulus under the integral to obtain (2)
with the same constant. No common complex mean-value point is used.
These generic results and proof cases were inspected in source-notes1612
and rechecked in recovery1613; they are reused, not reproved here.

## Conclusion

The family (1) is C^2 on [0,16], including its removable origin, and

    sup_(v in [0,16], sigma in [1,2], |w|<=2) |I''(v)|
                       <=1139.                           (3)

Consequently the prescribed finite mathematical sum satisfies

    sup_(sigma in [1,2], |w|<=2)
      |integral_0^16 I(v)dv - h*sum_(j=0)^4095 I(v_j)|
                 <=1139/98304 < 1/16.                   (4)

The sufficient derivative threshold for (2) to give error <1/16
is 6144; (3) meets it without changing the rule or parameter set.
This is a local effective specialization/reproduction of the cited
remainder under assessment1611, not a claim of discovery beyond the
sources checked. Separate critical audit1616 below validates this
statement without correction; no further evaluator claim is added.

Only the compact quadrature error for exact nodes is established.
C033a's already audited tail remains a separate allowance. Node
arithmetic, pole/prime/O errors, coefficient amplification and the
actual variation-2 residual <1/2 remain unpaid. No full cancellation,
signed upper control, unsmoothed Xi realization or actual-Xi
all-degree positivity follows.

## Proof

### 1. Regularity across the origin

Use the nonsingular expression in C033a's audited equation (14):

    A(v,w)=integral_0^1 (1-s)*cosh(s*w*v)ds,
    B(v)=integral_0^1 exp(-2*s*v)ds,
    R(v)=1/B(v), G(v)=exp(-sigma*v^2-v/2),
    I(v)=(w^2/2)*G(v)*A(v,w)*R(v).                       (5)

The compact s integrals may be differentiated in the real variable v
to every fixed order: on any bounded real v interval their integrands
and derivatives are continuous and uniformly bounded for |w|<=2.
Thus A,B and those derivatives are jointly continuous. For all real v,
B(v)>0, since its integrand is strictly positive; in particular the
reciprocal is smooth on a real neighborhood of [0,16]. The same holds
for G. Equation (5) agrees with (1) for v>0 and has value w^2/4 at0,
since A(0,w)=1/2 and B(0)=G(0)=1. It therefore gives a C^2 extension
through0, with jointly continuous first two derivatives on the full
compact parameter set. This includes w=0 without division by w.

### 2. Common product and reciprocal bounds

All estimates in this section hold for every real v>=0. From
exp(2*v)>=1+2*v, for v>0,

    B(v)=(1-exp(-2*v))/(2*v)>=1/(1+2*v).

The same inequality holds at0 by its value. Differentiating the compact
integral, and using 0<=s<=1, gives

    |B'(v)|<=2*B(v),  |B''(v)|<=4*B(v).

Hence, by the usual reciprocal derivative formulas,

    0<R(v)<=1+2*v,
    |R'(v)|=|B'(v)|/B(v)^2<=2*R(v),
    |R''(v)|=|2*B'(v)^2/B(v)^3-B''(v)/B(v)^2|
                                      <=12*R(v).         (6)

For complex z, |cosh z| and |sinh z| are at most exp(|z|), directly
from their two exponential terms. Differentiating A and using
|s*w|<=2 and integral_0^1(1-s)ds=1/2 therefore gives, for j=0,1,2,

    |partial_v^j A(v,w)|<=2^(j-1)*exp(2*v).               (7)

Put a=4*v+1/2. Since 1<=sigma<=2 and G(v)>0,

    |G'(v)|=(2*sigma*v+1/2)*G(v)<=a*G(v),
    |G''(v)|=|(2*sigma*v+1/2)^2-2*sigma|*G(v)
                                      <=(a^2+4)*G(v).   (8)

The six terms in the second derivative of GAR are G''AR, GA''R,
GAR'', 2G'A'R, 2G'AR' and 2GA'R'. Multiply their bounds by
|w|^2/2<=2 and use (6)-(8). Relative to the common factor
G(v)*R(v)*exp(2*v), their respective bounds are

    a^2+4,  4,  12,  4*a,  4*a,  8.

Their sum is a^2+8*a+28 = 16*v^2+36*v+129/4. Because sigma>=1,

    |I''(v)| <= (1+2*v)*(16*v^2+36*v+129/4)
                                *exp(-v^2+3*v/2)
       = (32*v^3+88*v^2+(201/2)*v+129/4)
                                *exp(-v^2+3*v/2).       (9)

All derivatives here are real-v derivatives; there is no positivity
assumption about the generally complex I or A. Equation (5) justifies
the same estimates at0 rather than using a singular quotient there.

### 3. A full-domain constant and the fixed-panel comparison

Completing a square gives

    -v^2+3*v/2 <= -v^2/2+9/8,

since the difference is (v-3/2)^2/2. For integer k>0, differentiating
v^k*exp(-v^2/2) on v>=0 shows its maximum occurs at sqrt(k) and
equals (k/e)^(k/2). The endpoint values give no larger maximum.
As e>2, this yields

    exp(-v^2/2)<=1,
    v*exp(-v^2/2)<=1,
    v^2*exp(-v^2/2)<=1,
    v^3*exp(-v^2/2)<=2.                                (10)

For the last bound, (3/e)^3 < (3/2)^3=27/8<4, then take the square
root. Also exp(9/8)<4: the exponential series gives e<3 and
exp(1/8)<=sum_(k>=0)(1/8)^k=8/7, so exp(9/8)<24/7<4.
For completeness e<3 follows from k!>=2^(k-1) for k>=2, with
strict inequality for k>=3, in the series for e.

Combine (9)-(10) to obtain the common bound

    |I''(v)| <= 4*(32*2+88+201/2+129/4)=1139,

valid in particular throughout [0,16] and on the entire parameter
set. This proves (3); no sampled maximum or decimal estimate is used.

The C^2 hypotheses of (2) have now been checked for each complex
member of the family, with a common modulus bound. Its fixed factor is

    16^3/(24*4096^2) = 2^12/(24*2^24) = 1/98304.

Thus (2) proves (4), since 98304/16=6144 and 1139<6144. The bound
is independent of sigma,w, so it also bounds the parameter supremum.
The w=0 member is identically zero and is included. This proof uses
exact values at precisely the stipulated 4096 midpoints and introduces
no rounding assertion, refinement, endpoint deletion or domain change.

### Critical audit1616 — 18 November2026

Under unchanged SPECIALIZE assessment1614, the separate audit accepts
(3)-(4) on exactly the stated closed domain and fixed rule. This is
REPRODUCTION: it verifies the local specialization, without a new
theorem beyond the cited sources, a node evaluator or an RH claim.
The generic midpoint theorem and its complete relevant integral-kernel
proof coverage are reused from assessment1614; no reproof or renewed
source retrieval is needed. The following is the full local replay.

**Endpoint and parameter regularity.** C033a(14) identifies I with
the expression (5) for v>0. For each derivative order through two,
the s-integrands of A and B and their v derivatives are continuous
and uniformly bounded on any compact real-v interval times the closed
w disk. Differentiation of these compact integrals is therefore valid,
with jointly continuous derivatives, including their parameter boundary.
The positive integrand defining B gives B(v)>0 for every real v.
In particular B(v)>=exp(-32)>0 on[0,16], and it stays positive on a
real neighborhood. Reciprocal differentiation is consequently valid
through the origin, without a one-sided quotient differentiation.
The smooth G factor also has jointly continuous v derivatives for
sigma in[1,2]. At0, A=1/2, R=G=1, so (5) has exactly the prescribed
w^2/4 value. It gives the required C^2 extension, including w=0,
the circle |w|=2 and both sigma endpoints. Uniform derivative claims
do not rely on separate singular factors in (1).

**Reciprocal and six-term replay.** For v>0, the elementary
exp(2v)>=1+2v gives exp(-2v)<=1/(1+2v), hence
B=(1-exp(-2v))/(2v)>=1/(1+2v). At0 this also holds.
Directly differentiating B gives B'=-2*integral_0^1 s*exp(-2sv)ds
and B''=4*integral_0^1 s^2*exp(-2sv)ds. Their moduli are at most
2B and4B for v>=0. Thus R'=-B'/B^2 and
R''=2(B')^2/B^3-B''/B^2 give precisely R<=1+2v,
|R'|<=2R, |R''|<=8R+4R=12R. No cancellation is assumed.
Each A derivative has a cosh or sinh factor with argument swv;
its modulus is at most exp(2v), while |sw|^j<=2^j and the
weight integral is1/2. This verifies all three bounds (7).
For G, its derivatives are -(2sigma*v+1/2)G and
[(2sigma*v+1/2)^2-2sigma]G. With a=4v+1/2 they give (8),
including sigma=1,2 and v=0.

The product rule gives exactly G''AR+GA''R+GAR''+
2G'A'R+2G'AR'+2GA'R'. After the outer |w|^2/2<=2,
their respective coefficients relative to G R exp(2v) are
a^2+4,4,12,4a,4a,8. All multiplicities and the A bound1/2
are included. The sum is a^2+8a+28=16v^2+36v+129/4.
Multiplication by1+2v gives32v^3+88v^2+(201/2)v+129/4.
Finally G*exp(2v)<=exp(-v^2+3v/2) uses sigma>=1.
This reproduces (9) for every v>=0, with complex modulus rather
than a sign claim about A, I or w^2.

**Global maximum and exact rule.** The square-completion slack is
(v-3/2)^2/2>=0, so the exponent comparison has the stated direction.
The maxima of v^k*exp(-v^2/2) are (k/e)^(k/2) for k=1,2,3.
Since e>2, they are bounded respectively by1,1,2: in the last
case (3/e)^3<27/8<4. The constant term is bounded by1.
The series bounds e<3 and exp(1/8)<=8/7 give
exp(9/8)<24/7<4. Consequently the full polynomial envelope is at most

    4*(64+88+201/2+129/4)=4*(1139/4)=1139.

This maximum argument covers all v>=0, hence the entire compact
integration interval; it is not a sampled parameter check.
The imported panel error identity has a real nonnegative kernel
of mass h^3/24. Applying it componentwise to complex I and then
using |integral K I''|<=integral K |I''| preserves the same1139
constant. No real or complex mean-value point is used. Summing
4096 panels of width1/256 gives factor
4096*(1/256)^3/24=1/98304, as also obtained from (2).
The required strict comparison is1139<98304/16=6144, with slack5005.
Thus the claimed error is indeed1139/98304<1/16 uniformly.
At w=0 both the integrand and its exact sum are zero; no division
by w or exclusion of this case occurs.

No statement or mathematical dependency changes in this audit:
C033a remains the sole direct local input. All divisor, multiplicity,
no-ordinate-zero, strip/counting and finite-zero/heat/fixed-v1
qualifications remain as stated in the hypotheses, rather than
being independently proved. Node rounding, tail recombination,
pole/prime/O evaluation, coefficient propagation, residual<1/2,
signed upper control and Xi realization remain unresolved. The audit
validates only this analytic compact-error component. It does not
reopen stops1586/1608 or certify any complete solution.

## Mathlib

Full matching coverage of this uniform gamma-family specialization and
fixed-panel bound has not been checked and is unknown. The precise
generic midpoint theorem and its complex-valued integral-kernel
application are cited above. Elementary differentiation, compact
integration and exponential estimates support the specialization;
no particular Mathlib theorem or formalization of the complete claim
is asserted. Unknown coverage is not evidence of absence.
