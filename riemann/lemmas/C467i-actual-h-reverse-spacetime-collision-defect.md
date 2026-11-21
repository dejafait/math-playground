# C467i — Bounded reverse spacetime minors and a double-collision defect

## Hypotheses

Use C467e–h with their audited hypotheses and original conventions:

\[
 n=3,\quad R=1/4,\quad a=1/16,\quad T_0=1/1920,\quad
 I=(-a,a)^3,\quad I^*=\{u\in I:\Delta(u)\ne0\},
\]
\[
 \beta(z)=B(1+z)-B(1)-B'(1)z,\quad g=\beta',\quad
 H(z)=H_0+\sum_j\beta(z_j),\quad H_0\in\mathbb R,
 \quad F(z)=\Delta(z)^2e^{-H(z)},
\]
\[
 \Delta(z)=\prod_{j<k}(z_k-z_j),\qquad
 Y_j'=2\sum_{k\ne j}{Y_j-Y_k\over|Y_j-Y_k|^2}
                       -\overline{g(Y_j)},\qquad Y(0,u)=iu.
                                                        \tag{1}
\]

The logarithm is the actual normalized B of C466z/audit988, through
C467e, with conjugation symmetry and |beta''|<40 on |z|<R.
C466/audit993 supplies that analytic bound through the same input.
Retain C466a's external qualifications for any reciprocal-density
interpretation. C467e–g/audit1017 and C467h/audit1021 are established
inputs; independent conceptual audit1025 below validates this result.
All derivatives use original physical time and the raw flat metric.
Lebesgue measure is completed. There is no changed weight, divided
coefficient, diagonal root-flow assumption or density/RH premise.

On (0,T_0) x I* put

\[
 \Theta=Y^*\left(F(z){dz_1\over i}\wedge{dz_2\over i}
                                      \wedge{dz_3\over i}\right).
\]

Let A be its spatial coefficient from C467h. For j=1,2,3 let M_j
be F(Y) times the complex determinant of D_uY/i with column j
replaced by Y_t/i. Define each coefficient to be zero on I\I*.
For a fixed smooth cutoff eta, zero on [0,1] and one on [4,infinity),
use the nominated cutoff

\[
 \chi_\epsilon(u)=\prod_{j<k}
                  \eta((u_k-u_j)^2/\epsilon^2).              \tag{2}
\]

## Conclusion

Every original mixed coefficient is measurable and uniformly bounded:

\[
 \|(M_1,M_2,M_3)(t,u)\|_2
       <{363\over800}e^{-H_0}\quad(u\in I^*,\ 0\le t\le T_0).
                                                               \tag{3}
\]

Together with C467h this gives an L1 extension of the entire original
form to the finite slab, including integrability as t decreases to zero.
Its spatial initial trace is still C467h's F(iu) in L1(I).

However, there is a real smooth compactly supported scalar test phi
in (0,T_0) x I for which

\[
 \operatorname{Re}\lim_{\epsilon\downarrow0}
       \int\phi\,d\chi_\epsilon\wedge\Theta>0.                \tag{4}
\]

Thus the L1 form is not distributionally closed. No choice of values
on the null initial diagonals changes this conclusion. This refutes
the proposed L1 extension **with zero interior collision defect**.
It does not refute an identity retaining that defect, a modified
construction, any global reverse route, or RH.

The contribution of a shrinking tube about the triple-collision line
is bounded by O(rho), uniformly for 0<epsilon<rho, as made precise
below. In particular the simultaneous cutoff-overlap region contributes
O(epsilon), with no equal-gap restriction. This does not erase the
defects along the incident double-collision faces.

## Proof

