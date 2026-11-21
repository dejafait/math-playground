# C744k: Polynomial-log action enclosure for the neutral Schur test

## Hypotheses

Use C744j's exact complex neutral graph, ell=log(3)/2, d=log(2),
a=d/sqrt(2), orthonormal p_n, z_n=p_n-r_n p_(n mod2), and forms
F_s=D+V-Q/2+s 2K_1+s 2a J_d, for s=-1,+1. Inner products are
linear in their first argument. Fix N=256 and let

    Z c=sum_(n=2)^256 c_n z_n,       A_s c=(D+V-Q/2+s 2K_1+s 2a J_d)Zc.

These are maps from C^255 to L2(0,ell). In particular the unbounded
multiplier V is applied only to polynomials; its actions are in L2.
All matrices below are matrices of the corresponding quadratic forms
in these coordinates. Q_N is the orthogonal complement of p_0,...,p_N.
No RH, extra support collar, shifted energy or H2 restriction is assumed.

The known general inputs remain C744j's cited regional Legendre spectrum
and complete-covariance Schur method. The additional elementary tool is
the Cauchy coefficient estimate from the Cauchy integral formula. The
calculation below specializes these known tools to enclose the action;
it does not claim a new general approximation or Schur theorem. Its
source scope is the unchanged step483 EXPLORE assessment.

## Conclusion

There are degree 96 polynomials q_hat and h_hat with exact rational
coefficients for which replacing q_0 by q_hat and
k_1(t)-1/(2t) by h_hat defines an action A_hat_s satisfying, for both signs,

    ||A_s-A_hat_s|| <= epsilon < 5.22*10^(-24).              (1)

This is a bound for the entire 255-column map in Euclidean coordinate
norm, not a per-column bound with an omitted dimension factor. The
singular Carleman action, endpoint-log multiplier and full reflection
are retained exactly. Each A_hat_s column is a polynomial plus three
polynomial multiples of log(v), log(1-v), log(1+v), separately on
the two intervals split at v=d/ell-1, where v=x/ell.

Define the exact finite matrices

    M_hat_s=Z^* A_hat_s,
    R_hat_s^0=A_hat_s^* Q_N A_hat_s,
    S_hat_s=M_hat_s-(250/171)R_hat_s^0.                    (2)

With M_s and the exact moment-corrected covariance R_s of C744j(8),

    M_s-(250/171)R_s >= S_hat_s-10^(-19) I.                (3)

Thus kernel truncation and the infinite moment-graph correction can
be paid below 10^(-19) in this Schur test. This does NOT bound the
error of evaluating (2) by floating-point quadrature. The exact finite
scalar products and matrix signs have not been enclosed here.

For example, certified S_hat_s>=I/25 for both signs would imply
F_s(h)>||h||_2^2/30 on every nonzero exact neutral smooth h, using
C744j with complementary floor18/25 and rho=19/20. That finite
inequality is an unresolved sufficient test, not an established premise.
No positive full margin, strict-half interaction bound or RH conclusion
is claimed. This local approximation result remains independently unaudited.

## Proof

### 1. Rational Taylor coefficients and uniform kernel errors

Write S(t)=sinh(t)/t with S(0)=1. The removable analytic functions are

    q_0(t)=[exp(t/2)/S(t)-1]/t,
    h_0(t)=k_1(t)-1/(2t)=[exp(-3t/2)/S(t)-1]/(2t).

These equal C744j's real kernels for t>0. On |t|<=2,

    |S(t)-1| <= sum_(j>=1) 4^j/(2j+1)! < 5/6.             (4)

Consequently S has no zeros there and |1/S|<6. On |t|=2,
exp(1)<3 and exp(3)<21 give |q_0(t)|<19/2<10 and
|h_0(t)|<127/4<32. The singularities at zero are removable since
the numerators vanish there. These bounds apply on a neighborhood
of the closed disk, so the Cauchy coefficient estimate applies on
its radius 2 circle.

For c=1/2 or -3/2, the Taylor coefficients of exp(ct)/S(t) are

    u_0(c)=1,
    u_n(c)=c^n/n! - sum_(j=1)^floor(n/2) u_(n-2j)(c)/(2j+1)!.

This follows by multiplying the two convergent series. Set

    q_hat(t)=sum_(j=0)^96 u_(j+1)(1/2)t^j,
    h_hat(t)=(1/2)sum_(j=0)^96 u_(j+1)(-3/2)t^j.

All coefficients are rational. In particular the first three are
(1/2,-1/24,-1/16) and (-3/4,23/48,-5/32), respectively.
The Cauchy bounds followed by a geometric tail sum give, using
ell<11/20 from C744j,

    sup_(0<=t<=ell) |q_0(t)-q_hat(t)| <= delta_q,
    delta_q=(400/29)(11/40)^97,
    sup_(0<=t<=2ell) |h_0(t)-h_hat(t)| <= delta_h,
    delta_h=(640/9)(11/20)^97.                            (5)

