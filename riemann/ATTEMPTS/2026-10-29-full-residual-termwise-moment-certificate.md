# Complete residual: termwise moment certificate — 29 October 2026

The approved target was to test whether second/fourth moment
interpolation certifies L477's full-scale absolute residual lower bound.
The complete finite expansions and rigorous failure of the specified
coefficientwise interval majorant are canonical in
[L478](../lemmas/L478-full-residual-moment-expansion-and-termwise-budget.md).
The invocation-start assessment was
[the full-residual moment comparison](../drafts/literature/2026-10-29-l477-residual-moment-interpolation-coverage.md).
All prior work and historical stops are preserved.

WHY IT FAILS: the complete second moment contains a U C cross term
whose positive-density index box has interior stationary points.
Adding the uniform second-derivative bounds separately has a budget
of order T^(3/2), exceeding the at-most O(T(log T)^8) complete
constant-phase mass. The resulting rigorous I_2 lower certificate is
zero, so interpolation cannot certify the requested L1 lower bound.
This is a failure of the specified majorant, not a lower bound on
actual integral magnitudes, a sign assertion for their sum, a bound
on the true quotient, or a disproof of the proposed L1 threshold.

Do not repeat this majorant with renamed indices. L478 (13) retains
an exact grouped signed arithmetic sum as a materially refined target;
its asymptotic evaluation requires new coverage and is nominated in
[the new assessment](../drafts/literature/2026-10-29-grouped-residual-cross-term-coverage.md).
No stationary-phase transformation or cancellation theorem was approved
in this turn. The other moment estimates, both defect thresholds,
negative-mass saving and global mixed positivity remain open.
