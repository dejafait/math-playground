# Lemma 721: discrete support-edge transfer for the original signed bump

## Hypotheses

Use the original fixed nonnegative smooth bump chi specified in L714:
its support is contained in I=[omega-delta,omega+delta], it equals one
on [omega-delta/2,omega+delta/2], and 0<delta<1/3000. All choices
are made before n. The support need not fill I; no endpoint law or
analytic extension of chi is assumed. Retain L714's audited exact p_n
and signed integral K_n=integral_I chi(v)*p_n(v)dv. Only n=12q+3,
q>=1, is used.

Use L719's audited holomorphic phase S and saddle s_v, and L720's
audited factorial expansion of the exact normalized kernel

    Q_n(v)=n^(-1/2)*exp(-n*S(v))*p_n(v).

In particular U=121/64, A=27/10, d=5/4, u=(3+4i)/10,
alpha=11/8, z_v=exp(-u*v/A), s_v=-z_v*F'(z_v), and

    S(v)=ell_D+1+log(U)-d*v/A+F(z_v).

L719 gives 9/5<Re(s_v)<37/20 and -37/20<Im(s_v)<-9/5
on a complex neighborhood of I. L720 supplies holomorphic a_k on
fixed complex neighborhoods, with a_0 bounded away from zero, and
constants C,epsilon>0 such that, on a common neighborhood of I,

    |a_k(v)|<=C^(k+1)*k!,
    |Q_n(v)-sum_(k=0)^(m-1) a_k(v)*n^(-k)|
                         <=C^(m+1)*m!*n^(-m)          (1)

for all sufficiently large permitted n and 1<=m<=epsilon*n.
This is the expansion of the entire exact kernel, including the full
complementary contour in L719--L720. It is not an expansion of a
selected contour segment alone.

Set b=sup supp(chi), r(v)=Re S(v), and log(0)=-infinity. L713,
L714 (6), L717 and L718 are not premises.

## Conclusion

The claimed local result is

    limsup_(q->infinity) log|K_(12q+3)|/(12q+3)
                         =r(b)=max_(supp chi) Re S.   (2)

The proof constructs a fixed density f with the same right support edge
as chi, and constants v0<b and gamma>0, such that for the exact samples

    n^(-1/2)*K_n=integral_(v0)^b f(v)*exp(n*S(v))dv+E_n,
    |E_n|<=C_1*exp(n*(r(b)-gamma)).                    (3)

The generating germ of the fixed-density term has a nonremovable
singularity at exp(-12*S(b)); the error series is holomorphic on a
strictly larger disk. No interpolation to noninteger sizes is used.

**Status: derived in step 194; accepted by the separate step-196
conceptual audit in Section 6 below.**
This is a local specialization within the approved exact support-transfer
target. No matching theorem for this array was located in the reused
assessment; that does not establish originality. No full limit, eventual
nonvanishing or sign is claimed. The actual residue rate, comparison of
the other response terms, complementary spatial Jensen defect,
amplitude/full charge, H/support, Xi realization and all-degree mixed
positivity remain unresolved. This is not an RH candidate.

## Proof

### 1. Source scope and exact phase geometry

