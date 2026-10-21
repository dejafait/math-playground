# L030 — The cyclic 0135 family cannot realize equality

## Hypotheses

Let F be any finite extension of F_97, H the order-sixteen subgroup
of F_97^*, and lambda: Z/16Z -> H any bijection. Put
\[
 C=\{(p(x))_{x\in H}:\deg p<8\},\qquad
 J_t=\{t,t+1,t+3,t+5\}\pmod {16},\quad A_t=\lambda(J_t).
\]
Fix words a,b in F^H and 1/4<=delta<5/16, with bad parameters
defined by [the pinned affine-line event](../foundations/02-pinned-affine-line-model.md).
Use L010's moment pencil, Hankel determinant D(T), and coordinate
locator polynomials ell_x(T). Assume D and every ell_x are nonzero
polynomials. Singular values of D are not excluded by hypothesis.

## Conclusion

It is impossible to have sixteen bad parameters whose error supports
are exactly the sixteen sets A_t. This exclusion holds for every
lambda, arbitrary extension-field input words and arbitrary assignment
of the bad parameters to the supports.

Consequently, in L010's nonpersistent case, a pencil with sixteen bad
parameters must have a support family not isomorphic to these cyclic
0135 supports under any bijection to H. This is a single-family
exclusion, not a global fifteen-count bound. The overall interval
11/q–16/q on the four-omission cell remains unchanged. No assertion
identifying the pinned event with the unread ABF26 definition is made.

## Proof

### Equality supplies actual full-weight moment representatives

Suppose such a pencil exists. L010's equality characterization supplies
sixteen distinct finite parameters and unique error representatives of
weight exactly four, with distinct supports. We may therefore denote
the parameter assigned to A_t by gamma_t and its error by e_t. Every
coordinate of e_t on A_t is nonzero, and e_t is zero off A_t. No
assumption relating gamma_t or these weights under cyclic translation
is made. L010 also supplies D(gamma_t)!=0; the argument below does
not need to divide by this value or by a parameter.

Use zero-based vector indices, writing
\[
 \sigma_j(z)=\sum_{x\in H}z_xx^{j+1}\quad(0\le j<8),
 \qquad m_i=(\lambda(i),\lambda(i)^2,\ldots,\lambda(i)^8)^T,
 \qquad U_t=\operatorname{span}_F\{m_i:i\in J_t\}.
\]
This is precisely L010's sigma_1,...,sigma_8, reindexed, and L029's
column convention. The witnessing agreement gives a codeword c_t
with a+gamma_t b=c_t+e_t. L010 proves ker(sigma)=C, so, for
u=sigma(a) and v=sigma(b), the full eight moment equations are
\[
 u_j+\gamma_t v_j
   =\sum_{i\in J_t}(e_t)_{\lambda(i)}\lambda(i)^{j+1}
       \quad(0\le j<8),\qquad
 u+\gamma_t v=\sigma(e_t)\in U_t.                 \tag{1}
\]
The moment columns on every set of at most eight distinct indices are
independent by L010's Vandermonde argument. In particular sigma(e_t)
is nonzero: otherwise independence of the four columns in J_t
would force all four actual weights to vanish. This checks possible
vanishing parameter syndromes using the errors, rather than assuming
it from the rank theorem.

### The necessary alternating equations match L029

For each t set P_t(X)=prod_(i in J_t)(X-lambda(i)). Let R_t have
as its row r the coefficients of X^r P_t(X) in degrees 0,...,7,
for 0<=r<4. These are exactly L029's rows. For i in J_t,
\[
 (R_t)_r m_i=\lambda(i)^{r+1}P_t(\lambda(i))=0.
\]
The power j+1 in (1) is essential to this pairing. Thus (1) gives
R_t u+gamma_t R_t v=0. Put alpha=R_t u and beta=R_t v. For
every 0<=r<s<4,
\[
 \alpha_r\beta_s-\alpha_s\beta_r=0,               \tag{2}
\]
because alpha=-gamma_t beta. This remains true if beta or alpha
vanishes; no division is used.

Define the 28 coordinates p_jk=u_jv_k-u_kv_j for 0<=j<k<8.
Expansion of (2) gives, with the exact lexicographic convention of
L029,
\[
 \sum_{j<k}\bigl((R_t)_{rj}(R_t)_{sk}
              -(R_t)_{rk}(R_t)_{sj}\bigr)p_{jk}=0.
                                                               \tag{3}
\]
Hence M_t p=0 for all sixteen t. Audited L029 proves that the stack
of its first eight blocks has rank 28 over F for every lambda.
Therefore p=0.

The exterior-basis interpretation of these coordinates is the known
one used in L029: Keith Conrad,
[*Exterior Powers*](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf),
Theorem 4.2, printed p. 11, with induced-map functoriality in
Theorems 5.1 and 5.4, printed pp. 15–17. Their free-module hypotheses
hold for the finite-dimensional F-spaces here. No new exterior-algebra
result or new rank calculation is asserted; (1)–(3) verify the actual
error specialization of the already proved matrix.

### All syndrome dimensions, including dependent directions

If u and v were independent, p could not vanish. Explicitly, if u
is nonzero, choose j with u_j!=0. The relations p=0 give
u_j v_k=u_k v_j for every k, hence v=(v_j/u_j)u. If u=0, the
vectors are already dependent. This excludes dimension two and
shows that dim span{u,v} is zero or one.

If it is zero, every u+gamma_t v is zero, contrary to the nonzero
syndrome established after (1).

