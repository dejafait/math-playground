# Refined strip envelope test — 2026-09-24

Gap: smaller logarithmic-index Laguerre signs in L266's witness range. Target: retain the factors 1+(πδexp(2|y|))^(−5/2) from L269 and obtain absolute complement error o(exp(Φ_*)/a) for every fixed h>5. This would combine with L288's positive-sector coefficient; sublogarithmic indices and bounded heights would still be unresolved. Abandon this particular absolute certificate if its own majorant has a main-scale or larger contribution in a fixed complement box.

Redundancy check: L290 uses the coarser uniform δ^(−5) loss and proves a sufficient threshold approximately 9.91. Its cutoff optimization cannot reach 5. The present test concerns the unweakened argument-dependent majorant, not another choice of that cutoff. L288 controls the positive sector only and does not control this box by signed cancellation.

Saved calculation before completion: near s=x=r/2, one kernel argument is bounded and the other is r+O(1). Only the bounded argument retains an exp(5r) strip loss. Together with exp(9r/2), the polynomial factor 2^(−2n), and the principal normalization, the proposed relative envelope mass has exponent [5/2−2(h−9/2)log 2]r. Check this using a box strictly inside the mixed-sign sector so there is no boundary-only artifact.

Result: [L291](../lemmas/L291-refined-strip-envelope-obstruction.md) proves a two-sided estimate for that box. The refined majorant fails the required little-o test for 5<h≤9/2+5/(4 log 2), approximately 6.303. This is a NEGATIVE result for the proposed certificate, not a negative Laguerre coefficient and not an obstruction to RH. It does not claim sufficiency above that threshold.

WHY IT FAILS: the small-real-argument kernel factor retains a large strip-bound cost on a positive-area mixed-sector box. Refining the prefactors alone still leaves more mass than the signed principal scale. Further cutoff tuning cannot remove this fixed box from the complement. A materially different test is to reflect the negative argument using theta evenness and examine the exact mixed-sector summand phase for a nonstationary cancellation estimate. Zero consecutive unresolved exploration turns; no RH candidate.
