# L047 — Five embedded quadratic graphs force common-center equality

## Hypotheses

Use C001a/C012a's E=F_65537, F=F_(65537^28), H<=E^* of order 1024,
k=64, and any integer m>=1. Fix g=19139=3^64 in E and
C={g^j:0<=j<=60}. Its 61 points are distinct. Let
T=(16,64,70,102,112,118,121), in this order, in the auxiliary field
F_137, as in L030. Define five auxiliary polynomials, indexed 0,...,4,
by their coefficients (constant,linear,quadratic):

```text
q0=(33,27,3), q1=(106,120,2), q2=(0,0,0),
q3=(64,44,1), q4=(34,47,2).
```

For each i let B_i be the set of seven actual E-labels
g^(61+137*j+rep(q_i(t_j))), 0<=j<=6, and put S_i=C union B_i.
Here rep is the representative in {0,...,136}; this is a set labeling,
not a map of fields. A realization means a single received array
Y:H->F^m and message tuples P_i in (F[X]_<64)^m agreeing with Y
on their respective selected supports S_i. Extra agreements are allowed.

## Conclusion

Every such realization has P_0=P_1=P_2=P_3=P_4, row by row as polynomial
tuples. In particular these five selected 68-supports cannot occur for
five pairwise distinct messages at one center, for any m>=1.

Nevertheless the five seven-sets B_i belong to the single pinned embedded
L030 quadratic family, independent in L027's pair/determinant local edge
systems. Thus those local restrictions miss this specific common-center
obstruction. The result supplies no quantitative family cap, no exclusion
for other embeddings, no cross-core consistency theorem, no unsafe list,
and no improvement of 955<=t_star(m)<=957. It is a finite REPRODUCTION of
assessed signed-matrix methods, not a claim of new general mathematics.
The separate critical audit below retains the specialization and certificate.

## Proof

