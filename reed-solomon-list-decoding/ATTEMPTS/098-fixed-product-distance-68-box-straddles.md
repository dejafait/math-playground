# Distance-68 unchanged-box spectral test — inconclusive and parked

WHY IT FAILS: The complete signed interval evaluation at the unchanged
L112 box has 22 strictly positive modes (47–68) and 47 strict straddles
(0–46), including the full constant-anchor mode. It has no negative
upper endpoint. Thus neither requested certificate is obtained: no
whole-shell PSD certificate and no fixed whole-box negative direction.
This is enclosure failure, not matrix infeasibility. The prior assessment's
straddle stop applies; no refinement, alternate enclosure, factor change,
midpoint verdict or added shell is attempted.

The full application record, precise reused imports, all hypotheses and
limitations are in
[the step-451 working record](../drafts/2026-10-24-fixed-product-distance-68-working.md).
The constructor and independent complete actual-union/beta certificate
are `scripts/finite-support/fixed-product-distance-68.json` and
`scripts/finite-support/fixed-product-distance-68-verification.json`:
69 relations, 414 presentations, all 69 modes, 10606 independent checks,
zero failures. The least positive interval lower endpoint divided by
c68 lies in [426459,426460)/10^6, at mode 47; this does not bound the
unresolved modes. L112–L119, L106/ATTEMPTS/089 and L026/ATTEMPTS/018
retain their distinct scopes. No main-gap or 955–957 boundary change
follows. A proposed global-kernel comparison needs separate literature
approval; no new mathematical result is claimed here.
