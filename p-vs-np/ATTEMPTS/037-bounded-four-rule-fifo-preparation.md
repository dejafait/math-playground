# Attempt 037 — bounded FIFO four-rule library preparation

The ready implementation target was L106 §6's direct source compiler on
the retained four fixtures. The new primitive-only preparation modules
and strict independent checker are in `scripts/parity-four-rule/`.
The bounded attempt prepared identity but not the next projection;
the compiler was not reached. See the exact budgets, endpoint, counters
and checked partial-archive digest in
`scripts/parity-four-rule/output/first-unprepared.json`, and the concise
report in `drafts/2026-10-24-direct-four-rule-parity-implementation-work.md`.

**WHY IT FAILS.** The declared relevant-subterm FIFO saturation exhausts
its 50,000-record allowance (49,998 records plus two reserved completion
slots) after 546,936 cut-pair trials without deriving the exact template
`¬¬(¬A∨¬B)∨A`. Only 1,253 queued records have been processed when its
generated frontier fills. All retained records are independently legal;
their last endpoint is not the requested one. This is a resource-limited
search failure, not a counterexample to canonical L109's known fixed-library
existence/effectivity or L106's conditional construction. Preserve the
archive and stop FIFO rather than silently normalizing its endpoint or
increasing its caps. A different bounded goal-directed preparation tactic
on this exact saved projection is an independently checkable next test
within the same approved implementation scope. No fixture compiler, H
integration, all-size bound or SAT conclusion has been verified.
