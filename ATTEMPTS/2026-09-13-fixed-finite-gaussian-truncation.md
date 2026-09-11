# Fixed finite truncation does not settle the tail — 2026-09-13

Attempt: use Gaussian decay to replace the normalized series by a fixed
finite polynomial, then choose a fixed amplitude cutoff from boundedness.

WHY IT FAILS: The mass moves to indices of order sqrt(T). Any fixed finite
set has normalized squared L2 mass tending to zero, while the full series
has mass tending to K>0. Its approximation error therefore tends to K.
The [canonical proof](../lemmas/L155-gaussian-window-reduction-for-truncated-tails.md)
also gives the valid moving-window reduction. That window grows with T;
its boundedness for each T gives no uniform cutoff. The desired tail bound
for the moving core remains open, not disproved by this failed truncation.
