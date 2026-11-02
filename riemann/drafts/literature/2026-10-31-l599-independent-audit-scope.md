# Independent audit of the fixed-pair reflected countermodel

TARGET: Audit L599's inverse-transform hypotheses, odd-periodization normalization, reconstruction constant and complete-tail certificate.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-object, stronger-result and duplicate searches in 2026-10-31-reflected-majorant-real-zero-comparison.md and its fixed-pair specialization; read L599, L233, L598 and the generic-implication stop. No changed comparison or new discovery search is needed for this audit.
SOURCE_EVIDENCE: Reopened Knapp Basic Real Analysis (digital second edition, 2016), VIII Props. 8.1(f,g)/8.2/8.10 and Thms. 8.4/8.15, printed pp.413–418,423,427–428, https://www.math.stonybrook.edu/~aknapp/download/b2-realanal-inside.pdf; inspected differentiation cases and complete periodization proof. Reopened Csordas arXiv:1309.0055v2 (2014), Defs. 1.1/1.2 and (2.1), printed pp.2–3, https://arxiv.org/pdf/1309.0055v2.
COMPARISON: The source hypotheses cover the Fourier tools and class definition used in L599, conditional on its asserted polynomial-Gaussian regularity. The exact inverse polynomial, L233 factor, odd-mode conversion, integration constant and infinite-tail comparison remain local audit obligations, not imported conclusions.
GAP: Source coverage is ready for the exact saved audit; independent correctness checking of L599 and replay of its complete certificate remain unperformed. No primary input is inaccessible or essential unread lead remains in this scope.
REASON: Separate theorem-level comparison now matches every analytic interface to an available theorem or an explicitly local verification obligation. Import the tools; audit only their specialization and the retained complete-tail argument. This approval establishes no new mathematical result and preserves the prior calculation.
SCOPE: Only L599 and the required convergence/endpoint portion of L598, L233's transform identity and the already cited primary Fourier/class inputs. No expanded comparison grid or actual-theta transfer.
LITERATURE_REASON: The newly written L599 and its independent audit were outside the earlier calculation approval; this separate source review checks those interfaces rather than repeating discovery on the ready fixed-pair target.

The exact audit should check the signs and factors in converting Knapp's
Fourier convention, using L233 at frequency 2x, subtracting the shifted
periodization, and integrating from D_h(0)=0. Inspect the complete odd
tail, not a finite numerical preview. Reuse the ready primary coverage
when adequate; identify any changed hypothesis before new browsing.

Essential inputs are L233 and L598 (only convergence and endpoint use),
plus the primary sources above. L599's analytic correctness remains
unaudited. The rational certificate cannot certify those analytic steps.
The critical acceptance test is preservation of the strict negative sign
under the exact normalizations and the complete tail bound; an error
requires correcting the canonical result and its route conclusion.

The audit is routine hypothesis/algebra/replay checking once its coverage
is approved. No justified new central creative mechanism is nominated:
the comparison gives no signed actual-Xi input, and constructing such an
input remains an independent unresolved gap. The historical actual-theta
grid stop remains in force for that particular finite scan.

Mathlib: retain the existing pinned supporting periodization coverage;
full comparison and Laguerre–Pólya coverage remain unchecked.

## Completed source comparison, 2026-10-31

This is a literature approval only. The following maps L599's proof
passages to source coverage and the work still required in the audit.
No displayed identity or strict sign in L599 has been independently
verified in this turn.

[Knapp, *Basic Real Analysis*, digital second edition (2016)](https://www.math.stonybrook.edu/~aknapp/download/b2-realanal-inside.pdf):
Proposition 8.1(f) requires the relevant integrable moment; (g) permits
either an L1 derivative or a C1 function with integrable derivative and
vanishing boundary values. Proposition 8.2 supplies the Gaussian pair.
Theorem 8.4 requires function and transform in L1; Proposition 8.10
supplies Schwartz inversion. Theorem 8.15 assumes Schwartz input. Its
proof gives locally uniform spatial derivative sums and identifies Fourier
coefficients by translated-interval integration. The printed convention
is exp(-2*pi*i*u*y). The full periodization proof, including coefficient
identification on p.428, and both differentiation cases were inspected.

[Csordas, *Fourier Transforms of Positive Definite Kernels and the Riemann
xi-Function*, arXiv:1309.0055v2, 21 February 2014](https://arxiv.org/pdf/1309.0055v2):
Definition 1.1 permits finite canonical products and a nonnegative
Gaussian parameter; (2.1) gives the first Laguerre inequality for class
members. Definition 1.2 imposes strict decrease and super-Gaussian
derivative decay. The latter theorem package is outside this comparison's
assumptions. The title here is the source's exact title; the shorter title
in L599 is bibliographic shorthand, not a distinct input.

| L599 passage | Coverage and remaining audit obligation |
| --- | --- |
| Imported results and kernel verification | The cited Fourier tools are sufficient if the stated regularity holds. Check each derivative/moment hypothesis, convention conversion, inverse polynomial, positivity and entire extension locally; class membership needs a direct comparison with Definition 1.1. |
| Associated transform and regularity | L233 is the exact local identity to check under the comparison hypotheses. Audit its full-line normalization and L599's asserted regularity of A; no admissible-kernel theorem replaces these checks. |
| Reflection, periodization and integration constant | Apply the Schwartz theorem to A only after verifying its premise. Check L598's convergence/endpoint portion, differentiated sums, negative-index sign, period rescaling, odd-mode factors and recovery from D_h(0)=0. A periodized derivative alone does not fix the constant. |
| Fixed pair and complete remainder | This is elementary local algebra and an infinite-series estimate, not an unread external theorem. Check every odd index in the stated tail bound and strict rational comparisons. Inspect the complete load-bearing certificate values and script during the audit; none was replayed here. |

Reproof of the general Fourier, Laguerre or periodization theorems is
unnecessary. The exact coefficients and reconstruction are justified
specialization work because the imported statements do not state this
reflected defect. The previously recorded duplicate/failure comparison
remains applicable: L233's older mixture lacks the extra real-zero
hypothesis, and the stopped actual-theta scan does not decide this model.
No novelty conclusion follows from the retained searches.

Accept the audit only if all hypotheses/interchanges and the complete
remainder preserve L599's strict negative sign. Otherwise correct the
canonical proof and qualify or retract its route stop as required. Do not
expand h,r, kernel parameters or actual-theta claims. This discriminator
can validate a generic-implication obstruction while leaving actual-Xi
positivity, the sine-weighted inequality and all higher-degree gaps open.

Mathlib coverage is reused from the fixed-pair assessment at revision
a151a9c425dad802e4e1578282116f26004739b8:
`SchwartzMap.tsum_eq_tsum_fourier` and
`Real.fourierCoeff_tsum_comp_add` support periodization only. No new
Mathlib search or full matching theorem claim is made.
