# L067 — Conditional charge-seven classifying map has constant L2 scale and is locally totally geodesic

## Hypotheses

Retain L052 and L060's actual conditional holomorphic bundle F on
B x Y, where B and Y are the identical marked K3 surface with L044's
fixed common hyperkahler metric g and complex structures I,J,K.
Thus F is locally free of rank two, slope-polystable at
Omega=p_B^*h+p_Y^*h, and

\[
 c_1(F)=0,\qquad \operatorname{ch}_2(F)=-6e_1-7e_2+\tau_D.
\]

Use the compatible Hermitian hyperholomorphic connection supplied by
L052. L060 makes each E_x=F|_{\{x\}\times Y} stable of charge seven
at the unchanged h. Let f:B -> M_H^s(2,0,-5) be L063's actual
classifying morphism. Use the natural injective differential of
L062/L064. The integral H places the family algebraically; the metric
below is the instanton L2 metric associated with g on Y, not a metric
chosen using H.

Near each f(x), work in the locally free h-stable analytic moduli
chart, equipped with its natural L2 hyperkahler metric G and induced
complex structures I_M,J_M,K_M. This chart is identified with the
corresponding germ of M_H^s at f(x), as justified below. Global F
existence, global injectivity, image normality, target completeness,
reconstruction and transverse transport are not assumed.

## Conclusion

The actual local maps represented by f commute with all induced
complex structures:

\[
 df\circ L_B=L_M\circ df\qquad(L=I,J,K).
 \tag{1}
\]

For the natural connection-moduli charts there is one constant c>0
on the connected B such that

\[
                     f^*G=cg_B.                         \tag{2}
\]

The scale depends on the L2 convention; no numerical value is claimed.
Each local embedded branch of f is totally geodesic in the smooth
L2 target. Moreover the parametrized map is totally geodesic for the
original source metric g_B: with the ambient connection pulled back,

\[
 \nabla^{f^*TM}_{u}(df(v))=df(\nabla^{g_B}_{u}v).
 \tag{3}
\]

This is a conditional ADVANCE and REPRODUCTION of the assessed
geometric tools. It strengthens the local constraints on a prospective
F but proves no separation, F existence, new algebraic Hodge class or
universal Hodge conclusion. The separate critical audit below preserves
these conditional conclusions without strengthening them.

## Proof

