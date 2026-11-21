# C466v — Affine small-background sign at every surviving time

## Hypotheses

Fix 0<a<R<infinity, 0<b<L<infinity, T_0>0, H_0 real,
and arbitrary complex coefficients A,B. On the bidisk
U_0={|q|<R, |z|<L} set
\[
 H(q,z)=H_0+Aq+Bz.
\]
Choose M_1>=sqrt(|A|^2+|B|^2), put M_2=0, and suppose
\[
 M_1T_0<\min\{R-a,L-b\},\qquad
 \epsilon=M_1\sqrt{a^2+b^2}\le1/100.                 \tag{1}
\]
These are whole-bidisk bounds: the holomorphic gradient is the
constant vector (A,B), and the holomorphic Hessian is zero. Every
affine member of the proposed class with a possibly larger M_2
also satisfies (1) after choosing its exact Hessian bound zero.
There is no reality condition on A or B.

Use C466s's unit flat raw flow, first maximal lifetime in
U=U_0 minus {q=0}, and fixed-physical-time parameter derivatives:
\[
 \dot X=\overline{(-2/q+A,B)},\quad X(0,r,s)=(ir,s),
 \quad |r|<a,\ |s|<b,\ r\ne0,
\]
\[
 J_t=[\partial_rX,\partial_sX],\quad F=q^2e^{-H},\qquad
 W_t=-F(X(t))\det_{\mathbb C}J_t/i \quad(t<\tau(r,s)).   \tag{2}
\]
No flow after the first lifetime or at r=0 is used.

## Conclusion

For every 0<=t<=T_0 with t<tau(r,s), W_t is nonzero and
\[
 \Re W_t\ \ge\ \cos(\gamma)|W_t|>0,\qquad
 \gamma=\epsilon+\frac{\epsilon}{2-\epsilon}
 \le\frac{299}{19900}<\frac1{50}.                       \tag{3}
\]
In particular, a purely rational lower bound is
\[
 \Re W_t\ge
 \left(1-\frac12\left(\frac{299}{19900}\right)^2\right)|W_t|>0.
                                                               \tag{4}
\]
Thus no affine H can provide the negative witness sought under
the displayed smallness condition, including arbitrary complex
constant drifts and times arbitrarily close to first collision.
No positive lower bound on |q| is assumed or inserted into (3).
The zero extension at stopped points has nonnegative real part
by definition, not by a boundary Jacobian assertion.

This is an obstruction to the affine ansatz within the approved
degree-at-most-two test. It leaves genuinely quadratic backgrounds,
the general holomorphic sign conjecture, actual-H applicability,
global signed integration, all-order signs and Xi transfer open.
The estimate is a local deduction under assessment969, whose bounded
search did not locate it; originality is not established. The proof
has not yet received a separate independent audit. It is not an RH
candidate or a disproof of the proposed general sign condition.

## Proof

### Imported local facts and their specialization

