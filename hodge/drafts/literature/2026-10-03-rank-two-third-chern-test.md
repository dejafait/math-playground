# Rank-two terminal bundle: third-Chern consistency — literature assessment

TARGET: Test the rank-two identity c_3(F)=0 against L029's mixed terminal-resolution Chern character for I_C^{oplus 2}, allowing arbitrary factor residues in L025's final W.
CHECKED: 2026-10-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded searches on 2026-10-03 screened rank-two third-Chern constraints, K3 products with real multiplication, doubled ideal-sheaf resolutions and normalization/Riemann--Roch formulas; representative queries and scope limits are recorded below. Reused the adequate doubled-source assessment for unchanged stability and generation inputs.
SOURCE_EVIDENCE: Read Fulton, Intersection Theory, second edition (1998), Theorem 3.2(a), pp. 50--52, Theorem 15.2, pp. 286--287, Theorem 18.3(1),(3),(5), pp. 353--354, and Example 18.3.3, p. 360, https://djvu.online/file/87GFN2nbfbdF7; Stacks Section 42.45, Tag 02UM, https://stacks.math.columbia.edu/tag/02UM, Lemma 42.39.1, Tag 02UD, https://stacks.math.columbia.edu/tag/02UD, Remark 42.56.11, Tag 0FET, https://stacks.math.columbia.edu/tag/0FET, and Sections 42.65--42.66, Tags 02UN/02UO. Precise applicability is below.
COMPARISON: Rank truncation, higher-character identities, exact-resolution additivity and proper Riemann--Roch are known. L029 computes only through degree four; L028's undoubled parity exclusion and L030's rank-divisible exclusion do not settle this changed test. No inspected result computes or excludes the full doubled rank-two terminal class in the final W with arbitrary residues and integral twist.
GAP: Apply the cited formulas to the existing finite normalization and the full signed terminal resolution, then compare degree-six classes under L029's actual invariant c_1,c_2 conditions. The support's third character and any resulting obstruction are uncomputed; formal compatibility would leave maps, stability and transverse transport open.
REASON: The missing higher-character coverage is now supplied without deriving a specialization. A separate mathematical turn may test this different rank identity; it does not renew the exhausted divisible/residue construction or the stopped resolved-map recipe.
SCOPE: X=S x S, the same very general cubic RM member and final W/metric as L025--L029; an actual rank-two locally free terminal bundle, arbitrary integral factor residues in W, any actual integral terminal twist, and the full first-two-Chern invariance hypotheses. Coverage includes finite-normalization bookkeeping and the degree-six consistency comparison, not bundle existence or higher Chern tests.
COVERED_TARGET: Compute the degree-six Chern character of O_C from L019's finite normalization sequence and proper Grothendieck--Riemann--Roch, retaining all three double points.
COVERED_TARGET: Determine whether the rank-two third-Chern condition imposes a residue-independent obstruction after L029's invariant c_1,c_2 equations in L025's final W, or only an additional necessary moment equation.

## Hypotheses

Preserve the exact saved target. Use L029's actual sequence

\[
0\longrightarrow E\longrightarrow P_2\longrightarrow P_1
 \longrightarrow P_0\longrightarrow I_C\oplus I_C
 \longrightarrow0,
\qquad F=E\otimes M,
\]

with rank(E)=2, product-line summands whose integral factor classes
belong to L025's final W, and an actual integral line bundle M.
Retain the common metric and invariant c_1(F),c_2(F).
Invariant c_1 is not assumed zero. No uniform rank divisibility,
integral chamber conjugation, exact maps or stability is inferred
from a virtual class.

The [earlier assessment](2026-09-27-doubled-source-cubic-resolution.md)
is sufficient for its unchanged generation, stability and invariant-form
framework. Its old construction window and the
[divisibility failure](../../ATTEMPTS/020-doubled-source-divisible-presentations.md)
remain closed. This review extends source coverage to a necessary
higher-degree identity, not to another construction search.

## Conclusion

