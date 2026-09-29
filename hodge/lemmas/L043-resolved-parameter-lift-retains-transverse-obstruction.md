# L043 — Resolving the parameter does not remove the fourth-direction obstruction

## Hypotheses

Retain the very-general cubic-RM surface S, operator U, elliptic
fibration, three points q_i, and spaces V_N, V_RM and V_D of
L006, L008 and L009. In particular retain L009's 21 distinct
finite nodal fibres and smooth finite diagonal-intersection fibres.
Let g:S -> S^{(3)} and K=J O_S be L042's actual norm-cycle map
and image ideal, with J having its full scheme structure.

Let p:B -> S be a finite composition of point blowups with B
smooth projective and K O_B invertible. Such a p is constructed
below with nine point blowups. Further point blowups are allowed.
Let rho:S^[3] -> S^{(3)} and let f:B -> S^[3] be the unique
lift with rho f=g p. Put A=C[epsilon]/(epsilon^2).

In the deformation test, let S_A have class kappa in V_RM and
restrict the target to S_A^[3]. Allow an arbitrary smooth
first-order deformation B_A of B and an arbitrary map
f_A:B_A -> S_A^[3] reducing to f. Do not assume that p, an
exceptional configuration, g, or an embedded image has already
deformed. Analytic compact-manifold deformations are allowed;
this includes the algebraic projective ones.

## Conclusion

The stated central lift exists after three point blowups over
each q_i. It is a lift from a smooth projective resolution of
Bl_K(S), not a lift on the original S ruled out by L042.

Even with all source motions allowed, every such f_A forces

\[
\kappa\in V_D.
\tag{1}
\]

For the nine-blowup construction, every direction of V_D does
occur. Thus the attainable induced RM target directions are
exactly V_D, of dimension three against four required. The
necessary containment (1) also holds after further point
blowups of the parameter surface.

This stops this resolved-lift recipe at first order. It supplies
no fourth-direction representative, new algebraic class or
general Hodge resolution. It does not exclude other central
support cycles, ramified families with zero first-order target
motion, or unrelated higher-dimensional cycle sources.

## Proof

**The central family away from the three triple collisions.**
Write Y=C union Delta_S with its reduced union scheme. By
L008, the normalization W of C maps finite flat of degree two
to S and is an embedding in S x S except at the three image
double points. Outside q_1,q_2,q_3 in the first factor, C is
therefore finite flat of degree two. Away from the two finite
diagonal-intersection fibres, it is disjoint from the diagonal.

At either finite intersection curve, L009 gives coordinates
u_1,w_1,u_2,w_2 and the ideal

\[
(w_2-w_1,(u_2-u_1)(u_2+u_1)).
\]

Over the first factor this part of the family has algebra
O_S[u_2]/(u_2^2-u_1^2), free of rank two. The remaining
C point is a disjoint rank-one summand. At a branch point
of W -> S disjoint from the diagonal, C itself supplies
the rank-two finite flat algebra; no reduced-fibre argument
replaces it. Hence Y over

\[
S^0=S\setminus\{q_1,q_2,q_3\}
\]

is a closed finite flat degree-three subscheme of S^0 x S.
It defines a Hilbert-cube map whose Hilbert--Chow cycle is
g on the dense distinct-support open, and therefore everywhere
on S^0 by separatedness and reducedness. L040's correctly
scoped necessity criterion implies K is invertible on S^0.

**Explicit principalization at infinity.** At q_i use L042's
formal coordinates and put D=(uv,u^3,v^3), so K=D^2.
On the first point-blowup chart u=x, v=xy,

\[
D O=x^2(y,x),\qquad K O=x^4(y,x)^2.
\tag{2}
\]

The other chart gives the symmetric formula. Thus precisely
two points on this exceptional P^1 remain nonprincipal,
the two tangent-axis points. Blow up each of them once.
On the two charts at either point, the ideal (x,y) becomes
(x) or (y), so (2) becomes principal. Elsewhere it already
was principal. These are actual points specified by tangent
lines; formal coordinates are only used to check their ideals.
Invertibility descends from the faithfully flat completed
local rings. This proves principalization by three blowups
per q_i and no blowup away from them.

