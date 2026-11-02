# 2 November 2026 — inverse-parameter polynomial attempt (step 50)

One proof attempt used the unchanged ready EXPLORE assessment
`drafts/literature/2026-11-02-inverse-parameter-polynomial-separator.md`.
No further literature review or new source assumption was needed.

[L675](../lemmas/L675-inverse-parameter-polynomial-range-and-degree-cost.md)
gives an exact polynomial action-range condition, a complete angular
preimage and bounds that apply to all preimages. An explicit cubic has
the prescribed zeros, normalization and closed-segment signs, but its
inverse is too expensive. The broader degree<=3*n/7 obstruction has
rate at least 1503/97790>1/100. This is an informative NEGATIVE for the
low-degree subfamily and local progress on range identification, not a
resolution of the full polynomial target or certified progress beyond
all literature. The full matching theorem was not found in the reused
bounded search; no originality claim follows.

Exact rational support is saved in
`scripts/one-sided-hankel/inverse-parameter-polynomial-check.json`.
All 19 arithmetic checks passed and the complete checks array was read.
They do not constitute a separate audit of the analytic proof. L675 and
L674 remain separately unaudited. The new DAG row uses only L666;
the older stops are comparisons, not mathematical inputs.

Decision: preserve the full target and its unchanged ready assessment.
Any successful family must eventually use degree above 3*n/7 and satisfy the exact
coefficient conditions and the full weighted angular cost; no high-degree
nonvanishing or cost bound is assumed. The scoped low-degree stop is in
`ATTEMPTS/2026-11-02-inverse-parameter-low-degree-cost-stop.md`.
Original H, support, Xi realization and all-degree signs remain open.
The scoped documentation checker passed: 747 nodes, 1832 edges, with
complete coverage, acyclicity, valid links and compact overviews.

## Preserved overview detail before the compact update

Audited C645g/h/r/v/w, L658/L661--L664/C663a/b; C645/L646 open. Unaudited: L647--L657/L659; stops L665/L667/L668/L670/L671. Audited L669: fixed-angle loss/log n unbounded; L672: e=0 complex-span <=O(n)e^(-11n/1000); L673: cone <=O(n^2)e^(-n/200). Unaudited C673a--d: contour stops; L674: specified positive-real disk cost >=c(67/66)^n. Segment signs/cone/H/support/Xi open.
