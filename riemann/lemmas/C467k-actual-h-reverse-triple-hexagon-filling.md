# C467k — The actual reverse triple hexagon and its zero-mass filling

## Hypotheses

Use the actual analytic background, regular coefficient Hamiltonian and
raw reverse flow of C467e/audit1017, C467i/audit1025's coefficient
velocity at zero momentum, and C467j/audit1029's straight pair chains
with their chamber-induced orientations. In particular,

\[
 n=3,\quad R=1/4,\quad a=1/16,\quad T_0=1/1920,
\]
\[
 \beta(z)=B(1+z)-B(1)-B'(1)z,\quad g=\beta',\quad
 H_0=3[B(1)-B'(1)]\in\mathbb R,
\]
\[
 H(z)=H_0+\sum_{k=1}^3\beta(z_k),\quad
 F(z)=\Delta(z)^2e^{-H(z)},\quad
 \Delta(z)=\prod_{k<l}(z_l-z_k),\quad
 \Omega=F\,{dz_1\over i}\wedge{dz_2\over i}\wedge{dz_3\over i}.
                                                               \tag{1}
\]

Here exp B(w)=xi(1/2+sqrt(w))/xi(1/2), with the real conjugation
normalization and |beta''|<40 on |z|<R inherited through C467e from
C466z/audit988 and C466/audit993. In particular beta(0)=beta'(0)=0
and |beta(z)|<=20|z|^2. The physical flow for distinct real initial
coordinates u is

\[
 Y_k'=2\sum_{l\ne k}{Y_k-Y_l\over|Y_k-Y_l|^2}
                         -\overline{g(Y_k)},\qquad Y(0,u)=iu.
                                                               \tag{2}
\]

Write e(q)=(sum q_k, sum_(k<l) q_k q_l, q_1 q_2 q_3). Let
(E(t,x),Pi(t,x)) be C467e's regular coefficient solution starting
at (e(x,x,x),0), and put

\[
 Q_{t,x}(v)=v^3-E_1v^2+E_2v-E_3,\qquad
 P_{E,\Pi}(v)=\Pi_1+(E_1-v)\Pi_2+(v^2-E_1v+E_2)\Pi_3.
                                                               \tag{3}
\]

The existence of simple real roots of Q at positive time, and their
identification with actual boundary traces, are conclusions below,
not hypotheses about a singular flow on the initial divisor.
Keep C466a's external qualifications for any reciprocal-density
interpretation. No density realization, all-degree sign or RH premise
is assumed. The chains below use raw physical time and the original
form (1), including its divisor zeros; no divided or modulus-square
weight is substituted.

## Conclusion

Set K=[-1/256,1/256]. There is one 0<T_*<=T_0 such that for
x in K and 0<t<=T_*, Q has three simple real roots q_1<q_2<q_3.
With rho=sqrt(t),

\[
 q_k=x+\rho\eta_k(\rho,x),\qquad
 (\eta_1,\eta_2,\eta_3)(0,x)=(-\sqrt6,0,\sqrt6),              \tag{4}
\]

where the eta_k are smooth up to rho=0, uniformly on K. Set
v_k=P_(E,Pi)(q_k)+i q_k and vbar=(v_1+v_2+v_3)/3. The six
actual chamber traces, in cyclic order, are

\[
 V_0=(v_1,v_2,v_3),\ V_1=(v_2,v_1,v_3),\ V_2=(v_3,v_1,v_2),
\]
\[
 V_3=(v_3,v_2,v_1),\ V_4=(v_2,v_3,v_1),\ V_5=(v_1,v_3,v_2),
 \qquad V_6=V_0.                                            \tag{5}
\]

Exactly the nominated maps

\[
 Z_j=(1-r)\bar v\,\mathbf1
                  +r[(1-\lambda)V_j+\lambda V_{j+1}],
 \quad 0\le r,\lambda\le1,\quad j=0,\ldots,5,               \tag{6}
\]

stay in the original analytic polydisc. All six use orientation
dt wedge dx wedge dr wedge dlambda, as forced by the incident pair
chains, not chosen independently for positivity. Their radial edges
match and cancel with induced signs; their r=1 boundaries cancel the
triple-side limits of the lower/upper pair chains, with label
permutations specified in the proof.

For the common minus normalization, the full spatial coefficient is

\[
 \mathcal C_j=-F(Z_j)
       \det_{\mathbb C}(Z_{j,x}/i,Z_{j,r}/i,Z_{j,\lambda}/i)
     =r^7t^4(1-2\lambda)^2G_j(\sqrt t,x,r,\lambda),
                                                               \tag{7}
\]

where G_j is smooth on the closed rescaled parameter box and

\[
 G_j(0,x,r,\lambda)
   =3888e^{-H_0-3\beta(ix)}(2-\lambda)^2(1+\lambda)^2,
 \qquad \operatorname{Re}\mathcal C_j\ge\tfrac12|\mathcal C_j|.
                                                               \tag{8}
\]

This includes every zero: for positive time the coefficient vanishes
exactly at r=0 or lambda=1/2. All four physical-time components of
Z_j^*Omega are integrable down to zero. The total spatial absolute
mass of the six parameterized triangles is O(t^4), hence tends to
zero. The complete tested identity (20) below retains time, x-side,
outer-edge and test-derivative terms and passes to t=0.

These local claims of attempt1031 are validated by the independent
conceptual audit1033 below. The pair-limit statement is smooth on each
compact positive-time slab; it does not assert a common separated-pair sector as its initial
separation tends to zero. No fixed full horizon, effective onset,
global cycle, lateral payment, all-degree positivity or Xi transfer is
proved. This is not a complete RH candidate.

## Proof

### Source scope and standard inputs

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-15-reverse-triple-hexagon-nomination-1029.md`,
completed by separate source comparison1030. It approves the unchanged
six maps (6), actual F, induced orientations, zero-set sector and
physical-time limit test. Its inspected permutohedral, hyperbolic-root,
Nuij and heat-flow statements do not establish these conclusions.
No novelty claim follows. The target-specific coefficient rescaling,
weighted determinant and boundary calculation are the additional work;
no general root-perturbation or calibration theorem is reproved.

Reuse the already assessed smooth ODE inputs: Gerald Teschl,
*Ordinary Differential Equations and Dynamical Systems*, April2012
preliminary version, [Lemma2.14/Corollary2.15, pp52–53; Theorem3.9,
p81; Theorem6.1, pp189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
C467e has already constructed the regular open coefficient domain and
proved smooth dependence there and agreement with (2) for every distinct
initial u on a common short interval. We use that result by citation,
and the ordinary finite-dimensional implicit function theorem only at
the three explicitly simple roots in (10) below.

For positive-time parameter boxes, import Brian Conrad, *Math396.
Stokes' theorem with corners*, [Theorem1.1 and proof, pp1–3](https://math.stanford.edu/~conrad/diffgeomPage/handouts/stokescorners.pdf).
The map extends smoothly to a neighborhood of each such box; a cutoff
equal to one on it meets the compact-support convention. Apply the
theorem to real and imaginary parts. Smooth pullback does not require
an immersion or nonzero weight. The smooth-map convention is also
covered by Guillemin–Sternberg, *Semi-classical analysis*, 13January2010,
[section13.13, (13.7)–(13.8), pp449–452](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf#page=449).
The final limit uses Hunter, *Measure Theory*, [Chapter4, Theorem4.24,
pp49–50](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf#page=11),
with explicit integrable majorants below. Reviews1024/1028/1030 already
assess these inputs; no additional literature or singular-current
theorem is needed for this calculation.

### Actual triple-root splitting

Put h_+(v)=Im g(iv). C467i(13), including its continuity justification
at repeated roots, gives at Pi=0

\[
 \partial_tE_t(e(q))\big|_0=(0,-6,-2e_1)+(D_qe)h_+(q).
\]

At q=(x,x,x), the three entries are
3h_+(x), -6+6xh_+(x), and -6x+3x^2h_+(x). Consequently, writing
Q_(t,x)(x+w)=w^3+a_2(t,x)w^2+a_1(t,x)w+a_0(t,x),

\[
 a_2(0,x)=a_1(0,x)=a_0(0,x)=0,\qquad
 (a_{2,t},a_{1,t},a_{0,t})(0,x)=(-3h_+(x),-6,0).             \tag{9}
\]

All these coefficients are smooth on a neighborhood of {0} x K.
Taylor's formula with integral remainder therefore supplies smooth
real functions b_2,b_1,b_0 such that
a_2=t b_2, a_1=-6t+t^2 b_1 and a_0=t^2 b_0. Thus for rho!=0,

\[
 \rho^{-3}Q_{\rho^2,x}(x+\rho y)
 =y^3+\rho b_2(\rho^2,x)y^2
       +[-6+\rho^2b_1(\rho^2,x)]y+\rho b_0(\rho^2,x).        \tag{10}
\]

The right side extends smoothly to rho=0. There it is y^3-6y,
whose derivatives at -sqrt6,0,sqrt6 are respectively 12,-6,12.
The real implicit function theorem, compactness of K and uniqueness
in disjoint root neighborhoods give three smooth real branches eta_k
on one common rho interval. They exhaust this monic cubic and remain
distinct and ordered for positive rho. This proves (4), with actual
background h_+ retained. It neither assumes hyperbolicity on an open
coefficient domain nor applies (2) on its initial diagonal.
Throughout, decrease the time further to C467e's common short-time
interval as necessary, so its actual-flow identification remains valid.

### Actual chamber and incident pair limits

For distinct u, C467e identifies the original flow with its coefficient
solution and reconstruction (3) on a common short interval, preserving
imaginary ordering. At every point (t,x) with t>0 just constructed,
Q_(t,x) has simple roots. The usual simple-root charts are smooth in
time and in the initial coefficients on a neighborhood of this point.
Taking u to (x,x,x) within each ordering chamber therefore identifies
its full trace with the corresponding permutation in (5). On any
[epsilon,T_*] x K, finitely many such charts give uniform smooth
dependence, after a harmless open enlargement of K. No relation between
the rate u approaches the diagonal and positive t is assumed.

For the incident pair, use initial coordinates (a,a,b). On the same
compact positive-time slab, its coefficient solution is close to the
triple solution when (a,b) is close to (x,x). Its roots are consequently
simple real roots: the three real implicit branches exhaust the cubic.
Distinct initial approximants identify these roots with the actual
pair boundary traces. This defines the same straight-pair formula
as C467j; at any separated point where C467j's local construction
applies the two descriptions agree, by their common coefficient flow
and ordered reconstruction. For b>a, the paired labels limit to
(v_1,v_2), with singleton v_3. For b<a, they limit to (v_2,v_3),
with singleton v_1. The preserved ordering of distinct approximants
determines these assignments; they are not arbitrary relabelings.

The resulting segments and their tangential t,a,b,s derivatives are
smooth on each such positive-time neighborhood. In particular their
restriction as a=b=x, with tangential derivative partial_a+partial_b,
converges with all t,x,s derivatives. The required neighborhood may
depend on epsilon. This proves the needed incident limiting maps and
forms without importing C467j's separated lower bound uniformly at
b=a. The time-zero estimates for the limiting filling will be proved
directly, not inferred from these neighborhoods.

### Exact affine geometry and its complete spatial determinant

The center is smooth in physical time even though the individual roots
use rho. Indeed summing the reconstruction polynomial gives exactly

\[
 3\bar v=3\Pi_1+2E_1\Pi_2+E_2\Pi_3+iE_1,
 \qquad \bar v(0,x)=ix,\quad \bar v_x(0,x)=i.                \tag{11}
\]

Set W_k(rho,x)=(v_k-vbar)/rho, extended smoothly at rho=0 by
integrating its rho derivative. Pi=O(t), including x derivatives,
and (4) imply

\[
 \sum_k W_k=0,\qquad W(0,x)=i\sqrt6(-1,0,1).                \tag{12}
\]

Let W^(j) have the slot order of V_j, and put
U_j=(1-lambda)W^(j)+lambda W^(j+1). Then

\[
 Z_j=\bar v\,\mathbf1+r\rho U_j,\quad
 Z_{j,x}=\bar v_x\mathbf1+r\rho U_{j,x},\quad
 Z_{j,r}=\rho U_j,\quad Z_{j,\lambda}=r\rho U_{j,\lambda}.
                                                               \tag{13}
\]

All U_j and their derivatives belong to the complex two-dimensional
plane sum z_k=0. With determinants taking their displayed vectors as
columns, define D_j=det(1,U_j,U_(j,lambda)). The determinant of the
three zero-sum columns in (13) vanishes, giving the exact identity

\[
 \det(Z_{j,x}/i,Z_{j,r}/i,Z_{j,\lambda}/i)
              =i\bar v_x r\rho^2D_j.                        \tag{14}
\]

Here i^(-3)=i. Each edge exchanges exactly two adjacent ranked values.
Their coordinate difference is (1-2lambda) times its value at lambda=0.
Define Lambda_j as that latter difference times the other two oriented
differences in Delta(U_j). This is a smooth function, defined even at
lambda=1/2, and satisfies exactly

\[
 \Delta(U_j)=(1-2\lambda)\Lambda_j,\qquad
 \Delta(Z_j)^2=r^6\rho^6(1-2\lambda)^2\Lambda_j^2.
\]

Substitution in (14) proves (7), with

\[
 G_j=-i\bar v_xD_j\Lambda_j^2e^{-H(Z_j)}.                    \tag{15}
\]

This is a factorization of the original form, not a different form
obtained by division on its zero set.

For completeness all six leading algebraic cases reduce to two.
Writing U_j(0)=i sqrt6 R_j, one has

\[
 R_0=(-1+\lambda,-\lambda,1),\qquad
 R_1=(\lambda,-1,1-\lambda).
\]

R_2,R_4 are the even cyclic slot permutations (3,1,2),(2,3,1)
of R_0; R_3,R_5 are the even cyclic slot permutations (3,1,2),
(2,3,1) of R_1. Direct expansion for these two displayed vectors gives
det(1,R_j,R_(j,lambda))=3, and
Delta(R_j)=(-1)^j(1-2lambda)(2-lambda)(1+lambda). Even slot
permutations preserve both identities. Therefore on all six triangles,

\[
 D_j(0)=-18,\qquad
 \Lambda_j(0)^2=-216(2-\lambda)^2(1+\lambda)^2.
\]

Together with (11) and Z_j(0)=ix*1 this gives exactly (8)'s
leading constant 3888. No frozen-background approximation has replaced
the exponential in (15).

### Uniform sector, domain and zeros

The maps (13) extend continuously in rho to the compact box
{0} x K x [0,1]^2, where all their coordinates equal ix and
|x|<=1/256<R. Decreasing the common time makes their entire images
lie in |z_k|<R. Smoothness of (15) on this closed rescaled box then
follows from the actual analytic beta and the functions already proved
smooth. All derivatives used below are bounded there.

On K,

\[
 |3\beta(ix)|\le60x^2\le15/16384<1/16.
\]

Since (2-lambda)(1+lambda)>=2 on [0,1] and H_0 is real,

\[
 \operatorname{Re}G_j(0)>\tfrac34|G_j(0)|,\qquad
 |G_j(0)|\ge15552e^{-H_0-15/16384}>0.                         \tag{16}
\]

Compact uniform continuity, over all six indices as well, permits
one T_*>0 such that |G_j-G_j(0)|<|G_j(0)|/8 throughout the box.
Thus Re G_j>(5/8)|G_j(0)| and |G_j|<(9/8)|G_j(0)|, giving
Re G_j>(5/9)|G_j| and nonvanishing. Multiplication by the nonnegative
factor r^7t^4(1-2lambda)^2 proves the required sector including its
zeros. It also proves their stated exact location. This step uses a
nonzero floor for the factored full coefficient; small absolute error
in the unfactored, vanishing coefficient would not suffice.

### Orientations forced by all six incident pair faces

Use the pair's initial coordinates
u=sigma(a-delta/2,a+delta/2,b), where sigma is a slot permutation
and epsilon_sigma its sign. The coordinate change before sigma has
determinant +1. Thus ambient chamber orientation dt du_1 du_2 du_3
is epsilon_sigma dt da ddelta db in this chart. Exactly C467j's
endpoint cancellation replaces delta by s with connector orientation
epsilon_sigma dt da ds db. This remains valid for b<a; being the
lower or upper pair does not alter that coordinate determinant.

At the triple side put h=b-a. The pair orientation becomes
epsilon_sigma dt da ds dh. For a lower pair, h>0, its outward
normal at h=0 is -partial_h, giving +epsilon_sigma dt dx ds.
For an upper pair, h<0, the normal is +partial_h, giving
-epsilon_sigma dt dx ds. In both cases write s=1-2lambda.
The edge begins at V_j when s=1 and ends at V_(j+1) when s=-1.
The complete choices are:

| j | Paired ranks; singleton | Slot order sigma of (low pair, high pair, singleton) | epsilon_sigma | h side |
|---|---|---|---|---|
| 0 | (1,2); 3 | (1,2,3) | +1 | h>0 |
| 1 | (2,3); 1 | (1,3,2) | -1 | h<0 |
| 2 | (1,2); 3 | (3,1,2) | +1 | h>0 |
| 3 | (2,3); 1 | (2,1,3) | -1 | h<0 |
| 4 | (1,2); 3 | (2,3,1) | +1 | h>0 |
| 5 | (2,3); 1 | (3,2,1) | -1 | h<0 |

For each row, the resulting pair boundary has negative orientation
in (t,x,lambda), because ds=-2 dlambda. Its map is exactly
(1-lambda)V_j+lambda V_(j+1), by the actual pair limits above.
The r=1 face of dt dx dr dlambda has positive orientation
dt dx dlambda, and the same map. These are opposite oriented
parameterized faces. The factor 2 from ds=-2 dlambda is part of
the change of variables, so the full restricted forms, not merely
their signs or leading terms, cancel.

Thus all six triangle orientations used in (14) are forced and agree.
At lambda=1 in triangle j and lambda=0 in triangle j+1, the maps
are both vbar*1+r(V_(j+1)-vbar*1), with equal t,x,r derivatives.
Their induced orientations are respectively -dt dx dr and
+dt dx dr, so all radial faces cancel, including the j=5,0 join.
At r=0 the map is vbar*1 and its restricted three-form is zero.
Multiplying every chamber, pair and filling form by the same minus
normalization preserves all these cancellations.

### Every physical-time component and its integrable bound

Suppress j, write s=1-2lambda, and define the four coefficients by

\[
 \Psi=Z^*\Omega
   =A\,dx\wedge dr\wedge d\lambda
    +B\,dt\wedge dx\wedge d\lambda
    +U\,dt\wedge dr\wedge d\lambda
    +V\,dt\wedge dx\wedge dr,                               \tag{17}
\]

where A,B,U,V are F times the determinants of the respective ordered
columns (Z_x,Z_r,Z_lambda), (Z_t,Z_x,Z_lambda),
(Z_t,Z_r,Z_lambda), (Z_t,Z_x,Z_r), each column divided by i.
In particular A=-mathcal C. Formula (13) gives, in physical time,

\[
 Z_t=\bar v_t\mathbf1
             +r\left({U_j\over2\rho}+{U_{j,\rho}\over2}\right).
                                                               \tag{18}
\]

The center derivative vbar_t is bounded by (11). The zero-sum plane
identity used in (14) now bounds both the spatial minor and the
(t,r,lambda) minor by C r rho^2: in the latter only vbar_t*1
survives with the two zero-sum columns. In the (t,x,lambda) minor,
only one common-direction column can contribute. Its remaining
terms are bounded by C r^2, since the largest product is
(r/rho)(r rho). In the (t,x,r) minor the same expansion bounds
the terms by C r, since (r/rho)rho=r; this coarse bound suffices.
Terms with three zero-sum columns vanish, and terms with two common
columns vanish. Hence these estimates include every determinant and
all potentially singular physical-time contributions.

The exact Vandermonde factorization gives
|F(Z)|<=C r^6 rho^6 s^2, with C finite and uniform. Enlarging C
over six triangles, and taking T_*<=1, yields

\[
 |A|+|U|\le C r^7t^4s^2,\qquad
 |B|\le C r^8t^3s^2,\qquad |V|\le C r^7t^3s^2.             \tag{19}
\]

The constants include the fixed e^(-H_0) background. These are bounds
on the original coefficients, not on divided forms. They hold at
r=0 and s=0 by their smooth positive-time definitions. In particular
the six spatial absolute integrals are at most C' t^4 on the finite
parameter boxes. All four spacetime components, the r=1 boundary B,
the radial-face V and the x-side U have integrable majorants down
to t=0. This proves zero initial spatial mass and the necessary
physical-time integrability without any time reparameterization of
the current.

### Full tested identity and the time-zero limit

For 0<epsilon<T<=T_* let Q=[epsilon,T] x K x [0,1]^2, with
orientation dt dx dr dlambda. For each triangle let phi_j be fixed
and smooth on a neighborhood of the closed parameter slab including
t=0. Across matching faces require matching test values under the
stated face maps; do not require test derivatives to vanish. For
outer cancellation the incident pair test restricts to the same value.

Omega is closed on the analytic polydisc, including its divisor,
because it is a holomorphic top-degree form. Smooth pullback gives
dPsi=0 at positive time. Direct expansion gives
dphi wedge Psi=(phi_t A-phi_x U+phi_r B-phi_lambda V)
dt dx dr dlambda. The cited Stokes theorem therefore reads, for each j,

\[
\begin{split}
 &\int_Q(\phi_t A-\phi_x U+\phi_r B-\phi_\lambda V)
                                       \,dt\,dx\,dr\,d\lambda\\
 &=\int_{K\times[0,1]^2}[\phi A]_{t=\epsilon}^{T}
                                       \,dx\,dr\,d\lambda\\
 &\quad+\int_\epsilon^T\!\int_K\!\int_0^1
                [\phi B]_{r=0}^{1}\,d\lambda\,dx\,dt\\
 &\quad-\int_\epsilon^T\!\int_0^1\!\int_0^1
                [\phi U]_{x=-1/256}^{1/256}\,d\lambda\,dr\,dt\\
 &\quad-\int_\epsilon^T\!\int_K\!\int_0^1
                [\phi V]_{\lambda=0}^{1}\,dr\,dx\,dt .     \tag{20}
\end{split}
\]

For the positive t,x,r,lambda normals the contractions of the
orientation form are respectively dx dr dlambda, -dt dr dlambda,
+dt dx dlambda, -dt dx dr; lower faces reverse these signs. Thus
(20) retains every face and every test derivative with its induced
sign. Summing over j cancels exactly the final radial-face line by
the equality of maps and matching tests. The r=0 term is zero. The
r=1 terms cancel precisely the incident pair triple-side terms as
proved above, with their full tangential physical-time coefficients.
Upper-time and x-side terms remain, and so do all the interior test
derivatives. No sign or payment for the remaining side terms is claimed.

For the fixed tests stipulated here, values and first derivatives are
bounded down to t=0. The lower-time term is O(epsilon^4) by (19).
All other terms have the stated integrable majorants times bounded
test quantities, including the radial and outer faces. Apply dominated
convergence separately to real and imaginary parts to let epsilon
decrease to zero in (20) and its sum. This proves the full limiting
tested identity and zero added initial mass. It does not assert
smooth physical-time root dependence at t=0 or a new zero-defect
extension of the original chamber form; C467i's defect is compensated
only by the explicitly added local chains.

### Scope of the result

The bounded discriminator succeeds for this prescribed filling: actual
traces, induced edge matching, one full spatial sector through all
zeros, and zero initial mass hold together at existential short time.
Stops1009 and1023 remain intact. The independent audit1033 below checks
the triple-limit identification, orientation table, exact factorization
and all four physical-time components without extending their scope.
Uniform pair neighborhoods down to zero time, global domains and their
outer/lateral payment, all other degrees and transfer to actual-Xi
positivity remain independent unpaid work. No global assembly or
resolution of L030–L032/C032a is inferred.

### Independent conceptual audit — 16 November 2026, step1033

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-16-reverse-triple-hexagon-audit-nomination-1031.md`,
separately approved in review1032. Reuse its inspected ODE, implicit
function, smooth-map Stokes and dominated-convergence coverage and the
precise source versions cited above. The mathematical inputs are exactly
C467e/audit1017, C467i/audit1025 and C467j/audit1029, retaining their
inherited analytic and external-density qualifications. This is a
REPRODUCTION audit of the prescribed construction, not a new construction
or a novelty claim. No general hyperbolicity theorem is used.

**Coefficient rescaling and actual traces.** Independently translating
the coefficient polynomial gives

\[
 a_2=3x-E_1,\quad a_1=3x^2-2xE_1+E_2,\quad
 a_0=x^3-x^2E_1+xE_2-E_3.
\]

At the repeated initial triple, C467i(13) gives
E'=(3h,-6+6xh,-6x+3x^2h), where h=Im g(ix). Thus
a_2'=-3h, a_1'=-6 and
a_0'=-3x^2h-6x+6x^2h+6x-3x^2h=0. These identities hold
for every x in an open neighborhood of K. Taylor's integral remainder
therefore gives exactly the smooth b-functions in (10), including
their x derivatives; the remainder in a_0 is O(t^2), not merely o(t).
The rescaled polynomial at zero is y(y^2-6), with derivative
12,-6,12 at its three roots. The real implicit function theorem gives
three real smooth branches on disjoint root neighborhoods. Compactness
of K gives one common rho interval; a monic cubic has no additional
roots. Restricting rho>0 proves the stated ordering and simplicity.

C467e's regular real ODE is defined on an open coefficient neighborhood
including the initial diagonal. Its agreement with distinct-data raw
flow holds on a common short interval, with imaginary order preserved.
At a fixed positive t the limiting triple polynomial now has simple
real roots. Real simple-root charts thus identify the ordered limits
of distinct-data solutions with (4), and their reconstruction with (5).
On [epsilon,T_*] times K the discriminants stay nonzero; compactness
and the smooth coefficient flow give uniform charts and convergence
of all tangential derivatives. Shrinking the common time and slightly
enlarging K within its original domain are legitimate here.

The same charts applied to initial coefficients e(a,a,b) near e(x,x,x)
give real simple roots on that positive-time slab. Distinct initial
approximants identify the pair traces: for b>a the paired labels are
the two smaller roots, and for b<a they are the two larger roots.
Their straight interpolation agrees with C467j wherever its separated
construction is defined, since both use the same coefficient solution
and ordered reconstruction. Taking a=b=x gives all six stated edges;
the diagonal tangential derivative is partial_a+partial_b. Smoothness
in these charts proves convergence of t,x and segment derivatives.
This checks the full restricted forms, not only their point values.
The neighborhoods may depend on epsilon. No uniform neighborhood or
pair-sector estimate as epsilon tends to zero has been established.

**Full coefficient and its nonzero reduced limit.** Newton's identity
sum q_k^2=E_1^2-2E_2 in the quadratic reconstruction (3) gives
sum P(q_k)=3Pi_1+2E_1Pi_2+E_2Pi_3. This verifies (11), so the
center and its physical-time and x derivatives are smooth at zero.
Since Pi(0,x)=0 identically, smooth dependence gives Pi=O(t) with
x derivatives. Hence v_k-vbar is smooth in rho, vanishes at rho=0,
and division by rho via its integral remainder gives a smooth W.
Its leading values are precisely i sqrt(6)(-1,0,1), with zero sum.

All U and its derivatives lie in the complex plane of zero-sum triples.
Consequently the three zero-sum columns in the spatial determinant
vanish. The surviving term is r rho^2 vbar_x det(1,U,U_lambda);
dividing three columns by i multiplies it by i. This verifies (14)
with its sign. The two slots exchanged by each edge have difference
(1-2lambda) times their initial difference. Factoring that single
linear factor in the polynomial Vandermonde is exact, including at
lambda=1/2. The powers in the complete coefficient are therefore
r^(6+1) rho^(6+2)=r^7 t^4, proving (7) and (15).

For R0=(-1+lambda,-lambda,1) and R1=(lambda,-1,1-lambda), direct
cross products give R0 cross R0_lambda=R1 cross R1_lambda=(1,1,1).
Their determinants with first column 1 are both 3. Their Vandermondes
are respectively plus and minus
(1-2lambda)(2-lambda)(1+lambda). The even cyclic slot permutations
specified in the proof give the other four cases with unchanged
determinant and the displayed alternating Vandermonde sign. Thus
D_j(0)=(i sqrt(6))^2 3=-18 and
Lambda_j(0)^2=(i sqrt(6))^6(2-lambda)^2(1+lambda)^2
=-216(2-lambda)^2(1+lambda)^2. Since -i vbar_x(0)=1,
their product is +3888, with the actual exponential retained.

The limiting images ix have a strict margin inside |z|<R. Compact
continuity puts the entire maps in that disk for a common short time
and gives smooth G on the closed rescaled box. The exact bound
60/256^2=15/16384 controls |3beta(ix)|. Hence Re G0>(3/4)|G0|,
and its modulus has the uniform floor
m=15552 exp(-H0-15/16384)>0. Uniform continuity can be applied
with the absolute tolerance m/8, which implies the stated relative
tolerance |G-G0|<|G0|/8 at every parameter point. It follows that
Re G>(5/8)|G0| and |G|<(9/8)|G0|, so Re G>(5/9)|G| and G
never vanishes. Multiplication by r^7 t^4(1-2lambda)^2 proves the
claimed 1/2 sector at all parameters and the exact positive-time zero
set. No argument of a zero form, or division of the current, is used.

**Six induced outer edges and internal faces.** The determinant of
(a,delta,b) to (a-delta/2,a+delta/2,b) is +1. After a slot permutation
sigma, chamber orientation is epsilon_sigma dt da ddelta db.
C467j's endpoint cancellation therefore forces the connector
orientation epsilon_sigma dt da ds db on both separation sides.
Writing h=b-a gives epsilon_sigma dt da ds dh. The h=0 face of
h>0 has orientation +epsilon_sigma dt dx ds, and that of h<0 has
orientation -epsilon_sigma dt dx ds. This follows by contracting
the last coordinate of a four-form; it is not a guessed edge sign.

Reading each row of the table as an output slot order, its s=1
endpoint is respectively V0,V1,V2,V3,V4,V5; s=-1 gives the next
vertex, including V0 in the last row. Explicitly the lower-pair rows
have slot orders (1,2,3),(3,1,2),(2,3,1), all even, while the
upper-pair rows have (1,3,2),(2,1,3),(3,2,1), all odd. The change
s=1-2lambda makes all six induced triple-side orientations negative
in (t,x,lambda). Each equals the r=1 triangle map with the opposite
orientation. The change-of-variable factor 2 is included by pullback,
so full three-forms cancel exactly. No independent sign choice was
made to obtain the spatial sector.

At adjacent lambda faces the maps, and their t,x,r derivatives, agree.
Contraction gives -dt dx dr at lambda=1 and +dt dx dr at lambda=0,
including the cyclic last/first join. At r=0 the restricted map has
only its common-coordinate direction and the restricted three-form
is zero. The same minus normalization on every piece preserves these
cancellations. Permuting a pair map also multiplies its pulled-back
three-form by epsilon_sigma, since F is symmetric; this is already
accounted for by its forced domain orientation, not an extra sign.

**All four physical-time minors.** For an explicit independent check
write c=vbar, u=U_j, w=partial_lambda U_j and use subscripts for
derivatives. Let d_A,d_B,d_U,d_V be the four divided-column
determinants in the order of (17), before multiplication by F. Expanding
the common-direction columns and using the zero-sum plane gives

\[
\begin{split}
 d_A&=i c_x r\rho^2\det(1,u,w),\\
 d_U&=i c_t r\rho^2\det(1,u,w),\\
 d_B&=i r^2\{c_t\rho^2\det(1,u_x,w)
       -\tfrac12c_x\det(1,u,w)
       -\tfrac12c_x\rho\det(1,u_\rho,w)\},\\
 d_V&=i r\{c_t\rho^2\det(1,u_x,u)
       -\tfrac12c_x\rho\det(1,u_\rho,u)\}.
\end{split}
\]

In the last line the apparent constant term is zero because it has
two u columns. These formulas follow from
Z_t=c_t 1+r[u/(2rho)+u_rho/2], so they include the possibly singular
physical-time derivative rather than replacing dt by d rho. All
displayed coefficient functions are bounded on the rescaled compact
box. In the order (d_A,d_B,d_U,d_V), for rho<=1 their bounds are
C r rho^2, C r^2, C r rho^2 and C r. Multiplying by the exact
bound |F|<=C r^6 rho^6(1-2lambda)^2 proves every estimate in (19).
They hold on the divisor by the original smooth positive-time formulas.
There is no missing mixed component of a three-form in four variables.

Integrating the spatial bound over finite K and the unit square gives
O(t^4). The interior time integrals are controlled by t^4 or t^3;
the r=1 trace B, radial traces V and x-side traces U have those same
integrable bounds. The lower-time spatial integral is O(epsilon^4).
All statements concern the original pullback coefficients with raw
physical time and the fixed analytic exponential.

**Tested identity and limiting scope.** On a compact positive-time
box the map is smooth with image inside the analytic polydisc; an open
extension and cutoff meet the cited Stokes hypotheses. Omega is closed
there even at its divisor, because it is a holomorphic top form.
Thus dPsi=0 and the coefficient of dphi wedge Psi is exactly
phi_t A-phi_x U+phi_r B-phi_lambda V. The positive coordinate-normal
contractions have signs +,-,+,- for t,x,r,lambda, respectively.
These verify every interior term and all four lines of (20).

Matching test values suffice for cancellation of matching face forms;
no normal or tangential test derivative is being equated or discarded.
Summation cancels radial faces, the r=0 forms vanish, and the r=1
terms cancel the identified incident pair triple-side traces. This is
a local equality of face maps on positive-time slabs, not construction
of a full integrable family of pair chains near t=0. The upper-time,
x-side and interior test-derivative terms remain exactly as written.

The stipulated parameter tests are fixed, smooth through physical
time zero, with bounded values and first derivatives. The estimates
above dominate all integrands independently of epsilon; use indicators
of [epsilon,T] on the fixed full slab for the interior and side limits.
The separate lower-time term tends to zero by O(epsilon^4). Hunter's
dominated convergence theorem, applied to real and imaginary parts,
then proves (20) and its sum down to t=0. No smoothness of the root map
in physical time at zero is assumed. Tests without the stipulated
bounded derivatives, and uniform pair-family limits at the joint
zero-separation/time corner, have not been justified by this argument.

**Decision.** All local claims pass with unchanged hypotheses, maps,
normalization and existential time. The audit validates a local triple
filling and its complete tested limit, not a new result beyond the
construction being checked. Stops1009/1023 remain intact. Uniform
pair-family sector and limiting control near zero separation/time,
lateral/outer payment, global signed assembly, other degrees and
actual-Xi positivity remain unpaid. No RH candidate is asserted.

## Mathlib

Full matching coverage for this actual weighted six-triangle filling,
its triple-trace identification, sector and complete boundary identity
has not been checked. No absence claim or formal verification is made.
The supporting tools are the explicitly cited smooth ODE, implicit
function, smooth Stokes and dominated convergence theorems, together
with finite-dimensional determinant identities. The target-specific
informal proof is independently checked in audit1033 above; source
assessment alone was not verification. No formal verification is claimed.
