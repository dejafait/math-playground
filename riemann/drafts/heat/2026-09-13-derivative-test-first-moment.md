# Derivative-test audit — 2026-09-13

The L173 reduction is complete and preserved. This step tests only classical
pointwise derivative estimates for its unweighted sums; the averaged
little-o claim remains unproved.

Checkpoint: for f(x)=(t−π/2)log(x/N)/(2π), t in the last block and
T=2πN², |f''| is comparable to 1 and f''' is comparable to N^(−1).
Second derivatives alone give O(N); third derivatives should give
O(N^(5/6)). Resume by verifying the named derivative theorem and its
uniformity for every truncated endpoint, then compare with the averaged
second moment. Do not infer nonvanishing from an inadequate upper bound.

## Completed audit

L174 verifies the uniform O(N^(5/6)) bound and the full-endpoint
first-moment range [c N^(1/6), C sqrt(N)]. Neither proves nor refutes
vanishing after division by sqrt(N). The named inputs were checked in
Robert's survey, Theorems 1 and 2 and the derivation preceding Theorem 2.
No numerical evidence was needed. The unresolved stationary-phase option
is to retain the dual phases rather than bound each transformed term
absolutely; no such transform is claimed proved in this checkpoint.
