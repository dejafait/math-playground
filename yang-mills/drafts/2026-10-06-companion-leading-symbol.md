# Companion leading-symbol attempt

STEP_ID: YM-20261006-057-companion-leading-symbol

Reuse the unchanged SPECIALIZE assessment in
`literature/2026-09-26-current-target.md`. The main gap remains the
complete fixed-box Ward coefficient and its cutoff dependence. The
intermediate target is the strongest apparent a^-4 contribution to
L041(4), before comparison with L039's a^-2 term. Continue if the
direction-summed principal contribution cancels; otherwise retain its
explicit coefficient and reassess compensation. Even cancellation leaves
subleading powers, the scaled limit, all other jets, the logarithm and
the interacting reflected-error bound unresolved.

Existing inputs checked: L040's exact compressed stencils and smooth
flowed bounds, L041's relative form bound and pinned diagonal identity,
ATTEMPTS/013 and /015. No prior result evaluates this unflowed diagonal.
This is not a repetition of the failed axial annihilation: the local
residual symbol is expected to be nonzero, with only its direction sum
canceling after contraction.

Reasoning checkpoint (not yet a proved asymptotic): freeze the first
physical derivatives M_jk of the compressed displacement at a point.
Write lambda_j=2-2 cos(theta_j), lambda=sum lambda_j and w_j=M_jj.
The affine residual symbol should be
sigma=(1/4) sum_j w_j lambda_j(lambda-lambda_j) when sum_j w_j=0.
The local dipole Green contraction is then
kappa_mu=integral lambda_mu sigma/lambda^2 over the normalized torus.
Permutation symmetry gives sum_mu kappa_mu=0; individually
kappa_mu=c w_mu with c>0. A variational exhaustion argument in the
discrete energy norm may justify the local limit without assuming a
continuum diagonal approximation. The full boundary collar must be
retained using L041's uniform bound. This would prove only
a^4 T_(i,a)->0, not the required O(a^-2) or a^2-scaled limit.

Completed: the canonical proof is L042 in
`../lemmas/L042-companion-leading-symbol-cancellation.md`. Its discrete
energy approximation justifies the full local dipole limit uniformly
away from physical faces. The principal diagonal is c_* w_mu with
c_*>0, so it is nonzero directionwise but sums to zero. Uniform
boundary-collar bounds then prove a^4 T_(i,a)->0 for both probes.
The other two H,L products separately have signed sums O(a^-2), using
the smooth flowed diagonal and exact pinned summation by parts.
All 15 exact Laurent-identity checks pass with zero coefficient defect.
No rate was obtained for the energy approximation. The resulting
o(a^-4) estimate does not exclude a^-3, other slower divergences, or
establish an a^2-scaled limit. The proposed principal-symbol test is
complete; the quantitative remainder is the unresolved continuation.
