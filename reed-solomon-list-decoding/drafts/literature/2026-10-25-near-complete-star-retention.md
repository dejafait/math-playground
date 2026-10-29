# Near-complete-star retention — completed source and scope review

TARGET: Assess whether L127's ambient-star equality lets L126's forbidden-pair matching exclude two compatible retained subfamilies of size at least 1532496 when their retained common star has at least 18633 supports.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the bounded matching, cross-intersection and polynomial-family searches recorded in 2026-10-25-two-core-full-star-thinning.md and the partial-isomorphism searches in 2026-10-25-near-complete-common-star-rigidity.md; targeted local checks read L126 in full, L127 hypotheses/conclusion, L125 scope, ATTEMPTS/105 and the relevant working/audit records. No existing incomplete-star retention theorem was located in those records; no fresh external search was needed.
SOURCE_EVIDENCE: Reused König (1931), authorized translation arXiv:2009.03780v1, unnumbered main theorem PDF p. 3 and graph proof pp. 1–2; Wang–Zhang arXiv:1101.2257v1 Theorem 1.1 p. 5; Borg–Feghali arXiv:2012.15356v2 Theorem 1 p. 3, as inspected in the full-star assessment. Audited L127 supplies ambient-star equality; audited L126 supplies the explicit nonstar bijection and conflicts under its stated hypotheses.
COMPARISON: L126's structural correspondence uses equality of ambient full stars; its final count explicitly uses full retention. L127 covers the changed overlap-to-ambient-equality step. General matching theory needs no undeletable star vertices, but does not certify the present retained-size claim; adapt the explicit matching count rather than invoke L126's full statement outside its hypotheses.
GAP: Verify the transfer from retained common supports to L127's ambient-overlap hypothesis, the ambient-only applicability of L126's nonstar pairing, and a valid retained-star contribution to the size sum; compare the resulting bound with two sizes of 1532496. No incomplete-star retention conclusion is established in this review.
REASON: The changed retention hypothesis has now been compared with the canonical proof and reusable sources. A bounded specialization is justified; the new applicability and counting steps must be proved in a later research turn rather than silently importing L126's full-retention conclusion.

## Exact proposed scope

Use L030's quadratic families and L127's q=137, unchanged seven-point
T, two 61-cores C=K union {a}, C'=K union {b}, and arbitrary ambient
bijections, with the left distinguished column 16. Consider retained
subfamilies of those full families. Require equal selection indicators
for all 68-supports containing K,a,b, at least 18633 such retained
supports, and intersection at most 63 for every two distinct retained
supports in the union. Equal supports are identified. Both retained
sizes are proposed to be at least 1532496. No probability laws or RS
realization are assumed, and no full-star retention is assumed.

The review should narrowly inspect L126's canonical matching proof and
reuse its source assessment plus the audited L125/L127 statements.
Determine whether existing coverage suffices for this exact specialization
and record precise imports and remaining applicability obligations.
Do not assume equality of ambient stars means all their supports are
retained. L030, L125, L126 and L127 are the intended local inputs; no
cross-notebook input is proposed. Mathlib coverage is not checked.

The main gap is still arbitrary-center 67/68 safety and bracket 955–957.
This proposed intermediate target tests robustness of the exhausted
full-star-preserving repair, under an explicitly weaker retention
hypothesis made accessible by L127. ATTEMPTS/105 remains valid evidence.
Continue only if the source comparison identifies a justified matching
specialization or another precise missing implication; if the matching
needs a full retained star, record that obstruction rather than silently
adding the hypothesis. Lower retained-star counts, arbitrary local laws,
global compatibility and actual RS lists remain independent gaps.

## Completed comparison and approved mathematical test

L126's proof separates the roles of its hypotheses. Its paragraph “Why
the audited rigidity applies after thinning” invokes equality of the
ambient full stars to obtain the arbitrary-label correspondence (1).
The polynomial maps (2) and (3), and the forbidden-pair verification,
are then formulated on ambient nonstar indices. Its “Disjoint-edge
counting” paragraph counts retained vertices of those pairs. Only its
subsequent star contribution explicitly counts every star member as
retained. This is a comparison of the existing proof's uses, not a proof
that the altered retention claim follows.

L127's audited statement concerns intersection of ambient stars, without
assuming packing or retention. The next attempt must justify that the
specified retained common supports qualify for that statement, invoke
its conclusion, and check every needed hypothesis of the structural
part of L126. It must not invoke L126's conclusion by name as though
its full-retention hypothesis had disappeared. The new difference is
the retained-star count and its combination with the existing matching.
No new classification, approximate-homomorphism theorem or matching
algorithm is proposed.

The existing [full-star source assessment](2026-10-25-two-core-full-star-thinning.md)
records the complete inspected primary statements. In particular,
König, *Graphok és matrixok* (1931), authorized translation *Graphs and
matrices*, [arXiv:2009.03780v1, unnumbered main theorem, PDF p. 3](https://arxiv.org/pdf/2009.03780v1),
identifies maximum matching size with minimum vertex-cover size for
finite bipartite graphs. Its graph proof, pp. 1–2, handles the required
finite setting without regularity or transitivity. The next attempt
needs only the elementary count from explicitly disjoint conflict edges;
there is no reason to reprove König or solve a general matching problem.
The part-transitivity and primitive-fragment hypotheses of Wang–Zhang,
[arXiv:1101.2257v1, Theorem 1.1, p. 5](https://arxiv.org/pdf/1101.2257v1),
remain unverified for these arbitrary labels. Borg–Feghali,
[arXiv:2012.15356v2, Theorem 1, p. 3](https://arxiv.org/pdf/2012.15356v2),
still concerns a lower cross-intersection condition, rather than this
upper intersection restriction. Neither supplies a numerical bound here.
These source comparisons are reused, not new primary-source inspections.

The [near-complete-star assessment](2026-10-25-near-complete-common-star-rigidity.md)
covers the earlier completion problem; its finite-group stability import
has already been used and separately audited in L127. Reuse L127 as an
established local input, without repeating its proof or browsing its
optional unread automorphism leads. No essential source is blocked for
this deterministic specialization. ATTEMPTS/105 remains the valid stop
for the full-star repair, not a ban on this changed overlap hypothesis.
The local working records and L126 audit coverage contain no already
proved incomplete-star retention result.

SCOPE: Exactly TARGET with the stated q,T, cores, arbitrary bijections, left column 16, equal retained common-support indicators, at least 18633 retained common supports and intersection bound 63; one symbolic specialization through overlap transfer, ambient rigidity, explicit nonstar matching and retained-star counting. No lower overlap, arbitrary law, different left column, global extension or RS realization.

Continue if those checks yield a rigorous retained-size obstruction
below the required two-sided threshold. If the pairing actually needs
retention rather than ambient equality, or if the resulting valid bound
fails to exclude both sizes, record that precise failure and abandon
this matching as sufficient evidence for the target. Do not infer a
realization from failure to exclude it. Any completed specialization
will need a separate critical review. No new retention theorem,
inequality, arithmetic certificate, lemma or mathematical script was
produced in this literature turn.

Mathlib: full instance coverage and matching support remain not checked;
unknown availability is not evidence of absence. PROOF.md and DAG.md
are unchanged because this review does not change the mathematical
argument. This assessment approves a later attempt, not its conclusion.

