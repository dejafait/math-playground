# Full-star-preserving thinning cannot retain both thresholds

WHY IT FAILS: [L126](../lemmas/L126-full-star-thinning-obstruction.md)
uses L125's audited rigidity for identical complete stars to pair all
2552584 nonstar blocks by a bijective polynomial map. Each pair has
distinct supports intersecting in at least 66 points, above 63. At most
one member per pair survives; counting both retained full stars gives
a size-sum upper bound of 2590122 and hence a balanced upper bound of
1295061, below the requested 1532496. This blocks only this repair of
L030's full families when the left distinguished point is in column 16
and both equal full stars survive. The separate 2026-10-25 critical audit
in L126 accepts the restricted proof. The bound is not asserted sharp; incomplete
stars, other columns and other laws remain outside this test. This is
not a universal local cap or an RS list bound, and does not replace
L030's valid single-core counterexample to that cap.
