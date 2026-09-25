# L002 — Comparison composite and normalized determinant transport

## Hypotheses

In a category, let X₀, X₁, X₂, X₃ and Y₀, Y₁, Y₂, Y₃ be objects. For i = 1, 2, 3, let bᵢ : Xᵢ₋₁ → Xᵢ and uᵢ : Yᵢ₋₁ → Yᵢ be isomorphisms. Let kᵢ : Xᵢ → Yᵢ, for i = 0, 1, 2, 3, be isomorphisms satisfying

uᵢ ∘ kᵢ₋₁ = kᵢ ∘ bᵢ.

Put c = u₃ ∘ u₂ ∘ u₁ ∘ k₀ ∘ b₁⁻¹ ∘ b₂⁻¹ : X₂ → Y₃. These are coherent maps satisfying the displayed equalities; independent choices from families of isomorphisms are not assumed to satisfy them.

For the numerical conclusion only, suppose additionally that a specified realization of c is a finite nonempty tuple of ℚ_p-linear isomorphisms Tᵣ : Vᵣ → Wᵣ, where p is prime and dim Vᵣ = dim Wᵣ = dᵣ > 0. Choose full ℤ_p-lattices Oᵣ, Lᵣ in Vᵣ and Pᵣ in Wᵣ. The reference lattices Oᵣ and Pᵣ retain their separate labels. Let wᵣ be positive rational weights with Σᵣ wᵣ = 1.

For arbitrary additive Haar measures μᵣ on Vᵣ and ηᵣ on Wᵣ, define

ν_O(L) = Σᵣ (wᵣ/dᵣ) log(μᵣ(Lᵣ)/μᵣ(Oᵣ)),

and define ν_P analogously using ηᵣ. All these lattice measures are positive and finite. Let D be a positive integer clearing the denominators of wᵣ/dᵣ, and put eᵣ = D wᵣ/dᵣ ∈ ℕ. Then Σᵣ eᵣdᵣ = D.

For a full lattice L in a d-dimensional space V, det L is its top exterior-power lattice in det V = ∧ᵈV. The relative determinant det L ⊗ (det O)⁻¹ is viewed as a fractional ℤ_p-ideal in ℚ_p by the canonical evaluation det V ⊗ (det V)⁎ ≅ ℚ_p. Define the fractional ideal

J_D(L;O) = ⊗ᵣ (det Lᵣ ⊗ (det Oᵣ)⁻¹)^{⊗eᵣ} ⊂ ℚ_p,

where the tensor product is identified with the product of the fractional ideals. Normalize additive Haar measure h on ℚ_p by h(ℤ_p) = 1.

The numerical realization is an extra hypothesis, not a consequence of a categorical isomorphism. In particular, this lemma does not assert that the actual IUT comparison has such a realization on its entire family of regions.

## Conclusion

The comparison path satisfies

c = u₃ ∘ k₂ = k₃ ∘ b₃.

Under the additional numerical hypotheses,

ν_O(L) = D⁻¹ log h(J_D(L;O)),

ν_P(TL) − ν_O(L) = ν_P(TO).

Consequently, transporting both the lattice and its reference preserves normalized log-volume: if Pᵣ = TᵣOᵣ for all r, then ν_P(TL) = ν_O(L). More generally, for the fixed references in the hypotheses, this equality holds if and only if ν_P(TO) = 0. This condition is an equality of weighted determinant volumes; it does not require componentwise lattice equality.

For any a ∈ ℤ, setting Lᵣ = pᵃOᵣ for all r gives J_D(L;O) = p^{aD}ℤ_p and ν_O(L) = −a log p. Replacing D by a positive integral multiple changes neither ν_O(L) nor the truth of an inequality between two such normalized values when the same D is used on both sides. None of these statements supplies a containment of an input lattice in an output hull.

## Proof

Using the first two commuting squares and cancelling inverse isomorphisms gives

u₂ ∘ u₁ ∘ k₀ ∘ b₁⁻¹ ∘ b₂⁻¹
= u₂ ∘ k₁ ∘ b₁ ∘ b₁⁻¹ ∘ b₂⁻¹
= k₂ ∘ b₂ ∘ b₂⁻¹
= k₂.

