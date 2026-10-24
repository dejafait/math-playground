# L158 — Four-twist determinant cups retain both extremal branches

## Hypotheses

Retain all of L157's conditional geometric data: identical marked projective
K3 factors S_1 and B, fixed common hyperkähler metric and real class h,
preferred HE lines L,L_B with class k, k.h=0 and k^2=-14 eta,
integral eta of degree one, and the full tensor tau_D. The hypothetical
locally free rank-two Omega-polystable F has integral c_1=0 and
ch(F)=2-14e_1-21e_2-tau_D+62e_1e_2. Impose z=|Z|=0 for this test.
Use L147's actual ordinary images M,W and L157's polystability,
opposite transforms H_r, cross-power duality and full line multiplicities.
Test exactly its formal branches (a,b)=(m_-1,m_1)=(12,2),(6,8).
These branches assert numerical decompositions, not geometric existence.

Put T_(e,d)=p_1^*L^e tensor p_2^*L_B^d and
V_(e,d)=H^1(X,F tensor T_(e,d)) for e,d in {-1,1}.
No scalar self-duality of M or H_1, and no value of an unevaluated
global cup map, is assumed.

## Conclusion

The four actual degree-one comparisons give dimensions (b,a,a,b)
for (V_--,V_-+,V_+-,V_++). Determinant cups between adjacent vertices
of this sign square vanish. Each opposite cup takes values in
H^2(O_X)=Cx+Cy, and each of its two scalar components is a perfect
bilinear pairing between the corresponding two degree-one spaces.
All polarized rank-two quartic relations have three plus signs.

These necessary constraints, including every such quartic relation
among these four groups, have a simultaneous formal assignment for
both branches. The largest required self-cup pairing rank is 78,
against 676 available. Thus this bounded relaxation excludes neither
branch and is parked. This NEGATIVE / REPRODUCTION result concerns
the limits of these selected identities, not the actual unknown cup
maps, existence of F or the formal residual bundles. It improves no
split-count bound and supplies no cycle, transport or resolution of
the universal primitive Hodge gap. The separate critical audit below
preserves this scoped compatibility verdict.

## Proof

**Scope and imported inputs.** Reuse the invocation-start SPECIALIZE
assessment `drafts/literature/2026-10-24-four-twist-determinant-cup-comparison.md`.
The potential downstream use was a common-kernel restriction beyond
L157's additive indices. The stopping test is compatibility of the
finite necessary relaxation; it does not authorize choosing actual
unknown global maps. ATTEMPTS/089's additive stop and ATTEMPTS/069's
uncontrolled-global-map warning remain in force.

