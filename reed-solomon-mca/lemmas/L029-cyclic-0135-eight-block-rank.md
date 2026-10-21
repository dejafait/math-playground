# L029 — Eight blocks force uniform rank for the cyclic 0135 family

## Hypotheses

Let F be any extension field of F_97, let H be the order-sixteen
multiplicative subgroup of F_97, and let lambda: Z/16Z -> H be a
bijection. In V=F^8 put
\[
 b_i=(\lambda(i),\lambda(i)^2,\ldots,\lambda(i)^8)^T,
 \qquad J_t=\{t,t+1,t+3,t+5\}\pmod {16},
 \qquad U_t=\operatorname{span}_F\{b_i:i\in J_t\}.
\]
For 0<=t<16 let P_t(X)=prod_(i in J_t)(X-lambda(i)). Let R_t have
as its four rows the coefficient vectors of X^r P_t(X), 0<=r<4,
in degrees 0,...,7. Define the six-by-28 matrix M_t by
\[
 (M_t)_{(r,s),(j,k)}
  =(R_t)_{rj}(R_t)_{sk}-(R_t)_{rk}(R_t)_{sj},
 \quad 0\le r<s<4,\quad 0\le j<k<8.
\]
Rows and columns are in lexicographic order. No cyclic ordering of
lambda, decomposability, error weights, or genericity is assumed.

## Conclusion

The stack M_0,...,M_7 has rank 28 over F. Hence the full sixteen-block
matrix has rank 28 for every lambda and over every such extension.
This concerns the entire exterior square, not only decomposable vectors.

This is a local rank result. The separate critical audit below found no
error. L030 now supplies its application to full-weight equality pencils,
including dependent syndrome directions; that application awaits its own
critical audit. No classification of arbitrary equality families or global
fifteen-count bound is asserted.

## Proof

### Imported machinery and the specialization

L010's Vandermonde argument gives independence of any eight distinct
b_i. Each smaller distinct collection is independent by extension to
eight. In particular b_0,...,b_7 form a basis of V. These facts hold
over F itself, since distinct nonzero prime-subfield values remain so.

Use L026's arbitrary-support annihilator construction and L027's
quotient equivalence. They apply to any four-element support: the row
of X^r P_t pairs with b_i as lambda(i)^(r+1)P_t(lambda(i)), and
the four rows have distinct leading degrees 4,5,6,7. Thus they are a
basis of U_t's annihilator, independently of the former 0125 supports.
If pi_t:V -> V/U_t is the quotient map, their six pairwise wedges
read every coordinate of wedge^2(V/U_t). Consequently, for every
p in wedge^2 V,
\[
 M_t p=0\quad\Longleftrightarrow\quad
 (\wedge^2\pi_t)(p)=0.                                      \tag{1}
\]
Here M_t acts on p's coordinates in the standard exterior basis.
The basis fact is also the standard exterior-basis theorem: Keith
Conrad, [*Exterior Powers*](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf),
Theorem 4.2, printed p. 11; functoriality is Theorems 5.1 and 5.4,
printed pp. 15–17. These theorems apply to finite-dimensional vector
spaces over F. We import this existing machinery, not L027's particular
kernel bases or any generic-rank result.

Write ij for b_i wedge b_j, with its displayed orientation. Let K_s
be the common kernel of the maps in (1) for 0<=t<s. We compute K_8
explicitly. The subsequent eight maps then have zero common kernel too.

### The first three constraints

The first three supports are
\[
 J_0=\{0,1,3,5\},\quad J_1=\{1,2,4,6\},\quad
 J_2=\{2,3,5,7\}.
\]
All are coordinate subspaces in the basis b_0,...,b_7. For each one,
the quotient's exterior basis consists of pairs of complementary
indices. The quotient map therefore kills exactly those basis wedges
with at least one endpoint in its support; different surviving basis
wedges have independent images. Intersecting these coordinate kernels
shows that K_3 has precisely the basis pairs meeting all three supports.

Their common intersection is empty. A pair meeting all three must
have an endpoint in at least two supports. Such endpoints are exactly
1,2,3,5. Endpoint 1 requires a partner in {2,3,5,7}; endpoint 2
requires one in {0,1,3,5}; and either endpoint 3 or 5 requires one
in {1,2,4,6}. Removing duplicate unordered pairs yields exactly
\[
 K_3=\operatorname{span}\{02,12,13,15,17,23,25,34,36,45,56\},
 \qquad\dim K_3=11.                                       \tag{2}
\]
These eleven vectors are distinct members of an exterior basis; the
enumeration and the coordinate-kernel argument establish exhaustiveness.

### The fourth constraint: the only coefficient issue

Here J_3={3,4,6,8}. In Q_3=V/U_3 write q_i=pi_3(b_i).
The vectors q_0,q_1,q_2,q_5 are a basis: together with the four
columns in J_3 their eight indices are distinct. Write
\[
 q_7=\alpha_0q_0+\alpha_1q_1+\alpha_2q_2+\alpha_5q_5.
\]
In particular alpha_0 is nonzero. Otherwise b_7 lies in the span of
the seven columns indexed by {3,4,6,8,1,2,5}. Together with b_7
these are eight distinct columns, contradicting independence. This
argument covers every lambda; it is not a generic nonvanishing claim.

