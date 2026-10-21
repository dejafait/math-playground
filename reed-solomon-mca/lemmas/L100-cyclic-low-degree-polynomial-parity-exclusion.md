# L100 — No additional polynomial product parity through degree four

## Hypotheses

Let k=F_97, let H be its subgroup of order sixteen, and let
h:Z/16Z -> H be any bijection. In V=k^8 use coordinates numbered
0,...,7 and put

    v_i=(1,h(i),...,h(i)^7)^transpose,
    B_s={s,s+1,s+4,s+6},   U_s=span_k{v_i:i in B_s}.

Suppose P is a two-dimensional k-subspace meeting every U_s nontrivially,
as in L097. Let E=k[X]_{<=7}, W=Ann(P) subset E, C=ev_h(W), and
D=(C*C)^perp, with the ordinary coordinate pairing. Thus dim W=6.
For R in k[X] of degree at most four, put z(R)_i=h(i)R(h(i)).
The zero polynomial is included. All full cyclic-plane conditions are
retained; the existence of P is not assumed established.

## Conclusion

    z(R) in D  if and only if  R is constant.

Equivalently, the intersection of D with this five-dimensional
polynomial-weight family is precisely k*(h(i))_i. In particular it
contains exactly one independent parity direction, against the six
needed for the previously proposed square-dimension upper bound ten.

This is a uniform exclusion of the specified nonconstant ansatz,
conditional on P. It neither excludes P nor supplies an upper bound
for the whole Schur square. General dense parities, uniform triangle
twelve, arbitrary equality families and challenge qualifications remain
unresolved; the interval 11/q–16/q is unchanged. The separate step-271
critical audit below found no defect in this conditional obstruction.

## Proof

### Inputs and why the specialization is needed

