# Fixed head-defect factor proposal — step573

The proposed certificate Ehat*Ehat<=.0001^2 M_cert did not produce a
Cholesky factor. Its complete script/JSON/NPZ/log remain in
scripts/separation-seven/signed-mixed-head-defect-floor-failure-573.*.
The failure is inconclusive: it is not a rigorous lower bound or a
rejection of the fixed quarter inequality. The printed candidate head
error is conditional on the failed factor and is not certified.

WHY IT FAILS: this proposal tried to normalize the raw defect before
using only the scalar H inverse floor. No complete factor was obtained,
so it could not justify its claimed small normalized defect. A small
outward-rounding omission in the diagonal-tail center was also present;
no conclusion is imported from that run. The same step's full inverse
correction succeeds with unchanged mathematical parameters, as proved
in [C999m Section14](../lemmas/C999m-neutral-tail-mixed-covariance-domain.md).
This stops only this unsuccessful certificate proposal; it establishes
neither an actual large error nor an obstruction to the mixed test.
