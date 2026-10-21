# L027 — Seven overlapping blocks force arbitrary-label rank 28

## Hypotheses

Let F be any extension field of F_97, let H be its prime subfield's
order-sixteen multiplicative subgroup, and let lambda: Z/16Z -> H be
any bijection. Put
\[
 I_t=\{t,t+1,t+2,t+5\}\subset\mathbb Z/16\mathbb Z,
 \qquad b_i=m(\lambda(i))=(\lambda(i),\ldots,\lambda(i)^8)^T\in F^8,
 \qquad U_t=\operatorname{span}\{b_i:i\in I_t\}.
\]
These are L025's indexed supports with arbitrary evaluation labels.
For each t let P_t(X)=prod_(i in I_t)(X-lambda(i)). Form the six-by-28
block M_t from the six pairwise alternating products of the coefficient
rows of X^r P_t(X), 0<=r<4, as in L026. Columns are indexed by 0<=j<k<8.
No cyclic evaluation order, genericity, condition on error weights, or
decomposability of an alternating vector is assumed.

## Conclusion

The stack of just M_0,...,M_6 has rank 28 over F. Consequently L026's
full sixteen-block matrix has rank 28 for every bijection lambda, over
F_97 and every extension.

There cannot be u,v in F^8, parameters gamma_t in F, and words e_t with
support exactly {lambda(i):i in I_t}, satisfying
\[
 \sigma(e_t)=u+\gamma_t v\qquad(0\le t<16).
\]
In particular this family cannot realize L010's sixteen-count equality
under any labeling by H, including over F_(97^20). This is a partial
family exclusion, not a classification of equality supports or a global
fifteen-count bound. It does not resolve ABF26 correspondence.

## Proof

### The polynomial constraints as quotient maps

Write V=F^8. L010 proves that any eight distinct b_i are independent.
Every smaller distinct collection is independent as well, by extending
it to eight among the sixteen columns. Thus dim U_t=4. L026 identifies
the four coefficient rows of X^r P_t with a basis of U_t's annihilator:
their pairing with b_i is lambda(i)^(r+1)P_t(lambda(i)); their distinct
leading degrees 4,5,6,7 give independence. We use that identification
with the same moment-index convention.

Let pi_t:V -> V/U_t be the quotient map. If p is any element of
the exterior square wedge^2 V, expansion in the coordinate wedges gives
\[
 (a\wedge b)(p)=\sum_{j<k}(a_jb_k-a_kb_j)p_{jk}
\]
for covectors a,b. The four annihilating rows descend to a basis of
(V/U_t)^*. Their six pair wedges are a basis of its alternating
two-forms: in any dual basis they read the six coordinates of
wedge^2(V/U_t). It follows, for every p and not only a decomposable p,
that
\[
 M_t p=0\quad\Longleftrightarrow\quad
 (\wedge^2\pi_t)(p)=0.                                      \tag{1}
\]
Define K_s as the intersection of these kernels for 0<=t<s. We shall
prove K_7=0. We abbreviate b_i wedge b_j by ij; this denotes a vector,
not a scalar coordinate, and reversing the order changes its sign.

The shared quadratic factors of consecutive P_t correspond to their
two shared indices. Instead of dividing these factors, (1) keeps their
overlap in a moment basis and permits exact elimination. The quotient
bases below justify every coefficient nonvanishing needed in that
elimination.

### First three blocks: dimension twelve

The union of I_0,I_1,I_2 is {0,...,7}, so b_0,...,b_7 form a basis.
For t=0,1,2 the quotient by U_t has the complementary b_i as a basis.
Its exterior-square map kills exactly the basis wedges ij with at
least one endpoint in I_t. Hence K_3 has as a basis the pairs meeting
all three of
\[
 I_0=\{0,1,2,5\},\quad I_1=\{1,2,3,6\},\quad I_2=\{2,3,4,7\}.
\]
The seven pairs containing 2 all qualify. A qualifying pair avoiding 2
must have one endpoint in at least two of the three sets. The only
such endpoints are 1 (the first two sets) and 3 (the last two). Pairing
1 with {3,4,7}, or 3 with {0,1,5}, gives exactly five further pairs.
Thus
\[
 K_3=\operatorname{span}\{20,21,23,24,25,26,27,13,14,17,03,35\},
 \qquad \dim K_3=12.                                      \tag{2}
\]
All listed wedges are distinct up to sign in a basis of wedge^2 V.

