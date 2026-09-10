# Lemma 24: an unconditional paired Hadamard product

**Hypotheses.** Ξ is as above. Select one representative α_j from each pair {α,-α} of its zeros, repeating according to multiplicity.

**Conclusion.** No α_j is zero, Σ_j|α_j|^{-2}<∞, and

Ξ(z)=M_0 Π_j(1-z²/α_j²),

locally uniformly on C. The factors may involve nonreal α_j; their reality has not been assumed.

**Proof.** Use the standard named Hadamard factorization theorem in its order-at-most-one form: if f is entire of order at most 1 and f(0)≠0, its nonzero zeros ρ, with multiplicity, satisfy Σ_ρ|ρ|^{-2}<∞ and

f(z)=f(0)exp(bz)Π_ρ[(1-z/ρ)exp(z/ρ)], with b=f'(0)/f(0).

The product converges locally uniformly. A precise supporting reference is [Hadamard factorization, Theorem 7.7 in the UCL introductory analytic number theory notes](https://www.homepages.ucl.ac.uk/~ucahpet/IANTnotes2018.pdf); the named theorem is the input here.

For Ξ, Lemma 23 proves the order hypothesis, Lemma 21 gives Ξ(0)=M_0>0, and evenness gives Ξ'(0)=0. Thus b=0. The zero set is invariant under α↦-α with equal multiplicities by evenness and local Taylor series. Since 0 is not a zero, all these pairs have two distinct elements. For |z/ρ|≤1/2, the logarithm of (1-z/ρ)exp(z/ρ) is bounded in modulus by a constant times |z/ρ|², from its power series. The reciprocal-square summability therefore permits reordering the product and grouping into ± pairs on every compact set; finitely many nearby zeros cause no issue. Each pair becomes (1-z/α)(1+z/α)=1-z²/α². This also proves local uniform convergence of the paired product and the asserted square summability for the representatives. ∎
