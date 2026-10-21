# Twist-five finite certificate — approved specialization

TARGET: Produce a finite independent certificate for q=L(E^5,1)/Omega(E^5) for E: y^2+y=x^3+x^2-2x by specializing the reviewed base-curve denominator theorem and rigorously enclosing the twist series and total Neron period, allowing q=0 as a stopping outcome.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed independent-twist-five source comparison; the exact fixed curve, positive twist, denominator mechanism and independent-enclosure techniques are unchanged.
SOURCE_EVIDENCE: Wuthrich arXiv:1608.06423v2 Proposition 1/Lemmas 4/6 https://arxiv.org/pdf/1608.06423v2; Cesnavicius Theorems 1.2/2.13 https://arxiv.org/pdf/1703.02951; Cremona Appendix Theorem 5.2 https://wstein.org/papers/ars-manin/html/node13.html; Cremona corrected second edition Propositions 2.11.1--2.11.2 https://johncremona.github.io/book/fulltext/chapter2.pdf and Section 3.7 https://johncremona.github.io/book/fulltext/chapter3.pdf; DLMF 19.8.1--19.8.5 https://dlmf.nist.gov/19.8.i; Pal Corollary 2.6/Theorem 3.2 https://arxiv.org/pdf/1012.0094v2; full inspected source qualifications in drafts/literature/2026-10-07-independent-twist-five-value.md.
COMPARISON: Reproduce the known analytic rational-recovery algorithm with an explicit fixed-input certificate; only the denominator/period bookkeeping and exact error/certificate implementation need specialization. No new algorithm or unproved Manin constant is proposed.
GAP: No q, root-sign calculation, specialized B or numerical enclosure has been produced. The calculation must derive and certify them before rational isolation; zero is a permitted failure of this chosen calibration twist.
REASON: Separate literature approval on 2026-10-07 repairs the missing direct source URLs and confirms unchanged fixed-input scope using the existing primary-source assessment; the next turn may perform the saved calculation. No new theorem coverage or mathematical result is claimed.
SCOPE: Only this minimal base curve and twist by 5; no BSD, finite Sha, assumed nonvanishing, L030 unknown scalar, coefficient production or rank claim.

## Separate approval and bounded mathematical test

Approved in the separate literature-only step BSD-2026-10-07-075-twist-five-source-link-recovery.
This approves source scope, not a computed certificate or a proof of BSD.
The completed source review supplies full citations and qualifications.
The exact target is unchanged; next default to implementation/calculation.

The approval reuses the primary proofs recorded in the independent-value
assessment and the Pal positive-d proof recorded in the calibration audit.
The source statements were spot-checked at their direct URLs: Wuthrich
Proposition 1 retains the strong-Weil Manin-constant assumption and the
unitary-cusp condition; Cesnavicius Theorem 2.13 retains a new optimal
quotient and the squarefree-at-each-prime conductor condition. Import the
published optimal-label verification (Cremona Appendix Theorem 5.2,
N<60000, exception 990h) and the exact model/torsion entry from
https://raw.githubusercontent.com/JohnCremona/ecdata/master/allcurves/allcurves.00000-09999
with the column and label conventions at https://johncremona.github.io/ecdata/.
Its rank column is not an input. The base arithmetic is still L030's
audited input; no theorem about the additive twist's Manin constant is
imported. The necessary denominator assembly remains mathematical work.

Cremona Chapter 2, printed pp. 37--39, Proposition 2.11.2 and the
following character-cycle identity cover both Fricke-sign branches at
an odd prime away from N. They do not certify nonvanishing in the
permitted branch. Pal v2, Corollary 2.6, printed p. 6, retains coprimality
to the minimal discriminant and d congruent to 1 modulo 4; Theorem 3.2,
printed pp. 7--8, uses the total integral of the absolute minimal
Neron differential. Keep that convention distinct from the real period
generator in Cremona Chapter 3, Section 3.7, printed pp. 97--98.
These are exactly the reviewed hypotheses, with component bookkeeping
and finite outward enclosures still to be certified in the research turn.
The Pal PDF text was accessible; one screenshot request timed out and
is not treated as evidence. Its already recorded complete positive-d
proof remains the reused coverage. Full Mathlib coverage is not checked.

ATTEMPTS/022--023 concern repeated conditional audits without input
production. This independent analytic certificate remains the approved
production test; neither historical stop is removed or reinterpreted.
No lemma, mathematical script, specialized B, q or root sign was produced
in this approval.

Use L030's audited arithmetic (minimal equation, conductor 389 and
positive discriminant), with its certificate.json, verification.json and
audit.json. Use L028 only for the already established twist/path/total-period
conventions. Its granted q is not an input. No L030 functional value or
unknown normalization scalar may enter analytic evaluation or denominator
production. Import the primary optimal-label identification for the exact
model, or independently verify that input before using the optimal theorem.
The inspected torsion entry may be imported precisely; any independent
torsion check must include its reduction hypotheses.

Write the specialization's proof, with canonical hypotheses, citations and
Mathlib qualification, in a lemma only in the later research turn.
Establish the rational-denominator bound B from the unitary-cusp theorem
and known twist identity, retaining the real component and period factors.
Do not assume a guessed B, Manin constant for the additive twist, or
rationality from a decimal.

Determine the Fricke-sign case exactly from the reviewed semistable
formula; the zero-sign branch stops this nonzero calibration choice.
For the other branch enclose the known twist series with the complete
tail and finite-arithmetic error. Compute the total minimal period through
the reviewed positive-root AGM formula and Pal comparison. Prove the
finite AGM brackets and certify every elementary-function/root interval;
library working precision alone is not an enclosure. Finite bisection,
Taylor bounds or outward interval arithmetic are implementation details
to justify in the later proof, not asserted results of this review.

Aim at a ratio interval of width strictly below 1/B^2, then explicitly
certify it contains exactly one rational of reduced denominator at most B;
the width test alone does not establish existence. Refine at most three
working precisions in this single bounded attempt, recording achieved and
required bounds. If no isolation is certified, save the full evidence and
the specific failure; if the isolated rational is zero, stop this fixed
nonzero-value route. If nonzero, q can later feed L028, whose ordinary-prime
condition still requires p>=5 and p!=5. Its calibration and L027/L026
applications are separate subsequent work.

All scripts and complete certificates belong under a new notebook-local
scripts/twist-five/ directory in the research turn; print only values,
actual/required bounds, failures and paths. No such files exist from this
literature turn. Unresolved scale, C, b, other L026 premises, finite
quotient F, divisible Sha, rational membership and complex-order comparison
remain. There is no BSD candidate.
