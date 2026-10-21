# Quotient and lifting — critical-audit source coverage

TARGET: Critically audit L107's invariant quotient, genus 38 and normalized square-class −3 lifting criterion, including every boundary fiber.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the construction and L106 audit assessments; read full L107 and targeted quotient attempt/history and ATTEMPTS/045–046; narrowly searched Stacks for the boundary étaleness criterion and inspected primary passages below.
SOURCE_EVIDENCE: Reuse Stacks 03BM, 09DU, 0BY6, 03AG and Milne LEC v2.21 Theorems 3.1/21.3 pp.27,130–131 from prior assessments; reinspected Stacks 0BY1 statement/proof, 0C1B differential calculation and Lemmas 53.12.1–4, 03PK Lemma 59.28.1/proof and following exact sequence, and 09EV statement/full proof on 2026-10-20.
COMPARISON: The primary results cover invariant-field/proper-model, tame-cover/genus and quadratic-unit lifting methods; none certifies L107's explicit invariant ring, ordered-return data, boundary parity or residue algebras without an independent specialization audit.
GAP: No essential source gap remains for the bounded audit; full mathematical verification of L107 and independent replay of every load-bearing certificate record remain undone.
REASON: Approve the changed audit scope using reusable coverage and explicit boundary source comparison; this review approves methods, not the correctness of L107 or its claimed genus/lifts.
SCOPE: Exactly TARGET using audited L106, including invariant scheme/fixed field, constants, proper normalization, complete branch action, boundary freeness, normalized residue algebras and uniformizer independence; no rational-point enumeration, other quadratic field or L095 integer elimination.
LITERATURE_REASON: The newly selected critical audit was REVIEW_REQUIRED; its boundary and scheme obligations required separate comparison with the already inspected construction coverage.

## Gap, use and continuation test

The main gap remains primitive integer elimination in both L095 systems
and compatibility of the remaining global factors, within the unresolved
Beal target. The intermediate target is independent verification of L107.
Reliable quotient geometry and reversible lifting could support a later
rational-point method; neither genus nor source readiness proves emptiness.

Continue after a complete audit of the invariant scheme, constants,
normalization, branch lifts and every normalized boundary residue-algebra
case, with full arithmetic replay. Localize and repair or qualify any
failure before using the affected conclusion. A genus cross-check alone
is insufficient. Boundary points retain only the proper-cover meaning;
disjoint quadratic factors are asserted only on the distinct-root open.

## Primary hypotheses, cases and reuse

The construction assessment
`drafts/literature/2026-10-20-minus-three-unmarked-quotient.md` already
compares the exact quotient/lifting statement with known terminology,
stronger general theorems and local duplicates. The L106 audit assessment
`drafts/literature/2026-10-20-fixed-minus-three-genus-audit.md` supplies
marked-cover coverage. Reuse both; no new discovery campaign or claim of
novelty is justified. L106 is an audited input; L107 is the object tested.

