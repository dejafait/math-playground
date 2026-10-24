# 2026-10-23 — bounded coefficient replay and restriction

Completed the exact gate-approved implementation using the ready
2026-10-22 coefficient assessment. The canonical result is L031's
derivative-facing supplement: all 54 good-prime rows, the nodal row,
255 factorizations and 256 coefficients agree; export is exactly 1..128.
Full records and zero-failure report are in
`scripts/finite-derivative-coefficients/`. The 48 inventoried input files
were preserved through execution. Bounds are 0.076641/180 seconds and
163638/134217728 bytes. No retry or kernel executed. This reproduces
known values with explicit provenance, not progress beyond checked
sources or a new BSD case. No new lemma or DAG edge is needed, and the
main argument is unchanged.

Next select separate approval of the proposed critical audit before any
audit execution. The original coefficient assessment is unchanged;
the new next assessment is REVIEW_REQUIRED. Remaining kernels, signed
assembly, strict derivative nonvanishing and the arbitrary-curve gap
remain open. The saved report distinguishes its pre-final-write timer
from the printed post-write measurement.
