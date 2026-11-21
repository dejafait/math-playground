# C467z — Actual chamber characteristics and the separated necessary trace

## Hypotheses

Retain C467e/audit1017's actual coefficient flow and momentum graph,
C467i/audit1025's chamber convention, and C467p/audit1049's original
lower pair and its fixed test. C467y's lower test is exactly this
phi_p. In particular

\[
n=3,\quad R=1/4,\quad a=1/16,\quad T_0=1/1920,\quad
X=1/256,\quad b_*=1/4096,\quad H_*=1/128,
\]
\[
\beta(z)=B(1+z)-B(1)-B'(1)z,\quad g=\beta',\quad
H=H_0+\sum_j\beta(z_j),\quad H_0\in\mathbb R,
\quad F=\Delta^2e^{-H},\quad
\Omega=F\bigwedge_{j=1}^3(dz_j/i).
\tag{1}
\]

B is the actual conjugation-normalized logarithm of
xi(1/2+sqrt(w))/xi(1/2), beta(0)=beta'(0)=0 and |beta''|<40
on |z|<R. All inherited finite-zero/product and C466a
reciprocal-density qualifications remain; no such source is replayed
or strengthened here. Time is raw physical time, the divisor and
algebraic-square weight are unchanged, and the entire form carries
the common minus sign.

Let f be any fixed smooth real function with 0<=f<=1, equal to one
on [-b_*,b_*], supported in (-2b_*,2b_*); neither f nor beta is
assumed even. Write G(q)=product_j f(q_j). The actual ordered chamber
is u1<u2<u3 in (-a,a)^3, with Y(0,u)=iu and C467e's reversed field.
A candidate scalar Theta is continuous up to its initial and collision
faces, smooth in the positive-time distinct-coordinate interior, and
satisfies

\[
d\Theta\wedge\operatorname{Re}(-Y^*\Omega)=0,
\qquad\Theta(0,u)=G(u).
\tag{2}
\]

Only a neighborhood inside this chamber of the displayed lower faces
is needed. If Theta has a time horizon smaller than one below, take
the minimum. No boundary derivative of Theta is assumed.

## Conclusion

There is one existential positive time tau<=T0 on which the actual
chamber adjoint has a smooth real physical-coordinate velocity b_c
on an open box containing [-a/2,a/2]^3, including its diagonals.
Its backward endpoint map R_c(t,q) is smooth on a neighborhood of
the lower-face images and satisfies |R_c(t,q)-q|<=Ct. This is an
auxiliary regular extension of the exact interior equation, not a
claim that every such path stays in the original chamber image.

Write q^+(t,x,h)=Im Y^+(t,x,x+h), using the actual ordered lower-face
limit supplied by C467p, including h=0. Define

\[
T_c(t,x,h)=G(R_c(t,q^+(t,x,h))).
\tag{3}
\]

This function is continuous on the whole compact face box
0<=t<=tau, |x|<=X, 0<=h<=H_*, with initial value f(x)^2 f(x+h).
For each fixed eta in (0,H_*], there is a possibly smaller
tau_eta>0 such that every candidate (2) necessarily satisfies

\[
\Theta(t,x,x,x+h)=T_c(t,x,h)
\quad(0\le t\le\tau_\eta,\ |x|\le X,\ \eta\le h\le H_*).
\tag{4}
\]

The backward paths giving (4) stay in the original ordered chamber
for earlier positive times and reach its time-zero interior; no free
side datum enters. In the squared initial lower-gap coordinate k,
their backward derivative lies between 4 and 12 after a suitable
common reduction depending on eta. Its exact time-zero face value
is 8. Forward incidence is therefore outward at these separated faces.

On the full face box there is also the uniform comparison

\[
|T_c(t,x,h)-\phi_p(t,x,1,h)|\le C_f t.                 \tag{5}
\]

This estimate proves neither equality nor a nonzero discrepancy.
For h approaching zero at fixed positive t, (3) is a particular
regularly transported value, not a proved necessary trace. No positive
lower bound for tau_eta as eta decreases to zero is established.
The precise incidence question left by this result is (15) below.
Independent conceptual audit1083 below validates this partial result
of attempt1080; C467 separately resolves its local corner sign.
It is not a matching theorem, a stopped matching class, an integrable
chamber identity, or an RH candidate.

## Proof

