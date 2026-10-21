# Cyclic rank-27 actual-error realization — source comparison

TARGET: Determine whether every rank-27 labeling of L087's cyclic family realizes sixteen actual bad parameters in the frozen affine-line model.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 234 searched the conditional cyclic realization and syndrome-line/secant terminology, compared the local analogous construction and stops, and reused the inspected random-RS and exterior assessments; queries and scope limits appear below.
SOURCE_EVIDENCE: Read the pinned ArkLib IsMCA/mcaError/AffineLineGenerator declarations; Hall Theorem 5.1.1 and complete proof; Chojecki's author TeX Section 3 normal-form proposition and exact syndrome--secant theorem, equations (3.1)–(3.4), with both proofs; read the relevant L010/L075/L076/L087/L088/L089 statements and construction ranges.
COMPARISON: The generic same-support syndrome reduction is known and should be cited. L075 already gives the finite-chart construction for another family; audited L088/L089 supply cyclic plane and fullness inputs. Their exact cyclic assembly, including the moment convention and locator gates, is not an inspected theorem and remains to be written separately.
GAP: Essential source coverage is ready; the conditional cyclic specialization remains unproved, no rank-27 labeling is known, and neither uniform rank 28 nor arbitrary-family coverage follows from this assessment.
REASON: The newly proposed actual-event application lay outside the saved exterior assessment; this separate source comparison approves one subsequent specialization attempt without performing it or certifying novelty.
SCOPE: Fixed F=F_(97^20), fixed order-sixteen H in F_97^*, every bijective h, exactly B_s={s,s+1,s+4,s+6}, and hypothetical rank M=27; construct a new chart and verify all L010 gates using audited cyclic inputs. No claim about a prescribed original chart, other families, or ABF26 is covered.

The proposal below is preserved from step 233. Its REVIEW_REQUIRED wording
describes the proposal at that time; the completed comparison and current
SPECIALIZE decision are recorded after it.

## Exact proposed scope

Fix F=F_(97^20), the order-sixteen subgroup H of F_97^*, a bijection
h:Z/16Z -> H, and blocks B_s={s,s+1,s+4,s+6}. Assume the full
alternating matrix M of L088 has rank 27. The proposed conclusion is
existence of input words for the length-sixteen, dimension-eight code
whose frozen affine-line event has sixteen distinct finite bad
parameters with these actual four-error supports on [1/4,5/16).
This is a proposed conditional statement, not an established theorem.
Check its exact event conventions against foundations/02 before
approval; no equivalence with the unread ABF26 event is proposed.

Prospective inputs are audited L087/L088/L089 and L010's precisely
scoped moment/event criterion. Their audited status does not prove
this application. Unshifted columns and shifted moments must be
reconciled; the excluded affine direction must be chosen and checked
without silently rationalizing an arbitrary original pencil. No rank-27
labeling is supplied. Actual-error existence, distinct finite parameters,
same-support failure and locator conditions remain proof obligations.

## Separate next review

Reuse existing exterior and finite-field source assessments only where
their exact hypotheses apply. Search the conditional realization
statement and standard syndrome-line/RS error-representation terminology;
compare precise source theorems with these hypotheses. Read necessary
parts of foundations/02, L010 and the analogous L075/L076 construction,
distinguishing its affine-plane incidence from the cyclic inputs.
Determine which parts can be imported and what specialization is
uncovered. This REVIEW_REQUIRED file authorizes no new mathematics.
Full matching Mathlib coverage is not checked.

A later complete conditional realization could connect rank deficiency
to sixteen-count attainment in the frozen model; a genuine extra
obstruction could identify an additional requirement on a deficient
labeling. Neither supplies a labeling, arbitrary-family coverage, a
uniform triangle bound or missing challenge qualifications. This target
does not reopen ATTEMPTS/020,031,032,033,034.

## Completed literature-only comparison — step 234

LITERATURE_REASON: The conditional actual-error target newly adds finite-chart,
moment-convention, locator and same-support hypotheses that the cyclic
exterior assessment expressly excluded. The existing ingredient assessments
are reused; this is not another search for the ready zero-kernel target.

