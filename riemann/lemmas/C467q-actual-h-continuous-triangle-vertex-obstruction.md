# C467q — Continuous adjoints fail at the actual triangle's collapsed vertex

## Hypotheses

Use C467e/audit1017's actual regular coefficient flow and
C467k/audit1033's j=0 triangle, with their unchanged normalization:

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

Here exp B(w)=h(w)=xi(1/2+sqrt(w))/xi(1/2), with the actual
conjugation-normalized logarithm, beta(0)=beta'(0)=0 and
|beta''|<40 on |z|<R. The entire completion and critical-strip
zero correspondence are L018. For existence of at least one zero
of h, retain C466a's recorded external first-zero input
14<gamma_1<15; its certificate is not independently replayed here.
Neither the reciprocal density nor any global positivity is used.

Write q1<q2<q3 for the positive-time roots from initial (x,x,x),
P for the actual real reconstruction polynomial, vj=P(qj)+i qj,
and vbar=(v1+v2+v3)/3. The original map is

\[
Z=(1-r)\bar v\,\mathbf1+
r[(1-\lambda)(v_1,v_2,v_3)+\lambda(v_2,v_1,v_3)].
\tag{2}
\]

Let f be any fixed C-infinity real function, 0<=f<=1, equal to 1
on [-b_*,b_*], with support in (-2b_*,2b_*). Consider a real psi
continuous on [0,tau] x [-X,X] x [0,1]^2 for some tau>0 within
the actual common short-time domain. Require psi to be smooth for
t>0, 0<r<1 (in particular through lambda=1/2), with the nominated
fixed-endpoint neighborhood extensions, and

\[
\psi(0,x,r,\lambda)=f(x)^3,\qquad
\psi(t,x,0,\lambda)\text{ independent of }\lambda,
\]
\[
d\psi\wedge\operatorname{Re}(-Z^*\Omega)=0
\quad(t>0,\ 0<r<1).
\tag{3}
\]

No differentiability at r=0 or t=0 is assumed. All coefficients
and time in (1)–(3) are original; no modulus-square replacement
or change to the flow, connector or triangle is made.

## Conclusion

There is no such psi on any positive common time interval. Therefore
the exact nomination1049/review1050 test with the selected C467p
whole edge value, 0<=psi<=1, four complex weighted derivatives in L1,
and the complete cutoff identity has no solution either. In fact the
obstruction uses only (3), continuity and interior smoothness. It
does not assume an edge value, an integrability failure or a corner jet.

This is the local obstruction obtained in attempt1051 and validated
by conceptual audit1053 below, with the stated external-input
qualification. It stops this collapsed continuous triangle
class; it does not refute RH or provide global
signed assembly, exterior payment, realization or actual-Xi positivity.
C467p's existing pair construction is not contradicted: it has no
collapsed triangle vertex. Its selection identifies the nominated
excluded subclass, rather than supplying a mathematical premise of
the stronger obstruction proved here.

## Proof

