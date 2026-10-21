# L079 — Complete finite cross-ratio exclusion of the affine-plane family

## Hypotheses

Let k=F_97, H its order-sixteen multiplicative subgroup, and F=F_(97^20).
Fix any bijection lambda from L072's abstract points to H. Use its exact
sixteen blocks and L077's ordered quadrilaterals. Suppose there are
sixteen pairwise distinct points t_A of P^1(F) satisfying all 48
identities in L077 (1). Define A,B,C,D by L078's exact four ordered
singleton tuples. They belong to k minus {0,1}.

The application to an L010 equality pencil uses L077's necessary
condition. No moment realization, rational original chart, embedding
of auxiliary F_4, or symmetry of H-labelings is assumed. The separate October 12 critical audit of the direct equality-pencil
application and its complete finite evidence found no defect. This is
a reviewed local family exclusion, not a complete challenge candidate.

## Conclusion

The hypothesized sixteen-point tuple does not exist. Consequently this
exact L072 family cannot be the full-support family of an L010 equality
pencil.

More explicitly, among all 95^4=81,450,625 admissible four-ratio tuples
over k, exactly 847,570 have L078's R=0. Of those, 8,648 have inconsistent
affine equations; 166,898 have a unique affine solution with a collision
among the twelve nonvertical directions; and 672,024 have a unique
solution with those twelve directions distinct. Recovering the three
remaining vertical directions rejects 209,214 of the last group by a
collision. Every remaining 462,810 tuple fails a quadrilateral equation.
Thus zero tuples survive the complete necessary system, against the
required threshold zero. All cases and rejection witnesses are saved
and replayed; this result has explicit computational dependence.

This is local progress toward removing L072's moment-realization
obstruction, not a theorem beyond the sources checked or a certified
originality claim. Other support families, uniform triangle twelve,
extraction and the challenge-definition qualifications remain open.
The global interval remains 11/q–16/q; this is no complete challenge
candidate and gives no new global count bound.

## Proof

### Reduction to a finite ratio universe, including extension-field cases

Normalize only the syndrome line, sending V0 to infinity, M0D0 to
zero and M1D0 to one. These points are distinct by hypothesis. Write
h_j=t_M0Dj, d_j=t_M1Dj and e_j=t_M2Dj. All twelve are finite, h_0=0
and d_0=1. L078 gives its five affine equations

    M(A,B,C,D) (d_1,d_2,d_3,1)^transpose = 0,

and the necessary equation R=0. Use exactly the matrix, normalization,
twelve-equation table and recovered h/e formulas in L078. No factors
vanishing for an admissible ratio are divided out. In particular this
step retains all coefficient-rank drops, and does not assume that
vanishing maximal minors implies affine consistency.

For clarity the original twelve equations are

    e_l-(1-r)h_j-r d_k=0,

with (j,k,l,r), in order, equal to

    (0,1,3,A), (0,2,1,B), (0,3,2,C),
    (1,0,2,1/(1-B)), (1,2,3,D), (1,3,0,(A-1)/A),
    (2,0,3,1/(1-C)), (2,1,0,(B-1)/B), (2,3,1,(D-1)/D),
    (3,0,1,1/(1-A)), (3,1,2,1/(1-D)), (3,2,0,(C-1)/C).

After h0,d0 are fixed, these are twelve affine equations in ten unknowns
h1,h2,h3,d1,d2,d3,e0,e1,e2,e3. Seven successive equations eliminate
e3,e1,e2,h1,h2,h3,e0, with nonzero pivots: the first three, the three
with k=0, and the first equation defining e0. The five remaining
equations are precisely L078's matrix system after clearing nonzero
factors. Thus the original coefficient and augmented ranks are seven
plus the respective reduced ranks. The independent replay also checks
these two equalities for every R-zero tuple using the original system.

The complete rank calculation gives the following cases, not merely
generic ranks:

| Reduced coefficient rank | Reduced augmented rank | Original ranks | Cases | Result |
|---|---|---|---:|---|
| 2 | 3 | 9,10 | 8,648 | inconsistent |
| 3 | 3 | 10,10 | 166,898 | unique, nonvertical collision |
| 3 | 3 | 10,10 | 672,024 | unique, twelve nonvertical points distinct |