### Source scope and the physical chamber graph

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-16-chamber-lower-pair-trace-nomination-1078.md`,
separately reviewed at1079. It covers this necessary-trace attempt.
The application work is the actual graph factorization and original
chamber incidence, not a reproof of a general characteristic theorem.
Import Gerald Teschl, *Ordinary Differential Equations and Dynamical
Systems*, April2012 author preliminary version,
[Theorems2.5/2.10 pp40–47, Lemma2.14/Corollary2.15 pp52–53,
Theorems3.9/3.12 pp81–84 and Theorem6.1/proof pp189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf),
within the regular domains verified below. Characteristic constancy
uses the ordinary chain rule on the smooth interior. No weak trace
theorem, Stokes limit, or time-zero jet theorem is imported.

Let e(q)=(q1+q2+q3,q1q2+q1q3+q2q3,q1q2q3), J_e=D_q e,
and denote C467e's elementary coefficient solution by
(E_t(e0),Pi_t(e0)). Let D_t=D_(e0) E_t and
pi_hat_t=Pi_t composed with E_t^{-1}. C467e(21)–(24) proves
smoothness on a neighborhood of a compact coefficient set containing
e([-a,a]^3), with D_t tending uniformly to the identity. Compact
containment and that local inverse therefore give, on reducing time,
one graph on all q in (-3a/4,3a/4)^3:

\[
p(t,q)=J_e(q)^T\widehat\pi_t(e(q)),\qquad Y=p(t,q)+iq.
\tag{6}
\]

More explicitly, a compact neighborhood of the smaller coefficient
image stays in E_t(V0) for small time: the inverse of a C1-small
perturbation of the identity exists on every fixed compact subset
of V0, by the inverse construction in C467e and its strict boundary
margin. This avoids extending an inverse only known on individual
simple-root charts. The graph is real and smooth even when q has
repeated entries. All its fixed finite-order derivatives are bounded
on smaller compact boxes. Since Pi_0 is identically zero, p and
all its spatial derivatives are O(t), while p_t is bounded.
At actual distinct chamber points (6) is the original flow graph,
by C467e's agreement and projection argument.

For l the remaining index, the exact reconstruction polynomial gives

\[
p_k-p_j=(q_k-q_j)\sigma_l,\qquad
\sigma_l=-\widehat\pi_{t,2}-q_l\widehat\pi_{t,3}=O(t).
\tag{7}
\]

Set M=Id-iD_qp and define smooth functions

\[
\widehat A=e^{-H(p+iq)}\prod_{l=1}^3(i+\sigma_l)^2\det M,
\qquad v=-iM^{-1}p_t.
\tag{8}
\]

For small common time M is invertible. Exactly, the original spatial
coefficient in these q coordinates is A=Delta(q)^2 widehat A.
At t=0, widehat A=-exp(-H(iq)). On the closure of the enlarged
q box, |sum beta(iq_j)|<=60(3a/4)^2<1/4. The continuous
small-time factors in (7)–(8) thus allow one common reduction with

\[
\operatorname{Re}(-\widehat A)\ge\tfrac12|\widehat A|>0.
\tag{9}
\]

This uses the full determinant and complex phase. It does not replace
Delta squared by a modulus square in the original form.

The replaced-column coefficients in the physical graph are A v_j,
since Z_q/i=M and Z_t/i=-ip_t at fixed q. C467i's wedge convention
then gives for a scalar chi
Re(A) chi_t - sum_j Re(A v_j) chi_(q_j)=0. Consequently define

\[
b_c=-\frac{\operatorname{Re}(\widehat A v)}
                 {\operatorname{Re}\widehat A}.               \tag{10}
\]

On the distinct-coordinate interior the original equation is exactly
chi_t+b_c dot D_q chi=0. The common minus sign cancels from this
ratio. Formula (10) extends smoothly across the q diagonals using
(8)–(9); it is only an auxiliary extension there, not a division
of the original current at its divisor. It has bounded derivatives
on every fixed smaller box. Permutation equivariance of p, invariance
of widehat A and the transformed matrix M prove equivariance of b_c.

As a sign and background check, at time zero p_t,j=-Re g(iq_j).
For distinct q this follows from the original raw equation and
D_qp(0,q)=0; smoothness proves it at repeated q too. Hence

\[
b_{c,j}(0,q)=-\tan\left(\operatorname{Im}\sum_l\beta(iq_l)\right)
                         \operatorname{Re}g(iq_j).             \tag{11}
\]

The actual background has not disappeared, and (10) is not the
auxiliary connector velocity of C467p.

### Regular physical paths and the exact incidence diagnostic

The terminal face images lie in a compact subbox of (-a/2,a/2)^3
for small common time: their time-zero coordinates have absolute
value at most X+H_*=3/256<a/2, and C467p's ordered-root continuity
is uniform. Boundedness of b_c and the strict box margin, followed
by the cited ODE continuation theorem, give backward solutions
Q(r;t,q) on 0<=r<=t for all these points and their neighborhoods.
Set R_c(t,q)=Q(0;t,q). Smooth dependence and integration of the
bounded velocity give its smoothness and |R_c-q|<=Ct.

These physical paths preserve strict ordering. Indeed equivariance
makes b_(c,j)=b_(c,k) on q_j=q_k. The smooth Hadamard factorization
along that hyperplane (equivalently, the integral of the normal
derivative) gives b_(c,k)-b_(c,j)=(q_k-q_j)d_jk with bounded d_jk.
Thus each gap along a path solves a scalar linear equation and
stays positive, within multiplicative factors exp(+-Ct) of its
terminal gap. This alone does NOT put the path in the evolving
image of the initial-coordinate chamber.

To test that additional condition define, along a physical path,

\[
\alpha(r)=E_r^{-1}(e(Q(r))),\qquad
V(r,Q)=D_r(\alpha)^{-1}
       [\partial_rE_r(\alpha)-J_e(Q)b_c(r,Q)].                 \tag{12}
\]

Here partial_r E holds alpha fixed, and D_r is evaluated at alpha.
With backward elapsed time s=t-r, the exact chain rule is
d alpha/ds=V(r,Q). All quantities exist in the common coefficient
domain even if alpha is not the coefficient vector of three real
roots. This latter reality condition is exactly what must be checked.

For a separated double root use the regular local coefficient chart

\[
e_*(m,k,y)=
(2m+y,\ m^2+2my-k/4,\ (m^2-k/4)y).
\tag{13}
\]

Its roots are m+-sqrt(k)/2 and y when k>=0. At k=0 its Jacobian
determinant, with columns m,k,y, is -(m-y)^2/2, so it is a real
smooth chart near a separated double root even for k of either sign.
The singleton is identified by its fixed separation; equivalently
one can continue that simple root and factor the remaining quadratic,
which makes these local charts agree on overlaps.

Put L(x)=(x^2,-x,1). Differentiating the polynomial at its double
root in chart (13) gives d k/ds=4 L(x)V/(x-y) at k=0.
On the actual lower face, alpha=e(x,x,x+h), so its exact backward
normal coefficient is

\[
\nu(t,x,h)=-\frac4h\,D(t,x,h),\qquad
D(t,x,h)=L(x)D_t(e(x,x,x+h))^{-1}
 [\partial_tE_t(e(x,x,x+h))-J_e(q^+)b_c(t,q^+)].
\tag{14}
\]

The required backward-inward sign is D<0, or equivalently nu>0.
At time zero C467i(13) gives
partial_t E=s(e)+J_e h_+, where s(e)=(0,-6,-2e1) and
h_+(u_j)=Im g(iu_j). At (x,x,y), L(x)J_e=0 and
L(x)s=2(x-y). These are direct polynomial identities, retaining
all background terms. Therefore D(0,x,h)=-2h and nu(0,x,h)=8.

Every factor in D is continuous on the compact set including t=h=0,
using C467p's uniform ordered-root limits. Thus, for some modulus
omega(t) tending to zero,

\[
D(t,x,h)=-2h+\varepsilon(t,x,h),\quad
\sup_{|x|\le X,\,0\le h\le H_*}|\varepsilon(t,x,h)|
 \le\omega(t),\qquad
\nu=8-4\varepsilon/h\quad(h>0).                              \tag{15}
\]

No O(t) rate or divisibility of epsilon by h is asserted. Continuity
does not establish epsilon<2h uniformly for positive h, and proves
neither sign nor nonzero value for D(t,x,0) at positive time.

### Backward confinement for every fixed separation floor

Fix eta>0. Use a compact family of the charts (13) around
|m|<=X, eta<=y-m<=H_*, with slightly enlarged x and separation
margins still strictly inside (-a,a). Near k=0 the singleton stays
strictly above the other roots whenever k>=0 is sufficiently small.
All inverse charts and derivatives have uniform bounds on this
family; those bounds are allowed to depend on eta.

Start a physical path at q^+(t,x,h), with h>=eta. Uniformly over
this family, Q(r) tends to (x,x,x+h) as t decreases to zero, for
all 0<=r<=t: terminal convergence is C467p's root continuity and
the path moves by at most Ct. Also alpha(r) tends uniformly to
e(x,x,x+h). Hence all alpha(r) lie in the above chart neighborhoods
when t<=tau_eta is small enough. This step uses only the already
constructed physical path, not hypothetical confinement of an
initial-root flow.

In these neighborhoods the continuous quantity
D_e k(alpha(r)) V(r,Q(r)) tends uniformly to its value 8 at
r=t=0, k=0. It follows, after another reduction, that

\[
4\le\frac{dk}{ds}\le12,
\qquad 4(t-r)\le k(r)\le12(t-r)\quad(0\le r\le t).
\tag{16}
\]

The same inequalities for the derivative hold for terminal points
from distinct initial triples tending to the face; their k(r) lies
between k(t)+4(t-r) and k(t)+12(t-r). The coefficients remain in
the same neighborhoods by continuity and their strict margins.
For r<t, (16) makes the two initial roots distinct and real, while
the chosen margins keep the singleton above them and all three
inside (-a,a). Thus alpha(r)=e(u(r)) for an ordered distinct real
triple. E_r(alpha(r))=e(Q(r)), so the ordered physical roots of
the actual chamber flow are exactly Q(r), by C467e's agreement and
ordering. This proves actual chamber confinement rather than just
physical q ordering. At r=0, E_0=Id and u(0)=Q(0).

For terminal distinct triples, (2), (10), and the chain rule make
Theta(r,u(r)) constant on 0<r<=t. The initial limit is G(Q(0))
by the permitted continuity of Theta. Let these terminal triples
approach the collision face. Smooth dependence of Q and continuity
of Theta then give (4). No derivative at time zero or on the
collision face was used. At no earlier time did these paths hit a
free lateral face or the other collision face.

### The fixed pair comparison and its exact limitation

Formula (3) is continuous on the entire displayed face box because
q^+ is continuous there and R_c is smooth on its physical box.
At t=0, R_c(0,q)=q, giving the stated initial product. The bounded
gradient of G and the displacement estimate yield uniformly
|T_c-G(q^+)|<=C_f t, including h=0.

C467p(33)–(36) constructs its fixed phi_p with the SAME function
G(Q)=f(Q1)f(Q2)f(Q3), evaluated at its own backward endpoint map.
At s=1 the physical point is exactly q^+, by the unchanged endpoint
map. Its separate bounded-velocity estimate gives
|phi_p(t,x,1,h)-G(q^+)|<=C_f t, including h=0 by its proved
continuity. The triangle inequality proves (5). No equality of the
two graph derivatives, velocities or endpoint maps was used.

The achieved tolerance in (5) is O(t); the matching condition needs
exact equality, while a class obstruction needs a strict discrepancy
at a point where the value is actually forced. Neither follows.
Likewise (15) is an absolute small-error estimate; common-horizon
incidence needs a relative error or another sign argument as h tends
to zero. The ordered physical flow can be regular even when its
inverse initial coefficient path exits the real-root region. No
uniform initial-access theorem or free-side alternative is proved
at that corner. The prior stops1043/1058/1060/1068 are unchanged and
do not settle these missing obligations. Exterior payment, separate
complex derivative products, global assembly, realization, higher
degrees and Xi transfer remain open.

### Independent conceptual audit — 16 November 2026, step1083

This is REPRODUCTION under the invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-16-chamber-incidence-audit-nomination-1081.md`,
separately completed at review1082. Reuse its primary-source coverage
and review1079's characteristic comparison. The audit imports the
already audited C467e coefficient flow, C467p endpoint construction
and C467y fixed lower selection with their original qualifications.
It neither replays the external finite-zero verification nor assumes
the all-degree positivity sought in L030–L032/C032a.