### Coverage and standard inputs

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-16-reverse-continuous-triangle-trace-nomination-1049.md`,
separately completed at review1050. Its source comparisons do not
settle this precise continuous class. We reuse its scope and the
existing analytic and ODE inputs; no new source search or originality
claim is made. The target-specific work is the exact graph phase and
passage of finite positive-time characteristics to the collapsed vertex.

Use ordinary smooth ODE existence, dependence, variational and compact
continuation results only away from time zero: Gerald Teschl,
*Ordinary Differential Equations and Dynamical Systems*, author-hosted
April2012 preliminary version,
[Lemma2.14/Corollary2.15, pp52–53; Theorem3.9, p81; Theorem6.1,
pp189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
These are the imports already assessed for C467e/p. The limits at zero
below follow from explicit bounded velocities and variations. The
identity theorem and elementary real-analytic uniqueness are standard
complex-analysis inputs already used in L018 and C467e.

The only external zero input used below is the existence assertion
recorded in C466a: Sra, *On some positivity properties of the Riemann
Xi function*,
[version-specific primary text W_pr5z5huy_v1, section2.1, (6)–(8)](https://hub.valency.io/works/W_pr5z5huy_v1),
which records the verified first ordinate in (14,15). C466a identifies
its external zero-isolation and Platt–Trudgian qualifications. We reuse
that already carried input, not its density theorem or stronger finite
verification. The elementary specialization needed here is simply that
h has a zero. No new zero-free region or numerical evidence is asserted.

### The actual background has a nontrivial even real part

Put

\[
G(y)=\operatorname{Re}g(iy)
     ={g(iy)+g(-iy)\over2}\quad(y\in\mathbb R).
\tag{4}
\]

The equality follows from conjugation. This is a real-analytic even
function near zero and G(0)=0. It is not identically zero. Indeed,
if it were, the holomorphic identity theorem would give
g(z)+g(-z)=0 on the original disk. Integrating with beta(0)=0 gives
beta(z)=beta(-z), and hence

\[
h(1+z)=e^{2B'(1)z}h(1-z).
\tag{5}
\]

Both sides are entire in z, so (5) would hold everywhere. L018 implies
that every zero w of h has Re w<1/4: choose s=1/2+sqrt(w), a zero
of xi, and use 0<Re s<1 and
Re w=(Re s-1/2)^2-(Im s)^2<1/4. On the other hand the recorded
first-zero input supplies at least one such w. Equation (5) would
make 2-w another zero, with Re(2-w)>7/4, a contradiction. This uses
only the classical critical strip, not RH or the October2026 inputs.

Since G is even, G(0)=0 and G is nonzero as an analytic function,
G'' is also not identically zero. Consequently G G'' cannot vanish
on any open real interval in its connected analytic domain. In
particular its zeros cannot cover an open part of the bump transition.

### Exact physical graph of the triangle

Use a new mean imaginary coordinate

\[
y=\tfrac13\sum_jq_j=E_1(t,x)/3.
\tag{6}
\]

The map x to y has derivative 1+O(t), so it has a unique smooth
local inverse x=x(t,y) on a slightly smaller fixed interval inside
(-X,X), for a common small time. We shall work near a bump-transition
point, well inside that interval. All following coefficient functions
are evaluated at x(t,y). Put

\[
m(t,y)=\tfrac13\sum_jP(q_j),\quad
d=q_3-y,\quad \alpha=q_2-q_1,\quad
S=\tfrac13\sum_j(q_j-y)^2,
\]
\[
k_1={P(q_2)-P(q_1)\over q_2-q_1},\qquad
k_3={P(q_3)-m\over d}.
\tag{7}
\]

The mean m is smooth in physical (t,y), by the symmetric identity
3m=3Pi1+2E1 Pi2+E2 Pi3. C467k's root rescaling gives, with
rho=sqrt(t),

\[
d=\sqrt6\rho+O(\rho^2),\quad
\alpha=\sqrt6\rho+O(\rho^2),\quad S=4\rho^2+O(\rho^3).
\tag{8}
\]

All remainders are smooth in (rho,y), with their y derivatives.
Writing P(z)=A_0+A_1z+Pi3 z^2 gives the exact identities

\[
k_1=-\Pi_2-q_3\Pi_3,
\qquad k_3-k_1=\Pi_3(2d-S/d).
\tag{9}
\]

For the second identity, the quadratic secant for k1 is
A1+Pi3(2y-d); the mean-subtracted quotient for k3 is
A1+Pi3(2y+d-S/d). Since Pi=O(t) smoothly in initial coefficients,
(8)–(9) show that k1 and k3 are t times smooth functions of (rho,y).
Thus k1,k3 and their y derivatives are O(t), while their derivatives
in physical t at fixed y, and the y derivatives of those derivatives,
are bounded. This statement differentiates the smooth factorizations,
not an unspecified remainder.

Write Q=Im Z and p=Re Z, and introduce

\[
\mathbf e=(-1/2,-1/2,1),\quad \mathbf v=(-1,1,0),\qquad
Q=y\mathbf1+\ell\mathbf e+v\mathbf v.
\]

On the triangle,

\[
\ell=rd,\qquad v=r(1-2\lambda)\alpha/2,
\qquad
p=m\mathbf1+k_3\ell\mathbf e+k_1v\mathbf v.
\tag{10}
\]

These are exact, by linear interpolation of the first two values
and the definition of k3 for the third. For t>0,r>0, (x,r,lambda)
to (y,ell,v) is a nonsingular real coordinate change, even at
lambda=1/2. No assertion about immersion at the collapsed vertex
is needed. Set w=v/ell. The interior triangle includes |w|<=1/3
for all small common time, since alpha/(2d) tends to 1/2.

### Reduced phase and bounded characteristic field near the vertex

In the real basis (1,e,v), the matrix D_Q p is triangular:

\[
D_Qp=\begin{pmatrix}
m_y&0&0\\ k_{3,y}\ell&k_3&0\\ k_{1,y}v&0&k_1
\end{pmatrix}.
\tag{11}
\]

Put M=Id-iD_Qp and u=-i M^{-1}p_t, with p_t at fixed Q, equivalently
fixed y,ell,v. For small time M is invertible. Its components in the
same basis are

\[
u_0={-i m_t\over1-i m_y},\quad
u_\ell=\ell u_3,\quad
u_3={-i k_{3,t}+i k_{3,y}u_0\over1-i k_3},
\]
\[
u_v=v u_1,\qquad
u_1={-i k_{1,t}+i k_{1,y}u_0\over1-i k_1},\quad
\det M=(1-i m_y)(1-i k_3)(1-i k_1).
\tag{12}
\]

All quantities in (12) are bounded and smooth in (rho,y); their y
derivatives are bounded. The exact differences of Z in (10) give

\[
\Delta(Z)^2=4(k_1+i)^2v^2
  [\tfrac94(k_3+i)^2\ell^2-(k_1+i)^2v^2]^2.
\tag{13}
\]

Accordingly F det M=ell^6 w^2 K, where the explicit smooth factor is

\[
K(t,y,\ell,w)=4(k_1+i)^2
 [\tfrac94(k_3+i)^2-(k_1+i)^2w^2]^2 e^{-H(Z)}\det M,
\]
\[
Z=(m+iy)\mathbf1+(k_3+i)\ell\mathbf e
                         +(k_1+i)w\ell\mathbf v.
\tag{14}
\]

On |w|<=1/3 this factor is nonzero for small time and ell near zero.
More precisely at t=ell=0 it is
-4(9/4-w^2)^2 exp(-H0-3beta(iy)). On a fixed compact mean interval
inside (-X,X), |3beta(iy)|<=60y^2<1/16. Uniform continuity therefore
gives |Re K|>=c|K|>0 on a common small (rho,ell) box, with c>0.
This also supplies a smooth phase branch locally; all quotient
derivatives in y,ell,w below are bounded there. Formula (14), including
its nonzero value at w=ell=0, is used solely for the auxiliary field.
The original form still vanishes there as in (13).

For completeness the real adjoint sign follows directly. In Q
coordinates dZ/i=M(dQ+u dt), so the pulled-back three-form is
kappa vol_Q+dt wedge iota_(kappa u)vol_Q, kappa=F det M. Wedging
dchi with its real part gives
(Re kappa chi_t-Re(kappa u) dot D_Q chi) dt wedge vol_Q.
Thus off w=0 the exact normalized equation is

\[
\chi_t+b\cdot D_Q\chi=0,\qquad
b=-\operatorname{Re}(Ku)/\operatorname{Re}K.
\tag{15}
\]

The common minus normalization cancels from this equation. For each
ell>0 it extends to w=0 by interior smoothness of chi and of (14)–(15),
because it holds on the dense set w!=0. This is not an assumed equation
on the original zero set; it is the continuous limit of a valid equation
where its real spatial coefficient is nonzero.

By (12), the real characteristic field has components

\[
\dot y=Y=-{\operatorname{Re}(Ku_0)\over\operatorname{Re}K},\quad
\dot\ell=\ell B_3,\quad \dot v=v B_1,\qquad
B_j=-{\operatorname{Re}(Ku_j)\over\operatorname{Re}K}.
\]

Consequently in (y,ell,w) it is exactly

\[
\dot y=Y(t,y,\ell,w),\quad
\dot\ell=\ell B_3(t,y,\ell,w),\quad
\dot w=w(B_1-B_3)(t,y,\ell,w).
\tag{16}
\]

These coefficients extend continuously to time zero and smoothly in
(y,ell,w) through ell=0, with bounded spatial first derivatives on the
small box. They are smooth in positive physical time. No time variable
has been substituted into the current or its equation. The sqrt(t)
notation only verifies boundedness of the original physical derivatives.

### Continuity forces a single vertex value to obey every angle drift

Suppose psi satisfies (3), and write chi(t,y,ell,v) for it in (10).
Continuity and the collapse requirement give a single value

\[
C(t,y)=\psi(t,x(t,y),0,\lambda),\quad
C(0,y)=f(y)^3,
\tag{17}
\]

independent of lambda. For fixed positive time, chi(t,y,ell,w ell)
tends to C(t,y) as ell decreases to zero, uniformly on local compact
sets of (t,y,w) with |w|<=1/3. This follows directly from continuity
on the original compact parameter box and (10), not from a derivative
trace assertion.

Fix a compact positive-time interval [s,t]. For sufficiently small
positive terminal ell, characteristics (16) stay inside the triangle
throughout that interval if their mean and angle have interior margins.
Indeed ell remains positive and changes by a factor between exp(-C(t-s))
and exp(C(t-s)); the outer d has a positive minimum on [s,t]. The mean
and angular velocities are bounded, so choosing a smaller interval if
needed retains their margins. For w=0 the angular coordinate is exactly
invariant, and one can use any [s,t] within a sufficiently small common
time and fixed interior mean interval. Smooth ODE theory applies on
each such positive-time interval. Smooth spatial dependence of (16)
down to ell=0 shows that these paths converge to its ell=0 paths.

The normalized equation (15), including w=0, makes chi constant along
the positive-ell paths. Pass to the limit using (17). The vertex value
C is therefore constant along the limiting paths

\[
\dot y=Y(t,y,0,w),\qquad
\dot w=w(B_1-B_3)(t,y,0,w).
\tag{18}
\]

For w=0 this is the scalar mean flow y'=Y(t,y,0,0). Let Phi(t,y)
be its backward time-zero endpoint. It exists locally on a fixed
interior mean interval: on (0,t] the velocity and its y derivative
are uniformly bounded; compact continuation first reaches every s>0,
and the endpoint is Cauchy as s decreases to zero. The same bounds
keep it inside the larger mean interval. Gronwall gives uniqueness
and continuous dependence up to zero. The variational equation on
[s,t] gives, in the limit,

\[
\Phi_y(t,y)=\exp\left(-\int_0^t
 Y_y(u,y(u),0,0)\,du\right)>0,\qquad \Phi(t,y)=y+O(t).
\tag{19}
\]

The convergence of the derivatives follows from bounded continuous
Y_y and the uniform convergence of the trajectories; equivalently
pass to the limit in their scalar variational integral equations.
Higher y derivatives are locally bounded by the same smooth compact
coefficients if needed. For positive t the endpoint is differentiable
in t by ordinary flow composition. Taking s to zero in the w=0 case
of (18), joint continuity of (17) gives

\[
C(t,y)=f(\Phi(t,y))^3.
\tag{20}
\]

In particular C is C1 for positive time; this regularity has been
deduced, not assumed at the vertex. At any positive (t,y) and any
|w|<1/3, use (18) on a sufficiently small interval about t and
differentiate (20) along that smooth path. Since C is independent of w,

\[
C_t(t,y)+Y(t,y,0,w)C_y(t,y)=0
\quad\hbox{for every }|w|<1/3.
\tag{21}
\]

Only fixed positive-time intervals and continuity were used to reach
(21). No joint t,r boundary jet, integrability interchange or edge
regularity has been inserted.

### Exact angular discrepancy and the bump contradiction

At ell=0 set K0=K(t,y,0,0) and

\[
D={4\over9}\left({k_1+i\over k_3+i}\right)^2.
\]

Then (14) gives K(t,y,0,w)=K0(1-Dw^2)^2. If z=w^2 and phi(z)
is any continuous phase branch of this nonzero factor, elementary
logarithmic differentiation gives

\[
{d\phi\over dz}=-{2\operatorname{Im}D\over|1-Dz|^2},\qquad
\operatorname{Im}D={8\over9}
{(1+k_1k_3)(k_3-k_1)\over(1+k_3^2)^2}.
\tag{22}
\]

There is no phase singularity, since Re K stays nonzero. From (12),
u0=m_t(m_y-i)/(1+m_y^2); thus

\[
Y(t,y,0,w)=-{m_t\over1+m_y^2}
       \left(m_y+{\operatorname{Im}K\over\operatorname{Re}K}\right).
\tag{23}
\]

Differentiating (23) in z at zero, using (22), shows that
Y(t,y,0,w) is nonconstant near w=0 whenever m_t(k3-k1)!=0.
Explicitly that derivative is
2m_t Im D sec^2(phi(0))/(1+m_y^2), nonzero in this case because
1+k1 k3 is positive at sufficiently small time. Equations (21) for
all angles therefore force the necessary condition

\[
m_t(t,y)(k_3-k_1)(t,y) C_y(t,y)=0.
\tag{24}
\]

It remains to check that this is an actual-data obstruction. At time
zero on distinct imaginary coordinates, the repulsion in the original
raw flow is purely imaginary, so
p_j'(0)=-Re g(iq_j)=-G(q_j). Since P(0) is identically zero,
the quadratic polynomial P_t(0,z) interpolates -G at those three
initial nodes. Its leading coefficient is Pi3_t. Letting the nodes
coalesce at y gives

\[
\Pi_{3,t}(0,y)=-\tfrac12G''(y),\qquad m_t(0,y)=-G(y).
\tag{25}
\]

The first limit follows from the ordinary second divided difference,
or the Taylor formula with integral remainder for G. C467e's smooth
coefficient field justifies its identification with the repeated-node
value. The mean identity follows either by averaging this polynomial
or by summing the raw equations before coalescence. Passing from fixed
initial x to fixed mean y introduces no extra time-zero term: both
Pi3(0,x) and m(0,x) vanish identically, so their x derivatives vanish.
Thus (25) holds with exactly the fixed-y time derivatives in (12).

Smooth coefficient dependence now yields
Pi3(t,y)=-t G''(y)/2+O(t^2) and m_t(t,y)=-G(y)+O(t).
Combining these with (8)–(9) gives

\[
k_3-k_1=-{4\over\sqrt6}G''(y)t^{3/2}+O(t^2),\qquad
m_t(k_3-k_1)={4\over\sqrt6}G(y)G''(y)t^{3/2}+O(t^2).
\tag{26}
\]

There is an open interval in (b_*,2b_*) on which f>0 and f'!=0:
f starts at 1 and becomes 0, so the mean value theorem and smoothness
supply such an interval (one may take a point where 0<f<1).
By (4)–(5), choose y0 in this interval with G(y0)G''(y0)!=0.
For all sufficiently small positive t, (26) makes m_t(k3-k1) at
(t,y0) nonzero. Equations (19)–(20) simultaneously give

\[
C_y(t,y_0)=3f(\Phi(t,y_0))^2f'(\Phi(t,y_0))\Phi_y(t,y_0)\ne0,
\tag{27}
\]

since Phi(t,y0) tends to y0 and Phi_y is positive. This contradicts
(24). All selected points have |x(t,y0)|<X and all characteristics
used in deriving (21) can be kept on strict angular and mean interiors.
Shrinking time is allowed for a contradiction to any proposed tau>0.

### Scope and checks

The contradiction precedes the prescribed r=1 value and any cutoff
identity. Hence it excludes the nominated class, which contains these
requirements, without having to infer a failure of weighted L1 control
or discard a boundary face. In particular, a construction with any
other edge data still cannot satisfy exactly (3) for this bump and
this collapsed continuity condition. A different filling or a class
without this vertex continuity is not addressed.

The essential source specialization was the existence/strip argument
in (4)–(5); the exact coefficient checks are (9), (11)–(14),
(22)–(23) and (25)–(26). No numerical script is used as proof.
This does not repeat C467n's joint-smooth initial-corner argument:
only interior smoothness, positive-time characteristic constancy and
continuity are used here. The independent audit below checks the
vertex-limit passage, the fixed-mean derivatives and angular phase.

### Independent conceptual audit — 16 November 2026, step1053

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-16-continuous-triangle-vertex-audit-nomination-1051.md`,
separately approved by review1052. This is a REPRODUCTION audit of
(4)–(27), not a new transport construction or a new standard theorem.
The hypotheses, normalization, constants and conclusion are unchanged.
The audited local contradiction passes, retaining C466a's external
first-zero existence qualification. The audit does not independently
verify that certificate or the entire source manuscript.

