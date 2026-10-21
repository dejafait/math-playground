# L089 — An exact-metric stable acyclic ordinary orthogonal tensor

## Hypotheses

Let S be L052's marked smooth projective complex K3 surface with its
unchanged hyperkähler metric and real Kähler class h. Write eta for
the integral point class, and L=O_S(k), where k.h=0 and k^2=-14.
Choose any locally free algebraic rank-two h-slope-stable bundles
E and B supplied by L080 and audited L088, respectively, with

\[
\det E\simeq\det B\simeq L,\qquad
c_2(E)=-2\eta,\qquad c_2(B)=-\eta.
\]

Here strict stability tests all positive-rank proper subsheaves of
smaller rank at the exact real class h. No generic independence of
the factors, actual image bundle or common product kernel is assumed.

## Conclusion

The algebraic locally free bundle

\[
K=E\otimes B\otimes L^{-1}
\]

is strictly h-slope-stable, has rank four, trivial determinant,
c_2(K)=8 eta, and H^i(S,K)=0 for i=0,1,2. It has a perfect
holomorphic symmetric O_S-valued pairing parallel for its induced
zero-Einstein unitary connection. This connection is anti-self-dual
and hence compatible with the unchanged hyperkähler metric.

Thus it supplies an individual block with L079's K_4 requirements.
This is a REPRODUCTION specialization of the assessed connection,
holonomy, group and cohomology inputs, not a new general tensor
stability theorem or Hodge-class algebraicity. The separate critical
audit below preserves this individual-block conclusion. No identification as an actual L079 image, common
F with the full negative mixed tensor, or transverse transport follows.

## Proof

