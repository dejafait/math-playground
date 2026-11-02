# L618: Suzuki's complete kernels vanish in compact-window norm as the parameter grows

## Hypotheses

Use L018's completion
\(\xi(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)/2\).
For real \(\theta>1\), take the complete kernel \(K_\theta\) of
Masatoshi Suzuki, *Integral operators arising from the Riemann zeta
function*, [arXiv:1907.07302v2](https://arxiv.org/pdf/1907.07302v2)
(6 March 2020), equation (1.10) and Theorem 1.2 (K-ii), (K-iii),
printed pp.2–3. Precisely, it is continuous, vanishes for \(x<0\),
has \(K_\theta(x)=O_\theta(e^{x/2})\) as \(x\to+\infty\), and

\[
 \int_{\mathbb R}K_\theta(x)e^{izx}\,dx
 =\exp\!\left(-2\theta\frac{\xi'(s)}{\xi(s)}\right),
 \qquad s=\tfrac12-iz,\quad\Im z>\tfrac12.                 \tag{1}
\]

The derivative is with respect to \(s\). No bound on the implicit
growth constant uniform in \(\theta\) is assumed. These kernel
properties are imported from the stated theorem, not reproved.
Its local determinant conclusion (K-v) and the implicit constants
in (3.14) are not inputs to the estimate below.

For \(t\ge0\), let \(K_\theta[t]\) act on
\(L^2(({-\infty},t),dx)\) by Suzuki's equation (1.1):

\[
 (K_\theta[t]f)(x)
 =\mathbf1_{x<t}\int_{-\infty}^t K_\theta(x+y)f(y)\,dy.      \tag{2}
\]

Open or closed endpoints do not change this \(L^2\) operator.
Fix a finite real \(T>0\).

## Conclusion

For every real \(\theta\ge2\),

\[
 \boxed{\quad
 \sup_{0\le t\le T}\|K_\theta[t]\|_{L^2\to L^2}
 \le 16T e^{31T}\left(\frac{28}{41}\right)^\theta.
 \quad}                                                       \tag{3}
\]

In particular the left side tends to zero as \(\theta\to+\infty\)
for each fixed \(T\). This is a parameter specialization of known
kernel and digamma representations, with explicit uniform estimates;
no originality beyond the checked sources is asserted. It neither
establishes a fixed-\(\theta\) all-window contraction nor controls
Xi's mixed signs. RH is not an assumption or a conclusion.

## Proof

### 1. An absolute bound for the complete arithmetic factor

L001 gives nonvanishing of \(\zeta\) on \(\Re s>1\).
Differentiate L005's holomorphic Euler logarithm there. On
\(\Re s\ge1+\delta\), \(\delta>0\), its derivative series has majorant

\[
 \sum_p\sum_{k\ge1}(\log p)p^{-k(1+\delta)}
 =\sum_{n\ge2}\Lambda(n)n^{-1-\delta}
 \le\sum_{n\ge2}(\log n)n^{-1-\delta}<\infty.              \tag{4}
\]

Here \(\Lambda(p^k)=\log p\) and \(\Lambda(n)=0\) otherwise;
unique factorization justifies the regrouping. The last convergence
follows from the integral test, with eventual monotonicity. Thus the
derivative series converges locally uniformly absolutely. Termwise
holomorphic differentiation and \(\exp L=\zeta\) give

\[
 \frac{\zeta'}{\zeta}(s)
 =-\sum_{n\ge2}\Lambda(n)n^{-s},\qquad \Re s>1.            \tag{5}
\]

On the fixed line \(s=16-iu\), \(u\in\mathbb R\), use
\(\Lambda(n)\le\log n\le n\) to obtain

\[
 \left|\frac{\zeta'}{\zeta}(16-iu)\right|
 \le\sum_{n\ge2}n^{-15}
 \le\int_1^\infty x^{-15}\,dx=\frac1{14}.                 \tag{6}
\]

The sum-integral comparison holds on every \([n-1,n]\) by
monotonicity. This treats the entire arithmetic factor before
exponentiation; no Dirichlet-series truncation is involved.

### 2. A digamma estimate with explicit constants

Use [DLMF 5.9.13](https://dlmf.nist.gov/5.9.E13), valid for
\(\Re w>0\) with the principal logarithm:

\[
 \psi(w)=\log w-\int_0^\infty h(v)e^{-wv}\,dv,
 \qquad h(v)=\frac1{1-e^{-v}}-\frac1v.                    \tag{7}
\]

For every \(v>0\), \(0<h(v)<1\). The lower inequality follows from
\(1-e^{-v}<v\); the upper follows from
\(h(v)=1+(e^v-1)^{-1}-v^{-1}\) and \(e^v-1>v\).
For \(a=\Re w>0\), the integral is therefore absolutely convergent,
and

\[
 |\psi(w)-\log w|\le\int_0^\infty e^{-av}\,dv=\frac1a,
 \qquad \Re\psi(w)\ge\log|w|-\frac1a.                   \tag{8}
\]

In particular \(w=s/2\), \(\Re s=16\), has \(a=8\).
Equations (6) and (8) hold for every real \(u\), independently of
\(\theta\), before exponentiation.

### 3. A uniformly integrable full multiplier

Logarithmic differentiation of L018's product gives on this line

\[
 \frac{\xi'}{\xi}(s)
 =\frac1s+\frac1{s-1}-\frac12\log\pi
   +\frac12\psi(s/2)+\frac{\zeta'}{\zeta}(s).              \tag{9}
\]

There is no zero or pole on the line. The rational real parts are
positive because \(\Re s=16>1\). Retaining these terms in (9)
and bounding their real parts below by zero, (6) and (8) yield

\[
 \Re\frac{\xi'}{\xi}(16-iu)
 \ge\frac12\log\frac{|16-iu|}{2\pi}-\frac1{16}-\frac1{14}.
                                                               \tag{10}
\]

Set \(c=31/2\) and
\(F_\theta(u)=\exp(-2\theta\xi'(16-iu)/\xi(16-iu))\).
Thus \(16-iu=1/2-i(u+ic)\). Multiplying (10) by \(-2\theta\)
and exponentiating gives

\[
 |F_\theta(u)|
 \le q^\theta(1+(u/16)^2)^{-\theta/2},
 \qquad q=\frac\pi8\exp\!\left(\frac{15}{56}\right).
                                                               \tag{11}
\]

All gamma, rational and arithmetic factors of (1) are included.
For \(0\le x<1\), comparison of nonnegative power series gives
\(e^x\le(1-x)^{-1}\). Also
\(\pi/4=\int_0^1(1+x^2)^{-1}dx<1\). Consequently

\[
 q\le\frac\pi8\frac{56}{41}
 =\frac{7\pi}{41}<\frac{28}{41}=:r<1.                    \tag{12}
\]

For \(\theta\ge2\), (11) therefore implies

\[
 \int_{\mathbb R}|F_\theta(u)|\,du
 \le r^\theta\int_{\mathbb R}\frac{du}{1+(u/16)^2}
 =16\pi r^\theta.                                       \tag{13}
\]

No printed fixed-parameter big-O constant has been promoted to a
uniform constant.

### 4. Weighted Fourier inversion and support compression

For each fixed \(\theta\ge2\), put
\(k_\theta(x)=e^{-cx}K_\theta(x)\). The imported continuity,
causality and fixed-parameter growth give \(k_\theta\in L^1(\mathbb R)\):
it vanishes for negative \(x\), is bounded on compact sets, and has
tail \(O_\theta(e^{-15x})\). Uniformity of this last constant is
not needed. On \(z=u+ic\), (1) identifies its Fourier transform,
in the convention

\[
 \widehat k_\theta(u)=\int_{\mathbb R}k_\theta(x)e^{iux}\,dx
 =F_\theta(u).
\]

Both \(k_\theta\) and its transform are in \(L^1\), by this argument
and (13). The standard \(L^1\) Fourier inversion theorem applies
at every continuity point, here every real \(x\), and gives

\[
 K_\theta(x)=\frac{e^{cx}}{2\pi}
       \int_{\mathbb R}F_\theta(u)e^{-iux}\,du,
 \qquad |K_\theta(x)|\le8e^{cx}r^\theta.                 \tag{14}
\]

This inverts the known kernel on a zero-free line; no contour shift
or unweighted global isometry is used. The new explicit bound is
independent of the unspecified growth constant used only to justify
integrability.

For \(t>0\), if \(x<-t\), \(y<t\), then \(x+y<0\);
similarly if \(y<-t\), \(x<t\). Thus causality makes (2)
zero outside the input/output square \([-t,t]^2\), up to null
endpoints. A nonzero kernel on the square has \(0\le x+y\le2t\),
so its absolute value is at most \(8e^{2ct}r^\theta\) by (14).
The restricted kernel is square integrable. The Hilbert--Schmidt
inequality, or Cauchy--Schwarz in \(y\) followed by integration in
\(x\), gives

\[
 \begin{aligned}
 \|K_\theta[t]\|_{L^2\to L^2}
 &\le\left(\int_{-t}^t\int_{-t}^t
                  |K_\theta(x+y)|^2\,dy\,dx\right)^{1/2}\\
 &\le2t\,8e^{2ct}r^\theta=16t e^{31t}r^\theta.
 \end{aligned}                                             \tag{15}
\]

This holds on the original infinite input space because the operator
ignores the part outside \([-t,t]\), and restriction has norm at
most one. For \(t=0\) the operator is zero, since \(x+y<0\)
almost everywhere in its domain. Finally \(t e^{31t}\le T e^{31T}\)
on \([0,T]\). This proves (3); its limit follows from \(0<r<1\)
with \(T\) fixed. ∎

### Qualifications and downstream use

The local advance is (3), not the known construction of Suzuki's
kernel. It uses only the absolutely convergent Euler half-plane,
not a newer zero-free manuscript or an RH-equivalent sign premise.
Its exponential window cost is explicit. Its quantifiers are
\(\forall T\ \lim_{\theta\to\infty}\sup_{t\le T}=0\);
it does not control all \(t\) for one fixed \(\theta\), give kernel
signs, or transfer any sign to Xi. It diagnoses why small operators
on each tested window after changing the smoothing parameter leave
the fixed-parameter global problem open. Mixed signs, realization
and terminal/zero-time limits remain independent unresolved gaps.
No scaling-law conclusion is claimed.

Only the source properties in the hypotheses are imported. This
calculation is not an independent audit of Suzuki's full manuscript
or its printed (3.14). The separate local critical review below verifies
the stated specialization, conditional only on the cited standard inputs.

### Independent audit (2026-11-01)

**Result: pass for exactly (3).** No correction to the inequality or
its hypotheses was needed. This review establishes the existing estimate
as a checked local input; it adds no stronger bound or new sign theorem.

The primary statements were directly checked again: Suzuki v2, printed
pp.1–3, (1.1), (1.10), Theorem 1.2 (K-ii)/(K-iii), use precisely this
completion, Fourier sign, real parameter range and causal operator.
The theorem assumes only real \(\theta>1\), not RH. Its growth constant
may depend on \(\theta\). DLMF 5.9(ii)'s domain heading and 5.9.13
give (7) with the principal logarithm on \(\Re w>0\). No theorem about
global determinant nonvanishing, innerness or signs is imported.

1. **Derivative and arithmetic part.** For each \(\delta>0\),
   \(\sum_{n\ge2}(\log n)n^{-1-\delta}\) converges and dominates
   every differentiated prime-power term on the stated closed half-plane.
   Together with L005's locally uniform original series this permits
   termwise holomorphic differentiation. L001 gives nonvanishing needed
   for the quotient. The comparison in (6) is in the correct direction:
   \(n^{-15}\le\int_{n-1}^n x^{-15}dx\). No finite prime truncation or
   unjustified differentiation is used.
2. **Signs and constants before exponentiation.** The elementary bounds
   \(0<h(v)<1\) make the integral in (7) absolutely convergent and
   give the uniform error \(1/8\) at \(w=8-iu/2\). The coefficient
   \(1/2\) in (9) changes this to a loss \(1/16\).
   The rational real parts are \(16/(256+u^2)>0\) and
   \(15/(225+u^2)>0\); dropping them is a valid lower bound.
   The arithmetic real part is at least \(-1/14\). Thus multiplying
   the total loss by \(2\theta\) gives
   \(2\theta(1/16+1/14)=15\theta/56\), exactly as in (11).
   Since \(1-15/56=41/56\), (12)'s elementary exponential bound
   gives \(q<28/41\). All factors are accounted for before raising
   to any real \(\theta\ge2\); there is no complex-power branch issue.
3. **Integrability and inversion.** The envelope in (11) is bounded
   by \(r^\theta/(1+(u/16)^2)\) for every real \(\theta\ge2\),
   whose integral is \(16\pi r^\theta\). In particular the endpoint
   \(\theta=2\) is integrable. With \(c=31/2\),
   \(s=1/2-i(u+ic)=16-iu\) and \(e^{i(u+ic)x}=e^{-cx}e^{iux}\).
   Causality, continuity and imported growth give the weighted function
   an integrable tail \(O_\theta(e^{-15x})\), with no negative tail.
   Both function and transform are therefore in \(L^1\) for each
   fixed parameter. Fourier inversion gives equality at every real
   \(x\) by continuity, with constant \((2\pi)^{-1}\); the kernel
   bound is consequently \(8e^{cx}r^\theta\). The unspecified source
   constant disappears because it is used only for membership in
   \(L^1\), not to estimate the inverse integral.
4. **Infinite space and endpoints.** For \(x,y<t\), either
   \(x<-t\) or \(y<-t\) forces \(x+y<0\), so the original operator
   ignores the input on \(({-\infty},-t)\) and vanishes there in its
   output. On the remaining square, the kernel bound uses only
   \(0\le x+y\le2t\). Its area is \(4t^2\), so the square root
   in the Hilbert--Schmidt estimate gives \(2t\), yielding (15).
   Restriction and extension by zero have norms at most one on the
   original space. At \(t=0\), \(x,y<0\) gives the zero operator;
   open/closed boundary choices differ only on null sets. Continuity
   and negative-support vanishing also imply \(K_\theta(0)=0\).
5. **Quantifiers and relevance.** For each fixed finite \(T>0\),
   the right side of (3) tends to zero because \(0<r<1\).
   Its factor \(Te^{31T}\) is unbounded as \(T\to\infty\), so this
   upper estimate supplies no all-window contraction for any fixed
   \(\theta\). An unbounded upper estimate does not prove that the
   actual norms grow or that global contraction fails. The audit
   neither changes the parameter order nor yields actual-Xi mixed
   signs, collision exclusion, realization or a terminal limit.

The direct mathematical inputs remain exactly L001/L005/L018. The
existing DAG row therefore requires no change. This is an informal
audit of a known-source specialization, not an audit of the imported
kernel construction or a formal verification.

## Mathlib

Full Suzuki-kernel and compact-window parameter-limit coverage has
not been checked; availability is unknown. L001/L005 retain supporting
Euler-product/nonvanishing coverage, including
`riemannZeta_ne_zero_of_one_lt_re` and
[`riemannZeta_eulerProduct_exp_log`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/EulerProduct/DirichletLSeries.html#riemannZeta_eulerProduct_exp_log).
These support arithmetic inputs only and do not formalize (1)–(3).
No formal verification or absence claim is made.
