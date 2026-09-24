# Coprime quadratic-root checkpoint — 2026-09-14

Starting from L187's g=1 sector, fix u and nonzero r. Then
m²≡−r mod u, (m,u)=1, and hence (r,u)=1. The exact m interval
intersects M, the stationary product bounds, the displacement lower
bound m≥|r−rho²|/(2rho), and Q's support bounds.

Draft route: count unit quadratic roots modulo prime powers, then use
CRT and at most floor(length/u)+1 representatives per root. Since
length=O(h)<u, the resulting bound is O_epsilon(u^epsilon) per (u,r).
Summing O(N²) moduli and O(N^(3/2)) displacements appears to give
O_epsilon(N^(7/2+epsilon)), worse than the inherited O(N^(3+epsilon)).
No equidistribution in the short interval has been proved.

Resume: verify the exact interval, prove the elementary prime-power root
bound, and test the finite reindexing including boundary and empty cases.
These draft statements are not proved DAG inputs.

Completed: L188 proves the exact interval identity and elementary root
bound. Its summed estimate loses N^(1/2) relative to the inherited bound.
The pointwise short-interval proportion is not justified. No draft
cancellation claim is promoted to a proved input.
