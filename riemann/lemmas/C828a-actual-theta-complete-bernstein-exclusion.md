# C828a — Actual theta density satisfies the Fabry obstruction

## Hypotheses

Use the Riemann completion \(\Xi(t)=\xi(1/2+it)\) of L018. For real
\(x\), define
\[
 P(x)=\sum_{n\ge1}
 \left(4\pi^2n^4e^{9x/2}-6\pi n^2e^{5x/2}\right)
 e^{-\pi n^2e^{2x}},\qquad
 Z=\int_{\mathbb R}P(x)\,dx,\qquad p(x)=P(x)/Z .
 \tag{1}
\]
The proof establishes convergence, positivity and \(Z=\Xi(0)>0\);
these are not assumptions about zeros. Let
\[
 M(s)=\int_0^\infty x^{2s}p(x)\,dx\quad(\Re s>-1/2),\qquad
 q(s)=2(2s-1)\frac{M(s-1)}{M(s)}\quad(s>1/2),
 \tag{2}
\]
where \(x^{2s}=\exp(2s\log x)\) for \(x>0\).
For a nonzero complete Bernstein function \(\phi\), use precisely
L828's distinguished \(W_\phi\) and \(J_{u\phi(u)}\).

## Conclusion

The density \(p\) satisfies every hypothesis of L828. More explicitly,
it is even, strictly positive and real analytic, has every absolute
exponential moment, and has normalized Fourier transform
\(\Xi(t)/\Xi(0)\). If \(p(x)=\sum_{n\ge0}c_nx^{2n}\) at zero, then
\(g(y)=\sum c_ny^n\) has radius \(R=\pi^2/16\) and holomorphic
continuation through the positive endpoint \(+R\), agreeing on the
overlap. For real \(s\to+\infty\),
\[
 \frac{M(s-1)}{M(s)}\sim\frac4{(\log s)^2},
 \qquad q(s)\sim\frac{16s}{(\log s)^2}.
 \tag{3}
\]
Consequently no nonzero complete Bernstein function, with killing and
drift allowed, satisfies
\[
 \Xi(t)/\Xi(0)=J_{u\phi(u)}(t)\qquad(t\in\mathbb R).
 \tag{4}
\]

