# Uniform square-root saddle assembly — 2026-09-23

Gap: exterior Laguerre positivity through L266’s height-only negative-witness cutoff. Intermediate target: a positive full saddle asymptotic uniformly for √a(log a)²≤h≤2√a(log a)². Its downstream use is to cover a previously untreated band below L271; lower indices and bounded heights remain separate unresolved steps. Continue if every contour error is o(exp(Φ_*)/a), and abandon this assembly if the strip loss or a domain mismatch leaves an error of main scale.

Redundancy and failure check: L269–L271 prove higher-index ranges. L273 rules out discarding connectors absolutely; L274 bounds their signed sum, while L275 only bounds an annulus. None already assembles the full integral in this band. The review retains signed cancellation and checks the rotated-square versus original-square inclusion explicitly.

## Result and assessment

[L276](../lemmas/L276-square-root-scale-saddle-assembly.md) supplies the complete informal assembly. The inner rotated model error integrates against mass O(1/a), the signed connector and annular errors are little-o at that scale, and the complement costs at most a^(7/2) times an arbitrarily strong fixed power saving obtained by choosing the outer radius constant. All comparisons hold uniformly over the integer band. No numerical experiment or external theorem lookup is needed for this step.

ADVANCE: strict actual-theta Laguerre positivity is established in a new band of indices of order √a(log a)³. This is less than the actual requirement of every index through a linear cutoff. In particular it does not supply the interval between this band and L271. The next direction tests adjustable patch radii over that interval, because simply increasing h with R=κh/a would eventually invalidate the small Taylor and connector errors. No interpolation theorem is asserted here. Zero unresolved exploration turns; prior unfinished changes preserved; no RH candidate obtained.

## Mathlib

Full statement and supporting coverage: not checked. L276 records the full informal proof and the supporting estimates used; no library match is claimed.
