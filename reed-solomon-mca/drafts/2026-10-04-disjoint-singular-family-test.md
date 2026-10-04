# Disjoint triple: first singular fourth-support family

Date: 2026-10-04. One mathematical attempt on the unchanged actual-pencil
COVERED_TARGET in the ready SPECIALIZE assessment
`drafts/literature/2026-10-03-nonpersistent-resultant-equality.md`.
The standard resultant, squarefree and exact finite-field tests are reused;
no essential unread source is needed for this specialization.

## Gap, target and stopping test

The pinned four-omission error interval is still 11/q–16/q, with fifteen
allowed. The preceding isolated nonprime-root certificate leaves four
zero-determinant systems. This step takes only the first, K={1,12,22,64},
for A0={1,8,12,18}, A1={22,27,33,47}, A2={50,64,70,75} at 0,1,2.
It seeks the rational-function kernel of its fourth-support recurrence,
retaining actual nonzero error weights and exceptional kernel ranks.

An actual sixteen-count witness would settle unsafety in this pinned cell.
An exact algebraic obstruction on this one family would close a stated
blind branch but would leave the other three singular systems, all-prime
configurations and arbitrary triples unresolved. Counts below eleven do
not improve the known lower bound. If the kernel or equality equations
leave unresolved families, save their precise equations and limitations;
do not substitute a prime-field sample for an extension-field exclusion.

## Saved unfinished reasoning

Form M_K(S) from the existing eight-by-twelve triple kernel. Its determinant
is identically zero. Use three-by-three minors to determine its generic
rank, a primitive polynomial kernel vector and the exact rank-exceptional
locus. Reconstruct all twelve original weights, eight affine moments and
the fourth error at S from that vector. Retain nonzero weights separately.
The resulting locator must be the actual signed-minor locator in a second
variable T. A prospective equality must retain coordinate simplicity,
nonzero D at every root and splitting over F_(97^20), as well as the
resultant power identity. A complete exclusion may use a necessary gate
if its applicability to every full-weight specialization is proved.

The three-by-three minors have common gcd S, and the first three rows
give the primitive kernel vector (83+7S,33+37S,76+59S,58+68S).
All twelve reconstructed weights are nonzero linear polynomials; at S=0
two weights of A0 vanish. No equality conclusion or next-family
calculation was asserted at that checkpoint.

## Completed family test

[L018](../lemmas/L018-first-disjoint-singular-family-exclusion.md) proves
that this full-weight singular family cannot have sixteen bad parameters.
The [script](../scripts/coefficient-feasibility/singular_family.py) saves
the [exact certificate](../scripts/coefficient-feasibility/singular-family-result.json).
The primitive kernel spans every specialization away from zero; the
rank-two zero specialization cannot retain two different full error
supports at the same parameter. The solved fourth weights and original
weights give the exact forbidden locus {0,1,2,47,49,52,83}.

The actual locator is retained as a bivariate signed-minor polynomial.
If a sixteen-count specialization existed, a root at coordinate 79 would
also occur at three other coordinates. All 455 triple gcds of the fifteen
coordinate resultants, after removing forbidden-weight factors, equal
S-16. This forces S=16 over every extension, rather than merely restricting
prime-field samples. All resultants are checked against independent
Sylvester determinants at 33 parameter values; all actual signed minors
are checked on a five-by-five evaluation grid.

At S=16 all coordinate locators have the common singular root T=7,
violating L010's equality conditions. The actual resultant fails all 48
fourth-root residuals. Separate simplicity, regularity and target-field
splitting gates also fail. Its regular four-error polynomial is exactly
T(T-1)(T-2)(T-16), which splits over the specified field. The only possible
lower-weight parameter is seven; all 560 three-support solves exclude it
over every extension. The original event independently agrees on all
2517 admissible supports, giving exactly {0,1,2,16}; infinity is nonsparse.

Outcome: NEGATIVE; STEP_KIND: RESEARCH; STEP_CLASSIFICATION: POTENTIALLY_NEW.
This closes one singular family and changes its generator decision, while
the global interval remains 11/q–16/q against fifteen. The standard
resultant and squarefree inputs are imported; the full family obstruction
is not covered by the inspected source statements. Certified originality
is not asserted. Stop this family. Three other singular systems,
all-prime configurations on other supports, arbitrary triples and the
parked July correspondence remain unresolved. No calculation on another
singular family is performed in this step.

## Mathlib

Full family exclusion and finite-certificate coverage: **not checked**.
Supporting resultant product and specialization coverage is **present**
in the previously read
[Resultant.Basic at commit 300d0e535721bc098547106fc297d8ba2a63f6bb](https://github.com/leanprover-community/mathlib4/blob/300d0e535721bc098547106fc297d8ba2a63f6bb/Mathlib/RingTheory/Polynomial/Resultant/Basic.lean),
including `Polynomial.resultant_prod_left` and
`Polynomial.resultant_map_map`. The full exclusion is **absent from that
source checked**; coverage elsewhere is **not checked**. Those results
support the audit, not the full conclusion.
