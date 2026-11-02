# Corollary 233b: L233's fixed mixture has an increasing Stein kernel near zero

## Hypotheses

Use exactly the comparison kernel of L233:

\[
g(u)=\pi^{-1/2}e^{-u^2},\qquad
k(u)=g(u)+\tfrac14\{g(u-2)+g(u+2)\}.
\]

Define its pointwise Stein ratio by

\[
N(u)=\int_u^\infty v k(v)\,dv,\qquad \tau(u)=N(u)/k(u).
\]

The normalized density is \(p=2k/3\). It has connected support R,
zero mean, finite absolute first moment, and strictly positive smooth
density. Thus the ratio is the pointwise version in Adrien Saumard,
*Weighted Poincare inequalities, concentration inequalities and tail
bounds related to Stein kernels in dimension one*,
[arXiv:1804.03926v3](https://arxiv.org/pdf/1804.03926v3), Section 2,
equation (6), printed pp. 3-4. The common normalization cancels.
Equation (5)'s integration-by-parts identity requires integrability of
both terms and its vanishing endpoint expression; that identity is
not applied in this proof.

## Conclusion

The ratio is smooth, and

\[
\tau'(0)=0,\qquad \tau''(0)>\frac{1328}{2187}>0.
\]

There exists \(\varepsilon>0\) such that
\(\tau'(u)>(1328/2187)u>0\) for \(0<u<\varepsilon\).
In particular, this fixed mixture does **not** have a nonincreasing
Stein kernel on the positive half-line.

Import unchanged from L233, with \(F(x)=\int_R k(u)e^{ixu}\,du\),

\[
(F'^2-FF'')(\pi/2)=-\tfrac78 e^{-\pi^2/8}<0.
\]

Consequently this model cannot refute the proposed implication from
Stein nonincrease to the first Fourier Laguerre sign: its additional
premise fails. Neither that implication, the actual-theta Stein
hypothesis, higher Xi signs, nor RH is decided here.

## Proof

All absolute moments of the finite Gaussian mixture converge, and
\(k>0\) everywhere. The fundamental theorem of calculus gives
\(N'(u)=-u k(u)\); hence \(N\) and \(\tau\) are smooth. Evenness gives
\(k'(0)=0\). Differentiating the quotient in the form

\[
\tau'(u)=-u-\tau(u)\frac{k'(u)}{k(u)}
\]

shows first that \(\tau'(0)=0\), and then that

\[
\tau''(0)=-1-\tau(0)\frac{k''(0)}{k(0)}.                 \tag{1}
\]

Put \(q=e^{-4}\) and \(I=\int_0^2 e^{-v^2}\,dv\). Direct
differentiation of \(g\) gives

\[
k(0)=\frac{1+q/2}{\sqrt\pi},\qquad
k''(0)=\frac{-2+7q}{\sqrt\pi}.                         \tag{2}
\]

For completeness, the only tail integral needed can be evaluated
without a numerical error-function value. For real \(a\), substitution
\(w=v-a\), and \(g'(w)=-2w g(w)\), give

\[
\int_0^\infty v g(v-a)\,dv
=\tfrac12 g(a)+a\int_{-a}^\infty g(w)\,dw.
\]

The Gaussian endpoint at infinity vanishes, and every integral here
is absolutely convergent. Adding this identity at \(a=2,-2\) yields
\(g(2)+2\int_{-2}^2 g(w)\,dw=g(2)+4\int_0^2 g(w)\,dw\).
Include the factor \(1/4\) and the centered contribution \(g(0)/2\)
to obtain

\[
N(0)=\tfrac12 k(0)+\frac{I}{\sqrt\pi},\qquad
\tau(0)=\tfrac12+\frac{I}{1+q/2}.                       \tag{3}
\]

The exponential series has positive remaining terms after
\(1+4+4^2/2=13\), so \(0<q<1/13\). Also
\(e^{-v^2}>1-v^2\) for \(0<v\le1\), and the integrand is positive
on \((1,2)\); therefore \(I>\int_0^1(1-v^2)\,dv=2/3\).
In particular, (2)-(3) imply the strict bounds

\[
\tau(0)>\tfrac12+\frac{2/3}{27/26}=\frac{185}{162},
\qquad
-\frac{k''(0)}{k(0)}
=\frac{2-7q}{1+q/2}>\frac{19/13}{27/26}=\frac{38}{27}.
\]

All compared numerators and denominators are positive. Substitution
in (1) now gives

\[
\tau''(0)>-1+\frac{185}{162}\frac{38}{27}
=\frac{1328}{2187}>0.
\]

Continuity of \(\tau''\) gives an \(\varepsilon>0\) on which
\(\tau''(v)>1328/2187\). Integration from zero, using \(\tau'(0)=0\),
proves the asserted positive derivative for \(0<u<\varepsilon\).
This analytic neighborhood argument certifies failure of global
nonincrease; no finite numerical sample or asymptotic truncation is used.
The Fourier assertion is precisely L233's previously proved value,
not a new Fourier calculation. No parameters of that model were changed.

## Mathlib

Full-result and supporting-result coverage not checked. No matching
formal theorem is claimed. The Stein definition is imported from the
precise source above; the fixed-model differentiation and strict
elementary bounds are proved here.
