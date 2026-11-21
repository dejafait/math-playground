# C467 — A quadratic corner layer reverses the lower chamber incidence

## Hypotheses

Retain C467z's actual chamber, coefficient flow E_t, regular physical
adjoint b_c and exact diagnostic D, with C467e's analytic coefficient
Hamiltonian. In particular n=3, R=1/4, a=1/16, T_0=1/1920,
X=1/256, b_*=1/4096 and H_*=1/128. The actual data are

\[
\beta(z)=B(1+z)-B(1)-B'(1)z,\quad g=\beta',\quad
H=H_0+\sum_j\beta(z_j),\quad F=\Delta^2e^{-H},\quad
\Omega=F\bigwedge_j(dz_j/i).
\tag{1}
\]

B is the conjugation-normalized logarithm of
xi(1/2+sqrt(w))/xi(1/2), H_0 is real and |beta''|<40 on |z|<R.
Use C467u's qualified actual signs, including its L018/L021/L024
paired-product and C466a finite-zero inputs. Specifically its cited
finite verification accounts for the positive ordinates through 100
on the line and isolates the first in (14,15); these are external
inputs, not certificates independently replayed here. The source is
Suvrit Sra, *On some positivity properties of the Riemann Xi function*,
[W_pr5z5huy_v1, section 2.1, (6)–(8)](https://hub.valency.io/works/W_pr5z5huy_v1),
with the qualifications recorded in C467u. No assumption about the
higher zeros lying on the line is added.

Keep raw time, the original divisor and common minus normalization.
The candidate scalar class is precisely C467z(2): continuous up to
initial/collision faces, smooth on the positive-time distinct interior,
initial product product_j f(u_j), where f is any fixed smooth real
function in [0,1], equal to one on [-b_*,b_*] and supported in
(-2b_*,2b_*). Neither f nor beta is assumed even. C467y's lower
selection remains the particular phi_p of C467p.

Write

\[
G(v)=\operatorname{Re}g(iv),\quad J(v)=\operatorname{Im}g(iv),
\quad \theta(x)=-3\operatorname{Im}\beta(ix),
\quad d(x)=-12G''(x)\tan\theta(x).
\tag{2}
\]

Here G is the background derivative, not the initial product denoted
G in C467z. Set e_x=e(x,x,x), L(x)=(x^2,-x,1). The diagnostic is
C467z(14), and the backward squared lower-gap derivative at a
separated lower face is exactly nu=-4D/h.

## Conclusion

On one sufficiently small common time interval the diagnostic has a
smooth coefficient extension through t=h=0, and uniformly for
|x|<=X, 0<=h<=H_* it satisfies

\[
D(t,x,0)=d(x)t^2+O(t^3),\qquad
\partial_hD(t,x,h)=-2+O(t),
\]
\[
D(t,x,h)=-2h+d(x)t^2+O(th+t^3).
\tag{3}
\]

The constants are finite on these fixed compact boxes. C467u gives
d(x)>0 for 0<x<=X and d(x)<0 for -X<=x<0. For each compact
K_+ contained in (0,X], after a time reduction depending on K_+,
there is a unique h_g(t,x) in (0,H_*) for t>0, x in K_+, with

\[
D(t,x,h_g)=0,\qquad h_g(t,x)=\tfrac12d(x)t^2+O(t^3).
\tag{4}
\]

D is positive below h_g and negative above it. Hence on
0<h<h_g the actual lower collision face is **backward outward**:
the inverse coefficient characteristic immediately leaves the
three-real-root region. Nearby interior backward characteristics
hit that collision side before time zero. Above h_g the local
backward normal incidence is inward. For each compact K_- contained
in [-X,0), D<0 for all 0<h<=H_* on a sufficiently small common
time interval, also giving local backward inward incidence there.
No classification at x=0 or global earlier-time confinement in the
inward portions is asserted by this result.

Every allowed f has a point x_0 in (b_*,2b_*) with f'(x_0)<0
and 0<f(x_0)<1. The outward layer therefore occurs on a nonconstant
part of the actual initial bump, on arbitrarily short time horizons.
Uniform backward initial access on the whole nominated face is false.
This stops that mechanism for making C467z's T_c a necessary trace
everywhere. It does **not** prove that T_c differs from phi_p, exclude
a continuous matching scalar, or construct compatible incoming data.
The separated necessary trace in C467z is unchanged.

This is attempt1081's local negative result, validated together with
its C467z input by independent conceptual audit1083 below. It is not a certified
novelty claim or an RH candidate. Exterior payment, other interfaces,
global assembly, realization, all degrees and Xi transfer remain open.

## Proof

### Source scope and the smooth coefficient diagnostic

The unchanged invocation-start EXPLORE assessment is
`drafts/literature/2026-11-16-chamber-lower-pair-trace-nomination-1078.md`,
separately reviewed at1079. The calculation remains its actual incidence
test. The assessment already compared the relevant characteristic tools
and stops1043/1058/1060/1068; those stops concern different classes.
We import C467u's actual signs without reproving the paired product or
finite verification. We use C467e/z's regular ODE construction, whose
standard source is Gerald Teschl, *Ordinary Differential Equations and
Dynamical Systems*, April2012 author preliminary version,
[Theorems2.5/2.10, Lemma2.14/Corollary2.15, Theorems3.9/3.12 and
Theorem6.1/proof, pp40–53,81–84,189–190](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf).
No singular-boundary ODE theorem or time-zero derivative of the unknown
scalar is used. The new work is the coefficient cancellation below.

Let pi_hat(t,e) be C467e's momentum graph, and put
p(t,q)=J_e(q)^T pi_hat(t,e(q)), Z=D_qp. On the common coefficient
neighborhood let

\[
S_t(e)=\widetilde h_\pi(e,\widehat\pi(t,e)),\qquad
C_t(e(q))=J_e(q)b_c(t,q).
\tag{5}
\]

S_t is smooth by C467e's finite-contour construction and local
smooth ODE flow/inverse. We justify the same coefficient regularity
for C_t, rather than inferring it from mere continuity of ordered roots.
In C467z(8) put M=Id-iZ, p_t at fixed q, and
P_sigma=product_l(i-pi_hat_2-q_l pi_hat_3)^2. Then

\[
\widehat A=e^{-H(p+iq)}P_\sigma\det M,\qquad
N=e^{-H(p+iq)}P_\sigma J_e(-i\operatorname{adj}(M)p_t),
\qquad C_t=-\frac{N+\overline N}{\widehat A+\overline{\widehat A}}.
\tag{6}
\]

The bars mean ordinary complex conjugation of the smooth coefficient
expressions at real (t,e). Formula (6) agrees
exactly with C467z(10) on distinct real q. All matrix entries before
the exponential are finite polynomials in q with smooth coefficients
in (t,e). This follows from p=J_e^T pi_hat and its derivatives;
determinant and adjugate introduce no inverse root gaps. Permutation
equivariance makes every scalar component in the numerator after J_e,
and the denominator, symmetric. The elementary theorem on symmetric
polynomials rewrites these finite polynomials in e with the same
smooth parameter dependence. The remaining sum
sum_j beta(P_{e,pi_hat}(q_j)+iq_j) is smooth in e by the same residue
formula as C467e(20): integrate beta(P(v)+iv) Q_e'(v)/Q_e(v) on
its fixed root-enclosing circle. Compact containment in the original
beta disk and a nonzero contour denominator justify all derivatives.
The conjugate expression is treated identically.

At t=0 the denominator in (6) is -2 Re exp(-H(iq)), nonzero on
the small compact real-root set under consideration by C467z's phase
bound. Compactness and continuity give a coefficient neighborhood
where it stays nonzero for small time, including nearby nonreal-root
coefficient vectors. Thus (6) is a smooth coefficient extension.
This argument is only an extension of the diagnostic; it does not
extend the original chamber's admissible initial coordinates.

Since E_t solves E'_t=S_t(E_t), define the pullback of a vector field by
E_t^*W=(D E_t)^(-1) W composed with E_t. C467z's exact diagnostic is
therefore

\[
D(t,x,h)=L(x)\,E_t^*(S_t-C_t)(e(x,x,x+h)).
\tag{7}
\]

This proves the asserted smooth extension. It also gives
D(0,x,h)=-2h, by C467z's time-zero identity. In particular
partial_h D=-2+O(t) uniformly on the fixed box. It remains to compute
the first nonzero term of (7) at h=0.

### Root-lift identities at a triple root

Call R_B(e(q))=J_e(q)B(q) a regular root lift when B is a smooth
permutation-equivariant vector field and this expression has a smooth
coefficient extension. All lifts used below have the smooth
extensions just established or the scalar residue construction above.
For a one-variable function a, write R_a for B_j(q)=a(q_j).
Use the bracket convention
[U,V]=D V U-D U V, and let s(e)=(0,-6,-2e_1).

At e_x, every regular lift satisfies L(x)R_B(e_x)=0: all B_j
agree there and J_e B is a multiple of e_x'. Also

\[
L(x)[s,R_B]\,(e_x)=0.
\tag{8}
\]

Here is a direct check of (8) and of the second bracket needed below.
The exact flow of s is
Psi_r(e)=(e_1,e_2-6r,e_3-2e_1r). At e_x its roots for r>0 are
x-sqrt(6r), x, x+sqrt(6r). Put delta=sqrt(6r) and evaluate B on
this triple. The third component after translation by x gives

\[
L(x)\Psi_r^*R_B(e_x)
=2r\,[B_1(x-\delta,x,x+\delta)+B_3(x-\delta,x,x+\delta)
                    -2B_2(x-\delta,x,x+\delta)].
\tag{9}
\]

Indeed L J_e B=-6r B_2 at these roots, and multiplication by
(D Psi_r)^(-1) adds 2r sum_j B_j to the L component. The bracketed
quantity vanishes at delta=0 and is an even smooth function of delta,
by the interchange of slots 1 and 3. It is O(delta^2). Differentiating
the smooth coefficient expression at r=0 proves (8). In particular
for a scalar a, (9) is
2r[a(x-delta)-2a(x)+a(x+delta)]=12a''(x)r^2+O(r^3), whence

\[
L(x)[s,[s,R_a]]\,(e_x)=24a''(x).
\tag{10}
\]

Brackets of two regular root lifts are regular root lifts: on the
distinct-root chart the chain rule identifies them with the lift of
the bracket of their q fields, and continuity extends the identity.
Thus their L components vanish at e_x.

We also need the following mixed case. If a smooth coefficient field
K satisfies L(x)K(e_x)=0 for every x in an interval, then
L(x)[R_j,K] evaluated at e_x is zero for every scalar j. To verify this without assuming
K itself is a regular lift, use R_j(e_x)=j(x)e_x' and

\[
L(x)D R_j(e_x)=-j(x)L'(x)+3j'(x)L(x).
\tag{11}
\]

For (11), translate the roots by x. At their zero triple the last
coefficient of R_j is j(x)e_2+3j'(x)e_3 plus terms of ordinary
coefficient degree at least two; this follows by expanding j(x+v)
in sum_j v_k v_l j(x+v_j). Its derivative gives (11) after undoing
the translation. Differentiating L(x)K(e_x)=0 gives
L D K R_j=-j L'K. Subtracting (11) applied to K proves the mixed
case. These are finite-dimensional algebra/chain-rule identities,
not imported positivity statements.

### Time expansion with the actual background retained

Put A(v)=-G(v), Phi(q)=sum_j Im beta(iq_j), and T(e(q))=tan Phi(q).
C467z(11) gives p_t(0,q)=(A(q_j)) and

\[
S_0=s+R_J,\qquad C_0=T R_A,\qquad S'_0=R_{A A'}.
\tag{12}
\]

