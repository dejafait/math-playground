# A full subgroup orbit as sixteen distinct bad challenges

Tested 2026-09-25 on the order-16 subgroup H of F_97^*. The proposed
mechanism shifts one four-sparse error by every element of H and allows
an arbitrary nonzero scalar normalization at each shift, with the aim of
placing all sixteen syndromes on one affine line. Sixteen distinct bad
parameters would exceed the budget at q=97^20.

WHY IT FAILS: The full
[orbit classification](../lemmas/L009-two-character-orbit-obstruction.md)
shows that a four-sparse error whose orbit spans at most two syndrome
dimensions must be supported on an order-four coset, with weights
proportional to x^(-u). Such an orbit has only four projective directions.
An affine line containing all its normalized shifts cannot contain zero,
so it meets each direction at most once. This supplies at most four
distinct parameters, below both the target sixteen and the existing
two-block count ten. The obstruction holds over every extension and
does not depend on a failed numerical search. It stops this full-orbit
construction, not general lines, partial-orbit configurations, or the
grand challenge. The detailed test and its scope are in the
[assessment](../drafts/2026-09-25-sixteen-challenge-budget-test.md).
