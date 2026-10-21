# 2026-10-04 — Termwise curvature transfer for the quadratic flow term

Within the screened combined-response calculation, tested whether the
nonradial quadratic flow jet could use the same forest-to-Hodge
curvature argument as the selected radial cubic vertex.

WHY IT FAILS: [L022](../lemmas/L022-quadratic-flow-longitudinal-obstruction.md)
constructs a pinned zero-linear-curvature input on which the actual
triplet term j_(3,2)(z_2) equals 1+O(a^2). It is therefore not a function
of linear curvature. The higher observable jets cancel this term on
that input, leaving O(a^4); omitting them loses a real cancellation.
This stops only the proposed termwise transfer. It does not show that
specific forest and Hodge covariances differ, rule out regrouping, or
stop the full coefficient calculation. The separate curvature-based
radial action insertion remains independently testable.
