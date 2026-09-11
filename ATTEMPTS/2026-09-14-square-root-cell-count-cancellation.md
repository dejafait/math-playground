# Square-root cell counting alone does not prove cancellation

Date: 2026-09-14.

Outcome: [L224](../lemmas/L224-paired-endpoint-sum-by-square-root-cells.md)
proves an improved paired endpoint bound by counting candidate b cells.

WHY IT FAILS: Each candidate cell has at most one integer m, but its
length is bounded rather than tending to infinity. An error of order one
per candidate b accumulates to O(h/N) per triple and O(N²h) in aggregate,
the upper scale of the real mass T. This estimate cannot imply S=o(T).
It does not refute cancellation of the actual signed sum; the weighted
occupancy discrepancy, including gcd(a,m)=1, remains to be estimated.
