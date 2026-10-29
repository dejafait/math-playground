# Split KS and extended tangent comparison — source coverage ready

TARGET: Compare L170's actual KS plane with the derived image of L108/L116's extended tangent summand at a reduced split point.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 568 compared targeted L108/L111/L116/L164/L170 passages, saved extension and actual-map assessments, histories 564–567 and ATTEMPTS/092–094; searched family KS, Atiyah pullback, relative Ext, reflexive extension and nonsimple base change, with exact queries below. No inspected source directly identifies these particular split-point maps; no novelty claim.
SOURCE_EVIDENCE: Inspected Huybrechts–Lehn E31 (1997), 10.1.5/7/8 and Example 10.1.9, pp. 218–221; Kuhn, Forum Math. Sigma 12 (2024), e100, Lemma 4.4/Claim 4.5 and Corollaries 4.6–4.7, pp. 32–35, and Lemmas 6.11–6.12 with proof, pp. 50–51; live Stacks 0EBJ, 0B91, 064B and 08J5 statements/proof scope. Reuse L164's inspected cup/base-change coverage.
COMPARISON: The all-family Atiyah/KS construction and its derived pullback compatibility cover nonsimple split fibres without stability or an ordinary middle-base-change isomorphism. Reflexive full faithfulness and local projective chain maps cover the remaining comparison tools, but none of these sources certifies the family-specific equality with L108's i or L164's e_z directly.
GAP: A later mathematical attempt must compare the trace-free family Atiyah morphism, its degree-one sheaf map, L108's specific extension, and the actual truncation j after derived restriction; retain all extra split-fibre directions and check the first-order convention. No essential source gap remains for this bounded attempt.
REASON: This separate literature-only step approves exactly TARGET for subsequent RESEARCH / REPRODUCTION specialization of known tools. It proves no equality, intersection vanishing, improved threshold or exclusion and changes no lemma or mathematical script.
SCOPE: L071/L108/L111/L116/L164/L170 conditional family, actual connection, finite reduced split support, actual i,j,e_z,kappa_z and general s,t; all-fibre Atiyah/KS naturality and local ordinary-to-derived comparison only, with no chosen new splitting or section integrability.
LITERATURE_REASON: The changed exact target was REVIEW_REQUIRED after step 567; existing stable-open/reflexive-extension and derived-base-change coverage left the all-family KS naturality scope unassessed. This turn fills that specific source gap.

## Retained target, assumptions and discriminating test

Main gap remains primitive Hodge realization and existence of F. This
intermediate target addresses the unresolved intersection in L170's
conditional section inequality. Plausible downstream use: if the maps
can be identified, test whether L116's actual direct-sum decomposition
controls the intersection of the full section image with the KS plane.
The prospective threshold is 24 under bracket vanishing, compared
with the currently justified bound 26. Neither that improvement nor
bracket vanishing is asserted; neither would alone exclude F.

Essential inputs to assess are L108's specific i:T_B -> M** and its
stable-open origin, L111's M=M** and actual fibre KS map, L116's
truncation and section decomposition, L164's e_z and evaluation, and
audited L170. Retain L071 and L094/L095/L109/L115 only as used in
those conditional inputs. No cross-notebook input. L169 is motivation
for eventual section quadrics, not a required input to this comparison.

Retain the identical marked K3 factors, fixed common metric, real
Kähler class, ordered triple, forms and actual connection. F is the
hypothetical locally free rank-two product-polystable bundle with
integral c_1=0 and ch=2-14e_1-21e_2-tau_D+62P. The finite split set
is reduced, and the question is conditional on a point z in it.
Use general s,t and the actual i,j,e_z,kappa_z; do not choose a new
splitting. No ordinary-middle-base-change isomorphism, arbitrary
section integrability, genericity, endpoint, F existence, or equality
of these tangent images is assumed. Empty support is vacuous.

Later continuation/abandonment test: after source approval, determine
whether e_z composed with i(z) equals kappa_z, or at least has the
same image, or isolate the precise obstruction to that comparison.
An equality only on the stable open is not by itself a comparison
of fibre classes in the extra derived middle space. Retain the
existing bound if this bridge fails. Stop at unknown section brackets;
do not infer vanishing from the additive splitting or tangent
integrability, and do not reopen the scalar-isotropy or cyclicity-only
routes in ATTEMPTS/092–094. Section quadrics, minimum square length,
complementary operation, transport and primitive realization remain
independent unresolved issues.

At invocation start this was a REVIEW_REQUIRED proposal. The separate
step 568 assessment below supplies source approval; it does not perform
the mathematical comparison. Full matching Mathlib coverage remains
unchecked, with no claim of absence.

## Completed source comparison — step 568

2026-10-26. LITERATURE / EXPLORATION / REPRODUCTION; actual task
literature_comparison. Ready coverage is local process progress, not a
mathematical advance beyond the sources. The argument in PROOF.md and
the DAG are unchanged.

### Primary statements, proof cases and applicability

Huybrechts–Lehn, *The Geometry of Moduli Spaces of Sheaves*, E31
(1997), [10.1.5, 10.1.7–8 and Example 10.1.9, pp. 218–221](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=230),
was reinspected in the 281-page primary book text. The relative
construction takes a flat coherent family on a smooth projective
surface over a finite-type base; it does not require stable or simple
fibres. The base component of the Atiyah class gives a sheaf map from
the base tangent sheaf to relative Ext^1. Example 10.1.9 checks its
dual-number interpretation using the first-neighbourhood extension and
an explicit pullback diagram. Here F is locally free and B is smooth;
the construction applies to the actual product family. The locally
free coefficient identifies relative self-Ext with higher direct images
of End(F). Trace-free projection and the convention matching L111 remain
specialization checks. The stable-moduli tangent isomorphism in 10.2.1,
used in L108 on U, is not an all-fibre theorem at split points.

