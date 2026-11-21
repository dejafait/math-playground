# Fixed-support equal-radius interval test: stop734

Ready assessment732/comparison733 was reused for the fixed-label family
test. The canonical proof and evidence are
[C998w Section5](../lemmas/C998w-support-grid-original-measure-residual-partial.md).
The constructor and independent exact-row replay certificates are
`scripts/separation-seven/fixed-support-shared-734.json` and
`scripts/separation-seven/fixed-support-row-replay-734.json`.

WHY IT FAILS: one interpolation preconditioner generated at k=10 has,
already at k=11, an exact row33 absolute sum in(1.58635,1.58636) for
I-R_A A_11. Thus every equal-radius box expands in that row, regardless
of the residual center, and cannot satisfy the chosen strict inclusion.
The Gram test passes there. This is a failure of the fixed unweighted
norm/equal-radius prescription, not evidence of negative weights or
failure of all Rump boxes. No later blocks or weights are tested and
the complete cost/storage gate remains unpaid. Old731 rules and the
728/732 implementation stops survive.

A componentwise-radius box is a specific remaining refinement under
the same source criteria and fixed support/anchor/preconditioners.
It would have to dominate the interval error action on every required
block simultaneously, then validate rounded weights and original
residuals and price all work. No such vector or inequality was tested
or established734. Repeating the equal-radius test is unjustified.
