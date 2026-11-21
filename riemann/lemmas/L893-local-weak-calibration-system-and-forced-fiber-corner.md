# Lemma 893: local weak calibration equations and the forced simple-fiber corner

## Hypotheses

Retain L847's actual entire function and positive constants,

\[
G(z)=\tfrac18\xi(\tfrac12+\tfrac{\sqrt z}{2}),\qquad
R>0,\quad RG'(R)/G(R)=1,\quad C=R^2/G(R)^2,
\]
\[
F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},
\qquad
\omega=F\frac{dz_1}{iz_1}\wedge\frac{dz_2}{iz_2}.
\tag{1}
\]

Use L879's smooth real periodic graph u:T^2 -> R^2, with
J=det(I-iDu) nowhere zero and stationarity under smooth radial
variations supported away from its density zeros. Write

\[
\Phi_u(y)_j=R e^{u_j(y)+iy_j},\quad Q=F(\Phi_u)J,\qquad
\mathcal B(u)=(2\pi)^{-2}\int_{T^2}|Q|.
\tag{2}
\]

Condition on the nominated strip S=(l,r)x(c,d), whose closure lies
in a lifted angular chart. Its only density zeros are the complete
simple G(z1)-zero fibers y1=gamma_1,gamma_2, where
l<gamma_1<gamma_2<r. G(z2) and z1-z2 are nonzero on the closure.
L879 supplies Q=lambda*s, with |lambda|=1 and smooth real s, and
opposite phases across each simple fiber. No existence of this
actual graph or configuration is asserted.

Let N be an open neighborhood of Phi_u(closure S) in (C*)^2.
Consider a real two-form a with locally Lipschitz coefficients,
using its continuous representative. The required properties are
distributional da=0, saturation Phi_u^*a=|Q| dy1 wedge dy2 on S,
and the pointwise upper inequality

\[
a_z(E_1,E_2)\leq|\omega_z(E_1,E_2)|\quad
(z\in N,\ A\in\mathbb R^{2\times2}),\qquad
(E_j)_k=z_k(A_{kj}+i\delta_{kj}).
\tag{3}
\]

Every F=0 point and every matrix with det(I-iA)=0 is included.
There is no left-hand absolute value, reversed-plane condition,
bound on A, or differentiability assumption beyond local Lipschitz
regularity. Shrinking N to the angular chart is allowed.

## Conclusion

Put x_j=log(|z_j|/R), let y_j be the lifted angles, and define

\[
\eta=(dx_1+i\,dy_1)\wedge(dx_2+i\,dy_2),\qquad
\beta=dy_1\wedge dy_2,\qquad \omega=-F\eta.
\]

The weakly closed forms satisfying (3) are exactly

\[
a=\operatorname{Re}((q-ir)\eta)-h\beta,\qquad
h\geq0,\quad q^2+r^2\leq|F|^2,
\tag{4}
\]
with real locally Lipschitz coefficients satisfying

\[
r_{x_j}=q_{y_j},\qquad (q+h)_{x_j}=-r_{y_j}
\quad(j=1,2)
\tag{5}
\]
as distributions on N. The inequalities in (4) hold everywhere.
Saturation is equivalent to the following exact traces on the graph:

\[
h(\Phi_u(y))=0,\qquad
(q-ir)(\Phi_u(y))=-|F(\Phi_u(y))|\frac{\overline{J(y)}}{|J(y)|}.
\tag{6}
\]

In particular, at an interior point p=(gamma,y0) of either simple
fiber, put zeta=z1(p), z2^0=z2(p), a0=partial_1 u1(p), and

