# Hardy-translate localization with the absolute moment-error envelope

The bounded Fourier-dual test and complete error specialization are in
[L637](../lemmas/L637-hardy-translate-dual-cost-and-absolute-error-budget.md),
which passed a separate conceptual audit on 1 November 2026. The original
bump, tolerance, finite complex coefficients, unnormalized atoms and
X-uniformity are retained.

WHY IT FAILS: The dual certificate forces TV at least
c*T^(1/4)*sqrt(log T), whereas making the proved complete absolute envelope
o(T*(log T)^6) requires TV=o(T^(3/25)*(log T)^2). The necessary cost
makes that envelope scale divided by T*(log T)^6 tend to infinity.
This closes the sufficient absolute-budget realization test under L637's
named imports. It is not a lower bound on the true remainder, a failure
of approximation itself, or an obstruction to cancellation-sensitive
estimates. No negative Xi interval or density theorem is assumed.

Reopening mathematical work on this route requires a materially stronger
error mechanism or a different realization dictionary with a new bounded
test. Repeating the filter or the same triangle-inequality envelope adds
no evidence. The originally proposed separate audit is now complete;
no bound or hypothesis changed. Its full replay is canonical in L637.
The absolute-budget route remains parked; this is not a ban on different
cancellation-sensitive mechanisms or realization dictionaries.
