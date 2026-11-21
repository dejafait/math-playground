# Lemma 866: arbitrary fixed even rank-one contacts force crossing fibers

## Hypotheses

Use the actual entire G and positive R,C of L847, with exactly

\[
 F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2}.
\]

Conditionally fix distinct nonzero zeros zeta,eta of G of respective
fixed finite even multiplicities m,n>=2. No actual multiple-zero pair
is asserted. Choose real argument lifts
p=(p1,p2)=(arg zeta,arg eta). Let u=(u1,u2) be real C2 on an open
angular neighborhood of p, and set

\[
 \Phi_j(\theta)=R\exp(u_j(\theta)+i\theta_j),\qquad
 \Phi(p)=(\zeta,\eta),\qquad
 J=\det(I-iDu),\qquad q=F(\Phi)J.
\]

Assume q is real nonnegative throughout this neighborhood, J(p)!=0,
and both real-linear maps D Phi1(p), D Phi2(p) have real rank one.
Use the original orientation dtheta1 wedge dtheta2. Do not assume
constant rank nearby, nondegenerate scalar minima, isolated contacts,
analytic u, exchange symmetry, or a periodic or global extension.

## Conclusion

For some epsilon>0, in coordinates x=theta1-p1, y=theta2-p2 on
U={|x|,|y|<epsilon}, the entire local contact sets are

\[
 \begin{split}
 \{G(\Phi_1)=0\}\cap U&=\{x=0\}\cap U,\\
 \{G(\Phi_2)=0\}\cap U&=\{y=0\}\cap U.                 \tag{1}
 \end{split}
\]

Equivalently, throughout these fibers,
u1(p1,p2+y)=log(|zeta|/R) and
u2(p1+x,p2)=log(|eta|/R). The full density vanishes exactly on
their union and is strictly positive elsewhere in U, conditionally
on the hypotheses. A finite ENTIRE G-contact census therefore cannot
contain this rank-one/rank-one branch of any fixed even orders.
The neighborhood may depend on the orders and on the given germ;
no estimate uniform in m,n or u is asserted.

This is a conditional extension of L865's two-double conclusion. The
independent conceptual audit of 6 November 2026 below accepted this
exact conditional result with its original normalization. The subsequent
direct normalization below was independently accepted in the separate
composition audit recorded at the end of the proof. It constructs no germ or actual zero configuration,
excludes neither rank-two nor
J(p)=0 contacts, and does not settle global extension or actual-Xi
all-degree mixed positivity. The original fiber proof's POTENTIALLY_NEW
classification means only that the recorded bounded search did not identify a matching
theorem, not that originality has been certified.

## Proof

### Source scope and the precise specialization

The original fiber proof uses the EXPLORE assessment
`drafts/literature/2026-11-06-all-even-rank-one-contact-fibers.md`.
L847 supplies the exact density. The rank-one tangent and strictly
positive scalar are now obtained directly below. The original proof
used L864 for these elementary facts; repeating only their short
justification is necessary to let L864 subsequently use this fiber
theorem without a circular argument. No part of L864's local rank
classification or global balance is used in the present proof.
L865 is a comparison, not a required input: its squared-product
argument alone does not handle all higher even orders.
The direct normalization rewrite is part of the subsequent SPECIALIZE
application covered before invocation by
`drafts/literature/2026-11-06-finite-census-all-label-balance.md`.
It is REPRODUCTION of the already used elementary normalization,
not a second fiber theorem or a new general factorization result.

