# Fixed starting-order audit, step 285

The approved target is the complete L077 audit under the unchanged
SPECIALIZE assessment. The main gap is arbitrary-curve rank equality
at analytic order at least two. A verified starting order could support
later index-prime and complete unit/class arithmetic for L066; it cannot
itself supply a Selmer enclosure or rational directions.

Read the full L077 proof, audited L067, both order implementations and
the saved Section 2/Proposition 4 comparison. The basis, field hypothesis,
triangular discriminant factor and Sylvester sign are consistent. The
producer and verifier both use Bareiss; review their determinant invariant
and supplement the full replay by a different exact row-elimination
calculation on both complete matrices. No new general theorem is sought.

One aggregate run in `scripts/seven-torsion/order-audit-285/` will include
full upstream replay, full order replay, both alternative determinants
and before/after original hashes. Limits are 180 seconds internally,
181 externally and 134217728 new bytes, with no retry or resumed stage.
Any missing evidence, failed identity or cap stops the run; preserve
partial reports. These were the pre-execution criteria.

## Completed evidence

The one aggregate run passes. The canonical proof and full applicability,
trace-index and determinant arguments are in
[L077](../lemmas/L077-conductor389-nonmonic-starting-order.md). Full exact
evidence is `scripts/seven-torsion/order-audit-285/`: all 4852 upstream
checks; all 48 basis elements, 110592 products and 2304 traces; complete
Bareiss chains; separate primitive-row determinants on both whole
matrices. Both signed integers agree. The determinant cross-check uses
elementary row multilinearity, with all rational multipliers accounted
for, rather than the same previous-pivot division.

Internal time 10.213518292061053 < 180 seconds; external time
10.340186832938343 < 181; 9080092 < 134217728 new bytes. All 65 original
files are unchanged. No retries or altered-evidence tests were performed.
The complete relevant evidence was checked by these full arithmetic
passes, not by JSON previews. This establishes the reliability of a known
fixed construction, with no claim beyond the checked source theorems.

## Recovery and different continuation

The recovery notice identifies repeated stalled literature work. The
actual saved assessment has no essential source blocker, so the ready
mathematical audit was executed without another retrieval. Repeating
Section 2 confirmation is now parked in ATTEMPTS/040. This is not a ban
on later arithmetic using L077, and it does not invalidate construction
step 283 or its source coverage. Previous incidence/interface stops remain.

Three distinct next mechanisms were compared, without executing any:

- General factorization of the 6870-digit discriminant: no certified
  factorization or runtime evidence; an unbounded attempt is unjustified.
- A radical/idealizer test at seven using L077's multiplication table:
  independently testable but only local; it would leave coverage of all
  other possible index primes unsettled.
- Complete division by the fixed primes 2,3,7,389, retaining the residual
  cofactor: a small exact support test that can either give complete
  support or a precise obstruction to the restricted-prime route.

Select the third mechanism for separate approval. The primes come from
the small model scaling, torsion degree and original bad prime; this is
motivation only, and the order discriminant can have additional primes.
No ramification or support claim is assumed. Cofactor one is the success
threshold; a larger cofactor stops that support claim and is preserved
without general factorization. Even success supplies no maximality,
field discriminant or S-unit/S-class completeness. L067 and L077 are the
only mathematical inputs; all L026 and descent/rationality gaps remain.
The new REVIEW_REQUIRED assessment records the exact target; no new
target has been calculated, derived or approved in this research turn.
