# Step 446 — bounded direct four-rule implementation

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-24-direct-four-rule-parity-implementation-coverage.md`.
The target remains its exact TARGET. Main gap: unrestricted SAT decision
or separation. Intermediate threshold: independently checked complete
exact-¬F primitive streams for the four retained fixtures. Downstream:
concrete source-interface verification before any occurrence/H integration.

Inputs inspected: L106 hypotheses and §§6–7; L109 §§1–3; L108 exact
syntax; L097 §§6.1–6.3; Attempt 036; retained fixture definitions.
No source refresh, new completeness claim, or old implication-only
synthesizer is used. Existing changes and old streams remain intact.

Preparation tactic: bounded forward primitive saturation over the exact
target's subterms and their negations, plus true/false; expansion images
come from that fixed relevant pool. Contraction, directed association and
cut are literal. This is an incomplete resource-bounded search, not a
new completeness algorithm. Each stored record is a primitive inference.
Prepare the complete fixed union manifest before receiving any fixture.

Declared search bounds, before execution: 50,000 stored records,
1,000,000 eligible cut pairs and 15 seconds per template; 250,000 stored
records, 5,000,000 eligible cut pairs and 90 seconds for the library.
Formula size bound per template: max(16, target nodes + 8). Stop at the
first unprepared template and save its exact target, search state,
bounds and reason. Do not replace the endpoint or add a rule. A failed
bounded saturation does not imply nonderivability. If preparation fails,
the compiler is NOT_REACHED; preserve all four inputs and independent
checker self-tests, and do not report fixture success.

Remaining obligations: implement/run preparation and independent strict
checking, then compile fixtures only if preparation completes. No H,
L087 provenance, original M/Q bound, all-size implementation bound,
general short proofs, universal W₂ or SAT conclusion is supplied.

## Completed bounded attempt

Run: `python3 scripts/parity-four-rule/run.py`. New modules are
`scripts/parity-four-rule/prepare.py`, `checker.py` and `run.py`;
the independent checker imports no emitter or old checker. The old
`scripts/parity-source/` implementation and outputs were not edited.

The fixed manifest has 72 expanded endpoints: 20 from L097 §6.1,
14 additional non-row endpoints from L106 §6.2, and 38 row endpoints.
The latter include both rhs bits, arities zero through three, and all
independent binary disjunction shapes of the canonical clauses. The
generator exhaustively Boolean-checks each endpoint over its slots.
All additive/Boolean abbreviations are expanded literally, with no
constant simplification. This manifest check is not a primitive proof.
See `scripts/parity-four-rule/output/library-manifest.json`.

Identity has a complete independently accepted 13-record primitive
archive. The first nontrivial template, projection-left, is unprepared:

    ¬¬(¬A∨¬B) ∨ A.

This is exactly `(A∧B)→A` under the fixed expansions. The FIFO search
stopped at its storage limit after 49,998 retained records, reserving
two of the 50,000 slots for the legal expansion/contraction that restores
a successful endpoint last. It tried 546,936 cut pairs against the
1,000,000 cap, processed 1,253 records, and retained formulas of at most
17 nodes (the declared `max(16, target nodes + 8)` cap). The time cap did
not bind. Its complete 6,452,342-byte archive, including unused records,
was independently checked: 35,550 cuts, 13,578 expansions, 855 directed
associations, 13 propositional axioms and the two ground axioms. This
checks the actual last formula, explicitly **not** the requested
projection endpoint. No endpoint replacement or extra primitive was used.
Exact target, pool, bounds, counters and complete-check digest are in
`scripts/parity-four-rule/output/first-unprepared.json`; the full partial
archive is `output/projection-left-preparation.jsonl` in that directory.

The separate nine-record checker exercise uses every primitive tag.
All 20 saved corruptions reject, covering each rule's arguments,
association direction, constants, wrong/forward/out-of-range/Boolean
references, reference arities, MP/assumption/context tags, malformed
syntax, alphabet and header/final endpoints. The last-endpoint corruption
appends a valid true axiom, so its rejection specifically tests the final
endpoint check. Complete results are in
`scripts/parity-four-rule/output/checker-results.json`.

All four old fixture JSON inputs were copied byte-for-byte and read back.
The independent checker reconstructs canonical clauses from the rows,
checks supplied λ and clause occurrences/order, and reconstructs their
actual global trees. Its exact endpoints agree with a separate emitter
reconstruction; the three-row endpoint has 45 nodes and retains
`[[0,[1,2]],[[3,4],5]]`. These are input checks. The compiler was not
reached: **0 of 4 required complete fixture streams**, and only **1 of 72
required library proofs**, were produced. Summary and paths are in
`scripts/parity-four-rule/output/summary.json`.

Outcome: EXPLORATION / RESEARCH / REPRODUCTION. The implementation tests
known L109 preparation and L106 §6 interfaces; it establishes no result
beyond the sources checked. Primary completeness input remains Shoenfield,
*Mathematical Logic* (1967), §2.6 pp.21–22 and §3.1 pp.27–30, as imported
and specialized in canonical L109 §§1–3. No external source review,
new completeness proof or new mathematical lemma was performed. Mathlib
matching remains unchecked and supplies no executable certificate here.

Stop this FIFO tactic; its frontier fills before even the first projection
is reached. This is not evidence of nonderivability or of infeasibility
of all finite-library preparation. One mathematical EXPLORATION turn is
used. The unchanged ready assessment permits a different bounded
preparation tactic for the same exact implementation target next turn:
goal-directed backward primitive synthesis, testing this saved exact
projection before the full manifest. Do not rerun FIFO or merely enlarge
its caps. Continue only on complete primitive exact-endpoint certificates;
park concrete preparation if the blocker persists under a different tactic.
H integration, short source-proof availability, M-only bounds, universal
W₂, arbitrary ER data and unrestricted SAT remain unresolved.
