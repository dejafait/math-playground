# Lemma 807: the first post-exact theta Gaussian error has one positive transition

## Hypotheses

Use the actual theta kernel K of L019 and the moments of L021. Put

\[
 m_j=\int_0^\infty u^{2j}K(u)\,du,\qquad
 d\mu(u)=K(u)\,du/m_0,
\]

and let nu be the pushforward of mu under v=u^2. Thus nu is a
probability measure on [0,infinity), with all finite moments, and
assigns positive measure to every nonempty open subinterval of
(0,infinity). Use exactly L795's normalization

\[
 P_d(x)=\int f_{d,x}(v)\,d\nu(v),\qquad
 f_{d,x}(v)=\sum_{j=0}^d(-1)^j\binom dj\frac{j!}{(2j)!}v^jx^j
 =\frac{d!}{(1/2)_d}L_d^{(-1/2)}(vx/4).                 \tag{1}
\]

For each integer n>=1 take the n-node Gaussian rule for nu, with
nodes v_1,...,v_n and weights w_1,...,w_n, and define

\[
 \begin{split}
 q_n(v)&=\prod_{i=1}^n(v-v_i),& s_n&=\sum_{i=1}^n v_i,\\
 h_n&=\int q_n(v)^2\,d\nu(v),&
 \alpha_n&=\frac{\int vq_n(v)^2\,d\nu(v)}{h_n},\\
 Q_{n,d}(x)&=\sum_{i=1}^n w_i f_{d,x}(v_i),&
 E_{n,d}(x)&=P_d(x)-Q_{n,d}(x).
 \end{split}                                                   \tag{2}
\]

These are the definitions used in L806; none of its derivative-sign
classification or error conclusions is assumed here. Orthogonality
and Gaussian exactness concern v and nu, not the polynomials P_d.

## Conclusion

All quantities in (2) exist, h_n>0, s_n>0 and alpha_n>0. Set

\[
 B_n=\alpha_n+2s_n>0,\qquad
 X_n=\frac{(4n+2)(4n+1)}{B_n}>0.
\]

The first two moment defects beyond Gaussian exactness are

\[
 \begin{split}
 \int v^{2n}\,d\nu-\sum_i w_i v_i^{2n}&=h_n,\\
 \int v^{2n+1}\,d\nu-\sum_i w_i v_i^{2n+1}&=h_n B_n.
 \end{split}                                                   \tag{3}
\]

For every real x, the exact polynomial error is

\[
 E_{n,2n+1}(x)
 =\frac{(2n+1)!}{(4n+2)!}\,h_n x^{2n}
    \big[(4n+2)(4n+1)-B_n x\big].                    \tag{4}
\]

Consequently E is strictly positive for 0<x<X_n, is zero at X_n,
and is strictly negative for x>X_n. The root X_n is simple. At x=0
E is zero with multiplicity exactly 2n. There are no vanishing leading
coefficients, zero-norm exceptions, missing n=1 cases or further
positive transitions for this actual law.

This is a local specialization of standard Gaussian polynomial
exactness, not a new quadrature theorem or a result beyond the checked
sources. It establishes a concrete signed comparison P>=Q before X_n
and P<=Q after X_n (strict away from the endpoints). It does not locate
X_n relative to roots or sign barriers of Q, prove Q hyperbolic, bound
comparison margins, or establish mixed positivity or RH. Higher-degree
errors are outside this conclusion.

## Proof

