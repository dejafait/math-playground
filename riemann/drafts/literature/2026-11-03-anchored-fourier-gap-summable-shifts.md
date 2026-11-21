# Source review: summable shifts in the anchored gap construction

TARGET: Assess whether L693's fixed-anchor Fourier gap can be realized with absolutely summable displacements sum_m |e_m|<infinity, retaining unit masses and |e_m|<=1/8.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 110 searched anchored/summable lattice prescriptions, stronger sequence spaces and obstructions; reused the bounded-shift assessment and local failures. No inspected theorem states the exact anchored l1 conclusion. Failed searches do not establish novelty or impossibility; primary reading and queries are recorded below.
SOURCE_EVIDENCE: Lev, RMI 38 (2022), Thm 4.8 p.1988 and Lemmas 4.2--4.7 pp.1983--1987; arXiv:2007.09930v3 Sections 2, 4.2--4.11, including complete relevant proof cases. In particular Lemma 4.3, published (4.6), and Section 4.7 supply localized nonlinear coefficient bounds. KL16 Thm 2.1 remains an unanchored l2 comparison. Kargaev, Math. USSR-Sb. 45 (1983), Thm 1 pp.405--406 and Section 4.2 p.409 provide stronger unanchored decay context, not the cancelling prescription.
COMPARISON: Lev's stated output is bounded, not l1, but his individual coefficient estimates offer a concrete regularity test for the same iteration. Kargaev's weighted zero-prescription and two-endpoint indicator construction do not state L693's fixed-anchor compensation. Smallness in a stronger norm is not supplied by L693's narrow cutoff.
GAP: Prove or refute coefficient-l1 persistence and passage to the limit for Lev's small-sup Picard iteration on L693's smooth prescribed data, without requiring its Wiener norm to be small; then check the existing translation and anchor specialization. This identified difference is unproved.
REASON: Essential source coverage now supports one bounded norm-persistence attempt rather than another search or a reproof of bounded-shift existence. No l1 construction, quantitative tail, finite transfer or new mathematical result is established in this literature-only step.
LITERATURE_REASON: Added l1 regularity lies outside the ready bounded-shift assessment and requires essential source coverage before a mathematical attempt.

The main gap remains actual-Xi mixed positivity. The prospective
intermediate target concerns the same measure

    mu=delta_0+sum_(m in Z) delta_(m+1/2+e_m),

with a nonempty distributional gap in (0,2*pi), real |e_m|<=1/8,
unit weights and the fixed anchor, now also sum_m |e_m|<infinity.
No prescribed gap width, reflection symmetry or effective l1 norm is
required. The canonical bounded-shift construction is L693. Do not
silently replace l1 by l2, c0, weighted masses or an unanchored lattice.

The proposed downstream use is a separate analysis of finite truncation
errors with the actual unit weights and endpoints retained. Summability
alone is not presented as a finite logarithmic bound; L666's rational W,
complex angular behavior, all M spatial moments, L657's zero/pole charges,
H/support and Xi realization remain open. This proposal is not a restart
of step 105's inconclusive finite numerical minimization.

The review requested by step 109 was literature-only. Its source test was:
search the exact regularity statement,
stronger sequence-space prescriptions and known obstructions, reusing
the existing comparison. Retrieve primary hypotheses and the essential
sequence-space proof cases before approving an application. An l1
version must accommodate L693's fixed a=1/8, b=3/8, epsilon=1/8 and
the cutoff chosen after the theorem's threshold; record any changed norm
or threshold dependence explicitly. Do not infer l1 from smooth source
data without a theorem or a separately approved derivation.

Continue if a precise import covers the strengthened statement or leaves
one source-assessed applicability difference. Otherwise preserve the
specific mismatch or obstruction and choose an independent target; do
not repeat the bounded-shift audit or treat inaccessible leads as results.
No theorem is being imported for this new regularity claim yet.
Mathlib coverage for the strengthened claim is unchecked.

## Completed review — 3 November 2026, step 110

### Load-bearing primary evidence

