# Sparse suffix-bound obstruction — 2026-09-11

Candidate: N_0=0 and N_k=4^k for k≥1. For N_{k−1}<n≤N_k,
set x_n²=k²(N_k+n)/2. The ratio x_n²/n decreases strictly within
each block and has endpoint value k²; hence the suffix set should
be exactly {N_k:k≥1}. Reciprocal-square mass per block is at most
2/k². Place Δ_{N_k}=2^{−N_k}+k²/4^k and Δ_r=2^{−r} elsewhere.
Then the first summand gives T_{N_k}≥1 and increments are summable.

Checkpoint: candidate UNPROVED pending audit of block boundaries,
exact suffix set, and series convergence. Resume by writing a standalone
counterexample proof if these checks hold. This only refutes selection
for T, not the full upward liminf assertion.

Completed audit: the construction and exact suffix set are proved in
`lemmas/L087-sparse-suffix-minima-obstruct-increment-bound-selection.md`.
The same proof also establishes that the actual upward contribution
vanishes at the endpoints. The candidate is superseded by that proof.
