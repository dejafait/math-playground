# Lemma 149: dyadic mean square with moving weights

**Hypotheses.** Let S(t) be the series defined in L138, for real t>0. Put c₀=exp(π²/16) and

K=2(1−1/sqrt(2))(2π)^(3/2)c₀² sqrt(π/2)exp(9/8)>0.

**Conclusion.** As T tends to infinity,

∫_T^(2T)|S(t)|²dt=K T^(−1/2)+O(T^(−1)log T).                 (1)

In particular no constants d>0 and δ<3/4 can satisfy |S(t)|≥d t^(−δ) for every sufficiently large t. This excludes δ=1/2. At δ=3/4 such a bound would require

d²≤(2π)^(3/2)c₀² sqrt(π/2)exp(9/8).

No uniform lower bound, including at or above 3/4, is asserted.

**Proof.**

Set N_t=sqrt(t/(2π)) and

b_n(t)=c₀ n^(−2)exp(−log(n/N_t)²).

Expansion of the square in L138 gives exactly

S(t)=exp(iπ log(N_t)/2) Σ_(n≥1)b_n(t)exp(i(t−π/2)log n).

The common phase has modulus one. On each compact positive t interval the sum converges absolutely uniformly, for b_n≤c₀n^(−2). Thus its squared modulus can be integrated termwise as an absolutely convergent double sum.

### Diagonal

For g_t(x)=c₀²x^(−4)exp(−2log(x/N_t)²), extended by zero at x=0, the substitution y=log(x/N_t) gives

∫₀^∞g_t(x)dx=c₀²N_t^(−3)∫_R exp(−2y²−3y)dy
 =c₀²N_t^(−3)sqrt(π/2)exp(9/8).

Also ∫₀^∞|g_t'(x)|dx=C N_t^(−4), with a finite constant C: differentiating and substituting gives the integral of
c₀²|−4−4y|exp(−2y²−4y).
The fundamental theorem of calculus on each [n−1,n] therefore bounds the difference between Σg_t(n) and its integral by C N_t^(−4). Gaussian decay justifies the zero endpoint and all limits. Integration in t yields the main term in (1), since

∫_T^(2T)t^(−3/2)dt=2(1−1/sqrt(2))T^(−1/2),

and an O(T^(−1)) error.

### Off diagonal with the weights retained

Take T≥2π and N=sqrt(T/(2π))≥1. Throughout [T,2T], log(N_t/N) lies in [0,log(2)/2]. Gaussian decay implies, with an absolute constant C,

b_n(t)≤B_n:=C N^(−2)f(n/N),  f(x)=min(x²,x^(−4)).          (2)

Indeed the scaled weight is c₀x^(−2)exp(−(log x−u)²), with u in that fixed compact interval. Its ratio to either stated power tends to zero at the corresponding end, uniformly in u, and is bounded on the intervening compact set.

For m≠n the positive product p(t)=b_m(t)b_n(t) is unimodal: its logarithm is a constant minus (log m−log N_t)²−(log n−log N_t)², a concave quadratic in the strictly increasing variable log N_t. Consequently its total variation on [T,2T] is at most 2 sup p. Integration by parts, including both endpoints, gives

|∫_T^(2T)p(t)exp(it log(m/n))dt|≤4B_mB_n/|log(m/n)|.       (3)

The extra constant phase exp(−iπ log(m/n)/2) has no effect.

We now bound the sum in (3), explicitly including the infinite tails. Elementary power sums give Σ_(n≥1)f(n/N)=O(N): below N use (n/N)² and above N use (n/N)^(−4). For m≥2n the denominator is at least log 2, so these pairs contribute O((ΣB_n)²)=O(N^(−2)).

For n<m<2n, log(m/n)≥(m−n)/(2n), and f(m/N)≤16f(n/N). The latter follows directly on each side of x=1 and across it, or from the bound 4 on the absolute logarithmic slopes of f. Hence these pairs contribute at most

C N^(−4) Σ_(n≥1)n f(n/N)² log(2n)=O(N^(−2)log(2N)).        (4)

For completeness, below N the sum before multiplication by N^(−4) is bounded by N^(−4)Σ_(n≤N)n⁵log(2n)=O(N²log(2N)). Above N it equals N⁸Σ_(n>N)n^(−7)log(2n)=O(N²log(2N)), by integral comparison (with a harmless adjustment for 1≤N<2). The reverse ordered pairs give the same estimate. This proves absolute summability of the integrated off-diagonal bounds and yields O(T^(−1)log T). Together with the diagonal it proves (1).

If the asserted uniform power lower bound held, then

∫_T^(2T)|S(t)|²dt≥d² T^(1−2δ)∫_1^2u^(−2δ)du.

The fixed integral is strictly positive. Comparison with (1) is impossible for δ<3/4. At δ=3/4, multiply by T^(1/2) and take the limit; dividing by 2(1−1/sqrt(2)) gives the stated necessary constant bound. ∎

## Scope and verification

The result controls an average, not the minimum. It leaves δ≥3/4 undecided and does not establish center nonvanishing or RH. Analytic verification checks the exact phase, Gaussian diagonal constant, integrable derivative error, product unimodality despite the moving weights, endpoint terms, and the infinite off-diagonal lattice sums. No numerical certificate or external theorem is required.
**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
