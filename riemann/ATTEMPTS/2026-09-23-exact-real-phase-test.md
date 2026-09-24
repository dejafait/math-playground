# Exact real phase test — 2026-09-23

Gap: exterior actual-theta Laguerre positivity through L266's witness cutoff. Target: a local saddle asymptotic with error o(exp(Φ_*)/a) at log a≤h≤2 log a, where n is of order (log a)². A successful local estimate could support a lower-index sign theorem if the complementary integral can also be controlled. Test the exact real phase substitution, its amplitude derivatives, and every boundary of the local square. Continue this mechanism if these errors vanish; do not infer global signs without an exterior bound of the same strength.

Redundancy: L275 controls an annulus only at much larger h, and L277 uses rotated inner patches whose strip clearance prevents this low-h application. The exact phase change uses no complex rotation. L269's polynomial strip loss remains relevant outside the square. The existing global result begins at ceil(√a(log a)³), not at (log a)².

Saved calculation before completing proof: put g(p)=sgn(p)√((exp(2√2p)−1−2√2p)/4). Then g'(0)=1 and f(p)=−2a g(p)² exactly. On a fixed small square, the transformed amplitude has bounded mixed variation. A central radius R=a^(−2/5) gives relative amplitude error O(aR³+ahR⁴)=o(1) and oscillatory annular error O(1/(√a R))=o(1). Theta error is bounded by (a^(−1)+exp(−γh))/h with γ>1 if the fixed square is small enough. The full complement has not been signed or bounded at main scale.

## Result and decision

[L278](../lemmas/L278-exact-real-phase-local-saddle.md) proves the full local target, including the transformed amplitude derivatives and all local boundary tails. It also proves that absolute mass outside the fixed squares exceeds the main scale by a diverging factor. Thus no global positivity at indices of order (log a)² follows. ADVANCE is the local low-h asymptotic, not an extension of the global sign theorem. Zero unresolved exploration turns; no RH candidate.

WHY THE ABSOLUTE EXTERIOR APPROACH FAILS: the fixed rectangle 2ε≤s−r≤3ε, 0≤x≤ε/10 has absolute mass at least c exp(Φ_*)a^(−0.02), whereas the required error is o(exp(Φ_*)/a). This is an actual modulus lower bound, not just a weakness of the strip majorant. The canonical proof is in L278. Continue with a signed exterior estimate exploiting the separable phase; low indices below this band and bounded heights remain independent gaps.

## Mathlib

Full statement and supporting coverage: not checked. L278 contains the informal proof; no library match claimed.
