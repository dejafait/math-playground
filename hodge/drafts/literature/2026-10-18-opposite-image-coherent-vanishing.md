# Opposite-image coherent vanishing — source comparison complete

TARGET: Determine whether a published coherent-cohomology vanishing theorem forces H^1(Z,O_Z)=0 for L118's actual opposite image under L120/L121/L129's hypotheses.
CHECKED: 2026-10-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Compared L118/L120/L121/L129 and saved compact-trianalytic, point-separation and normalization-quotient assessments; checked ATTEMPTS/070--072; searched trianalytic structure-sheaf cohomology, hypercomplex H^1, coherent normalization cohomology, irregularity, rational singularities and Du Bois vanishing. No matching untwisted vanishing theorem was identified in the inspected sources.
SOURCE_EVIDENCE: Verbitsky alg-geom/9703016v1, Proposition 6.1/Theorem 6.2 and complete proofs, printed pp. 26--27; Kollár--Kovács, JAMS 23 (2010), Corollary 1.1, Theorems 1.5--1.6 and Remark 1.11, pp. 791--794, statements; Kovács--Schwede--Smith, doi:10.1016/j.aim.2010.01.020, Corollary 6.6 and complete proof, author-proof PDF p. 21, with Theorems 6.2--6.3 statements, pp. 18--19; Stacks Definition 54.8.3 (0B4N). Reuse earlier inspected compact-Douady proof cases.
COMPARISON: Hypercomplex desingularization concerns the normalization; rational-singularity coverage assumes normality; Du Bois cohomology surjectivity does not assert vanishing; the nonnormal Kodaira theorem requires Cohen--Macaulay weakly semi-log-canonical singularities and an ample inverse twist. None supplies H^1(Z,O_Z)=0 at the actual image's retained hypotheses.
GAP: Original-image normality, the required singularity conditions and H^1(Z,C)=0 are unavailable; no inspected theorem transfers B's q=0 to O_Z. No untwisted positivity hypothesis or compact smooth extension of the actual ambient metric is supplied.
REASON: Park automatic coherent vanishing: these are specific hypothesis/conclusion mismatches, not a counterexample for the full F setting. No independently testable repair within the vanishing-only mechanism was identified; a distinct smooth diagonal-restriction prerequisite is proposed for separate review.
SCOPE: Only the exact TARGET; do not assume normality, rational singularities, global injectivity or a compact smooth hyperkahler ambient moduli space.
LITERATURE_REASON: The saved REVIEW_REQUIRED target changes from local normalization defects to global coherent vanishing; original-image and singular-vanishing theorem coverage was essential and unread.

## Completed comparison — 2026-10-18, step 392

This is one literature-only NEGATIVE result about the proposed inference.
It establishes neither vanishing nor nonvanishing for the actual image.
EXPLORE records the bounded search without an adequate match, not approval
to assert the missing vanishing. No theorem is applied to derive a new
mathematical result, and no originality claim is made. Universal primitive
Hodge realization and F existence remain unresolved.

### Primary statements and applicability

