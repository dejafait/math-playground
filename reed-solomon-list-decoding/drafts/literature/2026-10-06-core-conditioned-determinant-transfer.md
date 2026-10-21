# Core-conditioned determinant transfer — completed source comparison

TARGET: Assess a core-conditioned supersaturation transfer of L020's forbidden nonsingular triples from 7-subset links to 68-agreement support families.
CHECKED: 2026-10-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched weighted link supersaturation, high-dimensional Hoffman links, recursive theta with packing/forbidden intersections and sparse-intersection supersaturation; inspected the primary passages below and searched local assessments, histories and ATTEMPTS for duplicates.
SOURCE_EVIDENCE: Read Karamanlis–Dodos, Forum Math. Sigma 13 (2025), e99, Theorem 9.1, Corollary 9.2 and the proof's three-part outline, printed pp. 23–24; read Castro-Silva et al., Combinatorica 43 (2023), 909–938, equation (2), Definition 1.1, Theorem 2.1 with its full proof, Corollary 2.3, Theorem 3.1's statement/discussion and Section 5's averaging argument. Reused the old global-source comparisons.
COMPARISON: The inspected supersaturation theorem counts pairs and has a mandatory large-parameter condition, so it does not supply labeled triple supersaturation on the 7-layer. Recursive theta accepts unit vertex weights without edge-induced uniformity, but no computed local cap or global threshold certificate follows here.
GAP: Joint pair/triple specialization, exact core-incidence normalization and a sufficiently small quantitative local certificate remain unproved. No inspected result supplies the numerical saving or uniformity across cores.
REASON: Park direct supersaturation import and select a separately assessed pair-plus-recursive-theta reduction; its source coverage supports a bounded soundness/strength test, not numerical optimization or RS safety.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED; local-link supersaturation and cardinality transfer were essential missing coverage beyond the old direct global comparison.

## Initial proposal and test (retained; assessment completed below)

The main gap is arbitrary-center safety at 68 agreements. The proposed
intermediate target concerns links obtained by fixing a 61-subset C of H
and writing a selected 68-support containing C as C union A, with
|A|=7. The source review should look for a finite supersaturation or
weighted extremal statement that uses L020's actual labeled forbidden
triples, not exclusion of every triple with that intersection pattern.
It must separately address the cardinality transfer over cores. This
formulation is a proposed route, with no new derived bound.

Specific new idea: isolate a single core before choosing a measure or
counting forbidden triples, then test whether an inspected local-link
bound can be summed over cores. The old review tried direct global
68-set theorem import and left measure conversion unproved; that stop
is preserved. The local-link formulation may fail for the same reason
or be too weak. Primary theorem hypotheses, all essential cases and
explicit finite bounds must be read before any dependent calculation.

Continue only if a primary result or a documented uncovered intermediate
target supplies an independently testable local-link restriction with a
justified cardinality transfer and a concrete strength test against
T=65537^28/2^128. Reject direct import if it requires excluding allowed
antipodal triples, generic evaluation points, unproved uniformity, or
has no applicable transfer. Do not equate a source failure with a
disproof of the RS target. No spectrum, count or new lemma is approved
by this proposal.

Essential inputs: L001, C001a and L020; the old extremal assessment
records the relevant source comparisons and the universal-exclusion
stop ATTEMPTS/010. Preserve L021–L026 and ATTEMPTS/017–018 as independent
support-relaxation evidence. Selected supports allow extra agreements,
and the bound must cover whole tuples for every m>=1. Unknowns remain
the local quantitative restriction, global transfer, exact packing and
conditional maxima, full-SDP feasibility, list realization, sharpness,
67-agreement safety and ABF equivalence. Full matching Mathlib coverage
for the proposed transfer is not checked. The required literature-only
review is completed below; no new result is derived in this turn.

## Inspected primary comparisons

Miltiadis Karamanlis and Pandelis Dodos,
[Forbidden sparse intersections](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A26EB22B5CD8BD135BFCBABE4BC3AFD1/S2050509425100674a.pdf/forbidden_sparse_intersections.pdf),
final published version, Forum Math. Sigma 13 (2025), e99,
DOI 10.1017/fms.2025.10067, printed pp. 23–24. Theorem 9.1 assumes
positive integers ell<k<=n/2 and
10^5 sqrt(k)(ln n)^(3/2)<=delta<=min(ell,k-ell).
Under the product-density hypothesis (9.4), with epsilon(delta) defined
in (9.3), it gives an exp(-delta) lower bound for the normalized number
of ell-intersection pairs between the k- and (n-k)-layers. Corollary 9.2
is the equal-k-layer version; its proof complements one family and
replaces ell by k-ell. The proof outline conditions on 2ell-sets and
tracks intersection sizes, not determinants.

These are pair-count conclusions, requiring an additional labeled triple
argument even if applicable. The mandatory delta interval is unavailable
for n=963,k=7,ell=2: its lower endpoint already exceeds its upper endpoint
2. This is a source-hypothesis comparison, not an obstruction theorem for
RS safety. No epsilon expression is applied. The remaining supersaturation
proof was not needed for this rejection.

Davi Castro-Silva, Fernando Mário de Oliveira Filho, Lucas Slot and Frank
Vallentin, [A Recursive Theta Body for Hypergraphs](https://link.springer.com/content/pdf/10.1007/s00493-023-00040-9.pdf),
Combinatorica 43 (2023), 909–938, DOI 10.1007/s00493-023-00040-9,
final published version. Equation (2), p. 911, Definition 1.1, p. 912,
Theorem 2.1 and its full proof, pp. 915–916, and Corollary 2.3, p. 917,
supply an arbitrary-vertex-weight framework; exact statements are in
[the source note](../../foundations/07-core-conditioned-theta-source.md).
Unit weights remove the induced-measure coverage obstacle at this level.
Theorem 3.1's statement/discussion, p. 921, explains the distinction;
its spectral proof is not imported. Section 5, pp. 926–927, permits
averaging only over actual objective-preserving automorphisms. No
transitivity on cores is assumed. Theorem 2.5's weak-optimization statement
and initial induction, pp. 918–919, were read, but its full proof is not
imported and no practical or exact numerical solvability is inferred.

## Local checks and continuation

Read L020's full criterion/examples, L001, C001a, ATTEMPTS/010, history/040
and the old extremal assessment. Targeted searches found no completed
core-conditioned theta model or transfer. Reuse the earlier Hoffman,
whole-triangle and pair-forbidden-intersection comparisons. The antipodal
counterexample remains allowed, and a distance-only witness is not
automatically feasible in a model retaining the subgroup labels.

The narrower proof attempt is scoped in
[its assessment](2026-10-06-core-conditioned-pair-theta-reduction.md).
Joint-lift soundness and incidence transfer must be proved next turn;
neither is silently imported. This new ready continuation receives separate
supervisor approval next turn. No lemma, mathematical script, DAG edge or
PROOF argument changed. The bracket remains 955–957. The proposed model
has no established numeric cap, optimum or actual list realization.

Queries used: `"supersaturation" "links" "weighted" hypergraph Hoffman
bound`; `"high dimensional Hoffman" "independent" "links" hypergraph`;
`"supersaturation" "forbidden intersections" uniform families quantitative`;
`"A Recursive Theta Body for Hypergraphs" arxiv`; `"Karamanlis" "Dodos"
"Theorem 9.1" supersaturation`; `"recursive theta" "packing" hypergraphs`;
`"recursive theta" "forbidden" "intersections"`. Finite-field collinearity
and packing searches produced no inspected matching transfer. Unrelated
incidence/container hits remain unread leads. Search failure is not novelty.
