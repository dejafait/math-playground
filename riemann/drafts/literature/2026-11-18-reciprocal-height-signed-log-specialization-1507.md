# Finite reciprocal-height signed-log specialization1507

TARGET: Establish the signed-log identity integral_R(log|P_d(x)|-d log|x+b_1|)dx=pi H_d for the actual reciprocal Jensen polynomial, including repeated real zeros and the first nonzero symmetric-tail term with a fixed-d remainder.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Source review1507 searched polynomial log-modulus height identities, half-plane Poisson-Jensen and Bode formulas; scoped actual-Jensen/Jacobi duplicates and failures were compared. Queries and retrieval qualifications are in 2026-11-18-reciprocal-height-logarithmic-integral-source-notes-1507.md; no novelty claim.
SOURCE_EVIDENCE: Min Ru, Nevanlinna Theory, Theorem A1.1.1 and complete proof pp.1-2, https://www.math.uh.edu/~minru/log.pdf ; Emami-Naeini/de Roover arXiv:1902.11302v1 Theorem1/(12), Corollary3/(18), complete AppendixA/(23)-(27), https://arxiv.org/html/1902.11302v1 . Direct sources rechecked in recovery review1508; detailed hypotheses and limits remain in source-notes1507.
COMPARISON: Known finite-factor and Poisson-Jensen accounting supplies the method, not this written actual-family boundary/tail specialization. The control stability and conjugate-pair hypotheses cannot be assumed after rotation; a short finite-polynomial proof is justified.
GAP: Check absolute integrability of the combined signed log, multiplicities/common real zeros, monic and next-coefficient cancellation, factor pi and first symmetric-tail coefficient/remainder. No uniform-in-d bound or o(d) estimate is covered.
REASON: This finite interface is an independently testable prerequisite for later signed bulk/tail payment, materially distinct from C028a/C028c's positive coefficient norms; it is not a proposed new general identity or a proof of RH.
SCOPE: Only C028a's actual P_d=R_d/gamma_0, b_1=gamma_1/gamma_0 and C028b's H_d, integers d>=3, real-axis Lebesgue integrals up to finite null sets, and fixed-d tails after y=x+b_1. No all-degree upper estimate, degree-limit interchange or stable actual denominator is assumed.

Recovery review1508 (2026-11-18) completes the separate source approval.
Direct primary URLs above were opened and the theorem hypotheses and
essential proof cases rechecked. The exact target and SPECIALIZE scope
are unchanged. This approves the bounded next-turn proof attempt, not
the identity itself. No mathematical proof is performed this turn.
Use the complete source/hypothesis comparison in source-notes1507.

Essential local inputs: C028a fixes the polynomial and top coefficients;
C028b fixes actual heights, multiplicities and their RH-equivalent
threshold; L025 fixes the actual S_2 normalization if used in the tail.
C028c is a contrasting audited stop, not a mathematical input to the
candidate identity. No global logarithm from L025 is available.

Prove only the stated finite specialization. Import the named standard
theorem if used; avoid a general Poisson-Jensen reproof. A direct finite
factor calculation is justified to cover boundary roots and hypotheses
not met by the control theorem. Do not split divergent one-sided
factor integrals without retaining their cancellation. Give the range
and explicit dependence on d/coefficients for every tail remainder.
Repeated real roots and the denominator zero at -b_1 are required cases.
Full matching Mathlib availability is unknown and need not block this
informal check.

Continuation test: the exact identity, its pi/sign and a quantitative
fixed-d tail expansion must all pass without RH or hyperbolicity.
Failure must isolate the invalid normalization or limiting step.
Success supplies an interface for one later signed estimate, not the
o(d) payment itself. Any new uniform-in-d mechanism requires its own
source assessment. Stop identity-only elaboration without a concrete
subsequent estimate; no audit quota is intended.

## Source approval1508

The reported process defect was missing direct source URLs in this ready
assessment, although source-notes1507 already contained them. Both URLs
were accessible on 2026-11-18. Min Ru's printed pp.1-2 include the
finite-disk hypotheses, multiplicities, boundary rescaling instruction
and zero/pole-removal proof. The Bode HTML v1 contains Theorem1/(12),
Corollary3/(18) and all AppendixA/(23)-(27), including stable and
unstable pole cases and the conjugate-factor calculation. Its normalized
factorization and nonzero boundary parameters cannot be assumed for the
rotated actual family. No displayed antiderivative is certified by this
source approval; the finite-factor specialization must check its own
integrals. No larger source sweep is needed for this unchanged target.

C028a's hypotheses/normalization and coefficient discussion, and complete
C028b, were read to confirm scope. Their norm stop and RH-equivalent
height threshold remain intact. Duplicate/failure coverage from
source-notes1507 is reused, not presented as new search evidence. The
remaining proof obligations are precisely those in GAP and the continuation
test above. Mathlib remains unchecked. This is a process repair, with no
new theorem, height estimate or novelty claim.
