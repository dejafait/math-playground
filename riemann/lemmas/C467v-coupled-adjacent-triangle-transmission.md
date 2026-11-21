# C467v — Joint selection on two adjacent actual triangles

## Hypotheses

Retain C467e/audit1017's actual coefficient flow, C467k/audit1033's
triangles, C467p/audit1049's selected lower pair test, C467q/audit1053's
graph formulas, C467r/audit1056's isolated lower construction, and
C467t/u/audit1062's graph expansions and qualified incidence signs.
In particular keep

\[
n=3,\quad R=1/4,\quad a=1/16,\quad T_0=1/1920,
\quad X=1/256,\quad b_*=1/4096,\quad H_*=1/128,
\]
\[
\beta(z)=B(1+z)-B(1)-B'(1)z,\quad g=\beta',\quad
H=H_0+\sum_{k=1}^3\beta(z_k),\quad F=\Delta^2e^{-H},
\quad\Omega=F\bigwedge_{k=1}^3(dz_k/i).
\tag{1}
\]

B is the actual conjugation-normalized logarithm of
h(w)=xi(1/2+sqrt(w))/xi(1/2), H0 is real, and |beta''|<40 on
the original disk. The fixed smooth real bump satisfies 0<=f<=1,
f=1 on [-b_*,b_*], and supp f contained in (-2b_*,2b_*).
Neither f nor beta is assumed even. Raw time, the divisor and the
common minus normalization remain unchanged.

