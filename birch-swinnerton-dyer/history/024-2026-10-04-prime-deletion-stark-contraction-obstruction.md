# 2026-10-04 — Stark contraction preserves the p^2 transverse error

Completed one mathematical attempt on the exact saved COVERED_TARGET,
reusing its prior SPECIALIZE assessment. Reread the previously assessed
Sakamoto Section 2.5 and its named duality inputs; no new source search
or literature assessment was undertaken. Saved the working reasoning in
[the draft](../drafts/2026-10-04-prime-deletion-stark-contraction-test.md).

[L017](../lemmas/L017-prime-deletion-stark-contraction-retains-p2-error.md)
proves that the actual p-local canonical extension at N splits and its
rank-three to rank-two determinant contraction is an isomorphism. Its
divisor transitions retain the order-p error vectors, while the final
scalar product is zero modulo p^2. The nonzero-tau model now extends
the p-local sequence and both rank-one/rank-zero divisor diagrams,
beyond the constraints previously tested in L016. Exact checks over
Z/25Z pass for all five residual values of tau; see
[the output](../scripts/prime-deletion/p2-stark-contraction-result.json).

Outcome: NEGATIVE; classification: REPRODUCTION of the assessed framework.
This is new local evidence against automatic lifting from the tested
contraction data, not a result beyond checked literature. It evaluates no
arithmetic tau and constructs no full Stark/Kato system. The required
rational-rank lower bound remains missing; the achieved bound is r <= 2.
Preserve the failed promotion in ATTEMPTS/018.

Move to screening a coefficient-p^3 initial-Fitting test with the additional
analytic premise L(E,1)=0. This addresses the scalar information lost at
depth two, rather than repeating contraction or reciprocity. The changed
depth and initial-value comparison are not covered by the saved p^2
assessment, so a REVIEW_REQUIRED placeholder is created. No p^3 result
is derived in this turn. Exploration use is 0 of 3; STATUS remains
IN_PROGRESS with no candidate. Step identifier:
BSD-2026-10-04-024-prime-deletion-stark-contraction-obstruction.
