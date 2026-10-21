# L068 — Parallel tangent splitting passes the trace-free relative index test

## Hypotheses

Retain L052/L060's conditional actual bundle F on X=B x Y, with
B and Y the identical marked smooth projective K3 surface of L044,
the fixed common hyperkahler metric g and real Kahler class h.
F is locally free of rank two, slope-polystable for the product
metric, with c_1(F)=0 and

\[
 \beta=\operatorname{ch}_2(F)=-6e_1-7e_2+\tau_D.
\]

Here e_1=eta tensor 1, e_2=1 tensor eta, P=eta tensor eta and
the integral of eta on either surface is one. L060 supplies stable
charge-seven fibres E_x=F|_{\{x\} x Y}, the compatible connection,
and the full character

\[
 \operatorname{ch}(F)=2+\beta+20P,\qquad \beta^2=240P.
 \tag{1}
\]

Use L062/L064's natural injective Kodaira--Spencer differential,
L063's common-H classifying map f:B -> M_H^s(2,0,-5), and audited
L067's constant-scale, quaternionic, parametrized total geodesy in
the natural smooth local L2 connection-moduli charts. Write
p_B:X -> B and End_0(F)=ker(tr:End(F) -> O_X).
No global universal family, embedding, completeness, F existence,
normalization conclusion, reconstruction or transport is assumed.

## Conclusion

There is an actual algebraic, base-changing vector bundle
E=R^1p_{B*}End_0(F) such that

\[
 Rp_{B*}\operatorname{End}_0(F)=E[-1],\qquad
 \operatorname{ch}(E)=22-272\eta.
 \tag{2}
\]

The natural tangent comparison identifies the family KS map with
df into E. It gives a global holomorphic parallel splitting

\[
 E\simeq T_B\oplus N,\qquad
 \operatorname{ch}(N)=20-248\eta.
 \tag{3}
\]

The connections in (3) are pulled-back ambient Levi--Civita
connections under the natural local tangent comparisons. The first
is B's original Levi--Civita connection; the complement connection
is hyperholomorphic and Hermite--Einstein with zero constant at h.
Thus N is slope-zero polystable at the original h and has a parallel
nondegenerate holomorphic alternating form. In particular
c_1(N)=0 integrally, c_2(N)=248eta and

\[
 \chi(E)=-228,\qquad \chi(T_B)=-20,\qquad \chi(N)=-208.
 \tag{4}
\]

These conditions are compatible with the tested necessary RR,
cohomology and simple/alternating-bundle indices. Already the formal
single stable rank-twenty complement passes them. No stable or
polystable realization of that complement, or of F, follows.
Stop this bounded character/index mechanism. This is an informative
NEGATIVE and REPRODUCTION of known relative-Ext, geodesy and RR
tools, without a mathematical originality claim or Hodge candidate.

## Proof

**Verify trace-free concentration at every fibre.** In characteristic
zero, A -> (tr(A)/2)id splits the trace, so End_0(F) is an actual
locally free direct summand of End(F). GAGA makes these algebraic
bundles on the projective X. For each x, stability gives
Hom(E_x,E_x)=C id. The trace-free H^0 is therefore zero. The trace
pairing identifies End_0(E_x) with its dual, and K_Y=O_Y, so Serre
duality gives H^2(Y,End_0(E_x))=0 as well. Equivalently the full
Ext^2 trace map is an isomorphism, dual to the scalar inclusion;
its trace-free kernel is zero. This also checks smoothness of the
positive-rank stable locus at every f(x).

