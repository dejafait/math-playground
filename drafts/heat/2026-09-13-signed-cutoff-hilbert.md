# Signed cutoff Hilbert audit — 2026-09-13

Checkpoint before final verification. Use L156's finite-window A_n, λ_n,
H, Q, w. Set z_n=A_n exp(i(t−π/2)λ_n) and
B=Σ_(m≠n) z_m conjugate(z_n)/(i(λ_m−λ_n)).
B is real by pairing. Define C by replacing the numerator by
(A_m' A_n+A_m A_n')exp(i(t−π/2)(λ_m−λ_n)).
Candidate exact identity: B'=Q−D+C with D=Σ A_n².
Hilbert gives |B|=O(N), |C|=O(N/T), since separation is ≥1/(bN)
and Σ A_n²=O(1), Σ |A_n'|²=O(T^(−2)). Thus
E(Qw)=E(Dw)+[wB]/T−E(wC)−E(w'B).
The signed remainder retains its correlation but its Hilbert/variation
bound is O(N/M). This removes the logarithm but does not close the tail.
Integrating that remainder back uses B'=Q−D+C and returns the original
weighted moment, so no independent correlation estimate results.
Resume by checking signs, normalizations, and the precise scope of this
method limitation. These candidate assertions are not yet proved inputs.

Completed as L157 after checking all signs and normalizations. The
Hilbert bound removes only the logarithm; no uniform correlation bound
is proved. The exact reverse integration is a tautology.