**Imported local moduli and geodesy inputs.** Use Verbitsky,
*Hyperholomorphic bundles over a hyperkahler manifold*,
[arXiv:alg-geom/9307008v1](https://arxiv.org/pdf/alg-geom/9307008v1),
29 July 1993, Theorems 2.2--2.4 (PDF pp. 6--8), Definition 6.3 and
Theorems 6.1, 6.3--6.4 (pp. 22--24), Section 7 through Corollary 7.1
(pp. 24--28),
Section 9 (pp. 34--36) and Corollary 10.1 (pp. 36--37).
These provide stable/irreducible Hermite--Einstein correspondence,
zero contraction of hyperholomorphic curvature, natural local
classifying maps, and the smooth surface moduli's harmonic L2
hyperkahler structure and rotation through the same connections.
Import Verbitsky, *Deformations of trianalytic subvarieties of
hyperkahler manifolds*,
[arXiv:alg-geom/9610010v1, Definition 5.3 and Corollary 5.4,
PDF p. 30](https://arxiv.org/pdf/alg-geom/9610010v1#page=30),
9 October 1996: a metric- and quaternion-compatible hyperkahler
embedding is totally geodesic, without ambient compactness.
Use its Propositions 5.1--5.2 (PDF pp. 29--30) as the stated stronger
hypotheses underlying this corollary; do not import the broader wording
of Proposition 5.5 without its ambient curvature hypothesis. General
moduli and geodesy theorems are imported, not reproved. What remains
is their actual-family and source-metric applicability.

**The fixed connection supplies all the rotated fibres.** Write
nabla for F's given connection and nabla_x for its restriction to Y.
L052's curvature restriction argument makes nabla_x hyperholomorphic
for the fixed hyperkahler structure of Y. In particular its curvature
has zero contraction for every induced Kahler form. At I its
holomorphic bundle is E_x. Since E_x is stable, nabla_x is irreducible.
Equivalently a nontrivial parallel orthogonal splitting would give
holomorphic zero-slope subbundles at I, contradicting stability.
Irreducibility is a property of this connection and does not change
when the complex structure is rotated.

For L=aI+bJ+cK with a^2+b^2+c^2=1, integrate the (0,1)_L part of
nabla on B_L x Y_L. Its curvature is of type (1,1) for the simultaneous
product L, so this gives an actual holomorphic bundle F_L on that
product. Restriction commutes with taking this (0,1) operator. Thus its
fibre at x is precisely the holomorphic bundle E_{x,L} integrated from
nabla_x. The preceding zero contraction and irreducibility, with the
imported Hermite--Einstein correspondence, make E_{x,L} stable at the
rotated Kahler metric. This verifies every fibre, rather than assuming
stability survives rotation. Neither rotated projectivity nor an
integral rotated polarization is required for these analytic charts.

**Identify the same classifying map, including its I-germ.** Choose local
Hermitian differentiable identifications of F over a small parameter
neighborhood times Y, for example by unitary parallel transport along
parameter paths. The vertical connections nabla_x are then a smooth
family on one fixed Hermitian smooth bundle. Changing those identifications
only changes their unitary gauge representatives. The underlying
connection-valued map is

\[
                       \phi(x)=[\nabla_x].                \tag{4}
\]

Use Section 7's local connection-moduli description and Corollary
10.1 to regard the rotated stable-bundle charts as the same local
connection moduli with its respective induced complex structures.
The correspondence sends E_{x,L} to [nabla_x]: its given connection is
already Hermite--Einstein and irreducible, and the correspondence is
unique modulo unitary gauge. For each L, the actual holomorphic family
F_L therefore has a holomorphic local classifying map whose underlying
map is (4). This is an identification on nearby connection classes,
not just an isomorphism between abstract Ext spaces at x.

Here the analytic connection charts are the smooth reduced surface
moduli charts of the imported theorem. For a stable E on a K3,
Hom(E,E)=C and Serre duality gives Ext^2(E,E)=C. The dual of the trace
map is the scalar inclusion H^0(O_Y) -> Hom(E,E), an isomorphism.
Hence Ext^2(E,E)_0=0. The trace of the deformation Yoneda square
is zero: in a Dolbeault representative alpha the terms of
tr(alpha wedge alpha) cancel by cyclicity of trace and antisymmetry
of the one-forms. The quadratic cone in Verbitsky Theorem 6.2 is
therefore the entire Ext^1 space. Together with Corollary 7.1 this
gives a smooth local analytic chart with an actual classifying family
and the full natural Ext^1 tangent. The trace tangent H^1(O_Y) is
zero. The same calculation applies to each rotated K3, which need
not be projective. We use these reduced analytic charts for families
over smooth parameter spaces; such maps factor through the reduction.
No nonreduced tangent is silently replaced by a smaller tangent.

For the algebraic germ at I, import
[Huybrechts--Lehn, *The Geometry of Moduli Spaces of Sheaves*,
1997, Theorems 4.5.3--4.5.4, p. 102](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=114).
Their trace-free criterion makes the full M smooth at [E_x], since
Y is smooth projective, E_x is stable of positive rank two and
Ext^2(E_x,E_x)_0=0. Full Ext^2 is nonzero; Corollary 4.5.2's
Ext^2=0 criterion alone would not suffice. The numerical-class part
of M is open and closed by L063, imposing no further local condition.

Construct the comparison using an actual algebraic family. The proof of
[Huybrechts--Lehn Theorem 4.5.1 and Corollary 4.5.2, p. 101](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=113)
supplies an etale slice T -> M through a Quot point representing E_x,
carrying the restriction U of the Quot universal family. Shrink T
around that point so that every fibre is locally free and H-slope-stable.
Local freeness is open for this flat family with proper fibre Y;
slope-stability openness is the e=0 case of
[Huybrechts--Lehn Definition 3.A.1 and its following openness statement,
p. 74](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=86).
It applies to this smooth projective surface and L063's very ample H.
The central fibre is H-slope-stable, not merely Gieseker-stable.
Every nearby fibre has the same Chern classes. L063's uniform chamber
equivalence applies to all sheaves with these classes, so these fibres
are h-slope-stable as well. This checks the metric-stable neighborhood;
openness of Gieseker stability by itself would not check it.

Analytify U over T x Y. Since T -> M is etale and M is smooth here,
choose an analytic neighborhood T_0 mapping biholomorphically onto an
open neighborhood V in M^an. The actual analytic family U^an gives
a holomorphic map a:T_0 -> S_I into the local h-stable chart, by
Verbitsky Definition 6.3/Theorem 6.1. Its differential is the natural
KS map. The slice theorem and L064's exact GAGA/Dolbeault extension
comparison identify that map with the identity on Ext^1 under the
two natural tangent identifications. Both source and target are smooth
of this dimension, so the holomorphic inverse function theorem makes
a a biholomorphism after shrinking. This constructs V -> S_I using
an actual family; no relative algebraization theorem for arbitrary
analytic parameter spaces is assumed.

For b near x, the fibre of U over the point lying above f(b) is
isomorphic to E_b. Consequently the composite B -> V -> S_I and the
analytic classifying map of F have the same values. On the reduced
smooth source these are equal holomorphic maps (equivalently use
the local classifying-map uniqueness). At I their underlying map is
therefore exactly f, expressed in this natural analytic chart. Scalar
automorphisms and base-line twists do not change this argument; only
local families, not a global universal sheaf on M, were used.

Consequently (4) is smooth, since its I-description is f, and its
L-description is holomorphic for each induced L. Taking differentials
for I,J,K proves (1). L064's natural differential, or equivalently
L062's actual KS differential in this chart, is injective. Section 9's
L2 construction uses harmonic representatives in the deformation
quotient. This argument never declares the raw mixed-curvature
representative harmonic: gauge terms are removed by the imported
connection/coarse-moduli identification before the metric is evaluated.
The convention describing that harmonic tangent by conjugate
(1,0)-forms causes no substitution of an unrelated tangent map.

**Compare the induced metric with the original source metric.** Set
k=f^*G. Injectivity gives a smooth positive definite metric on B;
(1) and quaternionic Hermitian compatibility of G imply that k is
Hermitian for the fixed I,J,K on B. At each point choose a g_B-unit
vector e. The four vectors e,Ie,Je,Ke are a real orthonormal basis.
Hermitian compatibility makes their k-lengths equal. It makes
k(e,Ie)=k(e,Je)=k(e,Ke)=0, since each complex structure is skew-adjoint
for k. The remaining off-diagonal entries vanish by the quaternion
relations; for example
k(Ie,Je)=-k(e,IJe)=-k(e,Ke)=0. Thus

\[
                         k=c(x)g_B,
\]

with c(x)>0 smooth. This uses quaternionic dimension one of B; it
would not follow from quaternionic compatibility on a higher-dimensional
source.

Let omega_I^M and omega_I^B have the convention omega_I(u,v)=g(Iu,v).
Equation (1) gives f^*omega_I^M=c(x)omega_I^B. Both Kahler forms are
closed, whence dc wedge omega_I^B=0. Wedge with omega_I^B is injective
on real one-forms in dimension four: in a symplectic coframe with
omega_I^B=theta_1 wedge theta_2+theta_3 wedge theta_4, the four
coefficients of alpha wedge omega_I^B occupy four distinct basis
three-forms. Hence dc=0 on each parameter chart. Local connection
moduli charts use the same fixed L2 convention and their transitions
are the natural gauge identifications, so their metrics coincide on
overlaps. Thus c is locally constant on B, and connectedness gives
one positive constant. This proves (2). No comparison between the
signed Yoneda normalization in L062 and a positive metric has been
made, and no scale has been read off from its coefficient.

**Apply geodesy only after checking both compatibility requirements.**
Near any parameter point, shrink so that f is an embedding onto a
smooth local branch, by its injective differential and the local rank
theorem. Equip this parameter neighborhood with cg_B. Constant scaling
preserves its hyperkahler structures. Equations (1)--(2) make its map
to the L2 target a hyperkahler embedding in the exact sense of
Definition 5.3. Corollary 5.4 now makes that branch totally geodesic.
Its second fundamental form vanishes, and the tangential connection is
the Levi--Civita connection of the induced metric cg_B. A constant
positive metric scaling has the same Levi--Civita connection as g_B,
as follows directly from the Koszul formula. This proves (3) for the
parametrized map at the fixed source metric. The conclusion is local
in the target and holds at every parameter point; no completeness
or global embedding is used.

The attempt's continuation threshold is reached: same rotated germs,
quaternionic differential, constant pullback metric and zero second
fundamental form. This may support a later, separately assessed
branch-identification test. Distinct local branches can still meet;
nothing here rules out point identifications or establishes normality
of the original image. L065's normalization and L066's higher-Hom
uncertainty are not premises of this proof. F existence, reconstruction,
transverse transport and the general primitive Hodge gap remain open.
No mathematical script or numerical certificate is needed for these
exact applicability and metric arguments.

**Separate critical audit, 2026-10-07.** The conclusions survive.
The expanded slice construction above supplies the previously abbreviated
actual-family comparison, including the h-stable neighborhood and the
full algebraic germ's trace-free smoothness. On rotation, stability is
deduced from the same irreducible connection; it is not transported by
an arbitrary Ext-space isomorphism. The harmonic quotient is the natural
deformation quotient. In Corollary 7.1 the harmonic (1,0) coordinates
carry the conjugate complex structure when used to parametrize
holomorphic bundles; using its actual classifying family retains that
convention. The metric is evaluated only after passing to harmonic
representatives. Rescaling a stable bundle's Hermitian metric by a
positive scalar does not change the induced metric on End(E), and
unitary gauge changes preserve the L2 integral. Thus the fixed L2
normalization glues, including at distinct parameters with isomorphic
fibres. The dimension-four linear algebra, wedge injectivity, positive
constant scale and equality of the two source Levi--Civita connections
then check exactly the hypotheses of the imported geodesy corollary.
No substantive mathematical error or stronger consequence was found.
This audit is EXPLORATION and REPRODUCTION; the added applicability
details are not a new discovery. The direct mathematical inputs remain
L052, L060, L062, L063 and L064. Separation, image normality, F existence,
reconstruction, transport and the universal Hodge gap remain unresolved.

## Mathlib

Coverage of the full fixed-family rotation bridge, instanton L2 metric,
constant scale and local geodesy specialization: **not checked**.
No absence claim is made. The precise primary citations above provide
the general inputs; the actual-family and real-four-dimensional metric
checks are their local REPRODUCTION, without certified originality.
