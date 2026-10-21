# Equality coefficient Lefschetz test leaves a global cup entry

2026-10-17. The actual scalar-action reduction is canonical in
[L117](../lemmas/L117-equality-actual-scalar-cup-map-limit.md).
It is NEGATIVE / REPRODUCTION: the test identifies a specific remaining
entry but excludes no further kernel or cardinality. The separate critical
audit of 2026-10-17 (step 340), recorded in L117, preserves the reduction
and this stop; it finds no substantive error or stronger exclusion.

WHY IT FAILS: The base-factor map J is already invertible on the full
trivial section summand. Fibrewise degree vanishing only kills local
contributions; the actual fibre cup factors through a global class in
Ext^2(M,M), inducing an unevaluated map Phi_1 on sections. Coefficient
Lefschetz requires det(1+J^{-1}Phi_1) nonzero and supplies no value of
Phi_1. Setting it to zero, or assigning an eigenvalue, would replace
actual geometry with an unsupported matrix. Park this exclusion route;
reopening needs independent evaluation or control of that specific
actual class. Preserve the dimension/section stop in ATTEMPTS/068 and
the metric/normal-curvature qualifications of the earlier attempts.
