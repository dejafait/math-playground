# Dual-cover liminf draft — 2026-09-11

Let S_n=sum_{k<=n<l} y_k m_l/(l-k)^2. Remove k<=n/2
and l>=2n: their combined contribution is bounded by
4 (sum y) sum_{l>n}m_l/l^2 + 4 W sum_{k>n/2}y_k, tending to zero.
For N=2^j and N<=n<2N, remaining sites lie in [N/2,4N].
Write a_j=sum of m_l/l^2 and b_j=sum y_k on this window.
Both block sequences are summable by finite overlap.

Candidate: the discrete centered maximal weak estimate supplies a cut n
where the local y and m maximal averages are <=24 b_j/N and
24 (sum local m)/N. Splitting l-k into powers of two bounds the
near cross sum by 25(j+3) times the product of those averages,
hence by an absolute constant times (j+3)a_j b_j.
The liminf of (j+3)a_j b_j is zero: otherwise summability of
sqrt(a_j b_j), by Cauchy-Schwarz, contradicts divergence of sum 1/sqrt(j+3).

Checkpoint: this is draft reasoning, not yet a proved DAG input.
Resume by auditing the finite discrete maximal covering estimate, distance
shell constants, boundary conventions, and then applying Lemma 118.

Audit completed in Lemma 119. The finite greedy interval proof gives the
needed weak bound, and the selected-cut constant can be taken as 230400.
The liminf excludes every summable cover; Lemma 118 then proves universal
payoff existence. Stochastic and heat-flow consequences are not part of
this completed step.
