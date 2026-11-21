# Source comparison: a fixed atom and a perturbed half-lattice Fourier gap

TARGET: Assess whether primary Fourier-gap theorems cover the unit-weight measure delta_0+sum_(m in Z) delta_(m+1/2+e_m), |e_m|<=1/8, on a nonempty open interval I inside (0,2*pi), as an independently testable obstruction model for L666's signed correction.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 106 searched fixed extra points, unit counting masses, bounded lattice perturbations and Kargaev/Lev spectral prescriptions; inspected the primary Lev prescription theorem and the older Kolountzakis--Lev construction. Notebook-local searches found no earlier assessment of this exact anchored model; the nonuniform-kernel assessment and L665 stops were reused. No novelty inference is made.
SOURCE_EVIDENCE: Nir Lev, Rev. Mat. Iberoam. 38 (2022), 1975--1991, DOI 10.4171/RMI/1318, Theorem 4.8 and complete proof p.1988; Section 4.2--4.9, including Lemmas 4.2--4.7 and Theorem 4.1, pp.1983--1988. Signs and conjugation checked against arXiv:2007.09930v3 HTML, Section 4.10, equations (4.24)--(4.26). Kolountzakis--Lev, IMRN 2016(15), 4588--4601, author manuscript Theorem 2.1 and Sections 2--3, PDF pp.3--6, give the weaker unanchored comparison. Precise hypotheses and reading limits below.
COMPARISON: Lev permits arbitrary sufficiently small Hermitian spectral corrections away from zero while preserving unit masses and arbitrarily small real shifts. Smallness is sup_k |S-hat(k)|, not pointwise amplitude. The theorem does not explicitly include an extra spatial atom; translation by 1/2 and a localized compensating prescription remain an applicability calculation. The older zero-prescription construction alone does not cancel that atom.
GAP: Verify the half-lattice translation phase and an anchor-cancelling smooth prescription meeting Lev's fixed a,b,epsilon threshold on some nonempty interval; do not assume a prescribed width or effective threshold. The anchored existence statement is not proved in this literature-only turn. Finite truncation, actual rational W factors, all spatial moments and complete L657 charges remain entirely outside this source coverage.
REASON: Essential primary coverage is now available for a bounded theorem-specialization test, rather than another finite descent or access attempt. Import Lev's theorem instead of reproving its contraction argument; derive only the explicit anchor/translation applicability difference on a later research turn. No new gap or transfer lemma is established here.
LITERATURE_REASON: The saved REVIEW_REQUIRED target lacked essential primary Fourier-gap coverage for a fixed extra atom and unit masses; the older ready basis/interpolation assessment did not address this spectral prescription.
SCOPE: Fourier transforms are tempered distributions with exp(-i*omega*y); retain the fixed atom and all unit weights. No symmetry, decay, periodicity or regularity of e_m is given. A gap means distributional vanishing on an open I inside (0,2*pi), not on an interval containing zero.
COVERED_TARGET: Specialize Lev's Theorem 4.8 to test existence of real shifts |e_m|<=1/8 for which delta_0+sum_(m in Z) delta_(m+1/2+e_m) has a distributional Fourier gap on some nonempty open I inside (0,2*pi), checking the translation phase, spectral smallness and unit masses without finite A_n transfer.

## Purpose and source test

The main gap remains actual-Xi positivity. The immediate finite target is A_n(e)>=A_n(0)-n/100-C*log n on L666's cube. The completed calculation in `drafts/2026-11-03-signed-canonical-kernel-working-105.md` does not justify a theorem or repeated finite minimization.

Search primary statements for Fourier gaps of positive discrete counting measures, bounded lattice perturbations and forced finite defects. Retrieve exact hypotheses and essential construction/obstruction cases first. Check especially changed masses, signed measures, omission of the anchor, larger shifts, decay/density requirements and frequency conventions. Those changes are not automatically applicable. Label restricted comparisons and unread leads; snippets are not theorem inputs.

This measure is a proposed model, not a claimed limit of G. An applicable gap construction could motivate finite signed cancellation; an obstruction could motivate anchor protection. Either still needs finite endpoints, actual W factors and complex angular dependence, all M moments, torus zeros and L657's complete charge. No such implication is derived or approved here.

Continue for a precisely applicable statement or one concrete reviewable mathematical difference. Otherwise record the mismatch without claiming impossibility or novelty. Persistent source blockage parks this dependent lead instead of repeating retrieval turns.

Essential local context is L666's family/path, L657's K/Q and integrability, L690's audited baseline, L691's two-half result and L692's sparse limitation; none establishes this infinite model. Mathlib matching coverage is unchecked. No lemma or mathematical script was modified in this literature-only step.

## Completed comparison — 3 November 2026, step 106

### Primary prescription and exact hypotheses