Use L097's exact equivalence between membership in D and all twenty-one
unordered basis-product equations for W. The standard underlying
adjunction is Hugues Randriambololona, *On products and powers of linear
codes under componentwise multiplication*, Contemp. Math. 637 (2015),
3–78, Proposition 2.38, printed p. 28 of the
[author manuscript](https://perso.telecom-paristech.fr/randriam/maths/HR_AGCT-14.pdf),
[DOI 10.1090/conm/637/12749](https://doi.org/10.1090/conm/637/12749).
Its applicability without an MDS assumption is already justified in
L097 and its separate step-256 audit. No reproof of that theorem is
needed. L097 also proves that z(1) belongs to D.

L089, applied exactly as justified in L097, gives sixteen distinct
lines P intersect U_s, each with four nonzero block coefficients.
These conclusions hold over k: ranks and intersection dimensions do
not change on extending k to F_(97^20), and the defining matrices are
over k. L010 supplies the subgroup power sums and Vandermonde facts.
Below we specialize its locator determinant directly to the unshifted
moments of a newly chosen chart in P. We do not apply its bad-event
conclusion, assume an original chart, or use L096's realization.

The prior EXPLORE assessment
`drafts/literature/2026-10-17-cyclic-dense-polynomial-parity-test.md`
found no inspected theorem deciding this bounded family. The new work
is the coefficient-form calculation and its incompatibility with the
full block relations. Neither the general adjunction nor a full-GRS
conductor formula supplies that incompatibility.

### A plane direction with six zero initial moments is impossible

Let T_2=span_k{e_6,e_7} in V, where e_j is the coordinate unit vector.
We first show P intersect T_2=0. Suppose instead that 0!=t is in this
intersection, and choose a in P independent of t. No U_s contains t:
the first four coordinates of any vector sum_(i in B_s) c_i v_i are
an invertible four-by-four Vandermonde matrix times (c_i), whereas
the first four coordinates of t vanish. Thus each line P intersect U_s
has a unique representative a+lambda_s t. Its four block coefficients
c_(s,i) are nonzero, and the sixteen scalars lambda_s in k are distinct
by distinctness of the intersection lines.

Write m_j(T)=a_j+T t_j for 0<=j<=7. In particular m_0,...,m_5
are constant. Define

    D_0(T)=det(m_(r+c)(T))_(0<=r,c<=3),

    L(T,X)=det [ m_0 m_1 m_2 m_3 m_4
                 m_1 m_2 m_3 m_4 m_5
                 m_2 m_3 m_4 m_5 m_6
                 m_3 m_4 m_5 m_6 m_7
                   1   X   X^2 X^3 X^4 ].

Only the third and fourth rows depend on T. Determinant multilinearity
therefore gives deg_T L(T,x)<=2 for every fixed x in k, including all
cancellations and the possibility that the polynomial is identically zero.

At T=lambda_s the moments are sum_(i in B_s)c_(s,i)h(i)^j.
Let A_s=(h(i)^r)_(0<=r<=3,i in B_s), and let
J_s=(h(i)^c)_(i in B_s,0<=c<=4). The first four rows of L factor as
A_s diag(c_(s,i)) J_s. Their first four columns give

    D_0(lambda_s)=det(A_s)^2 product_(i in B_s)c_(s,i) != 0.

For x=h(i) with i in B_s the last row of L is already in the row
space of J_s, so L(lambda_s,x)=0. Its X^4 coefficient is
D_0(lambda_s). Consequently

    L(lambda_s,X)=D_0(lambda_s) product_(i in B_s)(X-h(i)).  (1)

This is L010's full-weight locator factorization with unshifted weights
c_(s,i); the displayed factorization verifies the change of convention.
Only actual nonzero block coefficients are used, not hypothetical error
weights or nonpersistent-locator assumptions.

Fix any coordinate i. Exactly the four distinct blocks with shifts
i,i-1,i-4,i-6 contain it. Thus L(T,h(i)) has the four distinct roots
lambda_s from those blocks. Its degree at most two forces it to be
identically zero. But any of the other twelve blocks omits i; at its
parameter (1) gives a nonzero value because D_0(lambda_s)!=0 and
all labels are distinct. This contradiction proves P intersect T_2=0.
In particular every deficient-degree branch of the locator is retained;
no generic-rank or nonvanishing assumption entered this argument.

### The complete polynomial-weight form

Suppose now that R is nonconstant of exact degree d, 1<=d<=4, with
coefficients r_0,...,r_d and r_d!=0. For arbitrary f,g in E,
the polynomial XRfg has degree at most nineteen and has no constant
term. The only exponent divisible by sixteen that can occur is sixteen.
L010's power sums, together with x^16=1 on H, therefore give

    sum_(x in H) x R(x)f(x)g(x) = 16 coeff_(X^15)(Rfg).           (2)

For exponents seventeen through nineteen, reduce to exponents one
through three using x^16=1. The scalar 16 is nonzero in k. Formula
(2) is valid even if R vanishes at some or all of its possible roots
in H; it divides by no evaluation of R.

Let beta_R(f,g)=coeff_(X^15)(Rfg). The assumption z(R) in D is exactly
beta_R(W,W)=0, by L097's full twenty-one-equation test and bilinearity.
We compute its radical on all of E, without choosing a generic W.

Put A_d=k[X]_{<=7-d}, of dimension 8-d. Every element of A_d
pairs to zero with E, since the degree of Rfg is then at most fourteen.
On the complementary ordered monomials X^(8-d),...,X^7 the matrix has
zero entries strictly before its anti-diagonal and constant anti-diagonal
r_d. More explicitly its (u,v) entry, 0<=u,v<d, is
r_(2d-1-u-v), interpreting coefficients outside 0,...,d as zero.
Its determinant is (-1)^(d(d-1)/2) r_d^d, which is nonzero. Hence
the radical is exactly A_d and the quotient E/A_d is nondegenerate
of dimension d, including all choices of lower coefficients of R.

Let m=dim(image(W -> E/A_d)). This image is totally isotropic for
the induced nondegenerate bilinear form. For such a subspace U,
U subset U^perp and dim U^perp=d-dim U; thus 2m<=d. Also

    dim(W intersect A_d)=6-m.                              (3)

We now exhaust the four possible exact degrees.

* If d=1, then m=0, so W subset A_1. Its annihilator P contains
  Ann(A_1)=k e_7, contradicting P intersect T_2=0.
* If d=2, then m<=1. The annihilator in T_2 of the top-two-coordinate
  image of W has dimension 2-m>=1. That annihilator is precisely
  P intersect T_2, again a contradiction.
* If d=3, then m<=1, so (3) gives dim(W intersect A_3)>=5.
  Since dim A_3=5, A_3 subset W. Consequently every vector of P
  has its coordinates 0,...,4 zero. No nonzero vector of any U_s
  has even its first four coordinates zero, by the four-column
  Vandermonde argument above. This contradicts P intersect U_s!=0.
* If d=4, then m<=2, so (3) gives dim(W intersect A_4)>=4.
  Since dim A_4=4, A_4 subset W. Every vector of P has its first
  four coordinates zero, contradicting the same block intersection.

Thus no nonconstant R in the specified range works. Every constant R
does work by L097's z(1) parity and linearity, including R=0. Finally
R -> z(R) is injective on degree-at-most-four polynomials: h(i)!=0
and sixteen distinct zeros would force such a polynomial to be zero.
This proves the exact one-dimensional intersection asserted above.

The proof uses all product equations through total isotropy, not one
selected factor. It includes zero evaluations, smaller exact degrees,
all lower-coefficient degeneracies, and every possible restricted-form
rank. It performs no labeling census. The new chart is used only for
a plane-vector contradiction, with no assertion about a prescribed
affine chart or its excluded point. The surviving constant direction
and unresolved general dense directions are consistent with this
exclusion; no contradiction to plane existence follows.

### Separate critical audit — October 17, 2026, step 271

This separate proof audit used the unchanged pre-invocation EXPLORE
assessment `drafts/literature/2026-10-17-cyclic-low-degree-parity-audit-scope.md`.
It checked the entire proof, the relevant L010 factorization, and the
precise L089/L097 input scopes. No mathematical defect or change to the
argument was found. This is verification of an existing local result,
not a new theorem, a new source import or certified originality.

**Plane input and scalar extension.** If a,b form a k-basis of P, they
remain independent over F_(97^20). For every s the quotient map from P
to V/U_s has rank at most one, since its kernel is nonzero. Therefore
a wedge b is a nonzero element of the exact common exterior kernel
in L089. Its plane is P after extension. L089 and its step-226 audit
supply distinct one-dimensional block intersections and full coefficients.
Intersection dimensions are computed by matrix ranks over k and cannot
change after extension. The intersection lines hence have nonzero
k-rational representatives, and their unique coefficients in the four
independent block columns lie in k and are nonzero there. This uses
neither actual errors nor a prescribed affine chart. L097's step-256
audit already checked this specialization; no extra input is needed.

**The low-degree locator contradiction.** A vector t in T_2 has
coordinates 0,...,5 zero. In particular its first four coordinates
vanish, so membership in any U_s would force all four coefficients to
vanish by the invertible initial Vandermonde. Thus a nonzero t in P
is outside every block line. For any independent a in P, the coefficient
of a in every block-line representative is nonzero; normalizing it to
one gives a unique a+lambda_s t. Distinct block lines give distinct
lambda_s in k. Scaling the representative preserves all four nonzero
block coefficients. This establishes every finite full block event
before the locator is used.

In the displayed determinant, rows one and two involve only m_0,...,m_5
and are constant in T. Rows three and four are affine in T, even when
t_6 or t_7 vanishes. The fifth row is constant. Multilinearity therefore
bounds the degree by two for each fixed x, without claiming exact
degree or assuming that the polynomial is nonzero. At each block
parameter the first four rows factor as A_s diag(c_(s,i)) J_s with
unshifted coefficients. The leading four-column minor is exactly
(det A_s)^2 product c_(s,i); there is no extra h(i) factor. Expanding
along the last row gives positive sign for its X^4 coefficient.
Invertibility makes the four block labels roots and the leading
coefficient nonzero, proving (1) directly from L010's algebraic method.
Its bad-event theorem, nonpersistent-polynomial hypotheses and L096
are not used.

For a fixed i the shifts i,i-1,i-4,i-6 are four distinct elements of
Z/16Z and hence give four distinct finite roots. The root bound makes
the degree-at-most-two polynomial identically zero. Among the other
twelve shifts, choose any one: its full block determinant and four
nonzero label differences make (1) nonzero at h(i). This contradicts
identical vanishing, including every possible degree drop and t_6=0
or t_7=0 case. Thus P intersect T_2=0 is valid under precisely the
stated plane hypotheses.

**Full product form and radical.** For arbitrary f,g in E, the
exponents of XRfg lie between one and nineteen. The sole possible
multiple of sixteen is sixteen; its coefficient is coeff_(X^15)(Rfg).
The subgroup sum for that monomial is 16, while every other monomial
sums to zero, including exponents seventeen through nineteen. Hence
(2) represents every product, not just a selected factor or diagonal
basis test. The twenty-one unordered products span the full symmetric
bilinear test. Zeros of R on H require no separate invertibility
assumption, because no evaluation of R is divided out.

For exact degree d the low-degree subspace A_d is in the radical by
the bound d+(7-d)+7=14. On the complementary monomials the index of
the required coefficient of R is 15-[(8-d+u)+(8-d+v)]
=2d-1-u-v. Entries with u+v<d-1 vanish, and the anti-diagonal is
r_d. Reversing the columns makes a triangular matrix with diagonal
r_d; undoing that reversal gives precisely the determinant sign
(-1)^(d(d-1)/2). Thus the stated radical is exact for every choice
of lower coefficients. In particular r_0 does not enter this form.
No generic-rank premise or diagonal-support restriction is present.

**All quotient dimensions.** Total isotropy of the image of W in
the nondegenerate quotient implies 2m<=d, regardless of whether that
quotient admits maximal isotropic spaces over k. Rank-nullity also
gives m>=6-(8-d)=d-2 whenever this lower bound is positive.
For d=1, m=0 and W is contained in A_1; double annihilation gives
e_7 in P. For d=2, the quotient is exactly the last two polynomial
coefficients, dual to T_2. Its annihilator inside T_2 is P intersect
T_2 and has dimension 2-m>=1. Both conclusions contradict the
proved locator obstruction.

For d=3 the two dimension bounds force m=1, so W intersect A_3 has
dimension five and equals A_3. For d=4 they force m=2 and W intersect
A_4=A_4 of dimension four. Thus P has its first five, respectively
first four, coordinates zero. Every nonzero block intersection would
contradict the same initial four-column Vandermonde. Smaller m in
either branch is already impossible by dimensions, rather than an
omitted restricted-rank case. These four cases exhaust every
nonconstant polynomial in the target range.

**Constants, scope and dependencies.** The zero vector is included,
and L097's power-sum argument gives z(c)=c z(1) in D for every
constant c. Injectivity of R -> z(R) follows from the sixteen distinct
nonzero evaluation labels and deg R<=4, so the intersection really
has dimension one. It does not give six independent directions or
contradict plane existence. The direct inputs remain exactly L010,
L089 and L097 as in the DAG; their indirect hypotheses and the existing
source qualifications are retained. The complete uniform argument
requires no finite script, sampled labeling, or certificate replay.
Mathlib coverage is still not checked. This audit supersedes the
pending-L100-audit wording in the unchanged PROOF.md overview; it
does not alter that overview's argument or the global error interval.

## Mathlib

Full matching coverage of this conditional polynomial-parity exclusion
has not been checked. No matching theorem or absence is claimed.
The existing L010/L089/L097 qualifications are retained. The imported
code-product adjunction has the precise citation above; the elementary
bilinear radical and specialized determinant arguments are written out
because they are the load-bearing local steps, not asserted library inputs.
