# Lemma 12: a convergent alternating representation in Re(s)>0

**Hypotheses.** Re(s)>0. Set η_N(s)=Σ_{n=1}^N(-1)^{n-1}n^{-s}.

**Conclusion.** η_N converges locally uniformly to a holomorphic function η on Re(s)>0. On this half-plane η(s)=(1-2^{1-s})ζ(s), interpreted with a removable singularity at s=1.

**Proof.** Fix a compact subset with Re(s)≥δ>0 and |s|≤R. For M≥N, put a_n=(-1)^{n-1} and A_n=Σ_{k=N}^n a_k, so |A_n|≤1. Summation by parts gives

Σ_{n=N}^M a_n n^{-s}=A_M M^{-s}+Σ_{n=N}^{M-1}A_n(n^{-s}-(n+1)^{-s}).

By integrating the derivative of x^{-s} on [n,n+1], the absolute value is at most

M^{-δ}+R∫_N^M x^{-δ-1}dx ≤ (1+R/δ)N^{-δ}.

This uniform Cauchy bound proves local uniform convergence; the Weierstrass theorem on locally uniform limits of holomorphic functions gives holomorphicity. On Re(s)>1, absolute convergence permits separating the even terms and gives η(s)=ζ(s)-2·2^{-s}ζ(s). The multiplier q(s)=1-2^{1-s} vanishes at 1, with q'(1)=log 2. Lemma 8 shows that q(s)ζ(s) has removable value log 2 at 1 and is holomorphic throughout Re(s)>0 after filling it in. The identity theorem on that connected half-plane proves the identity everywhere there. No division at a zero of q is used. ∎

**Mathlib.** Supporting results are present at the links below. A standalone theorem covering the full lemma has not been established by the recorded reference check.

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/LocallyUniformLimit.html

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Pow/Asymptotics.html#tendsto_rpow_neg_atTop

https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/RiemannZeta.html#zeta_eq_tsum_one_div_nat_add_one_cpow

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/InfiniteSum/NatInt.html#tsum_even_add_odd

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/RemovableSingularity.html#Complex.analyticAt_of_differentiable_on_punctured_nhds_of_continuousAt

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Pow/Deriv.html#HasDerivAt.const_cpow

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Analytic/Uniqueness.html#AnalyticOnNhd.eqOn_of_preconnected_of_eventuallyEq
