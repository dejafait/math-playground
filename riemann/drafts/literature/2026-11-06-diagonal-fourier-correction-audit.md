# Diagonal Fourier correction restriction: audit coverage

TARGET: Audit C868a's C1 Fourier reduction, diagonal Fejer limit and global correction-mode bound, including the H=0 rotation invariance and the absence of a sharp period conclusion.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the exact Fourier/diagonal search in 2026-11-06-one-sided-fourier-diagonal-period-test.md; the current mathematical turn checked the named one-sided attempts and histories and found no earlier completed coefficient/diagonal test. No new external search or novelty claim.
SOURCE_EVIDENCE: Grafakos, Classical Fourier Analysis 3rd ed. (2014), corrected Theorem1.2.19(2)/proof pp27-29 https://grafakos.missouri.edu/Books_Correction_Pages/CFA-Page27-29.pdf ; product Fejer Definition3.1.8/Remark3.1.9/Proposition3.1.10 pp180-181, Corollary3.2.2/proof p183, Theorem3.3.9(a)/proof pp196-197 https://www.math.stonybrook.edu/~bishop/classes/math638.F20/Grafakos_Classical_Fourier_Analysis.pdf ; Rudin, Principles of Mathematical Analysis 3rd ed. (1976), Theorem9.42/proof pp236-237 https://djvu.online/file/cNW6EtZ7m9PIB ; reuse the parent assessment's inspected proofs, with direct-source access and selected hypotheses/proof cases rechecked in this recovery turn.
COMPARISON: The prior ready coverage supplies compact C1 coefficient differentiation, periodic integration by parts and uniform product Fejer reconstruction. C868a is the target-specific calculation to audit; no imported theorem is claimed to supply its global coefficient bound or the sharp period threshold.
GAP: Independently check the profile regularity/signs, exact actual-diagonal trace, weighted finite-sum cancellation, positivity bound and global sampling step, without treating the remaining zero/resonant modes as controlled.
REASON: Literature-only recovery repairs missing direct source URLs for the unchanged audit target. Accessible original theorem texts support the previously assessed compact operations; no new essential source or changed mathematical hypothesis is identified. Coverage is ready for the separate conceptual audit, not approval of C868a itself.
SCOPE: C868a under exactly L868(1),(3)-(5), actual F, global real C1 q,r,h, h>=0 and exact modulus domination; no radial growth, summability, bandwidth, feasible approximation or graph-existence assumption.

The parent period-test assessment remains unchanged. This audit
assessment is the recovery step's STEP_REVIEW and NEXT_REVIEW. This new assessment covers only independent scrutiny of
the newly written restriction, not another full period attempt or an
unreviewed G-zero-fiber mechanism. It does not approve the mathematics
merely by recording adequate source coverage.

Essential input: L868's audited system and actual diagonal F(z,z)=0.
The bound on nonzero common angular frequencies is asserted on all
radial space by evaluating their one-variable profiles at equal radii;
the audit must check that this uses no limiting or growth premise.
Opposite-index modes and the zero mode have explicit exceptions.
The C3 regularity asserted for a coefficient profile must follow
from the C1 first-order system, not assumed second derivatives of
the original functions. The Fejer weights in the diagonal integral
are squared and select n1+n2=0. No unweighted infinite diagonal sum
or preservation of the original feasible class is allowed.

For H=0, both zero integral of a continuous nonnegative function and
uniform Fourier reconstruction are used. Check that the result is
only simultaneous angular invariance, which permits radial dependence.
It does not activate L868's radial-independent subclass theorem.
The full period inequality remains unresolved even if every step
of C868a passes. A discovered defect must be repaired or the statement
narrowed before downstream use. Mathlib matching coverage is unchecked.

An informative audit accepts the exact restriction or identifies and
repairs a real error; it must not convert the absence of a period
bound into a no-gain theorem. The mathematical attempt's conservative
EXPLORATION outcome and route stop remain independent of this approval.


## Direct-source recovery, 6 November 2026

LITERATURE_REASON: The supervisor requires direct source URLs in the ready audit assessment; the unchanged target needs no additional theorem discovery.

Opened all three URLs above successfully. Rechecked corrected Grafakos
Theorem 1.2.19(2), including the uniform-convergence proof on p29;
Proposition 3.1.10's product-kernel statement; Theorem 3.3.9(a)'s
hypotheses and the beginning of its periodic integration-by-parts proof;
and Rudin Theorem 9.42's full hypotheses and difference-quotient proof.
Reuse the parent assessment's complete inspected coverage for the other
listed definitions and proof passages; no new claim that every listed
page was reread in this recovery turn. The URLs point to the original
books (one hosted copy and one OCR transcription) and the author's
corrected pages, not to secondary summaries. Rudin's displayed OCR is
imperfect; the prior inspection is retained, and no altered theorem
statement is inferred from OCR artifacts.

For applicability, bounded continuous angular slices on the compact
torus meet the uniform-continuity hypothesis. Product Fejer reconstruction
uses normalized Haar measure after y/(2pi) rescaling. Rudin requires
existing slice integrals, an increasing integrator, and continuity of the
parameter derivative at the interior parameter uniformly in the integration
variable. Use the identity integrator; C1 on a compact radial neighborhood
times the angular torus supplies these conditions, coordinate by coordinate
and separately for real and imaginary parts. Periodic C1 angular slices
suffice for the first integration by parts used in the proposed audit;
no higher derivatives of the original functions are imported.

The source scope still stops at these operations. The profile C3 bootstrap,
squared finite Fejer weights, diagonal cancellation, global sampling and
H=0 conclusion remain the exact mathematical claims to audit. This review
neither proves nor rejects them. The recorded failure in
`ATTEMPTS/2026-11-06-fourier-diagonal-period-uncontrolled.md` preserves the
uncontrolled A+H threshold and exceptional modes. C868a is the existing
calculation, not a duplicate result to recreate. Factorization sources in
the parent assessment are not essential to this audit and were not reopened.
Mathlib full matching coverage remains unchecked. No lemma, mathematical
script, DAG edge or overview argument changed. This is a process repair,
not mathematical progress beyond the sources or new negative evidence.
