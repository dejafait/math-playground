# Disjoint d-tag exclusion — completed audit coverage

TARGET: Critically audit L049's uniform disjoint-d exclusion, including subgroup normalization, complete cubic grouping and independent certificate verification.
CHECKED: 2026-10-08
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused completed simultaneous-count discovery and same-d audit coverage; read L049 fully, L043 hypotheses and (4)–(10), L048 full-moment and scoped audit passages, histories 106–107 and ATTEMPTS/021–022; three narrow ratio-class/split-cubic queries produced no inspected matching theorem, as detailed below.
SOURCE_EVIDENCE: Reused inspected Chojecki v9.2 DR2/DR6–DRC, source lines 2785–2935, from the saved fourth-support extraction, and the primary Mathlib factor/root coverage recorded in the same-d audit assessment; no fresh primary theorem extraction or certificate verification was performed.
COMPARISON: Known recurrence tests cover all-eight-moment membership; audited L048 supplies the necessary cubic evaluations, distinctness and same-d intersection bound. Neither those inputs nor the inspected design theorems certify L049's fixed-H ratio-class grouping or computational completeness. No exact import was established.
GAP: Independently validate the passage to three distinct cubics, subgroup scaling, d-ignored overapproximation, complete key partition and every pair test; inspect and replay both implementations and full certificates before certifying L049.
REASON: Ingredient coverage and bounded comparison suffice for one separate critical audit of this unchanged target; approval concerns coverage, not the correctness or originality of L049.
SCOPE: F=F_(97^20), fixed order-sixteen H in F_97^*, k=8, pinned cell, gated tau=1 triple; two distinct d-tagged nonuniversal candidates satisfying every L043 (4)–(7) gate before (9), arbitrary extension-field weights and original finite chart, mu,nu!=0,-1 and E(mu),E(nu)!=0.
LITERATURE_REASON: The newly proposed L049 audit requires comparing its fixed-H three-cubic ratio obstruction and complete certificates; the ready counting and L048 audit assessments did not approve this separate critical-review scope.

## Gap, target and downstream use

Eleven and both twelve profiles remain open in the current local count
argument; arbitrary-support extraction and ABF26 identification are
independent challenge gaps. The intermediate target is certification or
repair of L049's stated fixed-H disjoint-d exclusion. A clean audit would
justify using its combination with audited L048 to restrict any existing
pair of d-tagged candidates to the W-intersection case. It would not force
such a pair, exclude that surviving case, or establish eleven.

The pending assessment supplied at startup was REVIEW_REQUIRED. This
separate literature step approves the same exact audit target. It does
not reject the preceding research step or derive or certify its mathematics.

## Reused primary results and applicability

Przemek Chojecki, *Shortening Bounds for Reed–Solomon MCA*, live author
TeX v9.2, July 17, 2026, source lines 2785–2935,
`drc:lem-locator-recurrence` (DR2) and `drc:thm-exact-compiler` (DR6–DRC),
[author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex).
Reuse the hypotheses, full proofs and zero-direction cases inspected on
2026-10-08 and extracted in
`2026-10-08-nine-union-fourth-support-incidence.md`, Primary recurrence
input and applicability. No fresh retrieval or identity with ePrint
2026/1463 is asserted; the live source is mutable.

For distinct weighted Vandermonde columns with nonzero multipliers and
t<R, span membership is equivalent to the R-t locator recurrences. The
fixed-pair compiler distinguishes zero projected direction from finite
transverse intersection. The saved specialization uses R=8,t=4,
eta_j=s_(j+1), j=0,...,7, and multipliers x in H, hence nonzero. It
permits arbitrary F-valued moments. This covers L043's full-moment input,
not simultaneous splitting or nonzero recovered weights. No reproof is
needed; L048's scoped audit independently checks its essential five-value
and same-d L046 uses. The remaining L046 assertions are not premises.