Import Jiri Lebl, *Guide to Cultivating Complex Analysis*, v1.10,
5 November 2026, [Theorem 2.4.7 and the finite-zero factorization
proof, pp49–50](https://www.jirka.org/ca/ca.pdf#page=49).
G is entire and G(0)>0 by L847, so is nonzero; the two exact orders
are explicit hypotheses. Thus the theorem supplies holomorphic units
g1,g2 on neighborhoods of zero with

\[
 G(\zeta+w)=w^m g_1(w),\quad G(\eta+v)=v^n g_2(v),\qquad
 g_1(0)=G^{(m)}(\zeta)/m!\ne0,\quad
 g_2(0)=G^{(n)}(\eta)/n!\ne0.
\]

For first-order differentiation and the real intermediate value
theorem use Lebl, *Basic Analysis I*, v6.3, 15 May 2026,
[Definition 4.1.1, p155](https://www.jirka.org/ra/realanal.pdf#page=155)
and [Theorem 3.3.8, pp132–134](https://www.jirka.org/ra/html/sec_minmaxint.html).
The reused assessment inspected both endpoint-order cases. Below the
real functions are explicit continuous projections of f or g on
compact signed-parameter segments inside the domain. No theorem is
applied to a discontinuous argument at a zero.

These standard inputs are imported rather than reproved. The new local
work is the full-coefficient, uniform-segment specialization and the
angular conclusion. The assessed Hatcher path-lifting tool is not
needed: a tilted real line and the real intermediate value theorem
suffice. No square root, logarithm, continuous phase lift, inverse
theorem or higher-order Taylor theorem for q is used.

### Full coefficient and normalized first-order maps

Translate p to (0,0) without changing orientation, and put
w1(x,y)=Phi1(p+(x,y))-zeta and w2(x,y)=Phi2(p+(x,y))-eta.
Shrink to an open angular rectangle with widths less than pi. By
continuity, require g1(w1), g2(w2), Phi1, Phi2, Phi1-Phi2 and J
all to be nonzero there. This uses the distinct nonzero centers,
nonzero units and J(p)!=0. In particular each coordinate image has
no G-zero label other than its specified center. L847 gives exactly

\[
 \begin{split}
 q&=K w_1^m w_2^n,\\
 K&=-C\frac{g_1(w_1)g_2(w_2)(\Phi_1-\Phi_2)^2}
                 {\Phi_1^2\Phi_2^2}J,\qquad K(0)=K_0\ne0. \tag{2}
 \end{split}
\]

Here K is continuous (indeed C1). All factors of the actual density,
including the minus sign, denominator, squared difference and complex
Jacobian, remain in (2). No contact factor has been divided out.

Write Du(p)=[[a,b],[c,d]]. Direct differentiation gives

\[
 Dw_1(0)(x,y)=\zeta((a+i)x+by),\qquad
 Dw_2(0)(x,y)=\eta(cx+(d+i)y).
\]

In the original real angular basis, multiplication by zeta or eta
has positive determinant |zeta|^2 or |eta|^2. The remaining real
matrices are [[a,b],[1,0]] and [[c,d],[0,1]], respectively, so
their determinants are -|zeta|^2 b and |eta|^2 c. Both differentials
have rank one by hypothesis, forcing b=c=0. Define the nonzero constants

\[
 \alpha=\zeta(a+i),\qquad \beta=\eta(d+i).
\]

Then D w1(0)(x,y)=alpha x and D w2(0)(x,y)=beta y. The nonzero
own-angle imaginary coefficients make alpha and beta nonzero for
real a,d. Along (x,y)=(t,t), with t>0 tending to zero, first-order
differentiability and continuity of K in (2) give

\[
 \frac{q(t,t)}{t^{m+n}}
 =K(t,t)\left(\frac{w_1(t,t)}t\right)^m
          \left(\frac{w_2(t,t)}t\right)^n
 \longrightarrow K_0\alpha^m\beta^n.
\]

Every left side is real nonnegative. Its limit is nonzero because
K0, alpha and beta are nonzero. Consequently

\[
 B_0:=K_0\alpha^m\beta^n\in\mathbb R_{>0}.              \tag{3}
\]

Set f=w1/alpha, g=w2/beta, and B=K alpha^m beta^n. Thus

\[
 q=B f^m g^n,\quad B(0)=B_0>0,\quad
 f(0)=g(0)=0,\quad Df(0)(x,y)=x,\quad Dg(0)(x,y)=y.      \tag{4}
\]

Only nonzero constants have been used as divisors.

### A uniform estimate on both signed families of segments

Write h=(x,y) and |h| for its Euclidean norm. Differentiability in
(4) gives a nonnegative function rho(r), defined for sufficiently
small r>0 and tending to zero as r decreases to zero, such that

\[
 |f(x,y)-x|\le\rho(r)|h|,\qquad
 |g(x,y)-y|\le\rho(r)|h|\qquad (|h|\le r).               \tag{5}
\]

For example take the supremum of the two remainder ratios over
0<|h|<=r and set the center remainders to zero. The definition of
differentiability makes these suprema finite for small r and proves
their convergence to zero. This uses first-order remainders of f,g,
not derivatives of order m+n of the C1 density.

For a signed t!=0 put s=|t|. On the horizontal segment
S_h(t)={(x,t): -s<=x<=s}, (5) gives uniformly

\[
 \left|\frac{g(x,t)}t-1\right|\le\sqrt2\rho(\sqrt2 s).
                                                               \tag{6}
\]

On the vertical segment S_v(t)={(t,y): -s<=y<=s} it gives

\[
 \left|\frac{f(t,y)}t-1\right|\le\sqrt2\rho(\sqrt2 s).
                                                               \tag{7}
\]

These estimates hold for both signs of t: their denominators in the
absolute-value estimates are s. Define, only on these nonzero-t
segments,

\[
 A_h(x,t)=B(x,t)\left(\frac{g(x,t)}t\right)^n,\qquad
 A_v(t,y)=B(t,y)\left(\frac{f(t,y)}t\right)^m.             \tag{8}
\]

Both A_h and A_v converge uniformly to B0 as s decreases to zero,
including both signs of t. Indeed B(h)->B0 uniformly on shrinking
balls by continuity at zero. If |z-1|<=delta, the binomial formula
gives |z^k-1|<=(1+delta)^k-1 for a fixed positive integer k.
Apply this with (6), k=n, or (7), k=m, and use boundedness of B
near zero. Thus, after a common shrink,

\[
 \operatorname{Re} A_h>B_0/2,\qquad
 \operatorname{Re} A_v>B_0/2                              \tag{9}
\]

at every point of the respective segments. Neither expression
divides by f or g; t!=0 is the only extra divisor in (8).

Put theta_m=pi/m and theta_n=pi/n. Both sines are strictly positive
for the fixed even orders under consideration. Choose one epsilon>0
so that all the preceding segments with 0<s<epsilon are in the
factorization rectangle, (9) holds, epsilon<pi, and

\[
 \sqrt2\rho(\sqrt2 s)
   <\tfrac12\min\{\sin\theta_m,\sin\theta_n\}
       \quad(0<s<\epsilon).                              \tag{10}
\]

The finite orders are fixed before epsilon is chosen. This is the
only small-angle loss as an order grows; no order-uniform assertion
is needed.

### Horizontal segments force the complete first fiber

Fix any signed t with 0<|t|<epsilon, and let s=|t|. On S_h(t)
consider the continuous real function

\[
 H_t(x)=\operatorname{Im}\bigl(e^{-i\theta_m}f(x,t)\bigr).
\]

By (5) and (10), f(s,t)/s differs from 1 by less than
sin(theta_m)/2, while f(-s,t)/s differs from -1 by less than that
amount. Taking the displayed rotated imaginary parts gives

\[
 H_t(-s)>\tfrac{s}{2}\sin\theta_m>0,\qquad
 H_t(s)<-\tfrac{s}{2}\sin\theta_m<0.                     \tag{11}
\]

These are the ordered endpoint signs for either sign of t. The
imported real intermediate value theorem gives an interior x_t
with H_t(x_t)=0. Write f(x_t,t)=r exp(i theta_m), r real.
Since m is even,

\[
 f(x_t,t)^m=e^{i\pi}r^m=-r^m,
 \qquad r^m\ge0,
\]

with equality exactly when r=0. Equations (4) and (8) give the
exact identity q(x_t,t)=t^n A_h(x_t,t) f(x_t,t)^m. Since n is
even, t^n>0 for this signed nonzero t. The assumed full sign and
(9) therefore imply

\[
 0\le\operatorname{Re}q(x_t,t)
    =-t^n r^m\operatorname{Re}A_h(x_t,t),
\]

so r=0. This is a contradiction to nonnegativity unless the exact
contact f=0 occurs; it is not merely a leading-polynomial test.

Hence Phi1(p+(x_t,t))=zeta. The exact radial formula and the center
condition say

\[
 \frac{\Phi_1(p+(x_t,t))}{\zeta}
   =\exp\bigl(u_1(p+(x_t,t))-u_1(p)\bigr)e^{i x_t}.
\]

The first factor is positive real. Equality to 1 forces
exp(i x_t)=1, and |x_t|<epsilon<pi forces x_t=0. Consequently
Phi1(p+(0,t))=zeta for EVERY 0<|t|<epsilon, with the center included
by hypothesis. Phi2 cannot equal eta anywhere on this horizontal
segment because its argument differs by t with 0<|t|<pi. No zero
of either factor was discarded or traversed by a phase lift.

### Vertical segments force the complete second fiber

For the same signed t and s, on S_v(t) use

\[
 V_t(y)=\operatorname{Im}\bigl(e^{-i\theta_n}g(t,y)\bigr).
\]

Equations (5) and (10) give V_t(-s)>s sin(theta_n)/2 and
V_t(s)<-s sin(theta_n)/2, for both signs of t. At an interior
zero y_t supplied by the real intermediate value theorem write
g(t,y_t)=r exp(i theta_n), r real. Since n is even, g^n=-r^n.
Now (4) and (8) give q(t,y_t)=t^m A_v(t,y_t) g(t,y_t)^n.
With t^m>0 and Re A_v>B0/2, nonnegativity of Re q forces r=0.
Thus Phi2(p+(t,y_t))=eta. Its exact radial formula forces
exp(i y_t)=1, hence y_t=0. This proves Phi2(p+(t,0))=eta for
every |t|<epsilon, including zero. On this segment Phi1 cannot
equal zeta because its nonzero angular difference is t.

### Entire contact union and qualifications

On U the holomorphic units are nonzero, so G(Phi1)=0 iff w1=0.
The radial argument of Phi1 then forces x=0. Conversely every
point of x=0 in U has w1=0 by the horizontal-segment result. This
proves the first equality in (1). Likewise G(Phi2)=0 iff w2=0,
its angular argument forces y=0, and the vertical-segment result
proves the converse everywhere on that fiber. The coordinate images
remain in the factorization neighborhoods, so no additional zero
label or local component has been omitted.

The coefficient K in (2) is nowhere zero on U, including its
difference and Jacobian factors. Thus q vanishes exactly when one
of w1,w2 vanishes. At all other points it is nonzero and real
nonnegative by hypothesis, hence strictly positive. Every open
neighborhood of the center contains infinitely many points of each
fiber. This proves the stated obstruction to a finite ENTIRE
contact census; a census counting only simultaneous contacts would
not be covered by that consequence.

The proof retains C2 regularity and all contacts, uses no rank
assumption away from p, and allows arbitrarily flat scalar
restrictions. It does not prove existence of the conditional germs.
Rank-two contacts, J(p)=0, actual multiple-zero data, global
extension, weighted signs and Xi positivity remain separate gaps.
The count-only, unweighted-moment and singular real-flux stops are
unaffected. No numerical evidence or mathematical script is used.

### Independent conceptual audit — 6 November 2026

This historical audit precedes the direct normalization rewrite above.
Its references to L864 record how the original normalization was
verified; they are not premises of the current proof. The separate
audit below now covers the rewrite; L864 records its own composition audit.

Use the unchanged invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-06-l866-even-fiber-conceptual-audit.md`.
This separate audit checks the full proof, including all signed
segments and the entire local contact union. The factorization,
differentiability and real IVT inputs are precisely the sources
cited above, with their approved coverage reused. No additional
essential theorem or mathematical defect was found. This is
REPRODUCTION: verification of an existing conditional local input,
not a new theorem or progress beyond the sources checked.

In (2), G is nonzero entire and the assumed exact finite orders give
units nonzero at the origin. Continuity of the coordinate maps puts
their images inside the two factorization neighborhoods. Distinctness
and nonzeroness of zeta,eta, and J(p)!=0, keep every coefficient
factor nonzero on one common smaller rectangle. The minus sign,
squared difference, both denominators and J agree with L847's full
pullback in the original angular orientation. C2 u gives C1 J and K;
no higher regularity of the density is needed.

For (3)--(4), L864's coordinate determinants are -|zeta|^2 b and
|eta|^2 c. Both ranks one give b=c=0. The resulting nonzero
alpha=zeta(a+i) and beta=eta(d+i) are exactly the derivatives in the
own-angle directions. L864's positive scalar is exactly K0 alpha^m
beta^n, with the same full K0 as (2). Thus B0 is strictly positive
real, not just nonnegative at a zero of the leading polynomial.
All normalizations divide only by these nonzero constants. No
constant-rank hypothesis away from p or germ sufficiency is imported.

To check the common uniform bounds explicitly, choose r0>0 so that
the closed ball of radius r0 is inside that rectangle. Differentiability
at zero makes the supremum rho(r) in (5) finite for small r and
forces rho(r)->0. Put

\[
 \delta(s)=\sqrt2\rho(\sqrt2s),\qquad
 E(s)=\sup_{|h|\le\sqrt2s}|B(h)-B_0|.
\]

For 0<s<r0/sqrt2, E(s)->0 by continuity at zero. On the horizontal
segments, write z=g(x,t)/t; on the vertical segments write z=f(t,y)/t.
In either case |z-1|<=delta(s), since |t|=s and |h|<=sqrt2 s,
even when t<0. For k=n horizontally and k=m vertically, the
binomial estimate used in the proof gives the explicit error bound

\[
 |B(h)z^k-B_0|
 \le E(s)(1+\delta(s))^k
       +B_0\big((1+\delta(s))^k-1\big).                 \tag{A1}
\]

Both right sides tend to zero for the two fixed finite orders.
Choose epsilon with sqrt2 epsilon<r0 and epsilon<pi such that
each bound in (A1) is <B0/2 and delta(s) is less than half of
both sin(pi/m) and sin(pi/n), for EVERY 0<s<epsilon. The limit
definitions permit these simultaneous strict inequalities without
assuming monotonicity of an error expression. This verifies (6)--(10)
for both signs and both entire families of segments. The common
square U is inside the coefficient neighborhood. No uniformity as
either order tends to infinity is claimed.

For the horizontal endpoints, f(-s,t)=-s+e_- and f(s,t)=s+e_+,
where |e_-|,|e_+|<=s delta(s). Rotation by exp(-i pi/m) therefore
gives H_t(-s)>=s sin(pi/m)-s delta(s)>s sin(pi/m)/2 and
H_t(s)<=-s sin(pi/m)+s delta(s)<-s sin(pi/m)/2. These endpoints
are ordered by x regardless of the sign of t. Continuity on the
closed segment gives an interior zero by the cited real IVT. At
that zero, f=r exp(i pi/m) with r real, so f^m=-r^m. Evenness
of m makes r^m positive unless r=0; evenness of n makes t^n>0.
Using the actual varying A_h, rather than B0 in its place, gives
Re q=-t^n r^m Re A_h. Its nonnegativity and Re A_h>B0/2 force
r=0. This conclusion uses no division by a contact factor and
no argument, root branch or logarithm through zero.

At that contact the exact radial identity gives exp(ix_t)=1,
because exp(u1(p+(x_t,t))-u1(p)) is positive real. The chosen
angular interval forces x_t=0, and equality of the moduli gives
the stated constant u1 value. This holds for each positive and
negative t in the interval; the center is already a contact.
The second factor cannot contact its label on this segment since
its angular difference is the fixed nonzero t with |t|<pi.

Vertically, g(t,-s)=-s+e_- and g(t,s)=s+e_+ obey the same error
bound. Rotation by exp(-i pi/n) yields opposite strict endpoint
signs. At the IVT zero, g=r exp(i pi/n), hence g^n=-r^n and
Re q=-t^m r^n Re A_v. Evenness of both orders and (9) again
force r=0. The second radial identity gives y_t=0 and the stated
constant u2 value. The first factor has fixed nonzero angular
difference t and cannot contact its label there. These checks
also cover m=2 or n=2, where the corresponding sine is one.

Finally, nonzero holomorphic units give G(Phi_j)=0 exactly when
w_j=0 throughout U. The angular identities put these zero sets
inside x=0 and y=0 respectively. The two signed-segment conclusions
give the reverse inclusions at EVERY point of those fibers, not
only a sequence approaching the center. The images stay in the
unit neighborhoods, so other G labels cannot contribute. Nonzero
K excludes extra density zeros from the diagonal or J. Off the
union the density is nonzero and, by the original full reality
and nonnegativity hypothesis, strictly positive. Each fiber has
infinitely many points in every neighborhood of p; this excludes
a finite ENTIRE contact census containing this branch. The
simultaneous-contact intersection alone can still be a single point.

This accepted the then-stated conclusion and proof without strengthening
the hypotheses or result. At that audit the proof used L847 and L864;
L865 and the count/moment/real-flux stops were comparisons only.
No nonisolated germ, actual multiple-zero pair, rank-two or J=0
classification, global extension, weighted sign bound or Xi positivity
is established. In particular this audit does not apply a global
regular-value formula to additional labels.

### Independent direct-normalization audit — 6 November 2026

This is the normalization part of the separate RESEARCH / proof_audit /
REPRODUCTION step under the unchanged invocation-start SPECIALIZE
assessment `drafts/literature/2026-11-06-all-label-balance-composition-audit.md`.
It accepts the rewrite without changing any hypothesis or conclusion.
The factorization and first-order inputs are the precise Lebl sources
above; their inspected coverage is reused. No new theorem is imported.

The real matrices before multiplication by the centers are
[[a,b],[1,0]] and [[c,d],[0,1]]. Multiplication by a nonzero complex
number has positive real determinant equal to its squared modulus.
Thus rank one at the center forces b=c=0 directly, with neither
matrix zero. This gives alpha=zeta(a+i) and beta=eta(d+i), both
nonzero for real a,d. This argument uses neither the binary-form
classification nor any global conclusion of L864.

Finite-zero factorization supplies units nonzero at the center.
Continuity of the maps, the units and J, together with distinct
nonzero centers and J(p)!=0, permits a common rectangle on which
the entire coefficient K in (2) is continuous and nonzero. The
denominators, minus sign and squared difference are exactly those of
L847 in the original angular orientation. Along h=(t,t), t>0,
the first-order limits are w1(h)/t -> alpha and w2(h)/t -> beta.
The open neighborhood contains this ray for all sufficiently small t.
Consequently q(h)/t^(m+n) tends to K0 alpha^m beta^n. The former
values lie in the closed ray [0,infinity); the latter product is
nonzero. It is therefore strictly positive real. This proves (3)
without appealing to L864 or to the fiber conclusion being proved.
Only the nonzero constants alpha,beta are divided out to obtain (4).

The rest of the proof receives precisely the same f,g,B and B0 as
the previously audited version. To verify this connection, put
delta(s)=sqrt(2)rho(sqrt(2)s) and
E(s)=sup_{|h|<=sqrt(2)s}|B(h)-B0|. For k=n on horizontal segments
and k=m on vertical segments, the coefficient error is at most
E(s)(1+delta(s))^k+B0((1+delta(s))^k-1), which tends to zero for
each fixed order. One epsilon works for both signs of t, both
coefficients and both sine bounds. The real IVT projections have
strictly opposite endpoint signs in the order -|t|,+|t|. At their
zeros, evenness gives respectively Re q=-t^n r^m Re A_h or
Re q=-t^m r^n Re A_v; the positive factors force r=0.
The exact radial arguments then force x=0 or y=0, respectively.
This applies for EVERY sufficiently small nonzero signed t. Nonzero
units give both inclusions in each fiber equality and exclude all
other local labels. Nonzero K excludes additional density zeros.

Thus the normalization genuinely reconnects the full existing fiber
proof, including all preimages, rather than replacing it with a
leading-polynomial claim. The present proof uses L847 and the stated
standard inputs only. References to L864 in the historical audit
describe the former proof and create no circular premise. Germ
existence, actual multiple zeros, J=0, global extension and Xi signs
are unchanged open questions. No substantive defect or uncovered
source requirement was found; this is local verification, not a new
mathematical result beyond the already written conditional theorem.

## Mathlib

Full matching coverage for this actual-G arbitrary-even crossed-fiber
statement has not been checked. The cited factorization,
differentiability and real intermediate value theorem are standard
mathematical inputs, with applicability checked above; no Lean
theorem names or formal verification are asserted. Unknown coverage
is not evidence of absence. The independent informal critical review
above is not formal verification or a new Mathlib coverage check.
