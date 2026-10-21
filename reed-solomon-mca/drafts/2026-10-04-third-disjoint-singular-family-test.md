# Third disjoint singular-family test — 2026-10-04

The ready actual-pencil COVERED_TARGET is specialized to K={8,47,64,75}
for A0={1,8,12,18}, A1={22,27,33,47}, A2={50,64,70,75} at 0,1,2.
The main gap remains 11/q–16/q versus an allowable fifteen. An exact
family exclusion would remove another unresolved singular branch; a
sixteen-count candidate would require all actual L010 equality and exact
F_(97^20) field gates. Arbitrary triples remain unresolved regardless.
The prior SPECIALIZE assessment supplies the standard resultant,
squarefree and extension-field tools; no new literature is needed.

Saved initial reasoning: the fourth-support matrix has zero determinant,
three-by-three minor gcd S-2, and primitive generic kernel
(18+88S,40+56S,94+50S,43+11S). The rank exception at S=2 must be
treated before using this kernel as a complete extension-field family.
The next calculation retains all sixteen weights and applies the actual
coordinate-resultant common-root test. No result for this family is yet
claimed. The previous singular families have distinct supports and
certificates; their exclusions are not assumed to cover this one.

## Completed bounded test

[L020](../lemmas/L020-third-disjoint-singular-family-exclusion.md) records
the complete informal proof. The
[script](../scripts/coefficient-feasibility/third_singular_family.py) saves
the [exact certificate](../scripts/coefficient-feasibility/third-singular-family-result.json).
The rank-two exception S=2 cannot retain different full supports A2 and K
at a single syndrome. The primitive kernel spans every other specialized
kernel over arbitrary extensions. Its full-weight locus excludes exactly
{0,1,2,27,33,49,66}; all original and fourth-support weights are retained.

Each of the 455 triple gcds of the fifteen coordinate-79 saturated
resultants is S-93. Equality would make a coordinate-79 root occur at
three other coordinates, forcing S=93 without a prime-field restriction.
At that specialization the coordinate-50 locator drops to degree three,
and every coordinate locator has common singular root T=82. Either
failure excludes equality. The actual product degree is 63, so the
degree-sixteen fourth-root test fails before coefficient recursion;
no candidate polynomial or 48 residual checks are reported. Independent
squarefree multiplicity decomposition agrees. Simplicity passes, while
degree, root regularity and splitting of every coordinate locator over
F_(97^20) fail. These gates are recorded separately.

The regular weight-four polynomial is T(T-1)(T-2)(T-93), exactly split
over F_(97^20). Testing all 560 three-support systems excludes the sole
possible lower-weight parameter T=82 over every extension. The direction
at infinity is nonsparse: D has nonzero leading coefficient, while only
coordinate 50 has a vanishing leading locator coefficient. An independent
original-event check on 2517 supports returns exactly {0,1,2,93}.

The certificate checks 125 actual-minor scalar evaluations and 495
Sylvester evaluations, within bounds that certify polynomial identities.
It also records a bounded redundancy check: neither coordinate scaling
x -> c*x nor inversion x -> c/x, for c in H, simultaneously permutes the
saved triple's supports and sends either earlier singular support to K.
This is not a full classification of automorphisms. The third family's
matrix, kernel, weights and resultants are newly computed; the same
standard tools and elimination mechanism are reused.

Outcome: NEGATIVE; STEP_KIND: RESEARCH; STEP_CLASSIFICATION: POTENTIALLY_NEW;
ACTUAL_TASK_TYPE: calculation. Stop this family as a sixteen-count
generator. The family exclusion is not established by the inspected
source statements, but no certified originality is asserted. The global
interval remains 11/q–16/q versus fifteen. One singular support,
all-prime configurations on other fourth supports, arbitrary triples
and July correspondence remain unresolved. The three singular tests
give informative exclusions rather than uninformative failures. No
calculation on the remaining support is made here.

## Mathlib

Full family exclusion and finite-certificate coverage: **not checked**.
Supporting resultant product/specialization coverage: **present** in
the previously read Resultant.Basic at commit
300d0e535721bc098547106fc297d8ba2a63f6bb, including
`Polynomial.resultant_prod_left` and `Polynomial.resultant_map_map`.
The full exclusion is **absent from that source checked**; elsewhere
coverage is **not checked**. L020 preserves the exact citations and
direct links. These support the calculation rather than match its result.
