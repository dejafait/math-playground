# Generic mixed residual norm after the endpoint cancellation

WHY IT FAILS: [L064](../lemmas/L064-mixed-pinned-endpoint-regrouping.md)
retains all four remaining mixed placements and gains one power by an
exact pinned endpoint cancellation. The general whitened residual bound
O(N), however, gives mixed curvature/path norms O(N³)/O(N⁴). With the
full axial cross norms this supplies only O(N^(7/2)), versus the required
O(N²). The first pair also has only O(N³). This stops this combination
of general residual norm and absolute-array Cauchy–Schwarz as a proof
of the a² threshold. It is not a lower bound or a counterexample to a
sharper signed estimate. The retained right circulation and fractional
cross-covariance weight have not been used jointly; testing that different
contraction remains open. Earlier stops in ATTEMPTS/017–018 are preserved.