The use of C467u retains its external finite-zero qualification:
the positive ordinates through 100 are accounted for on the line,
and a first zero in (14,15) exists. The precise carried locator is
Suvrit Sra, *On some positivity properties of the Riemann Xi function*,
[version W_pr5z5huy_v1, section2.1, (6)–(8)](https://hub.valency.io/works/W_pr5z5huy_v1),
as qualified in C466a and C467u. Those underlying finite certificates
are not replayed here. L018/L021/L024 retain their stated completion,
positivity and unconditional product hypotheses. No assertion about
higher zeros, reciprocal density, or RH is assumed.

Let q1<q2<q3, P and v_k=P(q_k)+i q_k be the actual triple data
from initial (x,x,x), and vbar their mean. Use exactly

\[
Z_0=(1-r)\bar v\mathbf1+
r[(1-\lambda)(v_1,v_2,v_3)+\lambda(v_2,v_1,v_3)],
\]
\[
Z_1=(1-r)\bar v\mathbf1+
r[(1-\lambda)(v_2,v_1,v_3)+\lambda(v_3,v_1,v_2)].
\tag{2}
\]

Write phi_p for precisely C467p(33)–(35)'s selected pair test,
including its h=0 trace. There is no prescribed upper outer edge
or prescribed common radial value. In particular psi0 is not fixed
to C467r's isolated selection.

## Conclusion

For one common existential tau>0 there are real psi0,psi1 in [0,1],
continuous on [0,tau] x [-X,X] x [0,1]^2, smooth for t>0 and
0<r<1 including the angular midpoints and fixed-endpoint neighborhood
extensions, with

\[
\psi_j(0,x,r,\lambda)=f(x)^3,\qquad
d\psi_j\wedge\operatorname{Re}(-Z_j^*\Omega)=0,
\]
\[
\psi_0(t,x,1,\lambda)=\phi_p(t,x,1-2\lambda,0),\qquad
\psi_0(t,x,r,1)=\psi_1(t,x,r,0).
\tag{3}
\]

For each j separately, all four original complex products
A_j psi_j,t, U_j psi_j,x, B_j psi_j,r, V_j psi_j,lambda are in L1.
Each complete C467k(20) identity passes to zero time and both radial
endpoints for independent cutoffs, retaining every endpoint term.
The original inner radial flux is zero. The common angular face
cancels when the two identities are added.

This local construction from attempt1064 is validated by the independent
conceptual audit1066 below, under the stated external-input qualification. It does
not match an upper pair, other triangles or chambers, pay exterior
terms, realize a density, prove all-degree signs, or transfer to Xi.
There is no complete RH candidate. No effective tau or certified
originality is claimed. The fixed-selection stop C467t/u is preserved:
this construction changes the lower interior where transmission requires it.

## Proof

### Gate and imported tools

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-16-coupled-adjacent-trace-nomination-1062.md`,
completed separately by review1063. It covers exactly (2)–(3), all
eight products and both full cutoff identities. Its inspected weak
network/semigroup theorems do not give the pointwise construction.
The additional work here is the actual two-chart transmission, corner
selection and weighted estimates, not a reproof of those general results.
Stops1058/1060 concern independent or fixed lower selections; C467q
requires one physical-vertex value. None of those extra restrictions
is imposed here.

Reuse Gerald Teschl, *Ordinary Differential Equations and Dynamical
Systems*, author-hosted April2012 preliminary version,
[Theorem2.5/proof, pp40–41; Lemma2.14/Corollary2.15, pp52–53;
Theorems3.9/3.12, pp81–84; Theorem6.1/proof, pp189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
Apply these ordinary ODE existence, dependence, variation and continuation
results on the smooth positive-time charts below. The limits at time zero
are justified by bounded velocities and uniform spatial estimates.
No theorem for an unverified weak inflow operator is invoked.

For positive-cutoff boxes use Brian Conrad, *Math396. Stokes' theorem
with corners*, [Theorem1.1/proof, pp1–3](https://math.stanford.edu/~conrad/diffgeomPage/handouts/stokescorners.pdf).
For the limits use John K. Hunter, *Measure Theory*,
[Chapter4, Theorem4.24, pp49–50](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf#page=11).
These sources and their applicability to smooth pullbacks of the original
closed form were assessed in the reused coverage. The new test majorants
are proved below before applying dominated convergence.

Constants below are finite constants of fixed compact neighborhoods,
including f. They need not be effective. All time reductions are common
to the two triangles and independent of terminal points or cutoffs.

### Common spatial coordinates and actual fields

Set y=E1(t,x)/3, with its local inverse x(t,y). C467k gives y_x=1+O(t)
and bounded y_t on a slightly enlarged original mean interval. Put

\[
d_+=q_3-y,\quad d_-=q_1-y,\quad
W_+={q_2-q_1\over2d_+},\quad W_-={q_3-q_2\over2d_-},\quad
D_\pm=d_\pm/\sqrt t.
\]
\[
m={1\over3}\sum P(q_k),\quad c=\Pi_3,\quad
a_0=-\Pi_2-y\Pi_3,\quad S={1\over3}\sum(q_k-y)^2,
\]
\[
k_{p,\pm}=a_0-cd_\pm,\qquad
k_{s,\pm}=a_0+c(d_\pm-S/d_\pm).
\tag{4}
\]

The lower graph uses e_+=(-1/2,-1/2,1), v_+=(-1,1,0);
the upper graph uses e_-=(-1/2,1,-1/2), v_-=(-1,0,1).
In either graph, with its own ell,w,

\[
Q=y\mathbf1+\ell\mathbf e_\pm+w\ell\mathbf v_\pm,
\quad p=m\mathbf1+k_{s,\pm}\ell\mathbf e_\pm
                         +k_{p,\pm}w\ell\mathbf v_\pm.
\tag{5}
\]

These are the exact C467q/C467t graphs of the original maps, not
relabelled backgrounds. Introduce a common nonnegative spatial coordinate
u=r sqrt(t), and a signed angular coordinate z=lambda0-1 on j=0 and
z=lambda1 on j=1. Thus the common side is z=0, the actual lower angular
interval is [-1,0], the upper is [0,1], and

\[
\ell=D_\pm u,\qquad
w=-(1+2z)W_+\ (j=0),\qquad
w=(1-2z)W_-\ (j=1).
\tag{6}
\]

Time is still the original physical t. The common outer boundary is
u=sqrt(t). The use of sqrt(t) in a spatial coordinate changes neither
the current nor the time integration.

For either graph define, exactly as in C467q/r/t,

\[
v_0={-i m_t\over1-i m_y},\qquad
v_a={-i k_{a,t}+i k_{a,y}v_0\over1-i k_a}\quad(a=p,s),
\]
\[
K=4(k_p+i)^2[\tfrac94(k_s+i)^2-(k_p+i)^2w^2]^2
e^{-H(p+iQ)}(1-i m_y)(1-i k_s)(1-i k_p),
\]
\[
Y=-{\operatorname{Re}(Kv_0)\over\operatorname{Re}K},\qquad
B_a=-{\operatorname{Re}(Kv_a)\over\operatorname{Re}K}.
\tag{7}
\]

The real-part floor in C467r, with the identical upper calculation in
C467t, holds on fixed small |u| neighborhoods and angular extensions
of the two intervals. Use |w|<3/4 with a margin. All images remain in
the original analytic polydisc. The fields and their spatial derivatives
are bounded and continuous down to t=0, and smooth at positive time.
The original real adjoint off its divisor is transport by
(Y,ell B_s,w(B_p-B_s)). At w=0 the original coefficients vanish;
the smooth field (7) is used only to construct a smooth test there.

In the common coordinates the field is

\[
b_j=(Y_j,u C_j,N_j),\qquad
C_j=B_s-{D_{\pm,t}+Y_jD_{\pm,y}\over D_\pm},
\]
\[
N_j=-{1-2\lambda_j\over2}
 \left[B_p-B_s-{W_{\pm,t}+Y_jW_{\pm,y}\over W_\pm}\right].
\tag{8}
\]

We next verify the uniform estimates needed for this coordinate change
and for transmission, including the actual side incidence.

### Incidence and the derivative correction at a crossing

C467t/audit1062 gives the factored symmetric expansions
M2=t[12+t R2(t,y)], M3=t^3[12 J''(y)+t R3(t,y)], with smooth
remainders, where G=Re g(iy) and J=Im g(iy). The centered cubic is
delta^3-(M2/2)delta-M3/3. Let A=sqrt(M2/2)=sqrt(t)a(t,y),
a(0,y)=sqrt6. Its rescaled roots are the smooth branches of
v^3-v-epsilon=0, epsilon=M3/(3A^3)=O(t^(3/2)). The branches at
-1,0,1 have first terms -1+epsilon/2, -epsilon, 1+epsilon/2.
Consequently D_+=a+O(t^(3/2)), D_-=-a+O(t^(3/2)), with factored
remainders smooth in sqrt(t),y. In particular D_t is bounded,
D_y is bounded, and both D's are separated from zero. Also

\[
W_+=\tfrac12-{2\over3\sqrt6}J''t^{3/2}+O(t^2),\qquad
W_-=-\tfrac12-{2\over3\sqrt6}J''t^{3/2}+O(t^2),
\]
\[
\partial_t\log|W_+|=-{2J''\over\sqrt6}\sqrt t+O(t),\qquad
\partial_t\log|W_-|={2J''\over\sqrt6}\sqrt t+O(t),\qquad
W_{\pm,y}=O(t^{3/2}).
\tag{9}
\]

The derivatives follow by differentiating these factorizations. Further,
c=-G''t/2+O(t^2), a0=O(t), and

\[
k_{p,+}-k_{s,+}={4\over\sqrt6}G''t^{3/2}+O(t^2),\qquad
k_{p,-}-k_{s,-}=-{4\over\sqrt6}G''t^{3/2}+O(t^2).
\tag{10}
\]

Their time derivatives are respectively +sqrt6 G''sqrt(t)+O(t)
and -sqrt6 G''sqrt(t)+O(t). Each slope and its y derivatives are
O(t), and each first time derivative and its y derivatives are bounded.
All the displayed remainders admit the differentiated bounds used here.
Equations (7)–(10) therefore give, on the fixed auxiliary spatial box,

\[
|Y_j|+|C_j|+|D_{y,u,z}Y_j|+|D_{y,u,z}C_j|\le C,
\quad |N_j|+|D_{y,u,z}N_j|\le C\sqrt t.
\tag{11}
\]

At z=0 the two physical maps coincide for every t,y,u, also in the
auxiliary radial extension. At t=0 their common imaginary coordinates
are (y,y-sqrt6 u,y+sqrt6 u) and their real coordinates vanish. Put

\[
\theta_u(y)=-\operatorname{Im}
 [\beta(iy)+\beta(i(y-\sqrt6u))+\beta(i(y+\sqrt6u))].
\]

Taylor's formula gives theta_u=theta+O(u^2), theta=-3 Im beta(iy),
uniformly on the chosen mean interval. The real-part floor makes all
tangents finite. Substitution in (7), using (10), gives on the side
Bp-Bs=-sqrt6 G''tan(theta_u)sqrt(t)+O(t) in the lower chart and
the opposite leading term in the upper chart. In (8), lambda0=1 and
lambda1=0. Hence both actual normal velocities have the same sign:

\[
N_j(t,y,u,0)={J''(y)-3G''(y)\tan\theta_u(y)\over\sqrt6}
                 \sqrt t+O(t)\quad(j=0,1).
\tag{12}
\]

The remainders are uniform on a fixed small u box. For the actual
0<=u<=sqrt(t), (12) is E(y)sqrt(t)/sqrt6+O(t), with E as in
C467t/u. This explicitly checks the whole radial side, not just its
vertex. On either compact positive or negative mean interval away
from zero, C467u gives E nonzero with sign y. Choose |u| sufficiently
small and then time sufficiently small. There are constants c0,C0>0
such that, throughout that interval,

\[
c_0\sqrt t\le |N_j(t,y,u,0)|\le C_0\sqrt t,\qquad
\operatorname{sgn}N_j=\operatorname{sgn}y.
\tag{13}
\]

The constants may depend on the fixed interval; no lower bound at y=0
is claimed. The actual interior is z<0 on the lower side and z>0 on
the upper side. Thus for y<0 characteristics pass upper to lower,
and for y>0 they pass lower to upper.

We also need bounds on their jump, not just their normals. At z=0 the
two graphs have the same F and v0. Their determinant factors are
(1-i m_y)(1-i ks)(1-i kp), and the corresponding slopes differ by
O(t^(3/2)). The remaining Vandermonde factors in K differ by a real
nonzero factor, since both are factorizations of the identical physical
F; this factor does not affect Im K/Re K. The phases of the determinants
therefore differ by O(t^(3/2)). Formula (7) gives
Y1-Y0=O(t^(3/2)). Formula (10) gives Bs,1-Bs,0=O(sqrt(t)).
The above D expansions give the same O(sqrt(t)) bound for the difference
of D_t/D; the difference of D_y/D is O(t^(3/2)). Finally (12) has
identical leading coefficients. Thus at the side

\[
Y_1-Y_0=O(t^{3/2}),\qquad
u(C_1-C_0)=O(u\sqrt t),\qquad N_1-N_0=O(t).
\tag{14}
\]

These uniform bounds hold also on the fixed small u extension. They
will control crossing derivatives without dividing by an uncontrolled
small angular coefficient.

### Piecewise characteristics and their expanding-edge hit

For now work on one compact mean band separated from zero, with nested
larger bands of the same sign. Extend the lower and upper graph fields
a fixed small distance beyond their free angular endpoints. Use (13)
only at their common side. A characteristic follows its chart's field
until z=0 and then follows the other field, at the same (t,y,u).
At positive time (13) gives unique transverse continuation. Every crossing
has the same orientation, so there is at most one crossing. The bounds
(11), nested mean margins and fixed angular extensions keep all paths
in this domain on one common small time interval. The multiplicative
radial equation gives

\[
e^{-Ct}u\le u(s)\le e^{Ct}u\quad(0\le s\le t).
\tag{15}
\]

For each positive lower time the piecewise flow is continuous, smooth
on each region of fixed crossing pattern, and has one-sided smooth
extensions at a terminal crossing. To control the derivative, differentiate
the equation z(s_c)=0 at a crossing time. If n=(0,0,1), the derivative
correction between the two ordinary variational flows is

\[
\mathcal S=I+{(b_{\rm after}-b_{\rm before})n^T
                         \over n\cdot b_{\rm before}}.
\tag{16}
\]

Indeed the hit-time variation is -n^T delta X/(n dot b_before);
subtracting the after-field time variation gives exactly (16). For
backward travel interchange before and after. By (13)–(14), both
versions are bounded uniformly down to zero time. Their radial-row
off-diagonal entry is O(u). Ordinary variational equations with (11)
and the single correction (16) consequently give

\[
|D_{y,u,z}X(s;t,y,u,z)|\le C,\quad
|\partial_y u(s)|+|\partial_z u(s)|\le Cu,
\quad |\partial_u u(s)|\le C.
\tag{17}
\]

For the radial row inside either chart, differentiate
u(s)=u exp(integral C_j); the derivatives of C_j are bounded.
The O(u) row of (16) preserves these estimates at the crossing.
Flow composition gives partial_t X=-D X b_terminal on each such
region, so all terminal-time derivatives are bounded and
|partial_t u(s)|<=Cu as well.

Bounded velocities make the endpoints Cauchy as s decreases to zero,
uniformly in the terminal data. Positive-time continuous dependence,
followed by this uniform limit, proves continuity of the time-zero
endpoint, including terminal points whose crossing time tends to zero.
Uniqueness follows by continuation on every positive interval. No
smoothness in physical time at zero or matching of the two fields
themselves is asserted. This also defines the flow for u=0.

For u>0 and u<=sqrt(t), set J(s)=u(s)^2-s. On the fixed small
radial box decrease its radius so 2u(s)^2|C_j|<=1/2. Then
J' is between -3/2 and -1/2 on each chart. It is continuous at a
crossing and strictly decreasing throughout. Since J(0)>0 and J(t)<=0,
there is a unique outer hit sigma in (0,t], with

\[
c u^2\le\sigma\le C u^2.
\tag{18}
\]

The segment after that hit stays in the actual radial domain. Before
stopping it may use an extension beyond a free angular endpoint, where
no value was prescribed. Using (17) to differentiate J(sigma)=0 gives,
on each branch,

\[
|\sigma_u|\le Cu,\qquad
|\sigma_t|+|\sigma_y|+|\sigma_z|\le Cu^2.
\tag{19}
\]

The other hit coordinates have bounded first terminal derivatives,
including time. These statements extend as one-sided bounds when the
hit is the outer corner z=0. Corner compatibility of the selected data,
rather than smoothness of the piecewise field, will remove the possible
solution singularity there.

### A corner-compatible upper outer value

Denote by R(t,y,u,z) the lower reference from C467r in (6), initially
for z in the lower extended interval and u<=sqrt(t). It solves the
lower transport, has range [0,1], and equals the prescribed edge at
u=sqrt(t). We need it slightly beyond that edge as a device to choose
upper data, not as a replacement lower boundary condition.

Such an extension follows from the same selected-edge hit. In C467r's
(y,ell,w) variables, the function ell(s)^2-d_+(s,y(s))^2 has derivative
between -8 and -4 on a small fixed box. For ell>d_+(t,y), follow the
lower field forward until its unique zero; for ell<=d_+ follow backward.
The hit time is comparable to ell^2. Existence follows from the positive
value at zero, the strict negative derivative, and continuation to a
time larger than a fixed multiple of ell^2+t. Choose the working time
and ell radius inside the already available coefficient horizon.
Means and angles retain the same strict margins as in C467r.

Evaluate exactly C467r(10)'s extended selected edge E at this hit.
No new boundary values are introduced. Its estimates (12), the radial
variation and the nonzero hit derivative give the same bounds as
C467r(17)–(19), also for a forward hit. In particular the derivative
of its hit time with respect to ell is O(ell), and its other terminal
derivatives are O(ell^2), so E_t=O(sigma^(-1/2)) causes no divergence
in R_ell. Transforming by (6), using bounded D_t and W_t from (9), gives

\[
|R_t|+|R_y|+|R_u|+|R_z|\le C_f,\qquad
|R(t,y,u,z)-f(y)^3|\le C_f(t+u),\quad 0\le R\le1.
\tag{20}
\]

These hold on a fixed small radial extension, for positive u,t, with
the needed angular margins. The comparison uses bounded mean drift,
hit time O(u^2), and the O(sqrt(sigma)) edge error. At u=sqrt(t) put
g0(t,y,z)=R(t,y,sqrt(t),z). It is the fixed lower outer datum and

\[
|g0-f(y)^3|\le C_f\sqrt t,\quad
|g0_t|\le C_f t^{-1/2},\quad |g0_y|+|g0_z|\le C_f.
\tag{21}
\]

Construct an upper solution germ W near the outer corner by following
the upper field to z=0 and evaluating R there. At an upper point with
u^2/t between 1/2 and 2 and |z|<=delta t^(3/2), (13), (11) and a
sufficiently small fixed delta ensure a unique hit at a time h between
t/2 and 2t. More explicitly, on this time interval normal velocity
has its fixed sign and magnitude at least c sqrt(t) in a sufficiently
small angular neighborhood: its z derivative is O(sqrt(t)). The time
needed to traverse |z| is at most C|z|/sqrt(t), less than t/2 for
small delta. Radial and mean displacements over this time respect
the fixed margins. Travel forward for negative y and backward for
positive y when z>0. A small signed z neighborhood is also allowed.

The positive-time implicit function theorem gives smooth dependence.
Using (11) in the variational equation on this interval, the derivative
of the angular flow with respect to initial y or u is O(t^(3/2)).
Dividing by the hit normal gives h_y,h_u=O(t), whereas h_z=O(t^(-1/2)).
Flow composition gives h_t=O(1). The other hit coordinates have bounded
t,y,u derivatives and z derivatives O(t^(-1/2)). Evaluating (20) there
proves

\[
|W-f(y)^3|\le C_f\sqrt t,\quad
|W_t|+|W_y|+|W_u|\le C_f,\quad |W_z|\le C_f t^{-1/2}.
\tag{22}
\]

Here W has range [0,1], solves the upper transport, and equals R at
z=0. The inverse hit construction is only auxiliary: backward hits
from the upper outer edge may have r>1. The extension (20) covers
them, and none is asserted to be a path inside the original triangle.

Choose a fixed smooth function chi:[0,infinity)->[0,1], equal to one
near [0,1/3] and zero on [2/3,infinity). On the upper outer boundary set

\[
g1(t,y,z)=f(y)^3+
\chi\!\left({z\over\delta t^{3/2}}\right)
 [W(t,y,\sqrt t,z)-f(y)^3]\quad(z\ge0).
\tag{23}
\]

Outside W's collar define the product term to be zero; the cutoff
already vanishes on a neighborhood of that collar boundary. Near
z=0 extend by W for a small negative z neighborhood. Thus g1 is
smooth at positive time, has range [0,1], and agrees with the upper
continuation germ exactly on a smaller corner collar. From (22),

\[
|g1-f(y)^3|\le C_f\sqrt t,\quad
|g1_t|\le C_f t^{-1/2},\quad
|g1_y|\le C_f,\quad |g1_z|\le C_f t^{-1}.
\tag{24}
\]

For the last estimate, the cutoff derivative costs t^(-3/2) times
O(sqrt(t)); for the time derivative it costs t^(-1) times that same
error, and the outer substitution contributes W_u/(2sqrt(t)).
These are the precise costs of selecting the upper outer data. The
cutoff is applied to free boundary values, not multiplied into an
interior solution of the transport equation.

### The selected component, its smoothness and continuous limits

For u>0 assign to each terminal point the value g0 or g1 at the unique
backward outer hit (18), according to the hit side. Follow the piecewise
characteristic with its actual transmission. This defines U(t,y,u,z).
It has range [0,1]. On each open region of fixed hit/crossing pattern it
is smooth and solves the corresponding original normalized transport.
On z=0 both side values agree, by the same piecewise trajectory.

There are two possible smoothness issues, which must be addressed
separately. At an interior shared side point t>0,0<u<sqrt(t), its
outgoing-chart solution is smooth: backwards it stays in that chart
until its outer hit (possibly beyond a free endpoint). The incoming
solution is its transport through a noncharacteristic side, by (13).
It therefore has a smooth one-sided extension using its own field.
No equality of the two charts' normal derivatives is required.

The second issue is the characteristic issued from the outer corner,
where the identity of the boundary supplying data changes. At every
positive-time corner, (23) equals W on an open collar, and W is the
upper continuation of the lower R. For negative y, an upper outer
point in that collar reaches the side in forward time, with value R;
the subsequent lower characteristic also carries R. Thus both hit
branches agree with the same smooth lower solution in a neighborhood
of their switch. For positive y, the same construction follows the
upper field backward to R on the extended side. It is a smooth upper
solution germ across the corner. Propagating that germ along the upper
positive-time flow shows that both hit branches agree as smooth
solutions near the entire corresponding switching characteristic.
Each fixed point there has a strictly positive corner time, so ordinary
local smooth-flow dependence applies. This proves all-order smoothness
at the switch, not just equality of the two boundary values.

The angular midpoint causes no additional switch: (7)–(8) are smooth
through it, without dividing the original test by its vanishing
Vandermonde. The free angular endpoints have the fixed auxiliary
margins already chosen. Hence U has precisely the required smooth
endpoint extensions for positive time and positive interior radius.

Let y0(t,y,u,z) be the continuous time-zero mean endpoint of the
piecewise auxiliary flow. The stopped path agrees with that full flow
down to its outer hit. Its remaining mean displacement is O(sigma).
Using (21),(24),(18),

\[
|U(t,y,u,z)-f(y0(t,y,u,z))^3|\le C_f u.
\tag{25}
\]

Consequently define U(t,y,0,z)=f(y0(t,y,0,z))^3. Uniform continuity
of the endpoint map proves joint continuity at u=0, including z=0.
This vertex value may depend on z. It is not the old independently
selected value on both sides. Since |y(s)-y|<=Ct and sigma<=t,
the direct outer comparison also gives

\[
|U(t,y,u,z)-f(y)^3|\le C_f\sqrt t
\quad(0\le u\le\sqrt t).
\tag{26}
\]

These estimates prove continuity at time zero uniformly in r and both
angles after (6), with f(x)^3 since y=x+O(t).

It remains to cover means near zero without using transversality there.
Take the construction on two open bands
b_*/4<+y<4b_* and b_*/4<-y<4b_*, using slightly larger compact
bands inside (-X,X) separated from zero. On |y|<b_*/2 set U=1;
on |y|>3b_* set U=0. These definitions agree on their overlaps after
one further common time reduction. To see exact equality, C467p's
selected function is the product of f at its backward physical initial
coordinates, differing from the edge coordinates by O(t). Those edge
coordinates are y+O(sqrt(t)), uniformly on the needed extensions.
Thus g0 and the reference R are exactly one on a slightly enlarged
central collar and exactly zero on a slightly enlarged outer collar.
The short corner paths, the convex combination (23) and the stopped
paths move the mean by only O(t), so they preserve those exact constant
values on the stated overlaps. The available gaps from b_* and 2b_*
are fixed and positive. This argument uses no monotonicity or evenness
of f. The same observation shows that the prescribed lower outer edge
itself is one or zero on those overlaps. This is gluing equal functions,
not multiplying an interior transport by a spatial cutoff.

The definitions therefore cover every original x and have smooth
x-endpoint extensions, where they are zero. Set
psi0(t,x,r,lambda)=U(t,y(t,x),r sqrt(t),lambda-1) and
psi1(t,x,r,lambda)=U(t,y(t,x),r sqrt(t),lambda).
All assertions of (3), including its exact selected lower edge and
radial equality at r=0 and r=1, now follow. The common minus sign
cancels from each transport quotient. At an original divisor zero
the undivided equation holds by its zero coefficients and the proved
interior smoothness.

### Eight separate products and both complete cutoff identities

On every smooth hit branch, (17)–(19), (21),(24), and sigma comparable
to u^2 give the deliberately coarse bound

\[
|U_t|+|U_y|+|U_u|+|U_z|\le C_f u^{-2}
\quad(t>0,\ 0<u<\sqrt t).
\tag{27}
\]

For example the largest boundary derivative is O(sigma^(-1)) in z;
the hit-coordinate derivatives are bounded. The boundary time derivative
O(sigma^(-1/2)) is multiplied by O(u) for a radial terminal derivative
and by O(u^2) for the other ones. These bounds also hold at the smooth
switch by continuity, and as one-sided limits at the common side.
The constant regions cause no loss. Converting (27) to the original
parameters, using y_x,y_t bounded and u_t=r/(2sqrt(t)), yields

\[
|\psi_{j,t}|\le C_f r^{-2}t^{-3/2},\qquad
|\psi_{j,x}|+|\psi_{j,\lambda}|\le C_f r^{-2}t^{-1},\qquad
|\psi_{j,r}|\le C_f r^{-2}t^{-1/2}.
\tag{28}
\]

Take tau<=1. C467k(19), for s_j=1-2lambda in each triangle, bounds
the original complex coefficients by
|A_j|+|U_j|<=C r^7 t^4 s_j^2, |B_j|<=C r^8 t^3 s_j^2,
|V_j|<=C r^7 t^3 s_j^2. Therefore, separately for j=0,1,

\[
|A_j\psi_{j,t}|\le C_f r^5t^{5/2}s_j^2,\quad
|U_j\psi_{j,x}|\le C_f r^5t^3s_j^2,
\]
\[
|B_j\psi_{j,r}|\le C_f r^6t^{5/2}s_j^2,\quad
|V_j\psi_{j,\lambda}|\le C_f r^5t^2s_j^2.
\tag{29}
\]

Each is integrable on the entire original parameter box. No real-part
cancellation or replacement by a modulus-square density is used.

For epsilon<=t<=T<=tau and eta<=r<=1-zeta, apply the cited Stokes
theorem to each smooth test. With C467k's original A,B,U,V the identity is

\[
\begin{split}
\int( A\psi_t-U\psi_x+B\psi_r-V\psi_\lambda)
&=\int[\psi A]_{t=\epsilon}^{T}
 +\int[\psi B]_{r=\eta}^{1-\zeta}\\
&\quad-\int[\psi U]_{x=-X}^{X}
 -\int[\psi V]_{\lambda=0}^{1}.
\end{split}
\tag{30}
\]

The integrals in each line use the other original coordinate intervals
in their induced order, exactly as in C467k(20). This is a complex
identity. Multiplication of the entire identity by the common minus
sign changes every term together. All four bulk products have the fixed
majorants (29), so dominated convergence applies independently to each
along any joint sequence epsilon,eta,zeta tending to zero.

The lower-time face is bounded by C epsilon^4 uniformly in both radial
cutoffs. The inner radial face is bounded in absolute integral by
C eta^8 T^4, uniformly in epsilon,zeta, and hence tends to zero.
Continuity at the outer radial face gives its full limit, dominated
by C t^3; removing its small time interval costs O(epsilon^4) uniformly
in zeta. The x faces have majorant C r^7 t^4 and the angular faces
C r^7 t^3. At fixed upper time continuity gives the full A-face limit.
Thus every term in (30) converges for independent cutoffs, with no
missing corner term and no imposed boundary derivative at r=0 or t=0.

Finally the restricted maps and their t,x,r derivatives agree at
lambda0=1 and lambda1=0. Their original V coefficients are equal,
their induced signs in (30) are opposite, and (3) gives the same test
value. These two terms cancel exactly upon addition. All other angular,
outer, time and x-side terms remain as written; no further cancellation
or favorable sign is asserted. This completes the local construction,
with the independent conceptual audit recorded below.

### Independent conceptual audit — 16 November 2026, step1066

This is a REPRODUCTION audit under the unchanged SPECIALIZE assessment
`drafts/literature/2026-11-16-coupled-adjacent-conceptual-audit-nomination-1064.md`,
approved separately by review1065. It validates the existing construction,
not an upper-pair extension or a new general transmission theorem. The
qualified finite-zero input in the hypotheses remains external and
unreplayed. C467s's entire reflected construction is not used.

The ordinary-chart, Stokes and dominated-convergence inputs are the
precisely cited Teschl, Conrad and Hunter results above. For (16) import
the identity-reset, stationary-guard specialization of Nathan J. Kong,
J. Joe Payne, James Zhu and Aaron M. Johnson, *Saltation Matrices: The
Essential Tool for Linearizing Hybrid Dynamical Systems*, Proceedings
of the IEEE 112(6) (2024), 585–608, DOI 10.1109/JPROC.2024.3440211,
[arXiv2306.06862v3, section III-B, equations (16)–(30), and
Appendices A/B](https://arxiv.org/html/2306.06862v3).
Review1065 inspected both event-time perturbation cases. The guard here
is z=0, the reset is the identity, and the positive-time extensions are
smooth and transverse by the checks below. Thus the formula is used
only on a fixed event branch at positive time. For reverse travel it
is the inverse correction, with the incoming and outgoing fields
interchanged. No cited theorem supplies the uniform zero-time estimates.
Burden et al.'s event-selected-flow theorem, compared in review1065,
is not needed to infer stronger smoothness across the field jump.

**Actual coordinates, differentiated expansions and full-side incidence.**
The inverse mean chart and all auxiliary mean intervals have strict
margins inside C467e's regular coefficient neighborhood. C467q's exact
quadratic reconstruction gives (4)–(5); the permuted upper graph is
checked in C467t/audit1062. In particular (6) sends z=0 to the same
physical triple in both charts. At positive t,u the coordinate changes
are nonsingular. At u=0 the graph quotient is used as an auxiliary
field only; no immersion of that collapsed face is asserted.

Let epsilon=M3/(3A^3). The simple branches of v^3-v-epsilon=0 have
values -1+epsilon/2+O(epsilon^2), -epsilon+O(epsilon^2), and
1+epsilon/2+O(epsilon^2), with smooth remainder functions. Consequently
W_+=1/2-epsilon+O(epsilon^2) and
W_-=-1/2-epsilon+O(epsilon^2). C467t/audit1062's factorizations give
epsilon=t^(3/2)[2J''/(3 sqrt(6))+t R(t,y)], with smooth R. This
proves both coefficients in (9), including their differentiated errors.
More specifically D_+=a(t,y)+t^(3/2)R_+(sqrt(t),y) and
D_-=-a(t,y)+t^(3/2)R_-(sqrt(t),y), where a(0,y)=sqrt(6).
Their first t derivatives and the required y derivatives are bounded.
Taking logarithms of the nonzero W's and differentiating gives exactly
the signs and coefficients of the two logarithmic derivatives in (9).
These are differentiated factorizations, not derivatives inferred from
an isolated asymptotic estimate.

The identity kp-ks=c(S/d-2d), S=M2/3, and
c=-G''t/2+O(t^2) give the opposite leading coefficients in (10).
Here S/d-2d has leading values -8 sqrt(t)/sqrt(6) and
+8 sqrt(t)/sqrt(6). The remainder is t^2 times a smooth function of
sqrt(t),y, so its t derivative is O(t). Also
kp,-−kp,+=O(t^(3/2)) and ks,-−ks,+=O(t^(3/2)), with t
derivatives O(sqrt(t)) and the same spatial bounds. The common a0
has smooth physical-time dependence. Thus (7) really has bounded
spatial derivatives. The chain rule for ell=D u and for w in (6)
gives (8), including both minus signs in its angular expression.
In particular Bp−Bs and its spatial derivatives are O(sqrt(t));
the logarithmic W term is of that same order. This proves (11)
uniformly on a fixed auxiliary box.

At t=0 on the side the physical coordinates are
i(y,y−sqrt(6)u,y+sqrt(6)u). The phase of K modulo pi is theta_u;
all determinant factors there equal 1. The symmetric two displacements
cancel the linear term in u, giving theta_u=theta+O(u^2), with
uniform bounded derivatives on compact mean bands. The leading
differences v_p−v_s are −i sqrt(6)G''sqrt(t) in the lower chart
and its negative in the upper. For a real a,
−Re(K(−ia))/Re K=−a Im K/Re K. Substitution in (8) therefore
gives (12) with coefficient (J''−3G''tan(theta_u))/sqrt(6) in
both charts. Positive-time changes in the side phase are O(t),
uniformly for fixed small u; their contribution fits the displayed
O(t) error. In the actual domain u^2<=t the change from theta_u
to theta gives a still smaller O(t^(3/2)) contribution.

C467u/audit1062 gives a strictly positive minimum of |E| on every
compact band used here, and its sign is that of y. First choose an
auxiliary u radius making the O(u^2) change smaller than half that
minimum, then choose time to absorb the O(t) error relative to sqrt(t).
This proves (13) throughout the actual side and the retained extension.
There is no use of such a minimum at y=0.

For u!=0 on the common side, the two Vandermonde expressions in K
differ by the real positive factor coming from ell^6 w^2; F itself
is identical. Their phase difference is therefore just the difference
of the determinant phases, O(t^(3/2)). This statement extends to
u=0 by the smooth factorizations. The common v0 then gives the
O(t^(3/2)) mean-field jump. The slope derivative differences give
the O(sqrt(t)) Bs jump. The D factorizations give
Delta(D_t/D)=O(sqrt(t)) and Delta(D_y/D)=O(t^(3/2)). Finally
(12) has the same leading coefficient on both sides. These facts
prove all three orders in (14), on the fixed auxiliary box as required.

**Crossing variations, endpoint continuity and the outer hit.**
Use nested mean bands of a fixed sign; bounded mean velocity keeps
paths in them for one common small time. On z=0 every crossing has
that same orientation by (13). A second crossing would require the
opposite orientation between the two sign regions, so is impossible.
The free angular endpoints have fixed extension margins, and the
O(sqrt(t)) angular velocity preserves those margins after decreasing
time. The multiplicative radial equation gives (15).

In (16) the three entries of (b_after−b_before)/(n dot b_before)
are respectively O(t), O(u), O(sqrt(t)). The reverse correction has
the same bounds because its denominator is the other normal, also
bounded below by c0 sqrt(t). Ordinary variational flows have uniformly
bounded matrices by (11). Their radial off-diagonal entries are O(u),
as follows by differentiating u(s)=u exp(integral C). Multiplying by
the single crossing correction preserves this row property and the
full matrix bound. This verifies (17) in both time directions on every
fixed branch. The reverse formula is also algebraically the inverse
of the forward one since n dot b_after is nonzero.

For fixed positive s the flow is continuous across changes of event
pattern: a crossing of zero duration has zero positional displacement,
and the event time is given by the transverse implicit equation. It
has the usual one-sided derivatives, not a claimed common derivative
across z=0. Bounded velocities give |X(s1)−X(s2)|<=C|s1−s2|,
uniformly in all retained terminal data. Thus the positive-time maps
converge uniformly as s decreases to zero, giving a continuous endpoint
map also when the crossing time tends to zero. Flow composition on
each branch gives the terminal-time derivative −DX b_terminal; its
radial row is O(u). No bound on a second t derivative is used.

For the outer hit J=u(s)^2−s, each smooth segment has
J'=2u(s)^2 C_j−1. Choose the auxiliary radius so |2u(s)^2 C_j|<=1/2.
Although J' may jump at the shared side, J is continuous and strictly
decreasing with slope bounds −3/2 and −1/2. Its values at 0 and t
have the stated opposite signs for 0<u<=sqrt(t). This proves existence
and uniqueness of sigma, and (15) at sigma gives sigma comparable to
u^2. At a fixed branch differentiation gives
sigma_a=−2u(sigma) partial_a u(sigma)/J'(sigma).
The radial row and terminal-time bound above give exactly (19).
Adding b(sigma) sigma_a to each fixed-time derivative bounds the
other hit coordinates. At a corner hit these are one-sided branch
bounds; smoothness of the selected scalar is checked separately below.

**Reference extension and the upper corner germ.**
For the lower reference, C467r/audit1056 verifies the selected edge
E, its positive-time smooth trace, its strict auxiliary margins and
the four estimates in C467r(12). Its equation for ell has bounded
spatial derivatives. The same edge function
J_l=ell(s)^2−d_+(s,y(s))^2 has −8<=J_l'<=−4 on a fixed small
box, independently of which direction leads to its zero. At s=0
its value is ell(0)^2>0. At a time C ell^2 its value is negative
for a sufficiently large fixed C, using the radial exponential bound
and d_+^2 comparable to s. Choose the box and final time so this
time lies inside the available coefficient and selected-edge horizon.
Thus the forward hit exists for points beyond the edge, is unique,
and is comparable to ell^2. All intervening means and angles remain
within their fixed margins. This supplies an actual extension, not
an arbitrary exterior datum.

The same variational calculation on a forward segment gives
sigma_ell=O(ell) and sigma_t,sigma_y,sigma_w=O(ell^2): the
additional term (d_+^2)_y partial_a y is O(sigma)=O(ell^2)
at the hit. The edge derivative E_t=O(sigma^(−1/2)) is therefore
multiplied by at least O(ell), and all reference derivatives are
bounded. Changing to u,z uses bounded D_t,W_t and their spatial
derivatives, as just checked. This proves (20), and differentiating
u=sqrt(t) gives (21). The reference comparison follows from mean
drift O(t+sigma) and edge error O(sqrt(sigma)).

For the upper germ, u^2/t in [1/2,2] and |z|<=delta t^(3/2)
place a side hit in [t/2,2t] for one fixed sufficiently small delta.
Throughout that interval (13) persists in a small angular neighborhood:
|partial_z N|<=C sqrt(t), and the mean and radial displacements
respect the chosen margins. The time to cover |z| is at most
C|z|/sqrt(t). Its orientation is forward for y<0,z>0 and backward
for y>0,z>0, exactly as asserted. The latter case may hit outside
the actual radial domain, which is why (20)'s extension is needed.

The angular variational entries from initial y,u to the hitting angle
are O(t^(3/2)), since their differential equations have forcing
O(sqrt(t)) over a time O(t), with bounded remaining variations.
Dividing by the side normal gives h_y,h_u=O(t), while h_z=O(t^(−1/2)).
The flow-composition identity gives h_t=O(1). The other hitting
coordinates have bounded t,y,u derivatives and O(t^(−1/2)) z
derivatives. Applying (20) proves every estimate in (22), including
the range and the comparison to f(y)^3. Hitting the same side point
along an upper characteristic proves that W solves that transport.

The derivative of chi(z/(delta t^(3/2))) in t is O(1/t) on its
support, and its z derivative is O(t^(−3/2)). Multiplication by
W−f(y)^3=O(sqrt(t)), together with W_u/(2sqrt(t)) on the outer
edge, gives g1_t=O(t^(−1/2)), g1_z=O(t^(−1)), and bounded g1_y.
This verifies (24). The cutoff is zero on a neighborhood of the
collar boundary, so no regularity claim is made about an undefined W
outside that collar. Near z=0 it is identically one and g1 equals
the same smooth upper germ on an open neighborhood.

**Smooth switches, continuous vertices and constant regions.**
On each fixed hit branch the construction is a smooth characteristic
solution. At a positive-time interior shared-side point the donor
chart, whose forward field points toward the side, has a backward
path staying in that chart; its outer-hit solution is smooth locally.
The receiver obtains a smooth one-sided extension by transverse
transport of that trace. This does not identify the two normal
derivatives.

At a switch issued from a positive-time outer corner, the scalar
agreement is stronger than agreement at one boundary point. For y<0,
the upper g1 agrees with W on an open collar; W transports to R at
the side and the subsequent lower trajectory carries the smooth
lower R. Both possible outer-hit branches therefore equal R on an
open neighborhood of the switching characteristic in the lower chart.
For y>0 the donor is the lower reference, and both branches agree with
its upper continuation W near the corner; the smooth upper flow
propagates this equality along the switching characteristic. Every
fixed interior point on such a characteristic has a positive corner
time. Hence local propagation proves equality of all derivatives,
without requiring a uniform higher-derivative bound at zero time.
This proves smoothness at the switch; midpoint smoothness follows
from the undivided field extension and the fixed angular margins.

The full auxiliary path after its outer hit agrees with the stopped
path. Its extra mean displacement to time zero is O(sigma). Both
outer data differ from f at their hit mean, cubed, by O(sqrt(sigma)).
Since sigma is comparable to u^2, (25) follows. The uniformly
continuous endpoint map proved above then gives joint continuity at
u=0, including the common side. It can depend on the angle, as
permitted. On the actual domain sigma<=t and the total mean drift
is O(t), so (26) follows uniformly. The inverse mean relation
y=x+O(t) gives the exact time-zero value f(x)^3.

For the remaining mean regions, C467p(33)–(34) expresses the selected
edge as the product of f at initial physical coordinates differing
from its edge coordinates by O(t). Those edge coordinates differ
from y by O(sqrt(t)). At the reference's forward or backward hit the
same statement has error O(t+u). Choose the auxiliary radius and
time below the fixed gaps to |y|=b_* and |y|=2b_* in the specified
overlaps. Thus all three factors are exactly 1 on the central overlap;
on the outer overlap all lie outside the support and the product is
exactly 0. The corner paths and stopped paths have mean displacement
O(t), so the same exact values persist through (23) and transport.
The constant and band solutions agree on open overlaps. This verifies
smooth gluing, with no evenness, monotonicity or interior cutoff
assumption on f. The bands and all auxiliary neighborhoods can be
chosen first, followed by finitely many common reductions of time.
The final tau is strictly inside the construction horizon, giving
the needed upper-time extension as well.

**Eight original products, independent limits and verdict.**
At every smooth hit branch, the derivatives of the hit coordinates
are bounded, g0 has the bounds (21), and g1 has (24). The largest
possible boundary derivative is O(sigma^(−1)) in the angular
coordinate; sigma comparable to u^2 therefore gives (27).
The boundary time derivative multiplies sigma_u=O(u) or the
O(u^2) other hit-time derivatives, and is no larger. Smooth germ
agreement carries the same first-derivative bounds to the switch.
In the original variables u_t=r/(2sqrt(t)), u_r=sqrt(t),
y_t,y_x=O(1) and z_lambda=1, so the deliberately weaker (28)
is valid for t,r<=1.

Multiplying by C467k(19)'s separate complex coefficient bounds gives,
for each j=0 and j=1, respectively
Cr^5 t^(5/2)s_j^2, Cr^5 t^3 s_j^2,
Cr^6 t^(5/2)s_j^2 and Cr^5 t^2 s_j^2.
All exponents at both lower endpoints exceed −1. These are eight
absolute majorants; neither the real transport identity nor a
cancellation between products is needed for their integrability.

On positive cutoff boxes the scalar is smooth with endpoint extensions,
and the original holomorphic top form is closed including its divisor.
With orientation dt dx dr dlambda, wedging dpsi with the pullback
gives A psi_t−U psi_x+B psi_r−V psi_lambda. The positive face
orientations are respectively +dx dr dlambda, −dt dr dlambda,
+dt dx dlambda and −dt dx dr, so (30) has exactly all four signs.
The common minus normalization changes the entire identity together.

For arbitrary independent cutoff sequences, dominated convergence
applies to each of the eight bulk terms with the fixed majorants.
The lower-time face is O(epsilon^4) uniformly in the radial cutoffs;
the inner radial face is O(eta^8 T^4) uniformly in the others.
On the outer radial face continuity and |psi B|<=Ct^3 give its
full limit, with discarded lower-time mass O(epsilon^4). The angular
faces are bounded by Cr^7t^3, and the x faces by Cr^7t^4; both
have continuous traces and integrable majorants. At fixed T the
spatial face is continuous with bound Cr^7T^4. These checks cover
all faces, including joint limits at their corners; no derivative at
r=0 or t=0 is asserted or required. Each full identity thus holds
independently of the manner of cutoff removal.

At the shared angular face the actual maps, F and their t,x,r
columns coincide, so the original V coefficients coincide. The tests
have the same continuous trace and the two angular endpoint signs
are opposite. Their complete limiting face integrals cancel. This
does not cancel or pay any remaining face. The audit therefore
validates (3), all eight L1 assertions and both full identities on
one common existential interval, under the original hypotheses.
It establishes a checked local input, not novelty beyond the sources
assessed or a complete RH argument. Stops1058/1060 are unchanged;
upper-pair compatibility, other interfaces, exterior payment,
realization, all degrees and Xi transfer remain unresolved.

## Mathlib

Full matching coverage for this actual two-triangle transmission,
corner-compatible selection, continuous vertex limit and independent
cutoff identities has not been checked. The supporting ODE,
implicit-function, Stokes and dominated-convergence inputs are not a
formalization of this result. No absence or formal-verification claim
is made. The informal construction is validated by audit1066 above;
this is not a formal verification and retains its external-input qualification.
