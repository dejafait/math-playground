# Attempt 049 — direct monomial-degree quotient is not support-linear

Step 528, 2026-10-27. The complete graphs, oriented right-closed maps,
minimal-support proof and resource qualifications are canonical in
[L114](../lemmas/L114-unary-product-degree-quotient-support-obstruction.md).

**WHY IT FAILS.** The common degree-chain graph is linear in the independent
endpoint size, and both arrows satisfy all boundary/transition equations.
But its observable monomial states force each map to contain all the
right-closed residual coefficients. On the explicit n=2^k parallel 1/x
layer family, each map needs 3^k+2 entries against denominator 10n+20.
The support ratio is unbounded even before charging indices or checking
work. This stops that degree-coordinate quotient, including attempts to
compress its description while retaining the same explicit-support
contract. It does not exclude operand-adapted bases, reverse arrows or
longer chains. A different next test uses operand-state coordinates for
a single 1+x layer moved past arbitrary G; iterated composition costs
remain unproved. Attempts 047–048 and earlier stopped receivers remain
preserved, with no change to their scope.
