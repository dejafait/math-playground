# C468c — Chamber glancing and a necessary first-jet transmission condition

## Hypotheses

Retain C468a/b's exact joint chamber/lower-pair problem and C467p's
inverse physical chart, with C467z/C467's chamber field and diagnostic.
In particular n=3, R=1/4, a0=1/16, T0=1/1920, X=1/256,
b_*=1/4096 and H_*=1/128. The chamber collar is
u=(x-d,x+d,x+h), |x|<=X, 0<=h<=H_*, 0<=d<=h/4;
the pair is the original |x|<=X, |s|<=1, 0<=h<=H_* box.
Keep the original endpoint permutation, actual B, beta, H, H0, F,
raw time, original divisor, algebraic-square form and common minus sign.
Here beta(z)=B(1+z)-B(1)-B'(1)z, H=H0+sum_j beta(z_j),
F=Delta^2 exp(-H), and B is the conjugation-normalized logarithm of
xi(1/2+sqrt(w))/xi(1/2), with |beta''|<40 on |z|<R.
The inherited L018/L021/L024/C466a finite-zero/product qualifications
and C467u's unreplayed low-zero verification remain. This argument
does not strengthen them or require the strict sign of d(x).

A joint candidate consists of real [0,1]-valued Theta and phi,
continuous on their original closed domains, smooth on their regular
positive-time interiors, satisfying the original undivided adjoint
equations and the initial products product_j f(u_j), f(x)^2 f(x+h).
The fixed smooth bump f is one on [-b_*,b_*], supported in
(-2b_*,2b_*), and need not be even. Its matched seam trace is
T(t,x,h)=Theta(t,x,x,x+h)=phi(t,x,1,h), with the prescribed
lower-slot permutation at s=-1. No boundary derivative is assumed.

In physical coordinates Q=(m-v,m+v,q), I=2m+q, c=x+h/3, let

\[
\rho(t,Q)=v^2-w_0(t,I,q),\qquad
w_0=\alpha(t,x,h)^2/4,\qquad D=\mathfrak D(t,x,h),
\]
\[
X_j=\partial_t+b_j\cdot D_Q\quad(j=c,p),\qquad
K_c=2\det D_t/N>0,\quad K_p=(\mu_c/\mu_p)K_c>0.
\tag{1}
\]

Use the positive-h inverse chart to extend D off the seam as a
function of (t,I,q), independent of v. C468a supplies, on rho=0,
X_c rho=K_c D and X_p rho=K_p D. Locally the original chamber is
rho>=0 and the original pair is rho<=0. The fields and these
functions are smooth near each fixed positive-t,h endpoint; the
normalized equations are used only at nonzero physical gaps.
C468a/b are checked with this result in conceptual audit1094.

## Conclusion

After one common positive time reduction there is d_c>0 such that
at every glancing point g with t,h>0 and strict x,h outer margins,

\[
D(g)=0\quad\Longrightarrow\quad
X_cD(g)\ge d_c/(4h)>0,\qquad
X_c^2\rho(g)=K_c(g)X_cD(g)>0.
\tag{2}
\]

Thus its chamber characteristic lies strictly inside the original
collar at both sufficiently close earlier and later times. These
neighborhoods and time lengths may depend on g; no h=0 bound follows.

For any joint candidate, fix such a g strictly inside its time interval
and in the core of C468b's return theorem. Transport its smooth values from a sufficiently
close earlier interior chamber section by the regular chamber field,
allowing that auxiliary transport off the original chamber. This
defines a smooth local function psi_minus near g. Define psi_plus
likewise from a later interior section. Then

\[
d\psi_{\rm minus}(g)=d\psi_{\rm plus}(g),\qquad
\psi_{\rm minus}(g)=\psi_{\rm plus}(g)=T(g),
\tag{3}
\]
\[
X_p\psi_{\rm minus}(g)=0,
\qquad
(b_p-b_c)(g)\cdot D_Q\psi_{\rm minus}(g)=0.
\tag{4}
\]

