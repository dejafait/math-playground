# C468e — A glancing trace obstruction to the joint chamber/pair selection

## Hypotheses

Retain the exact joint selection problem of nomination1086/review1087
and C468a–d, the actual coefficient flow of C467e, the inverse pair
chart of C467p, the regular physical chamber graph of C467z, and
C467's glancing diagnostic. In particular,

\[
n=3,\quad R=1/4,\quad a_0=1/16,\quad T_0=1/1920,\quad
X=1/256,\quad b_*=1/4096,\quad H_*=1/128.
\tag{1}
\]

The original initial-coordinate chamber collar is
u=(x-d,x+d,x+h), |x|<=X, 0<=h<=H_*, 0<=d<=h/4.
The pair is the original |x|<=X, |s|<=1, 0<=h<=H_* box, with
the original lower-slot permutation between its two s endpoints.
Use the actual conjugation-normalized logarithm
B(w)=log[xi(1/2+sqrt(w))/xi(1/2)] on its specified local branch,
beta(z)=B(1+z)-B(1)-B'(1)z, g=beta', and |beta''|<40 on |z|<R.
Keep H=H0+sum_j beta(z_j), real H0, F=Delta^2 exp(-H), the
algebraic square, original divisor, raw time and common minus sign.

Retain the inherited L018/L021/L024/C466a finite-zero/product
qualifications, in particular the signs imported through C467u.
Their cited finite verification accounts for positive ordinates
through100 on the line and isolates the first in (14,15): Suvrit Sra,
*On some positivity properties of the Riemann Xi function*,
[W_pr5z5huy_v1, section2.1, equations(6)–(8)](https://hub.valency.io/works/W_pr5z5huy_v1).
This external input has not been independently replayed here; no
stronger statement about zeros is introduced.

Let f be any fixed smooth real [0,1]-valued bump, equal to one on
[-b_*,b_*], supported in (-2b_*,2b_*), with no evenness assumption.
A joint candidate consists of real [0,1]-valued Theta and phi,
continuous on the two original closed domains including time zero,
smooth on their regular positive-time interiors, satisfying their
original undivided adjoint equations, and having initial values
product_j f(u_j) and f(x)^2 f(x+h). Their matched trace is

\[
T(t,x,h)=\Theta(t,x,x,x+h)=\phi(t,x,1,h).
\tag{2}
\]

No derivatives at time zero, at the collision face or at h=0 are
assumed. The outer-face extensions are allowed exactly as in the
nomination, with no prescribed lateral values beyond continuity
and the initial products. The original step did not audit its C468a–d inputs; their load-bearing
claims and this argument are checked in conceptual audit1094 below.

## Conclusion

Under these qualifications, no such jointly selected Theta and phi
exist on any positive common time horizon. The obstruction uses only
the positive endpoint and a compact positive-center portion of its
glancing surface. It therefore permits arbitrary choices of the
allowed outer-face data and does not fix either scalar to its earlier
auxiliary transport.

More precisely, the necessary glancing trace is smooth for t>0 and
obeys, in center coordinates c=x+h/3,

\[
\partial_c S+r(t,c)\partial_t S=0,\qquad |r(t,c)|\le C t,
\quad b_*\le c\le2b_*,\quad 0<t\le\tau,
\tag{3}
\]

for some C<infinity and tau>0. Its continuity at time zero gives
S(0,c)=f(c)^3. Equation(3) forces S(0,b_*)=S(0,2b_*), contradicting
1=0. These are necessary conditions on an unknown candidate, not
time-zero differentiations of it.

This is a qualified stop of the complete nominated collar/pair
class, broader than C468d's fixed-chamber stop, validated by
conceptual audit1094 below. It is not a disproof
of RH or of all signed-assembly mechanisms. Different domains or
regularity classes are not decided here. Integrability, cyclic
matching, global assembly, realization and actual-Xi positivity
remain separate; this result does not provide any of them.

## Proof

### Gate, comparison and imported tools

Use the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-16-boundary-fed-chamber-pair-nomination-1086.md`,
separately approved at review1087. Its target includes a forced-trace
obstruction for this jointly selected class. C468c supplies the
necessary first jet but does not propagate it along the glancing
surface. C468d evaluates that jet for one selected chamber datum;
its leading velocity calculation is reused, with the uniform error
rate needed here proved below. The narrow duplicate/failure check of
C467/C467p/u/z, C468a–d, working notes1088–1091 and stops1081/1091
found no such intrinsic glancing transport argument. The assessed
stops1043/1058/1060/1068/1084 retain their different hypotheses.
This comparison neither certifies novelty nor reopens a fixed datum.

Import the already assessed regular ODE results of Gerald Teschl,
*Ordinary Differential Equations and Dynamical Systems*, April2012
author preliminary version,
[Theorems2.5/2.10 pp40–47, Lemma2.14/Corollary2.15 pp52–53,
Theorems3.9/3.12 pp81–84 and Theorem6.1/proof pp189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf),
together with the classical smooth implicit function theorem and
Taylor theorem. Every new ODE below stays in a positive-time smooth
chart. The elementary logarithmic differential inequality is proved
where used. No general glancing existence theorem is imported or
reproved. The new work is the uniform actual-field cancellation and
its consequence for the trace forced by C468c.

### The glancing surface and its two tangent fields

Write D=mathfrak D for C467's smooth diagnostic. Fix a compact
interval K contained in (0,X) whose interior contains [b_*,2b_*];
for example K=[b_*/2,3b_*]. On a sufficiently small common horizon,
C467(3)–(4) and the implicit function theorem give a smooth graph

\[
h=h_g(t,x)=\tfrac12 d(x)t^2+O(t^3)>0,\qquad
D(t,x,h_g)=0,
\tag{4}
\]

uniformly on K. Here d(x)>0; after a reduction both h<=C_K t^2
and a positive lower comparison with t^2 hold on K. The graph is
smooth through t=0, since D_h(0,x,0)=-2. Its differentiated Taylor
bounds, including h_{g,x}=O(t^2), follow from that smooth implicit
graph, not differentiation of an unqualified O(t^3) error. All
glancing points under consideration have strict x and upper-h margins
and belong to the fixed-margin core of C468b/c after reducing time.

Use physical coordinates Q=(m-v,m+v,q), I=2m+q and
rho=v^2-w0(t,I,q), where w0 is the squared seam half-gap. At the
positive endpoint the physical fields are

\[
X_j=\partial_t+b_j\cdot D_Q\quad(j=c,p),\qquad
W=X_p-X_c=(b_p-b_c)\cdot D_Q.
\tag{5}
\]

C468a(2) gives X_j rho=K_j D on the seam, with K_j>0.
Thus both fields are tangent to rho=0 at glancing. C468c(2) gives
X_cD>=d_c/(4h)>0, where D is extended by the inverse (t,I,q)
chart independently of v, and d_c>0 is uniform. Define there

\[
\delta=\frac{W D}{X_cD},\qquad
Y=W-\delta X_c
  =X_p-\frac{X_pD}{X_cD}X_c.
\tag{6}
\]

This is a smooth tangent vector field on the positive-time glancing
surface: Y rho=0 and YD=0. The two defining differentials are
independent there, since rho_v=2v!=0 and D_h in the seam chart is
nonzero. In particular that surface has coordinates (t,x), or
(t,c) with c=x+h_g/3. The latter change has derivative
1+h_{g,x}/3>0. Restricting to a slightly smaller center interval
still containing [b_*,2b_*] defines a smooth h=eta(t,c) and
x=c-eta(t,c)/3. All estimates below are uniform on this interval.

### A uniform rate for the physical velocity difference

Put epsilon=sqrt(t), a(x)=Re g(ix), k(x)=tan(3 Im beta(ix)), and
define the scalar coefficient

\[
\mathcal B(x)=-\frac{\sqrt6}{6}(1+k(x)^2)a(x)a''(x).
\tag{7}
\]

C467u gives a(x)<0 and a''(x)<0 on K. Hence mathcal B is negative
and bounded away from zero there. We need the following strengthening
of C468d(14), with a uniform error rather than only a fixed-x limit:

\[
b_p-b_c=\mathcal B(x)t^{3/2}(1,1,1)+O_K(t^2).
\tag{8}
\]

Here and below a vector or matrix O bound is in any fixed norm.
We give the rate justification in full because it is load-bearing.
All coefficient-flow and chamber-graph functions in C467e/z are
smooth with bounded fixed finite-order derivatives on the compact
neighborhoods in those results. Use those neighborhoods, then shrink
time once for K. The initial seam vector is

e0(c,h)=(3c,3c^2-h^2/3,c^3-c h^2/3+2h^3/27).

C468d(3)–(5)'s polynomial Taylor calculation therefore holds with
uniform constants. The centered cubic, scaled by Q=mu+epsilon z,
is z^3-6z+O_K(epsilon)(1+|z|), with mu=c+O_K(t).
Its three limiting roots r=(-sqrt6,0,sqrt6) have nonzero derivatives
3r_j^2-6. Disjoint compact simple-root neighborhoods and the implicit
function/Taylor estimate give

\[
Q_j=c+\epsilon r_j+O_K(\epsilon^2),\qquad
\mathcal Q_t'(Q_j)=\epsilon^2(3r_j^2-6)+O_K(\epsilon^3).
\tag{9}
\]

No root separation constant here tends to zero after scaling.
For the two seam tangents Q_c and Q_W=Q_h/h, use exactly the
numerators L(Q_j)D_t e0_c and L(Q_j)D_t(e0_h/h) from C468d(5).
The first is t(3r_j^2-6)+O_K(t^(3/2)); the second is
(2/3)epsilon r_j+O_K(t). To retain the cancellation in the first,
write S0=s+R_j for the coefficient generator, with
s(e)=(0,-6,-2e1) and j(y)=Im g(iy). At the triple vector e_c,
L(Q_j)e_c'=3(Q_j-c)^2, D s(e_c)e_c'=(0,0,-6), and
D R_j(e_c)e_c'=j'(c)e_c'+j(c)e_c''.
Since L(Q_j)e_c''=6(c-Q_j), the last expression contributes
O_K(t^(3/2)); e0-e_c and e0_c-e_c' are O_K(h^2).
Division by the uniformly nonzero scaled denominators in (9) gives

\[
Q_c=(1,1,1)+O_K(\epsilon),\qquad
\epsilon Q_W=
\left(-\frac1{3\sqrt6},0,\frac1{3\sqrt6}\right)+O_K(\epsilon).
\tag{10}
\]

Let n=D_Q rho at the seam. Its defining equations are
n.Q_c=n.Q_W=0 and n.(-1,1,0)=2v.
The limiting three vectors in this linear system are independent;
also 2v=epsilon sqrt6+O_K(epsilon^2). Inverting the system with
the O_K(epsilon) errors from (10) proves

\[
n=\epsilon n_0+O_K(\epsilon^2),\qquad
n_0=\frac{\sqrt6}{3}(-1,2,-1).
\tag{11}
\]

For the graph comparison use C468d(8)–(10). Lower-slot symmetry
writes p_c=(P-vS,P+vS,W_c)(t,m,w,q), w=v^2, with smooth
P,S,W_c all divisible by t. The pair freezes their w argument at
w0, keeping v unchanged. Divided differences in w give exactly
p_p-p_c=t rho V. At glancing, the uniform compact smooth bounds
and m,q-x=O_K(epsilon), w0=O_K(t) give

\[
V=V_0+O_K(\epsilon),\qquad
V_0=(a''(x)/2,a''(x)/2,0).
\tag{12}
\]

Indeed at t=0, P/t is minus the mean of a(m-v),a(m+v), whose
w derivative at w=0 is -a''(m)/2; W_c/t=-a(q) is independent
of w. The remaining term v(S/t)_w is O_K(epsilon). Smooth even
factorization gives bounded further derivatives on the compact box,
so these are quantitative O_K(epsilon) errors. This argument
differentiates no h-dependent inverse: the divided-difference
integral is in the two values w,w0, both tending to zero.

Set Z_j=D_Q p_j, U_j=partial_t p_j at fixed Q, M_j=Id-iZ_j,
A_j=F det M_j and u_j=-i M_j^(-1)U_j. At the seam,

Z_p-Z_c=tVn,  U_p-U_c=tV rho_t.

There X_c rho=0, so rho_t=-n.b_c. Smoothness of the chamber graph
and its velocity gives Z_c=O_K(t),
U_c=U0+O_K(epsilon), b_c=kU0+O_K(epsilon), with
U0=-a(x)(1,1,1). Since n0.(1,1,1)=0, (11) yields
rho_t=O_K(t). Consequently, with E0=V0 n0 and
sigma=tr E0=sqrt6 a''(x)/6,

\[
Z_p-Z_c=t^{3/2}E_0+O_K(t^2),\quad
U_p-U_c=O_K(t^2),\quad E_0U_0=0.
\tag{13}
\]

The matrices and their inverses are uniformly bounded and tend to
Id. The determinant and inverse identities therefore imply

\[
q_A:=A_p/A_c=1-i\sigma t^{3/2}+O_K(t^2),\qquad
u_p-u_c=O_K(t^2),\qquad u_c=-iU_0+O_K(\epsilon).
\tag{14}
\]

For the middle estimate, the first inverse variation is
i M_c^(-1)(Z_p-Z_c)M_c^(-1); its contribution to u_p-u_c has
leading term t^(3/2)E0U0=0, and all remaining terms are O_K(t^2).
The common nonzero F cancels from q_A before taking estimates.
C467z's smooth factorization A_c=Delta(Q)^2 widehat A gives
A_c/Re A_c=1-ik(x)+O_K(epsilon), with a uniformly nonzero
normalized real part. Thus no inverse vanishing Vandermonde factor
is estimated. Write q_A=1+z. From b_j=-Re(A_j u_j)/Re A_j the
exact subtraction formula is

b_p-b_c=-[Re(A_c z u_c)+Re(A_c q_A(u_p-u_c))
                 +b_c Re(A_c z)]/Re(A_c q_A).

Divide by Re A_c and use (14). Its numerator is
-(1+k^2)sigma U0 t^(3/2)+O_K(t^2), and its denominator is
1+O_K(t^(3/2)). Hence b_p-b_c=(1+k^2)sigma U0 t^(3/2)
+O_K(t^2), which is (8). This proves the rate using actual
glancing and full complex densities. It is not an extension of
C468's fixed-h asymptotic into the shrinking layer.

### Cancellation in the inverse gap and the Ct slope bound

Distinguish the seam derivative q_c at fixed t,h from an inverse
coordinate derivative. C467p(12)–(17), (9)–(10) above and
h=O_K(t^2) give, uniformly along glancing,

\[
I_c=3+O_K(t),\quad I_W:=I_h/h=O_K(t),\quad
q_c=1+O_K(\sqrt t),\quad
\mathcal A:=I_c q_W-I_W q_c\asymp_K t^{-1/2}>0,
\tag{15}
\]

where q_W=q_h/h and mathcal A=N/mathcal Q_t'(q). The last
comparison is C467p's lambda=h+sqrt(t) bound. Since W has zero
time component, applying W to the two inverse-chart equations gives

\[
hW(h)=\frac{I_c W(q)-q_c W(I)}{\mathcal A},\qquad
I_c W(c)+I_W hW(h)=W(I).
\tag{16}
\]

Equation(8) gives W(q)=mathcal B t^(3/2)+O_K(t^2) and
W(I)=3 mathcal B t^(3/2)+O_K(t^2). The leading terms cancel
in the numerator of (16), leaving O_K(t^2). Dividing by the
positive quantity comparable to t^(-1/2) proves

\[
|hW(h)|\le C_K t^{5/2},\qquad
W(c)=\mathcal B(x)t^{3/2}+O_K(t^2).
\tag{17}
\]

The factor h has not been discarded; W(h) itself need not have
this bound. This is the crucial gain over a size estimate on W.

Write Dbar(t,c,h)=D(t,c-h/3,h). Its c and h derivatives are
uniformly bounded by C467's compact smoothness. Thus (17) gives
|WD|<=C_K(t^(3/2)+t^(5/2)/h). C468c supplies both
X_cD>=d_c/(4h) and |X_c c|<=C_K at these points. It follows that

\[
|\delta|\le C_K(h t^{3/2}+t^{5/2})\le C_K t^{5/2},\qquad
Y(t)=-\delta,\quad
Y(c)=\mathcal B(x)t^{3/2}+O_K(t^2).
\tag{18}
\]

Use the positive lower bound for |mathcal B| on K and reduce time
once more. Then Y(c) is nonzero and |Y(c)|>=b0 t^(3/2) for some
b0>0. Since Y is tangent to the glancing surface, its expression
in that surface's coordinates is Y(t) partial_t+Y(c) partial_c.
The function r=Y(t)/Y(c) is smooth for t>0 and satisfies |r|<=Ct.
No estimate on a derivative of an unknown scalar has been used.

### An arbitrary candidate has this smooth glancing trace

Suppose a joint candidate exists and define

S(t,c)=T(t,x(t,c),eta(t,c)).

Fix a positive-time glancing point in the above core. C468c's strict
chamber turning supplies a small regular neighborhood with
X_c^2 rho>0 and a strictly earlier interior section. Transport the
candidate's smooth section values by the regular chamber field to
get its smooth extension psi_minus. The same section represents
the candidate trace on a neighboring portion of the glancing
surface: a nearby glancing characteristic has rho=0 and X_c rho=0
at contact, and strict convexity along the flow keeps rho>0 between
that contact and the earlier section. After shrinking the neighborhood,
all other collar margins, including d<h/4 on the open segment,
hold as in C468c. Characteristic constancy and boundary continuity
therefore give T=psi_minus on that neighboring glancing portion.

This establishes local smoothness of S for t>0; no prescribed
boundary regularity is being silently added. At each such point
C468c(3)–(4) gives X_c psi_minus=X_p psi_minus=0. Choosing the
common local section just described is permissible in that result.
Equation(6) gives d psi_minus[Y]=0. Because Y is tangent to the
glancing surface and psi_minus agrees with its trace there, this
is Y(t) partial_t S+Y(c) partial_c S=0. Division by the proved
nonzero Y(c) gives (3).

The construction of this local section is allowed to depend on the
point. No uniform section size or bound on its scalar derivatives
as h tends to zero is required. On overlapping neighborhoods the
traces coincide because both are the original candidate trace.
Thus (3) is a well-defined equation on the whole positive-time
glancing strip, even though the auxiliary extensions need not agree
away from it. C468c's jet condition already incorporates C468b's
causal pair return; no same-time return or equal velocities are used.

### Glancing characteristics force an impossible initial trace

Let L=b_* be the length of [b_*,2b_*]. For any sufficiently small
t0>0 solve the regular scalar ODE

\[
\frac{dt(c)}{dc}=r(t(c),c),\qquad t(b_*)=t_0.
\tag{19}
\]

At positive t the coefficient is smooth, so the cited local ODE
theorem applies. While its solution stays in the positive strip,
|d log t/dc|<=C by (3). Integration gives

\[
t_0 e^{-CL}\le t(c)\le t_0 e^{CL}
\qquad(b_*\le c\le2b_*).
\tag{20}
\]

Choose t0 e^(CL)<tau/2. These bounds prevent both hitting zero
and exiting the upper time boundary over the indicated finite
center interval. That interval has a margin inside the chart.
For each fixed t0 the solution thus stays in a compact subset of
the smooth ODE domain, and the cited compact continuation theorem
extends it all the way to 2b_*.

Along it the chain rule and (3) give
d S(t(c),c)/dc=0. Hence S(t0,b_*)=S(t(2b_*),2b_*).
As t0 decreases to zero, (20) makes both endpoint times tend to
zero. Equation(4) gives eta(t,c)->0 and x(t,c)->c. The original
candidate is jointly continuous at the initial/collision face and
has the prescribed product there, so

\[
\lim_{t\downarrow0}S(t,c)=f(c)^3.
\tag{21}
\]

Taking the two limits proves f(b_*)^3=f(2b_*)^3. The left side is
one and the right side zero by the bump hypotheses, a contradiction.
No time-zero scalar derivative or uniform positive-h Taylor expansion
of that scalar occurs. It is the bounded logarithmic drift of the
glancing paths, not chamber initial-characteristic access, that
connects the two limiting initial values.

### Scope of the stop

Only fixed-margin positive-time points of the original collar/pair
are used before taking continuity at time zero. Their local chamber
segments remain in the collar and the C468c pair returns lie in
the original pair. Allowed values or extensions at the outer faces
cannot change the necessary equation(3). The negative endpoint
permutation imposes no needed extra premise: failure already occurs
at the positive endpoint.

The forced pair center and separated T_c constraints of C468a remain
valid but are not needed for this contradiction. Neither stopped
fixed scalar is restored. The result changes the route decision for
the nominated jointly selected smooth-interior, continuous-boundary
class, as subsequently validated by conceptual audit1094 of this argument
and its load-bearing C468a–d inputs.
It supplies no off-line zeta zero, positivity criterion or RH claim.

### Independent conceptual audit — 16 November 2026, step1094

The unchanged invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-16-joint-glancing-trace-audit-nomination-1092.md`,
separately approved in review1093. This REPRODUCTION conceptual audit
checks the entire obstruction, including C468a–d's application claims
in their audit1094 sections. The existing proof and prior stops are
preserved. The verdict concerns the exact original collar, affine pair,
scalar regularity and qualifications in the hypotheses, not RH.

The standard inputs remain Teschl's April2012 preliminary version,
Theorems2.5/2.10–2.11, Lemma2.14/Corollary2.15, Theorems3.9/3.12
and Theorem6.1/proof, with the page locators and primary coverage in
review1093 and the citation above. Every application below is on an
open smooth positive-time chart, with compact continuation established
where needed. Classical smooth implicit-function and Taylor theorems
are used after checking their concrete nondegeneracy and derivative
bounds. No general glancing trace theorem is asserted or reproved.

**Uniformity of the scaled calculation.** Choose K=[b_*/2,3b_*],
strictly inside (0,X). C467's smooth diagnostic has D_h=-2 at time
zero. Its smooth implicit solution h_g satisfies (4), including
h_{g,x}=O_K(t^2); compactness and d(x)>0 give two-sided comparison
with t^2. After a common reduction, the glancing set has strict
original x,upper-h margins. Its change c=x+h_g/3 has positive
x derivative and its image contains a fixed open interval around
[b_*,2b_*]. Thus one may use that entire center interval on one
horizon, without allowing x to approach zero.

C467e's coefficient flow is smooth on a fixed neighborhood, including
repeated initial roots; C467z's momentum graph is smooth on a fixed
physical box including all diagonals. All finite-order derivatives
used in (8)–(14) therefore have common bounds on smaller compact
boxes. In particular, the C1 remainder in E_t=e+tS0+O(t^2)
is uniform, as are the higher derivatives needed for the divided
differences. Along h_g, e0-e_c and e0_c-e_c' are O_K(t^4).
The scaled cubic is z^3-6z plus a perturbation whose value and
first z derivative are O_K(sqrt(t)) on the three separated root
neighborhoods. The nonzero limiting derivatives supply (9) with
common constants. No smoothness in the unscaled repeated roots is
being assumed.

The first numerator for Q_c is
3(Q_j-c)^2-6t+O_K(t^(3/2)), by the exact identities for
D s and D R_j in the proof. The second numerator is
(2/3)(Q_j-c)+2h/9+O_K(t). Division by (9) gives (10) with
O_K(sqrt(t)) errors, including the middle root. The system for
n/sqrt(t) uses the rows Q_c, sqrt(t)Q_W and (-1,1,0), and
right side (0,0,2v/sqrt(t)). Its limiting matrix is invertible.
Its inverse is uniformly bounded and differs from that limit by
O_K(sqrt(t)), proving the stronger n=sqrt(t)n0+O_K(t) in (11).

For (12), write pc=t(P1-vS1,P1+vS1,W1), with smooth bounded
functions and w derivatives on a compact half-box w>=0. The
one-sided smoothness in w follows from lower-slot evenness and
Taylor's formula with sufficiently many v derivatives. The line
segment between w and w0 is in that box. The divided-difference
formula gives V0 with error O_K(sqrt(t)), because
|m-x|+|q-x|=O_K(sqrt(t)), w0=O_K(t), and the remaining
v(S1)_w term is O_K(sqrt(t)). No derivative of w0 is needed to
bound V. The exact identity p_p-p_c=t rho V is differentiated
only on rho=0, where all differentiated-V terms vanish.

**The cancellation survives quantitative errors.** Smoothness of the
chamber field gives Z_c=O_K(t), U_c=U0+O_K(sqrt(t)) and
b_c=kU0+O_K(sqrt(t)). Since n0.U0=0, glancing implies
rho_t=-n.b_c=O_K(t), with the derivative at fixed physical Q.
Consequently Delta Z=t^(3/2)E0+O_K(t^2) and Delta U=O_K(t^2).
Both inverse matrices are uniformly bounded. The determinant remainder
and inverse identity give q_A=1-i sigma t^(3/2)+O_K(t^2),
and Delta u=O_K(t^2), since E0 U0=0. The original F cancels
exactly from q_A. The normalized chamber factor has its real part
bounded away from zero, yielding A_c/Re A_c=1-ik+O_K(sqrt(t)).
In the displayed real subtraction formula, after division by Re A_c,

    Re((1-ik)(-i sigma)(-iU0)) = -sigma U0,
    (kU0) Re((1-ik)(-i sigma)) = -k^2 sigma U0.

All omitted products are O_K(t^2): the coefficient errors are
O_K(sqrt(t)) multiplying t^(3/2), or are already O_K(t^2).
The denominator is 1+O_K(t^(3/2)). Its outer minus sign proves
(8), with exactly mathcal B=-(sqrt(6)/6)(1+k^2)a a''.
C467u/audit1062 gives a<0,a''<0 on K, so continuity makes
|mathcal B| uniformly positive there. This uses the qualified
actual-background signs, not a frozen or symmetric replacement.

The inverse-coordinate denominator in (15) is N/Q_t'(q),
positive and comparable to 1/(h+sqrt(t)), hence to t^(-1/2).
Applying the time-free W to I and q gives (16) with hW(h)
as its unknown; W(h) itself is not bounded by that formula's result.
The leading terms in its first numerator are
3 mathcal B t^(3/2)-3 mathcal B t^(3/2)=0.
The errors are O_K(t^2), using q_c=1+O_K(sqrt(t)),
I_c=3+O_K(t) and (8). Thus hW(h)=O_K(t^(5/2)).
The other equation, with I_W=O_K(t), gives
W(c)=mathcal B t^(3/2)+O_K(t^2). Bounded derivatives of
Dbar(t,c,h) then give
|WD|<=C_K(t^(3/2)+t^(5/2)/h). C468c supplies
X_cD>=d_c/(4h) and |X_c c|<=C_K. Hence
|delta|<=C_K(ht^(3/2)+t^(5/2))=O_K(t^(5/2)).
Equations (18) and the nonzero lower bound for |mathcal B|
prove |Y(c)|>=b0 t^(3/2) and |Y(t)/Y(c)|<=Ct.
Every estimate is uniform over the chosen compact center strip.

**Why the trace equation applies to an arbitrary candidate.** At a
fixed positive-time glancing point the defining differentials of
rho and D are independent: rho_v=2v>0, while D is independent
of v and D_h in the seam chart is nonzero. C468a's exact normal
identity makes X_c,X_p tangent to the seam there, and subtracting
(WD/X_cD)X_c makes Y tangent to D=0 as well. These are
spacetime tangencies, with Y(t)=-delta.

C468c's audit1094 proves that the two genuine interior sections
have a common first jet and that X_p psi_minus=X_c psi_minus=0
at contact. For a whole neighborhood of glancing contacts, the same
past section represents the trace: strict chamber convexity keeps
the intervening segment on rho>0, and the recovered initial-coordinate
chart keeps d<h/4 and the other collar margins. Characteristic
constancy and the candidate's boundary continuity identify these
values with its original T. Thus S is locally smooth on the
glancing surface at positive time, even though no boundary derivatives
were assumed. Applying the common jet to tangent Y gives (3).
The local section sizes and scalar derivative bounds may deteriorate
as t tends to zero; neither is used in the uniform slope estimate.
Overlaps agree because they restrict the same candidate trace.

**The limiting contradiction.** The coefficient r is smooth on an
open strip containing the compact center interval at every positive
time. For fixed t0>0 the ODE (19) is a regular initial-value problem.
The estimate |r|<=Ct implies |d log t/dc|<=C and hence (20)
while the solution exists. Taking t0 exp(Cb_*)<tau/2 keeps it
in a compact subset of this open positive-time strip, with a fixed
center margin. Teschl's compact continuation therefore reaches 2b_*.
The chain rule applied to the already smooth S makes its two endpoint
values equal. Both times tend to zero as t0 does; also eta tends
to zero and x tends to c. Joint continuity on the original closed
domains, not a derivative or uniform Taylor expansion of the scalar,
then gives the two limits f(b_*)^3 and f(2b_*)^3. They are exactly
1 and 0. Arbitrary asymmetric or oscillatory allowed bumps obey
these endpoint values, so the contradiction is independent of their
transition shape or any outer-face assignment.

**Verdict and qualifications.** The claimed exclusion of this entire
nominated collar/affine-pair class passes the independent conceptual
audit. In particular the required threshold |dt/dc|<=Ct is proved,
not merely a weaker O(sqrt(t)) estimate. The inspected earlier results
supply all direct mathematical inputs already listed in the DAG; no
new edge, theorem, effective time or numerical certificate is needed.
The external low-zero verification and paired-product qualifications
remain exactly those in the hypotheses and C467u. Full matching
Mathlib coverage remains unchecked. This validates local negative
information for signed assembly; it establishes no actual-Xi sign,
global current, off-line zero, or RH proof/disproof.

## Mathlib

Full matching coverage of this glancing-trace obstruction is unchecked.
Smooth ODE dependence and continuation, implicit-function and Taylor
tools, and matrix differentiation are supporting results, not a
formalization of the coupled problem or (3). No absence or certified
novelty claim is made.
