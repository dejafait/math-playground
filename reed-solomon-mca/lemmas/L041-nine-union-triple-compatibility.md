# L041 — Exact local compatibility for a nine-union triple

## Hypotheses

Let F=F_(97^20), let H be the order-sixteen subgroup of F_97^*,
and let C=RS[F,H,8]. Use L010's eight shifted moments
\[
 \sigma_j(z)=\sum_{x\in H}z_xx^j\quad(1\le j\le8),
 \qquad s(T)=\sigma(a)+T\sigma(b).
\]
Retain the pinned radius cell 1/4<=delta<5/16, L010's nonzero
polynomial D and every nonzero coordinate locator, and sixteen-count
equality. Choose three distinct original finite bad parameters
gamma_0,gamma_1,gamma_2 in F. Let e_i be their actual unique errors,
A_i=supp(e_i), and assume |U|=9 for U=A_0 union A_1 union A_2.
L010 gives distinct four-element A_i, nonzero weights on each A_i,
and sigma(e_i)=s(gamma_i). Parameters and weights range over F;
there is no rationality or projective-chart assumption.

Put
\[
 \alpha_0=\gamma_1-\gamma_2,\quad
 \alpha_1=\gamma_2-\gamma_0,\quad
 \alpha_2=\gamma_0-\gamma_1,\qquad
 Q(X)=\prod_{y\in H\setminus U}(X-y),\quad c_x=Q(x)\ (x\in U).
                                                        \tag{1}
\]
Every alpha_i and every c_x is nonzero. Extend c by zero outside U;
this is the evaluation word of Q on H.

## Conclusion

There is a unique lambda in F^* such that
\[
 \alpha_0e_0+\alpha_1e_1+\alpha_2e_2=\lambda c.           \tag{2}
\]
For x in U define I_x={i:x in A_i} and, for i in I_x,
\[
 b_{i,x}=\frac{\alpha_i e_i(x)}{\lambda c_x}.
\]
The following is the exact local compatibility criterion, including
all nonzero-weight gates:

| Membership I_x | Normalized weights on the present indices | Gate |
| --- | --- | --- |
| {i} | b_i=1 | automatic |
| {i,j}, i<j | b_i=p_x, b_j=1-p_x | p_x not in {0,1} |
| {0,1,2} | b_0=p_x, b_1=q_x, b_2=1-p_x-q_x | p_x q_x (1-p_x-q_x)!=0 |

For every present index the actual weight is
\[
 e_i(x)=\frac{\lambda c_x}{\alpha_i}b_{i,x};             \tag{3}
\]
all absent weights are zero. Different shared coordinates have
independent parameters in this description.

There are exactly four incidence patterns up to permutation of the
three error indices. Write n_ij for the number of coordinates with
I_x={i,j}, tau for the number with I_x={0,1,2}, and s_i for the
number with I_x={i}. The table lists representatives, not a choice
of field labels:

| tau | (n_01,n_02,n_12) | (s_0,s_1,s_2) |
| --- | --- | --- |
| 0 | (3,0,0) | (1,1,4) |
| 0 | (2,1,0) | (1,2,3) |
| 0 | (1,1,1) | (2,2,2) |
| 1 | (1,0,0) | (2,2,3) |

For prescribed supports and parameters the homogeneous moment-relation
kernel has dimension four. Its full-weight part has lambda!=0 and,
after one common nonzero scaling, exactly three shared-coordinate
parameters with precisely the displayed gates. The lambda=0 part
has dimension three and contains no full-weight triple. There is no
affine vector supported in U whose values at the three parameters
are the three e_i themselves: the affine compatibility is in moments,
and its nonzero codeword defect is exactly (2).

