# Lemma 141: uniform central-mode stationary phase

**Hypotheses.** Use I_k(t), N=sqrt(t/(2π)), and τ=t−π/2 from L140. Let t≥π, and let k be a positive integer satisfying N/2≤k≤2N. Set X_k=τ/(2πk) and r_k=X_k/N. All logarithms below are real logarithms of positive numbers.

**Conclusion.** As t→∞, uniformly over these integers,

I_k(t)=M_k(t)+O(X_k^(-1)τ^(-3/2)),                         (1)

where

M_k(t)=X_k^(-1)sqrt(2π/τ)exp(−log² r_k)
        ·exp(iτ(log X_k−1)−iπ/4).

In particular,

Σ_{N/2≤k≤2N} I_k(t)=Σ_{N/2≤k≤2N} M_k(t)+O(t^(-3/2)).       (2)

The sum of the absolute individual errors also is O(t^(-3/2)), hence o(t^(-1)). Multiplication by the factor C(t) in L140 preserves this order. Neither a lower bound for this central sum nor control of the other modes is asserted.

**Proof.**

Write X=X_k and r=r_k. Since τ/t∈[1/2,1] for t≥π, the range of k implies r∈[1/4,2]. Substituting x=Xu in L140's integral gives exactly

I_k=X^(-1+iτ)J_r(τ),
J_r(τ)=∫₀^∞ a_r(u)exp(iτφ(u))du,
a_r(u)=u^(-2)exp(−log²(ru)),   φ(u)=log u−u.               (3)

We prove, uniformly for r∈[1/4,2],

J_r(τ)=exp(−iτ−iπ/4)sqrt(2π/τ)a_r(1)+O(τ^(-3/2)).        (4)

Choose a fixed smooth cutoff χ supported in (1/2,3/2) and equal to one on a neighborhood of 1. On this interval introduce

v=sgn(u−1)sqrt(2(u−1−log u)).

Taylor expansion at 1 shows this is smooth there with dv/du=1 at 1. Away from 1, differentiating v²/2=u−1−log u gives v(dv/du)=(u−1)/u, so dv/du>0 throughout the interval. Thus it is a smooth change of variable with smooth inverse and φ(u)=−1−v²/2. The compact part of (3) becomes

exp(−iτ)∫_R g_r(v)exp(−iτv²/2)dv,
g_r(v)=χ(u(v))a_r(u(v))du/dv,

extended by zero beyond its compact support. These functions have a common compact support and uniform bounds on every fixed number of derivatives, since r ranges over a compact interval of positive numbers. Also g_r(0)=a_r(1).

Here is a direct uniform Gaussian estimate. For a smooth compactly supported g use the convention

ĝ(ξ)=∫_R g(v)exp(−iξv)dv.

Fourier inversion and the Gaussian identity give

∫ g(v)exp(−iτv²/2)dv
 =sqrt(2π/τ)exp(−iπ/4)(1/(2π))
    ∫ ĝ(ξ)exp(iξ²/(2τ))dξ.                               (5)

To justify the oscillatory Gaussian manipulation, first multiply the integrand by exp(−εv²), ε>0. Absolute integrability permits inversion and Fubini. The inner integral equals sqrt(π/(ε+iτ/2))exp(−ξ²/(4(ε+iτ/2))), using the square root continuous from the right half-plane. Its modulus is at most sqrt(2π/τ). Dominated convergence against |ĝ| and on the compact support of g then proves (5). The complex Gaussian formula itself follows from the real Gaussian integral by analytic continuation in its quadratic coefficient in the right half-plane and its linear coefficient in C; Gaussian domination on compact parameter sets justifies this continuation.

Since |exp(iq)−1|≤|q| for real q, (5) and Fourier inversion at zero imply an error bounded by

sqrt(2π/τ)/(4πτ) ∫ ξ²|ĝ(ξ)|dξ.

This integral is uniformly bounded for g=g_r: on |ξ|≤1 use ||g_r||_1; on |ξ|>1 integrate by parts four times to use |ĝ_r(ξ)|≤|ξ|^(-4)||g_r^(4)||_1. This proves (4) for the compact part, with uniform O(τ^(-3/2)) error.

It remains to bound the noncompact part. Put b_r=(1−χ)a_r and define Db=(b/φ')'. The functions involving 1/φ' are defined as zero in the neighborhood of 1 where b_r vanishes. Twice integrating by parts yields

∫₀^∞ b_r(u)exp(iτφ(u))du
 =(iτ)^(-2)∫₀^∞ D²b_r(u)exp(iτφ(u))du.                  (6)

For clarity, all the endpoint and integrability conditions here are uniform. Every fixed derivative of a_r is u^(-2−j)exp(−log²(ru)) times a polynomial in log(ru). With log r in a compact interval, these derivatives decay faster than any prescribed positive power of u at zero, and faster than any prescribed negative power at infinity, uniformly in r. Away from the removed neighborhood of 1, 1/φ'=u/(1−u) and its fixed derivatives have at most polynomial growth at the two ends. Consequently b_r/φ' and (Db_r)/φ' tend to zero at both endpoints, and ||D²b_r||_1 is uniformly bounded. On the intervening compact sets all denominators are bounded away from zero. Thus (6) is O(τ^(-2)), which is within the error in (4) for τ≥1.

Equation (3), a_r(1)=exp(−log²r), and |X^(iτ)|=1 now prove (1). There are O(N) integers in the range and each X_k≥N/4. Hence the absolute sum of the remainders is

O(N·N^(-1)τ^(-3/2))=O(t^(-3/2)),

proving (2). L140 gives |C(t)|=exp(π²/16), a fixed constant. ∎

## Scope and verification

Each leading term is O(t^(-1)); summing its modulus gives only O(t^(-1/2)). This does not bound the complex sum away from zero. Modes outside the specified central range are not included in (2), even though L140 represents the full series. No inference about a theta center lower bound, heat-interval strip, or RH follows from (2) alone.

Analytic verification checks the rescaling, phase sign, Morse-coordinate Jacobian, uniform fourth-derivative Fourier moment, Gaussian regularization, two endpoint integrations by parts, and absolute summation of errors. No numerical certificate is required. Formalization would require these uniform estimates, the smooth cutoff and coordinate inverse, Fourier inversion for compactly supported smooth functions, and the dominated Gaussian identity. No unproved cancellation statement is used.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
