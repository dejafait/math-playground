# L020 — Third disjoint singular fourth-support family excludes sixteen

## Hypotheses

Let F=F_(97^20), let H be the order-sixteen subgroup of F_97^*, and
let C=RS[F,H,8]. Use the pinned event on 1/4<=delta<5/16 and L010's
moment map sigma. Suppose a,b have full weight-four error representatives
at parameters 0,1,2 with respective supports

    A0={1,8,12,18}, A1={22,27,33,47}, A2={50,64,70,75}.

Suppose a+b*s also has a full weight-four representative on
K={8,47,64,75} for some finite s in F. All weights may range over F;
no restriction to prime-field coefficients is imposed.

## Conclusion

The bad set satisfies |B(a,b)|<=15. This singular fourth-support family
cannot attain L010's sixteen-count equality. The proof uses the explicit
finite polynomial certificate below and does not improve the global bound.
It covers neither the remaining singular support nor arbitrary triples.

Up to a common nonzero scalar, every permitted moment pencil is the
one-parameter family below, with full-weight locus

    s not in {0,1,2,27,33,49,66}.

Sixteen-count equality would force s=93. That specialization instead
has exactly four bad parameters {0,1,2,93}, even over the algebraic
closure. Its coordinate-50 locator has degree three, and every coordinate
locator has the common singular root T=82. Neither fact is compatible
with sixteen-count equality. This count improves no existing lower bound.

## Proof

By L010, ker(sigma)=C and the minimum nonzero codeword weight is nine.
Consequently a syndrome has at most one representative of weight at most
four. A full error at zero gives D(0)!=0. Moreover no coordinate locator
can be identically zero: its coordinate would have to belong to both
disjoint supports A0 and A1, by L010's pointwise identity. Thus L010's
nonpersistent hypotheses hold for every pair in this statement, and its
bad parameters are exactly its weight-at-most-four parameters.

The twelve weights at 0,1,2 satisfy

    -sigma(e0)+2sigma(e1)-sigma(e2)=0.

The matrix of this relation has columns -x^j,2x^j,-x^j on A0,A1,A2,
respectively, for 1<=j<=8. Its rank is eight over every extension of
F_97, since the twelve coordinates are distinct and every eight columns
form an invertible Vandermonde matrix times invertible diagonal factors.
A basis of its kernel, with final four coordinates forming the identity,
is

    (96,39,40,56,25,40,82,11,1,0,0,0)
    (51,74,67,73,85,77,66,39,0,1,0,0)
    (83,64,78,75,45,86,63,56,0,0,1,0)
    (49,44,73,56,75,69,89,86,0,0,0,1).

For its r-th vector put u_r=sigma(e0_r) and
v_r=sigma(e1_r)-sigma(e0_r). If f_K(X)=sum_(j=0)^4 f_j*X^j, the
fourth error is equivalent to M(s)z=0, where

    M(S)_(i,r)=sum_(j=0)^4 f_j*(u_(r,i+j)+S*v_(r,i+j)), i=1,...,4.

Necessity follows from f_K(x)=0 at each supported coordinate. For
sufficiency, solve the first four moments by Vandermonde inversion on K.
The solved weights and the supplied moments both satisfy the monic
f_K recurrence, recovering moments five through eight successively.
The separate full-weight check prevents replacing K by a smaller support.

In the displayed basis the matrix is

    [48+71S, 49+24S, 31+25S, 38+78S]
    [ 8+90S, 16+89S, 63+39S, 20+87S]
    [ 1+92S, 27+35S, 36+67S, 83+ 7S]
    [89+70S, 16+89S, 74+93S, 41+28S].

Its determinant is zero. The monic gcd of its sixteen three-by-three
minors is S-2, and its rank at two is two. Hence its rank is exactly
three at every other specialization over every extension. Cofactors
of its first three rows, divided by their polynomial gcd, give

    z(S)=(18+88S,40+56S,94+50S,43+11S).

Direct multiplication gives M(S)z(S)=0, and the first two entries of
z(S) are coprime. The vector therefore never specializes to zero and
spans every rank-three specialized kernel. At s=2 full representatives
on different supports A2 and K would have the same syndrome, contrary
to uniqueness. This excludes the entire exceptional kernel, not merely
the primitive vector at that point.

