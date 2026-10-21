# Approved uniform-cap attempt — working record

The unchanged EXPLORE assessment is
`drafts/literature/2026-10-06-core-theta-uniform-cap.md`.
Main gap: arbitrary-center 68-agreement safety. Target: beta_C<1532496
for every 61-core in L027. An above-threshold feasible shared lift is
an explicit abandonment test in that assessment; it concerns the
relaxation, not unsafe lists. L020's singular triples remain allowed.

Candidate obstruction, saved before verification: on 959 of 963 abstract
points use seven groups of 137 points. Graphs of all degree-at-most-two
polynomials over F_137, evaluated at seven distinct field elements,
give 137^3 seven-subsets intersecting pairwise in at most two points.
Average indicator outer products over all bijections to H minus C.
This preserves pair zeros and PSD without claiming these bijections
preserve the labeled hypergraph. Validate the link constraints directly.

Every B in W_A has |A intersect B|=2. Partition W_A by that pair;
the 21 parts are independent because a link edge requires empty triple
intersection. Therefore the constant vector 1/21 is in IND of the link.
The averaged row ratio should be 136/binomial(956,5), obtained from
21*136 codewords at exactly two agreements with a fixed quadratic.
Check the conditional orbit count, the scaling against 1/21, the whole
shared matrix and every core. If these pass, the cap is false for the
stated model even though neither actual list realization nor safety is
decided. No PSD matrix is to be approximated numerically.

Completed: the candidate passed. The canonical proof and qualifications
are in L028; the exact arithmetic certificate is
`scripts/finite-support/core-theta-obstruction-results.json` (11/11
checks, no failures). This working record is superseded by that proof.

Ready source coverage supplies indicator inclusion/convexity and
weighted supporting inequalities. This witness tests that exact model;
it introduces no extra hierarchy or determinant exclusions. No matching
local construction was found in the targeted L020–L027/core-assessment
search. Novelty is not established. Independent gaps include actual
packing realization by messages, the 67-agreement boundary and ABF
comparison.
