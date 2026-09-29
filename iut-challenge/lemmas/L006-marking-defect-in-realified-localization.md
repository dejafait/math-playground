# L006 — Marking defect in realified arithmetic localization

## Hypotheses

Work in the arithmetic Frobenioid fiber over ℚ, with identity base maps and its usual arithmetic degree normalization. At infinity use real isotropic objects. There is no additional geometric base data. Use the realifications of the global arithmetic and local Frobenioids in the cited constructions below.

Here is their divisor presentation in this fiber. Let V = ⊕_v ℝ, where v runs over the primes and infinity, V₊ = ⊕_v ℝ≥0, and λ(z) = Σ_v z_v. Coordinates already include the weights log p. Put H = ker λ. A global object is represented by g ∈ V, with degree d(g) = λ(g). A linear global arrow g → g′ has an effective divisor E ∈ V₊ and rational-function parameter h ∈ H satisfying

g + E = g′ + h.

A local realified object at v is represented by x_v ∈ ℝ. A linear arrow x_v → y_v has divisor e_v ≥ 0 and parameter u_v ∈ ℝ satisfying x_v + e_v = y_v + u_v. Localization is restriction to the v-coordinate, including restriction of E and h. These are presentations of the cited realified models; the rational-function parameters are real divisor coordinates, not necessarily elements of ℚ× or ℚ_v×.

Fix a global target D represented by d ∈ V, write B = λ(d), and use D_v = loc_v(D) as local targets. A marked collection consists of:

- a global object G represented by g;
- at every v, a local object X_v with a linear marking m_v : X_v → D_v, up to postcomposition by Aut(D_v);
- isomorphisms ι_v : loc_v(G) ≅ X_v in the local realifications.

The local objects and markings may already be realified. For collections retaining original local objects, apply their realification functors when forming the displayed data. Suppose the effective marking divisors e_v = Div(m_v) are finitely supported. This finiteness holds on the image of L005 considered below; it is not established here for every possible IUT collection.

A morphism of collections consists of a global arrow a : G → G′ and local arrows b_v : X_v → X′_v such that the localization squares commute and m_v = m′_v b_v up to target automorphisms. All base maps are identities. Compatibility with the linear markings forces these arrows to be linear: Frobenius degrees multiply and the markings have degree one.

This is the specialization of the three retained pieces of (cQ3) to the stated arithmetic fiber, prior to its (fQ1)/(fQ2) formal quotient. No equivalence with a full IUT prime-strip or identification of its distinguished q-pilot is assumed.

## Conclusion

1. The quantity

   δ_D(G, X, [m], ι) = B − d(G) − Σ_v e_v

   is well defined on these marked collections, independent of local representatives and localization isomorphism choices. It is invariant under their morphisms and hence under finite zigzags. Isomorphic choices of the global target, with compatible local identifications, give the same value.

2. There is a natural functor from the ordinary category C_D of L005 to these collections, obtained by realifying its global object and retaining its canonical localizations and local marking orbits. On its image,

   δ_D = Δ.

   Thus the L005 defect survives this realification as a function of the complete marked collection. It is not generally recoverable from the local markings alone when the global object and its localization identifications are varied.

3. The bound supplied by the data is

   d(G) = B − δ_D − Σ_v e_v ≤ B − δ_D.

   Every value of δ_D occurs with equality, even in collections with X_v = D_v and m_v the identity at every place. Realified localization therefore does not force δ_D = 0 or δ_D ≥ 0. The sufficient threshold for obtaining d(G) ≤ B from this estimate remains δ_D ≥ 0.

This does not establish descent through the formal quotient, transport of a distinguished pilot, or any estimate for the actual IUT quantities A and B. Finite zigzags in this fiber are not substituted for a formal quotient.

## Proof

### Applicability of the source presentation

