# Lemma 916: a full-theta inverse dilation score is not convex

## Hypotheses

Let K be L019's complete positive theta kernel, and fix lambda=1/40.
For x>0 set

    B(x)=log K(sqrt(x)),
    h(x)=-1-2x*(lambda+B'(x)).

For the global inverse use L915's independently proved shape estimate
h'(x)>19/10 on x>0 for 0<lambda<1/20. This part of L915 does not
assume a null contact, H2 positivity, any coordinate of c, or L914's
arithmetic contracts. Its named source input is George Csordas,
*Fourier transforms of positive definite kernels and the Riemann
xi-function*, arXiv:1309.0055v2 (21 February 2014), equation (4.2)
and Theorem 4.1, p.10, Theorem 4.2(b), p.11,
https://arxiv.org/pdf/1309.0055v2 . L915 checks the rescaling and the
origin slope bound. That source's original 1988 proof is not
independently audited here. No higher-derivative sign is imported.

## Conclusion

The global inverse H=h^(-1) on the open interval h((0,infinity)) is
smooth. At the exact interior point y0=h(1),

    h''(1)>50,             50<h'(1)<110,
    H''(y0)<-1/26620<0.

Thus H is not convex on its whole image. This rejects the nominated
global-convex sufficient comparison at this parameter. It does not
assert the existence of a null contact, prove or refute its flux
inequality, supply a reversed-order comparison, or resolve RH.
The independent proof audit in step190 below accepts this result,
with the stated named-source qualification retained.

## Proof

### Smoothness and the inverse-curvature formula

Write f(u)=log K(u). On a compact real neighborhood of any u>0,
L019's summands and their first three derivatives have bounds
C*(1+n^10)*exp(-c*n^2), where C,c>0 depend only on that neighborhood.
Indeed v_n=pi*n^2*exp(2u) is between fixed positive multiples of n^2;
each derivative has the form exp(u/2-v_n) times a polynomial of
degree at most five. The displayed bound is summable. Higher fixed
derivatives have analogous bounds. Hence termwise differentiation is
locally uniform, K is smooth and positive, and f is smooth.

With u=sqrt(x), the chain rule gives

    h(x)=-1-2lambda*u^2-u*f'(u),
    h'(x)=-2lambda-(f'(u)+u*f''(u))/(2u),
    h''(x)=(f'(u)-u*f''(u)-u^2*f'''(u))/(4u^3).       (1)

