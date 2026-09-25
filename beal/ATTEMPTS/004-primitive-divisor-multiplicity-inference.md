# Attempt 004 — Inferring a forbidden valuation from a primitive divisor

Tested on 2026-09-25. Outcome: NEGATIVE for the direct inference; the full coefficient system remains unresolved.

## WHY IT FAILS

The audited primitive-divisor theorem applies, but guarantees occurrence rather than an index-indivisible valuation. [L008](../lemmas/L008-primitive-divisor-multiplicity.md) constructs a primitive divisor 373 of U_31 with any prescribed positive multiplicity, including 31, while retaining the norm restrictions, the first-case shape t=3^29 h^31, and the strict trace inequality. Hence these properties cannot force every primitive divisor to have a forbidden multiplicity. The theorem's actual consequence k>=6p-1 is a lower bound, not the zero-solution threshold. The construction does not impose the full perfect-power equality, and the three exact controls fail it modulo 311; no Beal counterexample or impossibility of all divisor methods follows. A result forcing some divisor to have unsuitable multiplicity under the complete equation would be a materially stronger input and is not refuted here.
