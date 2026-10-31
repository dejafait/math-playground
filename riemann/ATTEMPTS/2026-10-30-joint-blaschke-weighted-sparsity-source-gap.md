# Joint local Blaschke extraction: source-comparison stop

The proposed target is the exact mesoscopic pair mass in
[drafts/literature/2026-10-30-joint-blaschke-mesoscopic-mass-coverage.md](../drafts/literature/2026-10-30-joint-blaschke-mesoscopic-mass-coverage.md).
This turn performed only source comparison; it derived no bound or
counterexample.

WHY IT FAILS: retaining all selected pair factors is already part of
[L474](../lemmas/L474-small-displacement-pair-mass-via-local-blaschke.md)
and [L475](../lemmas/L475-scale-adapted-band-cost-envelope.md).
Extracting additional zeros is a possible change, but the inspected
unconditional count theorems do not bound the sparse neighborhoods
with the required pair-quotient or disk-norm weight, and the mesoscopic
CLT does not cover fixed scales. Assuming the needed occupancy or
weighted exception saving would insert an unresolved premise. L475's
exponential envelope and local single-pair example remain evidence
about that tool only, not a disproof of the actual mass target.

Park this implementation until an independently testable weighted
selection/correlation input appears. A separate concrete lead is
Maples--Rodgers v2 Proposition 2.5's count-only L2 estimate; its
normalization and restricted indicator proof need a conceptual audit
before kernel use. The full inspected-source record and the proposed
restricted audit are in drafts/2026-10-30-joint-blaschke-source-review-working.md
and drafts/literature/2026-10-30-maples-rodgers-indicator-audit-coverage.md.
This new local-density input changes the mechanism from disk-supremum
suppression to integrated count control; no improvement is presumed.
