# Lemma 879: stationary radial graphs have one phase line, with an exact odd-contact obstruction to mass equality

## Hypotheses

Use exactly L847's actual entire function, positive constants and full
holomorphic form on X=(C*)^2:

\[
 G(z)=\tfrac18\xi\left(\tfrac12+\tfrac{\sqrt z}{2}\right),
 \qquad R>0,\quad RG'(R)/G(R)=1,\quad C=R^2/G(R)^2>0,
\]
\[
 F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},
 \qquad \omega=F\frac{dz_1}{iz_1}\wedge\frac{dz_2}{iz_2}.
                                                               \tag{1}
\]

Evenness defines G without a square-root branch. In particular G is
entire and G(0)>0. Let u:T^2 -> R^2 be smooth, real and periodic, and
retain the original angular orientation dy_1 wedge dy_2. Define

\[
 z_j(y)=\Phi_u(y)_j=R e^{u_j(y)+iy_j},\quad A=Du,\quad
 H=I-iA,\quad J=\det H,\quad Q=F(\Phi_u)J,
\]
\[
 \mathcal B(u)=\langle |Q|\rangle,\qquad
 M=\langle F(\Phi_0)\rangle.                              \tag{2}
\]

Here brackets are normalized integration on T^2, with factor
(2pi)^(-2). Assume J is nowhere zero and assume exactly the following
stationarity: for every smooth real periodic vector field v with
support compactly contained in U={Q!=0},

\[
             \left.\frac{d}{dt}\mathcal B(u+tv)\right|_{t=0}=0.
                                                               \tag{3}
\]

No nonnegativity, phase alignment, connectedness of U, symmetry,
prescribed collar, finite contact census, simple-zero assumption,
existence of any particular G zero, growth bound or RH premise is
made. All actual multiplicities and the squared diagonal are retained.

## Conclusion

There is a number lambda with |lambda|=1 such that

\[
                         Q=\lambda s,
             \qquad s:T^2\longrightarrow\mathbb R\text{ smooth}.
                                                               \tag{4}
\]

This is one global complex line, not necessarily one ray. Put

\[
 P_+=\langle\max(s,0)\rangle,\qquad
 P_-=\langle\max(-s,0)\rangle.
\]

Then the full mass defect is exactly

\[
 M=\lambda(P_+-P_-),\quad \mathcal B=P_++P_-,\qquad
          \mathcal B-|M|=2\min(P_+,P_-).                 \tag{5}
\]

Under (1)–(3), the following criterion is exact:

\[
 \mathcal B>|M|
 \quad\Longleftrightarrow\quad
 \begin{gathered}
 \text{there is a point with }z_1\ne z_2\text{ at which exactly one}\\
 \text{of }G(z_1),G(z_2)\text{ vanishes, and its multiplicity is odd.}
 \end{gathered}                                           \tag{6}
\]

Any point on the right forces a whole local angular fiber of that
same G zero, with opposite phases on its two sides. Conversely a
strict mass gap forces an open fiber segment of this type. In
particular, if all G zeros encountered by the graph have even
multiplicity, then B=|M|. Simultaneous G contacts, contacts on the
squared diagonal, and their coincidences are included in (4)–(6);
they are not silently removed from the graph or its integral.

The general-Du variation is a specialization of known contour
stationarity. The actual-divisor assembly and criterion (6) are the
result of the assessed bounded attempt; the source search did not
establish their originality. The independent conceptual audit of
6 November 2026 below accepts (4)–(6) under the unchanged hypotheses.
It neither constructs a stationary graph nor excludes the odd-contact
branch. Thus it does not settle the invocation's unconditional
stationary-graph equality, the sharp L868 period bound, existence or
compactness of optimal graphs, higher mixed positivity, or RH.

## Proof

### Assessed scope, sources and distinctions from earlier contacts