**Actual-background input.** L018 gives both reflection about 1/2 and
the open-strip location of every zero of xi. Thus h is entire, and
every h-zero w satisfies Re w<1/4, regardless of square-root choice.
If G vanished identically on any real interval in its domain, analytic
uniqueness would give g(z)+g(-z)=0 on the original disk. The derivative
of beta(z)-beta(-z) is precisely this sum, so its value at zero proves
beta(z)=beta(-z). Exponentiation gives (5), with the factor
exp(2B'(1)z); its sign and factor two are correct. Entire continuation
then sends any h-zero w to the h-zero 2-w. Existence of one zero from
the carried citation contradicts the open-strip bound. No density,
zero-count estimate, RH-equivalent sign or stronger zero-free region
is used. Since G is even and G(0)=0, G'' identically zero would also
force G identically zero. Each of G and G'' is therefore a nonzero
real-analytic function on the connected interval in use; their product
cannot vanish on an open bump-transition interval.

**Coordinates, secants and physical derivatives.** C467e's contour
Hamiltonian is smooth on an open coefficient neighborhood containing
the repeated initial triple, as checked in audit1017. C467k/audit1033
gives its actual ordered roots and their smooth rho-rescaling. Thus
E1/3=x+O(t), including x derivatives. The inverse x(t,y) exists on
nested fixed mean intervals for sufficiently small time. The identity
sum P(qj)=3Pi1+2E1 Pi2+E2 Pi3 proves smoothness of m in physical
(t,y). In particular, no derivative of an individual root is used
to assert that smoothness.

For P(z)=A0+A1 z+Pi3 z^2, A1=-Pi2-3y Pi3. Since
q1+q2=2y-d and the mean of qj^2 is y^2+S, the secants are exactly
k1=A1+Pi3(2y-d) and k3=A1+Pi3(2y+d-S/d). This verifies (9).
Writing d=rho d0 and S=rho^2 S0, d0(0,y)=sqrt(6) and S0(0,y)=4,
makes S/d=rho S0/d0 smooth on a fixed neighborhood. Since Pi=t times
a smooth function of (t,y), each kj=t aj(rho,y) with aj smooth.
Its physical derivative is aj+(rho/2) aj_rho; this and every needed
y derivative are bounded and continuous to t=0. Differentiating
an unqualified O(rho^2) error would not suffice; these factorizations do.

The differences and sum of the first two components in (2) give (10)
exactly, including the sign v=r(1-2lambda)alpha/2. The Jacobian from
(x,r,lambda) to (y,ell,v) is -y_x d r alpha, nonzero for t,r>0.
The fixed basis (1,e,v) has real determinant -3. Consequently the
ordinary Q-coordinate determinant is 3 y_x d r alpha, including at
lambda=1/2. This is a valid positive-time chart independently of the
zero of F there. The triangle is 0<ell<d and |w|<alpha/(2d);
alpha/(2d) tends uniformly to 1/2, so a box |w|<=1/3 lies strictly
inside its angular boundaries for small time.

**Original form, zeros and angular phase.** Differentiating (10) at
fixed Q gives (11). Solving the lower triangular system
M u=-i p_t gives every entry of (12), with p_t at fixed y,ell,v.
The three differences of Z are 2(k1+i)v and
(3/2)(k3+i)ell plus or minus (k1+i)v. Their squared product is
exactly (13). Thus the real factor removed off the divisor is ell^6 w^2,
and (14) gives K at w=0 without dividing by a complex phase.
At t=ell=0 its value is the displayed negative real polynomial in w
times exp(-H0-3beta(iy)). The bound |3beta(iy)|<1/16 and compactness
give a uniform nonzero real part for K on a smaller common box.
The graph and that box stay inside the original beta polydisc.

In Q coordinates, expanding the wedge of M(dQ+u dt) gives
kappa vol_Q+dt wedge iota_(kappa u)vol_Q. In dchi wedge this form,
the spatial derivative term is -kappa u dot D_Q chi. This verifies
the minus sign in b in (15). The common minus sign on the entire
current cancels. The equation is first obtained for w!=0; interior
smoothness of chi in the nonsingular chart and smoothness of the
normalized coefficients extend it to w=0 for ell>0. No equation is
asserted by division on the collapsed vertex itself. The components
in (16) and their spatial first derivatives extend continuously to
t=0 and smoothly across ell=0. This is enough for the limit arguments;
smoothness in physical time at zero is neither needed nor imported.

At ell=0 the ratio K/K0=(1-Dw^2)^2 follows directly from (14).
Indeed (k1+i)/(k3+i) has real numerator 1+k1 k3 and imaginary
numerator k3-k1 over 1+k3^2. Squaring verifies Im D in (22).
For z=w^2, Im[-2D/(1-Dz)]=-2 Im D/|1-Dz|^2, proving its phase
derivative. Also u0=m_t(m_y-i)/(1+m_y^2), which gives (23) with
the displayed sign. The derivative Y_z at z=0 is
2m_t Im D sec^2(phi(0))/(1+m_y^2). For small time 1+k1 k3>0,
so m_t(k3-k1)!=0 makes Y genuinely angle-dependent. Comparison
with w=0 is legitimate even though the original form vanishes there.

**Successive limits and deduced vertex regularity.** Fix nested compact
mean intervals around the bump transition, inside (-X,X). On the
extended box the field and its spatial first derivatives have a common
bound M. Shrink the time so that M times its length is smaller than
the mean margin. On any fixed [s,t] with s>0, d has a positive minimum.
For sufficiently small positive terminal ell, the equation
ell'=ell B3 keeps ell positive and at most ell(t) exp(M(t-s)), hence
strictly less than d along the whole trajectory. For w=0 the angle
stays zero. For any other strictly interior angle choose a small time
interval about the point so that its angular margin is retained.
These are actual interior triangle characteristics, not merely paths
of an auxiliary extension outside the triangle.

Uniform spatial Lipschitz bounds and Gronwall imply convergence of
these paths to the ell=0 paths as the terminal radius decreases to
zero. On [s,t], r=ell/d tends uniformly to zero. The inverse relation
lambda=(1-2dw/alpha)/2 stays in a compact angular interval. Joint
continuity of psi on its parameter box therefore identifies its
endpoint limits with the single C(t,y) in (17). Characteristic
constancy passes to that limit and proves (18), without differentiating
C or assuming a radial derivative bound. This limit is taken with s
fixed; it does not assert uniform immersion or characteristic retention
in the triangle as s tends to zero at positive radius.

For the separate central-angle time limit, |Y|<=M makes the backward
mean endpoints Cauchy as s tends to zero. The mean margin above retains
all endpoints in the larger interval. The bound |Y_y|<=M gives unique
limiting trajectories and the estimates
exp(-Mt)<=Phi_y(t,y)<=exp(Mt). More explicitly, the finite-s endpoint
derivative is exp(-integral_s^t Y_y(u,y(u),0,0) du). The trajectories
converge uniformly and Y_y is continuous on the compact box, so these
derivatives converge locally uniformly to (19). Uniform convergence
of the endpoint maps and their derivatives gives a differentiable
limit Phi; this is not an inference from pointwise convergence alone.
Positive-time flow composition makes Phi differentiable in t there.
Taking s to zero in the already established vertex constancy, using
C(s,y(s)) -> f(Phi)^3, proves (20). Only now is C differentiated
along the other limiting angle paths. This proves (21), and the phase
comparison above gives (24). The two limits and the order in which
vertex regularity is obtained are valid under the stated hypotheses.

**Confluent actual coefficients and the final contradiction.** For
distinct initial imaginary nodes, the repulsion term is imaginary and
the real raw velocity is -G(qj). Since P(0,z) is the zero polynomial,
differentiating P(t,qj(t)) at zero introduces no P_z qj' term.
The polynomial P_t(0,z) therefore interpolates -G. Its leading
coefficient is -G[q1,q2,q3], which tends to -G''(y)/2. The standard
confluent interpolation input is Carl de Boor, *Divided Differences*,
Surveys in Approximation Theory 1 (2005), 46–69, author version
21 December 2004, [Sections 8–9, pp60–64, Proposition43/(44),
(51)–(52)](https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf),
with its already assessed smooth real-node hypotheses. It is imported,
not reproved. Smoothness of the regular coefficient field identifies
this distinct-node limit with Pi3_t at the repeated initial triple.
The average real velocity similarly tends to -G(y). Both m(0,x)
and Pi3(0,x) vanish identically, so the coordinate change x=x(t,y)
adds zero to their time-zero derivatives. This verifies (25) at fixed
mean, rather than silently substituting fixed-initial-coordinate data.

Finally 2d-S/d=(8/sqrt(6))sqrt(t)+O(t), uniformly near the selected
mean. Multiplication by Pi3=-t G''/2+O(t^2) gives the coefficient
-4G''/sqrt(6) in (26), and multiplication by m_t=-G+O(t) gives
its positive 4G G''/sqrt(6). The remainder is O(t^2), smaller than
the nonzero leading t^(3/2) term at any fixed selected y0. The decrease
of f from 1 at b_* to 0 at 2b_* supplies a point with f'!=0; the
bounds 0<=f<=1 force 0<f<1 at such an interior point. Continuity
supplies an open interval with both properties. Analytic uniqueness
then permits y0 in that interval with G G''!=0. The limiting Phi and
positive Phi_y make (27) nonzero for sufficiently small time, violating
(24). All restrictions are local inside the original mean and angular
domains; shrinking time is allowed for any proposed tau>0.

The audit establishes exactly this local nonexistence. It neither
constructs the four weighted integrals nor proves a separate failure
of any one of them: the nominated class is excluded by a subset of
its requirements. C467p's pair result, other regularity classes and
different fillings are unaffected. No hypothesis or mathematical input
was changed, and no numerical or symbolic script is evidence for the
analytic limits. Global signed assembly and actual-Xi positivity remain
unresolved. This is validation of existing local work, not a claim of
progress beyond the sources checked or a complete RH candidate.

## Mathlib

Full matching coverage for this actual continuous collapsed-triangle
obstruction has not been checked. Supporting ODE, identity-theorem and
elementary differentiation facts are not a formalization of (18)–(27).
No new Mathlib search, exact declaration claim or absence claim is made.
Audit1053 checks the informal argument only; it does not supply a
formalization of the result or verify the carried external zero certificate.
