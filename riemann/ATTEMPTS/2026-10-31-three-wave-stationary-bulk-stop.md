# Equal-amplitude three-wave stationary bulk: threshold failure

The canonical proof and complete certificate description are in
[L577](../lemmas/L577-three-wave-stationary-bulk-clipped-upper-bound.md).
It meets the complete L473 covariance, exact stationary derivatives and
eventual scaled norm, but the clipped mean is at most
0.003136718<13/4000<1/288. This is a one-sided certified integral
bound with every quadrature and trig error included, not a sampled mean.

WHY IT FAILS: Adding a third equal-amplitude wave removes the special
two-wave factorization, but it still cannot supply enough clipped mass
at the prescribed covariance. The explicit 16-by-48 tensor quadrature,
with semiconvex upper errors and exact integer evaluation, puts its
whole expectation strictly below the required threshold. Finer grids
cannot rescue this choice. Stop this model; preserve L576's separate
exact-zero stop. Neither result excludes a different stationary law,
full fourth-moment realization or actual-Hardy transfer. A separate
independent audit of L577's computer-assisted application passed on
2026-10-31: both full integer replays, every rational trig enclosure and
all deterministic errors match; see L577's canonical audit section and
`scripts/three-wave/audit.json`. No stronger result is claimed.
