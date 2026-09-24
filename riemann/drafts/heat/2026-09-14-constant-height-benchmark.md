# Constant-height benchmark checkpoint — 2026-09-14

Scoped part of the occupancy discrepancy task: simplify heights and the real benchmark, without assuming phase distribution.

On J the stationary cutoffs are inactive. L220 gives H_m = min(2,4/C_R)+O(N^(-1/2)), uniformly, including C_R=2. L224 bounds the total number of candidates by O(N²h), so replacing heights costs O(N³). L223 gives F_m = H_0 4N^4/[av(v+1)]+O(N^(-3/2)). Summing costs O(N³). Count coprime m in J by finite Möbius inversion: |J| phi(a)/a + O(tau(a)). This yields a separated benchmark B_0 = 4N^4 |J| sum_a phi(a)^2/a^3 sum_(c,d)1/[cd(cd+1)].

Unproved: weighted strict candidate count C equals B_0+o(B_0). Resume by checking all uniform errors, especially cutoff ties and closed interval counts, then record the proved reduction only. This is not yet an aggregate cancellation bound.

Completed: the uniform errors and closed-endpoint Möbius count are proved in L227. The simplification error is O(N³); no occupancy cancellation was established. Current work is recorded only in PROGRESS.md.
