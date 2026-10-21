# Unmarked quotient and fixed-field lifting — source comparison

TARGET: Determine the normalization genus of L106's quotient by v -> −v and the precise square-class −3 condition for rational points to lift.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched the exact polynomial with Putz/quadratic/genus, quotient curves with involution and square-class lifting, and primary finite-group quotient/Kummer results; compared complete L106, its two prior genus assessments and ATTEMPTS/045–046; no inspected classification supplies this exact quotient calculation.
SOURCE_EVIDENCE: Stacks current HTML retrieved 2026-10-20: Proposition 39.23.9 (03BM), Lemma 9.21.6 (09DU), Theorem 53.2.6 (0BY1), Lemma 9.24.1 (09I6), Lemma 59.28.1 and following exact sequence (03PK), Lemmas 21.4.2–3 (03AG), Lemma 15.116.2 (09EV); reuse prior Milne/Stacks cover and genus coverage, with 53.12.2/4 reinspected.
COMPARISON: Known quotient, curve/function-field, Kummer and Riemann–Hurwitz theorems cover the method; identifying this quotient, all normalization ramification and its particular minus-three lifting class remains an instance-specific specialization.
GAP: Construct and verify invariant coordinates/function field, the complete quotient branch action and genus, and a reversible lifting criterion including boundary local charts; no quotient genus or instance-specific lifting formula is proved by this assessment.
REASON: Essential primary coverage is now available for the unchanged bounded target; import the general theorems and prove only their model-specific applicability next turn.
SCOPE: Exactly TARGET on L106's smooth proper normalization and its distinct-root open; include normalization boundary fibers and distinguish open factor markings from boundary lifts; no rational-point classification, other quadratic field or L095 integer elimination.
LITERATURE_REASON: The changed quotient-and-lifting scope required essential unread quotient and Kummer hypotheses beyond the ready marked-cover genus assessment.

## Gap, use, inputs and stopping test

The main gap is primitive integer elimination in both L095 systems and
global factor compatibility. The intermediate target is only the quotient
geometry with a reversible rational lifting condition. This could reduce
the geometric cost of a later rational-point computation while preventing
arbitrary quadratic factors from being mistaken for the fixed minus-three
factor. No lower genus or point-classification method is assumed.

The essential input is audited L106, including its exact model, actual
A_11 monodromy, full ramification data and both certificates in
scripts/global-fiber-genus/. No certificate was replayed in this review.
L095 is downstream context only, not a premise of quotient geometry.
Reuse the prior marked-cover and audit assessments for Milne comparison
and Stacks component/genus results; no repeat discovery is needed.

Continue only if the quotient identification, complete genus calculation
and reversible lifting criterion can all be justified, including boundary
points separately from the distinct-root open. Otherwise save the precise
obstruction and reassess before point arithmetic. Do not assume any
favorable genus or rational-point method. Retain the existing 1000-label
finite-arithmetic cap; this method requires no class-group backend.

## Primary hypotheses and essential proof cases inspected

All new Stacks citations refer to current primary HTML retrieved on
2026-10-20; numbering below is that displayed in this retrieval.

