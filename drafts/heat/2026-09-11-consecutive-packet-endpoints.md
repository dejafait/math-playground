# Consecutive packet endpoints — 2026-09-11

Draft checkpoint: let n=U_k+d_k−1 and T=U_(k+1) in Lemma 98.
Every j>n has x_j/sqrt(j)≥T^(1/4), whereas x_n=n^(3/4).
Thus x_j−x_n≥sqrt(n)(T^(1/4)−n^(1/4)). For the n terms in
Q_n this suggests Q_n≤H/(T^(1/4)−n^(1/4))²→0, for every
permitted height sequence, along the same fixed endpoints.

At this checkpoint the bound and its limit remain unproved. Resume by
checking normalized coordinates in the gap and all later packets,
then apply Lemma 84's far and reflected tail estimates.

Completed: the normalized-coordinate bound and both limits are proved
in Lemma 99. The endpoint near sum is at most 4H/U_(k+1)^(1/2).