On a fibre ch(E_x)=2-7eta, hence
ch(End_0(E_x))=3-28eta. Surface RR gives chi=6-28=-22, so
h^1(End_0(E_x))=22 at every x, not just generically. Import
[Stacks Lemma 36.30.4, 0B91](https://stacks.math.columbia.edu/tag/0B91)
and [Lemma 36.31.3, 0BDH](https://stacks.math.columbia.edu/tag/0BDH).
The smooth projective p_B is proper, finitely presented and flat;
its coefficient is locally free and perfect. The pushforward is
perfect with arbitrary derived base change. Its open locus of
rank-twenty-two concentration in degree one contains every closed
point of B, and is all B. This proves local freeness, all higher
image vanishings outside degree one, base change and the derived
statement in (2). The alternating K-class is -[E].

**Use the natural descended tangent comparison, rather than ranks.**
Import Huybrechts--Lehn, *The Geometry of Moduli Spaces of Sheaves*,
Aspects of Mathematics E31, Vieweg (1997),
[Section 10.2, Theorem 10.2.1, pp. 222--223, with the preceding
descent construction](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=234),
and Section 10.1.8/Example 10.1.9, pp. 220--221, for family KS.
The theorem applies to the positive-rank stable locus with vanishing
trace-free Ext^2 on a smooth projective surface. The preceding
fibre argument checks this for every E_x; L063 checks the common
algebraic moduli placement. Also H^1(O_Y)=0, so Ext^1(E_x,E_x)
equals H^1(End_0(E_x)).

The relative Ext on the stable Quot presentation descends naturally
to the tangent bundle on this smooth locus. Pulling its construction
back using the actual F gives E identified with f^*T_M on a smooth
open neighborhood of f(B). This use is local on B: local choices
of the classifying presentation recover F and its relative Ext.
Scalar conjugation acts trivially on End, trace and Ext; tensoring
a local representing family by a line from the base likewise leaves
End and its trace-free part unchanged. The natural identifications
therefore agree on overlaps and are global. A global universal
family on M is unnecessary. The descended KS identification and
L064's comparison on the actual dual-number extension identify
the differential as the same holomorphic map T_B -> E at every
point. Matching fibre dimensions alone would not justify this step.
Since L062 gives pointwise injectivity, its image is a holomorphic
rank-two subbundle.

More explicitly, pull back a stable Quot slice and its local family
to a cover of B. Locally that family and F differ by a base line:
the relative Hom between the two has one-dimensional H^0 on every
fibre, and cohomology and base change gives a line bundle of
homomorphisms. Evaluation from one family tensored with the pullback
of this line to the other is a fibrewise isomorphism, hence an
isomorphism of bundles. One can also use the local frame presentation
of F itself.
Two resulting identifications differ by scalar automorphisms of a
stable family. Conjugation on End_0 is independent of these scalars,
so even the scalar cocycle on a triple overlap disappears. The induced
relative H^1 identifications satisfy descent. Naturality of the
descended tangent construction in the cited theorem identifies this
specific descent with f^*T_M, not a possible twist of it. Analytifying
and using L064's extension comparison retains that same identification.

**Glue the parallel orthogonal complement on the parameter surface.**
Use audited L067 to express this natural tangent comparison in each
local h-stable connection-moduli chart with its harmonic L2 metric.
The fixed-gauge metric and tangent identifications coincide on
overlapping charts, including when different parameter points have
isomorphic fibres. Scalar changes of a stable Hermitian metric do
not change its End metric. Thus the pulled-back Hermitian metric
and ambient Levi--Civita connection on E glue on B. Its holomorphic
structure is the relative-Ext structure: on a Kahler target the
Levi--Civita connection on the holomorphic tangent bundle is its
Chern connection, and holomorphic pullback preserves that structure.

To check the connection transition, a holomorphic isomorphism of
stable h-Hermite--Einstein fibres takes one Hermitian metric to a
positive scalar multiple of the other. Its induced End isomorphism
is therefore an isometry, irrespective of that scalar's dependence
on the parameter. It intertwines the fibre deformation complexes and
their harmonic representatives. Unitary gauge invariance of the L2
integral then makes the *natural holomorphic* tangent transitions
isometries on their whole overlap. By uniqueness of the Chern
connection, those transitions identify the pulled-back connections,
including their parameter derivatives; no chosen gauge is asserted
constant in the parameter. The fixed I,J,K action on the harmonic
quotient is gauge-equivariant as well, so its metric symplectic forms
agree on overlaps. This uses h throughout; H is used only for the
coarse algebraic charts. Distinct points of B with the same image
still have separate pullback fibres, so this argument imposes no
identification between their tangent planes.

L067 gives, locally and therefore globally,
nabla^E_u(df(v))=df(nabla^{g_B}_u v). Its positive constant metric
scale makes df an isometry from a constant multiple of g_B.
Consequently df(T_B) is parallel. Its orthogonal complement N is
parallel, hence holomorphic and compatible with the direct sum in
(3). All three complex structures preserve both summands, because
df is quaternionic and the ambient metric is Hermitian for each.
No global embedding or nonintersecting image branches are used:
the splitting is of the parametrized pullback over B.

Import Verbitsky, *Deformations of trianalytic subvarieties of
hyperkahler manifolds*,
[alg-geom/9610010v1, 9 October 1996, Proposition 4.1/Lemma 4.3
and Propositions 5.1--5.2 with Section 5.3, PDF pp. 21--22,
29--31](https://arxiv.org/pdf/alg-geom/9610010v1#page=29).
Their local parallel normal connection is hyperholomorphic under
these hyperkahler-embedding hypotheses. Those hypotheses hold on
each L067 local branch with the constant source scale; they do not
require compactness of the ambient moduli charts. The conclusion
glues for N. Do not use Proposition 5.5's broader wording without
its curvature hypothesis. The ambient holomorphic symplectic form
is parallel; the tangent and normal summands are quaternionic and
symplectically orthogonal, and its restriction to N is nondegenerate.
These natural local forms also glue. Thus N has the stated parallel
holomorphic alternating form.

Import Verbitsky, *Hyperholomorphic bundles over a hyperkahler
manifold*,
[alg-geom/9307008v1, 29 July 1993, Theorems 2.2--2.3/Lemma 2.1,
PDF pp. 6--7](https://arxiv.org/pdf/alg-geom/9307008v1#page=6).
Invariant curvature has zero Kahler contraction. Since B is compact
Kahler, this actual compatible connection makes N slope-zero
polystable at the original h, permitting reducibility. The preserved
subconnection on T_B is B's Levi--Civita connection, since constant
metric scaling leaves that connection unchanged. No preservation
theorem for a projected Fourier index connection is an input.

**Evaluate the signed full relative character.** Import the Chern
character identities quoted in L048 from
[Stacks 42.45, 02UM](https://stacks.math.columbia.edu/tag/02UM),
and smooth proper GRR from Fulton, *Intersection Theory*, second
edition (1998), Theorem 15.2, pp. 286--287, Example 15.2.8,
pp. 291--292, also
[Stacks 42.66, 02UO](https://stacks.math.columbia.edu/tag/02UO).
These general statements are imported; the fixed-family evaluation
is the specialization. Duality changes the odd character signs;
here both odd characters are zero, so (1) gives

\[
 \begin{aligned}
 \operatorname{ch}(\operatorname{End}F)
  &=(2+\beta+20P)^2=4+4\beta+320P,\\
 \operatorname{ch}(\operatorname{End}_0F)
  &=3-24e_1-28e_2+4\tau_D+320P.
 \end{aligned}                                                    \tag{5}
\]

The top coefficient is 80+240, retaining the full mixed square
156P inside beta^2, including its transcendental contribution 120P.
The scalar subtraction is an actual trace splitting, not a formal
change to a deformation functor.

The relative Todd class is 1+2e_2. We have p_{B*}e_2=1,
p_{B*}P=eta, p_{B*}tau_D=0, and e_2 tau_D=0 by factor degrees.
Equation (5) therefore gives

\[
 \operatorname{ch}(p_{B!}\operatorname{End}_0F)
 =p_{B*}\bigl(\operatorname{ch}(\operatorname{End}_0F)(1+2e_2)\bigr)
 =-22+272\eta.                                                     \tag{6}
\]

In particular the top contribution is 320-48, not 320 alone.
Negate (6), because only R^1 is nonzero, to obtain (2). As a scalar
check, Rp_{B*}O_X has O_B in degrees zero and two; its alternating
character is 2. Thus the full End pushforward has rank -20 and
the trace-free one rank -22, as computed, with the same second
character. There is no surviving first character. Torsion-free
H^2(B,Z) promotes c_1(E)=0 to integral cohomology.

For a K3, ch(T_B)=2-24eta. Subtraction in the actual splitting
gives (3), including integral c_1(N)=0 and c_2(N)=248eta. Import
K3 HRR, Serre duality and the simple-sheaf Euler bound from
Huybrechts, *Lectures on K3 Surfaces*, author-hosted draft,
[Chapter 1, equations (2.5)--(2.6), Proposition 2.4, pp. 11--13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11),
and [Chapter 9, Sections 1.2--1.3, equations (1.2)--(1.4),
pp. 168--170](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=168).
For c_1=0, chi=2rank-c_2, proving (4). A further check uses
td(X)=1+2e_1+2e_2+4P: (5) gives
chi(X,End_0F)=12-48-56+320=228, equal to -chi(E).

**Apply only justified complement and summand indices.** The K3
symplectic form identifies T_B with Omega_B^1. It has H^0=H^2=0
and chi=-20, hence middle dimension twenty. The actual N is
self-dual by its alternating form. If t=h^0(B,N), Serre duality
therefore gives

\[
 (h^0,h^1,h^2)(N)=(t,208+2t,t),\qquad
 (h^0,h^1,h^2)(E)=(t,228+2t,t).                                    \tag{7}
\]

No value of t has been independently prescribed. Leray only
identifies H^j(X,End_0F) with H^{j-1}(B,E); it does not create
an additional vanishing or a conflicting dimension.

In a decomposition into stable zero-slope summands Q_i, individual
first Chern classes are not assumed zero. Write rank r_i,
c_1=d_i, and integral c_2=c_i eta. Surface RR and simple self-Ext
give the necessary conditions

\[
 \chi(Q_i)=2r_i+\tfrac12d_i^2-c_i,\qquad
 \chi(\operatorname{End}Q_i)=2r_i^2+(r_i-1)d_i^2-2r_ic_i\leq2.
 \tag{8}
\]

The inequality uses simplicity and Serre duality, so that self-Ext
dimensions in degrees zero and two are one. L052's actual metric
gives d_i in Zk with k^2=-14, but arbitrary such d_i must be kept.
For a nontrivial line of class mk, chi=2-7m^2; a trivial line has
two end cohomology dimensions. Neither alternative is eliminated
by (7), whose middle dimension is large and whose t is unknown.
No acyclicity, simplicity or rank-two charge bound is imposed on N.

It suffices to test a remaining formal alternative to see that
these conditions cannot exclude F: let N be a single stable
symplectic summand of rank twenty with d=0 and c=248. This is an
alternative for necessary tests, not an existence assertion.
Nontrivial zero-slope stability and dual stability give H^0=H^2=0,
so (7) would read (0,208,0). Its endomorphism character and index are

\[
 \operatorname{ch}(\operatorname{End}N)=400-9920\eta,\qquad
 \chi(\operatorname{End}N)=-9120\leq2,
\]

requiring self-Ext dimensions (1,9122,1), all nonnegative. The
parallel alternating structure has even complex rank, as required.
Its symplectic adjoint is Sym^2 N, with character
210-5456eta and chi=-5036: the second character is
(20+2)ch_2(N). In this stable alternative its H^0 is zero, since
it consists of symplectic infinitesimal endomorphisms and the only
global endomorphisms are scalars, which do not lie in that Lie
algebra. Self-duality gives H^2=0, leaving H^1 dimension 5036,
again compatible. These tensor-character identities follow from
the same imported character rules, not a new existence theorem.

For an explicit check of the tensor coefficient, write x_1,...,x_r
for formal Chern roots and sum x_i=c_1(N)=0. The Sym^2 weights are
x_i+x_j for i<j and 2x_i. Their squared sum is
(r+2)sum x_i^2+(sum x_i)^2, so division by two gives
ch_2(Sym^2 N)=(r+2)ch_2(N). At r=20 this is -5456eta;
twice its rank 210 minus 5456 is -5036. The End weights x_i-x_j
give ch_2(End N)=2r ch_2(N)=-9920eta and Euler value
800-9920=-9120. In the symplectic Lie algebra a scalar a id obeys
2a times the alternating form equals zero, hence a=0 in
characteristic zero. This checks the adjoint H^0 vanishing in the
formal stable alternative; duality then checks H^2. The resulting
middle dimensions 9122 and 5036 are also even, consistent with
the alternating Serre pairings induced by the symmetric trace
forms on End and on the symplectic Lie algebra. These checks do
not impose simplicity or these vanishings on the actual polystable N.

The required continuation threshold was a violated necessary
condition. None of the tested character, cohomology or simple/
symplectic-index conditions fails. This stops the bounded mechanism;
it does not decide whether the formal stable alternative exists at
h, embeds in an actual tangent pullback, or comes from an F. The
global mixed action, separation, reconstruction, other correction
pairs, transverse transport and universal primitive Hodge algebraicity
remain unresolved. ATTEMPTS/041--046 and the separate flat-index
source blocker remain independent preserved stops. Exact identities
suffice; no sampling or mathematical script is used.

**Separate critical audit, 2026-10-07.** The conditional conclusions
survive. The explicit descent and holomorphic-isometry overlap
arguments above check that E has the stated holomorphic structure
and Chern/Levi--Civita connection globally over B. L067's parametrized
geodesy makes df parallel with its original source connection; the
local normal theorem applies with the constant rescaling and glues
on this pullback. The quaternionic orthogonal complement is therefore
both holomorphic and symplectic without a global image embedding.
The independent character evaluation retains the scalar subtraction,
the 156P mixed square inside 240P, the relative Todd correction -48,
and the negative R^1 sign. Full-product RR agrees with relative RR.
The root-weight and cohomology checks verify the formal stable branch
used for the bounded compatibility verdict, without asserting its
existence. No substantive mathematical error or stronger obstruction
was found. This audit is EXPLORATION and REPRODUCTION, not a new
advance beyond the assessed sources. ATTEMPTS/047's stop is retained.
No other notebook, global normalization theorem, completeness
assumption or flat-index connection enters the proof.

## Mathlib

Coverage of this full actual-family relative tangent identification,
parallel complement and fixed-character compatibility: **not checked**.
No absence claim is made. The precise primary theorems above supply
the general inputs. The relative tangent/GRR formula is known overlap
recorded in the approved assessment; the present result is its scoped
REPRODUCTION, not progress beyond the sources checked or a solution
of the rational Hodge conjecture.
