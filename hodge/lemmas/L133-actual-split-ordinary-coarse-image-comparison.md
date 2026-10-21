# L133 — Actual split family and ordinary reduced coarse image

## Hypotheses

Retain L071's identical marked projective K3 factors S_1 and B=S_2,
their common hyperkähler metric, real class h, integral tensor tau_D
and zero-slope lattice Z k, where k^2=-14. Suppose there is a locally
free Omega-polystable rank-two F on S_1 x B with integral c_1(F)=0 and
ch_2(F)=-14e_1-21e_2-tau_D. Existence is not asserted.

Use L097's fixed very ample integral H and actual classifying morphism
f:B -> M=M_H^{ss}(2,0,-12), and L098's whole-map finiteness. Select
z in B with F_z=E=L direct sum L^{-1}, c_1(L)=k, if such a parameter
exists; put m_0=f(z). Retain L132's actual holomorphic family comparison
with the complete harmonic slice family xi over (K,0):

\[
 \alpha:(B,z)\longrightarrow(K,0),\qquad
 F|_{S_1\times(B,z)}\simeq\alpha^*\xi.                 \tag{1}
\]

Here K is the full integrability germ, not its quadratic truncation.
Its ambient harmonic space is H_+ direct sum H_-, with each summand
of dimension 26. The full automorphism group is G=(C*)^2; its effective
ratio character acts by (p,q) -> (ap,a^{-1}q). Use only L103's full-group
slice and ordinary analytic quotient inputs, not its selected first
plane, two-parameter family or degree conclusion. Write
q:K_red -> Y for the ordinary reduced analytic quotient germ.

## Conclusion

There is an isomorphism of ordinary reduced analytic germs

\[
 \Phi:(Y,q(0))\xrightarrow{\ \sim\ }(M^{an}_{red},m_0)
 \quad\hbox{with}\quad f^{an}|_{(B,z)}=\Phi\circ q\circ\alpha.
                                                               \tag{2}
\]

In particular, if I_z is the reduced analytic image germ of f from
this one source germ and J_z is that of q alpha, then Phi identifies
J_z with I_z, including their ordinary analytic structure sheaves.
More explicitly, with R=O_{M^{an}_{red},m_0}, C=O_{Y,q(0)} and
A=O_{B^{an},z}, the isomorphism Phi^*:R -> C satisfies

\[
 \ker(f^*:R\to A)=(\Phi^*)^{-1}
                   \ker((q\alpha)^*:C\to A).                 \tag{3}
\]

This conditional ADVANCE / REPRODUCTION specializes the assessed
semiversality and quotient theorems. The separate critical audit below
preserves the conclusion. It supplies no kernel F, split parameter, normality of I_z,
all-orders parity, local degree, separation, reconstruction, cycle or
transverse transport. Universal primitive Hodge realization remains
open. In particular, (2) does not import L103's degree bound for its
special chosen first plane into the arbitrary actual family.

## Proof

