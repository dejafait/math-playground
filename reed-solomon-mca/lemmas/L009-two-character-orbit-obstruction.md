# L009 — A two-character subgroup orbit gives only four directions

## Hypotheses

Let F be a finite field containing a multiplicative subgroup H of order sixteen,
and let K={x in H:x^4=1}, its order-four subgroup. In particular the
characteristic of F is not two. Let
\[
 C=\{(p(x))_{x\in H}:\deg p<8\},\qquad
 \sigma_j(w)=\sum_{x\in H}w_xx^j\quad(1\le j\le8).
\]
Write sigma(w) for this vector of eight moments. Let e be a nonzero
word of weight at most four, and define its multiplicative shifts by
e^(t)_x=e_(t^(-1)x), for t in H. Assume that the sixteen vectors
sigma(e^(t)) span a vector space of dimension at most two over F.

The application takes H to be the order-16 subgroup of F_97^*, inside
any extension F of F_97. The MCA event is the one in
[the pinned affine-line model](../foundations/02-pinned-affine-line-model.md),
with agreement supports of size at least twelve.

## Conclusion

There are a in H, u in {1,2,3,4}, and lambda in F^* such that
\[
 e_x=\begin{cases}\lambda x^{-u}&x\in aK,\\0&x\notin aK.\end{cases}       \tag{1}
\]
Conversely every such word satisfies the span hypothesis. Its orbit has
exactly four projective syndrome directions, not sixteen.

Consequently, the construction method that puts all sixteen shifts of
one four-sparse error, with arbitrary nonzero scalar normalizations, on
one affine syndrome line can supply at most four distinct challenges.
It cannot supply the sixteen needed to exceed the 2^-128 budget at
q=97^20. This rules out this whole-orbit construction only. It does not
bound arbitrary affine lines, partial orbits, or the full error E_C.

## Proof

For any integer d, summing x^d over H gives zero unless 16 divides d,
in which case it gives 16. Indeed, if h^d is not one for some h in H,
multiplication by h fixes the sum and also multiplies it by h^d. The
group is cyclic, so such an h exists when 16 does not divide d.
It follows that sigma annihilates C: on a monomial of degree at most
seven the relevant exponents j+deg(p) range from one to fifteen.
The moment matrix has rank eight, since any eight columns form a
Vandermonde matrix times a nonsingular diagonal matrix. Thus ker(sigma)=C.

Put s_j=sigma_j(e). Direct substitution gives
\[
 \sigma_j(e^{(t)})=t^j s_j.                                  \tag{2}
\]
The characters t -> t^j for 1<=j<=8 are linearly independent as
functions on H. Multiply a proposed relation by t^(-ell) and sum
over H to isolate 16 times its ell-th coefficient. Hence the rank
of the matrix with columns sigma(e^(t)) is exactly the number of
nonzero s_j. Multiplying each column by any nonzero scalar preserves
this rank.

Write A=supp(e) and w=|A|<=4. Any w consecutive zero moments would
force e=0: for exponents ell,...,ell+w-1 their equations have matrix
(x^(ell+i))_(0<=i<w,x in A), an invertible Vandermonde matrix times
the diagonal entries x^ell. All points of H are nonzero. In particular
four consecutive zero moments are impossible. If at most one of the
eight s_j were nonzero, four consecutive zeros would occur either
before or after it. The span hypothesis therefore gives exactly two
nonzero moments, at indices u<v. Absence of four consecutive zeros
forces
\[
 u\le4,\qquad v\ge5,\qquad v-u\le4.                        \tag{3}
\]
These conditions leave ten pairs. Rescale e so that s_u=1 and write
s_v=c, where c is nonzero; all other moments are zero.

Here is the required calculation for those ten possibilities. Form
\[
 M=(s_{i+j+1})_{0\le i,j\le3},\qquad D=\det M,
\]
and the polynomial determinant
\[
 L(X)=\det\begin{pmatrix}
 s_1&s_2&s_3&s_4&s_5\\
 s_2&s_3&s_4&s_5&s_6\\
 s_3&s_4&s_5&s_6&s_7\\
 s_4&s_5&s_6&s_7&s_8\\
 1&X&X^2&X^3&X^4
 \end{pmatrix}.
\]
If w=4, the factorization M=V diag(e_x*x) V^T, with
V_(i,x)=x^i, proves D!=0. Moreover the first four rows of the
matrix defining L span the four rows (1,x,x^2,x^3,x^4), x in A.
Thus L vanishes on A and has leading coefficient D, so
\[
 L(X)/D=\prod_{x\in A}(X-x).                                \tag{4}
\]
Expanding the displayed determinants after setting s_u=1,s_v=c
gives the following identities over the integers, hence over F:

