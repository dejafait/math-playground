# Corollary 919j: positive decreasing heat trace with a negative mixed witness

## Hypotheses

Use exactly the five multiplicity-one opposite-class representatives
of C919i:

    alpha=(57/4,21,25,101+i/4,101-i/4),
    beta_j=alpha_j^(-2), H(t)=sum_(j=1)^5 exp(-t alpha_j^2), t>0.

Both conjugate representatives are included once. This is a finite
model, not the actual Xi zero multiset. For real polynomials define

    Q(q)=sum_(j=1)^5 beta_j^2 q(beta_j)^2,
    P(X)=product_(j=1)^3 (X-beta_j).

Squares in Q are algebraic. Import C919i's independently accepted
step2206 result under its stated correct CPython integer/Fraction
execution assumption for the exact negative witness. The heat-sign
proof below is analytic and has no computational assumption.
No actual-zero census, Xi realization, infinite-tail estimate or
positive representing measure is assumed.

## Conclusion

For every real t>0, H(t)>0 and -H'(t)>0. For this same unchanged
model, C919i also gives H_(2,r)>0 for every integer r>=4, whereas
Q(X^158 P)<0, with precisely its arithmetic qualification above.

Consequently these two strict scalar heat signs, even together with
the stated all-shift degree-two signs, do not imply all-degree mixed
positivity for general models in this class. This does not refute an
actual-Xi-specific implication or RH. The independent step2210 audit
below accepts the heat calculation under these unchanged hypotheses.

## Proof

### Method coverage and exact finite specialization

Reuse the inspected phase-delay/retained-real-exponential method in
Suvrit Sra, *On some positivity properties of the Riemann Xi function*,
fixed first release20October2026, hexagon:2610.00584v1,
Section2.1/(2.1)-(2.3) pp3-4, complete Lemma2.2 and proof p4:
https://hexagonmath.org/pdf/2610.00584v1 . The completed1341 and2207
source assessments read the relevant short-phase and decay cases.
The source's actual-zero and counting hypotheses are not asserted
for this finite polynomial. Its theorem cannot be directly applied.
The necessary specialization is to pay exactly two conjugate terms
using one real term, including the additional derivative factor.
We give those model-specific constants and both time regimes below;
no general source theorem is reproved or imported with altered premises.
This is a known-method specialization classified REPRODUCTION, with
no originality or progress beyond the checked source methods claimed.

Put

    q=(57/4)^2=3249/16,
    a=101^2-(1/4)^2=163215/16, b=2*101/4=101/2.

Then (101+i/4)^2=a+ib and its conjugate square is a-ib.
Conjugation and Euler's formula give the real identity

    H(t)=exp(-qt)+exp(-441t)+exp(-625t)
           +2 exp(-at) cos(bt).                         (1)

All sums are finite, so termwise differentiation is valid everywhere.
In particular

    -H'(t)=q exp(-qt)+441 exp(-441t)+625 exp(-625t)
             +2 exp(-at)(a cos(bt)+b sin(bt)).           (2)

The plus sign before b sin(bt) follows by differentiating
exp(-at)cos(bt) and then taking its negative. Thus the derivative's
phase and full rate factor have not been dropped. All three real
rates, as well as a and b, are strictly positive.

### Small positive times

If 0<t<=1/100, then 0<bt<=101/200<1<pi/2. Hence cos(bt)>0
and sin(bt)>0. In (1) all real terms and the pair term are positive;
in (2) all real terms and the pair term are also positive. Thus both
required strict inequalities hold throughout this interval, including
the endpoint. There is no appeal to a sampled phase or a limiting
sign at zero.

### All remaining times

For t>=1/100 put x=(a-q)t. Direct rational subtraction yields

    a-q=79983/8,
    x>=79983/800>99.

For every positive x, the real exponential power series has positive
terms, so exp(x)>=1+x+x^2/2. Consequently

    exp(x)>1+99+99^2/2=10001/2>5000,
    exp(-x)<1/5000.                                    (3)

Using cos(bt)>=-1 in (1) and retaining just the first positive real
term gives

    H(t)>=exp(-qt)-2 exp(-at)
         =exp(-qt)(1-2 exp(-x))
         >(1-2/5000)exp(-qt)>0.                        (4)

For (2), the complete pair factor satisfies

    |a cos(bt)+b sin(bt)|<=a+b=164023/16,
    2(a+b)/q=328046/3249<101,

where the last strict inequality is the integer comparison
328046<101*3249=328149. Thus

    -H'(t)>=q exp(-qt)-2(a+b)exp(-at)
           =q exp(-qt)(1-[2(a+b)/q]exp(-x))
           >(1-101/5000)q exp(-qt)>0.                 (5)

