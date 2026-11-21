# L842 negative second-ray certificate — audit nomination

TARGET: Independently audit L842's rank-five negative second-ray certificate for the dyadic cubic product, including analytic scope, coefficient recurrences and determinant orientation.
CHECKED: 2026-11-06
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: Nomination only; no new external search. The completed calculation reused the prior SPECIALIZE assessment drafts/literature/2026-11-06-dyadic-cubic-infinite-tail-second-ray.md. Audit-specific source approval has not yet been completed.
SOURCE_EVIDENCE: Previously inspected Macdonald (1995), I.2 (2.4)–(2.6)/(2.9), pp.20–23, I.3 (3.4)/(3.5), pp.41–42, and McMullen notes (2025-12-02), compact-product criterion/Theorem3.1 p.80 and Cauchy formula/bound pp.12–13; reuse the parent assessment's evidence rather than treating this nomination as fresh inspection.
COMPARISON: The known identities and compact convergence cover the methods; the new local rank-five sign specialization needs independent replay of the hypotheses, rectangle orientation, recurrence arithmetic and complete finite certificate. No new theorem or general closure assertion is proposed.
GAP: A separate next-turn source approval must confirm this precise audit scope before mathematical audit. L841's whole first-ray proof, modified products, higher shifts and actual-Xi signs are outside this audit.
REASON: The completed negative calculation is preserved; its critical check is a separate target and is not self-approved in the derivation turn. No essential blocked asymptotic source is implicated.

## Proposed bounded audit

Canonical input is `lemmas/L842-dyadic-cubic-negative-second-ray-minor.md`.
Its only local mathematical input is L841's analytic product setup,
not L841's first-ray sign or L840's finite PF conclusion. Check compact
product existence and F(0)=1 at the exact scope used; full independent
audit of L841 remains a separate question.

Verify that self-similarity concerns the actual compact limit and gives
both exact coefficient recurrences. Check lambda=(r,r), conjugate (2^r),
ordinary coefficients, negative-index zeros and the rank-five matrix.
Check all displayed reciprocal coefficients and the exact negative
fraction. Replay and inspect the load-bearing rational certificate
`scripts/dyadic-cubic/second-ray-exact-certificate.json`, whose script
records every Leibniz term. A matching decimal or finite preview is
insufficient. The proof should need only a small reciprocal disk and a
fixed-rank limit, never a uniform-rank exchange or nonzero-minor division.

Success means validating or repairing that exact local obstruction;
failure means identifying the precise analytic, indexing or arithmetic
error. Neither outcome settles RH. This nomination does not approve
another rank search, pole mechanism, modified dyadic family or Xi
realization attempt. A future genuinely different central mechanism
requires its own exact target and source coverage. Full matching
Mathlib coverage remains unchecked, not absent.
