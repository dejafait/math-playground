# Single residual-stationary trial603: implementation allowance stop

The complete reasoning, citations, qualifications and artifact locations
are in [attempt603](../drafts/2026-11-12-residual-stationary-fixed-trial-603.md).
One finite-output stationary solve proposed and saved one dyadic map;
no regularization, pseudoinverse or tuning was used. Exact Z defines
neutrality. The full original head action was replayed independently.

WHY IT FAILS: The new computed head-action error upper estimate is
<.000032692462 but exceeds the verifier's preset .00001 allowance.
This inherited implementation budget is not a necessary threshold for
the .000999 target, and is not a lower bound on actual arithmetic error.
It caused an inconclusive early stop. Remaining finite covariance,
analytic errors, all infinite outputs and final matrix order are unpaid;
selection-stage output generation does not verify them. There is no
actual violating direction or canonical counterexample theorem to cite.
Preserve the map and stop without tuning. This is EXPLORATION, not an
informative mathematical negative. A different high-endpoint analytic
reduction is nominated for a separate source review; no result is assumed.
