# Summed second-derivative estimate — 2026-09-14

The calculation and its precise limits are proved in
[L231](../lemmas/L231-second-derivative-budget-for-the-paired-fourier-sum.md).

WHY IT FAILS: the b-phase curvature is of size k/e, rather than a
negative power of N at fixed frequency and divisor. The capped
second-derivative bound is therefore trivial for k>=e, including k=e=1.
Keeping the endpoint pair gains k/e only for k<=e, and summing this
bound leaves O(N²h (log N)²). Even the stronger uniform sawtooth bound
O(N²h log N) does not approach o(B_0). These are limitations of the
absolute upper-bound method, not evidence that the actual discrepancy
fails to cancel. A higher derivative test may improve a restricted
frequency range but has not been evaluated in this step.
