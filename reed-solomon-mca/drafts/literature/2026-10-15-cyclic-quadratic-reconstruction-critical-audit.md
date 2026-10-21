# L092 quadratic reconstruction audit — source-scope comparison

TARGET: Critically audit L092's seven-seed quadratic reconstruction, including its pole exclusions, genuine quadratic degree and at-most-two continuation bound.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read full L092, relevant L089/L090/L091 definitions and audited input statements, history/229 and ATTEMPTS/032–034; reused ready fixed-H and involution assessments; searched projective cross-ratio invariance, polynomial root bounds and exact cyclic seven-seed RS terminology on October 16.
SOURCE_EVIDENCE: Bobenko, Projective Geometry, draft December 12, 2019, Definition 2.19, Remark 2.20, homogeneous/affine/infinity cases, Lemma 2.21 with proof and Corollary 2.22 (printed pp. 21–22); Milne, Fields and Galois Theory v5.10 (September 2022), Sections 1.6–1.7 with argument (printed p. 10); reused Nguyen (2021), Section 2 and Proposition 1, through the ready L090 comparison.
COMPARISON: Known projective invariance and polynomial root counting cover the general machinery over F_97 and its extension; no inspected source gives the coupled cyclic D_15/S_8 specialization, its everywhere nonzero quadratic coefficient or the seven-seed completion table. These remain separate local audit obligations.
GAP: L092's at-most-two claim remains unaudited; uniform rank R>=3, rank-27 existence, arbitrary-family coverage and challenge qualifications remain unresolved. No inspected source supplies an exact cyclic theorem that can replace this audit.
REASON: The exact claims and essential primary machinery have now been compared; no essential unread source or artifact obligation remains. Proceed to the saved proof audit, with no new gates or elimination and no correctness verdict this turn.
SCOPE: Entire saved L092 at fixed F_(97^20), fixed order-sixteen H in F_97^*, arbitrary bijection and hypothetical nonzero full alternating kernel; normalization, two initial deductions, coupled quadratic and five final deductions only.
LITERATURE_REASON: The saved Next action was REVIEW_REQUIRED; its coupled two-label step and projective normalization exceeded the already assessed single-label audit. This separate comparison supplies the missing source scope.

## Original proposal — step 242, historical

The proposal below records the pre-review scope. The completed decision
above and comparison below govern continuation.

The next invocation is a literature-only comparison for exactly TARGET.
Read full L092 to determine its exact hypotheses, proof cases and any
artifact obligations, then reuse the ready L089/L090/L091 source
comparisons where applicable. Retrieve additional primary evidence only
for an essential uncovered point. This proposal is not an assessment
that the needed quadratic or branch claims are correct.

Essential inputs are L089, L090 and L091 with their audited unshifted
moment and finite-label conventions; retain L010/L087/L088 only through
those inputs. The recorded seed set is (0, 1, 2, 3, 5, 7, 9), whose D_1/D_10
closure adds 10,14. L092 proposes coupling D_15 and S_8 for the two
remaining labels and reconstructing the final five. Do not assume a
rank-27 labeling exists, gates are sufficient, or any L093–L096 result.
Projective normalization must not be treated as a symmetry of H.

The main gap is still uniform cyclic rank. The intermediate target is
trustworthiness of this bounded reconstruction input; downstream use is
a justified finite parametrization for any later independently approved
rank investigation. The audit acceptance test will require every
normalization and inverse-projectivity gate, all finite poles,
nonzero leading coefficient, repeated-root/degree cases and remaining
unique deductions. A defect narrows or rejects the affected claim;
passing establishes only the conditional bound, not existence or
uniform exclusion. Confirm the actual statement from L092 before
approving that test.

ATTEMPTS/032 remains the verified stop for single-label propagation;
ATTEMPTS/033–034 stop different joint-elimination attempts. A critical
audit of the saved quadratic result does not restart those routes.
No source blocker or budget reset is inferred, and full matching
Mathlib coverage is not checked. The next source review must set an
honest decision based on inspected material before dependent work.

## Completed source comparison — October 16, 2026, step 243

This is one literature-only comparison of exactly TARGET. Reading L092
identifies its assertions and exceptional cases; it does not audit its
algebra, derive a result, enumerate labels or run a mathematical script.
No canonical lemma, DAG edge or argument overview is changed.

### Relevance, exact input scope and reuse

The main local gap is uniform rank R>=3 (rank M=28) for the cyclic
family; rank-27 existence is also undecided. The intermediate target is
trust in the saved conditional at-most-two reconstruction. Its plausible
downstream use is a justified bounded parametrization for a separately
assessed rank investigation. Passing this audit would not itself settle
uniform rank, arbitrary equality families, the uniform triangle twelve
bound or the challenge's uncertified definition/parameter qualifications.

Full L092 was read. Its stronger gate-only conclusion concerns precisely
D_1,D_10,D_15,S_8,D_8,D_3,D_2,D_0,D_4; nonzero K supplies necessity
through L089–L091. Its seed set is {0,1,2,3,5,7,9}. The proof claims two
initial deductions, one two-label quadratic and five unique deductions.
It declares no numerical certificate or script essential. The original
H is fixed, the bijection arbitrary, and no actual errors, original
finite chart, weights, locators or L093–L096 conclusion are assumed.