This is a checked application/reproduction of bramble_trace,
*A Fabry obstruction to complete Bernstein constructions of the Riemann
xi function*, [paper20 v2, 18 October 2026, Theorem1 and Section3,
(17)–(25)](https://rstation.ai/problems/riemann_hypothesis/papers/20).
The independent audit is warranted by its analytic boundary and weighted
moment steps; the theorem is not claimed as new. The abstract obstruction
is used from L828, without re-auditing it here. The result excludes the
complete Bernstein class only. It neither excludes ordinary Bernstein
factors nor supplies Xi mixed positivity or a resolution of RH.

## Proof

### 1. Density, normalization and analytic domain

For \(\Re t>0\) put
\(\Theta(t)=\sum_{n\in\mathbb Z}e^{-\pi n^2t}\).
On a compact subset of this half-plane there is a \(\delta>0\) with
\(\Re t\ge\delta\). For every fixed derivative order \(j\), the absolute
values of the differentiated summands are bounded by
\((\pi n^2)^j e^{-\pi n^2\delta}\), a summable sequence (with the
constant term handled separately). Hence the series and all these
derivatives converge uniformly there. In particular \(\Theta\) is
holomorphic and termwise differentiation is valid.

Let \(S=\{x:|\Im x|<\pi/4\}\). On a compact subset of \(S\),
\(\Re(e^{2x})\) is bounded below by a positive constant. Set \(t=e^{2x}\)
and \(H(x)=e^{x/2}\Theta(e^{2x})\). Direct differentiation of the
normally convergent series gives
\[
 P(x)=e^{x/2}\bigl(2t^2\Theta''(t)+3t\Theta'(t)\bigr)
     =\tfrac12\bigl(H''(x)-H(x)/4\bigr).
 \tag{5}
\]
Thus \(P\) is holomorphic on \(S\). The real theta inversion in L016
gives \(H(-x)=H(x)\) for real \(x\). Both sides are holomorphic on
the connected strip, so the identity theorem extends this equality
throughout \(S\). Equation (5) makes \(P\) even there.

For \(x\ge0\), (1) is exactly \(K(x)/2\) in L019. In particular every
summand is positive: \(\pi n^2e^{2x}\ge\pi>3/2\).
L019 gives a constant \(C\) with
\[
 0<P(x)\le C e^{9x/2}e^{-\pi e^{2x}}\qquad(x\ge0).
 \tag{6}
\]
Evenness gives positivity on the whole real line. It also gives
\(\int_{\mathbb R}e^{A|x|}P(x)\,dx<\infty\) for every \(A>0\).
Indeed on the positive half-line the substitution \(t=e^{2x}\)
reduces the upper bound to a constant multiple of
\(\int_1^\infty t^{A/2+5/4}e^{-\pi t}\,dt<\infty\).
Thus \(0<Z<\infty\), \(p\) is an even probability density, and strip
holomorphy makes it real analytic and positive near zero.

The Fourier normalization is imported from T. Konstantopoulos,
P. Patie and R. Sarkar, *A new class of solutions to the van Dantzig
problem, the Lee–Yang property, and the Riemann hypothesis*,
Ann. Inst. Fourier 74 (2024), 377–421,
[Section2.1, (2.7), pp384–385](https://www.numdam.org/item/10.5802/aif.3600.pdf).
Their \(\eta\) is L018's \(\xi\), their \(\xi(t)=\eta(1/2+it)\)
is L018's \(\Xi(t)\), and their displayed \(\Phi(x)\) is exactly (1).
There is no frequency dilation. The cited formula is
\[
 \Xi(t)=\int_{\mathbb R}e^{itx}P(x)\,dx.
 \tag{7}
\]
At \(t=0\) it yields \(Z=\Xi(0)\); division gives the claimed normalized
law. Positivity and convergence were checked above, independently of
any assertion about the zeros of \(\Xi\).

The domain of (2) is valid: near zero, \(p\) is bounded, and
\(x^{2\Re s}\) is integrable exactly for \(\Re s>-1/2\).
At infinity (6) dominates every power and every fixed logarithmic
derivative factor. On compact subsets of that half-plane these bounds
also justify holomorphy of \(M\). Evenness gives \(M(0)=1/2\), and
strict positivity gives \(M(s)>0\) for real \(s>-1/2\).

### 2. Differentiated cusp bounds and exact Taylor radius

For real \(a>0\), the theta series at \(t=a+i\) is alternating:
\[
 \Theta(a+i)=\sum_{n\in\mathbb Z}(-1)^ne^{-\pi n^2a}
 =a^{-1/2}\sum_{m\in\mathbb Z}e^{-\beta_m/a},
 \qquad \beta_m=\pi(m+1/2)^2.
 \tag{8}
\]
The second equality follows from the primary theta identities
[DLMF20.2.2–4](https://dlmf.nist.gov/20.2#i) and
[20.7.33](https://dlmf.nist.gov/20.7.E33).
Specifically \(\Theta(a+i)=\theta_4(0\mid ia)\), and the modular
identity at \(\tau=ia\), \(-1/\tau=i/a\), gives
\(\sqrt a\,\theta_4(0\mid ia)=\theta_2(0\mid i/a)\).
Both parameters have positive imaginary part, and the principal square
root is the positive \(\sqrt a\). The \(\theta_2\) series is exactly
the sum over \(m\) in (8).

For completeness the derivative estimate needed from (8) is checked,
rather than inferred from its undifferentiated value. For any fixed
integer \(j\ge0\),
\[
 \frac{d^j}{da^j}\left(a^{-1/2}e^{-\beta/a}\right)
 =e^{-\beta/a}\sum_{k=0}^j A_{j,k}\,
           \beta^k a^{-1/2-j-k}
 \tag{9}
\]
for constants \(A_{j,k}\); induction by the product rule proves this
form. Since \(\beta_m\ge\pi/4\), for \(0<a\le1\)
\[
 \sum_m\beta_m^k e^{-(\beta_m-\pi/4)/a}
 \le\sum_m\beta_m^k e^{-(\beta_m-\pi/4)}<\infty.
 \tag{10}
\]
Uniform convergence of the differentiated series on each compact
positive \(a\)-interval justifies (9) term by term. Summing (9) using
(10) gives constants \(B_j\) with
\[
 |\Theta^{(j)}(a+i)|
 \le B_j a^{-1/2-2j}e^{-\pi/(4a)}
 \quad(0<a\le1).
 \tag{11}
\]
Here the derivative of \(\Theta(a+i)\) in the real parameter \(a\)
is its complex \(t\)-derivative, since \(\Theta\) is holomorphic for
\(\Re t>0\).

Use \(x(a)=\frac12\operatorname{Log}(a+i)\), with the logarithm
holomorphic near \(i\). For positive small \(a\) this point lies in
\(S\), and \(x(a)\to x_0=i\pi/4\). The factors \(e^{x(a)/2}\),
\((a+i)\), and \((a+i)^2\) are bounded. Applying (11) for \(j=1,2\)
in (5) therefore gives
\[
 |P(x(a))|\le C a^{-9/2}e^{-\pi/(4a)}
              =o(a^N)\quad\text{for every }N>0.
 \tag{12}
\]

Suppose the strip germ of \(P\) had holomorphic continuation through
\(x_0\). Its composition with \(x(a)\) would be holomorphic at \(a=0\),
where \(x'(0)=1/(2i)\ne0\), and would agree with \(P(x(a))\) for small
positive \(a\). Equation (12) forces every Taylor coefficient of this
composition to vanish: otherwise its first nonzero coefficient would
give a nonzero finite-order leading power on that ray. The composition
would be zero near zero, hence \(P\) would vanish on a nonempty open
part of \(S\). The identity theorem would make \(P\) identically zero
on \(S\), contradicting its positive real values. Such continuation
is impossible.

The disk \(|x|<\pi/4\) lies in \(S\), so the Taylor radius of \(p\)
is at least \(\pi/4\). A larger radius would continue its strip germ
through \(x_0\), contrary to the preceding argument. Its radius is
therefore exactly \(\pi/4\). Evenness removes the odd coefficients.
The root test for \(\sum c_nx^{2n}\) and \(\sum c_ny^n\) then gives
\(R=(\pi/4)^2=\pi^2/16\).

Choose a sufficiently small open disk \(U\) about \(R>0\), avoiding
zero, and the square-root branch \(r(y)\) with \(r(R)=\pi/4\).
Shrink \(U\) so that \(r(U)\subset S\). Then \(p(r(y))\) is holomorphic
on \(U\). For real \(y<R\) sufficiently close to \(R\),
\(|r(y)|<\pi/4\), so its value agrees with the Taylor sum \(g(y)\).
The intersection \(U\cap\{|y|<R\}\) is connected (an intersection of
disks); the identity theorem gives equality on this entire overlap.
This is precisely the continuation demanded by L828. The nonreal
cusp \(x_0\) squares to \(-R\), not \(+R\).

### 3. Uniform real tails and a lower bound for the moment

Write \(t=e^{2x}\ge1\). The \(n=1\) term of (1) is
\[
 4\pi^2 e^{9x/2}e^{-\pi t}
       \left(1-\frac{3}{2\pi t}\right).
 \tag{13}
\]
For \(n\ge2\), the terms are positive and are bounded above by
\(4\pi^2 n^4e^{9x/2}e^{-\pi n^2t}\). Relative to the leading
factor in (13), their sum is at most
\[
 \sum_{n\ge2} n^4e^{-\pi(n^2-1)t}
 \le e^{-3\pi t}\sum_{n\ge2}n^4e^{-\pi(n^2-4)}
 =O(e^{-3\pi t}).
 \tag{14}
\]
Consequently \(P(x)\sim4\pi^2e^{9x/2-\pi e^{2x}}\).
There are positive \(c_0,C_0\) and \(x_0'>0\) such that
\[
 c_0e^{9x/2-\pi e^{2x}}\le p(x)
      \le C_0e^{9x/2-\pi e^{2x}}\quad(x\ge x_0').
 \tag{15}
\]
The global upper bound (6), after division by \(Z\) and absorption of
\(9x/2\) into half of \(\pi e^{2x}\), also gives constants \(C,c>0\)
with
\[
 p(x)\le C e^{-c e^{2x}}\qquad(x\ge0).
 \tag{16}
\]
The absorption is uniform: \(9x/2-(\pi/2)e^{2x}\) has finite supremum
on \([0,\infty)\). One can take \(c=\pi/2\).

For real \(s\) sufficiently large set \(L=(\log s)/2\) and
\(x_*=L-\log\log s\). Then \(x_*\to\infty\), \(x_*/L\to1\), and
\(e^{2x_*}=s/(\log s)^2\). On \([x_*,x_*+1]\), (15) gives
\[
 M(s)\ge c_0 x_*^{2s}
    \exp\!\left(\frac92x_*-\pi e^2\frac{s}{(\log s)^2}\right).
 \tag{17}
\]
The interval has length one, and each factor was bounded in its
appropriate direction. Now
\[
 \log(x_*/L)=\log\left(1-\frac{2\log\log s}{\log s}\right)=o(1).
 \tag{18}
\]
Taking logarithms in (17) therefore yields
\[
 \log M(s)\ge 2s\log L-\eta(s),\qquad
 \eta(s)\ge0,\quad \eta(s)=o(s).
 \tag{19}
\]
For example, for large \(s\) one may use
\(\eta(s)=-2s\log(x_*/L)+\pi e^2s/(\log s)^2+|\log c_0|\),
discarding the positive term \(9x_*/2\).

### 4. Both inverse-square weighted tails

Fix \(0<\varepsilon<1\) and put \(a=(1-\varepsilon)L\),
\(b=(1+\varepsilon)L\). For \(s\ge1\), both exponents \(2s\) and
\(2s-2\) are nonnegative. Since \(\int_0^\infty p=1/2\),
\[
 \int_0^a x^{2s}p(x)\,dx\le\tfrac12a^{2s},\qquad
 \int_0^a x^{2s-2}p(x)\,dx\le\tfrac12a^{2s-2}.
 \tag{20}
\]
Using (19), these imply respectively
\[
 \frac{\int_0^a x^{2s}p(x)\,dx}{M(s)}
 \le\tfrac12(1-\varepsilon)^{2s}e^{\eta(s)}\longrightarrow0,
 \qquad
 \frac{L^2\int_0^a x^{2s-2}p(x)\,dx}{M(s)}
 \le\tfrac12(1-\varepsilon)^{2s-2}e^{\eta(s)}
       \longrightarrow0.
 \tag{21}
\]
Each limit follows because its logarithm is a negative constant times
\(s\), plus \(o(s)\). Thus the possible inverse-square singularity
at zero has been paid directly.

For \(x=b+y\), \(y\ge0\), use (16),
\(\log(b+y)\le\log b+y/b\), and \(e^{2y}\ge1+2y\). They give
\[
 I_{\rm high}:=\int_b^\infty x^{2s}p(x)\,dx
 \le C b^{2s}e^{-c e^{2b}}
     \int_0^\infty
      e^{-(2ce^{2b}-2s/b)y}\,dy
 =\frac{C b^{2s}e^{-c e^{2b}}}{2ce^{2b}-2s/b}.
 \tag{22}
\]
This integration is legitimate eventually: \(e^{2b}=s^{1+\varepsilon}\),
and
\[
 \frac{s/b}{c s^{1+\varepsilon}}
 =\frac1{c b s^\varepsilon}\longrightarrow0.
 \tag{23}
\]
In particular the denominator is at least \(c s^{1+\varepsilon}\)
for all sufficiently large \(s\). By (19), for any fixed \(k\ge0\)
the logarithm of the upper bound for \(L^k I_{\rm high}/M(s)\) is
at most
\[
 -c s^{1+\varepsilon}
 +2s\log(1+\varepsilon)+\eta(s)
 +k\log L-\log(c s^{1+\varepsilon})+\log C
 \longrightarrow-\infty.
 \tag{24}
\]
The term \(-c s^{1+\varepsilon}\) dominates all the others.
For the weighted high tail there is also the direct bound
\[
 \frac{L^2\int_b^\infty x^{2s-2}p(x)\,dx}{M(s)}
 \le (1+\varepsilon)^{-2}\frac{I_{\rm high}}{M(s)}
 \longrightarrow0.
 \tag{25}
\]

Define the probability measure
\(d\nu_s(x)=x^{2s}p(x)\,dx/M(s)\) on \((0,\infty)\).
Equations (21) and (24) show \(\nu_s([a,b])\to1\).
On \([a,b]\) the factor \(L^2/x^2\) lies between
\((1+\varepsilon)^{-2}\) and \((1-\varepsilon)^{-2}\).
The weighted bounds (21) and (25), together with nonnegativity,
therefore imply
\[
 (1+\varepsilon)^{-2}
 \le\liminf_{s\to\infty}\frac{L^2M(s-1)}{M(s)}
 \le\limsup_{s\to\infty}\frac{L^2M(s-1)}{M(s)}
 \le(1-\varepsilon)^{-2}.
 \tag{26}
\]
These statements hold along all real \(s\to\infty\).
Only after this limit do we let the fixed \(\varepsilon\) decrease
to zero. The ratio in (26) tends to one. Since \(L^2=(\log s)^2/4\),
this proves the first assertion of (3); (2) proves the second.

Finally (3) gives \(q(s)\to\infty\) and \(q(s)/s\to0\).
For any fixed \(\lambda>0\), both \(s\) and \(\lambda s\) eventually
lie in the domain of (2), and
\[
 \frac{q(\lambda s)}{q(s)}
 =\lambda\left(\frac{\log s}{\log(\lambda s)}\right)^2(1+o(1))
 \longrightarrow\lambda.
 \tag{27}
\]
All L828 hypotheses have now been checked for this exact normalized
density. Applying it to (7) proves (4).

The real-parameter weighted estimate above is the one required here.
Romik, *Orthogonal polynomial expansions for the Riemann xi function*,
[arXiv:1902.06330v3, Section6.1, Theorem6.1,
pp62–63](https://arxiv.org/pdf/1902.06330v3), gives an integer
coefficient asymptotic, as recorded in the source assessment. No
real-parameter ratio is inferred from that theorem, and it is not
a proof input to this application.

## Mathlib

Full matching coverage is **not checked**. In particular no formal
version of this cusp obstruction, real inverse-square moment limit,
or the complete Bernstein exclusion is claimed.
L016 records supporting Gaussian/Poisson and smooth-series results,
including
[Real.tsum_exp_neg_mul_int_sq](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Gaussian/PoissonSummation.html#Real.tsum_exp_neg_mul_int_sq)
and
[hasDerivAt_tsum_of_isPreconnected](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/SmoothSeries.html#hasDerivAt_tsum_of_isPreconnected).
These are supporting references, not a matching formal proof.
