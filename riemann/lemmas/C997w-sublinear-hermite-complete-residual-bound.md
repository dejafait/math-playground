# Corollary 997w: sublinear lower-node multiplicity pays the complete uncapped residual

## Hypotheses

Let n>=3 be an integer, with natural logarithms throughout. Retain
C997c(1),(4)–(6) and C997s's complete kernel:

    I=[7/4,9/4], z_star=1+i/8,
    gamma_j=15/8+j/(4n), 0<=j<=n,
    K_(n+2)(t)=(L_(n+1)^(2)(t)-1)/(n+1),
    g_n(t)=K_(n+2)(t) exp(-t/2) cosh(3t/8),
    k_n(c,z)=-2 exp(-cn/4) [integral_(cn)^(c(n+2)) g_n(t)exp(izt)dt
                             -integral_n^(n+2) g_n(t)exp(izt)dt].

Set

    m=min{n,ceil(2n/log n)}, ell=n+1-m,
    theta=(n+1)/(2n), a=exp(i theta/2), b=exp(i theta),
    alpha=(-7/2+i/2)n.

On D_n={y: Re(b^(-1)y)>0}, use the holomorphic branch

    Log_n(y)=Log(b^(-1)y)+i theta,
    f_n(y)=exp(alpha Log_n(y)),                            (1)

where Log on the right half-plane has argument in (-pi/2,pi/2).
Let p_n be the degree-at-most-n Hermite interpolant of f_n at a,b,
with multiplicities m,ell, and put A_(j,n)=[y^j]p_n. These coefficients
are unrestricted complex numbers, independent of c. Define

    e_n(t)=exp(i z_star t)-exp(15it/8)p_n(exp(it/(4n))),
    D_n(c)=k_n(c,z_star)-sum_(j=0)^n A_(j,n)k_n(c,gamma_j).

There is no coefficient-cap, positivity, zero-simplicity, reconstruction
or actual-Xi hypothesis. Both beta terms, both full closed spectral
windows, every zero of g_n and K's subtraction are retained.

## Conclusion

There is one integer N>=64, independent of c and of any testing measure,
such that for every integer n>=N,

    sup_(c in I)|D_n(c)| <= 2 exp(-n/32).                 (2)

In particular this specific interpolant meets the approved uncapped
complete-residual target O(exp(-n/64)). An effective numerical N is
not asserted. More explicit bounds for all n>=64 are (9) below.

For every finite complex Borel measure mu on I satisfying

    integral_I k_n(c,gamma_j)dmu(c)=0, 0<=j<=n,

the same N gives

    |integral_I k_n(c,z_star)dmu(c)|
                         <=2 exp(-n/32)||mu||_TV.          (3)

The measures may vary with n. This controls exact band-null target
action. It supplies neither a coefficient norm bound nor an upper bound
for C997s's capped E_n, nor a paid-leakage estimate without an additional
coefficient bound. C997a(8), selected/both-sign transfer, the original
assay and actual reconstruction, complements/regulators, L993, L984(H),
L966/L968 forcing and actual-Xi positivity remain unresolved.

Step385, 11 November2026: RESEARCH / REPRODUCTION / ADVANCE under the
unchanged pre-invocation EXPLORE review383, approved in step384. This is
a local quantitative specialization of an imported Hermite remainder,
not a claim of originality beyond the sources checked. The result was
unaudited at step385. The independent conceptual audit in step387 below
accepts (2)-(3) with unchanged hypotheses and constants. It is not an RH
candidate. C997v's balanced stop and C997r/t/u's scopes remain intact.

## Proof

### Imported remainder and exact finite construction

