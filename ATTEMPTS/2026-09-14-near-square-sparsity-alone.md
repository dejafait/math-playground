# Near-square sparsity alone — 2026-09-14

The tested inference was that the perfect-square sparsity bound extends
to an o(1) estimate throughout 0<|sqrt(k)−m|≤N^(−1/2).
The precise count and retained real projection are proved in
[L184](../lemmas/L184-near-square-stationary-contribution.md).

**WHY IT FAILS.** At m≍N² this root width permits O(N^(3/2)) integer
products per m. The divisor estimate and uniform kernel bound therefore
give only O_epsilon(N^(1/2+epsilon)), not a vanishing upper bound.
The saddle phase being close to i does not remove the G_k projection;
even the first-order d_k C_k term has no proved vanishing absolute bound.
This is a limitation of these estimates, not a lower bound or a
counterexample to actual signed cancellation. The narrower
N^(−1−kappa) window is negligible, but the full requested window still
requires control of the signed sum in L184 (3).
