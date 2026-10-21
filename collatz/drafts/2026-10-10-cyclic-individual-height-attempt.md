# Eighteen-word simultaneous-height attempt

Approved target: determine feasibility of the exact system in
`literature/2026-10-10-cyclic-individual-height-feasibility.md`.
Main gap: universal eventual descent. This is a bounded restricted-cycle
test, with integer/parity realization still relaxed.

Initial work checkpoint: L044 (5)–(6) already retains
h_(i+1)<(48/25)h_i+32/75 before weakening to factor 2.
Its numerical proof uses exactly the approved own-index inequalities
and the shifted endpoint equation, so it should apply to real heights.
With q=48/25 it gives h_(i+1)+1<q(h_i+1).
The proposed contradiction uses R=sum_(j=0)^17 q^j<150000,
L041's unchanged seed and N<(8/5)K+1242/1034, to force
N<11970000 log N+10800002. Check this on the entire ray
N>=338460000, not just at a scalar witness. No parameter screen is needed.

Success test: verify the real-height applicability, exact geometric bound,
and all-real monotonicity contradiction. Failure of any essential bridge
leaves feasibility unresolved; do not substitute a failed single tuple.
This uses the stronger already proved coefficient, not Attempt 021's
exhausted factor-2 comparison. Preserve all prior stop evidence.

Completed: [L046](../lemmas/L046-eighteen-word-individual-height-infeasibility.md)
proves the proposed contradiction on the entire admissible real ray.
The initial checkpoint is retained as reasoning history; the complete
proof and verification details are canonical in L046. No finite parameter
search was necessary. The separate critical audit remains pending.