### Fourth block: dimension eight

Here I_3={3,4,5,8}. In Q_3=V/U_3 write q_i=pi_3(b_i).
The four vectors q_0,q_1,q_2,q_6 form a basis, because the eight indices
{0,1,2,6,3,4,5,8} are distinct. Express
\[
 q_7=\alpha_0q_0+\alpha_1q_1+\alpha_2q_2+\alpha_6q_6.
\]
Each alpha_i is nonzero. If alpha_i=0, b_7 belongs to the span of the
four columns in I_3 and the three remaining basis columns. These seven
columns together with b_7 are eight distinct columns, contradicting
their independence. This argument requires no generic evaluations.

The images of the twelve wedges in (2) span precisely
\[
 q_2\wedge q_0,\quad q_2\wedge q_1,\quad q_2\wedge q_6,
 \quad q_1\wedge q_7.                                    \tag{3}
\]
Indeed the additional possible nonzero image q_2 wedge q_7 lies in
the first three's span, and all other images vanish. The first three
are independent basis wedges. The last has nonzero coefficient alpha_0
on q_1 wedge q_0, which is absent from their span. Thus the restricted
map has rank four and dim K_4=8.

Eight vectors in K_4 are
\[
 23,24,25,28,13,14,03,35.                                  \tag{4}
\]
Each pair meets every I_t for 0<=t<=3, which proves membership by (1).
They are independent: the seven except 28 are distinct basis wedges
in b_0,...,b_7. Expand b_8 in that basis. Its coefficient on b_6 is
nonzero, since otherwise b_8 and the seven basis columns other than
b_6 would be dependent. Consequently 28 has a nonzero coefficient on
26, absent from the other seven wedges. Dimension eight now proves
that (4) is a basis of K_4.

### Fifth block: dimension four

For I_4={4,5,6,9}, the quotient Q_4=V/U_4 has basis q_0,q_1,q_2,q_3,
where now q_i=pi_4(b_i). Again, the eight combined indices are distinct.
Every coefficient beta_i in q_8=sum_(i=0)^3 beta_i q_i is nonzero:
a zero coefficient would place b_8 in the span of seven other distinct
columns and contradict eight-column independence.

The only possibly nonzero images of (4) are
\[
 q_2\wedge q_3,\quad q_2\wedge q_8,\quad
 q_1\wedge q_3,\quad q_0\wedge q_3.                       \tag{5}
\]
The three displayed wedges having endpoint 3 are independent. The
remaining one has nonzero coefficient beta_0 on q_2 wedge q_0,
absent from their span. Thus (5) is independent and the map on K_4
has rank four. The four independent wedges killed by it are
\[
 K_5=\operatorname{span}\{24,25,14,35\},\qquad \dim K_5=4. \tag{6}
\]
Their independence follows in the original basis b_0,...,b_7; the
dimension calculation proves that no other kernel direction remains.

### Sixth and seventh blocks: zero kernel

For I_5={5,6,7,10}, Q_5=V/U_5 has basis q_1,q_2,q_3,q_4, by
eight-column independence. The images of 24 and 14 are the independent
basis wedges q_2 wedge q_4 and q_1 wedge q_4; the images of 25 and 35
are zero. Hence
\[
 K_6=\operatorname{span}\{25,35\},\qquad \dim K_6=2.       \tag{7}
\]
Finally I_6={6,7,8,11}. The images q_2,q_3,q_5 in V/U_6 are independent,
since their three indices and the four in I_6 are seven distinct
independent columns. Extend these three images to a quotient basis.
Then q_2 wedge q_5 and q_3 wedge q_5 are distinct independent basis
wedges. Thus the last quotient map is injective on K_6, proving K_7=0.

