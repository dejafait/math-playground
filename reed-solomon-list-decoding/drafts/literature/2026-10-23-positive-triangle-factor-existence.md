# Positive distance-factor existence — completed source comparison

TARGET: Determine whether positive distance-invariant product factors exist for L098's exact distinct-edge demands on all actual permitted triangles, without upper capacities.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step 410's prescribed-marginal/structural-zero/exponential-family searches and source comparison, plus step 411's conditional-capacity assessment; inspected L021,L098,L108,L109,L110 and ATTEMPTS/082,093 for the changed existence-only scope. No repeated broad search or novelty inference.
SOURCE_EVIDENCE: Csiszar–Shields, Information Theory and Statistics: A Tutorial, Foundations and Trends in Communications and Information Theory 1(4) (2004), 417–528, DOI 10.1561/0100000004, Theorems 3.1–3.2 and complete proofs pp.440–443, Remark 3.1 p.444, https://www.renyi.hu/~csiszar/Publications/Information_Theory_and_Statistics:_A_Tutorial.pdf ; directly reinspected PDF pages 27–31 (zero-based) in step 415. Reused the Benamou et al. arXiv:1412.5154v1 comparison in the multiplicative-scaling assessment; no new convergence import.
COMPARISON: The source covers finite full-support linear families, including dependent features; it does not verify this target's full support or distance-factor specialization. L108 gives nonnegative cone membership only. L110, L107 and L109 decide different conditional or restricted tests; ATTEMPTS/082,093 remain parked.
GAP: Establish full feasible support on all actual permitted triangles, justify mass/reference normalization, and justify invariant finite log potentials and absorption of the normalization constant; none is proved in this literature step. Upper capacities remain outside scope.
REASON: The existing finite theorem suffices for a bounded applicability proof without another essential source. Approve the already saved existence-only target for that specialization; do not infer existence from cone membership or repeat the failed capacity certificate.

SCOPE: Exactly the saved TARGET, with the fixed data and exclusions below; source import plus local support/normalization/symmetry proof only, without a numerical factor solve or upper-capacity calculation.
LITERATURE_REASON: The saved REVIEW_REQUIRED target changes the earlier conditional capacity question to existence; its essential comparison is full support and finite distance factors. This is its separate source-approval turn, reusing ready entropy coverage.

## Startup proposal — preserved scope and qualifications

Proposed scope: retain V=all 68-subsets of 1024 points, L021's exact
rational pairs c_i, and N=floor(65537^28/2^128)+1 from L098. Seek real
f_i>0 for 5<=i<=68, x_i=c_i*f_i, with z_T=x_i*x_j*x_h on every
unordered distinct triangle having sides at least five, and z_T=0
on every triangle with a forbidden side. Require each distinct edge
marginal to equal (N-2)c_i. Remove the two endpoint repetitions only;
keep zero demands and all actual-orbit multiplicities. No upper-capacity,
Boolean lower-row, source-PSD or RS realization claim is part of this target.

Essential proposed inputs are L021,L098,L108,L109,L110 and
foundations/04,12,13. Review L108's precise support statement before
using it for a strict-feasibility hypothesis; cone membership alone
must not be silently upgraded to positive product-factor existence.
The earlier entropy source notes are to be reused, with only essential
unread theorem/proof cases retrieved. No entropy theorem is reproved
or applied in the completed audit turn.

Downstream use: decide whether existence can be separated from the
unresolved capacity problem in this ansatz. Continue only if a precise
finite theorem and verified applicability obligations yield an
independently checkable target. If support/attainment or symmetry
hypotheses fail, record the exact obstruction and park that implication.
No factor solve, parameter scan, enlarged allowance or restart of
ATTEMPTS/082 is proposed. A passing existence theorem would still leave
true capacities, Boolean lower rows, full source lift, PSD and the
955–957 RS bracket unresolved. This proposal is not source approval.

Mathlib: matching theorem and supporting finite entropy-duality coverage
not checked. Unknown coverage is not evidence of absence.

## Step 415 — separate source approval

