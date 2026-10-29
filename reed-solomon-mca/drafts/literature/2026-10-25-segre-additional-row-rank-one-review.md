# Additional-row factor locus — completed source comparison

TARGET: Describe exactly one additional row's rank-one locus in C155a factor coordinates for every original pair and every distinct third support over every extension of F_97, including all zero-image cases.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 490 reused steps 481/485, searched projective linear-map fibers, intersecting three-space transversals and stronger three-subspace normal forms, and checked C155a/L109 plus the relevant L110–L125 scopes and ATTEMPTS/041–043,/048–049. Inspected primary projection/quotient tools support a bounded specialization; no exact arbitrary-pair factor-locus duplicate was found in the inspected local passages. Queries and limits below; no novelty inference.
SOURCE_EVIDENCE: Kostrikin–Manin, Linear Algebra and Geometry, 1997 paperback, Chapter 1 Theorem 3.12 pp. 20–21, section 6.2–6.9 pp. 44–46, Chapter 3 sections 6.2–6.4 pp. 222–226, 6.8–6.10 pp. 227–228, 8.1 p. 233 and 8.10 pp. 239–240, complete relevant statements/proofs at https://www.math.mcgill.ca/darmon/courses/19-20/algebra2/manin.pdf ; refreshed Sottile alg-geom/9510017v1 section 7.1 pp. 14–15 https://arxiv.org/pdf/alg-geom/9510017v1 ; reuse step-481/485 Bader–Cossidente–Lunardon, Stacks Tag 01WD and Conrad exterior coverage with their recorded locators.
COMPARISON: Arbitrary-field projectivization outside a linear kernel, quotient fibers, coimage/image identification and projective intersections cover the required elementary tools without a third-space disjointness hypothesis. Sottile's three non-intersecting planes do not cover this target. C155a supplies the fixed two factors; local specialization must still exhaust all third-row rank-one strata and identify their fibers, not just restate vanishing minors.
GAP: The original-map specialization and exhaustive zero/nonzero-image stratification remain unwritten. No simultaneous-row exclusion, numeric triple classification, recovery-gate removal or challenge identification follows from source coverage.
REASON: Essential comparison is complete for the unchanged field-valued target; approve one SPECIALIZE / REPRODUCTION proof attempt importing the general linear/projective tools. No local third-row theorem is derived in this literature-only turn.
LITERATURE_REASON: Step 489's additional-row target changes the ready two-space scope: intersections with the third kernel and zero images needed essential comparison. Reused prior geometry and retrieved only the missing projection/quotient tools.
SCOPE: Original L153 H/S/J and all original disjoint-support pairs through audited L155 and C155a; every distinct third support among the same 756 labels, with no disjointness from either factor assumed, over every E/F_97. Field-valued loci only; no scheme-theoretic intersection or descent assertion, all-triple census or solver.

## Proposed bounded target and test — retained preapproval scope

The main gap remains uniform twelve-row compatibility. A structural
description for one additional row could constrain factor coordinates
before any simultaneous-row solver is attempted. It would be a useful
intermediate input, not a twelve-row exclusion or feasible solving bound.

Use C155a, L155 and the actual L109 maps; L153 enters through L155.
Fix an arbitrary original disjoint-support pair a<b and a third original
support c distinct from both. Do not assume c's support or quotient
kernel is disjoint from either selected one. The object to describe is
the pairs ([x],[y]) in P(V_a)(E) times P(V_b)(E) for which Q_c on
span(x,y) has rank exactly one. A proposed structural description must
handle Q_c x=0, Q_c y=0 and both nonzero, and reject rank zero. This
paragraph defines the test, not its solution. No equation or stratum
classification is derived in this step.

First compare known common-transversal/linear-relation results with
these exact hypotheses. Reuse inspected sources when adequate; retrieve
only missing primary statements and exceptional cases. Check relevant
specific claims in L110–L125 and their recorded failures before selecting
new mathematics, without auditing or loading that whole branch. Generic
third/fourth-space counts and identifications of different labeled pair
kernels are not permitted substitutes. ATTEMPTS/048–049 stop input-rank
replays, not this distinct structural question.

Approve a bounded specialization only if it yields an exhaustive useful
description beyond restating N_c(x wedge y)=0, with every zero-image
case and E-rational factor retained. Import a matching theorem directly.
If the exact description is already local, cite it and choose its
unresolved application; if only generic results or tautological equations
are available, narrow the test or choose a different target rather than
claiming tractability. No all-triple census or solver is authorized by
this proposal. No theorem from another notebook is an input.

Nonzero lambda, full-weight and original finite-chart gates remain
separate, even after a rank-one description. Prospective coding use
retains q=97^20, k=8, the pinned cell, U_S, actual nonzero D/locators,
sixteen finite events, coding t=0, arbitrary weights/chart,
L056/L069/L040 and L051/L055 qualifications. C152a/L086/L152 and L154
are prospective uses only; L104 survivors, L151 label limits and
ATTEMPTS/041–043 remain. Representation and challenge identification
are unresolved. Mathlib coverage for the proposed target is not checked.

## Completed comparison — step 490

The SPECIALIZE decision supersedes the proposal's pending-review language.
This step approves source scope, not the mathematical conclusion. It made
no lemma, mathematical script, PROOF or DAG change. The exact TARGET is
unchanged. Outcome EXPLORATION: the new coverage enables a concrete proof
attempt, but establishes no new local result or radius bound.

### Primary input and precise applicability boundary

