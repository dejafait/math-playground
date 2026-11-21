# Fixed-dictionary dual enclosure limit1571

WHY IT FAILS: The approved residual threshold is strictly below 1/2.
Using only the retained coarse zero data, the implemented Gaussian and
primitive boxes give an exact robust optimum rho>999/1000 on both allowed
grids. The actual rational candidate has certified uniform residual at
most rho=1-approximately 1.40971634415e-43, so its error bound is inadequate.
This lower bound concerns independent enclosure boxes, not the actual
dictionary. It is neither an actual-kernel obstruction nor evidence that
variation-at-most-2 feasible measures exist. The complete calculation,
tail treatment and coefficient amplification are in
[calculation1571](../drafts/2026-11-18-bounded-variation-dual-calculation-1571.md)
and [the rational certificate](../scripts/smoothed-law/bounded_variation_dual_1571.json).

Stop this bounded attempt. More width grid points with the same boxes
cannot change its exact optimum. A sharper direct prime/gamma evaluation
would constitute a specific new input, subject to a separate source
assessment; it is not already derived or approved. The actual cone,
unrestricted variation and unsmoothed Xi realization remain unresolved.
