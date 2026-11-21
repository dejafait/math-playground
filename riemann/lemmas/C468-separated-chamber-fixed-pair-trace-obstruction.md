# C468 — The fixed lower-pair trace disagrees with separated chamber outflow

## Hypotheses

Retain C467e/audit1017's analytic coefficient flow, C467z/audit1083's
physical chamber graph and separated necessary trace, C467p/audit1049's
particular lower-pair test, and C467y's unchanged selection of that test.
Use C467u/audit1062's qualified actual-background signs. In particular,

\[
n=3,\ R=1/4,\ a_0=1/16,\ T_0=1/1920,\quad
X=1/256,\ b_*=1/4096,\ H_*=1/128,
\]
\[
\beta(z)=B(1+z)-B(1)-B'(1)z,\quad g=\beta',\quad
H=H_0+\sum_j\beta(z_j),\quad F=\Delta^2e^{-H},\quad
\Omega=F\bigwedge_j(dz_j/i).
\tag{1}
\]

B is the actual conjugation-normalized logarithm specified in those
inputs, H0 is real, beta(0)=beta'(0)=0 and |beta''|<40 on |z|<R.
Keep their L018/L021/L024/C466a finite-zero/product qualifications.
C467u's signs retain the cited finite verification through positive
ordinate100 and first-zero isolation in (14,15), from Suvrit Sra,
*On some positivity properties of the Riemann Xi function*,
[W_pr5z5huy_v1, section2.1, (6)–(8)](https://hub.valency.io/works/W_pr5z5huy_v1).
That external verification is not independently replayed here; no
assertion that the higher zeros lie on the line is assumed.

Let f be any fixed smooth real function in [0,1], equal to one on
[-b_*,b_*], with support in (-2b_*,2b_*). No evenness or monotonicity
is assumed. Put \(\mathcal G(Q)=\prod_j f(Q_j)\), and retain the actual
raw time, divisor, algebraic-square weight and common minus sign.
A candidate Theta has precisely C467z(2)'s continuity, interior
smoothness, initial product and undivided real-adjoint equation.
The proposed first-face match is

\[
\Theta(t,x,x,x+h)=\phi_p(t,x,1,h),
\qquad |x|\le X,\quad 0<h\le H_*,
\tag{2}
\]

on one positive time horizon. No time-zero derivative of Theta is
assumed. C467s is not an input. Distinctly from the fixed radius a0, put

\[
a(x)=\operatorname{Re}g(ix),\qquad j(x)=\operatorname{Im}g(ix).
\tag{3}
\]

## Conclusion

For fixed -X<x<X and 0<h<=H_* with x+h<X, there is a real
coefficient \(L_f(x,h)\) such that

\[
\phi_p(t,x,1,h)-T_c(t,x,h)
 =t^3 L_f(x,h)+O_{x,h,f}(t^{7/2})\quad(t\downarrow0).
\tag{4}
\]

The error is asserted with h fixed, not uniformly at the corner.
For every fixed such x,

\[
\lim_{h\downarrow0}hL_f(x,h)
 =-2\{1+\tan^2(3\operatorname{Im}\beta(ix))\}
       a(x)a''(x)f(x)^2 f'(x).
\tag{5}
\]

Every allowed f has an x0 in (b_*,2b_*) with 0<f(x0)<1 and f'(x0)<0.
C467u gives a(x0)<0 and a''(x0)<0, so (5) is strictly positive.
Choose one sufficiently small fixed h>0. Then (4) is strictly positive
at x0 for all sufficiently small positive times. C467z forces
Theta=T_c there, so (2) is impossible on every positive common horizon.

This stops C467y's fixed lower selection in the nominated continuous
chamber class, even before any h=0 matching requirement. It does not
exclude a different coupled selection of pair and chamber data, and
does not use initial-data forcing in C467's incoming corner layer.
Independent conceptual audit1086 below validates this result of
attempt1084 under its unchanged input qualifications.
Global assembly, exterior payment, realization, all degrees and Xi
transfer remain open; it is not an RH candidate or certified novelty.

## Proof

### Scope and ordinary tools

Use the invocation-start EXPLORE assessment nomination1078/review1079,
whose exact target includes comparison with this fixed endpoint.
Its source and duplicate comparison is reused. The new calculation is
the difference of the two specified transports, not a reproof of the
general characteristic theorem. Smooth ODE dependence and the
inhomogeneous variational equation use Gerald Teschl, *Ordinary
Differential Equations and Dynamical Systems*, April2012 preliminary
version, [Theorems2.5/2.10, Lemma2.14/Corollary2.15,
Theorems3.9/3.12 and Theorem6.1/proof,
pp40–53,81–84,189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
All applications below are on a fixed separated, regular open chart.
No singular-boundary extension theorem is used.

### The graphs and their exact interpolation difference

Fix y-x=h>0. Use physical coordinates

\[
Q=(m-v,m+v,y),\qquad w=v^2.
\tag{6}
\]

C467z supplies the smooth chamber graph \(p_c(t,Q)+iQ\), with
\(p_c(0,Q)=0\) and

\[
\partial_t p_c(0,Q)=U(Q),\qquad U_j(Q)=-a(Q_j).
\tag{7}
\]

C467e's analytic coefficient construction and its local inverse make
this graph real analytic locally; alternatively its smooth even/odd
factorizations below suffice. Fix a small neighborhood of (x,0,x+h)
in (m,v,y), with y-m>h/2. All chart constants may depend on h.

The lower collision image is \(w=w_0(t,m,y)\), where

\[
w_0(0,m,y)=0,\quad w_0(t,m,y)=2t+O_h(t^2),\quad
D_{(m,y)}w_0=O_h(t^2).
\tag{8}
\]

Indeed C467p's map from initial (c,h) to physical (I,q3) has
nonzero Jacobian at t=0 for positive h; I=2m+y and q3=y.
Its smooth inverse supplies w0. At a separated initial double root,
C467z(13) and its time-zero coefficient calculation give derivative8
for the squared full lower gap, hence derivative2 for its squared
half-gap. Changing to fixed (m,y) does not change that derivative
because w0(0,m,y) is identically zero. Smoothness gives (8), also
with differentiated remainders on the fixed chart.

Lower-slot symmetry gives analytic functions P,S,W of (t,m,w,y) with

\[
p_{c,1}=P(t,m,w,y)-vS(t,m,w,y),\quad
p_{c,2}=P(t,m,w,y)+vS(t,m,w,y),\quad
p_{c,3}=W(t,m,w,y).
\tag{9}
\]

Each function has a smooth factor t. C467p(19) linearly interpolates
the same two chamber endpoint momenta and leaves the singleton
unchanged. Thus its auxiliary graph \(p_p\) is exactly (9) with w in
P,S,W replaced by w0, but v unchanged. This identifies the graphs on
an open separated inverse chart, not just at one endpoint.
The integral formula for a divided difference gives

\[
\delta p:=p_p-p_c=t(w-w_0(t,m,y))V(t,Q),
\tag{10}
\]

with V smooth through v=0, lower-slot equivariant, and with bounded
derivatives on this fixed chart. Equation (7) yields

\[
V_0(Q):=V(0,Q)=
\left(
\frac{a(m-v)-a(m)+a'(m)v}{v^2},
\frac{a(m+v)-a(m)-a'(m)v}{v^2},
0\right).
\tag{11}
\]

Use the Taylor/integral values at v=0. If \(b=a''(x)/2\) and
\(Q_0=(x,x,x+h)\), then

\[
V_0(Q_0)=(b,b,0),\qquad
V_{0,2}-V_{0,1}=\tfrac13a'''(m)v+O(v^3).
\tag{12}
\]

This retains the actual beta and the actual coefficient flow.

### Exact velocity and its first graph variation

For a small real lower-slot-equivariant graph p and variation Z, set

\[
M_p=I-iD_Qp,\qquad
\mathscr B_p(Z)=
 -\frac{\operatorname{Re}\{F(p+iQ)\det M_p(-iM_p^{-1}Z)\}}
             {\operatorname{Re}\{F(p+iQ)\det M_p\}}.
\tag{13}
\]

It is linear in Z and is the exact original real-adjoint velocity
for v!=0. Cancel the explicit v^2 in numerator and denominator
to extend smoothly to v=0. In fact p2-p1 is divisible by v, the
other two gaps stay separated, and the phase at p=0 has a strict
nonzero real-part margin, as in C467p(22)–(25)/C467z(8)–(10).
The margin persists for the small interpolated graphs used below.
This constructs a velocity; it does not alter the original current
or assert an equation on its divisor.

Put

\[
k(Q)=\tan\left(\sum_j\operatorname{Im}\beta(iQ_j)\right),\quad
c(Q)=1+k(Q)^2,\quad
d_j(Q)=2\sum_{\ell\ne j}\frac1{Q_j-Q_\ell}+j(Q_j).
\tag{14}
\]

For lower-equivariant Z the lower-pair term of d dot Z is
(Z2-Z1)/v, which extends smoothly. Singleton denominators stay
bounded on the fixed chart. At the zero graph,

\[
\mathscr B_0(Z)=kZ,\qquad
D_p\mathscr B_0(P;Z)
 =-D_QP\,Z+c(\operatorname{div}P+d\cdot P)Z.
\tag{15}
\]

To check signs and phase, directly differentiate the actual F:

\[
D_p\log F(iQ)[P]
 =\sum_j[-a(Q_j)-i\,d_j(Q)]P_j.
\]

Also det(I-iDP)=1-i div P+O(P^2), and
\(-i(I-iDP)^{-1}Z=-iZ+DP\,Z+O(P^2Z)\).
The phase of F(iQ) is an integer multiple of pi minus sum Im beta(iQj),
whose tangent is -k. Substitution gives (15). First compute away
from v=0, then use the removable lower gap. No modulus square replaces F.

Define the oriented transport curvature

\[
\begin{split}
\mathcal R_p(U,V)={}&D_p\mathscr B_p(U;V)
                   -D_p\mathscr B_p(V;U)\\
 &+D_Q(\mathscr B_p(V))\,\mathscr B_p(U)
   -D_Q(\mathscr B_p(U))\,\mathscr B_p(V).
\end{split}
\tag{16}
\]

Spatial derivatives include the Q dependence of U,V. With
\(\mathcal R=\mathcal R_0\), (15) gives exactly

\[
\begin{split}
\mathcal R(U,V)={}&c\{DV\,U-DU\,V+
   (\operatorname{div}U+d\cdot U)V
  -(\operatorname{div}V+d\cdot V)U\}\\
 &+k\{(\nabla k\cdot U)V-(\nabla k\cdot V)U\}.
\end{split}
\tag{17}
\]

For any scalar s it follows that

\[
\mathcal R(U,sV)=s\mathcal R(U,V)
       +c\{(\nabla s\cdot U)V-(\nabla s\cdot V)U\}.
\tag{18}
\]

### Endpoint variation and the controlled remainder

Let T be terminal time and \(q_T=q^+(T,x,h)\).
Interpolate \(p_\lambda=p_c+\lambda\delta p\), 0<=lambda<=1.
Let \(Q_\lambda(r)\), 0<=r<=T, solve backward from qT with velocity
\(\mathscr B_{p_\lambda}(\partial_rp_\lambda)\).
For fixed h these fields are smooth on the open separated chart,
including v=0, with bounded derivatives for small time. The ordinary
ODE theorem and the strict chart margin give all these paths.
At lambda=0,1 these are precisely the endpoint transports defining
T_c and phi_p. At lambda=1 use C467p's inverse chart and uniqueness;
its auxiliary domain has a strict margin here.

Uniformly in lambda and r,

\[
m_\lambda(r)=x+O_h(T),\quad y_\lambda(r)=x+h+O_h(T),\quad
v_\lambda(r)^2=2T+O_h(T^2).
\tag{19}
\]

The bounded velocities give the first two estimates. Their lower
difference is v times a bounded smooth function, so v'=O_h(v) and
v(r)=v(T)exp(O_h(T)). At the terminal point (8) gives
v(T)^2=2T+O_h(T^2), proving the last estimate.

The exact endpoint-variation identity is

\[
\partial_\lambda Q_\lambda(0)
 =\int_0^T\mathcal U_\lambda(0,r)\,
       \mathcal R_{p_\lambda}(\partial_rp_\lambda,\delta p)
                    (r,Q_\lambda(r))\,dr,
\tag{20}
\]

where \(\mathcal U_\lambda(0,r)=I+O_h(T)\) is the variational
propagator. To verify both boundary terms and the orientation, set

\[
Z=\partial_\lambda Q_\lambda-
       \mathscr B_{p_\lambda}(\delta p)(r,Q_\lambda).
\]

Differentiating the ODE and using (16) gives
\(Z'=D_Qb_\lambda Z-\mathcal R_{p_\lambda}(\partial_rp_\lambda,\delta p)\).
At r=T the terminal point is fixed and delta p(T,qT)=0 by (10);
at r=0, delta p(0,Q)=0 identically. Thus Z(T)=0 and
Z(0)=partial_lambda Qlambda(0). Variation of constants gives (20).
These boundary conditions cancel the apparent second-order displacement.

Here are the remainder bounds needed in (20). All derivatives are in
physical Q coordinates and all constants below are for fixed h.
Along (19), smoothness and (7)–(12) give

\[
\begin{array}{ll}
p_\lambda=O(T)\text{ in fixed finite-order chart norms},&
\partial_rp_\lambda-U=O(T),\
D_Q(\partial_rp_\lambda-U)=O(T^{1/2}),\\
\delta p=O(T^2),&D_Q\delta p=O(T^{3/2}).
\end{array}
\tag{21}
\]

The lower secants of the last two vector fields are respectively
O(T) and O(T^2). These bounds follow from r(w-w0),
D_Qw=(-v,v,0), V2-V1=O(v), and (8).
After removal of v^2, (16) depends smoothly on the graph and is
bilinear in variation values and first spatial derivatives, including
their regular lower secants. There is no product of the first
derivatives of both variations: differentiating (13) in a graph
direction differentiates p and Dp, and the spatial term differentiates
the other variation only once. Its second graph derivatives, where
present in the spatial term, multiply variation values. Thus (21) gives

\[
\mathcal R_{p_\lambda}(\partial_rp_\lambda,\delta p)
 =\mathcal R(U,\delta p)+O_h(T^{5/2}).
\tag{22}
\]

For clarity, changing the graph from p_lambda to0 supplies an O(T)
coefficient multiplying a variation value and a first derivative
(or two values). The largest such product is O(T^{3/2}).
Replacing partial_r p_lambda by U supplies O(T) in value and
O(T^{1/2}) in first derivative, paired respectively with
O(T^{3/2}) and O(T^2) for delta p. Each error is O(T^{5/2}).
The removed lower secants satisfy the stronger bounds just given.

In (18) now use s=r(w-w0) and V=V(r,Q)=V0(Q)+O_h(r). Then

\[
s=2r(T-r)+O_h(T^3),\qquad
\nabla s=r\nabla w+O_h(T^3),
\]
\[
\nabla w\cdot U=-2a'(m)w+O(w^2),\qquad
\nabla w\cdot V_0=\tfrac13a'''(m)w+O(w^2).
\tag{23}
\]

All other factors of (17),(18) are smooth through v=0 with h fixed;
replacing Qlambda by Q0 changes them by O_h(T^{1/2}).
The O(r) error in V and its first derivative contributes at most
O_h(T^{5/2}) in (18). Hence the integrand's leading expression is

\[
2r(T-r)\mathcal R(U,V_0)(Q_0)
+2crT\{-2a'(x)V_0-\tfrac13a'''(x)U\}(Q_0)
+O_h(T^{5/2}).
\tag{24}
\]

Integrate r and then lambda. The two displayed scalar integrals are
T^3/3 and T^3, respectively. Therefore

\[
R_p(T,q_T)-R_c(T,q_T)=T^3K(x,h)+O_h(T^{7/2}),
\]
\[
K(x,h)=\tfrac13\mathcal R(U,V_0)(Q_0)
  +c(Q_0)\{-2a'(x)V_0(Q_0)-\tfrac13a'''(x)U(Q_0)\}.
\tag{25}
\]

The propagator error is O_h(T^4), because (24) is O_h(T^2).
All endpoints tend to Q0 at rate O_h(T^{1/2}), so smoothness of
the fixed product proves (4), with

\[
L_f(x,h)=D\mathcal G(Q_0)\cdot K(x,h).
\tag{26}
\]

No differentiability of the unknown Theta was used.

### The separation pole and the fixed-selection stop

Only now decrease h to zero in the explicit coefficient (25).
With b=a''(x)/2, the lower-pair and singleton terms in (14) give

\[
d\cdot V_0=\tfrac13a'''(x)-\frac{4b}{h}+2j(x)b.
\tag{27}
\]

The lower term is (V02-V01)/v from (12); each lower-singleton
pair contributes -2b/h. In contrast,

\[
d\cdot U=-2a'(x)+\frac{4(a(x)-a(x+h))}{h}
                  -2j(x)a(x)-j(x+h)a(x+h),
\tag{28}
\]

which stays bounded by the mean-value formula. DU,DV0, their
divergences, k and grad k are also bounded independently of small h.
Thus (17) has exactly the pole

\[
\mathcal R(U,V_0)(Q_0)=\frac{4c(Q_0)b}{h}U(Q_0)+O_x(1).
\tag{29}
\]

The remaining term of (25) is bounded. Since
\(D\mathcal G(x,x,x)\cdot U(x,x,x)=-3a(x)f(x)^2f'(x)\),
(26),(29) prove (5).

The mean-value theorem between f(b_*)=1 and f(2b_*)=0 supplies
x0 with f'(x0)<0. At this point f is strictly between0 and1,
since a differentiable function valued in [0,1] has zero derivative
where it attains either extreme. C467u's actual signs apply because
0<x0<2b_*<X, making (5) strictly positive. Choose h small enough
that x0+h<X, h<=H_* and L_f(x0,h)>0, and keep this h fixed.
Reduce time for (4), C467p's construction and C467z's necessary
trace with eta=h. Then (4) is positive throughout that punctured
interval, contradicting (2). Every positive proposed horizon
contains such times.

These are sequential limits: h selects one separated test point,
then time is reduced for that fixed point. There is no uniform
Taylor assertion at h=0, no use of the incoming corner, and no
inference from numerical data. The independent scopes of
stops1043/1058/1060/1068/1081 are preserved.

### Independent conceptual audit — 16 November 2026, step1086

This is a REPRODUCTION conceptual audit under the invocation-start
SPECIALIZE assessment nomination1084/review1085. The audit reuses its
source comparison and the stated C467e/p/u/y/z inputs. It imports
Gerald Teschl, *Ordinary Differential Equations and Dynamical Systems*,
April2012 author preliminary version,
[Theorems2.10–2.11 and (2.58), pp46–48; Theorem3.12 and
(3.88)–(3.97), pp82–84](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
These give smooth parameter dependence and variation of constants
on the regular open charts verified here, not the curvature or its
order of vanishing. No additional source theorem is needed or reproved.

**Exact graph identification and domains.** In coordinates (6), the
elementary coefficients are

\[
e(Q)=(2m+y,m^2-w+2my,(m^2-w)y).
\]

Writing the components of the chamber coefficient momentum as
\(\widehat\pi_j(t,e(Q))\), its reconstruction gives

\[
P=\widehat\pi_1+(m+y)\widehat\pi_2+my\widehat\pi_3,\quad
S=-\widehat\pi_2-y\widehat\pi_3,\quad
W=\widehat\pi_1+2m\widehat\pi_2+(m^2-w)\widehat\pi_3.
\]

Thus (9) is smooth in w directly from the coefficient chart; no
regularity at a square-root branch is presumed. All three functions
vanish identically at t=0 and have a smooth factor t. The singleton
root, lower mean and squared lower half-gap of the separated face
are smooth in (t,x,h). The map (x,h) to (m,y) at t=0 is
(x,x+h), with determinant one. Its local inverse supplies w0.
The time-zero squared full-gap derivative8 gives w0_t=2. Since
w0(0,m,y)=0 and w0_t(0,m,y)=2 identically, Taylor's formula gives
(8) with the differentiated O(t²) remainder as well.

At fixed (t,m,y) this face has precisely the coefficient momentum
used in C467p(19). Its lower affine interpolation is P(w0)±vS(w0)
and its singleton is W(w0). This proves the asserted equality of
graphs and (10) on an open chart. Dividing their smooth differences
in w gives V; differentiating at t=0 gives (11) and the Taylor
coefficients in (12). The singleton component V0,3 is zero because
the initial chamber velocity -a(y) is independent of w.

For a fixed h>0 choose a sufficiently small closed neighborhood of
(x,0,x+h) on which both singleton gaps stay positive, inside all
inverse-chart and physical-box margins. The interpolating graphs
have uniformly O(t) spatial derivatives of every needed fixed order.
They are defined also for lambda in a small open neighborhood of
[0,1] and t near zero, after a common reduction depending on h.
Their regularized real coefficients have the strict phase margin
at t=0, and hence for that reduced time. The smooth ODE theorem
therefore applies with lambda as a parameter, including its endpoints.
Bounded velocities keep every short backward path in this chart.
At lambda=1 the paths stay in C467p's enlarged cone with positive
inverse separation, so uniqueness identifies its endpoint map.
No assertion that intermediate graphs are actual chamber flows is used.

**Phase, curvature and endpoint signs.** Differentiation of the
actual logarithmic weight gives -a·P-i d·P, with the lower-gap
contribution to d·P exactly (P2-P1)/v. The determinant contributes
-i div P. Since Im F(iQ)/Re F(iQ)=-k, differentiating (13) gives
both terms of (15), including the minus sign on DP Z. Expanding
(16) then gives (17): the two derivative terms DV U-DU V receive
the factor 1+k², and differentiation of k gives its displayed
gradient terms. Replacing V by sV yields (18), including both
gradient-of-s terms with opposite signs.

For b_lambda=B_(p_lambda)(partial_r p_lambda), differentiate the
terminal-value ODE in lambda and subtract the total r derivative
of B_(p_lambda)(delta p). The terms B_(p_lambda)(partial_r delta p)
cancel. The remaining inhomogeneous term is minus (16), proving
Z'=D_Q b_lambda Z-R_(p_lambda). The terminal point qT is fixed
in lambda and lies on w=w0(T,m,y), so delta p(T,qT)=0. At the
initial endpoint delta p(0,Q)=0 for every Q. Thus both endpoint
terms vanish, and backward variation of constants gives exactly
the positive integral (20). Equality of graph values at the endpoint
alone would not identify the two velocities.

**First-order bilinear bound after gap removal.** Here is an explicit
justification of the potentially load-bearing assertion in (22).
For any lower-equivariant vector field A put

\[
\sigma_A=(A_2-A_1)/(2v)
\]

with its smooth value at v=0. Put z_j=p_j+iQ_j. The exact smooth
factor of the weight is

\[
F(p+iQ)/v^2
 =4(\sigma_p+i)^2(z_3-z_1)^2(z_3-z_2)^2e^{-H(p+iQ)}.
\]

Consequently (13) has the form B_p(A)=N_p A, where N_p is a
real matrix, smooth in the finite collection (Q,p,Dp,sigma_p)
on the chosen chart. Its denominator is bounded away from zero
there after normalizing by the nonzero fixed-h factors. In particular

\[
D_pN_p[A]=N_{,p}A+N_{,Dp}[DA]+N_{,\sigma}\sigma_A,
\]

and D_Q N_p depends additionally on D²p and D sigma_p. Inserting
these identities into (16) shows that, with C depending on the
fixed chart,

\[
|\mathcal R_p(A,B)|\le C\,\mathcal E(A,B),
\]
\[
\mathcal E(A,B)=|A||B|+|DA||B|+|A||DB|
                     +|\sigma_A||B|+|\sigma_B||A|.
\tag{30}
\]

There is no derivative of sigma_A or sigma_B and no product DA DB:
the graph derivative differentiates N_p only, and the spatial term
is D_Q(N_p B)N_p A-D_Q(N_p A)N_p B. Smooth dependence also gives

\[
|\mathcal R_p(A,B)-\mathcal R_0(A,B)|
 \le C\,\mathcal N(p)\mathcal E(A,B),
\]
\[
\mathcal N(p)=\sup\{|p|+|Dp|+|D^2p|+|\sigma_p|+|D\sigma_p|\}.
\tag{31}
\]

The supremum is on a slightly larger fixed chart. The lower secant
and its first derivative are bounded by the first and second
derivatives of p using the integral divided-difference formula.
Thus N(p_lambda)=O_h(T), including the derivatives needed in (31).
This estimate is a concrete consequence of the factorized velocity,
not an inference from smooth ODE dependence alone.

To apply it, write E=partial_r p_lambda-U and D=delta p. Along (19),
direct differentiation of r(w-w0)V gives

\[
|E|+|\sigma_E|=O_h(T),\quad |DE|=O_h(T^{1/2}),\qquad
|D|+|\sigma_D|=O_h(T^2),\quad |D_QD|=O_h(T^{3/2}).
\tag{32}
\]

Indeed partial_r[r(w-w0)V]=(w-w0-r partial_r w0)V
+r(w-w0)partial_r V. The coefficient in its first term is O(T),
its spatial gradient is O(T^(1/2)), and every scalar coefficient
here is even in v, so taking a lower secant introduces no new loss.
The chamber contribution to E is O(r) with all relevant derivatives.
For D, use D_Qw=(-v,v,0), D_Qw0=O(r²) and the bounded secant of V.
These facts prove every bound in (32), rather than differentiating
an undifferentiated big-O assertion.

The U,DU,sigma_U quantities are bounded on this fixed chart. Equations
(30)–(32) give
\(\mathcal E(U,D)=O_h(T^{3/2})\) and
\(\mathcal E(E,D)=O_h(T^{5/2})\). Apply (31) to (U,D) and
(30) to (E,D); the result is precisely (22).

**All remaining error terms and the coefficient.** Lower equivariance
makes the difference of the two lower velocity components v times
a bounded smooth function. Hence v(r)=v(T)exp(O_h(T)); the terminal
mean and singleton move by O_h(T), and their squared half-gap is
2T+O_h(T²). This verifies all of (19), including its stronger
O(T²) error for w, not merely an O(T^(3/2)) error.

In (18), s=r(w-w0)=2r(T-r)+O_h(T³) and
grad s=r grad w+O_h(T³). The two dot products with grad w are
exactly the Taylor expansions (23). The r-weighted terms therefore
improve from the crude O(T^(3/2)) bound to O(T²). The error in
V(r,Q)-V0(Q), including its first derivative and lower secant, is
O_h(r). In the s R(U,V) term it contributes O_h(T³); in the
gradient-of-s terms the crude O_h(T^(3/2)) gradient bound gives
at worst O_h(T^(5/2)). Errors O(w²) in (23) and D_Qw0 contribute
O_h(T³). Replacing the remaining smooth factors by their values
at Q0 costs O_h(T^(5/2)), since Q_lambda-Q0=O_h(T^(1/2)).
These exhaust the terms in (18) and prove (24).

The full integrand is therefore O_h(T²); its propagator error is
O_h(T³) before integration. Integrating the two leading terms
gives T³/3 and T³, and integrating the O_h(T^(5/2)) error gives
O_h(T^(7/2)), uniformly in lambda. This proves (25). Finally
integrate D G along the segment between the two endpoint maps.
Both endpoints are Q0+O_h(T^(1/2)); their difference is O_h(T³).
Replacing this gradient by D G(Q0) costs O_(h,f)(T^(7/2)).
This checks the scalar Taylor remainder in (4), not only the
vector transport remainder.

**Sequential sign and scope.** At v=0 the lower secant of V0
contributes a'''(x)/3 to d·V0. The two singleton terms each
contribute -2b/h, and its background term is 2j(x)b. This is (27).
For U the singleton contributions combine into
4(a(x)-a(x+h))/h, which is bounded, giving (28). All other
terms of (17) and (25) are bounded as h decreases, so (29) is
the sole pole. Multiplication by D G and use of b=a''/2 gives
exactly -2c a a'' f²f' in (5), with c tending to
1+tan²(3 Im beta(ix)). No error estimate in time was used uniformly
in h in this argument.

For every allowed f the mean-value point x0 in (b_*,2b_*) has
f'<0 and 0<f<1. The inherited C467u/audit1062 signs a<0 and
a''<0 apply there with their exact finite-zero/product qualification.
The limit in (5) is strictly positive. Choose h>0 once, small enough
for L_f>0 and x0+h<X, then reduce time for the fixed-h remainder
and C467z's necessary trace with eta=h. This proves the asserted
contradiction on every proposed positive horizon. It uses no unknown
time-zero scalar derivative, uniform corner forcing or common vertex
value. All of (4)–(5) and the stated fixed-selection exclusion pass
the audit. No stronger exclusion of reselected pair/chamber data
or new mathematical discovery is claimed.

## Mathlib

Full coverage of this actual-graph calculation and prescribed-trace
obstruction has not been checked. Supporting ODE tools are imported
by the precise Teschl citation above; their presence in Mathlib is
not asserted. No claim of absence from Mathlib or all literature is made.

