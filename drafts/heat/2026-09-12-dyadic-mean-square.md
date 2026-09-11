# Dyadic mean-square checkpoint — 2026-09-12

The preceding L148 step is complete; existing changes are preserved.
For L138's S, remove its unit common phase and write weights
b_n(t)=c₀ n^(−2)exp(−log(n/sqrt(t/(2π)))²), frequency log n.
Target: integral from T to 2T of |S|² = K T^(−1/2)+O(T^(−1)log T).
Diagonal follows by sum/integral comparison with variation O(t^(−2)).
Off diagonal: products b_m b_n are unimodal in log t, so integration
by parts costs at most 4 sup(b_m b_n)/|log(m/n)|.
With N=sqrt(T/(2π)), envelope b_n≤C N^(−2)f(n/N),
f(x)=min(x²,x^(−4)). Split pairs at m=2n; near pairs use
1/log(m/n)≤2n/(m−n) and f(m/N)≤16f(n/N).
Summation should give O(N^(−2)log(2N)).
Resume by checking this lattice estimate, diagonal constant, and exclusion
of every uniform power lower bound with δ<3/4. These draft claims are
unproved until the full lemma is saved and reviewed.

Completed: the envelope summation and diagonal constant were checked and
recorded in L149. The candidate asymptotic is proved there; no uniform
lower bound was inferred from the mean square.
