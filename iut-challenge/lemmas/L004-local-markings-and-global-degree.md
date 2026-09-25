# L004 — Local markings and the global degree defect

## Hypotheses

Work over ℚ with its usual real absolute value and normalized p-adic absolute values |p|_p = p⁻¹. A rank-one lattice system Λ consists of lattices

Λ_p = p^{a_p}ℤ_p ⊂ ℚ_p

at every prime p, where a_p ∈ ℤ and only finitely many a_p are nonzero, and the real unit ball Λ_∞ = [−r,r], where r > 0. A second system M has exponents b_p and real radius s > 0. Define

d(Λ) = log r − Σ_p a_p log p,  d(M) = log s − Σ_p b_p log p.

These are logarithmic volumes relative to ℤ_p and [−1,1], respectively, summed over the places. They are also the arithmetic degrees of the corresponding metrized rank-one ℤ-modules: if t_Λ = ∏_p p^{a_p}, use the module t_Λℤ ⊂ ℚ and the real norm x ↦ |x|/r, so that −log ‖t_Λ‖ = d(Λ).

A family of local markings consists of nonzero scalars c_p ∈ ℚ_p and c_∞ ∈ ℝ such that

c_pΛ_p ⊆ M_p at every prime p,  c_∞Λ_∞ ⊆ M_∞,

and c_p ∈ ℤ_p^× at all but finitely many primes. We allow postcomposition with automorphisms of the target lattice or real unit ball: the marking is the orbit of multiplication by c_p under ℤ_p^×, and of multiplication by c_∞ under {±1}. Morphisms of marked local objects are required to preserve these orbits.

Set

Δ(c) = log |c_∞| + Σ_p log |c_p|_p.

This is a finite sum. A compatible global scalar means a single a ∈ ℚ^× whose local multiplications satisfy the indicated inclusions. Compatibility with the specified marking orbits additionally requires a/c_p ∈ ℤ_p^× at every finite prime and a/c_∞ ∈ {±1} at infinity.

This is an ordinary arithmetic line model for testing local versus global compatibility. It is not asserted to realize the IUT formal quotient, its q-pilot, or its full indeterminacy family. The word linear in this model means an actual linear map over the indicated local field; the separate Frobenioid terminology is recorded in the source discussion below.

## Conclusion

1. Every family of local markings satisfies the exact bound

   d(Λ) + Δ(c) ≤ d(M).

   Equality holds if and only if all the local inclusions, including the real one, are equalities. Postcomposition by the allowed target automorphisms leaves Δ(c) unchanged. Thus local marking orbits do not remove the degree defect.

2. If a compatible global scalar exists, then d(Λ) ≤ d(M). If it represents the specified local orbits, then Δ(c) = 0. More generally, Δ(c) ≥ 0 is already sufficient to deduce this inequality from part 1; being induced by one rational scalar is a sufficient mechanism, not a necessary condition for a numerical degree inequality.

3. For every prime ℓ there are systems with

   d(Λ) = −log ℓ > −2 log ℓ = d(M)

   that nevertheless admit marking orbits represented by isomorphisms at every place. These markings preserve all local scalar unit actions and remain compatible with scalar extension and Galois actions at finite places. Both systems come from global metrized ℤ-modules, with their ordinary localization identifications. However, no nonzero compatible global scalar satisfying even just the inclusions exists. In this example Δ(c) = −log ℓ, so the bound in part 1 is sharp and gives only

   d(Λ) ≤ d(M) + log ℓ.

Consequently, existence of local markings, even together with localization of the objects and local equivariance, does not imply a global degree bound. A compatible global morphism, or some other control of the total defect, is additional information. This counterexample concerns that implication, not Corollary 3.12 of IUT III.

## Proof

The finite-place inclusion is equivalent to

v_p(c_p) + a_p ≥ b_p.

Multiplication by −log p gives

log |c_p|_p − a_p log p ≤ −b_p log p.

The real inclusion is equivalent to |c_∞|r ≤ s, hence to

log |c_∞| + log r ≤ log s.

Summing yields part 1. Only finitely many summands are nonzero. Each difference between the right and left local sides is nonnegative, so equality of the sums occurs exactly when every local difference is zero, which is exactly equality of all the local balls. A p-adic unit has absolute value one, as do ±1 at infinity. Changing representatives by target automorphisms therefore does not alter Δ(c).

