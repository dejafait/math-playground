# Degree-27 fixed-Galois full-pair lift — source-covered continuation

TARGET: Test whether L017's compact involution can be induced on J by an automorphism of the model MLF×-pair G_K acting on O_kbar^times with G_K component equal to the identity, using Hoshi Theorem 7.6 and Corollary 7.7; keep quotient-only and nonidentity-Galois actions outside the conclusion.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact ind2/MLF-pair source search completed in 2026-10-05-degree-27-actual-ind2-group.md; the inspected fixed-group automorphism kernel is stronger than a free choice of lattice maps and directly covers the needed necessary condition.
SOURCE_EVIDENCE: Hoshi, Introduction to Mono-anabelian Geometry, PMB (2021), pp. 5–44, DOI 10.5802/pmb.42, Definitions 5.1–5.5 and Remark 5.5.1 pp. 29–30, Theorem 7.6 with proof pp. 39–40, Corollary 7.7 p. 43; L017's explicit map and L016's established continuous logarithm on units supply the unchanged local inputs.
COMPARISON: The known theorem classifies the kernel on full group-monoid pairs, but does not evaluate L017's particular involution on J; only that finite explicit-map comparison and the induced logarithm action are left for research.
GAP: Justify passage from the profinite-unit exponent action on O_kbar^times to its logarithmic action on J, then decide whether L017's map has that form. Do not claim this kernel is the entire original-IUT ind2 group.
REASON: A bounded necessary lift test separates native full-pair compatibility from the already satisfied abstract lattice condition without assuming actual tensor or initial theta data.
SCOPE: K=Q_3(pi), pi^27=3, J and I from L015/L016, L017's fixed compact involution; full model MLF×-pair over identity G_K only. No tensor construction, arbitrary Galois automorphism search, invariant-quotient lifting theorem, new logarithm computation or original-IUT objection is covered.

## Imported theorem and hypotheses

Use the [published primary text](https://www.numdam.org/item/10.5802/pmb.42.pdf#page=36), not an attribution from memory. The [completed source comparison](2026-10-05-degree-27-actual-ind2-group.md) records versions, searches, exact definitions, proof cases and access evidence. Hoshi's model pair has the full absolute Galois group G_K and the unit monoid in an algebraic closure; an automorphism is a pair compatible with this action. Corollary 7.7's kernel over identity G is Ind×, as defined by profinite-unit exponentiation. Import this known theorem without reproof. It does not classify automorphisms of the already invariant or torsion-quotiented additive space.

The specialization must first restrict to G_K-invariant units O_K^times, then justify how exponentiation acts after the continuous logarithm. L016 already establishes logarithm continuity, its full image J and Z_3 stability; no new analytic formula or approximation is needed. The exact values defining A, B, w, z and g are in L017. Reuse its proved integrality and involution; do not recompute the orbit or invent a tensor realization.

## Bounded test and relevance

Determine whether there is a full-pair automorphism over identity G_K whose induced action on J is g restricted to J. A necessary scalar condition from the imported theorem must be justified under the stated logarithm identification. Test it on L017's explicit values rather than sampled matrices. A negative answer stops this full-pair/identity-G lift route only; a positive answer must exhibit the compatible full-pair map, not just a lattice matrix. Either outcome clarifies one concrete bridge toward the original comparison. Arbitrary changes of trivialization, nonidentity G_K and weaker forgotten structures require separate coverage.

Initial theta data, an actual tensor summand (source j starts at 1), the ind3-defined input, pilot transport, essentiality and normalized finite B >= A remain unresolved. This test has no bearing on L017's already audited auxiliary radius 243 versus 81 except its possible realization. No proof of liftability or nonliftability is derived in this assessment.

A canonical write-up should use the normal Hypotheses, Conclusion, Proof, Mathlib sections and classify the application as REPRODUCTION. Supporting/full matching Mathlib coverage: **not checked**. This newly written ready continuation needs the supervisor's separate next-turn approval before invocation; no dependent mathematics was performed this turn.
