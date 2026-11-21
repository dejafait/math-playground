# C468g — The first curved triangle on the common physical graph

## Hypotheses

Use C467k(3)–(6)/(9)–(10)/audit1033's actual ordered triple roots
q_1(t,x)<q_2(t,x)<q_3(t,x) from initial data (x,x,x). Use precisely
C468f(10)–(15)/audit1098's physical graph W(t,q)=p_c(t,q)+iq,
regular graph quantities widehat a and upsilon, and scalar chi(t,q).
These are the existing objects, with one common horizon reduced below.
Retain

\[
n=3,\ R=1/4,\ a_0=1/16,\ T_0=1/1920,\ X=1/256,
\quad b_*=1/4096,\ H_*=1/128,
\]
\[
\beta(z)=B(1+z)-B(1)-B'(1)z,\quad
H(z)=H_0+\sum_{j=1}^3\beta(z_j),\quad
H_0=3[B(1)-B'(1)]\in\mathbb R,
\]
\[
\Delta(z)=\prod_{j<k}(z_k-z_j),\quad
F(z)=\Delta(z)^2e^{-H(z)},\quad
\Omega=F(z)\bigwedge_{j=1}^3(dz_j/i).
\tag{1}
\]

B is the actual conjugation-normalized logarithm with
exp B(w)=xi(1/2+sqrt(w))/xi(1/2) on |w-1|<R; beta(0)=beta'(0)=0
and |beta''|<40 there. The finite-zero/product qualifications through
L018/L021/L024/C466a and the unreplayed external low-zero evidence are
retained, not strengthened. Neither RH nor an all-degree sign or density
realization is a premise.

Let f be any fixed real smooth function with 0<=f<=1, equal to one
on [-b_*,b_*], supported in (-2b_*,2b_*). Write G(q)=product_j f(q_j).
Neither f nor beta is assumed even. C468f's fixed scalar is
chi(t,q)=G(R_c(t,q)), with its already constructed regular physical
backward endpoint map R_c. No new scalar selection is made here.

Set c=(q_1+q_2+q_3)/3 and define only the first nominated triangle:

\[
Q(t,x,r,\lambda)=(1-r)c\mathbf1
 +r\big((1-\lambda)q_1+\lambda q_2,
        (1-\lambda)q_2+\lambda q_1,q_3\big),
\]
\[
Z=W(t,Q),\qquad \psi=\chi(t,Q),\qquad
K=[0,\tau]\times[-X,X]\times[0,1]\times[0,1].
\tag{2}
\]

Its orientation is dt wedge dx wedge dr wedge dlambda. Time is raw
physical time. The original algebraic-square form and its divisor are
unchanged; the common minus sign multiplies the chamber, connector and
triangle forms. No affine real-map minor or old triangle scalar is used.

## Conclusion

For one existential 0<tau<=T0 common with C468f, (2) remains in
|Z_j|<R. The scalar is real, takes values in [0,1], is continuous
on K and smooth for t>0, including its parameter faces. It satisfies

\[
\psi(0,x,r,\lambda)=f(x)^3,\qquad
d\psi\wedge\operatorname{Re}(-Z^*\Omega)=0.
\tag{3}
\]

The second identity holds on positive-time charts without division by
any vanishing coefficient. At r=1 there is exact map and scalar matching
to C468f's h=0 face with s=1-2lambda. The two induced faces have opposite
orientations, including the full change-of-variable factor, so their
weighted restricted forms cancel for tests with matching restrictions.

Write the original complex pullback as

\[
\Psi=Z^*\Omega=A\,dx\wedge dr\wedge d\lambda
 +B_\triangle\,dt\wedge dx\wedge d\lambda
 +U_\triangle\,dt\wedge dr\wedge d\lambda
 +V_\triangle\,dt\wedge dx\wedge dr.
\tag{4}
\]

Then Re(-A)>=|A|/2. For t>0, A vanishes exactly at r=0 or
lambda=1/2. Put rho=sqrt(t), s=1-2lambda. Constants are uniform
on K for t>0 and may depend on the fixed background; C_f may also
depend on f. The four complex coefficients obey

\[
|A|\le C s^2 r^7\rho^8,
\quad |B_\triangle|\le C s^2(r^7\rho^7+r^8\rho^6),
\]
\[
|U_\triangle|\le C s^2(r^7\rho^8+r^8\rho^7),
\quad |V_\triangle|\le C s^2(r^6\rho^7+r^7\rho^6).
\tag{5}
\]

Each of the four quantities

\[
|A\psi_t|,\quad |B_\triangle\psi_r|,\quad
|U_\triangle\psi_x|,\quad |V_\triangle\psi_\lambda|
\tag{6}
\]

is at most C_f s^2(r^7 rho^8+r^8 rho^7), separately and before
real adjoint cancellation. All eight terms have joint L1 majorants
through t=r=0. The spatial absolute mass at time t is O(t^4).
The initial-time face and inner radial face have zero limiting flux.
All other faces have their actual restrictions as joint-cutoff limits;
they are retained unless matched as just stated.

This local result of attempt1100 is **validated under its stated qualifications
by independent conceptual audit1102 below**. It supplies a replacement
for the first lower-interface triangle, not a six-triangle
assembly, upper-pair construction, payment of outer faces, chamber/global
identity, Xi realization or complete RH argument. C467q's old affine
vertex stop and C468e's affine glancing stop remain intact. No certified
originality beyond the sources checked is claimed.

## Proof

### Covered tools and the common domain

The invocation-start assessment is
`drafts/literature/2026-11-16-common-graph-first-triangle-nomination-1098.md`,
separately approved as EXPLORE in review1099. Reuse its primary coverage
and local comparisons. The new calculation concerns only (2), not a
general ODE, pullback or convergence theorem.

For the existing regular physical flow, C468f uses Gerald Teschl,
*Ordinary Differential Equations and Dynamical Systems*, April2012
author preliminary version,
[Theorems2.5/2.10–2.11 pp40–48; Lemma2.14/Corollary2.15 pp52–53;
Theorems3.9/3.12 pp81–84; Theorem6.1 pp189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
We import the constructed W, chi and bounds from C468f; no singular
initial-root ODE is solved here. For smooth composition of forms use
Victor Guillemin and Shlomo Sternberg, *Semi-classical analysis*,
13January2010 author version,
[sections13.5–13.6 pp441–442](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf).
Pullback preserves wedges, commutes with d and respects composition;
no immersion is required. Apply componentwise to complex forms on
positive-time smooth charts. The cutoff theorems and their precise
hypotheses are applied below, after the estimates.

C467k's proved root scaling is

\[
q_j=x+\rho\eta_j(\rho,x),\qquad
(\eta_1,\eta_2,\eta_3)(0,x)=(-\sqrt6,0,\sqrt6).
\tag{7}
\]

The eta functions extend smoothly to a neighborhood of the compact
rescaled box, with bounded derivatives there. Their actual-root
identification follows from the simple-root charts in C467k, including
the lower-face limit as h tends to zero. The center c=E_1(t,x)/3
is smooth in physical time, with c(0,x)=x, c_x(0,x)=1 and bounded
c_t. Thus, after a single uniform time reduction, c_x>=1/2.
This uses the smooth coefficient solution, not differentiation of an
uncontrolled time-zero root remainder.

C468f already places these actual roots, as the h=0 collar roots,
in [-a0/3,a0/3]^3. Every component of Q is a convex combination
of the roots, including the mean c, so the entire Q image lies in
the same box. C468f constructs W, chi on a neighborhood of that box,
with bounded derivatives and backward trajectories in the larger
physical box. Its bound |p_j|<=a0/2 consequently gives
|W_j(t,Q)|<=a0 sqrt(13)/6<R. Choose the minimum of these horizons
and C467k's, and reduce it finitely further as used below. This is
one horizon for the full parameter box, not a family indexed by r
or lambda. No confinement inside the evolving chamber is asserted.

Continuity of the roots and chi proves continuity of psi on K.
At t=0, Q=x*1 and chi(0,Q)=G(Q)=f(x)^3. At r=0, Q=c*1
is independent of lambda, so the scalar has an actual common vertex
value chi(t,c*1). This value follows from this map; no vertex law of
the stopped affine triangle is imported. At positive t all root,
graph and scalar functions are smooth on neighborhoods of the faces.

### Exact forms, equation and outer matching

Use C468f's graph notation, with the following quantities evaluated
at (t,Q) whenever composed:

\[
M=\mathrm{Id}-iD_qp_c,\quad
\upsilon=-iM^{-1}(p_c)_t,\quad
a(t,q)=\Delta(q)^2\widehat a(t,q).
\tag{8}
\]

Here a is the full physical spatial coefficient. The matrix M is
invertible, widehat a and upsilon are smooth and bounded, and
Re(-widehat a)>=|widehat a|/2>0 on the common physical box.
The exact complex factorization follows from C468f's graph formula,
not replacement of Delta(Z)^2 by a modulus square. In particular,
W_q/i=M and W_t/i=M upsilon. Factoring M from the three columns
gives all four new coefficients:

\[
A=a(t,Q)\det(Q_x,Q_r,Q_\lambda),
\quad B_\triangle=a(t,Q)\det(Q_t+\upsilon,Q_x,Q_\lambda),
\]
\[
U_\triangle=a(t,Q)\det(Q_t+\upsilon,Q_r,Q_\lambda),
\quad V_\triangle=a(t,Q)\det(Q_t+\upsilon,Q_x,Q_r).
\tag{9}
\]

These are complex determinants, with the orders in (4); no inverse
of the parameter Jacobian is used. C468f(14) proves the undivided
identity dchi wedge Re(-W^*Omega)=0 even on physical diagonals.
Pulling it back by (t,x,r,lambda)->(t,Q) proves (3), including at
r=0 and lambda=1/2 for t>0. Explicitly its coordinate form is

\[
\operatorname{Re}(A)\psi_t-
\operatorname{Re}(U_\triangle)\psi_x+
\operatorname{Re}(B_\triangle)\psi_r-
\operatorname{Re}(V_\triangle)\psi_\lambda=0.
\tag{10}
\]

The common minus sign multiplies the whole equation by -1.

At r=1 set s=1-2lambda. Then directly from the two definitions,

\[
Q(t,x,1,\lambda)=Q_p(t,x,s,0),\quad
Z(t,x,1,\lambda)=Z_{\rm new}(t,x,s,0),\quad
\psi(t,x,1,\lambda)=\phi(t,x,s,0).
\tag{11}
\]

C467k's simple-root limit and C468f's smooth positive-time faces
identify the roots on both sides. Equality holds with all tangential
derivatives for t>0 and continuously at t=0. For orientation,
C468f's dt dx ds dh gives +dt dx ds at its lower h face.
The triangle's upper r face has +dt dx dlambda. The edge change
ds=-2 dlambda reverses orientation. If V_p denotes C468f(6)'s
coefficient of dt dx ds, (9) yields the exact restriction

\[
B_\triangle(t,x,1,\lambda)=-2V_p(t,x,1-2\lambda,0).
\tag{12}
\]

For matching test restrictions the pair face integral over -1<=s<=1
is therefore the negative of the triangle face integral over
0<=lambda<=1. This proves cancellation of the full complex weighted
forms, as well as their common-minus real parts; no leading-order
matching suffices in its place. It makes no claim about other faces.

### Signed spatial determinant and its zeros

Put eta_bar=(eta_1+eta_2+eta_3)/3 and

\[
u(\rho,x,\lambda)=
\big((1-\lambda)\eta_1+\lambda\eta_2,
     (1-\lambda)\eta_2+\lambda\eta_1,\eta_3\big)
 -\overline\eta\mathbf1.
\]

Then Q=c*1+r rho u. All u, u_x and u_lambda lie in the real
two-dimensional zero-sum plane. Consequently their three-column
determinant is zero, and exactly

\[
J:=\det(Q_x,Q_r,Q_\lambda)
 =r\rho^2c_xD,\qquad D=\det(\mathbf1,u,u_\lambda).
\tag{13}
\]

For t>0 write delta=q_2-q_1>0. Since
u_lambda=(delta/rho,-delta/rho,0) and sum u_j=0, direct expansion
gives D=3delta(q_3-c)/rho^2>0. Equivalently, its smooth extension
has value 18 at rho=0, since
u(0)=sqrt(6)(-1+lambda,-lambda,1).
Thus J>0 for t,r>0, and J=0 at r=0, with |J|<=C r rho^2.

All differences in Q are r times their differences on the outer
edge. Their exact Vandermonde is

\[
\Delta(Q)=r^3\delta s
 (q_3-q_1-\lambda\delta)(q_3-q_2+\lambda\delta).
\tag{14}
\]

Both last factors are positive: each is at least q3-q2>0.
By (7), all three unfactored gaps are bounded above by C rho,
and delta/rho and (q3-q2)/rho are bounded below by a positive
constant on a reduced horizon. Hence

\[
|a(t,Q)|\le C r^6\rho^6s^2.
\tag{15}
\]

For t>0, Delta(Q)^2 vanishes precisely at r=0 or s=0.
Equations (9),(13) give A=Delta(Q)^2 widehat a J. The two real
factors are nonnegative, and their only zeros are those just listed.
The existing sector and nonvanishing of widehat a prove the asserted
sector and exact zero set of A. This is a sign calculation for the
full original complex coefficient, including its algebraic square.

### Four raw-time coefficients and four separate products

Bounded derivatives of the smooth rescaled u and the physical center
give, for rho>0,

\[
Q_t=c_t\mathbf1+\frac r{2\rho}(u+\rho u_\rho),\quad
Q_x=c_x\mathbf1+r\rho u_x,\quad
Q_r=\rho u,\quad Q_\lambda=r\rho u_\lambda.
\tag{16}
\]

In particular the respective bounds are C(1+r/rho), C, C rho
and C r rho, after taking rho<=1. The same bound C(1+r/rho)
holds for Q_t+upsilon. This is differentiation in raw time t;
rho is used only to prove the estimates and is not a new time
parameter for the form or its integral.

Use (15) and the determinant bound by the product of column norms
in each identity (9). The spatial minor is at most C r rho^2,
either by (13) or these column bounds. The B, U and V minors are
respectively at most

\[
C(r\rho+r^2),\qquad
C(r\rho^2+r^2\rho),\qquad C(\rho+r).
\tag{17}
\]

Multiplication by (15) proves all four bounds (5). These estimates
are deliberately coarse; no zero-sum cancellation of a time column,
old affine time minor or divided current is necessary.

C468f(12) gives |chi_t|+|D_q chi|<=C_f in physical coordinates.
The actual composed scalar therefore satisfies separately

\[
|\psi_t|\le C_f(1+r/\rho),\quad |\psi_x|\le C_f,
\quad |\psi_r|\le C_f\rho,\quad
|\psi_\lambda|\le C_f r\rho.
\tag{18}
\]

Multiplying the four bounds (5) by their respective bounds in (18)
gives, for each of (6), C_f s^2(r^7 rho^8+r^8 rho^7).
In the first product this is r7 rho8*(1+r/rho); in the second
it is (r7 rho7+r8 rho6)*rho; the third is the displayed U bound;
in the fourth it is (r6 rho7+r7 rho6)*r rho. Thus every product
has its own bound before (10) is applied. No derivative of psi at
t=0 is asserted or used.

For a simple joint majorant, (5) sums to at most C t^3, and (6)
sums to at most C_f t^(7/2), because r<=1 and rho<=1. Both
are integrable over K in dt dx dr dlambda. In particular their
integrals over t<epsilon or r<eta tend to zero jointly, with no
condition on the relative rates. The spatial slice integral of |A|
is at most C' t^4. Bounds are for the full coefficients, not merely
for previews, normalized densities or sums after cancellation.

### Actual faces and the cutoff identity

Let zeta be a fixed real smooth test on a neighborhood of K; bounded
first derivatives suffice for the following estimates. On every
positive-time slab all restricted maps and scalars are smooth up to
r=0 and the x,lambda faces. They have their actual pointwise face
limits. The estimates below independently control these face integrals.

On t=epsilon the spatial coefficient is at most C epsilon^4
uniformly in the full spatial box. Its face integral, with psi and
zeta, tends to zero uniformly in any simultaneous lower r cutoff.
The upper-time face is smooth in r; its omitted strip r<eta tends
to zero (also directly by the r^7 bound).

On r=eta the coefficient is B_triangle, bounded by
C(eta^7 t^(7/2)+eta^8 t^3). Its entire face integral in dt dx dlambda
is O(eta^7), uniformly in any lower time cutoff. Thus its limiting
flux is zero, agreeing with the actual restriction at r=0: there
Q_lambda=0 and the physical point is on the divisor. On r=1 the
coefficient B_triangle has the uniform integrable time majorant
C(t^(7/2)+t^3). Its actual trace is (12), so the outer matching
also holds for the limiting weighted integrals. The scalar is bounded
by one throughout.

On each x face, the coefficient U_triangle is bounded by
C r^7 t^(7/2). On each angular face, V_triangle is bounded by
C r^6 t^3. These estimates follow from (5) with rho<=1, absorbing
a factor two. They are integrable on the corresponding three-dimensional
faces, independent of epsilon,eta, and remain valid uniformly if
the faces are approached from inside the parameter box. Thus each
face has its actual restriction as its limit. To see joint cutoff
independence explicitly, the tails t<delta are uniformly small by
these displayed powers; the r<eta strips are uniformly small by
their r powers. On the remaining compact positive-time set ordinary
smooth convergence applies. The same reasoning applies to r=1
and the fixed upper-time face. This proves face convergence without
deducing it from bulk L1 or assuming a corner trace theorem.

For completeness, on K_(epsilon,eta)=[epsilon,tau] times [-X,X]
times [eta,1] times [0,1], Omega is a closed holomorphic three-form
on the verified polydisc, with zeros rather than poles on the divisor.
Hence dPsi=0. Smooth extensions and a compact cutoff equal to one
near this box meet the hypotheses of Brian Conrad,
[*Stokes' theorem with corners*, Theorem1.1 and coordinate proof,
pp1–3](https://math.stanford.edu/~conrad/diffgeomPage/handouts/stokescorners.pdf).
Applied to zeta psi Psi, componentwise, it gives

\[
\int_{\partial K_{\epsilon,\eta}}\zeta\psi\Psi
=\int_{K_{\epsilon,\eta}}
\big[A\partial_t(\zeta\psi)-U_\triangle\partial_x(\zeta\psi)
 +B_\triangle\partial_r(\zeta\psi)
 -V_\triangle\partial_\lambda(\zeta\psi)\big]
\,dt\,dx\,dr\,d\lambda.
\tag{19}
\]

The upper/lower t, x, r, lambda faces respectively carry signs
(+,-), (-,+), (+,-), (-,+) in their displayed coordinate orders
dx dr dlambda, dt dr dlambda, dt dx dlambda, dt dx dr.
All these terms are retained. Bounds (5) handle each term containing
a test derivative, and (6) each containing a scalar derivative.
The separate face estimates above handle the left side. John K.
Hunter, *Measure Theory*,
[Chapter4 Theorem4.24 and section4.6, pp49–50](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf),
applies to the measurable pointwise limits with the stated integrable,
cutoff-independent dominators, using real and imaginary parts.
Consequently (19) passes to every simultaneous epsilon,eta->0.
There is no extra independent corner term. Taking the common-minus
real part then uses (10) to remove only the scalar-derivative sum;
its four absolute integrability checks have already been supplied.

This completes the fixed first-triangle test under the inherited
qualifications. Other angular/radial matches, upper connectors, all
unmatched outer faces, a chamber/global identity and actual-Xi transfer
remain unresolved. No result about those independent obligations follows
from this local construction or its source gate.

### Independent conceptual audit — 16 November 2026, step1102

This is RESEARCH / REPRODUCTION under the invocation-start SPECIALIZE
assessment
`drafts/literature/2026-11-16-common-graph-first-triangle-audit-nomination-1100.md`,
approved separately in review1101. Reuse its inspected primary coverage
and the precise Teschl, Guillemin–Sternberg, Conrad and Hunter citations
above. The work here checks their application to this fixed map, not a
general theorem or a new construction. The direct mathematical inputs
remain C467k(3)–(6)/(9)–(10)/audit1033 and C468f(10)–(15)/audit1098.
Their C467e/z graph and C467l/p ordered-limit qualifications are retained.
In particular, this audit does not replay L018/L021/L024/C466a's external
low-zero/product evidence or supply an actual-Xi realization.

**One horizon, actual roots and scalar.** C467k's smooth rescaled
polynomial at rho=0 is y(y^2-6), with three simple roots. Its audited
real implicit-function charts give (7) and bounded rho and x derivatives
on a neighborhood of the compact x interval. They identify the ordered
triple trace with the h=0 limit of the same coefficient flow used by
C468f. Also sum q_j=E_1(t,x), so c=E_1/3 has bounded physical-time
derivatives and c_x(0,x)=1. This is essential: differentiability of c
at t=0 does not come from formally differentiating a square-root error.
Compactness permits one reduction giving c_x>=1/2.

C468f/audit1098 places the collar roots, including h=0, in the compact
box [-a0/3,a0/3]^3. The mean and the two-entry interpolation in (2)
are convex combinations of those roots; the whole Q image lies there.
The same audit constructs W, chi and their bounded derivatives on an
open neighborhood of that box, with backward endpoints in the larger
box. Its graph factor is nonzero and has the required sector throughout
the box, including physical diagonals. Taking the minimum of these
horizons and C467k's, with finitely many further compact reductions,
works simultaneously for every x,r,lambda. Since |p_j|<=a0/2,
|W_j|<=a0 sqrt(13)/6<R. No chamber-image confinement is used.

Thus psi=chi(t,Q) is the existing [0,1]-valued scalar, continuous on
K and smooth on neighborhoods of all positive-time parameter faces.
At t=0 every Q_j=x and chi(0,Q)=G(Q)=f(x)^3. At r=0 its value is
chi(t,c*1), independent of lambda. No symmetry under x->-x, time-zero
derivative of psi, old affine scalar or affine vertex equation enters.

**Exact complex columns, equation and orientation.** The three columns
of the differentiated map, after division by i, are M Q_v for a spatial
parameter v and M(Q_t+upsilon) for t. Consequently their determinants
are det M times the ordered columns in (9), with a=F(W)det M exactly.
C468f's pair-difference factorization gives a=Delta(Q)^2 widehat a;
there is no modulus-square replacement. This verifies all four complex
coefficients even at a zero of the real parameter Jacobian.

The physical identity C468f(14) holds before any division by Delta.
Smooth composition therefore gives (3) on every positive-time chart.
In dt,dx,dr,dlambda order, wedging dpsi into the four terms of (4)
gives signs +,+,-,- in their displayed A,B,U,V order, namely exactly
A psi_t-U psi_x+B psi_r-V psi_lambda in coordinate order. Taking
real parts gives (10), with the common minus sign multiplying all terms.

At r=1, write m=(q1+q2)/2 and delta=q2-q1. Then
m-s delta/2=q1+lambda delta and m+s delta/2=q2-lambda delta
for s=1-2lambda; the singleton is q3 on both sides. Ordered-root
identification gives equality of the actual maps and all tangential
positive-time derivatives. The scalar is the same chi evaluated there.
The outward-normal-first convention gives +dt dx ds on the pair's
lower h face, since contraction with -partial_h has that sign.
It gives +dt dx dlambda on the triangle's upper r face. The edge
map has ds=-2 dlambda, so its degree is negative and
Q_lambda=-2(Q_p)_s on that face. Formula (9) therefore gives
B_triangle=-2V_p, including the sign and full factor in (12).
For any matching test restrictions, direct substitution gives

    integral_0^1 zeta psi B_triangle dlambda
      = - integral_-1^1 zeta_pair phi V_p ds.

This verifies cancellation of the weighted complex restrictions, not
only their images or real spatial densities. The common minus sign
preserves cancellation.

**Spatial sign and exact zeros.** Differentiation in x keeps physical
time, hence rho, fixed. For Q=c*1+r*rho*u, its x column is
c_x*1+r*rho*u_x. All of u_x,u,u_lambda lie in the zero-sum plane,
so det(u_x,u,u_lambda)=0. This proves the exact Jacobian (13).
Writing d=delta/rho and k=(q3-c)/rho, one has u_lambda=(d,-d,0)
and u1+u2=-k. Expansion gives

    det(1,u,u_lambda)=d(2k-u1-u2)=3dk,
    J=3r c_x delta(q3-c).

Since q3 is strictly the largest root, q3-c>0. Both scaled factors
extend smoothly to rho=0 with limit sqrt(6), so D tends to 18 and
J is positive for t,r>0, with |J|<=C r rho^2. There is no missing
x-derivative term and no additional angular zero in this Jacobian.

The three differences in Q are exactly r delta s,
r(q3-q1-lambda delta), and r(q3-q2+lambda delta). Each of the last
two parentheses is at least q3-q2>0. Their scaled sizes are uniformly
bounded by (7), and delta/rho and (q3-q2)/rho stay positive on the
common horizon. Thus (14)–(15) hold with a genuine factor s^2.
Since A=Delta(Q)^2 J widehat a, its multiplier of widehat a is
real nonnegative. The inherited nonzero graph factor proves
Re(-A)>=|A|/2 and the exact positive-time zero set r=0 or s=0.

**Raw-time bounds and separate products.** The physical-time derivative
of rho is 1/(2rho). Bounded u,u_rho,u_x,u_lambda and c_t,c_x
therefore give exactly (16), with column bounds

    Q_t+upsilon: C(1+r/rho),   Q_x: C,
    Q_r: C rho,               Q_lambda: C r rho.

The complex determinant inequality applies also to the upsilon column.
Multiplying its four column-product bounds by C s^2 r^6 rho^6
gives, independently,

    A: C s^2 r^7 rho^8,
    B: C s^2 (r^7 rho^7+r^8 rho^6),
    U: C s^2 (r^7 rho^8+r^8 rho^7),
    V: C s^2 (r^6 rho^7+r^7 rho^6).

For A the exact real Jacobian supplies the same bound. For psi the
chain rule includes the separate physical chi_t term; the four
derivatives in t,x,r,lambda are bounded by
C_f(1+r/rho), C_f, C_f rho, C_f r rho. Hence each product in (6)
is bounded by C_f s^2(r^7 rho^8+r^8 rho^7), respectively by
multiplying A by 1+r/rho, B by rho, U by 1, and V by r rho.
No real cancellation has been used. For r,rho<=1, all four
coefficients have joint dominator C t^3 and all four products have
joint dominator C_f t^(7/2). These are integrable in the original
dt dx dr dlambda measure. In particular the spatial slice mass is
O(t^4); changing the time variable in the form is unnecessary.

**Each actual face and arbitrary cutoff rates.** Fix a bounded smooth
test. Multiplication by psi, whose modulus is at most one, preserves
the following bounds. The t=epsilon face uses A and has total mass
O(epsilon^4), independently of the lower radial cutoff. The upper
time face is smooth, and its omitted r<eta strip is O(eta^8).
The entire r=eta face uses B and is bounded in absolute integral by

    C[eta^7 tau^(9/2)+eta^8 tau^4],

uniformly in the lower time cutoff. It tends to zero, agreeing with
the actual r=0 restriction Q_lambda=0. The r=1 face uses its actual
coefficient (12), dominated by C(t^(7/2)+t^3); its time tail tends
to zero. C468f/audit1098 independently supplies the h->0 pair-face
limit with the same trace, so cancellation is valid even when the
two pieces take unrelated cutoffs.

On either x face, |U|<=C r^7 t^(7/2); on either angular face,
|V|<=C r^6 t^3. The omitted time tails are respectively
O(epsilon^(9/2)) and O(epsilon^4); the omitted radial strips are
respectively O(eta^8) and O(eta^7). These dominators are uniform on
nearby faces as well. On the remaining compact positive-time slab,
smoothness gives convergence to the actual restrictions. This checks
each face separately without extracting a face theorem from bulk L1,
and it gives the same limit along every joint cutoff sequence.

Omega is closed on the verified polydisc: its holomorphic coefficient
multiplies a top holomorphic degree form. Its divisor is a zero set,
not a pole. On each positive-time cutoff box the maps extend smoothly
to a neighborhood, so a compactly supported extension equal to the
integrand near that box meets Conrad's hypotheses. The induced upper
face signs for t,x,r,lambda are +,-,+,-, with opposite lower signs.
Direct exterior differentiation therefore reproduces every term and
sign in (19). Its test-derivative terms use (5); its four scalar-
derivative terms use (6). Hunter's dominated convergence applies to
real and imaginary parts with these cutoff-independent majorants and
the separately checked face limits. No corner contribution is missing.

The real adjoint reduction is for real tests zeta, now made explicit
above: Re(-zeta S)=zeta Re(-S) for the scalar-derivative sum S, and
(10) sets this to zero. The unreduced complex Stokes identity also
holds for complex tests, but one may not use (10) to cancel
Re(-zeta S) for an arbitrary complex zeta. A complex test of the real
form is instead handled by applying the real identity separately to
its real and imaginary parts. This clarification does not assume a
complex adjoint equation or strengthen the scalar construction.

All stated local claims pass with this explicit test convention and
the inherited qualifications. This validates the previously unaudited
first interface; it does not introduce a new mathematical construction
or certify novelty. The horizon is still existential. The other five
triangles, upper connectors, unmatched outer faces, chamber/global
assembly and actual-Xi all-degree positivity remain unpaid. Affine
stops1051/1091/1092 retain their scopes. No mathematical script or
numerical certificate was used or needed for this exact audit.

## Mathlib

Full matching Mathlib coverage for this curved actual-root triangle and
its weighted joint-cutoff statement is unchecked. The named ODE,
pullback, Stokes and dominated-convergence inputs are cited above;
supporting formalizations would not alone verify this specialization.
Audit1102 is an informal mathematical check, not a Lean verification
or evidence that a matching Mathlib theorem is absent.
