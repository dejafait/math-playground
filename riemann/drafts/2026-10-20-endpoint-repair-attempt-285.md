# Endpoint covariance attempt — step 285

Gate: the pre-existing SPECIALIZE endpoint-repair assessment, covered
target exactly as saved in PROGRESS at invocation. Main gap: global
mixed positivity. Intermediate test: remove L446's scalar defect by
changing entry 11 while preserving the selected law. Downstream use:
make the derivative-forced cross-covariance feasibility question
meaningful. Success requires exact J=0, exact seconds, support and
all original tolerances on a full eventual real-H ray.

Initial reasoning checkpoint (unfinished, before proof completion):
start with L443's covariance Sigma0 and its complete q. Add
K a(t), with a a nonnegative smooth endpoint bump, then subtract
K E_H(wa)/E_H w exactly. The two recentered endpoint bump responses
in J have opposite signs, since w>=1/4. Choose the bump at the
endpoint with the required sign; retain the whole old J, including
both rare endpoint values. Use width H^-10, so the large endpoint
amplitude can have negligible integrated fourth cost. Positivity and
negative trace follow by adding a positive K multiple and a tiny
signed correction, followed by L419's translated Borel realization.

Pointwise peak control uses the exact high entry
u*x0^2/max(ell^6,sqrt(2)*u)<=x0^2/sqrt(2), not an outer-H average.
L389's exact |x0|=|zeta(1/2+it)| and L391's already assessed
Bourgain consequence O(t^(1/6)) would give amplitude O(H^(1/3)).
Reused source coverage: drafts/literature/2026-10-10-discriminant-unequal-orientation-projection.md,
Theorem 5 (0.5), v2, and its separate signed-k1 audit assessment.
No fresh theorem, changed zeta hypothesis or source search is needed.

The original finite block must be checked: K22+K13=0, so its middle
residual is unchanged, but its first and third need not be exactly
zero. L443's same recentered sine right inverse has zero 11 entry
and can remove the tiny residuals without changing J or the exact
integrated matrix. These size and support estimates remain to be
written and checked; this note asserts no completed construction.

If the endpoint sign, pointwise envelope or translated-support
estimates fail, stop this ansatz and retain the failed inequality.
No derivative-forced cross entry, all-temporal identity, inter-H
consistency, actual sine limit, trajectory realization, clipping,
L413 margin or RH conclusion is being assumed.

Completed attempt: the construction and all quantitative checks are
now recorded in [L447](../lemmas/L447-endpoint-localized-covariance-repair.md).
The exact scalar defect and all three finite residuals are removed;
the complete original moments and supported law are retained.
This initial checkpoint is preserved as unfinished-work history,
not a second proof. The resulting lemma requires separate critical
review; derivative-forced cross-entry feasibility remains open.