Compose with u₃ and use the third square. This proves the categorical conclusion in exactly the stated category; no claim about a representation functor is needed or inferred.

For the numerical statements, choose a ℤ_p-basis of Oᵣ and write Lᵣ = AᵣOᵣ with Aᵣ ∈ GL_{dᵣ}(ℚ_p) in this basis. The Smith normal form theorem over the principal ideal domain ℤ_p, after clearing denominators, gives

Aᵣ = Uᵣ diag(p^{aᵣ₁}, …, p^{aᵣdᵣ}) Rᵣ,

with Uᵣ, Rᵣ ∈ GL_{dᵣ}(ℤ_p) and integer exponents aᵣs. A lattice-preserving linear automorphism preserves Haar measure: its pushforward is another Haar measure assigning the same measure to the reference lattice, so the uniqueness theorem for Haar measure makes the two measures equal. Thus the matrices Uᵣ and Rᵣ have no effect on the lattice measure ratio.

Write Qᵣ for the diagonal lattice and Cᵣ⁰ = Qᵣ ∩ ℤ_p^{dᵣ}. The indices are [ℤ_p^{dᵣ} : Cᵣ⁰] = p^{Σ_s max(0,aᵣs)} and [Qᵣ : Cᵣ⁰] = p^{Σ_s max(0,−aᵣs)}. Taking the ratio of the second index to the first, finite coset decompositions and translation invariance give

μᵣ(Lᵣ)/μᵣ(Oᵣ) = p^{−Σ_s aᵣs} = |det Aᵣ|_p.

This also covers negative exponents. The relative determinant ideal is (det Aᵣ)ℤ_p. An element z ≠ 0 of ℚ_p is p^{v_p(z)} times a unit, and the one-dimensional version of the same coset computation gives h(zℤ_p) = |z|_p. Consequently

log h(J_D(L;O))
= Σᵣ eᵣ log |det Aᵣ|_p
= D Σᵣ (wᵣ/dᵣ) log(μᵣ(Lᵣ)/μᵣ(Oᵣ))
= D ν_O(L).

This proves the determinant formula, including independence from the chosen lattice bases and the initial Haar-measure scalings.

Next choose a ℤ_p-basis of Pᵣ, and let Cᵣ be the matrix of Tᵣ from the chosen Oᵣ-basis to this Pᵣ-basis. The matrices defining TᵣLᵣ and TᵣOᵣ relative to Pᵣ are CᵣAᵣ and Cᵣ. Multiplicativity of the determinant gives

log(ηᵣ(TᵣLᵣ)/ηᵣ(Pᵣ))
= log |det(CᵣAᵣ)|_p
= log |det Aᵣ|_p + log |det Cᵣ|_p.

Multiplying by wᵣ/dᵣ and summing proves ν_P(TL) = ν_O(L) + ν_P(TO). All conclusions concerning reference transport follow immediately.

If Lᵣ = pᵃOᵣ, then det Lᵣ = p^{adᵣ}det Oᵣ. Hence J_D(L;O) = p^{aΣᵣeᵣdᵣ}ℤ_p = p^{aD}ℤ_p, proving the scalar calculation. If D is replaced by tD, each eᵣ is replaced by teᵣ, so J_{tD} = J_D^{⊗t}. Its log-measure is multiplied by t, exactly cancelling the change in the prefactor 1/(tD). Equivalently, for real numbers a₀, b₀, the inequalities Da₀ ≤ Db₀ and a₀ ≤ b₀ are equivalent because D > 0.

This last observation concerns a common determinant normalization. It does not cancel unequal scalings of different input objects, and it establishes neither a hull comparison nor a global arithmetic bound.

## Mathlib

Full statement: **not checked**. Supporting results for category composition, Smith normal form, exterior powers, and p-adic Haar measure: **not checked**. The named standard inputs used above are Smith normal form over a principal ideal domain and existence/uniqueness of Haar measure on locally compact Hausdorff groups. No absence or formal verification is claimed.