[Stacks Theorem 53.2.6, 0BY1](https://stacks.math.columbia.edu/tag/0BY1),
statement and proof, identifies transcendence-degree-one function fields
with normal proper/projective curves and nonconstant morphisms. Its
extension and normalization argument supports extending the involution
and invariant-field inclusion. The audit must establish the precise
field, degree, smoothness in characteristic zero and full constants;
a singular projective closure cannot replace the smooth proper model.
The invariant-degree input remains Lemma 9.21.6 (09DU), previously read.
The explicit free-module invariant calculation needs checking rather
than another general quotient theorem. Proposition 39.23.9 (03BM) is
available from the construction assessment if an abstract quotient is used.

Reuse Milne, *Lectures on Étale Cohomology*, v2.21 (22 March 2013),
Theorems 3.1/21.3, pp.27,130–131,
[author PDF](https://www.jmilne.org/math/CourseNotes/LECc.pdf), and Stacks
58.6.2 (0BND). Their cover/fiber-functor comparisons apply to the actual
branch-deleted finite étale cover. L106's established monodromy and
ordered model must be transported to the quotient action. The sources
do not verify the stored permutations, cycle lengths or ordered returns.

[Stacks Section 53.12, 0C1B](https://stacks.math.columbia.edu/tag/0C1B),
Lemmas 53.12.1–4 and preceding differential calculation, was reinspected.
Riemann–Hurwitz requires smooth proper curves, generic separability and
full constant fields. In characteristic zero the different multiplicity
is e−1. The same discussion identifies the relative differential stalk
and explains automatic flatness for nonconstant smooth-curve maps;
Lemma 53.12.1's proof cites 53.2.3 and 29.37.16 for the unramified/étale
passage. This covers the audit's local criterion once relative indices
are proved, rather than assuming boundary freeness from the open action.
Check all three omitted branch values and both ordered cycles above
every quotient cycle. Reuse 53.8.2 (0BY6) for genus base change; it does
not establish geometric integrality or constants for this example.

[Stacks Lemma 59.28.1 and subsequent exact sequence, 03PK](https://stacks.math.columbia.edu/tag/03PK),
statement, unit-root proof and field specialization, require n invertible.
The proof constructs a finite free étale algebra by adjoining an nth
root of a unit. For the audit, n=2 and the residue fields have
characteristic zero; the relevant DVRs are curve-point DVRs, not dyadic
integer rings. Reuse 21.4.2–3 (03AG) for torsor triviality/sections.
Neither source identifies the actual radical or its constant twist:
both directions of the claimed discriminant condition must be checked.

[Stacks Lemma 15.116.2, 09EV](https://stacks.math.columbia.edu/tag/09EV),
statement and full proof, concerns adjoining a root of a uniformizer:
it gives degree, integral closure, DVR structure and total ramification,
with the prime-to-residue-characteristic qualification for tameness.
It is not by itself a formula for arbitrary unit-twisted radicals.
The even-valuation/unit case in L107 instead invokes 03PK and a direct
completed-local calculation. Audit the claimed parity, the rescaling,
normalization identification and both split/nonsplit residue cases,
including why completion determines the claimed rational fiber. Review
uniformizer independence separately. No new boundary result is derived here.

Additional retrieval of 37.19.2 (03GV) states normalization commutes with
smooth base change, with quasi-compact/quasi-separated source hypothesis;
it is an optional supporting result, not an assertion that completion is
smooth. Retrievals of 59.26.2 (03PC), Section 41.9 (0250), and broad search
results supplied no additional input used here. No uninspected search
snippet is treated as a theorem. Mathlib coverage remains not checked.

## Duplicate/failure controls and audit evidence

Local checks used L107, its construction assessment/attempt and histories
365–366, plus L106's prior audit assessment and audit note. The quotient
construction is already recorded; repeating it is not new research.
ATTEMPTS/045's class-backend park and ATTEMPTS/046-minus-three-joint-factor-at-seven.md's
exact seven-adic witness concern independent mechanisms and stay intact.
They neither establish nor obstruct the proposed correctness audit.
No sibling notebook was read; no cross-notebook input is used.

Essential input IDs are L106 and L107. The next audit must read L106's
canonical audited proof as needed, and inspect the complete relevant
`scripts/global-fiber-genus/certificate.json` and `audit-certificate.json`.
For L107, independently reconstruct every unordered label, action, cycle
and ordered return, and both invariant-remainder identities; compare the
full `scripts/global-fiber-genus/quotient-certificate.json` with
`quotient.py`, without treating a preview or its reported check count as
verification. The generic local proof must also cover every rational
boundary fiber; no enumeration of unknown rational points is required.

This literature-only step ran no mathematical script, verified no
certificate arithmetic and changed no lemma, PROOF.md or DAG.md. Source
coverage is ready for the separate mathematical audit. Both L095 integer
systems, gcd/positivity, remaining factors and minus-eleven remain open.
