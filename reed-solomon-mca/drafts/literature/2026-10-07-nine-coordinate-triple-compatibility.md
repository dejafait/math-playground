# Nine-coordinate triple compatibility — completed source comparison

TARGET: Derive an exact compatibility criterion for three actual L010 equality errors with union size nine, allowing arbitrary F_(97^20) weights and original finite parameters.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded exact-target and affine-dependence/shortening searches; inspected L016's fixed-nine-union reduction and compared L010, L032, L040, prior shortening/ray assessments and ATTEMPTS/017, /019, /020, /021; queries and limits below.
SOURCE_EVIDENCE: Reused Hall Theorem 5.1.1 and full proof, printed pp. 63–64, and Marquez-Corbella–Pellikaan (2016) section 5, Definitions 5.1–5.2, Lemma 5.3 and following GRS formula, printed pp. 7–8, from the saved primary extracts; inspected Chojecki's live author TeX on 2026-10-08, thm:bounded-residual-kernel-ray, thm:single-mds-circuit-ray and complete proofs, and drc:lem-locator-recurrence/drc:thm-exact-compiler with proofs, direct URLs below.
COMPARISON: L016 already uses the one-dimensional shortened-code mechanism for fixed supports at 0,1,2. Standard shortening and distance cover its coding inputs, but arbitrary nine-union supports and original finite parameters require a separate exact specialization; neither L016's count five nor the circuit compiler's restricted count is an arbitrary-family bound.
GAP: Generalize only the local compatibility mechanism, including every support-membership case, parameter difference, kernel degeneracy and full-weight test; no general nine-union criterion or extraction theorem is established here.
REASON: Essential source coverage is adequate for one bounded reproduction of the existing fixed-triple mechanism with changed support/parameter hypotheses; no new mathematical relation was derived during this review.
SCOPE: The exact TARGET only, with the frozen field/domain/event, all eight moments, L010 nonpersistent hypotheses and sixteen-count equality, three distinct original finite parameters and their actual full-weight four-errors whose union is explicitly nine; no prime-subfield restriction on parameters or weights.
LITERATURE_REASON: The changed nine-coordinate scope was explicitly REVIEW_REQUIRED; source comparison now identifies the existing fixed-nine-triple overlap and an independently accessible circuit theorem rather than repeating ready union-six literature.

## Gap, intermediate target and decision test

The main gap is arbitrary-family sixteen-count equality: 11/q–16/q
against allowable fifteen. The intermediate target is the exact local
criterion in TARGET. It could constrain a support regime outside the
union-six branch, without assuming that every remaining family has such
a triple. Universal extraction, other union sizes, sixteen-count
completion, ABF26 identification and global fifteen remain open.

Essential input is L010; reuse L016's analytic mechanism, not its fixed
numerical count. L032 and L040 are comparisons. Retain F=F_(97^20),
H of order sixteen in F_97, k=8, the pinned cell, all eight shifted
moments, nonzero polynomial D and every locator, sixteen-count equality,
three distinct original finite parameters and their actual full-weight
four-errors, explicitly assumed union nine, arbitrary F weights and
parameters, same-support badness and unrestricted excluded [v].
No general kernel criterion or rational descent is assumed.

Continue on a necessary-and-sufficient local description beyond raw
moment equations, treating every support-membership and zero-weight case.
A useful constraint may leave completion unresolved. Reassess if this
only repackages the eight equations, leaves a degeneracy untreated or
needs essential unread mathematics. A compatible local triple is not a
sixteen-count witness and cannot refute the main target.

## Reused primary coding inputs

