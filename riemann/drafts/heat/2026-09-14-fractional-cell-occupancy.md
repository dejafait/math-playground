# Fractional cell occupancy checkpoint — 2026-09-14

Use L224's open cell (alpha,beta), length ell<1 for candidate b
in its interval (6) intersected with [N,2N]. Set k=floor(alpha)+1
and theta=k-alpha=1-{alpha}, including theta=1 when alpha is an
integer. Occupancy is exactly theta<ell, not a non-strict inequality.
Retain k in J and gcd(a,k)=1; evaluate the exact rounded overlap
at k. Draft claim: Z is the sum of these weighted indicators, so
S=o(T) is precisely their aggregate discrepancy from T being o(T).
No cancellation is proved. Before promotion, check uniform cell length
for every b in (6), endpoints and exact rational-square comparisons.

Completed: L225 proves the formula and the cell-length estimate on all
of Bset. Exact integer-arithmetic checks include both square endpoints
and weighted reindexing. No equidistribution statement was promoted.
