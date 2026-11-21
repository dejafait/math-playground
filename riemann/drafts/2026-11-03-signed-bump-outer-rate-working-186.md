# Signed outer bump rate — step 186

The invocation-start EXPLORE assessment is
`literature/2026-11-03-signed-bump-remainder-rate.md`; its exact target
and fixed L703 profile are unchanged. L714's audited finite inverse,
L715's audited logarithm and L716's audited uniform resolvent ratio
are the materially new inputs since the inconclusive step 175.

Main gap: actual-Xi all-degree mixed positivity. The intermediate
target is the actual signed rate of R_n(3/20) at u=(3+4i)/10. A
comparison with the actual P_n would decide this local boundary-peak
test; complementary defect, the other frequencies/comb/tails/moments,
angular persistence, amplitude/full charge, H/support and realization
would remain independent.

Bounded test: retain R_n=P_n+K_n exactly, insert the audited physical
inverse and ratio, and test the resulting complex phase on the original
real bump. No modulus replaces either defining integral. A signed rate
comparison, including cancellation/zero subsequences, is required to
continue this refinement. A pointwise kernel rate or an error larger
than the outer signed integral is insufficient; absent a new mechanism,
park this refinement in that event.

The recorded signed-bump inconclusive, absolute horizontal-contour and
positive-blend stops have been checked. They do not supply a signed
bound here. The existing source comparison is reused; no new general
saddle or bump endpoint theorem is imported or assumed.

## Saved partial reasoning before calculation

The exact remaining expression is

    K_n=(D_n H_n(0)/h) integral_I chi(v)
             exp(-n*d*v/A + ell_n(exp(-u*v/A))) Q_n(v) dv.

Thus the normalized kernel logarithm is controlled on I by L715 and
the prefactor has an elementary nonzero-factor Riemann sum. L716
controls Q_n uniformly away from zero. These pointwise facts do not
control the signed integral: the phase varies with n and the bump
has no supplied endpoint law. A diagnostic of the limiting phase and
its derivative will distinguish a possible exponential separation
from another outer-cancellation obstruction. Any diagnostic is not
a certificate; the actual fixed bump is not replaced or sampled.

L714 (6), if used, still requires checking its Riemann-sum and positive
compact-support arguments. No rate, lower bound, nonvanishing or
absence of exceptional subsequences for K_n or R_n is assumed.

## Completed bounded test

[L717](../lemmas/L717-signed-bump-kernel-phase-winding.md) records the
full proof and exact certificate. The kernel is eventually nonzero on
I, but its phase variation on the actual plateau is greater than
n*delta/20-pi. Thus no constant rotation, even one depending on n,
aligns its entire integrand in a closed half-plane. All six exact
interval checks pass. This is a new obstruction to a common-phase
lower certificate; it does not evaluate K_n or R_n. Outcome: NEGATIVE
for that tested inference; the approved signed-rate target is unresolved.

The binary64 phase diagnostic suggested a kernel rate near .0057,
compared with a residue endpoint expression near .00017, but neither
number is a certified comparison. It does not supply an actual fixed
bump, a signed integral or evidence for the negative theorem. Its
initial missing-mpmath failure was resolved using a standard-library
diagnostic; the exact certificate uses rational arithmetic independently.
No assertion here uses L714 (6) as an audited residue-rate input.

Park further pointwise-kernel/phase-alignment refinements: they leave
precisely the outer signed cancellation unpaid. The distinct proposed
mechanism is a nonremovable singularity of the generating function in
the size parameter, potentially forcing a subsequential lower rate
without an endpoint law or exclusion of zeros. The exact array and
possible cancellation make its applicability nonautomatic. The separate
nomination in `literature/2026-11-03-signed-bump-size-generating-function.md`
is REVIEW_REQUIRED; no generating-function result is derived or approved
in this step. Earlier stops and all unfinished work are preserved.
