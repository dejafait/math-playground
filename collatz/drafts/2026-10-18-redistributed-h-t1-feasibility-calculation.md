# Changed-H t=1 single-root calculation

Approved target: determine whether the redistributed-H t=1 affine cyclic
root satisfies every constraint of L051 (1)–(4). Reuse the prior SPECIALIZE
assessment `literature/2026-10-18-redistributed-h-t1-real-feasibility.md`.
The main gap remains universal eventual descent. One failed own-input
guard would reject this exact real candidate before arithmetic; a full
witness would instead limit the relaxation. Stop after this tuple.

Essential inputs: L051's full real system, L055's indexed table and
affine/analytic method, L079's H changes and total-count conventions.
L081 is comparison only. Both original witnesses and Attempts 026–031
remain valid. No cross-notebook input or integer realization is assumed.

Working test: with tails 2 through row 22, tail 20 at row 23 and
166504394 at row 24, recompute every incoming prefix and the cyclic
denominator. The row-18 incoming prefix has neither transferred tail.
If a fresh bound gives s_i/C_i<exp(24) on all input indices, its same
own-input H expression may be strictly negative. Prove growth at the
tail-20 row separately; do not import t=0 or original-H root bounds.
Touching zero is unresolved. No further allocation or table is tested.

Completed: [L082](../lemmas/L082-redistributed-h-t1-real-h-guard-failure.md)
proves one strictly failed row18 H guard. The tail-20 row has a fresh
multiplier floor 3^63/2^91>2; both transferred tails enter the full root.
All 153 exact certification checks pass. The certificate retains every
operand and bound in
`scripts/postspell-word-count/redistributed-h-t1-real-feasibility-certificate.json`.
No other guard classification is needed or asserted. This is local
REPRODUCTION with outcome NEGATIVE, not an independent critical audit
or an originality claim. The sole continuation is the separate critical
audit proposed in the REVIEW_REQUIRED assessment
`literature/2026-10-18-redistributed-h-t1-failure-critical-audit.md`.
