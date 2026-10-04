# L018 — First disjoint singular fourth-support family excludes sixteen

## Hypotheses

Let F=F_(97^20), let H be the order-sixteen subgroup of F_97^*, and
let C=RS[F,H,8]. Use the pinned event on 1/4<=delta<5/16 and L010's
moment map sigma. Suppose the input pair a,b has full weight-four error
representatives at parameters 0,1,2 with respective supports

    A0={1,8,12,18}, A1={22,27,33,47}, A2={50,64,70,75}.

Suppose it also has a full weight-four representative on
K={1,12,22,64} at some finite parameter s in F. All error weights may
range over F; no prime-field restriction is made.

## Conclusion

The bad set satisfies |B(a,b)|<=15. Thus this particular singular
fourth-support family cannot attain L010's sixteen-count equality.
The proof uses the explicit finite polynomial certificate below;
it is not a classification of the other singular supports or arbitrary
triples, and supplies no improved global bound.

Up to a common nonzero scalar, every permitted pair's moments are the
one-parameter family displayed in the proof. Its full-weight locus is

    s not in {0,1,2,47,49,52,83}.

A sixteen-count specialization would necessarily have s=16. That
specialization has exactly four bad parameters, {0,1,2,16}, even over
the algebraic closure, and all coordinate locators have the singular
common root T=7. Counts below eleven improve no existing lower bound.

## Proof

L010 gives ker(sigma)=C, minimum codeword weight nine and uniqueness of
weight-at-most-four representatives. It also identifies sparse parameters
with bad parameters when D and every coordinate locator are nonzero
polynomials. These nonvanishing conditions hold here: the full error at
zero gives D(0)!=0, and a persistent coordinate would lie in both disjoint
supports A0 and A1, by L010's pointwise locator identity.

The twelve weights of the errors at 0,1,2 satisfy

    -sigma(e0)+2sigma(e1)-sigma(e2)=0.

The eight-by-twelve matrix has columns -x^j, 2x^j, -x^j in the stated
support orders, 1<=j<=8. Its rank is eight over F_97 and every extension:
any eight of the twelve distinct Vandermonde columns are independent.
Its kernel has the following basis, with the last four coordinates
forming the identity matrix:

    (96,39,40,56,25,40,82,11,1,0,0,0)
    (51,74,67,73,85,77,66,39,0,1,0,0)
    (83,64,78,75,45,86,63,56,0,0,1,0)
    (49,44,73,56,75,69,89,86,0,0,0,1).

For the r-th basis vector let u_r=sigma(e0_r) and
v_r=sigma(e1_r)-sigma(e0_r). Put f_K(X)=sum_(j=0)^4 f_j X^j
and M(S)_(i,r)=sum_j f_j*(u_(r,i+j)+S*v_(r,i+j)), i=1,...,4.
The fourth error is equivalent to M(s)z=0. To verify sufficiency,
solve its first four moments by Vandermonde inversion on K. Both the
supplied moments and these solved weights satisfy the monic recurrence
f_K, which successively recovers moments five through eight. Necessity
follows by summing f_K(x)=0 over its supported errors. Nonzero weights
are retained separately.

In the displayed basis the matrix is

    [89+44S, 57+20S, 75+ 5S, 53+53S]
    [45+86S, 49+24S, 41+93S, 48+70S]
    [91+93S, 50+72S, 63+ 8S, 18+57S]
    [57+58S, 64+65S,  2+48S, 55+24S].

Its determinant is identically zero. The monic gcd of all sixteen
three-by-three minors is S. Thus its rank is exactly three at every
s!=0 over every extension, and its rank at zero is two. Cofactors of
the first three rows, divided by their polynomial gcd, give

    z(S)=(83+7S,33+37S,76+59S,58+68S).

Direct multiplication gives M(S)z(S)=0. The first two entries of z
are coprime, so z(s) never vanishes as a vector. It therefore spans
every rank-three specialized kernel. At s=0 the full errors on A0 and
K would represent the same syndrome and hence be equal, contradicting
their different supports. No rank-exceptional full-weight branch is lost.

