# Balanced equality supports: matching comparison and bounded specialization

TARGET: Determine whether L010's sixteen distinct four-element supports on sixteen coordinates, each coordinate used four times, necessarily contain three pairwise disjoint supports; compare the strongest applicable matching theorem or counterexample with L022's fixed-triple restriction.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched regular intersecting hypergraphs with uniformity four, eight vertices and degree four; regular intersecting families on 2k vertices; fractional matching bounds; and cyclic intersecting orbits; located and read primary papers listed below.
SOURCE_EVIDENCE: Ihringer–Kupavskii arXiv:1709.10462v3 Theorem 7 and its proof; Füredi (1991) Section 2 equation (2.1), Theorems 3.3 and 4.3 with their parameter restrictions; Ellis–Kalai–Narayanan arXiv:1702.02607v8 Section 4 Lemma 4.1 and its complete proof.
COMPARISON: The inspected regular-intersecting theorem guarantees only a disjoint pair here; the fractional bound does not force three; the cyclic difference-cover construction supplies a relevant known mechanism but not the exact sixteen-edge degree-four counterexample as a cited statement.
GAP: Verify a small cyclic seed's difference cover, orbit size and degrees, and the matching number of two disjoint copies; no exact incidence-only counterexample or triple theorem is claimed from this review.
REASON: Local verification of the exact size and degree requirements is justified against the known translate construction; it can reject the incidence-only reduction without another fixed-moment-triple enumeration.
SCOPE: Simple four-uniform four-regular families with sixteen vertices and sixteen edges; theorem comparison and finite specialization of a cyclic difference-cover orbit, excluding any assertion of affine-moment realizability.
COVERED_TARGET: Determine whether L010's sixteen distinct four-element supports on sixteen coordinates, each coordinate used four times, necessarily contain three pairwise disjoint supports; compare the strongest applicable matching theorem or counterexample with L022's fixed-triple restriction.
COVERED_TARGET: Specialize Ellis–Kalai–Narayanan Lemma 4.1 to A={0,1,2,4} in Z/8Z: check its difference cover, eight distinct translates and vertex degrees, then test whether two disjoint copies have sixteen edges, degree four and matching number two; use the result to accept or reject the incidence-only disjoint-triple reduction from L010, retaining L022's fixed-triple restriction.

## Claim, relevance and prior work

The gap is L010's possible sixteen-count equality, against an allowable
fifteen for the pinned F_(97^20) instance. The global interval stays
11/q–16/q. The intermediate target asks what follows from distinctness,
four-uniformity and degree four alone. Additional locator or moment
conditions are not hypotheses of this abstract matching test.

L010's conclusion and L022's hypotheses/conclusion were inspected.
Local searches in drafts/literature, history and ATTEMPTS found no prior
matching test. The saved triple's completed exclusion and the previous
warning about manufactured balanced locators remain relevant: neither
abstract incidence nor L022 establishes arbitrary moment compatibility.
This review neither reopens that exhausted triple nor assumes domain
automorphism transitivity.

## Queries and primary source locators

Queries included `regular intersecting hypergraph 4 uniform 8 vertices 4
regular matching`, `regular intersecting families 2k cyclic k subsets
matching hypergraphs`, `Furedi 1981 maximum degree fractional matchings
uniform hypergraphs pdf`, and `intersecting 8 orbit 4 cyclic family`.
No search snippet is used as theorem evidence.

