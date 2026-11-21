# Exact endpoint filter: bounded fixed-pivot construction stops

10 November 2026. The attempted homogeneous null-sequence construction
would solve successive rows through a fixed coefficient and use a
uniform bound on the resulting recursion to control exponential
growth. [L991](../lemmas/L991-endpoint-filter-fixed-pivot-unboundedness.md)
proves that every fixed-coordinate elimination has unbounded ratios
along exact integer indices where that pivot is nonzero, of either
sign. Its proof and precise qualifications are canonical there.

WHY IT FAILS: C990a supplies only nonvanishing of the full coefficient
vector. The bounded-recursion shortcut is false even away from the
leading cross-product collisions; avoiding those neighborhoods or
merely choosing another fixed pivot cannot repair it. Any exact zero
pivots must still be handled. This does not show that matrix products
grow too quickly, construct a growing null sequence, or disprove the
original inverse implication. Stop only this bounded fixed-pivot
construction. A refined implicit finite-section or solution-specific
argument requires its own uniform infinite-horizon estimates; changing
notation or inspecting longer numerical products is not that input.
The prior synthetic, lobe, averaging and Vaughan stops are preserved.
