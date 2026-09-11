# Arbitrary height selection — 2026-09-11

Checkpoint: proposed extension, not yet promoted. For nonattained height
supremum H, restrict to b_i>H-delta and jump only to strictly higher
heights, with rates (x_j-x_i)^(-2)+(x_j+x_i)^(-2). L122's increasing
payoff has generator at most twice its forward bound: backward terms
are negative. Cap exits above index R at f(R) in a finite chain. Strict
height increase prevents repeated states, so infinitely many jumps
must leave every finite set, even though indices need not increase.
An eventual positive lower bound on E throughout this superlevel set
would force finite expected lifetime by telescoping bounded heights.

Resume audit: justify each full row, finite cutoff coupling despite
backward jumps, exit-time convergence, and selection with both heights
approaching H and contributions approaching zero. Treat an attained
supremum separately. No heat-uniform or RH conclusion is proposed.

Completed: the audited proof is stored in Lemma 124. All cutoff and
selection checks passed analytically; this draft is no longer an
unfinished claim. Heat-uniform conclusions remain unproved.
