# C645h full boundary transfer — approved audit scope

TARGET: Audit C645h's full principal-part reduction and boundary lower bound under the exact sparse-census and interpolation hypotheses.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed searches in 2026-11-01-sparse-hankel-principal-part-transfer.md; compared C645h's complete written proof for input scope, C645g (1)–(6) and its application qualification, and the exact scalar-cancellation/envelope failure records. No new broad search or novelty inference.
SOURCE_EVIDENCE: Reused the parent's inspected Beck et al. Theorem 8.1.7(i), including the simple-pole proof, https://complexanalysis.org/web/sec_residue-thm.html ; Baratchart–Chevillard–Qian (2016), Section 2 pp.18–21, (17)–(19) pp.24–25 and (25) pp.27–28, https://www.must.edu.mo/images/SCSE/qiantao/QianTao_P147.pdf . Exact source statements and cases are retained in the parent review; no new retrieval or source-proof audit.
COMPARISON: The written application uses the parent's simple-pole decomposition, bounded analytic multiplier and contractive Hardy projection with unchanged synthetic hypotheses and C645g constants; no additional theorem, regularity weakening, Nehari/AAK norm identity or new estimate was introduced. The particular grid removals, collar, all-input identity and scale factors still require independent mathematical verification.
GAP: Source coverage suffices for the independent conceptual audit of the written specialization; that audit is not performed here. Actual-Xi census, clearance, realization and a smaller upper bound remain open.
REASON: This separate source-scope comparison approves the unchanged audit target; the parent's primary coverage is adequate and no essential unread input was identified. A later research turn must verify the local applicability proof rather than reprove general operator theory.
LITERATURE_REASON: The newly written C645h proof was the specific new review object requiring separate gate approval; the present turn compares its complete input inventory with ready parent coverage, without repeated browsing.
SCOPE: Only the complete proof of C645h with its unchanged synthetic hypotheses, exact q and constants; no higher-order poles, weakened regularity, actual-Xi application or new upper bound.

## Approval and subsequent audit scope

The nomination paragraphs below are preserved as the pre-approval record.
The completed comparison at the end supersedes their pending gate status;
it does not assign a mathematical audit verdict.

First compare this nomination with the unchanged parent SPECIALIZE
assessment `drafts/literature/2026-11-01-sparse-hankel-principal-part-transfer.md`.
Its sources and hypotheses should be reusable; this nomination does not
itself approve the new audit. If complete, a separate literature approval
may prepare the conceptual proof audit without broad new searching.
An essential mismatch must be stated precisely, not silently repaired.

For that later mathematical audit, read the full canonical C645h proof
and C645g's quantitative statement/application scope; load its proof only
where an actual dependency doubt requires it. Verify all n grid removals,
the complete distinct simple-pole list, residues after scaling with 1/R,
holomorphy of the remainder near the entire closed disk, the bounded
multiplier argument for arbitrary H2 inputs, and the one-sided norm
comparison with the exact anchor factor. Distinguish local existence of
a collar/bound from uniform control in n. Check (6) includes precisely
the small total-residue census and leaves actual-Xi assumptions open.

Continue if every singularity and operator-domain premise is accounted
for and the threshold follows without an extra R or a reversed inequality.
Otherwise identify a concrete counterexample or missing hypothesis and
preserve the failed proof before any later repair. C645d's scalar
cancellation and C645b's envelope stop remain valid comparisons; no
stopped positivity shortcut is reopened. This is no RH candidate and no
novelty assessment beyond the parent search. Matching Mathlib coverage
remains unchecked. No cross-notebook input is needed.

## Completed separate source-scope comparison — 1 November 2026

The main gap is actual-Xi signs at unbounded heights/all-degree mixed
positivity. The intermediate target is independent scrutiny of C645h's
synthetic full-residual transfer. If sound, this bridge could be used
against an independently proved upper bound strictly smaller than its
stated boundary threshold. Neither such an upper bound nor actual-Xi
realization is furnished by the sources or this review.

Read the complete parent assessment and C645h proof to inventory its
inputs, not to certify its derivation. Compare C645g's quantitative
statement and application qualification: the same delta, eta, n, exact
complex B_n, anchor x, q with 1/R, distinct grid-avoiding simple poles,
positive integer residues and small total-residue coefficient are retained.
C645h adds exactly the meromorphic F, holomorphic P and interpolation
already assessed by the parent. Its data-dependent neighborhood does
not request uniform collar size or uniform analytic-remainder bounds.
No extra theorem is invoked in its polynomial-density multiplier argument;
the validity of that argument for every H2 input remains an audit task.

Primary coverage is reused from L. Baratchart, S. Chevillard and T. Qian,
*Minimax principle and lower bounds in H2-rational approximation*,
J. Approx. Theory **206** (2016), 17–47,
[DOI 10.1016/j.jat.2015.03.004](https://doi.org/10.1016/j.jat.2015.03.004),
at the precise passages in SOURCE_EVIDENCE, and M. Beck et al.,
*A First Course in Complex Analysis*, online unversioned Theorem 8.1.7(i)
as inspected by the parent on 1 November 2026. These cover the general
decomposition and projection framework. They do not themselves state
C645h's grid-specific identity or its boundary threshold. This is why
SPECIALIZE, with an independent applicability audit, is appropriate;
IMPORT would not discharge those local checks. No changed hypothesis or
new relevant source undermines the ready assessment, so repeating external
retrieval is unnecessary. There is no essential unread lead or blocker.

Duplicate and failure comparison: C645g explicitly defers the full F/P
application; C645f's restricted predecessor is not a proof of the larger
family. C645h is the completed application being reviewed, not a request
for another lemma. Read the scalar-cancellation record
`ATTEMPTS/2026-11-01-inverse-blaschke-unit-residue-noncancellation-stop.md`
and envelope record
`ATTEMPTS/2026-11-01-completion-stripped-convexity-envelope-limit.md`.
They exclude neither this full-operator audit nor justify a scalar lower
bound or actual-residual upper bound. Their stops remain in force.

Decision: SPECIALIZE for the exact TARGET. Next perform one conceptual
proof audit using C645h and C645g's audited quantitative statement. Check
all grid removals and genuine poles, the neighborhood/collar argument,
every-input bounded multiplier, q's 1/R, normalized modes and measure,
the one-sided operator comparison and the exact anchor factor. Continue
only if those checks establish the stated identity and threshold without
additional hypotheses; otherwise record the precise mathematical defect
and preserve the proof before a separately scoped repair. Read C645g's
proof only where a concrete dependency doubt requires it. This gate
approval asserts neither a successful proof audit nor an RH candidate.

Outcome: EXPLORATION, a first completed comparison of the written
application's input scope with ready coverage. No new mathematical
result, source theorem, lemma, script or proof-assembly change. Full
matching Mathlib coverage remains unchecked. No cross-notebook input.
