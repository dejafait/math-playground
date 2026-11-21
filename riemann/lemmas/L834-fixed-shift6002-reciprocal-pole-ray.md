# Lemma 834: eventual positivity at fixed coefficient shift 6002

## Hypotheses

Use the actual completion of L018 and ordinary coefficients of L021/L776:

\[
G(w)=\frac18\xi\left(\frac12+\frac{\sqrt w}{2}\right)
    =\sum_{n\ge0}a_nw^n,\qquad
a_n=\frac{M_{2n}}{8\,4^n(2n)!},\qquad a_0>0.
\]

The square-root notation denotes the entire series. Put a_n=0 for n<0,
fix k=6002, and for integer r>=1 set

\[
D_{(r,k)}=\det[a_{k+j-i}]_{i,j=0}^{r-1},\qquad
F(z)=\frac{G(-z)}{a_0},\qquad
H_{\rm rec}(z)=\frac1{F(z)}=\sum_{n\ge0}h_nz^n
\]

near zero, with h_n=0 for n<0. Import the rigorous finite-height
verification as in L832, using the sign-change/count evidence of
Platt–Trudgian Section 2 explicitly below in addition to its Theorem 1.
No RH, residual PF_infinity, numerical zero enclosure, effective onset,
or uniformity in k is assumed.

## Conclusion

There is an integer r_0 such that D_(r,6002)>0 for every integer r>=r_0.
More precisely, the first k positive poles p_1<...<p_k of H_rec are
simple. With p_(k+1) the next pole, put

