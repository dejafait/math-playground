# Derksen finite fiber bound — approved quoted-bound evaluation

TARGET: Evaluate Derksen's Theorem 7 lower bound for A(965,10,9), with its prescribed field choice and Lemma 6 cases, against the strict benchmark 19800269675.
CHECKED: 2026-10-10
DECISION: IMPORT
SEARCH_EVIDENCE: Reuse the exact-parameter and B_h construction search in 2026-10-10-finite-nine-set-packing-lower-bound.md; the targeted local search in that assessment, its working note and dated packing/resource histories found source comparison but no evaluated Derksen certificate for these parameters.
SOURCE_EVIDENCE: Retrieved https://arxiv.org/pdf/math/0311385v1; inspected Proposition 2/Corollary 4, Theorem 5, complete Lemma 6 statement/proof and Theorem 7, printed pp. 2–5; extracted the essential formulas below. The original Bose–Chowla proof remains unaudited.
COMPARISON: The quoted theorem chain covers a finite distance-ten weight-nine existence bound; approve only its prescribed field selection, branch evaluation and integer comparison, not optimization or a new packing construction. No numerical bound is established this turn.
GAP: Source coverage is complete for the saved calculation; certify the prime-power choice, applicable branch, denominator and integer rounding next. Threshold crossing, L042 transfer and RS realization remain unproved.
REASON: Recovery requires a different independently testable mechanism; a bounded numerical application of an inspected algebraic existence theorem avoids the exhausted resource diagnostic and the unread Graham–Sloane scan.

This literature-only approval reuses the previous search and fills its
missing formula coverage. The exact target above is ready for a later
calculation, subject to the supervisor's separate approval of this changed
assessment. Do not restart general searches or the Graham–Sloane scan. Precise primary source:
Harm Derksen, *Error correcting codes and B_h-sequences*,
[arXiv:math/0311385v1, 21 November 2003](https://arxiv.org/pdf/math/0311385v1),
Proposition 2/Corollary 4 and Theorem 7 with Lemma 6, printed pp. 2–5.
The referenced Bose–Chowla proof was not audited; distinguish importing
the stated construction theorem from claiming a reproof of it.

## Mechanism comparison and chosen test

The main gap is arbitrary-center safety at 67/68 agreements. A useful
intermediate input would be a rigorously certified finite ordinary
packing lower bound, to test the L041 cap route through L042.

- **Finite algebraic fibers (selected).** Evaluate the specific
  inspected Derksen bound, including its prescribed prime-power choice
  and admissible Lemma 6 branch at h=4 and weight nine. This is a
  finite existence lower bound independent of the four-column LP.
  No numerical value for it has been established in this continuation.
- **Actual four-column augmentation (deferred).** Realize sufficiently
  many additions with checked pair intersections. L043 supplies only
  a resource budget and no suitable seed construction; selecting an
  unassessed large construction would broaden the completed target.
- **Point-conditioned compatibility upper bounds (deferred).** Add
  consistency constraints absent from L043. This could address the
  genuine missing intersection data, but no specific assessed system
  is ready; merely reoptimizing the same six resource rows is stopped
  by ATTEMPTS/027.

The selected bounded test is the exact integer lower bound supplied
by the stated theorem, compared strictly with 19800269675. If it
exceeds that number, use L042 only after a separate approved transfer
step; if it does not, park this particular quoted bound as insufficient.
That negative result would concern the bound, not all B_h constructions
or all ordinary packings. No field-size optimization beyond the stated
prescription, search for atypical large fibers, or new construction is
part of this proposed test.

Essential local interpretation inputs are L041 and audited L042.
L043 and ATTEMPTS/027 are contrasts, not mathematical premises.
An ordinary packing above b_*+1024 would obstruct the sufficient
uniform cap b_*=19800268651 after deletions, not prove an unsafe RS
list. Actual-label admissibility must follow from L042; cross-core
consistency, common-center realization, safety at 67/68 agreements
and ABF equivalence remain unresolved. Matching Mathlib coverage is
not checked. No source blockage is a prerequisite for this test.


## Essential primary formulas and qualifications

Write u for Lemma 6's degree parameter; q is a prime power,
0<u<q, and S has n elements. Its table is:

| Case | mu(q,n,u) |
| --- | --- |
| q>=n+u | (q-1)^u |
| n<q<n+u, n+u-q even | (q-1)^(q-n)(q^2-1)^((n+u-q)/2) |
| n<q<n+u, n+u-q odd | q(q-1)^(q-n)(q^2-1)^((n+u-q-1)/2) |
| q=n, u even | (q^2-1)^(u/2) |
| q=n, u odd | (q^2-1)^((u-3)/2)(q^3-1) |

The odd full-field row requires feasible degree at least three;
our possible degrees are four/five. The proof replaces higher factors,
repeated quadratics and excess repeated linear factors. Its odd
close-field case retains one double linear root. Full-field cases
use distinct quadratics and, for odd degree, one cubic.

Theorem 7 bounds c(n,h) by mu(q,q,h+1)/(q-1) if q=n-1
is a prime power; otherwise by mu(q,n,h), for the least prime
power q>=n. Corollary 4 gives A(n,2h+2,w)>=binomial(n,w)/c(n,h).
Proposition 2 proves fiber separation, including distances below 2h
by padding equal sums. Theorem 5 is imported, not reproved.

## Authorized calculation and stopping test

Use n=965, w=9, h=4. This matches distance ten without changing
the source's construction hypotheses. Leave the field choice and
branch to the calculation: explicitly certify whether 964 is a
prime power; if not, certify the least prime power at least 965.
Verify every needed degree is less than q. Use the table exactly,
retaining the q factor in the odd close-field case and the q-1
quotient only in Theorem 7(a). Record the full exact numerator,
denominator and ceiling justified by integer code size; do not use
floating-point comparison. This is a known-result application, with
no need to reprove the finite-field construction or optimize q.

A strict integer lower bound above 19800269675 warrants a separately
assessed L042 transfer. Otherwise park this specific prescription;
it does not refute other B_h constructions or actual packings.
This turn supplies coverage only, with no mathematical script,
branch calculation, new lemma or new extremal conclusion. Previous
searches establish no evaluated duplicate in the inspected paths.
Matching Mathlib coverage remains not checked.
