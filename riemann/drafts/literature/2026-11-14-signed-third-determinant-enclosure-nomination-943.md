# Signed third determinant enclosure — nomination943, comparison944

TARGET: Determine the sign of D_3(p;B'(1)) by a joint rigorous enclosure of p through p^(4) from full reciprocal-Xi inversion, with every quadrature and tail error controlled.
CHECKED: 2026-11-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Comparison944 screened the named C466 inputs and stops927/932/941, reused reviews930/935/938/942, and recovered assessment883's finite-order overlap. Exact reciprocal-xi/determinant/density and theta_1/xi/derivative searches led to the primary arXiv text below. A stronger source-stated strict sign matches this case; novelty is not inferred and no independent five-derivative certificate was found locally.
SOURCE_EVIDENCE: Sra, arXiv:2611.02944v1 (2 November 2026), Appendix C.16 definition and C.18 Lemma C.26, printed pp45-49, https://arxiv.org/pdf/2611.02944v1 ; inspected its statement, three proof domains and complete residue-tail/certificate case. Reuse C466k(7), C466l(1)/(5), C466n(4)-(15) and reviews935/938 for the numerical ingredients, with qualifications detailed below.
COMPARISON: The mathematical sign is already covered by a stronger cited result. Its strict differential statement is needed; weak PF confluence alone does not suffice. The requested independent joint enclosure is not supplied by that citation or by C466n's scalar certificate. Such a calculation would be reproduction and currently has no additional necessary purpose.
GAP: Independent derivative-weighted quadrature/tail budgets and the joint determinant interval remain unwritten; this review neither derives nor approves them as a necessary reproof. The source's certificates have not been independently replayed here. Import only its stated result with explicit version, normalization, finite-zero and computational qualifications; all-degree positivity and Xi transfer remain open.
REASON: Documented overlap changes the route: park the proposed sign-only computation and prepare a narrow known-result import. SPECIALIZE records that the sources cover the sign component, not the originally requested five-derivative numerical deliverable. No full numerical target completion, new determinant result or mathematical advance is claimed.
SCOPE: Same actual p=theta_1, h, x=B'(1)=S/3 and signed D_3 as nominated. The sole scheduled continuation is the narrower citation/application in signed-third-source-import-944.md. No original-line numerical implementation is scheduled; new numerical work would require an essential purpose and exact error coverage. Keep the Hub-v1 and arXiv-v1 inputs distinct.
LITERATURE_REASON: Nomination943 changed the evaluation point and derivative orders; its essential exact-target overlap comparison was missing. Existing inversion and scalar quadrature assessments are reused rather than rechecked as new work.

## Completed comparison944 — 14 November 2026

The main gap remains L030-L032/C032a actual-Xi all-degree
algebraic-square positivity. The nominated intermediate target tests
the full signed determinant after C466o's negative patches. Its
potential use was to distinguish a local determinant obstruction
from signed cancellation. The continuation test now finds that its
sign conclusion overlaps a known source claim, so a fresh computation
solely to determine that sign is not justified. No certificate was run.

### Decisive exact-source comparison

[Sra, arXiv:2611.02944v1](https://arxiv.org/pdf/2611.02944v1),
Appendix C.18, Lemma C.26, printed pp45-49, states strict positivity
of the differential determinants through order four for every positive
argument. Appendix C.16 defines the same sign convention. The proof
identifies p=c0*Theta and splits the positive axis into overlapping
domains. The relevant residue-box case uses verified-zero extraction,
a positive residual exponential moment, (C.70), rational congruences
and outward interval pivot checks. Its certificate records report
independent replays; none was replayed here.

This is the exact differential statement, not an inference of strictness
from nonnegative translation minors. C466k already establishes a
strictly positive evaluation point, and C466a fixes the density
normalization. Checking the positive constant multiplier is the only
normalization application left for the proposed canonical import;
this literature turn does not perform a new mathematical derivation.

The primary arXiv v1 PDF and HTML resolved. The author-v3 PDF endpoint
failed in this retrieval; no essential source is blocked because the
precise arXiv version is accessible. Assessment883 already recorded
the broader finite-order overlap, but nomination943 had not compared
the strict differential case. Do not silently replace C466a's older
Hub-v1 input or identify entire versions from their similar titles.
Retain the source's counting, finite verified-zero, extraction and
numerical-certificate trust qualifications. A theorem citation is not
an independent audit of those inputs.

### Reused numerical coverage and its limits

C466k(7) already covers every fixed derivative order. C466l explicitly
uses orders zero through four in the signed determinant identity.
There is therefore no need to reprove weighted inversion or Andreief.
C466n encloses S, c0 and a scalar value at S, rather than the requested
five values at S/3. Its fixed mesh, scalar fourth-derivative bound and
scalar omitted-tail number cannot simply be reused as derivative
error bounds.

Reuse review935's primary inspections of DLMF5.11(ii), Johansson
arXiv:1309.2877v1 Section2 Theorem1 (5)-(14), and Johansson
arXiv:1802.07942v1 Sections2/2.1/3.2. Reuse approval938's exact
DLMF3.5.6-8 Simpson hypotheses: a real C4 integrand, even equal-step
subdivision, and a fourth-derivative bound throughout each subinterval.
Those sources provide methods, not the missing derivative budgets.
Multiplication by powers of 1+it changes the quadrature and tail
requirements even when all special-function calls themselves stay
unchanged. No remainder may be differentiated from a value bound alone.
Every division still requires a denominator enclosure excluding zero,
and every common parameter interval must enclose the actual parameter.

If an independently motivated numerical reproduction is later proposed,
it must include all five absolute errors, parameter uncertainty, and
outward arithmetic through the actual determinant polynomial. Shared
parameters may widen interval bounds; ignoring their uncertainty is
invalid. A determinant interval containing zero is inconclusive. This
is an obligation list, not a new quadrature or determinant error lemma.

For ancillary context only, read Johansson's author-hosted
[Arb paper](https://fredrikj.net/math/arbpaper.pdf), introduction,
printed p1, on automatic interval error propagation and possible
overestimation; it supplies no certificate for the inherited elementary
interval implementation. Also inspected DLMF8.4.8's integer incomplete
Gamma formula as a possible tail-evaluation tool; no specialization or
tail bound was derived. These reads do not justify repeating known
finite-order signs merely to exercise an implementation.

### Duplicate/failure screen and decision

The actual queries were `"reciprocal xi" "determinant" density`,
`"theta_1" "xi" "derivatives"`, `Riemann xi reciprocal Laplace
density third order total positivity determinant`, and `Johansson Arb
rigorous ball arithmetic determinant interval matrix 2017`. Search
summaries were leads only. The exact arXiv theorem and relevant proof
case, not a search snippet or secondary post, determine this comparison.

Named local comparison included C466a/k/l/m/n/o, assessment883,
reviews930/935 and approvals938/942. The generic contact countermodels
are not actual-Xi counterexamples. Stop927 concerns scalar/pair phase,
stop932 conditional independence, and stop941 pointwise marginal
nonnegativity. None prohibits signed cancellation. The older reciprocal
coefficient-minor stop is an algebraic reformulation obstruction,
not this density-derivative test. Preserve all those records.

Outcome NEGATIVE is new decision evidence: the proposed sign-only
calculation would repeat a source-stated stronger result. It does not
give a negative determinant, disprove RH or independently validate the
source. No lemma, mathematical script, certificate, DAG or PROOF change
is made. Full matching Mathlib coverage remains unchecked. The narrower
known-result import is separately assessed in
2026-11-14-signed-third-source-import-944.md and receives next-turn
approval; the numerical deliverable remains unperformed and parked.

## Original nomination943 rationale (preserved)

The following paragraphs describe the original proposal, superseded
by comparison944's duplicate decision and narrower continuation above.

The main gap is still L030-L032/C032a actual-Xi all-degree
algebraic-square positivity. This finite test could show that full
signed integration survives the verified negative patches, or supply
a genuine local determinant obstruction. Neither outcome proves RH
or a global density-positivity criterion. The distinction is the
reason for this target; it is not another search for a negative ray.

Inputs for the prospective work are C466k's exact weighted inversion,
C466l's signed determinant identity, C466m's full completion and
C466n's S enclosure and numerical trust qualifications. C466a's
density assertion remains an external input. C466o supplies the
audited reason not to demand pointwise marginal nonnegativity; it
does not supply a determinant sign. These are prose citations, not
an additional dependency graph or an assertion that the new
calculation is already covered.

Before any mathematical script or new bound, reuse the appropriate
parts of review935 (DLMF Gamma remainder, Johansson zeta remainder,
and Simpson theorem) and determine exactly which derivative cases
were inspected. The new target changes both evaluation point and
derivative orders. Import any matching sign theorem by precise
citation instead of reproducing it. Otherwise assess only the
uncovered enclosure requirements. A needed but inaccessible primary
case is a source blocker, not permission to run an unqualified
numerical calculation. Full matching Mathlib coverage is unchecked.

The prospective discriminator is a proved determinant interval
strictly separated from zero after all errors are included. If it
contains zero, retain the actual interval and identify which error
or cancellation prevents separation; samples or requested precision
are not evidence of a sign. A positive enclosure is only one actual
signed case and warrants further work only with a concrete extension
mechanism. A negative enclosure requires a separate critical audit
before any stronger interpretation. No enclosure or new lemma has
been derived during nomination943.

The next turn is literature_comparison, standard/high, because the
essential task is comparing this changed scope with ready source
coverage and recorded failures. This is not creative proof work or
a candidate audit, and there is no repeated-source quota justification.
