# Step 307 — fixed known-point local-seven attempt

Approved target: test P=(0,0) in E(Q_7)/7E(Q_7) on
y^2+y=x^3+x^2-2x by exact W=[13]P. Prior SPECIALIZE coverage is
`drafts/literature/2026-10-18-known-point-local-seven-test.md`.

Main gap: arbitrary analytic order at least two still lacks rational-rank
equality. This finite test seeks actual local data only. Inputs are L030's
minimal model, L033's reduction group of order 13 and the rational point
recorded in L034; rational membership itself is immediate by substitution.
L062 is downstream motivation, not an input to this point computation.

Plan: retain every branch of one rational binary group-law chain, then
independently replay the chain and sequential additions on the translated
short model. Save full coordinates, rational denominators, projective
reduction and seven-valuations. Seek W nonidentity with formal parameter
valuation one. A failed hypothesis, valuation threshold or full replay
stops this fixed test, without changing point or depth.

The remaining applicability proof must exclude division points in the
entire local group using its reduction order, then use the imported
formal logarithm isomorphism on 7Z_7 and 49Z_7. No result is asserted yet.
Even success supplies neither every L026 premise nor D=D_div, a strict
rational direction, complete descent or arbitrary-curve rank comparison.

State at start: exact arithmetic and applicability proof not yet done;
unfinished order work and stopped routes remain preserved.

Completed: L081 records the full proof and exact value. Certificate and
complete replay are in `scripts/known-point-seven-307/`; all five binary
branches and thirteen sequential additions agree, projective reduction
is O and actual v_7(t)=1 meets required one. The initial independent
verifier's short-model line-ordinate sign error is preserved with its
failure record; its corrected full replay passes without changing the
producer or certificate. This is a successful known-method local
specialization, not a separately audited result or new rational rank.
The next assessment proposes only critical audit and remains
REVIEW_REQUIRED for separate approval. No L062 handoff is made.
