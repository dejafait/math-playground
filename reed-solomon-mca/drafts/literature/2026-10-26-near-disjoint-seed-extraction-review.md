# Near-disjoint four-row seed extraction — source comparison

TARGET: Determine whether every 12–14-edge linear two-plus-two family on the fixed S and J with maximum coordinate degree four contains four edges having one singleton intersection in S and five empty pairwise intersections, or give an explicit counterexample.
CHECKED: 2026-10-26
DECISION: EXPLORE
SEARCH_EVIDENCE: Read L152, C152a's same-family application, L086/L109's hypotheses and equality conclusions, L165's scope, L023/L025 and ATTEMPTS/048–049,/052–053; searched linear bounded-degree hypergraph near-matchings, (2,2)-partitioned hypergraphs and co-diamond terminology. No adequate exact match was located in this bounded search; see inspected sources and queries below.
SOURCE_EVIDENCE: Reused the inspected Füredi (1981) Corollary 3 scope in the prior disjoint-pair assessment; inspected Aharoni–Argue arXiv:1412.3067v2, definitions p. 1 and Example 3.1/Assertion 3.2 with proof p. 3; Alecu–Atminas–Lozin–Zamaraev, accepted manuscript (2021), Figure 1 p. 5 and section 4.2, Lemmas 4–6 and Theorem 4 with proof cases pp. 7–8.
COMPARISON: Existing coverage supplies a disjoint pair or results under additional intersecting/graph hypotheses, not the prescribed four edges with their sole intersection in S. L165's audited exclusion remains specific to one labeled seed; neither a matching number nor an unmarked co-diamond would transport its quotient matrices.
GAP: Decide the exact finite incidence implication under all stated hypotheses; no positive extraction or admissible counterexample is supplied by the checked sources or this review.
REASON: Essential source comparison is complete for one bounded proof/counterexample attempt on the unchanged target. EXPLORE records a documented search without an adequate match, not novelty, an exclusion theorem or evidence that the proposed implication is true.
SCOPE: S=(1,8,12,18,22,27,33), J=(47,50,64,70,75,79,85,89,96); 12–14 distinct supports I union K with |I|=|K|=2, every pair intersecting in at most one coordinate, and every coordinate of S union J in at most four supports. The proposed conclusion concerns four edges, not numeric labels or quotient ranks.

LITERATURE_REASON: At invocation start the stronger four-edge extraction target was REVIEW_REQUIRED and outside the prior disjoint-pair and fixed-seed audit assessments; this review addresses that changed conclusion only.

## Main gap, intermediate target and bounded test

The main local gap is uniform twelve-row exclusion in the represented
t=0 equality class. The intermediate target is the exact TARGET above,
on the stated fixed S and J, with isolated labels permitted. A positive
answer could organize a later geometric exclusion by this incidence
pattern. That later result would still need all original labels and
their actual maps; L165 provides no relabeling invariance.

Continue with one bounded proof or exact counterexample attempt after
separate next-turn approval of this newly completed assessment. A proof
must cover every m=12,13,14. A counterexample must display one complete
labeled family, verify distinctness, its two-plus-two partition,
linearity and every integer coordinate degree, and check every four-edge
subset for the specified S-intersection and five disjoint pairs. Such a
counterexample stops this unconditional extraction mechanism only.
Incomplete search or a graph example without a hypergraph realization
does not suffice. No all-original-quadruple rank sweep is proposed.

## Local coverage, duplicates and recorded failures

