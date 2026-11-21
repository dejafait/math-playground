# Lemma 787: conditional audit of the uniform complex-moment factorization

## Hypotheses

Let
\[
 \Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
                         e^{-\pi n^2e^{4u}},\qquad
 I(z)=\int_0^\infty u^{2z}\Phi(u)\,du.
\]
Use the principal logarithm in the power. In L786's exact normalization,
\(I(n)=(2n)!a_n\) for integers n>=0; this is the only local mathematical
input. No Fredholm, coefficient-sign or zero-location premise is assumed.

Fix an integer k>=10^9 and put D_k={z:|z-k|<=k/20}. The following are
**explicit conditional inputs**, not independently verified facts about
this kernel in this audit. Their source is W. Michałowski,
*An explicit uniform cubic wedge for consecutive Toeplitz minors of the
Riemann xi-coefficients*, [arXiv:2607.16795v1, Section 3](https://arxiv.org/html/2607.16795v1#S3),
18 July 2026. Numbering and constants bind to v1.

1. **Real saddle data.** Set B_0=2pi exp(4u_k),
   H_0=B_0-9/2-6/(B_0-3), and k=u_k H_0. Assume
   \(1<u_k<\log(k)/4\) and \((21/25)B_0\le H_0\le B_0\).
   These are the bounds used in the opening of Section 3 and the proof
   of Lemma 3.5. Put sigma=sqrt(u_k/k)>0.
2. **Tube and full saddle.** On Re(u)>=0.35, |Im(u)|<=0.1 assume
   \(\Phi=\Phi_1(1+R)\), with \(|R|\le\rho=1.1\cdot10^{-14}\),
   as in Lemma 3.1. Use the analytic log(Phi) on the interior of this
   tube agreeing with the real logarithm on its positive real interval.
   For every z in D_k assume an analytic full saddle u_s(z), with
   \(|u_s-u_k|\le3/200\) and
   \(\Psi_z'(u_s)=0\), where
   \(\Psi_z(u)=2z\operatorname{Log}u+\log\Phi(u)\).
   This is Lemma 3.3, including the sharper drift bound in its proof;
   analyticity is on the disk interior with continuation at its boundary.
3. **Global horizontal bound.** Write u_s=x_s+iy_s. For x>=0.35 assume
   \[
    -\operatorname{Re}\Psi_z''(x+iy_s)\ge(8/5)k/u_k^2.
   \]
   This is Lemma 3.4 on the stated horizontal line, for every z in D_k.
4. **Local derivative bounds.** For every z in D_k and |u-u_s|<=1/40
   assume
   \[
    -\operatorname{Re}\Psi_z''(u)\,\sigma^2\ge6,\qquad
    |\Psi_z'''(u)|\,\sigma^3\le100\sigma.
   \]
   At the saddle additionally assume
   \[
    A(z)=-\Psi_z''(u_s)\sigma^2,\qquad |A(z)|\le14.185.
   \]
   The first two bounds are in Lemma 3.5's statement. The last is the
   stronger upper bound in its proof; its headline upper bound is 20.
   The present audit deliberately retains 14.185 as a separate cited
   hypothesis. It does not certify that antecedent or substitute 20
   into a budget calculated with 14.185.

## Conclusion

Under these hypotheses, uniformly on D_k,
\[
 I(z)=e^{\Psi_z(u_s)}
      \sqrt{\frac{2\pi}{-\Psi_z''(u_s)}}\,(1+\varepsilon(z)),
 \qquad |\varepsilon(z)|<0.0158<0.018.                 \tag{1}
\]
The square root uses the principal branch, and epsilon is analytic on
the disk interior. Consequently I has no zero on the closed disk;
I/Gamma(2z+1) has an analytic logarithm in its interior.

This reproduces the inference in the cited Lemma 3.6 **conditionally**.
It does not yet establish its antecedents for the actual moment transform,
import the full cubic wedge, or prove any new coefficient-minor sign.

## Proof

The ready assessment is
`drafts/literature/2026-11-05-uniform-moment-factorization-audit.md`.
The purpose of this reproduction is to check the complete normalization,
contour and branches of the source inference, including constants which
the source delegates to ancillary code. No ancillary file was executed.

### Analytic domain and contour endpoints

On every compact subset of |Im(u)|<pi/8, Re(exp(4u)) has a strictly
positive minimum. The theta series and each of its differentiated
series are dominated there by C n^N exp(-c n^2), for suitable positive
constants. Thus Phi is holomorphic in that strip, including at u=0.
On the positive real axis its superexponential decay at infinity and
boundedness at zero make I holomorphic for Re(z)>-1/2, by local uniform
integrable domination (also after multiplying by powers of log(u)).

Fix z in D_k. Deform the positive real ray into the radial segment
from 0 to v=0.35+iy_s, followed by x+iy_s, x>=0.35. The swept region
lies in Re(u)>0 and |Im(u)|<=0.015, apart from the endpoint 0.
The integrand exp(2z Log(u)) Phi(u) is holomorphic there. Possible
zeros of Phi in the swept region are not singularities of this integrand;
no logarithm of Phi is needed on the radial segment.

For a truncated contour, the small circular connector at radius eta
has integral O_k(eta^(2 Re(z)+1)), uniformly for z in D_k. Indeed
Phi is bounded near zero, the argument factor is bounded for this
fixed compact z-disk, and the arc length is O(eta). Here
2 Re(z)+1>=1.9k+1>0. On the far vertical connector u=X+it,
|t|<=0.015, the theta series is bounded by
\[
 C e^{9X}\exp(-\pi e^{4X}\cos(0.06))
\]
for large X; the remaining power contributes at most exp(O_k(X)).
The vertical length is bounded, so this contribution tends to zero.
Cauchy's theorem on the finite contours and these limits give exactly
the integral over the deformed contour. This argument applies uniformly
for z in each fixed D_k; it does not require a single estimate for all k.

The tube hypothesis and the nonzero first summand give a logarithm
of Phi on the simply connected open tube. Its real-axis normalization
fixes it. Along the horizontal part exp(Psi_z(u)) is exactly the original
integrand. The source initially defines a first-summand phase without
the additive log(pi); here and in (1) the phase is the **full** log(Phi),
so no constant amplitude is lost in changing phases.

### Core window and its Gaussian normalization

The function log(k)/k decreases for k>=10^9, and log(10^9)<21. Hence
\[
 \sigma^2<\frac{21}{4\cdot10^9},\qquad
 2\sigma<1/40,\qquad x_s-2\sigma>0.35.
\]
Taylor's formula along the horizontal segment, using stationarity and
the local third-derivative bound, gives for real |y|<=2
\[
 \Psi_z(u_s+\sigma y)-\Psi_z(u_s)
       =-Ay^2/2+E(y),\qquad
 |E(y)|\le(100\sigma/6)|y|^3
       \le(400/3)\sigma<0.01.                       \tag{2}
\]
For the last strict inequality the square of the upper bound is less
than 7/75000<1/10000. All integration segments in this Taylor formula
stay in the specified local disk.

For Re(A)>=6, the complete complex Gaussian is
\[
 G_A=\int_{\mathbb R}e^{-Ay^2/2}\,dy=\sqrt{2\pi}/\sqrt A.
\]
This follows from the real Gaussian integral and holomorphic continuation
on Re(A)>0; on compact subsets the integrals are dominated by a real
Gaussian. The square root is principal. In particular
\[
 |G_A|\ge\sqrt{2\pi/14.185}>0.665.                 \tag{3}
\]
For example, 14.185(0.665)^2=6.272961625<6.28<2pi.
The absolute Gaussian integral is at most sqrt(pi/3). Therefore (2)
costs, in units |exp(Psi_z(u_s))| sigma, at most
\[
 (e^{0.01}-1)\sqrt{\pi/3}<0.0103.                 \tag{4}
\]
An elementary rational check is e^(1/100)-1<=199/19800 and
sqrt(pi/3)<128/125, using the exponential series and pi<22/7;
their product is 25472/2475000<103/10000. The two omitted Gaussian
tails satisfy Mills' elementary integral bound
\[
 2\int_2^\infty e^{-3y^2}\,dy\le e^{-12}/6<0.000002. \tag{5}
\]
This bound follows by replacing 1 by y/2 in the integral, then
integrating the derivative of exp(-3y^2). Thus no numerical integration
or assumption about cancellation in the true integral is being used.

### Both horizontal tail regions

Write t=x-x_s and delta=1/40. Within |t|<=delta the real part of
the first derivative vanishes at t=0. Integrating the local curvature
bound twice gives Re(Psi_z(u_s+t)-Psi_z(u_s))<=-3t^2/sigma^2.
In particular the portion 2sigma<=|t|<=delta is bounded by
\[
 2\int_2^\infty e^{-5y^2/2}\,dy
       \le e^{-10}/5<10^{-5}                       \tag{6}
\]
in the same normalization as (4). For the numerical inequality,
the exponential series gives e^2>22/3, and (22/3)^5>20000.

Outside |t|<=delta, integrate the global horizontal curvature twice
from x_s to obtain Re(Psi_z(u_s+t)-Psi_z(u_s))<=-b t^2,
where b=(4/5)k/u_k^2. Extending the two remaining intervals to
infinite real tails only enlarges the bound. Since sigma^(-1)<sqrt(k),
\[
 \frac2\sigma\int_\delta^\infty e^{-bt^2}\,dt
 \le\frac{\sqrt k}{b\delta}e^{-b\delta^2}
 <\frac{25\log^2k}{8\sqrt k}
       \exp\!\left(-\frac{k}{125\log^2 k}\right)<10^{-100}. \tag{7}
\]
For the final uniform inequality, log^2(k)/sqrt(k) decreases when
log(k)>4, while k/log^2(k) increases when log(k)>2. At k=10^9,
using log(k)<21 and sqrt(k)>10000, the prefactor is less than 1
and the positive exponent is greater than 18000. Since log(10)<3,
exp(-18000)<10^-100. This verifies the whole range, not a sample.
Equations (6)–(7) give a horizontal tail below 10^-4, as used in
the source budget.

### Radial connector, including its amplitude constant

On the connector, |u|<0.36 and |arg(u)|<=arctan(1/7). Consequently
\[
 |u^{2z}|\le
 \exp\bigl((19k/10)\log(0.36)+(k/10)\arctan(1/7)\bigr)
 <e^{-1.9k}.                                      \tag{8}
\]
For a rational margin, log(25/9)>97/95 and arctan(1/7)<1/7;
thus the exponent is less than -1.94k+k/70<-1.9k.
The logarithm inequality follows from
e<1631/600 and e^(2/95)<95/93, whose product is less than 25/9.
Both exponential bounds follow by summing their positive series and
bounding the remaining ratios geometrically.

We can verify the source's connector bound |Phi|<24 directly.
On the larger rectangle 0<=x<=0.35, |y|<=0.015, put c=cos(0.06).
Here c>0.99 and pi*c>9/4. Each of
e^(9x) exp(-pi*c*n^2*e^(4x)) and
e^(5x) exp(-pi*c*n^2*e^(4x)) decreases for x>=0, by logarithmic
differentiation. Thus, using pi<4 and pi*c>2,
\[
 |\Phi(x+iy)|
 \le\sum_{n\ge1}(2\pi^2n^4+3\pi n^2)e^{-\pi c n^2}
 <44\sum_{n\ge1}n^4 e^{-2n^2}
 \le\frac{44e^{-2}}{1-16e^{-6}}<7<24.             \tag{9}
\]
The geometric majorant uses n^4<=16^(n-1), proved by induction from
(1+1/n)^4<=16, and n^2>=1+3(n-1). For the last bound, e^2>7
gives 44e^-2/(1-16e^-6)<2156/327<7. The series is absolutely
convergent throughout this rectangle. This checks the needed constant
without importing the unreplayed ancillary enclosure.

For the saddle amplitude, |u_s|>19/20 and
|arg(u_s)|<arctan(1/19). Also
\[
 |B(u_s)|\le(5/4)B_0,\qquad
 \operatorname{Re}B(u_s)/2\le125k/168,
\]
using |u_s-u_k|<=3/200<1/20, H_0>=(21/25)B_0 and u_k>1.
The prefactor pi exp(5x_s)|B(u_s)-3| exceeds 1: indeed x_s>0.985,
B_0=2pi exp(4u_k)>294, and |B(u_s)|>(4/5)B_0, so
|B(u_s)-3|>232. The tube bound therefore gives
\[
 \frac1k\log|e^{\Psi_z(u_s)}|
 \ge\frac{21}{10}\log(19/20)
       -\frac1{10}\arctan(1/19)-\frac{125}{168}
       +\frac1k\log(1-\rho)>-0.9.                \tag{10}
\]
For the power term, if log|u_s|>=0 it is nonnegative; otherwise
use Re(z)<=21k/20 and log|u_s|>=log(19/20). Thus that inequality
does not reverse when the logarithm changes sign. To check the margin
in (10), use log(19/20)>=-1/19, arctan(1/19)<1/19 and
log(1-rho)>-2rho. The first three terms then exceed
-11/95-125/168>-0.86, leaving ample room for the last term.

Combining length<0.36, (8)–(10), and (3), the connector relative to
the full Gaussian main term is less than
\[
 \frac{0.36\cdot24}{0.665}\sqrt{k}\,e^{-k}
 <13\sqrt{k}\,e^{-k}<10^{-100}.                  \tag{11}
\]
The last expression decreases for k>1/2. At k=10^9 its prefactor
is less than 10^7, and 10^9>107log(10), proving the displayed
inequality without an ancillary numerical computation.

### Relative error and branches

In units |exp(Psi_z(u_s))| sigma, (4), (5) and the horizontal-tail
bound total less than 0.0103+0.000002+0.0001=0.010402.
Divide by |G_A|>0.665 and add (11). Then
\[
 \left|\frac{I(z)}{e^{\Psi_z(u_s)}\sigma G_A}-1\right|
 <\frac{0.010402}{0.665}+10^{-100}<0.0158<0.018.   \tag{12}
\]
For example, 0.0157*0.665=0.0104405>0.010402; this already
leaves much more room than 10^-100. All constants are used in
one normalization, including the factor sigma from the substitution.

The saddle and full phase are analytic in z, and
Re(-Psi_z''(u_s))>=6/sigma^2>0. The principal square root is
therefore analytic and nonzero; sigma G_A equals the square root
in (1). Define epsilon by this nonzero analytic main term. Its
analyticity follows without differentiating a remainder estimate or
assuming I nonvanishing. Bound (12) then proves nonvanishing of I.
Finally Gamma(2z+1) is holomorphic and nonzero here, and the disk
interior is simply connected, so I/Gamma(2z+1) has an analytic
logarithm. This completes the conditional inference.

**Qualification of source constants.** The proof does not claim a replay
of the source's ancillary values 0.6606 or 0.00734, nor does it need them.
The analytic antecedents and the sharper 14.185 upper bound remain
assumptions. The proof checks their implication and the independent
connector/tail scalar estimates only. Neither Proposition 3.7 nor the
other wedge gates or bounded-k/r positivity has been audited here.

## Mathlib

Full matching coverage is not checked. No formal theorem asserting this
specific theta-moment factorization or its constants is used. Complex
integration, dominated convergence, the Gaussian integral and analytic
logarithms are supporting standard facts, not a formal verification of
the conditional source hypotheses.
