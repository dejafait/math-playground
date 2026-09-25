# Attempt 002 — Excluding a repeated-cube signature from its quadratic factor alone

Tested on 2026-09-25. The single-factor shortcut fails; the exact factorization remains a useful intermediate input. This is not an obstruction to every descent or modular argument in the family.

## WHY IT FAILS

After splitting a^3+b^3=c^p, it is insufficient to assert that the positive primitive quadratic factor a^2-ab+b^2 cannot equal v^p or 3v^p. [L003](../lemmas/L003-repeated-cube-factorization.md) gives exact coprime witnesses for both shapes at p=5, and proves that the missing sum-power condition must be imposed simultaneously. The witnesses are not Beal solutions. The same lemma's positivity intervals grow with the auxiliary base, so they supply no upper height bound or uniform empty interval. The failed claim is a single-factor exclusion; the two fully constrained square-discriminant systems remain unexcluded.
