# Matching-two small-union criterion: bounded source comparison

TARGET: Assess whether every simple four-uniform family with sixteen edges on sixteen vertices, vertex degrees four and matching number two, contains six distinct edges whose union has at most eight vertices.
CHECKED: 2026-10-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Exact four-uniform/six-edge/eight-vertex and regular matching-number-two searches found no inspected exact theorem or counterexample; matching extremal bounds and sparse-configuration terminology were checked below.
SOURCE_EVIDENCE: Frankl–Łuczak–Mieczkowska (2012), Theorem 1 and its shifting setup, printed pp. 1–3; Shangguan arXiv:2210.11338v1, definition and Theorem 3, printed pp. 1–2, proof scope pp. 2–3; reuse of the saved Ihringer–Kupavskii, Füredi and Ellis–Kalai–Narayanan assessment.
COMPARISON: The matching theorem's size hypothesis excludes the target parameters; the sparse-configuration theorem is asymptotic and has a different union threshold; reused regular-intersecting and fractional bounds do not supply the six-edge conclusion.
GAP: The exact universal statement remains unproved and no inspected source gives its negation; a bounded exact counterexample test is warranted without a novelty claim.
REASON: Essential terminology and nearby theorem comparisons are now inspected; further browsing is not needed before one bounded mathematical test of this unchanged target.
SCOPE: The exact TARGET, including simple four-uniform sixteen-edge sixteen-vertex degree-four families of matching number exactly two; bounded counterexample testing, not an affine-moment theorem or classification of all equality pencils.

## Proposed relevance and bounded test

The main gap remains whether an L010 equality pencil exists, not whether
balanced incidence forces a disjoint triple. A small-union subfamily could
allow L024's affine-restriction mechanism to act within a larger family.
The proposed six-edge/eight-vertex threshold is a target for assessment,
not an established theorem or a claimed exclusion of general pencils.
Even if the set-system criterion holds, an independently approved
specialization to these smaller subfamilies would still be required.

Continue this criterion only if an inspected theorem or documented bounded
comparison supports a concrete mathematical test. A known counterexample
would abandon the universal criterion while preserving L024. Incomplete
coverage stays REVIEW_REQUIRED; source absence alone proves nothing.
No new result about this criterion is derived in step 035.

## Inputs and unresolved assumptions

Essential local inputs for the proposed downstream mechanism are L010,
L023 and L024. L010 equality supplies distinct four-element supports and
vertex degrees four; matching number two is a conditional case, not an
established property of every equality pencil. L024 only excludes the
exact doubled cyclic family. The universal small-union assertion, its
application to affine moments, and any reduction of arbitrary supports
to the saved L022 triple remain unresolved. The ABF26 definition and
challenge-level correspondence remain independent gaps.

The next turn may perform one bounded mathematical test of this unchanged
criterion. No criterion, counterexample or new lemma was derived in this
source review. Mathlib coverage of the exact criterion is not checked.


## Search record and primary comparison

Checked on 2026-10-05. Queries included `"regular" "hypergraph"
"matching number two"`, `"4-uniform" "six edges" "eight vertices"`,
`"4-uniform" "(8,6)" hypergraph`, `"four-regular" "four-uniform"
hypergraph matching`, and `"regular" "matching number" "sixteen"
hypergraph`. Broader searches used hypergraph matching/small union and
Brown–Erdős–Sós terminology. No result snippet is treated as a theorem.
Failure to find the exact statement does not establish novelty.

**Matching extremal theorem.** Frankl, Łuczak and Mieczkowska,
*On Matchings in Hypergraphs*, Electronic Journal of Combinatorics
19(2) (2012), P42, DOI 10.37236/2176,
[author-hosted published PDF](https://www.renyi.hu/~pfrankl/j101.pdf),
Theorem 1, printed p. 2. The statement requires k>3 and
n>2k²s/log k, and identifies the maximum-edge families with matching
number s as all k-sets meeting a fixed s-set. For k=4,s=2 the size
condition requires n>64/log 4, hence does not include n=16.
The extremal-family definition on p. 1 and the shifting setup,
Lemmas 2–5 and start of the proof on pp. 2–3 were read. These concern
maximum-edge families and do not transfer degree-four regularity or
this six-edge union condition to an arbitrary family. No theorem
application or reproof is proposed. The publisher PDF initially loaded
but subsequent extraction timed out; the author's published copy was
accessible. Its abstract differs from the journal landing-page abstract;
the numbered Theorem 1 controls this comparison.

**Sparse-configuration terminology and theorem.** Chong Shangguan,
*Degenerate Turán densities of sparse hypergraphs II: a solution to the
Brown-Erdős-Sós problem for every uniformity*,
[arXiv:2210.11338v1](https://arxiv.org/pdf/2210.11338v1), 20 October 2022.
The definition on printed p. 1 calls a family G_r(v,e)-free when every
e distinct edges have union of size at least v+1. Thus the sought
configuration uses the standard G_4(8,6) terminology. Theorem 3 on p. 2
asserts existence of the limit of f_r(n,er−2(e−1),e)/n² for fixed
r>=3,e>=3. With r=4,e=6 its union parameter is fourteen rather than
eight; it provides no exact sixteen-vertex regular matching-two result.
The proof outline and Lemmas 4–5 on pp. 2–3 were inspected: their
auxiliary exclusions and density comparison do not assert our finite
criterion. No later full proof is needed for an inapplicable theorem,
and no asymptotic construction is imported as a finite counterexample.

**Reused evidence.** The detailed comparison in
[the balanced-support assessment](2026-10-04-balanced-support-disjoint-triple.md)
remains applicable to regularity and matching obstructions. Its inspected
Ihringer–Kupavskii Theorem 7 only rules out a regular intersecting family
on sixteen vertices at uniformity four; Füredi's fractional matching
bound permits matching number two. The Ellis–Kalai–Narayanan translate
construction is already specialized in L023. L023 and L024 were read
in full, along with ATTEMPTS/016's stop: neither the incidence failure
nor its exact-family moment exclusion settles the proposed criterion.
No duplicate exact criterion was found in the targeted notebook search.

The nearly-perfect-matching and newer partite matching search results
are unread leads, not supporting theorems. The target has no partite,
small-codegree or asymptotic hypotheses; these leads are not essential
coverage blockers for the bounded test. No matching Mathlib theorem was
searched or claimed absent.

## Bounded continuation and decision threshold

Keep the exact TARGET as the next action. One concrete first test is
an exact search among full sixteen-translate orbits of four-element
seeds in Z/16Z, accepting only families meeting every target hypothesis.
This is a restricted counterexample search, not a proposed reduction of
all regular families to cyclic ones. Any purported counterexample must
have its full edge list retained and independently checked for simplicity,
all degrees, absence of every disjoint triple, existence of a disjoint
pair, and all six-edge unions having at least nine vertices. These are
verification requirements for the next turn, not calculations performed
here. A verified counterexample abandons the universal criterion. A
restricted search with no witness leaves it open and must not be reported
as a proof; continuation then requires a concrete noncyclic or structural
idea. No affine-moment implication is approved by this assessment.

Essential local inputs for relevance remain L010, L023 and L024; the
bounded incidence test itself uses only the stated finite hypotheses.
Even a universal positive answer would leave its affine-moment application,
arbitrary-triple reduction beyond L022, and the ABF26 correspondence
unresolved. The six-edge/eight-vertex threshold remains a proposed
intermediate target; the main error interval remains 11/q–16/q with an
allowable count of fifteen.