Reuse the invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-signed-bump-support-edge-transfer.md`.
Its identified missing specialization is an exact discrete analytic
Cauchy/operator realization, an applicable inverse, support geometry
and control of the entire exponential remainder. The following
construction supplies those items for this phase; it does not infer
them from scalar ellipticity or import a forward wavefront inclusion
backwards. No direct application of the reviewed continuous FIO or
real-coordinate sampled Laplace theorems is asserted.

The standard complex-analysis inputs are Cauchy's derivative formula,
[NIST DLMF 1.9(iii), (1.9.30)--(1.9.31)](https://dlmf.nist.gov/1.9.iii),
the holomorphic local inverse theorem in
[DLMF 1.10(vii), (1.10.12)--(1.10.14)](https://dlmf.nist.gov/1.10.vii),
and the finite contour residue theorem,
[DLMF 1.10(iv), (1.10.8)](https://dlmf.nist.gov/1.10.iv).
These precisely cited inputs were already inspected in the L716/L719
source comparisons. Their general theorems are imported. Below,
factorial estimates, finite integrations and the transverse endpoint
contour are written out because neither an abstract symbolic inverse
nor a branch jump identifies the exact sampled germ. No general FIO,
Borel summability or Plemelj theorem is reproved or silently assumed.

Differentiating the specified phase, not an absolute-value limit, gives

    S'(v)=(u*s_v-d)/A.                                (4)

Write s_v=x-i*y for real v. Both x and y lie between 9/5 and 37/20.
Thus Re(u*s_v)=3*x/10+2*y/5 and
Im(u*s_v)=2*x/5-3*y/10. Subtract d and divide by A in (4) to obtain

    1/270<Re S'(v)<1/60,
    11/180<Im S'(v)<2/27,
    |S'(v)|<1/10,                    v in I.         (5)

For the last bound, |S'|<=|Re S'|+|Im S'|<49/540<1/10.
In particular r is strictly increasing and attains its maximum on
supp(chi) precisely at b. Define

    Z(v)=exp(-12*S(v)).                               (6)

Its modulus is strictly decreasing on I, so distinct real v in I
have distinct Z(v): sampling causes no collision on this arc.
Also Z'(b)=-12*S'(b)*Z(b) is nonzero. The same derivative and
positive real-part properties hold on a sufficiently small real
extension past b, by holomorphy and continuity. This remains true
if b is an endpoint of the prescribed enclosure I.

### 2. A finite-path realization of the exact analytic symbol

Increase C in (1) so C>=1. On a slightly smaller fixed v neighborhood
define the jointly holomorphic germ

    B(v,t)=sum_(k>=1) a_k(v)*t^(k-1)/(k-1)!.          (7)

Indeed its k-th term is bounded by C^(k+1)*k*|t|^(k-1), so it
converges normally for |t|<1/C. Choose R>0 with 2*R<1/C.
The bound on |t|<=2*R and Cauchy's derivative formula give a single
C_B>=1 such that

    |partial_t^j B(v,t)|<=C_B^(j+1)*j!,
                      |t|<=R, j>=0.                 (8)

The coefficient identity at zero is
partial_t^j B(v,0)=a_(j+1)(v). No divergent formal series is summed
in (7); division by (k-1)! yields an actually convergent germ.

Choose ell>0 small enough that a=b-2*ell and v0=b-ell belong to I,
and that 2*ell/10<R. Such a choice is possible since
b>=omega+delta/2. All these numbers are fixed independently of n.
For v in [v0,b] follow the finite complex path

    t=S(v)-S(w),                 w from v down to a.

Writing w=v-tau, (5) supplies the uniform bounds

    Re t>=tau/270, |t|<=tau/10, |dt|<=d tau/10,
    0<=tau<=v-a<=2*ell,
    T_v=S(v)-S(a), Re T_v>=ell/270.                   (9)

All paths lie inside |t|<R. Set

    A_n(v)=a_0(v)+integral_(0 to T_v along this path)
                                  exp(-n*t)*B(v,t)dt. (10)

This is defined only at the allowed integer n if desired. For m>=2,
integrate by parts m-1 times along the finite path. The endpoint
primitive identity is valid on each smooth path because B is
holomorphic in t. It gives exactly

    A_n(v)-sum_(k=0)^(m-1) a_k(v)*n^(-k)
      =-exp(-n*T_v)*sum_(j=0)^(m-2)
                         partial_t^j B(v,T_v)*n^(-j-1)
       +n^(-(m-1))*integral_0^(T_v)
                         exp(-n*t)*partial_t^(m-1) B(v,t)dt. (11)

For m=1 the sum is empty and the last integral is simply (10)'s
integral, so the same interpretation holds. From (9),

    integral_path |exp(-n*t)| |dt|<=27/n.             (12)

Consequently the last term of (11) is at most
27*C_B^m*(m-1)!*n^(-m). Choose epsilon_1>0 with
C_B*epsilon_1<=1/2. If m<=epsilon_1*n, (8) bounds the endpoint sum by

    (C_B/n)*sum_(j=0)^(m-2) C_B^j*j!/n^j<=2*C_B/n.  (13)

Here j!<=j^j and C_B*j/n<=1/2 for j>=1; the j=0 term is one.
Thus, for all such m, (11) has a factorial error plus an endpoint
error at most (2*C_B/n)*exp(-n*ell/270), with constants independent
of m,n,v.

Compare (11) with the exact (1). There are constants D>=1,epsilon_2>0
such that for 1<=m<=epsilon_2*n the difference Q_n-A_n is at most

    D^(m+1)*m!*n^(-m)+(2*C_B/n)*exp(-n*ell/270).       (14)

Choose eta>0 with eta<=epsilon_2 and D*eta<=1/4, and set
m=floor(eta*n). For n>=2/eta, m>=eta*n/2, and

    D^(m+1)*m!*n^(-m)<=D*(D*m/n)^m
                             <=D*exp(-eta*log(4)*n/2).

Equations (9), (13)--(14) prove, for some c>0,

    sup_(v in [v0,b]) |Q_n(v)-A_n(v)|<=C_2*exp(-c*n). (15)

This is a comparison with the full exact sequence. All complementary
contour errors are already included in (1); no additional tail is
discarded in passing to (15). There is no division by a possibly small
signed integral and no interpolation to noninteger sizes.

### 3. A fixed upper-triangular operator and its support edge

Multiplying (10) by exp(n*S(v)) and changing its finite path variable
back to w gives the exact identity

    exp(n*S(v))*A_n(v)
      =a_0(v)*exp(n*S(v))
       +integral_a^v exp(n*S(w))*B(v,S(v)-S(w))*S'(w)dw. (16)

The sign is positive: t runs from 0 to T_v as w runs from v to a,
and dt=-S'(w)dw. All factors are bounded on this fixed triangle.
After multiplying by chi(v) and integrating v from v0 to b, compact
Fubini is therefore legitimate. The part with w>=v0 is

    integral_(v0)^b f(w)*exp(n*S(w))dw,
    f(w)=a_0(w)*chi(w)
          +S'(w)*integral_w^b chi(v)*B(v,S(v)-S(w))dv. (17)

This f is a fixed smooth, possibly complex-valued density on [v0,b].
The part with a<=w<=v0 is bounded by C_3*exp(n*r(v0)). The original
integral with v<=v0 has the same bound: (1) at m=1 bounds Q_n uniformly
and r is increasing. Integration of (15) against chi*exp(n*S) has
bound C_4*exp(n*(r(b)-c)). Therefore (3) holds, for example with

    gamma=min(c,r(b)-r(v0))/2>0.                      (18)

This localization is an identity plus an exponentially smaller error
for the original bump, not a replacement of that bump.

The upper-triangular operator in (17) preserves its right support edge.
To verify the needed inverse implication explicitly, suppose f is zero
on [b-e,b] for some e>0. On this interval divide by a_0, whose modulus
has a positive lower bound by L720. The remaining integral kernel is
bounded; write its modulus bound as M. Shrink e to e'>0 so that
e'<ell and M*e'<1 (if M=0 choose any sufficiently small e'). Then

    sup_[b-e',b] |chi|
               <=M*e'*sup_[b-e',b] |chi|.

Thus chi vanishes on that terminal interval, contradicting the
definition of b=sup supp(chi). Hence f is nonzero in every terminal
neighborhood of b. This establishes the support property of this actual
operator; it assumes neither noncancellation nor analyticity of chi.

### 4. The sampled Cauchy germ and the endpoint contour test

For q>=0 define the fixed-density moments

    M_q=integral_(v0)^b f(v)*exp((12q+3)*S(v))dv,
    R_*=exp(-12*r(b)), z_*=Z(b).

Uniform convergence of the geometric series on compact subdisks of
|z|<R_* justifies the exact generating formula

    M(z)=sum_(q>=0) M_q*z^q
        =integral_(v0)^b h(v)/(Z(v)-z)dv,
    h(v)=f(v)*exp(3*S(v))*Z(v).                       (19)

The same integral defines a holomorphic function off the compact arc
Gamma=Z([v0,b]), by positive distance from that arc on each compact
subset. Since |Z| is strictly decreasing, z_* is its unique point
of minimum modulus. The nonvanishing factors in h preserve f's
right support edge.

We show that the germ (19) cannot extend holomorphically through z_*.
It suffices for (2) to rule out extension to any disk of radius >R_*.
Suppose such an extension exists. The inverse theorem and Z'(b)!=0
give a small complex disk about b on which Z is one-to-one. By shrinking
it further, its image U has the following properties: U lies inside
the purported extension domain, and its intersection with Gamma is
exactly the image of the real segment ending at b. To exclude remote
pieces, first use injectivity on a larger local disk; then the compact
remaining real subarc is separated from z_* by (5)--(6), and a smaller
image U avoids it. Thus no unproved alias separation is being used.

More explicitly one can take U=Z({|w-b|<r0}), with

    U intersect Gamma=Z((b-r0,b]).

In this coordinate U minus Gamma is a disk cut along a real radius,
so it is connected. It contains an open set with |z|<R_*: for real
w>b sufficiently close to b, the continued inequality Re S'(w)>0
gives |Z(w)|<R_*. On that open set the extension equals the integral
(19). The identity theorem therefore identifies them on all of
U minus Gamma, on both sides of the slit. This is the point that an
interior branch jump alone would not establish.

For any 0<rho<r0 let C_rho be the positively oriented image under Z
of the circle |w-b|=rho. It meets Gamma exactly once, at Z(b-rho),
and transversally. Except at that one point, the integral in (19)
equals the asserted holomorphic extension on C_rho. The double integral
in the following contour computation is absolutely integrable. Indeed,
near the crossing, write the circle parameter as theta near pi and
v near b-rho. The difference

    Z(v)-Z(b+rho*exp(i*theta))

has, as a map of the two real variables, an invertible linear part
proportional to (v-(b-rho))+i*rho*(theta-pi). The nonzero Z' makes
its modulus bounded below by a positive constant times the Euclidean
distance to the crossing on a small neighborhood. The reciprocal of
that distance is locally integrable in two dimensions. Numerators and
curve speeds are bounded; away from the crossing compactness supplies
the remaining domination. Hence Fubini is valid even though the
pointwise contour formula is undefined at one parameter pair.

The holomorphic extension and the residue theorem now give

    0=integral_(C_rho) M(z)dz
     =integral_(v0)^b h(v)
                    *[integral_(C_rho) dz/(Z(v)-z)]dv
     =-2*pi*i*integral_(b-rho)^b h(v)dv.              (20)

The residue is -1 for b-rho<v<=b and zero for the remaining v;
the boundary value v=b-rho has measure zero. Holomorphic injectivity
of Z preserves the positive contour orientation and identifies its
interior. Because (20) holds for every sufficiently small rho and h
is continuous, differentiation yields h(b-rho)=0 for all those rho.
Then f vanishes on a terminal interval, contradicting Section 3.

This proves the required nonremovable endpoint singularity of the
germ from the origin. It does not rely on positivity of Taylor
coefficients, a specified flatness law or two unrelated boundary
branches of a Cauchy integral.

### 5. Exact samples, the entire error series and the limsup

Equation (3) compares the moments in (19) with
J_n=n^(-1/2)*K_n for all sufficiently large permitted n. Its error
series sum E_(12q+3)*z^q is normally convergent for

    |z|<exp(-12*(r(b)-gamma))>R_*.                   (21)

Omitting the finitely many sizes preceding (3) changes a generating
germ by a polynomial only. Thus the entire error, including the original
complementary contour, cannot remove the singularity in Section 4.

For completeness, the lower implication can be obtained directly from
coefficient bounds, without assuming a root asymptotic. If
limsup log|J_n|/n<r(b), choose a finite r1 strictly between r(b) and
max(r(b)-gamma,limsup log|J_n|/n). For all sufficiently large permitted
n, both J_n and E_n then have modulus at most a constant times
exp(n*r1). Their difference M_q has that bound at n=12q+3. The
series in (19) would consequently converge normally on
|z|<exp(-12*r1)>R_*, contradicting (20). This argument also covers
limsup=-infinity and zero subsequences.

Finally (1) at m=1 gives the direct upper bound

    |K_n|<=C_5*sqrt(n)*||chi||_L1*exp(n*r(b)).         (22)

The normalization n^(-1/2) changes log modulus divided by n by
(log n)/(2*n), which tends to zero and leaves every zero unchanged.
The lower implication and (22) establish (2), with log(0)=-infinity.
Only a limsup is established; no effective onset, full limit, eventual
nonvanishing, residue comparison or RH conclusion has been inferred.

### 6. Separate conceptual audit — 3 November 2026, step 196

The unchanged invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-03-signed-bump-support-transfer-audit.md`.
This audit read Sections 1--5 in full and checked their uses of the
audited L714 identities, L719 phase and L720 symbol, including L720's
whole-contour combination. It reproduces and validates the existing
local argument; it is not a new general support theorem or a claim of
progress beyond the sources checked. The common-phase and gamma/Rice
failures do not supply or invalidate any premise of this construction.

