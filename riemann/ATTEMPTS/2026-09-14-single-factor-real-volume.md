# Single-factor real-volume shortcut — 2026-09-14

The inverse single-factor intervals and exact weighted slice are recorded
in [L219](../lemmas/L219-single-factor-slice-and-real-measure-obstruction.md).

WHY IT FAILS: Replacing the integer support by its real interval lengths
does not supply the missing square-root saving. Under the explicit
interior-slice hypothesis in L219, the relaxed union itself has length
comparable to sqrt(N), rather than O(1). Without a discrepancy argument
real length does not bound integer occupancy in either direction anyway.
This rejects that shortcut, not the desired arithmetic estimate: exact
lengths and coprimality can still affect the integer sum, and no lower
bound for that sum has been proved.
