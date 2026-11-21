# Lemma 832: verified-height import of coefficient PF6001

## Hypotheses

Use the actual completion xi and Xi of L018 and the moments of L021.
Use only the ordinary-coefficient conventions of L776:

\[
G(w)=\frac18\xi\left(\frac12+\frac{\sqrt w}{2}\right)
 =\sum_{j\ge0}a_jw^j,\qquad
a_j=\frac{M_{2j}}{8\,4^j(2j)!},\qquad a_j=0\quad(j<0).
\]

The square-root expression denotes its entire series. No RH, simplicity,
strict minor sign, radius, Fredholm bound or hybrid-matrix hypothesis is
assumed. The external inputs below include the published rigorous
finite-height verification, which is imported rather than rerun.

## Conclusion

The actual sequence (a_j) is PF_6001: for every integer 1<=d<=6001
and arbitrary increasing nonnegative integers
p_1<...<p_d and q_1<...<q_d,

\[
\det[a_{q_j-p_i}]_{i,j=1}^d\ge0.
\]

In particular D_(r,k)=det[a_(k+j-i)]_(i,j=0)^(r-1)>=0 for
1<=r<=6001 and every integer k>=0. This is a known-result import,
not a new sign theorem. Strict positivity, a numerical lower bound,
hybrid stability and all-order positivity are not conclusions.

## Proof