**Common graph and exact sign.** The initial compact coefficient set
for the enlarged q box is strictly inside C467e's convex V_0. The
uniform C1 closeness of E_t to the identity supplies a common inverse
on a neighborhood of this compact set, with time and spatial
derivatives bounded after reducing time. This is more than an inverse
on each simple-root chart. Since Pi_0=0 as a function of e, every
fixed-order spatial derivative of p is O(t). The reconstruction
identity gives p_k-p_j=(q_k-q_j)(-pi_hat_2-q_l pi_hat_3), with the
displayed minus sign. Thus the spatial coefficient is exactly
Delta(q)^2 exp(-H) product_l(i+sigma_l)^2 det(Id-iD_qp).
At t=0 the product of the three squared i factors is -1. The
phase estimate uses
60(3a/4)^2=135/1024<1/4, and hence leaves the strict margin
required for (9). Compactness retains this margin for small time.

At fixed q, Z_t/i=-ip_t and Z_q/i=M. Replacing the jth spatial
column therefore gives A(-iM^{-1}p_t)_j. With dt preceding the
three ordered dq coordinates, wedging dchi with the form gives
Re(A)chi_t-sum_j Re(A v_j)chi_(q_j). This verifies (10), including
the common minus normalization's cancellation. It uses the algebraic
square, not a modulus square. At time zero put A_j^0=-Re g(iq_j)
and Phi=sum_j Im beta(iq_j). Then v_j=-iA_j^0 and
widehat A=-c exp(-iPhi), c>0. Consequently b_(c,j)=tan(Phi)A_j^0,
which is precisely (11). Equivariance follows from conjugating M by
the permutation matrix and permuting p_t; it does not use evenness
of beta or f. Equations (8)–(10) are smooth on an open q box,
so the cited regular ODE theorem applies there.

