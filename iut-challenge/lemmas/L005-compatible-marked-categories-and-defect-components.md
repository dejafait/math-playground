# L005 — Compatible marked categories and their degree ranges

## Hypotheses

Use the ordinary arithmetic line model of L004 over ℚ. A system Λ consists of finite lattices Λ_p = p^{a_p}ℤ_p with finitely supported integer exponents and a real ball Λ_∞ = [−r,r], r > 0. Its global metrized module is (∏_p p^{a_p})ℤ with norm |x|/r, and

d(Λ) = log r − Σ_p a_p log p.

Fix a target system D with exponents b_p and real radius s, and write B = d(D). At a finite prime let U_p = ℤ_p^×; at infinity let U_∞ = {±1}. These are the scalar automorphism groups of the target local balls.

Define a category C_D as follows. An object is (Λ,[c]), where c = (c_v) is a family of nonzero local scalars with

c_vΛ_v ⊆ D_v

at every place and c_p ∈ ℤ_p^× for almost every prime. The notation [c] denotes the independent U_v-orbits of these scalars. Every Λ is already globally defined and carries its canonical localization identifications.

A morphism a : (Λ,[c]) → (M,[e]) is a scalar a ∈ ℚ^× such that, at every place,

aΛ_v ⊆ M_v,   c_v/(e_v a) ∈ U_v.

Thus its local arrows really are the localizations of one admissible global morphism, and they respect the local markings. Composition is multiplication of rational scalars. A connected component means equivalence under finite zigzags of such morphisms, with either orientation allowed; it does not mean that every arrow is invertible.

Set

Δ(Λ,[c]) = log |c_∞| + Σ_p log |c_p|_p.

This category is an ordinary model with canonical localizations. No identification with realified Frobenioids, the actual IUT q-pilot, the formal quotient, or log-Kummer transport is assumed.

## Conclusion

1. C_D is a well-defined category and Δ is well defined on its objects. Its connected components are classified exactly by δ = Δ ∈ ℝ: two objects belong to the same component if and only if their defects agree.

2. The degree range within the component δ is exactly

   {d(Λ) : Δ(Λ,[c]) = δ} = (−∞, B − δ].

   In particular, its upper endpoint is attained. The degrees of all objects of C_D, without a component restriction, range over all ℝ. Requiring compatible global morphisms throughout the category therefore does not bound all its object degrees by B.

3. Let **D** = (D,[1]) be the identity-marked target. An object (Λ,[c]) admits a morphism to **D** if and only if Δ(Λ,[c]) = 0. This is also equivalent to belonging to the component of **D**. In that component d(Λ) ≤ B. A component δ ≥ 0 also has this degree bound, whereas every component δ < 0 contains an object of degree greater than B.

These are statements about the specified marking orbits. A nonzero defect does not by itself imply a reversed degree inequality for every object in its component. A global arrow to the identity-marked target is a sufficient comparison mechanism here, not a necessary condition for a numerical inequality or for the original IUT argument.

## Proof

Changing c_v or e_v by a factor in U_v does not change the condition c_v/(e_v a) ∈ U_v. The scalar 1 gives each identity arrow. If a carries (Λ,[c]) to (M,[e]) and b carries (M,[e]) to (N,[f]), then baΛ_v ⊆ N_v and

c_v/(f_v ba) = (c_v/(e_v a))(e_v/(f_v b)) ∈ U_v.

Associativity follows from multiplication in ℚ^×. This proves the category assertion, including compatibility with the canonical global localizations.

L004 proves that the finite sum defining Δ is invariant under the target-unit orbits and that

d(Λ) + Δ(Λ,[c]) ≤ B.

If a is a morphism as above, its orbit compatibility gives

log |c_v|_v = log |e_v|_v + log |a|_v

at every place, with the usual real absolute value at infinity. Summing and using the product formula over ℚ, proved in L004, gives Δ(Λ,[c]) = Δ(M,[e]). In particular Δ is constant along every finite zigzag. This uses the compatibility axiom on actual morphisms; it does not assume a global marking on every object.

For each δ ∈ ℝ define a distinguished object E_δ as follows:

(E_δ)_p = D_p for all finite p,   (E_δ)_∞ = [−s exp(−δ), s exp(−δ)],

with marking scalars e_p = 1 and e_∞ = exp(δ). All these markings map the local balls onto those of D. Therefore

Δ(E_δ) = δ,   d(E_δ) = B − δ.

Every object (Λ,[c]) of defect δ admits a morphism to E_δ. Indeed, put n_p = v_p(c_p), which has finite support, and let

a₀ = ∏_p p^{n_p} ∈ ℚ_{>0}.

At every finite prime c_p/a₀ ∈ U_p. At infinity, the equation for the defect reads

δ = log |c_∞| − Σ_p n_p log p,

so |c_∞| = exp(δ)a₀. Consequently c_∞/(e_∞a₀) ∈ {±1}, and at all places c_v/(e_va₀) ∈ U_v. Write c_v = u_ve_va₀ with u_v ∈ U_v. Since c_vΛ_v ⊆ D_v and u_v preserves D_v,

e_va₀Λ_v ⊆ D_v = e_v(E_δ)_v.

The scalar e_v is nonzero, hence this implies a₀Λ_v ⊆ (E_δ)_v. Thus a₀ is the required morphism, including the real norm condition.

Any two objects of defect δ now have a zigzag through E_δ. Together with invariance of Δ, this proves the exact classification of connected components. It does not assert that E_δ is a terminal object: both signs of a₀ give distinct morphisms in the category as defined.

The upper bound on the degree range follows from L004. For each η ≥ 0, keep the finite lattices and markings of E_δ but replace its real radius by s exp(−δ−η). The real image radius becomes s exp(−η) ≤ s, so this is still an object with defect δ, and its degree is B − δ − η. This proves that the range is the entire stated interval. Taking η = 0 and varying δ shows that the range over all components is ℝ.

Finally E₀ is exactly **D**. Invariance of Δ forces any arrow to **D** to start at defect zero; the preceding construction gives such an arrow whenever the defect is zero. It also proves the corresponding zigzag equivalence. The component range gives all assertions about δ ≥ 0 and δ < 0. For example, the ℓℤ versus ℓ²ℤ marking of L004 has δ = −log ℓ, so it belongs to a component whose top degree is B + log ℓ. It is a valid object of C_D and violates no compatibility axiom for morphisms of C_D. It simply has no arrow or zigzag to **D**. This sharpens the distinction between the definition of a category and the existence of a particular comparison arrow.

## Mathlib

Full statement: **not checked**. Supporting results for categories, connected components, rational valuations, and the product formula: **not checked**. The required defect inequality and product formula are proved in L004; the category, component classification, lifting, and sharp range computations are proved above. No claim of absence or formal verification is made.
