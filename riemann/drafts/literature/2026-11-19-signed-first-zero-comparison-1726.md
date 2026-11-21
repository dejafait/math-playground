# Signed first-zero comparison: bounded continuation1726

TARGET: Attempt one uniform signed first-zero-pair comparison for C032n's W/f^2 on [1,2], retaining the complete divisor and E correction; save the bound and park if its enclosure contains zero.
CHECKED: 2026-11-19
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed source review1726 and nomination1725 record exact/standard-term searches, local overlap and failed mechanisms; no matching signed theorem was located in the bounded screen. No claim of originality or exhaustive coverage. See drafts/literature/2026-11-19-signed-first-zero-source-working-1726.md.
SOURCE_EVIDENCE: FLINT certified contract/example https://flintlib.org/doc/acb_dirichlet/zeta-zeros.html and fixed low-index implementation https://github.com/flintlib/flint/blob/1d432c3bba36d1a29f6453ebfaa00e43f58c278f/src/acb_dirichlet/isolate_hardy_z_zero.c ; Arias de Reyna Section2 https://ir.cwi.nl/pub/19724/19724D.pdf ; Sra v1 Theorem3.3/AppendixC https://hexagonmath.org/pdf/2611.00345v1 ; Platt--Trudgian Theorem1/Section2 https://arxiv.org/pdf/2004.09765v1 ; Bellotti--Wong v2 Theorem1.1/Section5 https://arxiv.org/pdf/2412.15470v2 ; DLMF Gaussian transform/reflection https://dlmf.nist.gov/7.7.E2 https://dlmf.nist.gov/7.2.E3 https://dlmf.nist.gov/7.4.E3 . Reuse full cases and qualifications in source-working1726 and source-notes1709/1721/1577; inaccessible historical originals are not inputs.
COMPARISON: Known results cover low-zero isolation and analytic/counting interfaces, not the requested signed comparison. Stop1711 lost sign in absolute estimates; C033f now pays nonvanishing. Retain a signed first core and measure the entire remainder relative to it, including E, instead of repeating the modulus bound.
GAP: Need a verified leading signed contribution, full-divisor relative errors uniform in width, and effective control of the E correction; the sources do not establish them. C032n(16)-(17) also need sign/normalization checking before use. This test addresses one minor, not the main Xi positivity gap.
REASON: A new low-zero coverage input makes the nominated relative test concrete and independently falsifiable. No new calculation or lemma has been approved and proved together; this newly saved ready assessment needs separate approval next turn before the mathematical attempt.
SCOPE: Exactly C032j/m/n's full positive-ordinate divisor with multiplicity and conjugation, gamma>14, |delta|<1/2, sigma in [1,2], a=1/8, b=1/4; retain V(3*10^12), the real anchor, and all fixed-v1 qualifications. Low-zero separation uses the explicitly imported external certified result recorded in source-working1726. No RH or whole-divisor reality is assumed.

## Bounded attempt and evidence required

Use the existing f=k_sigma(1/8), g=k_sigma(1/4), W=f*dot g-g*dot f.
C033f gives f>0 under its stated inputs. Check the signs and
normalization of C032n(16)-(17) before using them. Keep the unique
simple first-zero pair with its actual factor1/2 normalization; every
other divisor member, including high complex centers and all
multiplicities, stays in the remainder. The source supplies a coarse
first interval and separation, not a finite replacement divisor.

Seek one explicit uniform negative upper margin for W/f^2 over the
closed interval, including both endpoints. Any leading-core sign,
positive lower normalization, relative profile/derivative error,
sine-linearization error and E contribution must be proved or enclosed
rigorously. Individual relative smallness must not be inferred from
an absolute small phase. Do not differentiate an unproved asymptotic
or transfer real-center formulas to complex centers without justification.

C032m/n provide dominated analytic exchanges. If the exact paired
resolvent in C032y is useful, use its source-qualified transform
interface; its older displayed count constant is not a ready input
under the corrected source coverage. Any effective tail needed here
must be justified using the assessed inclusive Bellotti--Wong v2
count, retaining cutoff multiplicities. No finite-zero database is
required if the complete remainder can instead be bounded analytically.
No new source theorem, erfc asymptotic or library capability outside
this assessment is assumed; essential changed coverage means stop and
record REVIEW_REQUIRED rather than derive uncovered mathematics.

A strict complete margin permits only C032n(19)'s stated two-point
conclusion. An interval containing zero is inconclusive; record the
actual and required bound and park this attempt. No grid extension,
identity lemma, phase-only argument or renewed modulus estimate is a
substitute. A rigorous opposite-sign certificate would be informative
negative evidence for this specified target and must be retained.

## Remaining limits and routing

### Separate recovery approval, 19 November 2026 (1727)

LITERATURE_REASON: The supervisor reported missing direct source URLs
in the ready assessment. This is a citation-field repair and separate
approval of the unchanged saved target, not a renewed theorem search.
The source notes already supplied these links and relevant proof cases;
no additional mathematical coverage or result is claimed.

Reopened the official FLINT API contract and its complete checked
example, and the Bellotti--Wong v2 version record. The latter confirms
the 7 July 2025 version; theorem and proof coverage are reused from
source-notes1721, not inferred from its abstract. FLINT's page identifies
version 3.7.0-dev, generated 17 November 2026, built from 1d432c3bba.
It warns that parts of the revised documentation are LLM-generated.
Retain the fixed-commit implementation and algorithm-case inspection
recorded in source-working1726, as well as the explicit qualification
that the external computation has not been independently rerun.
This approval supplies no independent library certification.

DECISION remains EXPLORE for exactly the existing TARGET and SCOPE.
Direct primary URLs now appear in SOURCE_EVIDENCE. No formulas,
hypotheses, sign estimates or continuation targets changed. The ready
source gate is approved for the next bounded mathematical attempt;
its signed remainder and E bounds remain proof obligations. A changed
target or essential new source input would require a fresh review.

Any later Chebyshev application still needs its exact hypotheses;
arbitrary signed measures, constant-span completeness, output
positivity, moments and actual-Xi realization remain unresolved.
Full matching Mathlib coverage is unchecked/unknown. The work would
be established-route development with a potentially new local estimate,
not a creative central RH mechanism or an independently verified
external zero calculation. No new lemma, inequality or script was
produced by this assessment. Source comparison is ready; separate
approval remains the next-turn gate controlled by the supervisor.
