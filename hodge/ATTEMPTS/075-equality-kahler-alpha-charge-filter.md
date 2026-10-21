# Equality-kernel normalized Kähler energy filter

2026-10-19. Tested the gate-approved normalized Kähler alpha-charge
criterion in both factor orders, retaining the pure term and full tensor.

WHY IT FAILS TO EXCLUDE THE KERNEL: [L131](../lemmas/L131-equality-kahler-alpha-charge-compatible.md)
computes strictly positive charges while both spectral minima equal -1.
Thus neither the negative/null-charge tests nor the strict spectral-gap
test applies. This parks precisely the normalized Kähler filter and
automatic splitting from it, without proving kernel existence or banning
other calibrations. Reopening this filter requires changed data or a
different applicable theorem; another recalculation of the same charge
is not a continuation. The separate Spin(7) lead needs actual-instanton
and orientation/source coverage before any mathematical application.
