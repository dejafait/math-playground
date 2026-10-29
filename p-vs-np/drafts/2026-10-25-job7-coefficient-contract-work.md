# Step 498 — coefficient contract work checkpoint

Approved target: prove soundness and state the full evidence/resource contract
for the separate fixed job-7 F₂ interface. The prior SPECIALIZE assessment is
`literature/2026-10-25-job7-coefficient-certificate-soundness.md`.

Read L035 in full; inspected L036 (5)–(9), L038 endpoint/splitting/gadget/right
closure, L055 §§2–3, L097 §§22–23, L108 §§11,13 boundary passages, and the
job reconstruction/copy checks in `receive_forward_job7.py`. Reused step 496's
primary-source comparison and Attempts 042–045; no source refresh or code
execution of stopped arithmetic. Existing unfinished work is preserved.

Planned sufficient certificate: for each independently transported difference
automaton (alpha,M,beta), supply B,c,T_a with alpha=cB, BM_a=T_aB,
B beta=0. Full rank and reachable-space equality are unnecessary for this
one-way implication. Import Kiefer's invariant-space semantics and give the
specialization/word induction, not a new PIT algorithm. Right closure:
K=(I+E0+...+E0^(N-1)), alpha=e_s K, M_a=E_a K, beta=e_t.
Check K=I+E0 K uniquely in a topological order. Never mix this with L055's
left closure. Empty word and r=0 must be explicit.

Pending: independently build ordered L035 reference from original operands;
three difference modes plus axiom-reference versus fg+gf; exact framing,
evidence/transport/work ledger and bounded later preflight. No finite equality,
rank, cap fit or implementation has been established. If any transport cannot
be checked from fixed bytes, save the precise gap instead of claiming success.

Completed: canonical specification and proof are in
`../lemmas/L110-job7-coefficient-certificate-contract.md`. It avoids a dense
closure oracle by checked topological row actions and specifies four separate
differences, including the ordered commutator. All pending specification
items above are written there; finite feasibility and implementation are
still unperformed. The next scope assessment is REVIEW_REQUIRED for a
separate critical audit. No stopped expansion was rerun and no old artifacts
were changed.
