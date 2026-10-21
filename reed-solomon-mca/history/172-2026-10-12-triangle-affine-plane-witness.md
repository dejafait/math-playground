# 2026-10-12 — Balanced triangle witness

The approved SPECIALIZE target has a complete affirmative witness in
[L072](../lemmas/L072-triangle-balanced-linear-support-witness.md),
obtained from the cited affine plane with four selected classes and
an explicit nonconcurrent triangle relabeling. This is a reproduction
of known design mathematics with a verified notebook specialization,
not progress beyond the checked sources. It supplies informative
negative evidence for useful-pair forcing from balance and the fixed
triangle alone; all additional pairs have union seven or eight.

The full supplementary certificate is
`scripts/triangle-incidence/affine-plane-certificate.json`; the analytic
proof covers all pair cases without relying on computation. The stop is
recorded in [ATTEMPTS/027](../ATTEMPTS/027-triangle-balance-only-useful-pair-forcing.md).
PROOF.md now records this argument change and DAG.md adds only L072,
with no local mathematical input (L057 supplies naming/motivation).
Prior work and stops are preserved. Uniform triangle twelve, actual
moment realization, arbitrary extraction and challenge qualifications
remain open, with no change to 11/q–16/q.

The sole continuation proposes a different, moment-compatibility
mechanism for this family; its assessment is REVIEW_REQUIRED in
`drafts/literature/2026-10-12-affine-plane-equality-realization.md`.
No new realization mathematics or approval was attempted here.

Validation: the supplementary check passed all sixteen block/degree
requirements and all 78 additional-pair checks, with maximum
intersection one against the required upper bound one and no failures.
Scoped documentation validation passed: 74 nodes, 150 edges, acyclic
and complete local coverage. The overview was compacted to 100 lines
without removing mathematical content.
