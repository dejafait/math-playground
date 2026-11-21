# Finite horizontal saddle: primary-source extraction1627

Read 18 November 2026: K. Kawano, *Logarithmic Inequalities of Arbitrary
Order for the Riemann Xi Coefficients*, Preprints.org202611.0383v1,
posted 4 November 2026, DOI10.20944/preprints202611.0383.v1,
https://www.preprints.org/manuscript/202611.0383/v1 . The version URL
redirects to the manuscript page, which currently identifies Version1
and marks it not peer reviewed. Statements below are extracted source
claims, not notebook theorems or verified numerical constants.

## Scope, normalization and contour

Section5.2, (28)-(29), Lemma5.1's contour and horizontal-phase proof
paragraphs, AppendixB's definitions and local four-term proof through
B_loc, its subsequent full-mode/tail formulas, and AppendixC through
its total allowance were inspected. The finite-band certificate and
AppendixC.1 differentiation are not inputs; no archive was retrieved.

Use C048a's I and Phi. Write p=sigma+i tau, r=|p|, L=log r,
w=W_0(2p/pi)=U+iV, u_0=w/2, y=V/2. The domain is
L>=12, sigma>=-r/(4L), with reflection for tau<0. Source (28) is

    S(p)=8 pi^(5/2) exp(9w/4) / sqrt(p(1+w))
           * exp(2p Log(w/2)-2p/w).

Branches are continued from positive real p. C048a already verifies
the fixed-height contour and branch prerequisite. The path is
0 -> iy -> infinity+iy, with the continued initial vertical primitive
retained. The short horizontal piece 0<=Re u<=1 is grouped with that
primitive in audited C048b; it must not be charged again as a saddle
tail. Neither C048a nor C048b proves the following local allowance.

On Re u>=1 the source separates

    h_p(u)=2p Log u-pi exp(2u),
    g(u)=8 pi^2 exp(9u/2)/u.

Here g exp(h_p) is the leading positive-power part of mode n=1,
not the full theta integrand. Source AppendixA.2 (A3), also inspected,
prints the full normalized factor with

    sum[n>=1] (n^4-3n^2/(2pi exp(2u)))
                    exp(-pi(n^2-1)exp(2u)).

Thus the negative lower-power n=1 part and n>=2 modes are separate
errors in AppendixB/C. No complex positivity is inferred from Phi's
real-axis positivity.

The finite local segment in AppendixC is u=u_0+s, real |s|<=d,
d=1/(3L), oriented left to right along the existing horizontal line.
There is no rotated descent segment and no extra joining contour at
its endpoints. The remainder of Re u>=1 consists of horizontal tails.
The actual containment Re(u_0)-d>1 and the logarithm/denominator cases
must be checked in the proposed audit using the established geometry.

## Complete relevant local proof cases as printed

AppendixB defines A_0=-h_p''(u_0)/2, B_0=h_p'''(u_0)/6,
g_0=g(u_0), a_1=g'(u_0)/g_0. It prints

    B_0=16p/(3w^3)-8p/(3w),
    h_p''''(z)=-12p/z^4-16pi exp(2z),
    g'/g=9/2-1/z,     g''/g=81/4-9/z+2/z^2.

With K=g(u_0+s)/g_0 and Z=B_0 s^3+R_4(s), the Taylor split is

    h_p(u_0+s)-h_p(u_0)=-A_0 s^2+Z.

The four residual terms in K exp(Z)-1-a_1 s-B_0 s^3 are printed as

    K-1-a_1 s; (K-1)B_0 s^3; K R_4; K(exp(Z)-1-Z).

The source uses the complex exponential remainder
|exp(Z)-1-Z|<=|Z|^2 exp(|Z|)/2, and bounds these by a quadratic,
a quartic and a sextic times an exponential. Both displayed odd
terms cancel on the symmetric interval against exp(-A_0 s^2),
including when A_0 is nonreal. The last exponential is absorbed
in a smaller real Gaussian curvature. Source AppendixB then uses
real Gaussian moments, for t>0 and j=1,2,3,

    (1/sqrt(pi)) integral_R s^(2j) exp(-t s^2) ds
        =(2j-1)!!/(2^j t^(j+1/2)).

For AppendixC the source replaces the finite-band constants by

    U>=3L/4, |w|<=1.01L, cos V>=1/L,
    v_0=pi exp(U) cos V>=1.9r/L^2,
    b=Re A_0>=3.9r/L^2, |A_0|<=6r/L.

The printed local bounds for real |s|<=d are

    |B_0|<=3.65r/L, |R_4(s)|<=2(r/L)|s|^4,
    |K|<=1.16, |a_1|<=4.75, |K-1-a_1 s|<=13s^2,
    |Z|<=3.71(r/L)|s|^3,
    -b s^2+|Z|<=-b_* s^2, b_*=(799/300)r/L^2.

