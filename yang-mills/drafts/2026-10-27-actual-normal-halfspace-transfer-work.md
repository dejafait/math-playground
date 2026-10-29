# Actual normal fields: half-space part of the approved face transfer

2026-10-27. One research attempt under the unchanged ready assessment
`literature/2026-10-27-actual-normal-source-face-transfer.md` and its exact
registered target. Existing changes and earlier unfinished work are preserved.

Main gap: the interacting continuum theory with a nonzero physical sector
and positive mass. Intermediate use: test the deep-layer and tangential
localization parts of the actual normal-source face transfer, retaining
the complete signed kernel and missing bulk second vertices. The separate
finite-cube comparison is not assumed. This is development within the
approved transfer, not a newly approved mechanism or a full solution.

Inputs inspected: L292(1)--(8),(16)--(25), L293(1)--(21), L287(1)--(13),
and L294's statement and source construction. The ready assessment supplies
the source/duplicate comparison; ATTEMPTS/048--049 retain the stopped
absolute-norm and generic gauge-identity arguments. No additional external
theorem is imported or required for the proposed kernel calculation.

Working reduction, not yet a proved result: after tangential Fourier
transform let K(q;n,m) be S_H(q;n,m)-S_inf(q;n-m)-S_inf(q;n+m+1), n,m>=0.
The last term is exactly the missing bulk second-vertex contribution
for the prescribed midpoint even extension. L293's absolute subtracted
loop bounds may imply sum_(n,m)|K(q;n,m)|<=C and a uniformly vanishing
depth tail near q=0. This must be verified for the complete normal-normal
Wilson/density block, including external curls, rather than inferred
from its signed constant-depth row sum.

For the actual localized sources, tangential C^3 bounds from L294 suggest
|hat u_n(q)|<=C A_(k,a) a^-3 (1+dist(q,0)/a)^-3. Together with the
kernel estimate this would give a half-space O(N) bound after the 3a^2
normalization. At fixed depth, midpoint evenness gives replacement by
the trace with error O(a^2 M^2); then L293's sigma(0)=0 should remove
the surface limit. Check Fourier normalization, all source orders,
absolute depth tails, finite-support/even-extension conventions and
complete mode domination before claiming this partial result.

Continuation/abandonment test: establish the uniform absolute defect
bound and fixed-mode half-space o(N) with summable A_(k,a)^2 constants.
If these fail, preserve the precise failing estimate. Even if they pass,
the finite cube need not satisfy the same comparison; no O(N) cube bound
or o(N) cube-to-half-space error follows from local entry convergence.

Unresolved throughout: L294's separate critical audit; the actual
finite-cube comparison, other groups and strata, full-box errors,
uniform higher perturbative remainder and interacting continuum/mass.

## Finite-cube comparison under examination

The exact relative heat images may supply the missing rate. On the
fixed collar and its finite stencil enlargement, all omitted images
are at distance at least cN. The candidate comparison is
|G_N-G_H|<=C N^-2, |F_N-F_H|+|J_N-J_H|<=C N^-3,
and |H_N-H_H|+|P_N-P_H|<=C N^-4, with F=CG and H=CGC*.
These are working estimates until their short/long heat-time cases,
staggered boundary conventions and sandwiched inverse square are proved.

If valid, the complete cubic difference must be bounded before any
external curl is discarded. AA uses two factors O(a A), AB uses one,
and BB uses none. Pairwise kernel differences then have per-anchor
sums O(1), O(N^-1), O(N^-2 log(eN)), respectively. With O(N^4)
anchors this gives O(A^2 N^2 log(eN)) before the 3a^2 normalization,
or O(A^2 log(eN)) afterward. The density and local quartic differences
should be no larger. This would be o(N), uniformly in the mode envelope.
The decisive point is a proved off-face heat comparison, not local
entry convergence or an assumption that the source has zero curl.

## Completed result and limits

The reductions above are completed in
[L295](../lemmas/L295-actual-normal-one-face-transfer.md). The proof
retains the midpoint Neumann and vertex Dirichlet heat images, the
short/long heat-time cases and the sandwiched inverse square. It obtains
the three proposed off-face kernel rates, then an O(log(eN)) normalized
cube-to-half-space error for the full signed normal block. The absolute
Fourier defect has a uniformly vanishing depth tail; tangential C^3
decay and L294's fixed-layer estimate give the actual-source half-space
o(N) limit. The complete external-mode sum is controlled by L294(6).

Thus the registered one-face transfer test passes at the level of the
written proof, with a separate critical audit pending for L294--L295.
The earlier working statements are preserved as a record, not left as
extra assumptions in the conclusion. This is a local partial ADVANCE
under EXPLORE, not a verified novelty claim or a complete Yang--Mills
candidate. All other components, groups/strata, full-box errors and
interacting/continuum/mass obligations remain unresolved.
