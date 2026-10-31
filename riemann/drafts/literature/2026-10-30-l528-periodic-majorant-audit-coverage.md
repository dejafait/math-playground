# L528 periodic-majorant audit nomination

TARGET: Critically audit L528's periodic-majorant bound c(h)<=mu<147/188<pi/4, checking the full-line majorization, support-period Parseval identity, exact mean and strict rational margin.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-symbol and finite-interval comparison in 2026-10-30-common-pole-test-shape-variational-coverage.md and the ready test assessment; checked L528 and the three common-pole stop records. New queries: site.math.mit.edu Fourier series Parseval identity orthonormal basis L2 notes; "common pole" "periodic majorant" Fourier. No inspected matching symbol-specific theorem; no novelty inference.
SOURCE_EVIDENCE: MIT RES.18-015, Spring 2024, Lecture 1, Theorems 1.1/1.2 and (1.2), printed pp.1--2, https://ocw.mit.edu/courses/res-18-015-topics-in-fourier-analysis-spring-2024/mitres_18_015_s24_lec01.pdf ; Teschl, GSM 99, 12 February 2009, (7.3), (7.9)--(7.10), Theorems 7.4/7.5 with relevant proof, pp.161,163--164, https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf . Standard named Tonelli theorem covers nonnegative product-measure interchange; the local application remains to audit.
COMPARISON: Known Fourier-series completeness/Parseval and real-line Plancherel cover the infinite-dimensional supporting inputs. They do not prove q<=m, evaluate this majorant mean, or establish its strict margin. L528 is the exact local proof to audit, not an independently validated source. Generic variational tools and the prior fixed-bump stops do not duplicate its uniform conclusion.
GAP: Essential source coverage for the saved critical audit is ready. Independently check L528 full-line branches, interval rescaling/coefficient normalization, Tonelli hypotheses, mean, strict comparisons and complete certificate/generator. No mathematical audit was performed this turn.
REASON: SPECIALIZE approves only reproduction/critical checking of the existing L528 argument with standard supporting theorems; it authorizes no new mechanism, changed symbol/support, trace extension or RH assertion. A citation alone does not validate the symbol-specific inequalities.
LITERATURE_REASON: The newly nominated audit had REVIEW_REQUIRED coverage for its finite-interval Parseval input; the prior ready comparison did not source-check this new proof mechanism. Reuse all unchanged symbol/route comparisons.
SCOPE: Exactly TARGET; fixed K, interval (-1,1), stated real-even smooth unit class and dm=dt/(2pi). No generalized trace, collective comparison or Xi transfer is nominated.

## Original nomination scope (retained; coverage decision completed below)

Essential input for the audit is L528 itself, including the complete
certificate at `scripts/common-pole-variational/majorant-certificate.json`
and its generator. L526/L527 are contextual contrasts, not mathematical
premises of L528. Review may reuse the original shape-source comparison
and both fixed-packet stop records; no broad source refresh is requested.

The delicate claim is exact period averaging: Fourier-series Parseval
must give sum_k |H(t+k pi)|^2=2 with the stated support/norm. Check
Tonelli, periodicity, the sign of q<=m for negative t, both branches
at a=0, the mean's factor of two and every strict bound. A failure
must identify whether the majorant, its mean, or only a loose rational
comparison needs repair. Numerical finite sections cannot replace
the uniform argument. Full Mathlib coverage remains unchecked.

The original main gap and unresolved trace, nullvector, missing-prime,
collective-sign and actual-Xi obligations remain. No new creative central
mechanism is source-ready here; this essential audit precedes routing
away from the fixed-symbol shape variation. REVIEW_REQUIRED is an
uncovered continuation, not a second completed literature step.

## Completed source comparison, 30 October 2026

This is one literature-only approval step, not the critical audit itself.
Read L528 in full to identify its required inputs, the existing ready
shape assessment and its companion comparison, and the fixed-symbol,
generic-increment and Sonin stop records. Read the certificate generator
only to identify its scope; a bounded preview of the certificate's scope
field supplied no mathematical validation. No replay was run and no
lemma or mathematical script was modified. The exact-symbol search
added no matching inspected theorem; the prior broader comparison is
reused rather than repeated. L526/L527 remain contextual only.

**Fourier series.** The primary [MIT lecture](https://ocw.mit.edu/courses/res-18-015-topics-in-fourier-analysis-spring-2024/mitres_18_015_s24_lec01.pdf),
Spring 2024, Theorem 1.2 and (1.2), p.2, states completeness and
Parseval for complex L2([0,1)) with Lebesgue measure and exponentials
exp(2 pi i k x). Read its statement/proof and the Lp approximation
case of Theorem 1.1 on pp.1--2. Endpoint matching belongs to the
continuous uniform-convergence case, not the L2 theorem. For the
saved audit, affine rescaling to (-1,1), unitary modulation and the
coefficient normalization are the necessary applicability checks.
This theorem imports the general identity; the claimed periodized
constant and subsequent averaging remain audit obligations. It does
not supply the phase-ratio bound.

**Real-line transform.** [Teschl's author-hosted GSM 99 edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
12 February 2009, defines the transform in (7.3), p.161, with factor
(2 pi)^(-n/2). Read Theorem 7.4 and its Gaussian-regularized inversion
proof, (7.9), and the extension/unity argument of Theorem 7.5,
pp.163--164. The latter applies to L2(R^n), with the integral
formula on L1 intersect L2. For n=1, zero-extended compact smooth h
is in that intersection; the audit must translate the source's
normalization to H and dt/(2 pi). No spectral claim is needed.
This standard import needs no reproof.

**Interchange and finite evidence.** The standard named Tonelli theorem
for a nonnegative measurable function on a product of sigma-finite
measure spaces is the pertinent interchange theorem: Lebesgue measure
on one period and counting measure on Z. Verifying measurability,
nonnegativity and the period partition in L528 remains part of the
application audit. No signed-integral interchange or numerical
truncation is justified by this source comparison. Elementary
Cauchy--Schwarz, Taylor remainder bounds and trigonometric identities
are standard named/elementary inputs already stated in L528; their
particular signs, endpoints and arithmetic must be checked there.
The generator records six rational comparisons, not an analytic
proof; inspect every comparison and its supporting analytic premise
in the next step. This review makes no certificate correctness claim.

The prior nomination's statement that source comparison was pending
is superseded by the completed SPECIALIZE fields above. Keep its
scope and discriminating test: either validate every uniform step and
the claimed strict gap >1/705, or identify the precise failed step.
No essential source blocker remains for that exact audit. Full matching
Mathlib coverage remains unchecked, not asserted absent. No
cross-notebook theorem input is used. A materially different central
mechanism remains unprepared; this essential audit precedes choosing
one, without reopening the fixed-shape search or resetting its stop.