Put w_ij=q_i wedge q_j. The complete image list for (2) is

| Input | Image in wedge^2 Q_3 |
| --- | --- |
| 02 | w_02 |
| 12 | w_12 |
| 13 | 0 |
| 15 | w_15 |
| 17 | -alpha_0 w_01 + alpha_2 w_12 + alpha_5 w_15 |
| 23 | 0 |
| 25 | w_25 |
| 34 | 0 |
| 36 | 0 |
| 45 | 0 |
| 56 | 0 |

The four images w_02,w_12,w_15,w_25 are independent basis wedges
in the quotient basis q_0,q_1,q_2,q_5. The image of 17 has nonzero
w_01 coefficient, absent from the other four. Thus the restriction
to K_3 has rank five. Its six killed basis vectors are independent,
so rank-nullity proves the exact kernel
\[
 K_4=\operatorname{span}\{13,23,34,36,45,56\},\quad\dim K_4=6. \tag{3}
\]
No coefficient has been divided out; no unexamined exceptional case
remains in this step.

### The next four constraints

For J_4={4,5,7,9}, the quotient has basis q_1,q_2,q_3,q_6:
these four indices and J_4 are eight distinct indices. The images of
the ordered basis in (3) are
\[
 (w_{13},w_{23},0,w_{36},0,0).
\]
The three nonzero entries are distinct basis wedges. Therefore
\[
 K_5=\operatorname{span}\{34,45,56\},\quad\dim K_5=3.        \tag{4}
\]
From now on q_i and w_ij always denote images in the current quotient.

For J_5={5,6,8,10}, q_3 and q_4 are independent: a dependence
modulo U_5 would be a dependence among the six distinct columns
indexed by {3,4,5,6,8,10}. Thus w_34 is nonzero. The three images
in (4) are (w_34,0,0), proving
\[
 K_6=\operatorname{span}\{45,56\},\quad\dim K_6=2.            \tag{5}
\]

For J_6={6,7,9,11}, q_4 and q_5 are independent by independence
of the six columns indexed by {4,5,6,7,9,11}. The two images in
(5) are (w_45,0), with w_45 nonzero. Hence
\[
 K_7=\operatorname{span}\{56\},\quad\dim K_7=1.              \tag{6}
\]

Finally J_7={7,8,10,12}. The columns indexed by {5,6,7,8,10,12}
are independent, so q_5,q_6 are independent modulo U_7. The image
of 56 is their nonzero wedge. This proves K_8=0. All remaining
constraints t=8,...,15 hold only on the zero vector in this common
kernel, so K_16=0 as well. Equation (1) and dim wedge^2 V=28 prove
both rank assertions.

### Scope and verification

The complete certificate is (2)–(6), the displayed full image lists,
and the final injectivity. The exact kernel dimensions after blocks
0,1,2 together and then each additional block through 7 are
11,6,3,2,1,0. The proof uses only eight-column independence and
exterior bases. It contains no numerical experiment, omitted kernel
branch, or assumption on decomposability. The separate critical audit
below checks it in full; no mathematical script is a premise.

The prior EXPLORE assessment
`drafts/literature/2026-10-06-cyclic-0135-full-rank.md` approved this
exact uniform-rank attempt and recorded the relevant primary source
comparisons. The existing 0125 kernel certificate does not prove this
claim: the supports and all residual bases here differ. The saved
seven-block containment failure in L028 is historical contrast, not
an input to this proof. This local advance is beyond the conclusions
of the sources checked, without a claim of certified originality.
Other support families and the main 11/q–16/q interval remain open.

### Separate critical audit, October 6, 2026

The approved audit under
`drafts/literature/2026-10-06-cyclic-0135-rank-audit.md` found no
mathematical defect. The following checks reproduce the existing
certificate; they establish no additional family exclusion or global
bound. Source coverage is reused, including Conrad's exterior-basis
and functoriality theorems precisely cited above.

**Column hypotheses and annihilator identification.** For any ordered
eight distinct indices i_1,...,i_8, the determinant of their moment
columns is
\[
 \left(\prod_{a=1}^8\lambda(i_a)\right)
 \prod_{1\le a<b\le8}(\lambda(i_b)-\lambda(i_a)).
\]
Every factor is nonzero for every bijection lambda. This is exactly
L010's Vandermonde input; neither its locator assumptions nor finiteness
of the extension is needed for this determinant identity. Any smaller
column set can be extended to eight. In particular dim U_t=4.
If X^r P_t(X)=sum_(j=0)^7 a_j X^j, its row pairs with b_i as
sum_j a_j lambda(i)^(j+1)=lambda(i)^(r+1)P_t(lambda(i)).
Thus the four rows annihilate U_t. They are independent: in a nonzero
linear combination, the row with largest r having nonzero coefficient
has a leading term of degree r+4 that cannot cancel. Since the
annihilator has dimension four, these rows form its basis.

