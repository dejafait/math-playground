# Remaining active rank-19 loci — completed source comparison

TARGET: Classify the complete extension-field Plucker loci and L109 gate dispositions of the uncovered rank-19 occurrences in L118's 239 activity-screen failures, excluding L112's nine recorded overlaps and L119's (0,320).
CHECKED: 2026-10-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step-330/332 coding, exterior and stronger-result comparisons; read L109's complete necessary gates, L112's homogeneous/gcd cases, L118's selection and audit scope, L119's hypotheses and step-333 history, and ATTEMPTS/041–042. Nine focused external queries covered binary-quadratic common zeros, polynomial gcds, finite-field extensions, Grassmannian lines and exact RS/MCA rank terminology; queries, inspected results and unread leads are distinguished below.
SOURCE_EVIDENCE: Freshly read J. S. Milne, Fields and Galois Theory, Kea Books 2022, sections 1.6–1.9 pp. 5–7, Proposition 2.17 p. 34, Lemma 2.19 and Proposition 2.20 pp. 35–36, Corollary 4.22 and Proposition 4.23 pp. 66–67, https://www.jmilne.org/math/Books/FT0.pdf ; Magma Handbook V2.29 (3 August 2026), GCD/XGCD, https://magma.maths.usyd.edu.au/magma/handbook/text/234 , and Roots/RootsInSplittingField/FactorisationOverSplittingField, https://magma.maths.usyd.edu.au/magma/handbook/text/211 . Reused the saved primary Hall, shortening and Conrad extractions identified below.
COMPARISON: Standard polynomial gcd/extension and finite-field results cover the algebraic tools; L109 already supplies all necessary pivot, projection, weight and prescribed-chart gates. The new work is a finite, record-specific specialization with complete certificates, not a reproof of those tools. L112/L117/L119 do not transfer their st=0 coefficients or dispositions to other matrices; no inspected source supplies this indexed classification.
GAP: Reconstruct and certify the exact selected matrices/bases, all homogeneous restrictions and every component's necessary gate disposition. Whole-line, empty, split, repeated, nonsplit and infinity branches must be certified or saved explicitly unresolved. No census, new exclusion, survivor or field descent is established by this review.
REASON: Essential coverage is now adequate for the unchanged bounded classification target. SPECIALIZE approves source scope for a later invocation subject to the supervisor's separate gate check; it does not certify a local computation or imply a third/pair/global bound.

LITERATURE_REASON: The enlarged family was REVIEW_REQUIRED and its general binary-quadratic/whole-line scope was outside the approved single-occurrence audit; reuse unchanged coding/exterior coverage and assess only the added algebraic cases.
SCOPE: Exactly F_(97^20), fixed H, S={1,8,12,18,22,27,33}, k=8, L118 screen_failure records of rank 19, excluding recorded L112_exchanged_rows and index (0,320); sixteen actual original finite events, t=0, actual nonzero D/locators, arbitrary weights and prescribed possibly nonrational chart. L109 necessary direction only; inherited L010/L103/L104 finite-certificate qualifications remain.

## Completed review — step 334

The main gap remains sixteen versus fifteen, with global interval
11/q–16/q. The intermediate target is the unchanged TARGET above.
Complete residual loci could supply further necessary-support exclusions
or identify surviving components needing additional rows. Neither output
alone excludes a third, fixed pair or arbitrary t=0 profile. Universal
representation/extraction and challenge-definition qualifications remain
independent gaps.

This is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION, actual task
literature_comparison. The advance in preparation is adequate source
coverage, not a mathematical result beyond those sources. No mathematical
exploration turn is spent. No lemma, mathematical script, certificate,
PROOF.md or DAG.md is changed.

## Primary algebra coverage and specialization boundary

