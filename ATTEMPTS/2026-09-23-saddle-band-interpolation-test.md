# Saddle band interpolation — 2026-09-23

Gap: actual-theta exterior Laguerre signs through L266's height-only witness cutoff. Intermediate target: a uniform saddle asymptotic on √a(log a)²≤h≤a^(3/4)(log a)³, connecting L276 to L271. Downstream use: remove the intervening index gap; lower indices and bounded heights remain unresolved. Continue if all relative errors tend uniformly to zero; abandon this radius mechanism if any connector, annulus, or exterior term remains of main scale.

Redundancy and previous failures: L276 covers only a factor-two h band. L271 starts at n≥a^(3/4)(log a)³. L273 rules out absolute removal of connector faces, so retain L274's signed sum and L275's oscillatory annulus. The new choice freezes the inner radius at R=κ(log a)²/√a instead of allowing it to grow with h. This is a uniformity test of the existing mechanism, not a new contour or a claim of all-index positivity.

Initial calculation saved before assembly: √a R=κ(log a)²; aR³=κ³(log a)^6/√a; a h R⁴≤κ⁴a^(−1/4)(log a)^11. All vanish as required (the first tends to infinity). The radius stays below κh/a. Check uniform strip clearance, connector mass, R<ε, the annular amplitude variation, the full complement, and overlap in n rather than just h before asserting a result.

## Result and assessment

[L277](../lemmas/L277-uniform-saddle-band-interpolation.md) supplies the full informal uniformity proof. The strip clearance, absolute connector error transfer, signed Fresnel comparison, oscillatory annulus, and exterior envelope all meet the little-o target. The largest new connector term is bounded by a^(−1/4)(log a)^11. The overlap is checked in n: the new interval includes all indices from ceil(√a(log a)³) up to L271's starting threshold. The two results thus give a single eventual positivity range up to any fixed linear upper bound.

ADVANCE: the intervening gap is removed, but the requirement is every index from 1 through L266's cutoff, not just this upper interval. Low indices and bounded exterior heights remain missing. This completes one focused interpolation step, with zero unresolved exploration turns. No numerical check or external citation is needed for these asymptotic inequalities; no RH candidate is recorded.

The reason for the next direction is L272's geometric barrier for shrinking h: strip-contained square rotation cannot capture full mass there. The exact separated imaginary phase from L275 offers a materially different local mechanism, a real change of variables reducing it exactly to a quadratic phase. Its amplitude remainder and boundary behavior must be tested before claiming signs below the present threshold.

## Mathlib

Full statement and supporting coverage: not checked. L277 records the full proof, using existing proved Fresnel, Gaussian, and theta estimates. No library match is claimed.
