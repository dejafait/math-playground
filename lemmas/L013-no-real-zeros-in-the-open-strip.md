# Lemma 13: no real zeros in the open strip

**Hypotheses.** σ is real and 0<σ<1.

**Conclusion.** η(σ)>0 and ζ(σ)<0. In particular every nontrivial zero of ζ has nonzero imaginary part.

**Proof.** The even partial sums are

η_{2N}(σ)=Σ_{n=1}^N[(2n-1)^{-σ}-(2n)^{-σ}].

Every summand is positive, and the first is 1-2^{-σ}>0. Lemma 12 gives convergence, hence η(σ)≥1-2^{-σ}>0. Since 2^{1-σ}>1, the multiplier 1-2^{1-σ} is negative, so the identity in Lemma 12 gives ζ(σ)<0. Lemma 9 excludes all remaining nontrivial zeros outside the open strip. ∎

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
