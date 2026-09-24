# Associated-saddle remainder test — 2026-09-23

Gap and target: actual-theta exterior Laguerre signs through L266's cutoff. Test uniform eventual positivity for fixed 0<λ_0≤n/a≤λ_1. This covers a proportional-index portion of the required linear cutoff, leaving n=o(a) and bounded heights unresolved. Continue this mechanism only if the total relative error tends to zero, including the complementary contour and the logarithmic Gaussian cancellation loss.

Redundancy: the previous complex-saddle attempt located the model saddle but supplied no relative remainder. L268 rules out the quadratic concentration certificate; L239's strip bounds alone are absolute estimates. This step tests the missing remainder, preserving those results and all existing changes.

## Result and decision

[L269](../lemmas/L269-proportional-index-laguerre-positivity.md) proves the full uniform asymptotic with positive leading term. The local square of radius h^(−2/5) has relative Taylor error O(a^(−1/5)(log a)^(11/5)) after accounting for Gaussian cancellation. A global strip bound costs only δ^(−5) for the product, with δ comparable to 1/log a. Outside the saddle squares the envelope loses exp(−c h^(1/5)); the apparently competing swapped maximum is suppressed by (l/m)^(2n). Both errors tend to zero relative to the positive signed Gaussian, not merely its modulus integral.

The continuation test passes: actual-theta D_n(Ξ;a)>0 uniformly on every fixed proportional-index interval for sufficiently large |a|. This is an ADVANCE toward exterior signs, not all-degree positivity or an RH candidate. Against the actual requirement K(a)~π|a|/(2log 4), the result covers a fixed positive fraction of indices but leaves all possible sublinear-index witnesses and bounded heights unresolved. The next useful question is whether the same remainder inequalities admit an explicit sublinear lower index threshold; simply sending λ_0 to zero in the theorem would be invalid. One remainder step completed; zero consecutive unresolved exploration turns remain.

## Mathlib

Full statement and supporting coverage: not checked, as recorded in L269. No library match is claimed.