### Source scope and standard imports

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-15-reverse-spacetime-extension-nomination-1021.md`,
completed in review1022. Its exact target includes proving an actual
nonintegrable coefficient or nonzero actual cutoff defect. Reuse its
primary comparisons and stops948/1009; neither stop settles (4).
This is a specialization of assessed tools, classified REPRODUCTION,
without an originality claim or a claim beyond the sources checked.

For smooth dependence and continuous-coefficient linear variation use
Gerald Teschl, *Ordinary Differential Equations and Dynamical Systems*,
author-hosted April2012 preliminary version,
[Lemma2.14/Corollary2.15, pp52–53; Theorem3.9, p81;
Theorem6.1, pp189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
C467e already constructs the needed regular coefficient Hamiltonian
and its smooth local flow, including repeated initial roots; individual
roots are not presumed smooth at t=0. Use the standard implicit
function theorem only at a simple third root and at later simple roots.
The quadratic formula handles the initial double root explicitly.

For the weak-form interpretation use Gol'dshtein–Troyanov,
[*On the naturality of the exterior differential*, arXiv:0801.4295v1,
28January2008, Definition2.2 and Lemma2.1](https://arxiv.org/html/0801.4295v1).
The smooth exterior derivative commutes with pullback off the diagonals.
Pass integrable test pairings to the limit by dominated convergence,
John K. Hunter, *Measure Theory*, [Chapter4, Theorem4.24, pp49–50](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf#page=11).
No automatic removability or Sobolev pullback theorem is invoked.
Harvey–Polking's sufficient removal criteria from review1022 are not
assumed: (4) tests the actual pairing directly. The coefficient
Jacobian and local reconstruction used below are already proved and
audited in C467e–h; no general coordinate theorem is reproved.

### Reconstruct every mixed coefficient before taking norms

Write Y=p+iq. Use C467f–g's centered scaled coordinates with L=1/8:

\[
 E=\kappa(q)=(c/L,b/L^2,d/L^3),\quad P=(3m/L,U,LV),
 \quad J=D_q\kappa,\quad J_0=D_u\kappa(u),
\]
\[
 \mathsf M=D_{E^0}E_t,\quad\mathsf N=D_{E^0}P_t,\quad
 \mathsf R=\mathsf N\mathsf M^{-1},\quad Q=D_uq.
\]

All these quantities are at a distinct initial triple. By C467g,
the local momentum graph exists, det mathsf M>0 and ||mathsf R||<=1/5.
C467h gives the real symmetric Z=D_qp, ||Z||<1/2. Set

\[
 K=I_3-iZ,\quad v=p_t-Zq_t,\quad
 W=E'-iJK^{-1}v.                                            \tag{5}
\]

Here the primes mean derivatives along the coefficient trajectory
with initial E^0 fixed. The momentum graph at fixed E has time
derivative P'-mathsf R E'. The canonical identity p=L^2 J^T P
therefore gives exactly

\[
 v=L^2J^T(P'-\mathsf R E'),\quad
 D_uY/i=KQ,\quad Y_t/i=Kq_t-iv,\quad
 Q=J^{-1}\mathsf M J_0.                                    \tag{6}
\]

Let w_l=U+Vr_l, where r_l=q_l-c. The full pair identity from C467f
is Y_k-Y_j=(q_k-q_j)(i-w_l), with l the remaining index. Also
det J=-Delta(q)/(3L^6). Cramer's rule applied to the replaced column
in (6), before any modulus is taken, gives the vector of all three
original replacement determinants:

\[
 \begin{pmatrix}M_1\\M_2\\M_3\end{pmatrix}
 =-3L^6e^{-H(Y)}\Delta(q)\prod_{l=1}^3(i-w_l)^2\det K\,
       \operatorname{adj}(J_0)\operatorname{adj}(\mathsf M)W.
                                                               \tag{7}
\]

Indeed the vector before cancellation is
F det K det Q Q^{-1}(q_t-iK^{-1}v). Substitute (6), use
det Q=det mathsf M det J_0/det J, and then
det J_0 J_0^{-1}=adj J_0 and det mathsf M mathsf M^{-1}=adj mathsf M.
Finally substitute Delta(Y)^2=Delta(q)^2 product_l(i-w_l)^2.
This proves (7) including its minus sign. It preserves the complex
weight and every determinant factor; modulus squares enter only bounds.

For du_hat_j in increasing index order the complete form is

\[
 \Theta=A\,du_1\wedge du_2\wedge du_3
       +\sum_{j=1}^3(-1)^{j-1}M_j\,dt\wedge du_{\widehat j}.
                                                               \tag{8}
\]

In particular dchi wedge Theta has coefficient
-sum_j (partial_j chi)M_j in orientation dt du_1 du_2 du_3.
This sign convention will be used in the collision test.

### Uniform bounds on the whole original slab

Here all norms are Euclidean operator or vector norms. C467f gives
||D_{q/L}E||_F^2<133/75, so

\[
 \|J\|<8\sqrt{133/75}<11,\quad \|J_0\|<11,
 \quad \|\operatorname{adj}J_0\|<121.                        \tag{9}
\]

The last inequality follows from the singular-value formula for a
three-dimensional adjugate, ||adj T||<=||T||^2. C467g/h give
mathsf M'=T mathsf M with ||T||<392+139/5<420. Gronwall's inequality
applied to its integral equation, with mathsf M(0)=I, gives

\[
 \|\mathsf M\|\le e^{420T_0}=e^{7/32}\le32/25<2,
 \qquad \|\operatorname{adj}\mathsf M\|<4.                  \tag{10}
\]

The elementary comparison e^x<=1/(1-x), 0<=x<1, is sufficient here.
The continuous linear system is along each already surviving
trajectory; no common positive gap is required.

For completeness the first derivatives needed for (5) also have
gap-independent bounds. In C467g's Hamiltonian (3)–(7), write
s_j=r_j/L, B=b/L^2, W_m=LV (to distinguish this scalar from (5)), and
phi(z)=beta(Lz)/L^2. On the interpolation interval,
|phi'|<44, sum|s_j|<19/10 and sum|s_j^2+2B/3|<4/5.
Differentiate that Hamiltonian with respect to P=(M,U,W_m).
Its three components E'=mathcal H_P satisfy

\[
 |E'_1|<44,\quad |E'_2|<384+(19/10)44<468,\quad
 |E'_3|<128(19/10)+(4/5)44<279,
 \qquad \|E'\|<800.                                       \tag{11}
\]

These use |-128/(1+(U+W_m s_j)^2)|<=128 for the singular part.
They do not differentiate an individual inverse root gap.
C467f gives |m'|<=40/sqrt(160)<4, |U'|<75 and |V'|<238.
Consequently ||P'||<96+75+30<210. Equations (5),(6),(9) imply

\[
 \|v\|<\frac{11}{64}(210+800/5)<64.
\]

Since Z is real symmetric, the singular values of K are
sqrt(1+lambda_j(Z)^2); hence ||K^{-1}||<=1 and |det K|<2.
It follows that ||W||<800+11(64)<1600. Finally C467h gives

\[
 e^{-\operatorname{Re}H(Y)}\le(8/5)e^{-H_0},\qquad
 |\Delta(q)|<1/125,\qquad \prod_l|i-w_l|^2<2.
\]

Combining these bounds in the full expression (7) proves (3), because

\[
 {3\over 8^6}\,{8\over5}\,{1\over125}\,2\cdot2\cdot121
                  \cdot4\cdot1600={363\over800}<1.           \tag{12}
\]

Smooth dependence off the initial diagonals makes all coefficients
continuous there. Their zero extensions are Borel measurable, since
the union of the three diagonals is closed and null. Boundedness of
the mixed coefficients and C467h's bound for A give L1 on the full
finite slab. Thus even arbitrarily unequal initial gaps and t near
zero create no integrability failure. This does not assert closure.

### The actual coefficient flow at a double initial collision

Only a small positive time interval is needed to test closure.
Use C467e's already constructed, regular elementary coefficient
Hamiltonian (16)–(22), with coordinates

\[
 e(q)=(q_1+q_2+q_3,q_1q_2+q_1q_3+q_2q_3,q_1q_2q_3),
 \quad J_e=D_qe,\quad p=J_e^T\pi.
\]

Its smooth solution (mathcal E_t(e^0),Pi_t(e^0)) with Pi_0=0 is
defined on a neighborhood of every initial e(u), including repeated
roots, for one common short time. C467e also gives its local momentum
graph pi_hat_t(e) and agreement with the original flow at distinct u.
It follows that p=J_e^T pi_hat_t(e(q)) is smooth in (t,q) even at
repeated q on this smaller domain. Its spatial derivative Z is zero
at t=0, as is pi_hat_0. No individual diagonal root flow is assumed.

Put u=(x-delta/2,x+delta/2,y), with (x,y) in a small neighborhood
of (0,1/32), so y-x is bounded below by a positive number and all
initial entries remain inside I. At delta=0 write e^0=e(x,x,y).
Let h_+(v)=Im g(iv). The coefficient velocity at initial zero momenta
is, exactly,

\[
 \partial_t\mathcal E_t(e(q))\big|_{t=0}
      =s(e(q))+J_e(q)(h_+(q_j))_{j=1}^3,
 \qquad s(e)=(0,-6,-2e_1).                                  \tag{13}
\]

For distinct q, each singular pair contributes zero to e'_1,
-2 to e'_2, and -2q_l to e'_3, where l is the remaining index.
The background is J_e h_+. Both sides of (13) extend continuously
to repeated q by the regular coefficient flow, proving (13) there
too. Thus the actual background is retained, not suppressed.

Let Q_t(v)=v^3-mathcal E_{t,1}v^2+mathcal E_{t,2}v-mathcal E_{t,3}
at this repeated initial datum. The background term in (13) gives
zero to partial_t Q_t(x) at t=0: differentiation with root velocities
h_+(q_j) gives -sum_j h_+(q_j) product_{k!=j}(x-q_k), and every
product vanishes at q=(x,x,y). The singular term therefore gives

\[
 \partial_t Q_t(x)\big|_{0}=-2(x-y).                         \tag{14}
\]

The simple third root continues smoothly as q_3(t)=y+O(t).
Factor the real monic polynomial as

\[
 Q_t(v)=(v-q_3(t))[(v-x)^2+\alpha(t)(v-x)+\gamma(t)].
\]

Here alpha(0)=gamma(0)=0 and (14) gives gamma'(0)=-2.
Hence alpha(t)=O(t), gamma(t)=-2t+O(t^2), and the discriminant
of the quadratic is 8t+O(t^2)>0 for all sufficiently small t>0.
The three roots are then real and distinct, with

\[
 q_1=x-\sqrt{2t}+O(t),\quad q_2=x+\sqrt{2t}+O(t),\quad
 q_3=y+O(t),\quad
 {\Delta(q)\over\sqrt t}\longrightarrow2\sqrt2\,(y-x)^2.
                                                               \tag{15}
\]

All bounds and limits here are locally uniform in (x,y). This follows
from smooth parameter dependence, the uniform separation of y from x,
and the explicit quadratic formula with discriminant 8t+O(t^2).
For every such positive t the simple-root charts identify these roots
with the limits of the actual solutions as delta decreases to zero
from above. The initial elementary coefficients depend smoothly on
delta^2; thus this chamber limit, with its t,x,y derivatives on compact
positive-time sets, exists. From delta<0 the first two labels exchange.

### The nonzero original tangential spacetime trace

In the coordinates (t,x,delta,y), let Bcal denote the coefficient of
dt wedge dx wedge dy in the restriction delta=constant. By (8),

\[
 \mathcal B=M_1-M_2
   =F(Y)\det_{\mathbb C}(Y_t/i,Y_x/i,Y_y/i).                 \tag{16}
\]

Use the short-time elementary coefficient graph just constructed.
Set v=p_t-Zq_t and K=I-iZ as before, and
W_e=partial_t mathcal E_t-iJ_e K^{-1}v. Exactly as in (6), but now
with det J_e=-Delta(q), its positive chamber boundary trace obeys

\[
 \mathcal B^+(t,x,y)
 =-e^{-H(Y)}\Delta(q)\prod_l(i-w_l)^2\det K\,
     \det(W_e,\partial_x\mathcal E_t,\partial_y\mathcal E_t).
                                                               \tag{17}
\]

This identity holds for t>0, where the evolved roots are simple.
Every factor on its right except the displayed Delta(q) has a
continuous limit as t decreases to zero; W_e contains no inverse J_e.
In particular K tends to I and all pair slopes w_l tend to zero.
The latter also follows directly from pi_hat_t tending to zero in
the elementary pair formula of C467e.

To compute the remaining determinant, set

\[
 X=\partial_x e(x,x,y)=(2,2x+2y,2xy)^T,\qquad
 V_y=\partial_y e(x,x,y)=(1,2x,x^2)^T.
\]

At t=0, v_j=-Re g(iq_j). For distinct q this is the actual initial
real velocity, because the singular velocity is purely imaginary
and Z=0. Continuity of the coefficient graph proves the same identity
at repeated q. Both J_e h_+ and J_e v are in the real span of X,V_y:
the first two entries of their respective root velocities coincide.
Consequently (13) implies

\[
 \lim_{t\downarrow0}
 \det(W_e,\partial_x\mathcal E_t,\partial_y\mathcal E_t)
       =\det((0,-6,-4x-2y)^T,X,V_y)=4(y-x)^2.                \tag{18}
\]

For example X cross V_y=2(x-y)(x^2,-x,1)^T, which checks this sign.
Also product_l(i-w_l)^2 tends to i^6=-1. Equations (15),(17),(18)
therefore give the explicit actual-background limit

\[
 \lim_{t\downarrow0}{\mathcal B^+(t,x,y)\over\sqrt t}
   =8\sqrt2\,e^{-H_0-2\beta(ix)-\beta(iy)}(y-x)^4.           \tag{19}
\]

This nonzero coefficient uses the original algebraic-square weight
and full determinant. At (x,y)=(0,1/32),
|beta(i/32)|<=20(1/32)^2=5/256, so the real part of the right side
of (19) is strictly positive. By locally uniform convergence and
continuity it follows that Re Bcal^+>0 for all sufficiently small
positive times in a fixed smaller (x,y) neighborhood.

Permutation equivariance of (1) exchanges labels 1 and 2 between
the delta>0 and delta<0 limits. F is symmetric, whereas the determinant
of its three labeled target coordinates changes sign. Thus

\[
 \mathcal B^-(t,x,y)=-\mathcal B^+(t,x,y).                   \tag{20}
\]

This is a jump of the tangential spacetime trace, not a failure of
the already proved spatial initial trace.

### Evaluate the nominated cutoff and account for triple collisions

Choose a nonnegative nonzero smooth psi(t,x,y) supported in the
positive-time region of Re Bcal^+>0 just obtained. Choose a real smooth
zeta(delta), equal to one near zero and supported in a small interval,
so that phi=psi zeta is compactly supported in (0,T_0) x I and the
third initial coordinate remains uniformly separated from the first
two on its support. The coordinate transformation
(x,delta,y) -> (x-delta/2,x+delta/2,y) has determinant +1.
For sufficiently small epsilon the two cutoff factors involving y
are identically one on this support. Formula (8) gives

\[
 d\chi_\epsilon\wedge\Theta
 =\partial_\delta\eta(\delta^2/\epsilon^2)\,
       \mathcal B(t,x,\delta,y)\,dt\wedge dx\wedge d\delta\wedge dy.
                                                               \tag{21}
\]

There is a plus sign: moving ddelta past dt and dx makes two swaps.
The derivative in (21) integrates to +1 over delta>0 and -1 over
delta<0. Rescale delta=epsilon r separately on r in [1,2] and
[-2,-1]. The boundary traces converge uniformly on these compact
positive-time sets and the derivative is bounded after rescaling.
Dominated convergence, (20), and zeta(0)=1 yield

\[
 \lim_{\epsilon\downarrow0}\int\phi\,d\chi_\epsilon\wedge\Theta
       =2\int\psi(t,x,y)\mathcal B^+(t,x,y)\,dt\,dx\,dy.
                                                               \tag{22}
\]

Its real part is strictly positive. This supplies (4) using the
prescribed product cutoff, with no outer box boundary involved.

To check the simultaneous-collision stratum independently, write
T_rho={u in I:max_{j<k}|u_j-u_k|<rho}. Each differentiated factor
of chi_epsilon is bounded by C_eta/epsilon and is supported where
one gap has modulus between epsilon and 2epsilon. Inside T_rho,
that gap has a set of lengths O(epsilon), an independent second gap
has lengths O(rho), and a translation coordinate has bounded length.
The associated linear coordinate changes have fixed nonzero
determinants. Thus, for any bounded compact test and 0<epsilon<rho,
(3) gives

\[
 \int_{(0,T_0)\times T_\rho}
       |\phi\,d\chi_\epsilon\wedge\Theta|
       \le C_{\phi,\eta,a,T_0}e^{-H_0}\rho.                  \tag{23}
\]

Here the absolute value is that of the coefficient in the oriented
Lebesgue volume. Only the mixed coefficients occur in this wedge.
When two cutoff transition regions meet, all three gaps are at most
4epsilon; applying (23) with rho=4epsilon gives O(epsilon).
More generally letting rho decrease to zero in (23) excludes a
separate concentrated triple-line contribution at any unequal gap
ratios. It does not claim cancellation of face defects in a fixed
neighborhood of that line. The positive test (22), already supported
away from the triple line, cannot be canceled by it.

Finally, off the initial diagonals, the holomorphic target three-form
is closed: dF has only dz components and each repeats a factor in
dz_1 wedge dz_2 wedge dz_3. Smooth pullback therefore gives dTheta=0
there. Apply compactly supported integration by parts to phi chi_epsilon
on this smooth domain. It gives

\[
 \int\chi_\epsilon d\phi\wedge\Theta
                   =-\int\phi\,d\chi_\epsilon\wedge\Theta.
\]

The left side tends to integral dphi wedge Theta by the established
L1 bounds and dominated convergence. Thus the distributional dTheta
paired with phi equals (22), which is nonzero. A change on a null set
cannot alter an L1 distribution. This completes the obstruction.

The result supplies an informative local negative for the zero-defect
extension, together with a positive integrability input. Independent
conceptual audit1025 below validates these claims within their scope.
It leaves outer-interface payment, any identity retaining collision
flux, global signed assembly, all degrees and Xi transfer unresolved.
No numerical experiment or mathematical script is used as evidence.

### Independent conceptual audit — 15 November 2026, step1025

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-15-reverse-spacetime-defect-audit-nomination-1023.md`,
completed in separate review1024. Reuse its primary ODE, weak-form and
dominated-convergence coverage. C467e–g/audit1017 and C467h/audit1021
are inputs; the conclusions of this lemma were not assumed in the
review. The complete proof (5)–(23) passes with unchanged hypotheses
and constants. This is a REPRODUCTION audit of a local specialization,
not a new theorem beyond the checked sources or a resolution of RH.
The independent verification below checks the signs and singular
limits; it does not reprove the cited general tools.

