# Lemma 902: normalized even defect moments strictly decrease with height

## Hypotheses

Use the actual positive theta kernel k(u)=K(|u|) of L019, with the
smooth evenness used in L309, and put Phi=k/2. Retain L309's explicit
L037 directed-rounding and exponential arithmetic contracts. In
particular, import L309's conclusion that V=-log k is smooth and even
and V'''(u)>0 for u>0. Its finite curvature certificate is not
independently replayed here. No Fourier-sign or RH assumption is made.

Use exactly L898's normalization: p=u+v, q=u-v,

\[
 A_{2j}(y)=\iint_{\mathbb R^2}p^2\operatorname{sinhc}(yp)
                  q^{2j}\Phi(u)\Phi(v)\,du\,dv,
 \qquad m_{2j}(y)=\frac{A_{2j}(y)}{A_0(y)},
 \quad 0\le y\le\tfrac12,
\]

where sinhc(0)=1 and sinhc(a)=sinh(a)/a otherwise.

## Conclusion

For every integer j>=1 and every 0<=y_1<y_2<=1/2,

\[
                 0<m_{2j}(y_2)<m_{2j}(y_1)<\infty.
 \tag{1}
\]

Each fixed-j moment is continuous on the closed height interval,
including y=0. The zeroth normalized moment is identically one.
This is a conditional-on-L309 coefficient estimate, not an inequality
for an alternating Taylor section or a Fourier transform. There is
no asserted positive gap uniform in j or in the pair of heights.

## Proof

### Imported ordering result and scope of the specialization

Use L. Dümbgen and A. Mösching, *On Stochastic Orders and Total
Positivity*, [arXiv:2209.07868v3](https://arxiv.org/pdf/2209.07868v3),
posted 7 March 2023, PDF dated 8 March 2023, Theorem 1 and Remark 4,
printed pp. 2–3; the relevant ratio-to-product and integral proof
steps are Steps 1–2 on p. 11. For Borel probability measures with
densities relative to a sigma-finite measure, an increasing density
ratio gives likelihood-ratio order, which implies stochastic order.
Here the common dominating measure is Lebesgue measure and the
densities are positive on (0,infinity), extended by zero elsewhere.
All normalizers and moments required below are verified explicitly.

The cited theorem supplies weak order. It does not state the present
theta/sinhc application or its strictness. Only those points are
developed below; the general ordering theorem and L309's curvature
calculation are not reproved. This is a specialization of established
methods, with no certified novelty claim.

### Conditional moments and the exact change of variables

Set u=s+t and v=s-t. Thus p=2s, q=2t and du dv=2 ds dt. Write

\[
 Q_s(t)=k(s+t)k(s-t),\quad Z(s)=\int_{\mathbb R}Q_s(t)\,dt,
 \quad h_j(s)=\frac{\int_{\mathbb R}t^{2j}Q_s(t)\,dt}{Z(s)}.
\]

The mass Z(s) is finite and positive for every real s. Every h_j(s)
is finite, positive, continuous and even in s. Positivity follows from
k>0 and the positive density away from t=0; evenness follows from
k(-u)=k(u). The locally uniform, polynomially weighted theta bounds
in L309 justify continuity and finiteness of these integrals. Explicitly,
on |s|<=S both |s+t| and |s-t| are at least |t|-S. L019's
superexponential bound, with k bounded on compact sets, therefore
dominates Q_s(t) times every fixed polynomial in t uniformly on that
s interval by an integrable function. Dominated convergence applies. In
particular h_0=1. We do not need to differentiate an improper integral.

For each fixed j, L898's domination bounds the absolute integrand
defining A_{2j}(y), uniformly for 0<=y<=1/2, by

\[
       p^2|q|^{2j}e^{|p|/2}\Phi(u)\Phi(v).
 \tag{2}
\]

This is integrable: L019's decay makes every integral of
(1+|u|)^d e^{B|u|}Phi(u) finite for fixed d,B, while
|p|,|q|<=|u|+|v|. Thus Tonelli/Fubini and the change of variables
are legitimate. Before reducing to s>0, the prefactor is
4 * 2^(2j) * (1/4) * 2 = 2^(2j+1); the four factors come from
p^2, q^(2j), the two Phi factors and the Jacobian, respectively.
Evenness in s gives the remaining factor two. Thus

\[
 A_{2j}(y)=2^{2j+2}\int_0^\infty
          s^2\operatorname{sinhc}(2ys)Z(s)h_j(s)\,ds.
 \tag{3}
\]

Define

\[
 N_y=\int_0^\infty s^2\operatorname{sinhc}(2ys)Z(s)\,ds
      =A_0(y)/4,
 \qquad
 d\mu_y(s)=\frac{s^2\operatorname{sinhc}(2ys)Z(s)}{N_y}\,ds.
\]

Here 0<N_y<infinity; mu_y has positive density throughout (0,infinity).
Equation (3) becomes

\[
                  m_{2j}(y)=2^{2j}\int h_j(s)\,d\mu_y(s).
 \tag{4}
\]

### The conditional difference law moves inward strictly

Let P_s have density f_s(r)=2Q_s(r)/Z(s) on r>0, the law of |t|
under Q_s/Z(s). For 0<=s_1<s_2 define R(r)=f_{s_2}(r)/f_{s_1}(r).
Its normalizing constant is independent of r. Ordinary differentiation
at fixed finite coordinates and the fundamental theorem of calculus
give

\[
 \frac{d}{dr}\log R(r)
 =-\int_{s_1}^{s_2}
       [V''(\sigma+r)-V''(\sigma-r)]\,d\sigma<0,
 \qquad r>0.
 \tag{5}
\]

Indeed V'' is even and strictly increasing on [0,infinity), by the
imported V'''>0 on (0,infinity). For sigma,r>0,
|sigma+r|>|sigma-r|, so the integrand is strictly positive. If s_1=0,
it vanishes only at sigma=0 and is positive on (0,s_2); the integral
is still strictly positive. Smooth evenness handles sigma=r without
any reflection cusp. Thus R is strictly decreasing. The cited ordering
criterion gives P_{s_2}<=lr P_{s_1} and consequently the same weak
stochastic order.