The source comparison is complete for the scoped test. Import the
standard identities by citation and specialize only their application
to C and the terminal resolution in a separate research turn.
SPECIALIZE does not mean that the bundle exists or is excluded.
No degree-six coefficient, new obstruction or lemma is derived here.

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. The search did
not establish a full literature match; it establishes no originality.
No essential source remains unread or blocked for this consistency
test. Mathematical exploration usage is unchanged.

## Proof — source statements and applicability, without a new proof

### Rank identity, additivity and the twist

Fulton, [Theorem 3.2(a), printed pp. 50--52](https://djvu.online/file/87GFN2nbfbdF7),
states that Chern classes above a vector bundle's rank vanish.
This covers the proposed c_3(F)=0 input. It applies to an actual
locally free F, not merely to a rank-two coherent or virtual class.

Read [Stacks Section 42.45, Tag 02UM](https://stacks.math.columbia.edu/tag/02UM),
including its displayed expansion

\[
\operatorname{ch}_3(G)
 =\frac{c_1(G)^3-3c_1(G)c_2(G)+3c_3(G)}6,
\]

and Lemmas 42.45.2--42.45.4. The character is defined using
exponentials of Chern roots; Lemma 42.45.2 gives additivity and
[Lemma 42.45.3, Tag 0F9D](https://stacks.math.columbia.edu/tag/0F9D)
gives tensor-product multiplicativity. Also read the exact twist
formula in [Lemma 42.39.1, Tag 02UD](https://stacks.math.columbia.edu/tag/02UD).
These supply the higher-character and integral-line-twist bookkeeping.
Do not reprove them or replace M by a rational normalization.

[Remark 42.56.11, Tag 0FET](https://stacks.math.columbia.edu/tag/0FET)
supplies additive and multiplicative character maps on perfect K-groups,
including distinguished-triangle additivity. This is the needed scope
for the coherent ideal source in the actual resolution; vector-bundle
Whitney additivity alone is not a statement about its singular kernels.
The cited formulas do not supply presentation maps.

### Proper Riemann--Roch and the singular support

Fulton, [Theorem 15.2, printed pp. 286--287](https://djvu.online/file/87GFN2nbfbdF7),
applies to any proper morphism f:Y -> Z between nonsingular varieties:

\[
\operatorname{ch}(f_!u)\operatorname{td}(T_Z)
 =f_*\bigl(\operatorname{ch}(u)\operatorname{td}(T_Y)\bigr).
\]

The theorem does not require f to be smooth or an embedding.
The normalization's ambient map has the required smooth source
and target by L008. Its precise application is left to the calculation.

Read [Theorem 18.3(1),(3),(5), pp. 353--354, and Example 18.3.3,
p. 360](https://djvu.online/file/87GFN2nbfbdF7).
They give covariance, the smooth-ambient character comparison and
the leading support term. The example compares Todd components under
a proper birational map that is an isomorphism off Z: components of
dimension greater than dim(Z) agree with the pushed components.
This is supporting coverage for finite singular corrections, not
a printed formula for this C.

Use the existing geometry rather than apply a smooth-support normal
bundle formula to C. L019 equation (10) already supplies the finite
normalization sequence with one skyscraper quotient at each of its
three double points. L008 supplies smooth W, finite normalization
and its canonical class. These are saved mathematical inputs, not
new calculations or substitutes for the required degree-six comparison.

[Stacks Section 42.65, Tag 02UN](https://stacks.math.columbia.edu/tag/02UN)
supplies the Todd expansion, including its first term c_1/2.
Read [Section 42.66, Tag 02UO](https://stacks.math.columbia.edu/tag/02UO):
its displayed Riemann--Roch case assumes a proper smooth morphism
and locally free higher images. Those hypotheses are not the present
normalization map's hypotheses. Use Fulton's broader theorem above;
do not silently attribute that scope to the Stacks paragraph.

The scan's second-edition identity was checked in the
[earlier source audit](2026-10-03-universal-sheaf-global-support-reduction.md).
Its host title says 1997; the book version used is the second edition,
1998. The new readings used the printed page numbers stated above.

### Closest previous results and the remaining difference

Reread L029 in full. Its signed resolution character, invariant first
moments and forced mixed second-character operator concern degree four
and below. Its integral signed-line example is confined to the
pre-chamber model and does not produce a rank-two bundle. No existing
notebook ch_3 calculation was found by the scoped search through lemmas,
drafts and foundations.

L028 fixes the undoubled transcendental coefficient and uses distinct
primary factors modulo two. L030 instead imposes divisibility of every
factor by terminal rank and excludes r>=3. Neither is an unrestricted
rank-two third-Chern obstruction. Keep both scoped failures intact.

Reuse the earlier assessment's primary readings of Mistretta,
[math/0310185v2, Theorem 3.1 and Lemma 3.4/Corollaries 3.5,3.10,
pp. 7--11](https://arxiv.org/pdf/math/0310185v2#page=7), and Verbitsky,
[alg-geom/9307008v1, Theorem 2.5, p. 9](https://arxiv.org/pdf/alg-geom/9307008v1#page=9).
The former's stable-terminal theorem uses an ideal source and powers
of one ample bundle; its general generation consequences do not
prescribe this doubled mixed resolution. The latter starts from an
existing stable bundle with invariant first two Chern classes.
Neither supplies this rank-two class or its higher-character consistency.
These sources were already adequately assessed and were not reread
merely to repeat that coverage.

## Required specialization and stopping test

The relevant gap is a representative that could permit transport in
the fourth NS-fixed RM direction. The proposed intermediate test is
a rank-two necessary consistency condition independent of L030's
extra divisibility. Compare the full degree-six identity, retaining
both factor components, the existing singular normalization correction,
all terms of the exact resolution and any permitted integral twist.
Use L029's invariant c_1,c_2 hypotheses without replacing them by
c_1=0 or by the pre-chamber example.

Continue for a structural incompatibility valid for the stated scope,
or a precise surviving necessary constraint with an independently
testable downstream use. If the equation is only an adjustable moment
condition, record that limitation and reassess; more residue sampling
or another signed virtual class alone does not justify reopening the
old construction. Complete the decision within the shared exploration
budget. None of these mathematical tests ran in this literature turn.

Even a consistent character leaves exact maps, local freeness and
stability to establish, followed by transverse transport. The known
span remains 21 on the existing family; three directions are attained
against four required. Arbitrary primitive fourfold classes and the
universal rational Hodge target remain unresolved. Rechecked Deligne's
[Clay statement, section 1 and remark 2(ii), p. 2](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf#page=2):
the rational formulation and finite-resolution discussion do not
prescribe a stable representative of rank two.

## Search and access record

Queries on 2026-10-03 included:

- `"K3" "product" "rank two" "Chern" bundle real multiplication`
- `"Chern character" "ch_3" "rank 2" Grothendieck Riemann Roch normalization`
- `"ideal sheaf" "non Cohen Macaulay" "third Chern" resolution`
- `"rank two" "third Chern" "K3" product`
- `"doubled" "ideal sheaf" "Chern" resolution K3`
- `"normalization" "Chern character" "surface" singular Riemann Roch`
- `"rank two" "terminal" "resolution" "Chern" Mistretta`
- `"K3" "real multiplication" "third Chern"`
- `"hyperholomorphic" "rank two" "product" "K3" Chern`
- `"Grothendieck-Riemann-Roch" "normalization" "third Chern"`
- `site:stacks.math.columbia.edu "Grothendieck-Riemann-Roch" smooth proper`
- `site:stacks.math.columbia.edu "c_i" "i > r" "Chern"`

Read the theorem statements, relevant proof scope and formulas in
the primary texts above, not search snippets as theorem evidence.
Other returned leads concerned sheaves on a single surface or P^3,
Hilbert powers, and twisted product constructions. Their full statements
were not all inspected, and no exclusion or theorem is imported from
them. They are not essential dependencies for this necessary-character
test. The bounded search did not identify a full match and cannot
certify novelty or exhaustive coverage.

## Mathlib

Coverage: **not checked** for the full rank-two consistency target.
No Mathlib match or absence from checked Mathlib sources is asserted.
The named, directly linked Fulton and Stacks statements are supporting
rank, character and Riemann--Roch inputs; they are not Mathlib theorem
identifications or a match for the complete terminal-resolution test.
Library lookup was not necessary for this assessment.
