# C019d — Actual Jensen circle: one integration by parts pays the shrinking annulus

## Hypotheses

Use exactly C019c's definitions and hypotheses: fixed field
\(K=\mathbb Q\), positive integer \(d\to\infty\), \(x\in[1,4]\),
\(q=q_e+xd^{-2/3}\), the source saddle \(u_q=r^2e^{-2i\alpha}\),
\(T,\Lambda,\kappa=\pi/2\), phase \(h_q\), amplitude \(a_q\),
\(H_q=\Re h_q(u_q)\), and the unchanged positive scale
\[
 P_d=\frac{d!}{d^d},\qquad
 M_d(x)=P_d|a_q(-2\alpha)|e^{dH_q}d^{-1/3}.
\]
In particular, with the lower branches \(-\pi\leq\arg u\leq0\),
\[
 h_q(u)=-qu+2\kappa\sqrt u+
        \frac{2\kappa}{\Lambda}\sqrt u\Log u-\Log u,
\]
\[
 w(\theta)=Tr e^{i\theta/2},\qquad
 a_q(\theta)=2^{-1/4}\pi^{1/4}w(\theta)^{7/4}
       \zeta(1/2+w(\theta))g_{\mathbb Q}(w(\theta)).
\]
The exact saddle equations include
\[
 qr-r^{-1}=\frac{2\kappa\alpha}{\Lambda\sin\alpha},\qquad
 (qr+r^{-1})\cos\alpha
       =\kappa\left(1+\frac{2+2\log r}{\Lambda}\right).
\]
Fix \(0<\theta_0\leq1/10\), independently of \(d,x\), and put
\(\epsilon=(\log d)d^{-1/3}\). For \(d\) large enough that
\(\epsilon<\theta_0\), define the actual annular contribution
\[
 I_{\rm ann}=\frac{P_d}{2\pi i}
  \int_{\substack{u=r^2e^{i\theta}\\
                    \epsilon\leq|\theta|\leq\theta_0}}
       F(T^2u)e^{-dqu}\frac{du}{u^{d+1}}.
\]
Both arcs have their original counterclockwise orientation. There is
no contour deformation, local-integral lower bound or Airy hypothesis.

## Conclusion

There are fixed positive constants \(B_0,B_1\), independent of
\(d,x\), and a common onset \(d_0(\theta_0)\) such that, for all
\(d\geq d_0(\theta_0)\) and \(x\in[1,4]\),
\[
 \boxed{\quad
 \frac{|I_{\rm ann}|}{M_d(x)}
 \leq \frac{1216B_0}{9\pi(\log d)^2}
       +\frac{32B_1}{3\pi d^{1/3}\log d}=o(1).
 \quad}                                                   \tag{1}
\]
Thus the supremum over \(x\in[1,4]\) tends to zero. The constants
are finite analytic bounds specified below, not numerically evaluated
constants; the onset is existential and may depend on \(\theta_0\).
This is an established-method specialization, retained after the
critical replay1350 below. It is not a sign result or a proof of RH.

## Proof

