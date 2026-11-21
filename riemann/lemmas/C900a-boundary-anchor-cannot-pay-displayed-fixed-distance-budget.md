# Corollary 900a: boundary anchor cannot pay the displayed fixed-distance budget

## Hypotheses

Use the actual Xi, theta kernel, C_y(x), A_0(y), a>0, Q>0 and
E_1>0 of L900. In particular x is real, 0<=y<=1/2, and the
normalizers are finite and strictly positive. Set

\[
 B=A_0(1/2),\qquad
 \mathcal E(x)=(1+|x|)^5 e^{-\pi|x|/2},\qquad
 D=\frac{32\,2^{9/2}E_1}{9B}>0.
\]

Let K be the particular finite positive constant in L900 (2):

\[
 K=2^{9/2}E_1\left(\frac{256}{27a}+\frac{16Q}{27a^2}\right).
\]

No RH, simplicity, nonvanishing of Xi or zeta, or sign of C_y is
assumed. Constants are fixed independently of x and y; their numerical
values have not been evaluated.

## Conclusion

For every real x,

\[
 0\leq
 \frac{|C_{1/2}(x)|}{B\mathcal E(x)}
 \leq \frac{D}{\sqrt{1+|x|}}.
 \tag{1}
\]

Consequently the ratio tends to zero as |x| tends to infinity,
covering both signs of x. For each fixed 0<=y<1/2, the displayed
sufficient test obtained by anchoring L900 (1) at v=1/2,

\[
 \frac{C_{1/2}(x)}{B}
   >K\mathcal E(x)(1/4-y^2),
 \tag{2}
\]

fails for all sufficiently large |x|. This rules out (2) as an
eventual fixed-distance signing mechanism. It does not show failure
of actual positivity, of a sharper interpolation bound, or of a
different anchor. No conclusion about shrinking distances or a
bounded frequency band is asserted.

## Proof

### Reuse of the stronger bound already proved in L900

L900 (3) defines

\[
 M_x=E_1(2+|x|)^{9/2}e^{-\pi|x|/2}.
\]

Before enlarging its power to 5, that audited proof establishes in
(6)–(7), for every real x and every 0<=v<=1/2,

\[
 |C_v(x)|\leq\frac{32}{9}M_x.
 \tag{3}
\]

Specifically its analytic squared-height function satisfies
|F_x(t)|<=2M_x/(1-t)^2<=32M_x/9 on 0<=t<=1/4, and
C_v(x)=F_x(v^2), including both endpoints. Thus (3) applies directly
at v=1/2; no boundary limiting argument or division by a height is
required. The present proof imports this established intermediate
estimate, rather than repeating its Cauchy argument or the underlying
completed-zeta estimates. The separately source-covered boundary
completion/ordinary-derivative computation is unnecessary for this
target. This is a consequence of existing bounds, not a stronger
estimate for Xi or a claim beyond the checked analytic framework.

Put T=|x|>=0. Since B>0 and the exponential factors are positive,
division of (3) at v=1/2 by B times the envelope is legitimate and gives

\[
 \frac{|C_{1/2}(x)|}{B\mathcal E(x)}
 \leq\frac{32E_1}{9B}
           \frac{(2+T)^{9/2}}{(1+T)^5}
 \leq\frac{32E_1\,2^{9/2}}{9B}(1+T)^{-1/2}.
\]

Here 2+T<=2(1+T), and both sides are positive before taking the
power 9/2. This proves (1), including T=0. Its upper bound tends to
zero, so the claimed little-o limit follows. No division by Xi or
zeta has occurred, including at any zero.

### Exact comparison with the displayed sufficient test

Fix 0<=y<1/2 and put delta=1/4-y^2>0. L900 (1), at v=1/2,
implies

\[
 \frac{C_y(x)}{A_0(y)}
 \geq\frac{C_{1/2}(x)}B-K\mathcal E(x)\,\delta.
 \tag{4}
\]

