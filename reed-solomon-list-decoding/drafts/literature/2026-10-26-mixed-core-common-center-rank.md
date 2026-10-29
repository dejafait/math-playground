# Mixed-core common-center interpolation — completed source comparison

TARGET: Compare known common-center interpolation-rank criteria for mixed two-core support collections in L130's setting, and identify one bounded obstruction test not implied by its pair-intersection conditions.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the 2026-10-05 RS-support, 2026-10-07 four-support, 2026-10-10 embedded-common-center and 2026-10-11 affine-translation assessments; scoped searches and readings compared L020/L030/L031/L049/L050/L130 and ATTEMPTS/031–032,103–106. Six narrow external queries found no inspected theorem deciding the proposed mixed embedding; exact queries and exclusions appear below.
SOURCE_EVIDENCE: Alrabiah–Guruswami–Li arXiv:2304.09445v3, Definition 2.5 and Lemma 2.7 including its complete proof, printed pp. 7–8, and Theorem 2.9/Remark 2.10, p. 9; Shangguan–Tamo arXiv:1911.01502v1, Definition 4.1, Lemma 4.3's common-root proof case, pp. 10–12, and Section 5's characteristic-two restriction, pp. 12–14. Reused the recorded BGM v4 comparison; L031's full criterion, two examples and audit qualifications were read locally.
COMPARISON: The signed matrix method is applicable as a necessary common-center constraint; generic/random rank theorems do not certify the fixed subgroup. L031 already certifies a nonrealizable consecutive-pair four-support pattern on a 60-core, with pair intersections 62. Its membership in two L130 ambient families is an unproved embedding obligation, not a new rank theorem or a consequence of L130's retention bounds.
GAP: Test one explicit two-left/two-right embedding of L031, including both distinguished-label conditions and full bijection completion. Even success leaves survival under L130's deletion, occurrence in arbitrary large retained families, quantitative caps and RS safety open.
REASON: Reusing the audited four-support obstruction gives a bounded common-center test beyond retention-to-overlap forcing and the stopped single-core cap tests, without reproving an existing interpolation criterion.
SCOPE: Source comparison only for E=F_65537, F=F_(65537^28), length 1024, dimension 64 and every tuple width m>=1. No new embedding, rank, lemma, mathematical script or RS realization is established.

LITERATURE_REASON: The invocation-start target was REVIEW_REQUIRED: the applicability of the existing common-center criteria to mixed two-core collections had not been compared. This completes that missing comparison and reuses ready theorem coverage instead of reopening generic-domain research.

## Main gap and selected intermediate target

The main gap is arbitrary-center 67/68 agreement safety, with the bracket
955–957 unchanged. The intermediate target is to test whether the existing
L031 consecutive-pair obstruction can be embedded as two supports from
each of L130's ambient families. L031 already distinguishes this pattern
from mere pairwise packing; the proposed embedding is not proved here.
If successful, it would show a specific common-center restriction inside
the mixed ambient model. Occurrence in large retained families and a
quantitative cap would still be independent gaps.

## Primary statements and exact applicability

Omar Alrabiah, Venkatesan Guruswami and Ray Li, *Randomly punctured
Reed–Solomon codes achieve list-decoding capacity over linear-sized
fields*, [arXiv:2304.09445v3](https://arxiv.org/pdf/2304.09445v3),
26 July 2023, Definition 2.5 and Lemma 2.7 with proof, printed pp. 7–8,
give signed equality rows and a kernel from message differences. Their
Theorem 2.9 and Remark 2.10, p. 9, give symbolic rank over a rational
function field; Lemma 3.1, p. 10, samples distinct evaluations randomly.
Neither certifies this prescribed subgroup. Selected supports, tuple
rows and arbitrary ambient-field coefficients require specialization;
L031 already supplies it for the proposed pattern. No generic-rank
theorem needs a reproof.

Chong Shangguan and Itzhak Tamo, *Combinatorial list-decoding of
Reed–Solomon codes beyond the Johnson radius*,
[arXiv:1911.01502v1](https://arxiv.org/pdf/1911.01502v1),
header 4 November 2019, Definition 4.1 and Lemma 4.3, printed pp. 10–12,
include the common-root removal proof case. Section 5, pp. 12–14,
assumes characteristic two for its unsigned matrices. Reuse L031's
signed specialization in characteristic 65537.

The BGM v4 comparison is reused from
`2026-09-26-current-target.md`, “New primary readings”: Brakensiek,
Gopi and Makam, [arXiv:2206.05256v4](https://arxiv.org/html/2206.05256v4),
28 August 2024, Theorem 1.13, Corollary 1.15 and Proposition 4.5.
The criterion and generic/random-domain guarantees do not decide fixed
subgroup ranks. This unchanged qualification was not researched again.

The strongest applicable local input is L031: six disjoint pair-only
two-sets, a disjoint 60-core, and four disjoint private two-sets yield
four 68-supports. Its consecutive-power example is nonrealizable for
all m>=1 over the pinned F; its antipodal example is realizable. This
preserves the rank-degeneracy warning and prevents universal incidence
exclusion. Import this audited example; do not manufacture another rank
lemma. It does not yet identify these supports as members of L130's
two ambient families.

## Duplicates, failures and source limits

L020's triple pattern is already avoided by L030, before actual-label
determinants are considered. Repeating that exclusion supplies nothing.
L049's translated five-graph exclusions hold at one specified labeling;
L050 and ATTEMPTS/031–032 show that the corresponding single-core cap
mechanisms leave too many blocks. They do not ban a new mixed embedding.
L130 and ATTEMPTS/106 close retention-only overlap forcing under their
stated hypotheses, without common-center compatibility. The earlier
full-law/full-star and selected-family budget stops in ATTEMPTS/103–105
are retained as scope limits, not general prohibitions.

External queries on 2026-10-26:

- `"Reed Solomon" "mixed" "agreement" "intersection matrix"`
- `Alrabiah Guruswami Li reduced intersection matrix Lemma 2.7 2304.09445`
- `"Reed Solomon" "agreement hypergraph" prescribed evaluation points`
- `"Reed Solomon" "two cores" interpolation`
- `"Reed Solomon" "common center" "four" "supports"`
- `"Reed Solomon" "agreement supports" "multiplicative subgroup" rank`

Search hits on hardware cores were irrelevant. Folded/multiplicity codes
were not imported. ECCC search listings mentioned 2026 prime-field
capacity results, and a 2026 survey appeared as a search hit; their
theorems were not inspected or used. They are unread leads, not coverage
for arbitrary interleaving over the pinned extension field. No novelty
or exhaustive-search claim follows. The pinned model's missing July ABF
comparison remains a qualification; no blocked source is retried here.

## Bounded continuation and stopping decision

The exact mathematical continuation is scoped in
`2026-10-26-mixed-core-l031-embedding.md`. It tests only one prescribed
embedding, importing L031's already certified obstruction. Continue only
after exhibiting both label maps, all four support memberships and the
distinguished-point conditions; reject the prescribed construction if
these finite constraints conflict. A failed construction is not an
impossibility theorem for other embeddings. No survival, universal
occurrence or threshold consequence is licensed by the finite test.

Essential inputs are L030, L031, L130 and the pinned instance/model;
L020/L049/L050 are comparisons. Full and supporting Mathlib coverage
for the proposed embedding is not checked. No cross-notebook input,
mathematical artifact or PROOF/DAG change is made. This is completed
source review with a concrete later test, not a mathematical advance.
The newly written continuation requires separate supervisor approval.