For clarity, if E_0' is the strict transform of the first
exceptional curve and E_1,E_2 are the two new exceptional
curves, the local divisor of K is

\[
4E_0'+6E_1+6E_2.
\]

All multiplicities belong to the full norm ideal D^2.
Replacing K by its radical would give a different calculation.
The global blowup universal property, [Stacks Lemma 31.33.5,
Tag 0806](https://stacks.math.columbia.edu/tag/0806), factors
p through Bl_K(S). It also gives the unique lift f to the
norm-ideal blowup S^[3] identified in L040. B is smooth
projective and its map to Bl_K(S) is proper birational, so
it is a smooth resolution of that blowup.

**All source motions admit some blowdown-map deformation.**
Use the already inspected simultaneous-map criterion of
[Iacono, arXiv:0705.4532v2, Theorem 5.5 and Remark 5.12,
equation (7), pp. 9,14--15](https://arxiv.org/pdf/0705.4532v2#page=14).
For a central map r:D' -> D, a pair of first-order classes
(eta,xi) is attained by a deformation of r exactly when

\[
dr(eta)=r^*(xi)\quad\hbox{in }H^1(D',r^*T_D).
\tag{3}
\]

This imports the map framework; it is not reproved here.
To apply it to every motion of a point blowup, check the
particular differential and pullback, rather than impose
persistence of its exceptional curves as an extra premise.

For r the blowup of a smooth point, its two local charts
give Rr_*O_{D'}=O_D. The degree-zero assertion is extension
of functions on a normal surface across the omitted point.
The degree-one assertion can be checked on the ordinary
blowup of A^2: the charts have rings C[x,t] and C[s,y],
with y=xt and s=t^{-1}; their intersection has ring
C[x,t,t^{-1}]. A monomial x^a t^b, a>=0, lies in the first
chart if b>=0, and if b<0 equals y^a s^{a-b} in the second.
Thus its Cech H^1 is zero. The same computation applies
after the local flat coordinate change for a smooth surface;
away from the centre r is an isomorphism. Higher direct
images vanish as well since the fibres have dimension one.
The projection formula and Leray consequently give

\[
r^*:H^1(D,T_D)\xrightarrow{\sim}H^1(D',r^*T_D).
\tag{4}
\]

The local Jacobian of (x,t) -> (x,xt) also checks

\[
0\longrightarrow T_{D'}\xrightarrow{dr}r^*T_D
\longrightarrow i_*O_E(1)\longrightarrow0.
\tag{5}
\]

Indeed the derivative is injective and its quotient is
supported on x=0; along E its image in the constant
two-dimensional tangent space at the centre is the
tautological O_E(-1), leaving quotient O_E(1).
In particular H^1(O_E(1))=0, so every target class can
also be attained. More essentially for the present test,
for *any* eta, (4) defines a unique xi satisfying (3).
Iacono therefore supplies a deformation of r with that
source class. Its source may be identified with the given
first-order D'_A, since these classes classify the
deformations up to isomorphism.

Apply this consecutively to the given sequence of point
blowups, starting with arbitrary B_A. It constructs some
smooth deformation S'_A of S and a morphism

\[
p_A:B_A\longrightarrow S'_A
\tag{6}
\]

reducing to p. This is a consequence for all source
motions, not a restriction to deformations chosen in
advance to preserve the resolution diagram. Off the
finite set of images of the blowup centres, (6) is an
isomorphism: it is proper with isomorphic special fibre
there, hence finite there, and the unit map is an
isomorphism by flatness and Nakayama. These arguments
also apply analytically using coherent proper pushforward.

**The map's periods identify S'_A with S_A.** Let Z be the
universal length-three subscheme on S^[3] x S. Use its
degree-two incidence correspondence

\[
\mu(t)=\operatorname{pr}_{S^{[3]}*}
             ([Z]\smile\operatorname{pr}_S^*t).
\]

Pulling Z back by f gives a finite flat family on B x S.
Over the complement of the blowup-centre images it is the
family Y just identified. Thus, on that open, f^*mu(t)
is the pullback to the *first* factor of Y's correspondence.
The transpose convention must be checked: on the dense
cover chart, v -> a zeta^{-1}/v exchanges
t=v+a/v and s=zeta v+zeta^{-1}a/v, with x,y unchanged.
The reduced closure C is therefore invariant under
transposition. L009's action U+id is consequently also
the action needed for this first-factor pullback.

The point-blowup cohomology decomposition is
H^2(B,Q)=p^*H^2(S,Q) plus its rational exceptional
divisor space. This follows successively by excision
for one blowup; equivalently, restriction off a point
retains H^2(S,Q) and adds one exceptional class upstairs.
All the added classes are of type (1,1). The difference
between f^*mu|_T and p^*(1+U) is thus a rational Hodge
map from T to that exceptional divisor space. It vanishes:
a rational Hodge functional T -> Q(-1), represented via
the nondegenerate cup pairing, would give a rational
(1,1)-vector in T, and L006's Lefschetz-(1,1) argument
excludes such a vector. We have proved the full central
identity, not just an identity on holomorphic forms:

\[
f^*\mu(t)=p^*(1+U)t\qquad(t\in T).
\tag{7}
\]

The same conclusion about exceptional corrections can
also be checked on every exceptional curve: its weighted
target support is the fixed finite cycle g(p(E)), and
the incidence class of a degree-two target class restricts
to zero there. There is no extra transcendental term
from the punctual Hilbert-cube fibre.

Use the functorial first-order Hodge filtration of smooth
proper complex deformations. Under the markings, maps
and relative incidence correspondences induce the constant
central cohomology maps; they preserve the varying Hodge
filtrations. Concretely, the infinitesimal variation of
a closed holomorphic two-form omega is the class
kappa contracted with omega in H^1(Omega^1): in local
trivializations the overlap discrepancy is
Lie_D omega=d(D contracted with omega). Changes of the
map contribute coboundaries. This gives the functorial
variation formula and explains why a first-order motion
of f does not change the rational operator in (7).
For the induced Hilbert cube the universal incidence
correspondence exists relatively, so mu takes its
surface F^2 line to the target F^2 filtration in exactly
this functorial sense.

Write omega_A for the marked target period. Since kappa
preserves both NS and U, omega_A lies in T tensor A and
in the same U-eigenspace as omega. Its eigenvalue is
theta, and theta+1 is nonzero: L006's cubic has value
1 at -1. Consequently (7) and Hodge functoriality give

\[
f_A^*\mu_A(\omega_A)=(1+\theta)p^*\omega_A
     \quad\hbox{in }F^2H^2(B_A).
\tag{8}
\]

The pullback by (6) identifies the one-dimensional F^2
line of S'_A with that of B_A. Its reduction is the
usual isomorphism on holomorphic two-forms for a point
blowup, so it remains an isomorphism over A by Nakayama
and Hodge base change. In cohomology its marked map is
the same p^*. Equation (8), its nonzero scalar and the
injectivity of p^* therefore force the period lines of
S'_A and S_A to agree, including the epsilon coefficient.

Infinitesimal K3 Torelli now gives xi=kappa, where xi is
the class of S'_A. Its needed form is elementary here:
contraction with the nowhere-vanishing omega is the
sheaf isomorphism T_S -> Omega_S^1, and the derivative
of the period line is the induced map on H^1. It is
injective. The same comparison can be checked directly
without choosing normalized generators for the period lines.
If eta is the class of B_A, functorial first-order variation
for p_A, f_A and the relative incidence correspondence gives

\[
\begin{aligned}
(1+\theta)p^*(\xi\mathbin{\lrcorner}\omega)
 &=\eta\mathbin{\lrcorner}f^*\mu(\omega)\\
 &=f^*\mu(\kappa\mathbin{\lrcorner}\omega)\\
 &=(1+\theta)p^*(\kappa\mathbin{\lrcorner}\omega)
 \quad\hbox{in }H^1(B,\Omega_B^1).
\end{aligned}
\]

The last equality uses that NS-fixed RM motion puts
kappa contracted with omega in the same T-eigenspace.
Injectivity of p^* and contraction with omega gives
xi=kappa again. Equality of marked first-order deformation
classes permits an isomorphism S'_A -> S_A reducing to
id_S. Compose (6) with it. This identifies the two
factors; it was not assumed at the start.

**Recover only the punctured embedded family, then C.**
Let Q contain q_1,q_2,q_3 and the finite images of any
extra blowup centres. Over S_A minus Q, p_A is now an
isomorphism. The pullback of the universal subscheme
by f_A is finite flat of degree three over B_A and a
closed subscheme of B_A x_A S_A. On this open it gives
an A-flat embedded lift of Y in the same S_A x_A S_A.
No assertion is made about an embedded flat pushforward
at Q, about the image scheme of f_A, or about a
simultaneous normalization of the universal family.

The necessity argument in L009 works on this puncture.
The diagonal sheet selected by its lifted idempotent
defines a vector field on the complement of F_+, F_-
and Q. Its local node equations give at most simple
base-direction poles along F_+ and F_-. Hartogs extends
it as a section of T_S(F_++F_-) across Q, including
points of Q lying on either fibre. Its projection to
the elliptic base is a section of O_{P^1}(4) vanishing
at the 21 nodal values, so is zero. The polar residues
then vanish, and H^0(S,T_S)=0 forces the sheet to be
the actual relative diagonal on the puncture.

L009's local colon calculation extracts an A-flat C
there, without a colon-flatness claim at an omitted
point. By L008, N_C=nu_*N_j with W smooth and N_j a
vector bundle. Removing finitely many first-factor
points removes only finitely many points of W, since
W -> S is finite. Hartogs for N_j extends the local
ideal-deformation sections uniquely. L007's
ideal-parametrization, as used in L009, then glues a
flat embedded lift of C in all of S_A x_A S_A.
L008 forces kappa in V_D. This proves (1).

This is the additional implication missing when merely
citing L009: all source motions have been accounted
for, their blowdown period has been compared with the
target period, and only a punctured embedded family
has been used before the justified Hartogs passage.

**The three permitted directions occur.** In the actual
Dickson family, the finite normalization maps and g
vary as in L008 and L042. The three fixed points at
infinity vary as sections, and L009's finite-order
averaging coordinates linearize their order-seven
action with constant weights. The norm determinants
therefore give the same relative ideal
(uv,u^3,v^3)^2 at each section. Blow up those sections
and the two tangent-axis sections on each first
exceptional divisor. Formula (2) principalizes the
relative norm ideal in the same charts.

Away from these sections the relative Y is finite flat
of degree three: its central family is S-flat there,
its Dickson-family embedded lift is flat by L009, and
the local flatness criterion gives flatness over the
deformed parameter surface. Thus the relative image
ideal is invertible there as well. The imported
blowup property gives f_A on the deformed nine-blowup
surface. Restriction to any tangent of that family
supplies every kappa in V_D. Together with (1) and
L008's dimensions this proves the exact threshold.

The [prior SPECIALIZE assessment](../drafts/literature/2026-10-03-resolved-parameter-hilbert-cube-deformation.md)
covers the unchanged target and the inspected map,
relative Hilbert-cube and blowup framework. The explicit
principalization, all-source application, period comparison
and punctured recovery are the geometry-specific difference.
No inspected theorem was a match for this full exclusion.
Classification is POTENTIALLY_NEW only in that limited
literature sense, with no certified originality claim.
The known framework is imported, not rediscovered.

## Mathlib

Coverage: **not checked** for the full resolved-parameter
exclusion, point-blowup deformation maps, incidence
period comparison or their combination. Iacono's
Theorem 5.5 and Remark 5.12 equation (7) and Stacks
Tag 0806, directly linked above, match the imported
framework portions. Ekedahl--Skjelnes' [Corollary 7.28,
Annals 179 (2014), pp. 836--837](https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n3-p01-p.pdf#page=32)
supports the relative Hilbert-cube/blowup identification.
None is a Mathlib theorem or a match for (1).
Excision for point-blowup cohomology, cohomological
functoriality, first-order Hodge variation, the local
flatness criterion and Nakayama are named supporting
inputs; their needed geometry-specific uses are given
above. No library absence or general Hodge resolution
is asserted.
