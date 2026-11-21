# Centered theta-power endpoint comparison — step427

The approved target was G_w>0 on [1,3/2] x [40,45], or one
rigorously nonpositive value there. Neither was established.
The exact source-based derivative, tail bound and endpoint diagnostic
are recorded in [C999f](../lemmas/C999f-centered-theta-power-derivative-endpoint-comparison.md).

WHY IT FAILS: After retaining the moving center, completion and theta
logarithm, the finite signed integral remains uncontrolled. Its tail
after x=2 is below 10^(-61), but the full unsigned enclosure is only
(-68,68). In the integrated kernel representation, modular symmetry
makes every endpoint term from finite integration by parts zero.
Bounding the remaining integral only in absolute value therefore
cannot decide the sign. The negative central kernel value in C999f
is not a nonpositive value of G_w. This parks that particular endpoint
comparison, not the uniform sign statement, event-restricted product
sign, the theta family or RH.

Reopening requires a materially refined signed comparison. The proposed
contour mechanism has not been tried or approved; its normalization,
logarithm branch, boundary terms and effective dominant contribution
need separate review. No backend retry, parameter sweep or new smaller
box is justified by this inconclusive attempt.