**Physical time and all mixed minors.** At fixed evolved E, the
time derivative of the local momentum graph is P'−mathsf R E'.
Differentiating p=L²Jᵀ P_hat(t,E(q)) along a trajectory gives

\[
 p_t=Zq_t+L^2J^T(P'-\mathsf R E').
\]

The derivative of Jᵀ with q belongs to Zq_t, not to a missing
term in v. Also E'=Jq_t and JQ=mathsf M J_0. These facts check
(5)–(6) without a rescaled time or an inverse-gap estimate.
For K=I−iZ, put b=q_t−iK⁻¹v. The replacement determinants of
KQ, with inserted column Kb, form det K det Q Q⁻¹b. Here

\[
 \det Q\,Q^{-1}b
 =\frac{\operatorname{adj}J_0\,
          \operatorname{adj}\mathsf M\,Jb}{\det J},
 \qquad Jb=E'-iJK^{-1}v.
\]

Thus the adjugates have exactly the order in (7). Multiplying by F,
using det J=−Delta(q)/(3L⁶) and
Delta(Y)²=Delta(q)² product_l(i−w_l)², gives its minus sign
and single remaining Delta(q). Every complex factor is retained.
Moving a time column from position j to the first position takes
j−1 swaps, giving (8). Wedging du_j into that term then gives
a minus sign for every j. Hence dchi wedge Theta has coefficient
−sum_j chi_j M_j in dt du_1 du_2 du_3.

