# Fixed-count coupled-tail attempt — working record

Approved target: test L051 (1)–(4) at r=25, K=397573379,
N=630138897, L=232565518 using the exact tail budget. Prior coverage:
`drafts/literature/2026-10-11-twenty-five-fixed-count-tail-budget.md`
(SPECIALIZE). Essential existing inputs are L051, L052 and L054;
the latter's envelope failure is preserved, not treated as feasibility.

The main gap is universal eventual descent. This bounded test seeks a
full real-system witness or an all-allocation contradiction, addressing
only one necessary count branch. Other branches, integer realization,
unrestricted cycles, entry and divergence are independent unresolved gaps.

Concrete mechanism: choose the first 24 tails equal to 2 and put the
remaining exact budget in the closing tail. Choose initial word parameters
within conservative forward lower-height guards, then adjust the last J
for the total tail congruence and the last H for the exact odd count.
The proposed parameters are not yet certified.

For c_i=3^(3J_i+H_i)/2^(4J_i+H_i+a_i), C_i=prod_{j<i} c_j,
and eta_i as in L051, the exact cyclic root would be
n_0=(sum_i eta_i/C_i)/(exp(Lambda)-1), with C_0=1.
This is the cited affine rational-cycle construction specialized to the
retained shifted coordinates, not an integer-cycle claim. Bound n_0
and each forward log height, then verify all own-index guards, the
minimum, seed, exact counts and closing endpoint. Failure of this
allocation alone would not exclude all allocations. Continue only for
a fully verified witness or contradiction; otherwise record the exact
unresolved constraint and stop the comparison. No stronger source
threshold or parity realization is assumed.

## Completed bounded attempt

The explicit allocation succeeds: see canonical L055 and
`scripts/postspell-word-count/fixed-count-tail-witness-certificate.json`.
Its 70 strict rational checks and 34 integer checks pass. The factored
rational cyclic root satisfies every endpoint, guard, seed, total and
tail congruence; the proof supplies exact closure without expanding huge
powers. This is an informative NEGATIVE for exclusion by the unchanged
real subsystem, not an integer cycle or a Collatz counterexample.
No claim of optimality or original general cycle theory is made.

Stop trying to exclude this branch using only L051 (1)–(4). Preserve
L054 and Attempt 025 as weaker method failures. Independent critical
audit of L055 remains pending; the current next action and its assessment
are recorded only in PROGRESS.md.
