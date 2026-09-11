# Large-divisor phase tail checkpoint — 2026-09-14

The previous L228 reduction is complete and preserved. Investigate its tail
P_{>D} using r_e=n_e-ell/e, where n_e counts multiples of e in the
strict open cell. Do not split the two fractional parts separately.

For a fixed a,m with e|a,m, cell membership implies
(m²-R+1)/a-b < bcd < (m²+R)/a.
Since N<=b<=2N, enlarge this to a product interval of length
2N+(2R-1)/a=O(N). Each positive integer product has at most
O_epsilon(N^epsilon) ordered factorizations b,c,d (product O(N³)).
This should bound the count by O_epsilon(N^(1+epsilon)) per a,m.
The number of (e,a,m) with e>D, e|a,m is at most
O(Nh/D+N log(2N)), from interval counts. Proposed tail bound:
O_epsilon(N^(2+epsilon)h/D+N^(2+epsilon)log(2N)).
Claims at this checkpoint are unproved pending full endpoint, divisor-bound,
and benchmark checks. Resume by completing these checks and recording L229.

Completed in L229. The proposed bound holds for every epsilon>0;
choosing epsilon<delta proves the N^delta cutoff error is o(B_0).
Strict endpoint algebra, positive product counting, repeated divisor
multiplicities and the real-length tail have been checked. No cancellation
estimate for the retained phases was obtained. This draft is preserved as
the interrupted-work checkpoint record, not an additional active task.