**Uniform comparisons.** C467f gives
||J||,||J_0||<8 sqrt(133/75)<11. The three-dimensional adjugate
norm is the product of the two largest singular values, so
||adj J_0||<121. The audited physical-time variation coefficient
has norm <392+139/5<420. Thus
||mathsf M||<=exp(420T_0)=exp(7/32)<=32/25<2 and
||adj mathsf M||<4. For each fixed distinct u the coefficient
matrix is continuous on the closed interval, as required for the
integral-equation form of Gronwall's inequality. A common positive
gap or a common full-horizon coefficient neighborhood is not needed.

For (11), phi'(0)=0, |phi''|<40 on |z|<2, and |z(s)|<11/10
give |phi'(z(s))|<44 by integration along the segment from 0.
At fixed E, the roots s_j do not depend on P=(M,U,W_m).
Differentiating C467g's physical-time Hamiltonian with respect to
these variables gives the background factors 1/3, −s_j, and
s_j²+2B/3. The singular term has zero M derivative and derivatives
−128/(1+w_j²), −128s_j/(1+w_j²) in the other variables.
The component bounds are therefore

\[
 44,\qquad384+\frac{19}{10}44=\frac{2338}{5}<468,
 \qquad128\frac{19}{10}+\frac45 44=\frac{1392}{5}<279.
\]

