# Corollary 795a: eventual positivity of the formal theta half-factor's first Hermite block

## Hypotheses

Use the actual theta kernel of L019, moments m_n=M_(2n) of L021,
and the polynomial of L795:

\[
 \gamma(n)=\frac{n!m_n}{(2n)!}>0,\qquad
 P_d(x)=\frac1{\gamma(0)}\sum_{j=0}^d(-1)^j\binom dj\gamma(j)x^j.
\]

For each integer d>=4 set

\[
 h=h_d=\frac{\gamma(d-1)}{\gamma(d)},\quad
 M_d(x)=\frac{\gamma(0)}{(-1)^d\gamma(d)}P_d(x),\quad
 C_d(y)=M_d(y+h).
\]

Use symmetric finite-free additive convolution at the same degree d,
in the coefficient convention specified below. Let Q_d denote the unique
real monic formal half-factor Q_d boxplus_d Q_d=C_d. Its existence here
is algebraic; no root condition is imposed. Write s_j for its algebraic
root power sums, counting complex roots with multiplicity, with s_0=d.

## Conclusion

For all sufficiently large integers d the proper Hermite principal block

\[
 H_d=(s_{i+j})_{0\le i,j\le2}
\]

is positive definite. More precisely, with w=W(2d/pi),

\[
 \frac{s_2}{dh^2}\longrightarrow\frac12,\qquad
 \frac{s_3}{dh^3}\longrightarrow\frac12,\qquad
 \frac{s_4}{dh^4}\longrightarrow1,\qquad s_1=0.
 \tag{1}
\]

Each convergence in (1) has error O(1/w+log^4(d)/d). Consequently

\[
 \frac1d\operatorname{diag}(1,h^{-1},h^{-2})H_d
       \operatorname{diag}(1,h^{-1},h^{-2})
 \longrightarrow
 H_\infty=\begin{pmatrix}1&0&1/2\\0&1/2&1/2\\1/2&1/2&1\end{pmatrix}.
 \tag{2}
\]

The seven principal minors of H_infinity, indexed respectively by
{0},{1},{2},{0,1},{0,2},{1,2},{0,1,2}, are

\[
 1,\quad\tfrac12,\quad1,\quad\tfrac12,\quad\tfrac34,
 \quad\tfrac14,\quad\tfrac18.                         \tag{3}
\]

Eventually each corresponding normalized minor exceeds half its value
in (3); in particular det(H_d)/(d^3 h^6)>1/16. No effective onset is
claimed. This retires this fixed-block eventual negative-minor detector.
It proves neither real-rootedness of Q_d nor the uniform half-factor
proposal, and does not settle shifted/mixed signs, global assembly or RH.
This is a local asymptotic specialization using established methods;
the checked literature did not identify this exact application, but
originality is not asserted. The separate step767 conceptual audit
validates this conclusion, with the explicit derivative recursion
corrected below; it supplies no effective onset or full-factor claim.

## Proof

### Imported inputs and exact normalization

