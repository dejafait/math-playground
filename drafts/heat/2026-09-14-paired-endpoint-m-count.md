# Paired endpoint m-count checkpoint

Date: 2026-09-14. CLI/model: Codex / GPT-6.
Prior L223 is complete and all existing changes are preserved.

For fixed a,c,d, retain the exact paired discrepancy as sampled mass
minus real mass. Positive f_m(b) forces avb-R < m² < a(v+1)b+R-1.
For b in [N,2N] the resulting square-root interval has length at most
0.6+o(1), using a<=1.2N and m near 2N² when it intersects J.
Only O(h/N+1) integers b can occur as m traverses J. This should give
an O(h/N) bound for the paired m sum, without dropping gcd in the
identity (drop it only in a nonnegative upper bound).

Resume: justify the interval length uniformly for cells meeting J,
write the exact candidate b range, and compare the resulting aggregate
bound to T. Little-o cancellation remains unproved.

Completed as L224: the uniform paired bound is O(h/N+1) per triple.
The remaining weighted square-root-cell occupancy discrepancy is unproved.
