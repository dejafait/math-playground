# C034r: fixed-bump Fourier-band detection, audited specialization

## Hypotheses

Use the classical normalization
\(\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\) and
\(\Xi(z)=\xi(1/2+iz)\). Fourier transforms have phase \(e^{-iuy}\),
inverse factor \(1/(2\pi)\), and Plancherel factor \(1/(2\pi)\).
The actual full theta kernel is
\[
 \Phi(y)=\sum_{n\ge1}
 (4\pi^2n^4e^{9|y|/2}-6\pi n^2e^{5|y|/2})e^{-\pi n^2e^{2|y|}}.
\]
Fix \(q=2\), \(Q=\log2\), and
\[
 g(y)=\begin{cases}e^{-1/(1-y^2)},&|y|<1,\\0,&|y|\ge1,\end{cases}
 \qquad h=-g''+\tfrac14g.
\]
Let \(E=L^2(\mathbb R,e^{-y/2}dy)\), \(Jf=e^{-y/4}f\),
\(T_rf(y)=f(y+r)\), and \(C_\Phi f=\Phi*f\). For any fixed \(H>0\),
define the orthogonal projection on this weighted space by
\[
 \widehat{J\Pi_Hf}(u)=1_{[-H,H]}(u)\widehat{Jf}(u).
\]
For real \(X\ge1\), with integer summation indices and the strict lower
endpoint shown, put
\[
 U_Xh=\sum_{X/2<n\le X}\frac{\mu(n)\log(X/n)}{\sqrt n}
                  T_{\log(n/X)}C_\Phi h,
 \qquad A(z)h=\int_0^Q t e^{-zt}T_{-t}C_\Phi h\,dt.
\]
Write
\[
 F_H(X)=\|\Pi_HU_Xh\|_E,
 \qquad E_H(Y)=\int_1^Y F_H(X)^2\frac{dX}{X}.
\]
When a zero is selected, it is an actual nontrivial zeta zero
\(\rho=1/2+\delta+i\gamma\) with \(0<\delta<1/2\) and exact order
\(m\ge1\). Existence of such a zero is a conditional premise, not an
assertion. No rightmost zero, simplicity or uniform zero separation is
assumed. The Fourier cutoff \(H\) here is not a primitive-index cutoff.

## Conclusion

The input is nonzero and compact smooth, belongs to \(E\), and satisfies
the two unweighted pole conditions \(\widehat h(i/2)=\widehat h(-i/2)=0\).
The operator \(A(z)\) is entire in operator norm. For \(\Re z>1/2\),
\[
 \int_1^\infty X^{-z-1}U_Xh\,dX
       =\frac{A(z)h}{\zeta(1/2+z)}                                      \tag{1}
\]
as an absolutely convergent Bochner integral. For every \(z\in\mathbb C\)
and every fixed \(H>0\), \(\Pi_HA(z)h\ne0\).

For any selected zero in the hypotheses, let
\[
 z_\rho=\delta+i\gamma,
 \qquad N_\rho=\frac{m!\,\Pi_HA(z_\rho)h}{\zeta^{(m)}(\rho)}.
\]
Then \(N_\rho\ne0\) and
\[
 \limsup_{Y\to\infty}
 \frac{E_H(Y)}{Y^{2\delta}(\log Y)^{2m-2}}
 \ge \frac{\|N_\rho\|_E^2}{2\delta(2m-2)!}>0.                         \tag{2}
\]
There also exist a single \(H>0\) and \(c>0\), depending on the fixed
input and \(q=2\), but independent of \(\delta,\gamma,m\), such that
\[
 \|\Pi_HA(\delta+i\gamma)h\|_E\ge\frac{c}{1+|\gamma|}
 \quad(0\le\delta\le1/2,\ \gamma\in\mathbb R).                       \tag{3}
\]
This is an existential positive band and constant, not a numerical
certificate. The full Laurent coefficient still contains
\(\zeta^{(m)}(\rho)\); (3) does not bound that derivative or make (2)
uniform in the zeros. Neither primitive-sector upper bound, a full
source-energy upper, nor the actual-Xi mixed sign condition is proved.

## Proof

### Source and purpose of the audit

