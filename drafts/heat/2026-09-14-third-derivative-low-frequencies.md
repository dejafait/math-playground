# Third-derivative low-frequency calculation — 2026-09-14

Checkpoint: existing L231 is complete. This step treats only L230's
frequencies k<=K=floor(N^(1/4)); the higher-frequency sum is unproved.

For t=k/e, alpha'''=3(av)^3/(8 alpha^5), and the beta formula
replaces av by a(v+1). Thus lambda is comparable to t/N.
The standard third-derivative bound is
M(t/N)^(1/6)+M^(1/2)(N/t)^(1/6).
L231's paired amplitude gives the additional min(1,t).

Resume by verifying partial-sum uniformity and summing the two terms
with 1/k and the O(N^3/e) triple count. For e<=K the two elementary
frequency sums are O((K/e)^(1/6)) and O(1), respectively.
Expected bound: N^3[M N^(-1/6)K^(1/6)+M^(1/2)N^(1/6)log(2K)],
which is o(B_0). This expectation is not yet a proved DAG input.
