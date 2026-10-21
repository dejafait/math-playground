# Uniform third-seed rank-only extrapolation

2026-10-18. The fixed-two-row extension test in
[L111](../lemmas/L111-fixed-two-row-third-support-classification.md)
classifies every disjoint third row at the fixed seven-set. Twenty-six
seeds are excluded, but four have 266 pairwise-linear deficient fourth
extensions in total. Their complete bases and exact rank checks are
preserved in `scripts/seven-coordinate/third-row-variation.json`.

WHY IT FAILS: L110's full-rank property does not persist for all third
rows. In the explicit L111 example, A3={22,33,79,89} and
A4={1,12,75,79} give rank 20 with a complete one-dimensional kernel,
despite pairwise linearity. Thus uniform rank-21 exclusion is false for
these support matrices. This is not a moment-compatible pencil or a
counterexample to fifteen: all L109 decomposability, projection, weight,
chart and remaining-event gates are unresolved. A critical audit and
then a genuinely gated feasibility test may use this residual evidence;
repeating the failed rank-only extrapolation is not justified.