C466s supplies the open survivor domain, smooth dependence at fixed
physical time on every compact surviving interval, and the identities
\[
 \dot J=\overline{(D^2S)J},\qquad
 \frac{d}{dt}F(X(t))=-\|\nabla S(X(t))\|_2^2F(X(t)),
 \quad S=-2\log q+H.                                  \tag{5}
\]
The first identity is the flat-metric real-variation formula of
Tanizaki, Nishimura and Verbaarschot, *Gradient flows without blow-up
for Lefschetz thimbles*, JHEP10(2017)100,
[arXiv:1706.03822v2, 27 September 2017, Appendix B,
(B.1)–(B.5), printed p22](https://arxiv.org/pdf/1706.03822v2).
Both the Hessian and the varied vector are conjugated. A compact
surviving trajectory lies in U, where the vector field is smooth;
this is the required scope of that formula and of ordinary smooth
ODE dependence. No uniform nonsingular neighborhood up to collision
is imported. The angle estimate below is the additional deduction;
the cited source does not supply (3).

The affine equations separate exactly:
\[
 \dot q=-2/\bar q+\bar A,\qquad z=s+\bar B t.           \tag{6}
\]
Hence q is independent of s, z_r=0, z_s=1, and
\[
 J_t=\operatorname{diag}(u(t),1),\quad u=q_r,\qquad
 \dot u=\frac{2}{\bar q^2}\bar u,\quad u(0)=i.         \tag{7}
\]
This is the complete two-parameter complex Jacobian, not a chosen
minor or the derivative at fixed radius. The derivative is taken
at fixed t in the open survivor domain.

### Radius and trajectory angle

Fix r,s and an arbitrary T<=T_0 with T<tau. All assertions below
are on [0,T], so all ODE coefficients and integrals are ordinary
finite ones. Write rho=|q|, rho_0=|r|, and k=|A|. A continuous
real angle theta exists on this interval, with
theta(0)=theta_0=sgn(r)pi/2. Equation (6) gives
\[
 \dot\rho=-2/\rho+\Re(Ae^{i\theta}),\qquad
 \dot\theta=-\Im(Ae^{i\theta})/\rho.                  \tag{8}
\]
As k rho_0<=epsilon<2, the radial derivative is strictly negative
whenever rho=rho_0. The solution starts at that radius and immediately
enters its interior; an upward first return is impossible since the
derivative at such a return would again be strictly negative. Thus
rho<=rho_0 throughout the surviving interval. It follows from (8)
that
\[
 \dot\rho\le-\frac{2-\epsilon}{\rho}<0,\qquad
 \int_0^t\frac{dv}{\rho(v)}
 \le\frac{\rho_0-\rho(t)}{2-\epsilon}.                 \tag{9}
\]
The integral inequality is obtained by integrating
(2-epsilon)/rho<=-dot rho, not by an improper endpoint substitution.
With delta=theta-theta_0, (8) and (9) imply
\[
 |\delta(t)|\le\frac{k(\rho_0-\rho(t))}{2-\epsilon}
 \le\frac{\epsilon}{2-\epsilon}=:d\le\frac1{199}.      \tag{10}
\]

These estimates cover the whole earlier interval [0,t]. They also
give |q|<=|r|<a<R, while (6) and the strict buffer give
|z|<=|s|+M_1T_0<b+M_1T_0<L. Thus no earlier outer-boundary event
can be hidden in this time range. The endpoint classification in
C466s implies that any finite first lifetime <=T_0 ends at q=0.
No extension through that event is asserted or needed.

### Fixed-time tangent angle

The scalar complex equation (7) is a homogeneous linear equation
over the reals. On [0,T] its coefficients are continuous. If u
vanished at a time, uniqueness for that real linear equation with
zero data at that time, also solved backwards on the compact interval,
would force u(0)=0. This contradicts u(0)=i. Consequently there is
a continuous differentiable angle alpha such that
\[
 u/i=|u|e^{i\alpha},\qquad \alpha(0)=0.
\]
Dividing (7) by the nonzero u on this interval gives
\[
 \dot\alpha
 =\Im\left(\frac{2\bar u}{\bar q^2u}\right)
 =-\frac{2}{\rho^2}\sin(2(\alpha-\delta)).             \tag{11}
\]
Indeed arg u=pi/2+alpha modulo 2pi. For positive r,
theta_0-pi/2=0; for negative r it is -pi. The doubled angle in
(11) therefore has the same sine in both cases. No orientation
reversal for negative r has been dropped.

For the right side of (11), evaluated at alpha=d, (10) gives
0<=2(d-delta)<=4d<pi, so that right side is nonpositive.
At alpha=-d it is nonnegative. The constants -d and d are thus
a subsolution and supersolution. On each compact surviving interval
the right side is continuous in time and locally Lipschitz in alpha;
the ordinary scalar comparison principle yields
\[
 -d\le\alpha(t)\le d.                                 \tag{12}
\]
Equivalently, the interval [-d,d] is invariant for this scalar ODE.
This also handles equality at a barrier: comparison uses local
Lipschitz uniqueness, not the invalid inference that a zero derivative
alone prevents crossing. If epsilon=0, then A=B=0, delta=0 and d=0;
(11) and uniqueness give alpha=0, so the same conclusion holds.
Although 2/rho^2 may become unbounded at collision, it is bounded
on each [0,T] used for comparison. The resulting constant d is
independent of T and of its distance to collision.

### Full weight, phase, and sign

By the second identity in (5), set
\[
 E_t=\exp\left(-\int_0^t
       \bigl(|-2/q(v)+A|^2+|B|^2\bigr)\,dv\right)>0.
\]
Then F(X(t))=F(X(0))E_t, where
F(X(0))=-r^2 exp(-H_0-iAr-Bs). Combining this exact phase
conservation with (2), (7) and (12) yields
\[
 W_t=r^2 e^{-H_0-\Re(iAr+Bs)}E_t|u(t)|
      \exp\bigl(i[\alpha(t)-\Im(iAr+Bs)]\bigr).        \tag{13}
\]
All factors outside the last exponential are strictly positive.
The Hermitian Cauchy–Schwarz inequality gives
\[
 |\Im(iAr+Bs)|\le |iAr+Bs|
 \le\sqrt{|A|^2+|B|^2}\sqrt{r^2+s^2}\le\epsilon.
\]
Thus (13) has an explicitly chosen real phase of absolute value
at most d+epsilon=gamma. Since epsilon<=1/100,
d<=1/199 and gamma<=299/19900<1/50<pi/2. The cosine is positive
and decreasing on [0,gamma], proving (3). The elementary real
inequality cos x>=1-x^2/2 gives (4). Every fixed survivor was
arbitrary; all constants are uniform, without taking a derivative
of a stopped map or an improper integral at its endpoint.

The only direct local mathematical input is C466s. The restriction
called the C466u buffer is imposed in (1); no current identity or
sign conclusion from C466u was used. The affine calculation is
needed because the ready literature comparison supplies local flow
identities but neither this tangent barrier nor a matching sign
theorem. It cannot be extended to a coupled Hessian simply by
retaining (7), which would omit the mixed Jacobian entries.

## Mathlib

No full matching Mathlib theorem for (3), this logarithmic survivor
flow or its tangent-angle barrier was checked. Availability is unknown,
not absent. The proof uses standard smooth real ODE dependence and
uniqueness, scalar comparison, complex chain rules and elementary
trigonometric inequalities; their formal supporting coverage was
not inspected in this step. No formal verification is claimed.
