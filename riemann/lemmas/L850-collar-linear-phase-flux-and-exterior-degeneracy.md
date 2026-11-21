# Lemma 850: collar linear-phase flux and an unavoidable exterior degeneracy

## Hypotheses

Use the actual entire G, R=R_1>0, C=R^2/G(R)^2>0, full form omega,
and graph orientation of L847. In particular

\[
 F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},
 \qquad \omega=F\frac{dz_1}{iz_1}\wedge\frac{dz_2}{iz_2}.
                                                               \tag{1}
\]

Let u be any of L849(18)'s smooth real exchange-equivariant cutoff
graphs, using exactly L848's prescribed data and L849's accepted local
branch, with 0<a<b_0<epsilon_0<pi/2. Thus u=0 in an open neighborhood
of the antipodal line dist(t,s)=pi, and its full scalar density q_u
is real on the collar dist(t,s)<2a. Retain the actual-G and
analytic/trusted-software qualifications of L848/L849. For the small
additional bound below, reuse only L778(2)–(5)'s polynomial evaluator
and its step433 audit, not its zero count or Fredholm norm.

Write theta=(t,s), A=Du, F(Phi_u)=P+iQ, and sigma=Im q_u. Variations
v:T^2 -> R^2 are smooth and real. The target additionally requires
exchange equivariance and vanishing on an open smaller diagonal collar.
No nonvanishing of F or of a graph Jacobian is assumed, and no divisor
is removed. No RH or information about off-line zeros is an input.

## Conclusion

The exact first variation, including at all zeros, is

\[
 D(\operatorname{Im}q)_u[v]=-\operatorname{div}(M_u v),\qquad
 M_u=P I+Q\operatorname{adj}A
 =\begin{pmatrix}P+Q A_{22}&-Q A_{12}\\-Q A_{21}&P+Q A_{11}\end{pmatrix},
                                                               \tag{2}
\]
\[
 \det M_u=P^2+PQ\operatorname{tr}A+Q^2\det A
          =|F(\Phi_u)|^2-Q\sigma.                            \tag{3}
\]

There exists a smooth real exchange-equivariant vector field W_0,
vanishing on a smaller diagonal collar, with div W_0=sigma. This is
an application of the known support-preserving divergence theorem,
not a solution of the constrained problem. That problem is precisely

\[
                     \operatorname{div}(M_u v)=\sigma.       \tag{4}
\]

Every permitted cutoff has an exterior point where M_u is the zero
matrix. Consequently a global pointwise inverse M_u^(-1) cannot lift
an arbitrary ordinary-divergence solution. On the positive collar
off the diagonal, by contrast, det M_u=|F|^2>0. These statements retain
the collision zero and all possible zeros of G.

No admissible solution of (4), and no obstruction to its full range,
is established. The failure concerns only global pointwise inversion;
it holds for every cutoff in the stated family but does not exclude a
smooth lift after choosing or modifying W_0. The bounded attempt is
EXPLORATION against its stronger solution-or-range-obstruction test.
This is neither global reality/nonnegativity nor a mixed-minor sign.
The derivation and new small certificate have not received a separate
conceptual audit. The original POTENTIALLY_NEW classification records
only the invocation-start comparison, not certified originality.

## Proof

### Prior coverage and named imports

The unchanged invocation-start EXPLORE assessment is
drafts/literature/2026-11-06-collar-preserving-linear-phase-correction.md.
It covers the full linear operator and the constrained actual-G range
test. Reuse its primary statements and essential proof cases:

