# L003 — Hull collapse and degree membership

## Hypotheses

For a set E and a nonempty proper subset S, let

π_S : E → (E ∖ S) ⊔ {∗_S}

send every element of S to the new point ∗_S and leave every element of E ∖ S unchanged. For a subset H ⊆ E write π_S[H] for its direct image, not an inverse image or an image of a formal diagram.

For the subgroup assertions, suppose E = G is an additive abelian group and S is a subgroup. H and K will also be subgroups of G.

For the volume assertions, specialize to G = ℚ_p^d with p prime and d ≥ 1. Let S be a full ℤ_p-lattice, let ℒ be the set of full ℤ_p-lattices in G, and fix one additive Haar measure μ. Set

ν(H) = d⁻¹ log μ(H),  B = ν(S).

All these values are finite. Let π_B : ℝ → (B, ∞) ⊔ {∗_B} collapse (−∞, B] to ∗_B. Define ℐ_S = {π_S[H] : H ∈ ℒ}, a set of subsets of the point quotient of G.

These are elementary models of a collapse operation. No hypothesis identifies ℒ, ℐ_S, or the maps below with the full IUT comparison or its formal categorical quotients.

## Conclusion

1. For every nonempty H ⊆ E, π_S[H] = {∗_S} if and only if H ⊆ S. For subgroups H,K of G,

   π_S[H] = π_S[K] ⇔ (H = K or both H ⊆ S and K ⊆ S).

   Thus the collapse still detects containment in S, even though it identifies distinct subgroups contained in S. The equality alternative is necessary for reflexivity outside S.

2. For H ∈ ℒ, π_S[H] = {∗_S} implies ν(H) ≤ B. There is a unique map

   ν̄ : ℐ_S → (B, ∞) ⊔ {∗_B}

   satisfying ν̄(π_S[H]) = π_B(ν(H)) for every H ∈ ℒ. In contrast, the real-valued map ν does not factor through H ↦ π_S[H]. The converse ν(H) ≤ B ⇒ H ⊆ S is false already in dimension two.

3. For every real A, π_B(A) = ∗_B is equivalent to A ≤ B. An identity composite on this quotient does not, by itself, imply that π_B(A) equals ∗_B. Equality with the distinguished class, rather than mere closure of a loop of maps, is the relevant membership assertion in this model.

4. If S contains distinct points s,t, direct image under π_S does not preserve their intersection:

   π_S[{s} ∩ {t}] = ∅, whereas π_S[{s}] ∩ π_S[{t}] = {∗_S}.

   Accordingly, intersecting after collapse cannot by itself supply a point in the original intersection. This statement concerns actual sets; it does not rule out defining separate formal objects.

## Proof

For any nonempty subset H, its image is the singleton {∗_S} exactly when it has no point outside S. This proves the first equivalence.

Now assume H,K,S are subgroups. Since 0 belongs to each, both π_S[H] and π_S[K] contain ∗_S, and their other elements are exactly H ∖ S and K ∖ S. If H = K, their images agree. If both H and K lie in S, both images are {∗_S}.

Conversely, suppose the images agree. If H ∖ S is empty, then K ∖ S is empty as well, giving the second alternative. Otherwise choose x ∈ H ∖ S = K ∖ S. Every h ∈ H ∖ S is already in K. For h ∈ H ∩ S, the element x+h cannot lie in S, since otherwise x = (x+h)−h would lie in S. Hence x+h belongs to H ∖ S = K ∖ S. Since x ∈ K, subtraction shows h ∈ K. Thus H ⊆ K; the same argument with H and K exchanged proves equality. No classification of lattices is used here.

For the volume assertions, a full lattice is compact and open, so it has positive finite Haar measure. If H ⊆ S are full lattices, H is open in the compact group S, so [S:H] is finite. Decompose S into these finitely many translates of H. Translation invariance gives

μ(S) = [S:H] μ(H),

ν(H) = B − d⁻¹ log [S:H] ≤ B.

This proves the upper bound. If π_S[H] = π_S[K], the subgroup result says that either H = K, in which case the degrees agree, or both lie in S, in which case π_B(ν(H)) = ∗_B = π_B(ν(K)). Therefore the formula defining ν̄ is independent of the representative. Every element of ℐ_S has a representative, so the formula defines ν̄ on its whole domain and determines it uniquely.

To show that ν itself does not factor, use H = S and K = pS. Both have image {∗_S}. A ℤ_p-basis of S identifies S/pS with (ℤ/pℤ)^d, so [S:pS] = p^d. Consequently

ν(pS) = B − log p ≠ B = ν(S).

For failure of the converse to the upper bound, take d = 2, S = ℤ_p × ℤ_p, and normalize μ(S) = 1. Let

H = p⁻¹ℤ_p × p²ℤ_p,  C = H ∩ S = ℤ_p × p²ℤ_p.

The indices are [S:C] = p² and [H:C] = p. The same coset calculation gives μ(H) = p⁻¹, so ν(H) = −½ log p < 0 = B. Nevertheless (p⁻¹,0) belongs to H and not to S. Thus region containment is a sufficient condition for the desired numerical inequality, and is strictly stronger than that inequality in this model.

For part 3, the fiber of ∗_B under π_B is (−∞, B] by definition. On the other hand, the identity map of the quotient fixes every class, including those represented by A > B. For example, take A = −1 and B = −2 and use identity maps throughout a loop on this quotient. The composite is the identity, but π_B(A) is the uncollapsed point −1. This refutes only the inference from an unmarked identity composite to membership. If a comparison proves equality with ∗_B for this particular A, it does prove A ≤ B; such an equality is not refuted by the example. No IUT data are claimed for it.

Finally, {s} ∩ {t} is empty when s ≠ t, so its direct image is empty. Both singleton images are {∗_S}, giving the second computation in part 4. Any replacement of the empty intersection by a formal diagram must therefore be distinguished from its ordinary set-theoretic realization before extracting statements about actual points or volumes.

## Mathlib

Full statement: **not checked**. Supporting results for quotient sets, subgroup images, finite subgroup indices, and Haar measure: **not checked**. The volume proof uses only the standard existence of additive Haar measure on ℚ_p^d, compactness/openness of full ℤ_p-lattices, and finite coset decompositions, with the required measure identities proved above. No absence or formal verification is claimed.
