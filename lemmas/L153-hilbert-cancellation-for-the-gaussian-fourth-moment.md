# Lemma 153: Hilbert cancellation for the Gaussian fourth moment

**Hypotheses.** Let `S(t)` and the positive coefficients `b_n(t)` be as in L149, and let `T` tend to infinity. Constants below are absolute.

**Conclusion.**

∫_T^(2T)|S(t)|⁴dt = O(T^(−2)log(2T)).                    (1)

There are constants a,c>0 such that, for every sufficiently large T,

meas{t∈[T,2T]: |S(t)|≥a T^(−3/4)} ≥ c T/log(2T).         (2)

This is not a positive-proportion estimate and gives no pointwise lower bound or nonvanishing assertion.

**Proof.**

Put N_t=sqrt(t/(2π)) and

a_k(t)=Σ_(mn=k)b_m(t)b_n(t).

After removing L149's common unit phase and squaring, |S(t)|⁴ is the squared modulus of

P(t)=Σ_(k≥1)a_k(t)exp(i(t−π/2)log k).                    (3)

The original series is absolutely uniformly convergent on [T,2T], and so are its square and every finite truncation used below.

### Two weighted Gaussian energies

We claim, uniformly for t∈[T,2T],

Σ_k k(1+|log(k/N_t²)|²)a_k(t)² = O(N_t^(−4)log(2N_t)).  (4)

Use L152's fixed-width energy estimate

D_β(M)=Σ_k A_k(β;M)²=O_β(M^(−6)log(2M)),                (5)

with center M=N_t. Expand the left side of (4) into the nonnegative sum over mn=pq=k. If x_1,…,x_4 are the four quantities log(n_j/M), put Q=Σ_j x_j² and z=log(k/M²)=x_1+x_2. Then |z|≤sqrt(2Q). Hence

exp(z)(1+z²)exp(−Q) ≤ C exp(−Q/2),                      (6)

because exp(sqrt(2Q))(1+2Q)exp(−Q/2) is bounded for Q≥0. Multiplying each expanded summand by k(1+z²)=M²exp(z)(1+z²), then applying (6) and Tonelli, bounds (4) by

C M²D_(1/2)(M)=O(M^(−4)log(2M)),

which proves the claim, including all infinite tails.

Direct differentiation gives an especially useful identity. Since

b_n'(t)=t^(−1)log(n/N_t)b_n(t),

every summand with mn=k has the same logarithmic factor, and therefore

a_k'(t)=t^(−1)log(k/N_t²)a_k(t).                         (7)

Termwise differentiation is valid on the compact interval: after one logarithmic factor the n-series is still dominated by a summable Gaussian-weighted series. From (4) and t asymp T,

E_0(t):=Σ_k k a_k(t)²=O(N^(−4)log(2N)),
E_1(t):=Σ_k k a_k'(t)²=O(T^(−2)N^(−4)log(2N)),           (8)

where N=sqrt(T/(2π)).

### Signed off-diagonal estimate

We use the standard Montgomery--Vaughan generalized Hilbert inequality in the following bilinear form. For distinct real λ_j, δ_j=min_(h≠j)|λ_j−λ_h|, and finite complex sequences x_j,y_j,

|Σ_(j≠h) x_j conjugate(y_h)/(λ_j−λ_h)|
 ≤ C(Σ_j |x_j|²/δ_j)^(1/2)(Σ_j |y_j|²/δ_j)^(1/2).       (9)

For λ_k=log k, the elementary inequality log(1+1/k)≥1/(2k) shows δ_k≥1/(2k). Thus the right side of (9) is at most

C(Σ_k k|x_k|²)^(1/2)(Σ_k k|y_k|²)^(1/2).               (10)

First truncate (3) at k≤K. Expanding its squared modulus and integrating, the diagonal is

∫_T^(2T)Σ_(k≤K)a_k(t)²dt.                               (11)

For the off diagonal, integrate each term by parts using λ_k−λ_l. At either endpoint u, (9)--(10), applied to x_k=y_k=a_k(u)exp(i(u−π/2)λ_k), bound the entire signed boundary sum by CE_0(u). For the integral containing the derivative of a_k a_l, apply the bilinear form twice, with the two choices

x_k=a_k'(t)exp(i(t−π/2)λ_k),  y_k=a_k(t)exp(i(t−π/2)λ_k)

and their reversal. Equations (8)--(10) bound its absolute value after integration by

C∫_T^(2T)E_0(t)^(1/2)E_1(t)^(1/2)dt
 =O(N^(−4)log(2N)).                                     (12)

The two endpoints have the same order. These estimates are uniform in K. Moreover, (8) makes the vectors and their derivative vectors converge in the weighted ℓ² norm, so (9) applied to differences proves convergence of every boundary and derivative bilinear form as K→∞. The diagonal passes by monotone convergence. Thus the integrated infinite expansion is justified without taking absolute values term by term.

By (5) at β=1, the diagonal (11), after K→∞, is

O(T N^(−6)log(2N))=O(N^(−4)log(2N)).                    (13)

Together (12), its endpoint bounds, and (13) prove (1), since N²=T/(2π).

For (2), use the same second-moment argument as in L152. If K_0>0 is L149's leading constant, choose a²=K_0/4. The complement of the set in (2) contributes at most (K_0/4)T^(−1/2) to the second moment, while L149 makes the full second moment at least (K_0/2)T^(−1/2) for large T. Cauchy--Schwarz on the indicated set, followed by (1), gives its measure at least cT/log(2T). ∎

## Scope, verification

The cancellation is in the integrated signed off diagonal; no cancellation or lower bound is asserted pointwise. The remaining logarithm is already present in the exact multiplicative diagonal from L151, although that fact is not needed for the upper bound. Consequently this method does not yield a positive proportion from the fourth moment.

Analytic verification checks the exact coefficient derivative, polynomial Gaussian absorption, all infinite Gaussian tails through L152's energy bound, the log-frequency separation, both integration-by-parts endpoints, the bilinear derivative terms, and convergence in weighted ℓ². No numerical certificate is needed.
**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
