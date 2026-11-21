# C467t — Adjacent vertex incidence and a conditional matching obstruction

## Hypotheses

Retain the actual coefficient flow of C467e/audit1017, triple roots and
j=1 map of C467k/audit1033, graph formulas of C467q/audit1053, the
selected j=0 test of C467r/audit1056, and C467s(8)–(17)'s two vertex
graphs and discrepancy. The latter formulas are checked below for their
use here; this does not audit C467s's entire pair/cutoff construction.
In particular retain

\[
n=3,\quad R=1/4,\quad a=1/16,\quad T_0=1/1920,
\quad X=1/256,\quad b_*=1/4096,\quad H_*=1/128,
\]
\[
\beta(z)=B(1+z)-B(1)-B'(1)z,\quad g=\beta',\quad
H=H_0+\sum_j\beta(z_j),\quad F=\Delta^2e^{-H},\quad
\Omega=F\bigwedge_{j=1}^3(dz_j/i).
\tag{1}
\]

Here B is the actual conjugation-normalized logarithm specified in the
inputs, H0 is real, beta(0)=beta'(0)=0 and |beta''|<40 on |z|<R.
Time, the divisor, and the common minus normalization are unchanged.
Let f be the fixed smooth real bump, 0<=f<=1, f=1 on [-b_*,b_*],
supported in (-2b_*,2b_*). No evenness of f or beta is imposed.

Write q1<q2<q3 for the actual positive-time roots from initial
(x,x,x), P for their real reconstruction polynomial, vj=P(qj)+i qj,
y=(q1+q2+q3)/3, and x=x(t,y) for the local inverse. Consider exactly

\[
Z_1=(1-r)\bar v\mathbf1+
r[(1-\lambda)(v_2,v_1,v_3)+\lambda(v_3,v_1,v_2)].
\tag{2}
\]

An admissible psi1 is continuous on the nominated closed parameter box,
smooth for t>0 and 0<r<1 with the stated endpoint extensions, has
psi1(0,x,r,lambda)=f(x)^3, and satisfies
dpsi1 wedge Re(-Z1^*Omega)=0 in its interior. For the obstruction also
require the nominated radial value
psi1(t,x,r,0)=psi_r(t,x,r,1), where psi_r is C467r's fixed function.
The full nomination additionally requires the upper-pair match, all
eight separate complex L1 products, both complete cutoff identities
and zero original inner radial flux. We do not weaken those requirements
for a positive result; the necessary condition below uses fewer of them.

Define real-analytic functions on the small mean interval by

\[
G(y)=\operatorname{Re}g(iy),\qquad J(y)=\operatorname{Im}g(iy),\qquad
\theta(y)=-3\operatorname{Im}\beta(iy),\qquad
E(y)=J''(y)-3G''(y)\tan\theta(y).
\tag{3}
\]

The small-phase bound in C467r makes the tangent finite. The meaning
of E here is a scalar incidence coefficient, not a symmetric root
coordinate. Retain the L018/C466a external first-zero qualification
when invoking C467q's nontriviality of G G''; it is not replayed here.

## Conclusion

In the upper graph coordinates

\[
d_-=q_1-y<0,\quad \ell=r d_-,\quad
w=(1-2\lambda)w_b(t,y),\qquad
w_b={q_3-q_2\over2d_-}<0,
\tag{4}
\]

the actual interior has w>w_b at the shared side lambda=0. The
limiting vertex characteristic field from C467s(11) has incidence

\[
\nu(t,y):=w_b(\mathcal B_p-\mathcal B_s)(t,y,0,w_b)
             -\partial_t w_b-Y(t,y,0,w_b)\partial_y w_b
={E(y)\over\sqrt6}\sqrt t+O(t).
\tag{5}
\]

The estimate is uniform on any compact mean interval strictly within
the original mean chart. If E(y0)<0, every admissible psi1 has, for
all sufficiently small positive t, the forced shared vertex value

\[
\psi_1(t,x(t,y_0),0,0)=f(y_-(0;t,y_0,w_b(t,y_0)))^3,
\tag{6}
\]

where y_- is the backward upper vertex characteristic. This is exactly
C467s's natural vertex value. In particular, if

