# 2026-10-26 — Retention-to-overlap bridge counterexample

STEP_ID: rsld-2026-10-26-505-zero-overlap-retention-counterexample

Completed one mathematical alteration test under the prior SPECIALIZE
[assessment](../drafts/literature/2026-10-26-threshold-retention-ambient-overlap.md).
[L130](../lemmas/L130-zero-star-overlap-retention-counterexample.md)
records the full proof and citation: the allowed right-dummy branch
gives zero common ambient-star overlap, yet finite averaging and
one-sided conflict deletion retain 2552584 left supports and at least
2346329 right supports with the required pair-intersection bound.
This is new negative evidence against the proposed forcing bridge,
not a disproof of RS safety or a novelty certification. No new source
review was needed; standard alteration tools were reused.

The exact certificate is
`scripts/finite-support/threshold-retention-alteration.json`.
All eleven arithmetic checks passed; complete intersection probabilities,
expectation, retained bounds and check fields were inspected. The
conditional sample-space, finite-averaging and packing arguments are
canonical in L130; arithmetic checks alone are not a critical audit.
The DAG's direct inputs are exactly L030 and L125, both used in the
proof. Existing L126/L129 obstructions are contrasts, not premises.

Decision: abandon retention alone as the missing overlap-forcing
bridge under these hypotheses; preserve that failure in ATTEMPTS/106
and seek separate critical audit of L130 after coverage approval.
The audit assessment is REVIEW_REQUIRED, not approved in this turn.
The main arbitrary-center 67/68 gap and bracket 955–957 remain open;
global compatibility, prescribed laws and RS realization are untouched.
All preexisting unfinished work is preserved.

Scoped documentation validation passed: 137 nodes, 499 unique edges,
acyclic graph, complete lemma coverage and valid links. The overview
was shortened to its required byte limit; full reasoning stays in L130.
Notebook-scoped `git diff --check -- .` also passed.
