# Attempt 021 — Extend the fixed retained-transfer scalar exclusion

The approved calculation fixed h_(i+1)+1<2(h_i+1), L041's seed and
prefix/length bounds, the published primitive odd-count threshold and
the explicitly retained integer/count/linear-form restrictions.

## WHY IT FAILS

[L045](../lemmas/L045-retained-transfer-word-count-cutoff.md) successfully
extends this assembled scalar exclusion through seventeen words, but
gives a simultaneous feasible scalar tuple at eighteen. Consequently
these retained constraints cannot exclude that first count. The tuple
does not satisfy asserted individual height, parity or closure conditions
and is not a cycle. Stop the unchanged comparison; any further exclusion
requires materially different retained information or a changed bound,
with separate target coverage. A critical audit of L045 is validation of
the completed step, not another attempt to extend the exhausted system.
Preserve the initial congruence failure and corrected certificate cited
in the canonical result. Universal entry, unrestricted counts/cycles,
divergence and eventual descent remain open.
