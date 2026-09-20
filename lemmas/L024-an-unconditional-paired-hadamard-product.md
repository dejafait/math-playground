# Lemma 24: an unconditional paired Hadamard product

**Hypotheses.** Ξ is as above. Select one representative α_j from each pair {α,-α} of its zeros, repeating according to multiplicity.

**Conclusion.** No α_j is zero, Σ_j|α_j|^{-2}<∞, and

Ξ(z)=M_0 Π_j(1-z²/α_j²),

locally uniformly on C. The factors may involve nonreal α_j; their reality has not been assumed.

**Proof.** Use the standard named Hadamard factorization theorem in its order-at-most-one form: if f is entire of order at most 1 and f(0)≠0, its nonzero zeros ρ, with multiplicity, satisfy Σ_ρ|ρ|^{-2}<∞ and

f(z)=f(0)exp(bz)Π_ρ[(1-z/ρ)exp(z/ρ)], with b=f'(0)/f(0).

The product converges locally uniformly. A precise supporting reference is [Hadamard factorization, Theorem 7.7 in the UCL introductory analytic number theory notes](https://www.homepages.ucl.ac.uk/~ucahpet/IANTnotes2018.pdf); the named theorem is the input here. Theorem 7.5 there supplies reciprocal-square summability (take order bound 1 and exponent 2; finitely many zeros near 0 cause no issue). Neither theorem assumes real zeros or finite exponential type.

For Ξ, Lemma 23 gives log B(R)=O(R log R), hence for every ε>0 an upper bound log B(R)≤C_ε R^{1+ε} for R≥1. This is exactly the order-at-most-one hypothesis, even though it does not assert log B(R)=O(R). Thus Lemma 23 proves the order hypothesis, Lemma 21 gives Ξ(0)=M_0>0, and evenness gives Ξ'(0)=0. To check the normalization without splitting divergent sums, let P be the genus-one product above. Its finite partial products all have value 1 and derivative 0 at 0. Local uniform convergence and the Cauchy integral formula give P(0)=1 and P′(0)=0. Differentiating f(z)=f(0)exp(bz)P(z) at 0 therefore gives b=f′(0)/f(0). Thus b=0. In particular no quadratic exponential is allowed by the factorization theorem; evenness alone would not exclude one without the growth hypothesis. The zero set is invariant under α↦-α with equal multiplicities by evenness and local Taylor series. Since 0 is not a zero, all these pairs have two distinct elements. For |z/ρ|≤1/2, the analytic logarithm normalized to vanish at z=0 is −Σ_{k≥2}(z/ρ)^k/k, whose modulus is at most |z/ρ|². On |z|≤R the sum of these bounds over |ρ|>2R is at most R²Σ_{|ρ|>2R}|ρ|⁻²<∞. The reciprocal-square summability therefore permits reordering the product and grouping into ± pairs on every compact set; finitely many nearby zeros cause no issue. Each pair becomes (1-z/α)(1+z/α)=1-z²/α². This also proves local uniform convergence of the paired product and the asserted square summability for the representatives. No separate series Σ1/ρ is formed or rearranged. On a compact set containing zeros, take all nearby factors as a finite head and apply the logarithm argument only to the nonvanishing tail, so no global logarithm of Ξ is required. Multiplicities are preserved, and Σ_j|α_j|⁻² is exactly half the sum over all zeros. ∎

This supplies Σ_j|β_j|<∞ for β_j=α_j⁻², the exact summability required by the polynomial detector. It supplies no sign for the mixed forms: the factors and nodes may still be nonreal. The statement and mathematical inputs are unchanged by this review.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
