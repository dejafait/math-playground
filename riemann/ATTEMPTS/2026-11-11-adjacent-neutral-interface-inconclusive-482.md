# Fixed adjacent neutral interface: half bound still unpaid

The single step482 attempt retained the two fixed touching cells, exact
moments, unshifted energy and prime delay. Its full reduction and the
sharp neutral response-tail norm are in
[C744i](../lemmas/C744i-adjacent-neutral-interface-and-sharp-response-tail.md).
The finite locator is `scripts/adjacent-neutral/interface-diagnostic-482.json`;
it is not a numerical certificate or an upper bound for beta_1.

WHY IT FAILS: Exact cancellation removes the completion terms and the
slowest exponential response, but cannot reduce the L2 norm of any fixed
remaining response tail below pi/2. Its sharpness sequence has diverging
logarithmic energy, so that observation also fails to give a relative
counterexample. Finite relative eigenvalues near0.468 and positive finite
matrix margins leave the entire complementary form space unpaid. The
required uniform positive margin in C744i(6) has neither a tail bound nor
certified finite enclosures. This is an inconclusive fixed-threshold
attempt, not an exhaustion or disproof of the energy target. Any further
attempt must retain energy in a rigorous finite-section/tail comparison;
repeating a slow-response L2 truncation cannot improve the sharp norm.
