# 2026-10-25 — Endpoint-pair count and deletion diagnostic

Completed the unchanged EXPLORE-approved target with L123, using L122's
matching-line histograms and audited C122a. Full proof and qualifications:
[L123](../lemmas/L123-certified-endpoint-pair-maximum.md). Complete evidence:
`scripts/finite-support/endpoint-pair-count.json` and its saved inputs/counts.
All 1023 ratios were enumerated with both endpoint-placement cases; the
maximum is 67798380, attained exactly by antipodal pairs. Four exhaustive
small-field comparisons, both placement sums, the unordered-pair total,
inverse symmetry and complete ratio coverage pass without failures.

The Bonferroni diagnostic gives a nontrivial uniform upper bound on full
configurations avoiding a 61-point core. Its proof distinguishes that
upper bound from the singleton union-bound lower bound. This is local
mathematical progress, not a new general incidence theorem or a resolution
beyond the checked sources. POTENTIALLY_NEW records only the bounded
search's lack of a matching theorem. The 955–957 bracket is unchanged;
selected-family transfer, threshold saving and the ABF comparison remain
open. Existing unfinished L121 and other work was preserved.

Continuation test passed: complete count is tractable and the diagnostic
improves the singleton-incidence upper bound. Next route is separate
approval for a critical audit of this new input, with REVIEW_REQUIRED
assessment `drafts/literature/2026-10-25-l123-critical-audit-coverage.md`.
No new continuation was researched or self-approved in this turn.