Import coefficient Dolbeault and Serre duality from Demailly,
*L2 vanishing theorems for positive line bundles and adjunction theory*,
[alg-geom/9410022v3](https://arxiv.org/pdf/alg-geom/9410022v3),
Sections 1.A (1.1)–(1.3), printed pp. 4–5, and 4.A (4.3)–(4.4'),
printed pp. 27–28. Import coherent/derived cup comparison and signed
interchange from [Stacks 20.31.3, 0FP3](https://stacks.math.columbia.edu/tag/0FP3)
and [15.59, 0GWN](https://stacks.math.columbia.edu/tag/0GWN);
actual counit and base-change compatibility from
[20.31.7, 0FP6](https://stacks.math.columbia.edu/tag/0FP6) and
[20.31.8, 0H99](https://stacks.math.columbia.edu/tag/0H99);
line-valued Kunneth from
[36.23.1, 0FLN](https://stacks.math.columbia.edu/tag/0FLN).
All coefficients are locally free on smooth projective complex
varieties. The factors are quasi-compact and quasi-separated and
Tor-independent over the affine field base. Thus these theorems
apply to the specified lines, not just to O. No general theorem is
reproved; the specialization below determines the actual groups,
trace components and finite signed relations.

For the relative trace use
[48.12.4, 0AAB](https://stacks.math.columbia.edu/tag/0AAB),
[48.7.1, 0B6J](https://stacks.math.columbia.edu/tag/0B6J) and
[48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT).
The projections are smooth projective of relative dimension two over
Noetherian bases; in particular they are proper flat of finite
presentation, and their fibre squares are Tor-independent. Use the
perfect/coherent setting and p^!O=omega_p[2]. L090 supplies the
actual coefficient/counit/trace method, not its different-data exclusion.

**Four actual comparisons.** Set P_e=Rp_2*(F tensor p_1^*L^e).
Since z=0, L147 gives W=0 and P_-=M[-1]. This is a genuine
single-cohomology-sheaf identification. Fix det F=O, which follows
from integral c_1=0 and Picard injection on this K3 product, and fix
nonzero holomorphic two-forms on both factors. Relative duality gives
RHom(P_-,O)=P_+[2]. Since M is locally free, its left side is
M^vee[1], whence P_+=M^vee[-1]. Denote these two middle bundles by
E_-=M and E_+=M^vee. Their actual degree-one relative cup/trace
pairing E_- tensor E_+ -> O is perfect. This does not give a form
on M alone. Equivalently z=0 leaves every charge-fourteen fibre
stable, and both line twists have zero endpoints.

Projection formula and single-row Leray, in both directions, give
for all four signs the actual maps

    V_(e,d) = H^0(B,E_e tensor L_B^d)
            = H^0(S_1,H_d tensor L^e).

L157 supplies opposite concentration independently for d=+1,-1.
Stable-Hom vanishing and the full line isotypic pieces of M,M^vee
therefore give, writing A=V_--, B'=V_-+, C=V_+-, D'=V_++,

    dim A = dim D' = b,       dim B' = dim C = a.

Here B' denotes a vector space, not the second K3 factor B.
Both comparisons use the same class of the same coefficient sheaf.

More explicitly, evaluation on a fibre under either displayed edge
map is restriction of that global coefficient class followed by the
coefficient base-change isomorphism. To see this, write a class as
O_base -> Rp_*Q[1]; its global representative is the composite with
the counit Lp^*Rp_*Q -> Q. Pulling back this composite to the fibre
is the counit defining the base-change map. All middle bundles here
are locally free and concentrated, so this base-change map is an
isomorphism. The general product comparison then identifies restriction
of a determinant cup with the cup of the restricted classes.

**Targets and the perfect controlled components.** Use the same fixed
wedge F tensor F -> O for every cup. For v in V_s and w in V_t write

    C_st(v,w) in H^2(X,T_(s+t))

for its determinant cup. Degree-one interchange and coefficient
alternation cancel, so C_ts(w,v)=C_st(v,w).
For every nonzero integer n, both L^n and L_B^n have zero endpoint
cohomology and h^1=7n^2-2, as proved in L157: a nonzero effective
divisor cannot have zero h-degree, and K3 RR/Serre duality apply.
For the zero power, coherent cohomology is (1,0,1). Kunneth gives:

* If s=t, H^2(T_(2s))=H^1(L^(2s_1)) tensor H^1(L_B^(2s_2)),
  of dimension 26^2=676.
* If s,t differ in just one sign, H^2(T_(s+t))=0.
* If t=-s, the target is Cx+Cy, where x,y are the pullbacks of
  nonzero theta_1,theta_2 in the two H^2(O) lines. They satisfy
  x^2=y^2=0 and xy is a nonzero generator of H^4(O_X).

For an opposite pair, write C_(s,-s)(v,w)=f_s(v,w)x+g_s(v,w)y.
Restriction to a p_2 fibre, followed by multiplication with its fixed
holomorphic two-form and Serre trace, equals c_1 f_s(v,w), where
c_1=Tr(theta_1 sigma_1) is nonzero. The other projection similarly
gives c_2 g_s(v,w), c_2 nonzero. The trace base-change theorems cited
above identify these with the actual relative cross-coefficient forms
on E_- and E_+, and on H_-1 and H_1, respectively. Their fibre cups
use exactly the same determinant wedge. Any alternative normalization
rescales a whole component by a nonzero constant, not its rank.

Each restricted form on these section spaces is perfect. Indeed a
perfect cross-duality between polystable bundles identifies their
full dual stable isotypic pieces. Cross blocks from a line type to
any nonmatching stable type vanish by equal-slope stable-Hom vanishing.
Consequently the full multiplicity spaces of dual line types pair
perfectly. Twisting these paired line types to O identifies their
multiplicity spaces with the displayed global sections; their pairing
matrix is constant on the projective connected base. Apply this to
E_-,E_+ and separately to H_-1,H_1. Thus f_s and g_s are both perfect.
No relation between those two matrices has been assumed.

**The signed identities and their complete range.** In a local
trivialization of all coefficient lines and det F, write each closed
coefficient (0,1)-form as alpha_i=e_1 a_i+e_2 b_i. For formal commuting
t_i, alpha=sum t_i alpha_i has determinant self-cup 2a wedge b,
whose exterior square is zero, by L090's coefficient calculation.
The coefficient of t_1t_2t_3t_4 in that square is eight times

    C_12 C_34 + C_13 C_24 + C_14 C_23 = 0.             (1)

This local calculation glues: every term has the identical line
coefficient T_(s_1+s_2+s_3+s_4). It holds in coherent cohomology by
the imported resolution comparison, including repeated inputs by
multilinearity. All three signs are plus; even Plucker signs would
be incorrect here.

On a product of these surfaces H^4(T_(u,v)) is zero unless u=v=0:
its only Kunneth contribution is H^2(L^u) tensor H^2(L_B^v).
For four chosen sign vertices let their counts be n_A,n_B',n_C,n_D'.
Vanishing of both total exponents gives n_A=n_D' and n_B'=n_C.
Their total is four, so the only potentially nonzero instances of
(1), up to permutation, are AD'AD', B'CB'C and AB'CD'.
The adjacent cups vanish, so the last case requires just

    C_AD'(u,v) C_B'C(w,t) = 0.                        (2)

The other two cases also retain the unknown self-cups. This lists
all quartic identities, not only the four-distinct-input relation.

**A simultaneous necessary-relaxation witness.** Choose abstract spaces
A,D' of dimension b and B',C of dimension a, with arbitrary perfect
pairings f:A x D' -> C and g:B' x C -> C. Assign

    C_AD'(u,v)=f(u,v)(x+y),
    C_B'C(w,t)=g(w,t)(x-y),

and assign all adjacent cups zero. Both scalar components in each
opposite cup are perfect, and (2) holds since (x+y)(x-y)=0.
These are assignments to unspecified components, not evaluations of
actual geometry or identifications of the two relative forms.

For any perfect f define its induced perfect symmetric-power pairing by

    K_f(u u',v v') = f(u,v)f(u',v') + f(u,v')f(u',v).

It is nondegenerate: in f-dual bases it pairs matching symmetric
monomials diagonally, with diagonal entries 2 for squares and 1 for
distinct-index monomials. In characteristic zero these are nonzero.
The actual cohomology cup pairs the target U_A=H^2(T_--^2) perfectly
with U_D'=H^2(T_++^2) into Cxy, by Serre duality (K_X=O).
Both dimensions are 676. Its Kunneth formula has the minus sign
from crossing the two degree-one factor classes; retaining the actual
perfect pairing absorbs this sign into a chosen dual basis and does
not replace it by an incorrectly signed tensor pairing.

Choose an injection Sym^2 A -> U_A. The perfect target pairing
surjects U_D' onto (Sym^2 A)^*. Choose a linear section of that
surjection and compose it with -2K_f to define Sym^2 D' -> U_D'.
These two maps define symmetric self-cups satisfying

    C_AA(u,u') C_D'D'(v,v') = -2K_f(u u',v v') xy.

The other two terms in (1) for AD'AD' sum to +2K_f xy because
(x+y)^2=2xy. Thus every such identity holds.
Independently use the perfect pairing U_B' x U_C -> Cxy and the
same construction with +2K_g to obtain their self-cups. The other
two terms for B'CB'C sum to -2K_g xy since (x-y)^2=-2xy.
Their identities hold as well. The two target pairs are distinct,
so these choices impose no conflicting assignments. Every other
quartic identity has zero H^4 target, as already proved.

The requisite inequalities are dim Sym^2 A=b(b+1)/2<=676 and
dim Sym^2 B'=a(a+1)/2<=676. For (a,b)=(12,2) these dimensions
are 78 and 3; for (6,8) they are 21 and 36. All maps in this
construction therefore exist as finite-dimensional linear maps.
This is an exact dimension-and-dual-basis certificate, requiring no
numerical search or mathematical script.

The assignment verifies all selected identities and the ranks forced
by both actual trace comparisons. It does not verify higher products,
other coefficient groups, any additional positivity relation, or
realizability by F. In particular it neither assigns the actual
self-cups nor asserts that their actual relative matrices have these
ratios. Nondegeneracy alone permits this witness; deciding actual
maps requires a separately justified input. The bounded mechanism
therefore stops with both formal branches compatible, while z<=119,
independent lower control and the universal Hodge gap are unchanged.

**Separate critical audit, 2026-10-24 (step 520).** Reuse the
invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-24-four-twist-cup-critical-audit.md` and
its inspected primary theorem statements and proof cases. The outcome
is EXPLORATION / REPRODUCTION: no substantive error or stronger
conclusion was found. This checks the stated specialization, not the
existence of its hypothetical input or a stronger cohomology-algebra
realization. L090's method is used with the present coefficients;
its different-character exclusion is not an input.

First, integral c_1(F)=0 trivializes the determinant because
H^1(X,O_X)=0 makes the integral first-class map on Pic(X) injective.
Fix one such trivialization throughout. At z=0 the actual W vanishes,
and L147 gives Rp_2*(F tensor p_1^*L^{-1})=M[-1], with M locally
free. Applying smooth-proper relative duality with omega_p=O and
relative dimension two gives

    RHom(M[-1],O)=M^vee[1]
      =Rp_2*(F tensor p_1^*L)[2].

Thus the positive coefficient has middle bundle M^vee and no other
cohomology sheaves. This shift calculation does not dualize a
nonfree point sheaf or assert M=M^vee. L157 independently supplies
H_- and H_+ with H_-^vee=H_+ and same-h polystability.
The four actual section identifications are, explicitly,

| Group | Forward section space | Opposite section space | Dimension |
| --- | --- | --- | --- |
| A | H^0(M tensor L_B^{-1}) | H^0(H_- tensor L^{-1}) | b |
| B' | H^0(M tensor L_B) | H^0(H_+ tensor L^{-1}) | a |
| C | H^0(M^vee tensor L_B^{-1}) | H^0(H_- tensor L) | a |
| D' | H^0(M^vee tensor L_B) | H^0(H_+ tensor L) | b |

In each row, a section of the middle bundle represents a morphism
O_base -> Rp_*Q[1], with Q the full double-twisted coefficient.
Adjunction makes its global class the pullback followed by the
counit. Restricting that same composite to a fibre gives its
coefficient base-change map. Concentration and local freeness ensure
that the middle base-change map is an isomorphism. In an opposite
pair the two base-line coefficients cancel by evaluation. The actual
product/counit compatibility followed by relative Serre trace
therefore identifies the forward form with c_1 f_s and the opposite
form with c_2 g_s. The c_i are the fixed nonzero fibre traces
Tr(theta_i sigma_i). They do not depend on the selected section.
This checks all four rows through both projections without choosing
independent classes or an inverse transform.

The perfect bundle dualities pair the complete dual line isotypic
pieces. To check restriction of perfection, a morphism from a line
to a nonmatching stable dual summand vanishes: both are stable of
slope zero, and a nonzero morphism would be an isomorphism. The same
argument kills the other cross block. Hence the multiplicity-space
block is invertible, not merely nonzero. Apply this to M,M^vee and
separately to H_-,H_+. Twisting each paired line to O gives exactly
the spaces in the table. Both f_s and g_s are therefore perfect;
this argument gives no relative phase or positivity comparison.

For the target check, every nonzero power has endpoints zero and
middle dimension 7n^2-2, while the zero power has dimensions (1,0,1).
An adjacent target has one nonzero even exponent and one zero
exponent, so every degree-two Kunneth summand vanishes. A self target
has two nonzero exponents of magnitude two and dimension 26*26=676.
An opposite target has precisely the two scalar classes x,y. In
degree four only the tensor of the degree-two factor groups can
occur. It is nonzero only when both total exponents vanish. Solving
those two equations for the four nonnegative vertex counts gives
n_A=n_D', n_B'=n_C and n_A+n_B'=2. This gives exactly the three
patterns (2,0,0,2), (0,2,2,0), (1,1,1,1), with no omitted repeated
vertex case.

Independently expand the local determinant square. Its degree-one
coefficient cup is symmetric because exterior interchange and
determinant interchange both contribute minus signs. In the square
of C(sum t_i alpha_i,sum t_i alpha_i), each partition of four
distinct formal labels into pairs occurs with coefficient eight:
two orders inside each pair and two orders of the even-degree
products. The local self-square is zero since (a wedge b)^2=0.
All three resulting terms therefore have coefficient +8, and each
has the same line weight, so the identity glues. Substitution of
equal vectors is permitted after this multilinear identity; it
introduces no independent sign convention.

Finally the witness is simultaneous. The opposite assignments
f(x+y) and g(x-y) have perfect components and product zero. For
the repeated A,D' case the sum of the two opposite-product terms
is 2K_f xy; the prescribed self-product is -2K_f xy. For B',C the
two terms instead sum to -2K_g xy and the self-product is +2K_g xy.
These equalities include u=u' and v=v': then K_f=2f(u,v)^2, so
the cancellation is -4f(u,v)^2+4f(u,v)^2=0, and similarly for g.
In dual symmetric-monomial bases K has diagonal entries 2 on squares
and 1 on mixed monomials, hence full rank. A perfect pairing of the
two 676-dimensional target spaces restricts surjectively to the dual
of any injected symmetric power. Its linear section realizes the
required signed K. The actual target pairing includes the minus
Kunneth sign; choosing dual bases for that pairing respects it.
The two opposite pairs of self targets have distinct line weights,
so their sections and injections can be chosen independently.
All remaining quartic products land in zero H^4 groups. The two
branch rank pairs are (3,78) and (36,21) in A,B' order, both within
676. No finite case or compatibility equation of the stated
relaxation remains unchecked.

This audit preserves ATTEMPTS/090's stop and ATTEMPTS/069's warning:
the construction assigns free entries of a necessary relaxation,
not the actual entries of cup maps. It asserts neither all additional
geometric constraints nor a cohomology algebra realizing the witness.
F existence, independent lower split control, transport and universal
primitive Hodge realization remain unresolved; z<=119 is unchanged.

## Mathlib

Full matching coverage for this geometric four-coefficient comparison
and compatibility specialization is not checked. Abstract symmetric
powers and perfect-pairing algebra would only support the final linear
algebra, not the actual Leray/counit/trace comparisons. Unknown coverage
is not absence; general inputs are imported by the precise citations
above. This is REPRODUCTION, without a certified originality claim.