By (1) this is the entire kernel of the first seven blocks, in the
28-dimensional space wedge^2 V. Rank-nullity proves rank 28. All
arguments apply over F itself; eight-column independence follows from
the nonzero Vandermonde factors on distinct nonzero elements of H,
which stay nonzero under extension. There is no specialization of a
generic minor, finite labeling sample, or unproved division.

### Consequence for actual syndromes

For a proposed realization, put p=u wedge v. In each quotient,
pi_t(u)+gamma_t pi_t(v)=0, so its alternating product is zero even
if pi_t(v)=0. Thus M_t p=0. The established rank forces p=0 and hence
u,v linearly dependent. For completeness, if u is nonzero, a nonzero
coordinate u_j together with all relations u_jv_k-u_kv_j=0 gives
v=(v_j/u_j)u; if u=0, dependence is immediate.

Each full-weight e_t has nonzero syndrome: its four moment columns
are independent. Consequently span{u,v} must be a one-dimensional
space contained in every U_t. But I_0 and I_6 are disjoint, as in L025,
and their eight columns are independent. Thus U_0 intersection U_6=0,
a contradiction. This excludes the zero-dimensional case as well.
It does not require distinct gamma_t, finite-extension weights, a
nonzero Hankel determinant, or nonpersistent locators; therefore it
applies in particular to the more restrictive L010 equality event.

### Source scope and verification qualifications

The saved pre-invocation EXPLORE assessment
`drafts/literature/2026-10-05-overlap-factor-universal-rank.md` covers
this full alternating-space target. Its inspected exterior-arrangement,
common-factor, and generic GM-MDS comparisons do not supply the fixed-H
rank. No theorem from those sources is imported or reproved here.
L010 supplies moment independence, L025 the support family and disjoint
pair, and L026 the coefficient-annihilator blocks. The displayed
elimination is a concrete certificate for that same matrix, expressed
in quotient bases; it does not change to a decomposable-kernel target.

The complete certificate is the explicit kernel bases (2), (4), (6),
(7), followed by zero, with every rank and nonzero coefficient justified
above. No mathematical script or numerical certificate is a premise.
This supplies a local proof beyond the previously checked cyclic and
finite-label cases, without claiming certified originality. The separate
critical audit below checks that proof; this is not a candidate complete
solution of the main challenge.

### Separate critical audit, October 5, 2026

The audit used the pre-existing EXPLORE assessment
`drafts/literature/2026-10-05-seven-block-critical-audit.md` and found no
mathematical error. It checked the full quotient argument, rather than
testing labelings or importing the earlier cyclic minors. The following
are the complete load-bearing checks. They verify the existing result;
no stronger family classification or numerical bound is claimed.

First, the column matrix on eight distinct evaluations x_1,...,x_8 has
determinant
\[
 \left(\prod_{i=1}^8 x_i\right)
 \prod_{1\le i<j\le8}(x_j-x_i)\ne0.
\]
This verifies precisely the part of L010 used in the elimination, over
every extension in the hypotheses. For any basis of eight such columns,
each coefficient of a ninth distinct column is nonzero: by Cramer's
rule it is a quotient of two determinants of this same form, with
possibly a sign from the column order. In a quotient basis obtained
by putting the four U_t columns first and four complementary columns
last, its last four coefficients are exactly the quotient coordinates.
This checks all alpha_i and beta_i, and the coefficient of b_6 in b_8,
without a genericity assumption or cancellation claim.

The pairing convention was checked directly: a coefficient row in
degrees 0,...,7 paired with (x,...,x^8) gives x times its polynomial
value. The four rows have distinct leading degrees and lie in a
four-dimensional annihilator, so are a basis. In the dual quotient
basis their six alternating products extract all six exterior
coordinates. Thus (1) is an equivalence on the whole 28-dimensional
space, with no decomposability assumption. For the first three blocks,
their quotients are coordinate projections in b_0,...,b_7; hence a
kernel is spanned by killed basis wedges, with no cancellations between
surviving wedges. Intersecting these three coordinate kernels gives
exactly the seven pairs containing 2 and the five additional pairs
13,14,17,03,35. This independently checks exhaustiveness of (2).