**Imported results and their scope.** The pre-invocation SPECIALIZE
assessment is
`drafts/literature/2026-10-19-actual-split-coarse-image-comparison.md`.
Import Greb–Toma, *Moduli spaces of sheaves that are semistable with
respect to a Kähler polarisation*, J. Éc. polytech. Math. 7 (2020),
233–261, DOI 10.5802/jep.116,
[Theorem 2.9, Proposition 2.17 and Remark 2.18, pp. 240, 245–246](https://jep.centre-mersenne.org/article/JEP_2020__7__233_0.pdf#page=8):
analytic openness of Gieseker semistability and analytic semiversality
of the actual universal family on a Quot slice at a closed polystable
point. Use the integral polarization H throughout this application.

Import Luna, *Slices étales*, Mém. Soc. Math. France 33 (1973),
81–105, DOI 10.24033/msmf.110,
[III.1, p. 97 and Remark 3, p. 98; II.2, pp. 95–96](https://www.numdam.org/item/MSMF_1973__33__81_0.pdf#page=18):
the strongly étale slice and quotient comparison at a closed orbit,
including singular ambient schemes and the complex analytic comparison.

Import Buchdahl–Schumacher, *An Analytic Application of Geometric
Invariant Theory*,
[arXiv:2008.04625v3, Definition 1, Theorems 1–3, pp. 4–8, Theorem 6, p. 11 and Section 5.2, pp. 13–15](https://arxiv.org/pdf/2008.04625v3):
restricted-action saturation and the ordinary invariant holomorphic
structure sheaf on its reduced analytic quotient. Reuse the actual
harmonic semiversality and small-slice isomorphism/orbit theorem cited
and checked in L132 and L103. These general results are imported;
we prove the family-specific comparison and image assertion below.
The weakly normal coarse-space theorem in the authors' second paper
is not used.

**The algebraic quotient chart belongs to this H.** L097 makes E a
Gieseker-polystable point for H: the two distinct line summands have
equal reduced H-Hilbert polynomials. Choose the usual semistable Quot
presentation for this H and the numerical class v=(2,0,-12), at a
framed representative t_0 of E. Its orbit is closed in the semistable
locus. One may use the GL(V) presentation with ineffective central
scalars; its orbits and quotient are those of the usual projective
linear presentation. Its stabilizer at t_0 is the full Aut(E)=G.

Take a GIT affine chart over an affine neighborhood of m_0 and the
Luna stabilizer slice T through t_0. Its universal Quot family zeta
is an actual family, with its G-linearization. Luna gives an étale
map T//G -> M near the distinguished quotient point. In analytic
germs this is an isomorphism. The associated-bundle slice map is
étale and transverse to the orbit, so Greb–Toma Proposition 2.17
applies to this Quot slice and its restricted universal family:
(T^{an},t_0,zeta) is analytically semiversal for E. Shrink about t_0
so the family is locally free. This shrinking is possible because
the non-locally-free locus is closed in S_1 times the base and its
projection is closed by properness of S_1, while the central fibre
is a bundle. Flatness is inherited from the Quot family.

We use reductions only after forming the semiversal families and
base changes. On the algebraic slice, reduction commutes with this
quotient: if N is the nilradical in its coordinate ring D, reductive
exactness gives (D/N)^G=D^G/N^G, and N^G is precisely the nilradical
of D^G. Thus (T_red//G) identifies with (T//G)_red. Analytification
and reduction give the ordinary reduced analytic quotient chart

\[
 \pi:(T^{an}_{red},t_0)\longrightarrow(Q,\bar t_0),\qquad
 \theta:(Q,\bar t_0)\xrightarrow{\sim}(M^{an}_{red},m_0).        \tag{4}
\]

No normality or smoothness of T, Q or M is required. The fixed
numerical-class part of M is open and closed and hence does not
alter this local chart.

**Two actual family base changes.** The harmonic family xi is
locally free, hence flat, and its central fibre is E. Theorem 2.9,
applied to H, allows its entire base representative to be shrunk
so every fibre is H-Gieseker-semistable. This uses no equivalence
between h-polystability and H-Gieseker-polystability for arbitrary
nearby bundles. The harmonic family is the full bundle deformation
family: H^1(O_{S_1})=0 removes scalar and diagonal tangent directions,
and the trace-free construction in L132 retains the full equations.
Thus neither family omits a determinant deformation parameter.

Analytic semiversality in both directions supplies holomorphic maps
of the full, possibly nonreduced germs

\[
 a:(K,0)\longrightarrow(T^{an},t_0),\qquad
 b:(T^{an},t_0)\longrightarrow(K,0),
 \quad a^*\zeta\simeq\xi,\quad b^*\xi\simeq\zeta.             \tag{5}
\]

These are isomorphisms of total families over their respective bases,
with central identifications chosen. They are not asserted to be
equivariant, inverse base maps or unique. Restricting (5) to reduced
bases gives the maps used below. In particular, every composite in
(5) has the same actual fibre bundle as the identity family at the
corresponding point.

**Ordinary quotient descent for the composites.** Set u=pi a on
K_red and v=q b on T^{an}_red. We check restricted invariance before
descending them.

If x and gx lie in a sufficiently small harmonic slice representative,
the actual slice families at these points are isomorphic by the
full-group slice theorem. By (5), zeta_{a(x)} and zeta_{a(gx)} are
therefore isomorphic. They give the same H-Gieseker class in M.
Since theta in (4) is an isomorphism of germs, u(x)=u(gx) on a
common small representative. This holds for every g with both
endpoints in that representative, not just for g near the identity.

If t and gt lie in a sufficiently small T representative, the
G-linearized Quot family gives zeta_t isomorphic to zeta_{gt}.
By (5) the two harmonic slice bundles at b(t) and b(gt) are
isomorphic. The small-slice isomorphism/orbit theorem of L103
applies to all sufficiently small integrable slice bundles, including
nonpolystable fibres, and places them in the same full G-orbit.
Consequently v(t)=v(gt). No equivariance of b was needed.

Here is the representative and saturation check. Choose a compact-form
invariant Hermitian ball in the harmonic representation, sufficiently
small for (5), the orbit theorem and the target coordinate charts.
The complete reduced integrability locus has the restricted action
of Buchdahl–Schumacher Definition 1. For T, choose a G-equivariant
closed affine embedding into a finite-dimensional representation,
carrying the fixed point t_0 to zero, and intersect with such a small
ball. An embedding of this kind is obtained from a finite-dimensional
G-stable set of algebra generators vanishing at t_0. T is invariant,
so its intersection has the same restricted-action property.

For either u or v, the endpoint equalities just proved extend its
coordinate functions to the saturation by the rule F(gx)=F(x).
This is well-defined: two representatives differ by a group element
with both endpoints in the original small locus. On each translated
open piece it is holomorphic by translation, and the endpoint
equalities make the functions agree on overlaps. The extensions are
G-invariant. Their images stay in the chosen target coordinate chart,
and the target equations still hold. Theorem 3, on the saturated
reduced representatives supplied by Theorems 1–2, now descends these
coordinate functions to ordinary holomorphic functions on the
quotient. The image of the original ball is a neighborhood of the
quotient base point and still represents the quotient germ, so
shrinking has not lost that germ. This constructs holomorphic maps

\[
 U:Y\longrightarrow Q,\qquad V:Q\longrightarrow Y,
 \quad Uq=\pi a,\qquad V\pi=qb.                              \tag{6}
\]

This argument uses the invariant structure sheaf in the reduced
category. Pointwise invariance alone was used only to construct the
invariant functions on saturated representatives, not as a substitute
for holomorphic descent.

**Inverse identities and the actual source map.** For x in K_red,
the families xi_{b(a(x))} and xi_x are isomorphic by (5). The harmonic
orbit theorem gives

\[
 (VU)q(x)=q b a(x)=q(x).
\]

For t in T^{an}_red, (5) gives zeta_{a(b(t))} isomorphic to zeta_t.
Their H-Gieseker classes agree; (4) then gives

\[
 (UV)\pi(t)=\pi a b(t)=\pi(t).
\]

The quotient maps are surjective on sufficiently small quotient
germs, using their saturated representatives. Thus VU and UV agree
with the respective identities on all points. Both quotient germs
are reduced; equality of coordinate functions on their points is
therefore equality of holomorphic functions. Hence U and V are
inverse holomorphic maps. Set Phi=theta U.

For the actual alpha of (1), (5) identifies (a alpha)^*zeta with
the actual family F on S_1 times (B,z). Its coarse classifying map
is therefore theta pi a alpha. To check compatibility with the
algebraic f of L097, one can choose a sufficiently large H-twist,
trivialize the locally free direct image on this small analytic base,
and use its evaluation quotient to map to the same Quot presentation.
Two such frames differ by the presentation group; the universal
family and (1),(5) give isomorphic fibres, hence identical quotient
classes. The resulting analytic map and f^{an} agree at every point.
Since B is reduced they agree as holomorphic maps, even if M is
nonreduced. Every map from B factors through M^{an}_red. Combining
this with (6) proves (2).

Finally L098 makes f finite. The analytic map germ from the selected
source point is finite onto its analytic image, so its image ideal
is exactly ker(f^*:R -> A). It is radical because A is reduced.
The same is true of q alpha by (2). Pulling (2) back to local rings
proves (3), and the quotient local rings R/ker f^* and
C/ker(q alpha)^* are identified. This is the ordinary reduced image
structure, without normalization or weak normalization.

Other parameters over m_0 have not been inserted into A or either
kernel. The reduced image of the whole finite preimage would instead
use the intersection of the corresponding one-source kernels. Its
possible additional branches do not change the assertion just proved.
No generic-degree calculation or invariant-jet truncation enters it.

**Separate critical audit, 2026-10-19 (step 410).** The pre-invocation
SPECIALIZE assessment is
`drafts/literature/2026-10-19-actual-split-coarse-image-critical-audit.md`.
The audit preserves the conditional conclusions (2) and (3). Outcome:
EXPLORATION / REPRODUCTION; no substantive error or stronger conclusion
was found. The details below check the two potentially ambiguous
applications, rather than reprove the imported general theorems.

First, the slice is taken in the actual framed Quot presentation for H.
Write P=GL(V) for that presentation group, R_0 for its semistable affine
chart, and G=Aut(E) for the stabilizer. Keeping GL rather than PGL
retains the scalar automorphisms in the sheaf stack. The associated
bundle map P x^G T -> R_0 is étale by Luna III.1, including its singular
case. At [1,t_0] its tangent map is the isomorphism

\[
 (\mathfrak p/\mathfrak g)\oplus T_{t_0}T
       \longrightarrow T_{t_0}R_0.
\]

The first summand maps onto the orbit tangent. Thus T has precisely
the tangent complement required by Greb–Toma Proposition 2.15. After
taking P-quotient stacks the associated-bundle map gives the étale
map [T/G] -> [R_0/P], preserving the central stabilizer. The affine
strongly étale chart supplies the affine local quotient presentation.
The universal Quot family is the actual object of the sheaf stack;
its restriction to T, not an unrelated deformation with the same
closed points, is the family zeta. Consequently Proposition 2.17's
formal-miniversality and analytic-semiversality proof applies to this
chosen slice. Its rank-two, projective, fixed-type hypotheses hold.
Theorem 2.9 makes the H-semistable stack open in the local deformation
problem, and properness of S_1 makes the locally free locus open.
Neither restriction discards a germ at E. L097's equal split Hilbert
polynomials establish the required closed polystable orbit.

For the other family, the complete harmonic equations and their actual
family are retained from L132. Vanishing of H^1(O_{S_1}) removes scalar
tangent parameters; the trace-free contraction retains the complete
integrability equation. This agrees with the full bundle semiversal
family of Buchdahl–Schumacher Theorem 1, not a quadratic obstruction
model. Applying the two semiversality statements yields (5) with family
isomorphisms. No equivariant or inverse choice of a and b is required.
In fact the subsequent argument needs only their restrictions to the
reduced bases; no inference about nonreduced coarse structures is made.

Here is the full saturation check for the invariant balls used above.
For either finite-dimensional ambient representation write
p:V_0 -> V_0//G and U_r={x:||x||<r}, using a maximal-compact-invariant
Hermitian norm. In this setting

\[
                  G U_r=p^{-1}(p(U_r)).                       \tag{7}
\]

The inclusion from left to right follows from invariance of p. For the
reverse inclusion, let p(x)=p(u) with u in U_r. An affine reductive
quotient fibre has a unique closed orbit contained in the closure of
every orbit in that fibre. By the Kempf–Ness minimum-norm statement
used in Buchdahl–Schumacher, Section 2.1, pp. 3–6, choose its minimum
representative w. Then ||w||<=||u||<r, and w belongs to the ordinary
closure of Gx. Since U_r is open, Gx meets U_r. Hence x belongs to
G U_r, proving (7). This argument includes the null fibre and zero.
It is specific to these norm balls, not an assertion about arbitrary
invariant open sets.

Put S=K_red in the harmonic ball, or S=T_red^an intersected with its
chosen embedding ball. Theorem 1 makes G S closed analytic in G U_r.
For any Stein neighborhood W of p(0) contained in the open p(U_r),
(7) therefore makes

\[
             \widetilde S_W=(G S)\cap p^{-1}(W)
\]

a closed invariant reduced analytic subset of the *full* preimage
p^{-1}(W). The coordinate functions extended by F(gx)=F(x) are defined
on all of G S: each translated small locus is relatively open there,
and the endpoint identities give equality on every overlap. Their
restrictions are consequently defined and holomorphic on all of
widetilde S_W. This is exactly the domain of Theorem 3, Section 2.2,
pp. 6–8, including its general reduced proof. No extension across a
missing boundary, weak normalization, or unproved replacement of a
translate union is needed. Theorem 2 makes the quotient image analytic;
its proof also shows that the small S meets every quotient class in
that image. For T, reductive exactness embeds its algebraic quotient
as the invariant closed subspace of V_0//G. The same ordinary analytic
invariant-sheaf theorem thus gives its analytification, with reduction
as verified before (4). The construction applies to both u and v.

Restricted invariance uses only the full small-slice orbit theorem,
Buchdahl–Schumacher Corollary 4.9, including its nonpolystable case.
The endpoint norms can be placed in its fixed small neighborhood
simultaneously; no bound on the intervening group element is needed.
For u, isomorphic bundles have the same H-Gieseker class. For v,
isomorphic bundles in the harmonic slice have the same full G-orbit.
These are distinct implications, and neither identifies a base-change
map itself with an equivariant map. All target coordinate equations
hold for the extended functions, so their descended functions give
maps into Q and Y, not merely into ambient coordinate spaces.

Finally shrink the two source representatives so a,b and the relevant
composites are defined. Their family isomorphisms identify b a(x) with
x as bundles, and a b(t) with t as bundles. Quotient surjectivity on
germs and reducedness then give the two inverse *holomorphic-map*
identities. Equality only on points would not justify this step for
nonreduced quotient germs. The same actual evaluation presentation of
F gives theta pi a alpha=f^an on the reduced B-germ; equality here is
independent of its chosen frame. This fixes the homomorphism to the
specific ring A=O_{B^an,z}, not just the ambient germ isomorphism.
Analytification of the finite f supplies a finite image germ at each
chosen source point. Its ideal is the pullback kernel, which is radical
because A is reduced. Thus (3) and the asserted ordinary image rings
follow. The full finite preimage would use a product of source local
rings, equivalently the intersection of their kernels, and is not being
substituted for A.

The direct mathematical inputs remain L071, L097, L098, the explicitly
restricted part of L103, and L132. No local degree, image normality,
nonempty split set, F existence, or Hodge-realization conclusion has
been added. The prior stopped metric and prescribed-jet routes are not
reopened by this audit.

## Mathlib

Full matching coverage is not checked. The analytic semiversal Quot
family, restricted harmonic quotient, invariant-sheaf descent and
family-compatible image comparison are imported and specialized from
the named primary sources above. No absence claim is made for Mathlib,
and no numerical or computational check substitutes for these inputs.