The standard tools in Section 1 are imported with their stated
hypotheses. The identity theorem and holomorphic parameter-integral
criterion are [DLMF 1.10(ii), (viii), (1.10.18)](https://dlmf.nist.gov/1.10).
For both Fubini uses, the precise additional input is Terence Tao,
*An Introduction to Measure Theory*, AMS GSM 126 (2011),
[author-hosted December 2012 preliminary text](https://terrytao.wordpress.com/wp-content/uploads/2012/12/gsm-126-tao5-measure-book.pdf),
Theorem 1.7.21 and its proof, printed pp.204--205, and Corollary 1.7.23,
p.206. It applies to measurable complex functions with integrable
modulus on the product of complete sigma-finite measure spaces.
Here these are finite real parameter intervals with completed Lebesgue
measure. The duplicated iteration in that version's (iii) is not used;
clauses (i)--(ii), the proof and corollary give the swapped-order result.
These sources were inspected in the saved assessment and are reused,
not re-proved. The application checks follow.

**Geometry and common domains.** From the specified S and s_v, the
chain rule gives (4) with its minus sign: z_v'=-u*z_v/A and
z_v*F'(z_v)=-s_v. The saddle rectangle bounds the real numerator
in (4) between 1/100 and 9/200 and the imaginary numerator between
33/200 and 1/5. Division by 27/10 gives exactly (5). The sum of
the two upper bounds is 49/540<1/10. Thus r'>0 and Z'!=0 on I,
and |Z| strictly decreases there. Compactness gives the needed real
extension at b, even if b is the enclosure endpoint. Taking ell
sufficiently small keeps a=b-2*ell inside I; no endpoint law for chi
enters. All symbol neighborhoods and all subsequent constants are
fixed before n or the truncation order.

**Finite realization and optimal truncation.** On a common smaller
closed v neighborhood the termwise majorant for (7) is summable on
|t|<=2*R when 2*C*R<1. Its sum has a uniform bound M_B; Cauchy
on the t disk then gives M_B*j!*R^(-j) on |t|<=R, which is (8)
after one enlargement of C_B. The factorial in (7) is essential:
the j-th derivative at zero is a_(j+1), without an additional j!.
An integration by parts contributes B(v,0)/n, subtracts
exp(-n*T_v)*B(v,T_v)/n, and leaves n^(-1) times the integral of
partial_t B. Iterating gives every sign and power in (11); at m=1
the endpoint sum is empty. From (9) the modulus integral is at most
(1/10)*integral_0^infinity exp(-n*tau/270)d tau=27/n.
For the endpoint sum, j!<=j^j and C_B*j/n<=1/2 give the geometric
bound 2*C_B/n uniformly through m<=epsilon_1*n. Thus both errors
in (14) are uniform at m=floor(eta*n); the factorial term is at most
D*4^(-m), and Re T_v>=ell/270 controls the other endpoint.
L720 (2) is for the full Q_n: its Section 4 explicitly absorbs the
entire complementary circle error at every order. Hence (15) retains
that error, rather than assuming it small relative to the signed K_n.

**Localization and actual support.** The substitution in (16) has
dt=-S'(w)dw; reversing its endpoints gives the plus sign. For each n
the double integral on a<=w<=v<=b, v>=v0, is bounded and therefore
absolutely integrable. Its w>=v0 part is exactly (17). The lower
triangle has r(w)<=r(v0); the original omitted v<=v0 piece has the
same bound since Q_n is uniformly bounded by (1) with m=1. Together
with (15), these are all of the errors in (3), with gamma in (18).
If f vanishes on a terminal interval, division by the nonzero a_0
gives the stated contraction on a sufficiently short terminal interval.
It forces chi=0 there, contradicting b=sup supp(chi). Neither a sign
for f nor an analytic extension of chi is used.

**One germ on both sides and the crossing integral.** On compact
subdisks of |z|<R_* the geometric ratio has modulus uniformly less
than one, giving precisely h=f*exp(3*S)*Z in (19). Off Gamma, positive
distance on compact sets bounds the integrand and its z derivative,
so the integral is holomorphic. Choose the inverse chart with closure
in a larger injective chart and r0<ell. Strict monotonicity of |Z| on
the real arc separates every remote arc portion from z_*. After
shrinking, U=Z({|w-b|<r0}) therefore meets Gamma in just
Z((b-r0,b]). Its slit complement is connected, and real w>b maps
inside |z|<R_*, giving a nonempty open common set. The identity theorem
identifies the proposed disk extension and (19) on both sides of the
slit; they are not independent branches.

For each fixed 0<rho<r0, write v_c=b-rho and theta=pi+t.
The denominator at the unique crossing has expansion

    Z(v)-Z(b+rho*exp(i*(pi+t)))
      =Z'(v_c)*[(v-v_c)+i*rho*t]
                        +O((v-v_c)^2+t^2).

Its real linear map has nonzero determinant rho*|Z'(v_c)|^2.
On a sufficiently small parameter disk its modulus is bounded below
by a positive constant times sqrt((v-v_c)^2+t^2). The modulus of
the numerator h(v) times the contour speed is bounded. In polar
coordinates the integral of the reciprocal distance is 2*pi times
the disk radius, hence finite; away from this sole crossing compact
separation bounds the rest. Fubini therefore applies to the entire
double integral, with the crossing assigned any value on its null set.
No bound uniform as rho tends to zero is needed.

Holomorphic injectivity preserves positive orientation and maps the
disk interior to the interior of C_rho. The inner integral in (20)
is -2*pi*i exactly for b-rho<v<=b and zero for all other v except
the one boundary value. The holomorphic extension has zero contour
integral. Thus the terminal integral of h is zero for every small
rho. Differentiating it gives h(b-rho)=0; continuity includes b.
The factors exp(3*S)*Z are nonzero, contradicting the support result
for f. The original sampled germ has the asserted endpoint obstruction.

**Full error and exact subsequence.** The estimate in (3) gives
normal convergence of its error series on (21). This means a larger
disk, not an assertion that the error series is entire on C. Start
both sampled series at any q0 for which (3) holds; the finitely omitted
M_q form a polynomial. No definition or estimate for an inadmissible
small kernel size is needed. If the limsup for J_n is below r(b),
choose max(r(b)-gamma,limsup log|J_n|/n)<r1<r(b). Both J_n and E_n
are bounded by constant multiples of exp(n*r1). At n=12q+3 this
would extend the moment series to |z|<exp(-12*r1), contrary to the
endpoint obstruction. This includes limsup=-infinity and zero terms.
Finally (22) and log(sqrt(n))/n -> 0 give precisely (2).

All claimed conclusions survive this independent audit. Direct inputs
remain L714, L719 and L720; L715/L716 are inherited through those inputs.
L713's envelope, L714 (6), L717 and L718 remain excluded. The audit
does not determine a full limit, eventual nonvanishing, the residue
comparison, any other response, a spatial Jensen bound or an Xi sign.

## Mathlib

Full matching coverage for this exact discrete support-transfer result
has not been checked. Supporting ingredients are the holomorphic inverse
theorem, Cauchy estimates, finite contour integration, uniform power-series
convergence and compact Fubini; no matching Mathlib theorem names have
been verified here. Unknown availability is not evidence of absence.