Using z(S) gives the following twelve error weights, in support order:

    e0: (80+21S,79S,76+6S,74S)
    e1: (40+17S,6+91S,19+78S,95+2S)
    e2: (83+7S,33+37S,76+59S,58+68S).

The solved weights on K at parameter S are

    (80+74S+40S^2,76+80S+38S^2,17S+40S^2,92S+5S^2).

The monic radical of the product of all sixteen weights is

    E(S)=S(S-1)(S-2)(S-47)(S-49)(S-52)(S-83).

Consequently the full-weight hypothesis is exactly E(s)!=0. Let
u(S)=sigma(e0(S)), v(S)=sigma(e1(S))-sigma(e0(S)). Form the actual
signed-minor locator L(S,T,X) from u(S)+T*v(S), and write
ell_x(S,T)=L(S,T,x). Its bidegree in (S,T) is at most (4,4).
Actual moments of any permitted pair are a common nonzero scalar
multiple of these; the locator is multiplied by the scalar's fourth
power. This changes neither roots nor equality conditions.

For each y in H minus {79} form the univariate elimination polynomial

    R_y(S)=Res_T(ell_79(S,T),ell_y(S,T)).

Each is nonzero of degree at most 32. Take its monic squarefree radical
and remove its gcd with E, obtaining r_y(S). This removal loses no root
at a full-weight specialization. The exact r_y are listed below; tuples
are coefficients in increasing powers of S, reduced modulo 97.

| y | r_y(S) |
| ---: | --- |
| 1 | (27,25,35,1) |
| 8 | (75,18,13,94,1) |
| 12 | (17,29,31,1) |
| 18 | (84,67,2,14,1) |
| 22 | (74,52,57,1) |
| 27 | (69,89,71,1) |
| 33 | (4,8,24,56,74,1) |
| 47 | (13,88,59,92,87,1) |
| 50 | (56,88,48,77,52,1) |
| 64 | (51,87,28,1) |
| 70 | (92,85,73,50,89,1) |
| 75 | (37,38,45,79,28,1) |
| 85 | (58,86,51,84,55,16,1) |
| 89 | (62,53,25,87,57,1) |
| 96 | (65,12,65,91,1,25,1) |

