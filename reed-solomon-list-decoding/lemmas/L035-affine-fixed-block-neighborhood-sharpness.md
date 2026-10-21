# L035 — Exact sharpness of the anchored fixed-block graph

## Hypotheses

Use C001a's actual subgroup H of size 1024 in E=F_65537. Fix any
60-subset C of H and any eight-subset A of H minus C. Put
X=H minus (C union A), so |X|=956. Let V be all eight-subsets B of
H minus C with |A intersect B|=3. Define a finite simple graph G on V.
Distinct B,B' are adjacent when either:

1. |B intersect B'|>=4; or
2. A intersect B intersect B' is empty, all three pair intersections
   of A,B,B' have size three, and the matrix of ascending coefficients
   of the three monic overlap cubics has rank three over E.

The second clause is exactly the forbidden anchored L033 case. Its
incidence hypotheses ensure disjoint overlap triples and two private
points per block. Rank-two cases are retained. This graph encodes only
these restrictions, not full L034 admissibility.

Order A by its integer E-residues and its 56 triples lexicographically.
Assign the slopes s_T=0,...,55 in the auxiliary field F_191 in that
order. Put Omega=({0,1,2,3,4} times F_191) disjoint union {*}. For
every bijection sigma:Omega -> X define

\[
 R_{T,b}=\{(x,s_Tx+b):x=0,1,2,3,4\},\qquad
 \mathcal I_\sigma=\{T\cup\sigma(R_{T,b}):T\in\tbinom A3,
                                      b\in\mathbb F_{191}\}.
\]

## Conclusion

For every C,A and every such bijection, I_sigma is independent in G
and has cardinality 10696. Moreover

\[
 \alpha(G)=T(3,8,5,956,10)=10696,
\]

where T is the ordinary doubly constant-weight maximum, with exact
head/tail weights three/five and binary minimum distance ten.
Thus adding these anchored labeled edges cannot improve this ordinary
neighborhood cardinality cap, at any actual C,A. This stops the specified
graph relaxation alone. It does not assert that I_sigma satisfies L033
on triples not containing A, any L031 quadruple condition, or the full
L034 neighborhood requirements. No whole-family bound, unsafe RS list,
safety at 68 or 67 agreements, or change to the 955–957 bracket follows.

## Proof

