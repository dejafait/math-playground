# Smooth amplitude cutoff audit — 2026-09-13

Draft checkpoint. Let H=exp(−i(t−π/2)log N)G_T and Q=|H|².
For w=χ(Q/M), with χ zero below 1 and one above 2, integration
by parts adds ∫w' A_m A_n exp(it log(m/n))dt/(i log(m/n)).
The finite window coefficients A_n=T^(3/4)b_n are O(T^(−1/4)),
with derivatives O(T^(−5/4)); frequency differences give pair sum
O(T^(1/2)log T) before division by interval length T.
Candidate bound: E Qw ≤ C/M + C T^(−1/2)log T (1+Var(w)).
After carrier removal E|H'|²=O(1) should follow by the same finite
window integration by parts, so Var(w)≤CT/sqrt(M).
This does not close a fixed-cutoff tail estimate. All claims here are
unproved until coefficient derivative, pair sum, and normalization audits
are completed. Resume by checking these estimates and documenting only
what the resulting upper bound establishes.

Completed as L156. The coefficient and centered derivative bounds hold.
Cauchy–Schwarz on |H H'| improves the draft variation estimate to CT/M,
but still leaves C sqrt(T)log(2T)/M in the tail bound. No fixed-cutoff
claim was promoted. The exact signed derivative remainder is preserved
in the lemma for a future cancellation audit.
