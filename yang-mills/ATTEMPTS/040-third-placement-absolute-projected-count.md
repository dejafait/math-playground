# Third placement: absolute projected energy count misses cubic scale

WHY IT FAILS: [L187, proof sections 3–5](../lemmas/L187-probe-quartic-third-placement-projected-trace.md)
retains the exact signed Q_3 trace and improves the global count through
the pinned scalar product rule and a separate upper-layer covariance
trace. Its two energy factors are bounded by O(N^(3/2)) and O(N^3);
the rough whitened residual is O(N), and the exterior normalization
is O(N^-2). Thus the complete estimate is O(N^(7/2)), versus required
O(N^3). This stops that absolute count as cubic closure. It is not
growth of either actual-probe response or failure of its scaled limit.
The signed trace remains independently testable; positivity of M,
smoothness on its rough leg, or deletion of the pinned jump would not
repair the estimate. ATTEMPTS/039's earlier stopped count is preserved.