Their sum is less than 791<800. C467f gives
|(3m/L)'|<96, |U'|<75, |(LV)'|<30, hence ||P'||<201<210.
It follows that ||v||<(11/64)(210+160)=2035/32<64.
The established symmetry of Z gives ||K⁻¹||<=1 and
|det K|<(5/4)^(3/2)<2. Hence ||W||<800+704<1600.
C467h's background, Vandermonde and pair-slope bounds yield exactly

\[
 \frac3{8^6}\frac85\frac1{125}\,2\,2\,121\,4\,1600
       =\frac{363}{800}.
\]

This verifies the original mixed vector bound (3), including both
time endpoints and arbitrary unequal gaps. Smooth dependence off
the initial planes and zero extension on the closed null planes
give joint Borel measurability. The finite slab and constant bound
give L1 integrability; C467h supplies the spatial bound and initial
L1 trace without alteration.

**Actual double-root splitting and chamber traces.** Only C467e's
common short-time elementary coefficient chart is used. Its smooth
flow is defined on an open neighborhood containing e(x,x,y).
The momentum graph makes p(t,q)=J_e(q)ᵀ pi_hat_t(e(q)) smooth
near (0,x,x,y), after shrinking that neighborhood and time if needed,
with Z=0 at t=0. No whole-horizon diagonal root map is assumed.

