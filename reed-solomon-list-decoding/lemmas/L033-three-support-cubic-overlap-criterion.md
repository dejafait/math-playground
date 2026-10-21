# L033 — Three-support cubic-overlap realizability criterion

## Hypotheses

Use C001a's E=F_65537, F=F_(65537^28), order-1024 subgroup H,
k=64 and any integer m>=1. Let C,U_12,U_23,U_31,W_1,W_2,W_3
be mutually disjoint subsets of H, with |C|=60, |U_ij|=3 and |W_i|=2.
Put S_1=C union U_12 union U_31 union W_1, and define S_2,S_3 by
incident overlaps in the same way. Each support has size 68.

Realizability means three pairwise distinct polynomial m-tuples over F,
strict row degree less than 64, and one center Y:H -> F^m agreeing with
P_i on S_i. Additional agreements are permitted; original messages and
center need not descend to E. Write G=product_(c in C)(X-c), and
q_ij=product_(u in U_ij)(X-u). Let M be the 4-by-3 matrix over E whose
columns are the ascending coefficients of q_12,q_23,q_31.

## Conclusion

The supports are realizable for any, hence every, m>=1 if and only if
rank_E M=2. Equivalently, all four 3-by-3 minors vanish. Rank is always
at least two and is unchanged over F. In the rank-two case every nonzero
kernel vector has three nonzero coordinates and a scalar realization
already exists over E. Every row's cyclic reduced differences in any
realization are described by this kernel extended to F.

Both realizable and forbidden patterns occur on actual H labels, for
any admissible C,W_i. Thus this is a nonvacuous local labeled restriction,
not universal pattern exclusion. It proves no extremal cap, unsafe list
above threshold, or improvement to 955<=t_star(m)<=957. The separate
critical audit below verifies this criterion and both finite certificates;
it establishes no additional extremal conclusion.

## Proof

