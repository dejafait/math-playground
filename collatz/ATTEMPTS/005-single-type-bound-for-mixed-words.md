# Attempt 005 — Transfer the repeated single-type starting bound to mixed words

Tested on 2026-09-25. The sharp starting bound for K consecutive (2,1)
blocks is 2^(3K+1)-5. This step tested whether allowing (3,1) blocks
preserves that bound, as a possible way to exclude all infinite itineraries
in the two-type alphabet. A bound allowed to depend on the start is outside
the prior fixed-window obstructions.

## WHY IT FAILS

[L005](../lemmas/L005-mixed-growing-word-congruences.md) verifies that
603 realizes (2,3,2,2), below the proposed length-four bound 8187. The
exact [enumeration](../scripts/mixed-growing-words/result.json) also shows
plateaus in the minimum start at lengths 3–4, 7–8, and 11–12, excluding
strict multiplicative growth of those minima at every extension. These
facts refute that particular transfer and per-extension growth claim;
they do not refute every lower bound tending to infinity. L005 separately
proves a divergent lower bound when one fixed mixed word is repeated,
excluding eventual periodicity, but its coefficients depend on the word.
The uniform estimate needed for arbitrary aperiodic words remains open,
as do other block types and compensation toward universal descent.
