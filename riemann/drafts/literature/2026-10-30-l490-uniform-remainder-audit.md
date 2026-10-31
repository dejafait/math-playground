# L490 uniform remainder: proposed critical audit

TARGET: Critically audit L490's uniform two-term remainder bound, checking the source hypotheses, moving floor, complex powers, all error terms and closed endpoints.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused exact-target searches in drafts/literature/2026-10-30-explicit-two-term-tail-remainder.md and drafts/heat/2026-10-30-explicit-positive-time-tail-source-review.md; inspected L490 and the direct-numerical-tail-extraction and tail-approval-loop-recovery failure records; reopened the versioned primary source on 2026-10-30 for the audit comparison below.
SOURCE_EVIDENCE: Directly inspected https://arxiv.org/html/1904.12438v2 (4 August 2019), definitions (1),(4)–(19), Theorem 1.3(13),(20)–(24), Section 2 complex-power convention, Proposition 6.6(ii) statement and proof, and its error-bound statements and following conversion; local application is lemmas/L490-explicit-two-term-positive-time-remainder.md.
COMPARISON: The explicit source inputs cover L490's hypotheses; its 153/10^6 bound requires the existing local elementary majorization, not direct import of an explicit tail cutoff. Coverage is ready for a separate replay of that majorization; this source comparison does not certify it.
GAP: No essential source-coverage blocker remains for this application audit. The independent replay of L490's majorants remains undone; saddle-proof audit and numerical phase/count claims remain outside scope.
REASON: A uniform residual is a concrete preparatory input for a later explicit tail count; catch source-transcription, sign, floor and endpoint errors before building that argument.
SCOPE: Audit only L490's existing application and exact rational majorants. No new phase theorem, contour count, source saddle reproof or collision-exclusion mechanism is proposed.

Essential inputs are the source theorem above; L490 uses no earlier local
lemma as a mathematical premise. L488/C489a motivate downstream use only.
The result must retain B_t nonvanishing, tL/4 (not tL/2), both time
endpoints, y endpoints, n=1, the n^(-Re(kappa)) factor and all x beyond
the edge. Test the complete analytic argument, not a height sample.

This source approval and the subsequent independent proof audit are
separate steps. The present turn performs no new calculation. Continue only if the literal imported inequalities
and every majorant give the stated result; otherwise preserve and repair
the precise failure. A successful audit still certifies neither a real/
simple numerical cutoff nor finite-collision exclusion or zero-time control.
Full matching Mathlib coverage remains unchecked. No new source search is
needed merely to repeat the existing numerical-target comparison.


## Completed source comparison, 2026-10-30

Theorem 1.3 uses the closed spatial region (5) and positive time at most
1/2. Its (14)–(19) supply the finite sums, conjugation and moving floor;
(20),(22)–(24) supply the other imported inequalities. Definitions
(6)–(11) specify the logarithms and nonvanishing factor; Section 2 fixes
complex powers. Proposition 6.6(ii), rather than Theorem 1.3(21), is
L490's precise real-part input: the displayed correction numerators
differ, respectively 8y(1-y) and 4y(1+y). Its proof treats this estimate
using the explicit rational expression for the real part of alpha.
No stronger tL/2 coefficient is imported. The conversion following
Proposition 6.6(vi) explicitly gives (24). These are inspected source
statements and proof cases, not a reproof of the saddle estimates.

No new broad search is needed: the numerical target and assumptions
remain within the previous assessment. This additional source read is
justified by the previously unapproved audit target and its exact
transcription checks. Direct-cutoff extraction remains stopped because
its constants are unspecified. The approval-loop stop concerns repeated
unchanged approval of L488, not this first coverage review of L490.

Approve exactly the saved TARGET for a mathematical turn. Retain every
existing proof obligation above, especially discontinuities of the
finite approximation at floor jumps: no holomorphic continuation of
that approximation across jumps is supplied here. Success means the
existing uniform claim survives a complete independent replay; failure
means record the exact inequality and range before any downstream use.
Neither outcome settles the main gap. Matching Mathlib coverage remains
unchecked. No lemma or mathematical script was changed in this review.
