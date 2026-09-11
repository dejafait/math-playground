# Frozen third-moment interpolation — 2026-09-13

The scoped attempt interpolated the available normalized frozen block
second and fourth moments to obtain a uniform third absolute moment.
The resulting estimate and its sharp logical limitation are proved in
[L172](../lemmas/L172-frozen-third-moment-and-first-moment-test.md).

WHY IT FAILS: Cauchy–Schwarz yields T^(1/8)sqrt(log T), which is
unbounded, and an explicit probability model attains this scale while
satisfying the two input moment bounds. This rules out that inference
alone, not the desired bound for the actual oscillatory sums. L172 also
isolates a first absolute moment obstruction that requires new information
about those sums; its hypothesis remains unproved.
