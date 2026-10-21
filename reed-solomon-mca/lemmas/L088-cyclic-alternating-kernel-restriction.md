# L088 — The cyclic alternating kernel has at most one direction

## Hypotheses

Let F=F_(97^20), let H be the order-sixteen subgroup of F_97^*,
and let h:Z/16Z -> H be any bijection. In V=F^8 put

    v_i=(1,h(i),...,h(i)^7)^transpose,
    B_t={t,t+1,t+4,t+6},
    U_t=span_F{v_i : i in B_t},
    K=intersection_(t=0)^15 ker(wedge^2 pi_t),

where indices are modulo sixteen and pi_t:V -> V/U_t is the quotient.
For p in wedge^2 V, tensor rank means the rank of contraction
p#:V^* -> V. No decomposability, weights, parameters, locator conditions
or restrictions on the labeling other than bijectivity are assumed.

## Conclusion

Every nonzero p in K has tensor rank two, and dim_F K<=1.
Consequently the full 96-by-28 alternating matrix has rank 27 or 28.
If its rank is 27, its kernel has a nonzero generator over F_97,
and that generator is decomposable over F_97.

This does not decide which of ranks 27 and 28 occurs for any labeling,
and in particular does not prove uniform zero kernel. No labeling with
nonzero kernel, full-weight errors or equality pencil is constructed.
The main interval remains 11/q–16/q. The separate step-223 critical
audit below found no defect in this partial restriction.

## Proof

### Inputs, conventions and the alternating reduction

Use L010's eight-column independence: its shifted moment column is
h(i)v_i, and h(i) is nonzero. Hence any eight distinct v_i are
independent, as is any smaller collection by extension to eight.
This also follows from the Vandermonde determinant
prod_(i<j)(h(j)-h(i)) on any ordered eight distinct indices.
L087 supplies the sixteen distinct linear four-blocks, degree four at
every vertex, and exactly three nonneighbors per vertex in their
collinearity graph. In particular different U_s,U_t have intersection
spanned by the columns in B_s intersect B_t: their union has at most
eight elements and is independent. Disjoint blocks give complementary
four-dimensional spaces.

For clarity the matrix assertion uses the unshifted convention.
Let P_t(X)=prod_(i in B_t)(X-h(i)). The coefficient rows R_(t,r)
of X^r P_t(X), 0<=r<4, in degrees 0,...,7, pair with v_i as
h(i)^r P_t(h(i)). They form a basis of Ann(U_t): they annihilate
the four columns and have distinct leading degrees 4,5,6,7.
For each r<s their row wedge has entries

    R_(t,r),j R_(t,s),k - R_(t,r),k R_(t,s),j,   j<k.

Stack these six rows for every t to obtain the stated matrix M.
L027's quotient equivalence applies to any annihilator basis: these
six rows read all coordinates of wedge^2(V/U_t). Thus ker M=K
on the entire exterior square. The standard machinery is Keith Conrad,
[*Exterior Powers*](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf),
Theorem 4.2 (printed pp. 11–12), Theorems 5.1 and 5.4 (pp. 15–17),
and Corollary 5.9 (p. 18), as inspected in the prior assessment.
Finite-dimensional vector spaces over F satisfy their hypotheses.
No particular residual basis from L027 or L029 is imported.

We spell out the elementary alternating reduction to keep degeneracy
on V explicit. Splitting off a nonzero two-by-two alternating block
by simultaneous basis elimination, and repeating on its complement,
writes a nonzero p as

    p=e_1 wedge f_1+...+e_r wedge f_r,

