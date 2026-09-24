# Sublinear saddle threshold test — 2026-09-23

Gap: actual-theta exterior Laguerre positivity through L266's height-only witness cutoff. Target: extend the controlled saddle asymptotic to n≥a^(4/5)(log a)², n≤Ca for fixed C, to reduce the uncovered large-height indices to a sublinear set. Continue only if both local and complementary-contour errors tend to zero relative to the signed Gaussian mass. Lower indices and bounded heights remain explicit later gaps.

Redundancy and previous failures: L269 proves fixed proportional ranges only; no recorded result supplies this sublinear range. L268's variance obstruction discards oscillation and is not used as a sign argument. The earlier contour-location exploration lacked a relative remainder; this step rechecks that remainder as δ approaches zero at a polynomial rate, rather than substituting a vanishing ratio into L269's theorem.

## Result and decision

[L270](../lemmas/L270-sublinear-index-laguerre-positivity.md) proves the target. Set ε=sqrt(M log a/h) with fixed sufficiently large M. The local relative error is O(a²(log a)^(3/2)/h^(5/2)), hence O(1/log a) at the chosen lower threshold. The complementary bound has a polynomial prefactor at most O(a^6(log a)²), overcome by exp(−c hε²)=a^(−cM). The swapped envelope box remains exponentially suppressed in n. All constants are checked without a positive lower bound on n/a.

ADVANCE: the uncovered large-height indices shrink from an unspecified sublinear regime to n<a^(4/5)(log a)². Compared with the actual required range 1≤n≤K(a)~πa/(2 log 4), this still omits a diverging number of indices, including every fixed index. No RH candidate or all-degree positivity is obtained. One focused threshold step completed; zero consecutive unresolved exploration turns.

Further small logarithmic optimizations of this modulus-based remainder are not the next target. Its local error exposes the power barrier h^(5/2) versus a². A concrete next test is to integrate the cubic and quartic Taylor corrections against the complex Gaussian exactly: odd total degree cancels on the symmetric domain, but one must check the quartic and squared-cubic contributions and their remainder before inferring a better range. This retains oscillation in the remainder itself and might address the remaining lower-index gap; no such bound is asserted here.

## Mathlib

Full statement and supporting coverage: not checked, as in L270. No library match is claimed.
