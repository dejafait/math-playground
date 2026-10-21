# Attempt 031 — Fixed joint witness real feasibility

## WHY IT FAILS

The exact L060 order surviving the two-prime diagnostics cannot satisfy
the retained simultaneous real system. Its unique minimum remains paired
with original row 8; that row's necessary J guard has left side >3280
and right side <26. Cyclic relabeling preserves this pairing. See the
canonical proof in
[L062](../lemmas/L062-joint-witness-minimum-real-guard-failure.md).
This rejects one real-feasibility candidate, not all orders or Collatz.
Earlier modular cancellations and the literal real witness remain valid;
no broader order search was performed. The separate critical audit in L062
found no defect: it verified the order-specific bounds, unique minimum,
strict necessary-guard failure and cyclic relabeling. The fixed-order
feasibility route remains stopped; other orders are not covered by this
stop.
