# IUT flaw challenge: argument overview

No candidate demonstration of an essential IUT flaw has been developed. The [challenge scope](foundations/01-challenge-scope.md) and [precise comparison claim](foundations/02-comparison-claim-and-sources.md) fix the source versions and distinguish the original claim from simplified models.

## Unresolved gap

The selected bottleneck is the inference from linked output data to input-volume membership in IUT III, Corollary 3.12, step (xi-f). In the notation A and B fixed in the source record, the required result is finite B with B ≥ A. No counterexample satisfying the original hypotheses, or proof that an essential inference is invalid under those hypotheses, has been supplied.

The unestablished bridge is compatibility between the actual comparison maps and numerical volume after all allowed images, hull formation, and normalization. The comparison path can be simplified at the level of its stated objects; this does not by itself furnish a linear realization or a numerical bound. An elementary hull collapse retains enough information to detect containment, but an identity composite alone does not identify the particular input degree with the collapsed output class. The remaining issue is transport of the distinguished pilot with its markings and global localization data. In an ordinary model, even a category whose every morphism respects global localization has objects of unbounded degree: its morphisms preserve a marking defect without forcing that defect to vanish. A successful objection must retain the source's realified and formal categorical structure and account for its numerical realization.

## Partial results

L001 establishes an elementary diagnostic: abstract generator-preserving cyclic-monoid isomorphisms and constructions in one fixed field do not force an inequality between lattice log-volumes. The apparent counterexample has volumes −log p and −2 log p, but its map doubles the fixed valuation. This diagnoses a weakened implication; it is not a counterexample to IUT. The underlying power-map issue is already present in the primary discussion, so no new IUT-specific advance is claimed.

L002 records the formal comparison-path cancellation and a conditional finite-packet normalization check. For linear transport T between labeled reference lattices O and P, the volume defect is exactly ν_P(TO); a common weighted determinant tensor power cancels after normalization. This rules out an artificial normalization discrepancy in that model. Its linear-realization hypotheses have not been established for the full IUT output, and it yields no estimate for B.

L003 validates the subgroup version of hull collapse: equal images mean equal subgroups or two subgroups contained in the collapsed hull. For p-adic lattices, log-volume descends after also collapsing all degrees at most the hull's degree, although exact log-volume does not descend. This preserves a conditional upper-bound test; it neither proves nor refutes the required identification for the actual input. Literal region containment is stronger than the numerical inequality and is not imposed as a necessary IUT hypothesis.

L004 tests markings at all places in an ordinary arithmetic line model. Local maps with multipliers c_v imply only d(input) + Σ_v log |c_v|_v ≤ d(output). A common rational multiplier has zero total defect by the product formula. However, ℓℤ and ℓ²ℤ with their usual real norms admit separate local isomorphisms with total defect −log ℓ and reversed global degrees. Their local arrows cannot be glued to a global norm-compatible morphism. This rejects local-marking existence as a sufficient test; it does not instantiate or invalidate the original formal transport.

L005 imposes global compatibility on every arrow of the ordinary marked category. Its connected components are exactly the total-defect fibers δ, with sharp degree ranges (−∞, d(output) − δ]. Thus the compatibility axiom does not itself remove the L004 object or give the desired bound. An arrow to the identity-marked output exists exactly in the zero-defect component. This distinguishes a compatibility axiom from existence of a particular comparison arrow; the effect of IUT's realification and formal quotient on this model invariant is not established.

## Known traps checked

- Original hypotheses are retained by precise source reference; a p-adic toy example does not instantiate them.
- Abstract degree renormalization is distinguished from fixed Haar-volume normalization.
- A common determinant tensor power is applied to both compared degrees; its cancellation neither identifies different ring structures nor supplies input membership in a hull.
- The Θ-pilot output involves all permitted images and a hull. A single chosen representative cannot stand in for that output without justification.
- Formal categorical quotients are distinguished from set quotients. Failure to preserve ordinary intersections does not, by itself, refute a formal construction, and loop closure is distinguished from membership of a particular input class.
- Localized global objects are distinguished from local arrows that come from a compatible global morphism. Frobenioid linearity means Frobenius degree one, and does not identify a map with a fixed-coordinate inclusion. An ordinary global morphism is a sufficient comparison mechanism in the model, not asserted to be necessary for IUT's numerical inequality.
- Compatibility of all morphisms in a category is distinguished from a global marking on each object. Ordinary connected components are not identified with a formal categorical quotient, and a negative marking defect is not by itself a violation of the numerical inequality for every object in that component.
- The prior critique and response are recorded as arguments to examine, not as correctness certificates.
- A missing derivation in this notebook is not a demonstrated contradiction. Neither abc nor prize adjudication is being resolved here.