Ranks of matrices over k do not change under a field extension: rank is
the largest size of a nonzero minor, and an injective field embedding
preserves every minor's zero/nonzero status. An inconsistent k-system
therefore remains inconsistent over F. In either rank-three reduced
case, its unique solution lies in k, by row reduction over k, and is
also its only solution over F. Hence every possible distinct solution
over F lies in the last row and already has all twelve nonvertical
coordinates in k. This rationality conclusion does not use L075's
rank-27 descent or its unaudited L073/L074 chain.

### All 48 right-hand sides depend on just A,B,C,D

The four ordered abstract singleton sets are

    G_A=(y_1,z_2,w_1,d_1), G_B=(y_2,c,d_6,d_5),
    G_C=(b,z_1,d_2,d_7), G_D=(a,d_4,d_3,w_2).

Every quadrilateral's singleton tuple is a permutation of exactly one
of these sets. There are twelve quadrilaterals per set. This finite
incidence assertion is checked for all 48 cases from L077's formula:
choose i,j,k in auxiliary F_4 with k!=i+j, put
e=i+(u+1)k+uj, and use blocks (V_i,M0D_j,M1D_k,M2D_e). Delete the
three pair intersections from each block to obtain its singleton.
The complete case table, including each resulting permutation, is
`scripts/triangle-incidence/affine-plane-full-ratio-incidence.json`.
The replay compares every row to L077's original complete incidence
certificate, including block order and all four singleton names.

For a group whose cross-ratio is r, a projectivity of its *label*
projective line sends its ordered points to (infinity,0,1,r).
Thus any permutation's ratio is computed with representatives

    q_0=(0,1), q_1=(1,0), q_2=(1,1), q_3=(1,r).

For the recorded permutation pi its numerator and denominator are

    n=[q_pi0,q_pi2][q_pi1,q_pi3],
    z=[q_pi0,q_pi3][q_pi1,q_pi2].

All four q's are distinct since r!=0,1, so z!=0. This use of
cross-ratio invariance does not change lambda, identify two labelings,
or impose a label symmetry on moments. It proves that A,B,C,D alone
determine every right-hand side of the 48 necessary identities.

### Recover the remaining verticals and reject every residual case

Use these three quadrilaterals from L077's reconstruction table:

| Unknown | Other blocks | Ordered singleton tuple | Right side |
|---|---|---|---|
| V1 | M0D0,M1D0,M2D1 | d_2,z_1,d_7,b | (C-1)/C |
| V2 | M0D0,M1D0,M2D2 | w_1,z_2,d_1,y_1 | (A-1)/A |
| V3 | M0D0,M1D0,M2D3 | d_6,c,d_5,y_2 | (B-1)/B |

For finite e and r!=0,1, solve chi(v,0,1,e)=r. Since
chi(v,0,1,e)=e(1-v)/(e-v), its homogeneous solution is

    v = (e-r, e(1-r)),

in the convention (1,z) for a finite point. The other three points
are distinct in the retained cases, so e!=0,1; the displayed vector
is nonzero. It also retains e=r, which gives infinity and is rejected
only by the required distinctness from V0. There is exactly one
projective solution: the homogeneous equation is nonzero and has a
one-dimensional kernel. It is over k and is the same unique solution
over F. Use e1,e2,e3 and the respective right sides in the table.

For every one of the 672,024 residual cases, form all sixteen nonzero
homogeneous directions. If any pair has determinant zero, reject the
case; the complete certificate records one witnessing pair. This
rejects 209,214. For each remaining case and each of the 48 ordered
quadrilaterals, compute its direction numerator L and denominator J
using the same bracket convention. Its required equality is

    L z - J n = 0.

Pairwise distinctness ensures nonzero direction denominators. The
complete check rejects all remaining 462,810 cases. A zero-based
index n refers to the i,j,k lexicographic order of the incidence table.
The first failed quadrilateral counts are

| Index | Cases |
|---:|---:|
| 13 | 452,088 |
| 14 | 10,469 |
| 15 | 252 |
| 16 | 1 |