Nir Lev, *An example concerning Fourier analytic criteria for translational
tiling*, Rev. Mat. Iberoam. **38** (2022), no.6, 1975--1991,
[published primary text](https://ems.press/content/serial-article-files/39104),
DOI 10.4171/RMI/1318, Theorem 4.8, p.1988:
for fixed 0<a<b<1/2 and epsilon>0 there is delta>0 such that every
distribution S with

    S(-t)=conjugate(S(t)),
    supp S contained in (-b,-a) union (a,b),
    sup_(k in Z) |S-hat(k)|<=delta

admits a real sequence lambda_m with |lambda_m-m|<=epsilon and

    Fourier(sum_m delta_(lambda_m))=delta_0+S on (-b,b).

The convention is exp(-2*pi*i*t*x). The sum has unit masses.
The source's smallness condition is on integer Fourier coefficients of S.
Read the entire theorem proof, including the multiplier
Psi=-1/(2*pi*i*t) on supp S and the identity
F'=delta_Z-delta_Lambda. Also read the supporting contraction and
distributional convergence cases, pp.1983--1988.
This is an imported theorem statement, not an anchored construction.

The PDF text extraction drops minus signs and conjugation bars in places.
Checked them against the author's
[arXiv:2007.09930v3 HTML, Section 4.10](https://arxiv.org/html/2007.09930v3#S4.SS10),
equations (4.24)--(4.26); the published counterparts are (4.15)--(4.16).
The [online-first publisher version](https://ems.press/content/serial-article-files/39103)
has the same theorem on PDF p.14. The sign in the derivative step is -S;
the concluding counting-measure correction is +S. These conventions are
load-bearing for the proposed specialization. No independent audit of
all background distribution theory is claimed.

### Weaker comparison and excluded substitutions

M. N. Kolountzakis and N. Lev, *On non-periodic tilings of the real line
by a function*, IMRN **2016**(15), 4588--4601,
[DOI 10.1093/imrn/rnv283](https://doi.org/10.1093/imrn/rnv283),
[nine-page author manuscript](https://eigen-space.org/ps/nonperiodic-tilings.pdf),
Theorem 2.1, PDF p.3, proof pp.3--5, and Section 3, p.6, were inspected.
For any 0<a<1/2 and epsilon>0 the construction gives nonzero real shifts
of size <epsilon tending to zero (indeed square summable), and its
unit counting measure has Fourier transform delta_0 on (-a,a).
The proof uses a contraction, distributional differentiation and Poisson
summation. This is a gap for a perturbed lattice without an extra atom.
It supplies neither a prescribed cancelling spectral correction nor
an obstruction for the anchored measure. A mere translation of that
conclusion does not address the additional atom.

Kargaev's original 1983 finite-measure indicator-set theorem was located
through the sources' references but not read independently; it is an
unread historical lead, not an additional imported premise. General gap
characterizations allowing arbitrary complex weights do not preserve the
specified counting measure. Poltoratski, *Spectral gaps for sets and
measures*, Acta Math. **208** (2012), 151--209, was opened only for its
initial finite-complex-measure scope. Further targeted retrieval timed
out, so no detailed theorem from it is used. This does not block the
accessible, more directly relevant Lev theorem. No density-only gap
claim is substituted for fixed weights.

### Bounded specialization remaining, not performed here

The precise outstanding applicability test is whether a smooth Hermitian
correction supported in fixed bands away from zero can compensate the
fixed atom after translating the theorem's lattice by 1/2, while meeting
its Fourier-coefficient threshold with epsilon=1/8. Allow the eventual
nonempty gap interval to be narrow: the saved target specifies no minimum
width. Keep a,b fixed before choosing a localized prescription, so that
its threshold is not silently varied with the gap width. Verify the
phase in the source's t convention, then convert to omega=2*pi*t.
Do not replace the threshold by a bound on pointwise amplitude.
This paragraph identifies a source-covered calculation; it does not
execute it or assert that its conclusion has been proved.

Continue if the explicit prescription meets all hypotheses and gives the
exact fixed-atom/unit-mass statement. Abandon that proposed application
if it needs altered masses, a moving anchor, shifts beyond 1/8, or an
unsupported smallness norm. Either outcome concerns this infinite model
only. There is no prescribed uniform interval, effective width, finite
truncation rate, analytic continuation to complex frequency, rational-W
approximation, all-moment estimate, torus-zero payment or A_n bound here.
The finite target A_n(e)>=A_n(0)-n/100-C*log n and the independent
H/support/actual-Xi realization gaps remain open. Any such changed
transfer target needs a separate assessment.

### Search and local-reuse record

Representative executed searches: `Kargaev spectral gap perturbations
integers counting measure prescribed points Fourier gap`; `Fourier
spectral gap positive measure unit masses extra point perturbation
lattice Kargaev Lev`; `Fourier gap extra point lattice`; `Kargaev
spectral gap Kolountzakis Lev perturbations integers Fourier`; and
`An example concerning Fourier analytic criteria arxiv`. Some combined
queries returned irrelevant group/operator spectral-gap results; none
was treated as Fourier-gap evidence. Primary texts were retrieved after
discovery, rather than relying on snippets.

The notebook-local search used the specific Fourier-gap/Kargaev/unit-weight/
fixed-atom terminology in drafts/literature, foundations, ATTEMPTS and
the current day's history. L666's exact family and L665's recorded
one-node/absolute-cost stops were read; L657 and L690--L692 were located
only for the unchanged contextual charge and sparse/two-half limitations.
The ready nonuniform-kernel assessment was reused, not refreshed.
No cross-notebook input was read. A local PDF download failed DNS;
the browser primary texts and accessible arXiv HTML supplied the needed
hypotheses and proof cases. No persistent essential source blocker remains.

Mathlib: full spectral-prescription theorem and the proposed anchored
specialization were not checked. Unknown availability is not absence.
No mathematical originality is asserted. The scope newly recorded above
is a proposed ready continuation, subject to separate next-turn approval.
