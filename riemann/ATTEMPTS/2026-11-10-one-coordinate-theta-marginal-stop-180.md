# One-coordinate theta marginal: pointwise stop, step180

The exact fixed n=2 marginal of the complete derivative-profile kernel
was tested under the existing EXPLORE assessment. Its full expression,
convergence proof, moment comparison and strict negative diagonal
limit are canonical in
[C969a](../lemmas/C969a-one-coordinate-marginal-negative-diagonal.md).
The independent step182 audit accepts the statement and proof without
correction; its full checks are recorded in that canonical file.

**WHY IT FAILS.** Integrating one coordinate does preserve positive
terms at the fastest two-coordinate growth rate, so L969's full-kernel
stop alone does not decide this test. The exact contraction also retains
both parts of the distant derivative subtraction and its two repeated
origin-factor placements. Actual theta-series monotonicity bounds the
remaining positive moments by the corresponding h moments; with the
prescribed normalization the resulting diagonal coefficient is strictly
negative. Thus one exact average does not yield a nonnegative
two-variable kernel. The proof uses no numerical normalization bound.

Retire this one-coordinate pointwise rule. Neither a negative value of
the final double integral nor any failure of all-index L966(16) follows.
The full-kernel, older profile and finite-window stops remain intact.
A different averaged observable or payment mechanism would require its
own discriminating target and source assessment; none is derived here.
