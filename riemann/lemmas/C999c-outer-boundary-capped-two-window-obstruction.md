# Corollary 999c: an outer boundary obstruction to capped two-window control

## Hypotheses

Use C997s's original integer n>=64, z_star=1+i/8, complex coefficients,
gamma_j=15/8+j/(4n), 0<=j<=n, and B_n=exp(sqrt(n)). Put

    p_n(y)=sum_(j=0)^n A_(j,n)y^j,  sum_j |A_(j,n)|<=B_n,
    e_n(t)=exp(i z_star t)-exp(15it/8)p_n(exp(it/(4n))),
    U_n=[7n/4,9(n+2)/4],  L_n=[n,n+2],
    T_U=18 exp(27/16)(n+2)exp(9n/32),
    T_L=8 exp(3/4)(n+2)exp(-n/16),
    Delta_n(p_n)=T_U sup_(t in U_n)|e_n(t)|
                         +T_L sup_(t in L_n)|e_n(t)|.       (1)

T_U,T_L are exactly C997c(5)'s upper variation bounds per unit input
TV, including their polynomial factors. This is review400's stronger
SUFFICIENT objective, not the integrated infimum E_n of C997s.
No converse between these objectives is assumed.

Use normalized circle measure dm=dtheta/(2pi), and set

    a=7/16, b=9/16, c_0=1/2, d=1/16,
    A={exp(i theta): a<theta<b}, J=T\A,
    H_J(y)=integral_J (zeta+y)/(zeta-y) dm(zeta), |y|<1,
    h_n(y)=y exp(-n H_J(y)/4),
    F_n(theta)=exp(-(1+7i)n theta/2),
    P_n=integral_A F_n(theta)h_n^*(exp(i theta)) dm.         (2)

This is the ONE selected permitted pair lambda=1/4, eta=0 in review401.
There is no parameter sweep. The asterisk denotes a nontangential
Hardy boundary function, not complex conjugation.

## Conclusion

There are fixed epsilon>0, C>0 and an integer N>=64, independent of
the coefficients, such that for all integers n>=N and all admissible p_n,

    Delta_n(p_n)>=C (n+2)/sqrt(n) exp((1/32+epsilon)n).      (3)

In particular no sequence of capped polynomials satisfies
Delta_n=O(exp(-n/64)). This contradicts an arbitrary finite big-O
constant, not merely a prescribed constant or a finite-degree fit.

An exact implicit choice is epsilon=5v/6, where v is the positive
constant constructed in (9)-(10) below. The boundary certificate is

    M_A=1/(16pi), M_J=(1-1/(16pi))exp(-n/4),
    sup_(a<=theta<=b)|F_n(theta)-p_n(exp(i theta))|
                  >= S_n:=(|P_n|-B_n M_J)/M_A.             (4)

Its numerator is eventually positive. More precisely, with the fixed
phase Phi, saddle z_0 and nonzero constant kappa below,

    P_n=kappa n^(-1/2)exp(n Phi(z_0))(1+o(1)),
    s:=Re Phi(z_0)>-1/4+epsilon,
    S_n>=|kappa|/(4M_A) n^(-1/2)exp(sn) eventually.        (5)

Step403, 11 November2026: RESEARCH / POTENTIALLY_NEW / NEGATIVE under
the unchanged, separately approved EXPLORE review401. The proof was
UNAUDITED at step403; the independent conceptual audit in step405 below
accepts (3)-(5) with unchanged hypotheses and bounds. This is a local obstruction
to (1), not a claim of originality beyond the sources checked, a lower
bound for E_n, or a candidate proof/disproof of RH. Its essential
analytic inputs are imported below; the new work is their specialization
and the explicit contour, noncancellation and rate comparison.

## Proof

### Imported tools and the bilinear certificate

