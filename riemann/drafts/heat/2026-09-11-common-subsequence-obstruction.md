# Draft checkpoint — 2026-09-11

Take P equal to all positive integers, so x_n=n^(3/4). Given any
proposed infinite index set S, choose n_l in S with n_l>=2^(4l)
and n_(l+1)>n_l+1. Put Δ_r=2^(-r)+Σ_l 1_{r=n_l}n_l^(-1/2),
b_1=1, and b_n=1+Σ_{r<n}Δ_r. All heights strictly increase to a
finite H. At a marked index the successor alone gives a fixed positive
lower bound for the full upward contribution: its squared horizontal
gap is <=(9/16)n_l^(-1/2), while Δ_(n_l) is between n_l^(-1/2)
and 2n_l^(-1/2). Thus E>=32/73. This disproves a common subsequence
for this P, with the height sequence chosen after the proposed indices.

Completed checkpoint: constants, quantifiers and product hypotheses were
audited and the result was stored in Lemma 102. This draft is retained
as the intermediate reasoning record; it is not a DAG input.