A. I. Kostrikin and Yu. I. Manin, *Linear Algebra and Geometry*, paperback
edition, Gordon and Breach, 1997, ISBN 90-5699-049-7, translated from the
second Russian edition by M. E. Alferieff. The
[university-hosted primary book](https://www.math.mcgill.ca/darmon/courses/19-20/algebra2/manin.pdf)
has 322 PDF pages, with printed-page numbers ten below PDF indices.
Read Chapter 1 Theorem 3.12 and proof (pp. 20–21), sections 6.2–6.9
and proofs (pp. 44–46); Chapter 3 sections 6.2–6.4 (pp. 222–226),
6.8–6.10 including Proposition 6.9's proof (pp. 227–228), 8.1
(p. 233), and all of 8.10 including its proof (pp. 239–240).
The field is arbitrary. These passages give rank-nullity, affine cosets
as quotient fibers, the coimage/image isomorphism, projective subspace
intersections, hyperplane complements, and projectivization away from
the kernel. Section 8.10 treats projection along a direct decomposition;
it is not a theorem making our restricted maps injective. Degenerate
zero maps and empty domains must use 8.1 and the linear formulation,
not assume the positive-dimensional summands of 8.10. The source does
not state our labeled third-row locus. Import these tools; justify their
local use without reproving the general results.

Apply this coverage only to finite-dimensional E-linear restrictions of
the actual Q_c to C155a's factors, retaining the actual common target
E^4. C155a supplies independent factor lines and the associated plane;
L109 supplies the exterior-map identity and the distinction between
projected rank zero and one. No new coding theorem is needed for this
structural step. The inspected geometry imposes no algebraic-closure,
characteristic-zero, genericity or support-disjointness assumption on c.
This is a comparison of hypotheses, not a derivation of the local locus.

Reused Bader–Cossidente–Lunardon section 2, Stacks Lemma 27.13.6 Tag
01WD, and Conrad's exterior-map and independence results from the ready
step-481/485 assessments. They cover the already established two-factor
geometry and alternating maps, not an extra-row exclusion. Refreshed the
complete [Sottile subsection 7.1](https://arxiv.org/pdf/alg-geom/9510017v1),
printed pp. 14–15: its three projective (n-1)-planes are non-intersecting
in P^(2n-1), and its finite fourth-plane count is generic. Neither
hypothesis can be imposed on arbitrary original c. No such count is used.

### Bounded discovery, duplicates and failed approaches

Queries used on 2026-10-25 included `projective linear map kernel fibers
projective spaces linear projection arbitrary field`, `three subspaces
common transversal intersecting subspaces projective rank one fiber
product linear maps`, `"linear projection" "P(ker" field pdf`,
`"Segre" "two linear maps" rank locus`, and `"projective" "linear maps"
"fiber product" kernel image`. Projection terminology led to the inspected
Kostrikin–Manin text. No searched exact statement supplied the complete
original-label specialization verbatim; this is not evidence of novelty.

Bourbaki *Algebra I*, Chapter II section 9.10, was a search lead only:
the web parser rejected the 22.7 MB PDF. Brenner's original three-subspace
normal-form theorem was not inspected; the located Enomoto–Watatani
Hilbert-space papers are not substituted for its arbitrary-field original.
Neither lead is essential to the approved elementary specialization.
Search snippets and inaccessible sources are not theorem inputs. PDF
screenshots for book indices 243 and 249 also failed; the complete
relevant primary text was accessible and read. No source blocker is hidden.

The local comparison read C155a's statement and ambient/rank proof,
L109's actual quotients and complete recovery-gate discussion, L111's
fixed-pair classification, L113's zero-rank/factor proof, L114's domain
and conclusion, L122's retained-plane conclusion, and L125's domain
and conclusion. Scoped searches of L110–L125 located the individual
seed/survivor scopes and L124's fixed-pair assembly. No all-branch audit
or certificate replay was needed. L111 fixes A1={1,8,47,50},
A2={12,18,64,70}; L125 fixes A2={12,18,64,75}. Those finite
classifications are not an arbitrary-pair factor-coordinate theorem.
L109 already contains the necessary rank condition; repeating it alone
would be a duplicate, not the requested structural description.

ATTEMPTS/041 records failure of uniform rank-only extrapolation;
/042 leaves residuals after a single coordinate-factor filter; /043 and
L122 preserve planes passing the selected four-row intrinsic gates.
ATTEMPTS/048–049 stop pair-rank stratification and automatic audit/encoding
repetition. These prevent claiming exclusion from a new parametrization,
but do not block the distinct third-row structural question. Preserve
all their evidence and L151's labeled-pair limitation.

### Approved proof scope and discriminating test

For the unchanged TARGET, seek an explicit description using restricted
linear kernels, images, their intersection in E^4, and projection fibers.
Required deliverables are an exhaustive treatment of each one-zero-image
case, the both-nonzero case via a shared projective image and its fibers,
and separate rejection of both-zero images. Retain empty intersections,
zero restrictions and every E-rational factor; never divide by an image
before separating its zero case. Identify fibers structurally, including
their parameters or dimensions when nonempty, rather than leave an
unanalysed bilinear equation. These are proof obligations, not results
established here. No incidence eligibility restriction on c is added.

Continue if a single source-based specialization proves exhaustion and
both directions over every E for all original labels, without extra
position assumptions. A precise failing case must be retained; if only
vanishing minors or a disjoint-third argument results, the requested
threshold is unmet and the structural claim must be narrowed or abandoned
before further work. No all-triple enumeration, solving bound or
simultaneous-row solver is authorized. Potential twelve-row use remains
prospective; the proposal's coding, weight/chart, representation and
challenge-identification qualifications remain unchanged.

Full matching Mathlib coverage is not checked; no absence claim is made.
The working record is `drafts/2026-10-25-additional-row-source-review-working.md`.
This literature step spends and resets no mathematical exploration turns;
one remains used since step 486. The next task is the exact TARGET as a
bounded REPRODUCTION proof attempt, not another source search absent a
new essential hypothesis or source defect.
