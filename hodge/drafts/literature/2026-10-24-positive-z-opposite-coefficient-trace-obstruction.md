# Positive-z opposite-coefficient trace obstruction — proposed coverage

TARGET: Test whether L159's two-trace obstruction forces m_{-1}m_1=0 for 0<=z<=119 while retaining the ordinary twisted top sheaf W.
CHECKED: 2026-10-24
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: Proposed after step 524's completed L159 audit; no discovery or theorem-level comparison for the changed positive-z scope has been performed.
SOURCE_EVIDENCE: Existing operator coverage is in 2026-10-24-dual-coefficient-quaternionic-trace-sign.md and 2026-10-24-dual-coefficient-trace-sign-critical-audit.md; existing actual degree-one comparisons are recorded in L157 and L158. Their adequacy after dropping z=0 remains to be reviewed.
COMPARISON: L159's separately audited exclusion retains z=0 and L158's four concentrated edges; it does not establish the proposed arbitrary-z multiplicity restriction.
GAP: Check exact source and local scope for the positive forward coefficient, both degree-one restriction comparisons and their strictness when the negative coefficient has nonzero ordinary top sheaf W; determine whether the existing harmonic/cup tools suffice without whole-base concentration.
REASON: Dropping z=0 changes an essential hypothesis, so a separate literature-only coverage decision is required before any mathematical extension; the completed audit remains accepted in its original scope.
LITERATURE_REASON: The changed hypothesis permits the twisted point sheaf W and does not supply L158's concentrated positive forward coefficient; reuse ready operator sources while reviewing this specific new edge/trace scope.

This is a proposed target, not an approval or a mathematical deduction.
The next invocation must perform the missing coverage comparison before
any proof attempt. Preserve the target text while assessing it. A ready
decision may reuse the existing primary assessments; no fresh browsing
quota is imposed. Inspect an additional source only for a named essential
uncertainty. If adequate coverage is unavailable, record that limitation
without setting an unknown actual cup entry or discarding the z=0 audit.

The main gap remains universal primitive rational Hodge realization.
The intermediate target is the stated conditional line-multiplicity
restriction. Its plausible downstream use is to narrow the actual line
spectrum of M outside the two extremal z=0 branches, which the additive
tests and L158's weaker multiplicative relaxation leave compatible.
It need not settle F existence, other stable summands, a lower split
count or transport. Those independent gaps remain open.

Retain identical marked K3 factors and common g,h; the hypothetical
locally free Omega-polystable rank-two F with integral c_1=0 and
ch(F)=2-14e_1-21e_2-tau_D+62P; preferred dual HE lines of class
k=(-4,-2,1,2), k.h=0, k^2=-14 eta and integral eta of degree one.
Now allow 0<=z<=119, including positive z; keep L147's actual M and
W, L153's polystability and L156's endpoint vanishings. The meaning
of m_t is L157's full line multiplicity. L071's actual connection,
L157's signed powers/degree-one comparison, audited L158's cups and
audited L159's operator/sign argument are the exact proposed inputs;
L093 supplies the retained untwisted concentration. No cross-notebook
input is proposed. No full matching Mathlib result is asserted.

The continuation test is source adequacy for the actual coefficient
comparisons with W retained. Approve a separate bounded proof attempt
only if those comparisons and the harmonic hypotheses are covered;
otherwise identify the precise missing coverage. Do not assume the
positive forward complex is M^vee[-1] at positive z, infer a
multiplicative derived splitting, or import a zero-z trace sign solely
from perfection. ATTEMPTS/069,/089,/090 and the completed z=0 argument
remain preserved.
