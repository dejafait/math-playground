# The proposed coefficient-weight retest repeats the old moment family

WHY IT FAILS: the precise Romik v3 (3.3) coefficient formula has a fixed
integration weight, not an additional degree-dependent multiplier.
Its normalized coefficients are moments in the basis already used by
[L530](../lemmas/L530-two-atom-pollaczek-outward-flow-root-loss.md).
Replacing that measure by arbitrary two-atom probabilities on the
previously proposed closed [0,1] domain repeats the failed implication.
The [source comparison](../drafts/literature/2026-10-30-theta-pollaczek-weighted-discriminator.md)
records the normalization and distinguishes the actual non-atomic
theta measure, whose support excludes the endpoint atom at 1 in L530.
No failure for that particular measure or a narrower smooth class is
inferred. Reopening needs a proved additional restriction and an
independent test; the nominal weight alone supplies neither.
