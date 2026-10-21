# Nonmonic starting-order test — source approval repaired

TARGET: Construct and independently verify the nonmonic order attached to L067's primitive polynomial H and its complete trace discriminant as the first gate for a maximal-order certificate.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step 281's exact maximal-order/nonmonic-order comparison and duplicate/failure search in 2026-10-17-torsion-field-maximal-order-certificate.md; this proposed test stays inside its inspected primitive-polynomial and exact-lattice scope, without an additional search.
SOURCE_EVIDENCE: Direct primary PDF https://www.impan.pl/shop/en/publication/transaction/download/product/82018 ; Del Corso--Dvornicich--Simon, Decomposition of primes in non-maximal orders, Acta Arith. 120 (2005), Section 2 pp. 232--234 and Proposition 4; inspected basis definition and triangular discriminant proof. Full citations, qualifications and finite contract: drafts/2026-10-17-maximal-order-source-review.md.
COMPARISON: Known mathematics gives the nonmonic starting-order construction and discriminant identity; this target tests complete fixed-field evidence and runtime only, not a new theorem or maximality.
GAP: No 48-element integral lattice, complete product/trace table or exact order-discriminant certificate exists; index-prime coverage, maximal overorders, field discriminant and unit/class completeness remain absent.
REASON: Step 282 separately rechecked Section 2 hypotheses and Proposition 4 and repaired the missing direct source URL; unchanged mathematical scope is ready for the bounded implementation, with no computation or maximality claimed.
SCOPE: Audited L067's full degree-48 field, H=343h and rational transports; all 48 basis elements, 110592 product slots and 2304 trace entries, inverse transports and two discriminants. Exactly one producer and one independent replay with fixed caps in the source review; no maximality, factorization, units/classes or stopped incidence reconstruction.

Use **Proposed bounded first test** in [the source review](../2026-10-17-maximal-order-source-review.md)
as the full input/output and stopping contract. The basis is the cited
Section 2 order basis, not raw powers of t. Certification includes ring
closure and the identity vector, not merely an invertible rational basis.
Ring closure is not integral closedness. Retain L067's full coordinate
transport; do not select a factor. L066 item 2 motivates the test but
contributes no premise; no L026 or Selmer hypothesis is used.

Passing permits only a separately assessed index-prime/maximality test.
Failure, missing complete evidence or either cap stops this representation
test with partial evidence preserved. Do not repeat norm interfaces,
resume stopped columns or enlarge caps. Faithful power classes, complete
S-units/S-classes, functions/local bounds, successful localization,
rational membership, divisible Sha and arbitrary-curve comparison remain
unresolved. Mathlib coverage is not checked. Proposed classification:
REPRODUCTION.

Approval repair (2026-10-17, step 282): primary PDF pp. 232--234 was
retrieved directly. Section 2 defines the order for primitive irreducible
F over a Dedekind ring; Proposition 4 proves the discriminant identity
by triangular basis change. L067 supplies the asserted field hypotheses
over Z; the implementation must still check every specified coefficient
and transport. This repeats existing coverage, not a mathematical advance.