1. [Stacks Proposition 39.23.9, tag 03BM](https://stacks.math.columbia.edu/tag/03BM).
   An affine groupoid with finite locally free source and target, whose
   relation map is an equivalence relation, has an affine invariant-ring
   quotient; the quotient map is finite locally free and its relation is
   the fiber product. Read the statement and proof, including invariants
   under flat base change, faithful flatness and the relation-ring
   isomorphism. On L106's open one must check the free action and affine
   setup. This does not justify freeness at unchecked boundary points.

2. [Stacks Lemma 9.21.6, Section 9.21, tag 09DU](https://stacks.math.columbia.edu/tag/09DU)
   gives a Galois extension of degree equal to a finite faithful
   automorphism group's order over its fixed field. Read its orbit-polynomial
   and finite-degree proof. [Theorem 53.2.6, tag 0BY1](https://stacks.math.columbia.edu/tag/0BY1)
   identifies transcendence-degree-one function fields with normal
   projective curves and nonconstant morphisms; read the extension of
   rational maps and compactification/normalization proof. These support
   a proper quotient defined by its invariant function field and extension
   of the involution. Identifying that field with explicit coordinates
   remains a research obligation. Characteristic zero permits smooth
   proper models; singular projective equations cannot replace them.

3. Reuse Milne, *Lectures on Étale Cohomology*, v2.21, Theorems 3.1/21.3,
   pp.27,130–131, and Stacks Theorem 58.6.2 from
   drafts/literature/2026-10-20-global-rational-quadratic-fiber-genus.md.
   Identify the quotient root-label action on the actual cover before
   applying component/orbit correspondence. Reinspected
   [Stacks 53.12.2/4, tag 0C1B](https://stacks.math.columbia.edu/tag/0C1B),
   including the characteristic-zero differential calculation: smooth
   proper curves, generically étale map and full constants are required;
   tame ramification contributes e−1. Retain all branch values and
   infinity on the normalization. Reuse previously assessed 53.8.2 and
   53.18.2 for genus base change and normalization. Freeness on the open
   and the marked genus alone do not settle boundary ramification.

4. [Stacks Lemma 9.24.1, Section 9.24, tag 09I6](https://stacks.math.columbia.edu/tag/09I6)
   gives a radical generator for a cyclic degree-n Galois extension when
   n is invertible and the base contains a primitive nth root of unity.
   Read its eigenvector proof. For degree two over a characteristic-zero
   function field these hypotheses are available; the particular radical,
   invariant coordinates and constant twist factor still need verification.
   Kummer theory does not supply the instance-specific discriminant formula.

5. [Stacks Lemma 59.28.1 and following exact sequence, tag 03PK](https://stacks.math.columbia.edu/tag/03PK)
   require n invertible. Read the proof using the finite free étale
   algebra adjoining an nth root of a unit, and the subsequent Picard
   exact sequence. At a field with n=2 this supplies square-class
   classification. [Lemmas 21.4.2–3, tag 03AG](https://stacks.math.columbia.edu/tag/03AG)
   identify torsor classes with H1 and triviality with existence of a
   section; read the abelian-sheaf extension construction. Together these
   cover rational lifting for the actual étale double-cover fiber.
   Next turn must identify its class with the fixed minus-three condition
   in both directions. A rational quadratic factor alone does not fix
   its splitting field.

6. For zeros/poles of a proposed radical, inspected
   [Stacks Lemma 15.116.2, tag 09EV](https://stacks.math.columbia.edu/tag/09EV),
   especially parts (1)–(5) and their DVR proof: adjoining an nth root of
   a uniformizer gives its integral closure and total ramification.
   Together with 59.28.1's unit-root étale construction, this covers local
   normalization charts after separating valuation from unit. This is a
   valuation at a point of a characteristic-zero curve, with number-field
   residue field, not a dyadic number-field valuation. Next turn must
   justify the charts, square rescalings and residue-field lifting tests,
   including any ramified case found. Substitution of zero or infinity
   into an unnormalized radical is insufficient. No boundary parity or
   lift is asserted here.

Also inspected Stacks 66.34.1 (071R), which alone supplies an algebraic-space
quotient, and 15.114.4 (09ED) plus 15.116.5 (0EXU), concerning residue Galois
groups and tame towers. These are secondary leads, not substitutes for
the affine quotient and checked local charts. Abhyankar search results
were not needed as another input. Mathlib coverage is not checked.

## Searches, duplicates and limits

Queries included the exact polynomial with Putz/quadratic/genus;
quotient curve involution quadratic twist rational points square class;
finite-group affine quotient invariants; and Kummer discrete valuation
normalization. No inspected classification supplies this exact target.
Search snippets, modular-curve twist abstracts, unrelated hyperelliptic
algorithms and non-primary discussions supplied no theorem used here.
No originality is inferred from the search.

Read complete L106 and both prior genus assessments. Targeted searches
in its attempt/audit notes and history/361–364 find the quotient only as
a future proposal. L106 distinguishes its markings from the quotient;
its audit supplies no quotient calculation. ATTEMPTS/045's class-backend
park and ATTEMPTS/046's exact seven-adic witness concern independent
mechanisms and remain unchanged. Neither globally bans this test.
No sibling notebook was read.

Approved next-turn obligations are the invariant model and its proper
normalization, complete quotient branch action and genus, and reversible
square-class lifting on the open with valid treatment at every rational
boundary point. A general local-chart criterion is acceptable without
enumerating rational points, but its hypotheses must be proved wherever
applied. Only open lifts have L106's disjoint-factor interpretation.
Import general theorems by citation; elementary invariant algebra and
local charts are the necessary specialization, not a reproof for novelty.

This literature step supplies source readiness only. It computes no
quotient genus, lifting formula or rational points and changes no lemma,
mathematical script, PROOF.md or DAG.md. L095 powers/gcd/positivity,
remaining global factors, minus-eleven and the main Beal gap remain open.
