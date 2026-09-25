# L010 — Sixteen-challenge bound for nondegenerate locator pencils

## Hypotheses

Let F be a finite field of order q containing a multiplicative subgroup
H of order sixteen, and let
\[
 C=\{(p(x))_{x\in H}:p\in F[X],\ \deg p<8\}.
\]
Fix words a,b in F^H. Use the event from
[the pinned affine-line model](../foundations/02-pinned-affine-line-model.md)
at a radius 1/4<=delta<5/16, so its agreement supports have size at
least twelve. Let B(a,b) denote its set of bad parameters in F.

For 1<=j<=8 put
\[
 \sigma_j(z)=\sum_{x\in H}z_xx^j,\qquad
 s_j(T)=\sigma_j(a)+T\sigma_j(b).
\]
Define polynomials
\[
 D(T)=\det(s_{i+j+1}(T))_{0\le i,j\le3},
\]
\[
 L(T,X)=\det\begin{pmatrix}
 s_1&s_2&s_3&s_4&s_5\\
 s_2&s_3&s_4&s_5&s_6\\
 s_3&s_4&s_5&s_6&s_7\\
 s_4&s_5&s_6&s_7&s_8\\
 1&X&X^2&X^3&X^4
 \end{pmatrix},\qquad \ell_x(T)=L(T,x)\quad(x\in H).
\]
The s_j in the determinant are evaluated at the indeterminate T.
Assume that D and all sixteen ell_x are nonzero polynomials in F[T].
Individual parameter values with D(gamma)=0 are allowed. No restriction
to prime-subfield input words or to a subgroup orbit is imposed.

## Conclusion

Every gamma for which a+gamma*b has an error representative of weight at
most four is bad on the complement of that error's support. That error
representative is unique. Let N_w be the number of such parameters whose
representative has weight exactly w, for 0<=w<=4. Then
\[
 4N_4+16N_3+32N_2+48N_1+64N_0
 \le\sum_{x\in H}\deg\ell_x\le64.                         \tag{1}
\]
Consequently
\[
 |B(a,b)|=\sum_{w=0}^4N_w
 \le16-3N_3-7N_2-11N_1-15N_0\le16.                       \tag{2}
\]

Equality |B(a,b)|=16 holds if and only if both of the following hold:

1. Every ell_x has degree four and splits into four distinct roots in F.
2. Each gamma that is a root of at least one ell_x has D(gamma)!=0
   and is a root of exactly four of the coordinate polynomials ell_x.

In this case all errors have weight four, their sixteen supports are
distinct, and each coordinate lies in exactly four supports. In particular,
any degree defect, any failure of this splitting/incidence criterion, or
any decodable parameter of weight below four gives at most fifteen bad
parameters under the stated hypotheses.

For H the order-16 subgroup of F_97^* and F=F_(97^20), the allowable
integer count at error budget 2^-128 is fifteen. Thus (2) alone does
not certify safety: its possible extremal count is one too large.
Neither existence nor impossibility of the equality configuration is
asserted. Pencils with D identically zero or some ell_x identically zero
are outside this statement. The general bounds 10/q and 69/q from L008's
lower construction and L004's certificate bound are not replaced by a
global 16/q bound.

## Proof

First, ker(sigma)=C. For 1<=d<=15 the sum of x^d over H is zero:
some h in H has h^d!=1, because X^d-1 cannot have sixteen distinct
roots, and multiplication by h both permutes that sum and multiplies it
by h^d. Thus each sigma_j annihilates evaluations of monomials of
degree less than eight. Any eight columns of the moment matrix are an
invertible Vandermonde matrix times a diagonal matrix with nonzero
entries x. Hence sigma has rank eight. Evaluation of polynomials of
degree less than eight is injective by the polynomial root bound, so
both C and ker(sigma) have dimension eight and are equal.

