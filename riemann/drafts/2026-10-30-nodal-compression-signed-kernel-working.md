# Conditional nullvector nodal compression — working record

2026-10-30. Active bounded attempt under the unchanged EXPLORE gate
`literature/2026-10-30-weil-nodal-nullvector-compression-coverage.md`.
The initial unfinished checkpoint is retained below; the completed
calculation is now canonical in L523.

Main gap: actual-Xi all-degree positivity. Intermediate target: at
L522's conditional normalized nullvector, additionally assuming the
complete form is nonnegative on this fixed interval, test whether
positive/negative-part compression forces S<=P-H in L516. Such an
inequality would force zero boundary flux, leaving realization,
positive-eigenvalue family estimates, collars and Xi transfer open.

Retain L515's reference part domain, L516's complete signed form,
L521's BV conclusion and L522's individual prime limits. No sign,
simplicity or nonzero nodal part is assumed. L522's nonzero left
trace and excluded reflected-endpoint collision remain hypotheses.
The standard domain citation is Fukushima–Oshima–Takeda, second
edition, Theorems 1.4.1 and 1.4.2(i), pp.25–28, already inspected
in the saved assessment; it applies only to the reference form.

Initial pending checks: specialize the exact continuous and atomic cross
kernel, justify its integrability for clipped vectors, apply the
weak null equation without division by nodal norms, and compare
the resulting fixed-shift overlaps with L522's Stieltjes derivatives.
Continue only for a concrete signed derivative restriction. Static
overlap identities alone park this implementation; they are not a
counterexample to the actual arithmetic criterion. Preserve L517's
non-eigenvector obstruction and L518's adjoint-residual stop.

Completed disposition: the exact signed-kernel specialization and
admissible inward-variation check are in
[L523](../lemmas/L523-complete-kernel-nodal-compression-and-inward-dilation.md).
The static compression leaves the signed slopes uncontrolled; the
inward energy derivative has the compatible, nonnegative sign.
This implementation is parked as recorded in the
[attempt disposition](../ATTEMPTS/2026-10-30-weil-nodal-compression-slope-gap.md).
No off-line zero, logical independence theorem or new positivity
range was obtained. No mathematical script was needed.
