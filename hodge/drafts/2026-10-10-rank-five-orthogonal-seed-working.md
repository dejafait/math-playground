# Rank-five orthogonal seed — bounded attempt

Target: Determine whether L079's acyclic stable orthogonal rank-five block J_5 exists at the exact metric h.

2026-10-10, step 186. Reuse the pre-existing EXPLORE assessment
`drafts/literature/2026-10-10-rank-five-acyclic-orthogonal-existence.md`.
The universal primitive-Hodge gap, common product kernel and transport
remain unresolved. This attempt addresses the seed prerequisite only;
the approved scope explicitly permits that intermediate result.

Inputs: L052's actual marked S,h and integral perpendicular lattice
Zk with k^2=-14; L079 identifies the desired rank-five block but is
motivation, not an existence premise. Read the relevant L053 source
specialization and preserve ATTEMPTS/043,/045,/053. No duplicate seed
construction was found in the scoped local comparison. No cross-notebook
input is used.

Working calculation: proposed E has v=(2,k,-3), v^2=-2, c_2=-2.
Yoshioka Theorem 0.1(1) supplies a torsion-free stable sheaf at general
H. Need a justified near-h general H and slope stability before using
the stable-hull argument: a defect of length t changes v^2 to -2-4t,
incompatible with simple K3 self-Ext for t>0. For an equal-slope
saturated rank-one factor at h, c_1=nk and the Chern equation would be
-2=length(Z)+length(W)+14n(n-1), which is impossible.

Pending at initial checkpoint: write the general-polarization and real-endpoint
bridges completely; then check cohomology and the actual split symmetric
form on O_S plus E plus E^vee. No stable rank-five deformation is yet
claimed. Stop this bounded step after a proved seed input; use the next
invocation for its form-preserving deformation model and realization.

Continuation test: retain this recipe only if the actual exact-h seed
exists and its perfect quadratic form has a justified deformation model.
Even a formal solution will not settle analytic realization, underlying
vector stability or J_5 existence. The seed itself has a trivial summand
and cannot be presented as the required stable acyclic block.

Completion: the seed prerequisite and all its applicability checks are
now canonical in L080. No deformation calculation was undertaken in
this bounded seed step. The unchanged pre-existing assessment still
covers the same existence target and its skew-adjoint deformation
component. Source rechecks confirmed the already assessed theorem
statements; they were not a new literature discovery turn. Current
routing and the single next action are in PROGRESS.md.
