# Residual width-range continuity discriminator1740

TARGET: Test whether C033i's residual law mu is excluded from C032q's finite signed width-mixture range by continuity at x=1 of the signed remainder after deconvolution by nu_1.
CHECKED: 2026-11-19
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1740 searched signed-mixture ranges, actual Sra widths, convolution exponentials and density regularity; no inspected exact range theorem was found. See drafts/literature/2026-11-19-residual-law-width-range-source-notes-1740.md for queries and duplicate/failure checks; no originality is inferred.
SOURCE_EVIDENCE: Reuse1736/1552: Cekanavicius--Vellaisamy2018 Section1/(23)-(24) https://www.vmsta.org/journal/VMSTA/article/114/read and Mimica2015 Propositions1.4(iv)/1.8 https://web.math.pmf.unizg.hr/~amimica/lt.pdf ; Sra2610.00584v1 Lemma2.1/PropositionB.1 https://hexagonmath.org/pdf/2610.00584v1 and Sra2611.00345v1 Proposition3.1/C.1 https://hexagonmath.org/pdf/2611.00345v1 ; Haslinger2.39 pp67-68 https://www.mat.univie.ac.at/~has/scriptneu.pdf and DLMF5.12.1 https://dlmf.nist.gov/5.12.E1 . Exact inspected hypotheses/proof cases are in notes1740; URL repair/recheck1741 is in recovery-notes1741.
COMPARISON: C032s/u supply endpoint finite differences and a two-width positive factor, not uniformly controlled continuum signed remainders. Measure exponentials supply total-variation convergence, not continuous densities; general identifiability and time-analyticity results do not fill this difference.
GAP: Establish finite signed remainder kernels uniformly on [1,2], local continuous density and sufficient series bounds near x=1, then test the exact inverse lambda from C033i using all-Borel identity and its support intervals. No invariant or nonrepresentation is established in this literature turn.
REASON: This is a concrete necessary-condition discriminator for the exact mu; it avoids unrestricted positivity pullback and tests a different interface from the parked recursion, transform-growth, reverse-order and coarse-box routes. It may fail without deciding the cone or RH.
SCOPE: Qualified actual C032j/q family, arbitrary finite real signed Borel eta on [1,2] of mass one, atoms and singular parts allowed, no common variation cap. C033i uses I=[1,3/2], mu with Levy measure L restricted off I, and its fixed lambda. Preserve all actual-divisor, multiplicity, counting, finite-zero, first-zero, heat and fixed-v1 source qualifications. No J_eta=0, density of nu_sigma, moment, positivity of a quotient, RH or Xi realization premise.

Coverage was nominated in literature review1740. Separate literature-only
recovery1741 repairs the missing direct source URLs and approves this
unchanged target's EXPLORE scope for a later mathematical attempt. See
[recovery notes1741](2026-11-19-residual-width-source-url-recovery-notes-1741.md).
This process repair neither proves a regularity invariant nor changes the
completed source review's mathematical outcome.

Use C032j/q and C033i as essential local inputs; C032s/u delimit the
existing endpoint scope. Follow the exact obligations and test in
source-notes1740. In particular, uniform total-variation control alone
does not permit a continuity conclusion. A fixed eta has finite variation,
but no uniform cap across the candidate class is allowed. Retain the atom
at zero and use finite signed uniqueness with that atom included.

Seek only enough regularity on an interval containing 1. Analyticity on
the whole half-line is unnecessary and not assumed. The elementary
source-covered route uses dominated convergence and Euler beta estimates
for the series, with the required actual bounds still to be proved.
If this route fails, record the failing estimate or representative issue;
do not silently add positivity, compact output support or density to eta.

Success is an exact range decision or an informative obstruction to this
specific discriminator. It would delimit the C033i stop within the actual
width family, leaving C032q/r cancellation, moment/tail and actual-Xi
positivity gaps independent. No full matching Mathlib theorem is claimed.
This is development using known measure/integration tools, not a claimed
new creative central RH mechanism or an application audit of C033i.
