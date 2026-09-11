# Growing prime band checkpoint — 2026-09-14

L206 is complete; existing work is preserved. Scope this step to Y<p<=N^(1/4), leaving larger primes unproved.

For step s=1 or p, the phase sqrt(acd(r+sj))/p has third derivative comparable to s^3/(pN) and length comparable to sqrt(N)/s. The normalized derivative bound is
O(k^(1/6)s^(1/2)p^(-1/6)N^(-1/6) + k^(-1/6)p^(1/6)N^(-1/12)).
For p<=N^(1/4), k<=N^(1/8), this is O(N^(-1/24)). Use periodic linear ramps of width N^(-1/16), Fourier cutoff N^(1/8), giving discrepancy O(N^(-1/24) log N). Summing joint frequencies costs another log N and interval rounding O(N^(-1/4)).

Resume by proving the uniform ramp bounds and pair counts, then store the scoped lemma. No estimate for primes greater than N^(1/4) is claimed.

Completed: the uniform bounds, interval approximation (including shrinking targets), and prime summation are proved in L207. The larger-prime tail remains unproved; PROGRESS.md records its precise next action.
