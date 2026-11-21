# C618a: Suzuki's shifted-line and low-frequency form bounds

## Hypotheses

Fix real numbers \(a_1>0\), \(c>1\) and \(T>0\). Let
\(0<a\le a_1\) and \(\phi\in L^2((-a,a),dt;\mathbb C)\).
No mean-zero, parity, positivity or smoothness condition is imposed.
All integrals use ordinary Lebesgue measure. Set

\[
 \widehat\phi(z)=\int_{-a}^a\phi(t)e^{izt}\,dt,\qquad
 \Phi(\phi,z)=\frac{\widehat\phi(z)-\widehat\phi(0)}z,
 \quad \Phi(\phi,0)=i\int_{-a}^a t\phi(t)\,dt,
\]
\[
 E_y(\phi)=\int_{\mathbb R}|\Phi(\phi,r+iy)|^2\,dr,\qquad
 L_T(\phi)=\int_{-T}^T|\Phi(\phi,r)|^2\,dr.
\]

The audited source claims are the two form estimates following (4.9)
and (4.11) in Masatoshi Suzuki, *Aspects of the screw function
corresponding to the Riemann zeta-function*, J. London Math. Soc.
108 (2023), 1448–1487, [DOI 10.1112/jlms.12785](https://doi.org/10.1112/jlms.12785),
[arXiv:2206.03682v4](https://arxiv.org/pdf/2206.03682v4), Theorem 4.2,
printed pp.12–15, especially pp.14–15. The PDF is dated 31 May 2023
internally. Its (4.2) is the transform convention above.

The only non-elementary mathematical import is Euclidean Plancherel,
including agreement of the integral and unitary transforms on
\(L^1\cap L^2\): Terence Tao, *245C, Notes 2: The Fourier transform*,
6 April 2009, [Section 3, (8), Theorem 43 and Exercise 44](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/).
We use its complex scalar, one-dimensional case. We do not reprove
Plancherel or assume Suzuki's form bounds as premises.

## Conclusion

Both audited inequalities hold, with the explicit uniform choices

\[
 \boxed{C_2(a_1,c)=e^{2ca_1},\qquad C_3(a_1,T)=\frac{2T}{\pi},
 \qquad a_2(a_1,T)=\min\left\{\frac{a_1}{2},\frac{\pi}{4T}\right\}.}
                                                               \tag{1}
\]
In particular,
\[
 E_{+c}(\phi),E_{-c}(\phi)\le C_2(a_1,c)E_0(\phi),             \tag{2}
\]
\[
 L_T(\phi)\le aC_3(a_1,T)E_0(\phi).                          \tag{3}
\]
All these integrals are finite. In fact (3) holds for every \(a>0\),
without the upper restriction \(a\le a_1\); if \(0<a\le a_2\),
its right side is at most \(E_0(\phi)/2\). Both frequency signs
\(\Phi(\phi,r)\) and \(\Phi(\phi,-r)\), and both conjugate shifted
arguments used by the source, obey these bounds as detailed below.

This is a reproduction and quantitative justification of known source
claims. The reproof is needed because pointwise comparison of kernels
does not by itself establish form comparison for arbitrary complex
tests. It resolves that analytic gate only. It does not audit all of
Theorem 4.2, supply its numerical positivity onset, prove all-window
positivity, or pay the arithmetic/complement and Xi-transfer gaps.
L030/L032/C032a describe those remaining gaps; they are context, not
premises here. No local lemma is a mathematical input.

## Proof

### A compactly supported primitive without a mean-zero assumption

Extend the following function by zero outside \([-a,a]\), assigning
any value at zero:
\[
 q_\phi(x)=
 \begin{cases}
  -\displaystyle\int_{-a}^{x}\phi(t)\,dt,&-a<x<0,\\[4pt]
   \displaystyle\int_x^a\phi(t)\,dt,&0<x<a.
 \end{cases}                                                   \tag{4}
\]
Since \(\|\phi\|_1\le\sqrt{2a}\|\phi\|_2\), these integrals
exist. Each half has an absolutely continuous representative with
derivative \(-\phi\) almost everywhere, and the outer traces are
zero. Its jump is
\[
 q_\phi(0+)-q_\phi(0-)=\int_{-a}^a\phi(t)\,dt.
\]
We retain this jump. No global Sobolev regularity of \(q_\phi\) or
zero integral of \(\phi\) is assumed.

For \(0<x<a\), Cauchy–Schwarz and Tonelli give
\[
 \begin{split}
 \int_0^a|q_\phi(x)|^2dx
 &\le\int_0^a(a-x)\int_x^a|\phi(t)|^2dt\,dx\\
 &=\int_0^a\left(at-\frac{t^2}{2}\right)|\phi(t)|^2dt
 \le\frac{a^2}{2}\int_0^a|\phi(t)|^2dt.
 \end{split}
\]
On the negative half, replacing \(x,t\) by \(-x,-t\) gives the
same estimate with \(\phi(-t)\); the minus sign in (4) disappears
under absolute value. Consequently
\[
 \|q_\phi\|_2^2\le\frac{a^2}{2}\|\phi\|_2^2,
 \qquad\|q_\phi\|_1\le\sqrt{2a}\|q_\phi\|_2.                \tag{5}
\]
For each real \(y\), also \(q_y(x)=e^{-yx}q_\phi(x)\) belongs
to \(L^1\cap L^2(\mathbb R)\): on its support the weight is
bounded by \(e^{|y|a}\).

For every complex \(z\), with the quotient interpreted continuously
at zero,
\[
 \frac{e^{izt}-1}{z}=i\int_0^t e^{izx}\,dx.
\]
For fixed \(z\), the absolute double integral after multiplying by
\(\phi(t)\) is bounded by
\(ae^{a|\operatorname{Im}z|}\|\phi\|_1<\infty\).
Fubini is therefore valid. On the negative half, the oriented
integral contributes the minus sign in (4), so
\[
 \Phi(\phi,z)=i\int_{-a}^a q_\phi(x)e^{izx}\,dx.             \tag{6}
\]
The same bound, uniform on compact sets of \(z\), justifies the
removable value at zero and differentiation there. In particular
there is no division by an unhandled zero frequency.

### Plancherel, normalization and the two shifted lines

Write Tao's transform as
\(\mathcal Ff(\xi)=\int f(x)e^{-2\pi i x\xi}dx\).
For \(f\in L^1\cap L^2\), its cited Plancherel theorem and the
change of variable \(\xi=-r/(2\pi)\) give
\[
 \int_{\mathbb R}\left|\int f(x)e^{irx}dx\right|^2dr
   =2\pi\|f\|_2^2.                                          \tag{7}
\]
Apply this to \(q_y\), which was verified to lie in the common
domain, and use (6). We obtain the exact identity
\[
 \boxed{E_y(\phi)=2\pi\int_{-a}^a e^{-2yx}|q_\phi(x)|^2dx.}  \tag{8}
\]
Thus every \(E_y\) is finite, and
\[
 E_{\pm c}(\phi)\le e^{2ca}E_0(\phi)
                    \le e^{2ca_1}E_0(\phi),
\]
as required. The shifted lines are evaluated by exponential weights
on the real spatial axis. This proof requires no contour deformation
and hence no assumption about limits of vertical contour edges.

For precision about the source's four shifted arguments, for
\(\varepsilon\in\{1,-1\}\), change the real variable to
\(u=\varepsilon r\) to obtain
\[
 \int_{\mathbb R}|\Phi(\phi,\varepsilon(r+ic))|^2dr=E_{\varepsilon c}(\phi),
 \quad
 \int_{\mathbb R}|\Phi(\phi,\varepsilon(r-ic))|^2dr=E_{-\varepsilon c}(\phi).
                                                               \tag{9}
\]
No symmetry or reality of \(\phi\) is used. In particular, for any
measurable multiplier \(B\) with \(|B(r)|\le M<\infty\),
Cauchy–Schwarz, (2) and (9) give absolute convergence and
\[
 \left|\frac1{2\pi}\int_{\mathbb R}B(r)
 \Phi(\phi,\varepsilon(r+ic))
 \overline{\Phi(\phi,\varepsilon(r-ic))}\,dr\right|
 \le\frac{MC_2}{2\pi}E_0(\phi).                             \tag{10}
\]
Here \(dz=dr\) on a horizontal line. This verifies the form-norm
step needed by the source's Cauchy–Schwarz argument; it does not
assert a bound for any particular arithmetic multiplier or certify
the other source constants.

### The low-frequency loss

For each real \(r\), (6) and Cauchy–Schwarz on a set of measure
\(2a\) give
\[
 |\Phi(\phi,r)|^2
 \le\left(\int_{-a}^a|q_\phi(x)|dx\right)^2
 \le2a\|q_\phi\|_2^2.
\]
Integration over \([-T,T]\), followed by (8) at \(y=0\), yields
\[
 L_T(\phi)\le4aT\|q_\phi\|_2^2
             =\frac{2aT}{\pi}E_0(\phi),                     \tag{11}
\]
which proves (3). Reflection \(r\mapsto-r\) leaves both intervals
\(\mathbb R\) and \([-T,T]\) invariant, so the same statement
holds with \(\Phi(\phi,-r)\). Both sides in (2)–(3) may also be
divided by \(2\pi\), exactly as in the source's displayed forms.
Since \(a\le a_2\) implies \(2aT/\pi\le1/2\), (1) supplies
the promised explicit small-window threshold. No division by
\(E_0\) was used, so the zero test is included.

This establishes the two asserted form inequalities directly for
complex tests. Pointwise kernel order is never used. The finite
constants may support later signed-form work, but their proof
contains no arithmetic sign information or inference to RH.

## Mathlib

Full matching coverage and supporting Fourier theorem names were not
checked in Mathlib in this step. This is not a claim of absence.
The named Plancherel source above is the analytic import; the
specialized primitive, shift and support arguments are fully given
here. No Lean verification or numerical evidence is claimed.
