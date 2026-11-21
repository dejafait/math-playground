# C467j — An oriented straight connector for one reverse double face

## Hypotheses

Use C467e's actual normalized logarithm and raw reversed flow, and
C467i/audit1025's actual positive-time double-face traces. In particular,

\[
 n=3,\quad R=1/4,\quad a=1/16,\quad T_0=1/1920,\quad I=(-a,a)^3,
\]
\[
 \beta(z)=B(1+z)-B(1)-B'(1)z,\quad g=\beta',\quad
 H_0=3[B(1)-B'(1)]\in\mathbb R,
\]
\[
 H(z)=H_0+\sum_{j=1}^3\beta(z_j),\quad
 F(z)=\Delta(z)^2e^{-H(z)},\quad
 \Delta(z)=\prod_{j<k}(z_k-z_j),\quad
 \Omega=F\,{dz_1\over i}\wedge{dz_2\over i}\wedge{dz_3\over i}.
                                                        \tag{1}
\]

Here exp B(w)=xi(1/2+sqrt(w))/xi(1/2), with B(1) real and
|beta''|<40 on |z|<R, as established through C466z/audit988 and
C466/audit993 in C467e. Thus beta(0)=beta'(0)=0 and
|beta(z)|<=20|z|^2 there. The original field, in physical time, is

\[
 Y_j'=2\sum_{k\ne j}{Y_j-Y_k\over|Y_j-Y_k|^2}
                  -\overline{g(Y_j)},\qquad Y(0,u)=iu.       \tag{2}
\]

For u=(x-delta/2,x+delta/2,y), let Y^+(t,x,y) be its delta>0
boundary trace from C467i, and Y^- its first-two-label exchange.
Take a separated compact rectangle K near (x,y)=(0,1/32), to be
chosen below. Define exactly the nominated connector

\[
 m=(Y^+_1+Y^+_2)/2,\quad d=(Y^+_2-Y^+_1)/2,\quad w=Y^+_3,
\]
\[
 \mathcal Z(t,x,s,y)=(m-sd,m+sd,w),\qquad -1\le s\le1.      \tag{3}
\]

Use orientation dt wedge dx wedge ds wedge dy. The connector is a
parameterized chain, not a trajectory of (2). The form (1) is defined
on the full polydisc, including the divisor; no vector field is
evaluated on that divisor. No divided weight, modulus-square
replacement, changed metric or time is allowed. Retain C466a's
external qualifications for any reciprocal-density interpretation;
no density construction, RH premise or global cycle is assumed.

## Conclusion

There are a closed rectangle K with (0,1/32) in its interior and

\[
 K\subset[-1/256,1/256]\times[7/256,9/256],\qquad
 0<\tau\le T_0,
\]

for which the actual connector remains in |z_j|<R and has the
following properties.

1. Its s=1 and s=-1 boundary maps, with induced orientations, cancel
   exactly the two chamber faces at delta=0. This uses the displayed
   positive parameter orientation, with no independent sign reversal
   of the connector. Time and lateral boundary terms are retained in
   (16) below.
2. With the same minus normalization as the reverse spatial form,

\[
 \mathcal C=-F(\mathcal Z)
       \det_{\mathbb C}(\mathcal Z_x/i,\mathcal Z_s/i,\mathcal Z_y/i),
 \qquad \operatorname{Re}\mathcal C\ge\tfrac12|\mathcal C|
                                                        \tag{4}
\]

   throughout (0,tau] x K x [-1,1]. For positive t its only zero on
   this patch is s=0. The argument includes this zero by an exact
   factorization of the original form.
3. All physical-time coefficients of Psi=Z^*Omega are L1 down to
   t=0, and its spatial mass tends to zero in L1 at rate O(t^(3/2)).
   Consequently the connector adds no initial spatial mass. The
   complete tested identity (16) passes to t=0 without an omitted
   lower-time term.

This supplies one local compensating collision contribution. Its
local claims are validated by the separate conceptual audit1029 below.
It does not eliminate C467i's raw defect, address a triple junction,
pay the lateral terms, construct a global cycle, prove positivity in
other degrees, or transfer positivity to Xi. The onset tau is
existential; no fixed-horizon or effective onset is asserted.

## Proof

### Source scope and the particular calculation required

The exact invocation-start EXPLORE target is in
`drafts/literature/2026-11-15-reverse-pair-connector-nomination-1025.md`,
completed by review1026. It covers this unchanged segment, original
weight, orientation, zero-set phase and initial-limit test. Its scoped
duplicate comparison retains stop1023 and distinguishes the prescribed
forward cap in stop1009. No matching theorem for this actual weighted
connector was found in that review; no originality claim follows.

Import Brian Conrad, *Math396. Stokes' theorem with corners*,
[Theorem1.1 and proof, pp1–3](https://math.stanford.edu/~conrad/diffgeomPage/handouts/stokescorners.pdf),
for the smooth parameter boxes below, separately for real and
imaginary parts. The compact box can be placed in an open parameter
neighborhood and furnished with a cutoff equal to one on it, so the
compact-support hypothesis is satisfied. Pullback is applied to a
smooth map; immersion of its image is not required. The ordinary
map-homotopy framework is also covered by Guillemin–Sternberg,
*Semi-classical analysis*, 13January2010, §13.13, (13.7)–(13.8),
[printed pp449–452](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf#page=449).
Only smooth pullback and Stokes are needed for the identity here.
These theorems are cited, not reproved or counted as a discovery.

C467e's regular coefficient flow and C467i's actual trace identification
are established inputs. Their ODE source is Teschl, *Ordinary
Differential Equations and Dynamical Systems*, April2012 preliminary
version, [Lemma2.14/Corollary2.15, pp52–53; Theorem3.9, p81;
Theorem6.1, pp189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
For the final integrable limit use Hunter, *Measure Theory*,
[Chapter4, Theorem4.24, pp49–50](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf#page=11).
Review1024 supplies the ready coverage for these imports. Their
hypotheses do not provide the connector estimates; the exact
reconstruction, full determinant and orientation calculation below
are the additional target-specific work. No special-Lagrangian,
singular-current extension or automatic collision-removal theorem is
assumed.

### Smooth coefficients of the actual split pair

Write (E(t,x,y),Pi(t,x,y)) for C467e's regular elementary-coefficient
trajectory starting at (e(x,x,y),0). Its reconstruction polynomial is

\[
 P(v)=\Pi_1+(E_1-v)\Pi_2+(v^2-E_1v+E_2)\Pi_3.              \tag{5}
\]

All its coefficients are smooth in (t,x,y) near t=0. C467i(13)–(15)
and its audit give a smooth simple third root q3(t,x,y), and a
factorization of the actual real root polynomial

\[
 Q_t(v)=(v-q_3)[(v-x)^2+\alpha(t,x,y)(v-x)+\gamma(t,x,y)],
\]

with alpha(0)=gamma(0)=0, gamma_t(0)=-2, and q3(0)=y. The actual
background was retained in that calculation. Choose K inside both
the displayed rectangle and its established neighborhood, still
containing (0,1/32) in its interior. In particular y-x>=3/128 on K.
All choices of sufficiently small time below are common on K.

Set q_c=x-alpha/2 and define

\[
 b(t,x,y)^2={\alpha^2-4\gamma\over4t},\qquad b(0,x,y)=\sqrt2.
                                                               \tag{6}
\]

This is smooth at zero: for f=alpha^2-4gamma, f(0)=0 and
f(t)/t=integral_0^1 f_t(theta t) dtheta, with f_t(0)=8. Thus the
positive square root in (6) is smooth for a common short time.
The split roots are q1=q_c-sqrt(t)b and q2=q_c+sqrt(t)b. Because
E1=2q_c+q3, the quadratic polynomial (5) gives exactly

\[
 m=P(q_c)+t b^2\Pi_3+iq_c,\qquad
 d=\sqrt t\,D,\quad D=b(i-\Pi_2-q_3\Pi_3),\qquad
 w=P(q_3)+iq_3.                                             \tag{7}
\]

These are the actual traces, since C467i identifies the ordered
positive-time simple roots and their reconstruction with the delta>0
limit of the original flow. Formula (7) uses that input, not a new
flow from a repeated initial root. It shows m,D,w smooth down to zero,
with

\[
 m(0,x,y)=ix,\quad D(0,x,y)=i\sqrt2,\quad w(0,x,y)=iy.       \tag{8}
\]

In particular their t,x,y derivatives are bounded on a sufficiently
small compact box. The only square-root loss in d_t is
D/(2sqrt(t)); d_x,d_y=O(sqrt(t)).

The trace of C467e's radial estimate gives
sum_j|Y_j^+|^2<=3/160<R^2. On the segment,

\[
 |m-sd|^2+|m+sd|^2+|w|^2
 =2|m|^2+2s^2|d|^2+|w|^2\le\sum_j|Y_j^+|^2<R^2.           \tag{9}
\]

Thus the whole connector lies in the original analytic polydisc,
including s=0. Smoothness on every positive-time closed box follows
from (7). This verifies the domain hypotheses for smooth pullback.

### The original spatial coefficient through every zero

Put W=w-m and J=m_x w_y-m_y w_x. Directly from (3), without any
modulus replacement,

\[
 \Delta(\mathcal Z)=2sd(W^2-s^2d^2),\qquad
 \det_{\mathbb C}(\mathcal Z_x/i,\mathcal Z_s/i,\mathcal Z_y/i)
       =2i d J.                                             \tag{10}
\]

For the second identity, the undivided determinant is 2dJ; division
by i in three columns multiplies it by i. Consequently the exact
coefficient (4) factors as

\[
 \mathcal C=s^2t^{3/2}G(t,x,s,y),
\]
\[
 G=-8iD^3(W^2-s^2tD^2)^2e^{-H(\mathcal Z)}J.                 \tag{11}
\]

The right side defining G is continuous on the closed box including
t=0 and s=0. This is an algebraic factorization of the original
coefficient, not substitution of a divided weight into the current.
Equations (8) give W(0)=i(y-x), J(0)=-1, hence

\[
 G_0(x,y):=G(0,x,s,y)
 =16\sqrt2\,e^{-H_0-2\beta(ix)-\beta(iy)}(y-x)^4.             \tag{12}
\]

On the containing rectangle, the actual background satisfies

\[
 |2\beta(ix)+\beta(iy)|
 \le20(2x^2+y^2)\le{415\over16384}<{1\over16}.
\]

Thus Re G0>(3/4)|G0| and min_K|G0|>0. Uniform continuity of (11)
on the compact product permits a common positive tau, reduced if
necessary, for which |G-G0|<|G0|/8 at every (t,x,s,y) under
consideration. Therefore

\[
 \operatorname{Re}G>{5\over8}|G_0|,\qquad
 |G|<{9\over8}|G_0|,\qquad
 \operatorname{Re}G>{5\over9}|G|\ge\tfrac12|G|.
                                                               \tag{13}
\]

Multiplication by s^2t^(3/2)>=0 proves (4), including equality at
s=0. Also G never vanishes, so these are exactly the zeros of C
at positive time. No normalized phase was assumed continuous at a
zero. Reduce tau to C467e's common short-time cone if needed: the
chamber and connector spatial forms then use the same global minus
normalization. No connector-only orientation reversal is made.

### Every mixed coefficient and the zero initial mass

Here dm,dd,dw denote parameter differentials in (t,x,y), and set
J_ab=m_a w_b-m_b w_a for a,b in {t,x,y}. Define

\[
 T=\det\begin{pmatrix}m_t&m_x&m_y\\d_t&d_x&d_y\\w_t&w_x&w_y\end{pmatrix}.
\]

The complete pullback, including all time components, is exactly

\[
 \Psi=2iF(\mathcal Z)\,dm\wedge(s\,dd+d\,ds)\wedge dw
 =A\,dx\wedge ds\wedge dy+B\,dt\wedge dx\wedge dy
       +U\,dt\wedge ds\wedge dy+V\,dt\wedge dx\wedge ds,
\]
\[
 A=2iF dJ_{xy}=-\mathcal C,\quad B=2iF sT,\quad
 U=2iF dJ_{ty},\quad V=-2iF dJ_{tx}.                         \tag{14}
\]

This follows by expanding dz1 wedge dz2=2 dm wedge d(sd), with
the same factor i from (10). In particular no time determinant is
replaced by the spatial determinant. On the compact box (7) gives
bounded J_ab, T=O(t^(-1/2)), d=O(sqrt(t)); (10) gives
F(Z)=O(e^(-H0)s^2t). Hence there is a finite constant C_K, independent
of t,s,x,y, such that

\[
 |A|+|U|+|V|\le C_K e^{-H_0}s^2t^{3/2},\qquad
 |B|\le C_K e^{-H_0}|s|^3\sqrt t.                            \tag{15}
\]

These bounds prove coefficientwise L1 integrability on the whole
finite parameter slab. In particular
integral_(K x [-1,1]) |A(t)| dx ds dy
<= (2/3)|K| C_K e^(-H0)t^(3/2), which tends to zero. They also
give integrable bounds for the endpoint B terms and all lateral
terms in the next identity. No boundary value of the singular field
(2) at s=0 or t=0 was used.

### Exact boundary cancellation with all tested terms retained

Let K=[x_-,x_+] x [y_-,y_+], 0<epsilon<T<=tau, and
Q=[epsilon,T] x [x_-,x_+] x [-1,1] x [y_-,y_+], with the
stipulated orientation. Let phi(t,x,y) be smooth on a neighborhood
of this box, independent of s. The form Omega is holomorphic of
top degree on the analytic polydisc, hence closed there. Thus
dPsi=0 at every positive time, also at s=0. Applying the cited
smooth Stokes theorem to phi Psi gives precisely

\[
\begin{split}
 &\int_Q(\phi_t A-\phi_x U-\phi_y V)\,dt\,dx\,ds\,dy\\
 &=\int_{x_-}^{x_+}\!\int_{-1}^1\!\int_{y_-}^{y_+}
       [\phi A]_{t=\epsilon}^{T}\,dy\,ds\,dx\\
 &\quad+\int_\epsilon^T\!\int_{x_-}^{x_+}\!\int_{y_-}^{y_+}
       \phi\,[B(t,x,1,y)-B(t,x,-1,y)]\,dy\,dx\,dt\\
 &\quad-\int_\epsilon^T\!\int_{-1}^1\!\int_{y_-}^{y_+}
       [\phi U]_{x=x_-}^{x_+}\,dy\,ds\,dt\\
 &\quad-\int_\epsilon^T\!\int_{x_-}^{x_+}\!\int_{-1}^1
       [\phi V]_{y=y_-}^{y_+}\,ds\,dx\,dt .                 \tag{16}
\end{split}
\]

For a general s-dependent phi the additional interior term is
+phi_s B, and endpoint tests are evaluated at their respective s
values. Formula (16) uses the common trace test required for matching
the two chambers; none of its derivatives has been discarded.

To check every face sign, contraction of dt dx ds dy with the
positive t,x,s,y coordinate vectors gives respectively dx ds dy,
-dt ds dy, +dt dx dy, -dt dx ds. Lower faces have the opposite
signs. This yields the four displayed lines on the right of (16).

The endpoint maps are exactly Z(t,x,1,y)=Y^+ and
Z(t,x,-1,y)=Y^-. Therefore B(t,x,1,y)=Bcal^+(t,x,y) and
B(t,x,-1,y)=Bcal^-(t,x,y), in C467i's notation. At the collision
boundary of the positive chamber delta>0, the outward normal is
-partial_delta, so its induced orientation in dt dx ddelta dy is
-dt dx dy. The negative chamber gives +dt dx dy. The connector's
s=1 face gives +dt dx dy and its s=-1 face gives -dt dx dy.
The maps and their oriented parameterizations consequently cancel
pairwise, exactly, at every positive time. This statement is about
the whole face map, not just an asymptotic scalar coefficient.

In particular C467i's Bcal^-=-Bcal^+ gives the connector face term
+2 integral phi Bcal^+ in (16), whereas the two chamber faces give
-2 integral phi Bcal^+. The initial change (x,delta,y) to u has
determinant +1, so no additional chamber sign is present. Multiplying
both chamber and connector forms by -1 to use (4) preserves this
cancellation.

For compact tests in (0,T) x int K the time and lateral terms vanish
by their stated support, leaving exactly the opposite of C467i's
compact collision pairing. For a fixed test smooth on a neighborhood
of the closed slab down to t=0, (15) makes
the lower-time term tend to zero as epsilon tends to zero. The
interior, endpoint and side integrals converge by the same bounds
and dominated convergence. Upper-time and lateral contributions
remain exactly as written; no positivity or payment for them has
been proved. This completes the local phase, orientation and limit
test, with C467i's raw-flux obstruction fully retained.

### Independent conceptual audit — 15 November 2026, step1029

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-15-reverse-pair-connector-audit-nomination-1027.md`,
with separate source repair1028. Reuse reviews1024/1026 for the
stated ODE, smooth-map Stokes and dominated-convergence imports.
The direct mathematical inputs remain C467e/audit1017 and
C467i/audit1025. No singular-pullback theorem or new source hypothesis
is needed. This independent local verification is REPRODUCTION,
not a novelty claim, and retains the raw zero-defect stop1023.

**Actual reconstruction and domain.** In C467i's audited actual
coefficient trajectory, the third root is simple at zero because
partial_v Q_0(y)=(y-x)^2>0. The implicit function theorem and
polynomial division give smooth real q3, alpha and gamma on a
neighborhood of the chosen compact K. The actual background was
retained in its calculation gamma_t(0)=-2. For f=alpha^2-4gamma,
f(0,x,y)=0 identically and f_t(0,x,y)=8. The integral of
f_t(theta t,x,y) over 0<=theta<=1 extends f/t smoothly, including
all spatial derivatives. Its positive square root divided by 2
is the smooth b of (6), with b(0)=sqrt(2). For a common short
time it is positive and the split pair stays separated from q3.
This uses y-x>=3/128, not a claim at triple collisions.

Independently, for h=sqrt(t)b the exact quadratic (5) gives

\[
 {P(q_c+h)+P(q_c-h)\over2}=P(q_c)+h^2\Pi_3,
\]
\[
 {P(q_c+h)-P(q_c-h)\over2}
       =h[-\Pi_2+(2q_c-E_1)\Pi_3].
\]

Using E_1=2q_c+q3 and adding the imaginary root coordinates proves
all of (7). C467i's preserved ordering identifies the positive
trace with these smaller/larger roots and the negative trace with
their exchange. Its convergence includes t,x,y derivatives on
compact positive-time sets, as needed for endpoint pullbacks.
No individual root derivative at t=0 is assumed. The explicit
m,D,w are smooth there, giving (8), J_xy(0)=-1, and bounded J_ab
for a,b in {t,x,y}. Their only square-root loss is
d_t=D/(2sqrt(t))+sqrt(t)D_t; d_x,d_y=O(sqrt(t)).

The limit of C467e's actual radial estimate gives
sum |Y_j^+|^2<=3/160. The parallelogram identity (9) holds for
real |s|<=1. Since 3/160<1/16, each connector component stays
strictly inside the analytic disk. On every positive-time compact
box it is smooth, also at s=0. The strict image-domain margin
allows an open parameter neighborhood for smooth Stokes.

**Complete constant and sector through zeros.** The gaps are
2sd, W+sd and W-sd. Their product proves the first formula (10).
Taking the half-sum and half-difference of the first two target
rows gives the undivided spatial determinant 2dJ_xy. Dividing
its three columns by i multiplies by i, not -i. Thus exactly

\[
 -F\det(\mathcal Z_x/i,\mathcal Z_s/i,\mathcal Z_y/i)
 =-8i s^2d^3(W^2-s^2d^2)^2e^{-H(\mathcal Z)}J_{xy}.
\]

Substitution d=sqrt(t)D proves (11) for the original coefficient,
without division at s=0. The expression for G is continuous on
the closed parameter product. At zero, D^3=-2sqrt(2)i,
W^4=(y-x)^4 and J_xy=-1. The constant is therefore
(-8i)(-2sqrt(2)i)(-1)=16sqrt(2), verifying (12) with the actual
exponential unchanged.

The containing rectangle gives
20(2x^2+y^2)<=20(2+81)/256^2=415/16384<1/16.
Since H0 is real, |arg G0|<1/16 and Re G0>(3/4)|G0|. Also

\[
 |G_0|\ge16\sqrt2\,e^{-H_0-415/16384}(3/128)^4>0.
\]

Only after establishing this uniform lower bound may compact
uniform continuity give |G-G0|<|G0|/8 on a common time interval.
It implies Re G>(5/8)|G0|, |G|<(9/8)|G0|, and hence (13).
Thus G has no zeros. Multiplication by s^2t^(3/2) proves (4)
at s=0 as well, and excludes every other positive-time zero on
the patch. This never assumes continuous argument of a vanishing
form. Intersecting with C467e's cone time gives the same minus
normalization for chambers and connector; no effective tau results.

**Every mixed coefficient and its bound.** The identity
dz1 wedge dz2=2 dm wedge (s dd+d ds), followed by i^(-3)=i,
gives (14). The no-ds coefficient is 2iF sT with precisely
the displayed row order (m,d,w) and columns (t,x,y).
In dm wedge ds wedge dw, the dt wedge dx wedge ds coefficient
is -J_tx, while the dt wedge ds wedge dy coefficient is J_ty.
This checks V=-2iF dJ_tx and U=2iF dJ_ty, as well as
A=2iF dJ_xy. These are all four three-form components.

Bounded first derivatives of m,w,D give J_ab=O(1) and
T=O(t^(-1/2)), uniformly on K. The exact gaps give
|F|<=C e^(-H0)s^2t, since the other factors are bounded and
|H(Z)-H0|<=20 sum |Z_j|^2<=3/8. Thus (15) follows with
one finite constant. At s=0 the whole original pullback is zero;
no singular field value or divided weight is being evaluated.
Integrating |A| uses integral_(-1)^1 s^2 ds=2/3 and gives
the stated O(t^(3/2)) spatial mass. All time-integrated
coefficients have majorants proportional to t^(3/2) or sqrt(t).
In particular endpoint B is O(sqrt(t)); the x and y side
coefficients are O(t^(3/2)). Each is integrable down to zero.

**Tests and orientations.** Holomorphic top-degree Omega is
closed on the full polydisc, including the divisor. Smooth
pullback therefore gives dPsi=0 at positive time. For an
arbitrary smooth parameter test the coefficient of dphi wedge Psi
in dt wedge dx wedge ds wedge dy is exactly

\[
 \phi_t A-\phi_x U+\phi_s B-\phi_y V.
\]

In particular the ds term makes two exchanges and has plus sign.
Contraction with the positive t,x,s,y coordinate normals gives
respectively dx ds dy, -dt ds dy, +dt dx dy, -dt dx ds;
lower faces have the opposite signs. The cited smooth Stokes
theorem, separately on real and imaginary parts, therefore gives
all four lines of (16). For s-independent phi the interior B
term is absent because phi_s=0, not because B is zero. For a
general test the stated additional term and distinct endpoint
test values are required. Neither immersion nor nonzero weight
is a Stokes hypothesis here.

The endpoint maps equal Y^+ and Y^- with their t,x,y derivatives.
Thus their B coefficients equal the full C467i traces, not merely
their leading asymptotics. The initial coordinate change has
determinant det([[1,-1/2,0],[1,1/2,0],[0,0,1]])=1. The positive
chamber's lower-delta face has sign minus, and the negative
chamber's upper-delta face has sign plus. The connector's s=1
face has plus sign and its s=-1 face minus sign. Equality of
each face map proves pairwise oriented cancellation. Equivalently,
using Bcal^-=-Bcal^+, the connector contributes
+2 integral phi Bcal^+ and the chambers -2 integral phi Bcal^+.
The same global minus normalization preserves their cancellation
and the proved sector; no connector-only sign is available.

For the zero-time limit the test is fixed and smooth on a
neighborhood of the closed slab, so it and its first derivatives
are bounded. This convention is now explicit in the original
proof. The lower-time integral is O(epsilon^(3/2)). All other
integrals are dominated, independently of epsilon, by the
coefficient bounds just proved times those bounded test quantities.
Apply the cited dominated convergence theorem to real and imaginary
parts, also to phi_s B if present. This proves the full limiting
tested identity, not smoothness of the root map at zero. Compact
interior tests remove the stated time and lateral terms by support;
general tests retain them. Their positivity or payment is unproved.

**Decision.** All local conclusions pass without changed constants
or mathematical hypotheses. The explicit bounded-test wording
clarifies the existing limit convention. This establishes one
separated face connector for existential short time. The lower
bound contains (y-x)^4 and supplies no uniform continuation to a
triple collision. Triple-junction compatibility, lateral/outer
payment, global assembly, all degrees and actual-Xi transfer remain
unresolved. The audit required exact algebra and analytic limits,
with no mathematical script or numerical evidence.

## Mathlib

Full matching coverage for this actual weighted connector, its
coefficient reconstruction, corners orientation and signed assembly
has not been checked. No absence claim or Lean verification is made.
The proof imports the explicitly cited smooth Stokes and dominated
convergence theorems and the audited local analytic inputs. The
target-specific calculation remains informal; conceptual audit1029
validates its local claims without formal verification or global assembly.
