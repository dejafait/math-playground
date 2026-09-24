# Near-square stationary contribution — 2026-09-14

Checkpoint (claims below initially unproved): existing L183 is complete;
its history entry was missing. Preserve that result without recomputation.
For stationary k with 0<|sqrt(k)−m|≤rho=N^(−1/2), the nearest integer m
is unique for large N, but can lie just outside [a−,a+]. Count m in
[a−−rho,a++rho]. Each m permits O(1+N²rho) integer k, giving
O(h(1+N²rho)N^epsilon) quadruples by L183's divisor argument.

Resume by checking this count, L182's subset error, and the exact real
projection cos(4πd)G_k−sin(4πd)C_k, where d=sqrt(k)−m,
G_k=integral sin(z²), C_k=integral cos(z²), at the original endpoints.
Proposed linearization G_k−4πd C_k has normalized error
O_epsilon(N^(−1/2+epsilon)); absolute main bound is only
O_epsilon(N^(1/2+epsilon)). These are not a proof of negligibility.
If confirmed, store a lemma and the precise failed sparsity inference;
leave estimation of the resulting signed sum as the sole next action.

Completed: the count and both error exponents are proved in L184.
The N^(−1−kappa) subwindow is negligible. For the requested width,
the signed sum with G_k−4πd_k C_k remains unestimated; the phase
correction cannot be discarded using the present absolute bounds.