L915's global lower bound makes h strictly increasing; a continuous
strictly increasing function on an open interval has an open interval
as its image here, and its nonvanishing derivative gives a smooth
inverse at every point of that image. In particular y0=h(1) is an
interior point and

    H''(y0)=-h''(1)/(h'(1))^3.                        (2)

It remains to bound the actual full kernel derivatives in (1).

### Derivative polynomials and an entire-series relative tail

For each summand put v_n=pi*n^2*exp(2u). Then

    K_n(u)=exp(u/2-v_n)*p0(v_n),  p0(v)=8v^2-12v.

Differentiation replaces a polynomial p by

    Dp(v)=2v*p'(v)+(1/2-2v)*p(v).

The next three polynomials, in increasing powers of v, are

    p1(v)=-30v+60v^2-16v^3,
    p2(v)=-75v+330v^2-224v^3+32v^4,
    p3(v)=-(375/2)v+1635v^2-2116v^3+720v^4-64v^5.

Let C_j be the sum of the absolute coefficients of p_j. Explicitly,

    (C0,C1,C2,C3)=(20,106,661,9445/2).

For w>=1, |p_j(w)|<=C_j*w^(j+2).
At u=1 write v=pi*exp(2). The elementary bounds 3<pi<4,
exp(2)>sum_(k=0)^4 2^k/k!=7 and e<3 give

    21<v<36,      p0(v)>7v^2.                        (3)

For completeness e<3 follows from k!>=2^(k-1) for k>=1 with
strict inequality for some terms, by summing the geometric majorant.
The positive exponential series also gives

    exp(3)>sum_(k=0)^8 3^k/k!=89641/4480>20.           (4)

For n=2+k, k>=0, induction gives n<=2*(3/2)^k, and
n^2-1>=3+5k since their difference is k(k-1)>=0. Therefore for
m=4,6,8,10 the COMPLETE positive series satisfies

    sum_(n>=2) n^m exp(-v*(n^2-1))
      < 2^m*20^(-21)/(1-(3/2)^m*20^(-35))
      < 2^(m+1)*20^(-21).                            (5)

Here (3)-(4) bound exp(-3v)<exp(-63)<20^(-21) and
exp(-5v)<exp(-105)<20^(-35). Each geometric ratio in (5)
is less than 1/2, including the largest m=10.

Define, with derivatives evaluated at u=1,

    a_j=K_1^(j)/K_1,             j=1,2,3,
    t_j=(sum_(n>=2) K_n^(j))/K_1,    j=0,1,2,3,
    M_j=C_j*36^j/7,             j=1,2,3,
    E_j=C_j*36^j*2^(2j+5)/(7*20^21),  j=0,1,2,3.

Equations (3)-(5), after cancellation of exp(1/2-v), prove

    |a_j|<=M_j,    0<=t0<E0,    |t_j|<E_j (j=1,2,3).

No tail summand is dropped or assumed to have the sign of a head
derivative. Positivity of t0 uses only positivity of K_n itself.

### Logarithmic derivatives: paying for the relative denominator

Set q_j=K^(j)(1)/K(1). Then

    q_j=(a_j+t_j)/(1+t0),
    |q_j-a_j|<=d_j:=E_j+M_j*E0,       j=1,2,3.       (6)

The denominator is at least one, so (6) has the stated orientation.
Let f1=log K_1 and define positive rational bounds

    L1=d1,
    L2=d2+d1*(2M1+d1),
    L3=d3+3*(d2*M1+M2*d1+d2*d1)
             +2*d1*(3M1^2+3M1*d1+d1^2).

Using f'=q1, f''=q2-q1^2, f'''=q3-3q2*q1+2q1^3,
and the identical expressions in a_j for f1 gives

    |f^(j)(1)-f1^(j)(1)|<=Lj,          j=1,2,3.      (7)

For example, the product difference is bounded by
|q2*q1-a2*a1|<=d2*M1+M2*d1+d2*d1; the cubic difference is bounded
by d1*(3M1^2+3M1*d1+d1^2). Thus the error formula accounts for
both nonlinear products, not just the raw differentiated tails.

All quantities in (6)-(7) are explicit rational numbers. Their
values obey the loose, independently readable bounds

    M1<600, M2<130000, M3<32000000,
    E0<10^(-24), E1<10^(-21), E2<10^(-18), E3<10^(-15).

These imply d1<2*10^(-21), d2<2*10^(-18), d3<2*10^(-15),
and hence L1<2*10^(-21), L2<5*10^(-18), L3<2*10^(-14).
In particular

    L1+L2+L3<1/100.                                  (8)

The certificate below checks (8) directly from the exact rational
formulas, without using rounded values.

### A positive full-kernel curvature margin

For the first summand, at u=1 put d=2v-3>39. Direct logarithmic
differentiation of exp(u/2-v)*4v*(2v-3), with v'=2v, gives

    f1'=9/2+6/d-2v,
    f1''=-4v-24v/d^2,
    f1'''=-8v+48v*(2v+3)/d^3.

Consequently, using 21<v<36 and dropping only positive terms,

    f1'-f1''-f1'''
      =9/2+10v+6/d+24v/d^2-48v*(2v+3)/d^3
      >9/2+210-48*36*75/39^3
      =932913/4394>212.                              (9)

Equations (7)-(9) give f'-f''-f'''>212-1/100>200.
By (1), h''(1)>50 for the full kernel.

To bound h'(1), use

    f1'+f1''=9/2-6v+6/d-24v/d^2,
    A_lower=9/2-216-24*36/39^2 < f1'+f1'',
    f1'+f1'' < A_upper=9/2-126+6/39.

Since 2lambda=1/20, (1) and (7) imply

    -1/20-(A_upper+L1+L2)/2 < h'(1)
      < -1/20-(A_lower-L1-L2)/2.

The left bound exceeds 50 and the right bound is below 110;
(8) already suffices to check these coarse margins. Both inequalities
refer to K, not K_1. Inserting them and h''(1)>50 into (2) gives

    H''(y0)<-50/110^3=-1/26620.

A twice differentiable convex function has nonnegative second
derivative at every interior point, so H is not convex on its image.
The witness's exact ordinate may equivalently be written

    y0=-21/20-K'(1)/K(1).

No numerical approximation to that ordinate is needed.

### Certificate, correction and verification limits

Run `python3 scripts/heat/inverse-score-curvature-188.py`.
The complete certificate is `scripts/heat/inverse-score-curvature-188.json`;
all 14 exact checks pass. Its entire `bounds` and `checks` fields were
inspected with `../scripts/loop/inspect_json.py --pointer ... --full`.
They include every relative-tail/error bound and the required strict
curvature thresholds. There is no floating-point calculation.

The first run failed an incorrectly hand-entered expected p3 coefficient
list. Applying the displayed recurrence manually gives coefficients
-375/2,1635,-2116,720,-64, agreeing with the generated polynomial;
the expected list was corrected. The failed certificate is preserved
at `scripts/heat/inverse-score-curvature-188-first-pass.json`.
This correction changes the check, not the recurrence-generated bounds.

The script verifies finite algebra and rational inequalities. It does
not independently audit smoothness, the analytic majorization,
the Csordas input/L915 specialization, or the inverse-function argument.
Those arguments are written above and independently audited below.
The pre-existing EXPLORE assessment supplied limited coverage,
not a claim that this negative witness is original in the literature.
No conclusion beyond the tested comparison prerequisite is claimed.

### Independent proof audit — 9 November 2026, step190

The pre-existing SPECIALIZE assessment
`drafts/literature/2026-11-09-l916-full-theta-witness-audit.md`
authorizes this fixed-parameter audit. The full proof and program above,
L019's complete summand, L915's source-coordinate/origin/monotonicity
argument and its prior conceptual audit were read. The named Csordas
v2 theorem is reused at exactly its previously assessed scope; no new
source search or audit of its original 1988 proof is claimed.

1. With v'=2v the product rule gives exactly Dp=2v*p'+(1/2-2v)*p.
   In p3, multiplication of p2's coefficients by 2k+1/2 and addition
   of the shifted -2p2 coefficients gives, successively,
   -375/2, (9/2)*330+150=1635,
   (13/2)*(-224)-660=-2116, (17/2)*32+448=720, -64.
   Thus the preserved first-pass expected array was wrong; the
   recurrence-generated array and its corrected expectation agree.
   The coefficient absolute sums are exactly those displayed above.
   On every compact positive-u neighborhood, v_n lies between
   positive constant multiples of n^2. Degrees at most five through
   order three give the stated summable n^10 Gaussian majorant.
   The same argument for each higher fixed order proves smoothness;
   no complex entire extension of the kernel is needed or asserted.

2. At u=1, p0(v)/v^2=8-12/v>8-12/21=52/7>7.
   Dividing each tail summand by K1 therefore gives the absolute
   bound (C_j/7)*v^j*n^(2j+4)*exp(-v*(n^2-1)).
   The integer inequalities in (5) hold also at k=0,1: the first
   follows from successive ratios (n+1)/n<=3/2 for n>=2, and the
   second from k(k-1)>=0. The strict exponential estimates and
   geometric ratios less than 1/2 then give E_j for the complete
   n>=2 sum. The denominator 1+t0 is at least one because every
   original summand is positive, independently of derivative signs.
   Thus (6) is valid with absolute errors. The product and cubic
   expansions in (7) give precisely L2 and L3, without assuming
   that q1 or q2 has the head's sign. The displayed loose M/E bounds
   also hold by rational comparison; they give d1<1.6*10^(-21),
   d2<1.13*10^(-18), d3<1.032*10^(-15), hence the still looser
   stated d/L bounds. The exact sum in (8) is checked separately.

3. Direct differentiation of log K1=u/2-v+log4+log v+log(2v-3)
   verifies all three f1 derivative formulas. In (9) the positive
   6/d and 24v/d^2 terms are discarded only for a lower bound;
   the negative term has magnitude below 48*36*75/39^3.
   Its stated rational lower bound is 932913/4394>212.
   Paying L1+L2+L3<1/100 therefore gives h''(1)>50.
   For the first derivative, A_lower discards a positive term and
   enlarges the magnitude of the negative rational term, while
   A_upper discards that negative term. Multiplication by -1/2
   reverses both bounds exactly as displayed. The same error sum
   makes the resulting lower bound exceed 50 and upper bound
   fall below 110; both are bounds for the full K.

4. Differentiating h=-1-2lambda*u^2-u*f'(u), using
   d/dx=(2u)^(-1)d/du twice, verifies (1), including its minus
   sign in front of u^2*f'''. L915's contact-independent conclusion
   applies because 0<1/40<1/20, and gives h'>19/10 everywhere on
   (0,infinity). For any x in that interval there are x_-<x<x_+
   in the same interval, so the interval image contains a
   neighborhood of h(x). Thus its whole image is open, h is
   globally one-to-one and the local smooth inverses agree there.
   Differentiating h(H(y))=y gives H'=1/h'(H)>0 and
   H''=-h''(H)/(h'(H))^3. At y0=h(1), h''>50 and
   0<h'<110 give h''/(h')^3>50/110^3, with a strict reversal
   after negation. This proves the stated negative threshold at
   an interior point. No endpoint extension or contact existence
   is used. The expression y0=-21/20-K'(1)/K(1) has the correct
   factors and sign.

The unchanged rational program was replayed: 14/14 checks pass and
there are no failures. The complete `derivative_polynomials`,
`coefficient_absolute_sums`, `bounds`, `checks` and `summary` values
in its certificate, and the complete failed first-pass coefficient
check, were inspected using `../scripts/loop/inspect_json.py` with
selected pointers and `--full`. In particular no certificate preview
was substituted for the full error fractions or strict margins.
The program establishes finite arithmetic; points 1–4 supply the
independent analytic/domain/orientation review. No substantive defect
was found. The DAG's direct inputs L019 and L915 are sufficient;
L058 is contextual and L914 is unnecessary. This is verification
of the recorded local witness, not a new result beyond the literature
checked. Signed residual comparison, contact flux, initialization,
tangency, other parameters, all-degree continuation and RH remain open.

## Mathlib

The full matching inverse-score witness and supporting theta, series,
logarithmic-derivative and inverse-function coverage have not been
checked in Mathlib. Availability is unknown, not asserted absent.
The proof uses exact rational arithmetic and the stated named source
input; it is an informal proof, not a Lean verification.
