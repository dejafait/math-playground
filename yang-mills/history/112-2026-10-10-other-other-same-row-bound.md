# 2026-10-10 — Other/other same-row class removed at leading scale

STEP_ID: YM-20261010-112-other-other-same-row-bound

One RESEARCH / REPRODUCTION proof attempt under the unchanged ready
[assessment](../drafts/literature/2026-10-10-other-other-cubic-leading-scale.md)
established [L086](../lemmas/L086-other-other-same-row-bound.md).
Outcome ADVANCE is local: the complete same-row class is O(N^(3/2))
and the explicit two-gradient term is O(N), so neither contributes at
a^3 scale. This specializes existing finite spectral and smooth-column
methods; no result beyond the sources checked is claimed.

The proof uses the correct full-array O(N^2) curvature estimate and
both interior endpoint weights, not the stopped upper-source bound.
All ordered pairs, pinned rows, both residual orders and heat modes
remain. Cofactor expansion exhausts the same-row class. The canonical
proof is analytic; no numerical script or source review was needed.

The unchanged target continues through the six distinct-row terms;
their joint scaled coefficient would need to be -4 gamma D_i before
the outside factor 3. Existence, value and stronger powers are still
open, and the smooth Z estimate is not an estimate of rough V.
[Continuation notes](../drafts/2026-10-10-other-other-same-row-attempt.md)
preserve this limitation. No full compensation or candidate is claimed.
Mathematical exploration usage is 0 of 3 after this relevant bound.
Documentation validation uses the notebook-scoped structure checker.
