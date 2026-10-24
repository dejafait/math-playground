# Attempt 038 — bounded goal-directed four-rule preparation

The different backward AND/OR tactic for the approved L106 source-only
implementation target also stops before the first projection. Exact
bounds, search limitations, and the fully independently checked partial
archive are recorded in
`scripts/parity-four-rule/output-goal-directed-447/first-unprepared.json`
and `drafts/2026-10-24-direct-four-rule-goal-directed-work.md`.

**WHY IT FAILS.** The finite target-subterm/negated-subterm pivot tactic,
with a 24-node formula cap, reaches depth 10 after 52,398 search states
without the exact `¬¬(¬A∨¬B)∨A` endpoint. Its 98 retained records are
legal primitive records, but do not prove that template. This is an
incomplete search failure, not a lower bound or counterexample to L109;
no claim of exhaustive proof-height search is made. Both this tactic
and FIFO Attempt 037 have now failed the same discriminating preparation
test, leaving 1/72 prepared library proofs and 0/4 source fixture streams.
Park concrete preparation, preserve all archives, and change to a
supplied-proof extraction test that does not depend on library synthesis,
subject to separate implementation-scope coverage approval. No H,
all-size implementation, general short-proof or SAT claim follows.