For the required strict polynomial comparison, put g(r)=r^(2j), j>=1.
Under P_{s_1}, E[R]=1, E[g]=h_j(s_1), and E[gR]=h_j(s_2), all finite.
Expanding the following absolutely integrable double integral yields

\[
 h_j(s_2)-h_j(s_1)
 =\frac12\iint(g(r)-g(r'))(R(r)-R(r'))
                         \,dP_{s_1}(r)\,dP_{s_1}(r')<0.
 \tag{6}
\]

Absolute integrability follows by bounding the integrand's absolute
value by (g(r)+g(r'))(R(r)+R(r')); its integral is
2h_j(s_2)+2h_j(s_1). The integrand in (6) is strictly negative whenever
r!=r', because g increases strictly and R decreases strictly.
The positive continuous density has no atoms, so that set has full
product measure. Hence h_j decreases strictly on [0,infinity), and
0<h_j(s)<=h_j(0)<infinity. This last bound will also control the next
change of probability law.

### The height law moves outward strictly

For 0<=y_1<y_2<=1/2 the Radon–Nikodym ratio is

\[
 T(s)=\frac{d\mu_{y_2}}{d\mu_{y_1}}(s)
     =\frac{N_{y_1}}{N_{y_2}}
       \frac{\operatorname{sinhc}(2y_2s)}
            {\operatorname{sinhc}(2y_1s)},\qquad s>0.
\]

To determine its direction, use [NIST DLMF 4.36.3](https://dlmf.nist.gov/4.36.E3), version 1.2.8, released
15 September 2026. At positive real a its partial-fraction formula
gives

\[
 F(a):=a\coth a=1+2\sum_{n\ge1}\frac{a^2}{a^2+\pi^2n^2}.
 \tag{7}
\]

The cited domain excludes a=n*pi*i; no positive real a is excluded.
On every bounded interval 0<=a<=M, the summands are bounded by
M^2/(pi^2 n^2). The series therefore defines a continuous extension
F(0)=1. Each summand increases with a>=0, strictly for any two distinct
nonnegative arguments, so F is strictly increasing on [0,infinity).
No differentiation of the series is being used.

For y>0, direct differentiation of sinhc gives

\[
 \frac{d}{ds}\log\operatorname{sinhc}(2ys)
                =\frac{F(2ys)-1}{s}.
\]

For y=0 the left side is zero and the same expression holds using
F(0)=1. Consequently, including the case y_1=0,

\[
          \frac{d}{ds}\log T(s)
            =\frac{F(2y_2s)-F(2y_1s)}{s}>0.
 \tag{8}
\]

Thus T increases strictly; the cited criterion gives
mu_{y_1}<=lr mu_{y_2}, hence the corresponding stochastic order.
Under mu_{y_1}, E[T]=1 and 0<h_j<=h_j(0). Expanding the two-copy
identity as in (6), now with h_j strictly decreasing and T strictly
increasing, proves

\[
 \int h_j\,d\mu_{y_2}-\int h_j\,d\mu_{y_1}
 =\frac12\iint(h_j(s)-h_j(s'))(T(s)-T(s'))
                      \,d\mu_{y_1}(s)\,d\mu_{y_1}(s')<0.
 \tag{9}
\]

The integrand is absolutely integrable, since h_j is bounded and
T has mean one. It is strictly negative off the diagonal, which has
zero product measure. Equation (4) now proves (1).

### Endpoints and unpaid signs

The proof compared y_1=0 directly in (8)–(9); it did not infer strict
endpoint order from continuity of weak inequalities. For completeness,
(2), continuity of sinhc, and dominated convergence show that every
A_{2j} is continuous on [0,1/2]. Also A_0(y)>=A_0(0)>0, since sinhc
is at least one on the real line. Division proves the stated continuity
of m_{2j}, including its y=0 limit. The upper endpoint y=1/2 is included
in the same dominator. All statements are for arbitrary but fixed j;
no estimate uniform in j or infinite degree interchange is required.

The two ratio directions and strictness pass the nominated test. They
permit ordered coefficient envelopes on height cells. Cosine is not
an increasing function of |q| on its full support, and alternating
coefficients cannot be signed termwise using (1). L312's conditional
cosine obstruction and L898's fixed cross-endpoint stop are unchanged;
they are contrasts, not inputs to (1). Signed margins, quantitative
height refinement, unbounded frequency coverage and the L030–L032/C032a
all-degree mixed positivity gap remain open. No zero information was
used and no RH candidate is claimed. The separate scoped audit of
8 November 2026 (step128) verified (3)–(9), including strictness at
s_1=0 and y_1=0, both two-copy integrability bounds and fixed-j
closed-height domination. It found no error in this application;
the inherited L309 arithmetic qualification remains unverified by
that audit. ∎

## Mathlib

Full matching coverage is not checked; availability is unknown.
No specific Mathlib theorem for the supporting likelihood-ratio order,
strict covariance comparison or hyperbolic identity has been identified.
The primary sources above establish the named standard inputs, not a
formal verification of this application or of L309's certificate.