Conversely, for any three four-element supports with union nine,
any three distinct original finite parameters, and any choices in
(3) satisfying these gates, the three moment vectors are values of
one affine syndrome pencil. If the first two moment vectors equal
those of a specified pencil s at gamma_0,gamma_1, the third does also.
All four patterns admit such full-weight choices over F. The first
two syndromes are linearly independent. Words realizing that pencil
can be chosen as
\[
 a_* =\frac{\gamma_1 e_0-\gamma_0 e_1}{\gamma_1-\gamma_0},
 \qquad b_* =\frac{e_1-e_0}{\gamma_1-\gamma_0}.          \tag{4}
\]
The three errors are unique and their original finite parameters are
bad on their respective complements, also for any a,b with the same
syndrome pencil. D is nonzero at those parameters. Any persistent
coordinate locator must be at a coordinate common to all three
supports; thus the tau=0 rows automatically have no persistent
locator. In the tau=1 row its single common coordinate still requires
a nonpersistence check. No row asserts sixteen-count completion,
degree-four splitting, rational descent, a universal nine-union
extraction or an improved global count. This is a reproduction of
L016's analytic mechanism with arbitrary supports and finite parameters,
not an import of its fixed-triple count five. A separate critical audit
on 2026-10-08 found no defect in these conditional claims; it establishes
no completion or global bound.

## Proof

### Standard inputs and their specialization

L010 gives ker(sigma)=C, uniqueness of a weight-at-most-four
representative, and the weight-four pointwise Hankel/locator formulas.
The standard GRS dimension and distance input is J. I. Hall,
*Notes on Coding Theory*, GRS chapter, Theorem 5.1.1 and its proof,
printed pp. 63–64 of the undated
[author-hosted chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf)
inspected in the reused assessment. Its hypotheses hold over F:
the sixteen evaluation points are distinct, all multipliers are one,
and 0<8<=16. No general distance theorem is reproved here.