A nonzero codeword has weight at least nine, since its polynomial has
at most seven roots in H. Two representatives of the same syndrome
with weight at most four would differ by a codeword of weight at most
eight; hence they are equal. Agreement with a codeword on at least
twelve coordinates is equivalent to having such a representative.

We establish the locator facts, including a converse that will be needed
for equality. Write R(T) for the first four rows of the displayed
five-by-five determinant. Expansion along its last row gives
\[
 L(T,X)=\sum_{j=0}^4 c_j(T)X^j,\qquad c_4(T)=D(T).
\]
Each coefficient is a signed four-by-four minor of R(T), so every c_j
and ell_x has degree at most four in T. Substituting any row of R(T)
for the last row gives a determinant with two equal rows. Therefore
\[
 \sum_{j=0}^4c_j(T)s_{i+j}(T)=0\qquad(1\le i\le4).        \tag{3}
\]

Fix a parameter gamma with error e of support A and weight w<=4.
The moment matrix at gamma factors as
\[
 R(\gamma)=V\,\operatorname{diag}(e_xx)_{x\in A}\,W,
 \qquad V_{i,x}=x^i\ (0\le i\le3),\quad
 W_{x,j}=x^j\ (0\le j\le4).                               \tag{4}
\]
In particular its rank is at most w. If w=4, the first four columns
give
\[
 D(\gamma)=\det(V)^2\prod_{x\in A}e_xx\ne0.
\]
The row space of R(gamma) then equals the row space of W. Appending
(1,x,x^2,x^3,x^4) for x in A produces a dependent row, so the locator
has these four roots. Its leading coefficient is D(gamma), proving
\[
 L(\gamma,X)=D(\gamma)\prod_{x\in A}(X-x).                 \tag{5}
\]
Thus precisely four coordinate locators vanish at a weight-four parameter.

Conversely, suppose D(gamma)!=0 and L(gamma,X) has four distinct
roots A in H. Its degree is four, so its monic normalization P(X) is
the product of X-x over A. Solve the first four equations
\[
 \sum_{x\in A}e_xx^j=s_j(\gamma)\qquad(1\le j\le4)
\]
by the invertible Vandermonde matrix. The moments generated by these
weights satisfy the recurrence with characteristic polynomial P:
multiply P(x)=0 by e_x*x^i and sum over x. Equation (3), divided by
D(gamma), gives the same recurrence for the supplied moments, for
i=1,...,4. Starting from the first four moments, induction gives equality
also for s_5,...,s_8. Thus the resulting e has the required full syndrome.
None of its four weights is zero, since otherwise (4) would force
D(gamma)=0. The kernel identity makes a+gamma*b-e a codeword. This
proves the converse without assuming that a split locator is automatically
a valid decoder output.

Next we check failure on the very same support, rather than counting
decodability as a substitute for the event. Let e be the representative
at gamma_0, let A=supp(e), and let S=H minus A. Suppose b|_S belonged
to C|_S. Some word f supported on A would then satisfy sigma(f)=sigma(b),
by subtracting a codeword agreeing with b on S. Hence over F[T]
the pencil's moments would be those of the word
\[
 e+(T-\gamma_0)f,
\]
supported on the fixed set A. If |A|<=3, the rank bound in (4), now
over F(T), forces D to be identically zero. If |A|=4, appending the
row (1,x,x^2,x^3,x^4) for any x in A gives a dependent determinant
for the whole pencil, so ell_x is identically zero. Both conclusions
contradict the hypotheses. Thus b fails on S, while a+gamma_0*b
agrees there with a codeword. Since |S|>=12, gamma_0 is bad.
The reverse implication follows immediately from the event's agreement
condition, completing the identification of B(a,b) with the decodable set.

For a parameter gamma_0 of weight w<=3, every four-by-four minor of
R(T) is divisible by (T-gamma_0)^(4-w). Indeed, put U=T-gamma_0
and write each such square matrix as M_0+U*M_1. Its constant matrix
has rank at most w by (4). In the determinant's multilinear expansion
by rows, a term of degree j<4-w uses more than w rows of M_0.
Those rows are linearly dependent even before the other rows are added,
so that term vanishes. This proves the divisibility claim for every c_j
and therefore every ell_x. The case w=0 is included and yields order
at least four at all sixteen coordinates. This argument treats finite
singular parameter values even though D is not the zero polynomial.

