# Corollary 997l: quarter-jet cancellation forces original-TV target loss

## Hypotheses

Use the COMPLETE response H_n^+(z;mu) of C997c(1), with its original
K_(n+2)=(L_(n+1)^(2)-1)/(n+1), integer n>=2. Put

    J=[15/8,17/8], z_star=1+i/8, m=floor(n/4),
    phi(c)=arccos(1-c/2)+sqrt(c*(4-c))/2.

Take the real branches in phi on J. Fix kappa=1 and one A in C997e's
sufficiently large admissible range before n. For a nonzero complex
polynomial P of degree<=n use the ORIGINAL normalization

    M_n(P)=integral_J exp(-A*n*(c-2)^2)*|P(c)|dc,
    dmu_P(c)=M_n(P)^(-1)*1_J(c)*exp(-A*n*(c-2)^2)*P(c)
                                      *exp(i*n*(phi(c)-c))dc.       (1)

Impose the exact constraints on the COMPLETE response

    (d/dz)^j H_n^+(2;mu_P)=0, 0<=j<m.                            (2)

Both beta terms, both short intervals, both slope endpoints and K's
constant subtraction are retained. These are finite hypothetical slope
measures, not actual zeta-zero data. In particular no separate moment
cancellation is assumed for the two spectral intervals or the two
analytic Laguerre branches. The fixed-A hypothesis keeps this result
inside the approved polynomial-packet scope; no numerical admissible
A or nonempty admissible range below 6553600 is assumed.

## Conclusion

For every n>=2 there are nonzero polynomials satisfying (1)-(2), with
original TV exactly one. The maximum of |H_n^+(z_star;mu_P)| over this
constrained normalized class is attained, although it may be zero.
There are absolute constants C<infinity and n_0 such that EVERY such
polynomial, including every maximizer, satisfies for n>=n_0

    sup_(gamma in J)|H_n^+(gamma;mu_P)|
                                 <=C*(n+2)*exp(-n/96),           (3)
    |H_n^+(z_star;mu_P)|          <=C*(n+2)*exp(-n/24).           (4)

The constants are independent of P and the fixed admissible A. Hence
the quarter-jet design pays closed-band suppression for every fixed
0<sigma<1/96 eventually, but cannot retain target size exp(-a_n) with
a_n>=0 and a_n/n->0 on any unbounded integer subsequence. If a scalar
multiple nu_n=s_n*mu_P meets that target threshold, then

    ||nu_n||_TV >= exp(n/24-a_n)/(C*(n+2)).                       (5)

A zero target cannot be normalized to a nonzero value. This stops the
specified floor(n/4) exact-jet selection, not all polynomial packets,
fewer or approximate jets, or the general point inequality.

Step342, 11 November 2026: RESEARCH / REPRODUCTION, outcome NEGATIVE,
under unchanged pre-invocation EXPLORE review329 and its COVERED_TARGET.
This is a sharper local subclass obstruction by specialization of
standard complex-approximation tools; no originality or progress beyond
the sources checked is claimed. The independent step344 conceptual
audit below accepts (1)-(20) without changing hypotheses or bounds.
It is not an RH candidate or an actual-Xi positivity statement.

## Proof

### Reused contracts and the quantitative specialization

