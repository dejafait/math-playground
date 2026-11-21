# Compact-width probability contract: ready nomination1539

TARGET: Audit the applicability of Mimica Corollary 2.2 and Fritz-Perrone-Rezagholi Propositions 4.7 and 4.10 to C032j/k/m, and record weak continuity of sigma -> nu_sigma on [1,2] and Borel evaluation measurability for every Borel subset of [0,infinity).
CHECKED: 2026-11-18
DECISION: IMPORT
SEARCH_EVIDENCE: Reuse the exact probability/support scope assessed in review1538, completed in source review1539; see drafts/literature/2026-11-18-compact-width-weak-continuity-sources-1539.md. No fresh search or creative claim is needed for this applicability audit.
SOURCE_EVIDENCE: Mimica2015 Corollary 2.2/p13 and Proposition 1.8/p9, https://web.math.pmf.unizg.hr/~amimica/lt.pdf ; Fritz-Perrone-Rezagholi arXiv:1910.03752v3 Definitions 4.1/4.6 and Propositions 4.7/4.10, pp39/41-43, https://arxiv.org/pdf/1910.03752v3 ; Tropp2024 Theorem 17.22/p260 and Theorem 17.39/p268, https://tropp.caltech.edu/notes/Tro24-Probability-Theory-LN.pdf . Full read boundaries and qualifications remain in source notes1539; local C032j/k/m applicability is unproved.
COMPARISON: The required general results are known; identify their hypotheses for the existing qualified family and import by precise citation, giving only the necessary applicability argument without reproof.
GAP: Check positive-ray sequential convergence and zero normalization, uniqueness/identification of the limiting law, both width endpoints, the half-line topology including possible mass at zero, and the Polish/completely regular interface before Borel evaluation.
REASON: This independently testable measure contract now has source coverage and may enable a later signed-mixture construction. It bypasses the blocked MIT source and does not reopen finite independence or direct compact-transform growth.
SCOPE: C032j/k/m with all inherited divisor/counting, heat-positivity and fixed-v1 probability-law qualifications; widths [1,2]; every Borel set in [0,infinity). Excludes mixture construction, signed-mixture positivity, cancellation uniqueness, moments and actual-Xi transfer.

Source-URL recovery1540 repairs this assessment without changing its
target, IMPORT decision or scope. No mathematical application has been
performed. The next invocation remains the separate applicability audit.

Continue only if the cited theorems apply to every convergent width
sequence under exactly these inputs. Record any additional premise.
No density, exponential moment or convergence of evaluations at all
atoms may be assumed. A new theorem or changed scope requires
REVIEW_REQUIRED before dependent research.

Use the full citations and source qualifications in notes1539. Any
eventual canonical corollary must retain its hypotheses, applicability
argument and unknown full Mathlib coverage. The downstream signed-mixture
question needs its own assessment and is not preapproved here.

## Direct-source recovery1540 (18 November 2026)

The required direct URLs now appear in SOURCE_EVIDENCE itself. Reopened
Mimica Corollary 2.2 and its proof (printed p13), and Fritz-Perrone-Rezagholi
Propositions 4.7/4.10 with proofs (printed pp41-43). Their probability,
normalization, topology and Borel qualifications agree with notes1539.
The latter proof uses open-set lower semicontinuity and a Dynkin-system
argument; it does not assert continuity for arbitrary Borel evaluations.
No general theorem was reproved or applied to the local family.

Tropp's direct PDF timed out on two requests today. Retain the explicit
previous inspected statement/proof record in notes1539; this access
failure supplies no new theorem evidence and does not erase that coverage.
The standard Helly-Bray bridge remains part of the subsequent audit,
including possible mass at zero. No additional source retrieval is
necessary merely to repeat that existing coverage.

This is a process repair, honestly STALLED mathematically: the prior
IMPORT decision is unchanged. Stops1302/1515/1525/1527/1534/1536/1538
remain; neither their mechanisms nor signed-mixture positivity are reopened.
Full matching Mathlib coverage remains unknown.
