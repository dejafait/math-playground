# C467n — Joint-corner incompatibility of the nominated smooth adjoint tests

## Hypotheses

Retain C467e/audit1017's actual analytic background and regular coefficient
flow, C467i/audit1025's initial coefficient velocity, C467j/audit1029's
original straight-pair form, and C467l/audit1037 and C467m/audit1041's
actual pair domain and conventions. In particular,

\[
n=3,\quad R=1/4,\quad a=1/16,\quad T_0=1/1920,
\]
\[
\beta(z)=B(1+z)-B(1)-B'(1)z,\quad g=\beta',\quad
H_0=3[B(1)-B'(1)]\in\mathbb R,
\]
\[
H(z)=H_0+\sum_j\beta(z_j),\quad
F(z)=\Delta(z)^2e^{-H(z)},\quad
\Omega=F(z)\bigwedge_{j=1}^3(dz_j/i).
\tag{1}
\]

Here exp B(w)=xi(1/2+sqrt(w))/xi(1/2), with the inherited conjugation
normalization, beta(0)=beta'(0)=0 and |beta''|<40 on |z|<R.
The qualifications from C466z/audit988, C466/audit993 and C466a remain;
no reciprocal-density realization or RH assumption is made.

Use the h>0 pair component with |x|<=X=1/256, h<=H_*=1/128,
|s|<=1, y=x+h. Its actual boundary trace is obtained from the raw
reverse flow

\[
Y_j'=2\sum_{k\ne j}\frac{Y_j-Y_k}{|Y_j-Y_k|^2}
                  -\overline{g(Y_j)},\qquad Y(0,u)=iu,
\tag{2}
\]

as u=(x-delta/2,x+delta/2,y), delta down to zero. Set
m=(Y_1^++Y_2^+)/2, d=(Y_2^+-Y_1^+)/2, w=Y_3^+ and

\[
Z=(m-sd,m+sd,w),\qquad \Psi=Z^*\Omega.
\tag{3}
\]

The orientation is dt wedge dx wedge ds wedge dh; the common minus
normalization is retained. Neither time, flow, weight nor connector
is changed. In particular Z is the specified chain, not a trajectory
of (2) at its interior divisor.

Let b=1/4096 and let f=chi0 be any smooth real function with
0<=f<=1, f=1 on [-b,b], and support contained in (-2b,2b).
The nomination1041/review1042 test requires a real phi smooth on a
neighborhood of this closed parameter piece down to t=h=0, with

\[
\phi(0,x,s,h)=f(x)^2f(x+h),\qquad
d\phi\wedge\operatorname{Re}(-\Psi)=0
\tag{4}
\]

on its positive-time smooth interior, for some common tau>0.
Neighborhood smoothness includes joint smoothness in the original
physical variables (t,x,s,h) at t=h=0. Merely separate smoothness at
t=0 for each h>0, or smoothness only after t is replaced by sqrt(t),
is a weaker condition and is not assumed to suffice.

## Conclusion

No such phi exists for any positive tau. Consequently the full nominated
family of smooth matched nonnegative chamber, pair and triangle tests
does not exist. Already the h>0 pair equation and its initial value
are incompatible with the required joint smoothness; neither the other
five matches nor exterior support or nonnegativity at positive time
is needed for this obstruction.

More precisely, the pair equation and joint smoothness force

\[
f(c)^3(\log f)''(c)=0
\quad\hbox{at every }c\in(-2b,2b)\hbox{ with }f(c)>0,
\tag{5}
\]

which contradicts the specified bump. This is an actual-data local
incompatibility, not a failed sufficient speed estimate or a frozen
background countermodel. The proof below is the result of attempt1043,
validated in the independent conceptual audit1045 below. It does not exclude weaker
test regularity, modified pieces, paid flux identities, or other
mechanisms, and it is not an RH disproof or a complete RH candidate.

## Proof

### Source scope and purpose of this calculation

The ready EXPLORE assessment is
`drafts/literature/2026-11-16-reverse-matched-adjoint-transport-nomination-1041.md`,
separately reviewed at1042. Its primary transport/network comparisons
do not assert existence or nonexistence for (4). This proof uses the
already established actual coefficient flow and original form, then
derives a necessary joint-corner condition for exactly the approved
test. No weak-transport or network theorem is applied outside its
hypotheses. The only additional general tools are Taylor's formula
with integral remainder and the real implicit function theorem at
simple polynomial roots. The latter has nonzero derivatives explicitly
checked below. This calculation is needed because the old stops1000,
1009 and1023 have different hypotheses and do not imply this conclusion.

### Smooth coefficient scaling, with the actual background retained

Change initial coordinates to

\[
c=x+h/3,\quad x=c-h/3,\quad y=c+2h/3.
\tag{6}
\]

The spatial coordinate change has determinant +1. It preserves
smoothness and the orientation. We work locally at any fixed c in
(-2b,2b); all sufficiently small positive h lie strictly inside the
original x and outer-h margins.

Write E(t,c,h),Pi(t,c,h) for the smooth coefficient solution of
C467e, starting at (e(c-h/3,c-h/3,c+2h/3),0), and let

\[
Q_{t,c,h}(v)=v^3-E_1v^2+E_2v-E_3,\qquad
P_t(v)=\Pi_1+(E_1-v)\Pi_2+(v^2-E_1v+E_2)\Pi_3.
\tag{7}
\]

The imaginary roots q_j reconstruct the actual traces by
Y_j^+=P_t(q_j)+iq_j. C467l proves this identification and the
ordering q_1<q_2<q_3 on h>0, including arbitrarily small h.
The coefficients in (7) are smooth on a neighborhood of t=h=0;
P_0 is identically zero, so each coefficient of P_t has a smooth
factor t.

Put h_+(v)=Im g(iv). C467i(13) gives the exact initial velocity

\[
\left.\partial_tE(t,e(q))\right|_0
=(0,-6,-2e_1)+(D_qe)(h_+(q_j))_{j=1}^3.
\tag{8}
\]

This holds at repeated roots by continuity of the regular coefficient
field. To check the required orders explicitly, put
v_j=(-h/3,-h/3,2h/3)_j and write

\[
Q_{t,c,h}(c+z)=z^3+a_2z^2+a_1z+a_0.
\]

At t=0 the coefficients are (0,-h^2/3,-2h^3/27). From (8),

\[
(a_2)_t(0)=-\sum_jh_+(c+v_j),
\]
\[
(a_1)_t(0)=-6-\sum_jv_jh_+(c+v_j)=-6+h^2R_1(c,h),
\]
\[
(a_0)_t(0)=-\sum_j\Big(\prod_{k\ne j}v_k\Big)
                          h_+(c+v_j)=h^2R_0(c,h),
\tag{9}
\]

with smooth R_0,R_1. In the middle line the constant background
cancels because sum v_j=0. In the last line the singular part
of (8) contributes 2e_1-6c=0. These identities retain the actual g.
Taylor's formula therefore gives smooth remainder representations

\[
a_2=tR_2,\quad
a_1=-h^2/3-6t+th^2R_1+t^2\widetilde R_1,
\]
\[
a_0=-2h^3/27+th^2R_0+t^2\widetilde R_0.
\tag{10}
\]

Now set t=rho^2 and h=k rho, with k>0 fixed. Substituting (10)
shows that rho^(-3)Q_(rho^2,c,k rho)(c+rho v) extends smoothly
in (rho,c,k) to rho=0, where it is exactly

\[
q_k(v)=v^3-(k^2/3+6)v-2k^3/27.
\tag{11}
\]

This is a justified leading limit of the original coefficients;
the background remainders in (10) have not been discarded before
their orders are established. The cubic discriminant is

\[
4(k^2/3+6)^3-27(2k^3/27)^2
=8(k^4+18k^2+108)>0.
\tag{12}
\]

Thus its three real roots are simple. The implicit function theorem
applies on a neighborhood of each fixed k>=0 and c under consideration.
Let r(k) be the largest root and let D(k)>0 be half the gap of
the other two roots. Their values are -r/2-D and -r/2+D, with

\[
D^2=k^2/3+6-3r^2/4,\quad
r(0)=\sqrt6,\quad D(0)^2=3/2.
\tag{13}
\]

For k>0, r>0 and implicit differentiation gives

\[
r_k=\frac{(2k/3)(r+k/3)}{3r^2-(k^2/3+6)}>0,
\quad
L:=\frac{r-kr_k}{2}
=\frac{6r}{3r^2-(k^2/3+6)}.
\tag{14}
\]

The denominator is the product of the largest root's two positive
gaps. All root expansions and their derivatives below are locally
uniform for c and k in compact neighborhoods with k>0. No estimate
uniform as k tends to zero will be used.

### Center and shape derivatives in physical time

Let zbar=(Y_1^++Y_2^++Y_3^+)/3 and gamma=w-zbar. Then
m=zbar-gamma/2, and

\[
Z=(\bar z-\gamma/2-sd,\bar z-\gamma/2+sd,\bar z+\gamma).
\tag{15}
\]

The symmetric sum is smooth in the initial coefficients by (7).
In particular zbar(0,c,h)=ic. At fixed c the derivative in h of
e(c-h/3,c-h/3,c+2h/3) vanishes at h=0. Consequently
zbar_h(t,c,0)=0 as well. Smooth division in t and h gives
zbar_h=th times a smooth function.

Summing the original equations (2) cancels all pair interactions.
At time zero, continuity from distinct initial data therefore gives

\[
\bar z_t(0,c,h)=-\tfrac13\sum_j\overline{g(i(c+v_j))}.
\]

Define real a(c), b_0(c) by
a(c)+ib_0(c)=-overline{g(ic)}. Since sum v_j=0, the last
display differs from a+ib_0 by O(h^2). Thus along our scaling,

\[
\bar z_c=i+O(\rho^2),\quad
\bar z_t=a+ib_0+O(\rho^2),\quad
\bar z_h=O(\rho^3).
\tag{16}
\]

The smooth scaled roots from (11) give

\[
\gamma=i\rho r+O(\rho^2),\qquad d=i\rho D+O(\rho^2),
\tag{17}
\]

where the displayed remainders are smooth scaled functions.
Their real parts actually have order rho^3: coefficients of P_t
have a factor t, and subtracting its values at roots, or subtracting
their mean, gives another factor rho. The leading r,D are independent
of c, so gamma_c,d_c=O(rho^2).

All t derivatives in the following display hold c,h fixed, not k.
Indeed differentiating rho R(rho,c,h/rho) yields
(R-kR_k+rho R_rho)/(2rho). It follows that

\[
\gamma_h=ir_k+O(\rho),\quad d_h=iD_k+O(\rho),\quad
\gamma_t=iL/\rho+O(1),\quad d_t=iM/\rho+O(1),
\]
\[
M=(D-kD_k)/2,\qquad \gamma_c,d_c=O(\rho^2).
\tag{18}
\]

This explicitly differentiates the smooth scaled remainders;
derivatives of unspecified pointwise big-O estimates are not assumed.

### All four original coefficients and their real ratios

C467j(14), after the positive coordinate change (6), gives

\[
\Psi=A\,dc\wedge ds\wedge dh+B_c\,dt\wedge dc\wedge dh
     +U\,dt\wedge ds\wedge dh+V\,dt\wedge dc\wedge ds.
\tag{19}
\]

Using (15) in those exact determinant identities gives

\[
A=3iFd(\bar z_c\gamma_h-\bar z_h\gamma_c),\quad
U=3iFd(\bar z_t\gamma_h-\bar z_h\gamma_t),
\]
\[
V=-3iFd(\bar z_t\gamma_c-\bar z_c\gamma_t),\qquad
B_c=3iFs\det\begin{pmatrix}
\bar z_t&\bar z_c&\bar z_h\\
d_t&d_c&d_h\\
\gamma_t&\gamma_c&\gamma_h
\end{pmatrix}.
\tag{20}
\]

For example dz1 wedge dz2 wedge dz3 equals
3 d(zbar) wedge d(sd) wedge d(gamma); division by i in its
three factors multiplies by i. This checks the factor and signs
in (20) directly. The adjoint equation in this orientation is

\[
\operatorname{Re}A\,\phi_t-\operatorname{Re}U\,\phi_c
+\operatorname{Re}B_c\,\phi_s-\operatorname{Re}V\,\phi_h=0.
\tag{21}
\]

Multiplying all forms by -1 leaves (21) unchanged. Fix s in (0,1),
so no division at the pair's s=0 zero is needed. Set

\[
E(c)=e^{-H_0-3\beta(ic)},\qquad
W(k,s)=4s^2D^2(9r^2/4-s^2D^2)^2>0.
\tag{22}
\]

The singleton is above both other roots, so 3r/2>D and the last
strict inequality holds. The exact original Vandermonde and weight give
F=-rho^6 W E+O(rho^7). Also |3beta(ic)|<=60c^2<1/16 on
the relevant c interval; H_0 is real, so Re E>0. Substitution
of (16)–(18) into every expression (20) yields

\[
A=-3\rho^7WE D r_k+O(\rho^8),
\]
\[
U=-3\rho^7WE D r_k(b_0-ia)+O(\rho^8),\quad
V=-3\rho^6WE D L+O(\rho^7),
\]
\[
B_c=3\rho^5WE s(Mr_k-D_kL)+O(\rho^6).
\tag{23}
\]

For the last sign, expanding the determinant in its center row
gives leading term i(Mr_k-D_kL)/rho. All the common factors
in (23), including the actual phase E, are retained. In particular
Re A is nonzero at sufficiently small rho>0 for each fixed k>0
and s in (0,1). Division below is only at these interior points,
not at h=0, s=0 or t=0.

Define the finite actual center drift

\[
v(c)=\frac{\operatorname{Re}[E(c)(b_0(c)-ia(c))]}
                {\operatorname{Re}E(c)}.
\tag{24}
\]

It need not be zero and need not equal b_0. Dividing (21) by Re A
gives phi_t+v_c phi_c+v_s phi_s+v_h phi_h=0, where (23) implies

\[
v_c\longrightarrow-v(c),\qquad
\rho v_h\longrightarrow-\frac{L}{r_k}
=-\frac{9r}{k(r+k/3)},
\]
\[
\rho^2v_s\longrightarrow
-\frac{s}{D}\left(M-\frac{D_kL}{r_k}\right)
=-\frac{s k}{D^2(r+k/3)}.
\tag{25}
\]

For completeness, differentiating (13) gives
D D_k=k/3-3rr_k/4. Therefore

\[
D\left(M-\frac{D_kL}{r_k}\right)
=\tfrac12\left(D^2-\frac{rD D_k}{r_k}\right)
=\tfrac12\left(k^2/3+6-\frac{rk}{3r_k}\right)
=\frac{k}{r+k/3},
\tag{26}
\]

where (14) or the cubic equation proves the last equality.
These are real limits of the original complex weighted determinants,
not quotients of absolute values or modulus-square replacements.

### The necessary corner relation and its contradiction

Suppose a smooth phi satisfying (4) exists. Fix c with f(c)>0 and
use a neighborhood on which f remains positive. Write

\[
P(c)=f(c)^3,\qquad K(c)=f(c)^3(\log f)''(c),\qquad
J(c,s)=\phi_t(0,c,s,0).
\tag{27}
\]

The letter J here denotes only this test derivative. The initial data
in the centered coordinates are

\[
\phi(0,c,s,h)=f(c-h/3)^2f(c+2h/3)
=P(c)+\tfrac13K(c)h^2+O(h^3).
\tag{28}
\]

To check the coefficient, the logarithm of the product is
3 log f(c)+(h^2/3)(log f)''(c)+O(h^3), with zero linear term.
Smoothness, including its mixed derivatives at the joint corner,
then gives along t=rho^2, h=k rho,

\[
\phi_t=J(c,s)+o(1),\quad \phi_c=P'(c)+o(1),\quad
\phi_h=(2/3)K(c)k\rho+O(\rho^2),\quad
\phi_s=\rho^2J_s(c,s)+o(\rho^2).
\tag{29}
\]

The last relation uses that the entire initial function (28) is
independent of s. Taking rho down to zero at each fixed k>0 and
s in (0,1) in (21)/(Re A), using (25) and (29), proves

\[
J-vP'-\frac{6r(k)}{r(k)+k/3}K
 -\frac{s k}{D(k)^2(r(k)+k/3)}J_s=0.
\tag{30}
\]

This necessary identity holds for every k>0. Now let k decrease
to zero in this explicit identity, after the preceding rho limit.
The functions J,J_s,P,K,v are independent of k, and (13) gives

\[
J(c,s)=v(c)P'(c)+6K(c)\quad(0<s<1).
\tag{31}
\]

Thus J_s=0 on that interval. Use k=1 in (30) and substitute (31):

\[
0=\left(6-\frac{6r(1)}{r(1)+1/3}\right)K(c)
=\frac{2}{r(1)+1/3}K(c).
\tag{32}
\]

The required factor is strictly positive because r(1)>0. Hence K(c)=0.
The limits have been sequential and only at positive h,t,s before
forming the necessary relation; no interchange of nonuniform limits
or regular characteristic across a coefficient zero is used.

We have proved (5) at every positive point of f in (-2b,2b).
Let I_f be the connected component of {f>0} containing [-b,b].
On I_f, (5) says (log f)''=0. Its derivative is therefore constant,
and f=1 on (-b,b) forces log f=0 throughout I_f. But I_f has a
finite endpoint inside (-2b,2b), since the support of f is contained
there. Continuity at that endpoint would require both f=1 and f=0,
a contradiction. This uses no monotonicity or special choice of bump.

The contradiction was obtained on one positive-h pair component,
strictly inside its exterior margins, for arbitrarily short positive
times. Imposing the remaining nominated conditions cannot repair it.
The decisive unpaid assumption in any attempted use of those tests
is their joint physical-time smoothness, not an estimate on escape
through an exterior face. Weaker corner regularity would be a changed
target requiring its own source assessment and tested-limit proof.

### Exact algebra check and its limits

Run `python3 scripts/reverse-adjoint/joint-corner-algebra-1043.py`.
The full certificate is
`scripts/reverse-adjoint/joint-corner-algebra-1043.json`.
All 14 exact rational-polynomial checks pass, with every required
residual equal to zero: the four spatial/mixed determinants, four
wedge signs, cubic discriminant, two root-velocity identities,
the obstruction factor and two initial Taylor coefficients.
The complete check records were inspected. The handwritten identities
above supply the proof; the script checks their algebra, not the
analytic hypotheses, differentiated remainder bounds, sequential
limits, or this conclusion's independent conceptual validity.

### Independent conceptual audit — 16 November 2026, step1045

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-16-reverse-joint-smooth-adjoint-audit-nomination-1043.md`,
separately approved at1044. This REPRODUCTION audit checks (8)–(32)
under the stated hypotheses. It neither constructs weaker tests nor
asserts originality. Direct mathematical inputs in the DAG are unchanged.
The following verifies their uses and the limiting argument; the
algebra certificate alone would not do so.

**Regularity class and sources.** Nomination1041 asks for smooth tests
on neighborhoods of the closed parameter pieces. C467m(18)'s tested
identity explicitly uses a neighborhood of [0,T] x [-X,X] x [-1,1]
x [-H_*,H_*]. The positive-h piece's one-sided closure includes
h=0 and t=h=0. Thus the nominated class supplies a smooth extension
there in physical t,x,s,h, even if the two h components have separate
tests. Only the positive component's extension is used. C467n makes
this hypothesis explicit in (4); a reading requiring smoothness merely
on h>0 would be a weaker target not settled here. The coordinate
change (6) is invertible and orientation preserving. For c in
(-2b,2b), x=c-h/3 and y=c+2h/3 stay strictly within the initial
and exterior margins for all sufficiently small positive h.

For smooth simple roots and smooth remainder functions, reuse
Karl-Hermann Neeb, *Manifolds and Transformation Groups*, WS05,
[Theorems I.1.9 and I.1.12, printed pp5–6](https://www.math.fau.de/wp-content/uploads/2024/01/mfkt.pdf).
The first assumes a C^k map on an open Euclidean set and invertible
derivative in the solved variable, and permits k=infinity. The second
is Taylor's integral formula along a segment within that domain.
Brian Conrad, *Higher derivatives and Taylor's formula via multilinear
maps*, [Theorem5.1, formulas(9)–(11) and proof, pp13–15](https://math.stanford.edu/~conrad/diffgeomPage/handouts/higherderiv.pdf),
also supplies the parameter-dependent integral formula. C467e's
regular coefficient field is analytic on an open neighborhood of the
initial discriminant, by its fixed-contour formula and audit1017.
Its cited Teschl smooth-flow theorem therefore supplies every finite
mixed derivative used here, also for small negative coefficient time.
This does not extend the singular physical root flow through a
collision. The implicit function theorem is used only after (12)
proves simplicity of the scaled roots.

**Coefficient orders and actual labels.** In C467i(13), each unordered
singular pair contributes (0,-2,-2q_l) to (E_1',E_2',E_3').
Their sum is (0,-6,-2e_1); the imaginary background velocity is
+Im g(iq_j). Both sides extend continuously through initial repeated
roots. This identity holds throughout C467e's initial coefficient
domain; C467i's later separated-patch estimates are not needed for it.

For the centered polynomial, a_2=3c-E_1,
a_1=3c^2-2cE_1+E_2 and a_0=c^3-c^2E_1+cE_2-E_3.
Their singular initial derivatives are 0,-6,0. The background terms
are exactly (9). Writing
h_+(c+v)=h_+(c)+v integral_0^1 h_+'(c+theta v)dtheta
shows that sum v_j h_+(c+v_j) has a smooth factor h^2.
Each product v_k v_l already has that factor. Integral Taylor
remainders in t then prove (10) with smooth functions. The scaled
polynomial has the explicit smooth extension

\[
v^3+\rho R_2v^2+
[-k^2/3-6+\rho^2(k^2R_1+\widetilde R_1)]v
-2k^3/27+\rho(k^2R_0+\widetilde R_0),
\]

where the remainders are evaluated at (rho^2,c,k rho). The
discriminant (12) is positive for all real k. Locally at each
k>=0 its three simple real roots continue smoothly in (rho,c,k).
For rho>0 their ordering agrees with C467l(12) and its actual trace
identification: the h>0 singleton is the largest root. No branch is
chosen across the unscaled initial discriminant. The derivative of
q_k at its largest root is positive; implicit differentiation proves
(14), with r_k>0 for k>0. At k=0, the roots are -sqrt(6),0,sqrt(6),
so r(0)=sqrt(6) and D(0)^2=3/2.

**Physical-time derivatives.** The exact symmetric sum is
3 zbar=3 Pi_1+2 E_1 Pi_2+E_2 Pi_3+i E_1. It is smooth in
(t,c,h), although the roots need not be. The h derivative of the
initial coefficients vanishes at h=0, hence zbar_h(t,c,0)=0.
Also zbar_h(0,c,h)=0. Two integral divisions give zbar_h=th R
with R smooth. Summing the distinct physical equations cancels all
interaction pairs. Continuity of the smooth symmetric sum extends
its initial velocity to repeated data. Its difference from
a(c)+i b_0(c) is O(h^2+t), since sum v_j=0. This proves (16).

The scaled roots give gamma=i rho r+rho^2 G and
d=i rho D+rho^2 D_1, with G,D_1 smooth in (rho,c,k).
Each coefficient of P_t has a smooth factor t; polynomial
subtraction of its values at roots gives a further factor rho.
Thus the real shape remainders are rho^3 times smooth functions.
Since r,D are independent of c, gamma_c,d_c=O(rho^2).
Holding c fixed, and holding t fixed for partial_h or h fixed
for partial_t, the exact operators are

\[
\partial_h=\rho^{-1}\partial_k,\qquad
\partial_t=(2\rho)^{-1}\partial_\rho
                  -k(2\rho^2)^{-1}\partial_k.
\]

For a smooth R, partial_t(rho^2 R)=R-(k/2)R_k+(rho/2)R_rho
and partial_h(rho^2 R)=rho R_k. These prove every order in (18),
without differentiating unspecified big-O estimates. All bounds here
are local at fixed k>0; no uniform control down to k=0 is required.

**Four minors, actual phase and division.** Expansion of (15) gives
dz_1 wedge dz_2 wedge dz_3=3 d(zbar) wedge d(sd) wedge d(gamma).
Multiplication by i^(-3)=i proves all four identities (20), including
their signs. Wedge multiplication by dphi gives +,-,+,- in (21).
The common minus normalization cancels from this zero equation.

Fix s in (0,1). Since D>0 and 3r/2>D, W>0. The six factors
of i in the squared Vandermonde give -rho^6 W. The weight tends
to the actual E(c). The bound |beta''|<40 and its two zero initial
Taylor coefficients imply |3beta(ic)|<=60c^2<1/16. As H_0 is
real, Re E>0. This proves the stated leading weighted factor F.

The common factor 3iFd is 3rho^7 W E D+O(rho^8). The brackets
for A,U,-V in (20) have leading terms -r_k,
(-b_0+i a)r_k, and L/rho, respectively. For B_c, the center's
c column is i+O(rho^2); its cofactor contributes
i(Mr_k-D_kL)/rho+O(1). The other center columns contribute
only O(1) or smaller errors. Thus all four orders and coefficients
in (23) hold. Re A has nonzero leading coefficient
-3 W D r_k Re E for each fixed k>0,s in (0,1). Division is
legitimate for sufficiently small positive rho and only at those
interior points.

Real parts retain the drift (24), yielding (25) with its displayed
signs. Independently, DD_k=k/3-3rr_k/4 and L=(r-kr_k)/2 give
the first two equalities of (26); substitution of (14) and q_k(r)=0
gives the last. No quotient of moduli, suppressed background phase,
or division by another possibly zero real coefficient is used.

**Test derivatives and successive limits.** Where f(c)>0 choose a
smaller c neighborhood on which log f is smooth. Integral Taylor
expansion gives (28) with a smooth h^3 remainder. Joint smoothness
gives exactly phi(t,c,s,h)=phi(0,c,s,h)+t G_0(t,c,s,h), with
G_0 smooth and G_0(0,c,s,0)=J(c,s). Differentiating proves (29):
in particular phi_s=t partial_s G_0, and phi_h has an O(t)
correction to its initial derivative. Its O(rho^2) remainder meets
a divided coefficient O(rho^(-1)) and vanishes. Also phi_s/rho^2
tends to J_s. The other coefficients have finite limits. Therefore
(30) holds for every fixed k>0, c and s in (0,1).

Only this established finite identity is then sent to k=0. Its
coefficients tend to 6 and 0 as stated in (31), while J,J_s,P,K,v
are independent of k. Hence J is constant in s and J_s=0. Taking
k=1 leaves the strictly positive coefficient 2/(r(1)+1/3) of K,
proving (32) and (5). No uniform-in-k remainder or quotient at k=0
enters the argument. On the positive component containing [-b,b],
log f is affine and its central flat value forces it to be zero.
Compact support gives a finite endpoint inside (-2b,2b), contradicting
continuity of f there. No monotonicity of f is assumed.

**Verification and verdict.** Replayed the unchanged exact-algebra
script and inspected the complete checks with
`python3 ../scripts/loop/inspect_json.py scripts/reverse-adjoint/joint-corner-algebra-1043.json --pointer /checks --full`.
All 14 residuals are exactly zero, with no failures. The analytic
checks above discharge the obligations outside that certificate.
The result passes with unchanged hypotheses, constants and direct
inputs. This validates the local obstruction of attempt1043; it
is not a new result beyond that written claim or a resolution of RH.
Weaker corner regularity, weighted weak tests, global assembly,
density realization, all degrees and Xi signs remain unresolved.
The older stops retain their original scopes.

## Mathlib

Full matching coverage for this actual-data joint-corner obstruction
has not been checked; neither absence nor formal verification is
asserted. The supporting mathematical tools used here are finite
dimensional smooth coefficient flow from C467e, the real implicit
function theorem at the explicitly simple cubic roots, Taylor's
formula, determinant expansion and elementary one-variable calculus.
The previously checked dominated-convergence support for C467m does
not prove this obstruction or construct less regular tests. No new
Mathlib theorem locator is claimed from an unperformed lookup. Audit1045
is an informal analytic verification, not a Lean formalization.