- Victor Guillemin and Shlomo Sternberg, *Semi-classical analysis*,
  manuscript dated 13 January 2010,
  [Section13.13, (13.7)–(13.9), pp449–452](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf#page=449):
  differentiation of pullbacks for smooth parameter-dependent maps,
  with contraction by the variation vector field along the map.
  Closedness of omega removes the contraction with d omega here.
  Neither the form nor the map's complex Jacobian must be nonzero.
- Pedro Teixeira, *Dacorogna–Moser theorem on the Jacobian determinant
  equation with control of support*, DCDS 37 (2017), 4071–4089,
  DOI10.3934/dcds.2017173;
  [arXiv:1608.06213v7, Section4, Theorem3/Remark3 and proof, pp8–10](https://arxiv.org/pdf/1608.06213v7#page=8):
  on a bounded connected smooth domain in R^n, n>=2, signed
  C^(r,alpha) data of zero integral vanishing on a boundary collar
  admit a C^(r+1,alpha) divergence solution zero on that collar.
  The same solution operator works across regularity indices, so
  smooth data give a smooth solution. The planar annulus and all
  data/support hypotheses are checked below. No nonlinear transport
  or unconstrained flow conclusion is imported.
- Jiří Lebl, *Guide to Cultivating Complex Analysis*, version1.10,
  5 November2026,
  [Theorem3.3.8, p79](https://www.jirka.org/ca/ca.pdf#page=79), as already
  inspected for L848: Cauchy's coefficient estimate on a closed disc
  where the function is holomorphic on a neighborhood. It is applied
  below to the entire difference G-P_0 and the radius1600 disc.

L847 supplies the exact pullback, closed-form homotopy invariance and
the C^1 Stokes input: Lebl, *Tasty Bits of Several Complex Variables*,
version4.4, 31 May2026,
[Appendix C, Theorem C.6 and regularity remark, p224](https://www.jirka.org/scv/scv.pdf#page=224).
All uses below have smooth forms and compact smooth domains.
These standard theorems are imported, not reproved. The calculation,
coordinate/support specialization and actual-G test are retained
because the inspected sources do not supply this constrained range.
The product and averaged-extension stops in L847/L848 have different
scopes and are not used as linear-range obstructions.

### Full first variation with its sign

For Phi_(u+tau v) the variation along Phi_u has components
dot z_j=z_j v_j. Put eta_j=dz_j/(iz_j). Then eta_j(dot Phi)=-i v_j
and Phi_u^*eta_j=dtheta_j-i du_j. The imported differentiation
formula, with the closed smooth omega of L847, gives

\[
 \left.\frac{d}{d\tau}\right|_0\Phi_{u+\tau v}^*\omega=d\beta,
 \qquad
 \beta=F(\Phi_u)\{v_2du_1-v_1du_2+i(v_2dt-v_1ds)\}.        \tag{5}
\]

In particular

\[
 \begin{split}
 \operatorname{Im}\beta_t&=Q(v_2A_{11}-v_1A_{21})+P v_2,\\
 \operatorname{Im}\beta_s&=Q(v_2A_{12}-v_1A_{22})-P v_1.
 \end{split}
\]

Thus Im beta=(M_u v)_2 dt-(M_u v)_1 ds and
d Im beta=-div(M_u v) dt wedge ds. This proves (2) in the original
orientation, not in midpoint coordinates. No division has occurred.
L847 gives sigma=Q(1-det A)-P tr A; expanding the determinant of
P I+Q adj A proves (3). On the positive collar q_u!=0 off the
diagonal, so F!=0 there, and sigma=0 proves the asserted invertibility.
On the diagonal F=0 is retained. The permitted v vanishes near it.

### A supported ordinary flux and the remaining constraint

L847's homotopy gives integral q_u=integral q_0. Since G has real
coefficients, q_0(-t,-s)=overline(q_0(t,s)); integration over the
torus shows integral Im q_0=0. Therefore integral sigma=0. Also
sigma=0 on dist(t,s)<2a by L849. This checks the compatibility for
ordinary divergence without claiming it sufficient for (4).

Fix 0<c<a. Remove the closed collar dist(t,s)<=2c and write the
remaining cylinder using t modulo2pi and lambda=t-s modulo2pi,
with 2c<lambda<2pi-2c. Map it diffeomorphically to the planar annulus

\[
 y=e^\lambda(\cos t,\sin t),\qquad
 e^{2c}<|y|<e^{2\pi-2c}.
\]

The orientations agree: dt wedge ds=d lambda wedge dt, whereas
dy_1 wedge dy_2=e^(2lambda) d lambda wedge dt. Set
g(y)=e^(-2lambda) sigma(t,t-lambda). It is real and smooth on the
closure of this bounded connected smooth annulus, zero on collars
of both boundary circles, and has integral zero. Choose such a collar
U contained in those zero neighborhoods. Teixeira Theorem3 gives a
smooth real Y with div_y Y=g and Y=0 on U. Its primitive
i_Y(dy_1 wedge dy_2), pulled back to the cylinder and extended by
zero across the removed collar, is a smooth real one-form beta_0
on T^2 with d beta_0=sigma dt wedge ds. Define W by
beta_0=W_1 ds-W_2 dt. Then div W=sigma, and W is zero on an open
diagonal collar. Extension is smooth because Y was already zero
on a neighborhood of each boundary.

Let E interchange the two coordinates. Exchange symmetry gives
sigma(E theta)=sigma(theta) and M_u(E theta)=E M_u(theta) E.
Consequently

\[
                W_0(\theta)=\tfrac12\{W(\theta)+E W(E\theta)\}
                                                               \tag{6}
\]

has div W_0=sigma, the same collar support property and exchange
equivariance. Thus neither this symmetry nor ordinary relative
divergence is the missing input. If a smooth supported v solves
(4) without exchange symmetry, the same averaging also supplies
an exchange-equivariant solution of (4).

A genuine correction must instead provide a smooth supported lift
M_u v=W_0+Z, where Z is a smooth divergence-free field with the
corresponding support and symmetry, or choose a suitable ordinary
flux directly. Pointwise membership in Im M_u is necessary and is
not asserted to imply a smooth lift. In the open flat exterior
A=0, so (4) is

\[
             \operatorname{div}(P v)=Q.                    \tag{7}
\]

If a smooth compact domain D lies in that flat region and its whole
boundary has P=0, the divergence theorem gives the necessary condition
integral_D Q=0. No such domain with a nonzero integral was certified
in this attempt. At a regular P-zero, (7) instead says
grad P dot v=Q, so M_u=0 at a point alone is not a range obstruction.
The global smooth lifting and all transition-region degeneracies
remain unproved.

### Qualified actual-G bounds for the exterior test

Let [p_n] be all 97 interval coefficients of L778's exact degree96
polynomial P_0, and let E_G be its saved uniform error upper endpoint.
The inherited contract is |G-P_0|<=E_G<3.141e-48 on |z|<=1600.
All three analytic tails remain in E_G, and all coefficient
uncertainties remain in the polynomial interval arithmetic.
Its theta calculation and trusted Decimal/software assumptions are
not rebuilt here. The new operations use exact Python Fraction
arithmetic on the saved rational endpoints.

Cauchy's coefficient estimate for G-P_0 gives

\[
 a_0\le p_{0,+}+E_G=:A_0,\qquad
 a_2\ge p_{2,-}-E_G/1600^2=:A_2.
\]

Exact rational evaluation yields

\[
                256^2 A_2-A_0>\frac1{1000}>0.              \tag{8}
\]

Strict positivity of all actual coefficients, from L775 as retained
in L847, implies

\[
 256G'(256)-G(256)
  =-a_0+\sum_{n\ge2}(n-1)a_n256^n
  \ge -a_0+a_2 256^2>0.
\]

The unique increasing mean-radius function xG'(x)/G(x) used to
define R in L775 tends to zero as x decreases to zero. Its value
at256 is greater than1, so 0<R<256. This is a finite-radius bound,
not a new zero-free-region assertion.

For j=0,...,255, evaluate P_0 on z in [-j-1,-j] by interval Horner
arithmetic using every coefficient interval. For intervals I,J,
their product is the interval between the minimum and maximum of
the four endpoint products, and their sum adds endpoints. These
operations contain every possible polynomial value by induction
through the finite Horner recurrence. Subtract E_G from each lower
endpoint and add it to each upper endpoint. The resulting 256
closed cells cover the entire interval, including all endpoints,
and their smallest lower endpoint satisfies exactly

\[
                   G(-x)>\frac1{100}\quad(0\le x\le256).
                                                               \tag{9}
\]

The numerical displays of the complete rational lower bounds are
0.00106733597846 for (8) and 0.0127187664132 for (9); the comparisons
to 1/1000 and 1/100, not rounded displays, are checked. No sampled
sign, root list or finite-computation extrapolation is used.

Reproduction from the notebook directory:

~~~text
python3 scripts/actual-g-radial-graph/linear_phase_exterior_bounds.py --output linear-phase-exterior-replay.json
python3 ../scripts/loop/inspect_json.py scripts/actual-g-radial-graph/linear-phase-exterior-bounds.json --pointer /checks --full
~~~

The generator refuses to overwrite existing evidence. The original
certificate is scripts/actual-g-radial-graph/linear-phase-exterior-bounds.json.
It retains the input hash, all inherited coefficient intervals and
error endpoints, every exact cell enclosure, all seven checks and
the empty failure list. The full checks and failure list were read;
the exact interval-loop implementation was inspected. Its status is
PASS_PENDING_INDEPENDENT_AUDIT, not a separate replay or conceptual
audit. The inherited analytic/software qualifications remain in force.

### An exterior singular matrix for every allowed cutoff

For every member of L849(18)'s family, the whole antipodal line
is contained in the open region u=0, Du=0. Parameterize half of it by
theta=(m+pi/2,m-pi/2), 0<=m<=pi/2. On this line put F_0=F(Phi_0).
The complete formula, with its original sign, is

\[
 F_0(m+\pi/2,m-\pi/2)
 =\frac{4C}{R^2}e^{-2im}G(iR e^{im})G(-iR e^{im}).         \tag{10}
\]

At m=0 its real part is 4C|G(iR)|^2/R^2>=0. At m=pi/2 it is
-4C G(-R)G(R)/R^2<0, because (8)–(9) give G(-R)>0 and G(R)>0.
Continuity supplies a point with P=Re F_0=0; if G(iR)=0, m=0
itself already suffices. Since M_u=P I throughout this open flat
region, M_u is the zero matrix at that point. This proof needs no
nonvanishing claim about G(iR) or other points on the radius-R circle.

The singular point therefore persists for every allowed cutoff
choice, but its possible nonzero residual Q and the derivative
terms in (7) cannot be discarded. A flux tailored to vanish with
the required smooth divisibility can still be possible. This stops
only automatic pointwise inversion after Teixeira's construction.
An admissible v, a violated full-range condition, nonlinear
convergence, global sign, other orders/shifts and RH remain open.

## Mathlib

Full matching Mathlib coverage of this actual-G constrained range
problem, the supported-flux specialization and the exterior certificate
was not checked. Supporting differential-form, matrix, integration
and complex-analysis results may exist; no formalization or absence
claim is made. The cited standard differentiation/divergence/Cauchy
inputs are imports. The informal specialization and exact rational
certificate retain their stated audit and inherited-input limits.