**Assessed sources and purpose.** The preexisting SPECIALIZE assessment is
`drafts/literature/2026-10-08-affine-fixed-block-neighborhood-test.md`.
Import Agrell–Vardy–Zeger, *Upper Bounds for Constant-Weight Codes*,
June 24, 2000 manuscript, [primary institutional PDF](https://publications.lib.chalmers.se/records/fulltext/local_14986.pdf),
definition (5), printed p. 3; Theorem 8 (37), p. 6; Theorem 32, p. 16;
and Theorem 36 (142), p. 17. The journal version is IEEE Trans. Inform.
Theory 46(7) (2000), 2373–2395, DOI 10.1109/18.887851; page numbers here
refer to the manuscript. The reused source assessment inspected the exact
statements. They supply exact-weight shortening, zero-head deletion and
the disjoint-support base, without evaluation labels. Their elementary
proofs are omitted in that source. The brief applicability justification
below checks the precise finite implementation and every floor.

L029 supplies the proved auxiliary affine intersection method and
primality of 191. The changed 56 triple classes and exact upper/lower
comparison require this specialization; L029's old 21-class link
certificate is not a matching theorem. L033 supplies the actual anchored
forbidden criterion. L034 shows why these are necessary conditions on
neighborhoods of actual selected-support families; it does not give the
sharpness asserted here. This is RESEARCH/REPRODUCTION of assessed
methods, not a claim of mathematical novelty beyond the checked sources.

**Ordinary upper bound.** A graph-independent family has pair intersections
at most three. Binary indicators on the disjoint parts A,X have weights
3,5, total weight eight and distance
16-2|B intersect B'|>=10. Hence alpha(G)<=T(3,8,5,956,10).
The source's octant conditions hold initially and at every used stage:
n1<=956, 2w1<=n1 and 2*5<=956, for
(w1,n1)=(3,8),(2,7),(1,6),(0,5).

Theorem 36 (142) gives

\[
 T(w_1,n_1,5,956,10)
 \le\left\lfloor\frac{n_1}{w_1}
                   T(w_1-1,n_1-1,5,956,10)\right\rfloor
 \quad(w_1>0).
\]

For this application, count incidences of a word with a head coordinate
equal to one. Among n1 coordinates one contains at least w1 times
the family size divided by n1 words. Retain those words and delete that
coordinate. Deleting a common one preserves all distances, the tail
weight and injectivity; the head weight drops by one. Thus w1 times
the original integer size is at most n1 times the shorter maximum,
which justifies the displayed floor, including empty codes.

By Theorem 32, a zero-weight head can be deleted:
T(0,5,5,956,10)=A(956,10,5). Theorem 8 (37) gives
A(956,10,5)=floor(956/5)=191. Indeed two weight-five supports at distance
at least ten are disjoint, so their size times five is at most 956;
191 disjoint five-subsets attain the bound. This verifies the finite
base case rather than importing a stronger packing statement.
The exact nested evaluation is

\[
 \left\lfloor\frac83\left\lfloor\frac72
        \left\lfloor6\left\lfloor\frac{956}5\right\rfloor
                     \right\rfloor\right\rfloor\right\rfloor
 =\left\lfloor\frac83\left\lfloor\frac72(1146)
                                    \right\rfloor\right\rfloor
 =10696.
\]

From inside outward the caps are 191,1146,4011,10696. The division
remainders are respectively 1,0,0,0. No T' bounded-head-weight maximum,
distance-changing puncture, or unfloored replacement is used.

**Construction and pair conflicts.** By L029, 191 is prime, and its
five distinct evaluation coordinates define a 956-point Omega with
one spare point. All 56 slopes are distinct in F_191. For a fixed T,
different intercepts give disjoint outside graphs: equality of points
forces the same x and then the same b. For T!=T', equality of a point
in the two graphs requires

\[
 (s_T-s_{T'})x=b'-b.
\]

The coefficient is nonzero, so there is at most one possible evaluation
coordinate x. Hence their outside intersections have size at most one.
Each B=T union sigma(R_(T,b)) belongs to V. Its intersection with A
recovers T. Within one T, different intercepts yield different nonempty
outside parts. The family therefore has 56*191=10696 distinct members.

Two members with the same T meet exactly in T, of size three. Two
members with different T,T' meet in at most |T intersect T'|+1<=3.
There is no pair-conflict edge. These intersection statements hold for
every sigma, as any bijection preserves intersections and its images
are outside A. They also prove the ordinary lower bound on T.

**Every anchored incidence case.** For any two distinct members B,B',
A intersect B intersect B'=T intersect T'. If this is nonempty,
the anchored L033 edge does not apply, regardless of pair intersections
or coefficient ranks. This covers equal T and all overlapping T,T'.
If it is empty, T and T' are disjoint, hence distinct; B intersect B'
consists only of their outside intersection, of size at most one.
It cannot have the required size three. Thus no pair of constructed
vertices even meets the complete incidence hypotheses of an anchored
L033 edge. There are no requisite cubic matrices to test. This is a
label-independent incidence argument for every actual labeling, not an
assumption that outside permutations preserve coefficient ranks. It
retains all singular cases and uses no generic-rank or field-descent
claim. The independent construction and ordinary upper bound prove
both equalities in the conclusion.

**Exact finite check.** Run `python3 scripts/finite-support/affine_neighborhood.py`.
It writes `scripts/finite-support/affine-neighborhood-results.json`, with
all 10696 abstract vertices, 56 same-slope records, all 1540 distinct
slope-pair records, all 191 offset intersection sizes per such pair,
the full pair histogram, every shortening dividend/divisor/remainder,
all check outcomes and failures. No actual C,A is sampled.

For each same-slope class it enumerates every unordered intercept pair.
For distinct slopes it directly intersects the graphs at intercepts
0,delta, for every delta in F_191. The common vertical translation
(x,y)->(x,y-b) sends the pair of intercepts b,c to 0,c-b. It preserves
all intersections and the spare point. Each delta therefore represents
exactly 191 pairs for that fixed ordered pair of slope classes. This
proves that the 294140 offset cases plus same-slope checks cover all
57196860 unordered vertex pairs without omitting equal intercepts.
Each distinct-slope offset histogram is {0:186,1:5}. All 15 checks
pass, with no failures; the complete benchmark, aggregate pair histogram,
checks and failures were inspected via the shared JSON inspector.

The symbolic proof above establishes all-label sharpness; the finite
certificate checks its exact parameters and incidence cases. The separate
critical audit below retains the result. Equality parks any stricter
cardinality claim using precisely this graph. Independent restrictions
among neighbors, L031, conversion to L034's cap 184665717, cross-core
consistency, large-list realization, 67-agreement safety and ABF
equivalence remain unresolved. In particular 10696 is a neighborhood
cap, not a cap on the full local family, and must not be substituted
for L034's family cap.

**Separate critical audit, 2026-10-08.** The preexisting assessment
`drafts/literature/2026-10-08-affine-neighborhood-critical-audit.md`
covers this audit. No correction to the theorem or its direct mathematical
inputs was needed. The audit reuses the precise AVZ statements cited
above and L029's prime-field construction; it adds no source or novelty
claim. L033's full incidence criterion and L034's membership proof were
checked against the graph definition, rather than importing their stronger
conclusions as assumptions about the constructed neighborhood.

For the upper bound, the four stages have exact weights (0,5), (1,5),
(2,5), (3,5), head lengths 5,6,7,8 and unchanged tail length 956
and distance ten. A common one is deleted only in a subcode where it
is shared; no distance drops. Injectivity survives deletion. The base
head consists of zeros and is deleted entirely, giving disjoint
five-subsets. The audited divisions are 956=5*191+1,
1146=1*1146, 8022=2*4011, and 32088=3*10696. All octant and positive
divisor hypotheses hold. This verifies every nested floor, not a real
bound subsequently rounded once.

For the lower bound, the recovered head triple and nonempty outside
graph distinguish every slope/intercept pair. A bijection maps outside
points only to X and preserves every intersection. Equal head triples
give pair intersection three; distinct head triples have at most two
common head points and at most one outside point. For an anchored edge,
the triple intersection is exactly the common head. If it is nonempty
the edge's hypotheses fail. If it is empty, the heads are distinct,
so the outside intersection is at most one, whereas the required third
pair intersection is three. These cases exhaust all vertex pairs.
If the forbidden incidence did occur, its empty triple intersection
would make the three overlaps disjoint, leaving exactly two private
points per eight-set; thus the graph's clause really matches L033.
No invariance of actual cubic ranks under a bijection is used. The
argument proves independence for every C,A and every sigma, not merely
for a sample of labels. The ordinary maximum T is sandwiched between
the same construction and the audited upper bound.

Run `python3 scripts/finite-support/audit_affine_neighborhood.py` for
the independent complete certificate audit. It reads the preserved
producer certificate in full and writes
`scripts/finite-support/affine-neighborhood-audit-results.json`, including
its source SHA-256, every reconstructed same-slope/offset record, exact
aggregate counts, shortening evidence and all failures. It imports no
producer code. Every stored vertex is decoded into five distinct
coordinates and checked against its line equation, its lexicographic
head and its complete slope/intercept key. All 10696 keys and supports
are distinct. The 955 used points each lie in 56 graphs, and the spare
point lies in none.

The audit enumerates all pairs sharing an outside point directly from
these incidence buckets. There are 1470700 such unordered pairs; none
appears in two buckets. Thus these are all pairs with positive outside
intersection and each intersection has size one. The full head classes
give 1016120 same-slope pairs and 1540*191^2 distinct-slope pairs.
Subtracting the enumerated positive pairs within each head-intersection
class accounts for every remaining zero-intersection pair. This yields
57196860 pairs in total, with the complete histogram:

```text
(head intersection, outside intersection): number of unordered pairs
(0,0):  9947280
(0,1):   267400
(1,0): 29841840
(1,1):   802200
(2,0): 14920920
(2,1):   401100
(3,0):  1016120
```

Every one of the 56 saved same-slope records and all 294140 offset
entries in the 1540 saved distinct-slope records agrees with this
independent enumeration. Each positive offset is also checked for all
191 common translations, totaling 1470700 translated pairs. Since this
equals the exhaustive positive-pair count, no additional positive case
is hidden among zero offsets. Equal intercepts are delta=0 and included.
Slope pairs are indexed with s<t, so the 191 choices of the first
intercept for each offset give distinct unordered vertex pairs without
identifying the slope classes or introducing a factor of two.

All 1559444 value/record comparisons pass, with no failures; the full
benchmark, coverage, histogram, comparison counts and failures were
inspected. The program verifies complete finite records; the preceding
proof supplies the universal quantifiers and incidence reasoning. It
does not verify any new exclusion among three or four neighbors, an
L034 family cap, cross-core consistency, or common-center realization.
The audit retains ATTEMPTS/024 only for the specified graph. The
955–957 bracket and the other qualifications in the conclusion remain
unchanged. This completes previously pending local verification, with
no progress beyond the assessed mathematical methods.

## Mathlib

Full matching graph sharpness and doubly constant-weight code bounds:
**not checked**. Supporting finite-field intersection, finite incidence
and graph independence theorem names: **not checked**. The precise
AVZ inputs above are imported; no absence or formal verification is
asserted. This result changes the viability of the prescribed relaxation,
not the RS safe-radius bracket or the original challenge status.