If it is one, write L=span{u,v}. For every t, (1) is a nonzero
vector of L, so it spans L and implies L subset U_t. This includes
u=0, v=0, and any attempted parameter at which u+gamma_t v vanishes:
such a parameter has already been excluded by the actual full weights.
There is no assumption that either quotient direction is nonzero.

For this actual family,
\[
 J_0=\{0,1,3,5\},\qquad J_6=\{6,7,9,11\}
\]
are disjoint. Their union consists of eight distinct indices, whose
eight moment columns are independent over F. If a vector belongs to
U_0 intersection U_6, expressing it in these two four-column spans
and subtracting gives a dependence among those eight columns.
All coefficients must be zero. Thus U_0 intersection U_6={0},
contradicting the inclusion of the nonzero line L in both spaces.
This disposes of dimension one and completes the contradiction.

### Scope and verification

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-06-cyclic-0135-equality-application.md`.
This reproduces L026/L027's general application mechanism with the
changed 0135 supports and L029's audited rank input; it does not import
their 0125-family conclusions. Writing the moment equations and actual
disjoint pair is necessary because the rank theorem alone cannot
exclude dependent directions. L010 supplies equality and moment facts;
L029 already supplies the annihilator rows and rank convention.
No mathematical script or sample labeling is a premise.

The argument checks all dimensions, full weights and finite distinct
parameters supplied by equality. It does not need further locator
conditions beyond those retained for invoking L010. Every independence
fact remains valid over the stipulated extension itself. In particular,
there is no cyclic symmetry assumption on lambda, weight transport,
generic minor, or exhaustive claim about other families. The separate
critical audit below found no defect in this application.

### Separate critical application audit, October 6, 2026

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-06-cyclic-0135-application-audit.md`.
This audit checks the application using L029's already audited rank;
it does not repeat rank discovery or extend the family theorem.
The exterior facts retain the precise Conrad citations above.

**Event and equality input.** Since 11<16(1-delta)<=12, an admissible
agreement set has at least twelve coordinates. A witnessing codeword
therefore gives an error of weight at most four. L010 applies over
the stipulated F: H has order sixteen, the code has dimension eight,
and D and every ell_x are nonzero polynomials. Its upper bound makes
the assumed sixteen bad parameters an equality case. In its multiplicity
inequality, any parameter of weight below four costs strictly more than
four of the total degree budget 64. Equality therefore forces all
sixteen errors to have weight four. Its minimum-distance argument
gives uniqueness, and its fixed-support argument rules out repeated
supports. Its weight-four factorization gives D(gamma_t)!=0, although
this application never divides by D. Parameters are distinct elements
of F; no projective parameter or infinity case is part of this event.

The application uses the necessary agreement part of badness, without
substituting closeness for the same-support failure condition: L010's
equality input already concerns exactly the pinned event. Singular
values are excluded at the sixteen witnessed parameters by equality,
not by an extra assumption on the entire pencil.

**Actual moments and signs.** A degree-below-eight codeword contributes
monomials of exponents 1 through 15 to the eight moments. L010's
subgroup-sum argument annihilates each, so sigma(c_t)=0 in all eight
coordinates. Thus (1) uses the actual nonzero error coordinates on A_t.
L029's b_i is exactly m_i; standard index j corresponds to coefficient
degree j and moment power j+1. A row of X^r P_t therefore pairs with
m_i as lambda(i)^(r+1)P_t(lambda(i)). There is no transpose or
reciprocal-coordinate change.

For two rows a_j=(R_t)_{rj}, b_j=(R_t)_{sj}, the ungrouped expansion
of (2) is sum_(j,k) a_j b_k (u_j v_k-u_k v_j). Diagonal terms
vanish. Grouping (j,k) with (k,j), for j<k, gives exactly
(a_j b_k-a_k b_j)(u_j v_k-u_k v_j), with neither a factor of two
nor a sign reversal. These are all six rows of L029's M_t in its
lexicographic convention. The first eight actual supports supply the
rank-28 stack. Arbitrary assignment of gamma_t to supports changes
none of this. If R_t v=0 then R_t u=0 too, and the alternating
equations still hold without division.

**Every syndrome dimension.** The determinant of eight moment columns
is the product of their nonzero labels and their pairwise differences,
as checked in L029. Extend any four columns to eight to obtain their
independence. Thus every actual full-weight error has nonzero syndrome.
Rank gives p=0, whose coordinate argument above excludes dimension two.
Dimension zero contradicts the nonzero syndromes. In dimension one,
each nonzero u+gamma_t v spans the same line L, including u=0 or
v=0. A parameter making this combination zero cannot have its stated
actual error, so is not an omitted case. The actual J_0 and J_6 have
union {0,1,3,5,6,7,9,11}, with eight distinct indices. Their moment
columns are independent for every bijection and allowed extension.
Subtracting two expressions of a vector in U_0 intersection U_6
forces all eight coefficients to vanish, contradicting the common
nonzero line. This exhausts dimension one.

All bridges in the approved audit survive. This verification supplies
no repaired error, new theorem, finite computation or improved global
count. Direct mathematical inputs remain L010 and L029. Arbitrary
families, the global fifteen bound and ABF26 identification remain
unresolved; full Mathlib coverage remains not checked.

## Mathlib

Coverage of this exact 0135 equality-family exclusion is **not checked**.
No full matching theorem, absence claim, or Lean verification is
asserted. L010 and L029 retain their stated qualifications for the
supporting moment, Vandermonde and exterior-algebra results.
