# Rotated connector modulus test — 2026-09-23

Gap: exterior low-index Laguerre positivity through L266's witness cutoff. Target: bound the connecting faces of L272's simultaneous rotation by o(exp(Φ_*)/a) at h~√a(log a)². This could justify a local contour replacement below L271's threshold; nonlinear errors and the global complement would still need control. Continue an absolute-value proof only if it beats the signed main scale; otherwise require a new cancellation mechanism.

Redundancy: L272 proves strip clearance, not connector estimates. L269–L271 estimate complements of larger real squares, not these rotating faces. Existing unfinished changes are preserved.

## Result and decision

[L273](../lemmas/L273-rotated-connectors-retain-main-scale-modulus.md) proves that each connecting face has absolute integral Θ(exp(Φ_*)/a), at the same scale as the signed saddle contribution. The actual theta/model error is uniformly o(1) on these faces, so this is not merely a formal Gaussian warning.

NEGATIVE: stop discarding these simultaneous-rotation connectors by absolute values. The required bound is little-o of that scale; the achieved two-sided bound excludes it. This does not exclude signed cancellation and gives no new positivity range. L266 still requires indices starting at one and bounded heights remain unresolved.

WHY IT FAILS: The initial angular layer of width 1/(aR²) has bounded modulus decay over a face whose area element is R dα dz. Its absolute mass is therefore of order 1/a. Full mass on the final Gaussian patch and strip clearance do not remove this boundary layer. The full proof is in L273.

One focused test resolved; zero consecutive unresolved exploration turns. A materially different estimate is now needed: test signed oscillatory cancellation on these faces, beginning with the exact quadratic model, before attempting another absolute contour bound. No RH candidate is obtained.

## Mathlib

Full statement and supporting coverage: not checked. No library match is claimed.
