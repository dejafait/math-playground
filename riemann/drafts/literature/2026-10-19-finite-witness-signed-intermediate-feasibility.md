# Source coverage: signed intermediate calibration for the fixed witness

TARGET: Test whether a redesign of L431's intermediate component can match L436's fixed P-weighted cubic limit while preserving every L431 constraint and avoiding {Delta>0,Bcal<0}.
CHECKED: 2026-10-19
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 244 searched moment-cone/Richter finite-support existence, signed cubic conditional zeta laws and measurable quadratic-cone covariance; inspected di Dio--Schmudgen 1809.00584v1 and Carlen--Lieb 0904.0734v2. Scoped comparisons with L417/L419/L421/L429/L431/L436 and their failure/coverage records found no matching full signed-intermediate repair; no novelty or absence theorem follows.
SOURCE_EVIDENCE: di Dio--Schmudgen 1809.00584v1, Definition 5 and Example 10 pp. 5--6, Lemma 11/Proposition 12 pp. 6--7 and Theorem 19/proof pp. 9--10; Carlen--Lieb 0904.0734v2, Horn theorem after (1.1), proof through (1.2), pp. 1--2. Reuse ready 2026-10-18-prime-cubic-intermediate-recalibration.md and 2026-10-18-growing-prime-poisson-law-feasibility.md for unchanged kernel/correction tools and audited L436 for P,I,beta I.
COMPARISON: Richter assumes positive-measure feasibility and signed atomic representation does not give nonnegative probabilities or a height-preserving kernel. Real Schur--Horn covers the covariance realization only after its matrix margins hold. L431's positive direction and bounded nonnegative circle multiplier do not cover a negative-cubic direction. No inspected theorem decides the changed exact-response feasibility question.
GAP: Prove or obstruct a uniformly effective measurable negative-cubic direction, bounded calibration of the unweighted, log-2 cosine and fixed-P cubic tests, and every induced mass, full mean/covariance, support, envelope and capped-cubic obligation. All of these remain unproved for the redesigned law.
REASON: Essential comparison is complete for one bounded EXPLORE attempt on the unchanged TARGET. Import the known tools rather than reprove general moment or matrix theorems; the unsupported direction and simultaneous preservation are the mathematical test, not approved conclusions.
LITERATURE_REASON: The changed mechanism permits a negative cubic component, which is outside L431's positive direction and nonnegative calibration scope; ready correction tools should be reused after checking the changed hypotheses.
SCOPE: Redesign the intermediate component only, with L421's high component and L429/L431's corrected bulk as interfaces; fixed L436 P and I, exact complete response and curvature, uniform dt/H, all original tolerances and fixed-prime limits, one eventual real-H family and every fixed cap parameter. No negative probability, actual conditional law, growing-character limit or global realization.

## Retained startup proposal

The proposal below is preserved as the record at invocation start. The
completed step-244 comparison following it supersedes its pending-gate
language only. No direction, calibration, redesigned law or impossibility
has been established in this literature turn.

The main target gap remains global mixed positivity. The proposed
intermediate question tests whether the fixed finite witness forces the
desired joint-sign orientation in the existing relaxation, rather than
only rejecting its positive-calibration subclass. It could delimit what
this new arithmetic input accomplishes before attempting actual clipping.
Even a feasible law would have no asserted actual critical-function or
cross-H realization and would not evaluate the actual statistic.

Keep the exact prescribed physical forms D(X;t)=Delta and
B(X;t)=Bcal, including curvature and the complete response. Retain
L431's uniform dt/H height marginal and every original tolerance,
all fixed-prime second correlations, full covariance/first-mean
corrections, and vanishing capped absolute cubic for every fixed cap
parameter with one all-real-H family. In addition require

    E_nu[D B P(t log 2,t log 3,t log 5)]
       = beta I (log H)^2+o((log H)^2),

where P and I are exactly audited L436, fixed before H. Preserve
L431's unweighted and cos(t log 2)-weighted cubics. The question asks
for this one extra fixed observable; it assumes no actual sine limit,
growing-character uniformity or conditional actual law. No specific
intermediate sign, direction, probability or calibration is asserted
to work. A negative-probability component is never permitted.

Essential inputs to assess: L436 for the new finite observable,
L431/L429 for the existing complete law, and L421/L419 for its exact
direction and correction interfaces. Use the already ready primary
coverage for those tools when unchanged. Check L417's sign-only
restriction and the L435/L436 positive-measure obstruction as contrasts,
not universal no-law theorems. Do not repeat the unavailable actual
clipped-moment theorem search or infer novelty from local absence.