For the last identity, the actual imaginary-coordinate velocity at
the physical graph is
2 sum_{k!=j}[(q_j-q_k)(1+sigma_l^2)]^(-1)+Im g(p_j+iq_j),
where l is the remaining index and sigma_l=-pi_hat_2-q_l pi_hat_3.
At time zero sigma=0, so the time derivative of every gap weight is
zero. At fixed q the background derivative is
Im g'(iq_j) A(q_j)=A'(q_j)A(q_j). This proves the last identity
after multiplying by J_e, including at repeated roots by continuity.

More generally, the coefficient contribution of a pair j,k to S_t is
(0,-2c_l,-2q_l c_l), c_l=(1+sigma_l^2)^(-1). At a triple root all
c_l agree, and the sum is (0,-6c,-6xc). Its L component is zero.
The background is a regular root lift, also with zero L component.
Consequently L S_t(e_x)=0 for every small t. Likewise L C_t(e_x)=0,
and every time derivative of C_t is a regular root lift.

Let V(t)=E_t^*(S_t-C_t). Differentiation of the inverse Jacobian
gives d(E_t^*W_t)/dt=E_t^*(W'_t+[S_t,W_t]). Applying this twice yields

\[
V'(0)=S'_0-C'_0-[S_0,C_0],
\]
\[
V''(0)=S''_0-C''_0+[S_0,S'_0]-[S'_0,C_0]
             -2[S_0,C'_0]-[S_0,[S_0,C_0]].
\tag{13}
\]

The L components of V(0) and V'(0) vanish at e_x by (8),(12).
In V'' every term except the last also has vanishing L component:
use L S''_0=L C''_0=0, S'_0 a regular root lift, (8), and closure
of regular lifts under brackets. In the last term expand S_0=s+R_J.
The terms [s,[R_J,C_0]] and [R_J,[R_J,C_0]] vanish after L by the
regular-lift identities. The term [R_J,[s,C_0]] vanishes by (11),
since (8) holds along the whole triple-root curve. Only
[s,[s,C_0]] remains. The product rule and (8),(10) give

\[
L[s,[s,T R_A]]\,(e_x)=T(e_x)\,24A''(x).
\tag{14}
\]

Indeed the other two terms are (s^2T)R_A and
2(sT)[s,R_A], each killed by L. Therefore the t^2 coefficient of
D(t,x,0)=L V(t)(e_x) is
-12 T(e_x)A''(x)=12 tan(3 Im beta(ix)) G''(x)=d(x).
Smoothness on a neighborhood of the compact x interval gives the
uniform O(t^3) remainder. Integration of partial_h D=-2+O(t)
then proves all of (3). No unknown scalar has been differentiated.

### The layer, the original-domain exit and the limitation

C467u proves G''<0 and sign theta(x)=sign x, with |theta|<1/16,
on this x interval. Thus d has the asserted strict signs. On a
compact K_+ let d_min>0 be its minimum. Formula (3) gives
D(t,x,0)>0 and D(t,x,H_*)<0 for small t>0. Reducing the same
time so -3<partial_h D<-1 gives a unique zero h_g, with the asserted
signs on either side. The derivative bound first gives h_g=O(t^2).
Substitution in (3) then gives (4), uniformly on K_+. For example,
after another common reduction, 0<h<=d_min t^2/8 implies
D>=d_min t^2/2>0. On K_-, D(t,x,0)<0; the same strictly negative
h derivative proves D<0 for every positive h<=H_*.

Fix t>0,x in K_+, and a separated h in (0,h_g). C467z's regular
double-root chart e_*(m,k,y) applies since y-m=h>0. With backward
elapsed time s, its exact initial normal derivative is

\[
\frac{dk}{ds}\bigg|_{s=0}=-\frac4hD(t,x,h)<0.
\tag{15}
\]

The inverse coefficient path is smooth in this chart at this fixed
positive t,h. Starting with k=0, it has k(s)<0 for all sufficiently
small s>0. The singleton remains separated and real, but the other
two roots form a nonreal conjugate pair. Thus it is outside the
original real-root chamber, even though the physical q coordinates
remain ordered. For nearby terminal interior points with k>0,
continuity gives dk/ds<=-c<0 in a small chart neighborhood. Choose
that neighborhood and a backward duration shorter than t with compact
margins, and then take the terminal k sufficiently small. The path
must hit k=0 within that duration, before time zero; up to that hit
all initial roots are ordered, real and within (-a,a). This is a
local boundary-access statement for actual chamber characteristics.
It does not assert any continuation of them as original chamber
paths after the hit.

Finally f(b_*)=1 and f(2b_*)=0 give an x_0 in (b_*,2b_*) with
f'(x_0)<0 by the mean value theorem. At such a point 0<f(x_0)<1,
since an interior extremal value 0 or 1 would have zero derivative.
Apply the positive-x result at this fixed x_0. Every positive proposed
common horizon contains outward-layer points and nearby interior
paths whose first backward access is to a collision side, not to
the initial surface. This invalidates the uniform-initial-access
mechanism; it says nothing contradictory about C467z's result with
a fixed positive separation floor and its floor-dependent time.

The real incoming face permits a boundary-data question that initial
characteristic constancy alone does not answer. In particular neither
T_c=phi_p nor T_c!=phi_p has been established where T_c is necessary;
no compatible choice on incoming sides has been constructed. At a
backward-inward face local incidence alone does not prove access all
the way to time zero. No existing historical stop is enlarged to a
ban on continuous matching selections, and no RH conclusion follows.

### Independent conceptual audit — 16 November 2026, step1083

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-16-chamber-incidence-audit-nomination-1081.md`,
separately completed at review1082. This REPRODUCTION audit verifies
the existing claim and its delicate coefficient-domain argument. It
does not derive a new matching mechanism or assert certified novelty.
C467z's audit1083 validates the physical graph and separated trace;
C467e/audit1017 and C467u/audit1062 are imported with their original
analytic and external finite-zero qualifications.

**Coefficient extension and its domain.** Write pi=pi_hat(t,e).
Holding (t,e) as parameters, the needed entries are

    p=J_e(q)^T pi,
    D_qp=sum_b pi_b D_q^2 e_b + J_e(q)^T (D_e pi) J_e(q),
    p_t=J_e(q)^T partial_t pi.

These are finite polynomials in q with smooth parameter coefficients.
Permutation matrices transform p_t as a vector and M by conjugation;
J_e transforms by the inverse permutation on its columns. Therefore
J_e adj(M)p_t is componentwise invariant. The product P_sigma and
det M are also invariant. Their symmetry holds with the parameter
symbols fixed, before setting those parameters equal to e(q).
This verifies the exact hypothesis for the fundamental theorem on
symmetric polynomials over a commutative coefficient ring: Keith
Conrad, *Symmetric Polynomials*, Theorem1.5 p1, proof section3
pp6–7 and the commutative-ring extension with footnote4 p13,
[author text inspected in review1082](https://kconrad.math.uconn.edu/blurbs/galoistheory/symmfunction.pdf).
Apply it over the ring of smooth complex-valued functions of (t,e),
then substitute the elementary coefficients of q. No arbitrary smooth
invariant-function descent is being asserted or reproved.

The remaining beta trace is a separate finite-contour construction.
C467e uses r=31/128, |P(v)|<1/128 and |v|<=r, so
|P(v)+iv|<1/4. Its strict Rouche margin puts every root inside
the contour and keeps Q_e nonzero on it in a smaller coefficient
neighborhood. The residue at a multiple root counts its multiplicity.
The same contour with integrand beta(P(v)+iv) thus supplies the
smooth extension of the exponential in (6); uniform contour bounds
justify each finite parameter derivative. At real coefficients take
ordinary complex conjugates of these extended values. One need not
conjugate an arbitrarily selected ordered nonreal root branch.

At time zero widehat A+conj(widehat A)=-2 Re exp(-H(iq));
C467z's full phase estimate makes this uniformly nonzero on the
compact real-root coefficient image. Continuity gives an open
coefficient neighborhood and one small common time on which the
denominator remains nonzero, including nonreal-root coefficients.
Equation (6) equals J_e b_c on distinct real roots, since
det(M)M^{-1}=adj(M). It therefore extends C_t as claimed. All
coefficient compositions in (7) remain in that neighborhood after
reducing time. The extension is not a claim that its coefficients
are admissible initial data for the original chamber.

**Root-lift and mixed terms.** At the triple root every regular
equivariant root field has equal components and its lift is tangent
to e_x. The exact s flow has the roots x-delta,x,x+delta with
delta^2=6r. At these roots L J_e=(0,-6r,0), whereas multiplying
by (D Psi_r)^{-1} adds 2r times the first coefficient component.
This gives (9) with its stated plus sign. Equivariance makes the
bracketed difference an even smooth function of delta vanishing
at zero, so it is O(delta^2). The smooth coefficient extension
permits differentiation at r=0. This proves L[s,R_B]=0.
For a scalar a the central difference is
a''(x)delta^2+O(delta^4), so the expression in (9) is
12a''(x)r^2+O(r^3). Its second r derivative is 24a''(x), not
12a''(x). This checks (10) and the Taylor factor used later.

For the mixed identity translate the roots by x, with elementary
coefficients epsilon. For the actual analytic scalar j=J, the third
component of R_j has linear coefficient jet
j(x)epsilon_2+3j'(x)epsilon_3. Indeed its constant Taylor term
is j(x)epsilon_2, its linear root term is 3j'(x)epsilon_3,
and each higher term is epsilon_3 times a positive-degree power
sum of the translated roots. The convergent analytic series gives
no further linear coefficient term. This analytic case is all that
the mixed cancellation needs. Undoing translation gives exactly

    L D R_j = -j L' + 3j' L.

If L K(e_x)=0 along the triple curve, differentiation gives
L D K R_j=-j L'K. Subtracting the preceding identity applied
to K makes L[R_j,K]=0. The relevant K=[s,C_0] satisfies that
hypothesis by (8) along the entire curve. Brackets of regular
lifts are regular lifts: the chain rule proves this on the open
simple-real-root locus; continuity of both smooth extensions gives
the identity and its vanishing L component at the triple root.
This checks all mixed cases without treating K itself as a root lift.

**Actual time dependence and pullback.** At fixed q, the graph
time derivative is p_t(0,q)=A(q), A=-G. The pair contribution to
S_t is (0,-2c_l,-2q_l c_l) with
c_l=(1+(-pi_2-q_l pi_3)^2)^{-1}. Since pi(0,e)=0, partial_t c_l
vanishes at zero. The background derivative is
Im g'(iq_j) A(q_j)=A'(q_j)A(q_j). Thus S'_0=R_(A A') exactly.
At a triple root the three c_l coincide and their sum is
(0,-6c,-6xc), killed by L; the background lift is also killed.
This proves L S_t(e_x)=0 for every small t, hence L S''_0=0.
For C_t and its time derivatives the underlying smooth q field is
equivariant, so they are regular lifts and their L components vanish.

The vector pullback convention and time-dependent generator are those
of Baillieul–Bloch–Crouch–Marsden, *Mechanics, Control, and Variational
Principles*, 28 September 1998 manuscript, section2.4 Theorem2.4.1
and (2.4.5)–(2.4.8), pp53–54,
[primary manuscript inspected in review1082](https://www.cds.caltech.edu/~murray/courses/cds/cds280/BLOCH.pdf).
Here the fields and E_t are smooth on an open coefficient domain and
E_t is invertible there. Including the transported field's explicit
time derivative, differentiating (D E_t)^{-1} W_t(E_t) gives
E_t^*(W'_t+[S_t,W_t]). A second differentiation gives every term
of (13), including the coefficient -2 on [S_0,C'_0].

In V'(0), S'_0 and C'_0 are regular lifts, and both terms in
[s+R_J,C_0] have zero L component. In V''(0), S''_0 and C''_0
vanish after L by the preceding time identities. The terms
[S_0,S'_0], [S'_0,C_0] and [S_0,C'_0] vanish by the first-bracket
or regular-lift rules. Expanding the last double bracket leaves
[s,[s,C_0]]: [s,[R_J,C_0]] uses (8),
[R_J,[R_J,C_0]] is a regular lift, and
[R_J,[s,C_0]] uses the mixed identity just verified. With C_0=T R_A,
the product rule contributes T[s,[s,R_A]], 2(sT)[s,R_A] and
(s^2T)R_A. Only the first survives L. Thus

    L V''(0)(e_x)=-24 T(e_x) A''(x),
    (1/2)L V''(0)(e_x)=-12 G''(x) tan(theta(x)).

The last equality uses A=-G and T(e_x)=tan(3 Im beta(ix))
=-tan(theta(x)). It verifies the sign and the factor d in (3).
No derivative of the candidate scalar occurs.

**Uniform layer and actual exit.** Smoothness on a neighborhood of
the fixed compact (x,h) box gives both the uniform O(t^3) Taylor
remainder at h=0 and partial_h D=-2+O(t). Integrating the latter
gives O(th+t^3), with no hidden division by h. C467u/audit1062
provides G''<0 and sign theta=sign x, |theta|<1/16, under its
paired-product and finite-zero hypotheses. It follows that d has
exactly the asserted signs. There is no uniform positive lower bound
for d as x approaches zero, and none is used.

For a fixed compact K_+, take d_min>0. After a time reduction,
D(t,x,0)>0, D(t,x,H_*)<0 and -3<partial_hD<-1. Existence,
uniqueness and the two signs of the glancing zero follow. First
h_g=O(t^2) by the derivative bound; substituting this into (3)
gives h_g=d(x)t^2/2+O(t^3). For K_- the negative value at h=0
and negative h derivative give the whole asserted inward interval.
These time choices depend on K_+ or K_- and imply no classification
at x=0 or uniform positive horizon approaching it.

Fix positive t and 0<h<h_g. The chart (13) of C467z is regular
at this separated double root, however small h is. Its exact backward
derivative is -4D/h<0, so k(s)<0 for a short backward interval.
Its real simple singleton persists while the quadratic pair becomes
nonreal. This is an exit from the original initial-root chamber,
despite continued physical q ordering. The strict inequality persists
in a small spacetime chart neighborhood. Choose a backward interval
shorter than t and terminal k>0 sufficiently small; integration of
k'<=-c<0 forces a hit of k=0 within that interval. Until the hit,
the inverse initial roots are ordered, distinct and inside (-a,a),
and the chart margins exclude every other face. C467e's uniqueness
therefore identifies these as actual chamber characteristics up to
the hit. No extension past it as a chamber path is claimed.

Finally the mean-value theorem on [b_*,2b_*] gives a point with
f'<0; the range constraint implies 0<f<1 there. The positive-x
argument at this fixed point supplies exit points for arbitrarily
small t. Hence uniform backward confinement to the initial surface
fails on every proposed common horizon. This says neither that the
initial data have no influence on an incoming trace nor that incoming
data can be chosen freely while preserving every interface.

All claims of the stated local result pass, with C467z's separated
necessary trace intact. Direct inputs remain C467e/u/z; no DAG
edge is added. Equality or discrepancy with phi_p on forced outflow,
compatible incoming data, global confinement, x=0, exterior payment,
realization, all degrees and Xi transfer remain open. The audit
validates the scoped stop1081, not a stop of the continuous matching
class. Reproducing this notebook argument is not a new discovery
beyond the sources checked.

## Mathlib

Full matching coverage has not been checked. The supporting analytic
ODE, inverse-function, residue and chain-rule tools are standard named
inputs, with the precise ODE citation above and the coefficient contour
application in C467e. No Mathlib theorem covering this actual incidence
specialization is claimed, and unchecked coverage is not absence.
