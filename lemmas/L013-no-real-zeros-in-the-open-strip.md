# Lemma 13: no real zeros in the open strip

**Hypotheses.** σ is real and 0<σ<1.

**Conclusion.** η(σ)>0 and ζ(σ)<0. In particular every nontrivial zero of ζ has nonzero imaginary part.

**Proof.** The even partial sums are

η_{2N}(σ)=Σ_{n=1}^N[(2n-1)^{-σ}-(2n)^{-σ}].

Every summand is positive, and the first is 1-2^{-σ}>0. Lemma 12 gives convergence, hence η(σ)≥1-2^{-σ}>0. Since 2^{1-σ}>1, the multiplier 1-2^{1-σ} is negative, so the identity in Lemma 12 gives ζ(σ)<0. Lemma 9 excludes all remaining nontrivial zeros outside the open strip. ∎

**Mathlib.** Supporting results are present at the links below. A standalone theorem covering the full lemma has not been established by the recorded reference check.

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Basic.html#Complex.re_tsum

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/InfiniteSum/Order.html

https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Pow/Real.html#Complex.ofReal_cpow
