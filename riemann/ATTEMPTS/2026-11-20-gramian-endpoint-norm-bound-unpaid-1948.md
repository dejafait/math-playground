# Fixed-horizon Gramian1948: endpoint norm estimate is insufficient

WHY IT FAILS: The exact endpoint and energy normalization in
[C029b](../lemmas/C029b-dynamical-gramian-endpoint-reduction.md)
cancels the apparent explicit 1/T gain. The all-coefficient semigroup
estimate proves r_d<=2*A/(1-exp(-2*A*d^2)), with the fixed
A=exp(b_1)*F(1)>1. This is only O(1), whereas the escape threshold
is o(1); an upper bound with a positive limiting right side also
does not prove a positive liminf. Thus this norm-only attempt settles
neither alternative. It does not stop the Gramian schedule, produce
an off-line zero, or pay the full trace norm.

The canonical result also retains the exact signed endpoint derivative
vector and energy-determinant ratio. Controlling that ratio is the
specific unresolved bound for a refined attempt at the same fixed
horizon; merely repeating the unsigned semigroup bound or changing
the horizon supplies no new evidence. C028h/i/o/p and C029a remain
scoped contrasts. No root reality, bounded conditioning, spectral
dominance or numerical coefficient contract has been assumed.