The main gap remains arbitrary-center safety at 67/68 agreements and,
on the current route, L098's shared capacitated-triangle feasibility.
The intermediate target is the exact TARGET above. Its downstream use
is to remove an existence hypothesis from L110's ansatz while leaving
the true capacity problem independent. No existence conclusion has been
established here, and the 955–957 bracket is unchanged.

### Imported theorem scope

For a finite alphabet and a strictly positive reference distribution,
Csiszar–Shields Theorem 3.1 gives a unique projection onto a nonempty
closed convex family, with that family's support. Theorem 3.2 puts the
projection in the finite-parameter exponential family when the linear
family has full support; otherwise it guarantees only its closure.
Its proof uses the span of the constraint vectors, without an
independence hypothesis. Remark 3.1 gives the restricted-support form.
The support argument, full-support span argument and boundary-limit
case were all read, not just the statements. Import these results;
do not reprove entropy duality or rely on iterative convergence.

### Exact local work left to the mathematical turn

L108's complete proof and critical audit establish nonnegative cone
membership, actual equilateral triangles at every permitted distance,
and coordinate-permutation symmetry of the unlabeled problem. They
do not state full feasible support on the permitted triangle alphabet.
That stronger hypothesis must receive its own argument. A concrete
test is to try a positive baseline on every permitted actual triangle
and distance-wise equilateral corrections for the residual demands.
This is a proposed support construction to check, not a constructed
weighting or a result of this source review.

Use the actual unordered permitted triangles as the alphabet and the
positive base products c_i*c_j*c_h as the reference before normalization.
Verify total-mass normalization and each edge-incidence feature against
the original demands. Do not substitute vertex marginals or a complete
tensor with different structural zeros. Keep null edges and their
incident zero weights explicit in the full model, even if removed from
the positive reference alphabet. Show why both removed endpoint terms
remain exactly c_i and are restored separately; there is no edge at i=0.

To obtain distance factors, check invariance of the normalized family
and reference under S_1024, then justify the use of unique projected
weights and averaging of real log edge potentials. Averaging positive
factors directly is not licensed. The proof must account for the
normalization constant across three edges per triangle and any
nonunique multiplier representation; uniqueness of factors is not
required or claimed. This is an applicability obligation, not an
assertion that distance invariance has already been established.

Retain every actual t-s class and its multiplicity when translating
back to original orbits. A distance-product ansatz deliberately gives
some different classes equal values; it must not be described as a
source-imposed equality or a general reduction of free triple variables.
Inputs are L021,L098,L108,L109,L110 and foundations/04,12,13. L109's
eight-atom and six-presentation passages were read for this accounting.

Continue if the support construction and these applicability checks
produce finite positive factors meeting every distinct-edge demand.
If a support or symmetry obstruction appears, record the specific
failed hypothesis and park that implication; cone membership alone
and a boundary limit are not successful substitutes. No parameter
scan, factor iteration, capacity allowance, or ATTEMPTS/082 restart is
part of the approved attempt. Even a successful specialization leaves
upper capacities, Boolean lower rows, full source lift, PSD and RS
realization open. No general source theorem needs a local reproof.

### Duplicate and failure comparison

Reuse the search record in
`drafts/literature/2026-10-23-capacitated-triangle-multiplicative-scaling.md`:
prescribed-marginal structural zeros, exponential-family convex support,
generalized iterative scaling, and triangle-edge marginals were searched.
Its inspected Csiszar–Shields passages suffice here; optional unread
1972/1975/1989 original scans remain leads, not premises or blockers.
The Benamou capacity-projection comparison is reused, without a new
browse or convergence claim. No exact local product-existence theorem
was located in that assessment; no originality claim follows.

L108 does not duplicate the positive-product conclusion. L110 and
ATTEMPTS/093 stop an excessive sufficient capacity allowance, not
existence. ATTEMPTS/082 rejects a different numerical prescription.
L107's failed common normalization and L109's restricted box-dual
nonseparation supply neither positive factors nor their nonexistence.
This is the separate review of step 414's already saved target:
SPECIALIZE is ready, while the local mathematical conclusion is open.
