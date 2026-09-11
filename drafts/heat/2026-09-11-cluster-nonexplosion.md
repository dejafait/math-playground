# Cluster nonexplosion draft — 2026-09-11

Inspected the completed L108 checkpoint and preserved all existing changes.
The requested summability-only cluster question is not yet resolved.

Scoped candidate: arbitrary finite distinct points in [k,k+1/4], with
m_k≤M k^alpha, 0≤alpha<1. Take a cluster-constant payoff f=k^p,
0<p<1−alpha. Internal generator terms vanish exactly. Between clusters
l>k the distance is at least (3/4)(l−k). Near terms are bounded by a
constant times k^(alpha+p−1)(1+log k); far terms by a constant times
k^(alpha+p−1). Both are bounded. Cap the payoff at cluster R and use
the finite-state exit argument from L108; finitely many points per
cluster make the stopped state space finite despite tiny internal gaps.

Checkpoint: candidate UNPROVED pending detailed bounds and exit audit.
Resume by checking constants, all exit destinations, and reciprocal-square
summability, then store the scoped theorem. The arbitrary summable-count
case remains explicit; for example floor(k/log(k+1)^2) exceeds every
sublinear power bound eventually.

Completed audit: the polynomial-count candidate is proved and stored in
Lemma 109. Near and far estimates, capped payoff, all retained rates,
and the holding-time coupling were checked. The summability-only case
remains unproved; this draft contains no additional proved assertion.
