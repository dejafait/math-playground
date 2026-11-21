# C759l: Explicit boundary bound for the complete even shift32 inverse

## Hypotheses

Let I=(-1,1), delta(x)=1-|x|, and let A_e be exactly C759k's
self-adjoint operator of the complete C759a Weil form on the real even
subspace of L2(I). In particular both original poles and all five
masked prime-power translations n=2,3,4,5,7 are retained. Use Lebesgue
measure, zero extension and C759k's compatible bounded-data actions.
Let g be any real even element of L-infinity(I), and put
u=(A_e+32I)^(-1)g. All function-space statements concern equivalence
classes; no continuity or boundary trace hypothesis is imposed.

The prior SPECIALIZE assessment
`drafts/literature/2026-11-13-even-boundary-exit-specialization-839.md`,
separately approved in recovery840, covers this exact target. This is
REPRODUCTION by quantitative specialization of the cited general
results, not a new general boundary theorem.

## Conclusion

With natural logarithms, the explicit finite constant

\[
 C_{\rm boundary}=\frac{200}{\sqrt{\log2\,\log(5/4)}}<640       \tag{1}
\]

satisfies

\[
 |u(x)|\le \frac{C_{\rm boundary}\|g\|_\infty}
                    {\sqrt{\log(e/\delta(x))}}
 \quad\hbox{for almost every }x\in I.                         \tag{2}
\]

This is an unsigned bounded-forcing estimate for the complete operator.
It supplies one weighted error ingredient. It supplies no positive
trial margin, complete lowest-even isolation, ground-state sign or
simplicity, parity ordering, continuous representative, endpoint trace,
or actual-Xi realization. It does not assert that the complete inverse
preserves order. The separate conceptual audit in Proof5 accepts the bound.

## Proof

### 1. Exact reference, full perturbation and forcing budget

Reuse C759k Proof1-5, including its separate conceptual audit. Its killed
reference G has exponent

\[
 \Psi(\xi)=\tfrac12\log(1+\xi^2),
 \qquad \nu(dx)=\frac{e^{-|x|}}{2|x|}\,dx,
 \qquad A_e=G-K.                                             \tag{3}
\]

Here the reference is the Levy process killed on exiting I, with the
part form and supported form-domain equality established in C759k.
It is not Brownian motion killed before subordination. In C759k(4),
K=bI+R+J-P includes the full integrable multiplier correction R, all
five paired masked translations J, and the even restriction P of both
original pole functionals. No term of K is removed here. The already
audited compatible estimates and equation are

\[
 \|K\|_{\infty\to\infty}<24,\qquad
 \|u\|_\infty\le\|g\|_\infty/8,\qquad
 u=R_0(g+Ku),\quad R_0=(G+32I)^{-1}.                          \tag{4}
\]

The equation is in L2 and the terms are the same bounded equivalence
classes. Thus h=g+Ku is real even and bounded, and

\[
 \|h\|_\infty\le\|g\|_\infty+24\|u\|_\infty
                 \le4\|g\|_\infty.                          \tag{5}
\]

This pays the complete perturbation budget using absolute norms. The
reference estimate below applies to signed h; no order property of
A_e is needed.

### 2. Imported global occupation and renewal bounds

