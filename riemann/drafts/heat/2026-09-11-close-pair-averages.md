# Close-pair averaging obstruction — 2026-09-11

Checkpoint before final proof. Candidate coordinates are x_{2k−1}=2^k,
x_{2k}=2^k+4^{−k}, with b_n=1−2^{−n}. The immediate successor of
each odd index has equal horizontal and vertical gaps 4^{−k}, hence
contributes 4^k to E. Every block [N,2N) for N≥2 contains an odd n≥N,
giving average at least 2^{N+1}/N. Reciprocal squares sum to at most
2Σ4^{−k}. These observations should refute unrestricted block averaging.

Resume by checking the product via Lemma 74 and all full-series tails,
then writing a canonical counterexample. Also check the even-index upper
bound: for j>2k, x_{2k}/x_j≤3/4, so E(w_{2k})≤34Σ_{j>2k}x_j^{−2}
≤(68/3)4^{−k}. Thus the example does not refute liminf E=0.
These are draft claims pending the final audit; not DAG inputs.

Completed: the candidate and even-index bound were audited and proved in
Lemma 83. No unfinished claim remains in this checkpoint.
