# L104 — Quadratic direct components of the rational-factor complement

## Hypotheses

Let A,B,C be positive integers with A^3+B^5=C^11 and gcd(A,B,C)=1.
Let E=Q[t]/((3t²+t+1)^5(1−5t)−B^5/C^11). Assume E has a rational
direct factor and write E≅Q×F for its entire degree-ten complement,
as in L103. Let K be a quadratic number field occurring as a direct
component of F, rather than merely as a subfield of a larger component.

We use only L093's ramification support and L103's imaginary signature
and whole two-adic products. No L094 discriminant refinement is assumed.

## Conclusion

Necessarily K is isomorphic to exactly one of

    Q(sqrt(−3)), Q(sqrt(−11)).

Both fields pass these signature, ramification-support and whole-factor
tests. This is an exhaustive necessary list for those tests, not a claim
that either occurs in an actual F or a polynomial fiber.

More precisely, write Ud for the unramified degree-d extension of Q2.

| Entire F tensor Q2 | Quadratic direct components permitted by these tests |
| --- | --- |
| U10 | None |
| U5 × U3 × U2 | Either listed field, using the entire U2 factor |
| U4 × U4 × U2 | Either listed field, using the entire U2 factor |

There is at most one quadratic global component. If it occurs, the
global degree partition is (8,2) or (4,4,2), subject to L103's table.
Compatibility of the remaining larger fields, compatible products,
fiber realization, both L095 integer systems and all other residual
signatures remain unresolved.

## Proof

L103 proves that every field component of F is totally imaginary, so K
is imaginary quadratic. L093 proves that the entire algebra E is
unramified outside {3,5,11}; hence each field component, including K,
is unramified outside this set. In particular K is unramified at two.

The standard quadratic classification gives K=Q(sqrt(d)) for a unique
negative squarefree integer d. Its maximal-ring discriminant is

    D_K=d if d≡1 (mod 4), and D_K=4d otherwise.