This is a reproduction/specialization of Leonard van Hemert,
*Exact Zero Detection and Compact Arithmetic Realizations for the
Riemann Xi Function*, v1.0.0, 11 October 2026,
DOI 10.5281/zenodo.23295277:
[tagged primary TeX](https://raw.githubusercontent.com/LeonardSEO/riemann-xi-zero-detection/refs/tags/v1.0.0/paper/paper.tex),
section “Every zero is visible in a fixed Fourier band,”
`lem:log-source-mellin`, `thm:fixed-band-cumulative`, equations FB1-FB8,
lines 11124-11317. The theta reconstruction is at lines 802-838 and
the Fourier convention at lines 89-90 and 7005-7009. These complete
relevant arguments were inspected on 2026-11-21. The source is treated
as an unreviewed manuscript; no assertion about the rest of it is made.
The previously saved assessment2080 authorizes this audit. The detailed
verification below is needed to check the actual kernel normalization,
the operator-valued continuation, and the claimed constant before local
use. It is not a claim of mathematical novelty.

We use the named standard results Gaussian Poisson summation, the
absolutely convergent reciprocal-zeta Dirichlet series on \(\Re s>1\),
Young's convolution inequality, Plancherel's theorem, absolute Bochner
Fubini, Cauchy--Schwarz, and the identity theorem for meromorphic
functions (applied to continuous linear functionals of vectors).
Their required domains and convergence are checked below; the standard
theorems themselves are not reproved.

### 1. Actual theta normalization and the chosen input

For \(\psi(t)=\sum_{n\ge1}e^{-\pi n^2t}\), Gaussian Poisson summation
gives \(1+2\psi(t)=t^{-1/2}(1+2\psi(1/t))\), \(t>0\).
The series and its derivatives converge normally on compact subsets
of \(t>0\). Absolute Mellin integration for \(\Re s>1\), splitting
at one, gives exactly
\[
 \xi(s)=\frac12+\frac{s(s-1)}2
 \int_1^\infty\psi(t)\{t^{s/2}+t^{(1-s)/2}\}\frac{dt}{t}.           \tag{4}
\]
For completeness, the two elementary terms before multiplying by
\(s(s-1)/2\) are \(1/(s-1)-1/s\); their contribution is \(1/2\).
The remaining integral converges locally uniformly for all \(s\),
with all derivatives, because of Gaussian decay. Thus (4) gives the
usual entire continuation and fixes the normalization.

Let \(p(u)=e^{u/2}\psi(e^{2u})\). Poisson summation gives
\(p(-u)=p(u)+\sinh(u/2)\), hence \(p'(0)=-1/4\).
Substitution \(t=e^{2u}\) in (4) yields
\[
 \Xi(z)=\frac12-2(z^2+1/4)\int_0^\infty p(u)\cos(zu)\,du.
\]
Direct differentiation gives \(p''-p/4=\Phi\) for \(u\ge0\).
The relation for \(p(-u)\) makes \(p''-p/4\) smoothly even, since
\((\partial^2-1/4)\sinh(u/2)=0\). Integration by parts twice gives
\[
 2\int_0^\infty(p''-p/4)\cos(zu)\,du
 =-2p'(0)-2(z^2+1/4)\int_0^\infty p\cos(zu)\,du=\Xi(z).
\]
Consequently \(\widehat\Phi(z)=\Xi(z)\) with either Fourier sign,
by evenness. There is no additional factor two.

Every summand of \(\Phi(u)\) for \(u\ge0\) is positive, since its
nonexponential factor is
\(2\pi n^2e^{5u/2}(2\pi n^2e^{2u}-3)>0\).
Moreover
\[
 0<\Phi(u)\le C e^{9|u|/2}e^{-(\pi/2)e^{2|u|}},\qquad
 C=4\pi^2\sum_{n\ge1}n^4e^{-\pi(n^2-1/2)}<\infty.
\]
Indeed split \(n^2e^{2u}=(1/2)e^{2u}+(n^2-1/2)e^{2u}\)
and use \(e^{2u}\ge1\). Each fixed derivative admits the same type
of bound with a changed exponential prefactor and constant, by
termwise differentiation. These bounds pay every integration by
parts above and every fixed exponential moment below.

The specified bump is smooth across \(\pm1\): each one-sided derivative
is a finite sum of powers of \((1-y^2)^{-1}\) and polynomials in \(y\)
times \(e^{-1/(1-y^2)}\), which tends to zero with every such power.
Thus \(g,h\in C_c^\infty\). Integration by parts on their compact
supports gives
\[
 \widehat h(z)=(z^2+1/4)\widehat g(z),\quad z\in\mathbb C.
\]
Both pole values vanish. Also
\(\widehat h(0)=\tfrac14\int g>0\), so \(h\ne0\), and its compact
support gives \(h\in E\). These are conditions on the original
unweighted transform of \(h\), not on \(\widehat{Jh}\).

### 2. Operators, multiplier and noncancellation

The map \(J\) is unitary and
\[
 JT_r=e^{r/4}T_rJ,\qquad \|T_r\|_{E\to E}=e^{r/4},\qquad
 JC_\Phi J^{-1}f=k*f,\quad k(y)=e^{-y/4}\Phi(y).
\]
Both \(k\) and \(e^{-y/4}\Phi'(y)\) are in \(L^1\), by the bounds
above. Young's inequality proves boundedness of the convolution
operators \(C_\Phi\) and \(C_{\Phi'}\) on \(E\). The fundamental
theorem of calculus for the translated kernel gives, for
\(s,t\in[0,Q]\),
\[
 \|T_{-t}C_\Phi-T_{-s}C_\Phi\|
 \le |t-s|\sup_{r\in[-Q,0]}e^{r/4}\|C_{\Phi'}\|
 \le |t-s|\|C_{\Phi'}\|.
\]
This can first be checked on smooth compact inputs and then extended
by density. Hence the integral defining \(A(z)\) exists in operator
norm. On compact \(z\)-sets its derivatives are dominated by
\(t^{j+1}e^{|\Re z|Q}e^{-t/4}\|C_\Phi\|\) on \([0,Q]\).
It follows that \(A\) is entire in that norm.

The Fourier transform of \(k\) is \(\Xi(u-i/4)\); the minus sign
is forced by \(e^{-i(u-i/4)y}=e^{-iuy}e^{-y/4}\).
Since \(\widehat{T_{-t}f}(u)=e^{-iut}\widehat f(u)\),
\[
 \widehat{JA(z)h}(u)=W(u)G_Q(z+1/4+iu),\quad
 W(u)=\Xi(u-i/4)\widehat{Jh}(u),                                  \tag{5}
\]
where
\[
 G_Q(\lambda)=\int_0^Q t e^{-\lambda t}dt
 =\frac{1-(1+Q\lambda)e^{-Q\lambda}}{\lambda^2},\quad
 G_Q(0)=Q^2/2.                                                     \tag{6}
\]
In particular, exactly
\[
 \|\Pi_HA(z)h\|_E^2
 =\frac1{2\pi}\int_{-H}^H|W(u)G_Q(z+1/4+iu)|^2du.                \tag{7}
\]

The factors \(\Xi\) and \(G_Q\) are entire and not identically zero
(their values at zero are positive). For fixed \(z\), their composed
zero sets on the real \(u\)-line are discrete. The transform
\(\widehat{Jh}\) is entire, by compact support, and not identically
zero, by Fourier uniqueness and \(h\ne0\). It cannot vanish throughout
a nonempty interval. Outside a measure-zero union of discrete sets
the product in (7) is nonzero. Thus (7) is strictly positive for every
\(H>0,z\in\mathbb C\). More generally the same reasoning works for
an \(E\)-input with \(\Pi_Hh\ne0\), since its transform is nonzero
on a subset of the band of positive measure. No positivity of a Weil
or algebraic mixed form enters this argument.

### 3. Absolute Mellin identity

On compact \(X\)-intervals, \(U_Xh\) has only finitely many terms,
each continuous between finitely many endpoint changes; it is
strongly measurable and locally bounded in \(E\). Each integer \(n\)
occurs for \(n\le X<2n\), up to endpoints of measure zero. Substituting
\(X=ne^t\) gives the norm majorant, for \(\sigma=\Re z>1/2\),
\[
 \sum_{n\ge1}\int_n^{2n}
 X^{-\sigma-1}\frac{|\mu(n)|\log(X/n)}{\sqrt n}
 \|T_{\log(n/X)}C_\Phi h\|_E\,dX
 \le \|C_\Phi\|\|h\|_E
 \sum_{n\ge1}n^{-\sigma-1/2}
 \int_0^Q t e^{-(\sigma+1/4)t}dt<\infty.
\]
Absolute Bochner Fubini is therefore applicable. The termwise vector
integral is \(\mu(n)n^{-z-1/2}A(z)h\). Summing with
\(\sum\mu(n)n^{-s}=1/\zeta(s)\), \(\Re s>1\), proves (1).
Projection commutes with these integrals because it is bounded.
Also \(\|U_Xh\|_E\le2Q\|C_\Phi\|\|h\|_E\sqrt X\), using
\(\sum_{n\le X}n^{-1/2}\le2\sqrt X\) and \(e^{r/4}\le1\) for
the shifts present. In particular all cumulative energies on bounded
intervals are finite. This crude bound is not a subpower upper.

### 4. Exact-order pole and cumulative lower bound

The meromorphic vector \(B(z)=\Pi_HA(z)h/\zeta(1/2+z)\) has,
at the selected zero, an exact pole of order \(m\), because (7)
prevents numerator cancellation. Its leading Laurent vector is
\(N_\rho\): the scalar Taylor coefficient in the denominator is
\(\zeta^{(m)}(\rho)/m!\ne0\).

Set \(v=\log X\), \(u(v)=\Pi_HU_{e^v}h\),
\(a(V)=E_H(e^V)=\int_0^V\|u(v)\|_E^2dv\), and \(k=2m-2\).
Let \(M\) be the limsup in (2), possibly infinite. If \(M=\infty\),
(2) holds immediately. Otherwise \(M\ge0\), and for every
\(\eta>0\) there is \(V_0>0\) with
\[
 a(V)\le(M+\eta)e^{2\delta V}V^k\quad(V\ge V_0).                  \tag{8}
\]
For \(s>2\delta\), integration by parts on finite intervals and
(8) show that
\[
 I_s:=\int_0^\infty e^{-sv}da(v)
      =s\int_0^\infty e^{-sv}a(v)dv<\infty.
\]
The endpoint at zero is zero because \(a(0)=0\); the endpoint at
infinity is zero since \(e^{-sV}a(V)\to0\).

For a compact subset of \(\Re z>\delta\), put
\(a_* =\min\Re z>\delta\) and choose \(2\delta<s<2a_*\).
For every integer \(j\ge0\), Cauchy--Schwarz gives the explicit
integrable compact majorant
\[
 \int_0^\infty v^j e^{-a_*v}\|u(v)\|_E dv
 \le I_s^{1/2}
 \left(\int_0^\infty v^{2j}e^{-(2a_*-s)v}dv\right)^{1/2}<\infty.
\]
Thus the actual vector integral
\(L(z)=\int_0^\infty e^{-zv}u(v)dv\) is holomorphic on this
half-plane, with derivatives under the integral. It equals \(B(z)\)
on \(\Re z>1/2\) by (1); here \(\delta<1/2\). The meromorphic
identity theorem on the connected half-plane, tested against all
continuous linear functionals on \(E\), identifies it with \(B\)
throughout \(\Re z>\delta\). If a noncanceling pole lay further
right this would already contradict finite \(M\). Its absence has
not been used as an assumption. The pole of zeta at \(s=1\) is a
zero of its reciprocal, hence creates no additional vector pole.

For \(\epsilon>0\), weighted Cauchy--Schwarz now gives
\[
 \|L(z_\rho+\epsilon)\|_E^2
 \le\frac1\epsilon\int_0^\infty
       e^{-(2\delta+\epsilon)v}da(v).                             \tag{9}
\]
Specifically split the integrand into factors \(e^{-\epsilon v/2}\)
and \(e^{-(z_\rho+\epsilon/2)v}u(v)\); the first squared integral
is \(1/\epsilon\). The boundary terms just checked, now with
\(s=2\delta+\epsilon\), give
\[
 \int_0^\infty e^{-(2\delta+\epsilon)v}da(v)
 =(2\delta+\epsilon)\int_0^\infty
                  e^{-(2\delta+\epsilon)v}a(v)dv
 \le C_{V_0}+(2\delta+\epsilon)(M+\eta)k!\epsilon^{-k-1},           \tag{10}
\]
where \(C_{V_0}<\infty\) is independent of \(0<\epsilon\le1\).
For the tail we used (8) and
\(\int_0^\infty e^{-\epsilon v}v^k dv=k!\epsilon^{-k-1}\).

Multiply (9)-(10) by \(\epsilon^{2m}\). The finite-interval term
is \(O(\epsilon^{2m-1})\to0\), including \(m=1\). Since
\(k+1=2m-1\), the remaining term tends to
\(2\delta(M+\eta)(2m-2)!\). The local Laurent expansion, valid
in a sufficiently small disk about this individual zero, gives
\(\epsilon^mL(z_\rho+\epsilon)\to N_\rho\) in \(E\).
Taking \(\epsilon\downarrow0\) and then \(\eta\downarrow0\)
proves (2). No uniform isolation radius or limit exchange over zeros
was used. The argument specifically requires \(\delta>0\); it
asserts no formula with denominator \(2\delta\) at \(\delta=0\).

### 5. One band for every height

For the selected input,
\[
 W(0)=\Xi(-i/4)\widehat h(-i/4)
     =\frac3{16}\Xi(-i/4)\int g(y)e^{-y/4}dy>0.
\]
The positivity of \(\Xi(-i/4)=\int\Phi(y)e^{-y/4}dy\) follows
from the actual positive kernel. Continuity permits a fixed \(H>0\)
and \(b>0\) with \(|W(u)|\ge b\) on \([-H,H]\).

Set \(R=2(e^{3Q/4}+1)/Q\). For
\(\lambda=r+i(\gamma+u)\), \(r\in[1/4,3/4]\), formula (6) gives
\[
 G_Q(\lambda)=-\frac{Qe^{-Q\lambda}}\lambda
                  +\frac{1-e^{-Q\lambda}}{\lambda^2}.
\]
The ratio of the upper bound on the second term to the magnitude of
the first is at most \((e^{Qr}+1)/(Q|\lambda|)\le1/2\) when
\(|\lambda|\ge R\). Therefore
\[
 |G_Q(\lambda)|\ge\frac{Qe^{-3Q/4}}{2|\lambda|}.
\]
If \(|\gamma|\ge\Gamma:=H+R\), this holds throughout the band,
because \(|\lambda|\ge|\gamma|-H\). Also
\(|\lambda|\le|\gamma|+H+3/4\). Formula (7), retaining its
Plancherel factor, yields
\[
 \|\Pi_HA(\delta+i\gamma)h\|_E
 \ge \frac{bQe^{-3Q/4}\sqrt{H/\pi}}
             {2(|\gamma|+H+3/4)}
 \ge \frac{c_1}{1+|\gamma|},\quad
 c_1=\frac{bQe^{-3Q/4}\sqrt{H/\pi}}{2\max(1,H+3/4)}>0.
\]
For the remaining rectangle \([0,1/2]\times[-\Gamma,\Gamma]\),
the function
\[
 I(\delta,\gamma)=\int_{-H}^H
       |G_Q(\delta+1/4+i(\gamma+u))|^2du
\]
is continuous, by continuity on the compact product. It is strictly
positive at each point: zero integral would, by continuity and
nonnegativity, make the entire function \(G_Q\) vanish on a segment,
contradicting \(G_Q(0)=Q^2/2\). Its compact minimum \(I_*>0\)
therefore exists. Formula (7) gives the lower bound
\(c_0=b\sqrt{I_*/(2\pi)}>0\) on this rectangle. Taking
\(c=\min(c_0,c_1)\) proves (3), including both endpoint values of
\(\delta\). The same input and band were used in both height cases.

### Audit result and limits

FB1-FB8 survive this specialization without a changed statement.
The weighted sign, theta factor, Bochner majorants, exact multiplicity,
infinite-limsup case, all Stieltjes endpoints, factorial and bounded-height
case have been checked. No arithmetic cancellation was inferred.
An eventual subpower upper for this same cumulative energy would have
to be proved independently; a favorable subsequence or an upper on
only one primitive sector cannot contradict (2). In particular the
norm square here is not the algebraic square in the notebook's
actual-node mixed criterion.

## Mathlib

Full matching theorem: not checked; availability is unknown. Supporting
Gaussian Poisson, Fourier/Plancherel, Bochner integration and zeta APIs
have not been matched to this normalization or to the vector pole
argument. No formal verification or absence claim is made. Reference:
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
