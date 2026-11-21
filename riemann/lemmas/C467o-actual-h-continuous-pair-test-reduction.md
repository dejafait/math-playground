# C467o — Conditional admissibility and physical-coordinate reduction for the continuous pair test

## Hypotheses

Retain C467e/audit1017, C467l/audit1037 and C467m/audit1041's
actual positive-h pair, analytic background, raw physical time and
orientation. In particular n=3, R=1/4, a=1/16, T_0=1/1920,
X=1/256, H_*=1/128, and

\[
\beta(z)=B(1+z)-B(1)-B'(1)z,\quad g=\beta',\quad
H=H_0+\sum_j\beta(z_j),\quad H_0=3[B(1)-B'(1)]\in\mathbb R,
\]
\[
F=\Delta^2e^{-H},\qquad \Omega=F\bigwedge_{j=1}^3(dz_j/i).
\tag{1}
\]

Here exp B(w)=xi(1/2+sqrt(w))/xi(1/2), beta(0)=beta'(0)=0,
and |beta''|<40 on |z|<R. The qualifications inherited from
C466z/audit988, C466/audit993 and C466a remain; no reciprocal-density
realization or RH premise is supplied.

For the actual ordered trace from initial (x,x,x+h), h>0, write
Y_j=P(q_j)+iq_j, q_1<q_2<q_3, using the regular coefficient flow
(E,Pi) and reconstruction polynomial of C467e. Put

\[
m=(Y_1+Y_2)/2,\quad d=(Y_2-Y_1)/2,\quad w=Y_3,\quad
Z=(m-sd,m+sd,w),\quad Q=\operatorname{Im}Z.
\tag{2}
\]

On the box K=[0,tau] x [-X,X] x [-1,1] x [0,H_*], use the
unmodified form and the dt dx ds dh orientation:

\[
\Psi=Z^*\Omega=A\,dx\,ds\,dh+B_c\,dt\,dx\,dh
                  +U\,dt\,ds\,dh+V\,dt\,dx\,ds.
\tag{3}
\]

Wedges are understood in (3). A common minus sign on the entire
form leaves all statements about its adjoint unchanged. Choose tau>0
no larger than the common times in C467e,l,m; a further reduction
specified below is allowed.

Let f be any smooth real function with 0<=f<=1, f=1 on
[-b_0,b_0], and support in (-2b_0,2b_0), where b_0=1/4096.

For the first conclusion, let phi be real and continuous on K, smooth locally
where t,h>0 with the nominated neighborhood extensions at fixed x,s
endpoints, and suppose

\[
\int_{K^\circ}(|A\phi_t|+|U\phi_x|+|B_c\phi_s|+|V\phi_h|)<\infty.
\tag{4}
\]

The integration here means the full finite box with t,h>0; its fixed
boundary faces have zero four-dimensional measure. No derivatives at
t=0 or h=0 are assumed. The absolute values in (4) concern the
complex products, not only their real parts.

## Conclusion

The complete positive-h component of C467m(18) has its stated limit
for arbitrary relative rates epsilon,eta down to zero. Its lower-time
term is zero, its inner term is the actual one-sided trace
integral phi(t,x,s,0)V_0^+(t,x,s) dt dx ds, and every other face
is retained. There is no additional term at t=h=0. In particular,
for the exact nomination1045 test, the cutoff identity follows from
continuity and (4); it is not a further existence assumption.

There is also an exact local reduction useful for seeking that test.
After reducing the common time once, (x,s,h) -> Q is a local real
diffeomorphism at every t>0,h>0, including s=0 and the fixed x,s
endpoints. In these charts write Z=p(t,Q)+iQ, with real p, and set

\[
M=I_3-iD_Qp,\qquad u=-iM^{-1}p_t,\qquad
\kappa=F(p+iQ)\det M.
\tag{5}
\]

M is invertible on these charts. For s!=0 define

\[
b=-\frac{\operatorname{Re}(\kappa u)}{\operatorname{Re}\kappa}.
\tag{6}
\]

This real auxiliary velocity has a smooth extension through s=0
at fixed positive t,h, proved by explicit factorization below.
Where s!=0, the original adjoint for phi=chi(t,Q(t,x,s,h)) is
exactly

\[
\chi_t+b\cdot D_Q\chi=0.
\tag{7}
\]

At s=0 all four original coefficients remain zero. A smooth chi
satisfying the extended (7) is a sufficient construction there;
the original current is never replaced or divided at its zero.

Here is one sufficient, not necessary, quantitative condition. If
such a chi is smooth on neighborhoods of the positive-time physical
images, has uniformly bounded chi_t and D_Q chi there, and its
composition is continuous on K with initial value
f(x)^2 f(x+h), then (4) holds. If also 0<=chi<=1, its composition
meets every condition of nomination1045. For example the correct
initial value would follow from a continuous ambient extension with
chi(0,Q)=f(Q_1)f(Q_2)f(Q_3), where f is the nominated bump and
bump radius b_0=1/4096. This paragraph does not assert the existence
of that extension or a solution of (7).

These partial reductions from attempt1047 are validated by the independent
conceptual audit1049 below. This lemma alone establishes no admissible
adjoint or incompatibility in the nominated continuous class. There is no
claim that the auxiliary field or its derivatives remain bounded
at h=0 or t=h=0. No full matching, exterior flux payment, global
assembly, realization, all-degree positivity or Xi transfer follows.

## Proof

### Source scope and standard inputs

Use the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-16-reverse-continuous-pair-adjoint-nomination-1045.md`,
separately reviewed at1046. It did not supply a matching continuous
adjoint theorem. The following is a partial attempt at its exact
target. It uses C467m's already proved coefficient and full-face
estimates; it imports no unverified weak-transport trace theorem.

For every positive-cutoff box, use Brian Conrad, *Math396. Stokes'
theorem with corners*, [Theorem1.1 and coordinate proof, pp1–3](https://math.stanford.edu/~conrad/diffgeomPage/handouts/stokescorners.pdf).
For limits use John K. Hunter, *Measure Theory*, [Chapter4,
Theorem4.24, pp49–50](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf).
These precise imports and their applicable smooth-box/complex-component
conventions are already assessed in C467m/audit1041 and reused by
review1046. They are not reproved. The difference here is that
bounded derivatives of the test are replaced by the four L1 products
in (4), while continuity supplies the face values. The real inverse
function theorem below is used only with a displayed positive Jacobian.

### The whole cutoff identity for the continuous test

Let 0<T<=tau and 0<epsilon<T, 0<eta<H_*. All maps and phi are
smooth on a neighborhood of the positive-cutoff box. The original
holomorphic top form is closed, including its divisor. Stokes gives

\[
\begin{split}
&\int_{[\epsilon,T]\times[-X,X]\times[-1,1]\times[\eta,H_*]}
 (A\phi_t-U\phi_x+B_c\phi_s-V\phi_h)\,dt\,dx\,ds\,dh\\
={}&\int_{[-X,X]\times[-1,1]\times[\eta,H_*]}
       [\phi A]_{t=\epsilon}^{T}\,dx\,ds\,dh\\
&+\int_{[\epsilon,T]\times[-X,X]\times[\eta,H_*]}
       [\phi B_c]_{s=-1}^{1}\,dt\,dx\,dh\\
&-\int_{[\epsilon,T]\times[-1,1]\times[\eta,H_*]}
       [\phi U]_{x=-X}^{X}\,dt\,ds\,dh\\
&-\int_{[\epsilon,T]\times[-X,X]\times[-1,1]}
       [\phi V]_{h=\eta}^{H_*}\,dt\,dx\,ds.
\end{split}
\tag{8}
\]

This is the positive-h restriction of C467m(18), not an identity
with the s endpoints or outer faces removed. Its signs follow from
the orientation dt dx ds dh. A common minus normalization multiplies
both sides by -1. If smoothness at the upper time and h endpoints is
understood only one-sided, first use T<tau and H'<H_* in (8), then
increase these endpoints. The bulk L1 assumption, continuity of phi
and the coefficient/face bounds (9) justify that passage. No extension
of phi beyond those two faces is needed.

Let M_phi=sup_K |phi|<infinity. C467m(5) gives, uniformly on the
whole box and its prescribed faces,

\[
|A|+|U|+|V|\le C s^2t^{3/2},\qquad |B_c|\le C|s|^3\sqrt t.
\tag{9}
\]

For the bulk, the sum in (4) is a fixed integrable majorant. The
two cutoff indicators converge almost everywhere along every joint
sequence, so dominated convergence applies separately to all four
complex products. No derivatives of shrinking cutoffs are used.

The entire lower-time integral in (8) is bounded by
C M_phi epsilon^(3/2), uniformly in eta. The upper-time integral
converges by boundedness of phi A on its fixed T face. For the x
faces and outer h face, (9) times M_phi gives an integrable
t^(3/2) majorant; for the s endpoints it gives an integrable sqrt(t)
majorant. Their actual prescribed-face bounds, rather than estimates
on almost-everywhere slices alone, justify all these limits with
the two indicators.

It remains to check the moving inner face. C467m's entire-face result
is V(t,x,s,eta) -> V_0^+(t,x,s) in L1(dt dx ds) on [0,T],
with a common t^(3/2) majorant. Uniform continuity of phi on K gives

\[
\sup_{t,x,s}|\phi(t,x,s,\eta)-\phi(t,x,s,0)|\longrightarrow0.
\tag{10}
\]

Thus the L1 difference between phi_eta V_eta and phi_0 V_0^+ is at
most the supremum in (10) times ||V_eta||_1, plus
M_phi ||V_eta-V_0^+||_1. Both tend to zero. Removing [0,epsilon]
from either entire-face integral costs at most
C M_phi epsilon^(5/2), uniformly in eta. This proves convergence
along arbitrary relative cutoff rates to the inner term stated above,
with its positive sign from the last line of (8). Every term of the
exact cutoff identity has now been treated. Its limit leaves no
unaccounted corner distribution. This proves the first conclusion.

### Nondegeneracy of the physical imaginary coordinates

Temporarily use independent x,y with y=x+h. Write
I=E_1(t,e^0), e^0=e(x,x,y), q=q_3, a_q=(I-q)/2 and
D=(q_2-q_1)/2>0. The underlying root polynomial is
Q_t(v)=v^3-E_1v^2+E_2v-E_3, distinct from the vector Q in (2).
Then

\[
Q=(a_q-sD,a_q+sD,q).
\tag{11}
\]

Let D_E be the derivative of E_t with respect to e^0, and write
L(q)=(q^2,-q,1), B_0=(1,2x,x^2), V_0=(0,1,x). The initial
coefficient derivatives obey

\[
\partial_y e^0=B_0,\qquad \partial_x e^0=2B_0+2hV_0.
\tag{12}
\]

Subscripts B_0,V_0 below mean directional derivatives in e^0 with
those vectors held fixed. The simple-root formula gives
q_W=L(q)D_E W/Q_t'(q). Consequently

\[
(a_q)_x q_y-(a_q)_y q_x
=\tfrac12(I_xq_y-I_yq_x)=\frac{hN_I}{Q_t'(q)},
\]
\[
N_I=I_{V_0}L(q)D_EB_0-I_{B_0}L(q)D_EV_0.
\tag{13}
\]

At t=0, D_E=I_3, I_{V_0}=0 and I_{B_0}=1, so N_I=q-x.
Regard q as an independent real variable in [-r_*,r_*] in this
expression. Smooth coefficient dependence on a compact neighborhood
of the initial set bounds its t derivative by a finite K. Hence
|N_I-(q-x)|<=Kt uniformly, even at h=0. C467l(14) gives the actual
root bound q-x>=h/3+sqrt(t)/2. Reducing the common time so that
2K sqrt(t)<=1/2 therefore ensures

\[
N_I\ge\tfrac12(q-x)>0.
\tag{14}
\]

The extreme-root derivative Q_t'(q)=(q-q_1)(q-q_2) is positive.
Taking the determinant in (11) gives exactly

\[
\det D_{(x,s,y)}Q=2D\big((a_q)_xq_y-(a_q)_yq_x\big)
                =\frac{2DhN_I}{Q_t'(q)}>0.
\tag{15}
\]

The change y=x+h has determinant +1, so (15) is also the required
(x,s,h) Jacobian. It is independent of s and stays positive at s=0.
All actual coefficient and root charts extend locally at the fixed
x,s endpoints. Thus the real inverse function theorem supplies the
claimed local (t,Q) charts, without a global injectivity assertion.

### The original real adjoint in those charts

In a chart, dZ/i=M dQ-i p_t dt=M(dQ+u dt). Let
vol_Q=dQ_1 wedge dQ_2 wedge dQ_3. Direct exterior multiplication gives

\[
\Psi=\kappa\,\mathrm{vol}_Q
       +dt\wedge\iota_{\kappa u}\mathrm{vol}_Q.
\tag{16}
\]

To justify invertibility and the zero explicitly, put
v=(Q_2-Q_1)/2=sD and eta_0=-Pi_2-q_3 Pi_3. The reconstruction
polynomial gives p_2-p_1=2v eta_0. With G_1=Z_3-Z_1 and
G_2=Z_3-Z_2, the original Vandermonde therefore gives

\[
F=v^2\widehat F,\qquad
\widehat F=-4(1-i\eta_0)^2G_1^2G_2^2e^{-H(Z)}.
\tag{17}
\]

Every G_j has positive imaginary part on this positive-h piece,
including s=0 and the endpoints. Thus the displayed smooth factor
widehat F is nonzero. Before assuming M invertible, spatial
pullback alone gives
A=F det M det D_(x,s,h)Q. The exact sector factorization in
C467l(27)–(30) says that -A/s^2 has strictly positive real part,
including its explicit smooth value at s=0. By (15) and D>0,

\[
\widehat\kappa:=\widehat F\det M,
\qquad
\operatorname{Re}(-\widehat\kappa)>0
\tag{18}
\]

at all these points, since A=s^2D^2 widehat kappa det DQ.
This proves det M!=0, including s=0, and hence validates (5),(16).
The formula

\[
b=-\operatorname{Re}(\widehat\kappa u)\big/
                         \operatorname{Re}\widehat\kappa
\tag{19}
\]

is smooth on each positive-t,h chart and agrees with (6) off s=0.
It is only an auxiliary formula for a sufficient construction; (3)
and its zero coefficients are retained everywhere.

Wedge dchi with the real part of (16). The result is

\[
\big(\operatorname{Re}\kappa\,\chi_t
 -\operatorname{Re}(\kappa u)\cdot D_Q\chi\big)
              dt\wedge\mathrm{vol}_Q.
\tag{20}
\]

For s!=0, Re kappa!=0 and (20) proves (7) with precisely the
sign in (6). A common minus sign changes neither equation. At s=0
the original form is zero by (17), so the original undivided adjoint
holds there directly, without evaluating a zero denominator. No
modulus-square equation has replaced the real complex-weighted one.

### A sufficient physical derivative estimate for all four products

C467l gives both adjacent imaginary gaps at least sqrt(t). At each
root, |Q_t'(q_j)| is therefore at least t. All derivatives E_r,
r in {t,x,h}, are bounded by smooth coefficient dependence on the
compact initial set. Differentiating the root polynomial yields

\[
|(q_j)_r|\le C/t\quad(r=t,x,h).
\tag{21}
\]

This is a deliberately coarse uniform estimate, also valid for
arbitrarily small h>0. From (11) and |s|<=1 it gives
|Q_r|<=C/t for these three derivatives. On the other hand
Q_s=(-D,D,0), and C467m(9) gives D<5sqrt(t)/2. Therefore

\[
|Q_t|+|Q_x|+|Q_h|\le C/t,\qquad |Q_s|\le C\sqrt t.
\tag{22}
\]

Suppose |chi_t|+|D_Q chi|<=K_chi on the relevant images.
The chain rule for phi=chi(t,Q), followed by (9),(22), gives,
after reducing tau<=1,

\[
|A\phi_t|+|U\phi_x|+|V\phi_h|
       \le C K_{\chi}s^2\sqrt t,\qquad
|B_c\phi_s|\le C K_{\chi}|s|^3t.
\tag{23}
\]

These are integrable on the full finite box and prove (4). They
bound the complex products separately. Continuity and the initial
trace in the sufficient hypothesis then allow the first part of the
proof to apply, giving every face of the required identity. The
range condition 0<=chi<=1 transfers directly to phi.

### What the attempt leaves unresolved

At any fixed t>0, (15) has a simple factor h. The other factors
extend smoothly and positively to h=0 on that positive-time slice,
by the ordered root charts and (14). Consequently this coordinate
change does not itself control its inverse as h tends to zero.
In particular, p_t in (5) is a derivative at fixed Q, not at fixed
(x,s,h). Smoothness and boundedness of the original coefficient
flow cannot be substituted for a bound on this derivative or on
D_Q b. Nor does the factorization at s=0 pay for the h=0 face.

No common backward characteristic construction through the degenerating
h boundary, no uniform physical derivative bound for its transported
bump, and no alternative sufficient weighted bound have been proved
in this attempt. The initial product on an ambient Q space is only
candidate data. A failed estimate in this sufficient class would not
exclude the larger nominated continuous class. C467n's joint-smooth
stop remains a contrast, not a premise that rules out these tests.

### Independent conceptual audit — 16 November 2026, step1049

This REPRODUCTION audit uses the invocation-start EXPLORE assessment
`drafts/literature/2026-11-16-reverse-continuous-pair-adjoint-nomination-1045.md`
(review1046), unchanged. It checks this reduction as an essential input
to the same continuous-test target. The C467e/l/m hypotheses, source
imports, original positive-h connector and common minus normalization
are retained. C467p is not used to prove any assertion of this lemma.

**Every cutoff term.** On each strictly positive cutoff box the actual
map and test are smooth, including the zero at s=0. Closedness of the
holomorphic top form holds on the whole polydisc. Conrad's cited
Stokes theorem thus applies separately to real and imaginary parts.
Expanding the wedge gives A phi_t-U phi_x+B_c phi_s-V phi_h;
the outward boundary signs are exactly those in (8). In particular
the inner h face contributes +phi V, and all s and x faces remain.

Assumption (4) supplies four integrable complex-product majorants,
not merely an integrable signed sum. Their products with the two
cutoff indicators converge by the cited DCT. C467m/audit1041 provides
pointwise coefficient bounds on each prescribed face, so it is valid
to use them there. The lower t face is O(epsilon^(3/2)) uniformly
in eta; the fixed x and outer h faces use t^(3/2), and the s faces
use sqrt(t). The upper t face is bounded at its fixed positive time.
If the upper endpoints first approach tau,H_*, the same bounds and
continuity justify that preliminary passage; no derivative at either
endpoint is required.

For the moving h face, C467m gives the full [0,T] L1 convergence
V_eta to V_0^+, not just convergence away from t=0. The difference
of the tested full-face integrals is bounded by

    ||phi_eta-phi_0||_infinity ||V_eta||_1
       + ||phi||_infinity ||V_eta-V_0^+||_1.

Compact continuity and the uniform L1 bound make this tend to zero.
Deleting its time interval [0,epsilon] costs O(epsilon^(5/2))
uniformly in eta, and the limit face has the same bound. Consequently
the limit is independent of the relative cutoff rates. These are all
terms of (8); no extra corner term remains in this tested identity.
This conclusion does not assert a removability theorem for other
tests or an ambient extension of the current.

**Coordinate and sign checks.** With y held independent of x,
e_y=B_0 and e_x=2B_0+2hV_0. Substitution in
(I_x q_y-I_y q_x)/2 gives h N_I/Q'(q), with exactly the numerator
in (13). At time zero that numerator is q-x. Its O(t) error is a
smooth-coefficient error uniform with q treated independently;
C467l's q-x>=h/3+sqrt(t)/2 absorbs it on one common time.
The determinant of (a_q-sD,a_q+sD,q) is
2D((a_q)_x q_y-(a_q)_y q_x): the differentiated D terms cancel.
Changing y to x+h preserves its sign. This verifies the positive
Jacobian at every s, including s=0, and at fixed endpoint extensions.

Spatial pullback gives A=F det(M) det(DQ) even before invertibility
of M is known. Factoring F=v^2 widehat F and using C467l's exact
sector at its zero then gives Re(-widehat F det M)>0. Thus M is
invertible also at s=0. Exterior multiplication of dQ+u dt yields
vol_Q+dt wedge i_u vol_Q; wedging dchi has the minus spatial term
in (20). The velocity is therefore the negative real ratio (19).
Only the auxiliary v^2 factor is canceled; the original form and
adjoint vanish undivided at s=0. No phase or algebraic square is
replaced by its modulus.

**Weighted derivative sufficiency.** At all three actual roots the
two root separations give |Q'(q_j)|>=t. Smooth coefficient bounds
therefore give the coarse C/t estimates at fixed initial parameters.
The s derivative instead has size alpha/2<=5sqrt(t)/2. Combining
these with bounded chi_t,D_Q chi and C467m's complex bounds proves
the two integrable estimates (23), separately for every product.
This implication is conditional on the physical derivative bounds;
it neither proves nor assumes those bounds for an unknown test.

All conclusions of C467o pass with the stated hypotheses. Its direct
mathematical inputs remain C467e, C467l and C467m. This is validation
of the existing local reduction, not a new existence theorem, source
novelty claim, global matching result or RH candidate.

## Mathlib

Full matching coverage for this actual coordinate reduction or the
continuous adjoint remains unchecked. The supporting locator reused
from C467m is
[`MeasureTheory.tendsto_integral_of_dominated_convergence`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/DominatedConvergence.html).
It does not supply the coefficient/face estimates, positive Jacobian,
actual transport field or existence of its test. No new Mathlib
search, matching theorem assertion or formal verification is claimed.
