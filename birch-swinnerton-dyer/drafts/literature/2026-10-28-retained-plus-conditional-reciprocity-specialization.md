# Conditional reciprocity specialization

TARGET: Specialize the assessed reciprocity theorem for L123's descended outer-plus coefficient under a nonzero rational Kummer localization, checking Q-descent, one global integral rescaling and every away-p local condition.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step 540's exact-target duality/local-condition search and duplicate/failure comparison in drafts/literature/2026-10-28-retained-plus-global-reciprocity-local-condition.md; no separate discovery or novelty claim.
SOURCE_EVIDENCE: Rubin, Euler systems (1999 AWS manuscript), I.7.3 and local/limit prerequisites, https://swc-math.github.io/aws/1999/99RubinES.pdf ; Rubin, Euler systems and modular elliptic curves, Section 5 and Proposition 5.1, https://swc-math.github.io/aws/1999/99RubinDur.pdf ; Darmon--Fornea, Mock plectic points, Definition 3.7 and following away-p paragraph, https://www.cambridge.org/core/journals/journal-of-the-institute-of-mathematics-of-jussieu/article/mock-plectic-points/1FB89BA4F920603AEE9D624B3897E876 ; Fornea, Plectic Heegner classes, v2, Definition 4.23 and Corollary 4.24, https://arxiv.org/html/2603.28327v2 ; inspected ranges and qualifications are in drafts/source-notes/2026-10-28-retained-plus-reciprocity-coverage.md.
COMPARISON: The required mechanism is a standard duality application; its remaining work concerns the actual descended rational coefficient and the precise conditional input, with no reproof of the cited duality theorem.
GAP: Verify the coefficient's Q-descent and localization compatibility, rational-to-integral transfer and all local hypotheses; a nonzero rational Kummer localization remains assumed, not constructed or inferred from analytic order two.
REASON: Prepare a bounded mathematical specialization after the separate approval of this newly written continuation; no lemma or mathematical script was written in the source-review turn.
SCOPE: L123's original A/K/p and complete coefficient construction only; conditional finite local membership, with rational Kummer membership of the coefficient, nonvanishing, strictness and all BSD comparisons excluded from the conclusion.

Retain L123 (5), its audited step-515 coefficient/descent conventions,
and the source note's list of required transfers. Use the actual global
symmetrized coefficient before localization, not R as a substitute for
a global class and not a raw measure value. The hypothesis is a rational
Kummer class with nonzero p-localization; explicitly match its span to
the finite local line at split-multiplicative p. Do not invoke L005's
good-reduction specialization unchanged.

The required threshold is a fully justified **conditional** finite-at-p
statement, with each away-p place and the real place accounted for.
Its plausible use is isolating the remaining point/rationality and
nonvanishing obstructions before any strict-Kummer rank argument.
Continue only if Q-descent, a single global integral lift and the cited
duality local conditions match. On a failed transfer, preserve the
failure and withhold the application. No hypothesis is supplied by
analytic order two, and finite membership alone cannot close BSD.

This is reproduction/specialization, not a creative mechanism. A
global integral lift after rationalization is not a bound for L123's
raw-measure projection. ATTEMPTS/058 and 061--063 remain preserved.
Mathlib: not checked. This new continuation receives the supervisor's
separate approval next turn; it was not executed in step 540.

Step 541 source-gate recovery (2026-10-28): direct primary URLs are now
present in this assessment, rather than only in its linked source note.
All four URLs resolved in the web reader. Rechecked the Rubin I.7.3
statement and Section 7 setup against the saved primary extract, the
elliptic Section 5 Kummer/self-orthogonality passage, the published
Definition 3.7 and following paragraph, and Fornea's Definition 4.23,
Corollary 4.24 and displayed descent formula (68). This preserves the
existing SPECIALIZE decision and exact target; it supplies no new
mathematical conclusion or actual-class application. Prior complete
proof coverage is reused, not claimed to have been repeated here.
