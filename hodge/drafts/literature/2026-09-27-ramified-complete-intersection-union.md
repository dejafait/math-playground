# Ramified complete-intersection union — literature assessment

TARGET: Determine whether an admissible complete-intersection union Y admits a flat lift over C[tau]/(tau^3) with product ambient deformation constant modulo tau^2 and order-tau^2 class in V_RM outside V_D, allowing arbitrary first-order motion of Y.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched ramified K3/RM correspondences, second-order sheaf obstructions, direct sums, deformations of morphisms and relative basic double linkage; read the primary statements identified below and reused the sufficient earlier singular-embedded and liaison comparisons.
SOURCE_EVIDENCE: Huybrechts--Thomas, arXiv:0805.3527v2, Corollary 3.4, p. 14, https://arxiv.org/pdf/0805.3527v2#page=14, with the 2014 erratum; Fiorenza--Iacono--Martinengo, arXiv:0904.1301v3, Theorem 7.6 and section 8, pp. 19--20, https://arxiv.org/pdf/0904.1301v3#page=19; Iacono--Lepri--Martinengo, arXiv:2605.19616v1, Theorem 5.5 and Corollary 5.7, p. 23, https://arxiv.org/pdf/2605.19616v1#page=23; further scope comparisons and direct links below.
COMPARISON: Known small-extension theory treats a specified first-order sheaf, and fixed-ambient sheaf/morphism theory retains its deformation data. None of the inspected statements computes this union's ramified obstruction or recovers its ideal summand for every earlier motion; L022 supplies only the central first-order exclusion.
GAP: Control arbitrary first-order union motion when lifting the linkage data over the length-three base, then evaluate the full obstruction or justify ideal recovery without assuming a preserved splitting, filtration or component. No such order-two calculation is supplied here.
REASON: Import the general obstruction tools and specialize their missing compatibility with this singular union. Ramification changes the lifting problem; neither central naturality nor fixed-ambient smoothing settles it. The exact target is retained for a separate research turn.

## Hypotheses

Use the same very general cubic S, X=S x S, original ample product H,
and admissible Y=C union V(f,g) of L022, with m,n>0. The ambient product
comes from a marked NS-fixed deformation of S, trivial modulo tau^2;
its order-tau^2 coefficient is required to lie in V_RM. The embedded
Y modulo tau^2 may have arbitrary first-order motion inside the
constant product. Neither its components nor any linkage splitting
are assumed constant or preserved.

Write A_1=C[tau]/(tau^2) and A_2=C[tau]/(tau^3). Retain the actual
ideal at every point, including C's three non-lci double points.
Admissibility means that f belongs to H^0(I_C(nH)), g belongs to
H^0(O_X(mH)), (f,g) is regular with smooth zero surface B, and g is
a nonzerodivisor on O_C. No ordering of m,n or existence of admissible
sections for every pair is added. Their lifts are not given data.

Reuse the unchanged rational Hodge formulation in the
[primary-source audit](../../foundations/01-target-and-scope.md).
The target is still rational cycle-class surjectivity for every smooth
projective complex variety, not an integral or nonprojective variant.

## Conclusion

The source review is complete: SPECIALIZE. The known general theories
below are supporting results to import by citation. None is a match
for the full saved target. The new work justified by this assessment
is only their explicit application to arbitrary earlier motion and
the union's forgotten presentation; no general theory needs reproof.

The constructive threshold is an actual flat lift whose later ambient
coefficient lies outside V_D. An exclusion must cover every allowed
first-order motion, rather than just the constant one. Even a successful
order-two lift would leave higher-order extension, algebraization,
transcendental action in an actual family, and the universal Hodge
problem unresolved. The attained span remains 21 on the known family.
The first-order bound remains at most three RM directions against
four required; this review supplies no new ramified bound or surface.

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION: one exploration
turn after L022's informative negative result. The outcome is a source
comparison and an actionable specialization, not a mathematical advance,
reproduction, or result beyond the checked literature. Failure to find
the exact theorem does not establish originality. No essential source
access gap remains for the selected framework.

## Proof

