# Signed connector cancellation test — 2026-09-23

Gap: exterior Laguerre signs below L271's threshold, needed through L266's witness cutoff. Intermediate target: the oriented sum of L273's four connectors is o(exp(Φ_*)/a) at h~√a(log a)² and R=κh/a. This could justify the local rotated patch replacement; the complementary contour and lower indices would remain unresolved. Continue if a rigorous signed estimate beats this scale and survives the actual theta/model error; otherwise stop this local replacement mechanism.

Redundancy and previous failures: L272 gives strip clearance only, and L273 rules out absolute-value removal of the faces. The older Fresnel lemmas concern arithmetic short sums, not this contour. This test uses signed Fresnel tails and Stokes, a different mechanism from the two preceding geometry/modulus tests. Existing unfinished changes are preserved.

## Result and decision

[L274](../lemmas/L274-signed-rotated-connector-cancellation.md) proves the required little-o bound for the oriented sum, including the actual theta integrand. The original square's two opposite Fresnel factors and the rotated Gaussian square have the same leading value. Stokes identifies their difference with the boundary sum, and the uniform model error times L273's absolute mass is negligible. The displayed relative errors all tend to zero; the largest recorded asymptotic term is O((log a)^(−2)).

ADVANCE: this removes the local connector obstruction at n~(1/2)√a(log a)³. It does not prove positivity at that scale: hR²→0 prevents absolute envelope suppression just outside the original patch. L266 still needs every index from one through its cutoff and bounded heights remain unresolved.

Continue with a signed estimate for the surrounding unrotated region, because the local replacement now meets its exact threshold. One focused test resolved; zero consecutive unresolved exploration turns. No RH candidate is obtained. Existing unfinished work is preserved.

## Mathlib

Full statement and supporting coverage: not checked. The analytic proof is stored in L274; no library match is claimed.