[Verbitsky, *Hypercomplex varieties*, alg-geom/9703016v1,
12 March 1997](https://arxiv.org/pdf/alg-geom/9703016v1#page=26),
Proposition 6.1 and Theorem 6.2, printed pp. 26--27: a hypercomplex
variety with an integrable induced complex structure has a smooth
normalization, compatible with its hypercomplex structure and independent
of that induced structure. The complete proof separates local smooth
components and glues structures on their disjoint union. It does not
identify the original structure sheaf with its normalization pushforward
or state coherent-cohomology vanishing. Even granting intrinsic
hypercomplex applicability to Z would not supply this target. Reuse the
point-separation assessment's inspection of the same theorem;
normalization is already supplied conditionally by L120.

[Kollár--Kovács, *Log canonical singularities are Du Bois*,
J. Amer. Math. Soc. **23** (2010), 791--813](https://sites.math.washington.edu/~kovacs/current/papers/Kollar_Kovacs__Log_canonical_singularities_are_Du_Bois.pdf),
Corollary 1.1, p. 791, gives surjectivity from complex singular
cohomology to coherent cohomology for a proper finite-type complex
scheme admitting the stated log-canonical pair. This is not vanishing;
H^1(Z,C)=0 and the pair hypothesis are not established. Theorem 1.5,
p. 792, assumes a proper surjective map with connected fibres between
normal varieties, an effective log-canonical boundary and relative
Q-triviality of its log canonical divisor. Normality is missing,
and a fibre with distinct collision points is not connected. Theorem
1.6 instead requires a left inverse of its specific derived ideal map;
none is available. Remark 1.11, p. 794, records DB implies seminormal.
These statements were inspected; their MMP/derived proofs were not
audited or imported. No DB assertion is made about Z.

[Kovács--Schwede--Smith, *The canonical sheaf of Du Bois
singularities*, Advances in Mathematics **224** (2010), 1618--1640,
doi:10.1016/j.aim.2010.01.020](https://sites.math.washington.edu/~kovacs/current/papers/Kovacs_Schwede_Smith__The_canonical_sheaf_of_Du_Bois_singularities.pdf#page=21),
Corollary 6.6, author-proof PDF p. 21: for a projective Cohen--Macaulay
weakly semi-log-canonical pair and an ample line bundle A,
H^i(X,A^{-1})=0 for i<dim X. The full short proof passes through a
DB cyclic cover, Theorem 6.2's surjections, and Theorem 6.3's
negative-twist Serre vanishing. Those two input statements, PDF
pp. 18--19, were inspected; their complete proofs and the preceding
singularity criterion were not audited. The singularity conditions on
Z are unproved. More decisively, the conclusion has an inverse ample
twist; O_Z is not such a twist on a projective surface. Extension to
nonnormal varieties does not remove that distinction. No replacement
by a limit of twists is justified here.

[Stacks Definition 54.8.3, tag 0B4N](https://stacks.math.columbia.edu/tag/0B4N)
starts with a local **normal** Nagata domain of dimension two. Its
rational-singularity H^1 condition concerns normal modifications of its
affine spectrum. It neither establishes normality of this image nor
states the requested global H^1 vanishing. The definition was read;
no resolution argument is invoked.

The saved [compact-trianalytic comparison](2026-10-17-equality-opposite-compact-trianalytic-deformations.md)
already inspected the compact-Douady proof cases and noncompact volume
replacement. Reuse that adequate coverage: the former requires compact
ambient geometry and controls a deformation space; the latter supplies
a trianalyticity criterion. Neither recorded statement is untwisted
coherent vanishing on this image. A sheaf compactification is not a
compact extension of the actual L2 metric. No repeat of that blocked
compactification route is proposed.

### Duplicates, search limits and decision

The exact conditional statements were read in L118/L120/L121/L129.
The [normalization-quotient comparison](2026-10-17-opposite-image-normalization-quotient.md)
already distinguishes weak normality from smooth normalization.
ATTEMPTS/070--072 are preserved; none computes this global cohomology
or proves separation. No duplicate completed exact vanishing review
was found in these relevant records. L129 bounds local length without
a global vanishing theorem. No normalization exact-sequence calculation
is performed in this literature turn.

Queries included `Verbitsky trianalytic subvarieties desingularization
normalization cohomology structure sheaf`, `trianalytic H^1 structure
sheaf non normal hyperkahler`, `"trianalytic" "cohomology" "structure
sheaf"`, `"hypercomplex varieties" "H^1"`, `"coherent cohomology"
"normalization" singular exact sequence irregularity`, `"Du Bois"
"H^1" "seminormal" projective`, `"trianalytic" "irregularity"`, and
`Kovacs Rational log canonical Du Bois singularities II Kodaira vanishing`.
Snippets and secondary discussions were discovery leads only. Kovács's
2000 paper was located but not read in full; the later KSS theorem above
supplies the inspected broader nonnormal statement. No exhaustive
literature or novelty claim follows from unsuccessful searches. Full
matching Mathlib coverage is **not checked**. A shell PDF download
failed DNS; browser access supplied the essential sources, so no
essential source blocker remains.

The continuation threshold is not met. Park the vanishing-only route;
reopen only for a precise new theorem with actual hypotheses. Smooth
normalization, pairwise gluing, untwisted Kodaira vanishing or another
compact-Douady citation does not suffice. This is not a theorem that
vanishing is false for F. A separately proposed smooth diagonal
restriction test avoids image singularities and requires its own review
before any calculation.

## Original proposal retained; superseded by the comparison above

The main gap remains universal primitive rational Hodge realization.
Audited L129 supplies conditional local bounds but no global numerical
obstruction. The proposed new intermediate target is the exact vanishing
H^1(Z,O_Z)=0, for the original reduced image Z, not its smooth
normalization B. Its plausible use is a future global comparison of the
normalization quotient and coherent cohomology. That comparison has not
been derived in this audit step, and the vanishing is not asserted.

Retain the actual opposite map of L118, the finite normalization of L120,
the finite reduced off-diagonal coincidence scheme of L121 and audited
L128/L129's local model and bound. F is still hypothetical: locally free
rank two, Omega-polystable, integral c_1=0 and
ch_2=-14e_1-21e_2-tau_D on the identical marked projective K3 factors.
Retain the common quaternionic structures, positive scale 2lambda and
ambient quaternionic dimension 39. The source is the whole projective
K3 B. The ambient stable moduli space supplies a common smooth
hyperkahler germ near each image point; a compact smooth ambient
hyperkahler manifold is not an established premise. The original image
may be nonnormal, and no collision is asserted to exist.

The next review should first inspect primary statements about coherent
cohomology of compact trianalytic images or their normalizations and
compare their actual hypotheses with this setup. Distinguish a theorem
about the normalization from a theorem about Z itself. Ordinary
normality or rational-singularity hypotheses cannot be supplied by
assuming the desired separation. Check local duplicates in the relevant
image/normalization and failed-route records before broader searching;
reuse existing coverage where it matches, but do not reopen the already
refuted minimal-defect inference in ATTEMPTS/070. ATTEMPTS/071--072 are
separate curvature stops, not global vanishing results.

Continuation test: approve a later mathematical application only if an
inspected primary theorem could yield the exact H^1-vanishing with
verified or independently testable missing hypotheses. If every relevant
result requires unproved normality, rational singularities or an
unavailable compact ambient metric, record that specific gap and park
the vanishing-only mechanism instead of repeating local-defect audits.
This review may fail; it need not create a lemma. No source access
blocker is currently known, and novelty and Mathlib coverage are unchecked.

At proposal time this assessment was REVIEW_REQUIRED. The comparison
above completes that review with a parked route and no same-turn
mathematical application.
