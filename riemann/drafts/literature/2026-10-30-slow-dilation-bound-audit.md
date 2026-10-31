# Independent audit nomination: slow-dilation bound

TARGET: Critically audit L504's supplementary slow-dilation bound (19), including Fourier normalization, the K-weight conversion and uniformity over all finite polynomial degrees and envelopes.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused drafts/literature/2026-10-30-slow-dilation-weighted-gap-cost.md and the actual query/source and duplicate/failure comparisons in its parent 2026-10-30-genuine-positive-class-runge-flux-test.md; narrowly compared L504's supplementary hypotheses/proof, the earlier L504 audit record and the slow-dilation stop. No new broad search or novelty claim.
SOURCE_EVIDENCE: Chremmos--Fikioris, Superoscillations with arbitrary polynomial shape, https://arxiv.org/pdf/1504.04822v1, Section II (2)--(4), printed pp. 4--5, Fourier convention in (6), p. 5, and Section V, printed p. 8, directly rechecked 2026-10-30; standard named Fourier inversion for Schwartz functions. The source does not assert (19); the earlier L504 audit excludes it.
COMPARISON: Global smooth compact spectral data meet the source's finite-degree regularity hypotheses; its polynomial Fourier-differentiation and dilation mechanism plus named Fourier inversion suffice as inputs for auditing the written local specialization. The K-weight conversion and uniform constants require replay, not import; no H_a positivity, source norm estimate or L503 conclusion is needed.
GAP: Independently confirm or correct (19), including its exact uniform quantifiers and T>exp(1) onset; this source-only approval does not validate the inequality. General H_a costs, other dilations and Xi transfer remain outside scope.
REASON: Separate approval now completes source scope for the unchanged nominated audit; a later RESEARCH/proof_audit may replay the local argument, classified REPRODUCTION. No new result is derived here.
SCOPE: Only L504's supplementary family and (19), with Fourier inversion and the cited support mechanism; no audit of L503, source approximation theorem, H_a existence, actual-Xi theorem or creative construction.

## Original nomination scope (before the separate approval below)

The target uses only L504 definitions and its supplementary calculation,
the prior inspected primary source and Fourier inversion. There is no
cross-notebook input or new theorem request. Do not redo broad Runge
searches. Check whether the existing assessment's source coverage is
adequate for this exact audit and, if so, approve the audit for a later
research turn. At nomination this was REVIEW_REQUIRED, not SOURCE_BLOCKED;
the separate approval below supersedes that source-gate status.

The source's arXiv footer is v1, 19 April 2015; the retrieved title page
says 6 July 2021. Its angular convention must be reconciled with
exp(2pi i v z). The global smooth compact spectrum is stronger than
its degree-dependent regularity assumptions. None of its approximation
or L2 conclusions implies the new M bound by citation alone.

## Proposed audit obligations, not audit conclusions

Check the scaled spectrum D psi(Dv), the sign and factor in polynomial
Fourier differentiation, global endpoint smoothness, real-axis Schwartz
decay and Fourier inversion's |phi_f|<=N. Verify N<=A_R M using the
ambient bandwidth R, including K(0)=0 and k_R>0. Check 4rb=R a/D,
b/B=log L/L<=1, the factor of two from the two sides, and the common
T>exp(1) onset. Test p=0 and division by M for nonzero p. No constants
may depend on degree, coefficients or envelope derivatives. Review
the consequence |Q_a|/(aM)<=C_R/B only for D>=max(1,B).

An audit may confirm or correct this routine specialization. It may
not infer H_a membership, general H_a bounds, other dilation regimes,
actual-Xi signs or RH. Full Mathlib coverage is unchecked. The direct
mathematical inputs of L504 remain empty in the local DAG: the
isolated-zero argument is written out, not imported from L503.

## Separate source-scope approval, 2026-10-30

LITERATURE_REASON: The calculation nominated a new, explicitly uncovered
audit of (19); the existing audit of L504 (1)--(4) does not cover that
addition. This required separate source-scope approval, reusing the
existing construction assessment rather than repeating Runge discovery.

Read the omitted calculation assessment and its parent's actual query,
source and overlap passages; the supplementary L504 hypotheses,
conclusion and complete proof; the slow-dilation attempt/history; and
the earlier L504 audit history. These distinguish the new audit from a
duplicate of the original full-space obstruction audit. The earlier
L503 weight-conversion overlap remains acknowledged; its theorem is
neither an input nor certified here. No cross-notebook result is used.

Directly reopened the linked primary PDF. Section II, equations
(2)--(3), p. 4, assumes a real finite-degree polynomial and an envelope
in PW_pi whose spectrum is globally C^(N-1) with Nth derivative of
bounded variation. Its proof differentiates the spectrum and retains
support; the following smoothness/decay discussion and equation (4),
p. 5, address polynomial growth and dilation D>=1. Equation (6) on
p. 5 writes the forward transform with exp(-i omega t), fixing the
angular convention. Section V, p. 8, explicitly allows smooth compact
bump spectra for arbitrary finite degree. The v1 footer/title-page
date discrepancy recorded above remains visible in this artifact.
The extracted decay formula's typography is not a basis for an L1
claim; the local audit uses its stronger smooth-spectrum hypothesis
and must check Schwartz decay and Fourier inversion itself.

The nominated family assumes R>0, T>exp(1), D>=max(1,B), an even
real entire envelope with e(0)=1 and globally smooth compact spectral
data, and any finite even real polynomial, including zero/constants.
The source's N>=2 comment concerns obtaining two zeros in the desired
interval, not an additional zero requirement imported into this audit.
The smooth-data setting is within the stated spectral mechanism for
each finite degree. General R and the 2pi convention require the
normalization replay already explicitly written in L504. Uniformity
over degrees, coefficients and envelopes is a local proof obligation;
it does not follow from a uniform smoothness constant in the source.

Thus the existing primary coverage is sufficient to attempt this
independent audit. The intermediate target remains the exact TARGET
above. Its downstream use is to validate or correct only the restricted
slow-dilation construction stop, relevant to the unresolved detector
cost route; all-degree actual-Xi positivity remains the main gap.
Continue to one audit: check every proposed obligation above, including
zero/constant polynomials and positivity of M before division. A pass
retains only that stop; a failure records the precise estimate and its
effect. No claim about the general H_a ratio is approved. Increasing
polynomial degree alone is not a new continuation mechanism.

Outcome EXPLORATION records completed scope comparison and removal of
this source gate, not a new bound, a mathematical audit or an advance
beyond the inspected sources. SPECIALIZE authorizes a later audit with
REPRODUCTION classification. Full Mathlib coverage remains unchecked.
No essential source blocker or unread load-bearing theorem remains
for this exact audit; no further literature turn is needed on unchanged
hypotheses. The proposed bound itself remains unaudited.
