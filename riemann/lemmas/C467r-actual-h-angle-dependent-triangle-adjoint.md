# C467r — An actual triangle adjoint with angular vertex values

## Hypotheses

Retain C467e/audit1017's regular coefficient solution, C467k/audit1033's
actual j=0 triangle, C467p/audit1049's selected pair test and auxiliary
characteristic construction, and C467q/audit1053's graph formulas
(6)–(16). In particular,

\[
n=3,\quad R=1/4,\quad a=1/16,\quad T_0=1/1920,
\quad X=1/256,\quad b_*=1/4096,
\]
\[
\beta(z)=B(1+z)-B(1)-B'(1)z,\quad g=\beta',\quad
H=H_0+\sum_j\beta(z_j),\quad H_0\in\mathbb R,
\]
\[
F=\Delta^2e^{-H},\qquad
\Omega=F\bigwedge_{j=1}^3(dz_j/i).
\tag{1}
\]

The background is the actual conjugation-normalized logarithm of
h(w)=xi(1/2+sqrt(w))/xi(1/2), with beta(0)=beta'(0)=0 and
|beta''|<40 on |z|<R. Retain the qualifications carried through the
inputs, including L018/C466a's unreplayed external first-zero input;
the nontriviality argument using that zero in C467q is not needed here.
No reciprocal-density realization, RH, or all-degree sign is assumed.

Let q1<q2<q3, P, vj=P(qj)+i qj and vbar be the actual triple data
from initial (x,x,x). The map and time are unchanged:

\[
Z=(1-r)\bar v\,\mathbf1+
r[(1-\lambda)(v_1,v_2,v_3)+\lambda(v_2,v_1,v_3)],
\quad 0\le r,\lambda\le1.
\tag{2}
\]

Let f be the fixed smooth real bump, 0<=f<=1, equal to 1 on
[-b_*,b_*], supported in (-2b_*,2b_*). Let phi_p be precisely
C467p(33)–(35)'s selected test, including its continuous h=0 trace.
Use C467k(17)'s original complex coefficients A,B,U,V, orientation
dt dx dr dlambda and the common minus normalization of the full form.

## Conclusion

For one common existential tau>0 there is a real psi, 0<=psi<=1,
continuous on [0,tau] x [-X,X] x [0,1]^2, smooth for positive time
and 0<r<1, including lambda=1/2 and the fixed x/lambda endpoint
neighborhoods, such that

\[
\psi(0,x,r,\lambda)=f(x)^3,\qquad
\psi(t,x,1,\lambda)=\phi_p(t,x,1-2\lambda,0),
\tag{3}
\]
\[
d\psi\wedge\operatorname{Re}(-Z^*\Omega)=0,
\qquad
\int\bigl(|A\psi_t|+|U\psi_x|+|B\psi_r|+|V\psi_\lambda|\bigr)<\infty.
\tag{4}
\]

The integral is on the entire parameter box. The complete complex
C467k(20) identity passes from epsilon<=t<=T and
eta<=r<=1-zeta to the full domain for arbitrary independent positive
epsilon,eta,zeta tending to zero. Every time, x, angular and outer
radial term is retained. The inner radial flux tends to zero,
uniformly in the other cutoffs; there is no additional corner term.

The vertex value is a continuous function of the angular parameter.
It is not required to descend to a single scalar on the collapsed
physical vertex. No derivative at t=0, r=0 or r=1 is asserted.
This is attempt1055's local construction, validated by the separate
conceptual audit1056 below. It supplies only one selected triangle/edge test;
other triangles, mutual and chamber matches, exterior payment,
realization, other degrees and actual-Xi positivity remain open.
It is not a complete RH candidate or a certified novelty claim.

## Proof