O. Arizmendi and D. Perales, *Cumulants for finite free convolution*,
[arXiv:1611.06598v2](https://arxiv.org/pdf/1611.06598v2), 7 March 2017,
Propositions3.4/3.6, pp7-8, give invertible monic coefficient/cumulant
coordinates and cumulant additivity without a real-root hypothesis.
Lemma4.1, p9, gives the coefficient/power-sum conversion. We use their
formal halving operation, with the symmetric additive coefficient formula
of Marcus--Spielman--Srivastava, *Finite free convolutions of polynomials*,
[arXiv:1504.00350v2](https://arxiv.org/pdf/1504.00350v2),
Definition1.1/(1)-(2), pp2-3:

\[
 a_k(f\boxplus_d g)=\sum_{i+j=k}
 \frac{(d-i)!(d-j)!}{d!(d-k)!}a_i(f)a_j(g),
 \qquad f(x)=\sum_{k=0}^d(-1)^ka_k(f)x^{d-k}.
 \tag{4}
\]

All a_0 are 1. Its forward real-root preservation theorem is not used.
The equations below verify the necessary low-order specialization and
normalization, rather than reprove the general cumulant theorem.

C. O'Sullivan, *Zeros of Jensen polynomials and asymptotics for the
Riemann xi function*, [arXiv:2007.13582v2](https://arxiv.org/html/2007.13582v2),
9 December 2020, (1.2), Theorem1.4 and Section7/(7.3)-(7.14), supplies,
at the fixed truncation order K=4 chosen before this calculation,

\[
 \gamma(n)=A(n)\left(B(n)+O\left(\frac{\log^4 n}{n^4}\right)\right),
 \quad B(x)=1+\sum_{k=1}^3\frac{c_k(W(2x/\pi))}{x^k},             \tag{5}
\]
\[
 A(x)=4\pi^2 e^{7w/4}\sqrt{\frac w{w+1}}
       \left(\frac{e w^2}{16x e^{2/w}}\right)^x,
 \qquad w=W(2x/\pi).
 \tag{6}
\]

Each c_k is the fixed rational function specified in (7.13), of size
O(w^k) at infinity; the constant in (5) depends on K only.
L021 and Xi(z)=xi(1/2+iz) identify m_n=xi^(2n)(1/2), so the gamma
normalization agrees exactly with source (1.2). There is no factor8
or factor4 change. The assessed Section7 proof absorbs the higher-theta
tail before applying Stirling; no theta truncation is assumed here.
We import (5) only at integer n and fixed offsets n=d-j.

M. B. Nathanson, *The Hermite-Sylvester criterion for real-rooted
polynomials*, [arXiv:1911.01745v2](https://arxiv.org/pdf/1911.01745v2),
24 November 2019, Lemmas1-2/Theorem1, pp1-3, identifies PSD of the full
Hermite matrix with real-rootedness, allowing multiplicities. Here only
a proper 3-by-3 block is evaluated, so no converse root conclusion follows.
The root powers throughout are algebraic powers, not absolute powers.

The prior target assessment is
`drafts/literature/2026-11-13-theta-half-factor-asymptotic-block-764.md`.
The finite degree-three/four factors L823/L824, common-symbol failure
L825 and reciprocal moment result L827 are contrasts, not inputs.

### Centering and the unique half-factor

Put q_j=gamma(d-j)/(gamma(d)h^j) for 0<=j<=4. Thus q_0=q_1=1.
The monic M_d has elementary coefficients binom(d,j)h^j q_j.
Translating by h, its centered elementary coefficient e_k is

\[
 e_k=\binom dk h^k\sum_{j=0}^k(-1)^{k-j}\binom kj q_j.
 \tag{7}
\]

Indeed the contribution of the jth monic coefficient to the kth one
is (-1)^(k-j)binom(d-j,k-j)h^(k-j); use
binom(d,j)binom(d-j,k-j)=binom(d,k)binom(k,j).
In particular e_1=0. Define

\[
 \delta_2=q_2-1,\quad \delta_3=q_3-3q_2+2,\quad
 \delta_4=q_4-4q_3+6q_2-3,
 \qquad e_k=\binom dk h^k\delta_k.               \tag{8}
\]

In (4), the two end terms for self-convolution are 2b_k, where b_k
is the kth elementary coefficient of Q_d. Every other term uses
b_i with i<k. Starting with b_0=1, solve these real triangular
equations successively; division by 2 is always allowed. This verifies
existence and uniqueness of the real monic Q_d at every degree and
identifies it with the formal halved-cumulant polynomial.
For k<=4, the equations and Newton identities give exactly

\[
 b_1=0,\quad b_2=e_2/2,\quad b_3=e_3/2,\quad
 b_4=e_4/2-\eta e_2^2/8,
 \quad \eta=\frac{(d-2)(d-3)}{d(d-1)},             \tag{9}
\]
\[
 s_1=0,\quad s_2=-e_2,\quad s_3=3e_3/2,\quad
 s_4=\frac{1+\eta}{2}e_2^2-2e_4.                 \tag{10}
\]

For (9), the sole nonzero interior k=4 term in (4) is eta b_2^2.
For (10), Newton gives s_2=-2b_2, s_3=3b_3 and
s_4=2b_2^2-4b_4. These identities hold over the complex roots without
any positive measure or hyperbolicity premise.

### Smooth explicit approximant, with the source remainder left undifferentiated

For sufficiently large real x, B(x)>0 and define
F(x)=log A(x)+log B(x). Taking logs in (5), at integer n only, yields

\[
 \log\gamma(n)=F(n)+O(\log^4(n)/n^4).             \tag{11}
\]

Indeed B tends to 1, so eventually B>=1/2. If rho_n denotes the
remainder inside the parentheses in (5), then |rho_n|<=1/4 eventually.
The derivative of log on [1/4,infinity) is at most 4, so
|log(B(n)+rho_n)-log B(n)|<=4|rho_n|. This uses no regularity of rho_n.

All derivatives below are of this explicit F, not of the remainder
or of an interpolation of gamma(n). Rationality and c_k(w)=O(w^k)
imply c_k^(r)(w)=O(w^(k-r)) for every fixed r>=0 at infinity:
expand a rational function in its Laurent series at infinity, where
its highest exponent is at most k. It has no poles beyond a fixed
point. Also w'=w/(x(1+w)) and w tends to infinity with w<=log(2x/pi)
eventually. Put D=(w/(1+w))d/dw. For T_k(x)=x^(-k)c_k(w(x)), the exact
recursion is

\[
 T_k^{(r)}(x)=x^{-k-r}R_{k,r}(w(x)),\qquad
 R_{k,0}=c_k,\qquad R_{k,r+1}=(D-k-r)R_{k,r}.
\]

Thus the scalar part of the operator changes at every derivative;
it is not always -k. Each R_{k,r} is rational, has no poles for large
w, and is O(w^k) by induction and the Laurent expansion just used.
For fixed r and k=1,2,3 this gives
T_k^(r)=O(log^k(x)/x^(k+r))=O(log(x)/x^(r+1)).
Consequently, for 0<=r<=5,

\[
 B(x)-1=O(\log x/x),\quad
 B^{(r)}(x)=O(\log x/x^{r+1})\ (r\ge1),\quad
 (\log B)^{(r)}(x)=O(\log x/x^{r+1})\ (r\ge1).   \tag{12}
\]

The last bound follows by differentiating log B: B is bounded away
from zero and every product with two or more derivatives has at least
one further factor O(log x/x). These are bounds on known smooth
functions and do not strengthen the regularity of (11).

Write
g(x)=x(1+2log w-log(16x)-2/w) and
p(x)=log(4pi^2)+7w/4+(log w-log(w+1))/2, so F=g+p+log B.
Direct differentiation gives

\[
 g'=\log(w^2/(16x)),\qquad
 g''=-a(w)/x,\quad a(w)=1-\frac2{w+1}.
\]

With the same D, let b=a-Da and c=Db-2b. Explicitly,

\[
 Da=\frac{2w}{(w+1)^3},\quad
 b=\frac{w^3+w^2-3w-1}{(w+1)^3},\quad
 Db=\frac{2w^2(w+4)}{(w+1)^5},\quad c=Db-2b.
\]

Then

\[
 g'''=b(w)/x^2,\quad g''''=c(w)/x^3,\quad
 a\to1,\ b\to1,\ c\to-2,\quad g^{(5)}=O(x^{-4}).
\]

In particular g^(5)=(Dc-3c)/x^4. These rational functions and their
D-derivatives are bounded at infinity; their displayed limits have
error O(1/w). For the prefactor,

\[
 Dp=\frac{7w}{4(w+1)}+\frac1{2(w+1)^2}.
\]

This is bounded rational, and p^(r)=x^(-r)S_r(w), with
S_1=Dp and S_(r+1)=(D-r)S_r, proves p^(r)=O(x^(-r)) for 1<=r<=5.
Together with (12), these bounds are uniform on [d-4,d], since
x/d tends uniformly to 1 there and w(x) tends uniformly to infinity.
Thus, putting t=F''(d), u=F'''(d), v=F''''(d),

\[
 dt=-1+O(1/w+1/d),\quad d^2u=1+O(1/w+1/d),\quad
 d^3v=-2+O(1/w+1/d),\quad
 \sup_{x\in[d-4,d]}|F^{(5)}(x)|=O(d^{-4}).       \tag{13}
\]

In particular t=O(d^(-1)), u=O(d^(-2)), v=O(d^(-3)).
Taylor's theorem on that fixed interval and the five separate integer
instances of (11) now imply, uniformly for j=0,...,4,

\[
 \log q_j=\frac{j^2-j}{2}t-\frac{j^3-j}{6}u
             +\frac{j^4-j}{24}v+O(\log^4(d)/d^4).        \tag{14}
\]

The identity behind (14) is log q_j=log gamma(d-j)+(j-1)log gamma(d)
-j log gamma(d-1). It cancels the constant and linear Taylor terms
exactly. The bounded Taylor remainder is O(d^(-4)). The coefficients
of the five errors in (11) are fixed integers with bounded total absolute
value for 0<=j<=4, so their contribution is O(log^4(d)/d^4).
No difference quotient of an unspecified remainder has been estimated
by a derivative.

### Cancellation through the fourth moment

Assign weights 1,2,3 to t,u,v. Expanding exp of (14) through weight3
is justified since its argument is O(1/d), and the omitted terms and
source errors are O(E), E=log^4(d)/d^4. This yields

\[
 \begin{aligned}
 q_2&=1+t-u+t^2/2+7v/12-tu+t^3/6+O(E),\\
 q_3&=1+3t-4u+9t^2/2+13v/4-12tu+9t^3/2+O(E),\\
 q_4&=1+6t-10u+18t^2+21v/2-60tu+36t^3+O(E).
 \end{aligned}                                                    \tag{15}
\]

Therefore

\[
 \begin{aligned}
 \delta_2&=t-u+t^2/2+7v/12-tu+t^3/6+O(E),\\
 \delta_3&=-u+3t^2+3v/2-9tu+4t^3+O(E),\\
 \delta_4&=3t^2+v-18tu+19t^3+O(E),\\
 \delta_2^2&=t^2-2tu+t^3+O(E).
 \end{aligned}                                                    \tag{16}
\]

The last error also absorbs weight4 terms O(d^(-4)); products involving
the previous O(E) error are smaller, since delta_2=O(1/d).
From (8)/(10),

\[
 \frac{s_2}{dh^2}=-\frac{d-1}{2}\delta_2\to\frac12,
 \qquad
 \frac{s_3}{dh^3}=\frac{(d-1)(d-2)}4\delta_3\to\frac12.          \tag{17}
\]

For the fourth power sum, retain the cancelling terms exactly. Put

\[
 A_d=\frac{d(d-1)(d^2-3d+3)}4,\qquad
 B_d=\frac{d(d-1)(d-2)(d-3)}{12}.
\]

Equation (10) divided by h^4 is A_d delta_2^2-B_d delta_4. Using
(16), dividing by d, and combining the t^2 terms before estimating,
gives

\[
\begin{aligned}
 \frac{s_4}{dh^4}
 ={}&\frac{(d-1)(2d-3)}4t^2
 +\frac{(d-1)(2d^2-12d+15)}2tu\\
 &+\frac{(d-1)(-16d^2+86d-105)}{12}t^3
 -\frac{(d-1)(d-2)(d-3)}{12}v
 +O(\log^4(d)/d).                                    \tag{18}
\end{aligned}
\]

In particular A_d-3B_d=d(d-1)(2d-3)/4 is order d^3, not d^4.
The source error O(E) is multiplied by at most O(d^4) and then divided
by d, giving the stated vanishing error. The four limits on the right
of (18), in order, are

\[
 \frac12,\qquad -1,\qquad \frac43,\qquad \frac16,
\]

whose sum is 1. Equations (13)/(16)-(18) also prove the common error
O(1/w+log^4(d)/d) asserted in (1). This controls every cancellation
needed for the selected block using K=4; no higher order or degree
sweep is needed.

### All principal minors and scope of the sign conclusion

Since Q_d has real coefficients, its algebraic power sums are real,
even if some roots are nonreal. The matrix in (2) is thus real symmetric
and has entries 1,0 and the three normalized quantities in (1).
Its minors converge to (3), since each minor is a polynomial in the
entries. There are only seven minors, each with a strictly positive
limit; choose one sufficiently large integer onset after which each
differs from its limit by less than half that limit. They are then all
positive. The principal-minor criterion gives positive definiteness.
Positive scalar multiplication and congruence by the invertible real
diagonal matrix preserve positive definiteness, proving the conclusion
for H_d itself. This congruence only measures the same block; it does
not alter the polynomial family or repair a common-symbol relation.

In particular the determinant is m_2 m_4-m_3^2-m_2^3 in terms of
m_j=s_j/(dh^j), and its limit is 1/2-1/4-1/8=1/8.
Checking all minors avoids an inference of PSD from nonnegative leading
minors alone. No full Hermite matrix, growing block, positive root
measure, finite-degree exception list or effective threshold is supplied.

### Exact algebra check

`python3 scripts/central-jacobi/half_factor_block_765.py` writes
`scripts/central-jacobi/half-factor-block-765.json`. Its 15 checks pass
using Python integer/Fraction multivariate arithmetic: (15)/(16), the
exact cancellation identity (18), its contracted fourth-moment limit,
and all seven limiting principal minors. No numerical degrees or fitted
coefficients are used. This is auxiliary finite algebra, not a proof
of the source asymptotic, derivative bounds or eventual positivity;
those are justified above. Python arithmetic remains an ordinary
software contract, and the displayed identities admit direct checking.

### Separate conceptual audit — 13 November 2026, step767

The preapproved scope was
`drafts/literature/2026-11-13-half-factor-block-conceptual-audit-765.md`.
The audit rechecked source Theorem1.4 and (7.9)/(7.13)-(7.14), using
the already assessed Section7/Laplace proof, against the exact local
normalization. It verified centering, the triangular equations and
Newton conversion directly. The changing derivative operator was made
explicit above; the log step, prefactor derivatives, uniform interval
bound and integer error passage were checked without differentiating
an unknown remainder. This repairs the earlier operator wording and
confirms the derivative estimates, rather than changing the theorem.

Independent coefficient collection in (18) gives A_d-3B_d for t^2,
-2A_d+18B_d for tu, A_d-19B_d for t^3, and -B_d for v, all divided by d.
After multiplication by t^2,tu,t^3,v respectively, the four limits are
1/2,-1,4/3,1/6; the total is 1.
The errors in (17) are at most O(1/w+log^4(d)/d), and the larger
fourth-moment multiplier is O(d^3) after normalization, hence also
gives O(log^4(d)/d). All seven minor limits in (3) were checked
directly, including the nonleading minors; their least value is 1/8>0.
The 15-check auxiliary program was replayed successfully, with its
complete expansions, cancellation polynomial, contracted expression,
minors and empty failure list inspected. Its arithmetic is not a
certificate for the analytic part of this audit.

The eventual-sign conclusion passes. The fixed-block negative-minor
detector is retired; no full Hermite positivity, finite exceptions,
degree-uniform real-rooted half-factor family or RH follows. This is
an audit/reproduction of the existing specialization, not a claim of
progress beyond the cited mathematics.

## Mathlib

Full matching coverage is not checked. Availability of this actual-theta
half-factor asymptotic and its Hermite block in Mathlib is unknown.
The imported analytic and finite-free theorems are used as mathematical
references, not asserted to be formalized; no absence claim is made.
