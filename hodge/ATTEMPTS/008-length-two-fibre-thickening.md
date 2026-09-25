# Attempt 008 — Adding the length-two fibre thickening

Date: 2026-09-25. Outcome: stopped for the transverse NS-fixed RM direction.

The tested scheme is C union B_2, where B_2 is the inverse image of the length-two point at (t_+,t_+) on the base conic. Its fundamental cycle is [C]+2[F_+ x F_+], so it still acts as U. This was a nonreduced replacement for the failed reduced fibre addition, not an assumption that multiplicity supplies a lift. The full proof is [L011](../lemmas/L011-length-two-union-retains-cubic-obstruction.md).

**WHY IT FAILS.** The local ideal (s,r^2 z) still bounds a lifted thickened component's normal displacement by a simple pole in z. Both layers of its nilpotent filtration have the genus-one no-pole property, forcing that displacement to be regular. A flat length-two component therefore persists in any global lift. Its residual is flat even if the component deforms by r^2=epsilon b, so the original C would have to lift. The kernel remains three-dimensional against four RM tangent dimensions required. This stops the specified thickening; it neither rejects every nonreduced representative nor gives a Hodge counterexample. The new evidence motivates changing the representation of the class rather than repeating this fibre-component test.
