# Actual Rice phase derivative: uncovered continuation nomination

TARGET: Assess whether C048j's relative error bound can transfer C048m's phase bound to the actual Rice integrand F_d^I (replace S by I in F_d^S), proving Im((F_d^I)'/F_d^I)>=1/(60log|p|) eventually for d^(1/3)<=|s|<=d^(2/3), Im s>=|s|/2, p=s+1/2 and Re p>=-|p|/(8log|p|).
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1670 completed the bounded exact-target/Cauchy/asymptotic-differentiation searches and scoped C048/Mellin/Rice duplicate/failure comparison. Queries, actually read passages and exclusions are recorded in 2026-11-19-actual-rice-phase-transfer-source-notes-1670.md; no novelty claim.
SOURCE_EVIDENCE: Nagel, Math722(Spring2012), Corollaries3.11--3.12, printed pp10--11, https://people.math.wisc.edu/~nagel/Math722Spring2012.pdf ; Krantz, Complex Variables: A Physical Approach, Section4.1.2(4.2), pp94--95, https://jontalle.web.engr.illinois.edu/Public/BOOKS/Kranz-ComplexVariables.pdf ; DLMF1.9.30--31 https://dlmf.nist.gov/1.9#E31 and2.1(ii) https://dlmf.nist.gov/2.1#ii . Relevant preprint differentiation case: Kawano202611.0383v1, AppendixC.1 first paragraph, https://www.preprints.org/manuscript/202611.0383/v1 ; exact hypothesis mismatch in notes1670.
COMPARISON: The named Cauchy estimate covers a holomorphic function on a neighborhood of a closed disk with a bound on its entire circle. C048j supplies a wider-sector value estimate; C048m supplies only the S-phase margin. The exact neighborhood and quantitative transfer remain ordinary specialization. Neither the source differentiation case nor fixed-sector Ritt directly settles this target.
GAP: Prove uniform admissible neighborhoods within the C048j value-bound region; control the entire circle, quotient/nonzero factors and derivative error; retain the exact shift and compare with the required phase margin. No such specialization or actual-I nonvanishing was derived in this literature turn.
REASON: Missing essential source coverage is now filled; SPECIALIZE permits one bounded REPRODUCTION attempt after separate approval. Import Cauchy rather than reprove it. Existing Rice comparisons and absolute-opening/crossing stops are reused; no further broad search or new sign mechanism is licensed.

LITERATURE_REASON: The target was REVIEW_REQUIRED at turn start and explicitly excluded from assessment1662; inspect the previously unread actual-I differentiation case and closed-disk Cauchy hypotheses before any mathematics.
SCOPE: Exact TARGET only, with C048a/j/m normalization and principal branches. Provisional REPRODUCTION specialization; excludes contour deformation, signed integration, endpoint control and any Xi/height implication. Newly completed review1670 is submitted for separate next-turn approval.

## Completed comparison1670 — 19 November2026

[Source notes1670](2026-11-19-actual-rice-phase-transfer-source-notes-1670.md)
retain the primary hypotheses, relevant proof cases, source-scope
mismatch, scoped duplicate/failure searches and the unproved obligations.
No essential source blocker remains for the bounded test. The proposed
inner-sector clearance has not been verified by this source review.
No lemma or mathematical script was written or changed. Mathlib full
matching coverage remains unchecked. Source coverage is local progress;
no result beyond the inspected sources or actual-I phase bound is claimed.

The mathematical continuation and its exact threshold are unchanged.
Require separate approval of this changed SPECIALIZE assessment before
invoking the transfer attempt. A successful attempt would be an input
to possible nonstationary cancellation; signed endpoint/global control
and the actual-Xi bridge would still be missing. A failed uniform
neighborhood or error comparison parks this prerequisite with evidence.

## Original nomination contract (superseded for coverage by review1670)

The main gap remains L030-L032/C032a actual-Xi all-degree algebraic-square
positivity, with C028b's sublinear height criterion and a sufficient
signed Mellin bridge unpaid. C828b's audited stop rules out the specified
holomorphic crossing; C048m's existing stop excludes stationary points
of S in its region. Neither stop establishes cancellation for the
actual finite Rice integrand. They are retained, not reopened.

The proposed intermediate threshold is the TARGET above, with
\(F_d^I(s)=\sqrt\pi\,4^{-s}I(s+1/2)B_d(s)/(Z\Gamma(s+1/2))\)
and the exact definitions and branches of C048j/m. This is a definition
of the proposed observable, not an assertion that its logarithmic
derivative is defined or has the proposed sign. The lower bound is a
candidate input to a later nonstationary contour-cancellation argument.
Even if obtained, arc geometry, endpoint terms, signed total control
and the sufficient Xi/height implication remain independent gaps.

The literature step should reuse assessment1662/source-notes1663 for
the S derivative, narrowly compare assessment1656 and stop1657 for the
absolute-opening failure, and check exact primary Cauchy estimates and
the applicable source's differentiated-error claims. It should decide
whether analytic neighborhood control licenses this transfer. Do not
differentiate a value asymptotic, quote a generic Rice theorem for a
different observable, or infer a contour sign from a phase derivative.
An adequate existing theorem should be imported or specialized.

Continue only if source coverage supports a bounded proof of the stated
threshold for the actual I in this inner sector. If a duplicate already
settles it, record and use that result; if the necessary neighborhood
or nonvanishing control fails, record the precise obstruction and park
this prerequisite. No numerical degree enlargement repairs such a
failure. No mathematical exploration budget is spent by this nomination.
No cross-notebook input is proposed; full matching Mathlib coverage is
unchecked. This routine transfer is not labeled a creative mechanism.
A concrete, source-covered new signed-Xi mechanism remains the blocker
to protected creative routing.
