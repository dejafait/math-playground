# Arbitrary-coordinate payoff checkpoint — 2026-09-11

Scope: transfer the finite-capacity alternative to actual distances, without
any cell grouping. This does not yet decide universal payoff existence.
For i≤n set A_in=Σ_(j>n)(x_j−x_i)^(-2), and zero otherwise.
Each entry is finite and A_nn>0, but there is no uniform diagonal bound.
Finite LP compactness only needs individual positive diagonals. Dual
feasibility follows by setting y_n=1/A_nn. The mixture and diagonal-limit
arguments therefore survive. A strictly increasing bounded correction
can be made with increments e_n=2^(-n)/(1+max_(i≤n) A_in), giving every
row at most one. The first row supplies Σ_j f(j)/x_j²<∞.

Resume checkpoint: audit this correction, write the full alternative as
L121, and record that exclusion (or construction) of a summable actual-
distance cover remains unproved. Do not promote universal payoff existence.

Completed: the scoped alternative and correction are now proved in L121.
The universal cover-exclusion claim remains unproved. The active next action
is recorded only in PROGRESS.md.
