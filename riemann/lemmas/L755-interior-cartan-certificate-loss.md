# Lemma 755: a paid interior Cartan certificate misses the proposed cutoff

## Hypotheses

Use L018's actual undeformed Xi and L266's notation

    H_a(y)=Xi(a+iy)Xi(a-iy),  T=2+|a|,  ell=log T.

Assume the external input exactly as registered in
[the October input note](../foundations/2026-10-quasi-riemann-input.md):
Baiying Liu, *Improved zero-free half-planes for the quasi-Riemann
hypothesis*, [arXiv:2610.12234v2](https://arxiv.org/html/2610.12234v2),
Corollary 33.2, with the Section 14 transfer to zeta. Thus zeta has
no zeros in Re(s)>34998281/40000000; its pole at 1 is allowed and
the boundary is not excluded. The external analytic proof and formal
import closure remain locally unaudited. This lemma is conditional
on that input, not an independent verification of it.

Fix

    w=14998281/40000000,  0<delta<w,
    eta=w+delta/8,  D=7delta,
    I=[s_-,s_+]=[w-7delta/8,w-5delta/8],
    c_*=w/2-delta/8.

Let C_G>0 and h_0>0 be universal constants for the one-variable
statement of Goldstein--Schlag, *On resonances and the formation of
gaps in the spectrum of quasi-periodic Schrödinger equations*,
Annals of Mathematics **173** (2011), 337--475, DOI
10.4007/annals.2011.173.1.9, Definition 2.1 and Lemma 2.4,
[pp.347--349](https://annals.math.princeton.edu/wp-content/uploads/annals-v173-n1-p09-p.pdf#page=11).
The precise nondegenerate form used is: for phi analytic in the unit
disk, finite U>=sup log|phi| and finite l<=log|phi(0)| with U>l,
and h>=h_0, outside disks of total radii <exp(-h),

    log|phi(z)| > U-C_G h(U-l),  |z|<1/6.             (GS)

The positive-deficit restriction U>l is essential to this strict form:
phi=1 and U=l=0 would otherwise require 0>0 outside the exceptional
disks. Both applications below have U>l. The source prints the strict
inequality without separating this degenerate case; we use only its
positive-deficit case, not the false equality-case extension.
Its exceptional-disk count retains multiplicity. Only (GS) and the
total-radii assertion are imported; the multidimensional result and
spectral applications are not used. Increase h_0 if necessary so
that the printed sufficiently-large-h condition holds at h_0. Put

    h=max(h_0,log56),
    E=max(55delta/8,55delta/4-2w),
    L=C_G h-1,  Q=L E.

All these parameters are fixed before a and a hypothetical displacement
b vary. Neither Xi(a)!=0 nor simplicity nor a bound on central
multiplicity is assumed.

## Conclusion

For every fixed nu>0 there are positive c,C,T_0, with C>=c, such
that for every real a with T>=T_0 there exists s=s(a) in I with

    H_a(s)>=A(a,s):=c exp(-pi|a|/2) T^(7/2+s-Q-nu)>0. (1)

Uniformly for s<R<1/2 the complete complex circle satisfies

    M_R(a):=max_(|y|=R)|H_a(y)|
        <=Mbar_R(a):=C exp(-pi|a|/2)
                         T^(7/2+max(w,R)+nu).          (2)

The constants and onset are independent of a,b and central
multiplicity. Every 0<b<=w-delta lies strictly below every s in I,
and I is strictly inside (b,w-delta/2). Thus (1)--(2) give a valid,
but uncompetitive, application of L266 at every such zero height.

Specifically, the sufficient upper certificate obtained from these
two estimates is

    K_cert(a,s,R)=ceil(
      [(max(w,R)-s+Q+2nu)ell
        +log(2C/c)-log(1-s^2/R^2)]/[2log(R/s)]).       (3)

L266's K formed with A(a,s) and the actual M_R is at most K_cert.
However, the leading coefficient in (3) is uniformly larger than
c_* for all s in I and s<R<1/2. More precisely, set

    Lambda_delta=log((1/2)/(w-7delta/8))>0.

Then

    (max(w,R)-s+Q+2nu)/(2log(R/s))
          > c_*+3delta/(8Lambda_delta).               (4)

For any fixed finite B_delta, this certificate therefore eventually
exceeds ceil(c_*ell+B_delta), even if s and R are selected afresh at
each height. The fixed choices R=w and nu=delta make (3) a finite
uniform O_delta(ell) cutoff, but do not certify the proposed saving.
For arbitrary fixed nu its constants may also depend on nu. Formula
(3) is explicit in existential constants; no numerical computability
or effective height onset is asserted.

This is a limitation of the displayed disk, interval, normalization,
growth envelope and (GS) application. It is NOT a lower bound on
the actual M_R/H_a(s), NOT a proof that another admissible s or R
fails, and NOT a disproof of the proposed actual-Xi cutoff. In
particular the existence of a large upper certificate says nothing
about the least negative-coefficient index. No coefficient sign,
new zero-free region or RH candidate follows. The generic constant
calibration below removes an arbitrary enlargement of C_G as the
reason this particular certificate fails; it does not make this an
optimal-Cartan impossibility theorem. The step-342 critical audit below
validates the conditional construction and comparison after the stated
positive-deficit correction; this remains a local REPRODUCTION, not
progress beyond the checked source methods.

## Proof

### 1. Growth and normalization with the registered width

Here the width in L461's conclusion cannot simply be replaced:
its conclusion has different hypotheses. We apply its inspected
Littlewood-logarithm mechanism on the changed zero-free domain, as
covered by the prior assessment. The source mechanism is Titchmarsh,
*The Theory of the Riemann Zeta-function*, second edition revised
by Heath-Brown (1986), Theorem 14.2 and proof, printed pp.336--337,
especially (14.2.5)--(14.2.6),
[primary text](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=173).
That printed theorem assumes RH and is not imported as a theorem
under our weaker premise. The changed-domain justification follows.

For any fixed rho>w with rho<1/2, let sigma_rho=1/2+rho and
sigma_*=1/2+w. At height t>0 center disks at 2+it with radii

    r0=1/2, r1=2-sigma_rho,
    r2=(r1+2-sigma_*)/2, r3=(r2+2-sigma_*)/2.

They satisfy r0<r1<r2<r3<2-sigma_*. A slightly larger disk
than r3 stays in Re(s)>sigma_* and misses the pole for large t.
Normalize its analytic logarithm of zeta by the absolutely
convergent Euler logarithm at the center. On the r0 disk the
branches agree and the logarithm is bounded by log zeta(3/2).
The elementary continuation formula used in L461,

    zeta(s)=s/(s-1)-s integral_1^infinity {x}x^(-s-1) dx,

is locally uniformly convergent for Re(s)>0 away from the pole;
it gives |zeta|<=O(t) on r3. Borel--Caratheodory on r3,r2
and Hadamard three-circles on r0,r1,r2 give a bound
O((log t)^theta), with

    theta=log(r1/r0)/log(r2/r0)<1,

for the full normalized logarithm on r1. Hence, for every fixed
epsilon>0, both |zeta| and its reciprocal are <=t^epsilon on
sigma_rho<=Re(s)<=2 at height t beyond one onset. For larger
bounded real parts use the absolutely convergent Euler series on
Re(s)>=2; conjugation gives negative heights. No Euler series
has been continued into its nonabsolute-convergence region.

The completed formula in L018 and complex Stirling,
[DLMF 5.11.1 and 5.11.3](https://dlmf.nist.gov/5.11), then give
the power 7/4+rho/2+epsilon for xi on Re(s)=1/2+rho,
with exponential exp(-pi|t|/4). Reflection gives the same bound
on Re(s)=1/2-rho. To cover the strip between these boundaries,
the continuation formula above supplies preliminary polynomial
growth after canceling that exponential. Apply the maximum modulus
principle to

    xi(s) exp(-i pi s/4)(s+rho+1)^(-q) exp(tau s^2),
    q=7/4+rho/2+epsilon, tau>0,

on finite rectangles in this strip. The power uses the analytic
logarithm in Re(s+rho+1)>=3/2. Its horizontal sides tend to
zero as their heights tend to infinity. First take that limit,
then tau down to zero. This proves the strip bound for nonnegative
heights; conjugation treats negative heights. No zero-free premise
inside the strip is used. This is precisely L461's damping proof
with the boundary hypotheses just verified on the changed domain.

Consequently, for any fixed U_0,V_0 and epsilon>0, at all sufficiently
large |a| and uniformly for |u|<=U_0, |v|<=V_0,

    |H_a(u+iv)| <= C_epsilon exp(-pi|a|/2)
                      T^(7/2+max(w,|u|)+epsilon).     (5)

To verify the claimed sharp w in this upper envelope without assuming
nonvanishing on the boundary, choose rho>w sufficiently close to w
that rho-w is smaller than the allowed epsilon loss. For |u|<=rho
use the full strip bound. For rho<=|u|<=U_0 use the preceding
uniform subpower bound and Stirling at real part 1/2+|u|, reflecting
the other factor. The two factors before reflection are exactly

    xi(1/2-u+i(a-v)), xi(1/2+u+i(a+v)).

Their heights have absolute values |a-v| and |a+v|. For |a|>V_0
their sum is exactly 2|a|; their powers compare uniformly to powers
of T. After reflection both real parts are 1/2+|u|, so the
total power is 7/2+|u| plus the two arbitrarily small zeta losses.
On the inner strip the power is 7/2+rho plus those losses. Choosing
rho-w and the losses with total <=epsilon proves (5).
Stirling is uniform on the fixed compact interval of positive real
parts after reflection, even when the original disk crossed Re(s)=0.
Thus no endpoint or real-axis-only maximum replaces the complex disk.

Since w<eta<9w/8<1/2, the line 1/2+eta lies strictly between
sigma_* and 1. The external premise, completed prefactors and
reflection give H_a(eta)=|xi(1/2+eta-ia)|^2>0 for every a.
The same logarithm estimate and Stirling give, for arbitrary
epsilon>0 beyond an onset independent of a,

    H_a(eta)>=c_epsilon exp(-pi|a|/2)
                                      T^(7/2+eta-epsilon). (6)

All real-part margins here are fixed before a varies. The onset
and constants may depend on delta and epsilon and are not effective.

### 2. Exceptional disks and the paid anchor exponent

Define the entire function of z

    phi_a(z)=exp(-Dz ell) H_a(eta+Dz)/H_a(eta).

It has phi_a(0)=1. The nonvanishing exponential preserves all zeros
and multiplicities, and the denominator is the independently
nonzero exterior value (6), not Xi(a) or a central derivative.
For |z|<=1 put u=eta+D Re(z). Equations (5)--(6) give

    log|phi_a(z)| <= [max(w,|u|)-u+2epsilon]ell+C_0.

The function max(w,|u|)-u is nonincreasing in u and has maximum
on eta-D<=u<=eta+D equal to

    max(w-(eta-D), -2(eta-D), 0)
       =max(55delta/8,55delta/4-2w)=E.                (7)

Take C_0>=0 and U=(E+2epsilon)ell+C_0 in (GS), with l=0.
Here E>=55delta/8>0 and ell>0, so U>l as required.
For s in I, |s-eta|<=delta<D/6. Under the scaling y=eta+Dz,
the exceptional disks have total radii <D exp(-h). Their
intersections with the real axis have total length at most twice
that sum, and

    2D exp(-h)<=14delta/56=delta/4=|I|.

The strict disk-sum inequality prevents those intersections from
covering I. Select a real s in I outside them. This is a selection
at each height, with no exceptional heights and no zero-separation
or simplicity assumption. The multiplicity-count part of (GS)
places no extra hypothesis on this application.

At that point (GS) gives log|phi_a((s-eta)/D)|>-L U, whence

    H_a(s) >= c_epsilon exp(-L C_0) exp(-pi|a|/2)
                 T^(7/2+s-Q-(1+2L)epsilon).           (8)

Here H_a(s)=|Xi(a+is)|^2 is nonnegative, and the strict modulus
lower bound makes it positive. Section 3 below shows L>1.
Choose epsilon>0 so that (1+2L)epsilon<=nu. This proves (1).
Equation (5), independently with loss nu and |u|,|v|<=1/2,
proves (2) uniformly for every allowed R. Increase C so C>=c.
All choices precede a,b and the selected s. In particular a central
zero of any multiplicity does not affect the argument or constants.

### 3. Calibration of the universal Cartan constant

This short test of (GS), not a reproof of Cartan's theorem, is
needed to distinguish a real loss of the specified certificate from
an arbitrary enlargement of an unspecified source constant.

Fix r>6 and apply (GS) to phi(z)=1+r z, U=log(1+r), l=0.
For all sufficiently large h the real interval

    J_h=[-1/r-exp(-h),-1/r+exp(-h)]

lies strictly in |z|<1/6. Its length is 2exp(-h), exceeding the
total length of real intersections of the exceptional disks. At
some z_h in J_h outside them, therefore,

    U-C_G h U < log|1+r z_h| <= log r-h.

Letting h tend to infinity proves C_G>=1/log(1+r). Letting
r decrease to 6 yields

    C_G>=1/log7.                                      (9)

This argument uses the universal constants in the fixed form (GS);
it does not assert a lower bound for a constant in a different Cartan
form or on a different observation disk. Since h>=log56 and
56>7^2,

    C_G h >=log56/log7>2,
    L>1,  Q>E>=55delta/8.                            (10)

### 4. Exact witness budget and its excess

Every b<=w-delta satisfies s_- -b>=delta/8>0, while
w-delta/2-s_+=delta/8>0. Thus s in I and s<R<1/2 are
legitimate L266 parameters for every hypothetical zero under test.
Inserting the positive lower model (1) and upper model (2) in
L266 gives (3). The actual circle maximum may be smaller; hence
only the inequality K_actual<=K_cert is justified.

To examine the leading coefficient, the allowable extra loss at
a fixed s,R for a coefficient no larger than c_* is

    F_R(s)=(w-delta/4)log(R/s)-max(w,R)+s.             (11)

For R<=w this increases with R. For R>=w its R derivative is
(w-delta/4)/R-1<0. Thus its maximum over s<R<1/2 is at
R=w. Since w-delta/4<w and log(w/s)>0,

    F_R(s)<= (w-delta/4)log(w/s)-w+s
           <= w log(w/s)-(w-s)
           <= (w-s)^2/s
           <= (7delta/8)^2/(w/8)
           = 49delta^2/(8w)<49delta/8.               (12)

The third inequality is log(1+x)<=x, with x=(w-s)/s.
The fourth uses w-s<=7delta/8 and s>=w-7delta/8>w/8.
Combining (10)--(12), the numerator in (3) exceeds
2c_*log(R/s) by more than 3delta/4, even before the positive
2nu loss. Also

    0<log(R/s)<log((1/2)/s_-)=Lambda_delta.

Division proves (4). The additive term in (3) is positive since
C>=c and 0<s/R<1. Thus no fixed additive B_delta can absorb
the uniform positive coefficient gap as ell grows. Explicitly, with
g=3delta/(8Lambda_delta)>0, choose ell so g ell>B_delta+1.
Then the real argument of ceil in (3) exceeds c_*ell+B_delta+1;
monotonicity of ceil gives the asserted strict integer comparison.
This remains true with height-dependent choices within this interval and range
of radii. It is a statement about the particular sufficient upper
certificate (3), not a lower bound on L266's exact ratio.

For completeness, fixing R=w and nu=delta gives s<=s_+<w and hence a
denominator bounded away from zero and 1-s^2/w^2 bounded away
from zero. The numerator is bounded above by a constant times ell
plus a constant, uniformly for s in I. Therefore the application
does give a finite O_delta(ell) witness cutoff, including arbitrary
central multiplicities. The already available exterior-anchor
cutoffs are better; this weaker bound is not advertised as an
improvement of them. The missing saving, the initial signs and the
outer zero layer all remain unresolved. No assertion about the
actual existence of a hypothetical off-line zero has been made. QED.

### Critical audit — 2026-11-04, step 342

**Verdict and repairs.** The conditional selected-anchor construction,
calibration (9), and certificate excess (4) pass the audit with U>l
in (GS). The earlier unrestricted strict formulation was false for
phi=1, U=l=0: the exceptional disks have real intersection length
<2exp(-h), which for large h cannot cover the real diameter of the
observation disk. A remaining point would have to satisfy 0>0.
This is a correction of a universal hypothesis, not a new small-value
theorem. The source's positive-deficit case is sufficient: in Section 2
U>0=l, and in Section 3 U=log(1+r)>0=l. Nothing is inferred from
the impossible equality-case premise. The O_delta assertion now fixes
nu=delta explicitly, and the word "computable" has been removed because
the constants and onset were only shown to exist. No conclusion about
the actual ratio, signs or zeros is strengthened by these repairs.

**Changed-domain analytic bounds.** Write a_*=2-sigma_*>0 and
kappa=(a_*-r3)/2>0. The disk of radius r3+kappa centered at 2+it
lies strictly to the right of sigma_*, and for t>r3+kappa+1 avoids
the pole. Hence an analytic logarithm exists on a neighborhood of the
closed r3 disk. Its agreement with the Euler logarithm on r0 follows
from connectedness and the normalized center value; their difference
is a constant multiple of 2pi i and vanishes at the center. Thus both
the real and imaginary parts of that branch are controlled on r0.
The continuation integral has, on any compact positive-real-part set,
integrable derivative majorants x^(-1-alpha)(1+log^k x) with alpha>0.
It gives O(t) on r3 without an unproved reciprocal estimate.
Borel--Caratheodory then controls the entire branch on r2 and
three-circles gives the fixed exponent theta<1 on r1. Its constants
depend on rho-w but not t. Applying the bound to the real part with
both signs proves the upper and reciprocal subpower estimates.

In the strip proof, compact heights on its vertical sides are absorbed
by continuity of entire xi. Preliminary polynomial growth times
exp(-pi|t|/4) is obtained on the right half from the continuation
formula and Stirling, then on the left half by reflection. For real q,
the analytic power has modulus |s+rho+1|^(-q), comparable to
(2+|t|)^(-q); exp(-i pi s/4) has modulus exp(pi t/4).
It cancels the gamma decay for t>=0 and reinforces it for t<0.
Thus both vertical sides are bounded before damping. At fixed tau>0
the horizontal sides vanish as their heights tend to infinity;
only afterwards does tau tend to zero at a fixed interior point.
Conjugation gives the negative-height estimate. No pole of zeta
remains in this completed-function maximum-modulus argument.

For a desired loss epsilon in (5), one may choose
0<rho-w<min(epsilon/3,(1/2-w)/2) and zeta loss epsilon/6
per factor. The combined loss is then less than epsilon. All choices
precede a and the point of the fixed complex disk. Outside the inner
strip, reflection puts both real parts at 1/2+|u| on one fixed compact
positive interval; the logarithm estimate covers its portion up to 2,
and absolute Euler convergence covers the rest. The exact shifted
heights have |a-v|+|a+v|=2|a| once |a|>V_0. For instance
|a|>=2V_0+2 makes each |a+v|,|a-v| comparable to T uniformly,
so no power or exponential loss is hidden in the comparison.
The lower bound at eta uses a fixed strictly positive margin delta/8
from sigma_*, and eta<1/2 avoids the pole even at height zero.
Only its large-height quantitative estimate is needed here.

**Selection, calibration and comparison.** The logarithm of the
normalized modulus is bounded by
[max(w,|u|)-u+2epsilon]ell+log(C_epsilon/c_epsilon).
The three affine pieces are 0 for u>=w, w-u for -w<=u<=w,
and -2u for u<=-w. They are nonincreasing, which verifies (7)
also when the disk crosses the negative-real-part regime. Scaling
maps I to [-1/7,-3/28], strictly inside the radius-1/6 disk.
The strict projected-length inequality ensures a surviving real point
at every height; overlapping disks or repeated zeros do not affect it.
No measurable or continuous choice of s(a) is used or needed.

For the calibration, fix r>6 before h tends to infinity. Rearranging
the linear-test inequality gives
(1-C_G log(1+r))h<log r-log(1+r).
It cannot hold for all large h if C_G log(1+r)<1. Taking r down
to 6 therefore proves (9) for the same universal C_G, regardless of
how large the fixed threshold h_0 is. The exceptional set may vary
with h; only its total radii enter this argument. In particular
C_G h>=log56/log7>2 is valid without knowing a numerical source
constant. It implies L>1 and Q>55delta/8, so the loss parameter
epsilon can be chosen once to satisfy (1+2L)epsilon<=nu.

The radius derivative in (11) is positive below w and negative above
w; hence (12) is an upper bound on the entire allowed radius range.
The loss surplus is Q-F_R(s)+2nu>3delta/4. Dividing by the positive
2log(R/s), whose logarithm is bounded above by Lambda_delta, gives
the uniform strict gap (4). The additive term is positive because
C>=c and 0<s/R<1, and the integer comparison is justified explicitly
above. This covers choices s(a),R(a) approaching each other with
height; such choices cannot remove the uniform lower coefficient gap.
For the actual maximum, L266 uses the SAME lower model A and its
ceiling is monotone in M_R. Thus K_actual<=K_cert. Replacing A by
H_a(s) could only decrease that ceiling further, not turn this
certificate-specific failure into a failure of the actual bound.

Every quantitative choice depends only on the fixed delta, nu and
chosen universal source constants before a,b vary. There is no claim
uniform in shrinking delta, no effective onset, and no dependence on
Xi(a) or on central multiplicity. The source-proof qualification for
Liu v2 remains unchanged. The reviewed direct local inputs are L018,
L266 and L461; no additional dependency is introduced by this audit.
The prescribed disk/envelope implementation stays parked, with its
original stop intact. An improvement requires a separately assessed
new quantitative input; the audit supplies no initial sign or RH candidate.

## Mathlib

Full matching coverage for this conditional selected-anchor statement,
the universal-constant calibration and certificate comparison has not
been checked. No absence claim or Lean verification is made. The
supporting Cartan, analytic-logarithm, Borel--Caratheodory, three-circles,
Stirling and Cauchy inputs are used as classical results with the
citations and changed-domain arguments above, not as claimed Mathlib
theorems. The relevant local analytic and witness inputs are L018,
L461 and L266; their formal coverage is not upgraded here.
