# Coarse complete-compression enclosure stop

11 November 2026, step463. Canonical reasoning and qualifications are in
[C744d](../lemmas/C744d-five-cell-coarse-compression-enclosure-insufficient.md).
Full matrix/error evidence is `scripts/five-cell-penalty/compression-463.json`;
the exact obstruction and recurrence checks are in
`scripts/five-cell-penalty/compression-checks-463.json`.

WHY IT FAILS: The approved fixed complete 64-mode test was attempted
with the accepted individual diagonal intervals, a 2048-response Gram
prefix, all ten moments, all nine prime powers and a rigorous uniform
PSD bound for every omitted response. Interval LDL paid only ten of
64 pivots. More than a failed solver is known: the independent box
admits an exact rational artificial matrix with a negative dyadic
Rayleigh numerator below -5.40072056e-10. Therefore universal positivity
of this coarse box is false. This does not produce a negative physical
complete direction; its entries need not share the physical analytic
correlations, and taking zero in a positive-tail interval does not mean
that the actual tail vanishes. The actual complete sign remains open.

Stop this coarse-prefix/independent-diagonal implementation. Another
solver on the unchanged box cannot certify all its members positive.
The already covered complete divided-difference method with materially
sharper diagonal information is a different evaluation mechanism for
the unchanged form, not a penalty/window/basis retuning. No such refined
matrix was calculated here, and its sign margin is unknown. Preserve
C744b's separate truncated-form stop and both source-artifact blockers.