Continuation/abandonment test: approve one bounded mathematical attempt
only after assessing the changed direction and correction scope.
Continue the proposed repair only if nonnegative conditional masses,
the desired cubic coefficients and every original tolerance can hold
with fixed constants on one eventual real-height ray. A uniform
direction obstruction or unavoidable leading error abandons this repair
alone; it does not decide the actual clipped mean. Partial progress may
leave the calibration or full-law correction unresolved, with no claim
of feasibility. No new lemma or mathematical script has been written.

Full matching Mathlib coverage is unchecked. Actual/global realization,
actual clipping, capped nondegeneracy, L413's full-error regulator margin
and global mixed positivity remain unresolved. This proposal is not a
ready gate and requires a separate literature approval turn.

## Completed comparison — 2026-10-19, step 244

This step is LITERATURE / NOVELTY_UNCHECKED / literature_comparison,
outcome EXPLORATION. It completes source coverage for the exact saved
target; it supplies no mathematical advance, new lemma, script or
feasibility certificate. PROOF.md and DAG.md do not change. Mathematical
exploration usage stays 0 of 3; this review neither spends nor resets it.

### Primary statements and their limits

Philipp J. di Dio and Konrad Schmudgen, *The multidimensional truncated
Moment Problem: The Moment Cone*, [arXiv:1809.00584v1](https://arxiv.org/pdf/1809.00584v1),
dated September 5, 2018, Definition 5 pp. 5--6, Lemma 11 and Proposition
12 pp. 6--7, Theorem 19 pp. 9--10. For finitely many measurable real
functions, Theorem 19 represents an existing positive moment sequence
by at most m atoms. Read its scalar case, interior separation argument
and boundary-face induction, including Lemma 11. Proposition 12 instead
uses linearly independent functions and an invertible evaluation matrix
to represent arbitrary vectors by signed atoms. Example 10 warns that
positivity of the Riesz functional alone need not give a representing
measure. These statements provide neither the required supported positive
law nor a conditional kernel retaining dt/H; signed atom weights cannot
be used as probabilities. No compactness, closure or strong-duality
conclusion is imported for the proposed construction.

Eric A. Carlen and Elliott H. Lieb, *Short proofs of theorems of Horn
and Mirsky on diagonals and eigenvalues of matrices*,
[arXiv:0904.0734v2](https://arxiv.org/pdf/0904.0734v2), May 13, 2009,
Horn theorem after (1.1), pp. 1--2. Majorization of a real proposed
diagonal by a real eigenvalue list suffices for orthogonal realization.
Read the two-dimensional rotation and inductive deletion/embedding
through (1.2). The trace-average diagonal is the existing L419/L431
specialization. This theorem alone asserts no Borel parameter choice,
strict translated support or cubic calibration; reuse L419's explicit
Borel implementation when its hypotheses have been verified.

The original Richter 1957 and Horn 1954 articles are references identified
in these primary expositions, not independently read additional inputs.
Schmudgen's 2405.08899 and the matricial moment problem 2310.00957 were
discovery leads only; their theorems were not inspected and are not needed
to make this bounded test ready. Search snippets and unrelated zeta
results supply no theorem input. No actual clipped-moment source search
was repeated.

### Reused coverage and exact local comparison

Reuse the completed assessments
`2026-10-18-prime-cubic-intermediate-recalibration.md`,
`2026-10-18-growing-prime-poisson-law-feasibility.md` and
`2026-10-16-prescribed-response-bulk-critical-audit.md` in this directory.
Their known Fejer-kernel, fixed-product averaging, sourced moment and
finite covariance tools have unchanged hypotheses here. Their approval
does not already prove a changed intermediate component works. No need
was found to repeat Young's moments, the finite-prime Poisson theorem,
the actual cubic coefficient evaluation or L436's audited finite witness.

Read L421's exact-form and positive-direction section (2), high component
(3)--(4), intermediate component (5)--(6) and correction interface;
L431's hypotheses/conclusion and full mass, normalization, covariance,
cubic, support and cap checks (12)--(21); L429's hypotheses and all-real-H
cutoff, moving normalization and translated-support checks (10)--(15);
L419's exact forms/trace and explicit six-state Borel construction; and
L436's hypotheses/conclusion, including the fixed degree, P, I and its
physical asymptotic. This is a scope comparison, not a new audit of the
established lemmas or their certificates.

L421's n(t) has D,B>0 and DB uniformly bounded below. Its sign reversal
does not furnish the requested alternative orientation: D is quadratic
and B linear, as those exact definitions specify. L419 supplies negative
bulk support and a negative covariance trace, but does not state a unit
direction with both B bounded positively away from zero and D bounded
negatively away from zero. Establishing a uniform usable negative cubic
direction, or a suitable replacement with controlled inverse size, is
therefore part of the next attempt. It is not inferred from a covariance
average, pointwise existence, or a model response.

The two failed-lift records
`ATTEMPTS/2026-10-16-actual-response-sign-only-lift.md` and
`ATTEMPTS/2026-10-16-actual-response-capped-radial-lift.md` were read
with L417's sharp scalar tests and radial-preservation limitation.
They restrict antipodal actual jets or pointwise radial preservation.
The proposed intermediate redesign retains integrated tolerances and
may change critical directions; those old stops do not decide it.
Likewise L435/L436 exclude positive calibration of their finite moment
data, not every joint-sign-avoiding probability law. L427/L428's narrower
obstructions and L431's valid calibration remain intact. No duplicate
signed-intermediate repair was found in the named local comparisons.

### Bounded mathematical test now covered

Keep the exact TARGET. First seek an exact-response measurable unit
direction with D<0, B>0 and a negative cubic uniformly separated from
zero on an eventual height ray; the existing positive direction remains
available. This is a sought threshold, not an asserted result. If this
first obligation can be met, test bounded sign-sensitive calibration
using nonnegative conditional masses at the intermediate radius
(log H)^(3/2). Its three required leading coefficients are beta,
gamma_2 and beta I for weights 1, cos(t log 2) and the exact L436 P.
Only these three cubics are added/retained; the target does not silently
ask to match the full three-prime character family or an actual sine
limit. P's degree and its finite bound are fixed before H, even though
large; constants may depend on this fixed witness.

Do not replace signed cubic contributions by signed probabilities.
Any use of a signed density or finite linear algebra must be accompanied
by an actual positive conditional kernel and support verification. Cite
the known representation tools where applicable. A general atom-count,
selection or duality reproof is unnecessary and would not resolve the
missing uniform direction or height marginal.

Recompute p, all new intermediate masses, w, W_H, N_H, g_H, Q, J_R,
D_R, d_H, m and the entire symmetric A_H. The reference bounds in
L431 (13)--(18) are established for its old component only. Check the
new nonnegative masses, Borel dependence, positive covariance and
negative trace before invoking L419's translated bulk construction.
Retain every raw second and both tiny odd errors, the first-B mean,
first-D tolerance, W^2 x-second correlation, each separately fixed-prime
second limit, all 23 signed/zero quartic coefficients, absolute third
and fourth envelopes, exact response and fixed physical bounds. Prove
vanishing capped absolute cubic for every fixed lambda with one family
independent of lambda. All assertions must hold for every sufficiently
large real H; a phase subsequence or growing-character claim is not a
substitute. No induced correction bound is proved in this review.

Continue if these inequalities close with fixed constants and one
eventual real-H family. A rigorous partial direction/calibration result
may leave independent correction gaps open, with no full-feasibility
claim. Stop this repair if a uniform direction obstruction or unavoidable
leading error prevents it; failure of one trial direction is not such an
obstruction. Preserve the result even if an uncovered next mechanism then
needs REVIEW_REQUIRED coverage. Do not reopen the parked clipping search
merely because this test fails.

Essential continuation IDs are L436, L431, L429, L421 and L419, with
L409/L430 for the already fixed cubic constants and L417 as the restricted
contrast. Global mixed positivity is the main gap. A feasible law would
show that this added finite witness still does not force the favorable
orientation in the relaxation; an obstruction would delimit this repair.
Neither would evaluate actual clipping or resolve actual/global
realization, capped nondegeneracy or L413's full-error regulator margin.
Full matching Mathlib coverage is unchecked; no absence is claimed.

Exact external queries: `moment cone Richter theorem prescribed support
finite moments signed measures di Dio Schmudgen`; `"zeta" "negative"
"cubic" "moment" conditional law`; `measurable selection quadratic cone
prescribed covariance Schur Horn negative trace`. Local searches were
limited to the named October-16/18/19 assessments, two failed lifts and
step-243 history; no sibling notebook or cross-notebook input was used.
