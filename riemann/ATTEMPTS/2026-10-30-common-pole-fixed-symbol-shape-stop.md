# Fixed-symbol shape variation: uniform threshold obstruction

2026-10-30. One approved mathematical attempt under the pre-existing
fixed-symbol EXPLORE assessment. The new canonical proof is
[L528](../lemmas/L528-common-pole-shape-periodic-majorant.md), with its
exact rational certificate under `scripts/common-pole-variational/`.
It awaits separate critical audit. The earlier L526/L527 packet stops
and combined-residual source-overlap stop remain unchanged.

Audit update, 30 October 2026: L528's first separate conceptual audit
validates the full-line majorant, the exact support-period Parseval
identity, the mean and every strict rational comparison. Its original
generator replay is byte-identical; independent arithmetic evidence
is in `scripts/common-pole-variational/majorant-audit-certificate.json`
relative to the notebook. The stop below is confirmed, with no stronger
bound or trace extension. The original provisional wording above
records the pre-audit stage; the canonical audit supersedes it.

WHY IT FAILS: Even allowing sign-changing real even smooth normalized
tests throughout (-1,1), the fixed functional satisfies
sup c(h)<=mu<147/188<pi/4, with a strict gap greater than 1/705.
A pointwise periodic majorant and exact Fourier-series Parseval
averaging cover the entire frequency line and all such tests. Thus
varying only this shape cannot reach the pi/4 absorption threshold.
This neither evaluates the true supremum nor extends the generic trace
formula to this class. It does not exclude different symbols/supports,
independent collective comparisons or RH. Reopening requires a material
change to the functional or a demonstrated error in the new bound;
repeating finite trial spaces cannot overcome a valid uniform estimate.
