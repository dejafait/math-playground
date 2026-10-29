# 094 — Cyclicity leaves the complementary global operation unevaluated

2026-10-25, step 551. EXPLORATION / REPRODUCTION. The actual-map
placement and complete degree-sign computation are canonical in
[L166](../lemmas/L166-complementary-yoneda-global-extension-operation.md).
They establish no bracket value, new bound or counterexample.

WHY IT FAILS TO PROVE VANISHING: The actual composite through r lies
in a global Ext^1 group, not the sheaf Hom group used for rj=id.
Pairing it against the full K gives a triple trace; cyclicity changes
the 1,1,2 expression into a 1,3 pairing with the same value, not its
negative. Neither local splitting nor the disappearance of the stalk
Ext^1s evaluates this global operation. Park cyclicity-only vanishing;
reopening needs an independently justified geometric identity for this
actual class or its section evaluations. This does not prove that
vanishing is false, and no abstract model is substituted for F.
Preserve ATTEMPTS/068,/092,/093. Polynomial compatibility is a different,
unreviewed test; L165's pointwise scalar lifts do not supply it.
