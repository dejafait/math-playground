# L046 — A conflicting pair in the fixed mixed-moment fiber

## Hypotheses

Use L045's universe Omega={0,...,8} times F_107, including every
column placement of profile (3,2,2,2). Distinct nine-sets conflict
when they meet in at least five points. Define the fixed map

\[
 \Phi(B)=\left(\sum_{(c,x)\in B}x,\ \sum_{(c,x)\in B}x^2,
               \sum_{(c,x)\in B}x^3,\ \sum_{(c,x)\in B}cx\right)
               \in\mathbf F_{107}^{4},
\]

with the indicated integer column labels embedded in F_107.

## Conclusion

The following distinct blocks have profile (3,2,2,2), meet in exactly
six points, and both have syndrome (36,96,22,67):

\[
 B=\{(0,0),(0,1),(0,2),(1,1),(1,10),(2,0),(2,10),(3,2),(3,10)\},
\]
\[
 B'=\{(0,0),(0,1),(0,2),(1,0),(1,10),(2,2),(2,10),(3,1),(3,10)\}.
\]

Thus the fibers of this particular map are not all compatible
families. Park its universal-separation argument. This does not
rule out compatible subfamilies within its fibers, other maps, or
large packings. It gives no packing-size estimate, labeled-cap
transfer, RS list, or 67/68 safety result.

## Proof

All displayed coordinates lie in the specified ranges. In column 0,
each block has the three distinct values 0,1,2. In each of columns
1,2,3 it has value 10 and one value in {0,1,2}, hence two distinct
points. Other columns are empty. Each block therefore has exactly
nine distinct points and the required profile. They differ because
(1,1) belongs to B and not to B'. Their complete intersection is

\[
 B\cap B'=\{(0,0),(0,1),(0,2),(1,10),(2,10),(3,10)\}.
\]

The variable points in columns 1,2,3 have different values between
the blocks, none equal to 10. Different columns cannot give equal
ordered pairs. Thus the intersection has exactly six points, exceeding
the conflict threshold five.

The multiset of values x in either block is
{0,0,1,1,2,2,10,10,10}. Their first three integer totals are therefore

\[
 2(0+1+2)+3\cdot10=36,\qquad
 2(0^2+1^2+2^2)+3\cdot10^2=310,\qquad
 2(0^3+1^3+2^3)+3\cdot10^3=3018.
\]

For the fourth total, column 0 contributes zero and the common
points with value 10 contribute (1+2+3)10=60. The variable points
contribute 1\cdot1+2\cdot0+3\cdot2=7 in B and
1\cdot0+2\cdot2+3\cdot1=7 in B'. Both integer totals are 67.
Since 310=2\cdot107+96 and 3018=28\cdot107+22, reduction gives
(36,96,22,67) in both blocks. This exact same-fiber conflicting
pair disproves universal separation.

This is direct finite arithmetic under the prior EXPLORE assessment
`drafts/literature/2026-10-10-mixed-moment-syndrome-test.md`.
No B_4 or pigeonhole packing theorem is invoked. The assessment's
Derksen v1 comparison explains why separation cannot be imported
for this map; no reproof of Derksen is needed. The local obstruction
was not supplied by the sources checked; that is not a claim of
originality.

Reproducer: `python3 scripts/finite-support/mixed_moment_collision.py`.
Complete certificate: `scripts/finite-support/mixed-moment-collision-results.json`.
The six permutations of 0,1,2, cyclically reassigned on columns
1,2,3 with other points fixed, give two passing witnesses. This is
not an exhaustive search of the universe. The selected witness field
was inspected in full, and the proof above verifies every load-bearing
quantity directly. A negative witness needs no exhaustive search.

**Separate critical audit (2026-10-10).** Under the preexisting EXPLORE
assessment `drafts/literature/2026-10-10-mixed-moment-collision-audit.md`,
the complete saved witness was independently reconstructed from the
displayed column descriptions, without importing the original script.
The audit records each point's four integer contributions and the
quotients and residues of all totals. Both total vectors are
(36,310,3018,67); their quotient vectors on division by 107 are
(0,2,28,0), with residues (36,96,22,67). The complete ordered-pair
intersection is the six-set displayed above. The left-only points are
{(1,1),(2,0),(3,2)} and the right-only points are
{(1,0),(2,2),(3,1)}. These disjoint differences verify distinctness
and exclude an accidental intersection caused by repeated values in
different columns. Each occupied column has the required number of
distinct points, and all nine labeled columns are retained.

Reproduction command:
`python3 scripts/finite-support/audit_mixed_moment_collision.py`.
The complete independent certificate is
`scripts/finite-support/mixed-moment-collision-audit-results.json`.
All 30 exact checks pass, including every saved witness field, the
incidental six cyclic trials/two witnesses, and the direct DAG input
L045. L045 supplies only the universe/profile and conflict definitions;
its numerical Gilbert bounds and its L043 baseline are not used here.

The logical inference is existential: one fiber contains two distinct
conflicting blocks. This negates the assertion that every fiber is a
compatible family. It neither proves that every fiber conflicts nor
excludes a compatible subfamily of this or another fiber. No source
separation theorem, exhaustive search, finite packing bound, actual
subgroup embedding or common-center realization is needed or proved.
The audit retains the fixed-map stop without a mathematical repair;
this is REPRODUCTION of the existing local obstruction, not a further
discovery beyond the sources checked. Mathlib coverage remains unchecked.

## Mathlib

Matching full-result coverage has not been checked. No Mathlib
theorem is used; this is explicit finite-set and F_107 arithmetic.
