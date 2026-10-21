# L021 — Fourth disjoint singular fourth-support family excludes sixteen

## Hypotheses

Let F=F_(97^20), H the order-sixteen subgroup of F_97^*, and
C=RS[F,H,8]. Use the pinned event on 1/4<=delta<5/16 and L010's
moment map sigma. Suppose a,b have full weight-four error representatives
at parameters 0,1,2 with respective supports

    A0={1,8,12,18}, A1={22,27,33,47}, A2={50,64,70,75}.

Suppose a+s*b has a full weight-four representative on K={12,33,47,50}
for a finite s in F. All weights may lie in F; no prime-field restriction
is imposed on s or on the weights.

## Conclusion

The bad set has size at most fifteen. This entire fourth singular family
cannot attain L010's sixteen-count equality, even after extending the
coefficient field to the algebraic closure. This is a restricted-family
exclusion, not a global fifteen bound or a resolution of the challenge.

Up to a common nonzero scalar, every permitted moment pencil is the
family below with s outside {0,1,2,14,28,57,59}. The necessary equality
parameter polynomial from its coordinate-resultant certificate is 1:
there is no surviving parameter on which further field gates could
produce equality. A sample at s=3 has exactly four bad parameters
{0,1,2,3}, even over the algebraic closure; that sample is not used to
exclude other specializations.

## Proof

By L010, ker(sigma)=C and every nonzero codeword has weight at least
nine. Two representatives of weight at most four with the same syndrome
therefore coincide. A full error at zero gives D(0)!=0. No coordinate
locator is identically zero: L010's pointwise identity at zero and one
would place its coordinate in both disjoint supports A0 and A1. Thus
L010's nonpersistent bound applies to every pair under consideration,
and its sparse parameters are exactly its bad parameters.

The twelve weights satisfy -sigma(e0)+2sigma(e1)-sigma(e2)=0. The
matrix of this relation has columns -x^j,2x^j,-x^j on the respective
supports, for 1<=j<=8. Its rank is eight over every extension: any
eight columns are a Vandermonde matrix times nonzero diagonal factors.
Its kernel basis, with identity in the final four coordinates, is

    (96,39,40,56,25,40,82,11,1,0,0,0)
    (51,74,67,73,85,77,66,39,0,1,0,0)
    (83,64,78,75,45,86,63,56,0,0,1,0)
    (49,44,73,56,75,69,89,86,0,0,0,1).

For the r-th basis vector define u_r=sigma(e0_r) and
v_r=sigma(e1_r)-sigma(e0_r). Write f_K(X)=sum_(j=0)^4 f_j*X^j.
The fourth syndrome has a representative on K exactly when M(s)z=0,
where M(S)_(i,r)=sum_(j=0)^4 f_j*(u_(r,i+j)+S*v_(r,i+j)), i=1,...,4.
Necessity uses f_K(x)=0 on K. For sufficiency invert the first-four-
moment Vandermonde matrix on K; both the supplied moments and the
solved weights satisfy the monic f_K recurrence, which recovers moments
five through eight. Retain the separate full-weight condition.

The matrix is

    [21+38S, 60+60S, 55+94S, 78+29S]
    [22+86S, 91+40S, 46+43S, 54+29S]
    [50+72S, 81+48S, 77+71S, 76+88S]
    [52+71S, 13+80S, 45+28S, 30+26S].

Its determinant is zero. The monic gcd of its sixteen three-by-three
minors is S-1, and its rank at one is two. Thus its rank is three at
every other specialization over every extension. Divide the cofactor
vector of its first three rows by the gcd of its entries to obtain

    z(S)=(33+80S,30+82S,83+7S,9+44S).

Direct multiplication gives M(S)z(S)=0, and the gcd of these entries
is 1. Consequently z never specializes to zero and spans each
rank-three kernel. At s=1, full errors on distinct supports A1 and K
would have the same syndrome, contradicting uniqueness. This excludes
the whole rank-two exceptional kernel, including vectors not obtained
by specializing z.

The twelve weights obtained from z, in the displayed support orders,
are

    e0: (49S,29S,82+36S,69S)
    e1: (25+72S,40+57S,46+33S,68+9S)
    e2: (33+80S,30+82S,83+7S,9+44S).

Vandermonde inversion on K at the fourth parameter S gives weights

    (82+71S+41S^2,61S+18S^2,57S+20S^2,49S+48S^2).

The monic radical of the product of these sixteen weight polynomials is

    E(S)=S(S-1)(S-2)(S-14)(S-28)(S-57)(S-59).

Thus full weight is equivalent to E(s)!=0 over every extension. Put
u(S)=sigma(e0(S)), v(S)=sigma(e1(S))-sigma(e0(S)) and form L010's
actual signed-minor locator from u(S)+T*v(S). Write ell_x(S,T) for
its evaluation at x in H. Each has bidegree at most (4,4). Multiplying
all weights by a nonzero scalar multiplies D and every locator by
its fourth power, preserving roots and every equality condition.

For y in H minus {79}, compute R_y(S)=Res_T(ell_79,ell_y). Each is
nonzero of degree at most 32. Take its monic squarefree radical and
divide by its gcd with E, obtaining r_y. The exact saturated radicals
are below, with coefficients in increasing S degree modulo 97.

