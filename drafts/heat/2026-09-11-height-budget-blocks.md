# Height-budget block selection — 2026-09-11

Draft checkpoint, initially UNPROVED. Preserve the block height mass
D_N=b_{4N}−b_N in the proof of Lemma 90: average Q≤16 R_N D_N,
where R_N=N(2+log M_N)/(M_N A_N²). On dyadic N=2^k the D_N
have total sum at most 2H, since every height increment belongs to at
most two such half-open intervals. Thus divergence of Σ_k 1/R_{2^k}
over nonempty blocks should force liminf R_{2^k}D_{2^k}=0.
For arbitrary blocks, a bounded-ratio subsequence suffices directly
because D_N→0. This addresses a scoped part of the current action,
including ratios bounded above and below, not every ratio bounded below.
Resume by auditing overlap endpoints, the divergent-weight selection,
and full-contribution tails before promoting the claim.

Completed audit: the claims above are proved in
`lemmas/L091-height-budget-selection-on-irregular-blocks.md`.
This draft is superseded for those claims; the residual regime remains
unproved and is stated in the lemma qualifications.
