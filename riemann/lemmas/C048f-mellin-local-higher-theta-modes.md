# Corollary C048f: the finite horizontal higher-theta-mode allowance

## Hypotheses

Use exactly C048c's parameters and principal branches:

\[
 r=|p|,\quad L=\log r\ge12,\quad \Re p\ge-r/(4L),\quad
 w=W_0(2p/\pi)=U+iV,\quad u_0=w/2,\quad d=1/(3L),
\]
\[
 h_p(u)=2p\operatorname{Log}u-\pi e^{2u},\quad
 g(u)=8\pi^2e^{9u/2}/u,\quad K(s)=g(u_0+s)/g(u_0),\quad
 A_0=-h_p''(u_0)/2.
\]

Every integration below is over real s from -d to d. Define

\[
 R_{\rm modes}(u)=\sum_{n=2}^{\infty}
 \left[n^4-\frac{3n^2}{2\pi e^{2u}}\right]
                  e^{-\pi(n^2-1)e^{2u}},
\]
\[
 T_{\rm modes}(p)=
 \frac{\left|\int_{-d}^{d}K(s)R_{\rm modes}(u_0+s)
                   e^{h_p(u_0+s)-h_p(u_0)}\,ds\right|}
      {|\sqrt{\pi/A_0}|}.
                                                        \tag{1}
\]

The Gaussian square root is principal. Convergence is justified below.
This is the operational finite local contribution in assessment1635,
not a full-path integral or an author-defined symbol T_modes. No
frequency-cell perturbation factor is included.