| y | r_y(S) |
| ---: | --- |
| 1 | (74,17,85,68,1) |
| 8 | (70,66,19,13,1) |
| 12 | (85,65,1) |
| 18 | (10,49,88,11,1) |
| 22 | (86,59,67,1) |
| 27 | (69,52,1) |
| 33 | (1) |
| 47 | (70,43,1) |
| 50 | (21,63,1) |
| 64 | (72,66,84,0,1) |
| 70 | (10,50,31,44,1) |
| 75 | (67,48,11,71,1) |
| 85 | (8,78,87,34,51,1) |
| 89 | (23,11,44,3,19,1) |
| 96 | (71,3,90,21,60,1) |

Every pair of distinct entries has gcd 1, so every triple does too.
These are finite exact polynomial identities, verified by Euclidean
arithmetic in the certificate below. Bezout's identity implies that no
pair can have a common root over any extension. The supporting extension
invariance is Milne, *Fields and Galois Theory*, v5.10 (September 2022),
Proposition 2.17, [printed p. 31](https://www.jmilne.org/math/CourseNotes/FT.pdf#page=31).

If sixteen bad parameters existed, L010 would give ell_79(s,T) degree
four with four simple roots, each shared with exactly three other
coordinate locators. At any such root, the corresponding three
resultants vanish at s: specialization of the fixed Sylvester determinant
at polynomials sharing a root is zero. Under equality the coordinate
degrees are four, so no degree-loss qualification is required. Since
E(s)!=0, removing only E factors preserves their roots at s. All three
corresponding r_y(s) would vanish. Their gcd is 1, a contradiction.
There is no equality survivor even over the algebraic closure, so none
can split over F_(97^20). L010's integer bound gives at most fifteen.
The proof imports the resultant/common-root machinery and investigates
only actual affine-moment compatibility, rather than re-proving that
standard machinery.

For an additional actual-pencil gate check, s=3 gives

    u=(59,39,8,10,32,29,32,51)
    v=(14,21,42,5,84,9,27,25)
    D=(33,77,43,61,56), in increasing T degree.

The coordinate product has degree 64. Coefficient fourth-root recursion
solves sixteen triangular coefficients, but all 48 remaining residuals
fail. Independently its squarefree multiplicity decomposition has factors
of degrees 42,3,4 at multiplicities 1,2,4 respectively, excluding the
required degree-sixteen fourth power. Every coordinate has degree four;
coordinate simplicity and splitting of all coordinate radicals over
F_(97^20) fail, while gcd(product,D)=1 passes. Full L010 equality fails.
These are sample gates, not tests claimed at every symbolic s.

The common coordinate-locator gcd is 1, excluding every lower-weight
parameter over the algebraic closure. The multiplicity-four factor of
the product of the coordinate radicals, after removing D roots, is
W(T)=T(T-1)(T-2)(T-3). L010's converse identifies its roots with the
regular weight-four parameters, proving the sample's exact four count.
All coordinate leading coefficients and the leading coefficient of D
are nonzero, so the direction at infinity is nonsparse as well. The
exact specified-field test gcd(W,T^(97^20)-T)=W passes; an unspecified
extension is not substituted for the target field.

Reproduce the finite certificate with

    python3 scripts/coefficient-feasibility/fourth_singular_family.py

Its output `scripts/coefficient-feasibility/fourth-singular-family-result.json`
retains matrices, kernels, every weight, fifteen resultants, 105 pairwise
and 455 triple gcds, and separate sample power/equality/field gates.
A five-by-five (S,T) grid independently checks all five signed minors
(125 scalar comparisons), and 33 S evaluations check each Sylvester
determinant (495 comparisons). The degree bounds make these coefficient
identity checks; all divisions are exact. An independent original-event
check of the sample on all 2517 admissible supports gives {0,1,2,3}.
A bounded scaling/inversion comparison to the earlier three supports is
recorded in the certificate; no full automorphism classification is used.
No previous singular-family exclusion is a mathematical premise.

Standard product and squarefree recognition tools are imported from
Milne Proposition 4.35(b), [printed p. 58](https://www.jmilne.org/math/CourseNotes/FT.pdf#page=58),
and Volkovich, *On Some Computations on Sparse Polynomials*, Lemmas
23–24, [p. 48:8](https://drops.dagstuhl.de/storage/00lipics/lipics-vol081-approx-random2017/LIPIcs.APPROX-RANDOM.2017.48/LIPIcs.APPROX-RANDOM.2017.48.pdf#page=8).
The exact finite-field root test uses Milne's finite-field discussion on
printed p. 53. These source statements support the tools, not the
constrained-family exclusion. The exclusion is POTENTIALLY_NEW relative
to the inspected sources, without any certified originality claim.

## Mathlib

Full family-exclusion and finite-certificate coverage: **not checked**.
Supporting Vandermonde, rank, gcd/Bezout and locator-incidence coverage
elsewhere: **not checked**. Supporting resultant product/specialization
coverage: **present** in the previously read
[Resultant.Basic at commit 300d0e535721bc098547106fc297d8ba2a63f6bb](https://github.com/leanprover-community/mathlib4/blob/300d0e535721bc098547106fc297d8ba2a63f6bb/Mathlib/RingTheory/Polynomial/Resultant/Basic.lean),
including
[`Polynomial.resultant_prod_left`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Resultant/Basic.html#Polynomial.resultant_prod_left)
and
[`Polynomial.resultant_map_map`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Resultant/Basic.html#Polynomial.resultant_map_map).
The full exclusion is **absent from that source checked**; coverage
elsewhere is **not checked**. No full match or Lean verification is claimed.
