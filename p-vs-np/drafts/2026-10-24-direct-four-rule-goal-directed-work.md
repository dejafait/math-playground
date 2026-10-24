# Step 447 — bounded goal-directed primitive preparation

Main gap: unrestricted SAT decision/separation. Approved intermediate target:
implement and independently check L106 §6's direct four-rule source compiler
on the retained three-row and zero-row fixtures. The unchanged step-445
SPECIALIZE assessment is reused. Inputs are L106 §§6–7, L109 §§1–3,
L108 exact syntax, L097 §§6.1–6.3, and the preserved step-446 artifacts.
Shoenfield, *Mathematical Logic* (1967), §2.6 pp.21–22 and §3.1 pp.27–30
is imported through audited L109; this implementation does not reprove
completeness or introduce a mathematical lemma. Mathlib matching is unchecked.

Downstream use: test the conditional source interface before occurrence/H
integration. Full threshold: all 72 whole fixed-library proofs and all four
exact-¬F primitive fixture streams, independently checked, with corruptions
rejected. A saved projection proof alone is only partial preparation.

Discriminating test: a different backward AND/OR search on the exact saved
projection, with semantic rejection of impossible assumption-free premises,
finite subterm/negated-subterm pivots, iterative depth and declared finite
state/time/record/formula limits. Every accepted operation still emits only
a literal primitive rule. Semantic tests never certify a proof endpoint.
The old FIFO search and all its outputs are preserved, not enlarged/rerun.
The budget is saved before search under
`scripts/parity-four-rule/output-goal-directed-447/budget.json`.
Stop at the first unprepared template or exhausted library budget. If this
different tactic is also blocked, park concrete preparation and recommend
a materially different independently testable target for separate coverage
approval. No short-proof availability, all-size implementation bound,
M-only bound, arbitrary ER data, universal W₂ or SAT transfer is supplied.

Unfinished checkpoint: implementation and bounded test follow; no result yet.

## Completed bounded test

The new `scripts/parity-four-rule/backward.py` and `run_backward.py` run
only backward primitive synthesis. Budget: depth at most 10, 60,000
recursive search states and 20 seconds per template, 20,000 retained
records, and formula nodes at most max(24,target nodes+12); global limits
are 200,000 states and 80 seconds. The pivot pool is precisely the target's
subtrees, their single negations, and the two constants. Premise truth
masks enumerate all four valuations of A,B and only prune; success
requires independently checked primitive records. The saved budget
precedes synthesis, and no bound was increased or FIFO fallback invoked.

The exact saved projection `¬¬(¬A∨¬B)∨A` remains unprepared after
52,398 search states and 206,940 considered cut options. All iterative
passes through depth 10 returned without the endpoint; the time, state
and retained-record caps did not bind. This is **not** exhaustive search
of all proofs of height 10: the pivot/formula restrictions omit proofs,
and cached earlier successful derivations may be reused independently
of depth. No mathematical height or nonderivability lower bound follows.
Elapsed synthesis was about 0.53 seconds, versus its 20-second ceiling.

Identity has a new complete five-record archive. Projection preparation
retains 98 records (8,696 bytes): 15 propositional axioms, both ground
axioms, 44 cuts, 34 expansions and three directed associations. The
unchanged independent checker reads and accepts the entire partial
archive at its actual last endpoint; that endpoint is explicitly not
the requested projection. Full record digest, counts, exact target,
pivots and limits are in
`scripts/parity-four-rule/output-goal-directed-447/first-unprepared.json`.
The full partial proof is `projection-left-preparation.jsonl` alongside
that report. No incomplete archive is imported as a library proof.

All 20 saved primitive/reference/syntax/alphabet/endpoint corruptions
reject under the unchanged independent checker. Each old fixture input
is copied byte-for-byte, read back and independently reconstructed;
these input checks do not certify any fixture proof. Thus completion is
still **1/72 library proofs and 0/4 primitive fixture streams**. The
compiler was not reached. Complete per-template reports and concise
actual/required totals are in
`scripts/parity-four-rule/output-goal-directed-447/summary.json`.
Reproduce with `python3 scripts/parity-four-rule/run_backward.py`;
the dedicated step-447 output directory is separate from all old outputs.

Outcome EXPLORATION / RESEARCH / REPRODUCTION. This is a second bounded
preparation tactic with new search evidence, not a mathematical advance
or a new obstruction theorem. Park concrete preparation after the two
unsuccessful tactics; do not rename or enlarge either search. The known
L109 existence/effectivity result and audited abstract L106 construction
remain unchanged. A materially different independently testable component
is L108 extraction on an already checked primitive proof: it receives its
proof rather than requiring any fixed-library synthesis. Its executable
scope is recorded as REVIEW_REQUIRED for a separate literature approval;
no extraction implementation or new mathematical claim is made here.