**Imported inputs and the bounded specialization.** Import the
compact-Kähler Hermite–Einstein correspondence at the chosen real
Kähler form and the line-bundle HE metric from Huybrechts,
*Lectures on K3 Surfaces*,
[author-hosted draft](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf),
Chapter 9, Section 4.2, Remark 4.8(i) and Theorem 4.9, pp. 181–182.
Import tensor Einstein functions and the parallel equality-slope
splitting/polystability criterion from Perego,
*Kobayashi–Hitchin corrispondence for twisted vector bundles*,
[arXiv:1910.01867v1](https://arxiv.org/pdf/1910.01867v1),
Propositions 3.10,3.15, pp. 47,49–50, and Theorem 4.19,
pp. 63–65. Use the ordinary case (twist one, B-field zero) on the
compact Kähler surface. The equality case includes extension of a
parallel splitting across the codimension-two singular set of a
saturated subsheaf. In particular an irreducible HE connection gives
strict slope stability; tensor HE alone gives only polystability.

For connected restricted holonomy and holonomy reduction use Nomizu,
*Reduction theorem for connections and its application to the problem
of isotropy and holonomy groups of a Riemannian manifold*, Nagoya
Math. J. 9 (1955), 57–66,
[Section I.1 and Proposition 2](https://doi.org/10.1017/S002776300002328X),
pp. 58–61; the general connectedness statement is also
Kobayashi–Nomizu, *Foundations of Differential Geometry*, vol. I,
Chapter II, Section 4, Theorem 4.2. The relevant frame bundles are
smooth principal bundles with Lie structure groups, and S is simply
connected, so full holonomy equals restricted holonomy. We take
compact closures explicitly rather than assuming holonomy is closed.
Import Goursat's subgroup description from Bauer–Sen–Zvengrowski,
*A generalized Goursat lemma*,
[arXiv:1109.0024v3](https://arxiv.org/pdf/1109.0024v3),
Theorem 2.1, p. 2. These general inputs are not reproved. The proper
projection, linked projection and tensor representation checks below
are the elementary applicability differences identified by the saved
SPECIALIZE assessment.

**The actual determinant, connection and form.** The determinant of
E is L: its integral first class is k by L080 and c_1 is injective
on Pic(S), since H^1(S,O_S)=0. This also underlies L088's determinant
identification. Fix both determinant isomorphisms. E and B have slope
zero because k.h=0; their HE connections therefore have zero Einstein
constant. Their determinant metrics give HE metrics on the same
holomorphic line L with zero constant. Two such line metrics differ
by a positive constant: the logarithm of their ratio solves the
scalar Laplace equation on compact connected S. Their Chern
connections are consequently identical. Rescale the bundle metrics
by positive constants to make both determinant metrics the same
metric on L. Use its dual metric on L^{-1}.

The induced tensor connection is the Chern connection of K and has
zero Einstein constant. Its trace curvature is
2 tr(F_E)+2 tr(F_B)-4 F_L=0. The determinant identity holds as an
identity of line bundles, not merely in rational cohomology:

\[
\det K=(\det E)^2\otimes(\det B)^2\otimes L^{-4}
\simeq\mathcal O_S.
\]

The two determinant-wedge forms define

\[
Q(e\otimes b\otimes a,\,e'\otimes b'\otimes a')
=(e\wedge e')(b\wedge b')aa',\qquad a,a'\in L^{-1}.
\]

It extends bilinearly, is symmetric because both wedge factors change
sign under interchange, and is perfect because both rank-two wedge
forms are perfect. The determinant identifications and wedge maps
are parallel for the chosen connections, so Q is parallel. This is
global ordinary normalization; no square root of L is introduced.

**Every projective projection is full.** Fix a base point and unitary
frames. Let H_E be the closure of the holonomy of E inside U(2).
Full holonomy is connected by simple connectedness of S, so its
closure is connected and compact. Its projective image is consequently
a connected closed subgroup of PU(2)=SO(3).

Every proper connected closed subgroup of SO(3) is trivial or a circle
conjugate to the rotations about one axis. Indeed, under the
identification so(3)=R^3 the bracket is the cross product. A
two-dimensional plane is not closed under that bracket; hence a
proper Lie subalgebra has dimension zero or one, and a nonzero
one-dimensional subalgebra exponentiates to such a circle. Connected
closed subgroups of dimension zero are trivial. The inverse image
of a circle in U(2) is conjugate to the diagonal unitary torus, and
the inverse image of the identity is scalar. In either proper case
H_E preserves a complex line in C^2.

An invariant line gives a global parallel line subbundle by parallel
transport (path independence follows from holonomy invariance).
Its (0,1) operator is the induced one, so the subbundle is holomorphic.
Its induced connection has zero Einstein constant, hence degree zero.
It contradicts E's strict h-stability. Thus the projective image of
H_E is all SO(3). The identical argument applies to B. This checks
the proper projections, including projectively flat factors, without
assuming either individual holonomy group is already closed.

**The linked joint case is impossible.** Let H be the compact closure
of the joint holonomy of the direct-sum connection on E and B in
U(2) x U(2), and let P be its projective image in SO(3) x SO(3).
Both projections of P are surjective: projections of compact closures
are precisely the closures of the projected holonomy. P is connected
and compact. The normal kernels in Goursat's description are closed
normal subgroups of SO(3). Such a subgroup is either trivial or all
SO(3): its Lie algebra is an ideal in simple so(3); if that ideal is
zero it is discrete, and conjugation by connected SO(3) fixes each
element, so it lies in the trivial center.

Goursat therefore leaves exactly two cases: P is the full product,
or it is the graph of an automorphism alpha of SO(3). In the latter
case alpha is continuous: the first projection of its compact graph
is a continuous bijection to Hausdorff SO(3), hence a homeomorphism.
A continuous Lie-group automorphism has a Lie-algebra isomorphism
d alpha intertwining the two adjoint actions. It identifies the
traceless skew-Hermitian endomorphism fibres for E and B as joint
holonomy representations. Parallel transport extends this intertwiner
to a global parallel real adjoint-bundle isomorphism; complexification
identifies End_0(E) and End_0(B). In particular their second Chern
classes must agree. It is not enough here merely that E and B are
nonisomorphic.

For rank two with first class k, the root calculation gives

\[
\operatorname{ch}(\operatorname{End}_0 V)
=3+(k^2-4c_2(V)),\qquad
c_2(\operatorname{End}_0 V)=4c_2(V)-k^2.
\]

To check the expression, if the roots are x,y, the traceless End
roots are 0,x-y,y-x, so ch_2=(x-y)^2=k^2-4c_2(V).
For E the second Chern class is 6 eta; for B it is 10 eta.
They differ in H^4(S,Z)=Z eta. Thus the graph case is impossible,
and P=SO(3) x SO(3).

**Irreducibility and strict exact-h stability.** Equality of the
determinant connections means every (g_E,g_B) in H satisfies
det(g_E)=det(g_B). K's holonomy closure is the image of H under

\[
\rho(g_E,g_B)=g_E\otimes g_B\,(\det g_E)^{-1}.
\]

For a Lie-algebra pair (X,Y), write
X=X_0+(tr X)I/2 and Y=Y_0+(tr Y)I/2. Since tr X=tr Y,

\[
d\rho(X,Y)=X_0\otimes I+I\otimes Y_0.
\]

Surjectivity onto both projective factors jointly makes the image
of this Lie algebra the full tensor action of su(2) plus su(2).
Its complexification is the standard action of sl_2(C) plus
sl_2(C) on C^2 tensor C^2. This action is irreducible: the two
diagonal Cartan operators have four distinct joint one-dimensional
weight spaces; an invariant subspace splits into these spaces, and
the raising and lowering operators in the two factors connect each
of the four to all the others. Any nonzero invariant subspace is
therefore the entire tensor space. Thus the actual HE connection
on K is irreducible. The imported equality-slope splitting theorem
now gives strict h-stability, including saturated subsheaves initially
singular at finitely many points. No integral replacement for h or
unproved generic-holonomy choice is used.

For compatibility, the zero-Einstein Chern curvature on the surface
is an endomorphism-valued primitive (1,1)-form, hence anti-self-dual.
Pointwise on a hyperkähler four-manifold the self-dual two-forms are
spanned by its three Kähler forms. Their orthogonal complement is
primitive (1,1) for every induced complex structure. Thus this same
connection remains of type (1,1) and zero contraction throughout
the fixed hyperkähler sphere. Q remains parallel for that connection.

**Full character and actual cohomology.** All surface characters
terminate in degree four. The two factors and the normalization have

\[
\operatorname{ch}(E)=2+k-5\eta,\quad
\operatorname{ch}(B)=2+k-6\eta,\quad
\operatorname{ch}(L^{-1})=1-k-7\eta.
\]

First their product is 4+4k-36 eta. Multiplying by the last factor
gives rank four, first class zero and second character

\[
-36\eta-4k^2+2k^2=-8\eta.
\]

Consequently ch(K)=4-8 eta and c_2(K)=8 eta, the required value.
The exact determinant identity above separately verifies integral
first-class vanishing.

Rank-two determinant duality gives E^vee=E tensor L^{-1}, so
K=Hom(E,B) as an actual holomorphic bundle. Apply the equal-slope
stable-Hom constraints (Perego, Proposition 4.15 and Corollary 4.16,
pp. 61–62). Here the endpoint vanishing can also be checked directly
with the actual ranks and determinants: a nonzero map E to B of
generic rank one has a rank-one kernel of negative h-degree by
stability of E. Its rank-one image then has positive degree, contrary
to stability of B. A map of generic rank two has determinant a
nonzero global section of Hom(det E,det B)=O_S, hence a nonzero
constant. It is everywhere an isomorphism, impossible since their
second Chern classes differ. Thus H^0(K)=Hom(E,B)=0. The same
argument gives H^0(K^vee)=Hom(B,E)=0.

Serre duality on S, with omega_S=O_S, gives H^2(K)=0; use
Hartshorne, *Algebraic Geometry*, III, Theorem 7.6. K3 RR is
Huybrechts, Chapter 1, Section 2.4, (2.6), p. 13:
chi(K)=2 rank(K)+ch_2(K)=8-8=0. With both endpoint groups zero
this forces H^1(K)=0. The Euler identity is used only after actual
endpoint vanishing. Every chosen pair E,B has these conclusions;
no extra selection of B or cohomological genericity is needed.

**Scope and traps.** The construction realizes one individual stable
acyclic symmetric K_4 at the specified h. It does not assert that
O_S plus K occurs as an actual image of any F, or match it jointly
with the independently constructed opposite block. Different adjoint
charges exclude a linked holonomy representation only after its
parallel bundle identification is established. A tensor of stable
bundles is not presumed stable, and no square-root determinant or
injectivity of complexification in real K-theory is used. No
characteristic-class computation here proves common-kernel existence
or Hodge-class algebraicity. ATTEMPTS/056's necessary-index stop
remains valid; this is a different constructive test.

**Independent critical audit (2026-10-11).** This audit uses the
unchanged SPECIALIZE coverage for this exact construction. It finds
no substantive error or stronger conclusion. It is EXPLORATION /
REPRODUCTION, not a second existence advance. The following checks
are applications of the precisely cited inputs above; the HE,
holonomy and K3 existence theorems are not reproved.

First, the only numerical inputs from L052, L080 and L088 are the
same actual S and h, k.h=0, k^2=-14, and the two locally free stable
rank-two bundles of determinant L and charges -2 and -1. Neither
the conditional existence of F in L052's other assertions nor an
actual image is an input. Simple connectedness is the K3 property.
The determinant isomorphisms are holomorphic. For any initially
chosen HE metrics, their determinant metrics, transferred to L,
have the same zero contraction. Their logarithmic ratio is globally
defined and harmonic, hence constant. Constant metric rescaling does
not change either Chern connection. Thus the equality of determinant
connections is global, including holonomy; it is stronger than equality
of their de Rham first classes. Tensoring by the actual L^{-1} cancels
the determinant connection and makes both wedge factors combine to a
parallel symmetric form. No local square roots need to glue. The
line identity for det(K) proves integral determinant triviality.

For the proper-projective case, the closure of connected holonomy
is still connected. Its compact projection is closed; a dense
nonclosed subgroup is not being classified as a Lie subgroup. The
inverse image of a connected proper projective subgroup preserves
a line in the standard two-dimensional representation, even when
the unitary centre is nontrivial. Parallel transport of that line
gives a smooth parallel subbundle on all of S. Its induced (0,1)
operator gives a holomorphic subbundle and its contracted curvature
is zero. It therefore violates strict stability at the same h.
This eliminates both a circle and the trivial projective group.

In the joint case compactness ensures surjectivity of the projection
of the closure onto each individual closure. Goursat's kernels are
closed normal subgroups of SO(3), not arbitrary Lie-algebra ideals;
the proof also eliminates discrete kernels using the trivial centre.
In a graph case, compactness gives continuity of the automorphism,
and its differential intertwines Ad(g) with Ad(alpha(g)). Central
unitary elements act trivially on both adjoints. Consequently this
intertwiner is invariant under the full actual joint holonomy. Its
parallel extension is well-defined along every loop and identifies
the real adjoint bundles; complexifying gives an isomorphism of
their underlying complex bundles. A smooth complex isomorphism
already forces equality of Chern classes, so no additional
algebraic-holonomy comparison is needed. The independently checked
values 4(-2)-(-14)=6 and 4(-1)-(-14)=10 contradict that equality.

The surviving compact joint group maps onto SO(3) x SO(3).
A surjective smooth homomorphism of compact Lie groups has
surjective differential here: its Lie-algebra image is the Lie
algebra of its closed image. On the equal-determinant subgroup,
the scalar parts of d rho cancel exactly. Hence the complexified
image is the full sl_2 plus sl_2 tensor action. The joint Cartan
weight decomposition and the two independent raising/lowering
actions exclude every proper complex invariant subspace. A subspace
invariant under actual holonomy would also be invariant under its
closure, so this proves irreducibility for the actual connection.
Perego's equality case applies to all saturated subsheaves, including
the codimension-two extension issue. Nonsaturated destabilizing
subsheaves would destabilize after saturation as well. Thus the
conclusion is strict real-h stability, not just tensor polystability.
The primitive (1,1) curvature is anti-self-dual coefficient by
coefficient on the Kähler surface, giving the claimed compatibility.

Finally, independently multiply the surface characters: the first
product has degree-four coefficient -10-12-14=-36 and first class
4k. The twist contributes 4(-7)-4k^2=-28+56, leaving -8.
The result is exactly rank four, c_1=0 and c_2=8 eta. The actual
isomorphism E^vee=E tensor L^{-1} identifies K with Hom(E,B), not
merely its character. For a rank-one map, the torsion-free kernel
and image have degrees adding to zero; their opposite required
signs contradict strict stability. For a full-rank map, the global
determinant is a nonzero constant and hence has no zero locus,
including at isolated points. The unequal second classes exclude
that isomorphism. Reversing E and B checks the dual endpoint as
well. Serre duality gives H^2=0, and only then does chi=8-8=0
give H^1=0. These checks apply to every pair allowed in the
hypotheses, without a genericity or semicontinuity assumption.

The individual K_4 conclusion survives. Its occurrence in an actual
L079 image, a common F, and transverse transport remain unproved.
The direct mathematical inputs remain L052, L080 and L088; L079
specifies downstream requirements and is not an existence premise.

## Mathlib

Full matching normalized-tensor existence, analytic joint-holonomy,
real-polarization stability and K3 acyclicity coverage: not checked.
Supporting Mathlib coverage is not checked; no matching declaration
or absence is asserted. The precise mathematical sources above are
the assessed inputs. No formal verification or originality is claimed.