| (u,v) | D | L(X)/D when D is nonzero |
|---|---|---|
| (1,5) | -c^3 | X^4-c |
| (2,5) | 0 | undefined; L=-c^3 X^3+c^4 |
| (2,6) | c^2 | X^4-c |
| (3,5) | c^2 | X^4-c X^2+c^2 |
| (3,6) | 0 | undefined; L=0 |
| (3,7) | -c | X^4-c |
| (4,5) | 1 | X^4-c X^3+c^2 X^2-c^3 X+c^4 |
| (4,6) | 1 | X^4-c X^2+c^2 |
| (4,7) | 1 | X^4-c X |
| (4,8) | 1 | X^4-c |

For every row other than (3,6), there are three consecutive zero
moments. Therefore w=4 in those nine rows. The row (2,5) is impossible
because D=0. For (4,7), the monic polynomial in (4) has zero as a
root, impossible since A consists of four nonzero points.

For (3,5) and (4,6), put P=X^4-c X^2+c^2. The identity
\[
 (X^2+c)P=X^6+c^3
\]
implies that the ratio of any two roots in H has both sixth and
sixteenth power one. Its square is therefore one, so P has at most
two distinct roots in H, contradicting (4). For (4,5), the identity
\[
 (X+c)(X^4-cX^3+c^2X^2-c^3X+c^4)=X^5+c^5
\]
shows that the ratio of any two roots in H has both fifth and
sixteenth power one. The ratio is one, so there is at most one such
root. These arguments require no assumptions on characteristic three
or five and still exclude four distinct roots in those characteristics.

In the remaining exceptional row (3,6), D=0 excludes w=4. The first
two zero moments exclude w<=2, so w=3. Write its support polynomial
as X^3+a_2 X^2+a_1 X+a_0. Multiplying its root equations by e_x*x^ell
and summing for ell=1,2,3 gives, successively,
\[
 a_2=0,\qquad a_1=0,\qquad a_0=-c.
\]
Its three roots would all satisfy x^3=c. Ratios in H would have both
third and sixteenth power one and hence equal one, a contradiction.

Only v=u+4, 1<=u<=4, remains. In all four cases (4) is X^4-c.
Choose a in A; then c=a^4 and A=aK. Restoring the original scale
s_u, the word s_u/(4*x^u) on aK has exactly the required moments:
\[
 \frac{s_u}{4}\sum_{x\in aK}x^{j-u}
 =\begin{cases}s_u&j=u,\\s_u a^4&j=u+4,\\0&\text{otherwise},\end{cases}
 \qquad1\le j\le8.
\]
The values on A are uniquely determined by any four consecutive
moments, by the same Vandermonde argument. This proves (1) with
lambda=s_u/4, and the displayed formula also proves its converse.

By (2), the nonzero projective syndrome is determined by
\[
 [s_u t^u:s_{u+4}t^{u+4}]=[1:a^4 t^4].                     \tag{5}
\]
The fourth-power map on H has image of size four, so there are exactly
four directions. If arbitrary nonzero multiples of all sixteen orbit
vectors lie on an affine line, that line cannot pass through zero:
its linear span contains the two-dimensional span of the orbit. An
affine line not through zero meets each projective direction in at most
one point; otherwise the line through two distinct collinear vectors
would contain zero. It therefore contains at most four distinct points
from these normalized shifts. A nonconstant affine parametrization
gamma -> sigma(f)+gamma*sigma(g) is injective, so they supply at most
four distinct challenges. A constant syndrome line cannot contain this
orbit. Codeword changes to the input words do not alter their syndromes.

This is already an obstruction before imposing same-support failure:
adding that requirement cannot increase the number of challenges.
No implication from mere decodability to MCA failure is used. The result
also does not exclude extra bad challenges on the same affine line
arising from errors outside the proposed whole orbit.

For the intended application, exact integer comparison gives
15*2^128 <= 97^20 < 16*2^128. The orbit bound four is below the
required count sixteen and even below L008's existing lower count ten.
Thus this mechanism does not improve the known bounds 10/q and 69/q.
It is an informative obstruction, not a security certificate or a claim
that sixteen bad challenges are impossible for general input words.

The auxiliary command `python3 scripts/subgroup-orbit/check.py` checks
all ten determinant identities by signed permutation expansion over
the integers. It also checks every pair of moment indices and all 1820
four-coordinate supports over F_97: precisely the four cosets of K work
for each pair (u,u+4), and no other pair works. Smaller supports are
included by allowing zero coefficients. The uniform proof above, rather
than this enumeration, establishes the result over arbitrary extensions.

## Mathlib

Coverage of the full orbit classification and its MCA obstruction in
Mathlib: **not checked**. Coverage of supporting finite Fourier,
Vandermonde, and determinant results: **not checked**. No matching
theorem or Lean verification is claimed. The needed identities and
linear-algebra arguments are proved above.

The previously read ArkLib declarations
[`CoreDefinitions.IsMCA` and `CoreDefinitions.mcaError`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ProximityGap/ProximityGenerators.lean#L98)
support the frozen event definition only. ArkLib is separate from Mathlib;
these definitions do not match this classification or certify agreement
with the unread ABF26 definition.
