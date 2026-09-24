# Small-argument exterior test — 2026-09-24

Gap: global actual-theta Laguerre signs through L266's witness cutoff. Intermediate target: at log a≤h≤2 log a, bound the absolute shifted integral where min(|s+x|,|s−x|)≤r/4 by o(exp(Φ_*)/a). This removes the central-kernel region from a future signed exterior estimate; the remaining exterior, smaller indices, and bounded heights stay unresolved. Continue if the decay absorbs the full δ^(−5) strip cost; abandon this absolute subregion mechanism if it does not.

Redundancy and failures: L269 supplies a global envelope but its stated theorem assumes proportional indices. L278 proves that the whole fixed-square exterior cannot be discarded absolutely. Its obstructing rectangle has both kernel arguments near r and is outside the present region. L275's local annulus does not reach the central kernel. The new test keeps the exact-series envelope, not a first-term approximation near zero.

Saved calculation: set m=max(|s|,|x|), l=min(|s|,|x|). The region is m−l≤r/4. If |m−r|≥r/4, the radial envelope loses exp(−c h r). Otherwise l≥r/2 and exp(2(m−r))(cosh(2l)−1)≥c exp(r/2). Either loss absorbs δ^(−5)=O((a/h)^5). The proof must also integrate the unbounded radial region.

## Result and assessment

[L279](../lemmas/L279-small-argument-exterior-suppression.md) proves the absolute bound C δ^(−5)(r+1)² exp(Φ_*−c h r). Relative to the required exp(Φ_*)/a it is exp(−c' (log a)²+O(log a)), hence tends to zero. ADVANCE is this subregion estimate only; no global sign range changes. Continue with the remaining exterior, retaining higher theta indices because small positive real arguments do not uniformly permit the first-term model. Zero consecutive unresolved exploration turns; no RH candidate.

## Mathlib

Full statement and supporting coverage: not checked. No library match claimed.
