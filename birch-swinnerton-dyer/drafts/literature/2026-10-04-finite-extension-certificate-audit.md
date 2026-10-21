# Finite-extension certificate: bounded audit coverage

TARGET: Audit L020 by tracing restriction/corestriction for non-Galois F and the finite Kummer diagram, and test the boundary m = v_p([F:Q]) in L018's divisible-quotient model without claiming arithmetic realization.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the saved transfer/Kummer search; on 2026-10-05 searched within both primary PDFs for Proposition 1.30, Proposition 4.2, equation (29), and the p. 129 diagram, then read the located statements and proof passages. No new web discovery query was necessary for the unchanged target.
SOURCE_EVIDENCE: Milne CFT v4.03, Chapter II Example 1.29/Proposition 1.30, p. 70, and Proposition 4.2, p. 87; Milne Elliptic Curves second edition, IV.(28)--(29), pp. 112--113 and diagram p. 129; exact read locators are retained in the prior assessment.
COMPARISON: The same inspected transfer and Kummer inputs support a critical audit of the conditional application; the boundary test asks only what the annihilator argument permits in the already established abstract divisible quotient, not for an arithmetic counterexample or a new torsor realization theorem.
GAP: Check the coefficient map and non-normal subgroup application, and separate a vacuous transfer bound at d = m from actual existence of a point-realizing field.
REASON: Complete the runner-required separate approval of the newly saved continuation; the existing source coverage suffices, and the mathematical audit is deferred to the next turn.
SCOPE: Retain L018 and L020, including a common finite field, both globally Kummer restricted classes, the degree factor and the absence of any finite-Sha assumption; allow m = d only in the formal boundary test.

## Reused sources and precise comparison

The prior [transfer assessment](2026-10-04-finite-extension-kummer-transfer.md)
contains the actual extraction record and applicability comparison.
[Milne CFT II.1.30, p. 70](https://www.jmilne.org/math/CourseNotes/CFT.pdf#page=79)
and [II.4.2, p. 87](https://www.jmilne.org/math/CourseNotes/CFT.pdf#page=96)
are the supporting finite-index and continuous-cohomology inputs.
[Milne EC IV.(28)--(29), pp. 112--113](https://www.jmilne.org/math/Books/EC2.pdf#page=117)
and [the coefficient diagram, p. 129](https://www.jmilne.org/math/Books/EC2.pdf#page=134)
cover exactness and transitions. They do not state the full L020 certificate.
No essential source remains unread for this algebraic audit; period-index
bounds and any construction of a common field are outside its scope.

The future test should trace which cohomology group receives each map,
check whether normality or injectivity was accidentally assumed, and
examine multiplication by p^m on a nonzero D[p^m] quotient at d = m.
Continue only if the conditional certificate survives these checks;
otherwise record and repair the precise error. An allowed formal
boundary quotient supplies no elliptic-curve counterexample. A sound
certificate would still leave global point production and the full
BSD gap unresolved. This audit is expected to be REPRODUCTION, not
an assertion of originality.

## Mathlib

Full statement and supporting transfer/Kummer coverage: **not checked**.
The named Milne results are supporting sources, not full Mathlib matches.

## Separate continuation approval — 2026-10-05

LITERATURE_REASON: The runner requires a separate approval turn for this newly saved continuation; the concrete source check is whether II.1.30 requires normality and whether the cited cohomology and Kummer passages cover the proposed map audit.

Read the primary PDFs in the versions already identified above. Reused
prior discovery rather than broaden the target. Source locators below
use zero-based PDF pages, while links use one-based PDF page numbers.

- CFT II.1.29--1.30, printed p. 70, PDF index 78: inspected the coset construction and proof; finite index is required, normality is not. II.4.2 and its preceding continuous-cochain argument, printed p. 87, PDF index 95: inspected discrete coefficients and finite-quotient passage. These are supporting inputs for the proposed profinite application, not a theorem stating the whole certificate. The next audit must still trace that application.
- EC IV.2, printed pp. 112--113, PDF indices 116--117: inspected multiplication exactness, equations (28)--(29), the restriction diagram and the number-field scope. Printed p. 129, PDF index 133: inspected the coefficient diagram. No Sha finiteness premise occurs in these sequences. The direction of each coefficient map remains a task for the mathematical audit, rather than a new result of this review.

**Decision:** SPECIALIZE remains adequate for the exact TARGET. No
essential source is unread within this scope. Import the named inputs;
only audit the local application and formal equality boundary. Do not
claim an arithmetic realizing field from the formal model. The review
adds retrieval evidence but changes no theorem coverage or route, so
its STEP_OUTCOME is STALLED, not an advance or negative mathematical
result. Existing lemmas and scripts remain unchanged.

The main gap, downstream use and continue/repair test stated above
remain in force. The achieved unconditional bound is r <= 2; the
required lower bound r >= 2 still needs the additional witness with
m > v_p([F:Q]). This turn does not perform the equality-boundary test.
It neither claims novelty nor supplies a BSD candidate.