The twelve weights obtained from z(S), in the displayed support orders,
are

    e0: (85S,27+8S,44S,93S)
    e1: (53+44S,10+87S,91+6S,50+11S)
    e2: (18+88S,40+56S,94+50S,43+11S).

The solved weights on K at parameter S are

    (27+8S+62S^2,25S+36S^2,21S+76S^2,16S+81S^2).

The monic radical of the product of these sixteen polynomials is

    E(S)=S(S-1)(S-2)(S-27)(S-33)(S-49)(S-66).

Thus full weight is equivalent to E(s)!=0, with no extension-field
zeros omitted. Put u(S)=sigma(e0(S)), v(S)=sigma(e1(S))-sigma(e0(S)).
Construct the actual signed-minor locator L(S,T,X) from u(S)+T*v(S),
and let ell_x(S,T)=L(S,T,x). Its bidegree in (S,T) is at most (4,4).
Every permitted pair's moments are a common nonzero scalar multiple
of this pencil; that multiplies D and every locator by the scalar's
fourth power, preserving all equality conditions and sparse parameters.

For each y in H minus {79}, form

    R_y(S)=Res_T(ell_79(S,T),ell_y(S,T)).

Each is a nonzero polynomial of degree at most 32. Take its monic
squarefree radical and divide by its gcd with E, obtaining r_y(S).
All resulting tuples below list coefficients in increasing S degree,
reduced modulo 97.

| y | r_y(S) |
| ---: | --- |
| 1 | (41,29,96,64,95,1) |
| 8 | (28,11,1) |
| 12 | (29,7,66,38,34,1) |
| 18 | (27,13,19,28,55,1) |
| 22 | (29,28,64,96,1) |
| 27 | (83,9,91,77,17,1) |
| 33 | (55,91,86,53,90,1) |
| 47 | (73,57,44,1) |
| 50 | (87,13,54,62,1) |
| 64 | (41,94,31,1) |
| 70 | (9,14,60,41,1) |
| 75 | (57,91,1) |
| 85 | (9,68,41,31,15,69,1) |
| 89 | (3,8,60,30,9,1) |
| 96 | (41,52,6,5,10,28,1) |