[Milne's 2022 book](https://www.jmilne.org/math/Books/FT0.pdf): read the
statements and full relevant proofs at printed pp. 5–7, 34–36, 66–67
(PDF pages 15–17, 44–46, 76–77). Sections 1.6–1.9 give division,
root bounds and extended Euclid; Proposition 2.17 makes polynomial gcds
unchanged under arbitrary field extension. Its proof uses divisibility
and a Bezout identity. Lemma 2.19 detects multiple roots by derivatives;
Proposition 2.20 treats inseparability. Corollary 4.22 and Proposition
4.23 give splitting and subfield criteria, including the proof's
degree-divisibility directions. Here coefficients are in F_97. An
irreducible quadratic's roots belong to F_(97^20) by Corollary 4.22
with d=2 and n=20; absence of prime-field roots is insufficient.
Import these standard results rather than reprove them. They determine
no coefficients or gates of a selected kernel.

[Magma GCD documentation](https://magma.maths.usyd.edu.au/magma/handbook/text/234),
V2.29, 3 August 2026: read GCD's zero-input conventions and XGCD's
field hypothesis, monic output and polynomial identity. These specify
possible certificate formats, not a requirement to use Magma.
[Finite-field roots documentation](https://magma.maths.usyd.edu.au/magma/handbook/text/211),
same version, distinguishes Roots in the coefficient field, with
multiplicities, from RootsInSplittingField and
FactorisationOverSplittingField in a returned minimal splitting field.
Read the complete H22E3 example, including its returned field and all-root
evaluation check. A base-field Roots call is not an extension exclusion.
No local Magma installation, licence, runtime bound or black-box
verification is asserted.

For later specialization, restrict L109's 35 homogeneous equations to
the complete two-vector kernel. Retain all coefficient triples. Use the
affine chart s=1 with exact gcd/divisibility/Bezout certificates and
check [0:1] directly in the homogeneous system. Treat an identically
zero system separately; a zero gcd is not an empty locus. Preserve
factor multiplicities while distinguishing points from multiplicities.
These are approved proof obligations applying the cited tools, not
identities computed or a new general solver proved in this source turn.

For each finite component or whole-line branch use L109's existing
nonzero-pivot reconstruction, covering every nonzero Plucker pivot and
every possible nonzero row-projection pivot. Its formulas already
specify rank zero, rank one, lambda zero, both canceled overlap weights
and the prescribed finite-direction gate. A later certificate must
retain the domains of all divisions and all eight original shifted
moments. On a whole line, prime-field point sampling is insufficient:
give complete chartwise conditions and exact identities, or record
the specific unresolved component and stop the bounded attempt.
No new universal implication about whole-line gates is imported here.
An intrinsic gate survivor remains only a necessary four-row survivor;
the original chart cannot be replaced by a newly convenient chart.

## Reused coding/exterior and stronger-result coverage

Read the saved primary extractions, not a new retrieval:
`2026-10-05-two-block-moment-obstruction.md`, “Primary theorem and
applicability”; `2026-10-07-six-coordinate-triple-equality-obstruction.md`,
“Primary shortening input”; and
`2026-10-18-residual-kernel-inactive-coordinate-review.md`, “Primary
coverage and exact specialization boundaries.” Hall, Notes on Coding
Theory, Theorem 5.1.1, printed pp. 63–64,
https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf ,
allows any field, distinct labels, nonzero multipliers and 0<k<=n.
The sixteen labels and unit multipliers at k=8 satisfy these conditions.
Marquez-Corbella–Pellikaan, FFAA 40 (2016), 224–245,
DOI 10.1016/j.ffa.2016.04.004, accepted manuscript 2016-02-29,
section 5 pp. 7–8, Definitions 5.1–5.2 and the GRS formula following
Lemma 5.3, https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf ,
covers each successive single-coordinate shortening. Seven distinct
labels J minus K are shortened, leaving positive dimension one and
nonzero retained label products. Do not substitute the MDS parameter
lemma outside its own stated range. No changed coding hypothesis or
general shortening reproof is needed.

Conrad, Exterior Powers, undated author PDF inspected October 18,
Theorems 4.2, 7.1, 7.5 and complete proofs pp. 11–12, 23–25,
https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf ,
covers exterior coordinates and the wedge-plane association over the
base field and extensions. L109 supplies the actual homogeneous
criterion and necessary gates, whose proof was read here through its
full chart/converse qualification. Only the necessary direction is
used; four selected rows do not meet its r>=6 converse hypothesis.

Reuse `2026-10-17-seven-coordinate-syndrome-bound-review.md` and
`2026-10-18-first-active-residual-gate-review.md`: inspected BCHKS
Theorems 1.3/4.6 do not supply the required count in this cell, and
Chojecki v9.2's inspected support-confinement statements require a
different hypothesis from coefficient-syndrome membership. The enlarged
record family does not change those comparisons. No freshness claim
for their mutable URLs is made. The saved Stacks/Magma ideal assessment
in `2026-10-18-fixed-pair-remaining-third-gates-review.md` remains an
optional tool reference; a proper ideal alone gives no prescribed-field
point. Full matching Mathlib coverage remains not checked, not absent.

## Exact selection, duplicates and failures

Read L118's domain, complete-basis and overlap passages, its separate
step-329 audit scope, and the source selector in
`scripts/seven-coordinate/inactive_coordinate_screen.py`. Inspect the
complete saved `/summary` and `/records/0` values with the JSON inspector;
these are provenance reads, not a fresh certificate replay. The first
record is excluded (0,279), illustrating why array position is not the
historical occurrence index. The saved summary records 599 occurrences,
360 omission passes and 239 failures, with nine L112 overlaps among the
failures; it supplies no count of the new rank-filtered target.

Select `/records` by `status == screen_failure`, `rank == 19`, absence
of `L112_exchanged_rows` in `prior_exclusions`, and
`(third_index,fourth_index) != (0,320)`. Preserve the original order
and indices, even for repeated kernels. Rank-20 records are outside
this target. Bind the master and shards to L118/L116 audited provenance;
reconstruct original matrices and complete bases before interpreting
their loci. The future count and full selected-index comparison are
implementation obligations, not calculations performed here.

L112's nine recorded exchanged-row overlaps are already exclusions;
its projective-line proof and exact gcd certificate were read, but its
st=0 shape is not transferred. L119's step-333 exclusion covers only
(0,320); L117's (0,279) is an omission pass and outside the selector.
The scoped October 18–19 assessment/history search found no completed
classification for the exact selected target. This is not evidence of
originality. ATTEMPTS/041–042 refute rank-only and label-1-only
extrapolations; neither stops a complete homogeneous/gated test.

## Search record and unread leads

Fresh queries, 2026-10-19:

- `homogeneous binary polynomials common zeros gcd projective line quadratic Plucker pencil decomposable bivectors`
- `site.magma.maths.usyd.edu.au handbook greatest common divisor polynomials extended finite fields factorisation`
- `site.jmilne.org Fields Galois Theory finite fields subfields degree divides`
- `"Reed Solomon" "Plucker" "rank 19"`
- `"binary quadratics" "common zeros" gcd`
- `site.magma.maths.usyd.edu.au/magma/handbook "FactorisationOverSplittingField" "Roots"`
- `"line" "Grassmannian" "quadrics" "finite field" Plucker intersection`
- `"Reed-Solomon" "seven" "Plücker"`
- `"mutual correlated agreement" "rank" exterior`

The inspected primary algebra sources are recorded above. General
Grassmannian snippets, nonprimary mirrors and unrelated geometry were
not used as theorem evidence. A new lead was Jo, ePrint 2026/1432,
[Reed–Solomon Mutual Correlated Agreement Beyond the Johnson Radius](https://eprint.iacr.org/2026/1432),
landing page revised 2026-08-19. Only its metadata/abstract were read;
the linked PDF returned 403. Its theorem hypotheses/proofs remain
unread and no result is imported or ruled out from that abstract.
This optional broader lead is not essential to the standard algebra
or exact local gate classification; it is not a persistent blocker
of this target. ABF26 likewise remains unread and unimported.

## Continuation/abandonment test

After separate gate approval, one bounded mathematical attempt should
produce the complete selected manifest and locus/gate dispositions,
or stop with a concrete unresolved algebraic branch. Continue if new
necessary exclusions or explicit surviving components change the next
research decision. Stop on completion or the first genuinely unresolved
branch rather than enlarging the census or repeating a failed screen.
Preserve zero weights, successful rows, extension roots and arbitrary
original charts. Do not claim a third/pair exclusion, a four-row converse,
universal seed extraction, a global bound improvement or a challenge
resolution. The unchanged TARGET is ready in source scope only.

## Original step-333 proposal (preserved)

The main gap is still sixteen versus fifteen, with interval 11/q–16/q.
The intermediate target would make the two-dimensional residual kernels
reliable inputs for later necessary-support assembly. It seeks complete
loci and gate dispositions rather than demanding an exclusion. Other
kernel dimensions, arbitrary t=0, universal representation/fixed-pair
extraction and challenge qualifications remain unresolved independently.

Use exactly F_(97^20), H, k=8 and
S={1,8,12,18,22,27,33}, with sixteen actual original finite events,
t=0 and actual nonzero D/locators. Weights and the prescribed chart may
be nonrational. Essential inputs are L109's independent nonzero wedge,
homogeneous criterion and necessary projection/lambda/weight/chart
gates, and the audited L118/L116 frozen occurrence records for exact
selection and indexing. L112's recorded nine overlaps and L119's
(0,320) are already covered and must be distinguished from new work.
Retain L010/L103/L104 computational qualifications inherited through
L109. No L086 extraction or four-row converse is needed for named
support-family exclusions; no third or fixed-pair conclusion is proposed.

The selected rank-19 list has not been inspected or counted in this
turn. Select from the existing 239 failures and verify original ranks
and complete bases in any later approved attempt, preserving the whole
historical 599/239 records. Do not assume that every selected kernel has
two decomposable points or that its first row fails. Whole projective
lines, irreducible homogeneous factors, repeated points, infinity, rank
zero, zero lambda, canceled weights and prescribed finite directions
all need explicit coverage. The binary-equation classification and its
extension-field interpretation require source comparison, not an
unrecorded assumption based on L119's example.

ATTEMPTS/041–042 already rule out uniform rank-only and label-1-only
extrapolation. The proposed method must use complete homogeneous loci
and all necessary row gates, rather than repeat either screen. Continue
if it gives a complete classification with new exclusions or explicit
surviving components that change the next research decision. Stop this
bounded classification on completion or a specific unresolved algebraic
branch; preserve failures and do not infer a global count or recursively
exclude a third. No mathematical exploration attempt is spent by this
proposal. Its next invocation is literature_comparison, not calculation.
