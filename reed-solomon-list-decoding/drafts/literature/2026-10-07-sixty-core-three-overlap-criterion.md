# Three-support, three-point-overlap criterion — scoped source comparison

TARGET: Determine the exact realizability criterion for three 68-supports with a 60-point common core, three disjoint three-point pair-only overlaps and two private points per support.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched three-codeword/common-intersection cubic realizability, pairwise intersections, three-way intersection matrices and exact 60/68 terms; compared L020/L031, prior RS-support/triple/four-support assessments and ATTEMPTS/010,019–023. No completed matching local criterion was found; this does not establish novelty.
SOURCE_EVIDENCE: Alrabiah–Guruswami–Li arXiv:2304.09445v3 (https://arxiv.org/pdf/2304.09445v3), Definition 2.5, Lemma 2.7 and complete proof, printed pp. 7–8, Theorem 2.9, p. 9; Shangguan–Tamo arXiv:1911.01502v1 (https://arxiv.org/pdf/1911.01502v1), Definition 4.1 and its kernel equivalence, Lemma 4.2 hypotheses, PDF pp. 9–11 (one-based), and common-root division in Lemma 4.3, PDF p. 11.
COMPARISON: The general difference-kernel dictionaries cover arbitrary finite fields and support patterns; the square-determinant theorem requires an even total pair-overlap size and does not cover the stated nine overlap points. Neither inspected result supplies the fixed-label converse with three pairwise distinct tuples.
GAP: Specialize the general dictionary with common-core removal, strict degree, all three distinctions, extension-field ranks, tuple-width necessity and a compatible-center converse; check nonvacuity over actual H labels. No quantitative cap or safety transfer is supplied.
REASON: This is a narrowly scoped reproduction of an inspected framework for changed overlap hypotheses, independent of the failed shortened cubic avoidance claim; direct generic determinant import is unavailable.
LITERATURE_REASON: The supplied REVIEW_REQUIRED target changes the overlap sizes and common core outside the previously ready L020/L031 scopes; exact source applicability and duplicates required comparison.
SCOPE: Exactly the TARGET pattern on C001a’s E=F_65537, F=F_(65537^28), order-1024 subgroup H, k=64 and all m>=1; selected supports permit extra agreements. One criterion attempt and a bounded actual-label nonvacuity check; no extremal bound or new packing construction.

## Main gap and prospective use

Arbitrary-center safety at 68/67 agreements remains open and
955<=t_star(m)<=957. An additional valid labeled restriction might combine
with L031’s four-support rule in a strengthened 60-core family bound.
This is a plausible downstream use, not an established counting route.
The new pattern does not itself exclude L032, whose displayed pair-only
overlaps have size two. A sufficient cap, exact 60-core incidence transfer,
cross-core consistency, common-center realization of large families,
67-agreement safety and ABF equivalence remain unresolved.

Fix a 60-subset C of H, three pair-only sets U_12,U_13,U_23 of size
three and private sets W_1,W_2,W_3 of size two, all seven sets mutually
disjoint. Set S_i=C union W_i union the two U_ij incident to i.
Realizability asks for three pairwise distinct polynomial m-tuples over F,
strict row degree less than 64, and one center agreeing on the selected
S_i. Neither messages nor center are presumed E-valued; extra agreements
are allowed. These are hypotheses, not a realized construction.

## Primary inputs inspected and their limits

Alrabiah, Guruswami and Li, *Randomly punctured Reed–Solomon codes achieve
list-decoding capacity over linear-sized fields*,
[v3](https://arxiv.org/pdf/2304.09445v3), 26 July 2023:
Definition 2.5 constructs signed Vandermonde rows over any finite field
for each hyperedge, using differences from the last message. Lemma 2.7
assumes distinct scalar RS codewords and their agreement hypergraph;
its complete proof exhibits the nonzero coefficient-difference kernel.
Theorem 2.9 assumes weak partition connectivity and asserts full column
rank over a rational-function field, not at prescribed subgroup labels.
Import the signed framework and scalar necessary kernel only. Selected
agreements, tuple distinctions and a converse still require local work.
No symbolic/random full-rank guarantee is transferred to H.

Shangguan and Tamo, *Combinatorial list-decoding of Reed–Solomon codes
beyond the Johnson radius*,
[v1](https://arxiv.org/pdf/1911.01502v1), 4 November 2019 arXiv stamp:
Definition 4.1 applies to any integer s>=1 and three subsets. It explicitly
equates a nonzero specialized kernel with three degree-less-than-s
polynomials summing to zero and vanishing on their respective overlaps.
Lemma 4.2 additionally requires empty triple intersection, an even total
pair-overlap size, s equal to half that total, and each pair size at most
s<=k. It gives symbolic nonzero determinant, not fixed-label rank.
Our total is nine, so this square-determinant lemma cannot be directly
imported. Lemma 4.3’s proof divides differences by the common-root product;
its global list-decoding theorem is not invoked. The general dictionary
remains usable without Lemma 4.2. No new criterion is derived here.

For ST, the one-based PDF page locations above are used to avoid the
printed-folio ambiguity in earlier local citations. Definition 4.1 begins
on PDF page 9 and its kernel dictionary continues on page 10; Lemma 4.2
is on page 10; Lemma 4.3’s common-root proof is on page 11. The theorem
identifiers and exact proof step are the controlling citations.
An initial retrieval of arXiv:1902.05903v1 was an irrelevant prior sparse-
hypergraph source; it supplies no input to this target. The correct ST
source above was retrieved and inspected. No essential access blocker
remains. Generic/higher-order-MDS coverage is reused from the prior
RS-support/four-support assessments; no broader theorem is reproved.

## Local duplicates, failed routes and research obligations

L020’s necessity, rank/descent, distinctness and center proof were read:
it treats a 61-core and size-two pair-only overlaps. L031’s corresponding
proof was read: it treats four supports on a 60-core with size-two overlaps.
Their conclusions cannot be substituted for the new pattern. Their
arguments are reusable methods, and any later specialization should be
classified REPRODUCTION rather than a new general rank theorem.
C001a fixes the field, degree, grid bracket and ambient threshold; L001
supplies the common-agreement/root bound. L027 is downstream comparison
only, not a proved 60-core cap transfer.

ATTEMPTS/010 preserves realizable singular triples, excluding any inference
of universal nonsingularity from symbolic results. ATTEMPTS/019–021 retain
the above-threshold obstruction to the old 61-core local edge system.
ATTEMPTS/022 is an administrative global-pair park, not mathematical
exhaustion. ATTEMPTS/023 preserves L032’s counterexample to the prescribed
shortened cubic avoidance claim. None bans a separately tested larger-
overlap restriction. Searches in the specific triple/60-core working
notes and histories found no completed matching result; no novelty claim
follows. All unfinished work is preserved.

For a later research attempt, import the cited dictionaries, justify the
common-root specialization and prove necessity/converse with all three
pairwise distinctions. Rank deficiency alone must not be called
realizability. Do not project a tuple without proving that distinctions
survive. Establish extension-field applicability and the status for every
m>=1, construct one compatible center if claiming sufficiency, and retain
strict degrees and extra agreements. Any finite diagnostic must save and
inspect full exact label/rank/witness evidence; no mathematical script was
run during this source review.

Continue if the exact criterion yields a genuine labeled restriction with
plausible counting use. Abandon a universal-exclusion claim upon a valid
realization, and abandon this restriction as a cap mechanism if it is
vacuous or only duplicates already enforced conditions. If nonvacuity is
unresolved, retain that gap rather than claiming an informative negative.
Full matching Mathlib coverage and supporting theorem names have not been
checked; this is not evidence of absence.

## Search record and next gate

Queries included `Reed Solomon three codewords intersection matrix common
intersection cubic polynomials Shangguan Tamo`, `"Reed Solomon" "three"
"pairwise intersections" realizability`, `"2304.09445" intersection matrix`,
`"Reed Solomon" "three" "cubic" "intersection"`, `"Reed Solomon" "60"
"three" "68"`, and `"three way intersection matrix" polynomials dependence`.
Exact-number queries were uninformative. Tree-packing and merged journal
search hits were discovery leads only; no new unread theorem is treated
as essential coverage. The exact scalar framework is inspected, while
the fixed-subgroup and simultaneous-tuple differences are explicitly
reserved for research.

This literature-only comparison writes no lemma, mathematical script,
DAG edge or PROOF argument. SPECIALIZE coverage is newly completed and
requires separate supervisor approval next turn before a research
invocation. The exact TARGET is preserved.
