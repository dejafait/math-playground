# C466r — Regular-background stopped weighted density

## Hypotheses

Let 0<a<R<infinity and let H be holomorphic on D_R={q in C:|q|<R}.
Fix finite nonnegative M_1,M_2 such that |H'(q)|<=M_1 and
|H''(q)|<=M_2 throughout D_R. Retain the finite complex value H(0)
in the data. On the punctured disk use the unit flat metric and
the upward raw conjugated-gradient flow
\[
 S(q)=-2\log q+H(q),\qquad
 \dot q=\overline{S'(q)}=-2/\overline q+\overline{H'(q)},
 \qquad q(0,r)=ir,\quad 0<|r|<a.                              \tag{1}
\]
The logarithm may be chosen locally: its derivatives and
F(q)=exp(-S(q))=q^2 exp(-H(q)) are single valued on the punctured
disk. No tangential coordinates or metric change are allowed.

For each r!=0 let [0,tau(r)) be the maximal forward interval in
D_R minus {0}. At finite tau stop at the limiting first zero hit
or first disk escape, including escape approached only as a limit.
Before that time let J(T,r)=partial_r q(T,r), with physical T held
fixed. Define
\[
 W_T(r)=-q(T,r)^2e^{-H(q(T,r))}J(T,r)/i\quad(T<\tau(r)),         \tag{2}
\]
and set W_T(r)=0 for T>=tau(r), and W_T(0)=0. This is a stipulated
stopped density, not a continuation of the classical flow or its
Jacobian through a singularity. The proof below shows that these
conventions are well defined and give a measurable density.

## Conclusion

Put K=M_2+M_1^2. For every finite T_0>=0 and 0<=T<=T_0,
\[
 |W_T(r)|\le C(T_0)r^2\quad(-a<r<a),\qquad
 C(T_0)=\exp\{KT_0-\Re H(0)+M_1a\}.                           \tag{3}
\]
In particular, for every Lebesgue measurable E subset (-a,a),
\[
 \sup_{0\le T\le T_0}\int_E |W_T(r)|\,dr
 \le C(T_0)\int_E r^2\,dr
 \le C(T_0)a^2|E|.                                           \tag{4}
\]
Thus omega(s)=C(T_0)a^2 s is a uniform-integrability modulus.
One explicit positive choice required by the target is T_0=a^2/8;
in fact every finite time horizon works. The constants are uniform
over all H with the specified derivative bounds and specified H(0).
If only Re H(0)>=b is specified, replace -Re H(0) by -b. R enters
through the domain and a<R; no additional dependence on R is needed.

This proves the arbitrary-measurable-set target, including sets near
moving hitting and escape boundaries, rather than only origin mass.
It concerns absolute integrability of the full signed density and
does not assert its positivity, continuity across an escape, integral
invariance, classical continuation after stopping, or completeness.
Tangential coupling, coordinate metric changes, global homology,
outer endpoints, all-degree signs and actual-Xi transfer remain open.
This is a local estimate not supplied by the inspected source
passages; no claim of established originality or RH resolution is made.

## Proof

### Source convention and the required specialization

