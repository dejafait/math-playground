# Direct summands and first-order union recovery — literature assessment

TARGET: Determine whether first-order obstruction functoriality recovers a sheaf lift of I_C from any lift of I_C(-mH) direct sum O_X(-nH) for m,n>0, and thereby removes the degree ordering in L018's union recovery.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched direct-summand and Atiyah obstruction lifting, nilpotent-base Tor amplitude, and relative basic double linkage; read the corrected Huybrechts--Thomas criterion, its universal construction, Buchweitz--Flenner naturality, and the Stacks statements below. Reused the earlier liaison comparison.
SOURCE_EVIDENCE: Huybrechts--Thomas, arXiv:0805.3527v2 (15 September 2013), Definition 2.6, Theorem 2.10, equation (3.6) and Corollary 3.4, pp. 7, 9, 12, 14, https://arxiv.org/pdf/0805.3527v2#page=14; Buchweitz--Flenner (2003), Corollary 3.13, p. 162; Stacks Lemmas 15.80.4 (07LU), 15.68.20 (0H75) and 15.68.3 (0654), https://stacks.math.columbia.edu/tag/0H75; full links and the erratum below.
COMPARISON: The inspected theory supplies a natural obstruction to existence of a perfect lift and the nilpotent-base criteria needed for flat sheaf lifts; lifting a specified quotient is a separate problem. The direct-summand mechanism is standard, but no inspected theorem states L018's all-positive-degree union recovery on this singular support.
GAP: Give only the explicit direct-summand applicability argument and check the remaining steps of L018 for arbitrary positive m,n, including perfectness of the given flat lift, base-relative flatness of the recovered sheaf, and ideal reconstruction. No revised union statement is established in this review.
REASON: Known functoriality makes a concrete alternative to the chosen-inclusion vanishing available. Import that theory and specialize its use in L018 before further classifying L.F>=4; a new obstruction theory or a reproof of the cited general results is unnecessary.

## Hypotheses

Retain the same NS-fixed first-order deformation X_A=S_A x_A S_A,
with A=C[epsilon]/(epsilon^2), and H_A extending H. The sheaf whose
existence is at issue is an A-flat coherent lift of the central direct sum
I_C(-mH) direct sum O_X(-nH). Its decomposition and either central
inclusion need not lift inside the given sheaf. The question is whether
some flat coherent lift of I_C must nevertheless exist.

For the downstream comparison, retain L018's admissible f,g and smooth
complete-intersection B, with Y=C union B and m,n>0. L019 already
supplies its support-cohomology vanishing for positive n. The ideal
remains singular at the three double points; a vector-bundle lifting
criterion alone would be insufficient. Reuse the unchanged rational
Hodge target and primary-source audit, most recently read in the
[support-cohomology assessment](2026-09-27-positive-degree-normalization-cohomology.md).

L020's nonzero group in fibre degree two and L021's all-positive-degree
vanishing in fibre degree three remain valid local calculations.
The range L.F>=4 remains uncomputed. Resolving that range is not a
prerequisite for testing whether this sufficient vanishing condition
is needed at all for existence of a recovered ideal lift.

## Conclusion

The source assessment is complete: SPECIALIZE. The closest known result
is the natural perfect-complex obstruction criterion, supplemented by
nilpotent-base perfectness and Tor-amplitude theorems. These are inputs
to import by citation. The remaining task is their explicit application
to the split central sheaf and the existing union-recovery argument;
the full geometric statement was not found as a cited theorem.

The source comparison supports testing existence of some summand lift
without requiring a chosen inclusion in the given middle-sheaf lift.
It does not identify that given lift with a direct sum. The exact saved
TARGET is retained for a separate research turn. No new obstruction
identity, sheaf lift, degree-independent recovery theorem, or larger
union-lifting kernel is proved here.

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION, using one
exploration turn since L021. No general theorem has been reproduced,
and no result beyond the checked literature is claimed. A future proof
must distinguish its citation-based input from the local applicability
check; failure to locate the full statement is not evidence of novelty.

## Proof

This section records source evidence and comparisons, not a new proof
of the proposed recovery statement.

### The corrected obstruction criterion and naturality

