# Oscillatory saddle annulus test — 2026-09-23

Gap: exterior Laguerre signs below L271's threshold, as required by L266's height-only witness target. Intermediate target: bound the actual shifted theta integral between the p,q squares of radii R=κh/a and ε=√(M log a/h) by o(exp(Φ_*)/a), at h~√a(log a)². This could complete the local-to-exterior cancellation estimate at that scale. Continue if the error beats the signed saddle scale; abandon this estimate if amplitude variation consumes its oscillatory saving.

Redundancy check: L272 establishes geometry, L273 rules out absolute connector removal, and L274 controls the signed connector sum. None estimates this surrounding annulus. L269–L271 use a local Taylor error whose modulus loss does not reach this scale. The present test keeps the exact separable imaginary phase and bounds the mixed variation of its real amplitude; it does not add another Taylor correction.

## Result and decision

[L275](../lemmas/L275-oscillatory-saddle-annulus-bound.md) proves the requested bound. A nonstationary primitive in one coordinate gains 1/(aR), while the other primitive is O(a^(−1/2)). The amplitude's mixed variation is uniformly bounded by Gaussian integration, so this gives relative error O((log a)^(−2)). The actual theta/model error contributes O(1/h+(a/h)exp(−c h)), also tending to zero.

ADVANCE: the precise annular target is met. No new global sign range is claimed before assembly of the inner patch and far exterior, and this scale alone would still leave the lower indices and bounded heights required by L266. The next direction is that assembly with explicit uniform parameter bounds, since both local boundary and annulus obstructions now have signed estimates. One focused test completed; zero unresolved exploration turns. No RH candidate obtained; prior unfinished changes preserved.

## Mathlib

Full statement and supporting coverage: not checked. L275 contains the full informal proof, with the integration-by-parts estimate proved directly.
