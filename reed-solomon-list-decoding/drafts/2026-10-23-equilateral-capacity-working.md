# Conditional equilateral capacity test — step 412

Gate: reuse the unchanged EXPLORE assessment
`drafts/literature/2026-10-23-equilateral-scaling-capacity-test.md`,
saved and separately approved before this invocation. Actual task:
one finite conditional calculation, with no factor-existence claim,
nonlinear solve, parameter scan or restart of ATTEMPTS/082.

The main gap is arbitrary-center safety at 67/68 agreements. Essential
inputs are L021,L098,L105,L108,L109 and foundations/04,12,13. The proposed
intermediate certificate could separate upper-capacity control from
positive distance-invariant scaling existence. Both existence and the
Boolean lower rows/full source lift/PSD/RS realization remain unresolved.

Write x_i=c_i*f_i>0 for 5<=i<=68 and conditionally assume exact distinct
edge marginals d_i=(N-2)c_i with N=floor(65537^28/2^128)+1. Let E_i
be the complete number of supports Z at distances i from both ends of
a fixed distance-i edge. Sum L109's actual D over j=h=i, hence s=i-t,
over every admissible t. Nonnegative equilateral contributions imply
E_i*x_i^3<=d_i. Multiplying these three conditional bounds gives an
upper allowance whose cube, divided by min(c_i,c_j,c_h)^3, is rational.
This is reasoning in progress pending exact finite evaluation.

Test: continue this certificate only if every permitted actual triangle
has allowance at most one. Any allowance above one parks this sufficient
certificate alone; it neither violates an actual solution nor rejects
scaling or capacitated primal feasibility. Retain endpoint repetitions,
zero edges, original t-s and all source multiplicities. Use complete
exact data and an independent equilateral-count reconstruction, not
L108's single exhibited orbit. No numerical preview will establish the
load-bearing verdict.


## Completed — step 412

The coherent finite calculation is complete: NEGATIVE, RESEARCH,
REPRODUCTION. Canonical proof and limitations are in
`lemmas/L110-equilateral-scaling-capacity-allowance-failure.md`; full
factored evidence is `scripts/finite-support/equilateral-capacity-allowance.json`.
All 41314 construction checks pass. Every saved side ratio was also
checked by integer cross multiplication against the stated maximum.
The exact maximum allowance is (N-2)/89469195005112, between 2.38*10^82
and 2.39*10^82 against required bound one. Park this sufficient
certificate only, as recorded in ATTEMPTS/093. This neither proves
an actual capacity violation nor rejects scaling or primal feasibility.
Independent critical review remains pending. The sole current action
and new REVIEW_REQUIRED assessment are recorded in PROGRESS.md.
