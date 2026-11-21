# L839 — A cubic with nonnegative solid rays and nonreal zeros

## Hypotheses

Let P(z)=1+z+z^2+z^3, let a_0=a_1=a_2=a_3=1, and set
a_n=0 for every other integer n. For positive integers r,k define
\[
D_{(r,k)}=\det[a_{k+j-i}]_{0\le i,j<r}.
\]
All statements concern these ordinary coefficients, with this zero
extension and with weak nonnegativity. No Xi realization, strict
positivity, infinite-degree assumption or assertion about all ordered
minors is a hypothesis.

## Conclusion

For every positive integer r,
\[
D_{(r,1)}=D_{(r,2)}=
\begin{cases}1,&r\equiv0,1\pmod4,\\0,&r\equiv2,3\pmod4,\end{cases}
\qquad D_{(r,3)}=1.
\]
For every r>=1 and k>3, D_{(r,k)}=0. Thus every positive-shift ray
is nonnegative at every positive rank, although P has nonreal zeros
i and -i (and the real zero -1).

Consequently, within a class allowing finite products, nonnegative
coefficients and tied-modulus nonreal zeros, even all-rank weak signs
on every such ray do not imply that the polynomial's zeros are real.
The weaker premise of separate eventual weak signs at every fixed
shift also fails to imply this conclusion. This does not refute RH,
give an actual-Xi counterexample, or decide a detector with additional
strictness, no-ties, infinite-degree or other structural hypotheses.

## Proof

### Imported finite determinant formula

Per Alexandersson, *Schur polynomials, banded Toeplitz matrices and
Widom's formula*, Electronic Journal of Combinatorics 19(4) (2012),
P22, [arXiv:1208.5607v1](https://arxiv.org/html/1208.5607v1),
Theorem 6, printed p.5, with its proof in Section 3.2, pp.11–12,
supplies the following finite distinct-variable formula. For elementary
coefficients of \(\prod_{j=1}^n(1+x_jz)\), normalized by a_0=1,
the determinant at shift k, 1<=k<n, is
\[
D_{(r,k)}=\sum_{|S|=k}\frac{B_S^{n-k}}{d_S}B_S^r,
\quad B_S=\prod_{j\in S}x_j,
\quad d_S=\prod_{j\in S,\ell\notin S}(x_j-x_\ell).
\tag{1}
\]
Here the source's deleted-column count c is our shift k, and its
matrix size is our rank r: deleting the first k columns leaves
entries a_{k+j-i}. Formula (1) is imported, not reproved. Equal
moduli are allowed; variables must be distinct. No general asymptotic
or oscillation assertion is used. The calculation below supplies the
specialization not already contained in the cited theorem.

### Coefficient match and the two interior shifts

Take n=3 and (x_1,x_2,x_3)=(1,i,-i). These are distinct and nonzero.
Their product polynomial is
\[
(1+z)(1+iz)(1-iz)=(1+z)(1+z^2)=P(z),
\]
so its elementary coefficients match exactly, including a_0=1.

For k=1 the singleton values (B_S,d_S,B_S^2/d_S) are
\[
\begin{array}{c|c|c|c}
S&B_S&d_S&B_S^2/d_S\\\hline
\{1\}&1&2&1/2\\
\{i\}&i&-2-2i&(1-i)/4\\
\{-i\}&-i&-2+2i&(1+i)/4
\end{array}
\]
where subsets are labeled by their variables. For example,
d_{\{i\}}=(i-1)(i+i)=-2-2i; thus no denominator vanishes.
For k=2 the pair values (B_S,d_S,B_S/d_S) are
\[
\begin{array}{c|c|c|c}
S&B_S&d_S&B_S/d_S\\\hline
\{1,i\}&i&-2+2i&(1-i)/4\\
\{1,-i\}&-i&-2-2i&(1+i)/4\\
\{i,-i\}&1&2&1/2
\end{array}
\]
For example, d_{\{1,i\}}=(1+i)(2i)=-2+2i.
Applying (1) to both tables gives exactly the same expression:
\[
D_{(r,1)}=D_{(r,2)}=
\frac12+\frac{1-i}{4}i^r+\frac{1+i}{4}(-i)^r.
\tag{2}
\]
The powers in (2) have period four. At r congruent to 0,1,2,3
modulo four, the last two terms sum respectively to 1/2,1/2,-1/2,-1/2.
This proves the claimed values for all positive r, retaining the
two zero residue classes; it is not a finite-rank numerical check.

### Boundary and exterior shifts; zeros

At k=3, every entry above the diagonal has index 3+j-i>3 and is
zero, while every diagonal entry is a_3=1. The matrix is lower
triangular with determinant 1 for every rank. At k>3, every entry
in the first row has index k+j>3 and is zero, so the determinant
vanishes for every positive rank. These arguments cover all remaining
shifts without extending (1) beyond its stated range.

The displayed factorization gives precisely the roots -1,i,-i,
all simple. In particular i is a genuine nonreal zero. The all-rank
sign premise is stronger than separate eventual nonnegativity on
each fixed-shift ray, so the same example refutes both universal
implications under the stated class. The ordinary coefficient
polynomial here must not be confused with Xi itself or with a
factorially normalized coefficient sequence. No limit interchange,
infinite product or RH-equivalent positivity premise occurs.

### Independent audit, 6 November 2026

The audit reread the cited v1 Theorem 6, the source matrix definition
and elementary-symmetric convention, and Section 3.2 through the full
proof of Theorem 6. Its selected-variable numerator contains each
selected variable n-k times, giving exactly B_S^(n-k), with no extra
sign, factorial or rank offset. The source theorem holds at every
positive matrix size and requires distinct variables, not distinct
moduli. Its more general recurrence theorem is unnecessary here.

Independently expanding all six denominators gives, in the order of
the two tables,
\[
(1-i)(1+i)=2,\quad (i-1)(2i)=-2-2i,\quad
(-i-1)(-2i)=-2+2i,
\]
\[
(1+i)(2i)=-2+2i,\quad (1-i)(-2i)=-2-2i,\quad
(i-1)(-i-1)=2.
\]
Division by these values confirms every table entry, including both
conjugate pairs. Substitution of i^r=1,i,-1,-i into (2) gives
1,1,0,0 respectively. These four cases exhaust all ranks because
both powers have period four. The zero first row for k>3 includes
rank one; lower triangularity at k=3 also holds at every rank.
Finally the coefficient variables are not the polynomial's zeros:
the zeros are -1/x_j, which here give precisely -1,i,-i. This checks
the nonreal-zero assertion without identifying a variable with its
root incorrectly. The audit found no correction to the proof or its
restricted conclusion. It validates the local specialization, not
originality beyond the cited method or an actual-Xi sign input.

## Mathlib

Full matching coverage of this counterexample and the finite subset
formula is unchecked. No claim of absence is made. The proof imports
the precise finite formula above and uses explicit complex arithmetic
and triangular/zero-row determinant identities for the specialization.
This is a reproduction/specialization of a known method; the source
search does not establish originality of the example.
