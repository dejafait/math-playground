# Actual negative-part majorant: proposed classical specialization

TARGET: Test whether a hypothetical nonnegative harmonic majorant of L504's actual negative part outside its finite obstacle forces f=0, using restriction above the obstacle and quadrant Phragmen--Lindelof.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed exact-question comparison in 2026-10-30-actual-negative-part-harmonic-majorant.md, including its exact-statement searches, duplicate check and separation from the L506 envelope stop; no claim of originality.
SOURCE_EVIDENCE: https://www.axler.net/HFT.pdf — Axler--Bourdon--Ramey, Harmonic Function Theory, second edition corrected 17 July 2020, Theorem 7.26 pp. 158--159 and Theorem 3.4 p. 47; https://www.oden.utexas.edu/media/pending_reports/book.pdf — Demkowicz, Lecture Notes on Non-Self Adjoint Operators and Related Topics, 4 December 2024, Theorem 3.9 and proof pp. 42--43. Direct PDFs and relevant statements/proofs reopened 2026-10-30; parent comparison and its searches reused.
COMPARISON: Standard positive-harmonic representation and strict sector growth control supply the needed tools, but no inspected theorem directly states the conditional finite-obstacle conclusion for L504's smooth Fourier class. The task is their local specialization, not a reproof or a new general majorant theorem.
GAP: Verify the vertical growth and symmetry implications of a hypothetical G, then verify bounded boundary data and the strict order condition after pole-free polynomial normalization in quadrants. The proposed f=0 conclusion is unproved.
REASON: Supervisor recovery requires direct source URLs in this ready assessment. This separate literature-only approval adds and verifies those URLs, preserving the prior SPECIALIZE decision and exact target; no new mathematical coverage or result is claimed. Restriction differs from L506's prescribed-envelope exhaustion; no extension through the obstacle is assumed.
SCOPE: Fixed R>0 and T>exp(1); retain L504's entire, even, real-on-R, smooth compact Fourier representation and continuum positivity hypothesis H_a. Assume a finite-valued nonnegative harmonic G majorizing max(0,-Re f) on {y>0} minus the closed rectangle [-a,a] times [b,B], with no extra growth or boundary regularity. Constants may depend on f,G,R,T. Nonzero membership is conditional; do not prove or assume H_a nonemptiness. This assessment received separate literature-only source approval on 2026-10-30; the specialization remains unproved and is reserved for the next research invocation.

Essential input: L504's definitions only; ABR and Demkowicz as cited
in the [parent comparison](2026-10-30-actual-negative-part-harmonic-majorant.md).
L506 is scope contrast, not an input to actual-data nonexistence.
There is no L503 or cross-notebook input.

Bounded test: seek polynomial imaginary-axis control from a putative
majorant on a half-plane strictly above B, and check whether the sector
theorem then conflicts with a nonzero member of the stated Fourier
class. Treat every intermediate implication as a proof obligation.
Do not drop the positive representation's term at infinity, equate
Re f and |f| without symmetry, introduce poles inside sectors, or use
the sector theorem at its order endpoint. Stop this test if any such
extra assumption is essential. Import the classical theorems by citation;
only the local application needs proof. This is reproduction/specialization,
not a creative central RH mechanism.

A successful obstruction would decide feasibility of this linear
majorization method, not prove the desired Q estimate false, divergence
of actual finite-truncation costs, Xi transfer or RH. These require
independent arguments. Mathlib coverage of the full specialization and
the cited inputs has not been checked.

## Separate source approval, 30 October 2026

LITERATURE_REASON: Repair the supervisor-reported missing direct source URLs; reuse the completed comparison without broadening its target or repeating discovery.

The [ABR primary PDF](https://www.axler.net/HFT.pdf) was accessible.
Rechecked Theorem 7.26 and its proof, printed pp. 158--159, retaining
the nonnegative linear height term representing mass at infinity.
Rechecked Theorem 3.4 and its open-ball dilation argument, printed p. 47:
the statement assumes positivity and harmonicity on the open unit ball,
without boundary continuity. Nonnegative cases still require the
added-constant limit already recorded in the parent assessment.

The [Demkowicz primary PDF](https://www.oden.utexas.edu/media/pending_reports/book.pdf)
was accessible with the stated title-page date. Rechecked Theorem 3.9
and the full damping/maximum-principle proof, printed pp. 42--43
(physical PDF pages 50--51). It requires analyticity in the sector,
continuous boundary values (or the stated boundary limsup replacement),
bounded ray values and growth exponent strictly below the angle parameter.
The proof retains the strict positive cosine margin and lets damping
tend to zero after controlling the circular boundary.

No local growth estimate, symmetry implication, normalization or majorant
nonexistence is proved here. SPECIALIZE is reaffirmed for the unchanged
target, not extended to other targets. This URL/process repair is
STALLED mathematically; it neither spends nor resets exploration usage.
The independent quantitative costs, compactness and Xi-transfer gaps
remain. Mathlib coverage remains unchecked.
