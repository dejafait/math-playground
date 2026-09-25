# Attempt 001 — Excluding a signature by unrestricted congruences

Tested on 2026-09-24. Outcome: NEGATIVE for this mechanism; no conclusion about the truth of Beal follows.

## WHY IT FAILS

The proposed intermediate target was a modulus with no primitive residue solution for a chosen exponent triple. [L001](../lemmas/L001-primitive-local-solubility.md) constructs pairwise coprime integer representatives above every lower bound for every modulus, and nonzero primitive p-adic solutions at every prime, including primes dividing the exponents. The needed number of surviving classes is zero; the construction leaves at least one for every modulus. Increasing the modulus or prime-power precision cannot meet the target without additional restrictions. This stops only an unrestricted local-solubility exclusion. Congruence sieves on a set constrained by a global descent, height bound, or other arithmetic condition are not refuted, and the result does not limit global modular methods.