Import J.-P. Calvi, *Lectures on Multivariate Polynomial Interpolation*,
Hanoi, summer2005, Chapter1, Theorem1.9 p14 and Theorems1.17–1.18 p21,
equations(1.36)–(1.39),
[author PDF](https://www.math.univ-toulouse.fr/~calvi/res_fichiers/MPI.pdf).
Review381/step382 inspected the complete repeated-node proof cases;
review383/step384 checked arbitrary positive multiplicities and the
varying-function scope. For a holomorphic function on a simply connected
domain and a piecewise C1 contour of index one around the interpolation
nodes and evaluation point, this finite-degree identity is

    f_n(y)-p_n(y)=(1/(2pi i)) integral_C
        omega(y)f_n(zeta)/[omega(zeta)(zeta-y)] dzeta,
    omega(y)=(y-a)^m(y-b)^ell.                            (4)

No fixed-function convergence theorem or uniform rate is imported.
The new work is bounding this identity for the specified coupled
function, multiplicities and windows. Interpolation theory is not
reproved.

Here 1<=m<=n and ell>=1. Both nodes belong to D_n and are distinct:
0<theta/2<=1/3 for n>=3, and b^(-1)a=exp(-i theta/2).
For an explicit construction, let T_(v,r) denote the Taylor polynomial
at v through degree r. Then

    p_n(y)=(y-b)^ell T_(a,m-1)[f_n(y)/(y-b)^ell]
             +(y-a)^m T_(b,ell-1)[f_n(y)/(y-a)^m].          (5)

Each quotient is holomorphic near its stated center. Each summand
has degree at most m+ell-1=n. At a the first matches f_n through order
m-1 and the second vanishes to order m; at b the roles are reversed.
Thus (5) is precisely the imported interpolant. Its coefficients give
the original grid because exp(15it/8)y^j=exp(i gamma_j t) when
y=exp(it/(4n)). No additional band frequencies are introduced.

### One contour encloses both complete windows

It suffices to prove the bounds for n>=64. Choose R=9/32 and the
positively oriented circle

    C_n={b(1+R exp(i u)): 0<=u<=2pi}.

Its closed disk lies in D_n because Re(b^(-1)zeta)>=1-R=23/32>0.
The center b is inside. The other node satisfies

    |a-b|<=theta/2=(n+1)/(4n)<=65/256<R,
    |zeta-a|>=R-|a-b|>=7/256>1/64, zeta in C_n,
    |zeta-b|=R.                                         (6)

Use |exp(iu)-exp(iv)|<=|u-v| for real u,v. For y=exp(it/(4n)),
on the upper window U=[7n/4,9(n+2)/4] it gives

    |y-a|<=u_n=5/16+7/(8n),
    |y-b|<=v_n=1/16+5/(8n).

Indeed the angle relative to a runs from 3/16-1/(4n) to
5/16+7/(8n), and relative to b from -1/16-1/(2n) to
1/16+5/(8n). On the lower window L=[n,n+2], it gives

    |y-a|<=1/(4n),
    |y-b|<=w_n=1/4+1/(2n).

For n>=64 both v_n and w_n are <=33/128. Hence all these evaluation
points lie strictly inside C_n, and

    |zeta-y|>=R-33/128=3/128, zeta in C_n.                (7)

The relative spectral angle t/(4n)-theta has absolute value at most
33/128 on the two windows, so it is in (-pi/2,pi/2). Consequently
Log_n(exp(it/(4n)))=it/(4n), without a branch jump. Direct substitution
of alpha yields exp(15it/8)f_n(exp(it/(4n)))=exp(it-t/8).
Thus (4) is the desired spectral error, multiplied by a factor of
modulus one. This also proves the identity at either interpolation
node; the error there is zero. No division by omega(y) is used.

The domain is simply connected, f_n is holomorphic on it, and C_n is
smooth with index one around every node and evaluation point, avoiding
all of them. These verify all hypotheses of the cited formula.

### The varying function and every multiplicity factor

Write zeta=bx on C_n. Then |x|>=23/32 and
|arg x|<=|Im x|/Re x<=9/23. Since theta>=1/2, (1) gives

    |f_n(zeta)|
      =exp(n[-(7/2)log|x|-(arg x+theta)/2])
      <=exp(Bn),
    B=-1/4+(7/2)log(32/23)+9/46.

By (6), |omega(zeta)|>64^(-m)R^ell. The contour length is
2pi R, and (7) gives R/(3/128)=12. Therefore (4) implies uniformly
on both full closed windows

    |e_n(t)|<=12 exp(Bn)(64|y-a|)^m(|y-b|/R)^ell.          (8)

This includes the entire n-dependent contour maximum of f_n; it is
not a fixed-function estimate with an unspecified growing constant.

### Conversion to the complete kernel

The audited C997c(4)–(6) finite-measure bounds, applied to a unit point
mass at any c in I, are

    T_U=18 exp(27/16)(n+2)exp(9n/32),
    T_L=8 exp(3/4)(n+2)exp(-n/16).

They bound the absolute variations of the upper and lower densities
-2 exp(-cn/4)g_n(t)dt and 2 exp(-cn/4)g_n(t)dt on their respective
intervals. Their input |g_n(t)|<=2(n+2)exp(3t/8) includes K's -1;
the underlying real Laguerre inequality is
[NIST DLMF18.14.8](https://dlmf.nist.gov/18.14.E8), as already justified
in C997c. C997s's step373 kernel audit verifies the retained two beta
exponents and subtraction. These are reused inputs, not reproofs.

Finite summation gives the exact decomposition D_n=U_n+V_n, where

    U_n(c)=-2 exp(-cn/4) integral_(cn)^(c(n+2)) g_n(t)e_n(t)dt,
    V_n(c)= 2 exp(-cn/4) integral_n^(n+2) g_n(t)e_n(t)dt.

Apply (8) with the distances proved above. For every n>=64,

    ||U_n||_C(I) <= F_U(n),
    F_U(n)=216 exp(27/16)(n+2)exp((B+9/32)n)
                  *(20+56/n)^m *[(2/9)(1+10/n)]^ell,

    ||V_n||_C(I) <= F_L(n),
    F_L(n)=96 exp(3/4)(n+2)exp((B-1/16)n)
                  *(16/n)^m *[(8/9)(1+2/n)]^ell.          (9)

These are upper bounds on the actual complete residual contributions.
They use absolute variation, impose no sign on g_n, and do not remove
any of its zeros. The reflected beta term, lower window, subtraction
and endpoints remain in the displayed exact decomposition.

### Strict rates and absorption of all prefactors

For n>=64, log n>=log64=6log2>3: the elementary integral for log2
is strictly greater than 1/2. Consequently the minimum in m is inactive
and

    2n/log n <= m < 2n/log n+1,
    m/n ->0, m log n/n ->2, ell/n ->1.                   (10)

The inequality m<n follows already from 2n/log n+1<2n/3+1<=n.
Taking logarithms of the positive explicit bounds (9) and dividing
by n gives genuine limits

    log F_U(n)/n -> kappa_U=B+9/32+log(2/9),
    log F_L(n)/n -> kappa_L=B-1/16-2+log(8/9).            (11)

In the first limit (m/n)log(20+56/n)->0. In the second,
(m/n)log(16/n)->-2 by (10). In both, the fixed constants and n+2
give logarithms o(n), ell/n->1, and log(1+10/n), log(1+2/n)->0.
Thus (11) charges every multiplicity-dependent and polynomial factor.

The following elementary rational bounds certify strict slack without
a numerical approximation. The positive exponential series gives

    exp(1/3)>1+1/3+1/18+1/162=113/81>32/23,
    B< -1/4+7/6+9/46=307/276.

For x=7/11, integration of 1/(1-u^2)>1+u^2 on (0,x) gives

    log(9/2)=2 integral_0^x du/(1-u^2)
              >2x+2x^3/3=5768/3993>23/16.

It follows that

    kappa_U <307/276+9/32-23/16=-97/2208<-1/32,
    kappa_L <307/276-1/16-2=-1049/1104<-1/32.             (12)

Since both limits in (11) are strictly below -1/32, there is a single
N>=64 such that F_U(n)<=exp(-n/32) and F_L(n)<=exp(-n/32) for all
integers n>=N. This deduction uses the full positive bounds (9),
including their prefactors. It is not an endpoint root-rate assertion
at equality. The triangle inequality now proves (2), and hence the
requested weaker rate with a fixed constant and one onset.

### Exact-band-null action and qualifications

The kernel is continuous on compact I for each fixed n,z. For a finite
complex measure mu all pairings exist. If its band pairings vanish,
finite linearity gives

    integral_I k_n(c,z_star)dmu(c)=integral_I D_n(c)dmu(c).

The total-variation inequality and (2) prove (3), uniformly over all
such measures. No conjugation convention, minimax theorem or infinite
limit interchange is involved. With nonzero band pairings, the extra
sum A_(j,n) integral k_n(c,gamma_j)dmu remains unpaid; (2) alone does
not control it under C997s's cap. This is why the uncapped conclusion
does not settle that objective or any actual-Xi sign question.

### Independent conceptual audit — step387, 11 November 2026

RESEARCH / REPRODUCTION / ADVANCE under the unchanged EXPLORE
review385, separately approved in step386. This audit accepts (1)-(12)
and conclusions (2)-(3). ADVANCE means local verification of this
quantitative specialization, not a discovery beyond the checked sources
or a resolution of an actual-Xi condition. No mathematical script or
new external theorem is needed for the following checks.

**Finite construction and imported hypotheses.** For every n>=3,
1<=m<=n and ell=n+1-m>=1. The two nodes are distinct and lie in the
rotated right half-plane. In (5), the quotient at a is holomorphic in
a neighborhood avoiding b, and the quotient at b in one avoiding a;
they need not be holomorphic on all of D_n. Multiplication back by
the respective denominator leaves Taylor error of order m at a and
ell at b. The other summand vanishes to that order. Both terms have
degree <=m+ell-1=n, so uniqueness of the cited Hermite interpolant
identifies (5). The coefficients therefore depend on n, not c, and
their monomials give exactly gamma_j=15/8+j/(4n), including j=n.

Calvi's cited Theorems1.9/1.17/1.18 are reused with their inspected
repeated-node cases in review381 and unequal-multiplicity comparison
in review383. They are finite-degree identities for each f_n, not
convergence theorems for a fixed function. The circle's closed disk is
inside D_n since 1-R=23/32>0. This also makes its interior a region of
holomorphy. The contour avoids the nodes and has index one about them
and every evaluation point considered below. At y=a or b the remainder
is zero; (4) still holds directly, without division by omega(y).

**Both complete windows and the branch.** Recomputing the angle
intervals gives, relative to a and b respectively,

    U: [3/16-1/(4n), 5/16+7/(8n)],
       [-1/16-1/(2n), 1/16+5/(8n)];
    L: [-1/(4n), 1/(4n)],
       [-1/4-1/(2n), -1/4].

These prove all the distance bounds used in (6)-(7) by the chord
inequality, with both endpoints retained. For n>=64, w_n<=33/128
and v_n<=37/512<33/128. Also R-|a-b|>=7/256>1/64.
Thus the common evaluation-contour separation is >=3/128 and the
contour length divided by 2pi times this separation is exactly 12.
The relative angles lie in (-pi/2,pi/2), so the rotated logarithm is
it/(4n). Multiplying alpha by this logarithm gives -t/8-7it/8;
the factor exp(15it/8) yields exactly exp(it-t/8). There is no hidden
branch multiple and the factor carrying the interpolation error has
modulus one.

**Varying function and complete kernel costs.** On the contour,
Log_n(bx)=log|x|+i(arg x+theta). Taking the real part of alpha times
this expression gives exactly the modulus displayed before (8).
The bounds |x|>=23/32, |arg x|<=9/23 and theta>=1/2 give B with
its stated sign. The lower bounds for both factors of omega(zeta)
give 64^m R^(-ell), charging all multiplicities. There is no growing
constant outside (8) left unestimated.

For each c, the two densities are exactly C997c(4); apply its audited
variation bounds to mu=delta_c. The entire upper interval lies in U
and the lower interval is L. Their signs agree with the displayed
decomposition D_n=U_n+V_n. Inserting (8) multiplies the two variation
prefactors by 12, giving 216 exp(27/16)(n+2) and
96 exp(3/4)(n+2). The remaining factors are precisely

    64u_n=20+56/n, v_n/R=(2/9)(1+10/n),
    64/(4n)=16/n, w_n/R=(8/9)(1+2/n).

This verifies (9) for every n>=64. C997c and C997s's step373 kernel
audit retain cosh's two beta exponents, K's constant subtraction,
and every zero. Neither (4), (8), nor the variation estimate divides
by g_n or assumes a sign. All integrations and sums are finite.

**Ceilings, rates and one onset.** From log n>3, the ceiling bound
m<2n/log n+1<n makes the minimum inactive for n>=64. It implies
m/n->0, m log n/n->2 and ell/n->1. In the logarithm of F_L the
factor (16/n)^m contributes -2, not zero; in F_U its corresponding
factor contributes zero. The logarithms of the fixed prefactors and
n+2 divided by n vanish. The remaining ell factors have exactly the
limits stated in (11). These are limits of the full positive bounds,
not merely of their exponential pieces.

The rational strict inequalities in (12) check exactly:
113*23-81*32=7>0 and 5768*16-3993*23=449>0. Hence
B<307/276 and log(9/2)>23/16. Substitution gives the two displayed
upper rates -97/2208 and -1049/1104. The first is below -1/32 by
7/552; the second is below -1/32 by 2029/2208 (and log(8/9)<0
was safely omitted). For example, epsilon=7/1104 is smaller than
both margins. By the two genuine limits, for all sufficiently large
n each log F(n)/n is at most its limit plus epsilon and hence less
than -1/32. Taking the maximum of their two onsets and 64 gives
one integer N. The scalar functions F_U,F_L depend only on n, so N
is independent of c and every testing measure. The triangle inequality
proves (2) with exactly the stated constant 2.

**Exact-null consequence and scope.** For fixed n,z, the integrand
is continuous and the finite endpoints depend continuously on c;
therefore k_n(c,z) is continuous on compact I. All pairings against
a finite complex Borel measure exist. Exact vanishing of the n+1
band pairings cancels the finite sum with the original coefficients,
using the bilinear convention integral k dmu, without conjugation.
Then |integral D_n dmu|<=||D_n||_infinity ||mu||_TV proves (3).
The same N works for n-dependent measures and arbitrary finite norms.
This argument is not an exchange of a measure-dependent limit.

The result gives no estimate of sum_j|A_(j,n)|. For nonzero band
pairings the finite correction sum does not vanish, so its cost is
still unpaid. In particular C997s's exp(sqrt(n)) cap and capped E_n
are not controlled by this audit. C997r concerns a different Taylor
family and does not settle the Hermite coefficients' cost; C997v's
balanced-envelope failure is not an input here. The remaining transfer,
reconstruction, regulator, forcing and actual-Xi gaps listed above
remain open. Direct mathematical inputs remain C997c and C997s;
Calvi is an external cited input. No DAG change is needed.

## Mathlib

Full matching coverage for this varying-function, unequal-multiplicity,
complete-kernel estimate has not been checked. No Mathlib theorem is
assumed. The imported analytic input is precisely Calvi's cited finite
Hermite remainder; the audited kernel variation input is C997c, with
C997s supplying the complete-kernel convention. Availability of generic
holomorphic or polynomial support would not itself certify (9)–(12).
