# Oblique leading alias: bounded contour attempt

Prepared STEP_ID: 2026-11-02-oblique-leading-saddle-01.
Invocation-start review: `drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md` (unchanged EXPLORE).
Actual task: proof_attempt/development within the approved Fourier/residue target.

Main gap: actual-Xi all-degree mixed positivity and unbounded-height signs.
Intermediate target: on C645v's sector, with odd m>=5, n=3m,
r=27/50 and the same common unit-residue Chebyshev nodes, prove
|b_0-2b_(2m)|>=c*n^(-A)*exp(-3n/100), uniformly beyond one onset.
Together with C645v's full tail, this would give a subfamily angular
detector bound. General pole families and actual-Xi realization remain
independent gaps; C645u offers only downstream polynomial comparison.

Inputs read: C645g normalization; C645l (23) and contour justification;
C645t admissibility; full C645v proof; C645u statement. Checked the
oblique alias draft/history, the previous two-coefficient stop and
scoped oblique script references. Existing ready source comparison is
reused. No new source theorem is needed for rational differentiation
and a bounded contour test. No saddle theorem has been imported.

Test: use the continuum logarithmic derivative of the exact rational
product to locate a candidate first-alias stationary point; test a
contour through it, all competing regions, and b_0. Continue only with
a rigorous margin, informative obstruction, or a materially refined
bounded mechanism. Numerical root locations alone prove none of the
required lower bound, angular uniformity, or full mean. If contour
dominance remains unproved, preserve the exact equations and failure.

## Partial reasoning saved before enclosure work

Put v(z)=x+i*r*cos(z), a=U*u, and
J(w)=-sum_(k>=1) w^k/[k*(k+1)]. On |w|<1 this is
integral_0^1 log(1-s*w) ds. The continuous logarithmic product is

    P(v,u)=log(x/v)+J(u/x)-J(u/v)+J(v/a)-J(x/a),
    H(z,u)=P(v(z),u)-(2*i/3)*z.

The exact stationary equation for the first alias's limiting phase is

    (-i*r*sin(z))*[1/v+(a/v^2)*log(1-v/a)
                              +(1/u)*log(1-u/v)] = 2*i/3.

All logarithms here use their power series on the indicated disks;
branch and domain bounds still need certification on the new contour.
The saved nonrigorous diagnostic locates a candidate at
z approximately 4.876972288459421+0.11410424409610605*i,
with Re H approximately .0056613852 and H'' approximately
-.20186987+.17099622*i. A circular contour through it has a larger
competing maximum approximately .16710. The curve
z(t)=t-i*kappa*sin(t), kappa=-Im(z_s)/sin(Re(z_s)), instead has
sampled maximum .00566137, maximum outside |t-Re(z_s)|>=.2
approximately .00187654, and maximum Re P approximately -.0697588.
These values motivate a continuous enclosure; they do not certify it.
The second located stationary point lies outside C645v's safe annulus
and is not asserted to contribute. No completeness of the root search
is assumed. Full diagnostic: `scripts/one-sided-hankel/oblique-leading-saddle-diagnostic.json`.

Planned bounded test: enclose a simple saddle throughout the fixed
sector, bound Re H below there and above on the complementary curved
contour, and bound the local real curvature. A direct global absolute
bound on the old circular contour cannot prove dominance. The product
also needs a uniform trapezoid expansion and a nonzero local Gaussian
contribution before any asymptotic lower bound is established.

## Completed attempt

[C645w](../lemmas/C645w-oblique-first-alias-saddle-lower-bound.md)
contains the full proof. The outward decimal certificate verifies a
unique saddle in the radius .0002 disk uniformly on C645v's entire
sector rectangle, Re H(z_s)>.005, complementary phase <.004, local
real curvature<-.05, whole-contour Re P<-.06, and a local Gaussian
parameter with .18<Re a<.22, |Im a|<.20. All 1024 contour cells and
32 local cells are included in the full certificate. The first radius
.0001 failed disk invariance; that complete failed certificate is
preserved. Two earlier implementation errors stopped before a
certificate and are recorded in the canonical proof.

The exact product has a uniform trapezoid expansion with its nonzero
endpoint amplitude. The curved-contour localization, complete
complementary estimate and a Gaussian moment noncancellation inequality
give |b_(2m)|>=c*n^(-1/2)*exp(n/200) beyond one uniform onset.
b_0 is O(exp(-.06n)); C645v controls the remaining aliases. Hence the
subfamily angular detector is >=c*sqrt(n)*exp(n/200). This excludes
this fixed Chebyshev subfamily as a countersequence at exponent 1/32,
but does not settle general families, actual-Xi realization or signs.

Outcome ADVANCE: evaluated local quantitative input; no certified
novelty. C645v and C645w remain unaudited. Next continuation under the
unchanged approved target is a conceptual audit of the contour,
outward arithmetic, moving-saddle uniformity and nonzero asymptotic,
including C645v's load-bearing tail. A new creative central mechanism
should not bypass this essential audit. No new source gate is claimed.
