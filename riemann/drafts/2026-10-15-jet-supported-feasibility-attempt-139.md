# Step 139: compatible-jet feasibility attempt

Target: the exact COVERED_TARGET in the supplied step-138 SPECIALIZE
assessment. Main gap: actual mixed positivity; downstream diagnostic:
whether the complete existing matrix forces the missing joint sign.
Continue if one law meets every stated scale and exact support; a failed
ansatz alone does not decide feasibility. L410 omits the matrix, L412
stops a frozen-height pairing, and L413 omits averaged moments, so none
decides this test. Their stops remain unchanged.

Initial work in progress, saved before the full argument: extract a finite
positive quartic measure on unit critical-jet directions and the compact
response annulus from the established actual fourth moments. Use the
already covered Bayer--Teichmann Corollary 2, with a constant coordinate,
and finite-dimensional subsequence compactness. This does not require
an unproved actual distribution limit or phase independence. The quartic
map has 21 matrix entries, d^2 and d B0^2. Its limit fixes the exact
coefficients, not rounded approximations.

Candidate lifting: rescale these finitely many directions by lambda
ell^2 and assign masses proportional to lambda^(-4) ell^(-4). Reverse
the critical triple where necessary so Delta Bcal is nonnegative while
avoiding Delta>0,Bcal<0. The exact curvature perturbation and possible
zero leading discriminants require explicit checking. The signed cubic
then has order ell^2 and may determine lambda. A remaining negative-
Delta atom of critical amplitude O(sqrt(ell)) can enforce the first
mean exactly without changing the quartic limits. Must still verify
strict positivity of the cubic tuning coefficient, all-real-H bounds,
the response lower bound, both U envelopes and physical ordinary-jet
conversion. No feasibility result is claimed in this checkpoint draft.

Completion: compactness extraction is unnecessary. A weighted pushforward
of the actual jets on each auxiliary interval already gives bounded
quartic data. An exactly calibrated positive scaling matches the cubic
mean, and one bulk atom fixes the first mean exactly. The full proof and
quantifiers are canonical in
[L414](../lemmas/L414-compatible-jet-joint-sign-moment-obstruction.md).
The law is explicit as a pushforward/integral formula; no numerical atom
locations or limiting actual joint distribution are asserted. Conditional
atomic replacement gives at most 29 atoms if desired. Separate critical
review remains pending. Existing literature coverage was reused; no
additional browsing or mathematical script was needed.
