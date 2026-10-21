# L100 — Stable equality-family map is locally totally geodesic at the fixed metric

## Hypotheses

Retain L097/L098's identical marked projective K3 factors S_1 and
B=S_2, fixed common hyperkähler metric g, ordered structures I,J,K,
real Kähler class h, and Omega=p_1^*h+p_2^*h. Suppose F is locally
free of rank two, Omega-slope-polystable, with integral c_1(F)=0 and

\[
 \operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D,
 \qquad D[\sigma]=2\lambda[\sigma],\quad 1<\lambda<5/4.
\]

Use its actual hyperholomorphic unitary connection and the all-fibre
harmonicity and norm of audited L095, as interpreted also in L098's
audit. No split fibre need exist. Let Z be L096's finite, possibly
empty nonstable set, U=B minus Z_red, and let
f:B -> M_H^{ss}(2,0,-12) be L097's actual common-H map. On U its
fibres are locally free h- and H-slope-stable and its target points
are Gieseker-stable. Use L098's natural coarse/actual-family tangent
comparison. The auxiliary H does not define the metric below.

In a connection-moduli chart near a stable restricted connection A,
normalize the real harmonic L2 metric by

\[
 G_A(a,b)=-\frac{1}{4\pi^2}\int_{S_1}
                \sum_j\operatorname{Tr}(a(f_j)b(f_j))\,dVol_g,
                                                        \tag{1}
\]

for real skew-adjoint ASD-harmonic one-forms and a g-orthonormal fibre
frame. This is a fixed positive constant normalization of the natural
L2 metric. The charts are identified with the actual stable algebraic
coarse germs below; that identification is a conclusion of the proof,
not an additional hypothesis. F existence, completeness, global
embedding and separation are not assumed.

## Conclusion

At every y in U the actual map, expressed in the smooth fixed-metric
connection chart, is quaternionic and immersive, with

\[
 df\circ L_B=L_M\circ df\quad(L=I,J,K),\qquad
                      f^*G=2\lambda g|_U.                \tag{2}
\]

Every local embedded branch is totally geodesic. For the parametrized
map and the original source Levi--Civita connection,

\[
 \nabla^{f^*TM}_u(df(v))=df(\nabla^{g}_u v)\quad\text{on }U. \tag{3}
\]

Thus its second fundamental form is zero on U. With another fixed
positive L2 normalization G'=c_0G, its scale is c_0 2lambda>0 and
the connection conclusion is unchanged. This is a conditional
ADVANCE / REPRODUCTION of assessed known tools. The separate critical
audit below preserves it. No assertion is made at Z or about coincident branches,
normality, original-image separation, kernel existence, reconstruction,
transport or universal primitive Hodge realization.

## Proof

**Imported inputs and differences from earlier work.** Reuse the
pre-invocation SPECIALIZE assessment
drafts/literature/2026-10-13-equality-stable-local-geodesy.md.
L067 supplies a methodological comparison only; its charge-seven
family conclusion is not an input. The changed equality family,
stable open and raw normalization are checked here.

