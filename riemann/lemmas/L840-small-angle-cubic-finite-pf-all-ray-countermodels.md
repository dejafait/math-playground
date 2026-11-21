# L840 — Prescribed finite PF order with nonnegative solid rays and nonreal zeros

## Hypotheses

Fix an integer m>=1, put N=m+2 and theta=pi/N, and let
\[
 P_m(z)=(1+z)(1+2\cos\theta\,z+z^2)=\sum_{j=0}^3 a_jz^j.
\]
Extend a_j by zero to all integers outside 0<=j<=3. For positive
integers r,k set
\[
 D_{(r,k)}=\det[a_{k+j-i}]_{0\le i,j<r}.
\]
PF_h means that every ordered minor of size at most h in
(a_(j-i))_(i,j>=0) is nonnegative. These are ordinary coefficients;
weak signs and tied moduli are allowed. There is no Xi realization,
infinite-degree hypothesis or strict-positivity assumption.

## Conclusion

For every prescribed m, the coefficient sequence is PF_(2m+2),
and in particular PF_m. All four coefficients are strictly positive,
and P_m has a nonreal conjugate pair of zeros. For every r>=1,
\[
 D_{(r,1)}=D_{(r,2)}=
 \frac{\sin((r+1)\theta/2)\sin((r+2)\theta/2)}
 {\sin(\theta/2)\sin\theta}\ge0.                    \tag{1}
\]
More precisely these determinants have period 2N in r, vanish
exactly when r is congruent to 2N-2 or 2N-1 modulo 2N, and are
strictly positive at the other residue classes. Also
\[
 D_{(r,3)}=1,\qquad D_{(r,k)}=0\quad(k>3).             \tag{2}
\]

Consequently, for each fixed finite h, a finite real polynomial can
have a PF_h coefficient sequence and nonnegative determinants on
every positive-shift solid ray at every rank, yet have nonreal zeros
(take m=h). Adding any prescribed finite PF order does not repair
the abstract weak-sign detector in this class. The polynomial may
depend on h. This does not assert one polynomial is PF_h for every h,
nor settle a detector with strict signs, infinite degree, no tied
moduli or actual-Xi structure. It is not a proof or disproof of RH.

## Proof

### Imported results and the finite-PF match

