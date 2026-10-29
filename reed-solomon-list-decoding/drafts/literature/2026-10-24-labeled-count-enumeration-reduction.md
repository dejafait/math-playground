# Exact labeled count — proposed enumeration reduction

TARGET: Establish an exact finite line-incidence enumeration reduction for ordered triples of pairwise disjoint unordered pairs in the order-1024 subgroup of F_65537 with collinear (sum,product) points, retaining antipodal degeneracies.
CHECKED: 2026-10-25
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed bounded discovery and duplicate/failure comparison in 2026-10-24-labeled-collinear-pair-triple-count.md; no matching exact labeled count or reduction was found in the inspected sources.
SOURCE_EVIDENCE: L020 supplies the determinant predicate. Murphy–Petridis https://arxiv.org/pdf/1601.03981v3 Lemma 1 (printed p. 2), full Section 2 lemma proof (p. 5), rechecked 2026-10-25; reuse inspected Cartesian-product comparisons in Macourt et al. https://arxiv.org/pdf/1701.06192v2 Definition 1.1, Theorem 1.2, Lemma 2.4 and https://arxiv.org/pdf/2003.03493v1 Section 3, Theorem 5.2; these do not directly solve the labeled target.
COMPARISON: Standard affine-line incidence counting is available; specialization to pair-image labels, disjoint endpoints, ordered triple multiplicity and any efficient subgroup symmetry reduction remains to be justified. No exact answer or new formula is asserted by this assessment.
GAP: Prove an exhaustive, nonovercounting finite reduction with explicit shared-endpoint and vertical-line treatment and a credible operation/storage bound. The numerical whole-subgroup count is subsequent work, not required in this bounded proof attempt.
REASON: This is a concrete prerequisite for the reviewed exact-count target, distinct from the parked capacity and failed supersaturation tests. It can succeed or fail independently of a global list-size transfer.
SCOPE: Exactly TARGET using L020, C001a and foundations/02. Elementary pair-image injectivity, affine-line classification, endpoint-collision accounting, ordering normalization and multiplicative-subgroup orbit reduction may be attempted, but none is assumed. No core deletion, genericity, asymptotic bound or new extremal theorem is covered.

## Bounded attempt and test

Main gap: arbitrary-center 67/68 agreement safety. Intermediate target:
a provably exact, implementable reduction of the whole-H labeled count.
Downstream use: obtain a certified density diagnostic for L020 before
considering any separately assessed uniform core or supersaturation estimate.
No conversion from aggregate density to list safety is licensed.

Use the known unique-line property and import Murphy–Petridis Lemma 1
by citation rather than reprove its general second-moment theorem. Any
reproduction of elementary finite counting must address the changed
endpoint-label constraints that the cited theorem does not contain.
Keep all pair objects unordered internally and triples ordered; all six
endpoints must be distinct. Prove any image injectivity and orbit
multiplicities actually used, including stabilizers, before division.
Explicitly distinguish repeated pair objects from different pairs sharing
an endpoint. Vertical lines and antipodal pairs must have complete cases,
not error terms. No symmetry on cores or on all support triples is assumed.

Continue only with an exhaustive exact formula/algorithm, a proof of its
multiplicities and an operation/storage estimate supporting a later finite
run. Stop this reduction if a collision/degeneracy case remains unaccounted
for or it gives only generic counts or a return to raw six-tuple enumeration
without a credible bounded implementation. Preserve partial reasoning and
state the exact failure. This turn has proposed these obligations, not
proved or tested them; at proposal time separate approval was required.
The source-coverage review below completes that separate literature step.

Unresolved independently: the actual numerical count, uniformity after a
61-point core deletion, selected-support supersaturation, sufficient saving
at epsilon*|F|, RS realization, 67/68 safety and ABF comparison. Existing
955–957 bracket and all historical stops remain unchanged. No cross-notebook
input. Matching Mathlib count coverage and incidence support are not checked.
Proposed research classification: POTENTIALLY_NEW, meaning only that the
bounded search did not establish matching source coverage, not originality.

## Completed source-link and scope review, 2026-10-25

The saved TARGET is unchanged. This separate literature-only review repairs
the missing direct primary-source URLs; it does not establish an enumeration
formula. Reuse the bounded discovery, duplicate comparison and complete
2017/2020 proof-case review recorded in
[the count assessment](2026-10-24-labeled-collinear-pair-triple-count.md).
The three versioned primary PDFs above were accessible on this date.

Rechecked Murphy–Petridis, *A Point-Line Incidence Identity in Finite Fields,
and Applications*, v3 (20 February 2016), Lemma 1, printed p. 2, and its
entire proof on printed p. 5. Its hypothesis is any point set in the affine
plane over a finite field; sums include all affine lines. The proof treats
equal and distinct point pairs separately, then gives the variance
calculation. Thus vertical lines are included. No subgroup-size or
genericity condition is imposed. Import this known result only as a
second-moment consistency check after defining the target point set;
do not reprove it. The identity does not supply disjoint endpoint labels
or the requested triple count.

The earlier Cartesian-product mismatch and degeneracy qualifications are
unchanged; no new applications of those bounds are asserted. Rechecked
L020's exact determinant statement and ATTEMPTS/010: antipodal examples
remain genuine, so universal exclusion is still refuted. This review does
not reopen the recorded core/link or whole-pattern transfer routes. L031
remains the previously identified nearby duplicate, not a count input.

DECISION remains EXPLORE for the exact bounded TARGET and the stated SCOPE.
This is adequate source coverage for a subsequent mathematical attempt,
not approval of any unproved counting claim. Pair-image injectivity,
shared-endpoint corrections, vertical/antipodal cases, ordering and any
orbit stabilizers all remain proof obligations. Continue only if the
complete reduction and a credible operation/storage bound are obtained;
otherwise preserve the exact obstruction and abandon this reduction.
No count, new lemma, mathematical script, or Mathlib coverage claim was
produced in this review. Unread leads remain nonessential leads, not inputs.