The invocation-start assessment is
`drafts/literature/2026-11-06-stationary-graph-phase-components.md`,
DECISION EXPLORE. It covers one bounded test of precisely (1)–(3),
including general-Du radial accessibility and all actual divisor
contacts. Reuse its inspected standard inputs:

- Scott Lawrence and Yukari Yamauchi, *Convex optimization and contour
  deformations*, arXiv:2311.13002v2, 14 August 2024,
  [Section II B, equations (11)–(16), pp3–4](https://arxiv.org/pdf/2311.13002v2#page=3).
  Their local variation concerns a holomorphic density and invertible
  complex Jacobian, away from density zeros, and gives componentwise
  phase constancy. Their unrestricted variations do not by themselves
  justify the real radial variations here. The calculation below checks
  that specialization and its orientation; no source sufficiency,
  convergence, attainment or global perfection statement is imported.
- Victor Guillemin and Shlomo Sternberg, *Semi-classical analysis*,
  13 January 2010,
  [Sections 13.13–13.14.1, equations (13.7)–(13.9), pp449–455](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf#page=449).
  Smooth pullback differentiation applies on the compact supports used
  below. Only this variation rule is used, not Moser existence. Direct
  evaluation checks the constrained matrix and signs.
- Jiří Lebl, *Guide to Cultivating Complex Analysis*, v1.10,
  5 November 2026,
  [Theorem 2.4.7 and its finite-order factorization proof, pp49–50](https://www.jirka.org/ca/ca.pdf#page=49).
  Since G is entire and G(0)>0, its zeros are isolated, finite in every
  compact annulus, and have finite order. Factorization is used only
  near an actual encountered zero. It asserts no simplicity or finite
  set of graph contacts.

L847 supplies the exact density, angular embedding and compact-homotopy
identity <Q>=M. L878's accepted coordinate-torus descent is a comparison;
its Du=0 formula is not substituted for the calculation below. L859,
L860 and L864–L866 have nonnegative-density hypotheses and are not
premises for a sign claim here. Their local germs give no periodic
extension. The product-graph, two-period and relaxed-dual-jet stops
remain at their recorded scopes. The targeted L847–L878 search and the
named contact and period records did not contain the present criterion;
this limited comparison is not certified novelty.

### Real radial variations see the whole phase gradient

Work in local angular coordinates, putting W=y-iu, so that
z_j=R exp(iW_j) and DW=H. Let f(W)=F(R exp(iW_1),R exp(iW_2)).
It is holomorphic in these coordinates, and Q=f(W)det H. A radial
variation has delta W=-iv. Differentiating the full pullback gives

\[
                    \delta Q=-i\operatorname{div}_y(QH^{-1}v).
                                                               \tag{7}
\]

Here H^{-1} maps the coordinate-indexed vector v to a vector in
the y variables. To check the indices and all derivative terms, write
QH^{-1}=f adj(H). In two dimensions

\[
 \operatorname{adj}(DW)=
 \begin{pmatrix}W_{2,2}&-W_{1,2}\\-W_{2,1}&W_{1,1}\end{pmatrix}.
\]

The divergence of either column is zero by equality of mixed second
derivatives. Also partial_k f=sum_a f_{W_a}H_{ak}, and
sum_k H_{ak}adj(H)_{kj}=J delta_{aj}. Expanding the divergence in
(7) therefore gives

\[
 -iJ\sum_j f_{W_j}v_j-i fJ\operatorname{tr}(H^{-1}Dv),
\]

which is exactly the derivative of f(W)det H when delta W=-iv and
delta H=-iDv. These checks specialize the known variation formula;
no general contour theorem is being reproved.

For a compact support in U, Q has a positive modulus minimum on that
support. The deformed density stays nonzero there for sufficiently
small |t|, uniformly. Outside the support, v and all its derivatives
vanish, so the entire density, including its zeros, is unchanged.
Smoothness and compactness justify differentiation of the mass
integral on the support. J also stays nonzero for small |t| since
its original modulus has a positive minimum on the compact torus.

On a small nonzero patch choose a smooth phase Q=|Q|e^{i phi} and
take v compactly supported in that patch. Integration by parts in
(7), with no boundary term, gives

\[
 \delta\mathcal B(v)
  =\operatorname{Re}\langle e^{-i\phi}
                [-i\operatorname{div}(QH^{-1}v)]\rangle
  =\langle |Q|\nabla\phi\cdot\operatorname{Re}(H^{-1})v\rangle.
                                                               \tag{8}
\]

For real A the required real matrix is invertible:

\[
 \det(I+A^2)=\det(I-iA)\det(I+iA)=|J|^2>0,
 \qquad \operatorname{Re}(H^{-1})=(I+A^2)^{-1}.           \tag{9}
\]

Indeed H^{-1}=(I+iA)(I+A^2)^{-1}. Invertibility, not positive
definiteness of I+A^2, is the relevant fact. For a nonnegative smooth
bump chi in the patch, the permitted real vector field

\[
                         v=-\chi(I+A^2)\nabla\phi
\]

has derivative -<chi |Q| |grad phi|^2>. Assumption (3), with bumps
near each point, forces grad phi=0. Thus Q/|Q| is constant on each
connected component of U. Conversely this componentwise constancy
implies (3): apply (8) to a finite partition of any compactly supported
v into nonzero phase patches. This converse concerns only the
specified off-zero radial variations, not all variations through zeros.

### A finite angular arrangement covers the whole divisor

For each coordinate j, compactness gives positive finite radii
r_j^- <= |z_j(y)| <= r_j^+. The zeros of G in this closed annulus
form a finite set Z_j by the cited isolated-zero theorem. Every
G(z_j(y))=0 therefore has y_j=arg(zeta) for some zeta in Z_j.
Let A_j be these finitely many angles, adding the angle 0 if needed.

Consider the following finite union S of circles in the parameter torus:

\[
 \{y_1=a:a\in A_1\},\qquad \{y_2=b:b\in A_2\},\qquad
                         \{y_1=y_2\pmod {2\pi}\}.       \tag{10}
\]

Because J never vanishes, every zero of Q belongs to S. The last
circle is only a covering set for z_1=z_2; equality of angles alone
does not assert equality of radii. Likewise a G angular fiber need
not consist of contacts. No added circle is an actual boundary or
removed part of the graph.

The distinct circles in (10) meet in a finite set V of vertices.
Their open edges are the connected pieces of S minus V. Their
complement has finitely many connected open faces: after cutting at
the added angle-0 circles, finitely many horizontal and vertical
lines cut the square into rectangles, and the line y_1=y_2 cuts
these into polygons. Identifying opposite sides gives (10). Q is
nonzero on every face. Its phase there is constant by (8)–(9).

The adjacency graph of these faces across open edges is connected.
For example, join interior points of two faces by a piecewise linear
path on the parameter torus. Move its finitely many segments slightly
to avoid the finite vertex set, avoid travel along an edge, and meet
each encountered line transversely. It crosses finitely many open
edges, providing the desired chain of faces. This elementary
parameter construction does not deform the actual graph or delete
its divisor.

### Across a single-G edge the only possible jump is its parity

Consider an open vertical edge E and its two adjacent faces.
There is no horizontal G-angle fiber or diagonal point in E, so
G(z_2)!=0 and z_1!=z_2 along E. If Q is nonzero at any point of E,
continuity shows that the two constant face phases are equal.

Otherwise Q=0 on all E, and hence G(z_1)=0 there. The continuous
map z_1 on the connected edge takes values in the finite set Z_1;
it is therefore one constant zeta on E. Write its actual order as
m>=1 and factor G(zeta+w)=w^m g(w), g(0)!=0. At any p in E,
using y=p+te_1 and a=partial_1 u_1(p),

\[
 z_1(p+te_1)-\zeta=\zeta(a+i)t+o(|t|).
\]

The coefficient zeta(a+i) is nonzero for every real a. With
eta=z_2(p), the full density consequently satisfies

\[
 Q(p+te_1)=D t^m+o(|t|^m),\qquad
 D=-C\frac{g(0)G(\eta)(\zeta-\eta)^2}{\zeta^2\eta^2}
             J(p)[\zeta(a+i)]^m\ne0.                    \tag{11}
\]

Small positive and negative t lie in the respective adjacent faces.
Taking normalized phases in (11) gives exactly

\[
                         \psi_- =(-1)^m\psi_+ .         \tag{12}
\]

The horizontal-edge argument uses e_2 and the second G factor and
is identical with indices exchanged. The orientation and full J
are already included in (11), so no further sign is introduced.
If an edge has both contact and noncontact points, the noncontact
point already fixes equal phases; (11) applied at any contact then
shows its order must be even. No regularity or finiteness of such
contact subsets was assumed.

### The squared diagonal never flips an adjacent phase

On an open diagonal edge both G factors are nonzero, since its
intersections with the vertical and horizontal fibers are vertices.
If Q is nonzero anywhere on the edge, the phases agree by continuity.
If Q vanishes throughout, take p on the edge, with z_1(p)=z_2(p)=zeta.
Transversely varying y_1 and holding y_2 fixed gives

\[
 z_1(p+te_1)-z_2(p+te_1)
 =\zeta\bigl(\partial_1u_1(p)-\partial_1u_2(p)+i\bigr)t+o(|t|).
\]

Its coefficient is nonzero, regardless of radial tangencies. Thus

\[
 Q(p+te_1)=D_\Delta t^2+o(t^2),\qquad
 D_\Delta=-C\frac{G(\zeta)^2}{\zeta^4}J(p)
  [\zeta(\partial_1u_1(p)-\partial_1u_2(p)+i)]^2\ne0.     \tag{13}
\]

The two phases agree. This also checks any individual diagonal
contact on an edge containing noncontact points. The multiplicity
two in the full form, not a positive-density assumption, gives this
conclusion.

### Global line and all simultaneous contacts

Equations (12)–(13) and face adjacency show that every face phase
equals either lambda or -lambda, where lambda is the phase on one
chosen face. Hence Im(conjugate(lambda)Q)=0 on the union of the
faces. That union is dense in T^2, so continuity gives the same
identity everywhere, proving (4).

This argument accounts for every simultaneous or coincident divisor
contact without making a contact-rank assertion. A simultaneous
G contact must have its two angles in A_1 and A_2, hence lies in V.
A G contact on z_1=z_2 also lies in V. They are finitely many
parameter points, although the entire individual contact sets may
contain complete fibers or other nonisolated subsets. Arbitrary
actual multiplicities, either coordinate rank, and any nontransverse
behavior at these vertices are allowed. They can restrict which
graphs exist, but cannot introduce a new relative phase between
faces: the adjacency paths avoid the finite vertices and already
compare all faces. The actual density at every such point is zero;
its continuity restores the points in (4). No local positive germ
or prescribed contact jet has been asserted to extend globally.

L847's full compact-homotopy identity gives <Q>=M, including all
zeros. Integrating the positive and negative parts of (4) now gives
(5). These integrals exist since Q is continuous on the compact torus.
Both signs are present if and only if both P_+ and P_- are positive:
a nonzero signed value has an open neighborhood of the same sign.
This proves that the defect is positive exactly when s has both signs.

### Intrinsic odd-contact criterion and the unresolved branch

First suppose p is any off-diagonal contact of exactly one G factor,
of odd order m. It need not lie in an open edge of the arrangement;
its angle could also belong to an irrelevant added fiber. Isolate
the encountered G zero zeta in a small disc and choose a small
angular rectangle about p where the other G factor and z_1-z_2
stay nonzero. Suppose the vanishing factor is the first one.
Within this rectangle its only possible zero is z_1=zeta, which
requires y_1=arg zeta. Hence Q is nonzero on each of the two open
half-rectangles. Formula (11) holds at p and, since m is odd, forces
their phases to be opposite. By (4) these give open sets of both
signs of s, so (5) gives B>|M|.

In fact Q must vanish along the whole central fiber of a sufficiently
small rectangle. If it were nonzero at a point on that fiber,
continuity there would identify the phases on its two sides,
contradicting the opposite constant phases of the half-rectangles.
The isolated-label choice then forces z_1=zeta on that fiber. This
is a necessary local consequence for an already given stationary
graph, not construction of such a graph or a germ. The second
coordinate case has the same proof.

Conversely, suppose B>|M|. Then s has both signs, and two faces
have opposite phases, since faces are dense and a nonzero value
persists on an open set. Connect these faces by an adjacency chain.
Some consecutive faces have opposite phases. Their common edge
cannot have a nonzero density point and cannot be a diagonal edge
by (13). It must therefore be a full-contact vertical or horizontal
edge as in (11)–(12), with odd m. Every point of this edge is
off the diagonal, has exactly that one vanishing G factor, and
has the same fixed actual zero label. This proves the other
direction of (6), including the open-fiber assertion.

The bound sought at invocation was B=|M| for every graph satisfying
(1)–(3). The bounded attempt reduces it to exclusion of the single
odd-contact branch in (6); it does not exclude that branch. In
particular, constant phase off zeros cannot be promoted to a single
global ray merely by saying that the diagonal is squared. An exact
periodic stationary graph containing such an odd contact would be
a counterexample to that intermediate implication, but none is
provided here. Conversely the existence of actual odd G zeros or
formal contact jets alone would not provide that counterexample.
Global compatibility, graph existence and the sharp-period question
remain open. The criterion makes no RH assertion or sign assumption.

### Independent conceptual audit, 6 November 2026

The invocation-start EXPLORE assessment
`drafts/literature/2026-11-06-l879-stationary-phase-line-audit.md`
covers this audit. The audit accepts (4)–(6), including the local
whole-fiber assertion, without changing any hypothesis or repairing
any mathematical assertion. This is an independent verification of
the submitted reduction, not a new stationarity theorem or a claim
of originality. The proof above remains the full argument. The
following checks make explicit the delicate cases that were tested.

For (7), the column divergences of adj(DW), rather than its row
divergences, vanish. With the stated row-coordinate convention for H,
the holomorphic chain rule contracts H adj(H)=J I and gives the
coefficient-variation term. The derivative-of-v term in delta Q is
-i f J tr(H^(-1) Dv), with the same index convention. Thus neither a
transpose nor an extra angular-orientation sign is missing. In (8),
integration by parts contributes i grad(e^(-i phi)); this equals
e^(-i phi) grad(phi), giving the displayed positive sign. The factor
(2pi)^(-2) occurs on both sides and creates no scale change.

The identity in (9) uses real A, so I+iA is the complex conjugate of
I-iA. Their commuting product is I+A^2, whose determinant is |J|^2.
The inverse of I+A^2 is real, and taking the real part of
(I+iA)(I+A^2)^(-1) proves exactly the required real invertibility.
It is not a claim that A is symmetric or that this inverse is positive.
The test field -chi(I+A^2)grad(phi) is real and smooth on the patch;
a bump compactly supported there gives a smooth zero extension.
Its substitution in (8) is exactly the negative weighted squared
gradient. A nonzero gradient at any point would give a strictly
negative derivative for a suitable nonnegative bump, contradicting
(3). Conversely a finite smooth partition over a compact support
justifies the stated off-zero stationarity when the phases are constant.
No global phase lift or variation through a zero is used in either
direction. The positive minimum of |Q| on the support, uniform small-t
continuity there and unchanged density outside it justify the modulus
derivative under the integral. Compactness also preserves J!=0 for
sufficiently small t for each fixed test field.

For (10), compact annuli contain finitely many ambient G zeros because
G is entire and not identically zero. This fact does not assert that
their inverse images are finite. Those inverse images lie on the
listed angular circles, whose finite intersections form V. Added
angle-0 circles only subdivide faces; they add no actual zeros.
In the cut square the complement consists of finitely many polygons.
Opposite-side identifications preserve the same local angular charts
and the same transverse comparisons. A finite polygonal path between
face interiors can be perturbed to avoid V, cross the finite lines
transversely and avoid running along them. Hence the adjacency used
in the proof is connected even when an edge has the same face on
both sides. In that case the comparison merely restricts which
contact parity can occur. The complement of S is dense.

At an open vertical edge there is neither a zero of the second G
factor nor a diagonal point. If any edge point is nonzero, its single
continuous phase limit agrees with both face phases. If every edge
point is zero, connectedness forces one fixed G-zero label. In (11),
zeta!=0 and a is real, so zeta(a+i)!=0; every remaining factor of D
is nonzero by these edge hypotheses and J!=0. Consequently the
normalized one-sided limits are D/|D| and (-1)^m D/|D|. The same
expansion at an individual contact on a partial-contact edge requires
no tangency or contact-isolation assumption; equal adjacent phases
then rule out odd m. Exchanging the coordinate labels in this scalar
density calculation does not exchange the oriented differential form.

At a diagonal edge the G factors are nonzero. The coefficient of the
transverse difference has imaginary part 1 after division by zeta,
so it cannot vanish. Equation (13) therefore has exactly order two,
and the two phases agree. This includes partial diagonal contacts.
Arbitrary simultaneous-G contacts and G-diagonal coincidences occur
only at the finite vertices V. No Taylor model there is required for
(4): the edge comparisons already relate every face, and the smooth
function Im(conjugate(lambda)Q) vanishes on their dense union and hence
everywhere. Defining s=conjugate(lambda)Q gives the claimed smooth
real function, including every vertex. This proves a line, not a ray.

For the forward implication in (6), at any single odd contact the
other G factor and the diagonal factor stay nonzero in a sufficiently
small rectangle, and the vanishing factor takes values in a disc
containing only its specified zero. In a local angular lift this zero
requires exactly the central coordinate angle. The two open
half-rectangles are therefore connected nonzero patches, even if the
point lies on an irrelevant added circle or at a vertex of (10).
Equation (11) gives their opposite phases. A nonzero point on the
central fiber would identify those phases by continuity, an immediate
contradiction; the isolated label then gives the entire local contact
fiber. This does not claim continuation through another actual divisor.

For the reverse implication, a strict mass gap supplies two open sets
of opposite signs, and each meets a face by density. An adjacency
chain between those faces contains an opposite-phase pair. Its edge
cannot contain a nonzero point and cannot be diagonal. Thus it is a
whole single-G edge, of odd order by (11)–(12), and furnishes exactly
the right side of (6). No count or regularity of the remaining contacts
is inferred. Finally L847's compact parameter-cylinder Stokes argument
gives <Q>=M without requiring nonvanishing intermediate Jacobians or
removing numerator zeros. Integrating s gives (5) with both positive
parts finite. The formula and both implications also cover M=0;
there is no division by M and no assumed sign of the actual period.

The audit leaves the automatic-single-ray stop intact. It neither
realizes nor excludes an odd contact in a global stationary graph,
and gives no compactness, flow, sharp-period, higher-sign or Xi-transfer
result. L847 remains the sole direct local mathematical input; the
known variation and factorization citations above retain their scoped
roles. Positivity-based contact results and L878/L868 remain comparisons,
not extra premises. No mathematical script or numerical preview was
needed for these exact analytic and topological checks.

## Mathlib

Full matching coverage for (4)–(6), and formal coverage of the
supporting variation and factorization specializations, were not
checked in this step. No Mathlib theorem is imported. Unknown
availability is not evidence of absence. The primary citations and
the exact application obligations are recorded above.
The independent audit is informal; it does not change this Mathlib
coverage status or constitute formal verification.