For the kernel restricted to U use I. Marquez-Corbella and R. Pellikaan,
*A characterization of MDS codes that have an error correcting pair*,
FFAA 40 (2016), 224–245,
[DOI 10.1016/j.ffa.2016.04.004](https://doi.org/10.1016/j.ffa.2016.04.004),
section 5, Definitions 5.1–5.2, Lemma 5.3 and the following unnumbered
GRS shortening formula, printed pp. 7–8 of the
[accepted manuscript dated 2016-02-29](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf).
These passages were inspected in the reused assessment. Shorten C at
exactly the seven labels in H minus U: first require zeros at those
labels and then delete them. Coordinate permutations move each deleted
label to the final position of the cited formula and move the retained
labels back afterward; they alter neither codeword zero conditions nor
evaluation multipliers. At step r=0,...,6 the current dimension
is 8-r>=2 and the length is 16-r. The next deletion changes the
dimension to 7-r>=1, multiplying each retained multiplier by its
difference from the deleted label. Every such difference is nonzero.
The final code is GRS_1 on U with multipliers
product_(y in H minus U)(x-y)=c_x. Equivalently,
\[
 \ker(\sigma|_{F^U})=\{\lambda c:\lambda\in F\}.        \tag{5}
\]
The general MDS shortening lemma's numerical hypothesis is also met:
16-7>=8. The explicit GRS formula identifies the multipliers, not
just the dimension. This repeats L016's analytic shortened-kernel
passage with U unrestricted. Its numerical certificate is not used.

### Complete support count and nonzero kernel coefficient

The alpha_i in (1) satisfy sum alpha_i=0 and
sum alpha_i gamma_i=0. Therefore the actual syndromes give
sigma(sum alpha_i e_i)=0. Equation (5) proves (2) with a unique
lambda, since c is nonzero.

Let m_j count coordinates with exactly j memberships among the A_i.
Counting coordinates and incidences gives
\[
 m_1+m_2+m_3=9,\qquad m_1+2m_2+3m_3=12,
 \qquad m_2+2m_3=3.                                    \tag{6}
\]
Thus either m_3=0,m_2=3,m_1=6, or m_3=1,m_2=1,m_1=7.
In particular a singleton coordinate exists. At one such coordinate
x in A_i, (2) gives alpha_i e_i(x)=lambda c_x, so full weight
forces lambda!=0. No lambda=0 full-weight branch is discarded.

For m_3=0 the three nonnegative integers n_01,n_02,n_12 sum
to three. Permuting the three error indices permutes these three
pair types arbitrarily. Their possibilities are consequently
(3,0,0),(2,1,0),(1,1,1) up to permutation. The four-element
support condition gives s_i=4-n_ij-n_ik. For m_3=1 the unique
double pair can be renamed {0,1}; then
s_i=4-n_ij-n_ik-1. These computations give the four rows exactly.
Every row has valid nonnegative singleton counts; assigning disjoint
sets of coordinates to its indicated types yields four-element
supports with union nine. No field-label or equality-completion
property is used in this enumeration.

### Coordinate parameterization and every degeneracy

Divide (2) at each x by lambda c_x. It says exactly
sum_(i in I_x) b_(i,x)=1. All present b_(i,x) are nonzero since
alpha_i,lambda,c_x and the actual weights are nonzero. Solving this
single coordinate equation gives the three membership rows and their
gates. Conversely each row satisfies that equation with precisely
the required full weights. This proves (3) in both directions.

For completeness retain lambda=0 before normalizing. Put
z_(i,x)=alpha_i e_i(x). The general solution at a singleton is
z_i=lambda c_x; at a double it is
z_i=d_x,z_j=lambda c_x-d_x; at a triple it is
z_0=d_(0,x),z_1=d_(1,x),z_2=lambda c_x-d_(0,x)-d_(1,x).
Here lambda and all displayed d's are unconstrained linear parameters.
There are m_2+2m_3=3 d's, so this parameterization is a linear
bijection from F^4 onto the moment-relation kernel. Injectivity follows
by recovering lambda at any singleton and the d's at the shared
coordinates. Surjectivity follows from (5) and the coordinate equations.
The lambda=0 subspace therefore has dimension three; all its singleton
weights vanish. It cannot describe the stipulated full-weight errors.
For lambda!=0, common scaling by lambda^-1 scales the errors and
both input words and preserves agreement/failure because the code
and its restrictions are linear. This fixes lambda=1 and leaves
exactly the three normalized shared-coordinate parameters.

An affine vector f(T) has sum alpha_i f(gamma_i)=0 because both
sum alpha_i and sum alpha_i gamma_i vanish. Its three values cannot
be these e_i, whose sum is the nonzero word lambda c. This explains
why the injective affine-lift argument for unions at most eight does
not apply. It is the one-dimensional codeword defect, not an omitted
zero-syndrome solution.

### Converse, original chart and same-support failure

Start with supports, parameters and gated weights as stated in the
converse. The coordinate formulas prove (2); c belongs to C by (5).
Thus sum alpha_i sigma(e_i)=0. Since alpha_2!=0, this is exactly
the affine interpolation relation through the first two syndromes.
Formula (4) realizes it at the original gamma_i without changing
parameters or the excluded projective direction [sigma(b)]. If the
first two syndromes are anchored to specified a,b, equality of the
two affine syndrome polynomials proves the third anchor too.

Full-weight choices exist for every row: choose lambda=1, choose
p_x=2 at every double, and choose p_x=q_x=1 at the triple, if present.
The other double weight and the third triple weight are -1.
They are all nonzero in characteristic 97. This proves only local
compatibility, not existence under the original sixteen-count premise.

The A_i are distinct: if two were equal, their union with the third
four-set would have size at most eight. Suppose
beta_0 sigma(e_0)+beta_1 sigma(e_1)=0. Then
beta_0 e_0+beta_1 e_1 is a codeword supported on at most eight
coordinates, hence is zero by the cited distance nine. Each of the
two distinct equal-size supports has a coordinate outside the other;
its nonzero error weight forces the corresponding beta to vanish.
The syndromes are independent. The transformation in (4) from the
first two syndromes to sigma(a_*),sigma(b_*) has determinant
1/(gamma_1-gamma_0), so these coefficient syndromes are independent
as well. No zero or dependent syndrome-direction case remains.

Every e_i is unique by L010's distance-based uniqueness, and
a+gamma_i b-e_i belongs to C whenever a,b realize the same pencil.
Hence there is agreement on S_i=H minus A_i, of size twelve.
Suppose b|_(S_i) belonged to C|_(S_i). Subtracting a codeword
with that restriction would give a word f supported on A_i with
sigma(f)=sigma(b). Since sigma(e_i)=sigma(a)+gamma_i sigma(b),
the whole pencil would belong to span{(x,x^2,...,x^8):x in A_i}.
For j!=i, sigma(e_j) would then have a representative supported on
A_i of weight at most four. Uniqueness forces it to equal e_j,
so A_j would be contained in A_i. Both have size four and are
distinct, a contradiction. Thus b fails on S_i, proving the actual
same-support event, rather than substituting sparse decodability.
This argument does not assume that the constructed pencil is
nonpersistent. Adding codewords to either input does not change it.

Finally L010's pointwise identities give
\[
 D(\gamma_i)=\det(V_{A_i})^2\prod_{x\in A_i} e_i(x)x\ne0,
 \qquad L(\gamma_i,X)=D(\gamma_i)\prod_{x\in A_i}(X-x).
\]
Consequently D is not the zero polynomial. If x is absent from some
A_i, then ell_x(gamma_i)!=0, so ell_x is not identically zero.
Only a coordinate in all three supports can remain a persistent
locator. For tau=0 none can; for tau=1 this reasoning leaves precisely
the common coordinate unchecked. Even in the nonpersistent rows,
these identities do not verify sixteen distinct finite bad parameters
or L010's global equality criterion. All additional parameters,
lower-weight errors and coordinate splitting/completion conditions
remain outside this local converse.

### Separate critical audit (2026-10-08)

The audit checked the full statement and proof against L010's actual
kernel, distance, pointwise identities and equality hypotheses, and
reused the precise standard-source coverage cited above. No defect or
missing mathematical premise was found. In particular:

- Seven successive shortenings use dimensions 8 through 2 before
  deletion and end at dimension 1. Coordinate permutations preserve
  the label-multiplier pairs; the successive factors are x-y, not
  their reciprocals. Extending the shortened codeword by seven zeros
  gives exactly the original shifted-moment kernel in (5).
- The incidence count is exhaustive. For tau=0 the permutation action
  on the three pair types is the full permutation group, yielding
  exactly the three listed partitions of 3. For tau=1 it is transitive
  on the one double pair. All four singleton-count rows sum correctly
  and make each support have size four. No other triple-intersection
  value is compatible with (6).
- The homogeneous kernel concerns twelve independently indexed weights,
  with weights at a shared label still separate for each error. The
  coordinate parameterization is bijective, including lambda=0 and
  possible cancellations at shared coordinates. Full weights remove
  exactly the stated gates. Normalizing lambda scales the pencil too;
  it does not claim to preserve an externally fixed nonzero pencil.
  The anchoring assertion applies to the unscaled weights of (3).
- In (4) the first two vector values are exactly e_0 and e_1. At the
  third parameter the residual is
  a_*+gamma_2 b_*-e_2=-(lambda/alpha_2)c, a codeword. This verifies
  the interpolation sign and the original finite chart directly.
  The two-syndrome change of basis has the stated nonzero determinant;
  independence uses distance nine and distinct full four-supports,
  without any rationality assumption on weights or parameters.
- Uniqueness is used only for representatives of weight at most four.
  If b agreed with a codeword on S_i, its residual on A_i and e_i
  would represent the whole pencil on A_i. At a different selected
  parameter uniqueness would force its actual distinct four-support
  into A_i, a contradiction. Thus agreement and input failure use
  the same twelve-coordinate S_i, which meets the pinned radius cell.
  This proof covers every pair of words with the given syndromes.
- The pointwise Hankel factorization is proved in L010 before any use
  of global locator nonvanishing. It therefore applies to the converse.
  Absence from one selected support proves a coordinate locator is
  nonzero as a polynomial; presence in all three supports does not
  prove it is zero or nonzero. Accordingly the tau=1 common locator,
  sixteen-count completion and universal extraction remain unchecked.

This is a correctness audit of the existing reproduction, not an
additional theorem or a verification of the challenge. The original
excluded projective direction is unrestricted. L016's finite certificate
and count five are not used, and no finite computation is required here.

## Mathlib

The full arbitrary-nine-union compatibility criterion and its
membership classification: **not checked**. Supporting GRS shortening,
shifted-moment kernel, distance, Vandermonde, affine interpolation and
Hankel/locator identities: **not checked** in Mathlib for this step.
L010 and the precise standard citations above are the informal inputs;
no matching Mathlib theorem or Lean verification is claimed. The
fixed L016 finite certificate is not an input to this result.
