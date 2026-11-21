# Relative singular-value source screen — completed1296

TARGET: Assess whether primary singular-value asymptotics for C032f's unchanged compact column Hankel operators A and B can supply a rigorous relative-spectrum obstruction to B*B>=d^2 A*A, without a differential intertwiner or boundary-trace assumption.
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed1296 checked C032e/f, ready1270/1276/1288 and stops1283/1292/1293, then searched primary singular-value comparison, continuous Hankel endpoint asymptotics, analytic/rapidly decaying kernels and theta kernels. Exact queries and inspected/unread distinctions below; no matching quantitative column-ratio theorem located, without an absence or novelty claim.
SOURCE_EVIDENCE: Ullrich2024 Section1 Bernstein-number definition/Proposition2 and Section3 proof; Pushnitski--Yafaev1412.0551v1 Theorems2.7--2.8/(2.3),(2.14)--(2.16) and Section3 proof cases; their1508.04279v2 Theorem5.1/(5.3)--(5.7), Sections6.2--6.4 and Theorem7.3; their accepted log20 manuscript Theorem3.1 and Sections3.4--3.5. Guiver2025 compactness coverage is reused from review1270 and its theorem/proof scope rechecked. Precise links and qualifications below.
COMPARISON: Standard Hilbert singular-value comparison has the required direction and allows common-input rectangular operators. Inspected nonzero Hankel leading terms instead require logarithmic endpoint tails or a real-axis local singularity; they do not supply this theta column's denominator lower bound. Upper decay bounds, even at every power, cannot settle the proposed ratio. Matrix-valued extensions do not remove that defect.
GAP: No positive denominator subsequence, quantitative asymptotic ratio, column leading constant, actual-range inclusion or delta verdict is established. Derivative-tail hypotheses of the upper-bound results have not been specialized; doing so alone would not meet the discriminator.
REASON: End the stipulated one screen and park this asymptotic test: no inspected source provides an applicable quantitative discriminator. EXPLORE is bounded source exploration, not a mathematical obstruction or an assertion that asymptotics cannot exist. Further dependent work requires a specific new two-sided column-asymptotic input.
SCOPE: One bounded literature-only screen of the unchanged A,B from C032f(1)-(3), using C032e's full Psi and fixed c; complex unweighted H and Y, one common scalar input and both output components. No new lemma, asymptotic derivation, singular-value computation or matrix truncation during the screen.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED lacked essential singular-value asymptotic coverage for this exact common-input column pair; ready Douglas/core and earlier source comparisons were reused, not reopened.

## Completed comparison1296 — 17 November 2026

The main gap, intermediate target and continuation test remain those of
the nomination below. The result of this screen is **park**, not approval
of a theta asymptotic calculation. No mathematics beyond the sources was
established. The original nomination is retained below as historical scope.

### Primary comparison principle