**Cited inputs and their scope.** Wojciech Michałowski,
*An explicit uniform cubic wedge for consecutive Toeplitz minors of the
Riemann xi-coefficients*,
[arXiv:2607.16795v1](https://arxiv.org/html/2607.16795v1#S1.SS2),
18 July 2026, Section 1.1, (1)–(3), defines exactly this G and its
ordinary coefficients. Section 1.2 supplies the finite-height sector
argument and its sufficient index condition m+1<=pi H. We use this
known sector conclusion, not the paper's separate cubic-tail theorem
or its certificates.

Dave Platt and Tim Trudgian, *The Riemann hypothesis is true up to
3 times 10^12*, Bull. London Math. Soc. **53** (2021), 792–797,
[arXiv:2004.09765v1](https://arxiv.org/pdf/2004.09765v1),
Theorem 1, printed p.2, proves that every nontrivial zero beta+i gamma
with 0<gamma<=H=3,000,175,332,800 has beta=1/2. Section 2,
pp.2–3, describes the interval-arithmetic verification and Turing count
excluding omitted zeros. This is a rigorous theorem input, not an
inference from a sample of zeros.

For the all-minor implication use I. J. Schoenberg's sufficient
polynomial sector theorem, *A note on multiply positive sequences and
the Descartes rule of signs*, Rend. Circ. Mat. Palermo (2) **4** (1955),
123–131, [DOI:10.1007/BF02846031](https://doi.org/10.1007/BF02846031),
as reproduced in Olga M. Katkova, *Multiple positivity and the Riemann
zeta-function*, Comput. Methods Funct. Theory **7** (2007), 13–31,
[DOI:10.1007/BF03321628](https://doi.org/10.1007/BF03321628).
Inspected numbering is Katkova's
[arXiv:math/0505174v1](https://arxiv.org/pdf/math/0505174v1),
Definition 2/(8), printed p.4, and Theorem B, printed p.5:
a real polynomial P with P(0)>0 and no zero in
|arg z|<pi m/(m+1) has its coefficient sequence in PF_m.
Definition 2 means every ordered Toeplitz minor of size at most m,
with coefficients extended by zero. The original Schoenberg proof
has not been read; no original theorem number is asserted.

Katkova (6), printed p.3, and the proof of Theorem 1, pp.5–6,
supply the order-one-half, positive-constant genus-zero product and
compact finite-product passage for xi_1(z)=xi(1/2+sqrt z).
We use that product input and the stated Theorem B, with the sector
from the modern verified-height argument. We do not import Katkova's
printed PF44 inference from a 43*pi/44 zero-free sector; its index
mismatch is irrelevant to the independently checked m=6001 below.

**Normalization and admissible sector.** The globally absolutely
convergent expansion in L021, with Xi(z)=xi(1/2+iz) from L018, gives

\[
\xi_1(z)=\sum_{j\ge0}b_jz^j,\quad
b_j=\frac{M_{2j}}{(2j)!},\qquad
G(w)=\frac18\xi_1(w/4),\quad a_j=8^{-1}4^{-j}b_j.
\]

These are ordinary Taylor coefficients: no factorial is removed.
The same identities hold after extension by zero to negative indices.
In particular G(0)=M_0/8>0. Positive rescaling of the variable does
not change arguments of nonzero zeros.

Here is the precise applicability of the cited height/sector statement.
L018 places each xi zero rho=beta+i gamma in 0<beta<1, and a zero
of G is w=4(rho-1/2)^2. The case gamma=0 is excluded by L021:
xi(beta)=Xi(i(1/2-beta))>0 for real beta. Conjugation in L018 extends
the closed verified positive-height range to negative heights. Thus
0<|gamma|<=H gives w=-4 gamma^2<0, including |gamma|=H.
For |gamma|>H the cited Section 1.2 gives

\[
\pi-|\arg w|
 =2\arctan\frac{|\beta-1/2|}{|\gamma|}<\frac1H.
\]

With m=6001, m+1=6002< H<pi H. Consequently all these zeros
avoid the open sector |arg w|<6001*pi/6002. This is a conservative
index, not a maximal-order assertion. Negative real zeros also avoid
that sector, whether their principal argument is taken as pi or -pi.
Neither a boundary zero exclusion at arbitrarily large height nor RH
has been inferred.

**Real products and passage to every fixed minor.** Apply the cited
Hadamard product input after the positive change of variable:

\[
G(w)=G(0)\prod_{\nu}(1-w/\omega_\nu),\qquad
\sum_\nu |\omega_\nu|^{-1}<\infty.
\]

The omega_nu enumerate zeros of G itself with multiplicity, not all
xi zeros separately (reflection-related xi zeros have the same image).
There is no zero at the origin. Reality of G permits an exhaustion
by finite multisets invariant under conjugation: include real zeros
and full nonreal conjugate pairs with their multiplicities. Each
finite product P_N has real coefficients, P_N(0)=G(0)>0, and only
zeros of G, so Theorem B gives P_N in PF_6001. Repeated roots are
allowed by the theorem and retained in these products; no simplicity
assumption is used. The reciprocal-modulus summability ensures the
grouped products converge uniformly on every compact set to G.

For completeness, the finite-minor limit in that cited passage needs
no uniformity in minor size or index. On any fixed circle about zero,
Cauchy's coefficient formula and compact convergence give
[w^j]P_N -> a_j for each fixed j>=0; negative coefficients remain
zero. For a fixed pair of finite increasing index sets, only finitely
many such coefficients occur. Its determinant is a polynomial in
those entries, hence the corresponding nonnegative determinants of
P_N tend to the displayed determinant of G. Their limit is
nonnegative. The index sets were arbitrary, proving PF_6001.

The rescaling check can equivalently be made in Katkova's coefficients.
For B=[b_(q_j-p_i)] and A=[a_(q_j-p_i)],

\[
A=8^{-1}\operatorname{diag}(4^{p_i})\,B\,
             \operatorname{diag}(4^{-q_j}),\qquad
\det A=8^{-d}4^{\sum_i p_i-\sum_j q_j}\det B.
\]

This factor is positive, including entries with negative coefficient
index, which are zero on both sides. The ordering of rows and columns
is preserved. For the consecutive minor take p_i=i-1 and
q_j=k+j-1; its factor is 8^(-r)4^(-rk)>0. This verifies the
normalization for the entire asserted family, not only a central cell.

L813's order-five cell is subsumed; L466's Laguerre signs are a
different family and are not premises. L830/L831 and the step659
hybrid reference are also not premises: their uncertain entries are
not an actual coefficient sequence covered by this import. The
result does not certify a determinant ratio, a cofactor estimate or
a strict sign. The actual all-degree gap remains open.

## Mathlib

Full matching coverage has not been checked. No presence or absence
claim is made for this finite-height PF theorem, the sufficient sector
theorem or the complete product/minor passage. The informal input is
the precisely cited mathematics above.