Nir Lev, *An example concerning Fourier analytic criteria for translational
tiling*, Rev. Mat. Iberoam. **38** (2022), 1975--1991,
DOI [10.4171/RMI/1318](https://doi.org/10.4171/RMI/1318),
[published text](https://ems.press/content/serial-article-files/39104),
[arXiv:2007.09930v3](https://arxiv.org/html/2007.09930v3#S4).
Reused the exact Theorem 4.8 hypotheses in L693 and the prior assessment;
read Sections 4.2--4.11 completely for the sequence-space comparison.
Section 2 defines coefficient-sup and Wiener norms. The actual fixed-point
spaces in Section 4.5 use coefficient-sup norms. No l1 output is stated.

The relevant additional source estimate is Lemma 4.3 (published p.1984,
equation (4.6); arXiv equation (4.10)). For a fixed cutoff Phi, a smooth
varphi with varphi'(0)=0, u,v in [-1,1], and the function

    psi_(u,v)(t)=[varphi(v*t)-varphi(u*t)]*Phi(t)/t,

its kth coefficient is bounded by

    max(|u|,|v|)*C*|v-u|/(1+|k|^m).

Read its integration-by-parts/integration-in-parameter proof and Lemma
4.2. Section 4.7 applies it with m=2 to each translated nonlinear
difference term; Sections 4.8--4.9 construct the coefficient-sup fixed
point. Section 4.10 then multiplies the prescribed correction by the
fixed smooth factor Psi=-1/(2*pi*i*t) on its support before applying
Theorem 4.1. Its derivative/Poisson argument preserves unit masses.
These are cited source estimates, not a newly proved l1 theorem.

### Stronger comparisons and reading limits

Kolountzakis--Lev, *On non-periodic tilings of the real line by a function*,
IMRN **2016**(15), 4588--4601, DOI
[10.1093/imrn/rnv283](https://doi.org/10.1093/imrn/rnv283),
[author manuscript](https://eigen-space.org/ps/nonperiodic-tilings.pdf),
Theorem 2.1 and Sections 2--3, manuscript pp.3--6: reused and checked
the theorem, continuous-function contraction and final differentiation
cases. It explicitly gives square-summable real shifts for a zero
prescription without the fixed extra atom. It cannot supply this target.

P. P. Kargaev, *The Fourier transform of the characteristic function of
a set, vanishing on an interval*, Math. USSR-Sb. **45** (1983), 397--410,
DOI [10.1070/SM1983v045n03ABEH001014](https://doi.org/10.1070/SM1983v045n03ABEH001014),
[primary article and English text](https://www.mathnet.ru/eng/sm2215):
inspected the introduction, Section 2's weighted-space definitions,
Theorem 1 and its following finite-measure signed-interval example
(k(n)=1+n^2), the scope of Theorem 2, and Section 4.2's unit-load remark
(pp.397, 400--401, 405--407, 409). This corrects a possible overstatement
of the comparison: original zero-prescription work has stronger decay
context than KL16's stated l2 version. The positive indicator construction
uses two moving endpoints; the one-endpoint signed construction and
unit-load remark prescribe zero, not the smooth correction cancelling
the fixed anchor. Neither is a matching anchored import. No independent
reproof or complete audit of Kargaev's weighted implicit-function argument
is claimed. OCR drops displayed conditions (19) and parts of Theorem 2;
attempted page images redirected to the site home. No omitted formula
is used as a premise. Lev's accessible coefficient estimates suffice
for the proposed test, so this comparison limitation is not an essential
source blocker.

Kargaev's 1987 sparse-spectrum Wiener correction paper was located;
only its abstract was inspected. It is an unread theorem-level lead,
not a prescription theorem input. No matching Mathlib coverage was checked.

### Exact applicability difference and bounded continuation

L693's cutoff may be made narrower after fixing a=1/8, b=3/8,
epsilon=1/8. Its proof controls the coefficient supremum. It supplies
no small Wiener-norm estimate. Smooth prescribed data alone cannot be
cited as l1 regularity of the nonlinear solution.

The independently testable difference is to examine persistence of
absolute coefficient summability along the existing small-sup iteration,
using the source's termwise estimates, and justify the limit. It is
permitted to reduce the fixed sup threshold and then select h; it is
not permitted to infer a stronger-norm smallness condition from shrinking
h. No summation estimate, iterative bound or l1 limiting argument is
derived here. If this persistence test succeeds, the derivative and
half-translation steps must still be applied with L693's anchor and
unit masses retained. No prescribed gap width or effective l1 norm is
required. A local proof of this difference would be development of the
known method, with no certified originality claim.

Continue only if the iteration closes at finite l1 norm with fixed
cutoffs and constants independent of h, or if another precisely justified
applicability argument supplies the same conclusion. Stop this mechanism
if it requires unproved smallness of the Wiener norm, changes masses or
anchor, or cannot justify l1 persistence and the limit. Such failure
would not refute existence of some other summable construction. Finite
unsmoothed tails, rational W, complex frequencies, complete logarithmic
charges, H/support and actual-Xi realization remain separate open gaps.

The exact proposed mathematical test and its scope are saved in
`drafts/literature/2026-11-03-anchored-summable-shifts-picard-scope.md`.
It needs separate continuation approval before invocation. Nothing in
this review changes L693 or the assembled argument.

### Search, duplicate and failure record

Executed queries included `Lev "2007.09930" "summable"`;
`Kolountzakis Lev Kargaev construction l1 perturbation integers spectral
gap prescribed Fourier transform`; `"Kargaev" "summable"`;
`"spectral gap" "summable" "integers"`; `"Kargaev" "prescribed"
"summable"`; `"Fourier" "gap" "summable perturbations"`;
`"Kargaev" "Wiener"`; `"Kargaev" "absolutely summable"`;
and the original characteristic-function article title/author query.
Many hits concerned unrelated operator gaps; none is theorem evidence.
No adequate matching anchored l1 theorem or obstruction was found in
the inspected material; this is not evidence of novelty or impossibility.

Searched only the anchored assessments/current anchored history and the
recorded signed-canonical failure, reusing step 106's broader local
duplicate checks. The bounded L693 audit is complete; step 105's finite
minimization remains inconclusive and is not reopened. No cross-notebook
input, lemma write, mathematical script or calculation occurred.
