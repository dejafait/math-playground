# 2026-10-04 — Combined-response forest-cancellation attempt

## Preflight and bounded target

The saved exact target is to compute the g^2 log(sqrt(tau)/a) coefficient
of L010's remaining two-probe response, including every correction. Reuse
the prior SPECIALIZE assessment in
[literature/2026-09-26-current-target.md](literature/2026-09-26-current-target.md);
no sources are sought or newly imported. The full overview, DAG, L011,
L016, L018, the earlier expansion and stopped isolated-density attempt
have been inspected. Other-notebook changes are preserved.

The local gap is the unevaluated complete one-loop coefficient. A useful
intermediate test is to locate its finite-mesh cancellation under a
nonlinear change of forest, rather than infer a logarithm from M2 alone.
This is different from the exhausted bulk-only locality import and uses
the ready forest/measure coverage. Test whether the action/measure group
is invariant by itself, or exactly which probe/insertion jet terms it
needs. A nonzero missing group stops partial-group extrapolation; an
exact cancellation supplies a correctness check for eventual full lattice
contractions. Neither outcome proves the logarithmic asymptotic, finite
matching, boundary control or reflected error <= c_box/2. The continuum
axioms, infrared limit and finite positive mass remain open.

## Reasoning saved before the calculation

Let the exact transition between two rooted forest slices in exponential
coordinates be theta' = T theta + Q(theta) + C(theta) + O(|theta|^4),
with Q quadratic and C cubic. After scaling theta=g x and removing the
linear map, write y=x+g q(x)+g^2 c(x). Set p=c-(Dq)q/2. Scalar pullbacks
then use exp[-g D_q-g^2 D_p] through this order. Exact reduced Haar
invariance should imply div q=0 and div p=M2'(T x)-M2(x). These identities
would identify a missing Jacobian cancellation not present in an isolated
M2 contraction.

For the action and the two observables, compute all transformed jets and
apply Gaussian integration by parts with W_v=D_v S2-div v. The discriminant
is the change of the action/measure-only covariance group with f0,r0 held
fixed. Its cancellation must be checked against the nonlinear jets,
including the Wilson-flow observable jets already specified in L011.
An exact rational two-link SU(2) Haar-preserving product map can test the
signs and nontriviality. It is a diagnostic, not the actual box coefficient.

## Result and decision

[L019](../lemmas/L019-combined-forest-jet-cancellation.md) gives the explicit
nonlinear coordinate-change jets, their Haar Jacobian, and the variation
of the action/measure group. The variation is canceled by the first- and
second-order observable/residual jets through connected Gaussian integration
by parts. This locates L018's previously aggregate cancellation without
assigning a separate higher vertex to a Hodge law. The calculation applies
at fixed mesh to both original probes, but the original probe-specific
polynomial contractions have not been evaluated.

The exact SU(2) product map (U,V)->(U^-1,UV) tests its BCH and Haar signs.
The first isotropic probe choice f=(u1+v1)^2, r=v1^2 happened to give zero
net action/measure change, despite nonzero isolated Haar change. This
reinforces that an altered density function alone is not a nonvanishing
contraction test. Changing the diagnostic to f=(u1+2v1)^2 gives action/
measure change +4/3, observable change -4/3, and invariant full coefficient
-8/3. Populated jets and a nonisotropic Gaussian also give nonzero group
changes and invariant full coefficients. These are exact diagnostic
identities, not original-box estimates or evidence for a logarithmic value.

Validation command:
`PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_forest_cancellation.py`.
It passes rational checks of the Jacobian identities, group-change formula,
connected integration by parts and independent normalized moment-series
arithmetic. The nonisotropic case retains a nonzero change of S3 and thus
tests the two-S3 term as well. No mesh extrapolation is performed.

Outcome: EXPLORATION / RESEARCH / REPRODUCTION. This is a finite-dimensional
specialization and correctness diagnostic, without a claim beyond the
checked literature. The target logarithm is still undetermined, and the
required reflected-error threshold c_box/2 is unchanged. One of three
inconclusive mathematical turns is used on the combined-cancellation
mechanism; earlier stopped-route evidence and budgets are preserved.

Keep the exact ready Next action and assessment. Further formal coordinate
identities would not resolve the internal loop contractions. The next
attempt must address those actual contractions, retaining all groups and
using L019 only as a consistency check. No additional literature need has
arisen. Physical-boundary subtraction, finite matching, a specified
coupling trajectory, continuum fields, full reflection positivity,
infrared control and finite positive mass remain unproved.
