# Quadratic square-root phase truncation

The occupancy audit considered approximating sqrt(uv) by
(u+v)/2-(u-v)²/[4(u+v)] on |u-v|=O(N^(3/2)).

WHY IT FAILS: the discarded quartic term can tend to a nonzero
constant, so this is not a uniform o(1) phase approximation.
[L201](../lemmas/L201-full-core-integer-phase-criterion.md) proves
this with an explicit integer u,v sequence and supplies a quartic
approximation with O(N^(-1)) remainder instead. The example does
not claim the original ordered factor restrictions, and neither
approximation supplies a phase-population lower bound. This
invalidates only the proposed uniform quadratic truncation.