\[
E(y_0)<0,\qquad (f^3)'(y_0)G(y_0)G''(y_0)\ne0,
\tag{7}
\]

the full nominated adjacent matching class has no solution on any
positive common time interval. Equivalently, existence in that class
requires E(y)>=0 at every point with (f^3)'(y)G(y)G''(y)!=0.

The overlap (7) is **not established by this conditional argument**.
Thus this result alone is a conditional obstruction and an explicit
test, not an exclusion of the current class. Its necessary-condition
chain is validated by conceptual audit1062 below. Other
triangles, chambers, exterior payment, realization, all degrees and
Xi transfer remain open. This is neither an RH candidate nor a claim
of novelty beyond the checked sources.

## Proof

### Gate, existing tools and the actual upper graph

The unchanged invocation-start assessment is
`drafts/literature/2026-11-16-adjacent-triangle-matching-nomination-1056.md`,
EXPLORE after separate review1057. Its actual characteristic compatibility
test covers this necessary condition; no changed source assessment is
approved during this mathematical attempt. Failure1058 stopped only
the selected conjugate construction, leaving precisely this incidence
issue. C467q's angle-independent vertex stop has a different hypothesis.

Use the already assessed smooth positive-time ODE results of Gerald
Teschl, *Ordinary Differential Equations and Dynamical Systems*,
author-hosted April2012 preliminary version,
[Lemma2.14/Corollary2.15, pp52–53; Theorem3.9, p81; Theorem6.1,
pp189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
The small-time limit uses the explicit bounded, spatially Lipschitz
field of C467r, with the same proof for the displayed upper graph.
No generic weak-transport or trace theorem is applied, and no standard
ODE theorem is reproved.

For completeness, set c=Pi3, a0=-Pi2-y Pi3 and
S=(sum(qj-y)^2)/3. The actual upper graph has

\[
\mathbf e=(-1/2,1,-1/2),\quad\mathbf v=(-1,0,1),\quad
Q=y\mathbf1+\ell\mathbf e+w\ell\mathbf v,
\]
\[
p=m\mathbf1+k_s\ell\mathbf e+k_p w\ell\mathbf v,
\quad k_p=a_0-cd_-,\quad k_s=a_0+c(d_--S/d_-).
\tag{8}
\]

These are C467s(9)–(10), obtained from the actual quadratic P, not
from a negation symmetry of beta. The basis has the same pair-distance
polynomial as C467q's graph; its possible orientation sign multiplies
the whole form and cancels in the transport quotient. Put

\[
u_0={-i m_t\over1-i m_y},\qquad
u_j={-i k_{j,t}+i k_{j,y}u_0\over1-i k_j}\quad(j=p,s),
\]
\[
K=4(k_p+i)^2[\tfrac94(k_s+i)^2-(k_p+i)^2w^2]^2
e^{-H(p+iQ)}(1-i m_y)(1-i k_s)(1-i k_p),
\]
\[
Y=-{\operatorname{Re}(Ku_0)\over\operatorname{Re}K},\qquad
\mathcal B_j=-{\operatorname{Re}(Ku_j)\over\operatorname{Re}K}.
\tag{9}
\]

Near ell=0 and w=-1/2, Re K has a nonzero floor relative to |K|:
at t=ell=0 it is the real part of
-4(9/4-w^2)^2 exp(-H0-3beta(iy)), with |3beta(iy)|<1/16.
The coefficients and their spatial derivatives extend boundedly to
t=0; they are smooth at positive time. The exact real equation off
the divisor is transport by

\[
\dot y=Y,\qquad \dot\ell=\ell\mathcal B_s,\qquad
\dot w=w(\mathcal B_p-\mathcal B_s).
\tag{10}
\]

This follows by C467q(11)–(16)'s determinant calculation applied to
(8); the real spatial coefficient is ell^6 w^2 Re K. In this proof
w stays near -1/2, so at ell<0 the division is legitimate. No
equation is postulated for the original zero form at ell=0.

### Centered-root asymmetry determines the moving angular boundary

Let delta_j=qj-y and M_k=sum delta_j^k. The symmetric quantities
M_k and P's coefficients are smooth in physical (t,x), and hence
in (t,y). C467k's root rescaling gives

\[
M_2=12t+O(t^2),\quad |\delta_j|\le C\sqrt t,\quad
a_0,c=O(t).
\tag{11}
\]

The O(t^2) remainder in M2 uses its physical-time smoothness and
its leading rescaled value 12. All spatial derivatives on the
compact mean interval have the corresponding smooth bounds.

Work first at fixed initial x. Set
V(t,x,z)=Im g(P(z)+iz). Taking imaginary parts of the actual raw
root equation, whose validity for positive-time boundary roots is
part of C467k, gives

\[
q_j'=2\sum_{k\ne j}{1\over(q_j-q_k)(1+s_{jk}^2)}+V(t,x,q_j),
\quad s_{jk}=a_0-c\delta_l\quad(\{j,k,l\}=\{1,2,3\}).
\]
\[
M_3'=6\sum_{j<k}{\delta_j+\delta_k\over1+s_{jk}^2}
 +3\sum_j(\delta_j^2-M_2/3)V(t,x,y+\delta_j).
\tag{12}
\]

The first sum is O(t^3). Indeed, as a function of delta,
1/(1+(a0-c delta)^2) differs from its value at delta=0 by
O(t^2)|delta|; sum delta_j=0 removes the constant term, and
M2=O(t) gives the claim. These estimates hold uniformly with x
derivatives; they concern exact divided secants of P.

Taylor-expand V in its last variable about y to cubic order, with
uniform O(delta^4) remainder. Write V_j for those derivatives at y.
The three centered roots satisfy the exact Newton identities
M4=M2^2/2 and M5=5M2 M3/6. Consequently (12) becomes

\[
M_3'=3V_1 M_3+{V_2\over4}M_2^2
       +O(t|M_3|+t^3).
\tag{13}
\]

For example the quadratic term before multiplication by 3 is
(V2/2)(M4-M2^2/3)=V2 M2^2/12. The quartic remainder contributes
O(t^3). Since P=O(t) with its needed derivatives, V2=J''(y)+O(t),
while y=x+O(t). M3(0,x)=0; the integral inequality from (13) first
gives M3=O(t^3). Substitution back into (13), with (11), then gives

\[
M_3(t,y)=12J''(y)t^3+O(t^4).
\tag{14}
\]

All divisions and integrations above are at t>0. Smoothness of the
symmetric coefficients at zero identifies the Taylor coefficients
in (14), so its remainder is t^4 times a smooth function; it is not
an unspecified remainder later differentiated.

Put A=sqrt(M2/2)>0 (distinct from the fixed radius a). The centered
cubic is delta^3-A^2 delta-M3/3. On writing delta=A z its roots
are smooth functions near -1,0,1 of epsilon=M3/(3A^3)=O(t^(3/2)).
Their first Taylor terms are
z_-= -1+epsilon/2+O(epsilon^2),
z_0=-epsilon+O(epsilon^2), and
z_+=1+epsilon/2+O(epsilon^2). Thus

\[
w_b=-\tfrac12-{M_3\over3A^3}+O((M_3/A^3)^2)
 =-\tfrac12-{2\over3\sqrt6}J''(y)t^{3/2}+O(t^2),
\]
\[
\partial_t w_b=-{J''(y)\over\sqrt6}\sqrt t+O(t),
\qquad \partial_yw_b=O(t^{3/2}).
\tag{15}
\]

For the first equality, the ratio is (z_+-z_0)/(2z_-), whose
expansion is -1/2-epsilon+O(epsilon^2). All expressions are smooth
in (rho,y), rho=sqrt(t); (11),(14) give factored remainders at
least rho^4 in the displayed weakened bound. Differentiating those
factorizations proves the derivative bounds in (15).

### The actual incidence and its orientation

C467q(25) gives c=-G''(y)t/2+O(t^2) and m_t(0,y)=-G(y).
Substitute d_-=-sqrt6 sqrt(t)+O(t), S=4t+O(t^(3/2)) into (8).
Then, with smooth rho remainders,

\[
k_p-k_s=-{4\over\sqrt6}G''(y)t^{3/2}+O(t^2),\qquad
\partial_t(k_p-k_s)=-\sqrt6 G''(y)\sqrt t+O(t).
\tag{16}
\]

The individual slopes and their y derivatives are O(t), with bounded
time derivatives. Therefore (9) gives
u_p-u_s=i sqrt6 G'' sqrt(t)+O(t). At ell=0 the phase of K modulo
pi is theta(y)+O(t). Since Re(iK)=-Im K,

\[
\mathcal B_p-\mathcal B_s
 =\sqrt6 G''(y)\tan\theta(y)\sqrt t+O(t).
\tag{17}
\]

Multiplying by w_b=-1/2+O(t^(3/2)) gives
-3G''tan(theta)sqrt(t)/sqrt6+O(t). Subtracting (15)'s time
derivative and Y partial_y w_b proves (5). In particular the sign
has not been inferred from an auxiliary extension. In the actual
domain D=w-w_b is positive on the inner side of lambda=0; hence
nu<0 means outgoing in forward time, and incoming when running
the same characteristics backward from the side into the triangle.

### Continuity forces the outgoing vertex value

Suppose E(y0)<0. Choose nested compact mean intervals about y0
inside the original chart, with E<=-kappa<0 on the larger one.
By (5), after decreasing time, nu(s,z)<=-c sqrt(s) for z there,
0<s<=t. The vertex field (10), ell=0, has bounded velocities and
bounded spatial derivatives. Its unique backward path from
(t,y0,w_b(t,y0)) exists down to zero and stays in the larger mean
interval and near w=-1/2, by C467r's compact-domain argument.

Along this path let D(s)=w(s)-w_b(s,y(s)). Subtract the value at
w=w_b from its differential equation. The mean value formula gives

\[
D'(s)=a(s)D(s)+\nu(s,y(s)),\quad |a(s)|\le C,\quad D(t)=0.
\tag{18}
\]

This uses the bounded w derivatives of the vertex field and (15);
the segment between w and w_b stays in the chosen auxiliary chart.
Variation of constants in (18) shows D(s)>0 for 0<=s<t, since
nu<0 for s>0. Also D(s)=O(t^(3/2)), by (5) and (18). Thus the
path has w_b<w<-w_b for every 0<s<t. The opposite angular side
cannot be reached, and the path stays strictly within the original
mean interval by the chosen margins. These facts locate the vertex
path in the actual angular domain, not just its extension.

Fix 0<s<t'<t. On [s,t'] the path has positive angular margins.
Approximate it by characteristics with small negative terminal ell.
Equation (10) preserves that sign and bounds |ell(u)| by a constant
multiple of its terminal magnitude. The original |d_-(u,y(u))| has
a positive minimum on this fixed interval. Thus for small enough
|ell| these paths have 0<r=ell/d_-<1, retain their angular and mean
margins, and converge uniformly to the vertex path. The original
adjoint equation is equivalent to (10) on these paths, so psi1 is
constant along them. Continuity on the closed original parameter box
lets ell tend to zero. Its vertex trace is consequently constant
along the vertex path on [s,t'].

Let t' increase to t, using continuity at lambda=0, then let s
decrease to zero. The original lambda(s) stays in [0,1]; uniform
continuity at t=0 applies even if it varies. Also
x(s,y(s))->y(0). The initial value is f(x)^3 for every lambda.
This proves (6), without differentiability of psi1 at either t=0
or r=0, without a lambda-independent vertex value, and without an
assumption about the upper-pair unknown or its boundary data.

### Comparison with the fixed trace and the remaining sign test

The needed part of C467s's residual can be checked directly from
(8)–(9). For the lower graph its two slope deviations from the
common a0 are +(3/sqrt6)G''t^(3/2) and -(1/sqrt6)G''t^(3/2);
for the upper graph they have the opposite signs. The imaginary
logarithmic derivatives of K at zero slopes and w=-1/2 are -5/2
for kp and -11/2 for ks. Indeed at general w they are
-3+4w^2/(9/4-w^2) and -1-9/(9/4-w^2). They include both
determinant factors. The lower phase increment is therefore
-(2/sqrt6)G''t^(3/2), and the upper one is its negative.

The mean field is
Y=-m_t(m_y+Im K/Re K)/(1+m_y^2). Its derivative with respect
to phase at time zero is G sec^2(theta). The isotropic mean field,
with both slopes replaced by a0, is independent of w and has bounded
y derivative. Hence the two backward means ending at the same (t,y)
differ at zero by

\[
y_+(0)-y_-(0)={8\over5\sqrt6}G(y)G''(y)
                       \sec^2\theta(y)t^{5/2}+O(t^3).
\tag{19}
\]

The sign is positive: the lower-minus-upper forward mean velocity
is -(4/sqrt6)G G''sec^2(theta)s^(3/2), and backward integration
negates it. For the error, both angular paths remain within O(sqrt(t))
of -1/2 by the bounded difference of slope velocities; the mean
expansion error is uniformly O(s^2+s^(3/2)|w+1/2|). Its integral
is O(t^3). Gronwall first bounds the mean difference by O(t^(5/2));
the isotropic-field difference and replacement of means by terminal y
then cost O(t^(7/2)). These are precisely the error controls in
C467s(15)–(16), rather than a differentiation of the residual itself.

C467r's fixed lower vertex value is f(y_+(0))^3, and (6) forces
the other value to be f(y_-(0))^3. Taylor's formula yields

\[
\psi_r(t,x(t,y),0,1)-\psi_1(t,x(t,y),0,0)
={8\over5\sqrt6}(f^3)'(y)G(y)G''(y)
                  \sec^2\theta(y)t^{5/2}+O(t^3)
\tag{20}
\]

wherever E(y)<0. Under (7) the leading coefficient is nonzero;
t^3=o(t^(5/2)). This contradicts the required radial equality for
every sufficiently small positive t, proving the conditional exclusion.
No original cutoff term or corner distribution was discarded: the
contradiction already follows from continuity and the interior equation.

Conjugation makes G even, J and theta odd, so E is odd. Oddness alone
does not establish (7), because f need not be even and the signs or
zeros of E on its two transition regions have not been controlled.
C467q proves G G'' is not identically zero with its stated external
qualification; that also does not give the missing sign of E.
Neither |beta''|<40 nor a numerical preview would certify that sign.
The original construction left its actual sign and overlap with the
fixed bump transition for a separate test. No class-wide stop follows
from this conditional argument in their absence.

### Conceptual audit — 16 November 2026, step1062

This REPRODUCTION audit uses the unchanged invocation-start SPECIALIZE
assessment `drafts/literature/2026-11-16-adjacent-incidence-obstruction-audit-nomination-1060.md`,
separately completed in review1061. It checks (5)–(20), including the
used graph and discrepancy passage C467s(8)–(17), but does not audit
C467s's reflected pair construction or its cutoff proof. No replacement
adjoint is constructed. The hypotheses, actual maps, original divisor,
raw time and common minus sign are unchanged.

The ODE input is Teschl's cited April2012 version, additionally
[Theorem2.5 and proof, pp40–41](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf):
continuous time dependence and a spatial Lipschitz bound give existence,
uniqueness and continuous dependence, including backward time. Together
with the already cited compact-continuation and smooth-flow results,
this applies to the explicit fields here. The bounds verified below
meet those hypotheses at zero; smooth physical-time dependence there
is not asserted. Variation of constants is applied only to the scalar
linear equation (18), not to the original singular root field.

**Raw graph, centered asymmetry and differentiated remainders.**
At lambda=0, (8)'s imaginary coordinates are exactly
(q2,q1,q3) when r=1: the second coordinate is y+d_-=q1 and
w_b d_-=(q3-q2)/2. Increasing lambda increases w since w_b<0.
The quadratic reconstruction P(z)=A0+A1 z+c z^2 has
A1=-Pi2-3yc; its paired secant and singleton quotient are precisely
a0-cd_- and a0+c(d_--S/d_-). Thus the actual angular interior is
w_b<w<-w_b, and ell<0 corresponds to r>0. The change from
(x,r,lambda) to (y,ell,w) is nonsingular at positive time and r>0.
The upper basis is a permutation of the lower basis; its orientation
changes an overall real sign only, which cancels in (9).

For the centered moment calculation all time derivatives in (12) are
first taken at fixed initial x. The imaginary part of the raw equation
is exactly the displayed q_j' equation: subtracting conjugate g adds
Im g, and the imaginary repulsion is
2/[(qj-qk)(1+s_jk^2)]. The repulsion cancels in the mean. Pairing
the j,k terms in 3 sum delta_j^2 q_j' therefore gives (12), including
the factor 6. For h(delta)=1/[1+(a0-c delta)^2], h'=O(t^2)
uniformly at the roots, because a0,c=O(t). Its constant part cancels
against sum delta_l=0, leaving O(t^2 M2)=O(t^3).

Taylor expansion of V has bounded fourth derivative on a common
compact analytic neighborhood. The constant term contributes zero;
the linear term is 3V1 M3. The quadratic contribution is V2 M2^2/4,
using M4=M2^2/2, and the cubic contribution is V3 M2 M3/4,
using M5=5M2 M3/6. The fourth-order remainder is O(t^3).
This proves (13) with bounded coefficients. Its integral inequality
first yields M3=O(t^3). Since M2=12t+O(t^2), P and its required
z derivatives are O(t), and y(t,x)=x+O(t), substitution then gives
M3'=36J''(x)t^2+O(t^3). Integrating proves (14), also at fixed
mean after using x(t,y)=y+O(t).

Both moments are smooth symmetric functions of the regular physical
coefficients. Taylor's theorem therefore gives the actual factorizations
M2=t[12+t R2(t,y)] and
M3=t^3[12J''(y)+t R3(t,y)], with smooth bounded remainders and
their needed y derivatives. In particular A=sqrt(t) a(t,y),
a(0,y)=sqrt6, is not an arbitrary O-term. The simple roots of
z^3-z-epsilon, epsilon=M3/(3A^3), give
w_b=-1/2-epsilon+epsilon^2 R(epsilon), with smooth R.
Differentiating this factored identity proves both derivatives in (15).
It justifies the O(t) derivative error, and not merely the undifferentiated
asymptotic. Similarly c=t[-G''/2+O(t)] and d_-=sqrt(t)D_-(sqrt(t),y)
with D_-(0,y)=-sqrt6 make (16)'s remainder t^2 times a smooth
function of sqrt(t),y. Its derivative is O(t).

**Incidence sign and common domain.**
The slope difference derivative in (16) gives
u_p-u_s=i sqrt6 G'' sqrt(t)+O(t). All denominator corrections
and k_y u0 differences have smaller order, since k_j=O(t),
k_p-k_s=O(t^(3/2)), and u0 is bounded. At ell=0 the phase
of K modulo pi is theta+O(t), so (17) has the displayed positive
sign. Multiplication by w_b and subtraction of w_b,t yields exactly
(J''-3G''tan(theta))sqrt(t)/sqrt6; the Y w_b,y term is O(t^(3/2)).
This proves (5) with its actual moving-boundary orientation.

Near w=-1/2, the limiting factor of K has absolute real part bounded
below by a positive multiple of its modulus. All k_t and k_ty are
bounded and continuous to zero by their factorizations, and the graph
stays strictly inside the analytic polydisc after choosing a common
small box. Thus Y, B_s, B_p and their spatial first derivatives are
uniformly bounded there. This is sufficient for the cited ODE theorems.
No estimate for a second physical-time derivative at zero is needed.
Nested mean intervals and a fixed angular neighborhood of -1/2 have
positive margins; reducing time by these fixed margins keeps every
path used below inside the auxiliary box and inside the original x
interval after the inverse mean-coordinate change.

**Outgoing vertex limit in the actual triangle.**
Fix y0 with E(y0)<0, and restrict its mean neighborhood so
E<=-kappa<0. The uniform remainder in (5) permits a common time
with nu(s,z)<=-c sqrt(s). For the backward vertex path, (18)
has the exact solution

\[
D(s)=-\int_s^t\exp\!\left(-\int_s^u a(v)\,dv\right)
                    \nu(u,y(u))\,du.
\]

Thus D(s)>=2c exp(-Ct)(t^(3/2)-s^(3/2))/3>0 for s<t,
and D(s)<=C' t^(3/2). The upper bound keeps it far from the
opposite side, whose distance tends to 1. The mean and angular bounds
prove actual-domain membership, rather than membership only in an
extension. For fixed 0<s<t'<t the angular and mean margins have
positive minima. Solve the full field backward from the same
(y(t'),w(t')) and ell(t')=-epsilon. Its multiplicative ell equation
preserves the negative sign; continuous dependence gives uniform
convergence to the vertex path as epsilon decreases to zero.
Since min_[s,t'] |d_-|>0, small epsilon gives 0<ell/d_-<1
throughout. These are actual interior characteristics with w near -1/2,
where ell^6 w^2 Re K is nonzero and division of the adjoint equation
is legitimate.

The test is constant on each approximating path. Continuity in the
original parameters passes this equality to ell=0 on [s,t'].
Let t' increase to t to reach lambda=0. Finally let s decrease to
zero. The inverse coordinate satisfies x(s,y(s))->y(0), while
lambda(s)=(1-w(s)/w_b(s,y(s)))/2 stays in [0,1]. Uniform
continuity on the closed original parameter box and the initial value
f(x)^3 give (6), even without any assumed limit of lambda(s).
The two successive limits use no derivatives of the test on r=0
or t=0. They do not impose a single physical-vertex value.

**Selected-trace discrepancy.**
At ell=0 the lower and upper graphs have the same m,a0,H0,beta
and differ only in their two slopes. Differentiating every factor of K
gives imaginary logarithmic derivatives
-3+4w^2/(9/4-w^2) and -1-9/(9/4-w^2); at w=-1/2 these
are -5/2 and -11/2. The determinant factors each contribute -1
to the appropriate coefficient. Inserting the lower deviations
(3,-1)G''t^(3/2)/sqrt6 gives phase increment
-2G''t^(3/2)/sqrt6, and the upper deviations give its negative.
The common isotropic factor is
-4(9/4-w^2)^2 exp(-H0-3beta(m+iy))(1-i m_y)(1-i a0)^8.
Its phase is independent of w in this chart. Consequently the
two mean fields have exactly C467s(15)'s expansion, with phase
derivative G sec^2(theta) at zero time.

Their angular speeds are O(sqrt(s)), and both terminal w values
are -1/2+O(sqrt(t)); hence their whole backward paths satisfy
|w+1/2|<=C sqrt(t). Their means remain y+O(t). Gronwall applied
to the difference of the two backward integral equations gives
sup |y_+-y_-|=O(t^(5/2)). The isotropic-field difference and
replacement of its smooth leading coefficient by the terminal mean
cost O(t^(7/2)). The remaining error integrates to
O(integral_0^t [s^2+sqrt(t)s^(3/2)] ds)=O(t^3).
Backward integration reverses the sign of the forward difference,
so the coefficient in (19) is +8/(5sqrt6), as stated.

C467r(20) supplies exactly f(y_+(0))^3 for the fixed lower
selection, whether its auxiliary backward path crosses an angular
side or not. The outgoing argument above supplies f(y_-(0))^3
for every admissible upper test. Taylor expansion of the fixed
smooth f^3 now proves (20); the derivative-replacement error is
O(t)*O(t^(5/2)). Under (7) its leading coefficient is nonzero,
and O(t^3)=o(t^(5/2)) gives a contradiction on every proposed
positive common time interval. If equality were specified only for
r>0, continuity at the shared vertex would give the same contradiction.

All necessary-condition links pass under the retained hypotheses.
This validates the conditional class obstruction, not the existence
of a match, the full C467s construction, or any global RH argument.

## Mathlib

Full matching coverage for the centered-root asymmetry, actual upper
incidence, continuous outgoing vertex trace and conditional matching
obstruction was not checked. C467e/k/q/r/s retain their supporting
coverage qualifications. Standard smooth ODE theory, Taylor expansion,
Newton identities and elementary integral inequalities are used in the
explicit roles above; no full Mathlib theorem is claimed present or
absent. No mathematical script or numerical certificate is used.
