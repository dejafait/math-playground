# Attempt 013 — A shifted dyadic valuation budget for postspell depth

Tested on 2026-10-05 under the inverse-to-height EXPLORE assessment.
Candidate mechanism: use the loss of v_2(11x+23) during B^J as a
consumable budget controlled at the original word boundary, and use
L023's actual preceding-word requirement to prevent replenishment.

## WHY IT FAILS

[L024](../lemmas/L024-postspell-shifted-valuation-replenishment.md)
proves that this valuation equals 4J+2 at every word input, falls to
2 after B^J, and can be replenished without bound by the remaining
O^H E^2 even for a fixed W(2,3) with an actual preceding word.
Its fully guarded three-word witness violates boundary nonincrease;
finite coding also rules out every finite depth bound depending only
on this starting valuation. Stop that consumable-valuation mechanism.
The roots vary with the prescribed finite chain, so neither an
arbitrary divergent root-height bound nor the Collatz conjecture is
refuted. Preserve Attempt 012's independent minimum-transfer failure.
Bounded coalescence on the surviving least-root cylinder is a different
possible target; its applicability and prior obstructions need separate
source review before any mathematical attempt.