**Cited inputs and purpose of the specialization.** The source is Ken
Ono, *An Asymptotic Jensen–Pólya Criterion for GRH*,
[arXiv:2610.38870v1](https://arxiv.org/html/2610.38870v1),
28 October 2026. Use Lemma7/(3.6)–(3.9), Lemma8/(3.12),
Lemma12/(4.3), the exact factorization (4.4)–(4.5), and the
half-plane Euler-product estimates in Lemma13's proof after (4.9).
The single finite-interval integration-by-parts identity is the one
in Lemma14's proof, immediately before (5.1)'s tail estimate.
Its identity is used, not its Gaussian conclusion or local hypotheses.
Proposition15's angular substitution agrees with C019c's normalization.

C019c already establishes, uniformly in \(x\),
\(\alpha\leq C_\alpha d^{-1/3}\), positive upper and lower bounds
for \(r\), \(\Lambda\to\infty\), \(Tr\to\infty\), the eventual
source range \(q_e<q\leq c_0T\), and the nonzero saddle amplitude.
The new work is the exact angular derivative test and amplitude
specialization on the moving annulus. The source's local linear
nonstationarity and rescaled local \(C^1\) theorem do not cover it.
No general theorem is reproved to replace a matching citation.

**Uniform onset and exact derivative.** Enlarge the common onset until
\[
 \epsilon<\theta_0,\qquad \alpha\leq\epsilon/4,\qquad
 C:=\frac{2\kappa r}{\Lambda}\leq1.
                                                               \tag{2}
\]
The middle condition follows from \(\log d\geq4C_\alpha\); the
last follows from the boundedness of \(r\). On the lower annulus set
\[
 \beta=-\theta/2,\quad z=e^{-i\beta},\quad A=qr^2,\quad
 R=\alpha/\sin\alpha,\quad
 \phi(\theta)=h_q(r^2e^{i\theta})-h_q(u_q).
\]
Here \(2\alpha\leq\beta\leq1/20\). The exact saddle equations give
\[
 A-1=CR,\qquad
 \kappa r\left(1+\frac{2+2\log r}{\Lambda}\right)
          =(A+1)\cos\alpha.
\]
Differentiate the displayed exact phase, keeping \(r,q,\Lambda\)
fixed during angular differentiation. It follows that
\[
 \begin{split}
 \phi'(\theta)
 &=i\left[-Ae^{i\theta}
   +\left((A+1)\cos\alpha+iC\theta/2\right)e^{i\theta/2}-1\right]\\
 &=iz\,(U(\beta)+iV(\beta)),\\
 U(\beta)&=(A+1)(\cos\alpha-\cos\beta),\\
 V(\beta)&=C(R\sin\beta-\beta).
 \end{split}                                                   \tag{3}
\]
There is no discarded \(1/\Lambda\) term. This exact use of the
saddle equations matters because \(\epsilon^2\ll1/\Lambda\).

For \(0\leq t\leq1\), use
\(t/2\leq\sin t\leq t\), \(1-\cos t\leq t^2/2\), and
\(0\leq t-\sin t\leq t^3/6\). Consequently
\(1\leq R\leq2\) and \(0\leq R-1\leq\alpha^2\).
By (2), \(1\leq A\leq3\). Therefore
\[
 \cos\alpha-\cos\beta
 =\int_\alpha^\beta\sin t\,dt
 \geq\frac{\beta^2-\alpha^2}{4}
 \geq\frac{3\beta^2}{16},
\]
and (3) yields the uniform nonstationarity bound
\[
 |\phi'(\theta)|\geq U(\beta)
 \geq\frac{3\beta^2}{8}
 =c_*|\theta|^2,\qquad c_*:=\frac3{32}.                \tag{4}
\]
In particular, division by \(\phi'\) on the closed retained interval
is legitimate.

For the second derivative, the same elementary estimates give
\[
 \begin{gathered}
 |U|\leq2\beta^2,\qquad
 |V|\leq\alpha^2\beta+\beta^3/6\leq\beta^3,\\
 |U_\beta|\leq4\beta,\qquad
 |V_\beta|=|C(R\cos\beta-1)|
       \leq\alpha^2+\beta^2/2\leq\beta^2.
 \end{gathered}
\]
Since \(z'=iz/2\) and \(d\beta/d\theta=-1/2\), differentiating
(3) gives
\[
 \phi''=-\frac z2(U+iV)-\frac{iz}2(U_\beta+iV_\beta),
 \qquad |\phi''|\leq\tfrac12(3\beta^2+5\beta)
                  \leq4\beta=2|\theta|.               \tag{5}
\]
As a direct algebra check, differentiating the first line of (3)
instead gives
\(\phi''=Az^2-\tfrac z2((A+1)\cos\alpha-iC\beta+C)\),
which agrees with this expression. No limiting phase replaces \(h_q\).
Lemma8/(3.12), in its full lower-semicircle range, also gives
\[
                  |e^{d\phi(\theta)}|\leq1.             \tag{6}
\]

**Amplitude and its actual angular derivative.** Put \(W=Tr\).
On the larger interval \(-\theta_0\leq\theta\leq0\), including
the saddle angle by (2),
\[
 |w|=W,\quad |\arg w|\leq1/20,\quad
 \sigma:=\Re(1/2+w)=1/2+W\cos(\theta/2)\geq1/2+W/2.
\]
Since \(W\to\infty\) uniformly, choose the onset so that
\(W\geq W_0\) and \(\sigma\geq4\) throughout this interval.
All sector and half-plane hypotheses of the imported estimates now
hold on this larger interval, not merely on a rescaled saddle interval.

Lemma13's proof supplies
\(\zeta(\sigma)^{-1}\leq|\zeta(\sigma+it)|\leq\zeta(\sigma)\)
for \(\sigma>1\), and
\(|\zeta'/\zeta(s)|\leq C_\zeta e^{-c_\zeta\Re s}\)
for \(\Re s\geq4\). These are uniform half-plane estimates from
the absolutely convergent Euler product. Lemma12 supplies
\(|\log g(w)|\leq C_g/W\) and \(|g'(w)/g(w)|\leq C_g/W^2\).
In particular every amplitude factor is nonzero here. Since the power
\(w^{7/4}\) has modulus \(W^{7/4}\), these estimates bound
\(|a_q(\theta)|/|a_q(-2\alpha)|\) above by a fixed constant \(B_0\).

Moreover \(w'=iw/2\), so direct differentiation gives
\[
 \frac{a_q'(\theta)}{a_q(\theta)}
 =\frac{7i}{8}+\frac{iw}{2}
   \left(\frac{\zeta'}{\zeta}(1/2+w)+\frac{g'}g(w)\right).
\]
Its modulus is bounded by
\[
 \frac78+\frac{C_\zeta W}{2}e^{-c_\zeta(1/2+W/2)}
             +\frac{C_g}{2W},
\]
which has a finite uniform upper bound \(B_*\). Thus, for
\(f(\theta)=a_q(\theta)/a_q(-2\alpha)\), take
\(B_1=B_0B_*\) to obtain
\[
                  |f|\leq B_0,\qquad |f'|\leq B_1.       \tag{7}
\]
This is a bound for the \(\theta\) derivative itself. No scale factor
from the source's coordinate \(y\) is suppressed.

**One integration by parts, with all endpoints and remainders.** Let
\(J=\int_{-\theta_0}^{-\epsilon}f(\theta)e^{d\phi(\theta)}d\theta\).
The phase is \(C^2\), the amplitude is \(C^1\), and (4) holds on
this finite closed interval. The elementary identity used in the
proof of source Lemma14 therefore applies exactly:
\[
 J=\left[\frac{fe^{d\phi}}{d\phi'}\right]_{-\theta_0}^{-\epsilon}
 -\frac1d\int_{-\theta_0}^{-\epsilon}
       \left(\frac{f'}{\phi'}-\frac{f\phi''}{(\phi')^2}\right)
                   e^{d\phi}\,d\theta.
\]
Using (4)–(7) and substituting \(t=|\theta|\) in the positive bounds
gives the complete certificate
\[
 \begin{split}
 |J|\leq\frac1d\Bigg[&\frac{B_0}{c_*}
                    (\epsilon^{-2}+\theta_0^{-2})\\
 &+\frac{B_1}{c_*}(\epsilon^{-1}-\theta_0^{-1})
  +\frac{B_0}{c_*^2}(\epsilon^{-2}-\theta_0^{-2})\Bigg].
 \end{split}                                                   \tag{8}
\]
The two terms in the first parentheses bound the two endpoints.
The second line comes respectively from integrating \(t^{-2}\)
and \(2t^{-3}\); both weighted remainder terms are retained.
Since \(0<\epsilon<\theta_0\), this is at most
\[
 \frac1d\left[
  B_0\left(\frac2{c_*}+\frac1{c_*^2}\right)\epsilon^{-2}
           +\frac{B_1}{c_*}\epsilon^{-1}\right].          \tag{9}
\]

**The two actual arcs and normalization.** By the exact factorization
(4.5) and \(du/u=i\,d\theta\), the lower contribution is
\[
 I_- =\frac{P_d}{2\pi}a_q(-2\alpha)e^{dh_q(u_q)}J.
\]
As in C019c, the actual angular integrand
\(F(T^2u)e^{-dqu}u^{-d}\) at \(-\theta\) is the complex conjugate
of that at \(\theta\). This uses real Taylor coefficients, real
\(q,r\), and integer \(d\). Substituting \(-\theta\) in the
counterclockwise upper interval \([\epsilon,\theta_0]\) reverses
both its limits and differential, so \(I_+=\overline{I_-}\).
There is no orientation minus sign or additional radius factor.
It follows that
\[
 \frac{|I_{\rm ann}|}{M_d(x)}
   \leq\frac{d^{1/3}}\pi|J|.
\]
Apply (9), \(c_*=3/32\),
\(d^{-2/3}\epsilon^{-2}=(\log d)^{-2}\), and
\(d^{-2/3}\epsilon^{-1}=d^{-1/3}/\log d\).
Since \(2/c_*+1/c_*^2=1216/9\), this is precisely (1).
Every onset and constant was chosen uniformly in \(x\in[1,4]\),
proving the stated supremum bound.

**Limitations.** The upper certificate succeeds for this annulus
with the original \(M_d\); it says nothing about a lower bound or
sign of the omitted local integral. Combined with C019c it pays the
angular complement of \(|\theta|<\epsilon\) at each fixed outer
cutoff, but a uniform cubic local comparison, real orientation and
nonzero signed reference margin are still unpaid. Exceptional roots,
every-degree hyperbolicity and actual-Xi all-degree positivity remain
open. No numerical evidence, contour exchange or new zero-free region
is used. The critical replay below retains exactly this scope.

**Critical replay, 17 November 2026 (1350).** The primary v1 source
was checked against the actual uses: (2.5)–(3.2), Lemma7's uniform
near-edge proof and exact (3.8)–(3.9), Lemma8 including its closed-arc
case, Lemma12/(4.3), (4.4)–(4.5), and the half-plane inequalities
inside Lemma13's proof. Lemma14's finite-interval identity and
Proposition15's angular substitution were checked separately from
their Gaussian conclusions. These are the previously assessed inputs;
no new theorem or source hypothesis is inserted by this replay.

For an independent differentiation, write the unshifted angular phase as
\[
 \Psi(\theta)=-Ae^{i\theta}
  +[2\kappa r+C(2\log r+i\theta)]e^{i\theta/2}
  -2\log r-i\theta.
\]
Its derivative is
\[
 \Psi'=i[-Az^2+(D-iC\beta)z-1],\qquad
 D=\kappa r+C(1+\log r)=(A+1)\cos\alpha.
\]
Dividing the bracket by \(z\) gives
\[
 -Az-z^{-1}+D-iC\beta
 =(A+1)(\cos\alpha-\cos\beta)
       +i[(A-1)\sin\beta-C\beta].
\]
The exact identity \(A-1=CR\) therefore reproduces (3), without
an asymptotic phase replacement. Differentiating this expression with
\(z'=iz/2\), \(\beta'=-1/2\) reproduces (5), including both signs.

All elementary bounds are on \(0<\alpha\leq\beta/2\) and
\(\beta\leq1/20\). In particular,
\[
 R-1=\frac{\alpha-\sin\alpha}{\sin\alpha}
       \leq\frac{\alpha^2}{3}\leq\alpha^2.
\]
The potentially delicate derivative estimate in (5) uses
\(R\cos\beta-1=(R-1)\cos\beta-(1-\cos\beta)\), so it really
is bounded by \(\alpha^2+\beta^2/2\); no factor \(R\) was lost.
Together with \(A+1\geq2\), integrating \(\sin t\geq t/2\)
gives (4)'s exact constant \(3/32\). The upper estimates give
\[
 |\phi''|\leq\tfrac12(3\beta^2+\beta^3+4\beta)
       \leq\tfrac12(3\beta^2+5\beta)\leq4\beta.
\]
Thus both bounds hold at the moving endpoint as well as inside the
interval; no pointwise-in-\(d\) constant replaces a uniform constant.

The amplitude comparison can also be made explicit without numerical
evaluation. Enlarge the same onset so that \(W\geq\max\{W_0,1\}\)
and \(\sigma\geq4\). Both the retained angles and the saddle angle
then have \(|\zeta|\) between \(\zeta(4)^{-1}\) and \(\zeta(4)\),
and \(|g|\) between \(e^{-C_g/W}\) and \(e^{C_g/W}\).
One admissible fixed choice is
\[
 B_0=\zeta(4)^2e^{2C_g},\quad
 B_*=\frac78+\frac{C_\zeta}{2}
       \sup_{t\geq1}t e^{-c_\zeta(1/2+t/2)}+\frac{C_g}{2},
 \quad B_1=B_0B_*.
\]
The displayed supremum is finite. This verifies both nonzero division
and (7) in the actual angular coordinate. All onset requirements are
compatible: C019c's uniform \(r\) bounds and
\(\alpha\leq C_\alpha d^{-1/3}\) imply \(W\to\infty\),
\(C\to0\), and \(\alpha/\epsilon\to0\) uniformly in \(x\).
Only \(\epsilon<\theta_0\) requires the chosen fixed cutoff.

Finally, direct integration of the positive remainder bounds yields
\(\int_\epsilon^{\theta_0}t^{-2}dt
=\epsilon^{-1}-\theta_0^{-1}\) and
\(\int_\epsilon^{\theta_0}2t^{-3}dt
=\epsilon^{-2}-\theta_0^{-2}\). The two separate endpoint terms
are \(B_0/(dc_*\epsilon^2)\) and
\(B_0/(dc_*\theta_0^2)\). This replays every term in (8).
Conjugation is applied to the actual single-valued angular integrand,
not to a chosen square root in isolation. Both arcs contribute the
factor \(P_d/(2\pi)\); their absolute-value sum divided by \(M_d\)
is bounded by \(d^{1/3}|J|/\pi\). The exact arithmetic
\(2/c_*+1/c_*^2=64/3+1024/9=1216/9\) and
\(1/c_*=32/3\) recovers (1).

The audit finds no failed inequality, missing endpoint, extra radius
factor or changed hypothesis. It retains the uniform upper certificate
and the sole direct notebook input C019c. This is verification of a
local specialization of the cited inputs, not progress beyond their
checked scope toward a sign theorem. It is not a foundational audit
of the whole source manuscript or its claimed formal artifacts.

## Mathlib

Full matching theorem and supporting formal theorem coverage were not
checked. The source's claimed autoformalization is not a verified Lean
artifact in this notebook. The proof is an informal specialization of
the precisely cited estimates, with its new elementary angular bounds
and endpoint calculation written out above.