For the last case, (A,B,C,D)=(8,9,78,73), the index-16 quadrilateral
is (V1,M0D1,M1D2,M2D2), with singletons (d_2,b,z_1,d_7).
The independent homogeneous recovery gives label numerator/denominator
(1,20), direction numerator/denominator (39,29), and
39*20-29*1=72!=0 modulo 97. Its complete sixteen-direction witness
is in `scripts/triangle-incidence/affine-plane-full-ratio-replay.json`,
field `selected_last_branch_witness`. This regression illustrates the
last branch; the proof uses every case, not this example or a preview.

All possible F-solutions were reduced to these finite k-cases, and all
are rejected. Applying L077 supplies the equality-pencil exclusion.
The proof does not assume that passing cross-ratios would suffice for
moment compatibility. No case passes, so no original-pencil construction
or inference of sufficiency is needed.

### Complete certificates, algorithms and reproduction obligations

All paths and commands below are relative to this notebook.

1. Compile `scripts/triangle-incidence/affine_plane_affine_rank.cpp`
   with `c++ -std=c++17 -O2` to `/tmp/mca-affine-rank`, then run
   `/tmp/mca-affine-rank scripts/triangle-incidence/affine-plane-affine-rank`.
   It visits every A,B,C in {2,...,96}. Write R as
   V^2 D^2+(-2UV+4BC(1-A)(1-B))D+U^2, with L078's U,V.
   If V=0 its linear coefficient is nonzero. Otherwise enumerate both
   square roots of the discriminant in k, including zero once, and
   apply the quadratic formula; exclude only D=0,1. This exhausts
   every admissible R-zero tuple. Gaussian elimination computes both
   reduced ranks; a consistent rank-three system is solved, checked
   against all five reduced and all twelve original equations, and
   tested for nonvertical collisions. It saves every R-zero case in
   `affine-plane-affine-rank-rows.csv`, every singular system with full
   RREF in `affine-plane-affine-rank-rank-drops.jsonl`, and complete
   counts/failures in `affine-plane-affine-rank.json`, all in that directory.
2. Compile `scripts/triangle-incidence/verify_affine_plane_affine_rank.cpp`
   to `/tmp/mca-affine-rank-verify` with the same flags, then run
   `/tmp/mca-affine-rank-verify scripts/triangle-incidence/affine-plane-affine-rank`.
   It directly visits all 95^4 tuples, substitutes R and checks exact
   equality with the producer's case set, rejecting duplicates. It
   independently builds and eliminates the original twelve-by-eleven
   affine system and compares ranks, solutions and statuses for all
   847,570 rows. Its full per-case output and summary are
   `affine-plane-affine-rank-replay.csv` and `-replay.json`.
3. Compile `scripts/triangle-incidence/affine_plane_full_ratio.cpp` to
   `/tmp/mca-full-ratio` with the same flags, then run
   `/tmp/mca-full-ratio scripts/triangle-incidence/affine-plane-affine-rank-rows.csv scripts/triangle-incidence/affine-plane-full-ratio`.
   It constructs all 48 incidence/permutation rows, recovers the three
   verticals, checks all sixteen directions and all 48 equations, and
   saves every one of the 672,024 rejection witnesses in
   `affine-plane-full-ratio-rows.csv`, the complete incidence table in
   `-incidence.json`, the empty passing list in `-passing.jsonl`, and
   full counts/failures in `affine-plane-full-ratio.json`.
4. Run `python3 scripts/triangle-incidence/verify_affine_plane_full_ratio.py`.
   It compares the entire incidence table with L077's original table.
   It reads every distinct-V0 source case and its corresponding rejection
   row, rejects missing/extra/reordered cases, and independently recovers
   V1,V2,V3 by solving the homogeneous first-slot equation, instead of
   using the producer's three explicit vertical formulas. It verifies
   the supplied collision or nonzero equation difference for every
   candidate. It saves complete totals, the selected last-branch witness
   and all failures in `affine-plane-full-ratio-replay.json`.

Every executed check passed with zero failures. The actual counts are
the tables above; the required thresholds are complete case-set equality,
all original systems and all 672,024 final rejection witnesses verified,
and zero final survivors. The final witness verifier need only check
the supplied failed equation or collided pair: one valid violation
excludes a necessary-system solution. The producer checks all 48 equations.
The replays use different equation and recovery paths but share field
arithmetic, the C++ compiler for the first stage and the L077/L078 input
identities. They are not a separate critical review of those inputs.
No floating point, random labels, positive-only sampling, or omitted
singular/infinity branch enters the calculation. The later audit below
checks these programs, their complete artifacts and the essential direct
input proofs.