L152's full abstract proof and audit establish only a disjoint pair
under the same incidence hypotheses. Its primary general input is
Z. Füredi, *Maximum degree and fractional matchings in uniform
hypergraphs*, Combinatorica 1(2) (1981), 155–162, Corollary 3 p. 158
([DOI](https://doi.org/10.1007/BF02579271)). Reuse the precise statement,
plane exception and inspected proof scope in
`drafts/literature/2026-10-24-two-overlap-disjoint-pair-extraction-review.md`.
That intersecting-family alternative supplies no four-edge conclusion.
The author-hosted scan failed to reopen through the web tool today;
unchanged adequate prior coverage is retained, so this is not an
essential source blocker or a reason to reprove the general theorem.

C152a's proof already checks the entire incidence-hypothesis transfer
for the actual E_2 family, using L086's full sixteen-support equality
family and L109's r=12+n_0 count. This is existing coverage, not a new
specialization here. It retains q=97^20, k=8, the pinned radius cell,
syndrome membership in U_S, nonzero actual determinant and locator
polynomials, sixteen actual finite events, t=0, arbitrary weights and
original chart, and the inherited L056/L069/L040, L051/L055 and
L104/L103 computational qualifications. Thus transfer of these abstract
incidence hypotheses is already available conditionally; no new actual
family or moment-compatible realization is asserted. The four-edge
conclusion itself remains unproved.

L165's hypotheses and conclusion confirm that its full-locus bound
concerns exactly (35,522,477,566). Its displayed supports motivate the
target; they supply neither extraction nor exclusion for other labels.
No detailed geometric proof or certificate is needed for this source
comparison, and no passed audit was replayed.

L023 and L025's displayed cyclic families are earlier counterexamples
to different extraction claims. Their first two translates share two
labels, violating today's linearity premise; the earlier assessment
already recorded this mismatch. They do not settle this TARGET.
The bounded notebook-local search found no earlier co-diamond or exact
four-edge extraction assessment. This is not a global duplicate claim.
ATTEMPTS/048–049 stop rank-only pair stratification and repeated passed
audits; ATTEMPTS/052 refutes universal four-row finiteness; /053 excludes
twelve rows on one family only. None is reopened or generalized here.

## Additional primary source comparison

**Ron Aharoni and C. J. Argue**, *Covers in Partitioned Intersecting
Hypergraphs*, [arXiv:1412.3067v2](https://arxiv.org/pdf/1412.3067v2),
1 January 2015; published European J. Combin. 51 (2016), 222–226,
[DOI](https://doi.org/10.1016/j.ejc.2015.05.005).
Read definitions p. 1 and section 3.1, Example 3.1 and Assertion 3.2,
with its proof p. 3. Their partition convention allows two vertices
per part. They give a ten-edge (2,2)-partitioned intersecting example
with cover number four. The proof checks intersection within and
between its two five-edge classes, then three-vertex covers lying in
one part or split between parts. The ten-edge example is not a
12–14-edge witness for this target. The result concerns cover numbers
for intersecting families; it does not force the requested near-matching.
In particular, replacing two-plus-two by four-partiteness or assuming a
three-vertex cover has no support here. References relevant to the
fractional matching comparison lead to the already assessed Füredi
paper. The publisher fetch returned 403; the versioned primary
manuscript was accessible, so no dependent access blocker remains.

**Bogdan Alecu, Aistis Atminas, Vadim Lozin and Viktor Zamaraev**,
*Graph classes with linear Ramsey numbers*, 2021 accepted manuscript,
[primary repository PDF](https://wrap.warwick.ac.uk/148196/1/WRAP-graph-classes-linear-Ramsey-numbers-Lozin-2021.pdf).
Read definitions p. 2, Figure 1 p. 5, and section 4.2 pp. 7–8.
The co-diamond is the four-vertex graph with one edge. Lemma 5 classifies
co-diamond-free bipartite graphs with an edge: either each vertex has
at most one non-neighbour across the partition, or the graph is
K_(s,t) plus one isolated vertex. Its proof separates zero, one and
at least two isolated vertices. Lemmas 4 and 6 and Theorem 4 use
additional diamond-freeness; read their independent-set and
clique/complement cases. No such graph hypotheses are supplied by
this TARGET. These unmarked graph results also do not specify that
the sole hyperedge intersection is in S. They therefore supply
terminology and conditional structure, not an import settling the
incidence question. No general graph-class theorem is reproved.

For terminology comparison only, one may inspect a family's intersection
graph and mark each intersection by its coordinate's part. The desired
pattern asks for a co-diamond whose sole adjacency is marked S.
This is a description of the target, not an extracted subgraph theorem;
unmarked co-diamond absence is a different condition. No hypergraph
or graph realization theorem is inferred from these papers.

## Search record, limits and continuation assumptions

Actual queries included `linear hypergraph induced matching one
intersecting pair four edges bounded maximum degree`, `hypergraph
"2+2" "matching" linear`, `hypergraph "(2,2)" "matching" uniform`,
`"co-diamond-free" graph structure isolated vertices`, `"two-plus-two"
hypergraph matching`, `hypergraph "near matching" four edges linear`,
`"hypergraphs" "one intersecting pair"`, `"linear hypergraph" "K2"
"2K1"`, and `"(2,2)" "partite" hypergraphs matching`. Followed the
partitioned-cover lead to its versioned primary manuscript and the
co-diamond lead to the accepted manuscript above. The earlier
*Linear Ramsey numbers* search hit is a different version/title and
is not used for theorem numbering. Other search hits on induced
matchings, asymptotic minimum degrees and algorithmic complexity were
not inspected as theorem inputs and supply no evidence for this target.
No assertion of novelty or exhaustive literature coverage follows from
failure to locate an exact match.

The ready scope is this single finite incidence target, not new rank
strata, a coding construction or geometric transfer. Essential local
comparison inputs are L152, C152a and its L086/L109 qualifications;
L165 is motivation only. L159–L161 are not premises. Exclusion for other
labels, the coding/chart/weight gates, arbitrary representation,
challenge identification and sharp radius remain unresolved. No
cross-notebook input was read. Full matching Mathlib coverage is
**not checked**; no absence or formal verification is claimed.

This literature-only step produced no lemma, new incidence bound,
counterexample, mathematical script or computational certificate.
