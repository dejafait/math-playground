# Lemma 852: every collar cutoff encounters a full-form zero in its transition

## Hypotheses

Use L847's actual entire G, R>0, C>0, full form and original angular
orientation. Use precisely L848's prescribed h,b and L849's accepted
analytic branch beta(m,delta). Let u be any L849(18) cutoff, with
0<a<b_0<epsilon_0<pi/2, where the local branch has L849's positive
full density for 0<|delta|<epsilon_0. In the collar chart,

\[
 u_1=\chi(\delta)(h(m)+\delta\beta(m,\delta)),\qquad
 u_2=\chi(\delta)(h(m)-\delta\beta(m,\delta)),
 \qquad t=m+\delta,\quad s=m-\delta.                         \tag{1}
\]

Write A=Du, J=1-det A-i tr A, F_u=F(Phi_u)=P+iQ,
q_u=F_u J, sigma=Im q_u, and M=P I+Q adj A. Thus L850's
first variation is D sigma[v]=-div(Mv). Retain the qualified bounds
R<256 and G(-x)>1/100 for 0<=x<=256 from L850(8)–(9).
Their complete finite proof and implementation are checked and replayed
below. The actual-G evaluator still has L778(2)–(5)/step433's analytic
and trusted-software qualifications; it is not rebuilt here.

For the residual assertion only, use L851's smooth symmetric trial
field v_* and r_u=sigma-div(Mv_*). No simplicity, zero census,
nonzero complex Jacobian, effective collar width, RH or nonlinear
existence theorem is assumed.

## Conclusion

For every permitted cutoff there is delta_* in (a,b_0) such that at

\[
 p=(\pi,\pi-2\delta_*),\qquad
 z_1(p)=-R\exp u_1(p),\qquad G(z_1(p))=0.                    \tag{2}
\]

Here z_1(p)!=z_2(p), F_u(p)=0, q_u(p)=0 and M(p)=0.
Exchange gives another distinct full-form zero E p in the other
transition strip. These are zeros of F itself, rather than merely
zeros of Re F in the flat exterior. In particular no choice of the
allowed cutoff makes M invertible throughout its transition.

This does **not** obstruct the full linear range. At any point p where
F_u(p)=0, define real numbers

\[
 \gamma_j(p)=\operatorname{Im}
       \left[J(p)z_j(p)\partial_{z_j}F(\Phi_u(p))\right].    \tag{3}
\]

Then the original equation at p requires exactly

\[
 \gamma(p)\mathbin{\cdot}v(p)=0,                            \tag{4}
\]

and the residual equation div(Mw)=r_u at p requires exactly

\[
 \gamma(p)\mathbin{\cdot}w(p)
       =-\gamma(p)\mathbin{\cdot}v_*(p).                    \tag{5}
\]

The assignment w(p)=-v_*(p) satisfies (5), including gamma=0.
At the two points in (2) and their exchange this assignment can be
realized by a smooth real exchange-equivariant field supported inside
the transition strips. This assertion is only about the equation at
those points, not on their neighborhoods or the full torus.

The bounded attempt remains EXPLORATION against its full-solution or
full-range-obstruction test. It excludes transition pointwise inversion
but does not establish smooth lifting through the forced zeros. No
global reality, sign, mixed-positivity or RH conclusion follows. This
new local result awaits a separate conceptual audit; POTENTIALLY_NEW
records bounded literature coverage, not certified originality.

## Proof

### Scope, prior results and prerequisite checks

The unchanged invocation-start EXPLORE assessment is
`drafts/literature/2026-11-06-collar-preserving-linear-phase-correction.md`.
It covers the actual constrained operator and its zeros, with the cutoff
choice retained. Targeted searches in the relative-phase drafts,
histories, L847–L851 and the pointwise-inverse stop located no prior
transition-zero or transition-range result. L850's exterior singularity
does not imply the assertion (2). L851's exterior lift does not extend
automatically across the transition. The known relative-divergence
theorem gives an ordinary flux, without ensuring a smooth M-preimage.