Reuse the primary supporting Mathlib inspections in
`2026-10-08-same-d-single-intersection-critical-audit.md`:
[Div.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Polynomial/Div.lean#L566),
`Polynomial.mul_divByMonic_eq_iff_isRoot` and `Polynomial.dvd_iff_isRoot`,
lines 566–576 under `[CommRing R]`;
[Roots.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Polynomial/Roots.lean#L65),
`Polynomial.card_roots`, `Polynomial.card_roots'`, `Polynomial.mem_roots`
and `Polynomial.card_le_degree_of_subset_roots`, lines 65–74, 98–99,
121–123 under `[CommRing R] [IsDomain R]`, retaining nonzero-polynomial
premises. F satisfies these hypotheses. These support the audited L048
input; they do not certify the finite ratio partition. Mutable master was
inspected previously, without a pinned commit or Lean compilation.
Full matching Mathlib coverage for L049 remains not checked, with no
absence claim. Ordinary field/group arithmetic in the normalization is
an audit obligation, not a new theorem imported or proved this turn.

## Comparison, discovery and preserved failures

Reuse `2026-10-08-nine-union-simultaneous-recovery-count.md`:
Guruswami–Kopparty, *Explicit Subspace Designs*, March 2013 author
manuscript, section 4.2 Theorem 14 and Claims 15–16, pp. 9–10, requires
structured disjoint root blocks. Goyal–Guruswami–Sun–Wootters,
arXiv:2607.08516v1, Theorem 3.27(1) requires an established design
inequality; Theorem 5.6 uses random evaluation points. Their recorded
hypotheses and proof comparisons do not match this fixed-H relaxed
three-cubic test. No new specialization of those theorems is proposed.

Fresh queries on 2026-10-08 were:
- `"Reed-Solomon" "cubic" "ratio" "support"`
- `"mutual correlated agreement" "97" "sixteen"`
- `"split cubics" "evaluation" "disjoint" finite field`

Returned material concerned watermarking, general GRS notes, plane-curve
splitting and unrelated computational research. None was read as matching
theorem coverage or used as a mathematical premise. There is no new
inspected primary theorem from these queries, and no novelty inference
from their failure. Reusable primary coverage above is the basis for
readiness. ABF26 and previously blocked nonessential leads stay parked.
No cross-notebook mathematical input is used.

L043 classifies individual recoveries; L048 bounds intersections but
leaves disjoint outside triples open. L016's count is label-specific.
Neither L044 descent, L045 profiles nor a full L046 audit is required for
L049's stated reduction. ATTEMPTS/022 rules out isolated degree summation,
and ATTEMPTS/021 preserves a support-only witness. This audit checks a
simultaneous, field-labeled moment obstruction and does not reopen either
exhausted counting mechanism. Histories 106–107 distinguish the audited
input from the newly unaudited certificate result.

## Ready audit and decision test

Read L049's complete reduction; the relevant L048 full-moment and audit
passages; and L043's exact gates. Use L010 and audited L041–L042 for setup
as needed. Check every implication independently, including nonzero
values, three distinct cubics and the excluded mu=-1 case. Verify that
scaling by h preserves the necessary ratios and intersections without
asserting chart descent, and that unordered pairs retain both y/z roles.
Check that ignoring d enlarges rather than restricts the search space.

Inspect `scripts/simultaneous-recovery/disjoint_d_pair.py` and
`verify_disjoint_d_pair.py`, and the complete `disjoint-d-pair-result.json`
and `disjoint-d-pair-verification.json` in that directory. Replay them
sequentially. Require exact choice coverage, all cubic memberships,
nonzero denominators, unique keys and exhaustive pairs in every group of
size at least three. L049 reports 8190 choices, 1351350 memberships and
38220 such pairs; these are audit targets, not newly verified evidence.
Its candidate-filtered zero counter alone is insufficient. Bounded JSON
previews and documentation validation cannot certify the full computation.

Continue if reduction, completeness and independent checks validate the
stated exclusion; repair or localize any defect and withhold unsupported
conclusions. A surviving disjoint pair invalidates this overapproximation
certificate and requires renewed actual-gate analysis, not a claimed
counterexample to MCA. Failure to justify a load-bearing reduction blocks
certification. A clean audit still leaves existence of two d-tags, their
W-intersection, other tags, B-disjoint candidates, eleven, full L044–L046
audits, universal lift/extraction and ABF26 unresolved.

No lemma or mathematical script was modified or executed. No new result
was derived. Mathematical exploration usage stays zero; the completed
literature step is EXPLORATION / NOVELTY_UNCHECKED, not a mathematical
advance or a fresh verification of the certificate.
