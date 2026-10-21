# Conditional quadratic enclosure: critical-audit continuation

TARGET: Critically audit L027's conditional quadratic enclosure, checking the uniform tail, exact residue representatives, inverse-unit-root substitution and fixed primitive normalization against its cited inputs.
CHECKED: 2026-10-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the searches and theorem-level comparison in drafts/literature/2026-10-06-primitive-quadratic-coefficient-error-bounds.md and the approved scope in drafts/literature/2026-10-06-quadratic-finite-error-specialization.md; the audit preserves exactly their hypotheses, coordinate and conditional threshold.
SOURCE_EVIDENCE: Stein--Wuthrich, Math. Comp. 82 (2013), Section 3 pp. 1762--1765, Propositions 3.1/3.5 and Corollary 3.3 with its monic-divisor proof, https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=6; Conrad, Hensel's Lemma, Theorem 4.1 p. 6, https://kconrad.math.uconn.edu/blurbs/gradnumthy/hensel.pdf#page=6; the exact formula and relevant statements/proof cases were retrieved again during L027's approved specialization, 2026-10-06.
COMPARISON: The audit checks the same elementary bookkeeping permitted by SPECIALIZE, rather than redoing source discovery or proving modular-symbol convergence; the all-level denominator and exact normalization remain supplied inputs.
GAP: L027 is a completed conditional proof awaiting this separate critical audit; no concrete normalized symbol certificate or nonzero coefficient exists here, and independent rational-membership and complex-order gaps remain.
REASON: Separate literature approval completed on 2026-10-06: the inspected inputs cover this unchanged audit scope; mathematical verification of L027 remains the next research step.
LITERATURE_REASON: The supervisor explicitly required separate approval of the newly written audit continuation; reuse prior adequate discovery and inspect only the load-bearing cited statements and proof case.
SCOPE: Only L027 under its unchanged non-CM, p>=5 good ordinary, primitive trivial-branch, real-Neron-period and kappa(gamma)=1+p conventions, exact symbols, certified uniform C>=0, n>=2 and unit-root residual precision M>=1; no normalization-production or implementation target is covered.

The full proof is in lemmas/L027-conditional-quadratic-coefficient-enclosure.md.
Review the exact ordinary measure formula and indexing in the cited source;
check that all polynomial coefficient denominators are bounded by C at every
level before using adjacent errors for a closed-lattice limit. Check the
simple-root conditions for both polynomials and that modular-symbol arguments
use exact integer residues. Check inverse powers without an exponent-dependent
precision loss and retain every binomial(j,2) term. Compare the fixed series
with foundations/05 and L004's strict enclosure criterion.

Continue only if every obligation is justified with these hypotheses; otherwise
record and repair the precise failed implication within this scope. An enclosure
containing zero cannot supply L026's independent coefficient premise. L026's
additional arithmetic and residual-family conditions remain separate; the audit
must not remove F, divisible Sha, rational membership or complex-order gaps.
The earlier ATTEMPTS/021 stop remains evidence for its distinct inference.
This assessment proposes a next audit, not an audit already performed and not
a new literature discovery. Mathlib coverage remains not checked.

## Separate source approval, 2026-10-06

Reused both named assessments and compared L027's stated inputs with
foundations/05. Reopened the publisher offprint (2013 final version):
Section 3, pp. 1762--1763 fixes the period, cosets and coordinate;
Proposition 3.1 is coefficientwise convergence. Corollary 3.3 and the
Proposition 3.5 proof, pp. 1764--1765, supply the adjacent estimate
through polynomial divisibility. The cited divisor is monic; the audit
must check that case rather than import Lemma 3.4 as an unrestricted
integral-quotient assertion. Section 3.3, p. 1766, fixes the ordinary
unit root. The already-recorded Lemma 3.6 wording and two-level tail
qualification remain excluded from the accepted inputs.

Reopened Conrad's undated live notes, Theorem 4.1, printed p. 6:
the strict residual/derivative hypothesis includes an exact distance
conclusion, not merely root existence. Its applicability to both
polynomials and inverse-power substitution remains an audit obligation.

DECISION stays SPECIALIZE. This completes source approval, not the
critical proof audit, and repeats adequate coverage without a new
mathematical input. No source blocker or widened hypothesis was found.
No duplicate enclosure is needed; audit the canonical L027. The
ATTEMPTS/021 failure concerns a separate finite-defect inference and
does not forbid this conditional precision check. Continue with the
unchanged target and test above, retaining every supplied certification
input and independent BSD gap. No lemma or mathematical script was changed.