**Original chamber and separation floor.** A bound for b_c and the
strict distance of the terminal images from the box boundary give
backward existence on [0,t] and |R_c-q|<=Ct. The smooth identity
b_(c,k)-b_(c,j)=(q_k-q_j)d_jk proves physical ordering by its scalar
linear gap equation. This does not assert initial-root reality.
Differentiating alpha(r)=E_r^{-1}(e(Q(r))) gives

    d alpha/dr=(D E_r)^{-1}(J_e b_c-partial_r E_r),

so the backward sign in (12) is correct. In the chart (13), at k=0,
L(m) applied to its m and y columns is zero and its k column is
(m-y)/4. Its determinant is -(m-y)^2/2. This proves
dk/ds=4L(m)V/(m-y) without choosing a square-root derivative at zero.
At time zero L(x)J_e(x,x,y)=0 and
L(x)(0,-6,-2(2x+y))=2(x-y). Thus D=-2h and nu=8 exactly.
Continuity alone yields the absolute remainder in (15), with no
division-uniform estimate as h decreases to zero.

For eta>0 the double-root charts have a common compact margin and
uniform inverse bounds. The constructed Q paths and their inverse
coefficients approach their time-zero double-root data uniformly as
the terminal t tends to zero. The continuous chart normal derivative
therefore stays in [4,12] for the whole backward interval, after a
time reduction depending on eta. Integrating gives (16). For terminal
interior approximants the initial k(t)>0 is added to both bounds.
The local chart margins keep the singleton above the lower two roots
and every initial root inside (-a,a). Hence for r<t the inverse
coefficients represent distinct ordered real roots. C467e's actual
flow agreement and ordering identify their physical roots with Q(r).
This is the needed original-domain argument; merely preserving the
order of Q would not suffice.

