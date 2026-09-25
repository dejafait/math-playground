# L001 — Cyclic monoid isomorphisms do not control lattice log-volume

## Hypotheses

Let p be a prime, let K = ℚ_p with normalized valuation v_p(p) = 1, and let O = ℤ_p. Let μ be additive Haar measure on K normalized by μ(O) = 1. Only translation invariance and finite additivity on compact open sets will be used.

For positive integers a and b, put

M_a = {p^(an) : n ∈ ℕ₀},  M_b = {p^(bn) : n ∈ ℕ₀},

viewed as multiplicative monoids with their specified embeddings in K. Write L_a = p^a O and L_b = p^b O. For a singleton {x}, x ≠ 0, define its lattice hull H({x}) to be the smallest O-submodule of K containing x, namely xO. This is the hull operation for this example only; no identification with all IUT hull constructions is asserted.

## Conclusion

The generator-preserving map φ(p^(an)) = p^(bn) is a monoid isomorphism, but

log μ(L_a) = −a log p,  log μ(L_b) = −b log p.

Consequently log μ(L_a) ≤ log μ(L_b) holds exactly when b ≤ a. In particular, a = 1 and b = 2 violate this inequality even though φ is the squaring map on M_1, executable in the same field, and both lattices are already their generators' lattice hulls.

The compatibility equation v_p(φ(x)) = v_p(x) for every x ∈ M_a holds exactly when a = b. Under that extra condition the two log-volumes agree. More generally, v_p(φ(x)) = (b/a)v_p(x).

These statements refute only an implication from the stated elementary hypotheses. They do not assert that this example satisfies IUT's input prime-strip link, simultaneous holomorphic expressibility, or permitted indeterminacies.

## Proof

The measure in the hypotheses exists by the Haar measure existence theorem for locally compact Hausdorff groups: ℚ_p is locally compact, and its compact open subgroup ℤ_p has positive finite Haar measure, which can be normalized to 1.

For c > 0, the exponents in p^(cn) are unique: equality of two such elements gives cn = cm by applying v_p, hence n = m. Thus φ is well-defined and bijective, with inverse p^(bn) ↦ p^(an). Addition of exponents proves multiplicativity and preservation of the identity. For a = 1, b = 2 it is exactly x ↦ x² on M_1.

For a positive integer c, reduction modulo p^c gives the disjoint decomposition

O = ⋃_{r=0}^{p^c−1} (r + p^c O).

Indeed, each p-adic integer has one residue modulo p^c, represented by exactly one integer in that range. Translation invariance gives equal measures to these p^c cosets. Finite additivity and μ(O) = 1 therefore imply μ(p^c O) = p^(−c). Taking real logarithms yields log μ(p^c O) = −c log p. Since log p > 0, comparison of the two log-volumes is equivalent to a ≥ b. For a = 1, b = 2, the required comparison would be −log p ≤ −2 log p, which is false.

Every O-submodule containing p^c contains all multiples p^c u for u ∈ O. Thus H({p^c}) = L_c. Taking this hull has no further effect on the computed measures.

On x = p^(an), valuation before and after φ is an and bn, respectively. This proves the scaling formula. Equality for all x forces a = b by setting n = 1; that condition also suffices. For the special counterexample, valuation-preserving compatibility fails already at p. Nor is φ the restriction of a unital ring endomorphism of K sending p to p²: such an endomorphism fixes 1 and hence fixes the integer p.

One can give M_b a new abstract degree d_b(p^(bn)) = an to make φ degree-preserving. However, for a ≠ b this degree differs from v_p on the specified embedding. It cannot be substituted into the previously fixed Haar-volume computation while retaining the same measure and lattices. This distinguishes an abstract renormalization from a volume comparison in the fixed valued field.

## Mathlib

Full statement: **not checked**. Supporting p-adic and Haar-measure results: **not checked**. The proof above is informal and self-contained given the stated p-adic and measure hypotheses. No library absence or machine verification is claimed.