At zero momentum, a singular pair contributes 0, −2, −2q_l
to e'_1,e'_2,e'_3 respectively. The actual background imaginary
velocity is h_+(q_j). Summing gives (13) at distinct roots;
continuity of the regular coefficient field extends it to repeated
roots. Every background term in partial_t Q_t(x) contains a
vanishing factor from the repeated pair. The remaining term is
−6x+2(2x+y)=−2(x−y), verifying (14).

The implicit function theorem gives q_3(t,x,y) smoothly, since
(y−x)² stays bounded away from zero. Polynomial division gives
smooth real alpha and gamma. Differentiating
Q_t(x)=(x−q_3(t))gamma(t) at zero gives gamma'(0)=−2.
Thus alpha=O(t), gamma=−2t+O(t²), and their discriminant is
8t+O(t²), uniformly on a compact (x,y) neighborhood. The quadratic
formula gives (15) and, for sufficiently small common positive time,
three real distinct roots with the pair separated from the third.

The initial coefficients e(x−delta/2,x+delta/2,y) are smooth in
(x,delta²,y). On each compact interval of these strictly positive
times the limiting roots are uniformly simple. Smooth dependence
and the simple-root implicit function theorem give convergence with
the t,x,y derivatives as delta tends to zero from either side.
C467f's preserved ordering identifies the delta>0 labels with the
smaller/larger split roots and the negative side with their exchange.
This checks the actual-flow traces without derivative convergence
at t=0 or a smooth initial root map.

