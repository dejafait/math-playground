# Normal-closure P3 and omitted-ell height — proposed scope

TARGET: Transfer L101's P3 control to the same normal closure, testing h_w<4sqrt(H) for every w|ell and the normalized omitted-ell contribution <sqrt(H)log(ell).
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step407 searched the two step398/399 assessments, L092/L100/L101 and ATTEMPTS/035 for P3, omitted-ell terms and duplicates; external queries `"Mochizuki" "P3" "height" "Corollary 2.2"` and `"elliptic" "local heights" "base change" "ramification"` found no inspected matching transfer theorem. General theorem coverage is reused; no originality inferred.
SOURCE_EVIDENCE: Fresh April 2020 IV reproduction, 87 pages, Corollary 2.2(ii) proof printed pp.44–47, especially P3 p.45, P5 p.46 and the first omitted-ell display p.47; reused GenEll Definition 3.3/Remark 3.3.1 p.17 and Milne ANT v3.08 Theorem 3.34 pp.59–60, Corollary 7.42/Remark 7.43 p.124, Exercise 4-2/solution pp.83,155 from step399. Milne version freshly confirmed; no new general theorem reproof.
COMPARISON: Source P3 concerns G_o; its omitted-ell use has a one-sixth normalization. General local-height and completion-degree inputs cover finite extensions including residue characteristic ell and nonnormal G_o. The factor-four local test and invariant normalized weighted sum remain a later specialization, not a quoted theorem.
GAP: Essential coverage is ready; a research turn must verify the actual relative completion degrees, height scaling and all-place weighted assembly for the same selected prime and fixed downstairs H. No transfer is proved here.
REASON: The new omitted-ell passage and existing general theorems suffice for this bounded specialization; import those theorems and prove only their same-member applicability and the stated bounds.
LITERATURE_REASON: The continuation changes from simultaneous selection and P2 transfer to quantitative P3 transfer and an essential comparison with the source's omitted-ell height term.
SCOPE: One L101 member and ordering, the same selected ell>=7, F=G_o, C_o=G_o^nor, and H computed over G_o; no common prime for orderings, integrality assumption, P4–P7 or complete repair.

The main gap remains original finite B>=A. The intermediate target is
quantitative control of the omitted ell contribution after normal
closure. A passing bound could support the source's treatment of an
ell-pole without first requiring that pole to be absent. It would
not establish native selected support or complete a field repair.

Essential inputs are L089,L090,L092,L100,L101. Keep the fixed family,
domains and closure, d=6, epsilon_d=1, full-coordinate literal field,
the same curve E_o and prime ell, and the April reproduction/def=
qualifications. For each F in {G_o,C_o}, the quantity to compare is

    H_ell(F)=(1/[F:Q]) sum_(x|ell) h_x f_x log(ell),

using every actual finite place over ell and its residue degree.
H in TARGET always means L101's total downstairs height. The local
factor-four threshold and the normalized threshold are proposed
tests; neither is derived or approved in this document.

First reuse the source readings in
`2026-10-22-height-selected-prime-avoidance-comparison.md` and the
local theorem coverage in
`2026-10-22-literal-to-normal-closure-selected-prime-transfer.md`.
Compare the exact source omitted-ell estimate and its field/height
normalization, then determine whether the general completion-degree
and height formulas cover this transfer. Retrieve only an essential
missing passage; do not repeat ATTEMPTS/035's authentication route.
Distinguish this bounded test from changing the selected prime or
asserting the source's entire construction for C_o.

Continue only with complete source coverage for the proposed local
and normalized bounds. A changed normalization, missing source
hypothesis or larger required term calls for a precise limitation
or corrected target, not silent retention of P3 over the changed
field. Full Mathlib coverage is unchecked. Ell-integrality/native
support, L092's relative degree excess, exact generation/complete
repair, P4–P7, native input/action/factorization/pilot, essentiality
and finite B>=A remain independent unresolved obligations.

## Completed source comparison — step407, 2026-10-23