**Known framework and specialization.** Import Shangguan–Tamo,
*Combinatorial list-decoding of Reed–Solomon codes beyond the Johnson
radius*, [arXiv:1911.01502v1](https://arxiv.org/pdf/1911.01502v1),
4 November 2019, Definition 4.1 and its complete kernel equivalence
(one-based PDF pp. 9–10), and common-root division in Lemma 4.3
(PDF p. 11). The general dictionary describes three polynomials summing
to zero with respective pair-overlap roots. Here its degree bound after
common-root division is s=64-60=4. Lemma 4.2 requires even total overlap
and does not apply to nine points; no square determinant or generic
nonvanishing theorem is imported. AGL, *Randomly punctured Reed–Solomon
codes achieve list-decoding capacity over linear-sized fields*,
[arXiv:2304.09445v3](https://arxiv.org/pdf/2304.09445v3), 26 July 2023,
Definition 2.5 and Lemma 2.7, printed pp. 7–8, also supplies the signed
necessary difference-kernel framework over arbitrary finite fields.
Its random/symbolic rank theorem is not used at fixed H.

The preexisting [SPECIALIZE assessment](../drafts/literature/2026-10-07-sixty-core-three-overlap-criterion.md)
covers this exact pattern. The argument below is a reproduction of that
framework specialized to strict degrees, selected agreements, arbitrary
extension-field tuples, all three distinctions and a converse center.
L020 and L031 are comparisons for different patterns, not criteria
assumed for these new overlaps.

**Necessity without scalar projection.** In row r of a realization put
D_12,r=P_1,r-P_2,r, D_23,r=P_2,r-P_3,r, D_31,r=P_3,r-P_1,r.
Their sum is zero. Each vanishes on the 60-point C, so by the factor
theorem it equals G times a polynomial of degree at most 63-60=3,
including zero. At each point in U_ij, G is nonzero and D_ij,r vanishes.
The quotient therefore is a scalar multiple of the monic cubic q_ij:

D_12,r=G a_r q_12, D_23,r=G b_r q_23, D_31,r=G c_r q_31.

Cancelling nonzero G from their sum gives M(a_r,b_r,c_r)^t=0 over F.
If rank_F M=3, all these differences vanish in every row, contradicting
pairwise distinctness. Thus a realization implies rank_F M<=2. This
uses separate rows and does not assume a projection preserves distinctions.

**Rank and distinctions.** Any two columns are independent over F:
a dependence between two nonzero monic cubics would make them equal,
whereas their disjoint root triples rule that out. Hence rank is at least
two. Rank is the largest size of a nonzero minor, and all minors lie in
E embedded injectively in F; their vanishing is unchanged on extension.
Consequently rank_F M=rank_E M. At rank two the kernel has dimension one.
A nonzero kernel vector with a zero coordinate would give a dependence
between the other two columns, which is impossible. Row reduction over
E supplies a nonzero E-valued vector z=(a,b,c), with abc nonzero.
Its F-span is the entire kernel over F. This proves also the asserted
row-wise description for arbitrary ambient tuples, without assuming their
coefficients descend.

**Converse and one center.** For such z set scalar messages

f_1=0, f_2=-aGq_12, f_3=cGq_31.

The cyclic differences are aGq_12,bGq_23,cGq_31, since
 a q_12+b q_23+c q_31=0. Every difference is nonzero and has degree
60+3=63. All messages have strict degree less than 64. L001's root
bound makes their evaluation vectors distinct on H. Prescribe Y=f_i
on S_i. On an overlap C union U_ij the corresponding difference
vanishes; these are exactly the pair intersections, so all prescriptions
are compatible, including on the triple intersection C. Set Y=0 outside
the union. Private points create no further compatibility condition.
Appending zero rows gives the required realization for every m>=1.
Additional agreements are harmless. This proves the equivalence.

**An actual-label realization.** Take the overlap triples, in cyclic order,

```text
U_12 = {1,25417,40120},
U_23 = {8306,27221,30011},
U_31 = {14177,16349,35012}.
```

All nine entries are distinct and each has 1024th power 1 modulo 65537.
The roots of X^1024-1 in E are exactly H: H already provides 1024
roots, the maximum possible number. Thus these are actual subgroup
points. Multiplying the three linear factors in each case gives

```text
q_12 = X^3-X^2+39857X+25680,
q_23 = X^3-X^2+39857X+40164,
q_31 = X^3-X^2+39857X+64509.
```

Their common nonconstant part and distinct constants give rank exactly
two. For constants d_1,d_2,d_3 the vector
(d_2-d_3,d_3-d_1,d_1-d_2) has coordinate sum zero and constant-weighted
sum zero by expansion. Here it is (41192,38829,51053), all nonzero modulo
65537. It is the required kernel witness. There remain 1015 domain points;
choose any 60 for C and six more for the three private pairs. The converse
constructs valid supports and one center for every m. No cardinality
claim beyond three messages is inferred.

**A forbidden actual-label configuration.** Let h=3^64 mod 65537=19139.
Exact powers give h^1024=1 and h^512=-1, hence order 1024. Put
U_12={1,h,h^2}, U_23={h^3,h^4,h^5}, U_31={h^6,h^7,h^8}.
These nine points are distinct. Write x_0=1,x_1=h^3,x_2=h^6,
A=1+h+h^2 and B=h+h^2+h^3=hA. Their cubics are

q_r=X^3-A x_r X^2+B x_r^2 X-h^3 x_r^3.

Since h!=1, (h-1)A=h^3-1!=0 by the order of h. Thus A and B
are nonzero. The coefficient rows for X^3,X^2,X are respectively
(1,1,1), -A(x_0,x_1,x_2), B(x_0^2,x_1^2,x_2^2).
Their determinant is -AB product_(i<j)(x_j-x_i), nonzero because
the x_i are distinct. Hence rank M=3 and no realization exists for
any m or admissible core/private choices. This is a fixed-domain proof,
independent of symbolic/random-domain nonvanishing results.

**Exact certificate and checks.** Run
`python3 scripts/finite-support/three_overlap_criterion.py`.
It writes `scripts/finite-support/three-overlap-results.json` with the
entire domain, both complete support configurations, cubics, matrices,
all four maximal minors, the realized kernel, full message coefficients,
all evaluations, one center, all agreement sets and pair equality sets.
Arithmetic is exact modulo 65537. Cubics are generated by factor
multiplication; all minors are computed by the explicit three-by-three
determinant expansion. Disjoint roots guarantee rank>=2, so these maximal
minors suffice to certify both ranks. Every kernel equation, prescription,
selected agreement and pair equality is checked over the entire domain.
The realized messages have degrees (-1,63,63), where -1 denotes zero.
Their pair equality sets are exactly C union U_ij, of size 63 each.

The complete small load-bearing records were inspected with the JSON
inspector at `/cases/realized/small` and `/cases/forbidden/small`, using
`--full`. All realized maximal minors are zero. The forbidden minors,
in ascending triples of row indices, are (45703,40818,47265,25894).
Its X^3,X^2,X minor has opposite row orientation to the ascending
(1,2,3) minor; both are nonzero. The complete construction checks report
no failures. The fixed selected-center rule yields agreement counts
(1017,68,68). Indeed f_1=0 agrees on its 68 selected points, plus the
949 outside the 75-point union; the nonzero messages have exactly their
63 roots in C union their specified overlap with f_1, and the other
pair equality set is also exhausted. These counts are compatible with
extra agreements, not an unsafe threshold certificate: three is far below
65537^28/2^128. The formulas above, rather than a preview of evaluation
arrays, justify the center and distinctness claims.

**Independent critical audit (2026-10-07).** The approved audit assessment
is `drafts/literature/2026-10-07-three-overlap-critical-audit.md`.
The necessity, rank/distinction argument and converse above survive
review without a mathematical correction. In particular a zero row
difference is included in the divisibility argument; rank three would
annihilate every row difference, whereas rank two gives the same
one-dimensional F-kernel in every row. No scalar projection or descent
of the original tuples is assumed. Disjoint monic root cubics force
every pair of columns to be independent, which rules out zero coordinates
in a nonzero kernel vector. The displayed scalar converse therefore
preserves all three distinctions. The seven-set disjointness identifies
every shared prescription, and the degree-63 difference root sets ensure
distinct evaluation vectors. The proof applies to arbitrary admissible
C and private sets, not just the certificate's chosen sets. Embedding the
constructed scalar messages with zero rows establishes all m>=1.

Run `python3 scripts/finite-support/audit_three_overlap.py` for the
independent full reconstruction. It imports no original producer code.
For roots r_1,...,r_d it calculates p_j=sum_i r_i^j and elementary
symmetric values by
`e_0=1; k e_k=sum_(j=1)^k (-1)^(j-1) e_(k-j) p_j`.
The coefficients are `(-1)^(d-i)e_(d-i)` in ascending order.
All used d are at most 63, so every divisor k is invertible in E.
This independently recovers the cubics, core polynomial and full
message polynomials without linear-factor multiplication. Direct sums
of coefficient-times-powers recover every evaluation. Gaussian
elimination independently supplies ranks and all four maximal minors;
the certificate records every elementary row operation and reduced matrix.

The audit enumerates all roots of X^1024-1 in E and identifies them
with the entire generated domain. It reconstructs every support and
every source-certificate field, comparing all types, keys, lengths and
7,328 scalar values exactly. All 41 separate mathematical checks pass,
including the seven disjoint sets, every cyclic polynomial identity,
all 1,024 compatible-center entries, all message evaluations, all
selected/full agreement sets and full pair equality sets. The ranks
are exactly 2 and 3; the realized agreement counts are (1017,68,68).
The forbidden descending-row Vandermonde minor is 39643, the negative
of the ascending-row value 25894 modulo 65537. No error or missing
distinction was found. Full reconstructed data, elimination certificates,
source SHA-256 and checks are saved in
`scripts/finite-support/three-overlap-audit-results.json`, with no failures.
Complete relevant data were machine-compared, not inferred from a preview.

This is verification of the existing specialization of the cited
frameworks. It is neither a new general theorem nor progress beyond
the assessed sources. Three messages remain strictly below the unsafe
threshold; a sufficient 60-core cap and incidence transfer, cross-core
consistency and a large common-center list remain unproved.

## Mathlib

Full matching coverage and supporting theorem names were not checked.
This is not evidence of absence. The factor theorem, polynomial root
bound, rank via minors and field-extension preservation are used with
explicit elementary arguments; no formal verification is claimed.