Use the standard intermediate value theorem on a real compact interval.
L850's differentiation identity imports Victor Guillemin and Shlomo
Sternberg, *Semi-classical analysis*, manuscript 13 January 2010,
[Section13.13, (13.7)–(13.9), pp449–452](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf#page=449).
Its hypotheses are smooth maps and forms; the form here is closed and
the parameter derivative is a vector field along the graph. Neither
F nor J must be nonzero. Direct contraction checks the sign: its
imaginary part is (Mv)_2 dt-(Mv)_1 ds, with exterior derivative
-div(Mv) dt wedge ds. No Moser or general singular-PDE theorem is used.
The endpoint specialization and value calculation below are not
supplied by these imported results, which is why they are written out.

The positive-axis radius and negative-axis bound are L850(8)–(9),
using Cauchy's coefficient estimate as previously assessed: Jiří Lebl,
*Guide to Cultivating Complex Analysis*, version1.10, 5 November2026,
[Theorem3.3.8, p79](https://www.jirka.org/ca/ca.pdf#page=79).
The difference G-P_0 is entire and its enclosing disk has radius1600,
so that theorem applies. I inspected the full finite argument and the
complete exact-Fraction implementation in
`scripts/actual-g-radial-graph/linear_phase_exterior_bounds.py`.
Its coefficient bound gives the strict saddle sign at256, and its
256 contiguous closed interval-Horner cells cover all of [-256,0].
Every coefficient interval and the full analytic error are retained.
The fresh replay
`scripts/actual-g-radial-graph/transition-negative-axis-replay.json`
passes all seven checks with no failures: the exact saddle margin
exceeds 1/1000, and the minimum cell lower bound exceeds 1/100.
Rounded displays are 0.00106733597846 and 0.0127187664132; the
exact comparisons, not these displays, certify the bounds.

For the use of v_*, I also checked L851's entire exterior argument:
the low-mode quadratic inequality makes its phase-coordinate derivative
strictly negative off the diagonal; its coordinate field divides only
by the positive area-weight A; differentiating its integral gives
div(P_0 v_ext)=Q_0 at every Re F_0 zero. Exchange averaging and
multiplication by 1-chi preserve smoothness and give the stated support.
The complete exact-certificate implementation was inspected and replayed
to `scripts/actual-g-radial-graph/exterior-phase-transition-replay.json`.
All eight checks pass, with exact phase margin greater than 1/4000;
the complete selected rational margin was inspected. This is a
prerequisite check for the present attempt, not a separate complete
audit of the inherited evaluator or all upstream lemmas.

Reproduce the finite checks with unused output filenames; both generators
refuse to overwrite evidence:

~~~text
python3 scripts/actual-g-radial-graph/linear_phase_exterior_bounds.py --output transition-negative-axis-next-replay.json
python3 scripts/actual-g-radial-graph/exterior_phase_certificate.py --output exterior-phase-transition-next-replay.json
~~~

### A forced crossing on the negative-real slice

Consider the path

\[
 \theta(\delta)=(\pi,\pi-2\delta),\qquad
 m=\pi-\delta,\qquad 0\leq\delta\leq b_0.                 \tag{6}
\]

It stays in the collar chart. Because the first angular coordinate is
exactly pi, z_1(theta(delta)) is negative real for the entire path,
regardless of the cutoff derivatives. G has real coefficients, so

\[
 T(\delta):=G\left(-R\exp u_1(\theta(\delta))\right)       \tag{7}
\]

is a continuous real function. At delta=0, the prescribed radial
function has r(pi)=1000 and u_1(pi,pi)=h(pi)=log(1000/R).
L848's accepted sector inequality on |z+400|=600, evaluated at
z=-1000, has Im(G(z)/z)=0. It therefore gives

\[
 \frac{G(-1000)}{-1000}>\frac{14}{10^9}>0,
 \qquad T(0)=G(-1000)<0.                                  \tag{8}
\]

On 0<delta<=a the cutoff and its derivatives agree with the accepted
local branch. L849 gives q_u(theta(delta))>=K_* delta^2/2>0.
This remains true at delta=a because the cutoff is smooth and
identically one on [-a,a]; all its nonconstant derivatives there
vanish at the endpoints as well. In the full identity q_u=F_u J,
all factors are finite. Thus q_u!=0 implies F_u!=0 and consequently
G(z_1)!=0. It follows that T(delta) never vanishes on [0,a].
Continuity and (8) give T(a)<0. This argument uses the entire positive
collar, not a truncated diagonal expansion or an effective width.

At delta=b_0 the cutoff is zero, hence u_1=0 and

\[
 T(b_0)=G(-R)>1/100>0,                                    \tag{9}
\]

by R<256 and the checked negative-axis bound. The intermediate value
theorem applied to [a,b_0] supplies a zero delta_* strictly between
its endpoints. This proves (2) without locating, counting or assuming
simplicity of any zero of G.

The two angular coordinates differ by 2delta_* in (0,pi), so z_1
and z_2 cannot be equal: equality would force their arguments to agree
modulo2pi. The full formula

\[
 F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2}
\]

therefore retains the G-zero rather than replacing it by a collision
zero. Its denominators are nonzero. Hence F_u(p)=0, P(p)=Q(p)=0,
q_u(p)=0 and M(p)=0. Exchange symmetry supplies a distinct point
E p with the factors interchanged. In the local collar chart their
half-separations are delta_* and -delta_*; in L851's open-cylinder
chart these are delta_* and pi-delta_*, in its two transition strips.
No statement about all zeros or their multiplicities is needed.

This rules out a scheme that resolves the flat exterior by L851 and
then assumes a uniformly invertible matrix on the remaining transition.
It does not rule out choosing a flux that has an appropriate smooth
preimage at these zeros, nor does it exclude the original global target.

### The full equation at a form zero has no value-level obstruction

Fix any p with F_u(p)=0, not necessarily a simple zero from (2).
For a real radial variation v, dot z_j=z_j v_j. Differentiate the
exact identity q_u=F_u J. The term F_u dot J vanishes at p, so

\[
 \bigl(D\sigma_u[v]\bigr)(p)
 =\operatorname{Im}\left[
      J(p)\sum_{j=1}^2 z_j(p)\partial_{z_j}F(\Phi_u(p))v_j(p)
                     \right]
 =\gamma(p)\mathbin{\cdot}v(p).                            \tag{10}
\]

This includes a zero complex Jacobian and all multiplicities: if the
coefficient vanishes, (10) simply equals zero. Since sigma(p)=0,
the target D sigma[v]=-sigma gives (4). Combining (10) with
L850's checked sign gives div(Mv)(p)=-gamma(p) dot v(p).
In particular

\[
 r_u(p)=\gamma(p)\mathbin{\cdot}v_*(p),\qquad
 \operatorname{div}(Mw)(p)=-\gamma(p)\mathbin{\cdot}w(p),
\]

which proves (5). If exactly G(z_1) vanishes, the product formula
also gives partial_(z_2)F=0 there. In the additional case gamma_1!=0,
(4) reduces to v_1(p)=0. Neither that nonvanishing nor simplicity is
assumed or asserted for the forced crossing.

For completeness the simultaneous pointwise assignment at p and E p
does respect support and symmetry. Choose disjoint small neighborhoods
of these distinct points, with closures inside their open transition
strips, interchanged by E. A smooth scalar bump eta supported in their
union and equal to one on smaller neighborhoods can be made exchange
invariant by averaging with its composition with E. Then
w_0=-eta v_* is smooth, real, exchange-equivariant, supported in the
transition strips and has w_0=-v_* at both points. The usual smooth
bump can be built with the same exp(-1/x) cutoff used in L849(18).
Thus (5) is satisfied at those points. On neighboring points the
equation need not hold: where v_*+w_0=0 it would require sigma=0,
which has not been shown. No neighborhood solution, smooth division,
jet compatibility or range theorem follows from this value test.

The attempt has therefore exposed unavoidable full-form transition
zeros and checked the first pointwise compatibility, but has not met
its stronger global threshold. Smooth local range through these zeros,
the remaining rank degeneracies, and compatible global transition flux
remain unresolved. The original existential cutoff freedom is intact.

## Mathlib

Full matching Mathlib coverage for these actual-G transition crossings
and the constrained linear range has not been checked. No formalization
or absence claim is made. The intermediate value theorem, Cauchy bounds,
pullback differentiation and smooth cutoffs are standard inputs; their
particular application and inherited numerical qualifications are stated
above. The new transition result remains an informal, unaudited input.
