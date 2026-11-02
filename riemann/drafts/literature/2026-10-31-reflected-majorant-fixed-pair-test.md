# Fixed real-zero comparison: full-tail sign test

TARGET: Test whether D_(pi/2)(pi/4)<0 for the inverse Fourier kernel of F(x)=(1-x^2)^2 exp(-2x^2), verifying positive even Schwartz input and Laguerre–Pólya membership and retaining the complete odd-harmonic tail.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed exact-comparison search in 2026-10-31-reflected-majorant-real-zero-comparison.md; no exact reflected obstruction or duplicate was located. The direct-source recovery on 2026-10-31 retains that comparison and the exact fixed-pair scope; no renewed discovery search is needed.
SOURCE_EVIDENCE: Direct primary sources reopened 2026-10-31: https://www.math.stonybrook.edu/~aknapp/download/b2-realanal-inside.pdf (2016, VIII Props. 8.1/8.2/8.10, Thms. 8.4/8.15) and https://arxiv.org/pdf/1309.0055v2 (2014, Defs. 1.1/1.2, (2.1)); exact hypotheses and inspected ranges below. Prior full reads of L233/L598 are retained; their application remains unchecked.
COMPARISON: Known theorems cover tools and the spectral sign under verified hypotheses. They do not decide this spatial reflected value. Derive only the exact normalization, inverse-kernel check and complete-tail comparison; do not reprove the imported theorems.
GAP: No inverse polynomial, reconstructed odd-harmonic formula, finite-part sign or complete-tail sign certificate has been established for this comparison. L598 is unaudited; its relevant reflection must be checked in the specialization.
REASON: This is an independently testable discriminator for the strength of the sufficient reflected condition, after the unsuccessful actual-theta grid. A countermodel would stop a generic implication, not RH or the actual-theta majorant.
SCOPE: Only the stated F and fixed h=pi/2, r=pi/4; no wider parameter search, general theorem for admissible kernels, Xi transfer or higher-degree positivity is covered.

Use the convention and complete-tail stopping test in the preceding
assessment. Essential local mathematical inputs are L233 and L598;
L019/L239 identify actual theta only for contrast and are not comparison
premises. Verify every kernel hypothesis rather than assuming it.

Import the cited Gaussian pair, Fourier differentiation/inversion,
Schwartz periodization and first Laguerre inequality. The calculation
must show all normalization constants, the integration constant when
recovering D from a periodized derivative, and absolute/uniform
convergence sufficient for each interchange. Do not periodize a nonsmooth
extension of G as if it were Schwartz. Source admissibility requires
stronger decay than Schwartz; do not invoke that theorem package.

For a sign certificate, bound the absolute complete remaining harmonic
tail by less than the magnitude of a signed finite contribution. If
no such bound is established in one bounded attempt, preserve the work
and stop this test without extending its scope. A nonnegative value at
this pair does not prove the universal implication. No scripts or
mathematical derivations were produced during either source review or this
direct-URL recovery. The assessment is ready for the unchanged calculation;
its readiness is source coverage, not verification of any comparison sign.

Mathlib: the preceding assessment identifies exact supporting
periodization declarations and pinned source. Full matching comparison
coverage and Laguerre–Pólya coverage remain unchecked.


## Direct-source gate recovery, 2026-10-31

This repairs the missing direct URL in the ready assessment. It changes no
mathematical target or decision and establishes no new mathematical result.
Reuse the preceding assessment's duplicate searches and recorded stops.

[Knapp, *Basic Real Analysis*, digital second edition (2016)](https://www.math.stonybrook.edu/~aknapp/download/b2-realanal-inside.pdf):
Chapter VIII, Proposition 8.1(f,g), p.413, requires integrable moments or
integrable derivatives as specified there. Proposition 8.2, pp.416–417,
gives the Gaussian transform; Theorem 8.4, p.418, requires both function
and transform integrable. Proposition 8.10, p.423, gives Schwartz
inversion. Theorem 8.15 and its full proof, pp.427–428, identify
periodization with the Fourier series for Schwartz functions. The proof
controls every differentiated spatial sum uniformly on bounded intervals
and identifies coefficients by integration over translated unit intervals.
Reopened the exact differentiation hypotheses, Gaussian statement,
inversion statements and full periodization proof. Its convention uses
exp(-2*pi*i*x*y); conversion remains an obligation of the calculation.
One screenshot timed out; readable PDF text supplied the needed evidence.

[Csordas, arXiv:1309.0055v2 (21 February 2014)](https://arxiv.org/pdf/1309.0055v2):
reopened p.2, Definition 1.1 and (2.1), with Definition 1.2. The
canonical-product class permits finite products; the first Laguerre
inequality holds for members of Laguerre–Pólya. Admissible kernels also
require strict decrease and super-Gaussian derivative decay. No such
admissibility follows from the proposed Schwartz condition. Import only
the class definition and inequality; check the proposed function separately.

[Official Mathlib source, pinned a151a9c425dad802e4e1578282116f26004739b8](https://github.com/leanprover-community/mathlib4/blob/a151a9c425dad802e4e1578282116f26004739b8/Mathlib/Analysis/Fourier/PoissonSummation.lean):
reopened `SchwartzMap.tsum_eq_tsum_fourier`, which takes a complex
Schwartz function on R and a real point. This is supporting periodization
coverage only; full comparison and Laguerre–Pólya coverage remain unchecked.

Continuation inputs remain L233 and L598, with L598's relevant argument
unaudited. Neither the imports nor this repair verify the inverse-kernel
hypotheses, reflection, reconstruction constant or complete harmonic tail.
Continue only with the single fixed-pair test and its existing stopping
criterion; no theta transfer or expanded search is authorized by this scope.
