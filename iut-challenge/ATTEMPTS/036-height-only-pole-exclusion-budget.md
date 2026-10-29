# Height-only pole exclusion — automatic enlargement stopped

WHY IT FAILS: The exact interval-only added cost and the source's
residual sufficient budget are proved in
[L116](../lemmas/L116-interval-pole-exclusion-budget-obstruction.md).
Bounding that cost by the retained scalar height leaves an explicit
deficit at large H. This is an upper-estimate failure, not an actual
cost lower bound. L116's separate numerical relaxation saturates the
interval itself, but is not an L089 member or an elliptic-curve
counterexample. No actual-family nonexistence or IUT flaw follows.

Step475 stops the automatic height-only deduction using the unchanged
finite-set theorem. A new continuation proposes arithmetic averaging
on the actual fixed coefficient lattice, which needs separate source
coverage and a joint same-member argument. Merely changing prime-counting
constants, repeating the scalar cap or ignoring interval overlaps does
not supply that information. The existing source and family qualifications
remain in force; this historical stop is not a ban on new arithmetic input.
