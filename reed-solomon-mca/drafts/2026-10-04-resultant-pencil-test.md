# Actual affine moment pencils: fourth-power test

Date: 2026-10-04. One mathematical attempt on the unchanged, ready
SPECIALIZE target in
[the saved assessment](literature/2026-10-03-nonpersistent-resultant-equality.md).

## Gap and bounded test

The pinned code has global bounds 10/q and 16/q at four omissions; its
budget permits fifteen. Only L010's nonpersistent sixteen-count equality
remains for this cell. The July source correspondence remains independent
and parked. The shared rules, complete overview, DAG, saved assessment and
unfinished local changes were read before calculation.

Import the resultant product formula and monic squarefree power recognition
cited in the assessment. For each supplied actual affine eight-moment
pencil, compute L010's five signed Hankel minors, its sixteen coordinate
quartics, and their product R. A candidate must have R=c*P^4 with P monic,
split squarefree of degree sixteen, all coordinate quartics simple, and
gcd(P,D)=1. Product multiplicities alone do not establish the last conditions.

The bounded search will vary the actual two-block construction across
partitions of H and also test independent eight-moment pencils. This uses
the construction only as a supply of candidates, not as a new proof of
L008. A failed prime-subfield sample excludes only that supplied pencil,
even if its polynomial failure persists over extensions. It cannot bound
all inputs over F_(97^20). Exact splitting for a polynomial with F_97
coefficients can be checked by divisibility into T^(97^20)-T without
constructing extension-field elements.

Continue with a full equality witness, a uniform obstruction, or a useful
restriction on the actual system. If the samples all fail, save the exact
tests and limits; do not claim a fifteen-count bound or call a reformulation
an advance. The later unscreened challenge definition and other radius
cells would remain even after deciding this pinned cell.

## Saved before the computation

No candidate or obstruction has yet been found in this step. The intended
power filter uses gcd(R,R') first, since a degree-64 fourth power of a
squarefree degree-sixteen polynomial has derivative gcd of degree 48 in
characteristic 97. All positive candidates must additionally pass direct
fourth-power equality and the full coordinate checks. Existing scripts,
lemmas and stopped orbit/source branches will be preserved.

## Restriction found during the test: proof checkpoint

All 256 supplied two-block partitions had only ten roots in the
multiplicity-four factor. The other 256 supplied pencils also failed the
target power test. This suggests examining the actual determinant, rather
than drawing a conclusion from the samples.

For a partition H=A disjoint-union B disjoint-union C of sizes 5,5,6,
write U=product_(x in A)(X-x), V=product_(x in B)(X-x),
Q=product_(x in C)(X-x). The actual locator should be a nonzero scalar
multiple of K(T,X)=(U(T)V(X)-V(T)U(X))/(X-T). For each of its four
moment rows, the kernel identity reduces to
U(T)*sum_(x in A) Q(x)V(x)x^i=0, i=1,...,4. Since UVQ=X^16-1,
Q(x)V(x)=16*x^15/U'(x) on A, and Lagrange interpolation gives
sum_(x in A) x^(i-1)/U'(x)=0. The T-coefficients of K have no common
factor: K(t,X) identically zero would require U(t)=V(t)=0. Hence the
proportionality scalar is polynomial in T, and degree four forces it
to be constant. A known weight-four parameter in A makes it nonzero.

This checks compatibility with the actual moments, rather than a generic
balanced incidence pattern. It also gives D proportional to U-V and
proves that no fixed-coordinate locator is the zero polynomial.

Any additional weight-four representative must have support inside C.
Equivalently four points of C must share U(x)/V(x)=r with r!=1.
The six-element set C has at most one fiber of size at least four, and
U-rV has degree five. A four-point fiber supplies one additional challenge;
a five-point fiber supplies five; no other extra challenges occur.
Thus the possible counts for this construction are 10, 11 and 15,
uniformly over extensions. The complete proof and precise same-support
justification are stored in the lemma artifact below. This restricts
the two-block class only; it is not a fifteen-count bound for all pencils.

## Completed result and limits

The proof is [L013](../lemmas/L013-two-block-locator-and-fiber-obstruction.md).
The original event identification and its converse are imported locally
from L010 after verifying both nonvanishing hypotheses. The new work is
the actual-moment divided-difference identity and its fiber application,
rather than a reproof of the standard resultant product or power test.
This restriction was not matched by the checked sources; it is potentially
beyond them, without a claim of originality.

The command `python3 scripts/resultant-pencil/check.py` saves
[the exact output](../scripts/resultant-pencil/result.json), with seed
2026100421. It tested:

| Supplied family | Pencils | Target squarefree fourth powers | Exact regular counts in F_(97^20) |
| --- | ---: | ---: | --- |
| Two-block partitions | 256 | 0 | 222 passed all regular-root checks, each with count 10 |
| Lines through two disjoint four-error representatives | 128 | 0 | 86 passed those checks, each with count 2 |
| Independent eight-moment pencils | 128 | 0 | 92 passed those checks, each with count 0 |

The two-block identity and fiber count were separately checked for all
256 supplied partitions, including the 34 outside the regular-root
shortcut: all had count ten, and their largest complement fiber had size
one (216 partitions) or two (40). Counts in the other rows are claimed
only for the stated regular cases. No squarefree power candidate was
found even before the full splitting and incidence validation.

For the first two-block sample, the normalized resultant factors as
G_10(T)^4*S_24(T), where G_10 and S_24 are squarefree and coprime.
The ten roots of G_10 are
{1,8,18,22,27,47,50,75,79,96}. Coordinate simplicity and gcd(R,D)=1
certify that precisely these are bad even over F_(97^20). The independent
interpolation audit of the original event checks all 2517 supports over
F_97 and returns the same set. Modular Frobenius verifies the required
extension-field root count without extrapolating from a base-field search.

The algebra controls also distinguish a manufactured fourth-power
product with repeated coordinate roots from one with simple roots, and
check splitting of an irreducible quartic in extension degree twenty.
These manufactured polynomials are algorithm checks, not proposed moment
pencils or equality witnesses.

Continue with the already covered general coefficient-feasibility target.
Stop this two-block partition generator as a sixteen-count witness:
L013's uniform upper count fifteen meets this class's budget, while the
required global upper count fifteen is still missing. The generic sample
failures supply no global obstruction. The scalar resultant equation
remains only a filter unless all coordinate and D conditions are imposed.

Outcome: ADVANCE for a useful class restriction, not for the negative
sample search. This is one mathematical attempt on the unchanged ready
resultant target. It produces no complete grand-challenge candidate and
does not reopen the parked July/four-block or full-orbit approaches.

## Mathlib

Supporting resultant products and specialization: **present** in the
previously inspected pinned Resultant.Basic source recorded in
[the assessment](literature/2026-10-03-nonpersistent-resultant-equality.md),
including `Polynomial.resultant_prod_left`,
`Polynomial.resultant_X_sub_C_left` and `Polynomial.resultant_map_map`.
The full locator/fiber classification: **not checked** in Mathlib and
**absent from that Resultant.Basic source checked**. No Lean verification
or full matching theorem is claimed. The standard power recognition is
imported from Volkovich's Lemmas 23–24; library coverage for that algorithm
is **not checked**.
