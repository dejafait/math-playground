# Negative central-strip localization checkpoint

The completed L195 step is preserved. Current calculation: a nonempty
exact floor interval implies uv <= m²+R and u(v+1) >= m²-R+1.
For |v-2N²|<=K N^(3/2), this confines u to
[(m²-R)/(2N²+K N^(3/2)+1), (m²+R)/(2N²-K N^(3/2))].
Its length is O_K(N^(3/2)), uniformly for m comparable to N².
Together with divisor bounds for the ordered factor multiplicities,
ell<=2R and phi(u)/u²<=N^-2, this should yield
Y_mid^- = O_(K,epsilon)(h N^(1+epsilon)).
This is an improved upper bound, not little-o of Nh. Coprimality is
retained in the exact sum and dropped only in the positive majorant.
Resume by checking the endpoint implications and interval length,
then save the scoped result and explicitly retain the missing decay.

Completed in L196: the endpoint localization, interval length and improved
upper bound are proved. The normalized estimate is only O(N^epsilon);
little-o decay remains unproved. No further calculation is in progress.