Thus (2) is indeed sufficient for strict positivity via this lower
bound. To see that this particular test eventually fails, take any
x satisfying

\[
 1+|x|\geq\left(\frac{2D}{K\delta}\right)^2.
 \tag{5}
\]

By (1),

\[
 \frac{C_{1/2}(x)}B
 \leq\frac{|C_{1/2}(x)|}B
 \leq\tfrac12 K\delta\mathcal E(x)
 <K\delta\mathcal E(x).
\]

The final inequality is strict because K, delta and the envelope
are positive. This contradicts (2), proving the asserted eventual
failure for either sign of x. Condition (5) is a symbolic threshold,
not an evaluated numerical onset. The case y=0 is included; the
case y=1/2 is excluded because delta=0 there. A distance varying
with x is not covered by this fixed-delta conclusion. Finally,
failure of a sufficient condition does not negate the positivity
it was intended to establish. Neither (1) nor (4) determines the
actual sign. ∎

This local obstruction removes the displayed fixed-distance budget
as an eventual route. The actual-Xi all-degree mixed positivity gap
L030–L032/C032a remains unresolved. The result is classified as
REPRODUCTION: the new local stopping conclusion uses the already
audited stronger preliminary bound of L900. The original step120
derivation was unaudited; the separate review below now verifies it.

### Independent audit (2026-11-08, step122)

The stated bound and the fixed-distance stopping conclusion pass the
approved audit without a mathematical repair. The imported input is
L900 (3), (6)–(7), not merely its weaker displayed conclusion (1).
In that proof the coefficient bound is uniform in real x, and the
squared-height series is analytic on |t|<1. On the closed interval
0<=t<=1/4 its modulus is at most 2M_x/(1-t)^2<=32M_x/9.
The identification C_v(x)=F_x(v^2) holds also at v=0 and v=1/2.
Thus using v=1/2 here does not require a boundary limit or an
additional derivative estimate.

Write T=|x|. The imported exponent is exactly 9/2. Since
2+T<=2(1+T), division by B(1+T)^5 exp(-pi T/2) gives precisely
(32/9)E_1 2^(9/2)/[B sqrt(1+T)], which is the displayed D bound.
All factors divided out are strictly positive, including at x=0.
Finiteness and positivity of B, a, Q and E_1 are inherited from
L900's hypotheses and real normalizers; hence the displayed D and K
are finite and strictly positive and independent of x,y. No optimal
choice of E_1 or numerical evaluation is needed for this conclusion.

For fixed 0<=y<1/2, delta=1/4-y^2 is strictly positive. The absolute
quotient-difference estimate in L900 implies exactly (4), with a
minus sign on its error, so (2) really is a sufficient strict test.
Taking positive square roots and reciprocals in (5) gives
D/sqrt(1+T)<=K delta/2. Consequently C_(1/2)(x)/B is at most
K delta times the envelope divided by 2, and is strictly less than
the threshold in (2), even when equality holds in (5). This is a
failure of the test itself, not just a failure to verify it.

Every step uses |x|, so both frequency signs are covered. The lower
height endpoint y=0 gives delta=1/4 and is included. At y=1/2 the
positive-distance argument and its strict threshold do not apply;
that endpoint is correctly excluded from the stopping conclusion.
For each fixed y the set specified by (5) contains both sufficiently
large frequency rays, but no uniform onset as y approaches 1/2 has
been proved. Constants remain unevaluated. A shrinking distance, a
bounded band, a sharper error budget and the actual sign all remain
outside the conclusion. Failure of this sufficient test proves no
failure of positivity and resolves no all-degree mixed sign.

The only direct mathematical input is L900, in agreement with the
unchanged local DAG. This is verification of a local consequence of
the already assessed analytic method, not a new growth or sign result.

## Mathlib

Full matching coverage has not been checked; availability is unknown.
No new supporting Mathlib theorem was inspected. The analytic input
is the canonical audited L900 estimate; no new external theorem,
numerical certificate or mathematical script is needed here.
