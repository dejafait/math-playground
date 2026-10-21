# L074 — Exclusion of rank four in the affine-plane alternating kernel

## Hypotheses

Let F be any extension of F_97, let H be the order-sixteen subgroup
of F_97^*, and label the sixteen points of L072 by an arbitrary
bijection lambda to H. Use precisely L072's sixteen blocks: the
vertical class and the slope-zero, slope-one and slope-u classes
of its auxiliary affine plane over F_4. That auxiliary field specifies
incidence only; no embedding into F is assumed.

Write V=F^8, m_x=(x,x^2,...,x^8)^transpose and
U_A=span{m_lambda(v):v in A}. For the quotient pi_A:V -> V/U_A, put

    K = {p in wedge^2 V : (wedge^2 pi_A)(p)=0 for every selected block A}.

This is the common alternating kernel defined in L073, using L026's
arbitrary-four-support equations. For a bivector p, its rank is the
dimension of S=im(p#:V^* -> V), where p# is contraction with p.
It is not the rank of the stacked matrix of equations.

## Conclusion

There is no rank-four bivector in K. Together with L073, every
nonzero element of K therefore has rank two and is decomposable.
The assertion is uniform over every bijection lambda and every F
as above, in particular F_(97^20).

This does not prove K=0, stacked rank 28, or impossibility of an L010
equality pencil. The rank-two tensors relevant to independent syndrome
directions remain unresolved. Neither L073 nor this new exclusion has
yet received a separate critical audit. No global bad-parameter bound
is improved.

## Proof

Suppose p in K has rank four, and set S=im(p#), so dim S=4.
We use the linear-algebra implication proved in L073: the inverse
alternating form on S makes S intersect U_A coisotropic, hence

    dim(S intersect U_A) >= 2                                      (1)

for every block A. No nondegenerate alternating form on all of V
is assumed. L010's Vandermonde argument gives independence of any
eight distinct moment columns, and hence of every smaller collection.

Choose a different block B in the same parallel class as A. Their
supports are disjoint four-sets, so U_A direct-sum U_B=V. In particular
S intersect U_A and S intersect U_B have zero intersection. By (1)
and dim S=4, both have dimension exactly two and

    S = (S intersect U_A) direct-sum (S intersect U_B).             (2)

Let Q=V/S, and denote the image of U_A in Q by W_A. It follows that
dim Q=4 and dim W_A=2. For two distinct blocks A,B in one parallel
class, W_A+W_B=Q because U_A+U_B=V; the dimensions then imply

    W_A intersect W_B = {0}.                                     (3)

These facts hold whether or not some moment columns project to zero.
For an abstract point v, write z_v for the image of m_lambda(v) in Q.
Call v a zero point if z_v=0, equivalently m_lambda(v) belongs to S.

### There are at most two zero points

Suppose v_1,v_2,v_3 were three distinct zero points. Their moment
columns are independent and span a three-dimensional space T inside S.
Each point belongs to exactly four selected blocks, by L072. Thus
at most twelve of the sixteen selected blocks contain one of these
three points, and there is a selected block A avoiding all three.
The seven columns indexed by A and v_1,v_2,v_3 are independent, so

    T intersect U_A = {0}.                                      (4)

On the other hand T and S intersect U_A have dimensions three and
two inside the four-dimensional S, by (2). Their intersection has
dimension at least one, contradicting (4). This argument also rules
out every larger set of zero points, by selecting any three of them.

### Three vertical rows still force incompatible intersections

If there is a zero point, omit the vertical block R_* containing
one such point. If there is none, omit any vertical block. Denote
the three remaining vertical blocks by R_0,R_1,R_2; these subscripts
are names for the chosen blocks, not prescribed auxiliary X-values.
There is at most one zero point in their union, since there are at
most two in the whole plane and the omitted row contains one whenever
the zero set is nonempty.

By (3), Q=W_R0 direct-sum W_R1, and W_R2 is disjoint from both
summands. Projection from W_R2 to W_R0 is an isomorphism: it is
injective by disjointness from W_R1 and both spaces have dimension two.
Consequently W_R2 is the graph of a linear map T_0:W_R0 -> W_R1.
Disjointness from W_R0 makes T_0 invertible. Identifying the second
factor with the first through T_0 gives coordinates Q=E direct-sum E
in which these three spaces are

    W_R0=E direct-sum 0,  W_R1=0 direct-sum E,
    W_R2={(a,a):a in E},                 dim E=2.                  (5)

Call a nonvertical selected block good if its three intersection
points with R_0,R_1,R_2 all have nonzero projection. In each nonvertical
parallel class at most one block is not good, because at most one
zero point lies on the three rows. Thus at least three slope-zero
blocks are good, and at least three slope-one blocks are good.

For any good block C, its projected columns at R_0 and R_1 are
(a_C,0) and (0,b_C), with a_C,b_C nonzero. They are independent
and lie in the two-dimensional W_C, so they span W_C. Its column
at R_2 is a nonzero diagonal vector (c_C,c_C), with c_C nonzero.
Expressing this vector in that basis gives

    c_C=alpha a_C=beta b_C,       alpha,beta nonzero.

Hence a_C and b_C span one common line l_C in E, and

    W_C = l_C direct-sum l_C.                                    (6)

Choose three good slope-zero blocks C_1,C_2,C_3. Their lines
l_C1,l_C2,l_C3 are pairwise distinct by (3) and (6): equality of
two of the lines would make the corresponding W spaces equal and
nonzero, contradicting (3). Choose one good slope-one block D.
Equation (6) also gives W_D=l_D direct-sum l_D.

L072 states that D meets each C_i in exactly one point. These
three intersection points are distinct, since the C_i are disjoint.
At most one of them lies on R_*, since D has exactly one point in
each vertical row. The other at least two intersection points lie
on R_0,R_1 or R_2 and have nonzero projections, because D is good.
For each such i, the common projected column is a nonzero vector in
W_D intersect W_Ci. But for lines in E, (6) implies

    (l_D direct-sum l_D) intersect (l_Ci direct-sum l_Ci)
        = (l_D intersect l_Ci) direct-sum (l_D intersect l_Ci).

A nonzero intersection forces l_D=l_Ci. The two intersection points
therefore force l_D to equal two of the distinct l_Ci, a contradiction.
This excludes rank four, including every zero-projection case.

L073 has already excluded ranks six and eight, and every nonzero
alternating tensor has positive even rank. Thus only rank two remains;
the alternating normal form used in L073 writes a rank-two tensor as
a wedge of two independent vectors. No parameter, weight, finite-chart,
locator or same-support condition follows merely from this remaining
rank possibility. All arguments used the actual moment columns under
the given labeling; choosing rows did not permute labels or assume
that an affine-plane automorphism preserves moments.

## Mathlib

Coverage of this exact family-specific exclusion is not checked.
No Mathlib theorem is imported, and unknown coverage is not absence.
The moment independence, exterior-kernel implication and cited incidence
model are reused from L010, L073 and L072, respectively. The proof above
supplies the zero-point and three-row specialization missing from the
previous restriction; it does not reprove a general affine-plane or
Reed–Solomon existence theorem. The saved EXPLORE comparison did not
identify a matching theorem, which is not a claim of certified novelty.