Import Verbitsky, *Hyperholomorphic bundles over a hyperkahler
manifold*, [alg-geom/9307008v1, 29 July 1993, Definition 6.3 and
Theorems 6.1--6.4, Section 7 through Corollary 7.1, Section 9 and
Corollary 10.1, PDF pp. 22--28, 34--37](https://arxiv.org/pdf/alg-geom/9307008v1#page=22).
These supply local natural classifying families and tangent maps,
stable/irreducible connection comparison, smooth surface moduli and
its harmonic L2 hyperkähler structure, including rotations through the
same connections. Import Huybrechts--Lehn, *The Geometry of Moduli
Spaces of Sheaves*, E31 (1997), [4.5.1--4.5.4, pp. 101--102](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=113)
for the actual étale-slice family, natural tangent and trace-free
smoothness; use [3.A.1 and the following openness statement,
p. 74](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=86)
for slope stability. L097's uniform h/H equivalence imports Greb--Toma,
*Compact moduli spaces for slope-semistable sheaves*, Algebraic Geometry
4 (2017), [Theorem 6.6 and Section 6.3.3, pp. 74--75](https://content.algebraicgeometry.nl/2017-1/2017-1-003.pdf#page=35).
These general results are not reproved.

**The actual stable connection germ.** Fix y in U and E=F_y. The
restricted connection A_y is hyperholomorphic and has zero contraction
for every induced fibre Kähler form by L097's retained connection input.
It is irreducible: a parallel orthogonal decomposition would give
proper holomorphic zero-slope summands at I, contradicting h-stability.
For every induced L, simultaneous product rotation integrates the
(0,1)_L part of the same F connection to an actual holomorphic bundle
on S_{1,L} x B_L. Its restrictions integrate exactly A_z, and
irreducibility and zero contraction make these restrictions stable
for the rotated metric. This argument is local on the underlying open
U and requires no rotated projectivity or integral polarization.

Smooth unitary identifications of the fibres over a small base ball
produce a smooth family of vertical connections on one fixed bundle.
Its connection-moduli map is phi(z)=[A_z]. Changing identifications
changes only the unitary gauge representatives. The imported rotated
classifying charts identify the same nearby classes [A_z] with their
induced complex structures, rather than unrelated abstract Ext spaces.

At any stable E on the K3, Hom(E,E)=C and Serre duality gives
Ext^2(E,E)=C. The dual trace map is the scalar inclusion
H^0(O_{S_1}) -> Hom(E,E), an isomorphism; hence Ext^2(E,E)_0=0.
Also H^1(O_{S_1})=0, so fixing determinant removes no tangent.
Huybrechts--Lehn 4.5.3--4.5.4 make the full algebraic stable germ
smooth. The numerical-class part is open and closed by L097. The
imported surface statement makes the corresponding analytic
connection germ smooth with full natural Ext^1 tangent. Full Ext^2
does not vanish and is not the criterion being used. The same
connection/surface construction applies under rotation.

**Compare actual germs at I.** The proof of Huybrechts--Lehn 4.5.1
supplies an étale slice T -> M^s through a Quot point for E, carrying
the restricted actual Quot family Q. Shrink T so that Q is locally
free and H-slope-stable: these are open conditions in this flat
proper surface family, and the central fibre has both properties.
All its fibres have the fixed surface Chern invariants. L097's
uniform fixed-invariant relative-stratum comparison identifies
H-slope stability with h-slope stability for all those sheaves,
not just the original restrictions F_z. Positive integral scaling
from the rational representative to H preserves this equivalence.
Thus Q supplies a genuinely h-stable neighborhood.

Choose an analytic neighborhood T_0 mapping biholomorphically onto
an open neighborhood V of f(y) in the smooth M^an. The actual family
Q^an has a holomorphic classifying map a:T_0 -> S_I into the stable
connection chart. Its differential is its natural Kodaira--Spencer
map. The slice tangent theorem and L098's exact, same-extension
GAGA/Dolbeault comparison identify this with the isomorphism on
Ext^1, under the two natural tangent identifications. Both germs
are smooth of that dimension. The inverse function theorem makes
a a biholomorphism after shrinking. This constructs the comparison
V -> S_I by an actual local family, without asserting relative
algebraization of arbitrary analytic families.

For z sufficiently near y, Q at the unique slice point above f(z)
has fibre isomorphic to F_z. HE uniqueness assigns that fibre the
same connection class [A_z]. Therefore the composite of f with
V -> S_I equals phi pointwise, and hence as a holomorphic map on
the reduced smooth source. Scalar automorphisms and base-line twists
do not change fibre classes or the induced End metric. No universal
family on the full coarse moduli space is needed.

**Quaternionic differential and the positive normalization.** In the
smooth identifications above, let H_u be the horizontal coefficient
and dot A_u the vertical connection variation in real direction u.
The actual mixed curvature is r_u=dot A_u-d_A H_u. Thus its
harmonic projection is precisely the tangent to [A_z]. By L095,
r_u itself is ASD-harmonic and trace-free at every fibre. This
all-fibre conclusion needs no point of Z; the split-point assumption
in L095 concerns only its extra split-slice identification, as
explicitly checked in L098's audit. Consequently dphi(u)=r_u in
the real harmonic tangent, with no unremoved gauge component.

The target's natural quaternionic structure is L_c a=-a composed
with L on these real one-forms. L095 gives r_{Lu}=L_c r_u.
The actual-germ comparison just proved therefore gives the first
identity of (2) for df. It agrees also with the holomorphic rotated
classifying maps through the same connections; the conjugate (1,0)
coordinate convention in the primary construction does not change
this natural real tangent identification.

Section 9's L2 metric integrates the fibrewise Hermitian harmonic
pairing. In real skew-adjoint connection coordinates it is a fixed
positive constant multiple of the integral of -Tr(a(f_j)b(f_j)).
Indeed a=b_0-b_0^*, b_0=a^{0,1}; the orthogonal (1,0) and (0,1)
parts have equal norm, so the real norm is twice the (0,1)
Hermitian norm. The coefficient End metric uses the same unitary
trace, and this factor is independent of connection and parameter.
Choose the positive normalization (1) on every chart. Constant
rescaling preserves the hyperkähler metric and complex structures.
Unitary gauge invariance and scalar independence of the End metric
make the normalization agree on chart overlaps, including near
isomorphic fibres at different parameters.

Now L095's actual pairing, rather than a signed Yoneda coefficient,
gives

\[
 G(dphi(u),dphi(w))=G(r_u,r_w)=2\lambda g(u,w).
\]

The achieved scale 2lambda lies in (2,5/2), strictly above the
required threshold zero. It proves immersion and the second identity
of (2) on every component of U with the same constant. No global
connectedness of U or closedness argument for a varying scale is
needed: the full prescribed tensor already fixes this actual scale.

**Apply the known embedding theorem at the unchanged source
connection.** Import Verbitsky, *Deformations of trianalytic
subvarieties of hyperkahler manifolds*,
[alg-geom/9610010v1, 9 October 1996, Propositions 5.1--5.2,
Definition 5.3 and Corollary 5.4, PDF pp. 29--30](https://arxiv.org/pdf/alg-geom/9610010v1#page=29).
A hyperkähler embedding, compatible with both metric and quaternionic
structures, is totally geodesic; no ambient compactness or completeness
is required. Retain the all-hyperholomorphic induced-connection scope
of Propositions 5.1--5.2, not the broader printed Proposition 5.5
whose proof uses an additional zero middle-curvature contraction.

The injective differential permits shrinking around y so that phi
is an embedding into its target chart. Give that source neighborhood
the metric 2lambda g and the original I,J,K. Constant positive
rescaling keeps it hyperkähler. Equation (2) verifies both requirements
of Definition 5.3, so Corollary 5.4 applies to this local branch.
Its induced tangent and normal bundles are the ones in the cited
trianalytic/hyperholomorphic setting. The second fundamental form
vanishes. The tangential connection is the Levi--Civita connection
of 2lambda g; the Koszul formula shows that this equals the
connection of g, since the scale is constant. This proves (3).

The continuation threshold is reached on U. Distinct local embedded
branches may still meet, and this argument makes no statement at
the singular split value. L099's normalization or degree-one
conclusion is not used. An ambient-curvature test would require its
own assessed scope; this proof performs none. Independent existence,
split-germ integration, reconstruction, transport and universal Hodge
gaps remain. No numerical certificate or mathematical script is needed.

**Separate critical audit, 2026-10-14 (step 264).** The pre-invocation
SPECIALIZE assessment is
drafts/literature/2026-10-14-equality-stable-geodesy-critical-audit.md.
The audit finds no substantive error, stronger obstruction or existence
result. Its outcome is EXPLORATION / REPRODUCTION, not another
mathematical advance. The following checks concern applicability to
the actual family; the cited general theorems are imported, not reproved.

First, the scope does not silently require a split point. L095's
coefficient-Bianchi and Coulomb arguments use the fixed product
connection at an arbitrary parameter, and its actual-form computation
of the norm holds on all of B. The chosen split point in that lemma
enters only the additional identification with the reducible slice.
L098's audit explicitly separates these statements. Thus those inputs
remain valid if Z is empty. At any y in U, h-stability forbids a
parallel proper summand of A_y. Simultaneous rotation changes its
holomorphic interpretation but neither its invariant curvature nor
irreducibility. This checks the stable connection premise for all
induced structures without assuming projectivity of a rotation.

For the actual coarse germ, apply the trace map at E=F_y. Serre
duality identifies its dual with
H^0(O) -> Hom(E,E), 1 -> id_E, an isomorphism. Hence the obstruction
space Ext^2(E,E)_0 is zero, although Ext^2(E,E)=C is not zero.
Also H^1(O)=0. The cited Huybrechts--Lehn 4.5.3--4.5.4 criterion
therefore gives smoothness for the determinant-fixed and full stable
germs with the same Ext^1 tangent. Its actual slice from 4.5.1 is
available even though the whole coarse moduli space has no universal
sheaf. Local freeness and H-slope stability hold on an open neighborhood
of its central point, by the cited openness input. Every fibre there
has the same surface Chern invariants. L097's stratum argument is
uniform over *all* sheaves with these invariants, so it applies to
this slice, not only the original family. The segment from h to its
rational representative stays in a single relative stratum; subsequent
positive integral scaling preserves every slope inequality. This
checks the essential h-stable neighborhood while retaining h as the
metric polarization.

The direction of the analytic comparison is also essential. Analytify
that actual algebraic slice family first. Its analytic classifying
map into the stable connection germ exists by the cited local-family
input. The natural slice tangent and exact GAGA/Dolbeault comparison
carry each dual-number deformation to the same extension class,
rather than choosing an abstract Ext^1 isomorphism. Both germs are
smooth, and this differential is an isomorphism, so the holomorphic
inverse function theorem supplies the claimed local biholomorphism.
The local slice point over f(z) represents F_z itself, since this is
the stable locus. HE uniqueness consequently identifies its unitary
connection class with [A_z]. Thus the constructed comparison sends
the actual f to phi. This does not use relative algebraization over
an arbitrary analytic base or an assumed inverse global transform.

Next, in a smooth unitary trivialization the real connection variation
is dot A_u, whereas mixed curvature is r_u=dot A_u-d_A H_u.
Their difference is a gauge tangent. L095 makes r_u harmonic, so it
is exactly the tangent's Coulomb representative: an exact harmonic
d_A s has squared norm <d_A^*d_A s,s>=0. Integral determinant
triviality and the actual determinant HE connection, as checked in
L095, make it trace-free. This removes both a possible horizontal
gauge error and an extra central tangent. For
v=(u-iIu)/2 and a fibre (0,1) vector bar t, invariance gives
R(Iu,bar t)=iR(u,bar t), hence R(v,bar t)=R(u,bar t).
Thus the complex natural tangent is exactly r_u^{0,1}, with no
extra factor. On real forms L_c a=-a composed with L satisfies
I_c J_c=K_c; L095's r_(Lu)=L_c r_u verifies the same ordered
quaternionic structure, not an opposite or conjugated triple.

For an independent normalization check put b=a^{0,1} for a real
skew-adjoint one-form. Then a=b-b^*, where star conjugates the form
leg and takes the coefficient adjoint. In the complexified metric
the two types are orthogonal, and star is an isometry. With the
ordinary Hermitian form on coefficient-valued (0,1)-forms this gives

\[
 \int_{S_1}-\operatorname{Tr}(a\wedge *a)
       =2\int_{S_1}|b|^2\,dVol,
 \qquad
 G(a,a)=\frac{1}{2\pi^2}\int_{S_1}|b|^2\,dVol.
\]

Here the star in the wedge expression is the real Hodge star;
the star in b^* is the conjugate coefficient adjoint just specified.
Real polarization gives the corresponding bilinear identity.
Consequently (1) is one fixed positive rescaling of the harmonic
metric in Verbitsky's Section 9, independent of y and E. The
conjugate (1,0) coordinates in Section 7 give the same real norm.
A scalar change of a stable fibre's HE metric cancels in its End
metric; a unitary gauge change preserves the trace and the harmonic
pairing. Therefore chart transitions retain this normalization.
No signed Yoneda pairing is used to assign its sign. With precisely
this G, the imported L095 identity yields
G(df(u),df(w))=2lambda g(u,w), with 2lambda in (2,5/2), exceeding
the required positivity threshold zero everywhere on U.

Finally, the injective differential gives a local embedded branch
after shrinking around each y. With source metric 2lambda g its
differential is an isometry and preserves I,J,K, which checks both
requirements of the cited Definition 5.3. The tangent and normal
projections commute with the quaternionic structures. For each
induced complex structure they are the induced holomorphic tangent
and normal connections; the pulled-back ambient connection is
hyperholomorphic as well. Thus all three connections lie in the
scope of Propositions 5.1--5.2 and Corollary 5.4. The zero ambient
curvature-contraction premise used in the appendix is retained;
the broader printed Proposition 5.5 is not invoked on its own.
These are local statements, so neither completeness nor compactness
of the branch is needed. The resulting tangent connection is that
of the induced metric 2lambda g. In the Koszul formula both the
metric and every term on its right acquire the same constant
factor, which cancels; hence this is exactly nabla^g. Equation (3)
therefore holds for the original parametrized map. Local identities
agree on overlaps, without identifying different source parameters.

The audit preserves only stable-open local geodesy. It imposes no
conclusion at Z, no tangent coincidence between branches, and no
global separation, kernel existence, reconstruction or transport.
The direct mathematical inputs remain L095, L097 and L098; neither
L067 nor L099 has been added as a premise. The universal primitive
Hodge gap is unchanged.

## Mathlib

Full matching coverage for this actual equality-family germ comparison,
harmonic metric normalization and fixed-metric geodesy specialization:
**not checked**. Unknown availability is not absence. The precise
primary results above supply the general tools. The applicability
argument is a local REPRODUCTION, with no originality or progress
beyond the inspected literature claimed. The separate critical audit
above preserves the conditional specialization and its qualifications.