\[
D=-C\frac{G'(\zeta)G(z_2^0)(\zeta-z_2^0)^2}
              {\zeta(z_2^0)^2}(a_0+i)\ne0,\qquad
K=|D|\frac{\overline{J(p)}}{|J(p)|}\ne0.
\tag{7}
\]
Then every saturating form must have the trace

\[
(q-ir)(\Phi_u(p+t e_1))=-K|t|+O(t^2)\quad(t\longrightarrow0).
\tag{8}
\]
Thus its coefficient q-ir is not differentiable at Phi_u(p).
In particular no C1 form can meet the nominated requirements.
Equation (8) is compatible with a finite Lipschitz bound; it does
**not** exclude the nominated locally Lipschitz class.

If a form satisfying (4)–(6) exists on N, then every smooth real
periodic replacement u+v with support(v) compact in S, endpoint
J_(u+v) nowhere zero, and full radial homotopy
Phi_(u+tv)(closure S) contained in N obeys

\[
\mathcal B(u+v)\geq\mathcal B(u).
\tag{9}
\]
No Jacobian nonvanishing is needed along the homotopy. This is a
conditional sufficient comparison, not existence of a certificate,
necessity of dual attainment, a local minimum theorem, or a descent
direction. The full Lipschitz compatibility question remains open.
This reduction and trace obstruction have not had an independent audit.

The mixed-coordinate test of 7 November 2026, step86, adds the following
necessary conditions, not a solution of the extension problem. On the
open ambient domain, with

\[
 T=\partial_{x_1}\partial_{y_2}-\partial_{x_2}\partial_{y_1},
 \qquad b=q+h,
\]

one has Tq=Tr=Tb=Th=0 in distributions. Near an interior simple-fiber
point, translate the logarithmic coordinates so that its local complex
divisor is w1=0. After shrinking to a product neighborhood, the graph
trace and weak closure imply

\[
 h(0,w_2)=0,\qquad 0\leq h(w_1,w_2)\leq L|w_1|,
 \qquad |q-ir|\leq M|w_1|,                              \tag{17}
\]

for finite local constants L,M. This does not prove h=0 off that
divisor. The proof below gives an actual-F diagnostic satisfying both
closure directions, domination and divisor vanishing, with nonzero h;
it explicitly fails the required graph saturation. Thus it is not a
counterexample to the full-class rigidity target. That target remains
open, and these added necessary conditions are also unaudited.

## Proof

### Assessed scope, source reuse and the purpose of the specialization

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-07-weak-local-paired-strip-calibration.md`.
It explicitly covers the local weak coefficient reduction, the
simple-fiber compatibility test and the compact-chain comparison.
The pointwise algebra of L868 is reused below. Its global C1 closure
and period conclusions are not assumed at the new regularity or on N.
L847 gives the actual full form and graph tangent pair; L879 gives
the conditional stationary graph and phase information. L867 and
L888–L892 are comparisons, not additional premises for (4)–(9).

For weak Stokes import Ilmari Kangasniemi and Eden Prywes,
*On the Moduli of Lipschitz Homology Classes*, Journal of Geometric
Analysis **35**, article 88 (2025),
[Sections 3.2, 4.2–4.3, Propositions 4.2 and 4.5 and the Appendix
proof of Proposition 4.2](https://doi.org/10.1007/s12220-025-01916-6).
These passages were inspected in the invocation-start assessment.
Proposition 4.5 gives Stokes for a singular Lipschitz k-chain in an
open set U of a topologically closed Lipschitz n-submanifold M of
an oriented Lipschitz Riemannian n-manifold, for a (k-1)-form in
W^{d,infinity}_loc(U). Here n=4, k=3, M is the ambient smooth
manifold X=(C*)^2 itself, and U=N. M is closed in itself. Locally
Lipschitz coefficients and distributional da=0 meet that Sobolev
hypothesis. Proposition 4.2 and its mollification argument identify
the integrals of the continuous representative with the ordinary
chain integrals used below. No finite-p exceptional-chain theorem,
unproved restriction of ambient a.e. derivatives, or smoothing that
preserves saturation is substituted for this source.

The matrix algebra is an application of L868, weak exterior
differentiation is calculated explicitly, and the corner follows
by ordinary Taylor expansion of the smooth actual density. These
are the necessary specializations, not a reproof of weak Stokes
or a claim of a new general calibration theorem. The source search
did not supply the desired full-strip certificate or nonexistence
theorem; no originality claim is inferred from that search.

### Pointwise algebra and distributional closure

In the smooth logarithmic coframe, locally Lipschitz regularity of
a is equivalent to that of its six real coefficient functions.
L868's fixed-point calculation does not differentiate these
coefficients. For clarity, in its coframe order the evaluation is

\[
-p b+q(ad-bc)+r a+s d+t+v c,
\qquad A=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\]
Testing d=-a, c=-(1+a^2)/b for both signs of b forces p=v=0,
r=s and q+t<=0. This only uses permitted matrices with J=0.
Set h=-(q+t). With U=det A-1 and V=tr A, all (U,V) in R^2
occur, and the remaining inequality is

\[
qU+rV-h\leq|F|\sqrt{U^2+V^2}.
\]
Positive scaling in (U,V) and Cauchy–Schwarz give exactly h>=0
and q²+r²<=|F|², including F=0. This is precisely L868's
pointwise argument, so it applies to every point of N without its
global or C1 assumptions. Linear combinations of the six original
coefficients make q,r,h locally Lipschitz. Conversely (4) gives
(3) at every matrix; at J=0 its value is -h.

Expand the form in (4):

\[
a=q\,dx_1\wedge dx_2+r\,dx_1\wedge dy_2
  +r\,dy_1\wedge dx_2-(q+h)\,dy_1\wedge dy_2.
\tag{10}
\]
Distributional differentiation, using the closed smooth coordinate
one-forms, gives

\[
\begin{split}
da={}&(q_{y_1}-r_{x_1})dx_1\wedge dx_2\wedge dy_1
 +(q_{y_2}-r_{x_2})dx_1\wedge dx_2\wedge dy_2\\
 &-((q+h)_{x_1}+r_{y_1})dx_1\wedge dy_1\wedge dy_2
 -((q+h)_{x_2}+r_{y_2})dx_2\wedge dy_1\wedge dy_2.
\end{split}
\tag{11}
\]
These are the four independent coordinate three-forms. Hence da=0
is equivalent to (5) as distributions. This calculation uses no
pointwise derivative on a divisor or on the graph, and no second
derivative. It proves the local weak equivalence claimed in (4)–(5).

### Saturation and the simple-fiber test

Write g=q-ir. L847's tangent formula gives eta(E1,E2)=-J and
beta(E1,E2)=1 along the original graph. Consequently

\[
(\Phi_u^*a)/(dy_1\wedge dy_2)
   =-\operatorname{Re}(gJ)-h
   \leq |g||J|-h\leq |F||J|-h\leq|Q|.
\tag{12}
\]
If equality holds, h=0. Since |J|>0, equality in both remaining
steps forces gJ=-|F||J|, a real nonpositive number. This gives
(6), including g=0 at F=0. Conversely (6) makes every inequality
in (12) an equality. Off the density zeros the same trace is

\[
g(\Phi_u)=-\overline{Q/|Q|}\,F(\Phi_u).
\tag{13}
\]
L879 identifies the phases in (13) as opposite constants on the
two sides of each simple fiber. This alone does not provide an
extension of g or h away from the graph.

Fix p as in (7). The whole fiber z1= zeta is constant, and
G'(zeta), G(z2^0), zeta-z2^0 and both coordinates are nonzero.
Along y=p+t e1, smoothness gives

\[
z_1(y)=\zeta+\zeta(a_0+i)t+O(t^2),\qquad
F(\Phi_u(y))=D t+O(t^2).
\tag{14}
\]
In differentiating F at t=0, every term other than the derivative
of G(z1) contains G(zeta)=0. Formula (14) therefore has exactly
the nonzero D in (7), with the squared diagonal and denominators
retained. The modulus inequality gives
|F(Phi_u(y))|=|D||t|+O(t²). Since J is smooth and nonzero,
overline(J(y))/|J(y)|=overline(J(p))/|J(p)|+O(|t|).
Substitution into (6) proves (8).

The value at t=0 is zero. The right derivative of this trace is
-K and the left derivative is K. They differ because K!=0.
If g were differentiable as an ambient real function at Phi_u(p),
composition with the smooth curve Phi_u(p+t e1) would have one
derivative there, a contradiction. A C1 form has differentiable
coefficients in the smooth coframe, so cannot saturate.

This argument deliberately stops short of a Lipschitz obstruction.
A trace proportional to |t| is Lipschitz. Moreover h>=0 and h=0
on the graph do not allow one to set its ambient derivatives to
zero there: a locally Lipschitz nonnegative function need not be
differentiable on its minimum set. Nor can the ambient a.e.
equations (5) be evaluated on that lower-dimensional set. Either
shortcut would remove precisely the weak possibilities still open.

### Conditional comparison on the complete compact boundary

Let v be a nominated competitor. Orient P=[0,1]x closure S by
dt wedge dy1 wedge dy2 and define

\[
\Psi(t,y)_j=R\exp(u_j(y)+t v_j(y)+iy_j).
\tag{15}
\]
This map is smooth on a neighborhood of the compact parameter
box and is Lipschitz there. Its image is a compact subset of N
by hypothesis. Triangulating the box supplies a finite singular
Lipschitz three-chain in N. Apply the cited Proposition 4.5 with
the continuous representative of a and distributional da=0.
Its boundary integral is zero. The t=1 face has orientation
dy1 wedge dy2, and t=0 has the negative orientation. On all four
side faces v=0 in a neighborhood, so partial_t Psi=0; the
pullback two-form on each such face is zero. Internal faces of
the triangulation cancel with opposite orientations. Thus

\[
\int_S\Phi_{u+v}^*a=\int_S\Phi_u^*a=\int_S|Q|\,dy.
\tag{16}
\]
Domination (3), with A=D(u+v), bounds the left side above by
integral_S |Q_(u+v)|. The graphs and densities coincide outside
S, so adding that complement and multiplying by (2pi)^(-2)
proves (9). Degeneracy of J or new zeros of F on the homotopy
produce no extra boundary; Proposition 4.5 is a chain theorem
and does not require Psi to be an immersion. The endpoint
condition J_(u+v)!=0 is part of the nominated competitor class,
but is not needed for this sufficient inequality.

The missing step is simultaneous solvability of (4)–(6) on a
neighborhood of the whole strip. The one-fiber test has ruled out
differentiable coefficients, not all Lipschitz coefficients. No
full-strip construction, weak nonexistence theorem, mass-lowering
replacement or sharp global period bound has been established.
Graph realization, competitors leaving N, other contact types,
higher signs and actual-Xi transfer remain independent gaps.

### Mixed-coordinate compatibility and the weak divisor trace — step86

The invocation-start EXPLORE assessment for this separate attempt is
`drafts/literature/2026-11-07-actual-fiber-mixed-coordinate-defect-rigidity.md`.
It covers the full actual-G weak system and graph traces. Its inspected
Aronszajn, Bony and differential-form continuation results supply no
applicable vanishing theorem here. None is imported with weakened
hypotheses. The following are direct consequences and tests of (4)–(6),
not a reproof of a continuation or calibration theorem. The C1
zero-fiber observation in L871 is a comparison; at this regularity its
pointwise differentiation must be replaced by the test-function limit
below. The actual-density diagnostic uses L868's q=-h, r=0 template
at a new local divisor; it is not a new general construction.

Set b=q+h. Equation (5) reads r_xj=q_yj and b_xj=-r_yj.
All second derivatives in the next display are distributional. They
exist for locally integrable functions and commute, directly from
their action on smooth compactly supported test functions. Consequently

\[
\begin{split}
 Tq&=\partial_{x_1}\partial_{x_2}r
        -\partial_{x_2}\partial_{x_1}r=0,\\
 Tr&=\partial_{y_2}\partial_{y_1}q
        -\partial_{y_1}\partial_{y_2}q=0,\\
 Tb&=-\partial_{y_2}\partial_{y_1}r
        +\partial_{y_1}\partial_{y_2}r=0.
\end{split}                                                   \tag{18}
\]

Subtracting the first identity from the third gives Th=0. A related
calculation in complex notation starts with
partial_bar_j g=-h_xj/2, g=q-ir, and commutes the two bar derivatives.
It also gives Th=0, not a scalar elliptic inequality for h. Up to an
irrelevant overall sign, T has principal symbol
xi_x1*xi_y2-xi_x2*xi_y1. It takes both signs and vanishes on nonzero
covectors. In particular it is neither elliptic nor the principal
part of a real sum-of-squares operator. This does not exclude a
different scalar reduction using the remaining full constraints.

Now translate w1 so that z1=zeta*exp(w1), and translate w2 around the
chosen nonzero second coordinate. Translations of the four real
logarithmic coordinates leave (5) and the coframe unchanged.
Simple vanishing of G(zeta), with
the other factors nonzero, gives

\[
 F(w_1,w_2)=w_1H(w_1,w_2),\qquad H\text{ holomorphic and nonzero}.
                                                               \tag{19}
\]

This is the full F, with both G factors, squared diagonal and
denominators retained. Choose a smaller product neighborhood
U=D_delta x (I_x+i I_y) whose closure is in the original neighborhood
and where H has no zero. The graph fiber has w1=0 and
w2=v(y2)+i*y2, with v smooth and v(y2) in I_x for y2 in I_y,
after shrinking the intervals. Write h0(w2)=h(0,w2). Domination
forces q(0,w2)=r(0,w2)=0 on the entire complex divisor, whereas
h0=0 is initially known only on that graph curve.

To use weak closure on the divisor without restricting an ambient
a.e. derivative identity, take a smooth compactly supported test
function psi(x2,y2) and a nonnegative smooth approximate identity
rho_epsilon(x1,y1) of total integral one, supported in D_epsilon.
Test (q+h)_x2+r_y2=0 against rho_epsilon(w1)psi(w2). This gives

\[
 \int\!\!\int \rho_\epsilon(w_1)
       \bigl[(q+h)(w_1,w_2)\psi_{x_2}(w_2)
                     +r(w_1,w_2)\psi_{y_2}(w_2)\bigr]
                      \,dw_1\,dw_2=0.                   \tag{20}
\]

All integrals have compact support. Continuity is uniform there;
thus q and r tend uniformly to zero as w1 tends to zero, and h tends
uniformly to h0. Passing to the limit in (20) proves
integral h0*psi_x2=0, or (h0)_x2=0 in distributions on the rectangle.
A continuous function with this property is independent of x2:
convolve on a smaller rectangle, use the zero classical x2 derivative
of each convolution, and take the uniform limit. Overlapping smaller
rectangles give the assertion on I_x x I_y. Hence h0=H0(y2) for a
continuous H0. The full graph trace (6) gives
H0(y2)=h0(v(y2),y2)=0 for every y2 in I_y. This proves the first
part of (17) on an open part of the complex divisor.

Local Lipschitz regularity gives one finite Lipschitz constant L on
a smaller compact convex product neighborhood: a finite local cover
and subdivision of each segment give such a constant if needed.
Compare (w1,w2) with (0,w2), both in that product. Nonnegativity and
the proved trace yield 0<=h(w1,w2)<=L|w1|. Boundedness of H there
gives |g|<=|F|<=M|w1| with M=max|H|. This proves (17). It is only
linear distance control; it gives no open-set vanishing, scalar
maximum principle or infinite-order vanishing hypothesis.

For a precise limit of this reduction, on a still smaller product
with |w1|<=delta and m=min|H|>0 choose any epsilon>0 with
epsilon*delta<=m. Define the smooth real diagnostic coefficients

\[
 q_*=-\epsilon x_1^2,\qquad r_*=0,\qquad h_*=\epsilon x_1^2.
                                                               \tag{21}
\]

For j=1,2, r_*,xj=q_*,yj=0 and
(q_*+h_*)_xj=-r_*,yj=0. Both weak closure directions therefore
hold on the entire neighborhood. Also

\[
 |q_*-ir_*|=\epsilon x_1^2
 \leq\epsilon|w_1|^2\leq m|w_1|\leq|F(w_1,w_2)|.
                                                               \tag{22}
\]

It has h_*>=0 and q_*=r_*=h_*=0 on w1=0. The pointwise algebra
of (4) verifies domination for every matrix, including F=0 and J=0.
There are points x1!=0 arbitrarily close to the fiber, at which
h_*>0. This uses the varying actual density through (19)–(22),
not a replacement of F by its linear part.

It fails the full graph trace: along the nominated transverse curve,
x1=a0*t+O(t^2), so g_*=O(t^2), while (8) requires
g=-K|t|+O(t^2) with K!=0. These statements cannot agree for all
small nonzero t, including when a0=0. No stationary graph, saturating
form or counterexample to the full target has been constructed.

The bounded attempt therefore stops at (17)–(22). Mixed compatibility,
nonnegativity, exact actual-F domination and the propagated divisor
trace alone do not decide the full saturation problem. No claim is
made that the full graph data cannot supply a stronger mechanism.
These necessary conditions do not alter the earlier scoped stops or
settle the main gap.

## Mathlib

Coverage of the full local weak calibration statement, the
Kangasniemi–Prywes singular-chain Stokes theorem, and the actual-G
trace specialization was not checked. No matching Mathlib theorem
or absence claim is asserted. The coordinate exterior algebra,
Cauchy–Schwarz and finite Taylor estimates are supporting elementary
steps, not a claim that the full result is formalized.
Coverage of (17)–(22), including the weak divisor-trace limit and
mixed-coordinate compatibility, was also not checked. No absence
claim or formal verification is asserted.
