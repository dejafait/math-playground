# Second disjoint singular-family test — 2026-10-04

The saved ready actual-pencil target is specialized to K={8,27,50,75}
for the disjoint supports in L018. The global gap is still 11/q–16/q
against fifteen. The bounded test is a complete kernel/rank and full-weight
analysis followed by coordinate-resultant elimination; any remaining
specializations must pass actual L010 equality and F_(97^20) splitting.
Standard algebraic ingredients are imported from the saved SPECIALIZE
assessment, not rederived. Arbitrary triples remain outside this test.

Initial exact calculation: determinant M(S) is zero; the gcd of its
three-by-three minors is S-2. A primitive generic kernel is
(69+9S,24+85S,37+30S,84+69S). The rank exceptional value S=2 must
be handled independently before treating this as a complete family.
This is saved unfinished reasoning, not yet a family exclusion.

## Completed bounded test

[L019](../lemmas/L019-second-disjoint-singular-family-exclusion.md) records
the full informal proof and precise standard citations. The
[script](../scripts/coefficient-feasibility/second_singular_family.py)
saves the [exact certificate](../scripts/coefficient-feasibility/second-singular-family-result.json).
The exceptional rank-two parameter S=2 cannot have both different full
supports A2 and K at the same syndrome, by weight-four uniqueness.
Away from it the primitive kernel spans every specialization. All original
and fourth-error weights are retained: their full-weight locus is
S outside {0,1,2,3,57,87,90}. No extension-field family is sampled away.

After removing only forbidden-weight factors, each of the 455 triple gcds
of the fifteen coordinate-79 resultants equals S-10. L010 equality would
make every root at coordinate 79 occur at three other coordinates, forcing
S=10 over every extension by these exact gcd identities. Its actual pencil
has common locator gcd T-87 with D(87)=0, contradicting L010 equality.
All 48 coefficient fourth-root residuals fail, in agreement with the
squarefree multiplicity test. Coordinate degree and simplicity pass;
root regularity and splitting of all coordinate locators over F_(97^20)
fail. The regular four-error polynomial is T(T-1)(T-2)(T-10), split over
the target field. Testing all 560 three-support systems excludes the only
possible lower-weight parameter T=87. Infinity is nonsparse. An independent
check of the original event on 2517 supports gives exactly {0,1,2,10}.

The proof covers arbitrary extension-field weights for this fixed triple
and fourth support. Neither the nonprime isolated-root certificate nor
L018 covers this support. A bounded redundancy check found no coordinate
map x -> c*x or x -> c/x, c in H, that both permutes the saved triple's
supports and sends L018's K to the present K; this is not a classification
of code automorphisms. The same elimination technique is reused, while the
rank exception, weights and resultants are computed for the changed support.

Outcome: NEGATIVE; STEP_KIND: RESEARCH; STEP_CLASSIFICATION: POTENTIALLY_NEW.
Stop this family as a sixteen-count generator. The result is a local
specialization beyond the inspected source statements, not certified
originality. The interval remains 11/q–16/q against fifteen. Two other
singular families, all-prime configurations on other supports, arbitrary
triples and July correspondence remain unresolved. No calculation on
another family was made in this step. The two singular tests gave
informative exclusions, not uninformative failures; continuing to the next
untested singular locus is justified by its unresolved full-weight kernel.

## Mathlib

Full family exclusion and finite-certificate coverage: **not checked**.
Supporting resultant product and specialization coverage: **present** in
the previously read Resultant.Basic at commit
300d0e535721bc098547106fc297d8ba2a63f6bb, including
`Polynomial.resultant_prod_left` and `Polynomial.resultant_map_map`.
The full exclusion is **absent from that source checked**; elsewhere it
is **not checked**. Direct source and declaration links are preserved in
L019. The tools support the calculation rather than match its conclusion.
