# Current checkpoint

STATUS: IN_PROGRESS
STEP_ID: 2026-09-25-12-tseitin-er-row-addition
STEP_OUTCOME: ADVANCE
STEP_EVIDENCE: lemmas/L012-tseitin-er-row-addition.md constructs legal ER parity-row additions and O(n² log n)-bit refutations of L010's family, hence O(N²) in binary input length; the family cannot provide superpolynomial ER lower bounds.
Bottleneck: No polynomial-time SAT algorithm or unconditional NP language outside P is established. The proof route still lacks both superpolynomial ER lower bounds and a justified global transfer from arbitrary polynomial-time SAT decision to polynomial ER proofs.
Route decision: The bounded parity certification is complete. Keep the automatic trace-to-ER shortcut stopped; isolate the remaining soundness-proof requirement by testing a conditional specialization from L011's explicit soundness CNFs.
Exploration turns used: 0
Next action: Construct the specialization from an ER refutation of L011's H_(A,N) to an ER refutation of each length-N CNF F rejected by A, and bound its overhead while retaining short soundness proofs as an explicit hypothesis.
