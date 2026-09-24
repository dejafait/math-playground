# Weighted inverse-interval discrepancy checkpoint

The completed L219 checkpoint is preserved. This step expands the exact
integer weight, rather than replacing it by a coprimality density.
For gcd(a,m)=1, on integers coprime to m,
phi(ab)/(ab)=(phi(a)/a) sum_{k|b, gcd(k,am)=1} mu(k)/k.
Insert sum_{j|m,j|b} mu(j); then gcd(j,k)=1 and b is a multiple of jk.
Only k<=floor(2N) is needed. A continuous extension of the exact cell
length, using the max/min endpoint expressions of L191, has uniformly
bounded variation: the lower envelope is convex, the upper concave,
and the positive part of their difference is unimodal, bounded by 2.
Thus progression sampling differs from its integral divided by jk by O(1).
The real main coefficient is (phi(a)/a)(phi(m)/m)
sum_{k<=floor(2N),gcd(k,am)=1} mu(k)/k^2, uniformly positive relative
to the two totient ratios since sum_{k>=2}1/k^2<1.
Resume by checking the extension at real N (ceil/floor outer endpoints),
proving the variation claim, and recording the resulting exact identity
and limitation. No saving or population lower bound is proved yet.

Completed audit: on the fixed v box the two moving product-support
cutoffs are redundant, so the extension is exactly piecewise affine
without rounding error. L220 records the completed identity and error
budget; the separate-error shortcut is archived under ATTEMPTS. The
350 rational checks passed, including 71 positive weighted sums. This
draft is no longer an unfinished checkpoint.
