# L109 — Capacitated two-distance dual nonseparation

## Hypotheses

Let V be all 68-subsets of a 1024-point set, H=binomial(1024,68),
and i(A,B)=|A\B|. Import the exact L021 vector a_i, 5<=i<=68, and
L098's fixed pair prescription

    N=floor(65537^28/2^128)+1,
    U=binomial(1024,64)/binomial(68,64),
    g_i=binomial(68,i)binomial(956,i),
    alpha=2(N-1)/(U-1),
    c_0=1, c_1=...=c_4=0, c_i=alpha*a_i/(2g_i) (i>=5).

In particular N>2, 0<alpha<1, c_i>0 for i>=5, and sum_i g_i*c_i=N.
For each unordered distinct edge e={A,B} put d_e=(N-2)c_i(A,B).
For each unordered triangle T of three distinct supports put
b_T=min_(e in T)c_i(e). Let W be its ordinary edge/triangle incidence
matrix. Test the finite box image W{z:0<=z_T<=b_T}; this bounded image
is not itself a cone. All actual triangles, including null-capacity
triangles, are included. No distance-only equality on primal variables
is imposed and no original t-s class is discarded.

Restrict edge multipliers to lambda_e=x when i(e)=5, lambda_e=y when
i(e)=6, and lambda_e=0 otherwise, for arbitrary real x,y. Define

    F(x,y)=sum_T b_T max(sum_(e in T)lambda_e,0)-sum_e lambda_e*d_e.

The separator convention is F<0. All c_i and N are frozen; triple
variables are free within this box. Boolean lower scalar rows, source
PSD conditions and RS labels are not part of this test.

## Conclusion

Let q be the least common denominator of all c_i, P_i=q*c_i, and

    S=3(N-2)(g_5*P_5+g_6*P_6)>0.

Then for all real x,y,

    F(x,y) >= H*S/(6q) * (4/6521) * (|x|+|y|).

Equality is attained at (x,y)=(-1,0); F(0,0)=0. In particular no signed
edge weight supported on half-distances 5 and 6 separates these demands
from this box image. This parks precisely this diagnostic. It does not
prove membership in the box image, any full source lift, shared scalar
feasibility, PSD, an actual packing or an RS list. The 955–957 bracket
is unchanged. This is a local REPRODUCTION of the assessed box-dual
method, not a claim of progress beyond the sources checked.

## Proof

