# Step 453 — full product global comparison completed

The approved target was: Test the global Johnson spectral lower bound against the diagonal correction for L112's full included-anchor matrix.
The prior SPECIALIZE assessment is
`drafts/literature/2026-10-24-full-product-johnson-kernel-comparison.md`.

The entrywise and exact-root anchor reasoning was saved here before the
finite evaluation. Its completed canonical proof, hypotheses, precise
source imports and qualifications are now in
[L120](../lemmas/L120-full-product-global-comparison-inconclusive.md).
No source theorem was reproved and no novelty is claimed.

The single unchanged-box test is complete and inconclusive: all 69 global
modes and 64 corrections were evaluated, but the comparison enclosure
strictly straddles zero. Independent polynomial reconstruction checked
all 4761 integer coefficients and every bound; 5206 checks pass, with
zero failures. Full evidence is in
`scripts/finite-support/full-product-global-comparison.json` and
`scripts/finite-support/full-product-global-comparison-verification.json`.
The straddle stop is recorded in
[ATTEMPTS/099](../ATTEMPTS/099-full-product-global-comparison-straddle.md).
No refinement, retuning, midpoint test or new root was attempted.

The plausible downstream use remains a full included-anchor PSD
certificate at the root, but this sufficient comparison supplies none.
Full source PSD, excluded-anchor PSD, global uniqueness, measures,
packing, RS realization and 67/68-agreement safety remain unresolved.
The exact current continuation and pending approval are in PROGRESS.md.
