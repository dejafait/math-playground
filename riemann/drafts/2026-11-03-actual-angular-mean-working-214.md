# Actual constant-angular mean attempt — step 214

Invocation-start target and review: exactly the TARGET in the supplied
`drafts/literature/2026-11-03-actual-angular-mean.md` (EXPLORE).
The saved target and assessment TARGET agree verbatim; the recovery
notice about a mismatch is superseded by this direct comparison, not by
an edit to supervisor state. A concrete mathematical attempt follows.

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
|mu_n|>=exp(-n/100) on an unbounded n=12q+3 subsequence, for the
unchanged L666 c_0 with a single actual L703/L708 profile. This would
feed the scalar E_0/D interface and L661 diagonal envelope; global
charge, H/support, realization and signs remain independent gaps.
Continue with that bound or a quantitative paid intermediate estimate;
stop if only a residue identity or the old origin/ambient costs remain.

Inputs checked: L666 exact product/pole cases; L703 hypotheses and
Sections 4–5; L708 hypotheses and fixed-profile qualifications;
C645o Section 2 and C645p Section 1 only as unaudited comparisons;
working 212 and origin/propagation stops in working 86/87. The anchor,
j=0, inverse angle, unit masses and both endpoints are retained.
No external search refresh or cross-notebook input is needed.

Unfinished contour calculation: deform the angular circle to radius
d/R=10/11. All common p_j have modulus <d/U<d/R and all a/t_j
have modulus >d, so no poles are crossed. With z=u/(d/R),
b=1-i*y/d and k_j=t_j/R, each nonzero-grid factor becomes
[(1+k_j*z)/(b+k_j*z)]*[(z+k_j*b)/(z+k_j)]. On |z|=1 its
squared modulus is |z+k_j*b|^2/|b+k_j*z|^2, and denominator
minus numerator is (|b|^2-1)*(1-k_j^2)>=0. This suggests a
uniform Gaussian tail and a real central frequency, unlike the
unit-circle growing envelope. Need prove finite-comb averaging and
bound the actual Picard correction before any lower-mean claim.
No quantitative target has yet been established.

## Mid-attempt checkpoint

The balanced contour supplies |W(x+i*y)|<=exp(-n*y^2/32)
for |y|<=1/2. Its central frequency is
omega(theta)=(A/d)*integral_0^1(1-(t/R)^2)/(1+2*(t/R)*cos(theta)+(t/R)^2)dt,
with 1<omega<28/5<2*pi. Proposed limit:
R*mu_n -> 1+mean_theta S_e(omega(theta)). A second-difference
summation of the Gaussian-localized unshifted comb should give O(n^(-1/2));
the shifted-minus-unshifted correction is dominated by C*sum|e_m|.
These limit justifications are being written in full, not assumed.

A promising uniform bound for the limit correction uses sum e_m^2<=rE
<=1/(16*pi^2) and the exact Picard identity only where Phi=1. It avoids
assuming a global bound on the arbitrary cutoff Phi. On the central
frequency band [3*pi/4,5*pi/4], T's support and Parseval give a linear
cost <8/15. Low/high bump costs are <91/320 using w<=3/81920;
nonlinear residual cost <7/60. Total <299/320. Rational ancillary
bounds pass in scripts/one-sided-hankel/actual-angular-mean-bounds-214.json;
load-bearing checks, constants and both integral endpoints were inspected
with the prescribed JSON inspector. This is not numerical evidence
for the mean and is not a completed theorem until all limit/pole cases
are justified in the canonical proof.

## Completed attempt

The full proof is now canonical in
[L726](../lemmas/L726-balanced-contour-actual-angular-mean.md).
It establishes an eventual positive constant lower mean, hence the
approved exp(-n/100) target and the original-D scalar comparison.
The Gaussian exponent uses n-1>=14n/15 (n>=15); all rational checks
were rerun after recording that factor. The finite-comb limit and
Picard correction are written out in full there, not assumed from
this checkpoint. No global bound on Phi is needed: the central band
uses Parseval and T's support. Exact ancillary bounds passed and all
load-bearing reported certificate values/checks were inspected.

Outcome ADVANCE, classification POTENTIALLY_NEW only in the bounded
literature-gate sense. No certified originality or RH resolution.
Separate conceptual review remains necessary; the newly nominated
audit-source assessment is REVIEW_REQUIRED. PROOF and the canonical
ID-only DAG changed only to register this argument. Prior unfinished
work and stopped routes were preserved.