**Full trace determinant and actual background.** The chain rule
Y_x=Y_{u_1}+Y_{u_2} proves (16) with M_1−M_2. Substituting
q_x=J_e⁻¹ partial_x mathcal E_t and the analogous y column,
and the time correction from (6), gives (17), including the
negative det J_e. On this short-time graph
v=J_eᵀ partial_t pi_hat_t at fixed q, so v is continuous down
to t=0 although q_t itself can diverge. Its initial value is
−Re g(iq_j), first at distinct roots from the original velocity
and then at repeated roots by continuity.

For a vector (h,h,k), J_e(h,h,k)=hX+kV_y. Both h_+(q) and
the initial v have this shape. Therefore their background terms
in W_e lie in the complex span of the other two columns and
contribute zero to the determinant. Independently,

\[
 X\mathbin{\times}V_y=2(x-y)(x^2,-x,1)^T,
\]
\[
 (0,-6,-4x-2y)\mathbin{\cdot}(X\mathbin{\times}V_y)
       =4(y-x)^2.
\]

As t tends to zero, K tends to I, the pair slopes tend to zero,
and their squared factors have product i⁶=−1. The negative
elementary Jacobian, that −1, the Vandermonde limit in (15), and
the last determinant give exactly 8 sqrt(2)(y−x)^4 in (19).
The retained background is exp(−H_0−2beta(ix)−beta(iy)), not 1.
At x=0,y=1/32 its real part is positive since beta(0)=0 and
|beta(i/32)|<=5/256<pi/2. Compact-uniform convergence then gives
the fixed positive patch required for the test. Permutation
equivariance exchanges target coordinates 1 and 2; F is unchanged
and the volume determinant reverses sign. This verifies (20).