For a nonzero univariate polynomial, the sum of its multiplicities at
distinct field roots is at most its degree: the corresponding powers of
distinct linear factors divide it. Apply this to each of the sixteen
ell_x. A weight-four parameter contributes at least one at each of its
four coordinates, by (5). A weight-w parameter with w<=3 contributes
at least 4-w at every coordinate. Sum these contributions over the
distinct parameters and then over x in H. This gives (1). Divide by
four and subtract the extra costs of weights zero through three to
obtain (2).

Suppose |B(a,b)|=16. Equation (2) forces N_0=N_1=N_2=N_3=0.
All inequalities in (1) must be equalities. In particular every ell_x
has degree four, and all its degree is used by distinct weight-four
parameters at whose supports x occurs. It therefore has exactly four
distinct roots in F, all bad, with no repeated or additional roots.
At each root parameter (5) says that D is nonzero and exactly four
coordinate locators vanish. This proves both necessary conditions.

Conversely, assume the two displayed equality conditions. Each of the
sixteen ell_x has four distinct field roots, giving 64 incidences.
Every parameter appearing among these roots has exactly four incidences,
so their union has sixteen elements. At each such parameter D is nonzero
and the locator has four distinct roots in H. The converse locator
argument and the same-support argument prove it is bad. The upper bound
(2) gives equality and excludes additional bad parameters.

In this case no two of the sixteen error supports can be the same set A.
If two distinct parameters had errors e_1,e_2 on A, subtracting their
syndromes would give a representative of sigma(b) supported on A.
The entire pencil would then be represented on A, forcing ell_x to be
identically zero for x in A as above. Finally, the four roots of each
ell_x are exactly the four parameters whose errors use coordinate x.
This proves the asserted distinctness and balanced incidence.

The field-budget comparison is the exact integer inequality
\[
 15\cdot2^{128}\le97^{20}<16\cdot2^{128}.
\]
For a fixed pair, its error contribution is |B(a,b)|/q. A bound of
sixteen therefore leaves the threshold undecided; a strict improvement
to fifteen for that pair would place its contribution within budget.
An upper bound for the maximum E_C would additionally have to cover
every input pair, including the excluded polynomial degeneracies.
No part of the proof identifies the frozen event with the unread ABF26
definition or resolves another radius cell.

The auxiliary command `python3 scripts/locator-incidence/check.py`
checks the determinant polynomials and their incidence counts over F_97.
It independently tests the original support event on all 2517 admissible
supports for the two-block construction and four pencils with a prescribed
weight-zero, -one, -two, or -three parameter. It checks the multiplicity
claims and the converse locator test at every field parameter. All five
pencils satisfy the nonvanishing hypotheses; the two-block example has
ten bad parameters, and each of the other four has just the prescribed
zero parameter over F_97. A fixed-four-coordinate pencil has 97 decodable
parameters but only four bad ones; its persistent locator roots exclude
it from the theorem. These are checks of the algebra and hypotheses,
not a maximization over pencils or an extrapolation of these finite counts
to extensions. The proof above applies over the full stated field.

## Mathlib

Coverage of the full incidence bound and equality characterization in
Mathlib: **not checked**. Coverage of supporting determinant, Vandermonde,
polynomial-root, and multiplicity results: **not checked**. No matching
theorem or Lean verification is claimed; the required arguments are given
above.

The previously read ArkLib declarations
[`CoreDefinitions.IsMCA` and `CoreDefinitions.mcaError`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ProximityGap/ProximityGenerators.lean#L98)
support the frozen event definition only. ArkLib is separate from Mathlib;
these declarations do not match the incidence theorem or certify its
correspondence with the unread ABF26 definition.
