# Prescribed scale-adapted band scheme, 29 October 2026

The gate-approved test used width h=u/log T cells, radius 6h disks
and radius-h area collars for h<d_j<=min(2h,1/16), retaining full
multiplicities and clipped windows. The complete specialization is
in [L475](../lemmas/L475-scale-adapted-band-cost-envelope.md).
Its envelope in units of T(log T)^3 is K(u)=E(7u)/u^3,
asymptotic to exp(7u)/(7u^4), so it fails the dyadic-tail test.

WHY IT FAILS: after gamma normalization and reflection, both vertical
directions cost exp(|y|log T). Finite-factor suppression controls
arbitrary occupancy but gives no suppression in a cell with one
simple pair. The continuous area bound therefore overwhelms the
algebraic scale gain. This is a failure of this explicit upper-bound
comparison; it is not a lower bound on actual pair mass and does not
disprove its target. Assuming large occupancy or a small selected
norm would insert precisely the unproved compensation.

Decision: park this geometry-plus-global-norm implementation. Its
reopening needs a materially new independently testable arithmetic
input. The next source-gated direction retains the signed background
in L471 (6), rather than bounding every negative pair separately.
L251's masking example already warns that generic first-sign facts
do not settle all-degree positivity. No signed cancellation estimate
has been derived or approved. Fixed-u bands, d_j>1/16, full B(T),
individual signs and RH remain open.

Outcome: NEGATIVE / RESEARCH / REPRODUCTION. This is local cost
bookkeeping with known tools, not a discovery beyond the sources.