Reuse the ready comparisons in
`2026-10-14-cyclic-family-alternating-kernel.md`,
`2026-10-15-cyclic-six-label-critical-audit.md` and
`2026-10-15-cyclic-remaining-gates-critical-audit.md` for their unchanged
inputs. Relevant definitions and audited statements in L089/L090/L091
were inspected to locate the exact unshifted convention and finite-label
scope. L010/L087/L088 enter only through those inputs. The old generic
evaluation theorems do not become fixed-H theorems in this audit.
Nguyen's *Projective Line Revisited*, J. Geometry and Graphics 25(2)
(2021), Section 2, pp. 188–189, and Proposition 1, p. 191, already cover
the characteristic-not-two involution, affine and inversion cases; reuse
the primary URL and inspected proof cases recorded in the L090 review.
No repeat retrieval or new involution theorem is required.

### Newly inspected primary comparisons

Queries issued October 16, 2026:

- `projective line cross ratio invariant projective transformation university notes theorem`
- `"Reed Solomon" "seven" "quadratic" reconstruction involution`
- `site.math.uconn.edu kconrad polynomial roots degree field`
- `"Reed-Solomon" "seven-seed"`
- `"cyclic" "D_15" "S_8" reconstruction`

The exact cyclic queries produced no inspected matching theorem; this
does not establish novelty. Search snippets and unrelated results were
screening only. Conrad's *Roots and Irreducibles* was an unread lead;
its extension-existence results are unnecessary here.

Alexander I. Bobenko, [*Projective Geometry*](https://page.math.tu-berlin.de/~bobenko/Lehre/Skripte/projective_part.pdf),
draft December 12, 2019, written by Thilo Rörig from the Geometry I
course and Boris Springborn's notes, author-hosted 84-page PDF.
Read Definition 2.19 and Remark 2.20 (printed p. 21), the representative,
affine and infinity cases, Lemma 2.21 with complete determinant proof
and Corollary 2.22 (p. 22). Remark 2.20 explicitly allows any field.
The homogeneous formulation covers distinct projective points, including
infinity, under an invertible linear map. Thus F_97 fits; no order,
topology or characteristic-zero assumption is needed. The displayed
limit language in the affine example is not needed: use homogeneous
coordinates. This covers general invariance, not L092's choice of
cross-ratio factors or transformed-H restrictions. Later geometric
propositions and involution exercises are unused.

J. S. Milne, [*Fields and Galois Theory*](https://www.jmilne.org/math/CourseNotes/FT.pdf),
v5.10, September 2022, author-hosted 144-page PDF. Read Sections
1.6–1.7 (printed p. 10), including the division/factor argument:
a nonconstant polynomial over a field has at most its degree many
distinct roots. This applies to F_97 and F_(97^20), without separability
or a square-discriminant hypothesis. It does not establish that L092's
cleared polynomial has degree two or excludes its denominator pole;
those are the local claims to audit. No reproof of root counting is
needed. Other Galois-theoretic results are unused.

The standard inputs can be cited precisely in the later canonical audit.
Direct checking of the saved coordinate formulas is warranted by their
particular cyclic indices, coefficient convention and branch claims;
it is not a reason to reprove general projective invariance. Full
matching Mathlib coverage remains not checked, not absent. No supporting
formal theorem is needed as an additional input for this informal audit.

### Duplicates, failure evidence and acceptance test

The targeted local search found the original step-229 derivation but no
completed separate L092 audit. L090 certifies the unique one-label
involution recovery; L091 certifies the S gate and its specified closure
limit. Neither checks the simultaneous quadratic. L095 changes the
seven seeds and is not an input or a duplicate proof of the original
seed-set bound. The supplied overview suffices to distinguish that scope;
its detailed proof need not be loaded for this target.

ATTEMPTS/032 stops the stated single-label propagation only.
ATTEMPTS/033 preserves an incomplete symbolic expansion, and
ATTEMPTS/034 stops the direct joint-gate elimination after no forbidden
factor was obtained. Their complete short records were read. This audit
does not restart those calculations, infer a global ban, enlarge an
expansion, sample ranks or sweep H-labelings. Preserve their evidence
and the earlier rank-sampling stop ATTEMPTS/020.

Continue with exactly TARGET. Check the D/S substitutions against the
audited input notation, the two initial D deductions and rejection gates.
Check normalization as an invertible projectivity, conjugation of the
involution and each cross-ratio factor, including b at infinity. Keep
T(H), inverse-projectivity poles and distinctness rather than assume a
subgroup symmetry. Check the claimed fractional-linear map's finite
pole, invertibility and nonzero numerator there, and the affine map's
nonzero slope. Check the cleared Q coefficient for every admitted seed
assignment, without relying on a generic nonvanishing assertion; retain
zero intercept, repeated roots, nonsplit roots and every inadmissible
label. Check the exact two-equation correspondence and exclusion of
the denominator root. Finally check all five continuation rows, their
previously known indices and unique recovery with every rejection gate.

Passing establishes only the saved necessary at-most-two bound. A failed
identity, omitted branch or unsupported uniqueness claim must narrow or
reject the affected statement and be recorded precisely. No existence,
sufficiency, new gate, stronger seed bound or uniform rank conclusion
is approved. This SPECIALIZE decision licenses a later REPRODUCTION
proof audit; it is not that audit. Outcome EXPLORATION reflects new
source comparison and a concrete ready test, with zero mathematical
exploration turns spent and no claimed advance beyond checked sources.
