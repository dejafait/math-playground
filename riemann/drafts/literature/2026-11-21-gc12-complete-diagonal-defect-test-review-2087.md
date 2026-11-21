# Complete GC12 diagonal transform: bounded defect test2087

TARGET: Test a nonnegative-defect Landau argument for GC12 by deriving the complete diagonal Mellin representation and determining whether C034s's selected conjugate pair forces a positive real-boundary obstruction without a rightmost-zero assumption.
CHECKED: 2026-11-21
DECISION: EXPLORE
SEARCH_EVIDENCE: Comparison2087 searched diagonal square-cutoff Dirichlet series, one-sided Landau/Mellin oscillation, and convolution singularities; reused exact-object/failure comparisons2080/2082/2084. Queries and read record: drafts/literature/2026-11-21-gc12-diagonal-source-notes-2087.md. No adequate matching theorem identified; no novelty claim.
SOURCE_EVIDENCE: Direct primary URLs: Kaczorowski--Pintz1986 p173 named Landau/Pólya statements https://personal.math.ubc.ca/~gerg/teaching/592-Fall2018/papers/1986.Kaczorowski_1.pdf ; DLMF2.5(i), equations2.5.1-2.5.7 https://dlmf.nist.gov/2.5.i ; both rechecked2026-11-21 in recovery2088. Other inspected comparisons and access limits: drafts/literature/2026-11-21-gc12-diagonal-source-notes-2087.md. C034s(1)-(18) is audited local input.
COMPARISON: Standard Mellin/Fubini methods cover initial-domain manipulations only after absolute bounds are checked. Inspected oscillation/additive-series theorems do not supply the complete GC12 transform or remove complementary terms. Hadamard singularity inclusion does not prove noncancellation. No citation closes the proposed test.
GAP: Establish an exact complete-transform representation and a genuine one-sided obstruction at its justified real boundary, or identify the precise unpaid complementary-term/continuation premise. A selected bidisk residue is not a positive singularity of the full transform.
REASON: One bounded global one-variable test differs from repeating automatic local pole removal. Separate source-gate approval2088 adds direct primary URLs and rechecks their scope; no identity or mathematical conclusion on this target was derived during2087 or2088.
SCOPE: Exact q=2, fixed bump, arithmetic weight, coprime mask, inclusive square cutoffs and actual ratio kernel of C034s. Selected actual zero has m>=1 and 0<delta<1/2. No rightmost zero, simplicity, uniform separation, RH, positivity of M_K or negligible complement is available.

## Proposed test, not a result

Keep the exact proposed object
\[
 \mathcal F(z)=\int_2^\infty M_{\lfloor X\rfloor}X^{-z-1}\,dX.
\]
First establish its defining absolute domain from the actual sum and
derive an exact representation there, with the lower endpoint and both
square boundaries accounted for. This is preparation, not the desired
obstruction. No representation is asserted in this assessment.

Test whether the complete representation forces a positive real-axis
obstruction incompatible with a one-sided subpower upper. A proof by
contradiction may temporarily assume that upper and study the resulting
nonnegative deficit. Distinguish that assumption from an established
estimate; prove every assertion about the deficit's integral, convergence
boundary and continuation. Do not infer absolute convergence of M's
transform from a one-sided bound.

Use the named Landau statement inspected in source-notes2087 only with
all its boundary/regularity hypotheses. Elementary inequalities for
actual nonnegative integrals and standard named holomorphy/Fubini inputs
are covered. No generalized Tauberian theorem, theorem with hypotheses
removed, or uniform zero-residue expansion is preapproved. Missing
essential source coverage stops dependent work.

## Pass and stop evidence

Continue only after a justified obstruction for the full transform/deficit,
with a real boundary reached from the defining domain and every competing
contribution paid. A local principal part continued behind an unknown
convergence boundary is insufficient. Pole order and sign must be proved
for the full object, not copied from C034s's local polynomial.

If this single attempt leaves an uncontrolled nonlocal term, inaccessible
boundary, possible accumulation/cancellation, or needs a rightmost zero,
save that exact term or premise and park the upper contradiction. Do not
repeat the local calculation or expand to a zero/frequency sweep. An
initial-domain identity alone is preparatory. A new demonstrated
obstruction may be NEGATIVE; restating the open gap is EXPLORATION/STALLED.

Essential inputs: C034s and C034r's verified kernel only. C034r's full-energy
detector explains downstream use, not GC12. L030-L032/C032a give relevance.
GC13/GC18, high primitive control, scale errors, full energy and mixed
transfer stay open. C034q/stops2076/2077/2079/2084 are contrasts; no
cross-notebook input. Full Mathlib coverage is unchecked.

Recommend proof_attempt/creative, deep_research/max, after separate
approval. The obstruction is survival and sign at the complete diagonal
convergence boundary despite signed nonlocal contributions. The bounded
test can reject this implication without settling RH or independent gaps.

## Separate source-gate approval2088

Recovery reason: the ready assessment lacked a direct source URL in its
source-evidence field. The existing notes2087 already supplied the links;
this repair does not reopen their screened detours or change TARGET.

On 2026-11-21, reopened the [Kaczorowski--Pintz primary scan](https://personal.math.ubc.ca/~gerg/teaching/592-Fall2018/papers/1986.Kaczorowski_1.pdf),
p173, named Landau/Pólya statements. Landau requires a real function,
holomorphy in the stated half-plane, failure on every larger half-plane,
and regularity at its real boundary point. It concludes repeated sign
changes. Pólya additionally requires meromorphic continuation farther
left. These statements do not identify GC12's boundary. The original
Landau article remains unread; no original proof import is claimed.

Reopened [DLMF §2.5(i)](https://dlmf.nist.gov/2.5.i),
equations2.5.1-2.5.7 and intervening hypotheses. The convolution
representation requires a common analytic strip; the residue expansion
requires meromorphic continuation and a permissible contour translation,
and retains an integral remainder. These are supporting formulas, not
a theorem paying GC12's complementary terms.

No new search was needed: reuse the exact-object searches, inspected
comparisons and failures recorded in notes2087. EXPLORE is approved for
one attempt at the unchanged TARGET, subject to all the proposed test's
pass/stop conditions above. This is source-gate repair, not mathematical
evidence or a novelty assessment. Full Mathlib coverage remains unchecked.
