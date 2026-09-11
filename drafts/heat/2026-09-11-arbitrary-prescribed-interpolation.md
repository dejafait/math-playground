# Arbitrary prescribed interpolation — 2026-09-11

Checkpoint: claim not yet promoted to a proved input. For arbitrary unbounded
P containing 1, each gap interpolant g_t(v)=sqrt(v)t^(1/4)(5/4-v/(4t))
has derivative at least (1/4)v^(-1/4) on v≤t. Its left endpoint
exceeds the prescribed value; its right endpoint equals it. Thus expect
x_j-x_n≥(j^(3/4)-n^(3/4))/3 globally, including all gap boundaries.
Resume by proving that discrete separation, then apply the finite
height-increment crossing argument of Lemma 78. On n∈[N,2N), j≤4N,
the full right sum is bounded by 64 sqrt(N) times the increment kernel.
The averaged finite contribution should be at most
64H(1+log(4N))/sqrt(N); far and reflected tails are O(H/sqrt(N)).
No numerical certificate is needed. The claim concerns all indices,
not necessarily a subsequence restricted to P; check the requested scope.

Completed: Lemma 100 proves the global separation and vanishing block
averages for every P. Selection restricted to P remains unproved here.
