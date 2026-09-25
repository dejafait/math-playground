# Attempt 003 — Excluding the ramified cube branch at 2 or 3

Tested on 2026-09-25. Outcome: NEGATIVE for an exclusion using only the tested exceptional-prime conditions. The global branch restriction remains useful.

## WHY IT FAILS

The proposed intermediate target was a lifting obstruction in system II after imposing u odd, v congruent to 1 modulo 12, and the exact valuation restrictions from L005. [L006](../lemmas/L006-constrained-exceptional-prime-solubility.md) constructs compatible primitive 2-adic and 3-adic points with all those local valuations. Its auxiliary parameters can also be coprime, have the required prime support, and satisfy the real positivity interval. The zero-survivor threshold is therefore unattainable by increasing only the precision at 2 and 3 or combining their finite congruences. The roots at different places are not one integer square. This stops neither tests at other primes nor sieves with further global constraints, descent, or height bounds; it supplies no Beal counterexample.
