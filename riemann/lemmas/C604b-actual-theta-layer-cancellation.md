# Corollary 604b: actual-theta layer cancellation

## Hypotheses

Use exactly L605's fixed full-line probability density
\(p(u)=k(u)/Z\), where \(k(u)=4\Phi(u/2)\) is the even extension
of L019's kernel and \(Z=\int_{\mathbb R}k\). Use C604a's
definitions of \(h,\tau,c,F,D,H_s,M,R,\ell,q,V,J_a\), in particular

\[
 F(x)=\int_{\mathbb R}p(u)e^{ixu}\,du,\quad
 D=F'^2-FF'',\quad q(a)=-\tau'(a),\quad
 \ell=\lim_{a\to\infty}\tau(a),\quad V=c-\ell.
\]

In addition to the named imports already used in L605 and C604a,
import George Csordas, *Fourier transforms of positive definite
kernels and the Riemann xi-function*,
[arXiv:1309.0055v2, 21 February 2014](https://arxiv.org/pdf/1309.0055v2),
equation (4.2), printed p.10, and Theorem 4.2(a), printed p.11:
for the same \(\Phi\),

\[
 T(s)=\int_s^\infty\Phi(\sqrt v)\,dv,
 \qquad (\log T)''(s)<0\quad(s>0).                         \tag{1}
\]

This exact strict-tail statement is imported, not its original proof.
Csordas attributes it to Csordas--Norfolk--Varga, *The Riemann
Hypothesis and the Turan inequalities*, Trans. Amer. Math. Soc.
296 (1986), 521-541, Proposition 2.1; that original proof has not
been independently audited here.

## Conclusion

All C604a hypotheses hold for this p, and
\(\tau'(u)<0\) for every \(u>0\), while \(\tau'(0)=0\).
Consequently its fixed-density constants

\[
\begin{split}
 w(a)&=q(a)p(a)^2=a p(a)^2+h(a)p'(a),\\
 A&=2\int_0^\infty w(a)\,da>0,\qquad
 P=\sup_{a\ge0}p(a),\\
 B&=2\left(\sup_{a\ge0}|p'(a)|+
                  \int_0^\infty|p''(a)|\,da\right),\qquad
 W=\int_0^\infty|w'(a)|\,da
\end{split}                                                   \tag{2}
\]

are finite. For every real x!=0,

\[
 M(x)=\ell F(x)^2+\int_0^\infty q(a)J_a(x)^2\,da,
 \quad J_a(x)=2\int_0^a p(u)\cos(xu)\,du,                    \tag{3}
\]
\[
 \left|M(x)-\ell F(x)^2-\frac{A}{x^2}\right|
 \le\frac{W+4PBV}{|x|^3}+\frac{B^2V}{|x|^4}.                \tag{4}
\]

As |x| tends to infinity,

\[
 M(x)=A/x^2+O_p(|x|^{-3}),\qquad
 R(x)=-A/x^2+O_p(|x|^{-3}).                                 \tag{5}
\]

Thus M>0 and R<0 eventually. For every integer N>=0,

\[
 D(x)=M(x)+R(x)=O_{p,N}(|x|^{-N}),\qquad
 \frac{D(x)}{M(x)}=O_{p,N}(|x|^{-N})                         \tag{6}
\]

with the ratio asserted only for sufficiently large |x|, where M>0.
Equivalently R/M=-1+O_{p,N}(|x|^{-N}) there for every N.
All constants and onsets concern this fixed p; none is evaluated or
asserted uniform over densities. No vanishing limiting floor is needed.

These are cancellation diagnostics for the actual theta density,
not a sign of D. They provide no separate estimate of R_+ or R_-,
effective height, higher Fourier Laguerre sign or RH conclusion.
An absolute error o(|x|^-2), or finitely many additional algebraic
orders, cannot alone determine the residual sign.

## Proof

**Unchanged base hypotheses.** L605 proves that this exact normalized
full-line p is strictly positive, even and smooth, and that each
derivative decays faster than every exponential. It checks the kernel
coordinate \(k(u)=4\Phi(u/2)\), both normalizations and the origin
regularity. Its Stein ratio is smooth, even and positive, nonincreasing
on [0,infinity), with c=tau(0) finite and positive. These are every
base hypothesis of C604a (and its L604 definitions). We reuse those
audited checks, rather than reprove the theta shape or hazard theorems.

**Strict-tail mapping.** Distinguish the auxiliary function
\(Q(s)=\Phi(\sqrt s)\) from the layer weight q=-tau'. L605 checks
\(J=\int_0^\infty Q\in(0,\infty)\), Q>0 and smoothness on s>0.
Its auxiliary survival and hazard satisfy

\[
 S(s)=T(s)/J,\qquad f(s)=Q(s)/J,\qquad r(s)=Q(s)/T(s).
\]

In particular the T in (1) is exactly its unnormalized auxiliary
tail, not a tail for the squared random variable with density p.
T>0, T'=-Q and the necessary derivatives exist on s>0. Therefore

\[
 (\log T)'=-r,\qquad r'=-(\log T)''>0.
\]

L605's identity tau(u)=2/r(u^2/4) now gives, by the chain rule,

\[
 \tau'(u)=-\frac{u\,r'(u^2/4)}{r(u^2/4)^2}
          =\frac{u\,(\log T)''(u^2/4)}{r(u^2/4)^2}<0
          \quad(u>0).                                      \tag{7}
\]

Here the derivative of u^2/4 is u/2, cancelling the numerator 2
in tau. No normalization factor Z or J remains. Source strictness
is used only at s>0. At u=0, L605 supplies the finite value
tau(0)=2J/Phi(0) and the smooth even extension tau'(0)=0;
no strict endpoint inequality is asserted or required.
Thus tau is nonconstant and q>0 for every a>0.

**Application with all qualifications.** All hypotheses of C604a
are now verified. Its constants and positive-coefficient conclusion
give (2); alternatively q p^2>0 on each compact positive interval
immediately supplies strict positivity of its integral. Its exact
layer formula and explicit uniform endpoint bound give (3)-(4),
including the possible floor ell F^2. Its nonconstant-case
asymptotics give (5), and its Schwartz and relative-cancellation
conclusions give (6). In particular the ratio is used only beyond
the onset at which M>=A/(2x^2); no division at a finite zero of M
is made. These assertions apply at both frequency ends.

The entire signed remainder R is retained. Equation (7) adds no
integrated estimate to the identity D=M+R, and the sign of a rapidly
decreasing function is not determined by its decay. The exact
required first-sign inequality remains R_-<=M+R_+ at every real
frequency. It is not assumed here. Independent higher signs remain
unresolved. This is a standard application of the cited strict-tail
theorem and the audited local results, not a new theta-shape theorem
or progress beyond those sources' conclusions about Fourier signs.

## Mathlib

Full matching-result and supporting-result coverage not checked;
no absence or formalization claim is made. The exact named strict-tail
theorem is imported, with its coordinate and derivative specialization
proved above. L605 and C604a retain their recorded source-proof and
Mathlib qualifications. No original-source proof audit is claimed.