Characteristic constancy is used first only for terminal interior
points on positive-time paths. Taking r down to zero uses the stated
continuity of Theta and E_0=Id; taking the terminal point to the face
uses smooth physical-path dependence and continuity of Theta again.
It yields (4) with no time-zero scalar derivative and no equation
postulated on a zero current. At t=0 the identity follows directly
from the initial datum. If eta=H_* the endpoint case follows from
the same slightly enlarged chart family.

**Selected endpoint and limitations.** C467p(2) gives Z=Y^+ at s=1,
and C467y keeps exactly this phi_p. Both backward endpoint maps move
their terminal physical point by at most Ct, and G has a bounded
gradient. Apply these two separate bounds and the triangle inequality;
continuity gives the h=0 endpoint as well. This proves (5) but gives
neither equality nor a strict discrepancy. The two velocities need
not be equal, and none of the argument assumes that they are.

All stated conclusions pass on their stated existential horizons.
C467's separately audited corner calculation limits the use of (3)
as a necessary trace; it does not contradict (4), whose time depends
on eta. No global characteristic confinement, chamber cutoff identity,
incoming-data selection or Xi transfer is supplied. Direct mathematical
inputs remain C467e/i/p/y; no DAG change is needed. This validates an
existing local input, not a mathematical discovery beyond the sources
checked or an RH candidate.

## Mathlib

Full matching coverage has not been checked. The analytic ODE,
inverse-function and chain-rule facts used here are standard named
inputs with the precise Teschl citation above; this is not a claim
that Mathlib contains the actual chamber specialization. No absence
or novelty claim is inferred from unchecked coverage.
