# Source and normalization audit — 2026-09-24

This is one bounded source audit and stress test, not a candidate resolution.

## Question fixed before the calculation

Gap: no essential flaw satisfying the hypotheses of an exact IUT claim has been established here. The selected point to understand is the input-volume membership inference in IUT III, Corollary 3.12, proof step (xi-f), following (xi-e).

Intermediate target: test the weakened assertion that an abstract identification of cyclic multiplicative monoids, together with constructions inside one fixed valued field and passage to a lattice hull, forces the input/output log-volume inequality. This weakened assertion must not be silently substituted for IUT's hypotheses.

Downstream use: distinguish a numerical compatibility obligation from mere abstract isomorphism, then locate what the actual construction supplies. An exact application would still need the full initial data, comparison maps, indeterminacies, hull, and normalizations.

Discriminating test: compare the lattices p Z_p and p^2 Z_p with additive Haar measure normalized by measure(Z_p)=1. Check both the abstract generator correspondence and whether it preserves the fixed valuation. If the apparent counterexample changes the latter, abandon it as a direct IUT counterexample; retain only the precise failure of the weakened implication.

## Redundancy and source checks

The local notebook initially contained no lemmas, attempts, or unfinished changes. Other notebooks have existing changes and are outside this step's edit scope.

The official announcement and the current prize page have been read. IUT III's author-hosted PDF is headed May 2020; the author's paper list dates it 2020-05-18. The selected corollary and the 2018 Scholze–Stix critique concern the same volume-comparison bottleneck, but their formulations must not be treated as interchangeable.

The power-map shortcut is already discussed in IUT III, Remark 3.11.1(vi)–(viii). Consequently its arithmetic cannot constitute a new objection to the full theory. The remaining audit concerns compatibility of the actual represented data, not existence of a power map.

## Completed test and assessment

The full calculation is [L001](../lemmas/L001-cyclic-monoid-isomorphism-does-not-control-volume.md). The achieved toy bound is B/A = 2 for A = −log p and B = −2 log p. Because A is negative, the desired B ≥ A would require B/A ≤ 1. The violation is exact, not numerical evidence. However, the same map doubles the fixed valuation, so it does not satisfy even the natural additional valuation-compatibility test. Its abstract degree can be renormalized, but that changes the relationship to the fixed Haar measure.

This establishes no violation for the original output B in the [source record](../foundations/02-comparison-claim-and-sources.md). There is no computed bound for that B. In particular, an example with one output generator cannot decide what happens to the full family of allowed output regions.

The bare power-map shortcut was rejected as a direct counterexample. This agrees with the redundancy check: the primary text already discusses it. The informative work of this step is the source-qualified separation of the weakened implication from the actual comparison obligation; it is not an original IUT-specific obstruction. The step is therefore conservatively counted as exploration, despite recording an elementary lemma.

The remaining uncertainty is whether the actual represented output carries the input's fixed numerical degree after the prescribed operations. The concrete source anchor for investigating that issue is the composite specified in Remark 3.11.1(iii) using Remark 3.10.2. No claim that it succeeds or fails has been established. Current continuation and the single next action are maintained only in PROGRESS.md.

## Checks and limits

The mathematical check is the exact coset-counting proof and the valuation computation in L001. No numerical experiment is needed. Mathlib coverage is not checked. The original initial-data conditions, comparison constructions, and full indeterminacy actions are not verified by this toy calculation.