The differential in (3) is the full spacetime differential. Nearby
outgoing seam data D<0 equal psi_minus, while incoming data D>0
equal psi_plus. These statements extract a necessary first jet from
interior smoothness; they do not assume smoothness at the collision
face or at time zero. In particular a prescribed smooth past-section
datum with a nonzero left side of (4) cannot be transmitted in the
nominated class, even if its pair return values are continuous.

No nonzero value of (4) is established for the actual candidate data.
The earlier section need not be connected to time zero within the
original collar, so psi_minus is not automatically C467z's T_c or
its physical extension. Equality of b_p and b_c is not assumed or
proved. This is a necessary local compatibility test, not a stopped
joint class, a sufficient condition, or a constructed selection.
Higher compatibility, repeated hits, outer faces, the common h=0
extension, integrability, cyclic matching and Xi transfer remain open.
Attempt1090 and its C468a/b inputs are checked in audit1094 below.

## Proof

### Coverage and standard tools

Use the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-16-boundary-fed-chamber-pair-nomination-1086.md`,
approved separately at review1087. The target includes smooth chamber
transmission through the collapsing original-pair return. C468b proves
continuity of that return, not (2) or the first-jet condition. The
fixed selections stopped in1043/1058/1060/1068/1084 and the uniform
initial-access stop1081 retain their scopes. In particular stop1043
assumes a stronger joint time-zero regularity than used here.

Import the assessed regular flow tools of Gerald Teschl, *Ordinary
Differential Equations and Dynamical Systems*, April2012 preliminary
version, [Theorems2.5/2.10 pp40–47, Lemma2.14/Corollary2.15 pp52–53,
Theorems3.9/3.12 pp81–84 and Theorem6.1/proof pp189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf),
and the classical smooth implicit function theorem and Taylor theorem.
All new flow uses below have smooth fields on a fixed positive-t,h
neighborhood. The application work is the actual chamber turning and
the compatibility of its two smooth extensions with the pair return;
no singular-boundary transport theorem is imported or reproved.

### The same inverse chart gives strict chamber turning

For any bounded physical velocity B in the common chart write B_I,
B_q for its fixed linear coordinate components. Differentiating
I(t,c,h), q(t,c,h) along that velocity gives exactly

\[
h\dot h=
\frac{I_c(B_q-q_t)-q_c(B_I-I_t)}{I_cq_W-I_Wq_c},
\qquad q_W=q_h/h,\quad I_W=I_h/h.
\tag{5}
\]

Here I_t,q_t on the right hold initial c,h fixed. C467p(9)–(17)
gives, with lambda=h+sqrt(t),

I_c>=2, |q_c|+|I_t|<=C, q_t>=c1/lambda-C,
and 0<c2/lambda<=I_c q_W-I_W q_c=N/Q'(q)<=C2/lambda.
It also bounds c_t,c_I,c_q and h h_t,h h_I,h h_q in the inverse
chart. Hence |dot c|<=C_B and |h dot h|<=C_B. In (5) the
numerator is at most -2c1/lambda+C_B. For sufficiently small fixed
delta and then sufficiently small time, h<=delta implies
lambda<=2delta and that numerator is at most -c1/lambda.
Division by the positive denominator, using its upper bound, gives

\[
\dot h\le-d_B/(2h),\qquad |\dot c|\le C_B
\quad(0<h\le\delta)
\tag{6}
\]

for some d_B>0. C467z's chamber field has a uniform bound on the
physical box containing these seam points. Apply (5)–(6) to B=b_c;
this does not identify it with the pair field. All constants may
be increased before choosing the common time.

C467's compact smooth diagnostic and D(0,x,h)=-2h give, as in
C468b(6)–(7), D_h-D_x/3<=-1, |D_t|+|D_x|<=C_D and
0<h<=A t^2 at every positive-h glancing point. Since x=c-h/3,

\[
X_cD=D_t+D_x\dot c+(D_h-D_x/3)\dot h
       \ge-C_0+d_c/(2h).
\tag{7}
\]

Reduce time until every glancing h<=A t^2 is both in (6)'s
collar and at most d_c/[4(C_0+1)]. This proves the first part
of (2). At glancing X_c is tangent to rho=0. Differentiate
the seam identity X_c rho=K_c D only in this tangent direction.
It gives X_c^2 rho=K_c X_cD there, proving the second part.
This differentiation does not extend the seam identity off the seam.

Taylor expansion along the chamber trajectory through g now gives
rho(r,Q_c(r))=a_c(r-t_g)^2/2+o((r-t_g)^2), where
a_c=X_c^2 rho(g)>0. In a sufficiently small neighborhood the
strict outer margins and the positive initial singleton separation
persist. The chamber side rho>0 corresponds to k=4d^2>0 by
C468a(9); shrink until also d<h/4. Thus both nearby noncontact
segments are in the regular original collar, not merely the
three-real-root region of an enlarged chamber.

### Smooth extensions from two actual interior sections

Fix g. Choose times r_minus<t_g<r_plus, all strictly positive,
so the two points on its chamber characteristic are in the regular
collar. Choose a small smooth flow neighborhood containing that
segment. It has h>0, nonzero physical gaps, and X_c^2 rho>0.
After shrinking, every trajectory in this neighborhood between
the two sections stays in the chart and within all other collar
margins. Neighborhoods of its points on the two sections lie wholly
in the regular chamber. The candidate values there are smooth in
physical coordinates: the original interior coefficient/root map
is a local smooth diffeomorphism at distinct initial coordinates.

Transport each section's values using the smooth extended chamber
field. This defines smooth psi_minus and psi_plus on a common
neighborhood of g, each solving X_c psi=0. They are auxiliary
extensions; crossing rho<0 in this definition does not assert that
the candidate is defined there.

There is an open set of chamber trajectories staying strictly on
rho>0 for the whole segment, whose closure contains the trajectory
through g. To check this precisely, parameterize nearby trajectories
by Q at time t_g. Their function of r given by rho(r,Q_c(r))
has a unique local critical point near t_g, smoothly depending on Q,
by X_c^2 rho>0 and the implicit function theorem. Its minimum m(Q)
has derivative D_Q rho(g) at Q_g, since its r derivative vanishes.
That covector is nonzero: in (I,q,v) coordinates rho_v=2v and
v=alpha/2>0 at this endpoint. Thus m>0 is a nonempty open side
accumulating at Q_g. Shrink the flow neighborhood so strict convexity
and the positive section values make this also the minimum on the
whole segment. These m>0 trajectories remain in the original collar.

The candidate is constant along each such trajectory by its exact
interior chamber equation. Consequently psi_minus=psi_plus on
the resulting open spacetime set accumulating at g. Their smooth
extensions therefore have the same value and all derivatives at g;
in particular their first differentials agree. Continuity of the
candidate along the central trajectory from either section identifies
their common value with T(g). This proves (3).

For a seam point z close to g with D(z)<0, the chamber derivative
of rho is negative. Along its backward chamber path this derivative
is still negative, by X_c^2 rho>0, until the earlier section.
Thus rho>0 all the way back and the path lies in the collar.
Characteristic constancy and boundary continuity give
T(z)=psi_minus(z). For D(z)>0 the identical forward argument to
the later section gives T(z)=psi_plus(z). These claims use a
small local neighborhood of g, not uniform initial access.

### First-order expansion of the causal pair return

Fix a core with strict outer margins and work on the common horizon
of C468b's positive-h return theorem and (2). Here g is any glancing
point in that core and horizon. Set a_p=X_p^2 rho(g)>0. Since X_p(g) is
tangent to the smooth seam, choose a smooth seam curve z_epsilon
with z_0=g and z'_0=X_p(g). The curve parameter epsilon here is
local and unrelated to the fixed outer margin. Then

\[
D(z_\epsilon)=\epsilon X_pD(g)+o(\epsilon)>0
\quad(\epsilon>0\text{ small}),\qquad
X_p\rho(z_\epsilon)=a_p\epsilon+o(\epsilon).
\tag{8}
\]

C468b supplies its first earlier pair hit R(z_epsilon), with
D(R)<0, and proves R(z_epsilon)->g. Write delta_epsilon for
the strictly positive elapsed time from R to z_epsilon. It tends
to zero. Taylor's theorem along the actual intervening pair path,
in this fixed smooth neighborhood, gives

\[
0=\rho(R)=
-\delta_\epsilon X_p\rho(z_\epsilon)
+\tfrac12\delta_\epsilon^2(a_p+o(1)).
\tag{9}
\]

The remainder is uniform as both the endpoint and the segment tend
to g; it follows directly from continuity of X_p^2 rho there.
Divide by the positive delta_epsilon and use (8), obtaining

\[
\delta_\epsilon=2\epsilon+o(\epsilon),\qquad
R(z_\epsilon)=g-\epsilon X_p(g)+o(\epsilon)
\tag{10}
\]

in spacetime coordinates. The latter uses smooth local flow
dependence and z_epsilon=g+epsilon X_p(g)+o(epsilon). No same-time
return, uniform h=0 remainder or equality of the two fields enters.

Both hits lie in the previously established outgoing/incoming trace
neighborhood. Joint matching and pair characteristic constancy give

\[
\psi_{\rm plus}(z_\epsilon)
=T(z_\epsilon)=T(R(z_\epsilon))
=\psi_{\rm minus}(R(z_\epsilon)).
\tag{11}
\]

Expand the two smooth functions at g using (3) and (10). The left
side is T(g)+epsilon d psi_minus(g)[X_p(g)]+o(epsilon);
the right is T(g)-epsilon d psi_minus(g)[X_p(g)]+o(epsilon).
Equation (11), division by epsilon and the limit give
X_p psi_minus(g)=0. Since X_c psi_minus=0 already, subtraction
proves (4). The negative endpoint follows after the original
permutation, without an extra independently prescribed trace.

### What the test leaves unpaid

The construction of psi_minus starts at an actual local chamber
section, where its values are those of a hypothetical candidate.
It does not prescribe them freely, nor force them from initial data.
Therefore (4) is an additional check on a proposed boundary-fed
selection, not a demonstrated conflict. Its sufficiency and its
actual value for globally compatible past data are unresolved.
All arguments after (2) fix a positive-t,h glancing point. They
give no uniform section size, derivative estimate or continuation
as h tends to zero. The pair-return continuity of C468b alone
cannot replace this first-jet test for the requested smooth chamber
interior. No failure of an estimate is recorded as a route stop.

### Independent conceptual audit — 16 November 2026, step1094

The invocation-start SPECIALIZE nomination1092/review1093 includes
this necessary first-jet argument. This is a REPRODUCTION audit of
its actual-domain application, using the cited regular ODE/implicit-
function/Taylor tools. C468a/b's audit1094 validates their incidence,
strict pair turning and causal-return inputs; C467p/z retain their
previously audited qualifications.

**Chamber turning and containment.** For an arbitrary bounded physical
velocity B, C467p's inverse-chart equations give (5), including the
fixed-initial q_t and I_t on its right. I_c>=2, bounded q_c,I_t,B,
q_t>=c1/lambda-C and the positive denominator <=C2/lambda imply
h dot h<=-c1/C2 once h and sqrt(t) are sufficiently small.
The inverse bounds also give |dot c|<=C_B. They apply to the
uniformly bounded chamber field b_c on its fixed physical box; no
pair/chamber velocity identity is used. The diagnostic chain rule
then proves (7) and X_cD>=d_c/(4h) at glancing. Tangential
differentiation of C468a's seam identity gives the claimed positive
X_c^2 rho. At a fixed g, its h is positive, v=alpha/2>0 and all
x,h,time margins are strict. The recovered (c,h,k) chart is smooth
by C468a's nonzero determinants. A sufficiently small neighborhood
therefore has k<h^2/4, with ordered singleton and strict outer margins.
Within it rho>0 implies k>0 and hence 0<d<h/4. The two Taylor
segments are genuinely in the original collar.

**Why two smooth extensions have the same jet.** Choose the two
interior sections first, sufficiently close to this fixed g, then a
flow tube where X_c^2 rho remains positive and all other collar
margins hold. The scalar is smooth on the two sections because the
initial-to-physical map is a local diffeomorphism at their distinct
initial roots. Smooth section transport defines psi_minus,psi_plus
on a common open spacetime neighborhood, without extending the
candidate itself to rho<0.

Parameterize paths by Q at time t_g. The implicit-function theorem
at the unique local critical time of rho gives a smooth minimum
m(Q). At Q_g, its differential is D_Q rho(g): the derivative of
the critical time is multiplied by the zero time derivative of rho.
This covector is nonzero since rho_v=2v>0 at fixed I,q. Hence there
is a nonempty open side m>0 approaching Q_g. Strict convexity and
the positive section values ensure that these whole segments remain
in rho>0, within the original collar. On the open spacetime set swept
out by them the candidate equation forces psi_minus=psi_plus. Their
smooth difference and every derivative vanish on this open set;
continuity of each derivative at g gives equality of the full
spacetime jets at g. An open neighborhood of g on which the two
extensions agree is neither claimed nor required. Continuity along
the two central segments identifies the common value as T(g).

For nearby seam points with D<0, strict convexity keeps the backward
segment to the earlier section in rho>0; for D>0 it keeps the
forward segment to the later section there. This verifies the two
trace representations actually used in (11). At any neighboring
glancing point, the same local earlier section also represents its
trace: its convex path has a zero minimum at contact and is strictly
inside before it. Thus this construction supports C468e's later
smooth trace restriction, with a section size allowed to depend on g.

**Causal first-order comparison.** On the seam at g, X_p is tangent
and has time component one. A smooth seam curve with derivative
X_p(g) therefore exists. Its diagnostic derivative is X_pD(g)>0
and its normal-speed derivative is X_p^2 rho(g)=a_p>0, by tangent
differentiation. This gives (8). C468b's return theorem gives a
strictly positive elapsed time delta_epsilon tending to zero and
D<0 at the earlier hit. The intervening paths tend to g by bounded
smooth local flow. Integrating the second derivative of rho on
those paths gives (9) with remainder o(delta_epsilon^2), uniformly
as epsilon tends to zero. Dividing by the nonzero delta_epsilon
yields delta_epsilon=2epsilon+o(epsilon), and the smooth flow gives
R(z_epsilon)=g-epsilon X_p(g)+o(epsilon) in spacetime.

Equation (11) uses exactly the candidate values on the two original
domains, not freely prescribed data. Substituting the common first
differential gives 2epsilon d psi_minus(g)[X_p(g)]+o(epsilon)=0.
Consequently X_p psi_minus(g)=0. Together with X_c psi_minus=0,
this proves (4). The arguments do not differentiate an unknown scalar
at the seam or at time zero. They extract a positive-time jet from
interior smoothness and a causal return, not from continuity alone.

The necessary first-jet conclusion passes with its original scope.
It neither makes the past-section datum equal to the auxiliary
initial transport nor provides sufficient matching conditions.

## Mathlib

Full matching coverage of this moving chamber/pair first-jet condition
is unchecked. Smooth ODE flow, the implicit function theorem, the
chain rule and Taylor's theorem are supporting tools, not a
formalization of the actual transmission problem. No absence or
certified novelty claim is made; this is not an RH resolution.
