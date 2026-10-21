# Complete L025 target — direct/mixed signed-limit attempt

Approved target: Determine whether L025's complete nonradial quartic-action response -kappa_0(f_(i,0),r_0,S_4-S_(4,rad)) has a finite a^3-scaled limit for both actual L010 probes.

Coverage is the unchanged EXPLORE assessment
`literature/2026-10-16-complete-residual-coefficient-cubic-assembly.md`.
The main construction gap is ultraviolet-uniform interacting matching
with reflected error <=c_box/2, followed by continuum and infrared
control. This attempt concerns only the remaining direct/direct and
two mixed terms in L216(16), not their evaluation or compensation.

Proposed mechanism: use L211's exact A=C^T J C. At fixed lattice
offsets in a compact physical interior, aJ has a constant-coefficient
limit with the displacement frozen and both ordered generator terms
retained. The two differentiated Green columns have a summable
product in four dimensions. First control that product's spatial tail,
then use local relative-to-infinite Green convergence and freeze only
the remaining finite stencil. L211(5) controls the two one-prefix
fiber tails by C/R+C/N after normalization by a. Thus fixed-offset
limits could be summed along the actual lower half-fibers before
the physical Riemann sum. L216 supplies the exterior U/a^2 limit
and the already established two-prefix contribution P_i.

Continue if those local limits are uniform on compact interiors and
the full response error is o(N^3); abandon this replacement if a
nonvanishing normalized boundary/tail error remains. Do not transfer
L065 to mixed blocks, smooth the upper pin, infer convergence from
boundedness, or discard either generator orientation. Essential inputs:
L018 L025 L028 L200 L211 L213 L214 L215 L216. Full heat sums,
constant modes, normal end rows, colors and both subtractions remain.
No mathematical scripts or numerical sign premises are planned.

Completed: L217 proves the local differentiated-Green convergence,
controls the full spatial product tail before freezing aJ, and sums
each original lower fiber using the uniform C/R+C/N tail. The original
direct/mixed block therefore has a finite signed cubic limit. With
L216 this establishes existence of the complete nonradial action
limit, without evaluation or compensation. All full proofs and
qualifications are canonical in
`../lemmas/L217-complete-nonradial-action-signed-cubic-limit.md`.

The new proof still warrants a separate critical audit. In particular,
retain the distinction between the fixed-offset Green limit and the
subsequent infinite half-fiber limit; (15) controls the latter uniformly
before the boundary collar is removed. No matrix is declared smooth
across the upper pin and no infinite inverse is treated as bounded on l2.