- **Ihringer–Kupavskii, Regular Intersecting Families**, accepted version,
  [arXiv:1709.10462v3](https://arxiv.org/pdf/1709.10462v3), 1 July 2019,
  Theorem 7, p. 3; proof in Section 3.3, p. 9. A regular intersecting
  k-uniform family has n<=k^2-k+1, with projective-plane equality.
  Its proof checks the strict inequality case and the equality case
  separately through the inner distribution. At k=4 its vertex threshold
  is thirteen, below sixteen, so it excludes matching number one, not
  matching number two. Section 4.2 Theorem 25 and the Section 4.3 table
  were also inspected: their eight-vertex extremal family has 32 edges
  and degree sixteen, not the required eight edges and degree four.
  Earlier-v1 search extracts call this an unproved conjecture; v3 proves
  Theorem 25. The v3 statement controls this comparison.

- **Füredi, On r-graphs and r-multihypergraphs with given maximum degree**,
  J. Austral. Math. Soc. A 50 (1991), 204–212,
  [primary publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/3F60335F218D9C250DA813F8B8A8B8CC/S1446788700032699a.pdf/on_rgraphs_and_rmultihypergraphs_with_given_maximum_degree.pdf),
  [DOI](https://doi.org/10.1017/S1446788700032699).
  Section 2, p. 206, equation (2.1) states
  nu*<=nu(r-1)+p/r for rank r>=3 when there are no p+1
  vertex-disjoint projective planes of order r-1. The fractional bound
  permits integral matching number two in the target comparison.
  Theorem 3.3 requires D>(r-1)^2 nu; Theorem 4.3 requires D sufficiently
  large, with an explicit sufficient threshold in its proof, pp. 210–211.
  Degree four is not certified by either large-degree hypothesis.
  Section 5's uniform edge-weight argument and Section 6's two proof
  cases were read. These are supporting bounds, not a triple theorem.
  The 1981 original cited there was not read; the author's explicit 1991
  restatement suffices for this comparison, so it is not an access blocker.

- **Ellis–Kalai–Narayanan, On symmetric intersecting families**,
  [arXiv:1702.02607v8](https://arxiv.org/pdf/1702.02607v8), 9 June 2022,
  Section 4, p. 12, observation preceding Lemma 4.1 and its proof.
  For a finite Abelian group G, a set S satisfies S-S=G exactly when
  its translate family is intersecting. The first part of Lemma 4.1
  uses these translates to obtain a symmetric intersecting family;
  the prime-order hypothesis is required only for the reverse comparison
  of the two minimum-uniformity quantities. The complete proof was read,
  including that reverse case, to avoid incorrectly imposing primality
  on the construction at order eight. It does not prescribe the seed
  A={0,1,2,4} or assert the required doubled example. Its orbit size,
  exact degrees and doubled matching number still need local checking.

## Decision and bounded mathematical test

The first two sources are supporting results; neither matches the full
triple assertion. The third supplies a known construction to specialize.
Import its translate/intersection equivalence by citation rather than
reprove it. The necessary local work is the exact small-instance check:
test the proposed seed's difference cover and stabilizer, list its orbit
without repeated edges, check all vertex degrees, and determine the
matching number after taking two copies on disjoint eight-vertex sets.
The seed is a proposed test input, not an inspected source example or a
result established in this literature turn.

If all required counts hold and the doubled matching number is two,
abandon the incidence-only triple implication. That would explain why
L022 cannot be made exhaustive by balanced incidence alone, while leaving
open whether moment-compatible equality families have extra structure.
If the seed fails, record the failing condition; failure does not prove
the triple implication. A bounded check of the other four-subsets of
Z/8Z under the same cited mechanism is within this assessment's scope,
but no repeated broad source search is needed first.

A proof of a triple theorem with additional moment hypotheses would
leave arbitrary-support and parameter-normalization gaps before L022
could yield the global fifteen bound. A combinatorial counterexample
would leave locator splitting, actual nonzero Hankel determinants and
affine-moment compatibility unresolved; it would not give an MCA witness.

No new mathematical result, calculation, lemma or script is produced.
Outcome of the review: EXPLORATION; the known construction and precise
small-instance difference are ready for a separate mathematical turn.
No originality claim is made. No essential source for that test remains
unread; further bibliographic leads are not prerequisites.

## Mathlib

Full sixteen-support statement, the cited matching bounds and cyclic
difference-cover construction: **not checked** in Mathlib. No library
theorem name or absence claim is asserted. The primary citations above
distinguish supporting bounds from the construction to specialize.