\[
R=\frac{p_k+p_{k+1}}2,\quad q=\frac{p_k}{R}<1,\quad
A_l=-\frac1{p_lF'(p_l)},\quad
\Delta=\prod_{1\le a<b\le k}(p_b-p_a),\quad
C_*=\frac{\Delta^2\prod_{l=1}^k|A_l|}
                {\prod_{l=1}^k p_l^{k-1}}>0.
\]

For r>=k-1 define real k-by-k matrices

\[
(Q_r)_{ij}=\sum_{l=1}^k A_l p_l^{-(r+j-i)},\quad
(E_r)_{ij}=h_{r+j-i}-(Q_r)_{ij},\qquad 0\le i,j<k.
\]

Then Q_r is invertible, and a finite constant C>=0 independent of r
satisfies

\[
\det Q_r=C_*\left(\prod_{l=1}^k p_l\right)^{-r}>0,
\qquad \|Q_r^{-1}E_r\|_\infty\le Cq^r\longrightarrow0.       \tag{1}
\]

Here the infinity norm is maximum absolute row sum. In particular,

\[
D_{(r,k)}=a_0^r C_*\left(\prod_{l=1}^k p_l\right)^{-r}
                   \bigl(1+O(q^r)\bigr),\qquad r\longrightarrow\infty.
                                                                    \tag{2}
\]

All constants are for this one fixed k. They are specified analytically
below but not numerically bounded. There is no certified overlap with
L832's finite-order region, no positivity at every rank, and no conclusion
about growing shifts, other minors or RH. This is a local reproduction/
specialization of known finite-duality and meromorphic-coefficient methods,
not new asymptotic theory. The separate conceptual audit of 2026-11-05,
step670, validates this fixed-shift conclusion with these qualifications.

## Proof

**1. Actual simple pole packet and an exact separating radius.**
Dave Platt and Tim Trudgian, *The Riemann hypothesis is true up to
3 times 10^12*, Bull. London Math. Soc. **53** (2021), 792–797,
[arXiv:2004.09765v1](https://arxiv.org/pdf/2004.09765v1), Theorem 1,
printed p.2, gives H=3,000,175,332,800 and the count
N=12,363,153,437,138 of positive-height nontrivial zeros up to H.
Section 2, pp.2–3, describes the rigorous sign-change computation and
Turing verification that the expected total has been accounted for.
It explicitly distinguishes counting isolated sign changes from storing
high-precision zero locations. We import this published verification,
not an unprinted list of numerical enclosures or a rerun of its code.

Here is the multiplicity implication needed for this application. The
counted sign changes supply disjoint open intervals with nonzero endpoints,
each containing at least one critical-line zero and hence at least one
unit of zero multiplicity. Turing's total count, which counts all zeros
with multiplicity, equals that sign-change count. Every interval must
therefore contribute exactly one unit, and no additional zero or extra
multiplicity can occur in the counted region. Thus these zeros are simple
and distinct. This uses the Section 2 evidence; the assertion that zeros
lie on the line, by itself, would not imply simplicity. The zeros of the
completed function being tested and of zeta have the same multiplicities
there by L018 (the other completion factors do not vanish).

Consequently the first k+1 positive ordinates can be ordered
0<gamma_1<...<gamma_(k+1)<H. The strict final inequality follows also
from N>k+1 and the existence of further distinct zeros below or at H.
The zeros of F are the images

\[
p=-4(\rho-1/2)^2,\qquad \rho=\beta+i\gamma.
\]

L018 puts every such rho in 0<beta<1; L021 excludes gamma=0,
since xi(beta)=Xi(i(1/2-beta))>0. For 0<|gamma|<=H the verification
and conjugation give p=4 gamma^2>0. Locally the change of variable
has nonzero derivative when gamma!=0, so it preserves multiplicity.
The pair of reflected ordinates +gamma and -gamma gives one zero of F,
not a doubled multiplicity: either local inverse branch represents the
same entire function. In particular p_j=4 gamma_j^2 are simple zeros
of F and simple poles of H_rec.

Explicitly, the identity F(4t^2)=Xi(t)/Xi(0) holds for complex t.
At t=gamma_j its derivative gives

\[
F'(p_j)=\frac{\Xi'(\gamma_j)}{8\gamma_j\Xi(0)}\ne0.
\]

Here Xi(0)=8a_0>0 and gamma_j>0. This also checks the factor4 in
the squared-image normalization and excludes a ramification at the
chosen zeros; no branch needs to be defined globally.

For every possible zero above the verified range, including off-line ones,

\[
|p|=4\bigl((\beta-1/2)^2+\gamma^2\bigr)>4H^2.
\]

Thus the open disk |z|<p_(k+1) contains exactly p_1,...,p_k as zeros
of F, and its boundary has no competing zero of smaller modulus hidden
by the square map. In particular the specified R lies strictly between
p_k and p_(k+1), and F has no zero on |z|=R. No decimal estimate of
gamma_k or its gap was used. The genus-zero product and finite-PF
conclusion in L832 are not required here; the imported height/count and
the exact zero correspondence are the relevant inputs.

**2. Reciprocal duality, including normalization and singular minors.**
Set e_n=a_n/a_0 for n>=0 and e_n=0 for n<0. Then
E(z)=sum e_n z^n=G(z)/a_0 and E(z)H_rec(-z)=1 near zero.
For m=r+k form the finite lower triangular matrix

\[
T=[e_{i-j}]_{i,j=0}^{m-1}.
\]

Its diagonal is 1, so det T=1 and it is invertible. The generating-series
identity, coefficient by coefficient in the finite triangular product,
identifies its inverse as

\[
(T^{-1})_{ij}=(-1)^{i-j}h_{i-j}.
\]

Import Jacobi's complementary-minor identity in A. Böttcher and H. Widom,
*Szegő via Jacobi*,
[arXiv:math/0604009v1](https://arxiv.org/pdf/math/0604009v1),
Theorem 2.1, printed p.3, with the shifted-block convention illustrated
by Corollary 2.3 and its proof, p.4. It requires only invertibility of
the full matrix, not of either selected minor. Equivalently this is the
rectangular dual Jacobi–Trudi identity: I. G. Macdonald, *Symmetric
Functions and Hall Polynomials*, second edition (1995), I.2 (2.6)–(2.9'),
pp.21–23, and I.3 (3.4)–(3.7'), pp.41–42. We apply the finite identity;
we do not reprove it or import a nonzero-winding asymptotic theorem.

For explicit parity bookkeeping choose increasing sets
I={k,...,k+r-1} and J={0,...,r-1}. Jacobi gives

\[
\det T[I,J]=(-1)^{\sum I+\sum J}
                    \det T\,\det T^{-1}[J^c,I^c].
\]

The use of zero-based indices changes the source's parity exponent by
an even integer. Here sum I+sum J=rk+r(r-1), of parity rk.
The complement has row indices r,...,r+k-1 and column indices
0,...,k-1, hence its entries are (-1)^(r+i-j)h_(r+i-j).
Factoring these signs out of rows and columns contributes (-1)^(rk).
The two parity factors cancel. Transposition of the two displayed
Toeplitz blocks does not change their determinants. It follows exactly
that, for every r>=1,

\[
D_{(r,k)}=a_0^r\det[h_{r+j-i}]_{i,j=0}^{k-1}.                \tag{3}
\]

Negative indices are zero throughout the triangular matrices and (3).
No selected determinant was divided by, so (3) includes singular cases.
There is no radius scaling in (3); the factor a_0^r is indispensable.
For the remaining asymptotics restrict to r>=k-1, so every index
r+j-i in the right side is nonnegative.

**3. Principal parts and a finite remainder constant.**
Since F is entire with F(0)=1, H_rec is meromorphic on the plane and
analytic at zero. Step 1 verifies all enclosed poles, their multiplicities,
and analyticity on the contour |z|=R. At p_l its residue is 1/F'(p_l),
so its complete simple-pole part can be written as A_l/(1-z/p_l),
where A_l=-1/(p_l F'(p_l)) is real and nonzero. Define

\[
B(z)=H_{\rm rec}(z)-\sum_{l=1}^k\frac{A_l}{1-z/p_l},\qquad
M=\max_{|z|=R}|B(z)|<\infty.
\]

The apparent singularities at p_1,...,p_k are removable in B; it is
holomorphic on |z|<p_(k+1), a neighborhood of the closed radius-R disk.
Apply Philippe Flajolet and Robert Sedgewick, *Analytic Combinatorics —
Basic Complex Asymptotics*, ALCOMFT-TR-03-100, first edition,
27 November 2003,
[author PDF](https://algo.inria.fr/flajolet/Publications/FlSe03.pdf),
Theorem IV.7, (22), and its two proofs, printed pp.29–30 (PDF pp.37–38).
Its meromorphic coefficient expansion retains every pole's principal
part, with a polynomial factor in n for a multiple pole. All poles here
have already been shown simple, so those factors are constants. The
source's analytic-remainder/Cauchy bound gives, with the explicit M above,

\[
h_n=\sum_{l=1}^k A_l p_l^{-n}+b_n,\qquad
|b_n|\le M R^{-n},\qquad n\ge0.                             \tag{4}
\]

This is an application of the cited theorem, with its constant retained;
no general meromorphic asymptotic result is being reproved. The coefficient
identity is first read near zero and the remainder bound on the larger
circle concerns B, which is holomorphic there. It does not assume that
the original Taylor series of H_rec converges past its first pole.

**4. Signs and the leading determinant.**
F is real on the real axis, F(0)=1, and its only positive zeros through
p_k are the ordered simple p_l. It has constant sign between successive
zeros and changes sign at each. Immediately to the right of p_l its
sign, and hence the sign of F'(p_l), is (-1)^l. Therefore

\[
\operatorname{sgn}(A_l)=(-1)^{l-1}.                         \tag{5}
\]

For zero-based row/column indices and 1<=l<=k put

\[
U_{il}=p_l^i,\qquad V_{lj}=p_l^{-j},\qquad
W_r=\operatorname{diag}(A_l p_l^{-r}).
\]

Direct multiplication of these finite matrices gives Q_r=U W_r V.
The distinct positive p_l make both Vandermonde matrices invertible;
W_r is invertible because A_l!=0. The standard Vandermonde determinant
formula gives, with K=k(k-1)/2,

\[
\det U=\Delta>0,\qquad
\det V=\prod_{a<b}(p_b^{-1}-p_a^{-1})
       =\frac{(-1)^K\Delta}{\prod_l p_l^{k-1}}.
\]

Equation (5) gives sign(prod A_l)=(-1)^K. Multiplying the three
determinants cancels these two signs and proves the determinant formula
in (1), with its positive constant C_*. Reality of residues and nodes
alone would not have sufficed; both orientations and (5) were used.

**5. Relative matrix error and transfer of the strict sign.**
All matrices U,V and all A_l are fixed when r varies. By the inverse
factorization and submultiplicativity of maximum row-sum norm, for r>=0,

\[
\|Q_r^{-1}\|_\infty
 \le \|V^{-1}\|_\infty\|U^{-1}\|_\infty
                \max_l(|A_l|^{-1}p_l^r)
 \le \|V^{-1}\|_\infty\|U^{-1}\|_\infty
                \max_l|A_l|^{-1}\,p_k^r.
\]

For r>=k-1, (4) bounds every entry of E_r. Retain all fixed index shifts
by defining the finite positive number

\[
S_R=\max_{0\le i<k}\sum_{j=0}^{k-1}R^{i-j}.
\]

Then ||E_r||_infinity<=M S_R R^(-r). Consequently (1) holds with

\[
C=M S_R\|V^{-1}\|_\infty\|U^{-1}\|_\infty
                    \max_l|A_l|^{-1}<\infty.                \tag{6}
\]

No numerical conditioning bound is needed for this fixed-k existence
claim; finiteness has been paid by distinct nodes and nonzero residues.
The constants may be very large, and no claim uniform in k follows.

Since 0<q<1, choose an integer r_0>=k-1 with Cq^(r_0)<1.
If C=0, r_0=k-1 suffices. For every r>=r_0 and 0<=t<=1,
I+t Q_r^(-1)E_r is invertible: its inverse is given by the convergent
Neumann series because ||t Q_r^(-1)E_r||_infinity<1. Its determinant
is real and continuous in t and equals 1 at t=0. It is never zero
on this segment, hence is positive at t=1. Thus

\[
\det(Q_r+E_r)=\det Q_r\det(I+Q_r^{-1}E_r)>0.
\]

Equation (3) and a_0>0 prove the claimed eventual strict sign.
For completeness, if delta=||Q_r^(-1)E_r||_infinity, every eigenvalue
of Q_r^(-1)E_r has modulus at most delta. The product formula for
the determinant, counting algebraic multiplicity, yields
|det(I+Q_r^(-1)E_r)-1|<=(1+delta)^k-1=O(delta) as delta->0,
since k is fixed. Combining this with (1) proves (2).

This supplies the analytic estimate absent from the earlier reciprocal
algebra stop, without contradicting that stop: duality alone still gives
no sign. L833's floor, L825's common-symbol obstruction, the step659
hybrid ratio and residual PF_infinity are not mathematical premises.
The unknown finite-rank region at this shift, effective constants,
simultaneous growing-parameter control, actual all-degree mixed positivity,
and RH remain unresolved. No numerical computation or general zero
simplicity conjecture has been used.

**Conceptual audit (2026-11-05, step670).** The full proof above passes
at its stated scope. The primary sign-change/count passages and the
complete finite-minor and meromorphic-coefficient theorem cases cited
above were checked. The finite-height computation is an imported rigorous
verification, not a computation replayed in this notebook. In particular,
the simplicity inference uses equality of a lower count by disjoint
sign-change intervals with the total multiplicity count, not the
line-location statement alone. The local derivative identity above makes
the squared-map multiplicity check explicit.

For (3), the full triangular matrix is invertible even if its selected
minor vanishes; both parity contributions are rk modulo2 and the original
minor has exactly r factors a_0. For (1), the pole residues have alternating
sign, the second Vandermonde has sign (-1)^(k(k-1)/2), and these signs
cancel. Every coefficient used in (4) is nonnegative-indexed once r>=k-1.
The remainder B is holomorphic on a neighborhood of the radius-R closed
disk, so its Cauchy constant M is finite without continuing the Taylor
series of H_rec across a pole. Equation (6) contains all the fixed shifts
and inverse norms: no r-dependent factor is suppressed. The real Neumann
segment proves positivity; small additive entry errors alone would not.

No mathematical correction or additional sign theorem is claimed by this
audit. It validates the previously unaudited standard specialization,
including (2), only for fixed k=6002 and sufficiently large r. It does not
bound M, individual pole gaps, inverse Vandermonde norms or the onset, nor
establish PF overlap or any joint growing-parameter estimate. The DAG row
is unchanged: L776 supplies conventions only, L832 the qualified external
verification, and L018/L021 the actual entire function and positivity at
zero. No Fredholm hypothesis or residual PF property was imported.

## Mathlib

Full matching coverage is unchecked; no presence or absence is claimed.
The precise cited finite-minor identity, published verification and
meromorphic coefficient theorem are the imported inputs. Vandermonde
determinants, Cauchy estimates, finite matrix norm inequalities and the
Neumann-series sign transfer are supporting standard mathematics, not
a claim that this full actual-Xi specialization has been formalized.