### Separate critical audit, 12 October 2026

The scoped audit read the full L010/L072/L077/L078/L079 proofs and all
seven essential incidence, polynomial, producer and verifier programs.
It found no mathematical defect in this direct equality-pencil exclusion.
It does not review L077's alternative rank-27 application through
L073–L076, or establish rank 28 independently of those inputs.

For the direct input chain, L010's shifted Vandermonde columns are
independent on every set of at most eight labels. A full error has
nonzero syndrome; two different blocks cannot have proportional full
syndromes, since their union has at most eight labels. This establishes
the two-dimensional syndrome plane and every required direction
separation without the rank-27 chain. L010's full equality proof retains
same-support failure, singular multiplicities and full weight before
this application. L072's explicit blocks meet the cited construction's
order-four hypotheses. L077's shortened code is exactly Q times the
linear polynomials; the four singleton coordinates make E injective.
The ordered kernel-functionals and syndrome determinants both give
bc/(ad), with all denominators nonzero. These checks validate the
necessary cross-ratios over the full extension field.

For L078, the first three equations and the k=0 equations have nonzero
pivots because A,B,C and their complements are nonzero. Eliminating e0
adds a seventh nonzero pivot. Substitution gives all five displayed
rows, including both e0 comparisons; expansion of all five minors was
replayed as exact polynomial arithmetic. If V=0, the nonzero linear
coefficient retains the degree-drop branch. The original-system replay
verifies both rank offsets for every retained tuple, so vanishing
maximal minors is never confused with affine consistency. Every one of
the 8,648 rank drops is inconsistent; there is no unsearched extension
family of solutions. Unique rational solutions remain unique over F
by invariance of nonzero minors under field extension.

Reproduction command:
`python3 scripts/triangle-incidence/audit_affine_plane_ratio.py`.
The full audit certificate is
`scripts/triangle-incidence/affine-plane-critical-audit.json`.
It records commands, exit codes, complete command output, pre/post hashes
and every additional equation-table comparison. All thirteen existing
artifacts reproduce byte for byte, with zero failures. The exhaustive
original-system replay covers 81,450,625/81,450,625 tuples and
847,570/847,570 R-zero systems. The full witness replay verifies
672,024/672,024 rejections, including 209,214 collisions and 462,810
nonzero equation differences, against required zero survivors.

The incidence replay reconstructs all 256 class choices and exactly 48
quadrilaterals, compares all 48 ordered singleton permutations, and
finds twelve per ratio group. Additional audit checks bridge each of
the twelve written V0 equations to its actual incidence permutation
for every one of 95 admissible values (1,140/1,140 checks). They also
bridge the three vertical ratios for all values (285/285 checks).
These are complete finite identities on their stated domain, not
sampled regressions. The first-slot homogeneous equation has a unique
nonzero solution because its other three points and label ratio are
distinct; e=r is retained as infinity. The final verifier independently
solves that equation and validates one actual violation for every
residual case. One such violation suffices for exclusion even without
rechecking the producer's claim that it is the first violation.

The programs use exact integer residues; the inspected intermediates
fit their integer types. The original-system verifier computes inverses
by exponentiation, while the producer uses an inverse table. Complete
coverage is checked by direct D substitution rather than the producer's
quadratic-root enumeration. The audit still depends on ordinary Python,
C++ compilation and arithmetic execution; it is not a Lean verification.
The full fixed-family conclusion is accepted within that explicit
computational scope. Other families, extraction, triangle twelve and
the challenge-definition qualifications remain unresolved.

## Mathlib

Coverage of this exact family-specific finite cross-ratio exclusion is
not checked; unknown availability is not absence. No Mathlib theorem is
used. L077 supplies the necessary quadrilateral identities, L078 their
matrix reduction and determinant obstruction, and L072 the incidence
table. The auxiliary design's primary citation is recorded in L072.
The elementary finite-field, homogeneous linear-equation and rank
arguments needed for this specialization are written above. The reused
EXPLORE assessment did not identify a matching source theorem; this
licenses the bounded computation, not an originality claim or a reproof
of the general design/MDS theorems.