### Coverage and imported tools

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-16-angle-dependent-triangle-trace-nomination-1053.md`,
separately completed by review1054. Its exact target is (3)–(4)
with angular parameter continuity and the full cutoff limit. Reuse
its comparison: weak trace theorems do not themselves provide this
test, and C467q's single physical-vertex obstruction does not exclude
it. No additional source assessment or standard-theorem reproof is
claimed in this mathematical attempt.

Import ordinary ODE existence, smooth dependence, variational and
compact continuation results from Gerald Teschl, *Ordinary Differential
Equations and Dynamical Systems*, author-hosted April2012 preliminary
version, [Lemma2.14/Corollary2.15, pp52–53; Theorem3.9, p81;
Theorem6.1 and proof, pp189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
Use smooth ODE theory only on the open positive-time charts verified
below. At time zero, bounded velocities and uniform spatial Lipschitz
estimates explicitly give the limiting flow and its uniqueness.
This is a boundary check for this field, not an invocation of a weak
transport theorem for an unverified normalized velocity.

For the cutoff identity use Brian Conrad, *Math396. Stokes' theorem
with corners*, [Theorem1.1 and proof, pp1–3](https://math.stanford.edu/~conrad/diffgeomPage/handouts/stokescorners.pdf),
and John K. Hunter, *Measure Theory*, [Chapter4, Theorem4.24,
pp49–50](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf#page=11).
These are the already assessed Stokes and dominated-convergence inputs
in C467k/o. Their smooth-box and integrable-majorant hypotheses are
checked below separately for real and imaginary parts.

All C constants below are finite constants of the fixed compact
analytic setup, and may increase. The time is decreased finitely many
times, using strict uniform margins. No reduction depends on the
terminal point or on a cutoff rate.

### A regular field on the angular parameter space

Use C467q's exact physical graph coordinates

\[
y=E_1(t,x)/3,\quad d=q_3-y,\quad \alpha=q_2-q_1,
\quad \ell=rd,\quad w=(1-2\lambda)\alpha/(2d).
\]
\[
\mathbf e=(-1/2,-1/2,1),\quad\mathbf v=(-1,1,0),\quad
Q=\operatorname{Im}Z=y\mathbf1+\ell\mathbf e+w\ell\mathbf v,
\]
\[
p=\operatorname{Re}Z=m\mathbf1+k_3\ell\mathbf e+k_1w\ell\mathbf v.
\tag{5}
\]

Here m=(sum P(qj))/3, k1=(P(q2)-P(q1))/alpha and
k3=(P(q3)-m)/d, evaluated at x=x(t,y). The inverse x exists on
nested fixed mean intervals around [-X,X], because y_x=1+O(t).
The compact regular coefficient domain in C467e and C467k's simple
rescaled-root implicit functions allow a small open enlargement of
the original x interval. Choose the nested mean intervals within
|y|<1/128. They have positive margins from the original image and
from |3y|=3/128, the pair construction's smaller mean boundary.

Write rho=sqrt(t). The exact smooth factorizations from C467k/q give

\[
d=\rho D(\rho,y),\quad D(0,y)=\sqrt6,\qquad
\alpha=\rho A_0(\rho,y),\quad A_0(0,y)=\sqrt6,
\]
\[
m\text{ smooth in }(t,y),\qquad k_j=t a_j(\rho,y),
\tag{6}
\]

with smooth bounded coefficient functions on these compact intervals.
In particular their needed y derivatives are bounded, k_(j,t) is
bounded and continuous to zero, and

\[
d^2=6t+O(t^{3/2}),\quad (d^2)_t=6+O(\sqrt t),\quad
|(d^2)_y|\le Ct,\quad |d_t|\le C/\sqrt t,
\]
\[
|d_y|\le C\sqrt t,\quad
\left|\partial_t\frac\alpha{2d}\right|\le C/\sqrt t,\quad
\left|\partial_y\frac\alpha{2d}\right|\le C.
\tag{7}
\]

These bounds differentiate (6), rather than an unqualified remainder.
Also y_t,y_x are bounded in the original (t,x) variables.

For clarity the field used from C467q is explicit. Put

\[
u_0={-i m_t\over1-i m_y},\qquad
u_j={-i k_{j,t}+i k_{j,y}u_0\over1-i k_j}\quad(j=1,3),
\]
\[
K=4(k_1+i)^2[\tfrac94(k_3+i)^2-(k_1+i)^2w^2]^2
 e^{-H(p+iQ)}(1-i m_y)(1-i k_3)(1-i k_1),
\]
\[
Y=-{\operatorname{Re}(Ku_0)\over\operatorname{Re}K},\qquad
\mathcal B_j=-{\operatorname{Re}(Ku_j)\over\operatorname{Re}K}.
\tag{8}
\]

Extend only these explicit graph formulas to a small fixed |ell|<L
and |w|<1, with the larger mean interval. This extends an auxiliary
field, and leaves the original map (2) unchanged. At t=ell=0,

\[
K=-4(9/4-w^2)^2e^{-H_0-3\beta(iy)}.
\]

For |w|<=1 the real polynomial has a positive floor, and
|3beta(iy)|<=60y^2<1/16 on the chosen mean interval. Uniform
continuity gives a nonzero real-part floor |Re K|>=c|K|>0 on a
smaller closed (rho,ell) box. The graph remains in |zj|<R there.
Consequently (8), and all its spatial derivatives in y,ell,w, are
uniformly bounded and continuous to t=0. They are smooth in positive
physical time. No time derivative of order two at zero is used.

The exact characteristic system is

\[
\dot y=Y(t,y,\ell,w),\qquad
\dot\ell=\ell\mathcal B_3(t,y,\ell,w),\qquad
\dot w=w(\mathcal B_1-\mathcal B_3)(t,y,\ell,w).
\tag{9}
\]

C467q(11)–(16) derive it from the original pulled-back real form:
in Q coordinates F det(Id-iD_Qp)=ell^6 w^2 K. Off w=0 and
ell=0 the adjoint is exactly transport by (9), with its stated minus
sign. The common minus sign on the whole current cancels from that
equation. On the original interior w=0, the undivided coefficients
all vanish; smooth extension of the test will suffice there.

### The selected whole edge is smooth at positive time

Define its slightly extended value by

\[
Q_e(t,y,w)=y\mathbf1+d(t,y)\mathbf e+w d(t,y)\mathbf v,
\qquad E(t,y,w)=\chi_p(t,Q_e(t,y,w)),
\tag{10}
\]

where chi_p is C467p(33)'s selected physical function, using its
one-sided h=0 trace. On the pair, I=3y, q=q3=y+d and its
ell_pair=(3q-I)/2=3d/2. Thus |v|/ell_pair=2|w|/3. For
|w|<=3/4 this is at most 1/2, strictly inside C467p(30a)'s 3/4
margin and (20)'s 4/5 cone. The chosen mean interval and h=0 have
strict margins from its other outer boundaries. The same constructed
chi_p, with the same initial product G(Q)=prod f(Qj), therefore
defines (10); no new or freely chosen edge values are substituted.
On the original edge, (10) is exactly phi_p(t,x,1-2lambda,0).

C467p establishes continuity and uniform physical first-derivative
bounds at h>0, but does not state positive-time tangential smoothness
of its trace. The following verifies that additional property needed
for the interior triangle construction.

Fix any positive-time point on this extended edge. In a neighborhood
of it use the pair's initial coordinates c,h and physical v, retaining
physical time t. At t>0 the singleton root q is simple, including at
h=0. In C467p(12)–(17), the entries a1,b1,a2,b2, the positive
denominator N, and the solutions c_I,c_q,c_t and h h_I,h h_q,h h_t
are smooth functions of (t,c,h,q) through h=0. All quantities with
an apparent h denominator enter the physical derivatives of e0 as
e_c c_j+W(h h_j). Hence p_t, D_Qp, its invertible matrix M, and
the explicitly factored real velocity b_p in C467p(22)–(25) are
smooth functions of (t,c,h,v) through h=0 in this neighborhood.
The factorization by v^2 is the auxiliary formula (23), valid at v=0;
its real-part floor persists. This also covers the central angle.

Let K_h=h dot h and C_c=dot c along a pair characteristic. Equation
C467p(28) expresses K_h as a quotient with denominator N/Q'(q)>0;
the first equation of (27) then expresses C_c without division by h.
Both are smooth through h=0 at this fixed positive time. Its proved
collar inequality (30) gives K_h<=-d_*/2<0, after choosing the
common time within that collar's time range. These are statements
about the actual velocity, including its background.

Parameterize a short backward segment by increasing h. Its equations
are

\[
\frac{dt}{dh}=\frac h{K_h},\qquad
\frac{dc}{dh}=\frac{h C_c}{K_h},\qquad
\frac{dv}{dh}=\frac{h(b_p)_v}{K_h}.
\tag{11}
\]

They form a smooth ODE on an open neighborhood of h=0 with the other
variables near the fixed terminal point. Start at h=0 and integrate
to a fixed small h1>0, keeping t above half that terminal time and
all outer margins strict. Teschl's smooth dependence applies. The
same map from a terminal h0>0 to h1 is a reparameterization of the
original backward characteristic, since K_h<0. From the endpoint
h1>0, C467p's time-zero endpoint map R0 is smooth on its common
backward domain. Composing the two maps gives a smooth function of
the terminal t,c,v. For h0>0 flow composition makes it exactly
G(R0); as h0 tends to zero it is the already selected continuous
trace. This proves that (10) is C-infinity for every t>0, locally
also beyond the fixed mean and angular endpoints. Reparameterizing
this auxiliary path does not change raw time in (1)–(4) or any current.

The first derivatives needed uniformly down to zero satisfy

\[
|E_t|\le C_f/\sqrt t,\qquad |E_y|\le C_f,\qquad
|E_w|\le C_f\sqrt t,\qquad 0\le E\le1,
\]
\[
|E(t,y,w)-f(y)^3|\le C_f\sqrt t.
\tag{12}
\]

To justify passage of C467p(34)'s bounds to this trace, approach it
by h=delta>0 at fixed I=3y and v=w d(t,y). Solve I(t,c,delta)=3y.
The pair's I_c>=2 and bounded I_t,I_h imply bounded c_y,c_t at
fixed delta. Its q_c is bounded and |q_t|<=C/(delta+sqrt(t)) at
fixed c,delta, by C467p(10),(14). The resulting physical maps
Q_delta have |(Q_delta)_y|<=C, |(Q_delta)_t|<=C/sqrt(t), and
|(Q_delta)_w|<=C sqrt(t). They remain inside the same auxiliary
domain for sufficiently small delta. Apply the uniform bounds
|D_Q chi_p|+|(chi_p)_t|<=C_f there. The resulting local difference
inequalities pass to the continuous limit; its just-proved smoothness
then gives the first three estimates in (12). No convergence of
uncontrolled h derivatives is asserted. Finally C467p(36), which
follows from bounded drift on this same auxiliary domain, gives
|chi_p-G(Q)|<=C_f t, also on the trace. Since Q_e=y1+O(sqrt(t))
and f has bounded derivative, the final estimate in (12) follows.

### A unique backward hit on the expanding edge

Shrink time so the original |w|=|1-2lambda|alpha/(2d) is at most
5/8 and d(t,y)<L/4. For a terminal point (t,y,ell,w) with
0<ell<=d(t,y) and |w|<=5/8, solve (9) backward. Its bounded
velocities keep y within the larger fixed mean interval and w within
|w|<3/4 when time is small. Its exact multiplicative radial equation
gives

\[
e^{-Ct}\ell\le\ell(s)\le e^{Ct}\ell\quad(0\le s\le t).
\tag{13}
\]

It cannot reach |ell|=L. These bounds have strict margins and hold
up to any proposed first exit, so positive-time compact continuation
reaches every s>0. Bounded velocities make the endpoints Cauchy as
s decreases to zero. Uniform spatial Lipschitz bounds and Gronwall
give unique limiting paths and uniform continuous dependence on
terminal data, including ell=0. Thus the flow is defined on [0,t]
for all these terminal points on one common interval. The same
margins cover neighborhoods of the fixed x and angular endpoints.

Along such a path set

\[
J(s)=\ell(s)^2-d(s,y(s))^2.
\]

First choose L small using the bounded coefficients on the original
auxiliary box, then choose time smaller. Equations (7),(9) give

\[
J'(s)=2\ell(s)^2\mathcal B_3-(d^2)_t-(d^2)_yY,
\qquad -8\le J'(s)\le-4.
\tag{14}
\]

Indeed arrange 5<=(d^2)_t<=7 and
|2ell^2 B3|+|(d^2)_yY|<=1 throughout the retained box. These
are strict compact-smallness choices with actual leading value 6;
they do not require a numerical estimate of an unknown constant.
The formula extends continuously to s=0 by (6)–(7).

Now J(t)<=0 and J(0)=ell(0)^2>0. There is exactly one
sigma in (0,t] with J(sigma)=0; sigma=t precisely on the edge.
For sigma<s<=t the path is on the inner side of that edge.
Using (6),(13) at the hit gives fixed positive constants c,C with

\[
c\ell^2\le\sigma\le C\ell^2.
\tag{15}
\]

Write y_sigma,w_sigma for the other coordinates at the hit. An
angular side may be crossed before the hit, but it lies in the
auxiliary |w|<3/4 domain just verified. Those sides have no prescribed
test values. Equation (10) supplies the same selected pair function
there. Thus this extension chooses free side traces and leaves the
entire prescribed original outer edge unchanged. No compatibility
between two edge hits is needed, because (14) excludes a second hit.

### Differentiated hit map and the constructed test

Let z=(y,ell,w) denote terminal coordinates. On positive time intervals
the variational equation for (9) and bounded spatial derivatives give
|D_z(y(s),ell(s),w(s))|<=C. More specifically, from the exponential
formula for ell(s) in (13),

\[
|\partial_j\ell(s)|\le C\ell\quad(j=y,w),\qquad
|\partial_\ell\ell(s)|\le C.
\tag{16}
\]

These estimates follow by differentiating the integral of B3 and
using the preceding full variational bound. For terminal time
differentiation at fixed z, flow composition gives
partial_t X(s;t,z)=-D_z X(s;t,z) V(t,z), where V is (9)'s field.
It follows that all these time derivatives are bounded and
|partial_t ell(s)|<=C ell, because V_ell=ell B3 and the other
entries in its radial variational row are O(ell). These estimates
hold uniformly down to s=0 by the same bounded integral equations;
no bound on a time derivative of V is required.

At s=sigma, differentiate J(sigma)=0 using (14). With s fixed,
its terminal derivatives are
2ell(s) partial_j ell(s)-(d^2)_y(s,y(s)) partial_j y(s).
By (7),(15),(16), the implicit-function estimates are therefore

\[
|\sigma_\ell|\le C\ell,\qquad
|\sigma_y|+|\sigma_w|+|\sigma_t|\le C\ell^2.
\tag{17}
\]

The derivatives of y_sigma and w_sigma with respect to any of
t,y,ell,w are bounded: differentiate the fixed-s flow and add the
bounded velocity times the corresponding derivative in (17).
The hit is smooth wherever t>0, 0<ell<d(t,y), since sigma>0
and J'(sigma) is nonzero. It approaches t smoothly locally at a
positive-time outer edge from the inner side.

Define

\[
\widetilde\psi(t,y,\ell,w)=E(\sigma,y_\sigma,w_\sigma)
\quad(0<\ell\le d(t,y)).
\tag{18}
\]

This is smooth in the positive-time interior, including w=0, and
has range [0,1]. Characteristic composition and the unique hit make
it constant on each characteristic while in that interior. Hence it
solves precisely (9)'s transport equation. Equations (12),(15),(17)
give the uniform bound

\[
|\widetilde\psi_t|+|\widetilde\psi_y|
 +|\widetilde\psi_\ell|+|\widetilde\psi_w|\le C_f.
\tag{19}
\]

For the potentially largest term, |E_t sigma_ell| is at most
C sigma^(-1/2) ell<=C. The other E_t terms are at most C ell;
E_y and E_w multiply bounded derivatives of the hit coordinates.
This explains why a bound on the edge derivative alone would have
been insufficient, and why its actual hit-time factor resolves it.

Let (y_0(t,y,w),w_0(t,y,w)) be the time-zero endpoint of (9) on
ell=0. Define the vertex trace by

\[
\widetilde\psi(t,y,0,w)=f(y_0(t,y,w))^3.
\tag{20}
\]

This is the limit of (18): as ell tends to zero, (15) gives
sigma->0; uniform continuous dependence of (9) gives
y_sigma->y0, w_sigma->w0; and (12) replaces the edge value by
f(y_sigma)^3 with error O(sqrt(sigma)). The convergence is uniform
on compact terminal parameter boxes. The limiting flow is continuous
in t,y,w, has y0=y+O(t), and at t=0 gives f(y)^3. It is allowed
to depend on w. No angle-independent vertex equation from C467q
is imposed.

Finally set psi by composing (18),(20) with (5). On r=1 the hit is
the terminal point, giving exactly (3)'s selected whole edge. At
positive time the continuous flow construction gives joint continuity
including both radial faces and all fixed endpoints. Uniformly in
the other parameters, |y_sigma-y|<=Ct and sigma<=t, so (12) gives

\[
|\psi(t,x,r,\lambda)-f(x)^3|\le C_f\sqrt t
\tag{21}
\]

after using y=x+O(t). The same estimate holds on r=0 by (20).
It supplies joint continuity at time zero with precisely the required
initial value, even when r and lambda vary arbitrarily. The strict
mean/angular margins give the fixed endpoint neighborhood extensions.
Take the final tau inside the constructed interval to cover the upper
time endpoint. The original undivided equation follows from (9) off
the divisor and the original vanishing coefficients at lambda=1/2.

### Four original complex products and every cutoff face

From (5)–(7),(19), at t>0, 0<r<1,

\[
|\psi_t|\le C_f/\sqrt t,\qquad |\psi_x|\le C_f,
\qquad |\psi_r|\le C_f\sqrt t,\qquad
|\psi_\lambda|\le C_f.
\tag{22}
\]

For example ell_t=r(d_t+d_y y_t)=O(r/sqrt(t)),
w_t=O(1/sqrt(t)), ell_r=d=O(sqrt(t)), and
w_lambda=-alpha/d=O(1); y_r=w_r=0. All x derivatives of these
coordinates are bounded. These are derivatives in original physical
time and parameters, not in rho or along a reparameterized current.

Use the already proved original coefficient bounds C467k(19), with
s=1-2lambda. They give separately

\[
|A\psi_t|\le C_f r^7 t^{7/2}s^2,\qquad
|U\psi_x|\le C_f r^7t^4s^2,
\]
\[
|B\psi_r|\le C_f r^8t^{7/2}s^2,\qquad
|V\psi_\lambda|\le C_f r^7t^3s^2.
\tag{23}
\]

Every right side is integrable on the full box. Absolute values are
taken before any real-part cancellation. At the original zero s=0
the coefficients remain zero; none has been replaced by a divided
weight or a modulus square.

For 0<epsilon<T<=tau and 0<eta<1-zeta<1 apply the cited Stokes
theorem to the smooth test on the positive-cutoff box. The original
holomorphic top form is closed, including its divisor. The full
identity is C467k(20), with r=eta and r=1-zeta in place of 0,1:
the bulk is A psi_t-U psi_x+B psi_r-V psi_lambda; its boundary
signs are +[psi A] at time, +[psi B] at radius,
-[psi U] at x and -[psi V] at lambda. All terms are complex.

For the bulk (23) is a fixed integrable majorant. Its cutoff indicators
converge almost everywhere along every joint sequence, so dominated
convergence applies to all four products separately. No derivatives
of shrinking cutoffs or cancellation of nonintegrable terms is used.
The lower-time integral is bounded by C epsilon^4, uniformly in
eta,zeta. At fixed upper time the continuous psi A is bounded on
the closed face, giving its full limit.

The inner radial term has the uniform bound

\[
\int_\epsilon^T\!\int_{-X}^X\!\int_0^1
|\psi(t,x,\eta,\lambda)B(t,x,\eta,\lambda)|
\,d\lambda\,dx\,dt\le C\eta^8 T^4\longrightarrow0.
\tag{24}
\]

Thus no angular choice of the bounded vertex value adds vertex flux.
On the outer radial face, continuity gives convergence to the entire
prescribed psi(t,x,1,lambda)B(t,x,1,lambda); its common majorant
is C t^3. Removing [0,epsilon] costs at most C epsilon^4,
uniformly in zeta. On the x faces the majorant is C r^7t^4,
and on the angular faces it is C r^7t^3. These bounds hold on the
actual faces by C467k(19), not merely for almost every interior slice.
Continuity and dominated convergence give their full limits for
arbitrary independent cutoffs. They are retained, with no assertion
that their signs are favorable or that they cancel against other pieces.

Every term of the full complex identity has now converged. Multiplying
the entire identity by the common minus sign changes all terms
together. This proves the required zero-defect limit with zero inner
radial flux and the whole selected outer edge. The argument gives
one local component and pays none of the independent global obligations
listed in the conclusion. The separate audit is recorded below.

### Independent conceptual audit — 16 November 2026, step1056

This is a REPRODUCTION audit of the unchanged EXPLORE target in
nomination1053/review1054. It reuses the assessed ODE, Stokes and
dominated-convergence imports cited above. No new source gate or
standard-theorem reproof is asserted. C467p/o's audit1049 and C467k's
audit1033 retain their hypotheses; C467q supplies its graph formulas,
not its single-vertex obstruction as a premise.

**Domain and original field.** C467e's regular coefficient flow exists
on a neighborhood of compact initial triples strictly inside (-a,a)^3.
Take an interval of initial x slightly larger than [-X,X] in that
domain. Its y_x=1+O(t)>0 inverse and the rescaled simple-root implicit
functions give the nested mean intervals in (5)–(7), all strictly
within |y|<1/128, with the original mean image in their interior.
Thus |I|=|3y|<3/128 has the required pair-domain margin. This extends
only an auxiliary formula; the original flow and time are unchanged.

The symmetric identity for 3m gives smoothness in physical time.
C467q's exact secants give k_j=t a_j(sqrt(t),y), so at fixed y
k_(j,t)=a_j+(sqrt(t)/2)partial_rho a_j extends continuously to zero
with bounded spatial derivatives. Also d^2=t D(sqrt(t),y)^2 gives
(d^2)_t=D^2+sqrt(t)D partial_rho D tending uniformly to 6 and
(d^2)_y=O(t). These differentiated identities verify (7), without
differentiating an unspecified asymptotic remainder.

The triangular graph matrix has diagonal m_y,k_3,k_1. Solving
M u=-i p_t gives exactly (8); factoring the squared Vandermonde
gives ell^6 w^2 K. For |w|<=1, 9/4-w^2>=5/4, while at t=ell=0
the phase satisfies |3beta(iy)|<=60y^2<1/16. Compactness therefore
gives the strict real-part floor on a smaller auxiliary box. The
quotient field and its spatial derivatives are bounded and continuous
to t=0, and smooth in positive time. The wedge calculation gives
the minus sign in (8)–(9). Only the auxiliary field has had ell^6 w^2
canceled; the original form retains its divisor zeros.

**Selected edge and trace smoothness.** At h=0 the pair has I=3y,
q=y+d, ell_pair=3d/2 and v=w d. For |w|<=3/4 its cone ratio
is at most 1/2, strictly inside both C467p(30a)'s 3/4 margin and
the 4/5 cone. The mean and upper-h margins also hold. Thus (10)
uses the selected C467p function, including on the extended edge.

Fix t_*>0. The singleton q(t,c,h) remains simple in an open
neighborhood of h=0. The entries and right sides of C467p(15)–(16)
are smooth there and N>0; their solutions c_I,c_q,c_t and the
canceled coefficients k_j=h h_j are therefore smooth. Every derivative
of e^0 used in p_t and D_Qp is e_c c_j+W k_j. Consequently
p_t,D_Qp,M^{-1}, the factored phase and b_p are smooth functions
of (t,c,h,v) there, including h=0 and v=0. No uncanceled h_j
is asserted smooth.

In C467p(28), N/Q'(q)>0 and the numerator are smooth at this
positive time. Thus K_h=h dot h is smooth; its first equation (27)
gives dot c=(b_I-I_t-I_W K_h)/I_c, also smooth since I_c>=2.
The collar inequality extends to h=0 by continuity and gives
K_h<=-d_*/2. Hence (11) is a smooth ODE through h=0. A short
segment to a fixed h_1>0 stays above t_*/2 and within all strict
margins. From its endpoint the C467p backward path stays at h>0
all the way to time zero, where its field is smooth. Its R_0 is
therefore smooth locally. Composition with the short segment is
smooth in terminal t,c,v. For terminal h_0>0, flow uniqueness
identifies it with G(R_0); the limit h_0=0 is exactly the selected
continuous trace. Local choices of h_1 suffice; uniform h_1 as
t_* tends to zero is neither claimed nor needed.

For uniform first derivatives approximate by h=delta>0 at fixed
I=3y and v=w d(t,y). The equation for c gives c_y=3/I_c and
c_t=-I_t/I_c, uniformly bounded. The singleton bounds give
|q_c|<=C and |q_t|<=C/(delta+sqrt(t)) at fixed c,delta.
The resulting maps Q_delta have y,t,w derivatives bounded by
C,C/sqrt(t),C sqrt(t), respectively. C467p(34)'s uniform bounds
apply in these auxiliary neighborhoods. Their difference inequalities
pass to the continuous trace on every compact positive-time interval;
its proved smoothness gives the first three estimates in (12), with
constants independent of delta and t. C467p(36) and
Q_e=y*1+O(sqrt(t)) give the last estimate. No singular normal
derivative of the trace has been inferred.

**Common backward domain and hit.** Bounded velocities preserve the
nested mean and angular margins for one common small time. The
radial exponential formula (13) preserves positivity and the fixed
ell bound. Compact continuation reaches every earlier positive time;
bounded velocities and spatial Lipschitz control give unique continuous
limiting paths at zero by the integral equation and Gronwall. No
time derivative of the velocity at zero is used.

Choose L first and then time so the two error terms in J' have
total absolute value at most 1 and 5<=(d^2)_t<=7. This proves
-8<=J'<=-4 throughout the retained box. Since J(t)<=0 and
J(0)=ell(0)^2>0, there is exactly one hit sigma, equal to t
precisely at the outer edge. At the hit d(sigma,y_sigma)^2 is
comparable to sigma, and ell(sigma)^2 is comparable to terminal
ell^2 by (13). This proves (15) uniformly. Crossing a parameter
angular side before the hit stays within |w|<3/4 and uses the
same selected extended edge function. There is no prescribed side
value in this target and no inference of a neighboring-triangle match.

**Hit variations and continuity.** The spatial variational equation
has a uniform Gronwall bound. Differentiating the radial exponential
solution gives O(ell) radial entries for terminal y,w variations
and O(1) for an ell variation. Flow composition gives
partial_t X=-D_z X V(t,z); its radial entry is also O(ell).
At fixed earlier s the terminal derivative of J is
2ell(s)partial_j ell(s)-(d^2)_y partial_j y(s). At the hit,
(d^2)_y=O(sigma)=O(ell^2). Division by J'(sigma), whose magnitude
is at least 4, gives sigma_ell=O(ell) and
sigma_t,sigma_y,sigma_w=O(ell^2). Hit-coordinate derivatives
include bounded velocities times these quantities and remain bounded.
The smooth positive-time flow and nonzero hit derivative justify
this implicit differentiation at every positive ell.

In (18)'s chain rule the largest possible contribution is
E_t sigma_ell=O(ell/sqrt(sigma))=O(1). The other time-of-hit
terms are O(ell); the spatial terms are bounded. This verifies
(19) without assuming E_t bounded at zero. As ell tends to zero,
sigma tends to zero and uniform continuous dependence gives (20).
Its angular dependence is allowed. Uniformly over the original box,
sigma<=t, |y_sigma-y|<=Ct and y=x+O(t) give (21), including
joint limits in t,r,lambda with initial value exactly f(x)^3.
At r=1 the hit is the terminal point, matching the entire selected
edge. The coordinate map is smooth for t,r>0, including the central
angle. Strict auxiliary margins supply fixed endpoint extensions.
No derivative at t=0 or r=0 is asserted.

**Complex products and all cutoff faces.** The original chain rule
gives y_t,y_x=O(1), ell_t=O(r/sqrt(t)), ell_r=O(sqrt(t)),
w_t=O(1/sqrt(t)), w_lambda=O(1), with bounded needed x
derivatives. Together with (19) these yield (22). Multiplying by
each original C467k(19) coefficient gives exactly (23), with time
powers 7/2,4,7/2,3. All four products are absolutely integrable
before taking real parts.

On a positive-cutoff box the test has a smooth neighborhood extension
and the pulled-back holomorphic top form is closed. Stokes gives
bulk A psi_t-U psi_x+B psi_r-V psi_lambda and upper-face signs
+,-,+,- in coordinate order t,x,r,lambda. Thus every face of
C467k(20), at the cutoff radii, is present.

The four bulk majorants dominate every joint cutoff sequence. The
lower-time integral is O(epsilon^4) uniformly in eta,zeta; the upper
time face is bounded and continuous. The inner radial integral is
at most C eta^8 integral_0^T t^3 dt, hence O(eta^8 T^4),
independently of both other cutoffs. The outer radial face converges
at every positive time to the whole prescribed edge and is dominated
by C t^3. The x and angular faces are dominated by C r^7 t^4
and C r^7 t^3. Dominated convergence applies to each real and
imaginary part with arbitrary independent cutoffs. Each finite-cutoff
identity already contains its complete boundary and every term has
a limit, leaving no unaccounted corner term. The real adjoint
annuls the real bulk, not its imaginary part; the complex identity
retains that part. The common minus normalization changes all terms
together.

**Verdict and limits.** Every nominated condition passes on one common
existential positive interval. This validates a local input, not a
new discovery beyond the construction being checked or a solution
of RH. Angular vertex values are not identified; neighboring matches,
exterior payment, realization, other degrees and Xi positivity remain
open. C467e, C467k, C467p and C467q are still the direct mathematical
inputs in the DAG row, with C467q used for its exact field formulas.
Their inherited analytic and external-input qualifications remain.
No numerical certificate or mathematical script is needed for this audit.

## Mathlib

Full matching coverage for this actual-data angular triangle adjoint,
selected-edge smoothness, hit estimates and independent-cutoff identity
has not been checked. Supporting smooth ODE, implicit-function, Stokes
and dominated-convergence facts are not a formalization of this result.
No new Mathlib search, exact declaration claim, absence claim or
formal-verification claim is made. The result is an informal local
input validated by conceptual audit1056, with the inherited source
qualifications retained.