The main local gap is whether sixteen actual bad parameters are possible
in the frozen four-omission cell, where safety requires at most fifteen.
The intermediate target is exactly TARGET, conditional on rank 27; it
does not seek or assume existence of such a labeling. Its downstream use
would be to decide whether a deficient cyclic labeling suffices for an
actual extremal pencil, or whether an additional obstruction must be
tested. Uniform rank, other support families, triangle twelve and the
challenge-definition qualifications remain independent open issues.

### Primary inputs and applicability

**Frozen event.** Re-read the immutable ArkLib revision
`e65197892890b8fd9b0dc05b8980273cf1d595cc`,
[*ProximityGenerators.lean*](https://raw.githubusercontent.com/Verified-zkEVM/ArkLib/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ProximityGap/ProximityGenerators.lean),
`CoreDefinitions.IsMCA`, `mcaError` and `AffineLineGenerator`
(source lines 98–104, 136–138 and 246–249 in the retrieved copy).
The field alphabet and two-row generator give the model fixed in
foundations/02: the same qualifying agreement set must fail for at least
one input, and the challenge is uniform over the whole field. These are
definition sources, not a verified Lean build or ABF26 identification.

**RS distance.** Reused the October 5 two-block assessment and re-read
J. I. Hall, [*Notes on Coding Theory*, GRS chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
undated author-hosted copy retrieved October 15, 2026, Theorem 5.1.1 and
its entire proof, printed pp. 63–64. It assumes a field, distinct
evaluations, nonzero multipliers and 0<k<=n, and gives dimension k and
distance n-k+1. Fixed H, unit multipliers and n=16,k=8 satisfy those
hypotheses over both fields. Cite this known input rather than reprove
RS distance. L010 already supplies the particular surjective moment map
and kernel identity needed here.

**Known syndrome reduction.** Przemek Chojecki,
[*Shortening Bounds for Reed–Solomon MCA*, author TeX](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex),
header dated July 17, 2026, mutable copy retrieved October 15, 2026,
Section 3, proposition `prop:syndrome-line-normal-form`, equation (3.2),
and theorem `thm:syndrome-secant-exact`, equations (3.3)–(3.4), were read
with both complete proofs and the preceding parity-check setup (3.1).
For a full-rank parity check with kernel C, the proposition equates
same-support badness with a syndrome-line meeting the error-support span
without both generators belonging to that span. The theorem takes the
union over errors of size at most n-a and maximizes using surjectivity.
Its proof explicitly allows any such parity check. This covers the
generic bridge; it supplies no cyclic rank decision, full coefficients
or locator nonpersistence. Cite the reduction; justify its particular
map and hypotheses locally. Byte identity with the September copy or
ePrint 2026/1463 is not asserted, and later claims are not imported.

### Comparison with the local construction

Read L010 in full, L075's hypotheses and conclusion and its entire
“Sufficiency, with all equality gates” section, and L076's finite-chart
test and final assembly. L075 is an existing analogous proof, not an
audited cyclic theorem. L073–L076 remain unaudited and their affine-plane
rank/fullness conclusions are not inputs to the proposed specialization.
L076's omitted parallel class and deficient-block argument are specific
to its family and are unnecessary comparison material once cyclic
fullness is taken from audited L089. No general fullness theorem is
being inferred from that analogy.

The future application has these exact obligations and available inputs:

| Obligation | Existing coverage and remaining application |
| --- | --- |
| A rational two-plane at rank 27 | Audited L088 states rational decomposability of the unique kernel; L089 states the resulting intersections. Use their exact fixed-H scope. |
| Sixteen distinct full intersection lines | Audited L089 states this for precisely these cyclic blocks. Do not import it from the affine-plane family. |
| A new finite chart containing all sixteen points | Compare L075's chart choice over F_97. This is a construction of inputs, not transport of a preassigned affine pencil. |
| All eight moments and nonzero actual error weights | Reconcile L088/L089's unshifted columns with L010's shifted columns, including coefficient rescaling. L010 supplies surjectivity and kernel C. |
| Nonzero D and every coordinate locator | Apply L010's pointwise full-error identities only after constructing full errors. L087 supplies degree four, so its avoidance condition must be checked in this application. |
| Badness on the same support | The cited normal form requires noncontainment. Alternatively L010 supplies its already proved argument after every polynomial hypothesis is verified. Decodability alone is insufficient. |
| Exactly sixteen over the whole extension | Apply the complete L010 bound, including singular and lower-weight parameters, after verifying its hypotheses; do not count only prime-field events. |

This table identifies a specialization to attempt, not a proof that its
gates have been met. No formula constructing a cyclic pencil or new
mathematical conclusion is established in this literature turn. Generic
syndrome geometry and L010 need no reproof; the exact cyclic application
must be written because neither the source theorem nor L075 states it.
REPRODUCTION is the appropriate classification for that later assembly;
this review makes no claim of progress beyond the inspected literature.

### Search, duplicates and parked leads

Targeted queries on October 15, 2026 were:

- `"Reed Solomon" "syndrome" "line" "mutual correlated agreement"`
- `"Reed Solomon" "rank 27" cyclic`
- `"Reed Solomon" "syndrome" "secant" line errors`
- `"Reed-Solomon" "syndrome" "line" "secant"`
- `"mutual correlated agreement" "syndrome"`
- `"Reed-Solomon" "syndrome" "cyclic" "sixteen"`
- `"Reed-Solomon" "transverse" "syndrome" "realization"`
- `"cyclic" "rank 27" "agreement"`
- `"syndrome" "line" "sixteen" "agreement"`

No exact cyclic realization statement was identified in the screened
results. This is no evidence of novelty. Secondary indexes were used
only to identify leads; their apparent challenge-resolution claims,
snippets and decoder patents are not theorem evidence.

Reuse `drafts/literature/2026-09-26-current-target.md` for Yuan–Zhu,
[arXiv:2605.07595v2](https://arxiv.org/html/2605.07595v2),
Definition 4.1 and Theorem 6.6, previously inspected at theorem level.
The current primary definition and ensemble restriction were rechecked:
common sparse lifts and high-probability iid random-RS conclusions do not
decide this fixed H or supply sixteen specified actual errors. No full
proof refresh or result from that source is needed here. Reuse the same
assessment's Gao–Yang–Xu–Kan comparison: a construction that may change
an evaluation point cannot be substituted for prescribed H. The ready
October 12 affine-plane assessment likewise limits generic/selectable
evaluation and four-subspace results; it is not a cyclic realization
theorem. Those full source readings were not repeated.

Okamoto ePrint 2025/1712 reappeared as an abstract-level syndrome-space
lead. The precise prior access failure and overlap limit are recorded
in `drafts/literature/2026-10-06-six-support-fixed-block-obstruction.md`.
Its theorem text remains unread, not an imported result or a basis for
novelty. Jo, ABF26 and the parked campaign artifacts also remain unread
as recorded in the prior assessments. None is an essential input for
this conditional frozen-model application; no repeated access attempt
was made. A GitHub commit-metadata request for the mutable Chojecki file
failed in the browser; the section labels, retrieval date and version
qualification above are retained instead of claiming an immutable copy.

The duplicate check distinguishes L075's conditional construction from
L089's already established fullness. ATTEMPTS/028 stops forcing a zero
coefficient for the affine-plane route, not this application. ATTEMPTS/031
prevents transferring its family theorem by isomorphism. ATTEMPTS/020
stops positive rank sampling, and ATTEMPTS/034 stops repeated joint-gate
elimination; ATTEMPTS/032–033 remain preserved. This target requires no
label sweep, expanded elimination or audit of L090–L095.

### Continuation and abandonment test

Essential coverage is complete for exactly TARGET, ready for a separate
invocation under supervisor approval. Attempt one citation-based cyclic
specialization using audited L087/L088/L089 and L010, with L075/L076
only as construction comparisons. Retain the fixed field, arbitrary
bijection and hypothetical rank 27 throughout. Check every row of the
obligation table; any reproof must be limited to the identified application
difference, not generic syndrome geometry or RS distance.

Continue if the attempt establishes all gates or identifies a precise
additional requirement with a concrete independent test. If an essential
gate does not follow, stop the asserted implication and preserve that
gap; do not call an unconstructed deficient plane a counterexample.
A successful conditional proof supplies no rank-27 labeling and therefore
no attained sixteen-count example. Uniform rank, arbitrary families,
triangle twelve and ABF26 qualifications remain unresolved either way.

Full matching Mathlib coverage and supporting formal coverage are **not
checked**; ArkLib's event declarations are separate. No lemma, mathematical
script, DAG or proof overview was changed. This source review uses zero
mathematical exploration turns and does not reset the carried count one.
