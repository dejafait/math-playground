# Rotated saddle strip test — 2026-09-23

Gap: low-index exterior theta Laguerre positivity required by L266. Target: remove the a/h Gaussian cancellation cost via a complex linear rotation, with a strip-contained Gaussian neighborhood. A successful local geometry test could support a lower sufficient index threshold, while contour connectors, global errors, lower indices, and bounded heights would remain unresolved. Abandon this rotation as a direct all-index certificate if its admissible Gaussian mass collapses at low indices.

Redundancy: L269–L271 use real local coordinates after a common t-shift; none rotates the mixed quadratic form. L268's variance obstruction concerns a different, nonoscillatory certificate. The previous assessment explicitly proposed this test. Existing changes and unfinished work were preserved.

## Result and decision

[L272](../lemmas/L272-rotated-saddle-strip-clearance.md) diagonalizes the quadratic phase by opposite rotations in u+x and u−x. It gives real decay of order a and the exact strip restriction √2 sin θ R<ρ~h/(2a). A Gaussian-sized admissible square can capture asymptotically all mass only when n≫√a log a. Fixed indices fail this condition decisively. A radius providing polynomially small Gaussian tails requires n at least on the scale √a(log a)^(3/2), with suitable constants.

NEGATIVE: stop the proposed direct all-index use of this rotation. This is new strip-clearance evidence, not a negative actual-theta sign and not a general impossibility theorem for contour methods. The geometry leaves a potentially useful threshold below L271's |a|^(3/4)(log |a|)³, but no additional positivity range is proved. The actual requirement still begins at n=1 and includes bounded heights.

WHY IT FAILS: On this specific rotated square, imaginary kernel displacements have order its radius, whereas the available strip clearance is only order h/a. At fixed index this is much smaller than the Gaussian width a^(−1/2). Extending the square far enough would leave the established analytic domain. The exact proof is in L272; no assertion is made that every admissible contour has this obstruction.

Continuation assessment completed in one turn; zero unresolved exploration turns. The next useful test is to control the connecting contour boundary at h≥√a(log a)², where both Gaussian localization and strip clearance have room, before claiming a lower sign threshold. A local homotopy by itself does not discard its boundary terms.

## Mathlib

Full statement and supporting coverage: not checked. No library match is claimed.