**Imported results and applicability.** Import Walter Gautschi,
*Orthogonal Polynomials: Computation and Approximation*, Oxford
University Press, first edition (2004), Theorems 1.6, 1.19, 1.45 and
1.46, pp.1-3, 7 and 21-23,
[book scan](https://csclub.uwaterloo.ca/~pbarfuss/Walter_Gautschi_-_Orthogonal_Polynomials_-_Computation_and_Approximation_%282004%29.pdf).
For a positive measure with all finite moments and positive-definite
polynomial inner product, these give the monic orthogonal polynomial,
its n distinct interior Gaussian nodes, positive quadrature weights,
and exactness through degree 2n-1. Infinite support supplies every n;
there is no truncation of nu. Gautschi Theorem 1.27, pp.10-11,
(1.3.2)-(1.3.7), identifies alpha_n in (2) as the diagonal coefficient
of the monic three-term recurrence. No recurrence estimate is needed.

The polynomial division method below is the finite-polynomial case
of the Hermite remainder: Carl de Boor, *Divided differences*, Surveys
in Approximation Theory 1 (2005), 46-69, Proposition 7, Example 6,
and Proposition 21; [author copy dated 21 June 2021](https://ftp.cs.wisc.edu/Approx/deboor2.pdf),
PDF pp.2-6, (4), (8)-(9), (16), (20). In particular the polynomial
remainder at the doubled Gaussian nodes is divisible by q_n^2,
including repeated interpolation centers. Here direct leading-term
subtraction suffices; no smooth-function mean-value point or
infinite-interval extension of such a theorem is used. Gaussian
existence, orthogonality, exactness and the general Hermite theorem
are imported, not reproved. The explicit specialization is needed to
retain both post-exact coefficients and the theta normalization.

For completeness, the actual-law hypotheses can be checked directly
from the local inputs. L019 gives K>0 and superexponential decay;
L021 gives 0<m_j<infinity. The pushforward therefore satisfies

\[
 \int v^j\,d\nu=m_j/m_0<\infty\qquad(j\ge0).
\]

Every nonzero real polynomial has nonzero square on some positive
open interval, to which nu assigns positive measure by L019/L795.
Its squared norm is therefore positive. Finiteness follows from the
finite moments. This verifies the polynomial positive-definiteness
required by the imported theorems, on the actual unbounded support.
The nodes are distinct and in (0,infinity), so s_n>0. The same open
interval argument applied to vq_n(v)^2 proves its integral strictly
positive. It is finite because moments through order 2n+1 are finite.
Thus h_n and alpha_n are finite and strictly positive.

Every polynomial here is absolutely nu integrable: on v>=0 its
absolute value is bounded by the sum of its coefficient magnitudes
times v^j. In particular all residuals and all monomials in (3) are
integrable. The quadrature sum is finite, and exactness on constants
gives sum_i w_i=1. L795's formula (1), based on NIST DLMF
[18.5.12](https://dlmf.nist.gov/18.5.E12), is used without changing
its x/4 factor or factorial normalization. Only finite sums are
integrated in this proof.

**The two moment defects.** Write the error functional on polynomials
as

\[
 \mathcal D_n[g]=\int g(v)\,d\nu(v)-\sum_iw_i g(v_i).
\]

It vanishes on every polynomial of degree at most 2n-1 by the imported
exactness. Since q_n is monic, v^(2n)-q_n^2 has degree at most 2n-1.
Since q_n(v_i)=0, linearity gives

\[
 \mathcal D_n[v^{2n}]=\mathcal D_n[q_n^2]=h_n.       \tag{5}
\]

The next coefficient of q_n is -s_n. More explicitly, for n>=1,

\[
 q_n(v)^2=v^{2n}-2s_n v^{2n-1}+r(v),\qquad
 \deg r\le2n-2.
\]

It follows that (v+2s_n)q_n(v)^2 has leading term v^(2n+1)
and zero coefficient of v^(2n). Hence

\[
 \deg\big[v^{2n+1}-(v+2s_n)q_n(v)^2\big]\le2n-1.
\]

Exactness applies to this residual, while the subtracted polynomial
vanishes at every quadrature node. Therefore

\[
 \begin{split}
 \mathcal D_n[v^{2n+1}]
 &=\int (v+2s_n)q_n(v)^2\,d\nu(v)\\
 &=h_n(\alpha_n+2s_n)=h_nB_n.                       \tag{6}
 \end{split}
\]

Equations (5)-(6) prove (3). Positivity is an actual integrated fact;
it does not follow from assuming a sign of a high derivative.

**Normalization and transition.** In (1) with d=2n+1, every term
of order j<=2n-1 in v is annihilated by D_n. The last two terms have
coefficients

\[
 c_{2n}=\frac{(2n+1)(2n)!}{(4n)!}>0,\qquad
 c_{2n+1}=-\frac{(2n+1)!}{(4n+2)!}<0.
\]

The power of x is kept outside each coefficient. Write
C_n=(2n+1)!/(4n+2)!>0. The exact coefficient ratio is

\[
 c_{2n}=C_n(4n+2)(4n+1),\qquad c_{2n+1}=-C_n.
\]

Thus (3) gives

\[
 E_{n,2n+1}(x)
 =c_{2n}x^{2n}h_n+c_{2n+1}x^{2n+1}h_nB_n,
\]

which is (4). All its prefactors are strictly positive for x>0;
the remaining bracket is strictly decreasing, with its sole zero
at the positive number X_n. This proves both strict signs. At X_n,
E'=-C_n h_n B_n X_n^(2n)<0, so the root is simple. At zero the
coefficient of x^(2n) is C_n h_n(4n+2)(4n+1)>0, proving the exact
multiplicity. These statements also follow as polynomial identities
at x=0, without division by x.

For the smallest case, put t_j=int v^j dnu. Then v_1=t_1,
w_1=1, q_1=v-t_1 and h_1=t_2-t_1^2>0. Formula (6) gives
h_1B_1=t_3-t_1^3>0. Consequently (4) reads

\[
 E_{1,3}(x)=\frac{h_1x^2}{120}(30-B_1x),\qquad
 X_1=\frac{30h_1}{t_3-t_1^3}.
\]

This agrees directly with f_(3,x)=1-(3/2)vx+(1/4)v^2x^2
-(1/120)v^3x^3, and includes n=1 without an empty-index exception.

**Limit of the result.** The threshold in (4) gives an exact
one-sided comparison on each of two intervals. Turning it into
root barriers requires independently established reference values
and margins with the necessary directions on those intervals.
No such reference hypothesis is assumed or proved. The L795 full-
support interlacing stop, L796 Favard stop, L805 compressed-pair
stop and L806 derivative-sign limitation retain their stated scopes;
none is used as a premise here. This result does not supply a
higher-degree or degree-uniform bridge to actual mixed positivity.

### Independent finite-polynomial audit, 5 November 2026 — step549

The exact invocation-start audit scope is
`drafts/literature/2026-11-05-theta-first-post-exact-audit.md`.
Independent replay found no mathematical defect in (1)-(6), their
actual-law applicability, strictness or endpoint cases. This audit
reuses the inspected primary-source coverage above; it neither
reproves Gaussian existence nor imports a new remainder theorem.

**Measure and theorem hypotheses.** For every j>=0 the pushforward
identity gives integral v^j dnu=m_j/m_0. On v>=0 every absolute
polynomial is bounded by a finite sum of these monomials. In
particular the audit needs moments only through 2n+1 for (3),
and through any fixed finite order for existence of the rule.
For 0<a<b, the preimage (sqrt(a),sqrt(b)) has positive K integral;
hence nu has full positive-half-line support. A nonzero polynomial
is bounded away from zero on some smaller positive interval.
Its square, and v times its square, therefore have strictly positive
integrals. Applied to the monic q_n, this proves 0<h_n<infinity
and 0<alpha_n<infinity. The cited Gaussian theorem supplies n
distinct nodes strictly inside (0,infinity), so 0<s_n<infinity.
There is no finite-support exception, endpoint node, moment-determinacy
assumption or limiting Gaussian rule in this use of the theorem.

**Residual degrees.** Independently expanding the two highest powers
of q_n^2 gives v^(2n)-2s_n v^(2n-1). Subtracting q_n^2 from
v^(2n) leaves degree<=2n-1. Multiplication by v+2s_n cancels
the coefficient of v^(2n) and leaves leading coefficient one
at v^(2n+1); the second residual again has degree<=2n-1.
Both residuals are therefore annihilated by the actual Gaussian
error functional. At each node both subtracted expressions vanish,
so their errors are exactly their integrals, h_n and
integral (v+2s_n)q_n^2 dnu=h_n(alpha_n+2s_n).
No sign-changing derivative or unspecified mean-value point enters.

**Normalization, signs and degeneracies.** Replaying L795's finite
coefficient formula, at j=2n the coefficient is
(2n+1)!/(4n)!, while at j=2n+1 it is
-(2n+1)!/(4n+2)!. The ratio of their magnitudes is exactly
(4n+2)(4n+1). All lower v powers are exact, so these two
coefficients give (4), with no missing factor of 4, factorial or
m_0. Since B_n>0, its affine bracket decreases strictly from a
positive constant to negative values. The other factor is positive
for x>0. At X_n differentiation gives
-C_n h_n B_n X_n^(2n)<0; at zero the x^(2n) coefficient is
strictly positive. Thus the asserted simple positive root and
exact multiplicity 2n at zero are valid without dividing by x.

The small case was replayed independently rather than inferred
from an empty polynomial sum. With t_j=integral v^j dnu,
exactness gives w_1=1 and v_1=t_1>0. Then
h_1=t_2-t_1^2>0 and
integral v(v-t_1)^2 dnu=t_3-2t_1t_2+t_1^3.
Adding 2t_1 h_1 gives h_1 B_1=t_3-t_1^3>0.
The coefficients 1,-3/2,1/4,-1/120 of f_(3,x) consequently
give exactly h_1 x^2(30-B_1 x)/120. No n=1 exception remains.

The direct local mathematical inputs remain L019, L021 and L795.
L806 contributes only notation; neither it nor the contrast results
L796/L805 supply an essential premise. The audit verifies this local
specialization, not an independently certified reference value,
reference hyperbolicity, root margin, higher-degree error or
degree-uniform mixed-positivity bridge. It is local validation of
known mathematical tools, with no claim beyond the sources checked.

## Mathlib

Full matching coverage has not been checked. Availability in Mathlib
of the actual-theta Gaussian rule, these two normalized moment-defect
identities and their all-n transition specialization is unknown.
No formal verification or absence claim is made. The complete finite
polynomial proof, strictness and integrability checks are above;
standard mathematical inputs have precise citations.