Here is the complete image check for the fourth block, with q_i in Q_3
and w_ij=q_i wedge q_j. Grouped entries have the same zero image.

| Input from (2) | Image |
| --- | --- |
| 20 | w_20 |
| 21 | w_21 |
| 23,24,25,13,14,03,35 | 0 |
| 26 | w_26 |
| 27 | alpha_0 w_20 + alpha_1 w_21 + alpha_6 w_26 |
| 17 | w_17 = alpha_0 w_10 + alpha_2 w_12 + alpha_6 w_16 |

All twelve inputs occur once. The last image is independent of
w_20,w_21,w_26 because its w_10 coefficient is nonzero, proving rank
four. Every vector in (4) meets all four support sets; in particular
28 meets the first three through 2 and the fourth through 8. The seven
other vectors in (4) are distinct original basis wedges, and none is
26. The nonzero b_6 coefficient in b_8 makes 28 independent of them.
Thus the displayed eight-dimensional subspace is the entire kernel,
not merely an included subspace.

For the fifth block the complete images of the ordered list (4) are
\[
 (w_{23},0,0,w_{28},w_{13},0,w_{03},0)
 \quad\text{in }\bigwedge^2 Q_4,
\]
where
\[
 w_{28}=\beta_0 w_{20}+\beta_1 w_{21}+\beta_3 w_{23}.
\]
In the quotient basis q_0,q_1,q_2,q_3, the entries in positions one,
five and seven are independent wedges containing q_3; the beta_0
term proves the remaining image independent of them. The four killed
inputs 24,25,14,35 are independent original basis wedges. Rank-nullity
therefore proves the exact four-dimensional kernel (6).

For the sixth block, the images of that ordered kernel basis are
(w_24,0,w_14,0) in the quotient basis q_1,q_2,q_3,q_4.
The two nonzero wedges are independent, so the kernel is exactly
span{25,35}. For the seventh block, independence of the seven columns
indexed by {2,3,5,6,7,8,11} implies independence of q_2,q_3,q_5
modulo U_6. Extending these to a quotient basis proves that w_25,w_35
are independent. This checks the final injectivity and the exact
dimension sequence 12,8,4,2,0. By the already checked equivalence (1),
the first seven coefficient blocks consequently have rank 28.

Finally, a nonzero error with its specified four-element support has
nonzero syndrome by independence of those four columns. Any proposed
realization gives pi_t(u)+gamma_t pi_t(v)=0, which implies the zero
alternating product even if pi_t(v)=0. Rank 28 forces u wedge v=0.
If span{u,v} has dimension zero, the nonzero syndromes contradict it.
If it has dimension one, each nonzero u+gamma_t v spans that same line,
so the line is contained in every U_t. The sets I_0={0,1,2,5} and
I_6={6,7,8,11} are disjoint; their eight independent columns make
U_0 intersection U_6 zero. This checks the dependent case, including
u=0, v=0 and repeated parameters, without any division by a weight
or a parameter.

For the application to L010, subtracting the witnessing codeword does
give sigma(e_t)=sigma(a)+gamma_t sigma(b). Indeed the moment functionals
annihilate degree-less-than-eight codewords: every exponent in such a
pairing lies between 1 and 15, whose sums over H vanish by the subgroup
argument in L010. Equality there supplies the required full-weight
four-element supports. The audit does not discard the determinant or
locator hypotheses of L010; the obstruction is stronger and needs none
of them. All determinant factors and coordinate arguments above hold
over the extension field itself, including infinite extensions. No
finite sample, unpublished source claim, or computational certificate
is a premise. The direct inputs remain L010, L025 and L026, and the
DAG is unchanged. Mathlib coverage remains as qualified below.

## Mathlib

Coverage of this exact seven-block rank and arbitrary-label support
exclusion is **not checked**. No full matching theorem, absence claim,
or Lean verification is asserted. L010 and L026 retain their existing
qualifications for the supporting Vandermonde and alternating algebra.
