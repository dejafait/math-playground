# Growing-order boundary attempt908: working checkpoint

Approved target: assessment906's exact range 2<=m<=floor((log s)^(1/4)).
Input: C466a's audited density qualifications, third-derivative disk estimate,
two-regime Fourier bound and exact tilt/scale identity. L018 fixes conventions.
Main gap remains L030-L032/C032a, with contact signs and propagation unpaid.

Provisional mechanism: split at T=log s, below A_s=s sqrt(v_s). The local
Taylor error is bounded by C s^(-1/4)(log s)^(-1/2)|t|^3. Split the
two-regime tail exponent in half to retain exp(-c T^2/2) and an integrable
exp(-c sqrt(|t|)/2) factor. Weighted errors should cost at most factorials
in derivative order. A crude adjugate estimate for the Gaussian derivative
matrix should cost exp(O(m^2 log(m+1))), still exp(o(log s)) in the trial range.

Unfinished checks: common constants for all derivatives, Gaussian inverse
and determinant normalization, actual g_s(0)^m division, and uniform onset.
No growing-order theorem is claimed in this provisional checkpoint.
Continue only if the full normalized relative error is <=1/2 uniformly;
otherwise preserve the exact failed comparison. No global PF or RH inference.

Completion908: the proposed comparison closes. Full reasoning and precise
source qualifications are canonical in
[C466g](../lemmas/C466g-growing-order-reciprocal-density-boundary-signs.md).
This earlier provisional record is retained; its unfinished checks are now
addressed there, with independent conceptual audit still pending.