Their descended functionals identify Q_t with F^4. The induced map on
exterior squares is an isomorphism, and in the standard wedge bases its
six coordinates are exactly the six row minors defining M_t. For
arbitrary p=sum_(j<k) p_jk e_j wedge e_k, each coordinate is
sum_(j<k)(a_j b_k-a_k b_j)p_jk. Consequently equation (1) holds on
all of wedge^2 V. Changing to the b_0,...,b_7 exterior basis is
invertible and introduces no decomposability assumption or rank loss.

**Exhaustiveness of the first intersection.** Each of J_0,J_1,J_2
is contained in {0,...,7}. Its quotient map kills the basis wedges
meeting the support and sends the others to distinct quotient basis
wedges. Its kernel therefore consists exactly of the former wedges;
there are no cancellations among the latter. Intersecting these three
coordinate kernels is consequently a test on each of all 28 pairs.
Independently enumerating by the smaller endpoint gives the following
complete list of partners whose pair meets all three supports:

| Smaller endpoint | Larger partners |
| --- | --- |
| 0 | 2 |
| 1 | 2,3,5,7 |
| 2 | 3,5 |
| 3 | 4,6 |
| 4 | 5 |
| 5 | 6 |
| 6 | none |

There are 1+4+2+2+1+1=11 pairs, exactly (2). In particular, this
test includes all excluded pairs as well as the eleven retained ones.

**Fourth block and its exceptional-coefficient check.** The union of
J_3={3,4,6,8} with {0,1,2,5} is the eight-element set
{0,1,2,3,4,5,6,8}, so the stated q_0,q_1,q_2,q_5 form a quotient
basis. If alpha_0 were zero, b_7 would lie in the span indexed by
{1,2,3,4,5,6,8}; adjoining 7 gives eight distinct columns and a
contradiction. No assumption on alpha_1,alpha_2,alpha_5 is needed.
Expanding q_1 wedge q_7 gives
-alpha_0 w_01+alpha_2 w_12+alpha_5 w_15, including the minus sign.
The complete ordered image list for (2) is
\[
 (w_{02},w_{12},0,w_{15},
 -\alpha_0w_{01}+\alpha_2w_{12}+\alpha_5w_{15},
 0,w_{25},0,0,0,0).
\]
Indeed q_3,q_4,q_6 vanish in this quotient. For a vector with
coefficients c_ij in (2), the zero-image equations are precisely
\[
 -\alpha_0c_{17}=0,\quad c_{02}=0,\quad
 c_{12}+\alpha_2c_{17}=0,\quad
 c_{15}+\alpha_5c_{17}=0,\quad c_{25}=0.
\]
The remaining quotient wedge w_05 has identically zero coefficient.
Thus c_17,c_02,c_12,c_15,c_25 all vanish and the other six
coefficients are free. This independently proves exactness of (3),
not merely that its displayed vectors lie in the kernel.

**Every remaining kernel.** For J_4={4,5,7,9}, its union with
{1,2,3,6} is the eight-element set {1,2,3,4,5,6,7,9}.
The images of (13,23,34,36,45,56) are
(w_13,w_23,0,w_36,0,0); q_4 and q_5 vanish, and the three nonzero
wedges are distinct basis wedges on q_1,q_2,q_3,q_6. Hence exactly
the coefficients of 13,23,36 must vanish, leaving (34,45,56).

For J_5={5,6,8,10}, its union with {3,4} is the six-element set
{3,4,5,6,8,10}. Column independence proves that q_3,q_4 are
independent modulo U_5, so w_34 is nonzero. The complete image list
of (34,45,56) is (w_34,0,0), leaving exactly (45,56).
For J_6={6,7,9,11}, the six distinct indices
{4,5,6,7,9,11} prove independence of q_4,q_5 modulo U_6.
The list (w_45,0) on (45,56) therefore leaves exactly (56).
For J_7={7,8,10,12}, the six distinct indices
{5,6,7,8,10,12} prove independence of q_5,q_6 modulo U_7;
the only remaining vector 56 has nonzero image. A wedge of two
independent vectors is nonzero by extending them to a basis and using
the exterior-basis theorem. This checks each smaller-set independence
claim and the final zero kernel without an omitted case.

The resulting dimensions are exactly 11,6,3,2,1,0. As the domain
has dimension 28, the first eight stacked blocks have rank 28;
adding the other blocks cannot reduce it or increase it above 28.
All determinants and all independence arguments remain valid in every
extension of F_97. No label permutation is treated as a symmetry of
the actual H-values. This audit uses no finite sample, numerical
certificate, error weights, syndrome-direction assumption, or locator
condition. Dependent directions and the full equality-pencil application
are separate unresolved obligations, outside this audit's scope.

## Mathlib

Coverage of this exact eight-block uniform-rank theorem is **not
checked**. No absence claim or Lean verification is asserted. L010,
L026 and L027 retain their qualifications for the supporting
Vandermonde, annihilator and exterior algebra.
