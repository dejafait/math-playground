# Square-displacement expansion checkpoint

Date: 2026-09-14. Work in progress; no new DAG input yet.

Group L184 (3) by k=m²+r, keeping the exact set of nonzero integer r
with a−²≤m²+r≤a+² and |sqrt(m²+r)−m|≤N^(−1/2).
Here m≍N², |r|=O(N^(3/2)), d=r/(2m)+O(N^(−3)).
The smooth saddle coordinate at a fixed endpoint has derivative O(N^(−1))
with respect to its root q, including at q=a±. Thus freezing both
Fresnel endpoints at q=m costs O(N^(−3/2)) per bounded Fresnel factor.
The absolute normalized mass is O_epsilon(N^(1/2+epsilon)), so this
cost is O_epsilon(N^(−1+epsilon)). The original L184 remainder is
O_epsilon(N^(−1/2+epsilon)). Preserve W(m²+r), with no smoothness claim.

Resume: prove the uniform coordinate derivative including roots just outside
the stationary interval, derive the two signed sums S0 and S1, and record
all accumulated errors before promoting the statement.

Completed: the derivative estimate extends smoothly across either endpoint,
and the exact two-short-sum reduction is proved in L185. Endpoint freezing
costs O_epsilon(N^(−1+epsilon)); the inherited error dominates. No arithmetic
weight expansion or cancellation is asserted. This checkpoint is closed.
