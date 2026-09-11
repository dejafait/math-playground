# Lemma 144: Gaussian-weighted dual Dirichlet series

**Hypotheses.** Use F,H,S from L138, C,N,τ from L140 and M_k from L143, for real t≥π. Put Q=τ/(2π), A=Q/N and, for complex s,

D(s;A)=Σ_{k≥1} k^(−s)exp(−log²(k/A)),
B(t)=Q^(−1)sqrt(2π/τ)exp(iτ(log Q−1)−iπ/4).

All logarithms of positive numbers are real.

**Conclusion.** D is entire in s for each fixed A>0, and

Σ_{k≥1}M_k(t)=B(t)D(−1+iτ;A),                              (1)
S(t)=C(t)B(t)D(−1+iτ;A)+O(t^(−3/2)),                       (2)
F(−1,t+3i/2)/H(t)=C(t)B(t)D(−1+iτ;A)+O(t^(−1)).           (3)

Here |CB|=e^(π²/16)(2π)^(3/2)τ^(−3/2). Thus (3) is equivalently

F(−1,t+3i/2)/(H(t)C(t)B(t))=D(−1+iτ;A)+O(sqrt(t)).        (4)

For A≥2 the absolute mass W(A)=Σ_{k≥1}k exp(−log²(k/A)) satisfies

c A²≤W(A)≤C₀ A²,   max_{k≥1} k exp(−log²(k/A))≤e^(1/4)A.  (5)

No lower bound for |D(−1+iτ;A)| is asserted. In particular, this transformation and the absolute-mass estimates do not supply a lower bound overcoming the error in (3).

**Proof.**

On any compact set of s, choose R with Re(s)≥−R. For sufficiently large k, k^R exp(−log²(k/A))≤k^(−2), since a quadratic in log k dominates every fixed linear function of log k. This proves locally uniform absolute convergence and hence entire dependence by the Weierstrass theorem. The same argument justifies absolute convergence at the evaluation point in (1).

Since X_k=Q/k and r_k=A/k in L143, its amplitude becomes

X_k^(−1)exp(−log² r_k)=Q^(−1)k exp(−log²(k/A)),

and its phase becomes

exp(iτ(log X_k−1)−iπ/4)
 =exp(iτ(log Q−1)−iπ/4)k^(−iτ).

Multiplying and summing proves (1) without a rearrangement of a conditionally convergent series. L143 bounds the absolute summed positive-mode error by O(t^(−3/2)). L142 bounds the negative modes exponentially, and the explicit zero mode in L140 is also exponentially small. Substitution into the exact Poisson identity in L140 proves (2). Combining (2) with L138 proves (3). Taking the modulus of B gives the stated constant, and τ is comparable to t, proving (4). Division is only by the explicit nonzero B,C,H, never by D.

For the lower bound in (5), there are at least A/2 integers in [A,2A] when A≥2. Each contributes at least A exp(−log²2). For the upper bound split at A. For k≤A the exponential is at most one and the sum of k is O(A²). For k>A, put y=log(k/A)>0. Since −y²+3y≤9/4,

k exp(−y²)≤e^(9/4)A³ k^(−2).

Integral comparison gives Σ_{k>A}k^(−2)≤2/A for A≥2, which completes the upper bound. Finally, for any k, put y=log(k/A), now of either sign. Its weight is A exp(y−y²)≤A e^(1/4), proving the maximum estimate.

Consequently any subset of m terms has absolute mass at most m e^(1/4)A, and hence at most a constant times m/A of W(A). As A is comparable to sqrt(t), every subset with m=o(sqrt(t)) has vanishing fraction of the absolute mass. In particular no such subset can dominate its complement by the reverse triangle inequality: even its absolute mass is eventually less than the complement's absolute mass. This is a limitation of that sufficient test, not a claim that the actual complex sum vanishes.

The positive weights multiply phases exp(−iτ log k). Positivity of the weights and absolute convergence yield only |D|≤W(A). To overcome an unspecified O(sqrt(t)) error in (4) by the reverse triangle inequality one would need a quantitative bound |D|≥(K+ε)sqrt(t), with K a valid error constant and ε>0, or a stronger bound such as |D|≥d t^(1/2+η) for some d,η>0. The latter would give |F/H| bounded below by a constant times t^(−1+η). Neither bound has been proved. A mere Ω(sqrt(t)) assertion with an unspecified small constant does not suffice. ∎

## Scope and formalization obligations

This is a re-expression and cancellation audit, not a proof that a lower bound is impossible. The entire smoothed series evaluated at Re(s)=−1 is not the ordinary absolutely convergent zeta Dirichlet series. No Euler product or reciprocal-zeta lower bound has been transferred to it. The center lower bound, heat-interval strip, and RH remain unresolved.

Analytic verification checks the phase sign, the Q and τ prefactors, compact convergence, the nonpositive-mode errors, the integer count in [A,2A], the Gaussian maximum, and the error scale after division. No numerical certificate is required. Formalization would require these identities and elementary estimates, locally uniform holomorphic convergence, and the cited additive expansions. No unproved lower bound is a mathematical input.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
