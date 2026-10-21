# RS-specific agreement-support bounds — completed bounded assessment

TARGET: Assess whether known bounds for realizable Reed–Solomon agreement-support families certify B_m(956/1024)<=65537^28/2^128 on C001a's instance for every m>=1.
CHECKED: 2026-10-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched RS agreement sets/support intersections, higher-order MDS, common-center generalized Singleton bounds and multiplicative-subgroup list upper bounds; inspected deterministic intersection-matrix statements and reused the recorded generic-MDS exclusion. Queries and precise readings appear below.
SOURCE_EVIDENCE: Read Shangguan–Tamo arXiv:1911.01502v1, Definition 4.1, Lemma 4.2 and Lemma 4.3 including common-root division; read Alrabiah–Guruswami–Li TR23-125, Definition 2.5, Lemma 2.7 and its proof, Theorem 2.10, Remark 2.11 and Lemma 3.1; reused BGM v4 comparison in the 2026-09-26 assessment.
COMPARISON: Deterministic specialized rank deficiency is a necessary support constraint; inspected symbolic/random full-rank results do not certify rank on the prescribed subgroup or the required factor exceeding 2.763. No inspected theorem certifies the saved uniform threshold.
GAP: A fixed-domain rank restriction needs a quantitative extremal-family bound to improve C001b; tuple/extension applicability and sufficiency of a proposed small-configuration test still need proof.
REASON: Park direct import of generic/random list guarantees; a bounded triple-support rank diagnostic is independently testable and could supply restrictions for a later extremal bound.

LITERATURE_REASON: RS-specific realizability was outside the ready unrestricted-packing assessments; primary algebraic constraints were essential missing coverage.

## Relevance and local checks

The main gap is arbitrary-center safety at 68 or 67 agreements. The saved
source target concerns 68 agreements, potentially raising the certified
lower endpoint to 956. L001, C001a and C001b were read in full. C001a retains
the instance, C012a/L019 qualifications and bracket 955<=t_star(m)<=957.
The nested-floor failure and history/037 were read; their stop remains.
Searching local assessments, lemmas, histories and ATTEMPTS found the prior
generic-MDS comparison, but no existing triple-support rank test. This is
not evidence of novelty. Family-specific failures L016–L018 remain parked.

## Primary comparison

Omar Alrabiah, Venkatesan Guruswami and Ray Li,
[Randomly punctured Reed–Solomon codes achieve list-decoding capacity over
linear-sized fields, ECCC TR23-125](https://eccc.weizmann.ac.il/report/2023/125/download),
original 30-page report: Definition 2.5, printed pp. 6–7, constructs a
wt(E)-by-(t-1)k reduced intersection matrix for a hypergraph on t vertices.
Its rows impose equality of evaluations within each hyperedge. Lemma 2.7,
p. 7, says the specialized matrix lacks full column rank for the agreement
hypergraph of scalar RS codewords around one center when they are not all
equal. Its proof uses their coefficient differences from the last word.
Theorem 2.10 and Remark 2.11, p. 8, give full rank over F_q(X_1,...,X_n)
for k-weakly-partition-connected hypergraphs, over every finite field.
Here every vertex partition P must satisfy
sum_e max(number of parts met by e minus 1,0)>=k(|P|-1), Definition 2.2.
Lemma 3.1, p. 9, gives a probability bound for uniformly random distinct
evaluation points. Those hypotheses do not supply a fixed-subgroup rank
certificate. No probability assertion is transferred to this domain.

Chong Shangguan and Itzhak Tamo,
[Combinatorial list-decoding of Reed-Solomon codes beyond the Johnson radius,
arXiv:1911.01502v1](https://arxiv.org/pdf/1911.01502v1),
stamp November 4, 2019, title-page date November 6: inspected Definition
4.1 and Lemma 4.2, printed pp. 10–11, and Lemma 4.3's common-root division,
pp. 11–12. The exact source statement needed for the narrower diagnostic
is recorded in its separate assessment below; nothing is reproved here.

Reuse [the prior BGM comparison](2026-09-26-current-target.md), section
“New primary readings”: Brakensiek–Gopi–Makam, arXiv:2206.05256v4,
Theorem 1.13 gives higher-order MDS/list-decoding equivalence with duality;
Corollary 1.15 and Proposition 4.5 supply generic/random RS guarantees.
The fixed code still needs its own intersection certificate. This duplicate
exclusion is retained, not reported as new evidence.

## Bounded search and remaining coverage

Queries executed:
- `Reed Solomon agreement sets list decoding combinatorial supports higher order MDS arbitrary evaluation points list size bound`
- `Reed Solomon list decoding support intersection constraints common received word generalized Singleton bound`
- `Shangguan Tamo generalized Singleton bound 3-wise intersection matrices theorem Reed Solomon arxiv`
- `Reed Solomon prescribed evaluation set list decoding support intersection matrix rank constraints`
- `"Reed Solomon" "agreement supports" "rank"`
- `"Reed Solomon" "multiplicative subgroup" "list size" upper bound`

Primary statements and essential proof cases were read before further
passages. Kumar–Ron-Zewi, TR26-032, contents, the beginning of Section 4.3
and bibliographic-note search hits were inspected as a source map to
Guruswami–Xing; the underlying theorem
was not read and is an unread lead, not an applicable bound or a source
blocker for the selected rank diagnostic. Search hits for folded,
linearized and randomly punctured codes, subgroup proximity lower examples
and informal prize submissions were not imported as upper theorems.
Previously assessed Johnson, packing and fixed-slack inputs are reused;
their failed or unquantified finite-instance transfers are not reopened.

This bounded review supplies no threshold certificate and makes no
exhaustiveness or novelty claim. A concrete follow-up is separately scoped
in [the triple-support assessment](2026-10-05-triple-support-rank-diagnostic.md).
Continue only if that diagnostic produces an explicit forbidden support
configuration or precisely characterized realizable degeneracy; abandon a
universal nonvanishing claim if a valid singular configuration is found.
Neither finding alone settles safety: a sufficiently strong family-count
estimate, 67-agreement safety, exact maxima and ABF comparison remain open.
Mathlib matching coverage was not checked. No lemma, mathematical script,
DAG edge or PROOF argument was changed in this literature-only step.
