# L119 — Opposite global parallel normal bundle and full character

## Hypotheses

Retain L118's identical marked projective K3 surfaces X=S_1 x S_2,
common hyperkähler metric g, ordered structures I,J,K, real ample
class h and product class Omega. Write e_1=eta tensor 1,
e_2=1 tensor eta and P=e_1e_2, with integral_S eta=1. Retain
L071's full integral tensor tau_D, including its divisor part, with
tau_D^2=156P. Suppose F is holomorphic locally free of rank two,
Omega-slope-polystable, with integral c_1(F)=0 and

\[
 \beta=\operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D.
\]

Use L071's actual compatible unitary connection and audited L118's
opposite classifying map f^-:B=S_1 -> M_H^s(2,0,-19), with fibre
Y=S_2, all-fibre stability, natural harmonic tangent comparison,
normalized L2 metric G and parametrized total-geodesy identity.
In particular (f^-)^*G=2lambda g, with 1<lambda<5/4, and df^-
is quaternionic. Set p=p_1 and V=End_0(F).

No existence of F, global embedding, image separation, compact ambient
metric, normal section, image deformation or transport is assumed.
Characters below lie in rational cohomology of B, not its Chow ring.

## Conclusion

The actual bundle

\[
 \mathcal E=R^1p_*V
\]

is locally free of complex rank 78, commutes with base change, and
Rp_*V is isomorphic to \mathcal E[-1]. Naturally it is the pullback
of the coarse-moduli tangent bundle along f^-, on its smooth locus.
The whole harmonic L2 metric and its Chern/Levi--Civita connection
glue on this pullback. There is a global holomorphic parallel splitting

\[
 \mathcal E=df^-(T_B)\oplus N^-,\qquad
 N^-=(df^-(T_B))^{\perp_G}.                                  \tag{1}
\]

The normal bundle here is on the parameter surface B. It is algebraic,
of complex rank 76, and carries the induced hyperholomorphic unitary
Chern connection, a parallel perfect alternating form and trivial
determinant. It is slope-zero polystable at the original h, allowing
reducibility. Its full cohomological character, and that of the tangent
pullback, are

\[
 \boxed{\operatorname{ch}(\mathcal E)=78-880\eta,\qquad
        \operatorname{ch}(N^-)=76-856\eta.}                    \tag{2}
\]

Thus c_1(N^-)=0 integrally and c_2(N^-)=856eta. This is a conditional
REPRODUCTION/specialization of the covered tools. The separate critical
audit below preserves the construction and calculation. They supply no F, section
count, new exclusion, cycle, transverse transport or universal Hodge
resolution. No simple/adjoint index or deformation test is performed.

## Proof

