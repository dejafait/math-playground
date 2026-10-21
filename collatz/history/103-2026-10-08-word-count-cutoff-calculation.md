# 103 — 2026-10-08: fixed word-count cutoff calculation

STEP_ID: collatz-2026-10-08-103-word-count-cutoff-calculation

[L043](../lemmas/L043-postspell-word-count-cutoff.md) excludes actual
closed concatenations for every 3<=r<=12. It retains L041's positive
linear form as well as the fixed length inequality and the cited
primitive odd-count threshold. An all-real monotonicity proof and
[exact certificate](../scripts/postspell-word-count/cutoff-certificate.json)
give the exclusion; all 23 checks passed. A scalar integer count tuple
at r=13 satisfies every explicitly retained comparison restriction.
Thus 12 is maximal for that specified initial scalar range, without
asserting any actual word or cycle at 13 or optimality among other bounds.

ADVANCE, RESEARCH/REPRODUCTION, actual task calculation, under the
unchanged pre-invocation SPECIALIZE
[assessment](../drafts/literature/2026-10-08-postspell-word-count-cutoff.md).
This is local optimization/application of known estimates, with no
claim of a new general theorem or progress beyond checked source
mathematics. The [working record](../drafts/2026-10-08-postspell-word-count-calculation.md)
preserves the early reasoning. Only direct input L041 is added to
the DAG; L042's audited applicability is a comparator. PROOF.md now
assembles the new restricted result and its limitations.

The [proposed critical-audit assessment](../drafts/literature/2026-10-08-word-count-cutoff-audit.md)
is REVIEW_REQUIRED for separate next-turn approval. The new result
awaits that independent audit; source-computation qualifications,
Attempt 019 and history 069 are preserved. Universal eventual descent,
entry, unrestricted counts, other cycles and divergence remain open.
This calculation is not an EXPLORATION turn; no supervisor counters,
scheduling state, shared infrastructure or other notebooks were edited.

Scoped documentation validation passed: 43 nodes, 58 unique edges,
acyclic DAG, complete file coverage, valid local links and compact
overviews. The sole new mathematical edge is L043: L041; the period
and positive-linear-form arguments genuinely use that all-r input.
Structural validation is not the pending mathematical critical audit.
