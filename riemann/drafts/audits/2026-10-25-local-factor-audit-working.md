# Finite local factor audit — working record

Approved target: critically audit bramble_trace v4 Section 4.3,
(18e)–(18h), including central zeros and repeated roots. Reuse
`drafts/literature/2026-10-25-local-factor-coefficient-audit-coverage.md`
(SPECIALIZE); classification REPRODUCTION. This is one mathematical
audit, not a new literature search or a broader manuscript audit.

Main gap: initial actual-Xi signs at unbounded heights, effective
bounded-height overlap and global mixed positivity. The intermediate
comparison could supply a checked product-tail component of L463.
Continue if finite coefficient domination, exact normalization and
uniform shell bounds all pass; otherwise record the failing assertion.

Inputs inspected: canonical L018/L024/L026/L027, L255 and L463;
source Section 4.3 in full. Reuse Titchmarsh, second edition,
Theorem 9.2, (9.2.1), p. 211, from the approved assessment.
L260's simplicity counterexample and the September 23 finite-level
and September 27 count/gap stops remain applicable to sufficiency
shortcuts, not this tail estimate.

Preliminary algebra: for q=p-M, iterate j*g_j<=U*g_(j-1)
upward to bound g_(q+k)/g_q by U^k/((q+1)...(q+k)). The
finite-B remainder then has exactly the source's binomial bound.
Zero roots only make some coefficient bounds smaller. Full proof
and the M=0 case still to be saved canonically.

Normalization to verify: a real positive zero gamma contributes
F_(gamma-t)(x) F_(gamma+t)(x)/gamma^4, F_a=x+a^2.
A conjugate pair gamma±id contributes Q_(gamma-t,d)(x)
Q_(gamma+t,d)(x)/(gamma^2+d^2)^4, with
Q_(a,d)=x^2+2(a^2-d^2)x+(a^2+d^2)^2.
Keep near factors monic; divide only far factors by their positive
constant terms. Thus a central real zero remains in B, never in a
denominator. For wholly far indices, removed constants are
(1-t^2/gamma^2)^2 or |1-t^2/(gamma+id)^2|^4, respectively.
Their deviations from one are O_t(gamma^-2).

Remaining checks: complete limit passage, positive convergent C_t,
shell estimates with endpoints and multiplicities, and one common
C for every t>=2 and every integer p>=C*log(t+2)^2.
No zero-free premise, numerical evidence, simplicity or central
nonvanishing is to be used. Broader L463 analytic estimates and the
external premise remain unaudited. No verdict yet.

Completion note: the bounded audit subsequently passed. The full proof,
including the scalar product, endpoint-safe shell counts and the common
constant, is canonical in
`lemmas/L464-uniform-local-factor-coefficient-tail-audit.md`.
The preliminary reasoning above is preserved as the working checkpoint.