Read Huybrechts--Thomas, *Deformation-obstruction theory for complexes
via Atiyah and Kodaira--Spencer classes*,
[arXiv:0805.3527v2, introductory theorem, pp. 1--2, and Corollary 3.4, p. 14](https://arxiv.org/pdf/0805.3527v2#page=14).
For a perfect complex P on a separated noetherian scheme X and a
square-zero thickening X' embeddable in a smooth ambient scheme,
the class (id_P tensor kappa) composed with A(P) vanishes exactly when
a perfect lift with derived restriction P exists. Simplicity and a
lifted filtration are not hypotheses.

Also read [Definition 2.6, p. 7, Theorem 2.10, p. 9, and equation (3.6), p. 12](https://arxiv.org/pdf/0805.3527v2#page=7).
The Atiyah and obstruction classes are obtained by applying universal
Fourier--Mukai kernel morphisms to P. This is the algebraic naturality
input relevant to the central splitting maps. It concerns the full
Ext obstruction, rather than its trace or Chern-character image.

Reread the [2014 erratum, Math. Ann. 358, 561--563, pp. 561--562](https://link.springer.com/content/pdf/10.1007/s00208-013-0999-x.pdf#page=1).
It corrects missing relative flatness assumptions and explicitly
retains the absolute criterion over a field; v2 incorporates the repair.
The intended use is absolute over C for X contained in X_A.

The notebook supplies the ambient hypotheses: X is smooth projective,
L012 gives finite local projective dimension for I_C even at its double
points, and the ample extension H_A makes X_A projective over A and
embeddable in a smooth complex ambient scheme as in L012. Neither
local freeness of I_C nor an lci hypothesis on C is required by this
source criterion. The new applicability issue is recovery from the
central splitting, not a new ambient deformation framework.

Read Buchweitz--Flenner, *A Semiregularity Map for Modules and
Applications to Deformations*, Compositio Math. 137 (2003), 135--210,
[Corollary 3.13, p. 162, following Proposition 3.11, p. 161](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/712BFB5F73E0C38B4B32206699B0277F/S0010437X03100413a.pdf/a-semiregularity-map-for-modules-and-applications-to-deformations.pdf#page=28).
The corollary states naturality of Atiyah powers as transformations of
exact functors on the coherent derived category. This corroborates
the mechanism for complexes, not just bundles. Its setting is complex
spaces; the algebraic input selected here is Huybrechts--Thomas's
universal construction, so no unexamined analytic algebraization step
is needed. The text of Corollary 3.13 was readable; the extracted
diagram in Proposition 3.11 was incomplete and is not separate evidence.

### Perfect lifts versus flat coherent sheaves

Read the following online Stacks statements and proofs on 2026-09-27;
the stable tags identify them despite changing chapter numbers.

- [Lemma 15.80.4, tag 07LU](https://stacks.math.columbia.edu/tag/07LU):
  perfectness of a derived reduction modulo a nilpotent ideal implies
  perfectness of the original complex. This addresses entry into the
  perfect-complex criterion from a given flat coherent lift.
- [Lemma 15.68.20, tag 0H75](https://stacks.math.columbia.edu/tag/0H75):
  derived reduction along a nilpotent surjection preserves and detects
  any specified Tor-amplitude interval. For the flat-sheaf comparison
  the relevant base is A -> C, and the interval is [0,0]. It is not
  an assertion that the singular ideal is locally free on X.
- [Lemma 15.68.3, tag 0654](https://stacks.math.columbia.edu/tag/0654):
  Tor amplitude in [a,b] is equivalent to a representative by flat
  modules in those degrees. This supplies the concentration and
  flatness input at [0,0]; coherence is retained from perfectness on
  the noetherian thickening.

The later applicability argument must keep the two rings distinct:
local perfectness concerns O_(X_A) -> O_X, whereas A-flatness concerns
A -> C. X_A is flat over A, and the lift is specified by derived
central restriction. Those are the relevant hypotheses to check,
including at C's three singular points. The sources remove the need
to invent a new concentration or flatness lemma.

### A chosen quotient remains a different lifting problem

Reread Stacks [Remark 99.7.9, tag 0CZU](https://stacks.math.columbia.edu/tag/0CZU)
and [Remark 99.7.10, tag 0CZV](https://stacks.math.columbia.edu/tag/0CZV),
in their flat-middle-sheaf setting. A specified quotient with kernel K
and quotient Q has its own obstruction in Ext^1(K,Q tensor J); if it
vanishes the quotient lifts form a Hom torsor. These are supporting
comparisons, not a theorem that a selected quotient always lifts.

This distinction is precisely what L018's equation (9) was addressing.
Its sufficient inclusion-lifting group can be nonzero without that
fact answering the existence question now under review. The known
nonzero group in L020 must therefore not be advertised as a transverse
lift, a nonzero actual inclusion obstruction, or an obstruction to
every possible recovery of an ideal sheaf.

### Comparison with the existing argument and the continuation test

Read L018 in full, L012's ideal reconstruction, L019's stated range,
the whole overview and DAG, ATTEMPTS/015, and history 029. Reuse the
[complete-intersection assessment](2026-09-27-ample-complete-intersection-union.md)
for the unchanged basic-double-linkage and fixed-ambient liaison
comparisons. That review already distinguished fixed-ambient liaison
from lifting in a prescribed deformation of X.

In L018 the strict ordering is used explicitly at equation (9), to
lift a selected line-summand inclusion. The earlier extension recovery
uses support cohomology and positive twists; the final determinant and
Hartogs reconstruction accepts an abstract flat ideal-sheaf lift.
This locates the proposed replacement in the existing proof. It does
not yet extend its quantified conclusion. L019 provides the support
vanishing for every n>0, while equality of lifting loci in L018 retains
the separate H^1(X,I_C(nH)) condition for lifting the selected f.

One bounded specialization of the unchanged target is justified:
check naturality on the central inclusion and retraction, apply the
cited perfectness/flatness criteria, and audit the extension and ideal
reconstruction for every admissible positive pair (m,n), including
m=n and m<n. Continue to an enlarged exclusion only if all these
passages hold. If one fails, identify that exact failed hypothesis
before returning to cohomology or proposing another mechanism. Do
not require the given E_A to split, and do not infer equality of
lifting loci from the forward recovery implication alone.

The downstream use is to decide whether positive ideal cohomology can
offer this representative an escape from recovery at all. This test
takes priority over the unfinished L.F>=4 classification and does not
repeat the earlier numerical tests or reopen a stopped rotation branch.
The established bound remains three allowed RM directions against four
required. The attained cycle span is still 21 on the same family;
no transverse surface or new algebraic Hodge class is supplied. Even a
successful recovery argument would exclude a representative class,
not resolve the universal rational Hodge conjecture. Higher-order
lifting and algebraization would remain necessary for a constructive
route using another representative.

### Search and access record

Queries on 2026-09-27 included:

- `"direct summand" "Atiyah class" deformation obstruction`
- `"obstruction" "direct sums" "deformation" sheaves Atiyah`
- `"Atiyah" "functorial" "Buchweitz" "Flenner"`
- `site.stacks.math.columbia.edu "complex" "flat" "nilpotent ideal" "amplitude"`
- `site.stacks.math.columbia.edu "perfect" "nilpotent ideal" "K" "surjective"`
- `"direct sum" "sheaves" "lifts" "Atiyah" obstruction`
- `"basic double linkage" "deformations" obstruction`
- `"K3" "union" "direct summand" obstruction`

Broader perfect-complex/flat-sheaf searches were refined to the stable
Stacks tags above. The essential criterion, its correction, naturality
construction, and nilpotent-base lemmas were read in primary sources.
The original Illusie, Lowen and Lieblich works cited by Huybrechts--Thomas
were not independently read; none is needed as an additional unread
premise here. Search excerpts about other liaison or K3 papers are
unassessed leads, not theorem evidence. No essential access gap remains
for the proposed specialization, and no novelty claim follows from
the search's failure to locate the full union statement.

## Mathlib

Coverage: **not checked** for the full statement or its supporting
obstruction, naturality and flatness inputs. The named primary results
above are supporting mathematical references, not a full matching
Mathlib theorem or a published statement of this union-recovery result.
No library absence or certified originality is asserted.
