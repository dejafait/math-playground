# Lemma 155: Gaussian-window reduction for truncated tails

**Hypotheses.** Use S and K from L149 and normalized expectation E_T from
L154. Put N=sqrt(T/(2π)), c₀=exp(π²/16), and fix 0<a<b<∞. Define

F_T(t)=T^(3/4)exp(−iπ log(N_t)/2)S(t),

G_T(t)=T^(3/4) Σ_(aN≤n≤bN) b_n(t) exp(i(t−π/2)log n),

R_T=F_T−G_T,

where N_t=sqrt(t/(2π)) and b_n(t)=c₀ n^(−2)exp(−log(n/N_t)²).
All sums are over positive integers and t∈[T,2T].

**Conclusion.** The normalized error satisfies

E_T|R_T|²=D(a,b)+O_(a,b)(T^(−1/2)log T),                 (1)

where

D(a,b)=c₀²(2π)^(3/2) ∫_1^2 ∫_((0,a)∪(b,∞))
 x^(−4) exp(−2(log x−(log u)/2)²) dx du.                (2)

In particular D(a,b)→0 as a↓0 and b↑∞. For every M>0,

E_T[|F_T|² 1_(|F_T|²>M)]
 ≤2E_T[|G_T|² 1_(|G_T|²>M/4)]+4E_T|R_T|².             (3)

Thus choose a,b with D(a,b)<K/64. If this moving core satisfies,
for some fixed M≥K/4 and all sufficiently large T,

E_T[|G_T|² 1_(|G_T|²>M/4)]≤K/16,                       (4)

then L154's tail target holds. Condition (4) remains unproved.
Truncation to any fixed finite set of indices instead has normalized
squared error tending to K, and cannot give arbitrarily small error.

**Proof.**

The exact representation and compact uniform absolute convergence follow
from L149. The complement of the window is independent of t on this dyadic
interval. Consequently L149's integration-by-parts argument for distinct
indices applies unchanged to the squared error. The absolute sum of its
integrated off-diagonal bounds is at most the bound for all indices,
O(T^(−1)log T). Multiplication by T^(1/2), the normalization for E_T|R_T|²,
makes its contribution O(T^(−1/2)log T). No cancellation claim for a
restricted time event is used here.

For the diagonal write t=Tu and n=Nx, and set

h_u(x)=x^(−4)exp(−2(log x−(log u)/2)²).

Uniformly for 1≤u≤2, this function has bounded supremum and bounded total
variation on (0,∞). Indeed its derivative has absolute integral

∫_R |−4−4(y−(log u)/2)| exp(−2(y−(log u)/2)²−4y)dy,

which is bounded uniformly on this compact u interval by Gaussian decay.
The extension of h_u to x=0 is zero. Multiplying by the indicator of
(0,a)∪(b,∞) adds at most two jumps bounded by the supremum. Comparing
mesh intervals of width 1/N with their sampled values therefore gives

Σ_(n<aN or n>bN) h_u(n/N)
 =N ∫_((0,a)∪(b,∞)) h_u(x)dx+O_(a,b)(1).

An endpoint coinciding with an integer changes the sum by at most two
bounded terms; hence the convention for strict complement inequalities
causes no problem. This estimate is uniform in u. Multiplying by c₀²N^(−4),
integrating in t, and normalizing by T^(1/2) yields (2), because
T^(3/2)N^(−3)=(2π)^(3/2). The error is O(T^(3/2)N^(−4))=O(T^(−1/2)).
Together with the off diagonal this proves (1).

The total integral in (2), with x ranging over (0,∞), is K: substitution
x=sqrt(u) exp(y) gives

∫₀^∞h_u(x)dx=u^(−3/2)sqrt(π/2)exp(9/8),

and ∫_1^2 u^(−3/2)du=2(1−1/sqrt(2)). This also proves integrability.
Dominated convergence then shows that the omitted integral tends to zero.

For (3), let A={|F_T|>sqrt(M)} and B={|G_T|>sqrt(M)/2}.
On A∩B use |F_T|²≤2|G_T|²+2|R_T|². On A outside B,
|R_T|≥|F_T|−|G_T|>|F_T|/2, so |F_T|²≤4|R_T|².
Integrating these disjoint pieces proves (3). For the chosen a,b,
(1) gives E_T|R_T|²≤K/32 eventually. Equations (3) and (4) then
bound the tail by 2K/16+4K/32=K/4. Since |F_T|²=X_T,
this is exactly the sufficient condition in L154.

Finally, let J be any fixed finite set of indices and define H_T by retaining
only J in F_T. For every fixed n∈J, uniformly on [T,2T],

T^(3/4)b_n(t)≤C_J T^(3/4)exp(−((log T)/2−C_J)²)→0.

Thus E_T|H_T|²→0. L149 gives E_T|F_T|²→K; Cauchy–Schwarz
bounds |E_T(F_T conjugate(H_T))| by the product of the two L2 norms,
which tends to zero. Expanding |F_T−H_T|² proves the last assertion. ∎

## Scope and verification

This proves a reduction for the actual Gaussian series, not a tail bound for
its moving core. The window contains order sqrt(T) indices. Its coefficients
and frequencies vary with T, so finite-polynomial boundedness for each T
supplies no uniform fixed cutoff. The off-diagonal bound above is on the
whole interval; it cannot simply be reused on the amplitude-selected set
{|G_T|²>M/4}, whose indicator has no established variation bound.
No positive-proportion improvement, nonvanishing, or RH result is claimed.

Verification is analytic: the mesh variation estimate with its two boundary
jumps, normalization, Gaussian integral, event split, and fixed-index limit.
No numerical certificate is needed.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