The source claim being reproduced is K. Kawano, *Logarithmic
Inequalities of Arbitrary Order for the Riemann Xi Coefficients*,
[Preprints.org202611.0383v1, posted4 November2026,
DOI10.20944/preprints202611.0383.v1](https://www.preprints.org/manuscript/202611.0383/v1),
Section5.2(28)/Lemma5.1(i), AppendixA.2(A3), AppendixB's unnumbered
B_modes and real t>=1 theta-series displays, and AppendixC's remaining
local-mode allocation. Source-notes1636 records the inspected primary
hypotheses. The source is not peer reviewed. Its claimed allowance is
a conclusion to verify, not an assumption. The unchanged SPECIALIZE
assessment1635 was available before this reproduction in step1637.

## Conclusion

The full series and the finite integral in (1) are well defined, and
throughout the stated closed sector

\[
 T_{\rm modes}(p)\le112\sqrt L\,e^{-5r/L^2}.            \tag{2}
\]

In fact the proof bounds the integral of the absolute integrand by the
same normalized allowance; it does not rely on cancellation of modes.
This is REPRODUCTION of the source's stated component, with an
operational-definition qualification, independently checked in
conceptual audit1639 below. No result beyond the checked source claim is asserted.
Horizontal tails, full Mellin assembly, zero counts, inversion and a
sufficient Mellin-to-sign bridge remain separate. In particular (2)
does not establish actual-Xi all-degree mixed positivity or RH.

## Proof

### 1. Reused sector estimates and the real theta parameter

C048c(6)-(12),(19) supplies, on the whole segment,

\[
 |w|<L,\quad \cos V>1/L,\quad
 v_0:=\pi e^U\cos V>2r/L^2,\quad \Re(u_0+s)>1,
 \quad |\Im(u_0+s)|<\pi/4,                              \tag{3}
\]
\[
 |K(s)|<29/25,\quad |A_0|<6r/L,\quad \Re A_0>0,
 \quad \left|e^{h_p(u_0+s)-h_p(u_0)}\right|
                    \le e^{-b_*s^2},\qquad
 b_*=\frac{799}{300}\frac r{L^2}>0.                    \tag{4}
\]

For the phase inequality in (4), use the exact decomposition
h_p(u_0+s)-h_p(u_0)=-A_0s^2+Z(s) in C048c and then its
-Re(A_0)s^2+|Z(s)| bound(19). It holds also at s=0.
No different-saddle amplitude estimate from L799 is used.

Since s is real, the relevant theta parameter is the positive real
number

\[
 \tau(s):=\Re(\pi e^{2(u_0+s)})=v_0e^{2s}.
\]

For |s|<=d and L>=12, the elementary exponential inequality gives

\[
 e^{2s}\ge e^{-2d}\ge1-2d\ge17/18,
 \qquad
 \tau(s)>\tau_0:=\frac{17}{9}\frac r{L^2}>1.          \tag{5}
\]

For the last prerequisite, the derivative of e^L/L^2 is
(e^L/L^2)(1-2/L)>0 on L>=12, and
 e^12>2^12=4096>144. Thus r/L^2>1 throughout the ray.
This establishes the real t>=1 hypothesis before using a theta-series
bound, uniformly also as L tends to infinity.

### 2. Complete series domination and legitimate finite integration

By L799's strip convergence proof and identity(4), R_modes is a normally
convergent holomorphic series on |Im u|<pi/4: it is precisely the
n>=2 part of that identity. That argument is independent of L799's
saddle or rotated-diameter estimates. More explicitly, on a compact
subset of this strip, Re(pi e^{2u}) has a positive minimum delta,
while the coefficient 3/(2pi e^{2u}) and exp(pi e^{2u}) are bounded.
The summands are bounded by C(n^4+n^2)e^{-delta n^2}. This majorant
sums, since its consecutive-term ratio tends to zero. The Weierstrass
M-test gives uniform absolute convergence on that compact set. Our
whole finite segment is compact strictly inside the strip by (3).
All other factors in (1) are continuous there. Hence the summed
integrand is continuous and integrable. If termwise integration is
used, the integral of the difference from a partial sum is bounded by
2d times its uniform error times the bounded remaining factors and
tends to zero. We can instead apply domination directly to the sum,
as below. No boundary of the strip or infinite contour is integrated.

The coefficient of each higher mode is the one in L799(4).
Dividing the n-th theta summand by its positive-power n=1 factor
4pi^2 exp(9u/2-pi exp(2u)) gives exactly

    [n^4-3n^2/(2pi exp(2u))] exp(-pi(n^2-1)exp(2u)).

The additional common factor 2/u in C048c's leading amplitude cancels
in this ratio. Thus no n^4, Jacobian or exponential factor is lost in
(1). C048c(3) also identifies its full leading normalization with S(p):
|S(p)|=|g(u_0)exp(h_p(u_0))| |sqrt(pi/A_0)|. This explains the local
relative contribution without assuming a global contour identity.

For Re u>1 and pi>3,

\[
 a(u):=\left|\frac3{2\pi e^{2u}}\right|
             =\frac3{2\pi}e^{-2\Re u}<1/2.
\]

Therefore, writing t=tau(s)>1 and using n^2<=n^4,

\[
 |R_{\rm modes}(u_0+s)|
 \le\sum_{n=2}^{\infty}(n^4+a(u_0+s)n^2)e^{-(n^2-1)t}
 \le\frac32\sum_{n=2}^{\infty}n^4e^{-(n^2-1)t}.        \tag{6}
\]

Here is a verification of the real-series bound printed in AppendixB,
with precisely its required t>=1 case. Put q_n=n^4e^{-(n^2-1)t}.
For every n>=2 and t>=1,

\[
 \frac{q_{n+1}}{q_n}
 =\left(1+\frac1n\right)^4e^{-(2n+1)t}
 \le\frac{81}{16}e^{-5}<\frac1{10}.                   \tag{7}
\]

Indeed the positive exponential series gives e>2 and e^2>7
(the terms through degree4 at 2 sum to7, with positive remainder).
Thus e^5=e(e^2)^2>98 and 81/(16*98)=81/1568<1/10.
Geometric summation of all terms gives

\[
 \sum_{n=2}^{\infty}q_n
 \le\frac{16}{1-1/10}e^{-3t}
 =\frac{160}{9}e^{-3t}<32e^{-3t}.                     \tag{8}
\]

This verifies the whole infinite tail, rather than only its first
term. Combining (5),(6),(8) yields the uniform pointwise estimate

\[
 |R_{\rm modes}(u_0+s)|
 \le48\exp\left(-\frac{17}{3}\frac r{L^2}\right).
                                                               \tag{9}
\]

### 3. Absolute finite integral, complex normalization and constants

Apply (4) and (9), preserving the actual finite integral. The integral
of its absolute integrand is at most

\[
 48\frac{29}{25}e^{-17r/(3L^2)}
                    \int_{-d}^{d}e^{-b_*s^2}\,ds
 \le48\frac{29}{25}e^{-17r/(3L^2)}\sqrt{\pi/b_*}.      \tag{10}
\]

Only the nonnegative real Gaussian majorant has been extended to the
real line. The real Gaussian formula is the specialization of
[NIST DLMF7.7.6](https://dlmf.nist.gov/7.7.E6) with its coefficient
 a=b_*>0 and b=c=x=0, followed by evenness. This is the same covered
Gaussian input as in C048c. There is no deformation, complex-Gaussian
modulus integral identity or theta-series interchange at infinity.

The triangle inequality bounds the numerator in (1) by (10).
Since |sqrt(pi/A_0)|=sqrt(pi/|A_0|), division gives

\[
 T_{\rm modes}(p)
 \le48\frac{29}{25}\sqrt{\frac{|A_0|}{b_*}}
                              e^{-17r/(3L^2)}
 \le48\frac{29}{25}\sqrt{\frac{1800}{799}}\sqrt L
                              e^{-17r/(3L^2)}.         \tag{11}
\]

In particular the normalization uses |A_0|, not Re A_0, in its numerator.
The exact scalar comparisons needed are

\[
 \frac{1800}{799}<\frac{64}{25}
 \quad(45000<51136),\qquad
 48\frac{29}{25}\frac85=\frac{11136}{125}<112,
 \qquad \frac{17}{3}>5.                               \tag{12}
\]

All quantities being squared or compared are positive. Equations
(11)-(12) imply (2), with explicit slack in both coefficient and
exponential rate. These stronger intermediate estimates are used only
to reproduce the printed allowance; no beyond-source conclusion is
claimed.

All input bounds and (5)-(12) hold on the full closed sector. In
particular r=e^12, positive real p, either angular boundary and
arbitrarily large r are included. Negative imaginary p is covered by
the even-in-V quantities in (3) and by complex moduli; equivalently
one can conjugate the principal branches. The permitted real p is
positive, and no step divides by Im p or V. The argument proves a
uniform finite local absolute budget with no assumptions about
horizontal tails, any zero, inversion or sufficient signs.

### Independent conceptual audit1639 — 19 November 2026

The unchanged SPECIALIZE assessment1637 covers exactly (1)-(2),
including the stronger absolute-integral assertion. The full proof,
C048c's relevant geometry, normalization and absorption argument, and
L799's strip convergence and identity(4) were checked using the saved
primary-source coverage in source-notes1636. The audit passes without
a mathematical correction or an additional hypothesis. This is local
verification of a source reproduction, not progress beyond the checked
source claim or a verification of its complete Mellin argument.

**Input applicability and the moving sector.** C048c's parameters are
identical, including d=1/(3L), the principal Lambert branch and the
closed sector. Its identities pi e^U=2r/|w| and cos V>1/L imply
v_0>2r/L^2. Its (11) puts the entire segment in Re u>1 and strictly
inside |Im u|<pi/4. Its exact phase decomposition and (19) give

    Re(h_p(u_0+s)-h_p(u_0))
      =-Re(A_0)s^2+Re Z(s)
      <=-Re(A_0)s^2+|Z(s)|<=-b_*s^2.

Here 39/10-371/300=799/300>0. In particular no assumption that
Z(s) is small is needed; at s=0 both sides are zero. The bounds on
K and |A_0| are from the same segment and same phase, not L799's
different saddle. Principal roots and g(u_0) are nonzero by C048c.

For every fixed p the closed segment is a compact subset of the open
theta strip. On an arbitrary compact subset, delta>0 and the bounded
coefficient in the displayed normal-convergence proof provide a
summable bound for every n>=2. Thus the locally uniform holomorphic
series and any finite termwise integration used here are legitimate.
There is no assertion of a single compact set or fixed strip clearance
for all unbounded p. Uniformity of (2) follows instead from (3)-(12),
which hold for every allowed p with the same constants. No limit in p
is interchanged with the sum or integral.

**Real theta parameter and the complete tail.** Taking the real part
of pi exp(2(u_0+s)) gives v_0 exp(2s), because s is real.
Since 2d<=1/18, exp(2s)>=17/18 throughout the interval. The
monotonicity calculation in (5) and 4096>144 establish r/L^2>1
on the whole radial ray, so tau>17r/(9L^2)>1 before the series
estimate is applied. The coefficient modulus is bounded by
n^4+a(u)n^2, with a(u)<1/2, hence by (3/2)n^4. The sign of a
complex coefficient is never used.

For every n>=2 the ratio in (7) is at most (81/16)exp(-5);
the positive exponential series gives exp(2)>7 and exp(1)>2,
so it is less than 81/1568<1/10. The first term is
16 exp(-3t), and summing the entire geometric majorant gives
(160/9)exp(-3t)<32 exp(-3t). This checks every term of the
infinite series and yields exactly (9), with 3*(17/9)=17/3.
No first-mode correction is counted in R_modes: the n=1
negative term remains a separate contribution.

**Amplitude and absolute normalization.** Dividing L799's nth
theta summand by 4pi^2 exp(9u/2-pi exp(2u)) leaves exactly the
coefficient and exponential in R_modes. Multiplying numerator and
leading term by the same 2/u preserves that ratio. Translation
u=u_0+s has du=ds. C048c(3) therefore gives the stated local
relative normalization, with neither an extra Jacobian nor an
assumed global Mellin identity. The operational interpretation of
T_modes remains qualified: this symbol is defined here, not in the
source, and excludes its frequency-cell perturbation factor.

The bounds apply pointwise to the absolute integrand. Since b_*>0,
the real specialization a=b_*, b=c=x=0 of DLMF7.7.6 and
evenness give sqrt(pi/b_*). Only that nonnegative Gaussian is
extended to the real line. Division by the actual root modulus
sqrt(pi/|A_0|) gives sqrt(|A_0|/b_*), including for nonreal A_0.
Consequently (11) bounds the normalized integral of the absolute
integrand itself, and the triangle inequality then proves (2).

The exact coefficient checks have positive margins
51136-45000=6136 and 112-11136/125=2864/125; the exponent
margin is 17/3-5=2/3. These elementary exact comparisons need
no numerical certificate or parameter sampling. All radial bounds
include L=12 and have no upper cutoff. The inherited strip and
curvature slack holds at both angular boundaries. Conjugation
preserves the principal branches and the moduli used here;
real p in this sector is positive, and no step divides by V.

The mathematical inputs remain C048c and the independent strip-series
part of L799; their existing DAG row needs no change. This audit
does not import L799's final amplitude estimate or its saddle
hypotheses. Horizontal tails, full assembly, zero counts, inversion,
and sufficient actual-Xi mixed signs are still unproved here.
There is no complete RH candidate.

## Mathlib

Full matching coverage is unchecked; no absence claim or formal
verification is made. Supporting mathematics consists of the strip
normal-convergence argument from L799, C048c's audited geometry and
phase bounds, the Weierstrass M-test, geometric summation and the precise
real Gaussian specialization above. The source's printed series bound
and local allowance were reverified because its inspected text leaves
the uniform parameter-specific finite-integral specialization implicit.
