# Local quotient density: proposed specialization coverage

TARGET: Construct a local relative-Coulomb quotient chart for L279 at fixed mesh and test equality of its complete g^2 source coefficient with R(s,t), including the full Haar and gauge-coordinate density jets and every variable normal link.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed exact-target comparison in 2026-10-25-relative-coulomb-source-representation.md; the proposed specialization uses precisely its stated scope and obligations, with no new source search or calculation.
SOURCE_EVIDENCE: Polyak https://arxiv.org/pdf/math/0406251v1 section 3.1, printed pp. 11–12, Remarks 3.1–3.2; Reshetikhin https://arxiv.org/pdf/1008.1411v1 Theorem 3 and proof, printed pp. 29–30, and local qualifications pp. 31–32; standard finite-dimensional analytic inverse-function and change-of-variables theorems. Full source comparison and access qualifications are in the parent assessment.
COMPARISON: General local quotient integration is known; the all-face relative chart, density jet and exact two-source comparison are mathematical specialization obligations. The temporal slab and linear Gaussian comparison cannot replace these checks.
GAP: Verify the local product map and orbit uniqueness, compute density through degree two with normalization and determinant sign, justify fixed-mesh source localization, and compare the complete logarithmic coefficient with L279(22).
REASON: A concrete alternative to the parked forest-contraction mechanism is now source-covered; deriving this applicability difference is justified, while reproving general gauge-fixing theory is unnecessary. Separate recovery review on 2026-10-25 approves this unchanged target for a later mathematical attempt after verifying direct primary URLs; no specialization was derived here.
SCOPE: L003 and L279, SU(2), fixed even N and a=8/N, real f_*, all-face pinned boundary-contained links, variable normal links, full four-dimensional d* slice, the unchanged bare reflected plaquette pair and sources near zero. No global slice, source-uniform remainder, mesh growth estimate or continuum conclusion.

Use the [completed comparison](2026-10-25-relative-coulomb-source-representation.md),
especially its five applicability obligations, source proof qualifications,
duplicate checks and continuation/abandonment test. L011 is needed only
as L279's already recorded expansion method. Do not use an unread
lattice theorem, a new gauge measure, or a linear transport of higher
jets as a premise. The expected classification is REPRODUCTION;
no claim beyond known finite-dimensional quotient methods is proposed.
Mathlib coverage of the full statement remains not checked.

## Separate recovery review: direct source verification

LITERATURE_REASON: The supervisor reported missing direct URLs in this
ready assessment. This bounded retrieval repairs that evidence field;
it does not reopen the completed search or change the target.

[Polyak, version 1](https://arxiv.org/pdf/math/0406251v1), section 3.1,
assumes a free, proper, isometric action and an invariant measure.
Remarks 3.1–3.2 describe the section/orbit Jacobian and justify the
constraint derivative by changing orbit coordinates at its unique zero.
This is a density prescription conditional on a valid section.

[Reshetikhin, version 1](https://arxiv.org/pdf/1008.1411v1), section 6.1,
assumes a free action, smooth quotient, compact ambient manifold,
invariant volume and analytic phase, finitely many critical orbits,
and a section intersecting each orbit once with invertible constraint
matrix. Theorem 3's proof uses this unique intersection in (34) to
identify the determinant. Section 6.2, printed pp. 31–32, restricts
the asymptotic construction to transverse neighborhoods of critical
orbits; section 6.3 begins by checking the semiclassical term. Its
oscillatory expansion supplies no Laplace remainder for this notebook.

These directly inspected passages preserve the parent's five
specialization obligations. Determinant orientation/absolute value and
normalization require checking the actual pulled-back positive Haar
density; the displayed signed determinant is not an automatic
positive-density identity. Neither source proves the all-face box chart
or complete two-source coefficient equality. Essential local inputs
remain L003 section 1 and L279 (7),(20)–(34); L011 supplies only the
existing expansion method. The parent's duplicate checks and
ATTEMPTS/047 stop evidence are reused. No new source obstruction was
found, and no unread lattice theorem is a premise.

Approval is for the unchanged SPECIALIZE target and REPRODUCTION
classification. This is a STALLED process repair, with no new result,
no exploration-budget reset, and no change to lemmas, scripts or DAG.
