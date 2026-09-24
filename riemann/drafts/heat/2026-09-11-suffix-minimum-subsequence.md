# Suffix-minimum subsequence — 2026-09-11

The unrestricted liminf question remains unproved. Scoped candidate:
under the monotone quartet hypotheses, add H−b_n≤C/n eventually.
Reciprocal-square summability implies x_n/sqrt(n)→∞. Therefore every
suffix of this multiplier sequence attains its minimum, yielding
unbounded indices n such that x_j≥x_n sqrt(j/n) for all j≥n.
At such indices split j=n+k into 1≤k≤n and k>n. In the first range,
x_j−x_n≥x_n k/((sqrt(2)+1)n), giving U_near≤12 h_n n²/x_n²
using sum k^{-2}≤2 and (sqrt(2)+1)²<6 (constant should be 24,
including the leading 2). In the second range x_j−x_n≥(1−1/sqrt(2))x_j,
so U_far is bounded by a constant times H sum_{j>2n}x_j^{-2}.
The candidate near bound tends to zero when n h_n is bounded because
n/x_n²→0. Reflected terms vanish by Lemma 74.

Resume: audit constants, suffix-minimum existence and unboundedness,
and the summability implication with finite blocks; then write the
scoped lemma if valid. This draft is not a proved DAG input. It does
not settle arbitrary slow height convergence.

Completed audit: Lemma 84 proves the scoped claim with the simpler near
constant 36 and far constant 32. It also records the sufficient condition
h_n n²/x_n²→0 along suffix minima. No draft assertion remains pending;
the unrestricted slow-height case remains open.