Import C997c(4)-(6), accepted by its step322 audit, for the exact finite
complex spectral measures, their supports and their total variations.
Its Laguerre estimate is L997(4), from
[NIST DLMF18.14.8](https://dlmf.nist.gov/18.14.E8), with the constant
subtraction included. Its finite-measure Fubini contracts and their
hypotheses remain as specified in that audited proof; we do not reprove
the Laguerre bound or substitute an asymptotic response here.

Use the standard rank-nullity theorem, precisely the Fundamental
Theorem of Linear Maps in Sheldon Axler,
[*Null Spaces and Ranges*](https://linear.axler.net/NullRange.pdf),
author-hosted slides retrieved 10 November 2026, PDF pp17-24, as
inspected in review332. Also use Cauchy's integral and derivative
formulas [DLMF1.9.30-31](https://dlmf.nist.gov/1.9#iii) and the Laurent
expansion theorem on an annulus, precisely
[DLMF1.10(iii), equations1.10.6-7](https://dlmf.nist.gov/1.10#iii).
For the ellipse coefficients and projection tail import L. N. Trefethen,
*Approximation Theory and Approximation Practice*, SIAM, 2013,
Chapter8, Theorems8.1/8.2, equations(8.1)-(8.3), in the
[primary chapter source](https://raw.githubusercontent.com/chebfun/ATAP/development/chap8.m),
lines104-169 including the complete proofs, inspected in step343.
That development-branch source was retrieved 11 November 2026; no commit
hash or identity with a particular book edition was established.
Use [DLMF18.5.1](https://dlmf.nist.gov/18.5.E1) for finite exterior
Chebyshev evaluation. The two newly inspected DLMF sections were
version1.2.8, release15 September2026, retrieved11 November2026.
These are known general tools. The finite
dimensional compactness statement used below is the Heine-Borel theorem.

Review329 covers the original weighted-L1 polynomial class and complex
growth costs; no stronger weighted extremizer theorem is imported.
C997g and its audit334 are comparison evidence for the stopped full
n-jet design, not a premise that m jets already fail. The required
specialization here is an ellipse coefficient estimate with only
m-1 degrees, including paid growth on the lower spectral interval.
The coefficient calculation is included to expose that cost, not as
a reproof or novelty claim for classical Chebyshev approximation.
No analytic saddle expansion, whole-line replacement, response Gram
estimate or unproved target condition number is used.

### Exact feasibility and the target maximizer

For fixed n let the unnormalized measure in (1), without M_n(P)^(-1),
be denoted by tilde_mu_P. Its dependence on the n+1 complex polynomial
coefficients is linear. Every fixed-order response derivative is a
complex-linear functional of P: all c and t domains are compact, and
differentiation of exp(izt) is dominated on compact z sets by a finite
constant against the finite variation measure. More explicitly, with
T=17(n+2)/8, |(it)^j exp(izt)|<=T^j exp(R*T) for |z|<=R on both
supports. This justifies entire dependence and every derivative used.

The m homogeneous constraints on tilde_mu_P therefore have a kernel
W_n of dimension at least n+1-m>0. A nonzero polynomial has only
finitely many zeros on J, and the Gaussian weight is positive and
continuous. Thus 0<M_n(P)<infinity for P!=0, and M_n is a norm on this
finite dimensional polynomial space. It is continuous in coefficients
by finite integration and the triangle inequality. On the Euclidean
coefficient unit sphere it has a positive minimum: continuity gives
an attained minimum by Heine-Borel, and a zero minimum would contradict
positive definiteness. Consequently {P in W_n:M_n(P)=1} is nonempty,
closed and bounded in coefficients, hence compact. The target
functional is continuous, so its absolute value has a maximum there.

Division by M_n(P) preserves all zero derivatives. The phase phi(c)-c
is real, so the measure (1) has TV precisely one. Every normalized
response in the statement arises from an element of that compact unit
sphere. Neither this existence argument nor the maximization asserts
that the target functional is nonzero on W_n. The bound below applies
even if it vanishes identically.

### Combined moments and the full spectral supports

For each such normalized measure C997c(4)-(6) gives exactly

    H(z)=H_n^+(z;mu_P)=integral exp(izt)d(nu_U+nu_L)(t),
    supp(nu_U) subset [15*n/8,17*(n+2)/8],
    supp(nu_L) subset [n,n+2],
    ||nu_U||_TV<=U*(n+2)*exp(9*n/32), U=18*exp(27/16),
    ||nu_L||_TV<=L*(n+2)*exp(-n/16), L=8*exp(3/4).          (6)

The narrower upper support follows from c in J; the coarser TV bounds
from I in C997c are retained. Both finite Fourier integrals are entire
by the same dominated differentiation. If nu=nu_U+nu_L, the constraints
give exactly

    integral exp(2it)*Q(t)dnu(t)=0 for deg(Q)<=m-1.          (7)

Indeed H^(j)(2)=i^j integral t^j exp(2it)dnu(t). Equation (7) is for
the SUM of the spectral measures only. It does not permit separate
subtraction from one interval without accounting for the other.

### An ellipse approximant within the fractional degree budget

Set

    b=2*n+17/8, r=(n+17)/8, a=n+1, d=b-a=n+9/8,
    tau=r/d, ell=ceil(n/log(d)), N=m-1-ell.                 (8)

Choose one absolute n_0 sufficiently large that, for all n>=n_0,

    tau<=1/6, N>=0, ell*log(224/31)<=n/96,
    d^(-ell)<=exp(-n).                                    (9)

Such an onset exists: tau<=1/6 for n>=47, ell/n->0,
m/n->1/4, and ell*log(d)>=n. No explicit small onset is claimed.
In particular (9) also gives ell*log(48/31)<=n/96.

For z in J union {z_star}, write s=i(z-2), y=(t-b)/r. On the
filled ellipse with semiaxes 17/8 and 15/8 define

    f_s(y)=exp(s*r*y)*(1+tau*y)^(-ell).

The boundary is y=(w+w^(-1))/2, |w|=4. Since |y|<=17/8,
|1+tau*y|>=31/48 on the entire filled ellipse, so f_s is holomorphic
on a neighborhood of it. Put

    E_s=r*sqrt((17*Re(s)/8)^2+(15*Im(s)/8)^2),
    B_s=exp(E_s)*(48/31)^ell.                             (10)

On the boundary, writing y=(17/8)cos(theta)+i(15/8)sin(theta)
shows Re(s*r*y)<=E_s, so |f_s|<=B_s there.

Here is the full coefficient estimate used, including its domain.
The composition F_s(w)=f_s((w+w^(-1))/2) is holomorphic on a
neighborhood of 1/4<=|w|<=4 and invariant under w->1/w. Its Laurent
coefficients c_j satisfy c_(-j)=c_j by uniqueness of Laurent expansion.
Cauchy's coefficient formula on |w|=4 gives

    |c_j|<=B_s*4^(-j), j>=0.

Let T_0(y)=1, T_1(y)=y and T_(j+1)(y)=2*y*T_j(y)-T_(j-1)(y).
Induction gives T_j((w+w^(-1))/2)=(w^j+w^(-j))/2. On |w|=1,
absolute convergence therefore gives, for every y in [-1,1],

    f_s(y)=c_0+2*sum_(j>=1)c_j*T_j(y).

Define S_N(y)=c_0+2*sum_(j=1)^N c_j*T_j(y). Since |T_j(y)|<=1
on [-1,1], summing the COMPLETE tail proves

    sup_[-1,1]|f_s-S_N|<=(8/3)*B_s*4^(-(N+1)).             (11)

For real |y|<=8 the same polynomial identity gives |T_j(y)|<=16^j:
inside [-1,1] use the unit circle, and outside it use the real root
of modulus |y|+sqrt(y^2-1)<=8+sqrt(63)<16. Thus the finite sum gives

    |S_N(y)|<=B_s+2*B_s*sum_(j=1)^N 4^j
                   <=(8/3)*B_s*4^N, |y|<=8.             (12)

This is a bound on a finite polynomial outside its approximation
interval, not a claim that the infinite series converges there.

Use the following polynomial in the SPECTRAL variable t:

    Q_(n,z)(t)=exp(s*b)*(1+(t-b)/d)^ell*S_N((t-b)/r).       (13)

Its degree is at most ell+N=m-1, so it is allowed in (7). It is not
the original slope polynomial P and never replaces M_n(P).

On the upper support |y|<=1 and |1+tau*y|<=7/6. Since
exp(s*t)=exp(s*b)*(1+tau*y)^ell*f_s(y), (11) gives

    sup_upper |exp(s*t)-Q_(n,z)(t)|
      <=(8/3)*exp(Re(s)*b+E_s)*(224/31)^ell*4^(-m).         (14)

Here N+1=m-ell and 4*(7/6)*(48/31)=224/31. On the lower support,

    |1+(t-b)/d|=|t-a|/d<=1/d,
    |(t-b)/r|<=(d+1)/r=(8*n+17)/(n+17)<8.

Equation (12) consequently proves

    sup_lower |Q_(n,z)(t)|
      <=(8/3)*exp(Re(s)*b+E_s)*(48/31)^ell*d^(-ell)*4^N.    (15)

Both closed endpoints of each interval are included. The lower factor
in (13) pays its distant-interval growth without assuming separate
upper-band cancellation.

### Uniform rates for the complete response

Subtract (13) using the combined identity (7), before splitting the
integral:

    H(z)=integral exp(2it)*(exp(s*t)-Q_(n,z)(t))dnu(t).     (16)

For real t, |exp(2it)|=1. Bound the upper contribution using (14),
and the lower contribution using (15) plus the original exp(s*t).

The elementary bounds 4/3<log(4)<2 suffice. For example
log(2)=2*integral_0^(1/3)(1-u^2)^(-1)du>2/3, while
log(2)=integral_1^2 dx/x<1. Since m>=n/4-1 and N<=n/4,

    4^(-m)<=4*exp(-n/3), 4^N<=exp(n/2).                   (17)

For real z in J, Re(s)=0 and |Im(s)|<=1/8, so
E_s<=15*r/64<=r/4=n/32+17/32. Combine (6),(9),(14)-(17) to obtain

    |H(z)| <= (32/3)*U*exp(17/32)*(n+2)*exp(-n/96)
                +L*(n+2)*exp(-n/16)
                +(8/3)*L*exp(17/32)*(n+2)*exp(-25*n/48),
                                                       z in J. (18)

The upper rate is 9/32+1/32+1/96-1/3=-1/96. The lower-polynomial
rate is -1/16+1/32+1/96-1+1/2=-25/48. The unaltered lower
exponential has modulus one. Thus this estimate is uniform on the
entire closed band, not just at nodes or at the jet center.

At z=z_star, s=-1/8-i. Equation (10) gives

    E_s=r*sqrt(14689)/64<2*r,
    Re(s)*b+E_s<=-b/8+2*r=255/64.                         (19)

In particular the target's exp(-b/8) exactly offsets the n-dependent
part of this coarse ellipse bound; it has not been dropped. The upper
rate is now 9/32+1/96-1/3=-1/24. The lower-polynomial rate is
-1/16+1/96-1+1/2=-53/96. On the lower support the original exponential
has modulus exp(-t/8)<=exp(-n/8). Hence

    |H(z_star)| <= (32/3)*U*exp(255/64)*(n+2)*exp(-n/24)
                     +L*(n+2)*exp(-3*n/16)
                     +(8/3)*L*exp(255/64)*(n+2)*exp(-53*n/96).
                                                                  (20)

For example the absolute constant

    C=(32/3)*U*exp(255/64)+L+(8/3)*L*exp(255/64)

suffices in both (3) and (4), since 255/64>17/32 and the remaining
rates are more negative. Every onset condition in (9) is independent
of A and P. We used only the original TV, the exact moments and the
closed spectral supports, not a coefficient bound on P.

Finally log(C*(n+2))=o(n). This proves the asserted band threshold
for any sigma<1/96, while
log(C*(n+2))-n/24+a_n tends to minus infinity when a_n/n->0.
Thus (4) contradicts target retention on every unbounded subsequence.
Complex linearity of H and TV(mu_P)=1 give (5).

### Qualifications and remaining gaps

Unlike a failed upper estimate, (4) is an actual conflicting bound
for every member of the specified class, including an exact target
maximizer. Existence alone would not have proved this. The argument
does not require that C997e's admissible A<6553600 range be nonempty:
it applies to any admissible fixed A, and in particular to any member
of that range if present. C997e supplies the phase and inherited scope
only; none of its large-A saddle estimates is used. No varying-A claim
or new optimal fraction of canceled moments is asserted.

The exact spectral measures already include both Laguerre branches,
both beta terms, both short intervals and K's -1. All operations are
finite-measure integrals, dominated differentiation or convergent
series on explicitly stated domains. No actual-zero sign assumption,
infinite-zero sum or RH-equivalent positivity is used.

This obstruction strengthens the scope of the exact-jet route stop
from n jets to the nominated floor(n/4) jets, with weaker but still
positive rates. Smaller or approximate jet budgets and arbitrary
polynomial designs are not decided. C997c branch recovery, the point
bridge, selected/both-sign transfer, C997a(8), original assay,
reconstruction, signed recovery, infinite-zero complements, regulator
uniformity, L993, L984(H) and actual-Xi positivity remain distinct
unpaid steps. The scoped proof is accepted by the audit below and leaves
STATUS IN_PROGRESS.

### Independent conceptual audit — step344, 11 November 2026

RESEARCH / REPRODUCTION under the unchanged pre-invocation SPECIALIZE
review342, whose primary source gap was filled in the separate step343.
The audit accepts (1)-(20), including both original-TV rates, without
correction or extension. This establishes a checked local obstruction,
not a result beyond the sources assessed or an RH candidate. The
following checks concern this specific specialization; the general
rank-nullity, Laurent and Chebyshev theorems are imported above.

**Feasibility, normalization and quantifiers.** Before normalization the
response is complex-linear in the n+1 coefficients of P. Its compact
spectral support is contained in [0,T], T=17(n+2)/8, and its variation
is finite for each coefficient vector. For every j and compact |z|<=R,
the derivative integrand has modulus at most T^j exp(RT), integrable
against that variation. Dominated differentiation therefore justifies
every derivative used in the homogeneous constraints. Rank-nullity gives dimension at
least n+1-floor(n/4)>0 without requiring independent constraints. At
n=2,3 the constraints are empty; the existence claim still holds.

The positive continuous Gaussian weight makes M_n a norm, since a
nonzero polynomial cannot vanish almost everywhere on J. In coefficient
coordinates it is continuous; its minimum on the Euclidean unit sphere
is positive. Thus its unit sphere in the closed linear kernel is
compact and nonempty for each fixed n and A. The target functional is
continuous on that sphere, proving attainment, even if its maximum is
zero. These compactness constants need not be uniform in n or A and
are not used in any response estimate. Real phi-c gives TV=1 exactly;
normalization neither adds nor removes a zero derivative.

**Exact combined measure and support geometry.** Applying the audited
C997c(4)-(6) to the measure supported on J gives the narrower upper
support [15n/8,17(n+2)/8] by direct inspection of its density. Its
midpoint and radius are exactly b and r in (8). The lower support has
midpoint a=n+1 and radius one. J is contained in C997c's I, so its
coarser upper/lower variation constants U and L remain valid at TV=1.
The identity H^(j)(2)=i^j integral t^j exp(2it)d(nu_U+nu_L) proves
(7). It does not prove either interval's moments vanish separately.
Equation (16) correctly subtracts the same polynomial from the combined
measure before the triangle inequality is used. Both beta terms, K's
constant and both closed intervals remain in that measure.

**Onset and analytic domain.** Algebra gives
tau=(n+17)/(8n+9)<=1/6 exactly when n>=47 for integer n. Since log(d)
tends to infinity, ell/n<=1/log(d)+1/n tends to zero, while m/n tends
to 1/4. Thus N>=0 and ell log(224/31)<=n/96 hold for every sufficiently
large n, with one absolute onset. Since d>1 and ell log(d)>=n, the
final condition d^(-ell)<=exp(-n) holds automatically. Also
log(48/31)<log(224/31). No A, polynomial coefficients or unspecified
asymptotic amplitude enter these onset conditions.

The filled ellipse has maximal modulus 17/8. Hence
|tau*y|<=17/48 and |1+tau*y|>=31/48 there. This strict separation
from the sole possible pole gives holomorphy on an open neighborhood
of the entire filled ellipse. The Joukowski map of the closed annulus
1/4<=|w|<=4 lies in that ellipse; compactness and continuity give an
open annular neighborhood on which F_s is holomorphic. Thus the
Laurent coefficient contour at radius4 is permitted, without an
unjustified appeal to holomorphy on a disk containing w=0. For
s=alpha+i*beta the boundary exponent is
r*((17/8)*alpha*cos(theta)-(15/8)*beta*sin(theta)), whose maximum
is E_s. This verifies the bound B_s with its full n,z,ell dependence.

**Coefficient convention and distant finite evaluation.** Invariance
under w->1/w and uniqueness of the annular expansion give c_(-j)=c_j.
The circle bound is |c_j|<=B_s*4^(-j) for j>=0. In Trefethen's
Chebyshev convention a_0=c_0 and a_j=2c_j for j>=1, so the constant
term is counted once. Absolute uniform convergence on |w|=1 allows
pairing the positive and negative Laurent coefficients, giving the
Chebyshev series on the full closed [-1,1]. The complete omitted tail
is bounded by 2B_s sum_(j>N)4^(-j)=(8/3)B_s4^(-(N+1)), exactly
(11), including N=0. This matches Theorem8.2's projection, not an
interpolation polynomial from finitely many samples.

For each real exterior y with 1<|y|<=8 select a real solution of
w+w^(-1)=2y whose modulus R=|y|+sqrt(y^2-1) satisfies 1<R<16.
DLMF18.5.1 gives |T_j(y)|<=(R^j+R^(-j))/2<=R^j<=16^j.
The same bound holds inside [-1,1] and at both endpoints. Therefore
the finite sum in (12) is at most
B_s[1+2*(4^(N+1)-4)/3]=B_s[(8/3)*4^N-5/3], for every N>=0,
which proves its stated upper bound. No infinite series is evaluated
at these exterior y values.

**Degree and the paid lower factor.** Q_(n,z) in (13) has degree at
most ell+N=m-1 in t. Multiplication by its lower factor gives precisely
exp(st) on the upper interval before truncation. There |y|<=1 and
|1+tau*y|<=7/6; the combination
4^(-(N+1))*(7/6)^ell*(48/31)^ell
=4^(-m)*(224/31)^ell proves (14), including its prefactor.
On the lower interval |t-a|<=1, so |1+(t-b)/d|<=d^(-1), and
|(t-b)/r|<=(d+1)/r=(8n+17)/(n+17)<8. Applying only the finite
bound (12) proves (15), with its full 4^N cost. The approximation
polynomial Q is unrelated to the original density polynomial P;
neither the degree allocation nor the lower factor renormalizes TV.

**Both rates and all remaining quantifiers.** The integral identities
for log(2) in (17) prove 4/3<log(4)<2. The floor inequalities
m>=n/4-1 and N<=n/4 then give the stated factor4 in 4^(-m)
and the upper bound exp(n/2) for 4^N. For real z in closed J,
E_s<=15r/64<=r/4=n/32+17/32. The three contributions from (16)
have respective rates

    9/32+1/32+1/96-1/3 = -1/96,
    -1/16,
    -1/16+1/32+1/96-1+1/2 = -25/48.

Their prefactors are exactly those of (18), uniform up to both
endpoints of J. At z_star the value of s is -1/8-i, not merely -i.
Here 14689=17^2+120^2<128^2, so E_s<2r and
-b/8+2r=255/64. The upper rate is
9/32+1/96-1/3=-1/24; the lower polynomial rate is
-1/16+1/96-1+1/2=-53/96. The original lower exponential has
modulus exp(-t/8)<=exp(-n/8), giving rate -3/16 after its TV
bound. This verifies all three terms of (20); the target imaginary
part is essential to this estimate.

The displayed common C dominates both sums because 255/64>17/32
and each residual exponent is more negative than its asserted rate.
C and the onset are independent of P and fixed admissible A. The
nonzero admissible A range from C997e is only a scope assumption;
no assertion that it intersects A<6553600 is required. The proof uses
no saddle asymptotics, no A-dependent compactness constant in a rate,
and no C997i or C997k input. Since log(C(n+2))=o(n), each fixed
sigma<1/96 is achieved on the band eventually, whereas (4) is strictly
below exp(-a_n) eventually whenever a_n=o(n). This excludes retention
on every unbounded subsequence. Linearity and TV=1 prove (5), while
a zero target cannot be made nonzero by scaling.

The audit used exact analytic inequalities, with no sampled or
numerical evidence. Direct mathematical inputs remain C997c and C997e;
the latter provides its phase and inherited parameter scope, not its
asymptotic conclusions. The stop remains confined to the exact
floor(n/4)-jet design. Smaller or approximate jets, other packet
families and every independent actual-Xi gap listed above remain open.

## Mathlib

Full matching coverage for this complete-response fractional-jet
obstruction has not been checked. Supporting rank-nullity, compactness,
complex-integration and polynomial facts do not amount to a formalized
proof of (3)-(5). No Mathlib result or numerical certificate is used
as a substitute for the analytic argument above.
