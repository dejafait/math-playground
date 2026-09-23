# Lemma 142: exponentially small negative Poisson modes

**Hypotheses.** Use the modes I_k(t), N=sqrt(t/(2π)), and τ=t−π/2 defined in L140, with real t≥π.

**Conclusion.** The entire negative-mode absolute sum satisfies

Σ_{m≥1}|I_{−m}(t)| ≤ sqrt(π)e N^(−2) exp(π²/4−πτ/2)/(2π)
                  = sqrt(π) exp(1+π²/2) t^(−1) exp(−πt/2).       (1)

In particular it is o(t^(−1)). Multiplication by C(t) from L140 preserves this conclusion. This bounds a part of the Poisson representation only; no lower bound for the positive-mode sum or the full series is asserted.

**Proof.**

Put θ=π/2. The real substitution x=N exp(y) gives, for every integer m≥1,

I_{−m}=N^(−1+iτ) ∫_R F_m(y)dy,
F_m(z)=exp(−z²+(−1+iτ)z+2πimN exp(z)).                         (2)

This is an entire function of z. For z=y+iv with 0≤v≤θ its modulus is exactly

|F_m(y+iv)|=exp(−y²+v²−y−τv−2πmN exp(y) sin v).              (3)

Since τ>0 and sin v≥0 on this interval, the vertical sides at y=±R have integrals in modulus at most

θ exp(−R²+R+θ²).

They tend to zero as R→∞. Both horizontal integrals converge absolutely, dominated by exp(−y²−y+θ²). Cauchy's theorem on the rectangle with vertices −R, R, R+iθ, −R+iθ, followed by these bounds, therefore proves

∫_R F_m(y)dy=∫_R F_m(y+iθ)dy.                               (4)

The contour argument is for each fixed m and t; it requires no uniform limiting interchange in m. Equations (2)–(4), |N^(iτ)|=1, and sin θ=1 give the uniform inequality

|I_{−m}|≤N^(−1) exp(θ²−τθ)
             ∫_R exp(−y²−y) exp(−2πmN exp(y))dy.             (5)

All integrands on the right are nonnegative. Tonelli's theorem permits summing their integrals, even before finiteness has been established. For a>0,

Σ_{m≥1} exp(−ma)=1/(exp(a)−1)≤1/a,

where the last inequality follows from exp(a)≥1+a. Applying this with a=2πN exp(y) proves

Σ_{m≥1}|I_{−m}|
 ≤ N^(−2) exp(θ²−τθ)/(2π) ∫_R exp(−y²−2y)dy
 = sqrt(π)e N^(−2) exp(θ²−τθ)/(2π).                         (6)

The final integral follows by completing the square, −y²−2y=1−(y+1)². This finite bound also proves the asserted absolute summability directly. Substituting θ=π/2, N²=t/(2π), and τ=t−π/2 gives (1). Finally |C(t)|=exp(π²/16) is constant by L140, so it does not change the little-o conclusion. ∎

## Scope, verification

The estimate is uniform over all negative integers, with no mode cutoff. Together with L140's zero-mode formula it removes nonpositive modes at the t^(−1) error scale. Positive modes outside the central range and cancellation among positive modes remain unresolved. No conclusion about a theta center lower bound, a common heat-interval strip, or RH follows.

Analytic validation checks the exact logarithmic substitution, the sign of the negative Fourier mode, the complex-shift modulus, both vanishing vertical sides, absolute horizontal domination, Tonelli's theorem, the geometric-series majorant, and the Gaussian constant. No numerical certificate is needed. Only L140 supplies mathematical inputs specific to this project.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
