# Same-d single-intersection restriction — completed audit coverage

TARGET: Critically audit L048's same-d-tag single-intersection restriction, quadratic identities and actual-support qualifications.
CHECKED: 2026-10-08
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused completed simultaneous-count discovery; read L048 and L046 in full, L043's hypotheses, recovery and scoped audit, L010's kernel proof, L047's disjoint-candidate hypotheses and ATTEMPTS/022; two fresh narrow coupling queries yielded no inspected matching theorem.
SOURCE_EVIDENCE: Reused inspected Chojecki v9.2 DR2/DR6–DRC, source lines 2785–2935, through the saved fourth-support assessment; freshly read Mathlib Polynomial.division factor-theorem and Roots root-bound statements and proofs with their ring/domain hypotheses, exact names and URLs below.
COMPARISON: Recurrence coverage supplies full-moment membership and finite transverse recovery; standard polynomial results cover factorization and root bounds over F. Neither covers L048's simultaneous identities. L046 excludes same-d double intersections, and L047 assumes a B-disjoint candidate. No exact import or stronger applicable conclusion was established.
GAP: Independently verify L048's normalized cubic signs, nonzero differences, four-evaluation W identity, residual coprimality and actual-support qualification, including its essential unaudited L046 uses.
REASON: Essential ingredient coverage is adequate for one separate scoped proof audit of the unchanged TARGET; the simultaneous coupling still requires direct verification and no novelty or count improvement is certified.
SCOPE: F=F_(97^20), H order sixteen in F_97^*, k=8, pinned cell, gated tau=1 pattern (2,2,3), arbitrary extension-field weights and original chart; two distinct d-tagged nonuniversal finite candidates satisfying every L043 (4)–(7) gate before (9), with mu,nu!=0,-1 and E(mu),E(nu)!=0.
LITERATURE_REASON: The newly proposed dedicated L048 audit needs comparison of its simultaneous coupling and essential L046 uses; the ready counting assessment did not approve this separate critical-review target.

The main count gap remains eleven rather than twelve. The approved audit
would validate or repair only a conditional input: two d-tagged recoveries
sharing one outside label must share a w-label, with all three residual
pairs disjoint. It must not assume that such candidates exist or intersect,
that the original chart is rational, or that relaxed witnesses have full
weights. The actual union-nine conclusion uses full weights explicitly.

## Primary ingredients and applicability

Reuse the primary extraction in
`2026-10-08-nine-union-fourth-support-incidence.md`, “Primary recurrence
input and applicability”: Przemek Chojecki, *Shortening Bounds for
Reed–Solomon MCA*, live author TeX v9.2, July 17, 2026, source lines
2785–2935, `drc:lem-locator-recurrence` (DR2) and
`drc:thm-exact-compiler` (DR6–DRC), both proofs and zero-direction cases
previously inspected on 2026-10-08
([author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex)).
No fresh retrieval of that mutable source or identity with ePrint
2026/1463 is claimed. Distinct weighted Vandermonde columns, nonzero
multipliers, redundancy R=8 and support size t=4<R give the fixed-support
recurrence test. Shifted moments eta_j=s_(j+1) and multipliers x in H
are exactly the saved specialization; arbitrary F-valued moments are
allowed. The compiler treats zero projected direction separately and
does not establish simultaneous support restrictions or nonzero recovered
weights. No reproof of either source result is needed for this audit.

Read L043's complete (4)–(10) criterion, missing-column recovery and
separate critical-audit passages. These distinguish all-eight-moment
membership after (7) from recovery using four moments, and separate (9)'s
nonzero-weight gate from the relaxed candidate. L010's kernel identity
was read in its full proof: its domain is an order-sixteen multiplicative
subgroup and its moments are indexed 1 through 8. These unchanged
hypotheses fit L046's polynomial lift. L046 was read in full to determine
the exact scope of its five-evaluation equations and coincident/double
intersection cases; reading is not a critical certification of those
claims. Their essential uses must be checked independently next turn.

Fresh primary polynomial coverage, inspected 2026-10-08, is the mutable
Mathlib master source, with no pinned commit or local Lean compilation:

