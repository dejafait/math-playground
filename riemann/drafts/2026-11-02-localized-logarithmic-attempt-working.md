# Localized logarithmic criterion — bounded mathematical attempt

Prepared STEP_ID: 2026-11-02-localized-logarithmic-research-01.
The supplied, unchanged EXPLORE assessment is
`literature/2026-11-02-localized-logarithmic-joint-moment.md`.
This invocation performs its exact target, with no new source approval.

Main gap: actual-Xi all-degree mixed positivity and unbounded-height
signs. Intermediate target: a connected angular arc of normalized
length at least n^(-2) on which the paid logarithmic mean of L649's
G_n reaches log D_single,n-n/16-C uniformly. By spatial Parseval and
logarithmic averaging this would lower-bound L651's S_n and hence its
joint projection. Matching upper bounds, Xi realization, signs and
the inherited audits remain independent.

Keep the complete L649 integer-mass family: n>=5, x=-5/4,
R=11/8, eta=1/100, t_j=j/n, common distinct poles on Re(a)=x,
|a|<=R-eta, x included, positive integer r_a, M=sum r_a<=n/3,
all n grid factors, conjugated denominator angle and normalized means.
No separation, symmetry or coefficient-integrality is assumed.

The relevant L649/L651 definitions and full reduction, C645p's
zero-continuation proof, C645x's scope, and the three prior angular
ATTEMPTS records were inspected. The supplied source comparison
already covers the imported Jensen and logarithmic-integrability
inputs; no repeat source review is required. The recorded finite
screens and ambient/fractional obstructions do not decide this target.

Continuation/abandonment test: obtain a uniform C/onset, an admissible
n-dependent sequence failing every allowed connected arc, or an
explicitly quantitatively bounded remaining term of the fully
accounted logarithmic expression. Integrability, point continuation,
a generic degree loss or a new finite screen alone is not decisive.

Unfinished reasoning saved before extended work: write
W_a(u)=(x/a) product_(1<=j<n) [(x-t_j*u)/(a-t_j*u)]
[(U*u-t_j*a)/(U*u-t_j*x)]. Its common interior angular poles are
p_j=t_j*x/U; exterior possible poles are a/t_j. W_a(0)=x/a,
so c_0(0) has positive real part, but C645p's ambient continuation
cost is too large. Any useful improvement must retain the angular
zero divisor or control spatial logarithmic loss using the actual
integer family. Denominator clearing must include all these factors,
even when individual factors cancel. No bound is claimed at this
checkpoint.

## Completed result and remaining obstacle

The canonical [L657](../lemmas/L657-localized-logarithmic-divisor-and-pole-cost.md)
contains the complete statement, proof, exact hypotheses and primary
citations. It establishes the bounded-cost branch of this attempt:
logarithmic means are legitimate, every spatial root/angular pole is
accounted for, and local denominator oscillation and diagonal localization
have explicit uniform costs. The first costs at most 8*pi/3 in the
paid expression on an n^(-2) arc; the diagonal comparison loses at most
log(30*e*pi*n). This is a finite-product specialization of the inspected
standard results, not a certified new theorem beyond those sources.

The central numerator estimate was not obtained. In L657 (8), choosing
a diagonal-maximizing center only supplies a sufficient test; its A_0
remains unbounded at the required scale. The full-circle identity (3)
likewise retains the unknown positive zero charge Z_n instead of
assuming it compensates the pole charge P_n. Neither discarding that
charge nor replacing it by a generic degree estimate reaches the
required rate. L657 is unaudited and is not a uniform lower bound for
S_n or an RH candidate. The original all-arc criterion remains open.

## Bounded diagnostic of the same logarithmic mechanism

`python3 scripts/one-sided-hankel/localized-logarithmic-screen.py`
saves all parameters, angular log means, full first-M coefficient norms,
squared-residue diagonals, selected spatial root data and limitations to
`scripts/one-sided-hankel/localized-logarithmic-screen.json`.
It tests twelve unit-residue families: n=51,99,195, M=n/3, centered
Chebyshev and uniform ordinates, each at radius 0.3 and 0.54. All include
the exact anchor and retain every grid factor and all M moments. The
spatial log quadrature uses 4096 samples and the angular circle 512.
All discrete arc lengths in the calculation exceed n^(-2), but discrete
arc optimization is not continuous arc optimization.

For uniform radius-0.3 families the apparent paid loss rates were
0.103588, 0.080871 and 0.060102, respectively, against 1/16=0.0625.
The corresponding paid margins with C=0 were about -2.0955, -1.8187
and 0.4677. These finite values do not refute an unspecified absolute
constant and onset. They give no admissible asymptotic all-arcs
obstruction. The other tested cases also gave no such obstruction.

Complete selected root-formula checks for the n=195 uniform and
Chebyshev radius-0.3 cases were inspected with the shared JSON inspector,
along with the limitations and selected reported scalar values. Those
checks compare the leading coefficient plus every root's log-plus
contribution with 4096/8192-point quadrature. Agreement is a numerical
implementation diagnostic only. No roundoff, root-location, spatial-log
quadrature or angular error is enclosed; none of these sampled numbers
enters L657. Finite parameter/nonfinite-value checks report no failures.
An initial optional import found mpmath unavailable; the completed
NumPy diagnostic does not require it, and no access workaround was used.

Stop this finite-screen batch. The next attempt keeps the exact approved
target and uses the new complete numerator accounting to test how the
integer-mass family moves its angular zeros relative to the common
poles. It must retain the spatial leading factor and roots, degree drops,
all angular divisor charges and the paid arc length. A numerator bound
at the required scale, a genuinely bounded additional cost, or an
admissible all-arcs failure is required; the choice of a diagonal peak
must not be silently promoted to necessity. L649/L651 and now L657 are
essential inputs; the full-grid component/correction from C645y/L650 and
inherited audit limitations remain. The assessment is reused unchanged.

