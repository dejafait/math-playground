# Fixed product excluded-anchor five/six matrix — source approval

TARGET: Test the complete excluded-anchor distance-five/six matrix throughout L112's unchanged product box, retaining every source entry and the full anchor.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 438 reused discovery and primary inspections in 2026-10-14-complemented-five-six-shell.md and 2026-10-23-fixed-product-coupled-five-six-psd.md; compared foundations/04,09,12,14, L063's source/dictionary/anchor cases, L098/L112 hypotheses, L116's full entry/reduction/interval ranges, ATTEMPTS/045,094 and history/437. Fresh queries were `"Schrijver" "constant weight" "excluded" semidefinite` and `"distance product" "constant weight" "semidefinite"`; no inspected result supplies this fixed-assignment verdict and no novelty inference follows.
SOURCE_EVIDENCE: Freshly read Schrijver https://homepages.cwi.nl/~lex/files/codes.pdf DOI 10.1109/TIT.2005.851748, author manuscript III.B (60)–(65), printed p.7, including both outer-product averages and scalar explanation; Kim–Toan https://arxiv.org/pdf/1212.3467v1 III.A Remark 11 and III.B (31)–(35), all conditions (i)–(iv), printed pp.8–9. Reuse foundations/09's full unequal-layer proof inspection and foundations/14's Rump §5.5 (5.16)–(5.17), author p.28, plus the retained positive-pivot Schur input.
COMPARISON: The primary statements cover opposite-pair-minus-triple coefficients, repeated words, original t-s symmetry, forbidden cases and unequal layers. L063 verifies the same necessary matrix geometry at different pairs/triples; L116 verifies included-anchor PSD at the present product box. Neither transfers its sign verdict to this changed affine family. The remaining work is a finite reproduction of assessed tools, not a missing general theorem.
GAP: Essential source coverage is ready; the complete current affine dictionary, zero anchor, coherent signed rectangular normalization and whole-box block signs remain to be checked. No excluded-anchor entry, interval, block or sign at L112's assignment was evaluated in this review.
REASON: Approve one bounded finite specialization at the exact saved target. Citation alone does not verify its immutable coefficients or PSD signs; no spectral, interval or completion theorem needs reproof.
SCOPE: Exactly TARGET at exact N, canonical c_i and all 64 original L112 endpoints/scales; complete excluded-anchor layers 0,5,6 only. Retain every source entry and verify the entire anchor before removing a zero row; no solve, scan, retuning, refinement or full-SDP assertion.
LITERATURE_REASON: Changed affine source family from included-anchor triples to excluded-anchor opposite-pair-minus-triple entries. This turn completes the essential scope comparison, reusing the ready algebraic and interval coverage.

The main gap remains arbitrary-center 67/68-agreement safety. Full
source PSD is unresolved for the shared scalar/exact-N assignment.
This different necessary matrix could reject that assignment or supply
one additional retained principal-matrix input. It cannot establish
full PSD or realization on its own.

The initial proposal above is now approved only in the exact scope below.
No cross-notebook input is used.

## Primary hypotheses and essential proof cases