The monic gcd of any pair is S-93, except the pair {22,47}, whose
gcd is (S-93)(S-35). Every triple of distinct entries has gcd S-93.
These are exact finite polynomial identities, not a search for roots
in F_97. Bezout's identity makes their common-root implication valid
in every extension; supporting gcd invariance under field extension
is Milne, *Fields and Galois Theory*, v5.10 (September 2022),
Proposition 2.17, [printed p. 31](https://www.jmilne.org/math/CourseNotes/FT.pdf#page=31).

If sixteen bad parameters existed, L010 would make ell_79(s,T) a
degree-four polynomial with four simple roots in F. Each root t occurs
at exactly three other distinct coordinates. The corresponding three
resultants therefore vanish at s. This is a necessary condition even
when another specialization drops degree: evaluation of the fixed
Sylvester determinant at two polynomials with a common root is zero.
Since E(s)!=0, removing only E factors loses no such root. The three
saturated radicals vanish at s, so their gcd forces s=93.

At that value the actual moment vectors are

    u=(27,35,72,88,73,77,88,19)
    v=(43,50,52,71,45,61,20,75).

The signed-minor coefficients of X^0,...,X^4, in increasing T degree,
are

    c0=(71,90,92,74,59)
    c1=(14,91,53,56,6)
    c2=(13,62,7,3,69)
    c3=(73,46,36,20,46)
    c4=D=(23,38,28,50,39).

Evaluation at coordinate 50 gives degree three; every other coordinate
locator has degree four. Thus the total degree is 63, already violating
L010's equality condition. Independently, all five coefficients vanish
at T=82 and the common gcd of the sixteen coordinate locators is exactly
T-82, with D(82)=0. That violates the required regular four-coordinate
incidence. Equality is impossible, and L010's integer bound gives
|B(a,b)|<=15 for the entire family.

The exceptional pencil's count can also be certified completely. The
multiplicity-four factor of the product of the sixteen coordinate
radicals, after removing D roots, is

    W(T)=T(T-1)(T-2)(T-93)=T^4+T^3+87T^2+8T.

By L010's converse, this is precisely the regular weight-four parameter
polynomial over the algebraic closure. Any weight-at-most-three parameter
would be a common locator root, so only T=82 remains to check. Its moments
are (61,61,68,90,77,35,79,58). For all 560 three-subsets of H, solve the
first three moments by Vandermonde inversion and test the remaining five;
none matches. This excludes smaller supports as well, by padding them
to a three-set with zero weights. The inverses and proposed weights
lie in F_97, so no extension weights evade these checks. The leading
coefficient of D is nonzero, and only coordinate 50 has a vanishing
leading locator coefficient. The direction at infinity is therefore
neither lower-weight nor weight four. The four finite parameters listed
above are exactly all bad parameters, and W divides T^(97^20)-T.

Reproduce the exact certificate with

    python3 scripts/coefficient-feasibility/third_singular_family.py

The output `scripts/coefficient-feasibility/third-singular-family-result.json`
stores all matrices, minors, weights, fifteen resultants, saturated
radicals, 105 pairwise and 455 triple gcds, and exceptional-pencil gates.
Supporting polynomial operations are reused from the existing scripts;
no previous family exclusion is used as a mathematical premise. A
five-by-five (S,T) grid independently checks all five actual signed minors
(125 scalar comparisons). Each resultant is compared with its evaluated
Sylvester determinant at 33 distinct S values (495 comparisons). The
bidegree and degree bounds make these coefficient identity checks.
Divisions are exact. The exceptional pencil is independently tested on
all 2517 admissible original-event supports, yielding {0,1,2,93}.

The standard resultant product and squarefree recognition ingredients
are imported from Milne Proposition 4.35(b),
[printed p. 58](https://www.jmilne.org/math/CourseNotes/FT.pdf#page=58),
and Volkovich, *On Some Computations on Sparse Polynomials*, Lemmas
23–24, [p. 48:8](https://drops.dagstuhl.de/storage/00lipics/lipics-vol081-approx-random2017/LIPIcs.APPROX-RANDOM.2017.48/LIPIcs.APPROX-RANDOM.2017.48.pdf#page=8).
Here the actual coordinate product has degree 63, so the degree gate
rejects c*P(T)^4 with deg(P)=16 before the coefficient recursion. No
48 residuals or candidate-root checks are claimed. Independent squarefree
multiplicity decomposition agrees with the rejection. Coordinate degree,
simplicity, regularity, and exact specified-field splitting are recorded
separately: simplicity passes, while degree, regularity and splitting
of all coordinate locators fail. Exact splitting is tested using gcd with
T^(97^20)-T, supported by Milne's finite-field discussion on printed
p. 53. The true four-error polynomial W splits in the specified field;
an unspecified extension is never substituted for F_(97^20).

## Mathlib

Coverage of the full family exclusion and finite polynomial certificate:
**not checked**. Supporting Vandermonde, rank-specialization, gcd/Bezout
and locator-incidence coverage elsewhere: **not checked**. No full
matching theorem or Lean verification is claimed.

Supporting resultant product and specialization coverage is **present**
in the previously read
[Resultant.Basic at commit 300d0e535721bc098547106fc297d8ba2a63f6bb](https://github.com/leanprover-community/mathlib4/blob/300d0e535721bc098547106fc297d8ba2a63f6bb/Mathlib/RingTheory/Polynomial/Resultant/Basic.lean),
including
[`Polynomial.resultant_prod_left`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Resultant/Basic.html#Polynomial.resultant_prod_left)
and
[`Polynomial.resultant_map_map`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Resultant/Basic.html#Polynomial.resultant_map_map).
The full family exclusion is **absent from that source checked**;
coverage elsewhere is **not checked**. These are supporting statements,
not a match for this conclusion.

The prior SPECIALIZE assessment supplies standard algebraic tools. This
local specialization is not established by the inspected source statements,
so it is POTENTIALLY_NEW relative to that coverage. No certified originality
or resolution of the main challenge is claimed.
