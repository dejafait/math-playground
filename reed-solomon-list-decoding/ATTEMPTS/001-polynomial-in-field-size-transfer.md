# Polynomial-in-field-size decoder transfer

Tested on 2026-09-24: infer the grand list threshold directly from the q^{O(1)} list bound in the formal Corollary 5.1 of TR26-164, by taking q sufficiently large.

## WHY IT FAILS

A polynomial upper bound in q does not imply an epsilon* q upper bound when its exponent is uncontrolled. The [audit's discriminating test](../drafts/2026-09-24-source-and-threshold-audit.md#discriminating-test-and-result) supplies the numerical implication witness; it is not a counterexample to RS list decoding. The [source comparison](../foundations/01-target-and-source-audit.md#current-bounds-located-with-qualifications) preserves the formal/informal distinction and the separately claimed geometric improvement. This rejects only the direct bound transfer. A bound independent of q, or a sharper exponent with quantitative constants, would be a materially different input.