**Imported method and necessary specialization.** Reuse the inspected
Boyd–Vandenberghe, *Convex Optimization*, Cambridge University Press
(2004), [author PDF](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf),
Section 5.7.3, Example 5.9, (5.68)–(5.71), printed pp.257–258, and
Section 5.8.1, pp.258–259. These give the finite box LP dual and
homogeneous feasibility certificate. Eliminate fixed b_T=0 coordinates
when applying the example with strictly separated endpoints. The local
support expression above retains their zero contributions explicitly.
No strong-duality or strict-feasibility assumption is needed to test a
separator. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-22-two-distance-capacitated-triangle-test.md`.

L098's normalized homogeneous contraction says that for a fixed edge
A,B the sum over all third supports Z is N*c_i. The two different terms
Z=A and Z=B each have value c_i and coefficient one. Removing them gives
the distinct-edge demand (N-2)c_i, including at c_i=0. At i=0 those
supports coincide; that row is only sum_i g_i*c_i=N and supplies no
edge demand. Division is only by the positive singleton normalization
N/H, never by c_i. L105's scalar specialization of Schrijver, *IEEE TIT*
51 (2005), 2859–2866, DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.B (62)–(65), printed p.7, bounds each distinct normalized moment
by the minimum of its three pair coordinates, with nonnegativity.
The source hypotheses, impossible-orbit qualification and unused (61)
prefactor remain as in foundations/04; the cardinality and indicator
inputs remain as in foundations/12,13 and L098.

Consequently a full source assignment at these pairs gives a weight
z_T on every actual unordered triangle with Wz=d and 0<=z_T<=b_T.
Dropping all other conditions is a necessary relaxation. For this box,
the maximization version of the cited dual is exactly F: on coordinate
T the maximum of z_T times its multiplier sum is b_T times the positive
part of that sum. Thus any feasible z has
sum_e lambda_e*d_e <= sum_T b_T max(sum_(e in T)lambda_e,0).
This fixes the sign without assuming the unproved feasibility. Distinct
primal coordinates are independently maximized only in this relaxation.

**Actual source accounting.** For a fixed anchor A, the original indices
range over 0<=i,j<=68,

    max(0,i+j-68)<=t<=min(i,j),
    max(0,i+j-956)<=s<=min(i,j), h=i+j-t-s.

In membership-bit order 000,001,010,011,100,101,110,111 for A,B,Z,
the eight atom sizes are

    (956-i-j+s, t, i-s, j-t, j-s, i-t, s, 68-i-j+t).       (1)

These ranges are exactly nonnegativity of (1). Their sum is 1024;
each support has size 68. Conversely partitioning the ground set into
these atoms realizes every such index, including repeated supports.
Selecting the removed and added sets relative to A gives the exact
number of ordered (B,Z) per anchor,

    G=A_t B_s,
    A_t=68!/[t!(i-t)!(j-t)!(68-i-j+t)!],
    B_s=956!/[s!(i-s)!(j-s)!(956-i-j+s)!].                 (2)

Factorial cancellation gives

    G=g_i D,
    D=binomial(i,t)binomial(68-i,j-t)
      binomial(i,s)binomial(956-i,j-s).

Every original coefficient is positive; forbidden positive distances
are actual orbits, with zero capacity, not impossible entries.

Here is a symbolic check of all six presentations for every original
entry, independent of the constructor's presentation loop. Permuting
the three bit labels in (1) gives all six orders of the three supports.
For an anchor a and other supports b,c, the new t is its singleton atom
n_(1<<a), and the new s is the opposite pair-only atom
n_((1<<b)|(1<<c)). The three singleton-minus-opposite-pair differences
are t-s, (i-s)-(i-t)=t-s, and (j-s)-(j-t)=t-s. Thus t-s is preserved
in every order, and the new distances are the corresponding permutation
of (i,j,h). All ranges still hold because they describe the permuted
nonnegative atoms. Moreover

    H*G=1024! / product_(r=0)^7 n_r!

is unchanged by permuting these atoms. Hence the source multiplicity,
distinctness and capacity are unchanged in all six presentations.
This argument includes zero atoms, repeated distances and repeated
supports. For distinct supports the action on their ordered
presentations is free: there are six orders even when some index keys
coincide. Thus dividing total ordered counts by six, not by the number
of distinct keys, counts each unordered triangle once.

For i>0 the repeated Z terms have (j,t,s)=(0,0,0),(i,i,i), D=1 each.
For i=0, t=s=0, D=g_j and all such triples are repeated. There are
3*68+1=205 repeated original entries. Distinctness is exactly i,j,h>0.
The actual source ranges have 1,500,625 entries; all are retained.
The finite checks below also retain all 10,232 entries with a forbidden
positive distance and confirm their capacities are zero.

**Exact support aggregation, without a primal quotient.** Put
m=# of distances among i,j,h equal to 5, and k=# equal to 6. For each
0<=m,k with m+k<=3 let

    K_(m,k)=sum G*min(P_i,P_j,P_h),                       (3)

where the sum is over all distinct original entries with these counts.
These are sums of independently maximized contributions; (3) does not
equate primal moments with different t-s. Every unordered edge of
distance i has H*g_i/2 presentations counted over endpoints. Therefore

    F(x,y)=H/(6q) * J(x,y),
    J(x,y)=sum_(m,k) K_(m,k) max(mx+ky,0)
           -3(N-2)(g_5*P_5*x+g_6*P_6*y).               (4)

The factor 3 in the demand term is the conversion of 1/2 to 1/6,
not a third repetition. As total-count checks,
sum_i g_i=H, sum_(distinct entries)G=(H-1)(H-2), and
H/6 times that last sum is binomial(H,3). Each bucket separately has
integral unordered count H*sum G/6. Null-capacity entries are counted
before their contributions vanish.

**Complete two-weight test.** The function J is positively homogeneous.
It suffices to minimize it on |x|+|y|=1, plus the zero vector separately.
Every nonconstant positive-part argument has m,k nonnegative integers,
m+k<=3; its possible zero line is one of
x=0, y=0, x+y=0, 2x+y=0, x+2y=0. Include the axes also as diamond
corners. In cyclic order the complete endpoints, before normalization
by |x|+|y|, are

    (1,0), (0,1), (-1,2), (-1,1), (-2,1),
    (-1,0), (0,-1), (1,-2), (1,-1), (2,-1).             (5)

Successive normalized endpoints lie on the same closed diamond side.
For every listed line its values at successive endpoints have
nonnegative product. Thus no positive-part argument changes sign inside
a segment, and J is affine there. These ten successive segments cover
all four sides with their boundaries; each affine minimum is at an
endpoint. Overpartitioning by an unused line would be harmless.

For every direction (a,b) in (5), the exact evaluation is

    J(a,b)/((|a|+|b|)*S)
      =[sum K_(m,k) max(ma+kb,0)
        -3(N-2)(g_5*P_5*a+g_6*P_6*b)] / ((|a|+|b|)*S).

The complete saved rational values, independently checked as described
below, are all at least 4/6521. At (-1,0) the positive parts all vanish,
and the value is exactly g_5*P_5/(g_5*P_5+g_6*P_6)=4/6521. Therefore
the bound holds on every segment and, by positive homogeneity, everywhere.
At zero both terms in (4) vanish. This proves the stated strict
nonseparation for every nonzero multiplier in the specified plane.

**Independent audit of the saved evidence (2026-10-23, step 409).**
The original bounded attempt is
`scripts/finite-support/capacitated_two_distance_test.py`. Its complete
saved evidence is `scripts/finite-support/capacitated-two-distance-results.json`,
losslessly packaged as the same path with `.gz` appended. The original
run failed its final storage assertion: 84,481,702 bytes versus
67,108,864 permitted. The 26,035,289-byte gzip meets that cap. Both
decompressed and original SHA-256 are
`c26d6d8d9ab453874f0aba97c81cd99049ba5fd8c65b122b2aad032c61b0be44`.
The original obstruction stage and AssertionError remain preserved.
They are not relabeled as a successful original run.

The independent audit is reproducible from the notebook by

    python3 scripts/finite-support/audit_capacitated_two_distance.py

It imports no constructor routine and does not repeat the original
1,500,625-entry enumeration or perform a new search. It reconstructs
all 69 pairs from L021's canonical rational vector, the demand and
source factors, and all 4,761 saved (i,j) tables. For every pair it
checks the complete t,s ranges and every factor in (2) by the independent
binomial factorizations
A_t=binomial(68,i)binomial(i,t)binomial(68-i,j-t) and its 956 analogue.
Their products therefore certify every individual G=g_i D.

To verify every saved h aggregate, form
A(z)=sum_t A_t z^t and B(z)=sum_s B_s z^s. Its sum G at h is exactly
the coefficient of z^(i+j-h) in A(z)B(z). Each coefficient is
nonnegative and at most A(1)B(1)=g_i*g_j<=H^2. Choose L with 2^L>H^2.
The base-2^L digits of the exact integer A(2^L)B(2^L) are consequently
these coefficients with no carries. The audit checks every digit
against the saved aggregate. A second product with coefficients one
checks all entry counts, using 2^13>69^2; the intersection-interval
count independently agrees. These are exact integer identities, not
floating convolution or checks of only total sums. Complete ranges,
all digits, and total sums preclude missing h records. All capacity
descriptors, repeated terms, null entries, buckets, unordered counts,
ten complete rational evaluations and segment signs are compared.

All 386,498 checks pass with no failures. The full audit certificate is
`scripts/finite-support/capacitated-two-distance-critical-audit.json`.
It retains the complete buckets, pair inputs, exact margins, segment
signs and per-table reconstruction hashes against the full original
evidence. All relevant values are actually checked; a preview is not
used as verification. The separate symbolic argument above establishes
the six presentations, box sign and completeness of (5). The original
source and constructor hashes are checked unchanged.

This audit completes the previously unfinished nonseparation attempt.
L105's independent-row result, L106's restricted-support rejection,
L107's failed common-normalization theorem application and L108's
uncapacitated conclusion retain their different scopes. Other weight
supports and full scalar/cardinality feasibility remain unresolved.

## Mathlib

Full matching capacitated triangle and two-weight specialization: not
checked. Supporting finite box LP duality, subset counting, polynomial
coefficient and exact rational arithmetic coverage: not checked.
Unknown availability is not evidence of absence. No Mathlib theorem
or uninspected external result is assumed.