Nikolas Kuhn, *The Atiyah class on algebraic stacks*, Forum of
Mathematics, Sigma **12** (2024), e100, 1–54,
[published primary text, DOI 10.1017/fms.2024.109](https://doi.org/10.1017/fms.2024.109),
fills the explicit naturality scope. Read Lemma 4.4/Claim 4.5 and
Corollaries 4.6–4.7, pp. 32–35, including flat representatives,
principal-parts connecting maps and K-flat cone/pullback comparison.
For a morphism of algebraic stacks and E in D^{<=0}_qcoh, the Atiyah
class commutes with derived pullback and the induced cotangent map for
a 2-commutative square; no flatness of that square is assumed. Schemes
and locally free F in degree zero meet this scope. Lemmas 6.11–6.12,
pp. 50–51, identify the contracted class with a deformation extension
for an affine T, a trivial square-zero thickening by I, and an extension
with I tensor E -> I Ebar an isomorphism. Read the proof's principal-parts
diagram and its restriction calculation. Dual numbers and a pulled-back
locally free family meet those hypotheses. All pullbacks are derived.
The HTML diagram images failed extraction; the published PDF supplied
the complete diagrams and proof cases. No essential access blocker
remains. The stronger moduli obstruction theorem 1.4 is unnecessary.

[Stacks Lemma 31.13.12, 0EBJ](https://stacks.math.columbia.edu/tag/0EBJ)
was reinspected with its full proof: for an integral locally Noetherian
scheme and an open complement whose ambient local rings have depth at
least two, restriction and pushforward give an equivalence on coherent
reflexive modules. The smooth K3 base and finite removed set satisfy
the ambient hypotheses; L111 supplies M=M**. This is coverage for a
comparison of actual sheaf maps, not uniqueness of arbitrary derived
maps from their stable-open restrictions, nor a metric extension.

[Stacks Lemma 36.30.4(1), 0B91](https://stacks.math.columbia.edu/tag/0B91)
applies to a proper flat finitely presented morphism and a perfect
coefficient, giving perfect pushforward and arbitrary derived base
change. The product projection and V satisfy these conditions. Reuse
L164's cup/adjunction compatibility coverage from
`2026-10-25-adjoint-point-bracket-critical-audit.md` and the step 566
assessment; this target changes neither coefficient nor fibre square.
No ordinary degree-one base-change isomorphism is imported.

[Stacks Lemma 13.19.8, 064B](https://stacks.math.columbia.edu/tag/064B)
identifies homotopy and derived morphisms from a bounded-above complex
of projective objects. Its statement and dual-proof reference were read;
the lemma is imported. Use it locally in the module category, where the
tangent stalk is finite free, not as a claim that vector bundles are
projective objects in the global sheaf category.
[Remark 13.12.4, 08J5](https://stacks.math.columbia.edu/tag/08J5)
and its short-exact-sequence/quasi-isomorphism construction give the
canonical truncation triangle. These tools cover checking the local
lift against the actual j. They do not themselves perform that check.

### Searches, duplicates and limitations

Queries on 2026-10-26: `"Kodaira-Spencer" "Atiyah class" "base change"
vector bundles families relative Ext`; `"Kodaira-Spencer" "R^1" "End"
family vector bundle morphism tangent`; `Huybrechts Lehn Kodaira Spencer
family Atiyah class 10.1.8 10.2.1`; `Nikolas Kuhn Atiyah class on algebraic
stacks arxiv 4.7 6.12`; `"Kodaira-Spencer" "reflexive" "Ext" extension
base change`; `"Kodaira-Spencer map" "base change" "sheaves" Atiyah
non-simple`. Broader hits on deformation obstructions and derived KS
were discovery leads only; they supply no theorem input. The inspected
general constructions are stronger than a stable-only comparison in
their hypotheses, but do not state the exact conditional-family result.
The bounded search does not establish novelty.

L108 already identifies the stable-open sheaf map and its unique
reflexive extension. L111 identifies the actual split KS classes through
first-order connecting maps; L164 identifies e_z using the actual j.
L170 expressly leaves their comparison unproved. Thus recomputing its
radical is a duplicate, whereas the present comparison has an identified
missing compatibility. ATTEMPTS/092–094 retain unknown section brackets,+nunrestricted complementary lifts and the unevaluated global operation.
None is reopened by source approval. Derived concentration, simplicity
at z, formality, multiplicative splitting and arbitrary section
integrability are not covered conclusions.

### Approved mathematical boundary

The subsequent attempt should import these standard constructions and
check only their actual-family specialization. In particular it must
retain the distinction between a degree-one sheaf map and its derived
lift, justify the trace-free projection, compare with the specific i on
U before using extension, and verify compatibility with the actual j
and first-order kappa_z after restriction. Equality on U alone is not
the required derived-fibre argument. A common nonzero convention scalar
must be stated if only equality of images is justified. Do not discard
the two extra middle directions or choose a new splitting to force the
answer. No reproof of the imported general theorems is needed.

Continue if that bounded comparison identifies the maps/images; if a
compatibility fails, record the exact missing statement and retain 26.
No map equality, section-intersection conclusion or 24 threshold is
derived in this source review. Actual section quadrics and their
brackets, square length, complementary operation, F existence,
transport and primitive realization remain unresolved independently.