The evidence consists of primary statements and their scope comparisons;
there is no proof or calculation of a new lifting assertion here.

### The specified small extension, not just the central fibre

Reread Huybrechts--Thomas, *Deformation-obstruction theory for complexes
via Atiyah and Kodaira--Spencer classes*,
[arXiv:0805.3527v2 (15 September 2013), introduction, pp. 1--2, and Theorem 3.3/Corollary 3.4, p. 14](https://arxiv.org/pdf/0805.3527v2#page=14).
For a perfect complex on a noetherian separated scheme and a square-zero
thickening embeddable in a smooth ambient scheme, the product of its
truncated Atiyah class with the thickening's Kodaira--Spencer class is
the full obstruction to a perfect lift; the lifts, when nonempty, form
the stated Ext^1 torsor. Reducedness of the smaller scheme is not required.

The application to review is X_(A_1) inside X_(A_2), with the chosen
first-order sheaf as input. A central splitting is not a splitting of
that input. In particular, using only the ordinary differential sheaf
of the smooth central X would omit the nonreduced-base issue. The
theorem does not compute this input's obstruction or preserve its maps.
The ambient embedding and perfectness checks must accompany the use.

Also reread the
[2014 erratum, Math. Ann. 358, 561--563, p. 561](https://link.springer.com/content/pdf/10.1007/s00208-013-0999-x.pdf#page=1).
It requires flatness over the auxiliary base in the relative formulation
and explicitly retains the absolute formulation over a field. Select
the corrected absolute criterion over C, rather than applying an
uncorrected relative statement over a nonreduced base. The v2 source
incorporates the correction.

### Earlier motion and the difference between sheaves and their maps

Read Fiorenza--Iacono--Martinengo, *Differential graded Lie algebras
controlling infinitesimal deformations of coherent sheaves*,
[arXiv:0904.1301v3 (19 November 2009), section 1, p. 4, Theorem 7.6 and section 8, pp. 19--20](https://arxiv.org/pdf/0904.1301v3#page=19).
Their deformation functor concerns flat coherent sheaves on the fixed
X over local Artin algebras in characteristic zero. A locally free
resolution gives the endomorphism dg Lie algebra whose Maurer--Cartan
functor, with descent and gauge equivalence, controls these deformations;
the tangent and obstruction spaces are Ext^1 and Ext^2. Negative
cohomology vanishing needed for the descent theorem is supplied for
coherent sheaves in section 8.

This is an available description of arbitrary motion on the constant
first-order product. It is not an assertion that a deformation of a
direct sum stays split, or that its self and mixed extension data may
be discarded. Its fixed-ambient statement alone does not supply the
later ambient coefficient. No formality theorem or quadratic-only
description at all orders is assumed; no block product is evaluated here.

Read Iacono--Lepri--Martinengo, *Deformations of morphisms of coherent
sheaves*,
[arXiv:2605.19616v1 (19 May 2026), Theorem 5.5, Remark 5.6 and Corollary 5.7, p. 23, and Remark 5.9, p. 24](https://arxiv.org/pdf/2605.19616v1#page=23).
This preprint controls simultaneous deformation of two coherent sheaves
and their morphism on a fixed smooth variety in characteristic zero.
Theorem 5.5 identifies the deformation groupoid with a dg Lie algebra
model; Corollary 5.7 gives its long exact sequence involving self-Ext
and mixed Ext. Remark 5.6 retains the compatible-resolution requirement
for broader settings. Remark 5.9 separately treats the graph inside a
fixed middle sheaf, with Hom tangent and Ext^1 obstruction spaces.

This supplies a precise comparison for recovering a chosen map, beyond
deforming its endpoints. It provides no general smoothness of the
forgetful map and no relative linkage recovery in our prescribed
deformation of X. It is a supporting comparison, not a necessary new
premise replacing the corrected small-extension criterion.

### Linkage, smoothing and previously screened tools

Reuse the theorem-level liaison comparison in the
[complete-intersection assessment](2026-09-27-ample-complete-intersection-union.md):
Migliore--Nagel,
[*Applications of Liaison*, Theorems 2.7--2.8, pp. 5--6](https://academicweb.nd.edu/~jmiglior/MN14-webpg.pdf#page=5),
and Hartshorne,
[*On Rao's theorems and the Lazarsfeld--Rao property*, Hypotheses 2.1 and Theorem 3.4, pp. 377 and 382](https://www.numdam.org/item/AFST_2003_6_12_3_375_0.pdf#page=9).
Their construction and biliaison conclusions concern a fixed ambient
scheme with their stated hypotheses. They do not assert that an
arbitrary deformation of Y preserves its linkage presentation in a
prescribed moving product. No new reading of these sources is claimed.

The new searches also located Nollet--Rao, *Smoothing surfaces on
fourfolds*, Canad. Math. Bull. 68 (2025), 1389--1410. Read
[Theorems 1.2--1.3, p. 1390, Hypotheses 3.1 and 4.1, pp. 1398--1399 and 1404, and Theorem 4.5, p. 1406](https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/71AD4FADE0EE92EDE18D4768FACAE54F/S0008439525100751a.pdf/smoothing-surfaces-on-fourfolds.pdf#page=2).
The first theorem produces smooth degeneracy loci for general maps
under CD2 reflexivity, filtration, global-generation and rank-gap
hypotheses on a fixed smooth threefold or fourfold. Theorem 4.5 gives
smoothability of integral members of specified linkage classes in
projective three- or four-space, subject to its sheaf hypotheses.
Neither statement provides containment in our assigned X_(A_2) or a
lift of every earlier union motion. No identification of our singular
middle sheaf with their CD2 reflexive input is supplied. These are
stronger fixed-ambient smoothing comparisons, not a solution of the
ramified target.

Reuse Buchweitz--Flenner's singular embedded criterion as assessed in
the [earlier ramified review](2026-09-27-ramified-three-rotation-lift.md):
[Lemmas 7.6--7.7 and Theorem 7.8, pp. 190--191](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/712BFB5F73E0C38B4B32206699B0277F/S0010437X03100413a.pdf/a-semiregularity-map-for-modules-and-applications-to-deformations.pdf#page=56).
Its small-extension obstruction for a flat closed subspace permits a
nonreduced lower base. It is an alternative framework for the actual
embedded Y_(A_1), without replacing this singular union by a smooth
complete intersection or its normal bundle. The conditional
semiregularity theorem gives no automatic vanishing here.

The [direct-summand assessment](2026-09-27-direct-summand-obstruction-recovery.md)
already inspected the nilpotent-reduction criteria
[Stacks 07LU](https://stacks.math.columbia.edu/tag/07LU),
[0H75](https://stacks.math.columbia.edu/tag/0H75) and
[0654](https://stacks.math.columbia.edu/tag/0654), and the chosen-quotient
obstruction in [0CZU](https://stacks.math.columbia.edu/tag/0CZU).
Their general statements are reused, not newly searched. They can
support perfectness and base-flatness checks at a further nilpotent
extension; they do not supply a lift or a compatible quotient by
themselves. The earlier Pridham comparison remains sufficient:
[Corollaries 2.22 and 2.25, Remark 2.27](https://arxiv.org/pdf/1208.3111v4#page=18)
control the semiregularity image, not the unresolved kernel. Neither
Hodge persistence nor passing to a trace settles the full obstruction.

### Redundancy, downstream use and the bounded test

The first-order smooth complete-intersection route is stopped by L022.
The cohomology range L.F>=4 cannot remove that obstruction and is not
a reason to repeat its inclusion-lifting test. The possible ramified
mechanism changes the order of the ambient deformation and permits
nonconstant earlier motion; it is not justified by relabeling the
same first-order lift. L016's ramified rotation calculation retained
all first-order motions, but its geometry and trace argument concern
a different representative.

Read L022, the relevant L018 extension argument, ATTEMPTS/015 and
history 031, after the whole overview and DAG. L022's known central
middle sheaf is E=I_C(-mH) direct sum O_X(-nH), with extension kernel
O_X(-(m+n)H). Its proof explicitly recovers existence of some central
summand lift, not compatibility with a given earlier deformation.
The new target does not assume that this missing compatibility follows.

One bounded specialization of the unchanged target is justified:

1. Check whether the central linkage extension can be recovered over
   A_2 from an arbitrary embedded Y lift, keeping its reduction over
   A_1. Audit extension recovery across this small extension rather
   than assuming L022's dual-number argument already handles it.
2. If a middle sheaf is recovered, retain every allowed first-order
   self and mixed extension of its two central summands. Use the
   cited obstruction for that actual A_1 sheaf. Test whether the
   relevant mixed groups/products or a justified filtration recovery
   can rule out cancellation of the later ambient obstruction. A
   central retraction, a dimension count, or a nonzero Ext group is
   not that test's answer.
3. For an exclusion via a recovered ideal, justify its flat coherent
   and embedded reconstruction over A_2, including infinity, and
   control its earlier motion before applying the central obstruction
   from L008. For a positive result, construct the full flat embedded
   Y_(A_2); a perfect middle-sheaf lift alone is insufficient.

Continue on an actual transverse lift or a specific surviving
cancellation with a bounded remaining compatibility check. Stop this
representative if every permitted earlier motion is excluded. Failure
only for the constant motion, one degree ordering or a selected union
does not exclude the whole existential target. Do not restart the
unnecessary first-order inclusion-cohomology classification. This is
the first exploration turn in this assessment/test sequence; finish
the continuation or stop decision within the shared three-turn budget.

The possible downstream gain is still an algebraic representative
extending the non-scalar action U beyond the Dickson family, since
L018's cycle identity adds only a divisor-product class. A second-order
success would be an intermediate result, not the required actual-family
extension or the universal Hodge conjecture. No order-two obstruction
identity, cancellation, flat lift or recovery theorem is derived here.

### Search record and access boundary

Queries on 2026-09-27 included:

- `"K3" "real multiplication" "ramified" deformation correspondence`
- `"direct sum" sheaves "second order" obstruction`
- `"basic double" linkage deformation Artin`
- `sheaf deformations second order obstruction Yoneda square Maurer Cartan`
- `deformation "direct sums" sheaves "Yoneda"`
- `coherent sheaves deformations differential graded Lie algebra Fiorenza Iacono Martinengo theorem`
- `"basic double linkage" "infinitesimal" deformation`
- `"liaison" "deformation functors" "Artin"`
- `"K3" "complete intersection" "ramified" "correspondence"`
- `"Yoneda square" "obstruction" sheaf deformation pdf`

Exact-geometry searches did not locate a theorem deciding the saved
lift. Broader queries located the fixed-ambient smoothing and morphism
papers above; their actual statements, rather than search summaries,
were compared. The source versions and theorem numbers identify the
copies inspected. The FIM numbering is that of v3, not an assertion
about the journal version's numbering. The 2026 morphism source is a
preprint, not a claimed published theorem.

Lepri's *Cyclic forms on DG-Lie algebroids and semiregularity* (2024)
was inspected only at the introduction, not used as theorem evidence.
Search leads for *Liaison and deformation*, vector-bundle Yoneda-square
formulas and recent Higgs-bundle results were not read at theorem level
and are not inputs. Illusie's original general theory and the original
liaison references behind the reused assessments were not independently
read this turn. The selected perfect-complex and coherent-sheaf
frameworks were accessible in primary text, so none of those unread
leads is an essential source dependency. This is a bounded assessment,
not a claim that no matching result exists anywhere.

The pending assessment's exact target, degree range, allowed earlier
motion and relevance are preserved. Its REVIEW_REQUIRED decision is
replaced only after this source comparison; the calculation is reserved
for the next ordinary research turn. See
[history 032](../../history/032-2026-09-27-ramified-complete-intersection-literature.md).

## Mathlib

Coverage: **not checked** for the full ramified union statement and
the supporting obstruction, morphism and liaison inputs. The named
results and direct links above are mathematical references; none is
represented as a full matching theorem for Y or as a Mathlib theorem.
No library absence or certified originality is asserted.
