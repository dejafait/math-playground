# Uncompressed ordered-pair translation action — fixed cost stop

2026-10-16, step 247. This stop applies to the chosen uncompressed
2016-dimensional rational action presentation, not incidence maps or
full descent in general.

## WHY IT FAILS

The domain and full secant inverse are verified in
[L069](../lemmas/L069-conductor389-seven-ordered-pair-domain.md).
The full translation-action stream produced only 329 of 2016 required
columns, 32920675 bytes, across 372.06086778640747 seconds of recorded
writes against a 180-second arithmetic-stage budget. The intended timer
did not wrap that loop; the preserved overrun was externally stopped,
not reported as compliant. The 128-MiB byte limit was not reached.
Translation/curve checks and stored columns have no independent mathematical
replay and supply no quotient, pullback or norm. Costs, the interrupted
producer/report/log and schema-only inspection are in
`scripts/seven-torsion/incidence-247/`; the canonical domain proof is not
duplicated here. Park this fixed action representation. A compressed
scalar-invariant direction presentation is a different, independently
testable mechanism needing separate source comparison and full rational
transports before use. No infeasibility theorem, cap extension, Selmer
claim or ban on a justified new implementation follows.