with these 2r vectors independent. Each nonzero block coefficient is
absorbed into one vector; the process stops at a zero remaining block.
Thus S=im(p#) is their span and has dimension 2r. On S the inverse
of p is a nondegenerate alternating form omega. For any subspace U,
put T=S intersect U. The map S/T -> V/U is injective, and so is its
exterior square by the cited Corollary 5.9. The condition that p maps
to zero is therefore equivalent to vanishing of its pairing on
Ann_S(T) times Ann_S(T). Under the inverse-form identification of
S with S^*, Ann_S(T) corresponds to T^perp. Hence T^perp is isotropic,
so T^perp is contained in (T^perp)^perp=T. Consequently

    dim(S intersect U)>=r.                                      (1)

If equality holds, this intersection is Lagrangian in S. This is the
short coordinate reduction used as a method in L073; it is justified
here because L073's plane-specific conclusions do not apply to L087.
No conclusion or parallel-class hypothesis from L073–L079 is assumed.

### Ranks eight and six

If p has rank eight, S=V and (1) makes every U_t Lagrangian.
Fix an index x. The four blocks through x have twelve distinct other
vertices by L087's linearity. Their columns are omega-orthogonal to
v_x. Eight of these columns span V, making v_x orthogonal to V,
contrary to nondegeneracy and v_x!=0. Thus rank eight is impossible.

If p has rank six, (1) implies that each U_t has image of dimension
at most one in Q=V/S, which has dimension two. At most six v_i lie
in S, since any seven are independent. Let N be the indices of the
nonzero projected columns; then |N|>=10. The collinearity graph
induced on N is connected. Indeed each vertex has only three
nonneighbors even in the full graph. If the induced graph were
disconnected, every component would have size at least |N|-3,
because every vertex outside it is a nonneighbor of a vertex inside.
Two components would imply 2(|N|-3)<=|N|, contrary to |N|>=10.
On each edge the two nonzero projections lie in one block image
of dimension at most one, so they are proportional. Connectivity
therefore makes all nonzero projections proportional. But the v_i
span V and their projections span the two-dimensional Q. This
contradiction excludes rank six, including every possible zero column.

### An incidence separation fact

Any two distinct vertices belong to disjoint blocks, one containing
each. Here is a complete certificate. For (0,d), 1<=d<=8, use the
block shifts in the two right-hand columns:

| d | Block containing 0 | Block containing d |
| --- | --- | --- |
| 1 | 10 | 1 |
| 2 | 10 | 1 |
| 3 | 10 | 3 |
| 4 | 12 | 4 |
| 5 | 12 | 4 |
| 6 | 15 | 6 |
| 7 | 0 | 7 |
| 8 | 0 | 8 |

The required blocks are
B_10={10,11,14,0}, B_1={1,2,5,7}, B_3={3,4,7,9},
B_12={12,13,0,2}, B_4={4,5,8,10}, B_15={15,0,3,5},
B_6={6,7,10,12}, B_0={0,1,4,6}, B_7={7,8,11,13},
and B_8={8,9,12,14}. Each listed pair is disjoint and contains its
designated vertices. Translate indices to handle an arbitrary first
vertex. If the difference is 9,...,15, reverse the pair first; its
new difference is 1,...,7. This covers all unordered pairs. Translation
here selects blocks of the abstract family; it assumes no symmetry of h.

Also B_t and B_(t+7) are disjoint for every t, as is seen from
B_0 and B_7 followed by translation.

### Rank four, retaining all zero projections

Suppose dim S=4. By (1), each S intersect U_t has dimension at
least two. Its disjoint partner U_(t+7) has the same lower bound,
and these intersections are disjoint subspaces of S. Both therefore
have dimension exactly two. In Q=V/S write W_t=pi(U_t); then
dim W_t=2. Whenever B_a,B_b are disjoint, U_a+U_b=V, so
W_a+W_b=Q. Since dim Q=4, these two W spaces are complementary.

It follows from the separation certificate that no two nonzero
projected columns pi(v_x),pi(v_y) are proportional: choose disjoint
containing blocks, whose complementary W spaces would otherwise
intersect nontrivially. Zero columns have not been excluded. Their
index set Z has size at most four by five-column independence.

Consider the sixteen translated triples of blocks
(B_t,B_(t+1),B_(t+2)). Their three pairwise intersections are the
distinct vertices t+1,t+2,t+6, and their union is the nine-element
set {t,t+1,...,t+8}. A fixed vertex lies among those three intersection
vertices for exactly three t. Thus at most 3|Z|<=12 of the sixteen
triples have a zero projection at an intersection vertex. Choose one
of the remaining triples, and abbreviate its block images by A,B,C
in their displayed order. They are two-dimensional. The nonzero
projection at t+1 belongs to A intersect B, so dim(A+B)<=3.
The projections at t+6 and t+2 lie in A intersect C and B intersect C,
respectively. They are nonzero and not proportional by separation,
so they span C. Hence C is contained in A+B.

All nine columns of the triple's union consequently project into a
space of dimension at most three. Choose any eight of those columns.
They span V, so their projections must span Q of dimension four.
This contradiction excludes rank four. All possible sets Z, including
the empty set, were retained. Since alternating rank is even, every
nonzero member of K now has rank two.

### The common kernel cannot have two independent members

We first record a second complete incidence consequence. For any
t and any nonzero a in U_t, there exist two disjoint blocks C,D
such that a belongs to neither U_C nor U_D. It suffices to describe
the translated case t=0. Take C=B_7 and D=B_14={14,15,2,4}.
They are disjoint. Also U_0 intersect U_7=0 and
U_0 intersect U_14=F v_4 by independence of their seven-column union.
Thus this pair works unless a is proportional to v_4. In that case
use B_1 and B_8, which are disjoint and both avoid 4; independence
of the five columns obtained by adjoining v_4 to either block shows
that neither span contains v_4. For arbitrary t, translate all indices,
including the exceptional vertex t+4. These statements use incidence
and column independence, not equivariance of the label values.

Now put A=U_0 and B=U_7, so V=A direct-sum B. The exterior
decomposition is

    wedge^2 V = wedge^2 A direct-sum (A wedge B) direct-sum wedge^2 B.

The quotient constraints for blocks 0 and 7 force K to lie in
A wedge B, naturally identified with A tensor B. If its coefficient
matrix in bases of A,B is C, contraction of the corresponding bivector
has block matrix [[0,C],[-C^transpose,0]], up to an overall sign.
Its rank is 2 rank(C): its two image components have independent
locations and dimensions rank(C),rank(C^transpose). Every nonzero
member of K therefore corresponds to a rank-one matrix, and can be
written a wedge b with nonzero a in A and b in B.

Suppose p=a wedge b and p'=c wedge d are independent members of K.
If a,c are independent and b,d are independent, the cross matrix of
p+p' has rank two: contraction by functionals on B taking respective
values (1,0) and (0,1) on (b,d) yields a and c. This contradicts the
rank-two tensor conclusion for p+p' in K. Thus a,c or b,d are
dependent. They cannot both be dependent because p,p' are independent.
After absorbing scalars and possibly interchanging A and B (which
only changes the wedge sign), write

    p=a wedge b,   p'=a wedge d,

where a is a nonzero vector in one of U_0,U_7, and b,d are independent
in the complementary block space. Consequently T=span{a,b,d} has
dimension three.

Choose the two disjoint blocks C,D avoiding a by the preceding
incidence consequence (at t=0 or t=7 as appropriate). In either
quotient, pi(a) is nonzero and the two kernel equations give
pi(a) wedge pi(b)=pi(a) wedge pi(d)=0. Both pi(b) and pi(d)
are therefore multiples of pi(a), including the possibility of zero.
Thus dim pi(T)=1 and dim(T intersect U_C)=dim(T intersect U_D)=2.
Two two-dimensional subspaces of the three-dimensional T intersect
nontrivially. But U_C intersect U_D=0 by disjointness and eight-column
independence. This contradiction proves dim K<=1.

### Residual test and scope

Since dim wedge^2 V=28 and ker M=K, rank M is 27 or 28. Every
entry of M is in F_97. Matrix rank is unchanged on field extension:
it is the largest order of a nonzero minor, and the inclusion of fields
preserves zero and nonzero determinants. If rank M=27, row reduction
over F_97 supplies a nonzero rational kernel generator. It still has
tensor rank two over F_97 by the same minor criterion, and alternating
elimination there expresses it as a wedge of two rational vectors.
No rational original affine chart or actual errors follow from this.

The exact unproved alternative is whether rank 27 occurs at any
bijection h. Uniform nonvanishing of at least one 28-by-28 minor for
each h would finish the approved zero-kernel target; one verified
rank-27 matrix and nonzero kernel vector would refute it. A rank-27
tensor still requires all separate full-weight, parameter, locator and
same-support conditions for an equality application. The present
argument neither supplies those conditions nor excludes rank 27.

This is the bounded analytic pass authorized by
`drafts/literature/2026-10-14-cyclic-family-alternating-kernel.md`.
The exact theorem was not covered by the sources checked; the result
is recorded as POTENTIALLY_NEW, not a certified originality claim.
The argument uses no sampled ranks, labeling sweep, computation or
plane-specific tensor restriction. Its complete incidence certificates
are the displayed lists and the explicit exceptional common-factor
case. The separate critical audit is recorded below.

### Separate critical audit — October 14, 2026, step 223

The audit used the pre-existing EXPLORE scope in
`drafts/literature/2026-10-14-cyclic-kernel-restriction-audit.md`
and checked the entire proof above. No mathematical defect or necessary
change to the argument was found. This validates a local input; it is
not a new theorem beyond L088 or a certification of originality.
The following records the load-bearing checks, including degeneracies.

**Inputs and the full matrix.** L010's independence proof uses only
distinct nonzero evaluation points, not its nonpersistent-locator or
bad-event hypotheses. Multiplying each unshifted column by h(i)
recovers its shifted column, preserving every span and independence
claim. L027's quotient-coordinate argument applies to any annihilator
basis. Here evaluation of the unshifted coefficient row is exactly
h(i)^r P_t(h(i)), with no extra h(i). The four rows have distinct
leading degrees and span the four-dimensional annihilator, so their
six wedges detect the complete six-dimensional quotient exterior
square. Sixteen blocks therefore give exactly 96 rows on 28 columns;
ker M=K does not require decomposability. L087's difference calculation
supplies distinct linear blocks, degree four and three nonneighbors
at every vertex. No plane-family result, actual-error assumption or
finite certificate is an input. The cited Conrad results cover the
exterior operations over the stated field, as recorded in the ready
source assessment; no further source import or reproof is needed.

**Alternating reduction and ranks six/eight.** Characteristic 97 is
not two. Alternating elimination gives even contraction rank 2r and
puts p in wedge^2 S, where S is its contraction image. The inverse
alternating form is used only on S. Restricting to Ann_S(T) with
T=S intersect U, and injecting S/T into V/U, identifies the zero
quotient condition with isotropy of T^perp. Nondegeneracy on S gives
T^perp contained in T, hence 2r-dim T<=dim T. This proves (1) even
when the original alternating matrix on V is singular. In rank eight,
the four blocks through x provide twelve distinct other columns
orthogonal to v_x; eight span V, a contradiction. In rank six,
at most six columns project to zero, so |N|>=10. In a disconnected
induced graph each component has size at least |N|-3; two components
would require |N|<=6. Thus nonzero projections are all proportional
by connectedness, contradicting their spanning a two-dimensional
quotient. Zero projections were neither divided by nor discarded
from the spanning argument.

**Complete separation certificate and rank four.** Every displayed
row was checked directly: the eight shift pairs are (10,1), (10,1),
(10,3), (12,4), (12,4), (15,6), (0,7), (0,8), for d=1,...,8.
Each first block contains 0, each second contains d, and every pair
is disjoint. For a difference above eight, interchange the two
vertices before applying a translation. This reverses the ordered
pair, not the block family; no reflection symmetry or symmetry of
h is required. B_t and B_(t+7) are disjoint for all t. At rank four
their intersections with S have dimensions at least two and direct
sum inside S, hence exactly two. For any disjoint blocks their
quotient images consequently have dimensions two and direct sum Q.
Separation then excludes proportional nonzero projected columns.

For the base translated triangle, the intersections are respectively
{t+1}, {t+6}, {t+2}, and its union is {t,...,t+8}. These statements
remain true modulo sixteen because these nine residues are distinct.
At most four original columns lie in S. A zero column z spoils only
the triples with t=z-1,z-2,z-6. Their union therefore spoils at most
twelve of the sixteen triples, even if several zeros spoil the same
triple. In a remaining triple, the first shared projection makes
dim(A+B)<=3; the other two shared projections are distinct and
nonproportional, and form a basis of C inside A+B. All nine original
columns project into this space. Any eight span V, which would force
dim Q<=3 instead of four. This covers every zero set, including none.

**Kernel dimension and its exceptional factor.** The constraints for
blocks 0 and 7 kill the two pure exterior summands of V=U_0 direct-sum
U_7, leaving only the cross summand. Its contraction matrix has rank
twice the cross-matrix rank. If two independent tensors had independent
factors on both sides, their sum would have cross rank two and tensor
rank four, already excluded. Their common factor therefore lies in
one of U_0,U_7, while the two other factors are independent in the
complement; the resulting T has dimension exactly three.

For t=0 the pair B_7,B_14 is disjoint, U_0 intersect U_7=0, and
U_0 intersect U_14=F v_4: the union of the latter two blocks has
seven independent columns. A nonzero common factor in U_0 is thus
avoided by both spans unless proportional to v_4. For this exception,
B_1 and B_8 are disjoint and avoid 4, and adjoining v_4 to each
gives five independent columns. Translation handles t=7 with the
exceptional column v_11. The chosen quotients each retain the common
factor nonzero; the two wedge equations make the entire image of T
one-dimensional, including zero images of either other factor.
Thus both intersections with T have dimension two. They cannot be
disjoint inside a three-space, whereas the two block spans are
disjoint. This proves dim K<=1 without assuming a general theorem
classifying linear spaces of decomposable tensors.

**Descent and limits.** The matrix entries lie in F_97. Nonzero-minor
rank is preserved under its inclusion in F, so a rank-27 stack has a
one-dimensional kernel already over F_97. A nonzero generator there
has contraction rank two over F and, again by minors, over F_97.
Alternating elimination over F_97 expresses it as a wedge over that
same field. This conclusion concerns only the kernel tensor. No
choice of original chart, full weights, distinct parameters, locator
conditions, same-support failure or equality realization is inferred.

The sole direct mathematical inputs remain L010, L027 and L087; DAG
edges need no change. The written incidence checks are complete, so
no numerical rank sampling or supplementary mathematical script was
needed. The argument itself is unchanged, so PROOF.md is unchanged.
Rank 27 is neither exhibited nor excluded, and arbitrary-family and
challenge-definition gaps remain. Full Mathlib coverage remains
unchecked as stated below.

## Mathlib

The full cyclic-family restriction has not been checked in Mathlib.
No absence or Lean-verification claim is made. The external exterior
algebra inputs are cited above; the moment independence is reused from
L010 and the quotient interpretation from L027, with conventions checked.
