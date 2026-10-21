# Extremal transfer of the triple-support restriction — bounded review

TARGET: Assess whether known extremal bounds for 68-subset families constrained by L020 certify B_m(956/1024)<=65537^28/2^128 on C001a's instance for every m>=1.
CHECKED: 2026-10-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched forbidden triple intersections, triangle-free hypergraph bounds, fixed-point RS agreement families, and root-pair sum/product collinearity; inspected the primary statements below and reused the ready RS-rank and packing assessments. No matching numerical transfer was found; this does not establish absence or novelty.
SOURCE_EVIDENCE: Read Filmus–Golubev–Lifshitz arXiv:1911.02297v1 Section 1.1 and Section 4/Theorem 4.1 with its proof; Frankl et al. arXiv:2405.16452v1 Section 1.1 and Theorem 1; Karamanlis–Dodos, Forum Math. Sigma 13 (2025), e99, Theorem 1.1. Reused Shangguan–Tamo and Bailey–Burgess coverage.
COMPARISON: General spectral bounds require presently uncomputed fixed-domain spectra and measure conversion; whole-pattern triangle exclusions and pairwise forbidden intersections do not encode L020's label-dependent restriction. No inspected conclusion certifies the exact threshold; C001b still exceeds it by a factor in [2.763,2.764).
GAP: Neither a uniform counting certificate nor a justified density-to-cardinality transfer is supplied for determinant-constrained selected-support families.
REASON: Park direct extremal-theorem import; propose a separately reviewed Delsarte distance-distribution certificate as an independently testable support bound, preserving the determinant route and its degeneracies.
LITERATURE_REASON: Essential quantitative extremal coverage was missing from the ready local rank diagnostic; this is the required review of that changed target.

## Gap, scope and stopping test

The main gap is arbitrary-center safety at 68 agreements. The reviewed
intermediate target was a known counting bound using L020; a sufficient
bound would certify error index 956 for every m>=1. Continue direct import
only with matching hypotheses and an upper bound U satisfying
2^128 U<=65537^28 (equality safe). This bounded review supplies neither.
Do not treat failure to find a theorem as disproof of a possible transfer.

Inputs L001, C001a, C001b and L020 were checked through their relevant
proof passages; C001a retains C012a/L019. L020 permits extra agreements
and genuine antipodal triples. No frequency or distribution assumption,
restriction on other triple patterns, or scalar/tuple equality is available.
The 67-agreement boundary and ABF equivalence remain independently open.
No new mathematical result or numerical bound was derived in this review.

## Inspected primary comparisons

Yuval Filmus, Konstantin Golubev and Noam Lifshitz,
[High dimensional Hoffman bound and applications in extremal combinatorics](https://arxiv.org/pdf/1911.02297v1),
v1, November 6, 2019 stamp, Section 1.1, pp. 2–3; Section 4,
Theorem 4.1 and proof, pp. 10–12: for a weighted r-uniform hypergraph,
alpha<=1-1/product_{i=0}^{r-2}(1-lambda_i), where lambda_i is the
minimum skeleton eigenvalue over supported i-face links. Alpha is measured
in the induced vertex distribution. This is a potential framework for
forbidden nonsingular triples, not a computed certificate: spectra and
conversion to unweighted family size are missing. Subgroup multiplication
alone does not establish uniform weight on all 68-subsets. Theorem 1.5's
empty-symmetric-difference triangles and n<=4k-1 regime do not match our
61-core pattern with unique portions. No application or eigenvalue claim
is made here; other spectral results cited there remain unread leads.

Peter Frankl, Zoltan Furedi, Ido Goorevitch, Ron Holzman and Gabor Simonyi,
[Triangle-free triple systems](https://arxiv.org/pdf/2405.16452v1),
v1, May 26, 2024, Section 1.1, p. 2, and Theorem 1, p. 6:
a 3-uniform family excluding all four triangle types A,B,C,D has at most
floor(n^2/8) edges. Our family consists of 68-subsets; turning forbidden
support triples into edges instead makes the candidate family an
independent vertex set. This edge bound is not that independence bound.
Neither deleting the core nor pairing points has an established
cardinality-preserving transfer. The theorem is not applied.

Miltiadis Karamanlis and Pandelis Dodos,
[Forbidden sparse intersections](https://doi.org/10.1017/fms.2025.10067),
Forum of Mathematics, Sigma 13 (2025), e99, published June 26, 2025,
Theorem 1.1: cross families forbidding every intersection of size ell,
with 0<p<=p'<=1/2 and ell<=pn, satisfy a product biased-measure bound
2 exp(-min(ell,pn-ell)^2/(58^2 pn)). L020 does not forbid pair
intersection size 63: its realizable example has that size in all three
pairs. Exclusions at sizes >=64 come from L001, without exploiting the
new determinant constraint. Layer and supersaturation extensions are
unread leads and no threshold improvement is inferred from them.

## Duplicate/failure search and continuation

Local searches in literature assessments, history and ATTEMPTS for
extremal, triple, Delsarte, linear programming, Hoffman and triangle-free
found the ready rank/packing reviews and the two recorded stops, but no
completed Delsarte calculation. ATTEMPTS/009 preserves the nested-floor
certificate failure; ATTEMPTS/010 preserves the false universal-exclusion
route. Neither is rerun. L016–L018 remain parked.

An independent distance-distribution mechanism is proposed in
[the Delsarte assessment](2026-10-05-delsarte-support-certificate.md).
This does not exploit L020 or claim to resolve its quantitative transfer.
It offers a finite certificate test for the same 68-agreement gap without
assuming generic evaluation points. That new ready continuation requires
separate supervisor approval next turn; no LP or other mathematical script
was run here. Full matching Mathlib coverage for these counting results:
not checked. No canonical lemma, DAG or PROOF argument changed.

Search queries actually used include:
- `extremal set families forbidden triple intersections packing designs triangle sparse hypergraph bounds`
- `Reed Solomon list decoding intersection families extremal hypergraph fixed evaluation points Shangguan Tamo`
- `root pairs sum product collinear finite field subgroup extremal set families`
- `Delsarte linear programming bound constant weight codes theorem Hahn polynomials pdf`

Search results are discovery leads, not theorem evidence; only the precise
passages above support the comparisons. Ready Shangguan–Tamo v1 Definition
4.1/Lemmas 4.2–4.3 and Bailey–Burgess Proposition 1.1.4 coverage is reused
from the prior assessments without renewed browsing.
