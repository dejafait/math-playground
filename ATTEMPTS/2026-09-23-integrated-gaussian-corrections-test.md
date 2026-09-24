# Integrated Gaussian correction test — 2026-09-23

Gap: exterior actual-theta Laguerre signs below L270's threshold, needed through L266's height-only negative-witness cutoff. Intermediate target: integrate the first nonzero phase corrections and test whether a controlled residual permits a strictly lower power threshold. Its downstream use is to reduce the possible large-height witness indices; low indices and bounded heights are explicitly unresolved. Continue only if the residual is small relative to the signed Gaussian contribution, not merely if its formal corrections are small.

Redundancy check: L269 uses a cubic modulus bound, and L270 resizes its square. Neither integrates these corrections. The prior sublinear assessment explicitly leaves this test open. L268's variance failure does not address oscillatory Gaussian moments. Existing unfinished changes were preserved.

## Result and decision

[L271](../lemmas/L271-integrated-gaussian-corrections-lower-threshold.md) gives explicit cubic/quartic polynomials and a finite Gaussian-moment formula for the quartic and squared-cubic integrals. Each normalized correction is O(1/a). The odd cubic integrates to zero even on the local square. A controlled exponential remainder has relative bound

O(a²(log a)^(5/2)/h^(7/2)+a³(log a)^(7/2)/h^(9/2)+a⁴(log a)^(9/2)/h^(11/2)).

This tends to zero for n≥a^(3/4)(log a)³, uniformly up to Ca. Polynomial Gaussian tails and the whole complementary contour are also negligible after choosing the fixed square-size constant large enough. ADVANCE: the sufficient threshold is strictly smaller than L270's, since their ratio is a^(−1/20)log a→0. The required range still starts at n=1; no complete RH argument or candidate follows.

One focused step completed; zero consecutive unresolved exploration turns. Continue with a structurally different local-contour test: determine whether a complex linear change of the two saddle coordinates can make the Gaussian decay scale a while preserving admissible theta contours. This could avoid repeatedly increasing Taylor order to improve a modulus remainder, but contour accessibility and complementary bounds are not yet established. The present remainder alone still needs h≫a^(8/11)(log a)^(9/11).

Verification: exact rational arithmetic independently checked the exponential/hyperbolic cubic and quartic coefficients, logarithm coefficients, and all three remainder exponents. SymPy was unavailable; no package was installed. These checks support the written proof and are not an interval certificate or an RH verification.

## Mathlib

Full statement and supporting library coverage: not checked. The Gaussian source identity is proved directly in L271; no library match is claimed.
