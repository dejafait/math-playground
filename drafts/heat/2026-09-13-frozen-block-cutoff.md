# Frozen block cutoff checkpoint — 2026-09-13

The prior L168 step is complete; existing changes are preserved.
For midpoint c_j and d_n(t)=A_n(t)−A_n(c_j), L156 gives
sup|d_n|≤C h T^(−5/4), sup|d_n'|≤C T^(−5/4).
The diagonal block mean square of the difference sum is O((h/T)^2).
Integration by parts bounds each off-diagonal integral by
C h² T^(−5/2)/|log(m/n)|, including both endpoints.
Thus E_j|difference|²≤C(h/T)² K, K=1+sqrt(T)log T/h.
Both original and frozen sums have block energy O(K).
Cauchy–Schwarz then suggests E_j|Q−Q_frozen|≤C(h/T)K;
χ''' gives a cutoff difference ≤Cχ h K/(TM).

Resume: audit the product derivative and all normalizations, combine with
L168 and |W_j−bar W|≤C(log T)^4, and store L169. At h≈T^(3/4)
the anticipated covariance error is Oχ((1+1/M)T^(−1/4)(log T)^4).
The frozen cutoff means themselves remain unevaluated; no signed
cancellation claim is proved at this checkpoint.

Recovery audit: the product derivative is bounded by C h T^(−5/2),
so its block integral and both endpoints cost C h² T^(−5/2).
After the frequency sum and division by h this is
C h T^(−3/2) log T, exactly (h/T)² times sqrt(T)log T/h.
The remaining work is to write the full L169 proof and validate the graph.

Completed: audited estimates and full proof are stored in L169. The frozen
signed correlation remains unproved; the current next action is in PROGRESS.md.