Tanizaki, Nishimura and Verbaarschot, *Gradient flows without blow-up
for Lefschetz thimbles*, JHEP 10 (2017) 100,
[arXiv:1706.03822v2](https://arxiv.org/pdf/1706.03822v2),
27 September 2017, Appendix B, (B.1)–(B.5), printed p22, gives the
real-parameter variational law. Its flat-metric, one-variable case is
\[
 \dot J=\overline{S''(q)J},\qquad J(0,r)=i.                    \tag{5}
\]
The conjugation acts on J as well as S''. The hypotheses for this
local specialization hold on every compact subset of the punctured
disk, where the branch derivatives are holomorphic and the vector
field is smooth. Global thimble assumptions are not used.

The same source, Section 2.2, (2.19)–(2.21) and footnotes 1–2,
printed p6, drops regular terms in its simple-zero collision example
and qualifies discarded mass by weight-times-Jacobian control. It
does not supply (3) for the present arbitrary H class. Sections
3.1–3.2, printed pp7–9, change the metric and do not prove the raw
flow statement here. The estimate below is the necessary additional
specialization of the imported variational machinery, not a reproof
of those source theorems. C466q is the exact H=0 comparison control;
its conclusion is not a premise of the proof below.

### Lifetimes, derivatives and measurability

Regard C as R^2. The vector field in (1) is smooth on
U=D_R minus {0}. The Picard–Lindelof existence and uniqueness
theorem, its maximal-continuation theorem, and smooth dependence of
smooth ODE solutions on initial data give a unique maximal solution
and a smooth flow on its open time-initial-data domain. For every
fixed surviving (T,r), the trajectory on [0,T] is a compact subset
of U. Local smooth dependence therefore applies to a neighborhood
of this initial ir throughout that interval. Its derivative along
the initial curve is the fixed-time J in (5).

Here finite maximal lifetimes have exactly the stated stopping
interpretation. Along (1), with rho=|q| and h=H'(q),
\[
 \frac{d}{dT}\rho^2=-4+2\Re(qh),\qquad
 \left|\frac{d}{dT}\rho^2\right|\le4+2RM_1.                  \tag{6}
\]
If tau(r)<infinity, this Lipschitz bound gives a limit of rho^2 as
T increases to tau, hence a limit ell of rho in [0,R]. If ell=0,
q tends to zero. If ell>0, then near tau the speed is bounded by
2/rho+M_1, so q is Cauchy and has a limit q_* of modulus ell.
When 0<ell<R, this limit lies in U and local existence at q_* would
extend the solution beyond tau, contradicting maximality. Hence the
only remaining finite endpoint is ell=R, with q_* on the disk
boundary. This proves that finite lifetime means a first limiting
zero hit or escape, without presupposing an extension of H outside
the disk. No earlier zero or escape is possible inside the maximal
interval in U. Infinite lifetimes require no stopping event.

The survivor set
\[
 \mathcal U=\{(T,r):T\ge0,\ 0<|r|<a,\ T<\tau(r)\}
\]
is relatively open in [0,infinity) times (-a,a): this follows by
pulling back the open flow domain along r maps to ir. The formula
in (2) is smooth on this domain, with relative continuity at T=0.
Extending it by zero on the complement gives a jointly Borel
function. To see this without any boundary regularity, the inverse
image of an open subset of C is its relatively open inverse image
inside the Borel set mathcal U, together with the complement of
mathcal U if that open subset contains zero. Both are Borel.
Each time slice is therefore measurable, including after the
stipulated value at r=0. No differentiability of tau or regularity
of the survivor boundary is required.

### Differential estimate for the full weighted density

Fix r!=0 and any surviving time interval. Set
f=S'=-2/q+h and g=S''=2/q^2+H''(q). Since F'/F=-f, (1) implies
\[
 \dot F=F'\overline f=-|f|^2F,\qquad
 \frac{d}{dT}|F|^2=-2|f|^2|F|^2.                             \tag{7}
\]
This calculation uses the analytic F, so introduces no logarithm
branch or phase-choice ambiguity. By (5),
\[
 \frac{d}{dT}|J|^2
 =2\Re\{\overline J\,\overline{gJ}\}
 \le2|g||J|^2.                                              \tag{8}
\]
Work with Y=|FJ|^2=|W_T(r)|^2. Equations (7)–(8) give
\[
 \dot Y\le2(|g|-|f|^2)Y.                                    \tag{9}
\]
This squared-norm computation needs neither division by J nor an
assumption that the real initial variation stays in a fixed direction.

For rho>0, the exact identity
\[
 |f|^2=4/\rho^2-4\Re(qh)/\rho^2+|h|^2
\]
and the triangle bound |g|<=2/rho^2+M_2 imply
\[
 \begin{aligned}
 |g|-|f|^2
 &\le M_2-2/\rho^2+4\Re(qh)/\rho^2-|h|^2\\
 &\le M_2-2/\rho^2+4|h|/\rho-|h|^2\\
 &=M_2+|h|^2-2(1/\rho-|h|)^2\\
 &\le M_2+M_1^2=K.                                         \tag{10}
 \end{aligned}
\]
In particular the singular terms have a uniform upper bound as
rho decreases to zero. No lower cutoff for rho, lower bound for
|f|, smallness of H, or separation from a critical point is assumed.

The differential Gronwall inequality applied to (9)–(10), on any
closed subinterval [0,T] of the maximal interval, now gives
\[
 |W_T(r)|\le e^{KT}|W_0(r)|
 =e^{KT}r^2e^{-\Re H(ir)}.                                   \tag{11}
\]
Every surviving T is such an endpoint. The constant K is independent
of the compact interval and its distance to zero or the disk
boundary; thus no singular cutoff limit is being suppressed.

The straight segment from 0 to ir lies in D_R and the fundamental
theorem of calculus gives
\[
 H(ir)-H(0)=\int_0^1 H'(tir)\,ir\,dt,\qquad
 |H(ir)-H(0)|\le M_1|r|\le M_1a.                             \tag{12}
\]
Equations (11)–(12) prove (3) on survivors. On every stopped point,
including the entire hitting or escape boundary, and at r=0, (3)
holds because the density is defined to be zero. In particular no
boundary trace of the unstopped Jacobian is assigned or multiplied
by a vanishing weight.

### Measurable-set and class-uniform conclusion

Integrating the pointwise bound (3) over any Lebesgue measurable E
gives (4), since |r|<a. Its constant is independent of T in [0,T_0],
so the same bound holds after taking the supremum. The linear
omega(s) tends to zero with s and is finite. The envelope also
gives total absolute mass at most 2C(T_0)a^3/3. It works equally
for sets chosen near any moving stopping boundary; no description
of that boundary entered the bound.

All estimates used only the common R,a,H(0),M_1,M_2 and T_0;
the trajectories, lifetimes and survivor domains themselves may
depend on H. Consequently (4) holds also after a supremum over
all backgrounds with those data, without assuming any common
survivor domain. The class-uniform quantifier is therefore proved.

For H=0 the coefficient K vanishes and (11) reduces to the
envelope |W_T(r)|<=r^2, consistent with C466q. For nonzero H the
density in (2) can be complex. Estimating its modulus has not
replaced it by a positive density in any signed integral. Nothing
here asserts that the integral on an evolving stopped curve equals
the original one or that the outer endpoint costs vanish.

### Independent conceptual audit954 — 14 November 2026

The audit under assessment952, separately approved at step953,
accepts (3)–(4) under exactly the stated hypotheses. No bound or
hypothesis is changed. This verifies the existing specialization;
it is not a new mathematical result beyond that proof or a claim
of originality relative to uninspected literature.

For the fixed-time variation, differentiation of the real smooth
vector field gives
partial_r overline(f(q))=overline(g(q)J), including the conjugation
on J. The initial derivative is i for both signs of r. Directly,
W_0=r^2 exp(-H(ir)), so its modulus is the initial value used in
(11). The signed prefactor in (2) has unit modulus and does not
alter the estimate. In (8) the exact derivative is
2 Re(overline(g) overline(J)^2); its upper bound is valid even if
J vanishes. The scalar identity f=(-2+qh)/q verifies the cross term
in (10) for complex q and h, without a reality assumption. The
completed square is therefore valid with the stated constant K.
Gronwall applies on each compact time interval before tau, with
the same K for every interval; no limit theorem at tau is invoked.

For completeness of the endpoint argument, at a positive radial
limit ell the eventual speed bound can be taken to be
4/ell+M_1. Hence
|q(t)-q(s)|<=(4/ell+M_1)|t-s| for sufficiently late s,t<tau.
This proves a unique complex endpoint, not merely a radial limit.
If 0<ell<R, the integral equation extends continuously to tau and
the smooth vector field at q_* supplies the local continuation,
contradicting maximality. If ell=R, no continuation outside D_R is
used. If ell=0, the radial limit itself gives q->0. The uniform
Lipschitz estimate for rho^2 in (6) excludes a missing case with
no radial limit. Thus stopping at every finite tau is well defined.

For the measurable extension, the standard smooth maximal flow
domain in time and initial position is open. Its pullback to the
initial curve, restricted to nonnegative time, is precisely the
relative-open set mathcal U. This includes the relative neighborhoods
at T=0; r=0 is outside the domain. The inverse-image argument above
proves joint Borel measurability even at an irregular survivor
boundary. It does not require a continuous lifetime function or
matching traces at an escape. At tau the assigned value is zero,
so extending (3) uses only that definition, not a boundary limit of J.

Finally, let mathcal H be the class sharing the stated bounds and
H(0), or the stated lower bound b for its real part. For each fixed
Lebesgue measurable E the proof gives, with the corresponding C,
\[
 \sup_{H\in\mathcal H,\ 0\le T\le T_0}
 \int_E |W_T^H(r)|\,dr
 \le C(T_0)\int_E r^2\,dr\le C(T_0)a^2|E|.
\]
This is a supremum of numbers all bounded by the same envelope;
there is no exchange of a supremum with an integral and no
measurability assumption on the indexing class. Equivalently, any
choices of measurable sets E_{H,T} of measure at most s have each
integral at most C(T_0)a^2 s. The total-mass bound stated above
also supplies the boundedness part of uniform integrability.
The argument remains valid for T_0=0 and for every finite positive
T_0; it does not assert a bound uniform as T_0 tends to infinity.

C466q was checked as a comparison only; it supplies no premise of
this proof. The direct mathematical inputs remain the cited local
variational law and the named smooth ODE and Gronwall theorems, so
the empty DAG row is unchanged. The audit found no counterexample
or proof error and made no inference of a zero trace, L1 continuity
at escapes, a conserved signed integral, a positive density, metric
invariance, or a global contour. Those claims are outside (3)–(4).

## Mathlib

Full matching coverage of this stopped logarithmic-flow estimate
has not been checked. The inputs are the standard smooth real ODE
existence/continuation/dependence theorems, the cited flat-metric
variational law, the differential Gronwall inequality, elementary
complex differentiation, and integration of a measurable envelope.
No exact full-result Mathlib theorem is claimed; unknown coverage
is not evidence of absence. The informal proof and its scope were
independently audited at step954; this is not a formal verification.
