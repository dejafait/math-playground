# Lemma 833: an actual minor floor from a verified zero divisor

## Hypotheses

Use the actual completion of L018, the positivity of L021 and only
the ordinary-coefficient definitions of L776:

\[
G(w)=\frac18\xi\left(\frac12+\frac{\sqrt w}{2}\right)
     =\sum_{n\ge0}a_nw^n,\qquad a_n=0\quad(n<0),
\]

\[
D_{(r,k)}=\det[a_{k+j-i}]_{i,j=0}^{r-1}.
\]

The square-root expression denotes the entire series. Use L832's
unconditional zero-sector and positive genus-zero product inputs,
with the external theorem qualifications below. Set

\[
H=3\,000\,175\,332\,800,\qquad m=6000,\qquad r=m+1=6001.
\]

No RH, zero simplicity, hybrid regularity, zero-count radius,
Fredholm estimate or perturbation bound is assumed.

## Conclusion

For this actual coefficient minor,

\[
\boxed{D_{(6001,6000)}\ \ge\
G(0)^{6001}(4H^2)^{-6000\cdot6001}>0.}                 \tag{1}
\]

Here G(0)=xi(1/2)/8=M_0/8>0 is an exactly specified constant;
no numerical enclosure of it or individual zero ordinates is used.
The integer exponent is 36,006,000. This is a finite quantitative
specialization of known composition and sector results. It supplies
neither an all-order sign theorem nor an absolute perturbation or
hybrid cofactor comparison.

## Proof

