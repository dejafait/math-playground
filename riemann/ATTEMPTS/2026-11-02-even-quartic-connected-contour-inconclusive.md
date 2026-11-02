# Even-quartic connected-contour test: inconclusive bounded search

The step-43 calculation tested L673's phase gauge with real quadratic and
quartic terms, allowing connected contours rather than only rectangles.
The complete reasoning boundaries and diagnostic are recorded in
[the working record](../drafts/2026-11-02-positive-cone-quartic-working-43.md)
and `scripts/one-sided-hankel/positive-cone-quartic-screen.json`.
No new theorem or canonical counterexample proof exists for this attempt.

WHY IT FAILS AS A CONTINUATION: the best selected path after the bounded
parameter/spatial search had a dense sampled maximum about -0.00638225,
above the required -0.01. Independently low horizontal-slice values did
not guarantee a connected enclosing contour and were rejected. Exact
polygon geometry checks do not supply continuous exponent bounds. The
search neither proves global quartic optimality nor excludes a better
quartic gauge or contour, and it does not decide the cone distance. Park
further tuning of this tested mechanism unless a materially new idea or
discriminating test is supplied; do not reinterpret the numerical failure
as a mathematical lower bound. L673 and the qualified C673a/C673b stops
remain intact. A proposed exact even rational factor is a distinct next
test, with its analytic branch, signs and rate all unresolved.
