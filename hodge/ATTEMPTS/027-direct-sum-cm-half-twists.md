# Arbitrary CM actions on inherited direct sums

Tested 2026-10-02. Outcome: NEGATIVE. Classification: REPRODUCTION.
Stop the recipe with W=T(S)^{oplus m}, its inherited Hodge structure,
and any unital CM field action through M_m(E).

## Proposed use

Find an effective polarized weight-one half twist, providing an
auxiliary abelian candidate for the cubic action. Algebraic comparison
cycles with S would remain necessary after a successful Hodge test.

## WHY IT FAILS

[L036](../lemmas/L036-direct-sum-cm-actions-have-no-effective-half-twist.md)
proves that every allowed action has conjugate embedding pairs of
equal multiplicity on the top Hodge piece. An action can exist only
for even m, and every CM type then leaves exactly m/2 forbidden top
dimensions against zero required. This holds for fields not containing
E, arbitrary mixing of copies and actions without an assumed adjoint
compatibility. Increasing multiplicity cannot rescue this inherited
direct-sum construction. The conclusion does not exclude different
Hodge structures, other auxiliary representations or algebraicity
of the cubic action.
