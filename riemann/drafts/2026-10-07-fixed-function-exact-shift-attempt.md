# Fixed-function exact-shift attempt — 2026-10-07

Approved scope: the unchanged fixed-function target in
`literature/2026-10-07-fixed-function-exact-shift-common-zeros.md`.
Main gap: actual-theta positivity/total signed margin; this test only
asks whether geometry can force eventual disjointness.

Work in progress, not a proved result. Let a_n=A^n for a large fixed A,
b_n²=a_n²+d_n, and P(z)=prod_n(1-z²/a_n²)(1-z²/b_n²).
At z=a_n-2i, cancellation is equivalent to
 d_n=4a_n tan(phi_n)-4,
where phi_n is the argument of (1+ia_n)/(5/2+ia_n) plus
all other quadratic-factor arguments, with a multiple of 2pi removed
for each earlier pair. The expected center is D_n=2-32(n-1).
Thus b_n is below a_n for n>=2, unlike the isolated quartic.

Pending test: prove the map sends the simultaneous boxes
|d_n-D_n|<=1 into themselves, uniformly in n and in all other
coordinates; solve every finite system by Brouwer and pass to a
diagonal limit with a uniform phase tail. Then prove convergence,
nonvanishing off the stated simple real zeros and order zero directly.
If uniform solvability or exact limiting cancellation fails, keep the
failure instead of claiming a construction. L375 is contrast only;
L068's logarithmic-tail technique needs its real-root specialization
checked. No actual-family physical inequality is assumed.

Completed bounded attempt: the uniform map estimate and exact limiting
equations close. The full statement and proof are canonical in
[L376](../lemmas/L376-fixed-entire-exact-shift-common-zeros.md).
The outcome is negative evidence for geometry-only eventual disjointness,
not a negative result about RH. No numerical script or finite residual
is used. A separate critical audit remains required; the original
work-in-progress notes above are retained as the saved checkpoint.
