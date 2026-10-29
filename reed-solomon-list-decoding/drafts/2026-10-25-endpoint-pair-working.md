# Endpoint-pair attempt checkpoint

Approved target and scope: the unchanged EXPLORE assessment
`literature/2026-10-25-endpoint-pair-incidence-count.md`.
Main gap: arbitrary-center 67/68 safety. Intermediate target: exact maximum
of the two-endpoint count in C122a. Possible use: Bonferroni upper bound
on whole-domain configurations avoiding a 61-point core, not a list bound.

Working reduction (not yet certified): fix a=1 by multiplication in H.
For A={1,x}, same-edge contribution is the sum over eligible lines through
A of 3(r-1)(r-2). For disjoint B={b,c}, its unique line with A contributes
6(r-2) to each of the different-edge counts at b and c. L122 makes all
eligible lines matchings. Read occupancy from the audited histograms using
the proved slope transport. All x!=1 and all disjoint B are enumerated;
vertical and horizontal lines are explicit. Expected checks: sum same=6T/n,
sum different=24T/n, inverse-ratio invariance, exhaustive small instances.
No new global incidence theorem is needed or claimed.

Cost: at most (n-1) binomial(n,2) pair-line trials plus (n-1)(q+1)
same-edge line queries; about 603 million simple exact queries total.
Use compiled integer arithmetic with all modular products widened.
Continue if full coverage and diagnostic improvement certify; otherwise
preserve the failure. Core transfer, selected-support supersaturation,
RS realization, threshold saving and ABF comparison remain unresolved.

Completed: L123 is now the canonical proof. All 1023 ratios give maximum
67798380, uniquely at -1; same/different counts and Bonferroni arithmetic
are certified in `scripts/finite-support/endpoint-pair-count.json`.
No sampled maximum is used. The separate critical-audit continuation is
REVIEW_REQUIRED; this working note grants no additional approval.