The global construction is [Mochizuki, Frobenioids I, June 2008, Theorem 5.2(i)–(ii), pp. 100–101; Proposition 5.3, p. 103; Example 6.3 and Theorem 6.4(i), pp. 112–116](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20I.pdf#page=100). Import the arithmetic degree quotient by citation, as recorded in the foundation note: the real span of principal divisors is H. The model-arrow relation specializes to g + E = g′ + h. Isomorphisms have E = 0, so λ(g) is independent of the representative.

For the local models and contact functors use [Frobenioids II, June 2008, Examples 1.1(i), 3.3(i)–(ii), and 5.6(iii)–(iv), pp. 7–8, 27–28, 63–65](https://www.researchgate.net/publication/267018843_THE_GEOMETRY_OF_FROBENIOIDS_II_POLY-FROBENIOIDS). The global contact functor restricts divisors and rational functions to local coordinates; the separate local contact functor becomes an equivalence after realification, by Remark 5.3.3. In a local fiber the real span of principal divisors is the whole one-dimensional divisor space. Thus its realified model has the local arrow formula stated above. The coproduct in the global contact functor has one component when localizing the chosen object Spec(ℚ) at v. This justifies using one coordinate at a time.

Use the [February 2019 corrections, item (3)](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20II%20%28comments%29.pdf): the archimedean effective coordinate uses minus the logarithm of norm. The realified models are of model type and birationally Frobenius-normalized, so the additional hypotheses in the [January 2024 corrections, item (29)](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Geometry%20of%20Frobenioids%20I%20%28comments%29.pdf) cause no omitted assumption here. No birationalization of an arbitrary marked category is used.

These are cited constructions, not a reproof of the arithmetic Picard theorem. The specialization to the marked collections is the calculation that follows. The three pieces and compatibility diagrams being specialized are those of [IUT III, May 2020, Remark 3.9.5(ix)(cQ3), pp. 141–142](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20III.pdf#page=141).

### The invariant and the localization diagrams

In a local model, an isomorphism x → y has e = 0 and u = x − y. It is unique over the identity base map. Indeed, an inverse forces both Frobenius degrees to be one and both nonnegative divisors to be zero; the arrow relation then determines u. In particular, a target automorphism has zero divisor and trivial image in this realified fiber. Original target-unit orbits therefore do not change e_v.

Write x_v for the chosen representative of X_v. The isomorphism ι_v has parameter g_v − x_v. The marking m_v has parameter x_v + e_v − d_v. Composition of linear arrows adds these parameters and adds their divisors. Consequently the composite

f_v = m_v ι_v : loc_v(G) → D_v

has divisor e_v and parameter

u_v = g_v + e_v − d_v.

Although the individual x_v need not be finitely supported, u = g + e − d is finitely supported. Hence

−λ(u) = λ(d) − λ(g) − λ(e) = δ_D.

This description accounts for the localization identifications, not just the raw local markings. Changing the representative x_v changes the two summands in the composite parameter by opposite amounts. Isomorphic global representatives change g by an element of H, which has total degree zero. The same argument applies to an isomorphic target d. Changing markings by target automorphisms leaves e unchanged. For fixed objects the realified identity-base localization isomorphism is unique; any choices made before realification give that same image. These observations prove well-definedness and all the stated choice invariances.

Now let (a, b_v) be a morphism of collections and let E be the effective divisor of a. Since the localization squares commute and their vertical isomorphisms have zero divisor,

Div(b_v) = E_v.

Marking compatibility gives e_v = e′_v + E_v. The global arrow relation and h ∈ H give

d(G′) = d(G) + λ(E).

It follows that

d(G′) + λ(e′) = d(G) + λ(E) + λ(e′) = d(G) + λ(e).

Subtracting from B proves δ_D invariance. A finite zigzag preserves it by applying this equality to each arrow in either orientation. This calculation uses the global arrow and the localization squares together.

### Agreement with the ordinary marked category

Take the notation of L005: Λ_p = p^{a_p}ℤ_p, Λ_∞ = [−r,r], D_p = p^{b_p}ℤ_p, D_∞ = [−s,s], and marking scalars c_v. In the arithmetic divisor presentation choose

g_p = −a_p log p,   g_∞ = log r,

d_p = −b_p log p,   d_∞ = log s.

These represent the metrized modules in L005: at p the divisor coordinate for the module p^{a_p}ℤ_p is −a_p, while the real metric contributes log r. Their degrees are exactly the degrees used there.

Take X_v to be the original local objects and ι_v to be their canonical identifications with the localizations of G after realification. The marking divisors are

e_p = (v_p(c_p) + a_p − b_p) log p,

e_∞ = log(s/(|c_∞|r)).

They are nonnegative by the local inclusions and have finite support. These formulas also follow directly from the local arrow relation with rational-function parameter −log |c_v|_v. Thus the composite parameter u_v is −log |c_v|_v, and

δ_D = −Σ_v u_v = Σ_v log |c_v|_v = Δ.

A morphism a ∈ ℚ× of C_D has global parameter h_v = −log |a|_v ∈ H, by the cited arithmetic principal-divisor statement. Its localizations and marking compatibilities give exactly the required squares and triangles after realification. Identities and composition are preserved by the realification and localization functors. This establishes the asserted functor and agreement, without assuming C_D itself is a Frobenioid.

### What localization does and does not force

Let ε_∞ ∈ V have coordinate one at infinity and zero elsewhere. For any δ ∈ ℝ take

g = d − δ ε_∞,   X_v = D_v,   m_v = id_{D_v}.

There is an isomorphism loc_v(G) → D_v in every local realified fiber: its parameter is g_v − d_v and its divisor is zero. Choose these as ι_v. This is a collection with the original local target objects and identity markings, a global realified object, and the required localization isomorphisms. It has e = 0, δ_D = δ, and d(G) = B − δ. In particular, the raw local markings are identical for all these collections, while their defects differ. Their global degrees distinguish the collections; no isomorphism between different degrees is being asserted.

The displayed formula for d(G) now proves the bound and its attainment. This establishes survival and possible nonvanishing of the defect in the stated arithmetic specialization. It supplies no sign condition on the actual transported q-pilot and no conclusion about the quotient (fQ2) modulo (fQ1).

## Mathlib

Full marked-localization statement: **not checked**. Supporting Frobenioid, arithmetic degree, divisor, and category results: **not checked**. The named source results above provide the global and local constructions, not a Mathlib match or verification of the full IUT comparison. The marked-collection calculation is a reproduction/specialization of those constructions; no progress beyond the checked literature is claimed.