The required thresholds in (4) and (5) are both1; their error ratios
are strictly below2/5000 and101/5000 respectively. Equations (3)-(5)
hold for every real t>=1/100, without a large-time cutoff or a uniform
positive lower bound as t tends to infinity. Together with the first
case they prove both signs for every positive time. By the mean value
theorem, -H'>0 also implies that H is strictly decreasing.

### Unchanged mixed obstruction and limits

The representatives, beta, multiplicities and P above are exactly
those of C919i. Therefore its accepted all-integer-r>=4 degree-two
positive definiteness and its prescribed negative Q(X^158 P) apply
without changing any hypothesis. Its negative rational certificate
is reused, not recalculated or inferred from these heat signs.
The all-time sign proof adds no assumption to that witness.

This supplies a single model possessing all the listed scalar and
degree-two properties while failing the stated higher-degree sign.
It rules out their sufficiency alone over this model class. It says
nothing against a mechanism that uses additional actual-Xi theta
structure. Complete monotonicity, higher derivative signs and actual
realization have neither been assumed nor proved. The main gap in
L030-L032/C032a remains open; no complete RH candidate is asserted.

### Independent analytic and scope audit, 21 November 2026 (step2210)

**Verdict.** Accepted without correction under the unchanged ready
SPECIALIZE assessment2208, separately approved2209. This is the first
independent audit of the finite heat calculation, classified
REPRODUCTION. It accepts a local known-method specialization and
does not claim a new result beyond the methods already inspected.

**Identities and short interval.** Squaring 101+i/4 gives
10201-1/16+i(101/2), exactly a+ib with the displayed positive a,b.
The other square is its conjugate; neither occurrence is omitted.
Their exponentials therefore sum to the real pair in (1).
Differentiating that pair and changing its sign gives
2 exp(-at)(a cos(bt)+b sin(bt)), exactly (2). In particular the
derivative's sine coefficient is positive, not negative or absent.
For 0<t<=1/100, its angle is in (0,101/200], contained strictly
in (0,pi/2). Both trigonometric factors and every real rate are
positive. This proves strict positivity of both sums throughout
the entire short interval, including its right endpoint.

**Decay interval and exact margins.** Independently subtracting the
rates gives (163215-3249)/16=79983/8. Thus for t>=1/100,
x>=79983/800>99, since 79983>79200. The exponential series has
nonnegative terms at x>0, so

    exp(x)>=1+x+x^2/2>1+99+9801/2=10001/2>5000.

Hence exp(-x)<1/5000, uniformly on this interval. The triangle
inequality bounds the derivative pair by a+b because a,b>0 and
|cos|,|sin|<=1. Direct addition gives
a+b=(163215+808)/16=164023/16. Its relative coefficient is
328046/3249<101; the positive cross-product difference is
328149-328046=103. Discarding the other two positive real terms
is valid in both lower bounds. Consequently (4) and (5) yield

    H(t)>(2499/2500) exp(-qt)>0,
    -H'(t)>(4899/5000) q exp(-qt)>0.

The error ratios are strictly below 2/5000 and 101/5000, respectively;
the required threshold is 1 in each case. The two intervals overlap
at 1/100 and exhaust every positive real t. All differentiation is
of finite sums; the exponential factors remain positive at every
finite t even though the lower bounds tend to zero as t grows.
The mean value theorem therefore gives strict decrease on (0,infinity).
No sampling, numerical exponential bound or limit interchange is used.

**Imported witness and scope.** Compared the hypotheses, conclusion,
finite normalization and accepted2206 audit of C919i with the model
here. The five alpha values, multiplicity one for both conjugates,
beta=alpha^(-2), algebraic-square Q, monic P, integer range r>=4
and prescribed witness exponent158 coincide exactly. Thus its
positive-definite degree-two matrices and negative Q(X^158 P)
are applicable without new hypotheses or parameter choices. The
negative witness retains C919i's correct CPython integer/Fraction
execution assumption; its certificate was neither rerun nor used
to prove the analytic heat signs. No witness search or arithmetic
replay was performed. The analytic audit needs no such execution
assumption. Positivity of these two scalar heat sums does not assert
complete monotonicity, a positive reciprocal-node measure, actual-Xi
realization or all-degree mixed positivity. The generic sufficiency
limitation is accepted with precisely that arithmetic qualification.

The argument and sole direct mathematical input C919i are unchanged;
no DAG change or new lemma is needed. Full matching Mathlib coverage
remains unchecked, as qualified below.

## Mathlib

Full matching coverage for this frozen model has not been checked.
Supporting exponential, trigonometric and finite differentiation
coverage has not been looked up for this step. The precise primary
source above supplies method coverage, not a matching Mathlib theorem.
Unknown coverage is not a claim of absence; this is an informal proof.