Mario Ullrich, *Inequalities between s-numbers*, Advances in Operator
Theory **9**, article82 (2024),
[Section1 and Proposition2, with Section3 proof](https://doi.org/10.1007/s43036-024-00386-x).
Read the real/complex Banach-space conventions, Bernstein-number
subspace formula, ideal property(S3), Hilbert equality and its proof.
These give the standard necessary comparison
`s_n(B)>=d s_n(A)` when the compact Hilbert-space maps satisfy
`||Bh||>=d||Ah||` for every common input h. It is a conditional
specialization of the cited variational characterization: the same
n-dimensional input subspaces are used, while output dimensions may
differ. No self-adjointness of A or B is needed. This checks the
nomination's direction, without asserting its premise for theta.
When s_n(A)>0 the necessary ratio bound is therefore d. Neither
positivity of infinitely many denominators nor their size is supplied
by this general theorem. No general comparison theorem is reproved.

### Continuous scalar upper estimates

A. Pushnitski and D. Yafaev, *Sharp estimates for singular values of
Hankel operators*,
[arXiv:1412.0551v1](https://arxiv.org/pdf/1412.0551), 1December2014,
printed pp5,8 and11--15, (2.3), Theorems2.7--2.8 and their Section3
proofs. For alpha>0 set M=0 if alpha<1/2, otherwise M=floor(alpha)+1.
A locally bounded complex scalar h, C^M when required, must satisfy
`|h^(m)(t)|<=A_m t^(-1-m)<log t>^(-alpha)` for all t>0 and
0<=m<=M; here `<x>=sqrt(1+x^2)`. The conclusion is
`s_n(Gamma(h))=O(n^(-alpha))`. Little-o endpoint hypotheses give
little-o singular values. Read both the low-alpha interpolation case
and the derivative/dyadic Fourier estimates, followed by the compact
cutoff approximation in the little-o proof. These are upper estimates;
no denominator lower bound follows. The theta value estimate C032e(8)
is not an imported estimate on its derivatives. No such specialization
or stacked-output extension was derived this turn.

### Nonzero asymptotic terms and their scope

Pushnitski--Yafaev, *Localization principle for compact Hankel operators*,
[arXiv:1508.04279v2](https://arxiv.org/pdf/1508.04279), 20October2015,
Theorem5.1, printed pp18--19, (5.3)--(5.7), Sections6.2--6.4 pp20--23;
Theorem7.3/proof pp25. Read the scalar complex continuous theorem,
including its M(alpha) derivative remainders: endpoint models are
`b_0/[t(log(1/t))^alpha]` at zero and finitely many
`b_l exp(-ia_l t)/[t(log t)^alpha]` at infinity with distinct real a_l.
The leading constant is `v(alpha)(sum_l |b_l|^(1/alpha))^alpha`.
Its proof combines model asymptotics and disjoint symbol singular
supports, paying the remainder in the little-o ideal. The local variant
requires a truncated-power singularity at a positive real t_0.
The actual kernels are smooth at every finite nonnegative real point
and have the C032f(7) rapid value tail. Thus these nonzero endpoint
models supply no theta leading term; even a justified zero-coefficient
application would furnish no lower bound. The real exponential tilts
are not the theorem's unitary oscillatory modulations. Polynomial
multipliers do not justify ignoring its endpoint/remainder requirements.

Pushnitski--Yafaev, *Asymptotic behavior of eigenvalues of Hankel
operators*, IMRN **2015**(22),11861--11886,
[accepted manuscript log20](https://kclpure.kcl.ac.uk/ws/files/52081451/log20.pdf),
Theorem3.1, manuscript p10, Section3.4 p14 and Section3.5 pp14--15.
The real scalar theorem assumes the same two logarithmic endpoint
models, with derivative remainders through its specified M(alpha),
and yields positive/negative eigenvalue coefficients from b_0,b_infinity.
Read the model-plus-small-remainder proof and matrix extension. That
extension requires square Hermitian matrix kernels and Hermitian
endpoint coefficients; its proof invokes the matrix Weyl theorem.
It is not a theorem stated for a rectangular column. A separately
justified dilation could address that format, but could not create
missing nonzero endpoint coefficients or a finer-than-power lower
bound. No dilation, theta asymptotic or matrix Weyl proof is imported.

Guiver, *Regularity and Compactness Properties of Integral Hankel
Operators and Their Singular Vectors*, CAOT **19**, article6 (2025),
[Theorem2.3(1) and proof](https://doi.org/10.1007/s11785-024-01627-w),
is reused from review1270: integrable compact-operator-valued kernels
give compactness. Rechecked its square value-space convention and
finite-dimensional proof referral. Its regularity/compactness assertions
are not a two-sided singular-value asymptotic. No new theorem from
this source is required or imported here.

### Bounded searches, reuse and stop

Queries actually used included `Pushnitski Yafaev asymptotic singular
values Hankel operators integral rapidly decaying kernels analytic
endpoints`, `Hankel integral operators analytic kernel singular values
Widom super exponential decay asymptotics matrix valued`, `compact
operators singular values product inequality s_n AB bounded operator
approximation numbers theorem`, `"Hankel operators" "exponential"
"asymptotics" "analytic"`, `"singular values" "Hankel" "entire"
kernel asymptotic`, and `"Hankel" "theta" "singular values" asymptotics`.
The search returned no inspected exact theta-column theorem. Widom
discrete moment-matrix results and rational-approximation leads remained
unread comparisons, not evidence about this continuous pair. The arXiv
HTML endpoints for the two older papers failed; their PDFs above were
accessible. The King's sharp-estimates endpoint returned403 and was
replaced by the versioned arXiv PDF. These are resolved retrieval
failures, not persistent source blockers or reasons for another screen.

Local duplicate checks retain review1276's finite-data warning, ready1288's
rectangular-action scope, stop1283's squared-output metric problem and
the exact divisor/trace stops1292/1293. No result from another notebook
was read. The relevant first C032f proof ranges and C032e's full-theta
value/continuation ranges were read; (21)--(25) are not assumed.

The required discriminator was a rigorous positive-denominator
subsequence with ratio tending to zero. Nothing inspected supplies it.
Finer analytic-singularity asymptotics remain an unassessed possibility,
not an approved continuation. Comparable spectra would also leave
operator order and actual range inclusion unpaid. Stop after this screen;
do not compute finite singular values or prove mere rapid decay to fill
a mathematical turn. Delta and the independent signed actual-Q bridge,
source metric, graph realization and initialization remain open.
Full matching Mathlib coverage is unchecked, not asserted absent.

The independent continuation is bounded central-gap discovery outside
the branch realization, with its own REVIEW_REQUIRED nomination1296.
The alternative cluster-rounding and count-only countermodel audits
were checked narrowly and found already completed (audits1263 and106/118);
the stale pending labels in PROOF are not grounds to repeat them.
No PROOF/DAG argument changed, and no lemma or mathematical script was
written. No exploration-budget reset or RH candidate is claimed.

## Original nomination1295 (historical scope)

The main gap remains L030-L032/C032a's actual algebraic-square
positivity in every degree. The auxiliary question is whether the
relative inequality in C032f(5) can be ruled out by a necessary spectral
comparison. A result about delta would still leave the signed actual-Q
identification, completed source metric, realization, initialization
and all-degree signs unresolved.

The proposed discriminator is a rigorous subsequence of indices with
s_n(A)>0 and s_n(B)/s_n(A) tending to zero, where s_n denotes decreasing
singular values counted with multiplicity. First verify from a precise
primary theorem the necessary singular-value comparison implied by
the operator inequality, including its direction and the common input
space; do not take this nomination as its proof. Then check whether
inspected Hankel asymptotic theorems cover the actual two-component
operators and can support that discriminator. Neither existence of the
subsequence nor any asymptotic formula is asserted here.

Inspect theorem hypotheses and the relevant proof cases before large
passages. In particular check half-line versus discrete Hankel models,
scalar versus column output, complex spaces, which endpoint or analytic
singularity controls the asymptotic, and whether polynomial multipliers
(1+t) and ((1-c)-(1+c)t) fall within the theorem with controlled errors.
Individual scalar-component asymptotics do not automatically give the
singular values of the stacked operator sharing one input. Upper bounds
on both operators alone cannot provide an upper bound on their ratio;
one must have an appropriate lower bound for the denominator as well.
Do not replace full theta by a finite mode or a positive Gram model.

Use targeted local checks before external retrieval, including the
finite-data warning in `2026-11-17-theta-joint-evaluation-review-1276.md`
and the scope contrast in ready1288. Retain stop1283's failure of separate
scalar symbol/inertia data to compare squared paired outputs, stop1289's
fixed differential exclusion, and source stops1292/1293. This nomination
does not reopen their mechanisms. Existing relevant source assessments
should be reused if the newly inspected target actually matches them.

Continue only if an inspected source supplies an applicable quantitative
framework and one specified asymptotic obligation that could discriminate
the relative inequality. Nominate that single obligation for its separate
gate before mathematics. If the sources give only compactness, qualitative
decay, unmatched models, or comparable nonzero leading ratios with no
discriminator, park this test after the one screen. Comparable singular
values would not establish the operator inequality or actual range
inclusion. Source inapplicability is not a delta decision.

There is presently no justified creative central-sign target: the exact
signed-Xi identification remains missing after the completed reflection
and theta-identity comparisons. This source screen is an auxiliary
literature_comparison, not relabeled creative to meet scheduling. Missing
essential singular-value coverage justifies the next literature turn;
the ready C032i audit was completed before this nomination. No mathematical
exploration counter reset, mathematical result, Mathlib check or RH
candidate is asserted. Full matching Mathlib coverage is unknown.
