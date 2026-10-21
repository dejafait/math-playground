# L135 — Actual opposite off-diagonal relative Hom stalk has length one

## Hypotheses

Retain L071's equality-kernel setting and L118/L121's actual opposite
family in full. Thus B=S_1 and Y=S_2 are the identical marked smooth
projective complex K3 surfaces with the specified common hyperkähler
metric, ordered structures, real ample class h and product class Omega.
The full integral mixed tensor tau_D and its self-adjoint operator D
are those of L071, with D sigma=2lambda sigma and 1<lambda<5/4.
Suppose F on B times Y is holomorphic locally free of rank two,
Omega-slope-polystable, with integral c_1(F)=0 and

    ch_2(F)=-14 e_1-21 e_2-tau_D.

Use the actual algebraic family G on Y times B obtained by exchanging
the factors of F. Write E_x=G|_{Y times {x}}. L118 gives one common H
for which every E_x is stable of rank two, determinant O_Y and charge
21, and the natural classifying map f:B -> M_H^s(2,0,-19). Its natural
KS differential is the actual family deformation class. L121 gives
finite reduced off-diagonal coincidences and, at any such coincidence,
zero intersection of the two natural tangent planes in the same smooth
stable-moduli tangent space. These conclusions retain L120's hypotheses
through L121; no normality of the original image is assumed.

Put T=B times B, p:Y times T -> T, and let G_i be the pullback of G
using the ith B coordinate. Set

    K=Rp_*(G_1^vee tensor G_2),
    K_rev=Rp_*(G_2^vee tensor G_1).

Select a closed r=(b,c) with b unequal to c and E_b isomorphic to E_c.
This is a conditional selection: neither F nor any such r is known to
exist. All local work is away from the diagonal. No trace-free Hom
coefficient is imposed between these independently varying bundles.

## Conclusion

For R=O_{T,r}, maximal ideal m and residue field k=C, the ordinary
coherent stalk satisfies

    (R^2 p_*(G_1^vee tensor G_2))_r is isomorphic to R/m.

In particular its R-length is exactly one and its annihilator is m.
The isomorphism with k is not canonical without a choice of endpoint
generator. The reverse Hom stalk also has length one, by the same
argument with the pair exchanged. The actual and required last-row
cotangent ranks are both four.

This is a conditional ADVANCE / REPRODUCTION of the assessed tools;
the separate critical audit below preserves it. It determines a local multiplicity
of an allowed collision, not its existence or impossibility. No
cardinality bound, useful global coincidence/normalization-defect
comparison, separation, F, algebraic cycle or transport is supplied.
Universal primitive rational Hodge realization remains unresolved.

## Proof

