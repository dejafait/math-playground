# Step 457 — bounded parameterized extraction work

Approved target: implement the supplied literal-four-rule L108 interface under
`drafts/literature/2026-10-24-parameterized-four-rule-extraction.md` (SPECIALIZE).
This is RESEARCH / REPRODUCTION / implementation, not new mathematics.

Main gap: unrestricted SAT decision/separation. Intermediate target: caller-bound,
typed, bounded extraction and complete independent reception of all source roots.
Downstream use: a supplied-proof interface for later conditional compositions;
source-proof availability, library synthesis and unrestricted transfer remain open.
Continue only on complete accepted examples and discriminating malformed inputs;
stop on literal/provenance/name loss, an uncovered correction operand or a cap.
Existing fixture archives 449/451/453/455 and Attempts 037/038 are preserved.

Implementation plan saved before longer work: new strict input module receives an
external request (exact SHA, goal, ordered alphabet, complete supplied dictionary),
preparses duplicate keys/nesting/types/caps before the literal checker, and keeps
symbol namespaces typed. New emitter uses private L035/L036 module instances,
preflights their explicit copies, and attaches every line/transition separately.
New receiver imports neither emitter nor correction code; independent free-word
arithmetic checks block contracts and both identities at every indexed line.
Exact-word arithmetic is a capped diagnostic, not the polynomial construction
algorithm or an all-size verifier. Caps do not bound all interpreter memory.

Final execution evidence and limitations will be added after the bounded test.

Completed implementation evidence is canonical in L108 §10. Reproduction:
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/four-rule-extraction/test_parameterized.py`.
All six accepted inputs / 35 roots pass; all 192 old-fixture complete polynomial
comparisons agree after typed transport; 47 expected malformed/cap cases reject;
one neutral duplicate label passes. Full certificates, all root/block polynomials,
actual/required limits, source/request bytes and script hashes are in
`scripts/four-rule-extraction/output-457/`. All 176 old archive files are unchanged.
The legal original `1` singleton has free output placeholder 0, zero output 0,
and substituted output original-0 plus its square, so the formerly colliding
scalar/name boundary is exercised directly. Atomic or/not and unused originals
are also received in the larger reordered case. No accepted cap is exhausted.

Largest accepted totals are 17,689 records, 223,971 bytes, 45,260 multiplication
pairs, nine words, length four and 4,223 stored table words, below the unchanged
six diagnostic caps. A deliberate synthetic L035 copy preflight rejects
4,000,010 records before copying; other intentional stops retain exact reasons.
The receiver checks complete objects, not a bounded preview. Scripts share only
strict input/symbol helpers and the literal checker; no correction evaluator is
imported into the receiver. Constructor counters remain bounded claims.

Outcome: local implementation ADVANCE / RESEARCH / REPRODUCTION. No new theorem,
all-size executable guarantee or unrestricted SAT progress is claimed. PROOF.md
and DAG.md are unchanged because the mathematical argument and inputs did not
change. Separate audit-scope approval and then critical code/evidence review are
still required. Source proofs, library preparation and SAT transfer remain open.