A rational prime ramifies exactly when it divides D_K. We import these
facts from Jack Shotton, *Number Theory III*, Michaelmas 2026,
**Proposition 5.14 and Theorem 5.17**
([author's notes](https://www.maths.dur.ac.uk/users/jack.g.shotton/Teaching/number-theory/notes.html)),
and Gyujin Oh, *An Invitation to Modern Algebraic Number Theory*,
author-hosted revised version accessed 2026-10-20, **Example 1.28,
pp.19–20, and Theorem 4.11, pp.78–79**
([primary PDF](https://www.math.columbia.edu/~gyujinoh/ANT_revised.pdf)).
The exact target's prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-complement-quadratic-components.md`.

If two divides d, then two divides D_K, which is forbidden. Every odd
prime divisor of d divides D_K, so must be one of 3,5,11. Consequently
d=−3^a 5^b 11^c with a,b,c each zero or one: these eight possibilities
are exhaustive, including the empty product d=−1. The discriminant
formula and exclusion of ramification at two give the full table:

| d | D_K | Ramification support contained in {3,5,11}? |
| --- | --- | --- |
| −1 | −4 | No: two ramifies |
| −3 | −3 | Yes |
| −5 | −20 | No: two ramifies |
| −11 | −11 | Yes |
| −15 | −15 | Yes |
| −33 | −132 | No: two ramifies |
| −55 | −55 | Yes |
| −165 | −660 | No: two ramifies |

Thus precisely d=−3,−11,−15,−55 survive signature and support alone.
For squarefree d≡1 (mod 4), two splits if d≡1 (mod 8) and is inert
if d≡5 (mod 8). We import this odd-discriminant splitting criterion
from Oh, **Exercise 2.1 solution, p.222** (same version). It applies
to all four remaining d; the distinct even-discriminant case is not
being used. It yields:

| d | d modulo 8 | K tensor Q2 |
| --- | --- | --- |
| −3 | 5 | U2 |
| −11 | 5 | U2 |
| −15 | 1 | Q2 × Q2 |
| −55 | 1 | Q2 × Q2 |

In the inert cases, degree two and absence of ramification identify
the completion with the unique unramified quadratic extension U2.
In the split cases, both degree-one factors must be retained.

Since K is a global direct component, K tensor Q2 is a direct product
factor of the entire F tensor Q2. By uniqueness of finite-étale field
decomposition, it must be a product of whole local field factors.
Equivalently, its defining global idempotent maps to zero or one in
each local field; it cannot select a proper subfield inside that field.
L103 gives the three whole products U10, U5×U3×U2 and U4×U4×U2.
None contains any Q2 factor, so neither split quadratic can occur.
The product U10 has no subset of local factors of total dimension two,
so has no quadratic direct component at all. In each other product,
the unique subset of total dimension two is the single U2 factor.
Thus precisely Q(sqrt(−3)) and Q(sqrt(−11)) pass the whole-factor
test, and each must consume that U2. This also proves that two
quadratic global components cannot coexist.

For clarity about the sufficiency claimed for the tests, each listed
field is imaginary, has discriminant supported in {3,5,11}, and has
completion U2. Removing that U2 leaves U5×U3 in the second row,
whose only even-degree grouping is one degree-eight component; in the
third row it leaves the two labeled U4 factors, grouped either together
or separately. These are exactly the (8,2) and (4,4,2) degree patterns
specified by L103. This checks the stated necessary tests for both
fields without constructing the degree-eight or degree-four fields,
a compatible global product, or a fiber of the polynomial.

The finite enumeration and whole-factor matching are a REPRODUCTION
specialization of the inspected standard inputs. No result beyond
those checked methods or novelty is claimed. In particular, Putz's
Proposition 5.26 uses special coefficients and stronger local data;
its terminal exclusion is not an input here. Quadratic subfields of
U4 or U10 are not direct factors. All eight squarefree cases and all
four remaining completions are displayed, so no numerical sample or
mathematical script is needed. The separate critical application audit
is recorded below.

### Independent critical application audit — 2026-10-20

Verdict: **PASS without correction**, for the necessary tests exactly
as stated. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-complement-quadratic-components-audit.md`.
The inspected primary results and source versions cited above are reused;
no fresh source inspection or independent replay of Putz's computational
theorem is claimed. This audit checks their finite application, not a
stronger field classification or realization statement.

The hypotheses and entire algebra agree with audited L093 and L103.
In particular the rational factor is assumed globally. Its unique real
embedding exhausts the real factor of E; hence a quadratic component of
F is imaginary, rather than just having even degree. Unramifiedness of
the whole algebra outside {3,5,11} applies to each of its field components.
The cited maximal-discriminant criterion therefore applies to K itself,
without a polynomial-order or polynomial-discriminant substitution.

Independently enumerate the subsets of {3,5,11}. Squarefreeness permits
each prime at most once, negativity fixes the sign, and the empty subset
must be included. The following is the complete arithmetic check:

| Prime subset | d | d modulo 4 | Maximal discriminant | Pass support? |
| --- | --- | --- | --- | --- |
| empty | −1 | 3 | −4 | No |
| {3} | −3 | 1 | −3 | Yes |
| {5} | −5 | 3 | −20 | No |
| {11} | −11 | 1 | −11 | Yes |
| {3,5} | −15 | 1 | −15 | Yes |
| {3,11} | −33 | 3 | −132 | No |
| {5,11} | −55 | 1 | −55 | Yes |
| {3,5,11} | −165 | 3 | −660 | No |

Even squarefree d are excluded before this table because two would
ramify. An odd prime outside the support cannot disappear from D_K.
These observations and the eight subsets prove exhaustion, not just
correctness of the displayed examples. Every failed row has a factor
two in D_K; each successful row has only the allowed odd prime factors.

For the four successful rows the integral-basis polynomial in the cited
odd-discriminant splitting criterion is X²−X+(1−d)/4. Its constants
and complete reductions give an independent arithmetic application check:

| d | (1−d)/4 | d modulo 8 | Polynomial modulo 2 | Entire completion |
| --- | --- | --- | --- | --- |
| −3 | 1 | 5 | X²+X+1 | U2 |
| −11 | 3 | 5 | X²+X+1 | U2 |
| −15 | 4 | 1 | X(X+1) | Q2 × Q2 |
| −55 | 14 | 1 | X(X+1) | Q2 × Q2 |

The first polynomial has no root in F2; the second has its two distinct
roots. The cited criterion applies because all four d are squarefree
and congruent to one modulo four. No even-discriminant case is imported
from a different theorem. Since two is unramified, the inert degree-two
field is U2; in each split case both degree-one factors are indispensable.

For whole-factor matching, the idempotent defining K in F becomes zero
or one in each local field. Its support must therefore be a subset of
the whole local factors, of dimension two. This uses the same audited
base-change argument as L103. All nonempty subsets are listed here;
letters label positions, including the two isomorphic U4 factors:

| Local degrees | Nonempty subsets and their dimensions | Dimension-two subset |
| --- | --- | --- |
| a=10 | a:10 | None |
| a=5, b=3, c=2 | a:5; b:3; c:2; ab:8; ac:7; bc:5; abc:10 | c only |
| a=4, b=4, c=2 | a:4; b:4; c:2; ab:8; ac:6; bc:6; abc:10 | c only |

No row has a degree-one local factor, so no subset can realize the
two-factor split quadratic algebra. In the two rows with c:2 the whole
factor is U2, matching each of the two inert quadratic fields. Both
fields have the required imaginary signature and allowed discriminant;
the uniqueness in the cited squarefree classification also distinguishes
their global isomorphism classes. Thus no omitted quadratic passes these
tests and neither listed quadratic is falsely rejected by them.

Two global quadratic components would require disjoint dimension-two
subsets, which the table rules out. After assigning c to the sole
quadratic component, the remaining labeled degrees 5 and 3 must be
grouped together because both remaining global degrees must be even.
For the remaining labeled degrees 4 and 4, precisely the joined block
and the two separate blocks are possible. These exhaust the assignments
with a quadratic component and give exactly (8,2) or (4,4,2), with
the per-local-type restriction stated above. A quadratic subfield inside
U4 or U10 supplies no idempotent and is never a possible assignment.

The check verifies eight support candidates, four completions and all
fifteen nonempty local-factor subsets. The required exclusion threshold
for a quadratic-branch elimination would be zero candidates; two remain.
No missing case, mathematical correction or stronger result was found.
Compatibility of larger global fields, a simultaneous global product,
fiber realization and integer solutions are still unproved. L094 and
Putz's special-coefficient eliminations are not used. The direct inputs
remain L093 and L103. This is REPRODUCTION of assessed methods and
verification of existing local progress, not progress beyond those sources.

## Mathlib

Full matching coverage of this specialization and supporting quadratic
classification, discriminant and completion declarations: **not checked**.
No absence claim or formal verification is asserted.