**Scope, imports and known overlap.** Reuse the pre-invocation SPECIALIZE
assessment `drafts/literature/2026-10-20-opposite-off-diagonal-relative-hom-stalk.md`.
Markman, *Generators of the cohomology ring of moduli spaces of sheaves
on symplectic surfaces*, J. reine angew. Math. 544 (2002), 61--82,
[math/0009109v4, Section 2, Remark 3(2), proof through (11), and
Section 3](https://arxiv.org/pdf/math/0009109v4), already gives the
universal-family line-bundle-on-diagonal mechanism, including local
universal-family treatment. We specialize that known mechanism through
the actual coefficient sequence below. We do not reprove his general
diagonal theorem, assume a universal sheaf on M, or pull back all its
ordinary Ext sheaves. The specialization is necessary to verify the
two independently varying actual families and their four-dimensional
pair base. L066 and L110 are method comparisons, not inputs to this
charge or stalk length. ATTEMPTS/046's separation failure remains valid.

Import perfect pushforward and arbitrary derived base change from
[Stacks Lemma 36.30.4(1), 0B91](https://stacks.math.columbia.edu/tag/0B91).
Here p is proper, flat, finitely presented, and the coefficient is a
vector bundle, hence perfect. Import minimal free representatives and
their spreading from [Lemmas 15.77.6--7,
0BCC](https://stacks.math.columbia.edu/tag/0BCC) and
[0BCD](https://stacks.math.columbia.edu/tag/0BCD). The local base R is
Noetherian regular of dimension four. The cochain connecting-map
naturality used below is [Lemma 12.13.12,
0117](https://stacks.math.columbia.edu/tag/0117).

Use stable Hom and simplicity in Huybrechts--Lehn, *The Geometry of
Moduli Spaces of Sheaves*, first edition (1997),
[Proposition 1.2.7 and Corollary 1.2.8, pp. 11--12](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=23),
and named surface Serre duality. All fibres are stable for the same H
and have the same numerical class. Use projective GAGA and the
Dolbeault resolution naturally on coefficient exact sequences.

For the actual deformation comparison use Fiorenza--Iacono--Martinengo,
*Differential graded Lie algebras controlling infinitesimal deformations
of coherent sheaves*, JEMS 14 (2012), 521--540, DOI 10.4171/JEMS/310,
[0904.1301v3, Remark 7.3, Theorem 7.6 and Section 8, printed
pp. 17--21](https://arxiv.org/pdf/0904.1301v3#page=17), and
Budur--Wang, *Cohomology jump loci of differential graded Lie algebras*,
Compositio Math. 151 (2015), 1499--1528, DOI 10.1112/S0010437X14007970,
[1309.2264v2, Definitions 3.2--3.8, Proposition 3.10 and Lemma 3.11,
pp. 10--12](https://arxiv.org/pdf/1309.2264v2#page=10).
The bundles in degree zero satisfy the negative-cohomology hypothesis;
their Dolbeault modules are bounded with finite cohomology on compact Y.
Apply to the direct sum with its block-diagonal deformations and keep
the off-diagonal Hom block; simplicity of the direct sum is unnecessary.
Neither formality nor a zero-Chern resonance theorem is used.

Actual relative duality is the composition/trace construction of
[Stacks Remark 48.12.6, 0G81](https://stacks.math.columbia.edu/tag/0G81).
It pairs the forward and reverse complexes with relative surface shift
two; base dimension four does not change that shift. Fix a nonzero
holomorphic two-form sigma_Y. Its fibre Serre pairing is written below
directly, so neither an arbitrary self-duality of K nor an identification
with a trace-free End complex is assumed.

**Derived fibres, support and minimal presentation.** By derived base
change the fibre of K at (x,y) is RHom_Y(E_x,E_y). Stable Hom detection
gives endpoint dimensions zero for nonisomorphic fibres, and one for
isomorphic fibres, using Serre duality for the top degree. Higher Ext
groups vanish because Y is a surface and both coefficients are bundles.
Surface Hirzebruch--Riemann--Roch gives, for all x,y,

    ch(E_x^vee) ch(E_y) td(Y)
      =(2-21 eta)^2(1+2 eta)=4-76 eta,
    chi(E_x,E_y)=-76.

Thus the derived-fibre dimensions are (0,76,0) off the isomorphism
locus and (1,78,1) on it. Equivalently v=(2,0,-19) has square 76.
There is no mixed term after restriction of the parameters to points.
At r, minimality therefore supplies a representative

    K_R: R --d0--> R^78 --d1--> R

in degrees 0,1,2, whose differentials vanish modulo m. Choose a basis
of the last R and let I be the ideal generated by the 78 entries of
d1. Then I is contained in m and the actual ordinary top stalk is R/I.
This follows by taking cohomology of the perfect representative, with
no ordinary middle-sheaf base-change assumption.

For completeness the representative spreads to a neighborhood of r.
There its top cokernel tensored with any residue field is its top
derived-fibre cohomology, since it is the cokernel of the last row.
Stable Hom/Serre and Nakayama identify its support with the isomorphism
locus. Shrink away from the diagonal and the other finitely many
off-diagonal coincidences of L121. The top sheaf is then supported
only at r. This support observation alone supplies no multiplicity.

**Comparing the actual infinitesimal sequence.** Write E_1=E_b and
E_2=E_c. For t=(u,v) in T_rT=T_bB direct sum T_cB let
A=k[epsilon]/(epsilon^2), with R -> A determined by t. Pulling back
the two actual families gives bundles E_{1,A}, E_{2,A} on Y_A. Their
Hom bundle V_A has the exact coefficient sequence, viewed on Y,

    0 -> V_0 --epsilon--> V_A -> V_0 -> 0,
    V_0=Hom(E_1,E_2).                                      (1)

Its exactness follows from local freeness over A. The analogous
sequence holds for V_rev=Hom(E_2,E_1).

Here is a concrete natural comparison with the minimal representative.
Take a finite affine cover of separated Y. Its finite Cech complex J
for the coefficient over Y times Spec R has R-flat terms: on each
affine intersection that coefficient is a projective module over the
product coordinate ring, which is R-flat. It represents Rp_* locally,
and tensoring with A or k gives the actual base-changed Cech complex.
Choose a chain map K_R -> J representing the derived isomorphism;
bounded free K_R permits such a map. Both complexes are bounded flat,
so tensoring preserves this quasi-isomorphism. This gives a commuting
diagram with exact rows

    0 -> K_k -> K_A -> K_k -> 0
         |       |       |
    0 -> J_k -> J_A -> J_k -> 0.

The first arrows are epsilon and the last arrows are reduction. The
bottom row computes (1). Connecting-map naturality (0117) identifies
both degrees zero and one with those of the top row. Coherent GAGA on
projective Y is exact and natural on (1), and Dolbeault computes its
analytic connecting maps. This verifies the maps, not just equality
of cohomology dimensions. The same construction applies to K_rev.

Since K_k has zero differentials, the degree-one connecting map is
exactly the linearization ell(t) of d1: lift a middle vector to K_A,
apply d1_A, and divide by epsilon. Under the above identifications,

    ell(t): Ext^1(E_1,E_2) -> Ext^2(E_1,E_2).              (2)

**The two-sided differential and its reverse transpose.** Choose smooth
trivializations of the two actual dual-number bundles and write their
Dolbeault differentials as dbar_i+epsilon a_i. Here a_1 and a_2 are
closed End-valued (0,1)-forms representing kappa_b(u), kappa_c(v),
respectively, by L118's natural KS identification. Such splittings
exist for these bundle extensions in the smooth category. On a
degree-j forward Hom form beta, the perturbed differential is

    dbar_Hom beta + epsilon (a_2 wedge beta-(-1)^j beta wedge a_1).

Thus the actual degree-one connecting map (2) is

    ell(t)[beta]=[a_2 wedge beta+beta wedge a_1].           (3)

On a closed reverse degree-zero morphism psi:E_2 -> E_1 its reverse
connecting map is

    delta_rev(t)psi=[a_1 psi-psi a_2]
                     in Ext^1(E_2,E_1).                  (4)

Changing either smooth splitting changes the induced expressions by
coboundaries, as also follows from the intrinsic sequence (1).

Choose any isomorphism phi:E_1 -> E_2 and put psi=phi^{-1}. This psi
generates Hom(E_2,E_1). The two Serre pairings

    P(psi,z)=integral_Y sigma_Y wedge Tr_{E_1}(psi z),
    Q(w,beta)=integral_Y sigma_Y wedge Tr_{E_1}(w wedge beta)

are perfect in degrees (0,2) and (1,1) between reverse and forward
Hom. Nondegeneracy is surface Serre duality and the perfect coefficient
trace pairing. In particular P(psi,-) is a nonzero isomorphism
Ext^2(E_1,E_2) -> C. No sign or positivity convention for a metric
is needed; the same nonzero Serre normalization is used throughout.

For closed beta of degree one, graded cyclicity, with both a_1 and
beta odd, gives

    Tr(psi beta wedge a_1)=-Tr(a_1 psi wedge beta).

Consequently (3) has the exact transpose formula

    P(psi,ell(t)[beta])
      = integral_Y sigma_Y wedge Tr((psi a_2-a_1 psi) wedge beta)
      = -Q(delta_rev(t)psi,[beta]).                       (5)

Both independently varying factors remain in (3)--(5). In particular
this is not the scalar commutator of one moving bundle; that would
erase the needed off-diagonal difference.

**Full rank and the ordinary length.** Compose (4) on the right with
phi to identify its target with Ext^1(E_1,E_1). It becomes

    (delta_rev(t)psi) phi
         = kappa_b(u)-psi kappa_c(v) phi.                 (6)

The natural stable-moduli tangent comparison in L118 identifies these
two summands with df_b(u) and df_c(v) in the same tangent space at
f(b)=f(c). Conjugation by an isomorphism is exactly that natural
identification; the scalar ambiguity acts trivially. L121 says their
two complex two-planes have zero intersection, and L118 says each
differential is injective. Hence (6) vanishes only when u=v=0.
The reverse degree-zero map on the selected generator is therefore
injective on all of T_rT, of complex dimension four.

By perfectness of Q and (5), ell(t)=0 implies delta_rev(t)psi=0,
and thus t=0. The transpose of t |-> ell(t), after choosing the last
R-generator, is precisely the map sending a middle residue vector
to the linear part of its last-row coefficient in m/m^2. Since the
former is injective, these coefficients span the entire cotangent
space: actual rank four equals required rank four. Therefore

    I+m^2=m.

The finite R-module m/I satisfies m(m/I)=(m^2+I)/I=m/I. Apply
[Stacks Lemma 10.20.1, 00DV, part (2)](https://stacks.math.columbia.edu/tag/00DV):
m lies in the Jacobson radical, so m/I=0. Thus I=m, including all
higher-order row terms, and the actual top cohomology stalk is R/m,
of length one. Exchanging the two coordinates repeats the proof for
the reverse Hom stalk. No extra target or independent mechanism is
introduced by that symmetry.

**Limitations and traps.** Reduced coincidence was not substituted for
an annihilator theorem: it furnished natural tangent information,
while (1)--(5) separately identify the actual top-row variation. A
derived Ext^2 dimension of one furnished a minimal last-row rank only,
not its cokernel length. Both Hom factors, the odd cyclic sign and
reverse rather than self-Hom duality are retained. Nakayama uses the
whole four-dimensional cotangent space, not a radical or a rank test
on one parameter surface. This is compatible with a central isolated
Hom jump, exactly the limitation recorded in ATTEMPTS/046. If the
off-diagonal locus is empty the statement is vacuous. A useful global
count or defect comparison remains a separate unproved gap.

**Separate critical audit, 2026-10-20 (step 419).** The prior SPECIALIZE
assessment is
`drafts/literature/2026-10-20-opposite-hom-stalk-critical-audit.md`.
This audit finds no substantive error or stronger conclusion. Its
outcome is EXPLORATION / RESEARCH / REPRODUCTION, actual task proof_audit.
It checks this specialization under the stated inputs, rather than
independently reproving the entire upstream equality-kernel route.

First, the coefficient really is a vector bundle on the product with
the fixed projective surface. Its restriction to an affine intersection
U=Spec C_U of a finite affine cover of Y is a finite projective module
over C_U tensor_k R, where k=C is the ground field. This algebra is R-flat,
since C_U is a k-vector space, and its projective coefficient module
is R-flat as well. Separatedness of Y makes all finite intersections
affine. The alternating finite Cech complex J is bounded and computes
the actual coefficient cohomology after either base change R -> A or
R -> k. The base-change inputs are Stacks 0B91 and its concrete
flat-coefficient proof case 0A1D, as checked in the audit assessment.

The chosen derived isomorphism K_R -> J is represented by an R-linear
chain map because K_R is bounded projective. Its cone is a bounded
acyclic complex of flat modules. Starting at its last nonzero degree,
the short exact sequences of cycles show inductively that every cycle
is flat: in 0 -> Z^i -> C^i -> Z^{i+1} -> 0 both C^i and Z^{i+1}
are flat, so Z^i is flat. Those sequences remain exact after arbitrary
tensoring. Thus the cone stays acyclic after tensoring with A and k;
the vertical maps in the displayed epsilon diagram are indeed
quasi-isomorphisms. This reasoning also covers the zero tangent,
where R -> A need not be surjective. Flatness of each term preserves
0 -> k -> A -> k -> 0 as an R-module sequence. All three vertical
arrows arise from the same chain map, so they commute with epsilon
and reduction, not merely with an abstract cohomology identification.
Connecting-map naturality therefore identifies the actual coefficient
connecting map with the derivative of the minimal last row. Exact
GAGA and the natural Dolbeault resolution apply to the same sequence
of coherent O_Y-modules, including the dual-number middle term.

Next, the two independent deformations cannot be combined into a
single adjoint variation. Direct differentiation of a degree-j Hom
coefficient gives a_2 beta-(-1)^j beta a_1. Hence degree one has the
plus sign in (3), while reverse degree zero has the minus sign in
(4). After fixing phi and psi=phi^{-1}, cyclic permutation of the odd
forms beta and a_1 gives

    Tr(psi beta a_1)=-Tr(a_1 psi beta),
    P(psi,ell(t)beta)=-Q(a_1 psi-psi a_2,beta).

The fixed sigma_Y has even degree and introduces no additional sign.
These are pairings between reverse and forward Hom, not an assumed
self-pairing of one complex. Serre duality makes Q perfect and makes
P(psi,-) nonzero on the one-dimensional Ext^2. Scaling phi changes
the selected generator but cannot change any of these rank tests.

Finally, both KS classes are compared in one actual coarse tangent
space. L118's same-extension comparison carries each dual-number
family to its natural Ext^1 class. Transport of the second bundle by
phi acts on that class by conjugation; stable scalar automorphisms act
trivially. L121's two complex two-planes have zero intersection there,
retaining L120's finite birationality input. Consequently
kappa_b(u)-psi kappa_c(v)phi=0 forces u=v=0. Perfectness of Q then
makes the map t -> ell(t) injective on the entire four-dimensional
T_r(B times B). Dualizing gives surjectivity from the 78 middle
residue classes onto m/m^2. The Ext dimensions (1,78,1) follow from
the full charge-21 computation chi=-76, not the earlier charge-seven
model. With I contained in m, surjectivity is precisely I+m^2=m.
The finite module m/I satisfies m(m/I)=m/I, so local Nakayama gives
I=m. This proves the whole ordinary cokernel is k, including all
higher row terms. There is no appeal to ordinary middle-sheaf base
change, radical support, or an arbitrary model differential.

The direct mathematical inputs remain L071, L118 and L121, with L120
retained through L121. L066/L110 are comparisons only. No DAG edge or
main argument changes. This verifies the previously stated local
multiplicity, not existence of F or of a collision, a global count,
image separation, or a Hodge-conjecture resolution. ATTEMPTS/046's
isolated-central-jump limitation remains intact. The audit gives no
advance beyond the inspected known relative-Ext mechanism.

## Mathlib

Full matching coverage for this actual-family relative Hom stalk
specialization is **not checked**, not asserted absent. The imported
perfectness/base-change, minimal-complex, natural deformation, Serre
duality and Nakayama inputs have precise citations above and in the
reused assessment. The specialization is a REPRODUCTION of known
mechanisms with a conditional local conclusion, not a novelty claim or
a verified Hodge resolution. The separate audit above preserves the
conditional specialization; full matching Mathlib coverage is still
not checked.
