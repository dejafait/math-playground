# Centered primitive covariance checkpoint — 2026-09-13

The previous L166 step is complete. This step uses its Gaussian profile and
L156's carrier-removed derivative estimates. Set
P(t)=∫_T^t(W(s)−bar W)ds. Both endpoints vanish, and the exact
covariance is −E_T[P χ'''(Q/M)Q']/M.

Proof plan: establish ||P||∞≍T(log T)^4. For the lower bound use
u=t/T, g(u)=W(Tu)−bar W, p(u)=∫_1^u g, and
∫g²=−∫p g'. L166 supplies ∫|g|≍(log T)^4 and
sup|g'|=O((log T)^4). Cauchy–Schwarz then gives the claim.
The absolute derivative estimate is O(T(log T)^4/M), worse than
the direct O((log T)^4) bound. Neither is an actual error lower bound.

Checkpoint: finish the normalization, support restriction, and scope audit;
store as L167, then update DAG/history/PROGRESS and run structure validation.

Completed: the proof and scope audit are stored in L167. No signed
covariance lower bound follows from the primitive lower bound.