For completeness, (4) is enclosed by summing through j=12 and
bounding its remaining positive series by the first omitted term
4^13/27! divided by 1-4/(28*29). For exp(x), the degree m prefix
plus [x^(m+1)/(m+1)!]/[1-x/(m+2)] is an upper bound when
0<=x<m+2. Use (x,m)=(1,20),(3,32). All these comparisons are
performed with exact fractions in the certificate below; no sampled
complex boundary values or floating-point Taylor residuals are used.

### 2. Entire-map L2 enclosure and elementary size bounds

Define Q_hat and H_hat by kernels q_hat(|x-y|) and h_hat(x+y).
Let C be the Carleman operator with kernel 1/(x+y) on (0,ell).
Then K_1=C/2+H, where H has kernel h_0(x+y). Put

    A_hat_s=[D+V-Q_hat/2+s C+s 2H_hat+s 2a J_d]Z.

A kernel bounded pointwise by delta on this square has operator
norm at most its Hilbert-Schmidt norm ell*delta. It follows that

    ||A_s-A_hat_s|| <= ell(delta_q/2+2delta_h)||Z||.        (6)

We bound ||Z|| without rounding or truncating the moment graph.
The b_n bounds and square-ratio estimate in C744j(7), with t=ell/4<1/7
and exp(t^2/6)<2, give

    eta^2 <= sum_(n>=2) b_n^2 <= 2b_2^2 < 8/245 < 1/25.

The elementary exponential bound here follows also from
exp(t^2/6)<=sum_(j>=0)(1/294)^j<2. Orthogonality of high
coordinates to p_0,p_1 gives ||Z||^2<=1+eta^2<26/25<(51/50)^2.
Thus a permitted exact value for epsilon in (1) is

    epsilon=(51/50)(11/20)(delta_q/2+2delta_h).            (7)

We also need a generous rigorous size bound for A_s. Under the unitary
change g(v)=sqrt(ell)f(ell v), its potential is

    V(ell v)=c_0-(1/2)log(v(1-v)), c_0=-gamma-log(2pi ell).

Here |c_0|<3: 0<=gamma<1 by the harmonic-number integral comparison;
ell>1/2 follows from exp(1)<3; Archimedes' 3<pi<22/7 and ell<11/20
give 1<2pi ell<4<exp(2), the last since exp(1)>2.

For a degree 256 polynomial g on (0,1), the orthonormal Legendre
expansion and |P_n(u)|<=1 on [-1,1] give

    ||g||_infinity <= sqrt(sum_(n=0)^256 (2n+1))||g||_2
                   =257||g||_2.

One justification of the classical bound used here is Laplace's
representation P_n(u)=pi^(-1)int_0^pi
(u+i sqrt(1-u^2)cos(theta))^n dtheta for real |u|<=1.
The integrand has modulus at most 1. The representation follows by
summing its geometric generating series for small complex z: the
integral is (1-2uz+z^2)^(-1/2), the Legendre generating function.
The elementary integral of 1/(a+b cos(theta)) is obtained by the
substitution tan(theta/2); analytic continuation near z=0 justifies
the complex coefficients. Thus the bound applies also to complex
linear combinations through Cauchy-Schwarz.

Since ||log v||_2=||log(1-v)||_2=sqrt(2), this proves

    ||Vf||_2 <= (3+257sqrt(2))||f||_2.

The diagonal operator has norm H_256<7 on this polynomial space,
using H_256<=1+log256 and log2<7/10. C744j's bounded-operator estimate
gives ||-Q/2+s 2K_1+s 2aJ_d||<=ell/4+pi+2a<5, since
ell/4<11/80, pi<22/7 and 2a=sqrt(2)log2<(3/2)(7/10).
Consequently, using sqrt(2)<3/2,

    ||A_s|| < (51/50)(7+3+257*3/2+5)=40851/100 < 500.     (8)

No bounded-multiplier assertion about V on the whole space is used.
This bound is solely on the fixed polynomial head.

### 3. Exact polynomial-log action, including the reflection jump

Here is an explicit finite evaluation scheme for A_hat_s; no numerical
recurrence for Legendre Q-functions is needed. On the unit interval
write g(v)=sum_k c_k v^k. Define, for integers j,k>=0,

    Phi_(j,k)(v)=sum_(m=0)^k binom(k,m)v^(k-m)
        [(-1)^m v^(j+m+1)+(1-v)^(j+m+1)]/(j+m+1),
    Psi_(j,k)(v)=sum_(m=0)^j binom(j,m)v^(j-m)/(m+k+1).

Splitting the first integral at w=v, substituting w=v-u or v+u,
and expanding finite binomials proves

    int_0^1 |v-w|^j w^k dw=Phi_(j,k)(v),
    int_0^1 (v+w)^j w^k dw=Psi_(j,k)(v).

