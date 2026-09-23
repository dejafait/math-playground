# Lemma 17: split Mellin integral with entire remainder

**Hypotheses.** ψ is as in Lemma 16. For s∈C put

I(s)=∫_1^∞ψ(x)(x^{s/2}+x^{(1-s)/2})dx/x,

where all powers use the real logarithm of x.

**Conclusion.** I is entire, I(s)=I(1-s), and for Re(s)>1,

π^{-s/2}Γ(s/2)ζ(s)=1/(s-1)-1/s+I(s).

**Proof.** For σ=Re(s)>1, the integral of the absolute values of the summands in ∫_0^∞Σ_{n≥1}e^{-πn²x}x^{s/2-1}dx is

Σ_{n≥1}∫_0^∞e^{-πn²x}x^{σ/2-1}dx=π^{-σ/2}Γ(σ/2)Σ_{n≥1}n^{-σ}<∞.

Thus Fubini's theorem permits termwise integration. The substitution u=πn²x and Euler's gamma integral give the left side in the conclusion. Split the x-integral at 1. Lemma 16 gives ψ(x)=(x^{-1/2}-1)/2+x^{-1/2}ψ(1/x) for 0<x<1. The elementary part integrates, for σ>1, to 1/(s-1)-1/s. Substituting y=1/x in the remaining part yields ∫_1^∞ψ(y)y^{(1-s)/2}dy/y, completing the identity.

On a compact set of s, both Re(s)/2 and (1-Re(s))/2 are bounded above by some finite A. Lemma 16 bounds the integrand in absolute value by 2C_0e^{-πx}x^{A-1}. Its k-th complex s derivative has the same bound times (log x/2)^k, also integrable for each fixed k. Dominated differentiation proves that I is entire. Reflection just interchanges its two summands, proving I(s)=I(1-s). ∎

**Mathlib.** Supporting results are present at the links below. A standalone theorem covering the full lemma has not been established by the recorded reference check.

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Complex/Log.html

https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/Bochner/Basic.html

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Pow/Real.html

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Gaussian/GaussianIntegral.html#integrableOn_rpow_mul_exp_neg_mul_rpow

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/ExpDeriv.html

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Log/Basic.html#Real.log_le_self

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/ParametricIntegral.html#hasDerivAt_integral_of_dominated_loc_of_deriv_le

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Gamma/Basic.html#Complex.integral_cpow_mul_exp_neg_mul_Ioi

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Gamma/Basic.html#Real.integral_rpow_mul_exp_neg_mul_Ioi

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/PSeries.html#Real.summable_nat_rpow