- [Mathlib/Algebra/Polynomial/Div.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Polynomial/Div.lean#L548),
  `Polynomial.mul_divByMonic_eq_iff_isRoot` and
  `Polynomial.dvd_iff_isRoot`, statements and proofs at source lines
  566–576 under `[CommRing R]`: a root a is equivalent to divisibility
  by X-C a.
- [Mathlib/Algebra/Polynomial/Roots.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Polynomial/Roots.lean#L44),
  `Polynomial.card_roots`, `Polynomial.card_roots'`,
  `Polynomial.mem_roots` and `Polynomial.card_le_degree_of_subset_roots`,
  statements and proofs at lines 65–74, 98–99 and 121–123 under
  `[CommRing R] [IsDomain R]`. These give the root-count ingredients,
  retaining the nonzero-polynomial premise for membership/degree.

F is a field and satisfies both sets of hypotheses. These are supporting
results for the already written factor/root arguments, not a matching
Mathlib theorem for L048. No full-result coverage or absence claim is
made. This source review does not establish L048's degree bounds,
nonvanishing premises, algebraic identities or full-weight conclusion;
those are the next audit's obligations. Import these standard ingredients
by citation rather than inventing a decoder or root-bound reproof.

## Duplicates, bounded discovery and failures

Reuse `2026-10-08-nine-union-simultaneous-recovery-count.md` in full,
including its final continuation test. Guruswami–Kopparty Theorem 14
and Claims 15–16 require structured disjoint blocks; the inspected
Goyal–Guruswami–Sun–Wootters Theorem 3.27(1) needs an established design
inequality and Theorem 5.6 uses random evaluation points. Those comparisons
give no import for the present fixed H and relaxed recovery systems.
L016's fixed-label count is not used. L043 supplies individual-support
recovery; L046 does not locate a single shared outside label in W;
L047's hypotheses require a candidate avoiding B and thus do not match
the present two d-tagged candidates. L045 is motivation only; neither
its twelve profiles nor L044 descent is required here.

Fresh queries were `"Reed-Solomon" "cubic" "shared" "support" MCA`
and `"Reed-Solomon" "same" "intersection" "quadratic" correlated agreement`.
Results included general proximity/list-decoding metadata, agreement
hypergraph material, unrelated implementations and secondary summaries.
They were not inspected as theorem coverage and establish no exact
coupling import; failed searches are not evidence of originality.
ABF26 and the saved nonessential source blockers remain parked and give
no premise for this model-only audit. No cross-notebook input is used.

ATTEMPTS/022 was read completely. Isolated cubic degrees reproduce the
existing per-coordinate capacities and allow both twelve profiles. A
scoped audit of simultaneous equations does not reopen that exhausted
isolated-degree count. The earlier support-only stops remain preserved.

## Ready audit and decision tests

L048 was read in full. Coverage is now approved separately from its
derivation; the proof itself is still unaudited. L046's full audit remains
outstanding, and checking its essential same-d uses will not certify its
other tag/cross-ratio conclusions or L045. No mathematical proof, lemma
or script was changed during this literature-only review.

Continue to one independently performed proof audit. Its discriminating
checks are the signs of the normalized
cubic differences, their nonvanishing and degree-three factorizations,
the four-evaluation W identity, and the mu+1/nu+1 factors in residual
coprimality. Check L046's nonzero polynomial lift before its five
evaluations and its same-d coincident and double-intersection exclusions.
Retain original finite parameters, every quotient gate, zero recovered
weights and the distinction between a witnessing set and an actual
full-weight support. The actual recentering additionally requires both
recovered words to be full; neither their fullness nor existence or
intersection of two d-tagged candidates may be assumed globally.
A defect should be repaired or localized with its exact effect on the
conclusion; if an essential implication cannot be justified, withhold
that conclusion rather than certify the audit. A clean scoped audit
would leave the eleven
bound, disjoint same-d case, other tag pairings and challenge gap open.
The 11/q–16/q interval, independent full L044–L046 audits, universal
extraction, other local patterns and ABF26 identification remain open.
This is completed literature exploration and audit-scope approval, not
new mathematics or an independent proof audit. Mathematical exploration
usage is unchanged.