Mohammad Adm, Jürgen Garloff and Mikhail Tyaglov, *Total nonnegativity
of finite Hurwitz matrices and root location of polynomials*,
J. Math. Anal. Appl. **467** (2018), 148–170,
[published author PDF](https://www-home.htwg-konstanz.de/~garloff/JMAA-3_Adm_Garloff_Tyaglov.pdf),
Theorem 5.7 and (5.9), printed p.161, record Schoenberg's known
PF_K family
\[
 g(z)=\prod_{j=1}^{d}\bigl(z+e^{i\phi(d-2j+1)}\bigr),
 \qquad \phi=\frac{\pi}{d+K-1}.                       \tag{3}
\]
The coefficient sequence in (3) is PF_K, with weak inequalities;
the equality-angle case is included. We import this stated family,
not any converse for products. The original cited source is
I. J. Schoenberg, *On the zeros of the generating functions of multiply
positive sequences and functions*, Ann. of Math. (2) **62** (1955),
447–471; its original proof has not been independently read.
The all-ordered-minor convention is also explicit in Olga M. Katkova,
*Multiple positivity and the Riemann zeta-function*,
[math/0505174v1](https://arxiv.org/pdf/math/0505174v1),
Definition 2/(8), printed p.4. No separate PF44 inference is used.

Take d=3 and K=2m+2 in (3). Then d+K-1=2m+4=2N,
phi=theta/2, and the three phases are theta,0,-theta. Writing
q=e^(i theta), their polynomial is exactly
\[
 (z+q)(z+1)(z+q^{-1})
 =(1+z)(z^2+2\cos\theta\,z+1)=P_m(z).                \tag{4}
\]
There is no normalization factor: both constant and leading
coefficients equal 1. The ascending and descending coefficient lists
are identical, so a monic descending-coefficient convention gives
the same sequence here. Thus (3) gives PF_(2m+2) for the stipulated
zero extension. Restricting the allowed minor sizes gives PF_m.
This is a known-result specialization, not a new finite-PF theorem.

For the interior solid determinants we import Per Alexandersson,
*Schur polynomials, banded Toeplitz matrices and Widom's formula*,
Electron. J. Combin. **19**(4) (2012), P22,
[arXiv:1208.5607v1](https://arxiv.org/html/1208.5607v1),
Theorem 6, printed p.5, with proof in Section 3.2, pp.11–12.
For distinct complex variables x_1,...,x_n, elementary coefficients
of product_j(1+x_jz), and 1<=k<n, the theorem gives at every
positive rank r
\[
 D_{(r,k)}=\sum_{|S|=k}\frac{B_S^{n-k}}{d_S}B_S^r,
 \quad B_S=\prod_{j\in S}x_j,
 \quad d_S=\prod_{j\in S,\ell\notin S}(x_j-x_\ell).
                                                               \tag{5}
\]
The source's deleted-column count c is our shift k, and its matrix
size is our rank r; the retained matrix has entries a_(k+j-i).
Equal moduli are allowed. No asymptotic, oscillation theorem or
coalescing-variable limit is imported. The ready literature assessment
has inspected these source statements and the relevant finite-formula
proof cases; below we supply only the coefficient and sign
specialization missing from their conclusions.

### Exact shift-one formula

Since m>=1, 0<theta<=pi/3. Thus 1,q,q^(-1) are distinct and
nonzero, and
\[
 \prod_{x\in\{1,q,q^{-1}\}}(1+xz)=P_m(z),\qquad
 (a_0,a_1,a_2,a_3)=(1,b,b,1),\quad b=1+2\cos\theta>0.
                                                               \tag{6}
\]
The variables in (5) therefore match exactly. Let s=sin(theta/2)>0;
also sin(theta)>0. For n=3,k=1, the singleton coefficients
B_S^2/d_S are
\[
 \begin{aligned}
 A_1&=\frac{1}{(1-q)(1-q^{-1})}=\frac{1}{4s^2},\\
 A_q&=\frac{q^2}{(q-1)(q-q^{-1})}
      =-\frac{e^{3i\theta/2}}{4s\sin\theta},\\
 A_{q^{-1}}&=\overline{A_q}
      =-\frac{e^{-3i\theta/2}}{4s\sin\theta}.
 \end{aligned}                                                 \tag{7}
\]
Indeed (1-q)(1-q^(-1))=2-2cos(theta)=4s^2,
q-1=2i e^(i theta/2)s and q-q^(-1)=2i sin(theta).
These identities check every nonzero denominator and the phase in
(7); conjugation gives the third singleton without a sign change.
Substituting (7) into (5) gives
\[
 \begin{aligned}
 D_{(r,1)}
 &=\frac{1}{4s^2}
   -\frac{\cos((r+3/2)\theta)}{2s\sin\theta}\\
 &=\frac{\cos(\theta/2)-\cos((r+3/2)\theta)}{2s\sin\theta}\\
 &=\frac{\sin((r+1)\theta/2)\sin((r+2)\theta/2)}
          {s\sin\theta}.
 \end{aligned}                                                 \tag{8}
\]
The second equality uses sin(theta)=2s cos(theta/2).
The third is cos(A)-cos(B)=2sin((B+A)/2)sin((B-A)/2).
Thus (8) is exact for all positive ranks, with no numerical or
large-rank approximation.

### Shift two and every rank residue

The zero-extended sequence satisfies a_j=a_(3-j) for every integer j,
including j outside 0,...,3. Hence at every rank
\[
 a_{2+j-i}=a_{1+i-j},
\]
so the shift-two matrix is the transpose of the shift-one matrix.
Their determinants are equal. This proves (1)'s equality without
another source specialization.

In (8), theta/2=pi/(2N). Replacing r by r+2N changes the sign
of each sine in the numerator, leaving their product unchanged.
For any integer r>=1 write r=2N ell+t, with 0<=t<=2N-1.
The two sine factors have the common sign multiplier (-1)^ell.
If 0<=t<=2N-3, the integers t+1 and t+2 lie between 1 and
2N-1; both sine values are strictly positive. If t=2N-2, the
second sine is sin(pi)=0. If t=2N-1, the first sine is sin(pi)=0.
These cases exhaust all ranks and give exactly the two asserted
zero classes. The denominator is strictly positive. Weak zeros are
retained; strict positivity on all ranks is not concluded.

### Boundary/exterior shifts and nonreal zeros

At k=3, each above-diagonal entry has index 3+j-i>3, hence is
zero, while every diagonal entry is a_3=1. The matrix is lower
triangular, proving D_(r,3)=1 for every r. At k>3 the entire
first row consists of a_(k+j)=0, proving D_(r,k)=0 for every
positive rank. These direct checks exhaust the remaining positive
shifts, without applying (5) outside its range.

From (4) the three polynomial roots are -1,-q,-q^(-1), all simple.
Because 0<theta<=pi/3, sin(theta)>0, so -q and -q^(-1) are
nonreal. Equivalently the elementary variables in (6) give roots
-1/x, which is the same unordered root set. The variables themselves
are not identified with polynomial zeros.

Equations (1)–(2), the imported PF conclusion and these actual
nonreal polynomial roots establish the claimed conjunction for
every finite m. They strengthen the finite-class obstruction of
L839 by adjoining any prescribed finite PF order. L839 is context,
not a premise; the only mathematical inputs are the cited results.
No compact limit as m tends to infinity is taken: theta=0, where
the variables merge and the roots become real, is excluded.
All-degree positivity of arbitrary ordered minors, signed growing
shifts for Xi, and realization by Xi remain unresolved. There is
no contour interchange, infinite product, numerical sign inference
or target-equivalent positivity assumption in this finite calculation.

### Independent audit, 6 November 2026

The audit re-opened Adm–Garloff–Tyaglov, Definition 5.3 and
Theorem 5.4, printed p.159, and Theorem 5.7 with the following
example (5.9), printed p.161. The PF assertion being imported is
the explicit example (5.9), not the converse of Theorem 5.7's
zero-free-sector implication. Its denominator is d+K-1, its phase
is phi(d-2j+1), and it asserts membership in PF_K, not strict
positivity. At d=3, K=2m+2 these give precisely (4). Definition
5.3 quantifies over all ordered minors through K. Palindromicity
removes the source's descending-coefficient convention issue.
Katkova Definition 2/(8), printed p.4, independently confirms the
same upper-Toeplitz zero-extension convention. The original 1955
proof remains unread; the published explicit family is the cited input.

Alexandersson's Section 1.1 defines D_c^r by deleting the first c
columns and no rows; its entries therefore are a_(c+j-i), not
a_(c+i-j) with a shifted row origin. Theorem 6 requires distinct
variables and s_0=1 and holds for every positive rank. Both conditions
hold here, including m=1. Its product of x_i/(x_i-x_j) gives exactly
B_S^(3-k)/d_S in (5); no ordering of their moduli is required.
Section 3.2, Lemma 15 and Proposition 16 with the complete proof
of Theorem 6, was rechecked: the rectangular partition has r
repeated k times, so the finite formula has no delayed-rank onset.
The unrelated recurrence's onset in Remark 14 is not an extra
hypothesis of Theorem 6.

There is also a direct normalization check independent of that
formula. Write H_r=D_(r,1) and H_0=1. The shift-one matrix has
diagonal b, first two upper diagonals b,1, first lower diagonal 1,
and all further diagonals zero. Expansion along its first row gives
for r>=3
\[
 H_r=bH_{r-1}-bH_{r-2}+H_{r-3},\qquad
 H_1=b,\quad H_2=b^2-b.                              \tag{9}
\]
Indeed, after removal of column j=1,2,3 (in one-based indexing),
the first j-1 retained columns force the successive lower-diagonal
entries 1; the remaining block is the shift-one matrix of size r-j.
Their cofactor signs are +,-,+, respectively. All later entries
of the first row are zero. This proves (9), without dividing by
any minor, including at the zero rank classes.

The right side of (8), viewed as a sequence in r>=0, is a constant
plus a linear combination of q^r and q^(-r). Each satisfies (9)
because
\[
 (t-1)(t-q)(t-q^{-1})=t^3-bt^2+bt-1.
\]
With x=theta/2, its values at r=0,1,2 are respectively
\[
 1,\quad \frac{\sin 3x}{\sin x}=b,\quad
 \frac{\sin 3x}{\sin x}\frac{\sin 4x}{\sin 2x}
 =b(b-1).
\]
Thus recurrence uniqueness independently verifies (8) at every
rank. This short second check is included to audit the imported
formula's phase and normalization; it does not reprove the PF import.

Finally, the denominator in (8) stays positive for every finite
m>=1, so the two rank zero classes are zeros of the numerator,
never indeterminate quotients. The residue argument covers the
wraparound t=2N-1 as a zero rather than a negative value. Transposition
uses the palindromic identity on all integer indices; at shifts 3
and above the triangular and zero-row checks apply even at rank 1.
The roots are -1,-q,-q^(-1), not the elementary variables themselves.
No error or missing case was found. The audit validates this known-method
finite-class obstruction only. It supplies no new actual-Xi sign
estimate, uniform-in-m infinite limit or claim of originality.

## Mathlib

Full matching Mathlib coverage of this family, its PF order and the
finite subset formula is unchecked. No absence claim is made.
The imports are precisely (3) and (5); the specialization uses finite
complex arithmetic, trigonometric identities, determinant transposition,
triangularity and a zero row. This is a reproduction/specialization
of known finite methods; the checked source search does not establish
originality of the combined obstruction. The independent audit above
found no error within the stated finite scope.
