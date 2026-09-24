# Dense suffix averaging — 2026-09-11

Draft claim, initially UNPROVED: if |S intersect [N,2N)| >= delta N
for every sufficiently large integer N, actual near sums average to zero
on these sets for arbitrary bounded increasing heights.

Checkpoint: put t=min(S intersect [N,2N)), A=a_t. For sqrt(N)<=j<=N/2,
choose r in S intersect [j,2j); then r<N<=t, a_r<=A, and
x_j²<=x_r²<=2j A². Reciprocal-square summability should imply
log(N)/A² tends to zero. For n in the selected block and n<k<=2n,
x_k-x_n >= A(k-n)/(4 sqrt(N)). Finite increment crossing bounds
the sum of near sums by 16 N H (1+log(4N))/A². Divide by the
number of selected indices. Audit endpoints, density usage, and tails
before promoting the claim. General irregular suffix sets remain open.

Completed: endpoint and limiting audits passed. The scoped result is
proved in lemmas/L089-upward-averaging-at-dense-suffix-minima.md.
The irregular-density case is not proved by this draft or that lemma.
