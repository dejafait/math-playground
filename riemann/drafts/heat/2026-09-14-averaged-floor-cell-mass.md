# Averaged floor-cell mass checkpoint

Preserved completed L196 and all pre-existing changes. For fixed u,v,
nonempty exact cells force uv-R <= m² <= u(v+1)+R-1.
Since m is comparable to N² and u=O(N²), only O(1) integers m
can occur. Thus the exact coprime weighted sum of alpha_m ell is
O(R), without any density replacement.

The union of L196 product intervals over M_in has length O_K(h+N^(3/2))
=O_K(N^(3/2)), since M_in lies in an interval of length h/(2π).
An interval of products of length L contains at most
O(L+N) ordered pairs a,b in [N,2N]: for each a there are at most
L/a+1 possible b. Both u and the central v strip consequently have
O_K(N^(3/2)) total bounded-profile pair mass. Reordering gives
O_K(R N^(-2) N³)=O_K(N^(5/2))=O_K(Nh).

Resume by verifying the union interval endpoints, the O(1) m count
including singleton floor cells, and the weighted finite rearrangement.
This does not prove little-o or a lower bound; no claim is yet promoted.

Completed in L197: audited exact cell endpoints, the common interval,
and weighted pair counting. The O_K(Nh) bound is proved; little-o and
any matching lower bound remain unproved. No calculation is in progress.