The monic gcd of any two entries is S-16, except the pair {22,89},
whose gcd is (S-16)(S-78). In particular every triple of distinct
entries has gcd S-16. These are finite polynomial identities, not a
sample of roots in the prime field. Bezout's identity transfers their
common-root implication to every extension. Supporting gcd invariance
under field extension is Milne, *Fields and Galois Theory*, v5.10
(September 2022), Proposition 2.17,
[printed p. 31](https://www.jmilne.org/math/CourseNotes/FT.pdf#page=31).

Suppose sixteen bad parameters existed. L010 makes ell_79(s,T) a
degree-four polynomial with four simple field roots. Choose any root
t. Exactly three other distinct coordinate locators vanish at t.
Their three resultants R_y therefore vanish at s. The degree-four
specialization here respects the Sylvester determinant; alternatively
the common root directly makes that determinant singular. Since E(s)!=0,
the same three r_y vanish. Their gcd forces s=16.

At s=16 the actual moment vectors are

    u=(51,40,66,48,25,4,27,27),
    v=(74,52,9,74,6,78,53,23).

The signed-minor locator coefficients, again in increasing T powers,
are

    c0=(9,25,33,64,48)
    c1=(25,58,43,42,27)
    c2=(44,60,79,24,75)
    c3=(68,32,90,11,50)
    c4=D=(48,43,42,25,13).

All five vanish at T=7. The common gcd of all coordinate locators is
exactly T-7; D(7)=0. Thus this root violates L010's required nonzero
Hankel determinant and four-coordinate incidence. Equality is impossible.
L010's integer upper bound now gives |B(a,b)|<=15 for the whole family.

For completeness, the exceptional pencil's exact count is also certified.
The multiplicity-four factor of the product of the sixteen coordinate
radicals, after removing D-roots, is

    W(T)=T(T-1)(T-2)(T-16)=T^4+78T^3+50T^2+65T.

By L010's converse this is precisely the regular weight-four parameter
polynomial, including over the algebraic closure. Any lower-weight
parameter would be a common locator root, so only T=7 needs testing.
Its moments are (84,16,32,81,67,65,10,91). For every one of the 560
three-subsets of H, solve the first three moments by Vandermonde
inversion and check the remaining five; none matches. This excludes
weight at most three over every extension, since that inverse and the
unique proposed weights lie in F_97. D has nonzero leading coefficient
and every coordinate locator has degree four, so the original point
at infinity is not sparse. The four displayed finite parameters are
therefore all bad parameters. W divides T^(97^20)-T exactly.

The reproduction command

    python3 scripts/coefficient-feasibility/singular_family.py

saves `scripts/coefficient-feasibility/singular-family-result.json`.
It stores the complete matrix, kernel, weights, bivariate signed minors,
fifteen resultants, saturated radicals, 105 pairwise and 455 triple gcds,
and the exceptional pencil. A five-by-five (S,T) evaluation grid checks
all five actual minors against independent scalar determinants (125
comparisons), proving equality of their coefficients within the stated
bidegree bounds. Each resultant is independently compared to its
evaluated Sylvester determinant at 33 distinct S values (495 comparisons),
proving all its coefficients within degree 32. Polynomial divisions are
exact. The complete original support event at s=16 is independently
checked on all 2517 admissible supports, yielding {0,1,2,16}.

The audit imports the resultant and squarefree ingredients from Milne
Proposition 4.35(b), [printed p. 58](https://www.jmilne.org/math/CourseNotes/FT.pdf#page=58),
and Volkovich, *On Some Computations on Sparse Polynomials*, Lemmas
23–24, [p. 48:8](https://drops.dagstuhl.de/storage/00lipics/lipics-vol081-approx-random2017/LIPIcs.APPROX-RANDOM.2017.48/LIPIcs.APPROX-RANDOM.2017.48.pdf#page=8).
For s=16 it compares every one of the 48 fourth-root residuals with
squarefree multiplicity decomposition; all fail. Coordinate degree,
simplicity, root regularity, candidate squarefreeness and D-coprimality,
and exact F_(97^20) splitting are separately recorded. Specified-field
splitting uses gcd with T^(97^20)-T, as covered by the saved assessment's
finite-field input on Milne's printed p. 53. No unspecified extension
is substituted for the target field.

## Mathlib

Coverage of the full singular-family exclusion and the finite polynomial
certificate: **not checked**. Supporting Vandermonde, rank-specialization,
gcd/Bezout and locator-incidence coverage elsewhere: **not checked**.
No Lean verification or full matching theorem is claimed.

Supporting resultant product and specialization coverage is **present**
in the previously read
[Resultant.Basic at commit 300d0e535721bc098547106fc297d8ba2a63f6bb](https://github.com/leanprover-community/mathlib4/blob/300d0e535721bc098547106fc297d8ba2a63f6bb/Mathlib/RingTheory/Polynomial/Resultant/Basic.lean),
including
[`Polynomial.resultant_prod_left`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Resultant/Basic.html#Polynomial.resultant_prod_left)
and
[`Polynomial.resultant_map_map`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Resultant/Basic.html#Polynomial.resultant_map_map).
The full family obstruction is **absent from that source checked**;
coverage elsewhere is **not checked**. These support the audit rather
than match the conclusion.

The standard algebraic tools are imported from the prior SPECIALIZE
assessment. The family exclusion is a local specialization not established
by the inspected source statements, classified POTENTIALLY_NEW relative
to that coverage. This is not a claim of certified originality.