Import Grzywny--Ryznar, *Potential theory of one-dimensional geometric
stable processes*, [arXiv:1107.0745v1](https://arxiv.org/pdf/1107.0745v1),
Section3, Proposition3.5 (printed p7), specifically its upper bound
and upper-bound proof. For a symmetric non-compound-Poisson Levy
process, with ladder normalization kappa(z,0)=sqrt(z), it gives

\[
 \mathbb E^y\tau_{(0,R)}
 \le V(\min\{y,R-y\})V(R),\qquad 0<y<R.                      \tag{6}
\]

The upper proof uses nonnegative occupation and half-line domination;
its coefficient is1. Its lower estimate and unspecified lower constant
are not used. This theorem is imported, not reproved.

Import Kwaśnicki--Małecki--Ryznar, *Suprema of Lévy processes*,
Ann. Probab.41(3B)(2013),2047-2065, DOI10.1214/11-AOP719,
[arXiv:1103.0935v3](https://arxiv.org/pdf/1103.0935v3), Theorem4.4
(electronic-reprint pp14-15). Its global upper estimate is

\[
 V(a)\le\frac5{\sqrt{\Psi(1/a)}},\qquad a>0.                 \tag{7}
\]

Its hypotheses are symmetry, not compound Poisson, and monotonicity
of Psi(xi) and xi^2/Psi(xi) for xi>0. Section3 equation(3.1) fixes
local-time constant1; Section4's log-Psi identity before Proposition4.3
uses the same normalized V as(6). The proof of the upper bound includes
the explicit factor5, not an unspecified comparison constant. No
regular-variation onset or lower bound is used.

For (3), symmetry and infinite Levy measure are explicit: integrating
exp(-x)/(2x) near0 diverges, so it is not compound Poisson. Psi is strictly
increasing for xi>0. To check the other monotonicity, put s=xi^2>0.
The derivative of s/log(1+s) has the sign of
log(1+s)-s/(1+s). The latter is0 at s=0 and has derivative
s/(1+s)^2>0. Thus xi^2/Psi(xi)=2s/log(1+s) is increasing as required.

The half-speed normalization is the one checked in L513's normalization
passage and reused in C759k Proof5. Explicitly the normalized ladder
height exponent is

\[
 \kappa_\Psi(a)=\exp\left(\frac1\pi\int_0^\infty
              \frac{a\log\Psi(t)}{a^2+t^2}\,dt\right),
 \qquad\int_{[0,\infty)}e^{-ay}\,dV(y)=1/\kappa_\Psi(a).
                                                                    \tag{8}
\]

Multiplying GR's exponent log(1+xi^2) by1/2 multiplies kappa by
1/sqrt2 and V by sqrt2, because the integral of a/(a^2+t^2) is pi/2.
The product V(.)V(.) and expected exit time both acquire factor2.
Consequently (6) applies unchanged to the half-speed V; (7) is applied
directly to the half-speed Psi in(3). There is no further time factor.
The local-time normalization kappa(z,0)=sqrt(z) is retained.

Translation x->x+1 maps I to(0,2), preserving the reference process
law up to its starting point and its exit time. With R=2, (6)-(7) give
for every interior starting point

\[
 \mathbb E^x\tau_I
 \le V(\delta(x))V(2)
 \le\frac{25}{\sqrt{\Psi(1/\delta(x))\Psi(1/2)}}
 =\frac{50}{\sqrt{\log(1+\delta(x)^{-2})\log(5/4)}}.          \tag{9}
\]

This covers the center delta=1 as well as the full boundary regime.

### 3. Signed discounted occupation and the compatible L2 action

Choose a bounded Borel representative of h with absolute value at most
H=||h||infinity everywhere. Let X be the reference process and define

\[
 U_h(x)=\mathbb E^x\int_0^{\tau_I}e^{-32t}h(X_t)\,dt
       =\int_0^\infty e^{-32t}P_t^Ih(x)\,dt.                 \tag{10}
\]

The killed transition kernel P_t^I and its compatible L2 action T_t
are those already imported in C759k Proof1/3/5 from GR Section2 and
the part-process correspondence. The whole-line transition law has a
Lebesgue density for every t>0, and the killed transition measure is
dominated by that law. Thus altering h on a Lebesgue null set does
not alter P_t^Ih(x) for t>0; integrating time does not introduce a
contribution from t=0. Formula(10) therefore respects bounded
equivalence classes. Tonelli on the absolute integrand, bounded by
H exp(-32t), justifies the signed expectation, time integral and
measurable potential. Positivity is used only for this reference kernel.

We have |U_h|<=H/32, so U_h belongs to L2(I). For any real phi in
L2(I), also phi in L1(I), the absolute double integral is at most
H||phi||_1/32. Fubini, the compatible kernel action at each t, and
C759k(10)'s L2 Laplace-resolvent identity yield

\[
 \int_I\phi(x)U_h(x)dx
 =\int_0^\infty e^{-32t}\langle\phi,T_th\rangle dt
 =\langle\phi,R_0h\rangle.                                  \tag{11}
\]

Hence U_h=R_0h in L2, by testing their L2 difference. This avoids
assuming a common pointwise exceptional set for all t, strong
continuity in L-infinity, or a Bochner integral in that space. In
particular (4) implies u=U_h almost everywhere. If an even representative
is desired, average U_h(x) and U_h(-x); the class and the bounds are
unchanged.

Dropping the discount after taking absolute values is valid for this
reference occupation measure. From(9)-(10),

\[
 |U_h(x)|\le H\,\mathbb E^x\tau_I
 \le\frac{50H}{\sqrt{\log(1+\delta(x)^{-2})\log(5/4)}}.       \tag{12}
\]

### 4. Global logarithmic weight and explicit numerical ceiling

For every0<delta<=1 put t=log(1/delta)>=0. The function
L(t)=log(1+exp(2t)) satisfies L(0)=log2 and
L'(t)=2/(1+exp(-2t))>=1. Since log2<1,

\[
 \log(1+\delta^{-2})\ge\log2+t
 \ge(\log2)(1+t)=(\log2)\log(e/\delta).                    \tag{13}
\]

Thus(5),(12)-(13) prove(1)-(2) almost everywhere for arbitrary signed
even bounded g. There is no endpoint asymptotic substituted for a
uniform inequality.

Finally log2=integral_1^2 ds/s>1/2 and
log(5/4)=integral_1^(5/4) ds/s>1/5. Their product exceeds1/10,
so C_boundary<200sqrt10<640, where the last strict inequality follows
by squaring sqrt10<16/5. This is an analytic certificate of the
numerical ceiling; no sampling or floating-point trust assumption is
needed. The required threshold was a specified finite constant, not
an optimized value. No sign or RH conclusion follows from it.

### 5. Separate conceptual audit, 13 November2026, step843

The prior SPECIALIZE assessment
`drafts/literature/2026-11-13-even-boundary-constant-audit-841.md`,
separately approved842, covers exactly this audit. The bound passes
without changing its hypotheses, constant or almost-everywhere conclusion.
This verifies a local specialization of known results; it establishes
neither a new general theorem nor any of the excluded sign conclusions.

**Primary imports and normalization.** Reopened the versioned PDFs
cited in Proof2. GR's Section3 normalization is on printed pp5-6;
Proposition3.5 and its complete upper-bound proof are on p7. Its
upper coefficient is1, using symmetry and half-line occupation.
KMR's equation(3.1), c=1 and kappa(z,0)=sqrt(z) are on reprint p6;
its renewal-transform and log-exponent identities are on p14.
Theorem4.4 and its upper proof, pp14-15, give coefficient5 globally
under the two stated monotonicities. These are imported results,
not new proofs of general exit-time or renewal theorems.

The shared c=1 normalization identifies the two renewal functions;
neither may be multiplied by an arbitrary constant. In(8) the
log-exponent integral converges: near0 its integrand has only a
logarithmic singularity; at infinity it is O(log(log(t))/t^2).
For Psi=Psi_GR/2 its logarithm changes by -log2, so the logarithm
of kappa changes by -(log2)/2. Uniqueness of the renewal Laplace
transform gives V=sqrt2 V_GR. Pathwise time rescaling makes the
exit time twice as large, agreeing with the product of the two V
factors. Applying(7) to this Psi already pays that factor. No extra
factor2 belongs in(9). L513 supplies precisely this normalization,
without importing its separate signed trace conclusion.

The process is symmetric and has infinite Levy measure. With
s=xi^2, the derivative of s/log(1+s) has positive numerator
log(1+s)-s/(1+s), whose derivative is s/(1+s)^2 and value at0
is0. Both KMR monotonicities hold on the entire required interval.
Translation gives interval length2, not1; thus Psi(1/2) is
half log(5/4). Combining the two coefficient5 bounds yields25,
and the two half-exponents yield the coefficient50 in(9).

**Full forcing.** C759k(4),(9),(12) and its Proof5 give the same
compatible L2/L-infinity equation u=R_0(g+Ku). Its K includes
the multiplier remainder, all five paired masked shifts, and the
even restriction of both poles with their actual sign. Consequently
H=||g+Ku||infinity<=||g||infinity+24||u||infinity
<=4||g||infinity. No favorable pole is dropped, and no order
preservation of the complete inverse is used. The strict norm
bound below24 may safely be relaxed to24 in this estimate.

**Signed occupation and equivalence classes.** GR Section2,
printed pp3-4, supplies the transition-density mixture and killed
kernel domination. Half speed preserves absolute continuity at
every t>0. For a Lebesgue null set N and every starting x,
P^x(X_t in N,t<tau_I)=0 for t>0. Tonelli gives zero expected
discounted occupation of N. Hence replacing a bounded Borel h on
a null set leaves(10) unchanged, even though paths can visit N.
The time singleton0 has zero integration measure. No boundedness
of the transition density on its diagonal is required.

Choose a representative bounded everywhere by H; such a Borel
representative exists for an essentially bounded Lebesgue class.
The absolute expected discounted integral is at most H/32, which
justifies the signed expectation/time interchange and gives a
bounded measurable U_h. For every real phi in L2(I), finiteness
of I gives phi in L1(I), and the absolute space-time integral is
at most H||phi||_1/32. Fubini is therefore valid. At each t the
killed-kernel action agrees in L2 with T_t by C759k's part-form
identification. Pairing first in space gives(11), independently
of how its time-dependent null sets vary. The L2 Laplace identity
then identifies U_h with R_0h; testing their L2 difference proves
equality of classes. C759k's equation identifies this class with u.
This pays the full signed passage without an L-infinity C0 or
Bochner-integral assumption, continuity, or pointwise traces.

**Whole boundary range and ceiling.** Absolute values followed by
discount removal give |U_h(x)|<=H E^x tau_I for every interior x.
For t=log(1/delta)>=0, L'(t)>=1 implies
L(t)>=log2+t>=(log2)(1+t); equality at t=0 is allowed.
Thus no asymptotic estimate replaces the all-delta inequality(13).
The resulting coefficient is exactly 50 times4 divided by
sqrt(log2 log(5/4)). The strict integral estimates log2>1/2
and log(5/4)>1/5 imply its bound by200sqrt10<640, since
400000<409600. The required threshold, a specified finite
constant valid for every0<delta<=1, is met analytically.

All mathematical inputs remain L513's normalization and C759k,
with the two primary theorems cited directly above. No dependency
is added. This audit needs no numerical script. The estimate
still assumes bounded forcing; it does not show that an arbitrary
L2 eigenfunction is bounded. Positive trial margin, complete even
isolation, parity and actual-Xi realization remain unresolved.

## Mathlib

Full matching theorem and supporting Mathlib coverage were not checked.
The cited exit-time and renewal theorems are imported with their exact
hypotheses; only the interval, speed, global weight, full forcing budget
and compatible signed occupation specialization are supplied here.
Unknown coverage is not absence, and no formal verification is claimed.
