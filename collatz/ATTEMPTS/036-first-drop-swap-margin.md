# Attempt 036 — Uniform first-drop adjacent-swap margin order

Tested on 2026-10-28 in step535 under the saved EXPLORE assessment
`drafts/literature/2026-10-28-first-drop-swap-margin.md`. The proposed
certificate was M(u10v)<=M(u01v) at the least representatives >=2,
with both words guarded by first coefficient drop at the last step.
Its prospective use was a sorting reduction for coefficient-to-actual
descent, still requiring connectivity, base positivity and finite-drop
existence. None of those additional premises was assumed.

## WHY IT FAILS

[L109](../lemmas/L109-first-drop-swap-margin-counterexample.md) proves
an exact guarded reversal at length5: 11010-to-11100 changes the
margin from32 to96. The known decrease in the additive remainder does
not offset the upward change of the least representative. The full
modular-carry comparison, every prefix guard and both direct integer
trajectories are in that canonical proof; the complete certificate is
`scripts/first-drop-swap-margin/certificate.json`. The search stopped
on this first reversal and did not finish length5 or run lengths6–24.
Abandon this uniform order. No weakened variant is proposed or tested
in the same step. This does not refute Collatz, the coefficient stopping
time conjecture or the sourced remainder-order theorem. Future work
needs a materially different mechanism or independently testable target.
