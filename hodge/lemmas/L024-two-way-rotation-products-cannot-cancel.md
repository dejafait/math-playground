# L024 — Two-way rotation products cannot cancel the transverse obstruction

## Hypotheses

Use the very general cubic Dickson surface S, X=S x S, and the
reduced rotation supports C and C^(2) with the genericity hypotheses
of L014. Set P=O_C, Q=O_(C^(2)), and F=P direct sum Q. Retain the
marked spaces V_D contained in V_RM contained in V_N of L008.

Let A_1=C[tau]/(tau^2), A_2=C[tau]/(tau^3). The prescribed ambient
product X_2=S_2 x_(A_2) S_2 has an identified constant reduction over
A_1 and order-tau^2 coefficient kappa in V_RM. Thus its two factors
have the same coefficient. Permit precisely the first-order sheaf
motions

\[
\xi=\begin{pmatrix}0&b\\a&0\end{pmatrix},\qquad
a\in\operatorname{Ext}^1_X(P,Q),\quad
b\in\operatorname{Ext}^1_X(Q,P).
\tag{1}
\]

There is no first-order self component. Second-order corrections
are arbitrary. A lift means an A_2-flat coherent sheaf with the
specified first-order deformation class; neither splitting nor
filtration is required to lift. All supports include their three
singular points at infinity.

## Conclusion

Each mixed Ext^1 group is C^7: four coordinates belong to the
finite elliptic intersection curves and three to the infinity
points. Write o_P(kappa), o_Q(kappa) for the central
Atiyah--Kodaira--Spencer obstruction classes of the two sheaves.
With the compatible Maurer--Cartan/Yoneda convention, the full
order-two obstruction for (1) is

\[
\bigl(o_P(\kappa)+b\circ a,\quad
      o_Q(\kappa)+a\circ b\bigr)
\in\operatorname{Ext}^2_X(P,P)\oplus
       \operatorname{Ext}^2_X(Q,Q).
\tag{2}
\]

Its other matrix blocks vanish. No single pair (a,b) makes (2)
zero for kappa in V_RM outside V_D. More precisely,

\[
\{\kappa\in V_{\rm RM}:\text{some }(a,b)\text{ makes (2) zero}\}
=V_D.
\tag{3}
\]

This is an equality of admissible coefficient sets, proved below;
linearity of a quadratic lifting problem is not assumed. Equality
asserts existence of some motion, not that every motion lifts in
V_D. Reversing the overall ambient-obstruction sign convention
does not alter the exclusion.

The action of ch_2(F) is U^2+U-2 id by L014, hence non-scalar.
Nevertheless only the three existing RM directions are admissible,
against four required. This stops the stated mixed-only order-two
test, not self motions, other representatives or higher orders.
The known 21-dimensional span remains confined to the same family;
no Hodge counterexample or complete Hodge candidate follows.

## Proof

**Both directed groups, including infinity.** Near each finite
intersection curve D use L014's coordinates

\[
R=\mathbb C\{r,q,z,w\},\quad
M=R/(z,r),\quad N=R/(z,q),\quad r=Q_1(t,s),\ q=Q_2(t,s).
\tag{4}
\]

The Koszul calculation in L017 gives Ext^1_R(M,N)=O_D and zero
Hom. Interchanging r,q gives Ext^1_R(N,M)=O_D and zero Hom in
the reverse direction. Intrinsically these are respectively the
normal lines of D in C^(2) and in C. D is a whole smooth elliptic
fibre on each normalization, and the indicated base equations
trivialize both lines. Consequently a and b restrict to scalars
a_D,b_D in these trivializations.

At an infinity point the two supports have ideals
J_1 intersect J_(-1) and J_2 intersect J_(-2), with the graph planes
and weights specified in L014. L017's normalization-sequence Ext
calculation applies in either direction. Here is why swapping its
source and target preserves every needed condition. All four
planes are pairwise transverse; the two target-plane bivector
lines are linearly independent, so the relevant map from
Ext^2(k,target normalization) to Ext^2(k,k) is injective. Restriction
of an ambient tangent vector to the two source conormal spaces
is an isomorphism, since the source planes are transverse. The
same long exact sequences therefore give Ext^1=k in each direction,
as a module killed by the maximal ideal. This retains both
two-branch singular sheaves; neither is replaced by a smooth branch.

