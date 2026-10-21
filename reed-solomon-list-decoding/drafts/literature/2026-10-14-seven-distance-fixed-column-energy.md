# Distance-seven fixed-column energy — source comparison approved

TARGET: Evaluate the exact generalized-Schur energy of L065's explicit rational distance-seven column against the unchanged L061 base and decide whether it gives a one-column PSD extension.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready 2026-10-13 full-shell-column-energy assessment and foundations/10; compared the relevant L060,L061,L065 proof passages, ATTEMPTS/041,042,043,046,047 and history/221. Directly reopened Sano's primary Section 2 criterion and range-inverse proof. No new broad search or novelty inference.
SOURCE_EVIDENCE: Takashi Sano (version of record 27 February 2026), DOI 10.1007/s44146-026-00231-y, Section 2 Theorem 2.1/proof, Corollary 2.2, Theorem 2.6/both proof directions and Lemma 2.7/both proof cases; publisher full text read 2026-10-14. Reuse foundations/09,10,12 and the prior energy assessment for unchanged inputs.
COMPARISON: The known finite Hermitian singular-block criterion and range-inverse construction cover this real finite anchored base even when singular. They do not evaluate L065's fixed column or identify the weighted quotient inverse with full-space inverse action. L060 supplies a different verified application, not this energy verdict.
GAP: Research must justify the full-space weighted inverse action with anchor retained, reconstruct exactly the fixed L065 witness and unchanged L061 base, and certify its energy comparison with p7. No coefficient, energy value or PSD verdict is established in this literature step.
REASON: Essential source coverage is adequate for one exact finite specialization; the change from a five-shell base to the coupled anchored five/six base requires a new application and certificate, not a new general source theorem.
LITERATURE_REASON: The new fixed-column energy scope was outside the approved full-kernel-only audit. This separate comparison resolves that coverage gap while reusing ready inverse-action and singular-PSD literature.
SCOPE: Exactly TARGET, positive rho, original p7=3539/248922676958508, unchanged L061 base and L062 dictionary, and exactly L065's u=v=0,w=-c_4/a^42_4 witness. No family optimization, retuning, multiple columns, new shell or actual-label averaging.

## Relevance and discriminating test

The main gap is arbitrary-center safety at 67/68 agreements; the finite
bracket remains 955–957. The intermediate target is the energy verdict
for this single fixed distance-seven column. A pass would retain one
larger PSD principal matrix for later extension tests; a failure would
reject this witness while leaving the three-parameter compatible family
open. Neither alone resolves the main gap or proves a uniform SDP bound.

The continuation test is an exact energy at most the unchanged normalized
new diagonal p7, including equality. An exact larger value abandons only
this fixed column as a PSD extension of this fixed base. Failure to
justify normalization or the lifted inverse action leaves the test
unresolved, rather than establishing either verdict. Do not silently
minimize over the compatible family after a fixed-witness failure.

## Primary theorem comparison

Import Sano, *Moore-Penrose inverse, generalized Schur complement and
inertia*, Acta Scientiarum Mathematicarum (2026),
[Section 2 publisher full text](https://link.springer.com/article/10.1007/s44146-026-00231-y).
Theorem 2.6 characterizes PSD of a finite Hermitian block matrix by PSD
of its retained block, the kernel inclusion, and nonnegativity of the
generalized Schur complement. Its proof treats necessity through the PSD
square root and sufficiency through Corollary 2.2's invertible triangular
congruence. Corollary 2.2 also equates the range and kernel conditions.
Lemma 2.7 constructs the inverse on the range using the restriction to
the kernel's orthogonal complement, and zero on the orthogonal range
complement. Both proof cases were inspected; finite-dimensional ranges
are closed. No nonsingularity or maximal-rank hypothesis is required.

Applicability: the proposed base is finite and real symmetric; its PSD
input is L061, and L065 supplies whole-base kernel compatibility. The
new diagonal is scalar and positive. These are within the source's
hypotheses. The paper supplies no value for the prescribed column.
No source theorem needs reproof. The application-specific weighted
realization remains a research obligation, not a result of this review.

Reuse foundations/10 and the ready assessment
`drafts/literature/2026-10-13-full-shell-column-energy.md` for the previous
source search, exact primary passages and unread-lead qualifications.
Albert (1969), Theorem 1 remains an attributed original, not a newly
inspected proof. The previously inaccessible Boyd book is irrelevant to
this fixed-column test: no parameter minimization is requested. No
additional convex-optimization source is essential here.

## Exact specialization obligations

Essential local inputs remain L021,L053,L056,L059,L060,L061,L062,L065
and foundations/09,10,12. This is coverage for their stated scope, not a
new critical audit of all those inputs. In particular retain the entire
immutable lookup and every original pair, including positive rho and p7.
L065 specifies the witness uniquely, with its anchor entry p7 after
normalization by rho; its complete rational certificate must be consumed
when computing, rather than a preview of selected coordinates.

L065 already provides the 86-coordinate action on orbit-constant functions,
positive orbit weights (anchor weight one), weighted self-adjointness,
and the full-kernel averaging justification. Research must establish
that its chosen inverse solution lifts to the actual retained matrix
and has the required full-space range interpretation. Check every action
residual and, if claiming the Moore–Penrose inverse vector itself, its
weighted kernel orthogonality. An unweighted Euclidean pseudoinverse of
the nonsymmetric quotient is insufficient. Quotient rank 37 is not a
rank assertion about the full base; no omitted-mode multiplicity may be
inserted in place of actual orbit norms.

Retain both layers and the anchor in the primary calculation. If instead
using an anchor congruence, transport the entire enlarged matrix and
column and apply the source theorem to the resulting block; no general
pseudoinverse transport through congruence is licensed. L060's positive
constant mode and anchor caution remains relevant, but its distance-six
energy and interval optimum cannot be reused as this verdict. The
coupled inverse must include all cross-layer and singular directions.
No specific compressed energy identity is derived here.

## Duplicates, stops and bounded authorization

ATTEMPTS/041,042 concern the smaller distance-six kernel and energy
tests. ATTEMPTS/043 retains the simultaneous five/six base, while
ATTEMPTS/046 retains one distance-seven small-principal pattern.
ATTEMPTS/047 and history/221 explicitly leave this scalar energy open.
The relevant local records provide no duplicate fixed-column energy
verdict. Their passing certificates do not settle the current test.
The old kernel stop remains valid and does not ban this different test.

Approve one REPRODUCTION calculation under this SPECIALIZE assessment.
Save the complete rational witness, weights, base action, inverse evidence,
residuals and actual-versus-required energy comparison to disk, with a
canonical proof if a result is obtained. No mathematical script was run
or written and no new lemma was derived in this review. A later result
must receive any separate critical review required by notebook policy.

Multiple new columns, global moment consistency and PSD, actual labels,
representing measures, packings and RS realization remain unproved.
Full matching Mathlib coverage and supporting weighted inverse coverage
remain not checked; unknown availability is not evidence of absence.
