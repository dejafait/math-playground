# Blockwise cutoff covariance checkpoint — 2026-09-13

Prior L167 is complete. Partition [T,2T] into equal blocks of length
h=T/ceil(T/H), so H/2≤h≤H for 1≤H≤T. With f=χ''(Q/M),
block means f_j,W_j, the covariance splits exactly into
Σ(h/T)(W_j−bar W)f_j plus within-block centered products.
The latter are O(H(log T)^4/T), using |W'|≤C(log T)^4/T.

Resume: verify local mean square by L156's finite-sum integration by
parts on each block; its normalized error is O(sqrt(T)log T/h).
This controls only a first moment of Q and transition mass, not signed
cutoff means. Give explicit same-first-moment probability laws with
unequal χ'' expectations, carefully distinguished from the actual Q.
Then store L168, archive the inference failure, update graph and history,
and validate. No cutoff cancellation claim is proved at this checkpoint.

Completed: L168 contains the exact decomposition, local estimate, and
first-moment information obstruction. No signed cancellation is claimed.
