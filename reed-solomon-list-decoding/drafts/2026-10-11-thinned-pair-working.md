# Approved threshold-thinning test — working record

Target: Test exact global pair feasibility at T=floor(65537^28/2^128)+1 using independently thinned L030 moments, with all Johnson eigenspaces and the augmented constant coordinate retained.

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-11-thinned-global-pair-threshold.md`; its TARGET
matches the checkpoint exactly. This invocation therefore performs the
approved calculation, resolving the reported matching issue without
changing the assessment or treating the earlier process rejection as
mathematical evidence.

Main gap: arbitrary-center 68-agreement safety, with independent
67-agreement safety unresolved. Intermediate test: one changed global
pair prescription at the first integer exceeding the true threshold.
Downstream use: discriminate whether this pair-only prescription is
still obstructed near the threshold. Feasibility stops this exclusion
diagnostic; infeasibility excludes this assignment only. Neither proves
a uniform bound, a representing measure, an RS list or a boundary change.

Inputs read: L051 including its critical review, L030's full pair-count
argument, L021's normalization and exact verification, C001a,
foundations/09 and /11, ATTEMPTS/033. The supplied assessment already
checks the other duplicates and local failure routes. No essential
source coverage is missing and no fresh source review is needed.

Use f=T/M=theta*rho and F=f sum_i b_i A_i, a_i=v_i b_i.
Fixed a_0=1, a_1,...,a_4=0 and a_i=theta*v_i*d_(7-i)/N_(7-i)
for i=5,6,7. Nonnegative a_8,...,a_68 are free. The imported spectral
and Schur theorems make the exact test s_j=sum_i q_ji*a_i>=0
for j=1,...,68, and s_0>=T. This is a direct specialization of the
assessed theorem, retaining all 69 eigenspaces and singular cases.
Do not impose L051's zero-variance or triangular kernel equations.

Initial bounded plan: try one exact first-61-row candidate, then if
needed use high-precision phase-I linear programming and exact basis
reconstruction. Save full vectors and all inequalities to disk.
Discovery status is not proof; accept only a complete exact primal
or dual certificate. Failed reconstruction leaves this slice unresolved.

Unfinished: no feasibility claim yet. No mathematical input outside
the approved target is being tested.


Completed: first-61-row candidate fails spectral rows 63,64. Decimal
phase I takes 115 pivots and its exact primal fails rows 60,62.
An exact direct dual eliminates every free coordinate; its constant
weight is zero and the fixed bound is negative. Two integer tail
simplifications fail; the third rational tail 23191266/140599441
produces a compact 61-equation witness. All failures are preserved.
The independent coefficient/weight reconstruction passes all 5172
checks. Canonical proof: lemmas/L052-threshold-thinned-global-pair-infeasibility.md.
This stops exactly the approved prescription. Separate critical proof
review requires the new REVIEW_REQUIRED assessment; no boundary or
complete-resolution claim is made.
