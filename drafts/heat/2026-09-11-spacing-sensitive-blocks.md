# Spacing-sensitive block checkpoint — 2026-09-11

Initially UNPROVED. The preceding height-budget step is complete.
For B=S∩[N,2N), let d be its minimum spacing (set d=N for a
singleton). After expansion in height increments, the coefficient at r
is bounded by 2 sum_{n∈B,n≤r}1/(r−n+1). Ordering these n backwards
bounds this by 2[1+(1+log M)/d]. This replaces the logarithmic crowding
factor by a spacing-sensitive factor. Proposed average bound:
32 T_N D_N, where T_N=N[1+(1+log M)/d]/(M A_N²).
Resume by checking finite summation endpoints, singleton convention,
and the inverse-ratio budget argument. No universal liminf or example
in the entire residual regime is claimed.

Completed: the sharpened harmonic-number version and its selection
criteria are proved in `lemmas/L092-spacing-sensitive-height-budget-selection.md`.
The full residual problem remains unproved. The next task is to test
realizability of the new criterion within that residual regime.
