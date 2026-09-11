# Exact multiplicative diagonal checkpoint — 2026-09-12

Work through L150 was complete on entry and is preserved. Parametrize
mn=pq uniquely as m=gr, p=gs, n=hs, q=hr with (r,s)=1.
Then D(N)=sum_(r,s)=1 (sum_g b_gr b_gs)^2, where
b_n=c0 n^-2 exp(-log(n/N)^2). The inner sum equals
c0²(rs)^-2 exp(-log(r/s)^2/2) H(N/sqrt(rs)), with
H(X)=sum_g g^-4 exp(-2log(g/X)^2).
Target: D(N) comparable to N^-6 log N. Prove H(X)≤C X^-3
min(1,X²) using integral plus variation for X≥1 and a Gaussian
power bound for X<1; prove H(X)≥c X^-3 for X≥2 by g in [X,2X].
Upper bound via dyadic blocks in r,s; lower bound via coprime pairs
in disjoint squares [R,2R), R dyadic and large, R≤N/4.
Coprime density follows by the union bound over common divisors d≥2,
with sum d^-2≤3/4 and error O(R log R). These are draft claims pending
full verification. Resume with the dyadic upper tail and density details.

Completed in L151. Both bounds hold, giving the exact diagonal order
T^(-2)log T. The full fourth moment remains undetermined because its
integrated off-diagonal contribution is signed. No numerical evidence
was used. The one direct mathematical input is L149's weight definition.