L. Baratchart, J. Leblond and F. Seyfert, *Constrained L2-approximation
by polynomials on subsets of the circle*, author manuscript22 March2017,
Section3, equations(2)-(7), printed pp2-4, supplies Hardy boundary limits,
the Cauchy formula and the outer function with prescribed positive
boundary modulus whose logarithm is integrable. See the
[author manuscript](https://www-sop.inria.fr/members/Juliette.Leblond/Papiers/BLSFields2017.pdf).
Theorem1's proof, equation(15), p6, also uses the exponential of an
indicator's Riesz-Herglotz transform. These are standard imported
contracts, separately checked in step402; no extremal-rate theorem
from that paper is invoked or reproved.

For each fixed n, rho=1 on A and rho=exp(-n/4) on J is positive,
bounded and has integrable logarithm. The outer function for this rho
is exp(-n H_J/4). Also Re H_J>=0 in the disk because it is the Poisson
integral of 1_J. Thus h_n is bounded analytic, h_n(0)=0, and its boundary
modulus is 1 on A and exp(-n/4) on J almost everywhere. This gives
the two masses in (4), both computed with normalized measure. In
particular M_A>0. No boundary value at either endpoint is required.

Every polynomial p satisfies p h_n in H^2. The imported Cauchy formula
at zero, equivalently its circle line integral with the factor 1/zeta,
gives

    integral_T p(zeta) h_n^*(zeta) dm(zeta)=(p h_n)(0)=0.   (6)

Products and limits are legitimate: h_n has its finite-p Hardy boundary
limit, p is continuous and bounded on the circle, and multiplication
by p preserves L2 convergence. This is a BILINEAR dtheta identity;
there is no conjugated test function or omitted circle Jacobian.

The original complex coefficient cap gives directly
|p_n(zeta)|<=sum_j |A_(j,n)|<=B_n for every |zeta|=1. By (6),

    P_n=integral_A (F_n-p_n)h_n^* dm-integral_J p_n h_n^* dm.

Taking absolute values proves (4). Only the one-way coefficient-to-
circle bound is used; no reverse norm equivalence is assumed.

### Exact analytic phase and endpoint conventions

For a<Re z<b, Im z>=0, define

    L(z)=Log sin((z-a)/2)-Log sin((b-z)/2),
    Phi(z)=-(1+7i)z/2+i L(z)/(4pi).                       (7)

Both logarithms are principal. For Im z>0, the first sine has positive
real and positive imaginary parts and the second positive real and
negative imaginary parts. The formula extends analytically across the
open real interval; neither sine vanishes there. On that interval L is
real. In the upper rectangle 0<Im L<pi.

Direct integration of the Cauchy kernel gives, for H_A=1-H_J,

    H_A(y)=d/pi-(i/pi)Log((1-y exp(-ib))/(1-y exp(-ia))),
    H_J(exp(iz))=-i L(z)/pi.                              (8)

For clarity, the first logarithm is its analytic branch equal to zero
at y=0. The ratio at y=exp(iz) is
-exp(-id)exp(-L(z)). Its logarithm in the rectangle is
i(pi-d)-L(z): on the open lower edge its argument is pi-d, and
continuation fixes the branch throughout. Substitution proves the
second identity. This fixes the sign of the boundary phase without
an appeal to an unsigned modulus estimate.

Taking the boundary limit in (8) shows
F_n(theta)h_n^*(exp(i theta))=exp(i theta)exp(n Phi(theta))
for a<theta<b. This is a bounded, integrable function for each n;
the logarithmic oscillations at a,b do not require endpoint continuity.

### A fixed saddle inside the permitted upper rectangle

Set

    u=cos d+7 sin d/(100pi), beta=sin d/(100pi).

There is a unique v>0 solving

    sinh v sqrt(1-u^2/cosh(v)^2)=beta.                    (9)

Here 0<u<1. To verify the needed bounds using only 3<pi<4 and
elementary Taylor inequalities,

    cos d<u<1-d^2/2+d^4/24+7d/300<2499/2500,
    0<beta<1/4800,
    sqrt(1-u^2)>sqrt(4999)/2500>7/250.

The left side of (9) is continuous and strictly increasing from zero
to infinity: both positive factors are strictly increasing for v>0.
At v=1/100 it is greater than 7/25000>1/4800. Consequently

    0<v<1/100.

Also cosh(1/100)<=1+1/19998<1+1/10000; the first estimate follows
by bounding each (2k)! below by 2 in the convergent positive series
for cosh-1. In contrast,
u/cos d=1+7 tan d/(100pi)>1+7/6400. Thus cosh v<u/cos d.
The unique r=arccos(u/cosh v) therefore satisfies

    0<r<d,
    cos r cosh v=u, sin r sinh v=beta,
    z_0=c_0-r+iv.                                        (10)

All constants are independent of n. No numerical location or fitted
saddle is used in these inequalities.

Differentiation of (7), using the sum-of-cotangents identity, gives

    Phi'(z)=-(1+7i)/2
          +i sin d/[4pi*(cos(z-c_0)-cos d)].              (11)

By (10), cos(z_0-c_0)-cos d=(7+i)sin d/(100pi).
Since 25i/(7+i)=(1+7i)/2, equation(11) gives Phi'(z_0)=0.

### Global dominance and nondegeneracy on one horizontal contour

For x in [a,b], put t=x-c_0, K=sin d/(4pi). Equation(11) gives

    Re Phi'(x+iv)=-1/2
      -K sin t sinh v/[(cos t cosh v-cos d)^2
                                      +sin(t)^2 sinh(v)^2].

This is strictly negative for x>=c_0. For x<=c_0 it equals
-1/2+Q(c_0-x), where

    Q(t)=K sinh v sin t/D(t), 0<=t<=d,
    D(t)=(cos t cosh v-cos d)^2+sin(t)^2 sinh(v)^2>0.

Q is strictly increasing. Here is the full sign check. Write
C_d=cos d, H=cosh v, w=cos t. Then

    D(t)=w^2+H^2-1-2w H C_d+C_d^2,
    Q'(t)/(K sinh v)=N(w)/D(t)^2,
    N(w)=-w^3+(H^2+1+C_d^2)w-2H C_d.

On C_d<=w<=1, N''(w)=-6w<0, and

    N(C_d)=C_d(H-1)^2>0, N(1)=(H-C_d)^2>0.

A concave function lies above its endpoint chord, so N>0 throughout.
This proves Q'>0 without a sampled monotonicity claim. Since
Phi'(z_0)=0, Q(r)=1/2. It follows that Re Phi(x+iv) increases strictly
up to x=c_0-r and decreases strictly thereafter on the WHOLE segment.
Moreover

    Re Phi''(z_0)=-Q'(r)<0.                              (12)

The saddle is thus simple and is the unique global maximum of the real
part on that contour. Every closed portion away from it has a strictly
smaller real part by continuity and compactness.

At the midpoint of the same contour,

    L(c_0+iv)=2i arctan(cot(d/2)tanh(v/2)),
    Re Phi(c_0+iv)=-1/4+7v/2
                   -arctan(cot(d/2)tanh(v/2))/(2pi).

For positive arguments, arctan q<q and tanh q<q; also cot(d/2)<32.
Hence the arctangent is less than 16v. Global dominance and pi>3 give

    s=Re Phi(z_0)>=Re Phi(c_0+iv)
          >-1/4+(7/2-8/pi)v>-1/4+5v/6.                  (13)

This establishes a strict rate advantage over leakage without replacing
the complex integral by its absolute envelope.

### Contour deformation with both endpoint pieces paid

Apply the Cauchy integral theorem to exp(iz)exp(n Phi(z)) in the
rectangle [a,b]+i[0,v], with small quarter-disks about a,b deleted.
There are no other zeros of either sine or logarithm cuts in this
domain. On its interior and open lower edge, Im L>=0, so for fixed n
the integrand is bounded near each deleted corner by
exp(n(-a/2+7v/2)). The shrinking quarter-circle integrals therefore tend
to zero. The improper integrals on the remaining edges converge
absolutely, including the original oscillatory lower edge.

The result is the top integral, oriented left to right, plus a left
upward integral minus a right upward integral. On z=a+iy or z=b+iy,
0<y<=v, the argument difference defining Im L is at least pi/2:
at the left endpoint the numerator has argument pi/2 and the denominator
negative argument; at the right endpoint the denominator has argument
-pi/2 and the numerator positive argument. Thus on both vertical edges

    Re Phi(z)<=-a/2+7v/2-1/8<-247/800,
    |exp(iz)|=exp(-y)<=1.

In particular,

    P_n=(1/(2pi))integral_a^b exp(i(x+iv))
                               exp(n Phi(x+iv))dx+R_n,
    |R_n|<=(v/pi)exp(-247n/800).                          (14)

The corner limit is taken for each fixed n before using this uniform
bound. No joint endpoint/n limit or unbounded interchange is assumed.

### Imported simple-saddle formula and noncancelling action

Import the fixed simple-saddle expansion from NIST DLMF
[Section2.4(iv), equations2.4.15-16](https://dlmf.nist.gov/2.4#E15),
with Section2.4(iii)'s hypotheses and (2.4.16)'s branch convention;
also Olver, *Asymptotics and Special Functions*,1997 reprint, pp121-127.
The DLMF statement, hypotheses and leading coefficient were checked
directly on11 November2026 inside review401's existing section scope;
the site's release number was not independently checked. The standard
asymptotic theorem is not reproved.

Apply it on the top segment with phase p=-Phi, amplitude q(z)=exp(iz),
and positive parameter n. These are fixed analytic functions on a
neighborhood of that segment. Equations(10)-(12) supply the unique
interior minimum, simple saddle and positive real part of p''.
The compactness gap above supplies strict decay away from the saddle.
Absolute endpoint convergence is uniform: on the top segment
Re Phi<=-a/2+7v/2<-147/800 and |q|<=1. The direction toward the right
endpoint is horizontal, so (12) selects the square root with positive
real part. There is no n-dependent amplitude or unproved steepest-path
assumption. The imported leading term yields, for the top integral
including its normalization,

    kappa n^(-1/2)exp(n Phi(z_0))(1+o(1)),
    kappa=exp(iz_0)/sqrt(-2pi Phi''(z_0)) != 0.            (15)

By (13), s>-1/4, while 247/800>1/4. The ratio of (14)'s remainder to
the modulus of (15)'s leading term is bounded by a fixed multiple of
sqrt(n)exp(-(247/800+s)n), which tends to zero. This proves the complex
asymptotic in (5), with a genuinely nonzero leading coefficient; it
also excludes cancellation against either endpoint piece.

### Leakage, original windows and the decisive rate

For all sufficiently large n, (5) first gives
|P_n|>=(|kappa|/2)n^(-1/2)exp(sn). Therefore

    B_n M_J/|P_n|
      <=[2(1-M_A)/|kappa|]sqrt(n)
                             exp(sqrt(n)-(s+1/4)n) -> 0,

because s+1/4>epsilon=5v/6>0. Eventually this ratio is at most1/2.
Substitution into (4) proves the stated lower bound for S_n in (5).
All onsets and constants depend only on the fixed arc and pair,
not on the polynomial or an unspecified big-O constant.

For a<=theta<=b, t=4n theta lies in [7n/4,9n/4], a closed subset of
the ORIGINAL U_n. Direct substitution, with no change of grid, gives

    e_n(4n theta)=exp(15in theta/2)
                           [F_n(theta)-p_n(exp(i theta))].

Its prefactor has modulus one. The nonnegative lower-window term in
(1) consequently gives Delta_n>=T_U S_n. Using (5),(13) proves (3)
with C=18 exp(27/16)|kappa|/(4M_A). In particular the exact requested
score satisfies

    T_U S_n exp(n/64)
       >=C (n+2)/sqrt(n)exp((3/64+epsilon)n) -> infinity.  (16)

The actual target-action decay rate -s is strictly less than
1/4-epsilon; leakage has rate1/4 up to exp(sqrt(n)), and the requested
weighted threshold is19/64. All comparisons hold along all sufficiently
large integers, so an unbounded subsequence is not needed.

### Scope and remaining gaps

C997c(4)-(6), applied to the unit atom at each c in I and to the finite
band sum, makes Delta_n a sufficient upper bound for the complete
integrated residual of that polynomial. This does not make it a
necessary bound. The proof above acts on a spectral subarc; it cannot
exclude cancellation after integration against the actual signed
Laguerre densities. Thus C997s's capped E_n remains open. The lower
window, upper endpoint enlargement, both beta terms and the constant
subtraction in K are retained in the objective and the downstream
complete-kernel contract. None is replaced by a different model.

C997x/y/z and spectral-tail341 are comparisons only, not proof inputs.
Their earlier stops retain their exact scopes. C997a(8), selected and
both-sign transfer, assay/reconstruction, complements/regulators, L993,
L984(H), L966/L968 forcing and actual-Xi positivity remain unresolved.
No cross-notebook theorem is used. The independent review below checks
the logarithm branches, the Q' sign identity, saddle hypotheses and
uniform coefficient quantifiers before accepting this scoped obstruction.

### Independent conceptual audit — step405, 11 November 2026

RESEARCH / REPRODUCTION / ADVANCE under the unchanged EXPLORE
review403, separately source-approved in step404 before this audit.
ADVANCE records local verification of an existing mathematical input,
not a new bound or a discovery beyond the sources checked. The full
proof above and C997c(4)-(6), C997s's original kernel, grid and cap were
checked. The BLS and DLMF contracts are reused at the precise citations
above; their local applicability is verified here. No numerical evidence,
new mathematical script, additional source theorem or new lemma is used.

**Bilinear normalization and boundary limits.** The arc length is
1/8, hence its normalized mass is 1/(16pi). The Poisson real part of
H_J is nonnegative and has boundary value 1_J almost everywhere. For
each fixed n, multiplication of its bounded outer function by y puts
h_n in H^2 with h_n(0)=0 and gives precisely the moduli in (4).
For a fixed polynomial p, multiplication preserves the H^2 boundary
limit; the normalized circle mean of p h_n is its constant coefficient.
Thus (6) uses dtheta/(2pi), with neither a conjugate nor an extra
exp(i theta). The factor y is essential to its zero value. In the
target integral that same factor becomes the amplitude exp(iz) in
(14)-(15). The coefficient cap supplies |p|<=B_n on the whole circle.
The triangle inequality then gives (4) with the stated subtraction
and no unproved extremal or converse norm assertion. Endpoint boundary
values of h_n are unnecessary because the two endpoints have zero
circle measure; F_n-p_n is continuous on the closed arc for its supremum.

**Branches and corner deformation.** Integration of the Cauchy kernel
in theta gives the minus-i coefficient in H_A in (8). Factoring
1-exp(iw)=-2i exp(iw/2)sin(w/2) gives the ratio
-exp(-id-L(z)). On a<Re z<b, Im z>0 the numerator sine has argument
in (0,pi/2) and the denominator sine in (-pi/2,0). Thus 0<Im L<pi,
and neither principal logarithm meets its cut or a zero. On the open
lower edge the analytic logarithm of the ratio equals i(pi-d)-L;
analytic continuation through the connected rectangle fixes that same
branch inside. Inserting it in H_A gives H_J=-iL/pi, with the sign in
(7), not its conjugate. The identity extends to the vertical edges
away from the corners by continuity.

Near either deleted corner the fixed-n integrand has modulus at most
exp(n(-a/2+7v/2)), since Im L>=0 and |exp(iz)|<=1. A quarter-circle's
length tends to zero, which pays each corner before n tends to infinity.
Both vertical integrals converge absolutely. On the left edge the
numerator argument is pi/2 and the denominator argument is negative;
on the right edge the denominator argument is -pi/2 and the numerator
argument is positive. Consequently Im L>=pi/2 on both edges. With
v<1/100, -a/2+7v/2-1/8<-247/800. Cauchy's oriented rectangle gives
bottom=top+left-upward-right-upward, so the two absolute vertical
lengths and the normalization yield exactly (14). No endpoint term
with a slower exponential rate is omitted.

**Saddle existence and whole-contour dominance.** The elementary bounds
in (9) are valid: 0<u<2499/2500 gives sqrt(1-u^2)>7/250, and
beta<1/4800. The positive increasing left side of (9) exceeds
7/25000 at v=1/100, which is larger than beta. Thus its unique solution
satisfies 0<v<1/100. The positive-series bound
cosh(1/100)-1<=1/19998<1/10000, whereas
u/cos d-1>7/6400, proves 0<r<d. Equation (9) then gives both identities
in (10). In (11) the denominator at z_0 is (7+i)sin d/(100pi), and
25i/(7+i)=(1+7i)/2 verifies the complex saddle equation exactly.

Differentiation of D(t) gives the cubic N(w) displayed above with no
missing factor or sign. At its endpoints N(C_d)=C_d(H-1)^2>0 and
N(1)=(H-C_d)^2>0. Since C_d>0, N''=-6w<0 on the entire interval;
its endpoint chord is strictly positive. This proves Q'>0 everywhere,
not just near r. For x<c_0 the real derivative is -1/2+Q(c_0-x),
so it changes from positive to negative exactly at c_0-r; for x>=c_0
it is already negative. The maximum is unique and interior, with
Re Phi''(z_0)=-Q'(r)<0. This supplies both simplicity and a strict
compact real-part gap outside every fixed saddle neighborhood.

**Imported saddle expansion and its nonzero term.** For p=-Phi and
q=exp(iz), analyticity holds on a neighborhood of the closed top
segment: its endpoints have positive imaginary part and are separated
from the sine zeros and cuts. Re p has the unique minimum just proved.
The endpoints have a strict phase gap. On this finite contour the
amplitude is bounded, and Re Phi<-147/800; hence the absolute endpoint
convergence required by the cited DLMF contract is uniform for positive
n bounded away from zero. The parameter direction is arg n=0 and the
path direction from the saddle toward b is horizontal. Since
Re p''(z_0)>0, the prescribed square root has positive real part. The
two halves of the simple-saddle formula therefore combine with the
same Gaussian coefficient. After division by 2pi it is precisely
q(z_0)/sqrt(2pi p''(z_0))=kappa in (15). Both numerator and denominator
are nonzero, so this is a relative 1+o(1) asymptotic, not an absolute
envelope bound that could conceal cancellation.

At the midpoint, cot(d/2)<32, tanh(v/2)<v/2 and arctan x<x for x>0
give (13): s>-1/4+(7/2-8/pi)v>-1/4+5v/6. The saddle dominates that
midpoint and both vertical pieces. Indeed their ratio to its leading
modulus is O(sqrt(n)exp(-(247/800+s)n)), whose exponent is strictly
negative because s>-1/4. Thus (5)'s full complex asymptotic follows.

**Uniform rate and exact scope.** Set epsilon=5v/6>0. Leakage divided
by the leading target modulus is at most a fixed multiple of
sqrt(n)exp(sqrt(n)-(s+1/4)n); this tends to zero since s+1/4>epsilon.
The two eventual factors 1/2 used in the proof give
S_n>=|kappa|exp(sn)/(4M_A sqrt(n)). The fixed phase, amplitude,
endpoint estimates and cap contain no polynomial coefficients, so the
common onset N and all constants are independent of the chosen p_n.
For the original grid, t=4n theta gives exactly
e_n(t)=exp(15in theta/2)(F_n(theta)-p_n(exp(i theta))). The fixed closed
arc maps inside the original U_n, including both of its own endpoints.
The lower-window contribution is nonnegative in Delta_n. Multiplying
by its original T_U adds 9/32 to s, strictly exceeding
1/32+epsilon, and then multiplication by exp(n/64) gives (16).
The same lower bound defeats every finite big-O constant, although
the point at which it exceeds a chosen constant may depend on that
constant. No explicit numerical onset is asserted or needed.

The audit accepts (3)-(5) without repair. It changes the stop's status
from unaudited to audited, preserving its scope. C997c only gives the
integrated residual <=Delta_n for each polynomial; a lower bound on
Delta_n cannot be reversed into a lower bound on that residual or E_n.
C997x/y/z and spectral-tail341 were checked as contrasts, not used as
proof inputs. The two listed DAG inputs remain C997c and C997s; all
external tools are cited above. Actual-Xi positivity, L984(H), forcing,
the selected-response transfer and every other stated gap remain open.

## Mathlib

Full matching coverage for this capped, growing-target boundary
obstruction is unknown and was not checked. No absence claim is made.
Hardy/outer and saddle tools are imported from the precise classical
sources above; no Mathlib theorem or formal verification is assumed.
