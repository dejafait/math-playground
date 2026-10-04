# Disjoint triple: exact nonprime fourth-support roots

Date: 2026-10-04. One mathematical attempt on the unchanged actual-pencil
COVERED_TARGET in the [ready SPECIALIZE assessment](literature/2026-10-03-nonpersistent-resultant-equality.md).
The standard resultant, squarefree and finite-field ingredients are reused;
no additional literature review is needed.

## Gap, intermediate target and stopping test

The pinned four-omission interval remains 11/q–16/q, with fifteen allowed.
The common-coordinate triple has been excluded and is stopped. This step
tests the previously unsearched nonprime roots for the disjoint triple
A0={1,8,12,18}, A1={22,27,33,47}, A2={50,64,70,75} at 0,1,2.
The earlier prime-field search left 402 target-field root occurrences
for this layout, as well as four zero-determinant systems. Only the
nonzero-determinant, nonprime-root branch is tested here.

An actual sixteen-count witness would decide unsafety for this pinned
cell. A complete exclusion of this finite algebraic branch would close
an explicit omission of the earlier generator, but would not exclude
the four zero-determinant families, arbitrary support triples or the
general nonpersistent equality. The eleven-count witness remains the
benchmark; a smaller count improves no global bound.

## Saved unfinished reasoning

Reuse the eight-by-twelve triple kernel and four-by-four fourth-support
recurrence matrix M_K(T) from the previous three-support test. Their
entries lie in F_97 and det M_K has degree at most four. Factor its
squarefree radical over F_97. A nonprime root lies in F_(97^20) exactly
when its irreducible factor has degree two or four; degree three is
excluded. For each such factor f, work in the exact field F_97[T]/(f)
at alpha=T mod f, recover ker M_K(alpha), and retain only actual full
weights for all four prescribed supports. One root per irreducible
factor suffices for Frobenius-invariant audits, with its degree retained
as the number of conjugate root occurrences. Larger kernels remain
explicitly unresolved rather than replaced by a chosen basis vector.

Every retained pencil will receive an independently reconstructed actual
Hankel locator, the complete L010 equality checks, coefficient fourth-root
recursion, and splitting by gcd with T^(97^20)-T over its coefficient
field. Conjugate roots and field representations are not assumed to
give distinct projective pencils. No bound or candidate is asserted
before these computations.

## Mathlib

The full extension-root generator and constrained pencil enumeration:
**not checked**. Supporting resultant product and specialization coverage
is **present** in the previously read
[Resultant.Basic at commit 300d0e535721bc098547106fc297d8ba2a63f6bb](https://github.com/leanprover-community/mathlib4/blob/300d0e535721bc098547106fc297d8ba2a63f6bb/Mathlib/RingTheory/Polynomial/Resultant/Basic.lean),
including `Polynomial.resultant_prod_left` and
`Polynomial.resultant_map_map`; these are not a full matching theorem.
Finite-field implementation and kernel coverage elsewhere is **not checked**.

## Completed branch test

[L017](../lemmas/L017-disjoint-triple-nonprime-isolated-branch.md) gives
the field-descent argument, complete finite-certificate qualification and
original-event passage. The [script](../scripts/coefficient-feasibility/extension_roots.py)
and [certificate](../scripts/coefficient-feasibility/extension-root-result.json)
exhaust all 1817 fourth supports and all their nonprime target-field roots
when the determinant is nonzero. All 402 root occurrences come from 201
irreducible quadratic factor occurrences; no quartic factors or larger
kernels remain. Every kernel has twelve nonzero triple weights and four
nonzero fourth weights. A single root per factor is audited, with its
Frobenius conjugate retained by degree and invariance rather than counted
as an assumed distinct projective line.

Each resulting pencil has exactly four bad parameters over the algebraic
closure and the target field, namely its prescribed 0,1,2 and nonprime
fourth parameter. The exact distinct-incidence polynomial equals the
displayed product of those four transformed roots. The common locator
gcd is one, excluding all lower weights. Actual signed minors are checked
by independent scalar determinants at five points; their recurrence
identities, all fourth-root residuals, squarefree multiplicities and exact
F_(97^20) splitting gates agree. All 201 products fail the fourth-power
identity. The example over alpha^2+55alpha+74=0 independently passes
the original event on all 2517 admissible supports, including the chart
change and infinity check.

Outcome: NEGATIVE; STEP_KIND: RESEARCH; STEP_CLASSIFICATION: REPRODUCTION.
This is a complete exclusion of the stated isolated extension-root branch,
with explicit finite-certificate dependence. It changes the generator
decision rather than the global interval 11/q–16/q against fifteen.
The standard algebraic ingredients are imported; the covered local
moment/recurrence framework is specialized and implemented. No certified
originality or advance beyond the checked literature is claimed.

Stop this branch. The four zero-determinant supports are {1,12,22,64},
{8,27,50,75}, {8,47,64,75} and {12,33,47,50}. The next direction
within the same ready actual-pencil target is the first of these:
parameterize ker M_K(T) over F_97(T), retain its full-weight locus and
test the actual equality conditions. No calculation on that next branch
is performed here. Arbitrary triples, all-prime parameter configurations
and July correspondence remain unresolved. Consecutive uninformative
mathematical turns used: zero after this informative negative.