For completeness, the volume interpretation at a finite prime is immediate from finite indices: ℤ_p/p^nℤ_p has p^n elements for n ≥ 0, so translation invariance and μ_p(ℤ_p) = 1 give μ_p(p^nℤ_p) = p⁻ⁿ. Using ℤ_p ⊂ p⁻ⁿℤ_p proves the same formula for negative exponents. At infinity the ratio of the lengths of [−r,r] and [−1,1] is r. This also checks the signs in the definition of d.

Write any a ∈ ℚ^× uniquely as a = ε∏_p p^{n_p}, with ε ∈ {±1}, integers n_p, and finite support. Then

log |a| = Σ_p n_p log p,  log |a|_p = −n_p log p.

Their sum over all places is zero. This proves the product formula over ℚ in the normalization used here. Apply part 1 to the family c_v = a to obtain d(Λ) ≤ d(M). If this family represents the originally specified orbits, the automorphism invariance proved above gives Δ(c) = 0. The last assertion of part 2 follows directly from d(Λ) + Δ(c) ≤ d(M).

For part 3, take r = s = 1 and

Λ_ℓ = ℓℤ_ℓ,  M_ℓ = ℓ²ℤ_ℓ;

Λ_p = M_p = ℤ_p for p ≠ ℓ.

These are the localizations of the global modules ℓℤ and ℓ²ℤ in their rational lines, equipped with the usual real norm. At primes p ≠ ℓ the equalities ℓℤ_p = ℤ_p = ℓ²ℤ_p follow because ℓ is a p-adic unit. Their real unit balls are both [−1,1]. The asserted degrees follow from the definition.

Choose c_ℓ = ℓ, c_p = 1 for p ≠ ℓ, and c_∞ = 1. Each multiplication maps the specified source lattice or real ball onto its target. At a finite place, scalar multiplication commutes with every unit u ∈ ℤ_p^×. In the category of orbit-marked local objects, every such u remains an automorphism: multiplication by c_p followed or preceded by u gives the same target-unit orbit. Thus this example does not obtain its degree discrepancy by discarding local unit actions.

After a finite extension K/ℚ_p the lattices become ℓO_K and ℓ²O_K when p = ℓ, and O_K otherwise. The same multipliers still give isomorphisms. They commute with scalar units in O_K and with every K/ℚ_p automorphism because the multipliers lie in ℚ_p. They also commute with the maps induced by further field extensions. These assertions establish the claimed local equivariance and base-change compatibility; they do not establish the other structures required of an IUT prime-strip.

Suppose a ∈ ℚ^× gave a compatible global scalar satisfying the inclusions. At ℓ one would have v_ℓ(a) ≥ 1; at every p ≠ ℓ one would have v_p(a) ≥ 0. By prime factorization, a would be a nonzero integer divisible by ℓ. The real inclusion would require |a| ≤ 1, contradicting |a| ≥ ℓ > 1. Therefore even a global morphism with weaker inclusions, rather than the prescribed isomorphism orbits, does not exist. Finally,

Δ(c) = log |ℓ|_ℓ = −log ℓ,

which gives equality in part 1 and the claimed insufficient bound.

The source motivation is [IUT III, Remark 3.9.5(ix)(cQ3), pp. 141–142](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf#page=141). Its local marking is an Aut(D)-orbit of a linear morphism to the determinant object D. Its local-global collections also retain a global object and localization isomorphisms, and impose compatibility on morphisms. [Frobenioids I, Definition 1.2(i), p. 21](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20I.pdf#page=21) defines linearity by Frobenius degree one, separately from isometry. These citations motivate preserving the markings and checking global compatibility; they are not citations of the counterexample or an identification of it with the original IUT construction. A formal diagram could supply a valid degree comparison by a mechanism other than the ordinary global scalar considered here.

## Mathlib

Full statement: **not checked**. Supporting results concerning valuations, localizations, unit actions, rank-one arithmetic degrees, and the product formula: **not checked**. The needed product formula over ℚ and all volume and morphism computations were proved explicitly above. The primary-source definitions cited in the proof concern the application boundary, not Mathlib coverage. No absence or formal verification is claimed.