J. I. Hall, *Notes on Coding Theory*, [GRS chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
Theorem 5.1.1 and full proof, printed pp. 63–64, undated author-hosted
copy inspected 2026-10-05. Reuse the complete extraction in
`2026-10-05-two-block-moment-obstruction.md`. The hypotheses are any
field, distinct evaluation points, nonzero multipliers, and 0<k<=n;
the conclusion is dimension k and distance n-k+1. Our n=16,k=8,
distinct H labels and unit multipliers satisfy these over F itself.
L010 supplies the exact shifted-moment kernel and eight-column
invertibility. No distance or parity-check reproof is needed.

I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
[DOI 10.1016/j.ffa.2016.04.004](https://doi.org/10.1016/j.ffa.2016.04.004),
[accepted manuscript dated 2016-02-29](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
section 5, Definitions 5.1–5.2, Lemma 5.3 and following unnumbered GRS
shortening paragraph, printed pp. 7–8. Reuse the inspected extract in
`2026-10-07-six-coordinate-triple-equality-obstruction.md` and its scope
assessment. Shortening first requires zeros at deleted labels. The GRS
paragraph reduces dimension by one at a deletion and multiplies retained
multipliers by the difference from the deleted label. Repeated use
requires checking each positive dimension and each nonzero difference.
Deletion of the seven labels outside a specified nine-set is within that
formula's scope. The general MDS lemma states n-m>=k; 16-7>=8 meets it.
This verifies source applicability, not any triple compatibility or
unique affine lift assertion. Today's PDF open returned Internal Error;
complete prior coverage is reused, not claimed freshly reinspected.

## Newly inspected circuit and recurrence comparison

[Chojecki, live RS_MCA_Paving_v9.2.tex](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex),
inspected 2026-10-08; not certified identical to ePrint 2026/1463.
Read full statements and proofs at source lines 1370–1460 and 2785–2935.
Named labels provide citation anchors if line numbers move.
`thm:bounded-residual-kernel-ray` assumes transverse finite witnesses
contained in a fixed U and gives (t+1)|F|^kappa(U).
`thm:single-mds-circuit-ray` requires RS redundancy R, |U|=R+1 and t<R;
its bound is binom(R+1,2). Its proof uses a full-weight circuit kernel
and charges transverse slopes to pairs of affine coordinate functions.
The recurrence lemma DR2 tests support-span membership; DR6–DRC solve
proportional projected syndromes, separating zero direction from
transverse finite intersection. The common-intersection cases were read.
For R=8,t=4 the circuit bound is 36 and requires every counted support
inside U. Only our selected triple is assumed inside its nine-set.
These results give neither fifteen nor an exact classification of three
prescribed full-weight errors. No arbitrary-family premise is imported.

The prior twelve-incidence assessment already records the general
ray-compiler comparison and inadequate general MCA estimates. Reuse
those conclusions; no broader prize-source audit is repeated.

## Local duplicates, failures and searches

Read L016 through its exact fixed-triple parameterization and converse,
and its finite-certificate scope. Its supports are
{1,8,12,18}, {1,8,22,27}, {1,33,47,50}, at parameters 0,1,2.
Its first proof uses a scalar degree-seven vanishing polynomial on the
complement of that union; its normalized full-weight gate is specific
to those supports. Its count five is also specific. The proposed work
reproduces/generalizes that analytic mechanism, rather than discovering
it independently. L032 assumes union at most eight and uses injectivity;
its affine lift cannot be extended by citation. L040 excludes union six
only. No cross-notebook input is used.

Actual searches on 2026-10-08:

- `"Reed Solomon" "three" "nine" syndrome compatibility errors`
- `"MDS" "three" "minimum weight" codewords supports affine dependence`
- `"Reed Solomon" "triple" "mutual correlated agreement"`
- `"Reed-Solomon" "affine dependence" "errors"`
- `"GRS" "shortening" "minimum weight" supports`

Hits included decoder implementations, codeword-design papers,
subfield-subcode articles and campaign/proximity leads. Snippets do not
establish matching coverage; no result is imported from them. The direct
author source above was the inspected primary lead. Parked Jo/ABF26 and
campaign artifacts remain unread; no novelty or progress beyond those
sources is asserted. Mathlib coverage of the exact criterion is not checked.

Read ATTEMPTS/017, /019, /020 and /021 in full. Their stops preserve the
failure of universal small-union extraction, exhausted cyclic containment,
positive-only labeled rank sampling and support-only all-disjoint exclusion.
None supplies or bans this conditional actual-weight test. Do not reopen
those mechanisms or presume universal nine-union extraction.

## Ready continuation

One bounded proof attempt on the unchanged TARGET is covered as
REPRODUCTION. Use L010 and L016's existing analytic mechanism, citing
the standard inputs above rather than reproving them. The difference to
justify is arbitrary supports, all membership patterns and original
finite parameters, including full-weight and kernel-degeneracy tests and
both directions of the local criterion. Any normalization must be
justified and translated back; no rational parameters or excluded [v]
follow from rational labels. Keep local moment compatibility distinct
from same-support badness, nonpersistent locators and completion to
sixteen errors. The numerical certificate in L016 is not an input.
This separately completes step 082's pending coverage review. No new
lemma, mathematical relation or mathematical script was written here.