Globally the mixed Hom sheaves are zero: neither reduced target
has a component in common with the source, and a source-ideal
element nonzero on both target branches is a nonzerodivisor on
the target. The local-to-global Ext spectral sequence therefore
identifies each global Ext^1 with H^0 of its Ext^1 sheaf. Its
support is the disjoint union of four curves and three points.
Each complete elliptic curve has only constant global functions.
This proves the two seven-dimensional descriptions, using the
supporting framework [Stacks, tag 0BQP](https://stacks.math.columbia.edu/tag/0BQP).
No statement about global Ext^2 follows just from these local data.

**The obstruction of the actual earlier motion.** Import the
pair-deformation model of Iacono--Manetti, *On Deformations of Pairs
(Manifold, Coherent Sheaf)*, published Canad. J. Math. 71 (2019),
[Theorem 7.11, p. 1235; equations (5.2) and (7.1), pp. 1224 and 1234](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B017822BED1B8D6202816C2E10C0A30D/S0008414X18000561a.pdf/on_deformations_of_pairs_manifold_coherent_sheaf.pdf#page=27).
A finite locally free resolution of F exists on smooth projective
X. Take the direct sum of resolutions of P and Q. The kernel of
the model's anchor to ambient deformations is the global derived
endomorphism complex, with its matrix decomposition and usual
Yoneda multiplication. This model controls flat coherent-sheaf
deformations, without simplicity, stability or a preserved splitting.

Choose a closed degree-one endomorphism cochain representing (1).
An ambient cocycle for kappa can be lifted to the pair model using
block-diagonal local data for the two resolutions. Its differential
in the kernel represents the diagonal Atiyah obstruction. Denote
this lift by kappa-tilde and allow an arbitrary kernel cochain eta
of degree one at order two. The Maurer--Cartan expression for

\[
\tau\xi+\tau^2(\widetilde\kappa+\eta)
\]

has order-two coefficient

\[
d\widetilde\kappa+d\eta+\tfrac12[\xi,\xi]
=d\widetilde\kappa+d\eta+\xi^2.
\tag{5}
\]

There is no earlier ambient term; brackets involving kappa-tilde
first occur at order three. The square of the off-diagonal matrix
is diagonal, with entries b composed with a and a composed with b.
Thus (5) gives (2), and vanishing in the two global Ext^2 groups
is equivalent to the existence of an A_2-flat sheaf lift. In
particular this is a simultaneous test with the same a and b.
An endomorphism coboundary correction eta keeps the prescribed
ambient projection fixed. These assertions use the global model,
not products in stalk Ext groups or a formality theorem.

We use the sign convention identifying the boundary of the ambient
cocycle with o_F(kappa). If the opposite convention is chosen,
replace kappa by -kappa in the displayed test; V_D is unchanged.
The same excluded coefficient set therefore results with either
overall sign. This is also the expansion of the corrected
[Huybrechts--Thomas criterion, arXiv:0805.3527v2, Corollary 3.4, p. 14](https://arxiv.org/pdf/0805.3527v2#page=14)
for the actual A_1 sheaf, with the
[absolute-over-C correction in the 2014 erratum, pp. 561--562](https://link.springer.com/content/pdf/10.1007/s00208-013-0999-x.pdf#page=1).
The pair model directly supplies flat sheaves here. In a use of
the latter criterion, flatness and smoothness of the ambient
family give perfectness of the deformed sheaf from a finite
central resolution; the preserved ample class gives a projective
embedding in a smooth C-scheme. Replacing the actual A_1 sheaf by
the central direct sum would incorrectly omit xi^2 in (5).

It remains to exclude a flat sheaf lift for transverse kappa.
We do this by a global geometric consequence of such a lift. This
need not assign coordinates to every global Ext^2 class.

**A local reference for arbitrary mixed motion.** Assume that a
lift F_2 exists. Trivialize the smooth ambient deformation locally
near (4), compatibly with its fixed reduction over A_1. A reference
lift for the local first-order class has two generators m,n with

\[
zm=zn=0,\qquad rm=\tau a_Dn,\qquad qn=\tau b_Dm.
\tag{6}
\]

It is the cokernel over (R/(z)) tensor A_2 of the matrix

\[
\begin{pmatrix}r&-\tau b_D\\-\tau a_D&q\end{pmatrix}.
\tag{7}
\]

This is A_2-flat. Indeed the central matrix diag(r,q) is injective
over R/(z). Induction on the tau-adic filtration shows that (7)
is injective. Its two-term resolution consists of A_2-flat modules
and remains exact on the left modulo tau. Hence Tor_1 with the
residue field is zero; the local flatness criterion for the
nilpotent Artinian base proves flatness. Its A_1 reduction has
exactly the two mixed classes: in the relations r m=tau a_D n
and q n=tau b_D m they are the usual Koszul extension coordinates.
Its self classes vanish. Thus its A_1 reduction is isomorphic,
with marking, to the restriction of the actual first-order sheaf.

The two lifts, with such an identification fixed, differ by a
central Ext^1_R(M direct sum N,M direct sum N) class times tau^2.
This is the small-extension torsor from the same deformation
model, since tau annihilates the extension ideal (tau^2).
The two self blocks are ordinary regular normal displacements of
the smooth branches; the second-order mixed blocks restrict to
zero where only one central branch remains. No assertion that
F_2 splits follows or is needed.

For q invertible, eliminating n in (6) gives r=tau^2 a_Db_D/q
on the cyclic M branch. Eliminating m for r invertible gives
q=tau^2 a_Db_D/r on the N branch. Consequently the actual branch
supports have order-two displacements

\[
\begin{array}{ll}
M:& \delta r=a_Db_D/q+u_M,\quad \delta z=v_M,\\
N:& \delta q=a_Db_D/r+u_N,\quad \delta z=v_N,
\end{array}
\tag{8}
\]

where each u and v is regular on its entire central branch in
the chart. Restriction of the torsor action proves this assertion:
only the respective self block survives on a separated branch,
and Ext^1 of its smooth cyclic sheaf is its normal bundle. Terms
from a second-order mixed block combined with an earlier mixed
term have order at least three. Thus (8) retains arbitrary
second-order corrections. In particular the fibre-normal shift
has no pole, and the only base-normal residue is a_Db_D. Changing
representatives or the local identification changes regular parts,
not this residue.

**Global fibre identities force all four residues to vanish.**
Off the other component, the first-order sheaf class is zero:
restriction kills both mixed Ext groups. Its support is therefore
constant modulo tau^2. The actual sheaf F_2 there is locally cyclic
by Nakayama, and its annihilator quotient is A_2-flat. Thus it
gives an embedded lift of the separated branch with no order-tau
support motion; it need not have a chosen global generator.

Over a small disk in the dense open of the first elliptic base,
the central supports are separated unramified graphs. Properness
and central finiteness imply finiteness of their lifted supports
over the first factor. The pushforward of each sheaf piece is a
line bundle: it is A_2-flat with central module locally free of
rank one over the first factor, so the local flatness criterion
and Nakayama apply. Functions from the second factor act through
the endomorphisms of that line bundle, which form O of the first
factor. This defines an actual graph morphism. This construction
does not make the whole F_2 a quotient algebra or choose a flat
Fitting support.

The graph morphism sends complete smooth elliptic fibres to
fibres. To see this over A_2, take its second base-coordinate
function, reduce modulo tau, subtract a lifted function of the
first base, and repeat on the two remaining tau-adic layers.
Functions on the central complete connected elliptic fibres are
constant, so each coefficient comes from that base. The induced
map of smooth proper elliptic fibres reduces to an isomorphism;
finiteness and the rank-one algebra argument make it an isomorphism
over A_2. It therefore preserves j, by the same Weierstrass
invariance used in L014. Write

\[
J_2(t)=J_0(t)+\tau^2\dot J(t),\qquad
A_{e,k}=\dot J(p_{e,k}),\quad e=\pm1,\ k=1,2,3.
\tag{9}
\]

The NS-fixed pencil exists as in L008, pulled back along
epsilon -> tau^2; the chosen constant reduction permits (9).
An order-two coordinate change of the base does not change the
critical values A_(e,k), since J_0'(p_(e,k))=0.

At the ordered critical pair (p_(e,1),p_(e,2)), C is present and
C^(2) is absent. Both projections of this branch are unramified,
so the preceding graph argument applies on a neighbourhood of
the whole smooth fibre. Its support has no order-tau motion.
Evaluating its j identity at this pair gives
A_(e,1)=A_(e,2): order-two shifts of either argument multiply
J_0', which vanishes there. At (p_(e,1),p_(e,3)), only C^(2)
is present and the same reasoning gives A_(e,1)=A_(e,3). Hence

\[
A_{e,1}=A_{e,2}=A_{e,3}\quad(e=\pm1).
\tag{10}
\]

At a mixed curve over (p_(e,2),p_(e,3)), L014 gives
J_0(t)-J_0(s)=H(t,s)r q with H|_D=h_D nonzero. Insert (8) into
the j identity on the punctured M graph. Its order-two coefficient
extends to D: the simple pole in delta r is multiplied by q.
Restricting this coefficient to D gives

\[
A_{e,2}-A_{e,3}+h_D a_Db_D=0.
\tag{11}
\]

The regular terms in (8) are multiplied by q and vanish on D;
the fibre-normal displacement does not enter j. The N graph gives
the same residue equation. The reversed ordered pair has its own
nonzero h_D and the same conclusion. Equations (10)--(11) prove

\[
a_Db_D=0\quad\hbox{on each of the four finite curves}.
\tag{12}
\]

These are constraints on actual global lifts, not independent
choices of local smoothing parameters. Neither (12) nor a local
product calculation asserts that either global Yoneda product is
zero; classes in higher local-to-global filtration and the point
contributions have not been discarded.

**Recovering C and retaining all infinity parameters.** The
absence of order-tau support motion lets us regard the separated
supports as first-order embedded lifts over B=C[epsilon]/(epsilon^2),
with epsilon sent to tau^2. Locally the ambient transitions, and
the ideal variations of these supports, have only an order-two
coefficient. They therefore descend to the first-order ambient
X_B of coefficient kappa. No arbitrary sheaf F_2 is being descended.

By (8) and (12), both normal components of the recovered C
displacement extend regularly across every finite mixed curve.
They give a flat embedded smooth-branch lift by L007's ideal
parametrization. These local lifts agree with the support away
from the other component. On overlaps, the difference is a regular
normal section that vanishes on that dense complement, so it
vanishes everywhere. Together with the annihilator construction
off C^(2), they give an embedded lift of C minus its three infinity
points in X_B.

The three coordinates of a and the three coordinates of b at
infinity remain arbitrary throughout this argument. On a punctured
neighbourhood of such a point the two central supports separate,
so restriction again kills their mixed first-order motions. The
preceding recovery gives a punctured C lift. Trivialize the
first-order ambient deformation locally. Its difference from the
constant C is a section of N_C on the punctured neighbourhood.
L008 identifies N_C with nu_*N_j, where the normalization is a
smooth surface and N_j is locally free. Removing the infinity
point removes two points on that surface. Hartogs extends the
section uniquely; L007 then supplies a flat embedded lift on the
whole neighbourhood. Uniqueness glues it to the recovered lift.
Proper GAGA over B applies to the analytic construction.

Thus every hypothetical F_2, with arbitrary punctual mixed data,
would yield an embedded C_B. This is the global obstruction
detector: no vanishing of punctual Yoneda products, or automatic
flatness of an annihilator at the singular points, is assumed.
L008 forces kappa into V_D. In view of (2)--(5), simultaneous
cancellation for any kappa outside V_D is impossible in the full
global Ext^2 groups, not merely in a local quotient.

For the converse in (3), take a=b=0. Along V_D the Dickson family
lifts both supports by L014, so both central Atiyah obstructions
vanish. Pullback along epsilon -> tau^2 supplies the required
constant-first-order direct sum. This proves existence for every
kappa in V_D, without claiming that every nonzero mixed motion
extends there.

The dimensions three and four are those in L008. Additivity gives
ch_2(F)=[C]+[C^(2)], whose non-scalar action was computed in L014.
No enlarged span or transverse family is obtained. Self motions,
other sheaves, higher-order lifting and algebraization remain
outside this restricted test; arbitrary primitive fourfold classes
and higher dimensions remain gaps in the universal Hodge target.

## Mathlib

Coverage of the full statement: **not checked**. No matching
Mathlib theorem, supporting Mathlib identifier or absence from
checked library sources is asserted. The named pair-deformation
theorem, corrected Atiyah criterion and linked local-to-global
spectral sequence are supporting inputs, not matches for (3).
Koszul resolutions, the local flatness criterion, Nakayama,
Hartogs and proper GAGA are the other named general tools used.

The [prior SPECIALIZE assessment](../drafts/literature/2026-09-27-two-way-rotation-yoneda-products.md)
is reused with its exact target and hypotheses unchanged. The
general theory is imported; the block expansion and local matrix
are reproductions of that theory. The finite-fibre compatibility
and global recovery excluding these mixed products were not
matched by the checked sources. Classification is POTENTIALLY_NEW
in that limited sense, not certified originality or a claim of a
general mathematical discovery. No surface formality theorem or
automatic semiregularity injectivity is used.