**Precise external inputs.** Dave Platt and Tim Trudgian,
*The Riemann hypothesis is true up to 3 times 10^12*,
Bull. London Math. Soc. **53** (2021), 792–797,
[arXiv:2004.09765v1](https://arxiv.org/pdf/2004.09765v1),
Theorem 1, printed p.2, gives the verified height H above and the
count 12,363,153,437,138 of the lowest nontrivial zeros on the
critical line. Its introduction uses positive heights 0<gamma<=H;
Section 2, pp.2–3, describes the interval-arithmetic verification
and Turing count excluding missing zeros. We import this rigorous
finite-height theorem, rather than infer a count from a sample.

For the sector theorem use I. J. Schoenberg, *A note on multiply
positive sequences and the Descartes rule of signs*, Rend. Circ.
Mat. Palermo (2) **4** (1955), 123–131,
[DOI:10.1007/BF02846031](https://doi.org/10.1007/BF02846031),
as reproduced in Olga M. Katkova, *Multiple positivity and the
Riemann zeta-function*, Comput. Methods Funct. Theory **7** (2007),
13–31, [arXiv:math/0505174v1](https://arxiv.org/pdf/math/0505174v1),
Theorem B, printed p.5. A real polynomial with positive constant
term and no zero in the open sector |arg w|<pi*d/(d+1) has
coefficient sequence PF_d. Katkova's Definition 2/(8), p.4, means
nonnegativity of every ordered Toeplitz minor of size at most d,
with negative coefficients set to zero. Repeated roots are allowed.
Katkova (6), p.3, and the proof of Theorem 1, pp.5–6, give the
genus-zero product and finite-product passage used in L832. We use
that passage and Theorem B, not the printed PF44 index inference.
The original Schoenberg proof has not been inspected.

Finally Allan Pinkus, *Totally Positive Matrices*, Cambridge Tracts
in Mathematics **181** (2010), Section 1.1, pp.2–3,
[publisher excerpt](https://assets.cambridge.org/97805211/94082/excerpt/9780521194082_excerpt.pdf),
gives the finite Cauchy–Binet identity for rectangular matrices and
increasing row, column and intermediate sets. Only this identity
is needed. No strict-product conclusion of Proposition 1.4 is
invoked, and no infinite Cauchy–Binet interchange occurs.

**The genuine degree-m divisor.** The positive-height count exceeds
m. Select m positive-height critical-line zeros
rho_l=1/2+i*gamma_l, 0<gamma_l<=H, with multiplicity. Selection
never uses more copies of an ordinate than its true multiplicity;
the first m zeros in increasing positive height, with repetitions,
are one possible selection. Define

\[
c_l=\frac1{4\gamma_l^2}>0,\qquad
P(w)=\prod_{l=1}^{m}(1+c_lw)=\sum_{n=0}^{m}p_nw^n.
                                                               \tag{2}
\]

To verify the scale and multiplicity, the defining identity is
xi(s)=8G(4(s-1/2)^2). At s=rho_l the derivative of
s -> 4(s-1/2)^2 is 8i*gamma_l, which is nonzero. Thus the
multiplicity at rho_l equals the multiplicity of G at
omega_l=-4*gamma_l^2. Reflection to 1/2-i*gamma_l gives the
same G zero, not a second copy. Distinct positive ordinates have
distinct squared images. Consequently (2) has degree exactly m,
constant term 1, and divides G with the selected multiplicities.
The quotient

\[
R(w)=G(w)/P(w)=\sum_{n\ge0}b_nw^n,\qquad b_n=0\quad(n<0),
\]

extends to an entire real function and has b_0=G(0)>0.

**Residual signs checked directly.** L832 supplies the actual product

\[
G(w)=G(0)\prod_{\nu}(1-w/\omega_\nu),\qquad
\sum_\nu|\omega_\nu|^{-1}<\infty,
\]

where the zeros are those of G, with their own multiplicities.
Its zeros avoid |arg w|<6001*pi/6002. Removing exactly the m
selected negative-real factors gives the product for R, with
unchanged positive constant G(0), remaining reciprocal-modulus
sum finite, and the same sector exclusion. Removing these real
factors preserves the conjugation-invariant multiset of remaining
zeros, including at partially removed repeated negative-real roots.

Exhaust the remaining multiset by finite conjugation-invariant
multisets, with all retained multiplicities. Each corresponding
product, with constant G(0), is a real polynomial satisfying
Theorem B for d=6001. Reciprocal summability gives convergence
of these products to R uniformly on every compact set. For each
fixed coefficient, Cauchy's formula on a fixed circle gives
coefficient convergence; for each fixed finite minor, its
determinant is a polynomial in finitely many such coefficients.
Thus the nonnegative minors pass to the limit. It follows that
(b_n) is PF_6001. This checks the sector/product hypotheses for
the residual itself; it does not assume PF closure under division.

All roots of P are negative real and P(0)=1. The same Theorem B
with d=6001 gives (p_n) in PF_6001, extending p_n by zero for
n<0 and n>m. This requires no simplicity or strict-minor theorem.

**Exact finite convolution.** Put N=m+r-1=12000 and define real
matrices U of size r by N+1 and V of size N+1 by r by

\[
U_{i,h}=p_{h-i},\quad 0\le i\le r-1,\ 0\le h\le N;
\qquad
V_{h,j}=b_{m+j-h},\quad 0\le h\le N,\ 0\le j\le r-1.
                                                               \tag{3}
\]

For fixed i,j, any term p_(h-i)b_(m+j-h) that is nonzero must
have h>=i>=0, h<=i+m, and h<=m+j<=N. Hence every possible
term is in (3), and all excluded integer indices contribute zero.
Since G=PR, ordinary coefficient convolution gives exactly

\[
(UV)_{i,j}=\sum_{h=0}^{N}p_{h-i}b_{m+j-h}
          =a_{m+j-i}.                                      \tag{4}
\]

The least coefficient index in (4) is m-(r-1)=0; there is no
ambiguous negative-index product coefficient. There is no
convergence issue in (4): the polynomial P gives a finite sum.

Finite Cauchy–Binet now gives

\[
D_{(r,m)}=
\sum_{0\le s_0<\cdots<s_{r-1}\le N}
\det[p_{s_j-i}]_{i,j=0}^{r-1}
\det[b_{m+j-s_i}]_{i,j=0}^{r-1}.                         \tag{5}
\]

Every determinant in the first factor is an ordered PF_6001
minor with row set {0,...,r-1} and column set {s_0,...,s_(r-1)}.
Every second factor has row set {s_0,...,s_(r-1)} and column
set {m,...,m+r-1}, also in increasing nonnegative order. Both
have size r=6001, so all summands in (5) are nonnegative.
The intermediate collection is nonempty, since N+1=12001>=r.

**One positive summand and its bound.** Retain only
s_i=m+i for i=0,...,r-1, an admissible increasing set with last
index m+r-1=N. The first matrix in that summand has entries
p_(m+j-i). For j>i its index exceeds m, so it is lower
triangular with diagonal p_m. The second matrix has entries
b_(j-i); for j<i its index is negative, so it is upper
triangular with diagonal b_0. There is no row or column reversal.
The contribution of this summand is therefore

\[
p_m^r b_0^r=G(0)^r\left(\prod_{l=1}^{m}
                       \frac1{4\gamma_l^2}\right)^r>0.
                                                               \tag{6}
\]

Each gamma_l is positive and at most H. Thus
p_m>= (4H^2)^(-m). Combining (5), (6) and G(0)>0 from L021
gives (1), with mr=6000*6001=36,006,000. Closed-height endpoints
and repeated roots are included in the same inequality.

The resulting positive constant can be extremely small. No estimate
has been made of a perturbation, reference determinant, cofactor,
inverse norm or determinant ratio. In particular the step659
hybrid comparison and actual all-degree mixed positivity remain
unresolved. Numerical zero sampling, limit uniformity in minor
size and RH-equivalent positivity are not used.

**Bounded proof audit, 5 November 2026, step666.** The stated floor
passes the separately approved audit, with no correction to the
argument. In particular, selection uses the positive-height count
only; the derivative 8i*gamma is nonzero at every selected zero,
and negative-height reflection does not supply another G factor.
Removal of any allowed portion of a repeated negative-real root
leaves a conjugation-invariant residual multiset and the same
absolutely convergent product. The residual's ordered minors follow
from its own real finite products and fixed-minor limits, rather
than an unproved quotient-closure property.

For the finite algebra, the complete possible nonzero support for
each entry of (4) is the integer interval
`i <= h <= min(i+m,m+j)`, contained in `0 <= h <= 12000`.
An index below i makes p_(h-i) zero; one above i+m also makes it
zero; one above m+j makes b_(m+j-h) zero. Thus no omitted term
can affect (4). The PF matrices have entries coefficient_(column-row):
the second determinant in (5) has increasing rows s_i and increasing
columns m+j, without a transpose or reversal. Both determinants
have size exactly 6001. At the selected S, the zero entries lie above
the diagonal for the p factor and below it for the b factor.
Their diagonal products are p_m^6001 and G(0)^6001, respectively.
Finally 0<gamma_l<=H gives the lower, not upper, bound on each
reciprocal square, with 6000*6001=36,006,000 factors after raising
to the power 6001. These checks include closed endpoints and
repeated roots. No unsupported hypothesis, sign, support case or
factor bound was found.

This audit verifies a local standard specialization under the cited
external theorem inputs; it does not independently rerun the
finite-height verification or inspect Schoenberg's original proof.
The full Cauchy–Binet sum is finite, so neither uniform control in
minor order nor an infinite determinant interchange is required.
The audit supplies no comparison with a perturbation cost and no
extension of the claimed order range.

## Mathlib

Full matching coverage has not been checked. No presence or absence
claim is made for this specialized floor or its complete analytic
inputs. The proof imports the precisely cited theorems and uses
only their checked specialization, finite convolution and finite
Cauchy–Binet; it does not reprove those source theorems.
