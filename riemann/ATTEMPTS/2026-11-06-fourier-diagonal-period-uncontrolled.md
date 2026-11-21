# Fourier/diagonal compatibility does not yet control the period

2026-11-06. One mathematical attempt used the prior EXPLORE coverage
in `drafts/literature/2026-11-06-one-sided-fourier-diagonal-period-test.md`.
The complete intermediate calculation is canonical in
[C868a](../lemmas/C868a-diagonal-mean-and-fourier-correction-bounds.md),
newly written and unaudited. This records no counterexample to the
full admissible class and no impossibility theorem for the target.

**WHY IT FAILS TO FINISH.** The actual diagonal fixes the mean of q
along equal-radius tori, so positivity provides a uniform bound on
the correction modes whose two indices have nonzero sum. However,
the bound is in terms of an uncontrolled nonnegative mean H; the
period is the separate constant A plus H. The zero mode and the
opposite-index modes away from the diagonal remain. No comparison
of A+H with -|M| follows from the completed calculation. Dropping
those modes, treating Fejer approximants as feasible under the fixed
modulus constraint, or imposing extra growth would not finish the
approved problem. The all-F-zero domination has not been exploited
enough to close this gap.

Stop the Fourier/diagonal-only period attempt unchanged. The new
restriction can be retained and audited, but a subsequent period
attempt needs materially new control, such as a demonstrated use
of the other G-zero fibers, and appropriate coverage for its exact
target. That possibility is not a derived or approved continuation.
L867's narrower stop and L868's weaker bound/zero-period example
retain their scope. No implication for the actual-Xi higher signs
or RH has been established. Outcome EXPLORATION records that the
restriction has no demonstrated threshold leverage yet, and does
not reset the mathematical exploration budget.