These stronger Lambert and curvature constants are audit obligations.
C048b only needed and proved cos V>1/(4L), |w|<L+2 and U>3L/4;
its success does not establish these stronger source premises.

AppendixC assigns quartic coefficient <22r/L and sextic coefficient
<8(r/L)^2, then gives the normalized local error bound

    sqrt(|A_0|) [13/(2b^(3/2))
                  +33r/(2L b^(5/2))
                  +15r^2/(L^2 b_*^(7/2))].

It compares this with A_loc L^(9/2)/r, where

    A_loc=sqrt(6) [13/(2(3.9)^(3/2)12^2)
                   +33/(2(3.9)^(5/2)12)
                   +15/(799/300)^(7/2)] <1.318214.

All decimal constants are terminating rational values in a future
exact comparison. These formulas have been read, not recomputed or
proved here. In particular the normalization loss sqrt(|A_0|) is
retained: a horizontal complex Gaussian cannot be replaced by a real
Gaussian without that cost.

## Separate allowances and their limits

The source budgets near-left, near-right and Gaussian-extension errors
separately, with coefficients respectively <.091191, <.096514 and
<.099276 times L^(9/2)/r. Their formulas depend on
y_0=exp(12)/12^4 and monotonicity of sqrt(y)exp(-cy) for
y=exp(L)/L^4. They are not contained in A_loc.

AppendixC also prints distant-left relative bound
sqrt(6/pi)L^(11/2)exp(-2r/L^2)/(3sqrt(r)), lower-power first-mode
bound 2L^(3/2)/r, and other local-mode bound
112sqrt(L)exp(-5r/L^2). The distant-left and extra-mode costs
are each assigned <10^-4 L^(9/2)/r. Together with the origin
allocation and the local terms, its claimed coefficient sum is
<1.606651<1.7, used for (29). None of these remaining allowances,
their assembly, zero count, differentiation, inversion or sufficient
mixed signs is imported or approved by this review.

## Duplicate and known-theorem comparison

L798: phase 2s Log z+(9/2)z-pi exp(2z), stationary point
x(pi exp(2x)-9/4)=s, rotated segment x+a v of radius 3/(16Re x),
normalization sqrt(2pi/A). L799: full theta amplitude rho relative
to 4pi^2 exp((9/2)z-pi exp(2z)) on that same rotated segment.
L800: real Gaussian completion in v, with curvature |A|.

Kawano: phase h_p, stationary point w/2, amplitude g containing
exp(9u/2)/u, horizontal width 1/(3L), complex curvature A_0 and
normalization sqrt(pi/A_0). These explicit hypotheses differ.
Neither substituting the exponent 2s=2p-1 nor changing a curvature
symbol supplies the unchanged phase, saddle and contour hypotheses
of L798-L800. This is a theorem-scope comparison, not a new bound or
a proof that no alternative transfer could ever exist.

Reuse the primary-theorem assessment in
`2026-11-05-actual-mellin-remainder-source-scope.md`: DLMF2.4(iii)-(iv)
and O'Sullivan, PJM298(2019),157-199, Assumptions1.1/Theorem1.2
pp159-160, local inverse/Cauchy argument pp171-172 and Corollary5.1
pp175-176. Those inspected fixed-phase results require path domination
and constants controlled with the phase and geometry. Their odd-term
cancellation method is relevant, but they do not supply the moving
sector's explicit A_loc. No repeated primary saddle search is needed.

Reinspected https://dlmf.nist.gov/7.7.E6 : real lower endpoint x,
Re a>0, integral exp(-(a t^2+2bt+c)) from x to infinity equals
(1/2)sqrt(pi/a)exp((b^2-ac)/a)erfc(sqrt(a)x+b/sqrt(a)).
For the nominated audit the intended complex Gaussian coefficient
is A_0; Re A_0>0 and the square-root branch still require proof.
Real error moments use positive real b and b_*, with convergence
and moment specializations to be justified in that audit. This
named standard integration input does not verify the local constants.

Discovery queries: `"Kawano" "Xi" "saddle" "1.318214"` and
`"Logarithmic Inequalities of Arbitrary Order" Mellin saddle`.
The exact source was found; no inspected stronger independent theorem
covering this effective constant was located. Aggregator hits were
not theorem evidence; no novelty is inferred. The recorded global
automatic-import, finite-index-transfer and reciprocal-kernel stops
were read and retained. Full matching Mathlib coverage is unknown.

The one nominated test is defined in
`2026-11-18-mellin-horizontal-local-audit-1627.md`. It audits only
the leading-mode local phase/amplitude cost. This source review
does not perform that test and does not approve its own mathematics.
