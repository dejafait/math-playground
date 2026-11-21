# C466q — Frozen double-zero stopped weighted flow

## Hypotheses

Fix a finite real a>0. There is one complex normal coordinate q with
unit Euclidean metric and no regular background or tangential variables.
On q!=0 use any local branch of S(q)=-2 log q, and the upward raw
conjugated-gradient convention
\[
 \partial_Tq=\overline{S'(q)}=-2/\overline q,
 \qquad q(0,r)=ir,\quad 0<|r|<a.
\]
The branch affects neither this vector field nor exp(-S)=q^2.
Let J(T,r)=partial_r q(T,r), always holding physical time T fixed,
where the trajectory exists before its first hit of zero. Define the
oriented weighted density there by
\[
 W_T(r)=-q(T,r)^2 J(T,r)/i.
\]
Define W_T to be zero on initial points whose first hit has occurred,
including the hitting boundary, and set W_T(0)=0. This is a definition
of a density, not classical continuation of a trajectory or its
Jacobian through zero. All times in this result are nonnegative.

## Conclusion

The maximal forward nonsingular trajectory, hitting time and fixed-time
Jacobian are
\[
 q(T,r)=i\operatorname{sgn}(r)\sqrt{r^2-4T},\qquad
 T_*(r)=r^2/4,\qquad
 J(T,r)=i\frac{|r|}{\sqrt{r^2-4T}}\quad(0\le T<T_*(r)).             \tag{1}
\]
The full stopped signed density is
\[
 W_T(r)=|r|\sqrt{(r^2-4T)_+},\qquad 0\le W_T(r)\le r^2,          \tag{2}
\]
where x_+=max(x,0). It has zero one-sided traces at every hitting
boundary, although J diverges at a fixed positive-time boundary.
It agrees with ordinary oriented change of variables on each
surviving branch, whose outer endpoints move with T. In particular
\[
 \int_{-a}^a |W_T(r)|\,dr
 =\frac23(a^2-4T)_+^{3/2}\le\frac23a^3.                         \tag{3}
\]
For every Lebesgue measurable E subset (-a,a),
\[
 \sup_{T\ge0}\int_E|W_T(r)|\,dr\le a^2 |E|.                    \tag{4}
\]
Thus this family is uniformly integrable, including near moving
hitting boundaries. Explicitly, for any delta>0 and T_0=a^2/8,
\[
 \sup_{0\le T\le T_0}\int_{|r|<\min(\delta,a)}|W_T(r)|\,dr
 =\frac23\min(\delta,a)^3\longrightarrow0.                     \tag{5}
\]

For fixed r!=0, substitution T=tau r^2 into the fixed-time quantities
in (1) is pre-collision exactly when 0<=tau<1/4, and gives
\[
 q(\tau r^2,r)=ir\sqrt{1-4\tau},\quad
 J(\tau r^2,r)=\frac{i}{\sqrt{1-4\tau}},\quad
 W_{\tau r^2}(r)=r^2\sqrt{1-4\tau}.                             \tag{6}
\]
At tau>=1/4 only the stipulated stopped density exists, with value
zero; there is no claimed classical J there. Differentiating the
composite variable-time curve gives i sqrt(1-4 tau), not the J in (6).

These are a reproduction/specialization of elementary logarithmic
flow machinery. They remove a collision-mass objection only for this
exact frozen model. They provide no actual-function perturbation
estimate, global homology or endpoint control, determinant sign,
all-order positivity or Xi realization.

## Proof

### Source convention and scope

Tanizaki, Nishimura and Verbaarschot, *Gradient flows without blow-up
for Lefschetz thimbles*, JHEP 10 (2017) 100,
[arXiv:1706.03822v2](https://arxiv.org/pdf/1706.03822v2),
27 September 2017, Section 2.2, (2.19)–(2.21) and footnotes 1–2
(printed p6), discuss the leading simple-zero collision and qualify
discarded mass by weight-times-Jacobian control. Appendix B
(B.1)–(B.5), printed p22, gives the real-parameter variational law;
for a flat metric it is dot J=overline(S''(q)J). The conjugation acts
on J too. Those passages supply the convention and the reason to
retain the full Jacobian; their approximate simple-zero example is
not an exact theorem about this double-zero model. The explicit
solution and bounds below are necessary to justify that specialization.

Lawrence and Yamauchi, *Normalizing flows and the real-time sign
problem*, Phys. Rev. D 103 (2021) 114509,
[published PDF](https://scoap3-prod-backend.s3.cern.ch/media/files/62831/10.1103/PhysRevD.103.114509.pdf),
IV.A–IV.B, printed pp5–6, (12)–(21), retain the residual Jacobian
phase and allow nonsmooth collision contours. No global invariance
or positivity theorem is imported from this discussion. The signed
definition above, rather than action phase alone, is what is tested.

### Nonsingular solution and derivative

Write q=iy on the imaginary axis. The vector field there is -2i/y,
so y'=-2/y and (y^2)'=-4. With y(0)=r, the same-sign solution is
y=sgn(r)sqrt(r^2-4T) on the interval in (1). Direct substitution
verifies the full complex equation and initial value. The vector
field -2/overline q is smooth as a real vector field on C minus {0};
the Picard–Lindelof local existence and uniqueness theorem
makes this the unique solution up to its hit. The formula exists
at every earlier time and tends to zero at T_*(r), so the forward
nonsingular interval is maximal. A classical extension through that
time would have q=0 there, outside the vector field's domain.

On either open surviving initial branch, differentiate at fixed T:
\[
 \partial_r\{\operatorname{sgn}(r)\sqrt{r^2-4T}\}
 =\frac{\operatorname{sgn}(r)r}{\sqrt{r^2-4T}}
 =\frac{|r|}{\sqrt{r^2-4T}}.
\]
This proves (1), including J(0,r)=i on both branches. It also checks
the source variational law: S''=2/q^2=-2/(r^2-4T), and both dot J
and overline(S''J) equal 2i|r|/(r^2-4T)^(3/2). No modulus has been
substituted for the signed complex Jacobian.

Since q^2=-(r^2-4T), multiplication in the stated order gives
-q^2J/i=|r|sqrt(r^2-4T). The zero extension gives (2), since T>=0
and sqrt((r^2-4T)_+)<=|r|. For a fixed 0<T<a^2/4 the hitting
initial values are r=+-2sqrt(T). On approach from either surviving
side J/i tends to positive infinity, whereas W_T tends to zero.
The deleted-side density is zero too. At T=0 the density is r^2
and its origin trace is zero. At later times with no survivors it
is zero everywhere. Indeed (2) is jointly continuous in (T,r).
This proves consistency of the weighted extension by its traces,
without assigning a nonexistent derivative at collision or multiplying
such a derivative by a zero weight.

### Change of variables and mass

For 0<=T<a^2/4 put c=2sqrt(T) and b=sqrt(a^2-4T).
The surviving initial branches are (-a,-c) and (c,a), mapped to
the imaginary segments with y in (-b,0) and (0,b), respectively.
At T=0 these descriptions simply omit the origin. On each branch
r maps to y with dy/dr=|r|/sqrt(r^2-4T)>0, so orientation is retained.
The weighted form satisfies exactly
\[
 W_T(r)\,dr=-q^2\,dq/i=y^2\,dy.
\]
Ordinary change of variables first on compact subintervals, followed
by nonnegative monotone limits to the open endpoints, therefore gives
\[
 \int_{-a}^{-c}W_T\,dr=\int_{-b}^{0}y^2\,dy=b^3/3,
 \qquad
 \int_c^a W_T\,dr=\int_0^b y^2\,dy=b^3/3.
\]
The deleted region contributes zero by definition. This proves (3)
for these T; for T>=a^2/4 it follows because every initial point
has hit. Equivalently, direct integration uses
\(\int_c^a r\sqrt{r^2-c^2}\,dr=(a^2-c^2)^{3/2}/3\).
Thus the ordinary density accounts for the full surviving-branch
integral, with no missing boundary mass in this definition.

This calculation does not assert invariance for the original finite
segment: its limiting outer images are +-ib, not +-ia. For
0<T<a^2/4 the derivative of the total mass is
-4sqrt(a^2-4T), so the endpoint motion has a nonzero effect.

### Uniform integrability, and the time distinction

The integrable envelope r^2 in (2) gives (4), uniformly for all T.
For every epsilon>0, |E|<epsilon/a^2 therefore implies
sup_T integral_E |W_T|<epsilon. This includes arbitrary measurable
sets following the hitting boundaries; it is stronger than origin
control alone. Let d=min(delta,a). Replacing a by d in (3) gives
the exact origin mass 2(d^2-4T)_+^(3/2)/3. Its maximum over any
time interval containing zero is 2d^3/3, proving (5) with the explicit
positive T_0 in the conclusion. Joint continuity and the envelope
also imply L1 continuity in physical time by dominated convergence.
In particular at fixed positive T the origin neighborhood is wholly
deleted once delta<=2sqrt(T).

For r!=0, the pre-hit inequality tau r^2<r^2/4 is equivalent to
tau<1/4. Substitution into (1) and (2), after differentiating at
fixed T, proves (6). In contrast the composite curve r maps to
q(tau r^2,r)=ir sqrt(1-4 tau) has derivative i sqrt(1-4 tau).
Its own weighted pullback would be r^2(1-4 tau)^(3/2), a different
quantity from the fixed-time density evaluated in (6). For fixed
tau in [0,1/4), (6) tends quadratically to zero as r tends to zero;
as tau increases to 1/4 the fixed-time J diverges but that weighted
density tends to zero. At and after the hit only the stopped density
is defined. No flow completeness through the singularity is inferred.

The bound sought in review948 is thus met, including the full
measurable-set test. Collision singularity alone is not an obstruction
in this control. None of the argument treats a nonzero analytic
background, a different metric, coupled coordinates, noncompact
ends, or signed cancellation for the actual Xi weight.

## Mathlib

Full matching coverage of this stopped logarithmic-flow result has
not been checked. The proof uses elementary differentiation,
smooth real ODE uniqueness, one-dimensional change of variables and
dominated convergence. No exact Mathlib theorem for the full result
is claimed; unknown availability is not evidence of absence.