Import Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE Trans. Inform. Theory 51
(2005), 2859–2866, DOI
[10.1109/TIT.2005.851748](https://doi.org/10.1109/TIT.2005.851748),
[eight-page author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.B (60)–(65), printed p.7, specifically the second matrix in (64).
Cross-check Hyun Kwang Kim and Phan Thanh Toan, *Improved Semidefinite
Programming Bound on Sizes of Codes*,
[arXiv:1212.3467v1](https://arxiv.org/pdf/1212.3467v1), 14 December 2012,
III.A Remark 11 and III.B (31)–(35), printed pp.8–9, specifically (33).
For nonempty binary constant-weight codes these are necessary PSD
constraints, without RS, field, linearity or design hypotheses.
The even-distance assumptions d>=4 and d<2w<=n hold for
n=1024,w=68,v=956,d=10. The distinct algebraic task is to evaluate an
invariant matrix; it does not assume that a code or measure exists.

Fresh primary reading covered both inclusion/exclusion outer-product
averages (60), triple normalization (62)–(63), both PSD families (64),
all scalar conditions (65), and the explanation retaining the triple
symmetric-difference invariant. Kim–Toan (31) explicitly assigns zero
to impossible multinomial orbits. Read its full (32)–(35), including
the ranges W_k={k,...,w-k}, V_l={l,...,v-l} and all four conditions.
The imported affine coefficient is p_(i+j-t-s)-y_ij^(t,s).
The suspect complement prefactor with 2^n in Schrijver (61) remains
unused and unrepaired, as in foundations/04. Equation (64), independently
restated by Kim–Toan (33), is the imported PSD statement.
Screenshot requests returned references only; no visual inspection or
new frozen local PDF is claimed. Readable formula text supplied these cases.

Reuse the primary mixed-layer coverage in foundations/09: Schrijver
(7), Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), printed
pp.2,5–7, with the complete tensor and extension/reset proof. This
algebra retains unequal layer indices and positive binomial rescalings.
Principal restriction to layers 0,5,6 is within both ground-set ranges
68 and 956. L063's canonical proof already records this geometry:
49 surviving modes, 36 with both shell coordinates and 13 with layer
six only; the anchor appears only in the constant mode. L116 independently
retains the same geometry for the present assignment. These established
counts are reused as checks, not newly derived here. No omitted mode
or separate normalization of each rectangle is licensed.

Rump, *Verification methods: Rigorous results using floating-point
arithmetic*, Acta Numerica 19 (2010), 287–449, DOI
[10.1017/S096249291000005X](https://doi.org/10.1017/S096249291000005X),
[corrected author PDF](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf),
§5.5 (5.16)–(5.17), author p.28, supplies enclosing expression arithmetic.
Reuse foundations/14 and the ready coupled-product assessment's inspected
scope: exact rational endpoints, signed sums, products and squares,
with possible dependency overestimation. No new root theorem is needed;
L112 already encloses one root. Division requires an interval excluding
zero. If positive shell pivots are established, use the retained
Brouwer–Haemers *Spectra of Graphs*,
[author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
Theorem 2.7.1(i), p.36, for the positive-pivot Schur congruence.
Complete minors or explicit range checks are required at zero pivots.
All these tools are imported without reproof. Full matching Mathlib
coverage and supporting rectangular/interval coverage remain not checked;
unknown coverage is not evidence of absence.

## Application comparison, duplicates and stops

Use exactly L021's canonical a_i and L098/L112's N and c_i, including
c_0=1, c_1=...=c_4=0 and all required c_i through c_12. Source p_i is
c_i, and source y is the normalized triple moment, as recorded in
L112–L116. For distinct permitted triples use only the existing distance
product; repetitions use their Boolean pair/singleton values. This is
an application contract, not an evaluation of the excluded-anchor matrix.

L063's previously proved dictionary cases explain the essential anchor
distinction: its five anchor layer cases vanish, while its shell diagonal
is 1-p_l; there is no positive-anchor Schur subtraction. The proposed
calculation must verify these same source identities with the current
Boolean data before deleting an anchor coordinate. It must not reuse
L116's included-anchor constant subtraction. Reanchoring preserves the
underlying unordered y, while the opposite pair and hence the affine
entry can change. Both facts are explicit in L063's proof and the source.
Preserve D, original t-s and every full six-presentation key.

The discovery recorded in the ready 2026-10-14 complemented assessment
already searched the exact method and stronger completion results.
The two fresh narrow queries listed above returned general coding/SDP
and stronger-hierarchy leads, without an inspected fixed-product verdict.
Those new broad leads were not read and are nonessential. Do not treat
search snippets as theorem evidence or infer novelty from this search.

ATTEMPTS/045 stops exclusion by this matrix only at L062's different
witness, whose fixed pairs and completed triples differ from this recipe.
L063's complete pass and critical audit are method precedent, not moment
or sign inputs. ATTEMPTS/094 stops only the included-anchor test at the
current recipe; history/437 and L116 retain its completed critical audit,
superseding historical pending-review wording. Neither stop is a global
ban or a duplicate of the present coefficient test. No full solve,
retuning, translated-pole route or exhausted earlier prescription is reopened.

## Approved calculation and continuation test

Essential inputs: L021,L098,L112,L113,L114,L115,L116 and
foundations/04,09,12,14. Reuse the retained joint root/capacity audit,
L114's consumed-input audit and the completed included-anchor audits.
Use L063 only for the already assessed source and normalization method;
do not import its witness or PSD verdict. Bind complete relevant evidence,
including exact N, canonical pairs and every original endpoint/scale,
before relying on it. A preview or summary count is not verification.

Reconstruct all 121 actual shell relations and 726 presentations already
identified by L116, both signed rectangular directions in one coherent
normalization, all surviving modes with multiplicities, null and forbidden
cases, Boolean diagonals, both endpoint repetitions and the coincident
anchor. Verify the entire zero anchor before deletion. Check each complete
affine block by enclosing arithmetic at the unchanged box, without an
included-anchor correction. Save complete certificates with actual and
required bounds, all failures and reproduction paths.

A complete whole-box PSD certificate parks this necessary matrix as an
exclusion diagnostic. A fixed direction with a rigorous negative bound
throughout the original box rejects its enclosed root's assignment as a
full-PSD witness. A negative midpoint, a failing sufficient interval test,
or one non-root point does not reject the root. An interval straddle is
inconclusive; stop and preserve it without refinement, solving, scanning
or retuning. Other layers, full source PSD, stronger distributions,
global root uniqueness, measures, packing, RS realization and arbitrary-
center safety at 67/68 agreements remain unresolved in every case.

RESEARCH / REPRODUCTION is approved for the exact unchanged TARGET.
This literature-only step establishes source coverage and no new lemma,
excluded-anchor coefficient evaluation, mathematical script or PSD verdict.
