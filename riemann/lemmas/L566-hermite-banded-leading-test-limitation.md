# Lemma 566: the four-leading-coefficient Hermite Gram test is insufficient

## Hypotheses

Use the actual coefficients, even kernel Phi_R and polynomial P_N of
L564, with physicists' Hermite normalization:

    b_(2n)=1/[2^(2n)(2n)!] integral_R
                       u^(2n) exp(-u^2/4) Phi_R(u) du > 0,
    P_N(t)=sum_(n=0)^N (-1)^n b_(2n) H_(2n)(t),
    D(f)=f'^2-f f''.

Let N>=2 be an integer, m=2N, q=m-1, and
v=(H_0,...,H_q)^T. Consider real symmetric matrices G indexed by
0,...,q with G_(j,k)=0 if j,k have opposite parity or |j-k|>2.
The proposed full certificate is D(P_N)=v^T G v with G PSD.
The approved diagnostic matches only degrees 2m-2, 2m-4, 2m-6
and 2m-8, retaining all entries contributing at those degrees.

The finite Hermite formula is imported from Cormac O'Sullivan,
*Zeros of Jensen polynomials and asymptotics for the Riemann xi
function*, [arXiv:2007.13582v2, opening of section 2](https://arxiv.org/html/2007.13582v2#S2),
9 December 2020. Actual coefficients and the expansion are from Dan
Romik, *Orthogonal polynomial expansions for the Riemann xi function*,
[arXiv:1902.06330v3, (2.1), Theorem 2.1/(2.2)](https://arxiv.org/html/1902.06330v3#S2),
with normalization and the complete kernel bound as in L564.

The PSD-Gram/SOS framework is known: Gatermann–Parrilo,
*Symmetry groups, semidefinite programs, and sums of squares*,
[arXiv:math/0211450v1, Lemma 2.1, pp. 4–5](https://arxiv.org/pdf/math/0211450v1).
An invertible real basis change preserves this equivalence by
congruence. Its Theorem 3.3 permits finite-symmetry averaging;
it does not imply a Hermite bandwidth constraint. Singular PSD
pivot qualifications are in Vandenberghe–Andersen,
*Chordal Graphs and Semidefinite Optimization*,
[section 9.1, pp. 337–338](https://www.seas.ucla.edu/~vandenbe/publications/chordalsdp.pdf),
DOI 10.1561/2400000006. Their Theorem 10.1 is a completion theorem,
not a sufficient test for a prescribed zero-filled matrix. No such
completion inference is used here.

## Conclusion

1. For every N>=3, a matrix G of the prescribed sparsity is PSD and
   matches all four specified coefficients of D(P_N). Its two
   supported parity blocks can be chosen positive definite on their
   supported coordinates, all other rows and columns zero. This
   construction works for every real choice of
   the three subleading coefficients of the normalized polynomial;
   it imposes no additional restriction on the actual b sequence.

2. At N=2 the four coefficients are the entire discriminant. No PSD
   Gram matrix, even without the bandwidth restriction, represents
   D(P_2). An exact rational interval certificate gives

       Q=b_2^2+16 b_2 b_4+96 b_4^2-4 b_0 b_4 < 0,

   whereas PSD would require Q>=0. In particular D(P_2) is negative
   at the real point with t^2=(3+b_2/(4b_4))/2.

Thus the universal full-certificate assertion for every N>=2 fails
at its initial index, but this does NOT exclude a full certificate at
unbounded cutoffs. Every L564 cutoff N=ceil(16(T+1)^2), T>=1, is at
least 64 and passes this four-coefficient diagnostic. For N>=3 the
constructed PSD polynomial can differ from D(P_N) in degrees at most
4N-10. Its positivity supplies no sign for that omitted difference,
D(P_N), D(Xi), higher forms, or RH. The finite specialization and
computational certificate pass the independent application audit below;
the imported source manuscripts are not independently audited here.

## Proof

### Normalization and complete discriminant coefficients

Set h_j=2^(-j)H_j, A=(-1)^N 2^m b_m and p=P_N/A. Then A!=0,
p is monic, D(P_N)=A^2 D(p), and the original Gram matrix is

    G=A^2 E^(-1) C E^(-1), E=diag(2^0,...,2^q),          (1)

when C is the Gram matrix on h=(h_0,...,h_q)^T for D(p).
This positive diagonal congruence preserves PSD, parity and bandwidth.

For j>=0 define the following coefficients, with a falling factorial
zero whenever its length exceeds j:

    alpha_j=-j(j-1)/4,
    beta_j=j(j-1)(j-2)(j-3)/32,
    gamma_j=-j(j-1)(j-2)(j-3)(j-4)(j-5)/384.

The imported finite Hermite formula gives
h_j=t^j+alpha_j t^(j-2)+beta_j t^(j-4)+gamma_j t^(j-6)+...
with terms of negative degree absent. This convention defines
coefficients at nonnegative indices only, not polynomials H_j for
negative j. Put r_l=b_(m-2l)/b_m for 0<=l<=N. Then the first
coefficients of p are

    u=alpha_m-r_1/4,
    v=beta_m-(r_1/4)alpha_(m-2)+r_2/16,
    w=gamma_m-(r_1/4)beta_(m-2)
                 +(r_2/16)alpha_(m-4)-r_3/64, m>=6.     (2)

At m=4, w is absent and is set to zero solely for the next coefficient
formulas; no r_3 or negative Hermite index is used. Thus
p=t^m+u t^(m-2)+v t^(m-4)+w t^(m-6)+..., with absent terms
understood as just specified. In particular, (2) retains all lower
Hermite terms that can contribute, with their actual alternating signs.

Let d_k=[t^(2m-2-2k)]D(p), k=0,1,2,3. The complete coefficients are

    d_0=m,
    d_1=2(m-3)u,
    d_2=(m-2)u^2+2(m-10)v,
    d_3=2(m-5)uv+2(m-21)w.                              (3)

For verification, two distinct monomials a t^i and b t^j contribute
[2ij-i(i-1)-j(j-1)]ab=[i+j-(i-j)^2]ab at degree i+j-2.
A monomial a t^i paired with itself contributes i a^2. Applying
these identities to degree deficits 0,2,4,6 gives (3). All other
pairs have total deficit at least eight, so cannot contribute. The
identities include constants, whose derivatives vanish, and yield
(3) also at m=4 with w=0. This is the whole discriminant, not a
sum of the individual Hermite discriminants.

### All contributing entries and their necessary PSD conditions

For j>=0 write

    U_j=2alpha_j,
    V_j=alpha_j^2+2beta_j,
    W_j=2gamma_j+2alpha_j beta_j.

For j>=2 write

    F_j=alpha_j+alpha_(j-2),
    B_j=beta_j+beta_(j-2)+alpha_j alpha_(j-2).

These are respectively the first three coefficients below the leading
term of h_j^2 and the first two below that of h_j h_(j-2).
Define x_i=C_(q-i,q-i), i=0,1,2,3, and
y_i=C_(q-i,q-i-2), i=0,1,2, when the indices exist. The four
matching equations are exactly

    x_0=m,
    U_q x_0+x_1+2y_0=d_1,
    V_q x_0+U_(q-1)x_1+x_2+2F_q y_0+2y_1=d_2,
    W_q x_0+V_(q-1)x_1+U_(q-2)x_2+x_3
                         +2B_q y_0+2F_(q-1)y_1+2y_2=d_3. (4)

At q=3 (N=2), the final 2y_2 term is omitted: its indices would
be 1 and -1. All other entries and coefficients in (4) exist there.
To prove completeness, a diagonal term at index j has degree 2j,
so only j>=q-3 is visible in these four degrees. An allowed
off-diagonal term has indices j,j-2 and degree 2j-2, so only
j>=q-2 is visible. This gives precisely the stated lists, including
the boundary exception. Opposite-parity and longer-range terms are
zero by hypothesis.

For N>=3, x_4=C_(q-4,q-4) also exists. It does not appear in (4),
but cannot be discarded from the PSD test because it couples to
x_2 through y_2. The relevant principal blocks are

    O = [[m,   y_0, 0],       E_0 = [[x_1, y_1],
         [y_0, x_2, y_2],              [y_1, x_3]],
         [0,   y_2, x_4]],                                  (5)

on indices (q,q-2,q-4) and (q-1,q-3), respectively. Since m>0,
put s=x_2-y_0^2/m. Necessary conditions, and sufficient conditions
for these particular blocks, are

    s>=0, x_4>=0, s x_4>=y_2^2;
    x_1>=0, x_3>=0, x_1 x_3>=y_1^2.                      (6)

These include singular cases: s=0 forces y_2=0; x_4=0 also
forces y_2=0; x_1=0 or x_3=0 forces y_1=0. They follow by
completing the m square and the elementary 2-by-2 PSD criterion,
without dividing by any possibly zero pivot. At N=2, O is instead
[[4,y_0],[y_0,x_2]], whose condition is x_2>=y_0^2/4; the
even block and its singular alternatives are unchanged. Additional
entries of a general larger matrix could impose further conditions;
passing (6) alone would not prove that matrix PSD.

### Explicit realization of the leading equations when N>=3

Use all the actual values (2)–(3) and choose the entries sequentially:

    x_0=m, x_1=1,
    y_0=(d_1-U_q m-1)/2,
    x_2=y_0^2/m+1,
    y_1=(d_2-V_q m-U_(q-1)-x_2-2F_q y_0)/2,
    x_3=y_1^2+1,
    y_2=(d_3-W_q m-V_(q-1)-U_(q-2)x_2-x_3
                              -2B_q y_0-2F_(q-1)y_1)/2,
    x_4=y_2^2+1.                                        (7)

All quantities are finite real numbers, and the only nonconstant
denominator is m>0. Set every other entry of C to zero. Each line
of (4) is then satisfied by construction. This does not presume any
sign or asymptotic relation among the actual coefficient ratios.

The zero-filled matrix itself is PSD. Indeed, the quadratic forms
of its two supported blocks, with coordinates z_0,z_2,z_4 and
z_1,z_3, are exactly

    m(z_0+(y_0/m)z_2)^2+(z_2+y_2 z_4)^2+z_4^2,
    (z_1+y_1 z_3)^2+z_3^2.                              (8)

Both are positive definite on their respective coordinate spaces.
The remaining coordinates have zero rows and columns. Thus (8)
proves PSD of C and hence of G in (1); no dense PSD completion is
substituted. At the initial large-case index N=3, q=5, the five
used indices are 5,4,3,2,1 and the remaining index 0 has a zero
row, so this construction has no hidden negative index.

The even polynomials D(p) and h^T C h agree at their top four
degrees and both have degree at most 2m-2. Their difference has
degree at most 2m-10. The unconstrained remainder is exactly why
the construction is not a full certificate for D(P_N).

### Actual initial index N=2

Here

    p=t^4-a t^2+c,
    a=3+b_2/(4b_4)>0,
    c=3/4+b_2/(8b_4)+b_0/(16b_4)>0,
    D(p)=4t^6-2a t^4+(2a^2-12c)t^2+2ac.                (9)

All four even coefficients are included. At the real point
t_0=sqrt(a/2), p'(t_0)=0, p''(t_0)=4a, so

    D(p)(t_0)=a(a^2-4c),
    a^2-4c=Q/(16 b_4^2),
    D(P_2)(t_0)=16a Q.                                 (10)

PSD of any representing Gram matrix implies nonnegativity at every
real evaluation vector, including t_0, regardless of singularities.
Thus Q>=0 is necessary. The following exact coefficient bounds show
that it fails for the actual kernel; this is not a test on free or
asymptotic substitute coefficients.

The executable certificate is
`scripts/hermite-gram/leading-block-boundary-certificate.py`, with
full output in
`scripts/hermite-gram/leading-block-boundary-certificate.json`.
Reproduce from the active notebook by

    python3 scripts/hermite-gram/leading-block-boundary-certificate.py

It uses only Python integers and rational Fractions, no floating-point
exponential, quadrature estimate, API, coefficient fit or omitted
unsigned error. Its interval rules and both tail estimates are as
follows, so the certificate's inequalities are independently checkable.

* Fixed-point endpoints have denominator S=2^160. Addition/subtraction
  are exact at that scale; multiplication takes the minimum and maximum
  of the four endpoint products and rounds outward by integer floor
  and ceiling. Division by a positive integer is likewise outward.
* For 0<=x<=1, use the Taylor polynomial for exp(x) through order
  40 and remainder bounded by 3/41!, since exp(1)<3. All Taylor
  operations use the same outward rules. For larger positive x,
  halve the argument until it is at most one and square the enclosing
  positive interval back. For negative x, take outward reciprocals
  of the interval for exp(-x). For x<=-128 it suffices to use
  [0,2^(-128)], because exp(1)>2. Monotonicity encloses exp of an
  interval by the corresponding endpoint bounds. No underflow is used.
* Pi is enclosed using Machin's identity
  pi=16 arctan(1/5)-4 arctan(1/239). Alternating arctangent sums
  of 16 and 6 terms, respectively, with the next term as error,
  are rational enclosures. To fix the identity's branch, double-angle
  formulas give tan(4 arctan(1/5))=120/119 and then
  tan(4 arctan(1/5)-arctan(1/239))=1. The angle is between zero
  and pi/2, so it is pi/4. The alternating-series enclosures and
  the familiar elementary bounds 3<pi<4 give strict endpoint checks.
* On [0,6], divide into 3072 panels of length 1/512 and include
  theta indices k=1,2,3,4. On each entire panel interval-enclose
  u^(2n) exp(-u^2/4) times the finite sum

      2 sum_(k=1)^4 [2pi^2 k^4 exp(9u/2)
                       -3pi k^2 exp(5u/2)] exp(-pi k^2 exp(2u)).

  Each bracket is positive for u>=0 and pi>3, so replacing a
  negative lower interval endpoint by zero is valid. Multiply the
  resulting interval by the panel length and sum. This is an
  enclosure of the integral, not a midpoint or trapezoidal rule.
  Multiply by two for the full even integral. Every panel interval
  is retained in the certificate.
* For the omitted theta indices k>=5 on [0,6], dropping the negative
  summand and using the decreasing function
  exp(9u/2-pi k^2 exp(2u)) gives

      0<=Phi_tail(u)<=64 sum_(k>=5) k^4 2^(-3k^2)
                       <=80000*2^(-75).

  The derivative of the exponent is 9/2-2pi k^2 exp(2u)<0.
  The successive ratio of k^4 2^(-3k^2) for k>=5 is at most
  16*2^(-33)<1/2, so the sum is at most twice its initial term,
  1250*2^(-75). Its contribution to the full 2n-th moment is at
  most 2*80000*2^(-75)*6^(2n+1)/(2n+1), since the extra Gaussian
  is at most one. Positivity supplies zero as a lower tail bound.
* Beyond u=6, L564 gives Phi_R(u)<=10000 exp(-u^2). Put
  A_0=5/4, L=6, and define

      R_0=1/(2A_0 L),
      R_2=L/(2A_0)+R_0/(2A_0),
      R_4=L^3/(2A_0)+3R_2/(2A_0).

  Then integral_L^infinity u^j exp(-A_0 u^2) du
  <=R_j exp(-A_0 L^2) for j=0,2,4. For j=0, compare 1<=u/L
  and integrate u exp(-A_0u^2); integration by parts gives the
  other two recurrences, with zero boundary term at infinity.
  Thus 20000 R_(2n) exp(-45), enclosed by the same exponential
  routine, bounds the full moment tail. This covers all theta
  indices there; it does not assume the first summand dominates.

Divide the resulting full moment intervals by 2^(2n)(2n)!.
The certificate gives the following outward rational decimal bounds:

    0.4830496619561212 <= b_0 <= 0.5000058552234447,
    0.0027078764722780 <= b_2 <= 0.0028563015049729,
    0.0000071100966671 <= b_4 <= 0.0000075733754218.       (11)

The bounds are deliberately loose. For a short exact sign check,
(11) implies b_0>=12/25, b_2<=3/1000 and
7/10^6<=b_4<=8/10^6. Since all coefficients are positive,

    Q <= (3/1000)^2+16(3/1000)(8/10^6)
                        +96(8/10^6)^2-4(12/25)(7/10^6)
       =-0.000004049856 < 0.                            (12)

Using all digits of (11), the certificate also records the stronger
exact upper bound
-522804520345451444198390511/10^32<0. The weaker exact bound (12)
already suffices. Equations (10)–(12) disprove PSD representation at
N=2, including every singular-block alternative. No claim about an
off-line zero of Xi is involved.

### Relevance and limitations

The source framework is imported, not reproved as a new result.
The specialization (2)–(8) identifies why the proposed leading test
does not constrain the actual large-cutoff sequence: the previously
unconstrained x_4 can absorb the last coupling. Removing it would
give an invalid stronger PSD restriction. L565's diagonal-CD
obstruction remains a separate, valid result about a different cone;
it is not a mathematical premise of this proof.

The finite N=2 failure does not meet the unbounded-cutoff abandonment
test. Park only this four-coefficient diagnostic after recording its
limitation; the full bandwidth-two certificate remains unsettled for
the L564 cutoffs. Full lower-coefficient matching, any signed Xi
transfer margin compatible with zeros and multiplicities, and higher
forms remain unresolved. No originality beyond the recorded source
comparison or independent manuscript verification is asserted.

### Independent application and certificate audit, 2026-10-31

The approved audit accepts the stated result without a mathematical
repair. The conclusion's strict definiteness is explicitly on supported
coordinates; the full matrix can have zero rows. The input normalization
agrees with L019's K=2Phi_R and
L020's cosine integral; full-line even moments therefore have exactly
the factor two and denominators 2^(2n)(2n)! used here. Romik's
coefficient/expansion theorem and evenness remain imported inputs.

For the universal algebra, differentiating two monomials gives the
cross coefficient i+j-(i-j)^2. The possibilities at total deficits
0,2,4,6 are respectively (0,0), (0,2), (0,4)/(2,2), and
(0,6)/(2,4). They give all terms of (3), including the constant
terms at m=4 and m=6. Squaring the finite Hermite formula gives
U,V,W; multiplying h_j by h_(j-2) gives F,B. Their degrees give
exactly the visible entries of (4). All lower diagonals and edges
are invisible at those four degrees, but x_4 is a required free
PSD variable when q>=5. No negative-index polynomial is used.

Completing the first square of O leaves the symmetric block
[[s,y_2],[y_2,x_4]]. Its diagonal/product inequalities are equivalent
to PSD even at s=0 or x_4=0, with y_2 then zero. The same criterion
on E_0 forces y_1=0 at either zero diagonal. Thus (6) includes all
singular cases, without assuming that separate clique tests prove
zero-filled PSD. For (7), s=1 and x_4=y_2^2+1; expanding (8)
recovers all five diagonals and three couplings of the actual matrix.
The remaining rows are zero. This verifies PSD, the boundary q=5,
and the diagonal congruence (1) for every N>=3, independently of
any coefficient asymptotic. The omitted difference is even of
degree at most 2m-10. At m=4 direct differentiation of (9) gives
(10), so Q<0 rules out every PSD representation, not merely (6).

The original rational certificate was replayed and the complete
saved evidence independently audited by

    python3 scripts/hermite-gram/l566-certificate-audit.py

The full audit is `scripts/hermite-gram/l566-certificate-audit.json`.
It checks every interval primitive against its exact rational image,
all 3072 ordered panels and their complete sums, the moment-to-b
normalization, both tails, all outward decimal bounds, and both exact
Q bounds. Each non-clipped exponential argument is additionally
enclosed independently at scale 2^192, using 48 Taylor terms after
reduction to [0,1/2], remainder <=2/49!, squaring and positive
reciprocals. All 22744 independent enclosures are contained in the
original enclosures; exp(0)=1 is handled exactly. The 20236 clipped calls
are covered analytically by exp(x)<2^-128 for x<=-128, since e>2.
The original full certificate replays byte-for-byte unchanged. The
audit harness initially over-enclosed exp(0) while testing inclusion
in the original exact singleton; handling zero exactly corrected
that harness issue, with no change to the mathematical certificate.

For the integration domains, every bracket is positive because
2pi k^2 exp(2u)-3>0. This justifies clamping only a negative interval
lower endpoint, without replacing the signed theta formula. Machin's
identity has tangent one; the angle is strictly positive by
4(1/5-1/375)-1/239>0 and at most 4/5<pi/2. Hence its branch
is pi/4; the alternating-series intervals really enclose pi.
The Gaussian argument interval is [-u_hi^2/4,-u_lo^2/4] with outward
rounding, and the monotonic exponential enclosures hold over each
entire panel, not only endpoints of a quadrature formula.

For k>=5 the exponent derivative 9/2-2pi k^2 exp(2u) is
negative on the entire [0,6]. Dropping the negative summand gives
64 k^4 exp(-pi k^2)<=64 k^4 2^(-3k^2); the successive-ratio
bound 16*2^-33<1/2 covers every omitted k. Integrating u^(2n)
and multiplying by two gives exactly the stored theta tails.
For u>=6 the full-kernel L564 envelope gives 10000 exp(-5u^2/4)
after the extra Gaussian. Integration by parts with its zero
infinite boundary term gives the stated R_0,R_2,R_4 recurrence.
Thus the spatial tails cover all indices, and adding the two
positive errors to the upper moment bound leaves no omitted domain.

The exact Q upper bound remains
-522804520345451444198390511/10^32<0; the independently reconstructed
short bound is -4049856/10^12<0. No numerical tolerance or sign
guess is used. This audits a finite specialization and implementation,
not originality or the imported manuscript proofs. Since all L564
cutoffs are >=64, the N=2 failure cannot be used to reject their full
Gram matrices. Park only the four-coefficient diagnostic; full lower
matching, signed Xi transfer and higher positivity remain unproved.

## Mathlib

Coverage of this full restricted-Gram diagnostic, actual N=2 sign,
and its rational certificate has not been checked. Availability is
unknown, not absent. General PSD/congruence, polynomial and Hermite
facts would be supporting results, not a matching theorem for the
actual coefficients. Reference:
https://leanprover-community.github.io/mathlib4_docs/