**Cutoff pairing, unequal gaps and weak derivative.** The change
(x,delta,y)↦u has determinant +1. Wedging ddelta with the trace
term Bcal dt wedge dx wedge dy requires two swaps, hence gives
the plus sign in (21). On the selected compact support the other
two cutoff factors are 1 for small epsilon. The two rescaled
transition integrals are

\[
 \int_1^2 2r\eta'(r^2)\,dr=1,
 \qquad\int_{-2}^{-1}2r\eta'(r^2)\,dr=-1.
\]

No monotonicity of eta is required. Uniform positive-time trace
convergence and the bounded rescaled derivative justify DCT on
these fixed intervals. Their combined limit is Bcal^+−Bcal^−,
giving (22). A nonnegative nonzero smooth psi in the positive
patch makes its real part strictly positive.

For the triple estimate, a differentiated pair factor is at most
4||eta'||_infinity/epsilon on epsilon<=|g|<=2epsilon; the other
two factors are bounded. Use one original coordinate as translation
coordinate and two independent gaps (g,h); the linear Jacobian
has absolute determinant 1. In T_rho the g band has total length
at most 2epsilon, h has length at most 2rho, and translation has
length 2a. Thus spatial volume is at most 8a epsilon rho.
Contraction by dg costs at most sqrt(2)||M||. Summing the three
factors and integrating the finite time interval proves (23),
uniformly in all gap ratios. Two overlapping transition bands
have all gaps at most 4epsilon, yielding O(epsilon); equality
boundaries are null and do not affect this estimate. This excludes
a separate concentration on the triple line, not incident face
flux in a fixed neighborhood.

Finally the holomorphic target top form is smooth and closed even
on its zero divisor. Smooth pullback is closed away from the initial
planes. Compact support and the cutoff justify integration by parts.
The L1 bound supplies a majorant for chi_epsilon dphi wedge Theta;
the growing cutoff derivative was handled separately by rescaling,
not by an unjustified DCT. In the established orientation,

\[
 \langle d\Theta,\phi\rangle
       =-\int d\phi\wedge\Theta
       =\lim_{\epsilon\downarrow0}\int\phi\,d\chi_\epsilon\wedge\Theta.
\]

The real test above has nonzero pairing. A null-set change cannot
alter an L1 distribution. This validates the L1 bound and scoped
zero-defect stop, with no collision-flux payment, outer-interface
balance, global assembly, all-degree positivity or Xi transfer.
No solution candidate or new source import is asserted; the existing
source and Mathlib qualifications remain.

## Mathlib

Full matching coverage for the singular reverse spacetime pullback and
its collision defect has not been checked. Reuse C467h/review1018's
supporting `MeasureTheory.tendsto_integral_of_dominated_convergence`
in [MeasureTheory.Integral.DominatedConvergence](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/DominatedConvergence.html).
The uses above have measurable integrands, integrable majorants and
pointwise or compact-uniform convergence. No Lean formalization or
absence of other relevant Mathlib theorems is claimed.