Likewise polynomial division, including the k=0 case with empty sum,
gives the exact Carleman action

    int_0^1 w^k/(v+w)dw
       =sum_(r=0)^(k-1) (-v)^r/(k-r)
                         +(-v)^k[log(1+v)-log v].        (9)

Multiplication of the quotient by v+w verifies the division, and
the remaining integral is the displayed logarithm. Let q_j and h_j
be the coefficients in Section1. The unitary action on g is exactly

    Dg+c_0 g-(g/2)[log v+log(1-v)]
       -(ell/2)sum_(j,k) q_j ell^j c_k Phi_(j,k)(v)
       +s int_0^1 g(w)/(v+w)dw
       +s 2ell sum_(j,k) h_j ell^j c_k Psi_(j,k)(v)
       +s 2a 1_(d/ell-1,1)(v) g(d/ell-v).                (10)

Dg is computed in its finite Legendre expansion, with the exact
harmonic diagonal. Both sums have 0<=j<=96 and the original finite
range of k. Formula (9) makes (10) a polynomial on each side of the
reflection jump, plus the three log terms with coefficients

    log v: -g(v)/2-s g(-v),
    log(1-v): -g(v)/2,
    log(1+v): s g(-v).

The polynomial degree is at most353 for this head. Every product
needed for (2) is integrable: polynomial coefficients are finite on
the closed interval and endpoint logarithms have integrable squares.
The interval split keeps the entire partial reflection and its jump.
All moments r_n, ell, d, a, gamma and pi in these exact formulas still
need certified arithmetic when numerically evaluating the finite
integrals. Exact formulas do not themselves pay cancellation or rounding
error. In particular the large coefficients g(-v) cannot be evaluated
at ordinary precision and silently treated as exact.

### 4. Paying the full covariance perturbation

Let W map (t_0,t_1) to sum_e t_e v_(e,N) in C744j. Its norm is
epsilon_N. Let D_s=P_(0,1)A_s be the two low action coordinates.
The exact coupling map is F_s^couple=Q_N A_s-W D_s; its Gram matrix
is R_s. This notation distinguishes the coupling map from the form F_s.
C744j's elementary tail bound gives

    epsilon_256^2 < 72*515/7^512 < 10^(-200).

Thus, with tau=10^(-100) and d_F=epsilon+500tau, (7)-(8) give

    ||F_s^couple-Q_N A_hat_s|| <= d_F,
    ||Q_N A_hat_s|| < 501,       d_F<1.

For bounded maps U and V, expansion of U^*U-V^*V gives operator
norm at most (2||V||+||U-V||)||U-V||. Therefore

    ||R_s-R_hat_s^0|| <= 1003 d_F,
    ||M_s-M_hat_s|| <= ||Z||epsilon < 2epsilon.           (11)

Both M matrices are Hermitian: each approximated kernel has its
original symmetry, and D,V,J_d are unchanged. The moment correction
has been bounded as an operator; it was not omitted or inferred zero
from floating-point underflow. Equations (11) prove (3) with the more
precise perturbation

    epsilon_S=2epsilon+(250/171)*1003*(epsilon+500*10^(-100))
             < 10^(-19).                                (12)

Here (250/171) is exactly 1/(rho*18/25) for rho=19/20. C744j's
complementary lower bound exceeds 18/25 for both signs. If the exact
finite matrices in (2) were enclosed at least I/25, (3) would give
delta>1/25-10^(-19)>9/250. The reserve (1-rho)*(18/25) is 9/250.
C744j's square completion and eta^2<1/25 would then give

    mu > (9/250)/(26/25)=9/260>1/30.

This is only a conditional threshold for the still-unpaid finite test.
It makes no positivity inference from an approximate matrix or from
the degree 256 locator in step484.

### 5. Certificate scope and remaining work

Run `python3 scripts/adjacent-neutral/action-enclosure-485.py`.
The exact Fraction certificate is saved at
`scripts/adjacent-neutral/action-enclosure-485.json`, with all 97
coefficients of each kernel, both 98-coefficient quotient residuals,
all rational operands and all 19 checks. All 19 checks pass. The
upward-rounded display bounds are epsilon<=5.21328181664e-24 and
epsilon_S<=7.65504887662e-21, below the required 10^-22 and10^-19.
Only exact rational comparisons, not these displays, decide the checks.

This pays analytic kernel replacement, a finite-head operator size
bound and the tail moment correction. The script does not construct
or enclose the 255-dimensional matrices in (2). Their polynomial-log
scalar products, exact finite constants, covariance subtraction and
lower spectral bounds remain unresolved. Finite positivity alone
would still be insufficient without C744j's paid complement and
coupling; the explicit conditional test above retains both.
Remote, non-neutral, odd and all-window propagation gaps are unchanged.

## Mathlib

Full matching coverage of this exact-neutral action enclosure has not
been checked; availability is unknown. Cauchy estimates, polynomial
integration, Hilbert-Schmidt bounds and finite Gram perturbations are
supporting standard mathematics, not a formal certificate of the
unresolved Schur signs. No absence or novelty claim is made.