**Imported method and reason for specialization.** Alrabiah, Guruswami
and Li, *Randomly punctured Reed–Solomon codes achieve list-decoding
capacity over linear-sized fields*,
[arXiv:2304.09445v3](https://arxiv.org/pdf/2304.09445v3), 26 July 2023,
Definition 2.5 and Lemma 2.7 with its proof, printed pp. 7–8, supply
the signed intersection matrix, a star at every hyperedge, and the
coefficient-difference kernel obtained by subtracting the last message.
Its scalar statement is over arbitrary finite fields. The saved
[SPECIALIZE assessment](../drafts/literature/2026-10-10-embedded-quadratic-bounded-search.md)
requires the common-root, selected-support, arbitrary-overlap and tuple
justifications below, plus an exact calculation for these actual labels.
L020/L031 supply comparisons only: their special incidence hypotheses
are not invoked. We neither reprove nor use symbolic/generic/random-domain
rank conclusions for these fixed subgroup points.

**Exact incidence, including every higher overlap.** C012a proves
g^1024=1 and g^512=-1, hence exact order 1024. The exponents for B_i
are between 61 and 1019, in seven disjoint 137-element intervals.
They are distinct from the core exponents 0,...,60. Thus the label map
on all 959 auxiliary points is injective and each S_i has size 68.
The following are the complete exponent and label rows, in column order:

```text
i   exponents
0   61,273,381,495,609,801,978
1   133,284,420,472,609,801,951
2   61,198,335,472,609,746,883
3   126,324,433,495,609,746,910
4   126,198,444,489,718,746,951

i   labels modulo 65537
0   3414,431,33622,1065,34155,59991,30525
1   47705,45093,29441,4938,34155,59991,57044
2   3414,22499,2130,4938,34155,32106,21079
3   10048,32839,32984,1065,34155,32106,4893
4   10048,22499,55315,30087,15161,32106,57044
```

Outside C the complete pair intersections are

```text
01: 34155,59991       02: 3414,34155     03: 1065,34155
04: empty             12: 4938,34155     13: 34155
14: 57044             23: 32106,34155    24: 22499,32106
34: 10048,32106
```

The nonempty higher outside intersections are 012,013,023,123 and 0123,
each {34155}, and 234={32106}. All other triple, quadruple and quintuple
outside intersections are empty. Every full intersection also contains C.
In particular C is exactly the common intersection of all five supports;
no pair-only assumption is made. The individual auxiliary polynomial
values and all 26 full subset intersections are retained in the certificate.
Distinct auxiliary quadratics meet in at most two graph points; L030's
proved incidence avoidance on this T applies to every triple of them.
Consequently these B_i are independent in the old local edge systems,
without presuming that the injection preserves field operations. Mapping
L030's four dummy points to g^1020,...,g^1023 extends the injection to
the full bijection onto H minus C required by that result.

**Necessary reduced equations for every tuple row.** Put
G_C(X)=product_(c in C)(X-c), of degree 61. Fix any row a of a putative
realization. Since all five messages agree with Y on C, P_i,a-P_4,a
vanishes on C. Repeated use of the factor theorem at distinct roots gives

\[
 P_{i,a}-P_{4,a}=G_C h_{i,a},\qquad \deg h_{i,a}\le2,
 \quad 0\le i\le3;\qquad h_{4,a}=0.
\]

Zero differences are included. For x outside C, G_C(x) is nonzero.
If x lies in several S_i, all their P_i,a(x) equal Y_a(x), so all
their h_i,a(x) are equal. Choose the least incident index as anchor,
and impose one equality with each other incident index. Such a star
imposes all pair equalities at that point by subtraction. This keeps
every higher overlap; extra center agreements can only add equations.

Write the twelve coefficients of h_0,a,...,h_3,a in constant,linear,
quadratic order as v_a. With V(x)=(1,x,x^2), each equality h_i(x)-h_j(x)
gives the signed blocks +V(x) and -V(x), omitting the block for index 4.
The complete star list, ordered by actual label then other index, is

```text
x       anchor  other
1065       0      3
3414       0      2
4938       1      2
10048      3      4
22499      2      4
32106      2      3
32106      2      4
34155      0      1
34155      0      2
34155      0      3
57044      1      4
59991      0      1
```

Thus M v_a=0 over F, where the full E-matrix M is

```text
1 1065 20096 0 0 0 0 0 0 65536 64472 45441
1 3414 55347 0 0 0 65536 62123 10190 0 0 0
0 0 0 1 4938 4080 65536 60599 61457 0 0 0
0 0 0 0 0 0 0 0 0 1 10048 35324
0 0 0 0 0 0 1 22499 62750 0 0 0
0 0 0 0 0 0 1 32106 29300 65536 33431 36237
0 0 0 0 0 0 1 32106 29300 0 0 0
1 34155 5425 65536 31382 60112 0 0 0 0 0 0
1 34155 5425 0 0 0 65536 31382 60112 0 0 0
1 34155 5425 0 0 0 0 0 0 65536 31382 60112
0 0 0 1 57044 40349 0 0 0 0 0 0
1 59991 21263 65536 5546 44274 0 0 0 0 0 0
```

**Complete exact inverse certificate.** All following entries are in E.
The matrix U has the displayed rows:

```text
25656 54771 15856 16550 64795 58208 51877 44990 38716 63760 63390 34256
60619 56598 63002 11674 18592 58221 58756 29122 15969 23908 42052 10395
11654 55435 2056 49707 26111 43402 39828 4974 51850 60188 15428 12510
46293 13547 146 665 62631 20119 14979 39138 18499 65327 52800 13807
14108 64065 8676 27411 38233 42655 56578 38834 64725 36185 8852 44231
10146 14810 43040 14055 11699 25594 48123 24250 27566 43852 57197 10450
360 47847 58153 5382 53376 55012 38218 41808 40605 15547 34099 50444
47226 27776 5659 44105 32099 55648 13043 18727 1818 6768 41827 28759
13493 23287 10150 34601 18306 25136 50964 24683 60969 61509 27203 12670
29548 62677 15811 24650 2775 32776 34860 32322 57460 27862 3253 52279
24530 43467 50286 6759 6061 38538 57633 8814 8479 9228 60621 36556
25111 2174 15067 1522 22868 25913 14151 28227 45691 16035 26996 13836
```

Direct modular multiplication checks all entries of UM=MU=I_12.
Independently, fraction-free elimination of the displayed integer lifts
gives det(M)=-49740849785522550165823979466653588692992014892312,
whose residue modulo 65537 is 26669, nonzero. Exact divisions and the
complete integer elimination trace are saved. The determinant residue
also agrees with the product of the modular elementary-operation factors.
The inverse identity alone is already a sufficient rank certificate.

The E->F embedding preserves UM=I, so from Mv_a=0 follows v_a=0 in
each row, hence P_i,a=P_4,a for all i. This proves the equality conclusion
for arbitrary m, without descent, scalar projection, or any assumption
about distinction in an individual row. It precludes pairwise distinct
messages. It does not assert that a singular matrix would realize them.

**Bounded-search provenance and verification.** Run
`python3 scripts/finite-support/embedded_quadratic_search.py` from this
notebook. The full certificate is
`scripts/finite-support/embedded-quadratic-search-results.json`.
The exact assessed pool has 363 lexicographically ordered coefficient
triples. The prescribed LCG, including singleton ties, makes 49 draws
through trials 0,...,10. Trial 10 has size 5 and ordered zero-based pool
indices (80,280,0,176,85), giving precisely the five polynomials above.
Every preceding trial has positive augmented-rank increment for every
pair map. Trial 10 has rank 12 in 12 columns and every pair augmentation
still has rank 12. The first reported pair is (0,1); its explicit W M=D_01
identity is also saved. The search stops there, before trial 11, as required.

All 285 checks pass, with no failures: generator order and injection,
distinct pool graphs, every tested support cardinality and higher
intersection, direct signed-incidence reconstruction, complete invertible
operation replay and UM=R identities, all pair augmented identities,
both inverse identities, all ten trial-10 pair-map row-space identities,
and the independent determinant check. Full pool, draw eligible lists,
candidate order, growth ties, matrices, transformations, row operations,
pair maps and augmented matrices are saved, including repeated trials
if any. The complete trial-10 matrix, inverse, polynomials, labels,
intersections and determinant were inspected; previews are not used as
mathematical evidence. These are finite certificate checks accompanying
the row-wise proof, not the later separate critical audit.

**Separate critical audit (2026-10-10, step 142).** The unchanged
SPECIALIZE assessment
[critical-audit scope](../drafts/literature/2026-10-10-embedded-quadratic-critical-audit.md)
was saved before this audit. Its source comparison imports AGL v3
Definition 2.5 and Lemma 2.7, cited above, and retains Shangguan–Tamo,
*Combinatorial list-decoding of Reed–Solomon codes beyond the Johnson
radius*, [arXiv:1911.01502v1](https://arxiv.org/pdf/1911.01502v1),
4 November 2019, Lemma 4.3, printed pp. 11–12, for common-root removal.
The elementary factor-theorem application above is written explicitly
because this instance permits arbitrary overlaps, zero differences,
selected rather than exact agreement supports, and extension-field tuple
rows. No generic-rank theorem or characteristic-two unsigned matrix is used.

Run `python3 scripts/finite-support/audit_embedded_quadratic.py`.
The independent implementation imports no original search functions and
does not run the search. It reads and reconstructs all eleven saved trials;
growth-score checks evaluate only the prescribed pool against recorded
prefixes. It checks the entire 363-element pool, all 49 LCG draws including
singleton ties, every eligible list and selected index, and the exact
early stop. All 94 pair tests before trial 10 have positive augmented-rank
increment; the ten final tests have increment zero. These are provenance
checks, not positive-realization claims about the preceding candidates.

Every graph value, exponent, actual label, support, subset intersection,
signed star and matrix is reconstructed. In particular all 26 final
subset intersections are checked, including empty ones and the common
61-point core. The injection on 959 graph points and the four dummy labels
is checked against all 1024 distinct subgroup powers. The canonical
printed coefficient triples, exponent/label rows, signed stars, matrix
and inverse agree entry by entry with the reconstructed evidence.

For each base and pair-augmented matrix, the audit replays every invertible
row operation on both the matrix and an identity matrix, checks the whole
transformation and RREF identities including all zero rows, and independently
computes rank by column-space elimination. This covers 104 pair tests and
17077 recorded operations, including 111 operations for the final base
matrix. It checks both full inverse identities and all ten final pair-map
identities. Rational Gaussian elimination, choosing the last available
pivot rather than the original first-pivot integer method, independently
gives the displayed integer determinant and residue 26669. Separately,
every saved Bareiss state and all 506 exact divisions are checked; the
modular operation determinant agrees as well.

The full independent certificate is
`scripts/finite-support/embedded-quadratic-critical-audit-results.json`.
All 2343 checks pass with zero failures; achieved and required full rank
are both 12. The original certificate is unchanged, with SHA-256
`40157ba7440ef639ec238405c7c25f5b03ec1b07b6d5d69b10abb2974a985b49`.
Complete arrays and identities are processed, not sampled from previews.

The logical review retains the following necessity argument. Distinct core
roots divide every difference, even the zero difference; degree less than
64 leaves a quotient of degree at most two. The core factor is nonzero at
every outside label. At each such label all incident messages agree, so
the full signed star is necessary even with higher overlaps or additional
agreements. For each tuple row the twelve quotient coefficients lie in F;
the prime-field inverse identity remains valid in F and forces them all
to vanish. No common scalar row distinguishing all messages, descent,
or singularity converse is assumed. L030 applies through the completed
set bijection and its incidence-only exclusion; field operations are not
transported. Its previously audited general incidence result is imported,
not claimed to have been fully reaudited here. C001a/C012a fix the instance
and its unchanged bracket. The direct DAG inputs therefore remain unchanged.

This audit verifies the existing finite REPRODUCTION and makes its
additional actual-label restriction available for later use. It proves
no quantitative cap, other-embedding statement, cross-core compatibility,
67/68-agreement safety, or result beyond the assessed source methods.

## Mathlib

Full matching obstruction: **not checked** in Mathlib. Supporting
factor-theorem, polynomial root bounds, finite-field and matrix identities
are standard inputs; no specific Mathlib coverage is asserted. The AGL
scalar signed-matrix theorem is the precise imported source method.
Its tuple specialization and this finite instance are justified above;
no theorem for actual-label caps or the unresolved safety boundary is
imported or claimed.