The proposed-scope paragraphs above preserve the pre-review test. This
completion supersedes their pending-coverage language; it approves only
the identical TARGET for a subsequent research invocation.

### Essential source passage and qualifications

The [April 2020 IV reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf#page=47),
Corollary 2.2(ii) proof, printed p.47, first display, uses

    (1/6) log(q^{not-dividing-2}) - (1/6) log(q)
      <= (1/6) sqrt(H) log(ell).

P3 is printed on p.45; P5 and its nonemptiness argument are on p.46.
The height sum on p.44 is normalized over F before adjoining ell-torsion.
The p.47 display concerns the omitted ell term after excluding two.
It is not a claim that the curve is good at ell. Its subsequent
inequalities use P1; they do not assert transfer to a changed field.
This reading retains the reproduction/def= boundary; author/journal
authentication remains unresolved and ATTEMPTS/035 is not reopened.
The glyph in q^{not-dividing-2} denotes omission of dyadic places.
No source-normalized pilot is defined for C_o by this review.

Text extraction was inspected across pp.44–47. Web screenshot requests
returned references without usable image content. Optional local raster
extraction failed (PyMuPDF unavailable; shell download DNS unavailable).
No visual verification is claimed. The relevant text distinguishes the
one-sixth coefficients and the pre-ell-division height. These extraction
limits do not remove the reused source-version qualification.

### General imports and applicability comparison

Reuse the exact statements and relevant cases recorded in
`2026-10-22-literal-to-normal-closure-selected-prime-transfer.md`,
Primary statements and Applicability obligations:

- [GenEll, Math. J. Okayama Univ. 52 (2010)](https://www.math.okayama-u.ac.jp/mjou/mjou52/_01_mochizuki.pdf#page=17),
  Definition 3.3/Remark 3.3.1, p.17: integer valuation downstairs,
  with split-extension Tate order divided by ramification index.
  The nonsplit case is included. L100's separately audited proof
  identifies this height at every actual completion of both fields.
- [Milne, ANT v3.08, 19 July 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
  Theorem 3.34 and full Galois proof pp.59–60: for a number-field
  extension and a fixed base prime, sum of relative e*f is the
  field degree; Galois equality of individual indices needs normality.
  Corollary 7.42/Remark 7.43 p.124 and Exercise 4-2/solution pp.83,155
  cover local degree e*f and valuation/ramification restriction.
  The same formulas apply to C_o/G_o and each actual extending place;
  no tameness or exclusion of residue characteristic ell is required.

L092 supplies the actual global degrees, and L100/L101 supply the
same curve, local-height convention and strict downstairs P3. These
are adequate existing inputs; the target is not a duplicate conclusion
of any of them. No general base-change theorem needs reproof. The
later proof must explicitly specialize the imports to this tower.
It must bound each local extension using the actual relative global
degree, rather than assume equal local indices over nonnormal G_o.
For H_ell it must regroup all actual places above each downstairs
place with relative residue degrees. A pointwise factor-four estimate
alone is not a proof of the requested normalized threshold. Treat
zero heights separately so strictness is not lost. H remains the
original downstairs total; do not reselect ell or replace H by a
height over an ell-division field.

### Decision and bounded continuation

SPECIALIZE is appropriate: the missing work is the indicated finite
tower and weighted-sum specialization of known results. It will be
REPRODUCTION, not progress beyond the sources checked. The source's
one-sixth coefficient must be retained if comparing with its omitted
term; controlling H_ell(C_o) alone does not construct that native term
or validate a repaired application of Theorem 1.10.

Continue with exactly TARGET if the actual completions and full
weights give both proposed strict bounds. On a failed normalization
or degree hypothesis, record a limitation rather than substitute a
larger bound silently. Main gap, downstream use and unresolved inputs
are as stated in the preserved scope: L089,L090,L092,L100,L101, one
member/order/prime, same fixed family and closure. Native support,
ell-integrality, P4–P7, relative degree excess, complete repair and
essentiality remain independent. Full Mathlib coverage is unchecked;
search hits about a formalization are unread leads, not imports.
No lemma, mathematical script, DAG edge or argument change is made.