**Coverage and scope.** The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-17-opposite-global-normal-character.md`, whose
exact COVERED_TARGET is this construction and full character. The direct
mathematical inputs are L071 and audited L118. The descent/connection
proof of L068 is a methodological comparison, not an input of its
different hypotheses or character. L108's forward hull and point-defect
formula is not used. General theorems below are imported rather than
reproved; the family-specific checks are supplied here.

**All-fibre concentration.** Characteristic zero splits the actual trace
by A -> (tr(A)/2)id, giving End(F)=O_X direct sum V. For every x in B,
L118 gives stability of E_x=F|_{\{x\}\times Y}. Therefore H^0(Y,End(E_x)) is
the scalars, and H^0(Y,End_0(E_x))=0. The trace pairing is perfect on
End_0(E_x); since K_Y=O_Y, Serre duality gives H^2(Y,End_0(E_x))=0.
The full Ext^2 is retained: its trace to H^2(O_Y) is an isomorphism,
dual to the scalar inclusion, so only its trace-free part vanishes.

On this fibre ch(E_x)=2-21eta, hence
ch(End_0(E_x))=3-84eta. With td(Y)=1+2eta, surface HRR gives
chi(Y,End_0(E_x))=6-84=-78. Consequently its degree-one cohomology
has dimension 78 at every x. Import
[Stacks Lemma 36.30.4 (0B91)](https://stacks.math.columbia.edu/tag/0B91)
and [Lemma 36.31.3 (0BDK)](https://stacks.math.columbia.edu/tag/0BDK):
p is smooth projective, proper, finitely presented and flat, and V
is finite locally free and perfect. Thus Rp_*V is perfect and has
arbitrary derived base change. The open single-degree rank-78
concentration locus contains all closed complex points of B. Its
closed complement is empty, since B is of finite type over C.
This proves concentration, local freeness and base change everywhere,
including at geometric nonclosed points. Its alternating K-class is
-[\mathcal E]. No punctured extension or point defect is involved.

**Natural global tangent identification.** Import Huybrechts--Lehn,
*The Geometry of Moduli Spaces of Sheaves*, E31, Vieweg (1997),
[Section 10.2, Theorem 10.2.1 and its descent proof, pp. 222--223](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=234),
with [10.1.8/Example 10.1.9, pp. 220--221](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=232)
for the natural family KS convention. The positive-rank stable locus
with vanishing trace-free Ext^2 is smooth and has the descended relative
Ext^1 tangent bundle. The preceding checks apply at every f^-(x).
Also H^1(O_Y)=0, so full and trace-free Ext^1 coincide. Pull back this
construction by L118's actual family and classifying map, obtaining
\mathcal E=(f^-)^*T_M along the relevant smooth locus. This is a natural
identification, not a rank comparison.

Explicitly, after an étale slice cover, pull back local representing
families to B. Any such family and F have isomorphic stable fibres.
Their relative Hom has constant fibre H^0 dimension one; cohomology
and base change gives a line of homomorphisms, and evaluation gives
an isomorphism between one family tensored by that base line and the
other. Evaluation is an isomorphism because it is so on every fibre.
Two choices differ by scalar automorphisms. Conjugation on End_0
cancels these scalars, as well as the base-line twists; hence the
induced relative H^1 identifications descend, even across scalar
triple-overlap cocycles. The cited tangent construction identifies
this very descent with the tangent pullback, without a universal
sheaf. Naturality carries the actual dual-number extension to its
KS class. L118's same-extension GAGA/Dolbeault comparison identifies
the algebraic differential with the actual harmonic derivative r^-_u.
Its pointwise injectivity makes df^-(T_B) a holomorphic rank-two
subbundle of \mathcal E.

**Whole-metric and connection overlaps.** In every L118 connection
chart, identify \mathcal E with the full ASD-harmonic tangent space,
not only with its rank-two image plane. A holomorphic isomorphism
between stable h-Hermite--Einstein fibre bundles takes their HE
metrics to positive scalar multiples by uniqueness. The induced
End_0 isomorphism is an isometry and intertwines their vertical
Chern connections, deformation complexes and harmonic representatives.
Scalar variation in the base cancels in End_0. The negative-unitary-
trace L2 integral with L118's fixed normalization therefore agrees
under these natural holomorphic transitions on the entire tangent
space. If comparison gauges vary with the parameter, differentiating
them adds a d_A-exact term to a variation; harmonic projection kills
that term. No gauge is assumed constant along B.

Thus the whole pulled-back Hermitian metric glues smoothly on
\mathcal E. The Levi--Civita connection of each Kähler connection
chart is the Chern connection on its holomorphic tangent bundle.
Its holomorphic pullback is the Chern connection of the pulled-back
metric. Uniqueness of the Chern connection under a holomorphic
isometry identifies these local connections on overlaps, including
their base derivatives. The ordered I,J,K actions and associated
metric symplectic forms are gauge-equivariant on the harmonic
quotient, so they glue as well. H is used for algebraic placement;
the fibre metric remains the same h throughout this argument.

**The parallel complement.** L118's parametrized identity now holds
for this globally identified connection:

\[
 \nabla^{\mathcal E}_u(df^-(v))=df^-(\nabla^g_u v).             \tag{3}
\]

The constant factor 2lambda in the induced metric does not change
the source Levi--Civita connection. Hence df^-(T_B) is parallel,
and its Hermitian orthogonal complement N^- is parallel and
holomorphic. Both are invariant under all three structures, because
df^- is quaternionic. The parallel ambient holomorphic symplectic
form restricts perfectly to N^-: for a quaternionic orthogonal
splitting, G(Jv,w) and G(Kv,w) have zero cross blocks. It gives
the claimed alternating form and determinant trivialization.

Import Verbitsky, *Deformations of trianalytic subvarieties of
hyperkahler manifolds*,
[alg-geom/9610010v1 (9 October 1996), Proposition 4.1/Lemma 4.3,
Propositions 5.1--5.2 and Appendix 5.3, PDF pp. 21--22, 29--31](https://arxiv.org/pdf/alg-geom/9610010v1#page=29).
On each local branch supplied by L118, these give the induced normal
hyperholomorphic connection. The source metric is 2lambda g, with
unchanged connection and ordered structures; hyperholomorphicity
is unchanged by this constant scaling. The all-three-induced-
connections hypotheses, including the middle curvature's zero
contraction in the appendix, are those already checked in L118.
No compactness of the ambient connection chart is needed, and
Proposition 5.5 alone is not used. The local normal connections
are precisely the restrictions of the glued connection in (3),
so they glue to the stated connection on N^-.

For completeness, invariant curvature has zero Kähler contraction
by Verbitsky, *Hyperholomorphic bundles over a hyperkahler manifold*,
[alg-geom/9307008v1 (29 July 1993), Lemma 2.1 and Theorems 2.2--2.3,
PDF pp. 6--7](https://arxiv.org/pdf/alg-geom/9307008v1#page=6).
The compact-Kähler HE correspondence therefore makes N^- slope-zero
polystable at h. This allows reducibility. GAGA algebraizes the
holomorphic splitting, bundle and form on projective B. Different
points with isomorphic fibres still have separate pullback fibres;
no assertion about a normal bundle on the image is made.

**Full opposite signed GRR.** Use L071's rank-two character identities,
from Fulton, *Intersection Theory*, second edition (1998), Theorem
3.2(a), pp. 50--52, and [Stacks 42.45 (02UM)](https://stacks.math.columbia.edu/tag/02UM).
Here e_i^2=e_i tau_D=0 by factor degree. Therefore

\[
 \beta^2=(2\cdot14\cdot21+156)P=744P,\qquad
 \operatorname{ch}(F)=2+\beta+\frac{\beta^2}{12}
                    =2+\beta+62P.                           \tag{4}
\]

Both odd characters vanish, and duality preserves the displayed
even ones. Multiplication and the actual trace splitting give

\[
 \operatorname{ch}(V)=\operatorname{ch}(F)\operatorname{ch}(F^\vee)-1
 =3+4\beta+(4\cdot62+744)P
 =3-56e_1-84e_2-4\tau_D+992P.                              \tag{5}
\]

The full 156 from the mixed square is retained, including the
transcendental contribution 120. Reversing the mixed sign does not
alter its square; the scalar subtraction changes the rank to three.

Import smooth proper GRR from Fulton, Theorem 15.2, pp. 286--287,
Example 15.2.8, pp. 291--292; also
[Stacks 42.66 (02UO)](https://stacks.math.columbia.edu/tag/02UO).
The projection is p_1, so the relative Todd class is 1+2e_2.
Fibre integration has p_*e_2=1, p_*P=eta, p_*e_1=p_*tau_D=0,
and e_2 tau_D=0. Applying the cycle-class map to algebraic GRR yields

\[
 \begin{aligned}
 \operatorname{ch}(p_!V)
 &=p_*\bigl(\operatorname{ch}(V)(1+2e_2)\bigr)\\
 &=(6-84)+(992-112)\eta=-78+880\eta.                     \tag{6}
 \end{aligned}
\]

The Todd correction -112 is twice the pure base coefficient -56;
using the other projection's -168 would be incorrect. By all-fibre
concentration p_!V=-[\mathcal E], so (6) proves the first formula
in (2), including zero first character. As a trace-subtraction check,
Rp_*O_X has O_B in degrees zero and two, with alternating character
2. Thus p_!End(F) has character -76+880eta, exactly two more than
(6); full Ext^2 has not been discarded before removing the scalars.

On a K3 surface ch(T_B)=2-24eta: c_1(T_B)=0 and surface HRR with
chi(O_B)=2 gives integral c_2(T_B)=24. Subtracting this character
in the actual splitting (1) gives

\[
 \operatorname{ch}(N^-)=(78-880\eta)-(2-24\eta)=76-856\eta.
\]

The parallel alternating form already gives integral c_1(N^-)=0;
then ch_2=-c_2 proves the stated second Chern class (integrally,
since H^4(B,Z)=Z eta). These are every surviving degree of the
cohomological character on B. The prescribed cohomological data of
F do not determine its Chow character, so no Chow identity is claimed.

The concentration and actual holomorphic-isometry overlap tests both
succeed. This ends the approved construction/character attempt.
ATTEMPTS/047's compatible-index stop, ATTEMPTS/066's punctured-metric
warning, and ATTEMPTS/069's uncontrolled actual cup entry remain
intact. No new index, normal-section or deformation test is inferred
from (2). Common-kernel existence, separation, image deformation,
transverse transport and universal primitive Hodge realization remain
independent unresolved gaps.

**Separate critical audit, 2026-10-17 (step 350).** The pre-invocation
SPECIALIZE assessment is
`drafts/literature/2026-10-17-opposite-global-normal-critical-audit.md`.
The audit checks the actual descent, the whole metric and its connection,
and the complete opposite character. It finds no substantive error or
stronger conclusion. Its outcome is EXPLORATION / REPRODUCTION, actual
task type proof_audit; verification of this conditional specialization
is not a new mathematical input or progress beyond the sources checked.
The following details make explicit the checks on the argument above.

First, concentration concerns the actual trace-free coefficient. On
every fibre stability kills its H^0, and the nondegenerate trace pairing
identifies its dual with itself. Serre duality therefore kills its H^2,
while the scalar coefficient still has H^0=H^2=C. Surface RR gives
3 times 2 minus 84, so the only remaining dimension is 78. The proper
flat perfect-base-change hypotheses of Stacks 0B91 hold for p_1 and V;
the fixed-degree concentration locus of 0BDK is open and contains all
closed points. Its closed complement in the finite-type complex base
must be empty. This checks actual local freeness, not just the virtual
rank. In particular there is no split-fibre skyscraper contribution.

For descent, let T be an etale parameter neighborhood and let Q denote
a pulled-back representing family over T times Y. The relative Hom
from F_T to Q has fibre H^0 of dimension one everywhere because the
stable fibres are isomorphic. The degree-zero cohomology-and-base-change
theorem applies to this flat locally free Hom coefficient: its H^0
dimension is constant. Thus L=p_{T*}Hom(F_T,Q) is a line bundle with
the stated base-change fibres. Evaluation gives

\[
 p_T^*L\otimes F_T\longrightarrow Q.
\]

On every closed fibre a nonzero homomorphism of these isomorphic stable
bundles is an isomorphism. The determinant of evaluation is consequently
nowhere zero, so evaluation is an isomorphism on T times Y. Changing a
local generator of L multiplies this map by an invertible scalar.
Conjugation on End_0 is independent of that choice, including on triple
overlaps. The canonical identification End_0(F_T tensor p_T^*L)=
End_0(F_T) also respects the relative Dolbeault differential: the base
line has no vertical differential contribution. Consequently the
relative H^1 identifications themselves satisfy descent, rather than
only their ranks or isomorphism classes. Huybrechts--Lehn 10.2.1, at
the citation above, identifies this descended relative Ext with the
coarse tangent. H^1(O_Y)=0 removes no extra tangent sector, and the
natural KS map carries the same actual extension. This verifies the
comparison with L118, without a universal sheaf or a chosen trivialization
of the scalar gerbe.

Next consider the full harmonic fibre, allowing all its 78 complex
directions. If u is a holomorphic comparison of stable HE bundles, HE
uniqueness gives u^*h_Q=c h_F for a positive scalar c on that fibre.
For endomorphisms the factor c cancels in taking adjoints and hence
in the trace inner product. It also cancels in the vertical Chern
connection. Conjugation by u therefore intertwines both the vertical
deformation differential and its adjoint, and is an isometry on their
whole harmonic cohomology. The scalar c may vary smoothly with the
parameter; neither this assertion nor cancellation assumes it constant
on T. Smoothness of the metric in each chart comes from L118's smooth
irreducible connection germ and its harmonic L2 metric.

The transitions on relative H^1 are holomorphic by the preceding
descent. Their full harmonic isometry is stronger than an isometry
only on df^-(T_B). Thus they intertwine the Chern connections, with
all their parameter derivatives, by uniqueness of the Chern connection
of a Hermitian holomorphic bundle. In a varying gauge, an additional
d_A-exact term in the derivative of the represented connection is
orthogonal to every harmonic class; this is precisely the quotient
tangent convention in Li Section 2.2 at the citation above. It does
not authorize dropping base derivatives from a connection matrix.
On a Kahler chart the tangent Chern connection is Levi--Civita, and
holomorphic pullback preserves the Chern characterization. Hence the
connections compared here really are the pullbacks used in (3).
Gauge equivariance also preserves the ordered quaternionic structures
and their metric symplectic forms.

There is no missing all-induced curvature hypothesis in passing to the
normal bundle. Locally the ambient tangent connection is Kahler for
each induced structure L, and its curvature satisfies
R^M(L a,L b)=R^M(a,b). Since L118 gives df^-(L u)=L df^-(u), its
pullback curvature satisfies

\[
 R^{\mathcal E}(Lu,Lv)
 =R^M(df^-(Lu),df^-(Lv))
 =R^{\mathcal E}(u,v).
\]

This checks the middle connection directly on the same pullback,
not a replacement metric. L118's already established parametrized
geodesy makes df^-(T_B) parallel. For its orthogonal projector P_T,
\(\nabla^{\mathcal E}P_T=0\), so the curvature is block diagonal and
the normal curvature is its restriction, with no second-fundamental-
form correction. Both blocks inherit the displayed invariance; the
tangent block is the connection of g because the factor 2lambda is
constant. On the real four-dimensional base, invariant two-forms are
ASD and have zero contraction with each of the three Kahler forms,
coefficient by coefficient. In particular the middle curvature has
zero contraction as required in the cited appendix. This independently
checks the all-three-connection scope used above and the identity of
the local normal connections on overlaps. It uses the proved geodesy
of L118, not a circular proof of it from a prospective normal bundle.

For v,w in different quaternionic orthogonal summands, both G(Jv,w)
and G(Kv,w) vanish. The ambient parallel complex symplectic form is
therefore block diagonal and nondegenerate on N^-. Its 38th exterior
power trivializes det((N^-)^*) holomorphically. This gives integral
c_1=0, before any rational-character argument. The actual invariant
unitary connection on compact B is HE with constant zero, so the
compact-Kahler correspondence gives polystability, with no simplicity
assumption. GAGA algebraizes the holomorphic bundle and form, not the
metric as an algebraic object. All these constructions are on B; a
coincidence of two image points identifies neither parameter fibre.

Finally, a root calculation independently checks every character
degree. With formal rank-two roots x,-x, set beta=x^2. Then

\[
 \operatorname{ch}(F)=e^x+e^{-x}
       =2+\beta+\beta^2/12,
 \qquad
 \operatorname{ch}(End_0F)=1+e^{2x}+e^{-2x}
       =3+4\beta+\tfrac43\beta^2.
\]

Only degrees at most eight on X are retained. L071 gives the full
mixed square 156P; the two pure cross products contribute 588P.
Thus beta^2=744P, ch_4(F)=62P and ch_4(V)=992P. There are no odd
characters. Pushing over S_2 retains -84e_2 and the rank Todd term
6e_2 in degree zero, and 992P together with -112P in degree four
on B. No degree-six term on X can survive to a first Chern character:
ch_3(V)=0, e_2 tau_D=0 and td_1(Y)=0. Consequently

\[
 \operatorname{ch}(p_!V)=-78+880\eta,
 \quad \operatorname{ch}(\mathcal E)=78-880\eta,
 \quad \operatorname{ch}(N^-)=76-856\eta.
\]

An independent absolute RR check on X gives
chi(X,V)=12-280+992=724; surface RR for E gives
chi(B,E)=156-880=-724, as required by concentration in R^1.
Here -280=8(-14-21) keeps both pure coefficients. This is a check
on the alternating sign, not a normal-section or simple-index test.
The integral determinant argument above and H^4(B,Z)=Z eta then
give c_2(N^-)=856eta. No Chow-level conclusion is inferred.

The audit thus preserves (1)--(2) and all conditional qualifications.
No repair or narrowing is required. ATTEMPTS/047, 066 and 069, and
the compact-image/boundary stops, are unchanged. In particular this
audit supplies no section dimension, image deformation, F existence,
global separation, cycle or transverse transport.

## Mathlib

Full matching coverage for this actual-family global tangent descent,
parallel normal connection and opposite character: **not checked**.
Unknown coverage is not absence. The precise primary citations above
supply the general descent, concentration, Chern and GRR inputs;
this is a conditional REPRODUCTION with no beyond-source or novelty
claim. The separate critical audit above preserves this conditional
specialization; it is not a review of a complete Hodge-conjecture argument.
