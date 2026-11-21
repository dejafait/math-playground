# Compact-width coefficient-span test: source review1532

TARGET: Assess uniform approximation of 1 by the odd coefficient functions of C032m's kernel as a test excluding mass-one signed cancellation on [1,2].
CHECKED: 2026-11-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1532 checked the exact kernel, coefficient-span/completeness terminology, signed-mixture comparisons and Gaussian width-evolution leads; local duplicate/failure screening and exact queries are in source-notes1532. No inspected theorem matches this family's completeness question; this bounded search makes no novelty claim.
SOURCE_EVIDENCE: Reuse C032j/k/m and source-notes1528. Newly inspected Bühler-Salamon2016 Theorem2.3.22/Corollary2.3.24 pp70-71 and Theorem5.4.5 pp200-203; Tao2009 Notes12 Theorem24 compact proof, Lemma29/proof, Exercise31 and Remark33; Borwein-Erdelyi Theorem2.1 p3 and relevant proof pp7-8; Nolen Math227 Section2.3 (3.17), P0-P1 pp14-15 and derivative proof pp16-17. Precise URLs and qualifications are in drafts/literature/2026-11-18-coefficient-span-source-notes-1532.md.
COMPARISON: Known separation and signed Riesz representation cover the abstract duality, conditional on real continuous coefficients; they do not settle constant membership. Stone-Weierstrass needs an algebra containing constants; Muntz needs power functions and already includes 1. Neither supplies the missing coefficient structure. Finite independence and Powers-Xu remain insufficient for this continuum signed question.
GAP: No uniform approximating sequence or mass-one annihilator is known. A specific next mechanism is the exact Gaussian-width evolution and whether it provides a usable closed linear coefficient relation; its nonlinear closure and uniformity must be tested mathematically, not assumed from the heat equation for the underlying Gaussian.
REASON: Essential duality coverage is now inspected. Replace further generic completeness searches with one bounded width-evolution test; source access to probability kernels remains parked. The narrowed next target is assessed separately in odd-kernel-width-evolution1532 for subsequent approval.
SCOPE: Real finite signed Borel eta on [1,2], with arbitrary finite total variation and mass one; C032m's fixed actual divisor and source qualifications. No finite-support restriction, distributional weights, width-zero limit, probability mixture, moment implication, positivity or Xi realization is included.

## Completed review1532

The source ledger is
[source-notes1532](2026-11-18-coefficient-span-source-notes-1532.md).
This is a literature EXPLORATION, not a new completeness theorem or a
negative answer to the approximation question. General duality is known;
the kernel-specific structure remains unpaid. No lemma or mathematical
script was written, and the main proof and DAG did not change.

The next mathematical target is
[width-evolution1532](2026-11-18-odd-kernel-width-evolution-1532.md),
subject to separate approval of that newly written assessment. It is a
test of a proposed mechanism, not an assumption that a closed recurrence
exists. Full Mathlib coverage is unchecked.

## Original nomination1531, preserved as historical rationale

The following proposed test and instructions describe the state before
review1532; references to unread sources below are superseded by the
completed fields and source ledger above.

### Exact proposed test

Write the already defined odd kernel as

    K(sigma,w)=exp(-E_sigma(w))*sinh(O_sigma(w)),
    phi_n(sigma)=[w^(2*n+1)] K(sigma,w),  n>=0.

The proposed approximation question is whether the constant function 1
belongs to the uniform closure of the real linear span of the phi_n
on the full closed interval [1,2]. This is a question to assess, not a
density claim or a theorem proved in this turn. C032m supplies the
analytic interface; the real-valued coefficient premise must be checked
against C032j/k's actual-divisor conjugation symmetry when applying a
real duality theorem.

The next turn should inspect the relevant Hahn-Banach separation and
Riesz representation statements and their essential proof cases, then
search the exact coefficient family, stronger completeness results and
known obstructions. Record which hypotheses are verified locally and
which would require a new estimate. The proposed dual criterion is
itself part of this source assessment; no general finite-independence
theorem is being silently extended to integral relations.

The discriminator for later mathematics would be a uniformly justified
sequence of finite coefficient combinations approaching 1, or a
rigorously separated constant and a corresponding finite signed
annihilator. A finite grid fit, a fixed nonzero approximation error,
pairwise distinction, or finitely many zero odd moments does not settle
the target for measures of unrestricted finite total variation. This
turn constructs neither approximants nor an annihilator. Assess whether
a concrete covered way of testing this question exists; do not turn a
restatement into an asserted advance.

### Relevance and route decision at nomination1531

The main gap is still L030-L032/C032a actual-Xi all-degree positivity.
The possible downstream use is to exclude, or precisely delimit, the
remaining compact-width full-cancellation mechanism after finite
stop1302. Even an annihilator with mass one would not establish a
nonnegative probability mixture, its exponential moments or its
identification with unsmoothed Xi. All those independent gaps and
C032j's external-source qualifications remain.

Use C032m and C032j/k as the essential local inputs. Finite stop1302 and
the comparisons in source-notes1528 are scope limits, not assumptions
of the proposed completeness claim. The old probability-kernel access
blocker is parked; this scalar test does not depend on resolving it.
Do not reopen finite mixtures by adding more widths or more finite
Taylor constraints. No cross-notebook result is proposed.

Continue to a mathematical attempt only if the source review identifies
a matching theorem or one specific, covered approximation/separation
test with its assumptions stated. Otherwise retain the missing premise
and nominate a materially different target rather than repeating the
analytic audit or inaccessible-source search. No source-covered central
sign mechanism is available yet, so this source comparison is not
designated a creative proof attempt. Full Mathlib coverage is unknown.
