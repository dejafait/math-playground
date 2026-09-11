# Actual near sums at sparse suffix minima — 2026-09-11

Candidate scoped result, initially UNPROVED: enumerate the suffix set as
s_l and put a_n=x_n/sqrt(n), c_l=s_l/x_{s_l}², and
epsilon_l=a_{s_{l+1}}/a_{s_l}−1. If Σ_l c_l<∞, the actual near sum
has liminf zero through this set. This includes s_{l+1}≥q s_l eventually
for any fixed q>1.

Reasoning checkpoint: the minimum over indices j>s_l is attained at
s_{l+1}, so every such a_j≥a_{s_{l+1}}. For 1≤k≤s_l this should give
x_{s_l+k}−x_{s_l}≥x_{s_l}(epsilon_l+k/(3s_l)). Integrating the decreasing
square reciprocal bounds the near sum by 3H c_l/epsilon_l when
epsilon_l>0. Since a_{s_l}→∞, Σ epsilon_l=∞; summability of c_l should
force liminf c_l/epsilon_l=0 along positive epsilon_l.

Resume: audit tail-minimum identification including ties, the integral
bound, subsequence selection, and the disjoint-block proof of Σc_l<∞
under geometric spacing. This does not yet settle suffix sets without
that summability condition. No unrestricted assertion is proved.

Completed audit: the scoped claim, including the full upward contribution
and geometric-spacing case, is proved in
`lemmas/L088-actual-upward-subsequence-at-sparse-suffix-minima.md`.
The unrestricted claim remains unproved; this draft is superseded by
the canonical proof for the stated sufficient condition.
