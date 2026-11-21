# Lemma 707: spatial growth transfer and a sufficient cancellation budget

## Hypotheses

Fix one actual L703 profile before n varies and retain L666's full
family, with n=12q+3, q>=1, M=n/3, x=-5/4, R=11/8, U=121/64,
A=27/10 and Y=9/20. Thus the distinct spatial nodes are

    p_a=a/R, a in Z_n={x} union
        {x+i*A*(m+1/2+e_m)/n: -2q<=m<2q},
    W_a(u)=(x/a)*product_(j=1)^(n-1)
        [(x-(j/n)*u)/(a-(j/n)*u)]
        *[(U*u-(j/n)*a)/(U*u-(j/n)*x)],
    c_k(u)=R^(-1)*sum_a W_a(u)*p_a^k,
    G_n(u,z)=sum_(k=0)^(M-1)c_k(u)*z^k.

The anchor has W_x=1. All original masses are one. The inverse angular
variable, j=0 factor x/a, both finite endpoints and every moment remain
in these exact expressions. Use rational continuation on |u|=1/2.
L706 gives finite continuous coefficients, nonzero spatial slices and
finite-n absolute logarithmic integrability on this product torus.
The profile is not replaced by a finitely supported or n-dependent one.

For spatial radius r>0 and normalized circle means, put

    S_(n,r)(u)=max_(|z|<=r)|G_n(u,z)|,
    Delta_n(u)=log S_(n,1)(u)-mean_(|z|=1)log|G_n(u,z)|,
    J_sp(n)=mean_(|u|=1/2) Delta_n(u),
    s=65/64, b_n(u)=log(S_(n,s)(u)/S_(n,1)(u)),
    B_sp(n)=mean_(|u|=1/2)b_n(u),
    rho=sqrt(2824/3025), v=s*rho, alpha=-log rho,
    A_n(u)=R^(-1)*sum_a |W_a(u)|,
    C_n(u)=log^+(A_n(u)/S_(n,1)(u)),
    Cbar_n=mean_(|u|=1/2) C_n(u),
    log^+(t)=max(0,log t), t>0.

A_n is only an auxiliary absolute-weight envelope; it does not replace
the original diagonal D or the signed polynomial G_n. All logarithms
are natural. No relative remainder or sublinear cancellation budget
is assumed.

## Conclusion

For every allowed n, the degree-independent transfer is

    0<=J_sp(n)<=[3*log 2/log s]*B_sp(n).                    (1)

There is no additive error. Constant slices, actual degree drops and
zeros on any spatial comparison circle are included. In particular
B_sp=o(n) would imply J_sp=o(n), but neither assertion is proved here.

The exact geometric remainder G_n=F_n-T_n, with

    F_n(u,z)=R^(-1)*sum_a W_a(u)/(1-p_a*z),
    T_n(u,z)=R^(-1)*sum_a W_a(u)*(p_a*z)^M/(1-p_a*z),

obeys

    v^2=59657/61952<1,
    max_(|z|<=s)|T_n(u,z)|<=A_n(u)*v^M/(1-v),
    tau_s:=-log(v)/3=(1/6)*log(61952/59657)>0.             (2)

This is an absolute bound. A sufficient budget for the growth target is

    b_n(u)<=min{(M-1)*log s, (log s/alpha)*C_n(u)+C_s},
    B_sp(n)<=(log s/alpha)*Cbar_n+C_s,
    C_s=log s+log[(s-1)^(-1)+(1-v)^(-1)].                 (3)

Consequently Cbar_n=o(n) would suffice. This stronger statement is
unproved and is not asserted necessary for B_sp=o(n).

The tested full-moment interpolation bound is explicitly insufficient
to normalize (2). With N=M-1, delta_n=81/(110n), and

    Lambda_n=[2*(1+rho)/delta_n]^N/N!,

it gives only

    A_n(u)/S_(n,1)(u)<=Lambda_n,
    max_(|z|<=s)|T_n(u,z)|/S_(n,1)(u)
                                  <=E_n:=Lambda_n*v^M/(1-v), (4)
    log Lambda_n/n -> lambda_*
        :=[1+log((220/27)*(1+rho))]/3>1/3,
    log E_n/n -> lambda_*-tau_s>97/300>0.                 (5)

The computed upper certificate E_n grows exponentially whereas a
vanishing relative error would require a bound tending to zero.
This does NOT lower-bound the actual remainder, Cbar_n or B_sp. The
bound B_sp/n<=log(s)/3+o(1) in (3) still permits positive linear
growth; the required threshold is zero. The attempt therefore leaves
the approved fixed-profile asymptotic inconclusive.

Equation (1) is a reproduction of standard analytic tools at the
specified radii. Equations (2)--(5) are elementary bounds for testing
this route, not a new signed-coercivity theorem. No originality beyond
the checked sources, full-circle sublinear estimate or RH progress is
claimed. There has been no separate critical audit of this lemma.
Angular amplitude, complete charge, H/support, Xi realization and
actual-Xi all-degree signs remain independent unresolved claims.

## Proof

### 1. Approved scope and precise standard imports

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-03-spatial-doubling-growth-attempt-scope.md`,
separately approved in step 159. Its parent comparison records the
primary theorem statements, essential proof cases, duplicates and
failed approaches. Those readings are reused; no new source search
or changed-source claim is made.

Import Hadamard's three-circles theorem in K. Ramachandra,
*On the Mean-Value and Omega-Theorems for the Riemann Zeta-Function*,
TIFR Lectures 85 (1995),
[Theorem 1.5.2 and proof, printed p.27, PDF p.37](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr85.pdf#page=37).
For f analytic on a neighborhood of the closed comparison annulus,
0<r_1<r_2<r_3 and M_i=max_(|z|=r_i)|f(z)|, it gives

    M_2^[log(r_3/r_1)]<=M_1^[log(r_3/r_2)]
                                      *M_3^[log(r_2/r_1)].

No zero-free hypothesis is required. Polynomials satisfy the stated
analyticity assumption, and the maximum-modulus principle identifies
their circle and disk maxima.

Import the boundary-zero Poisson--Jensen inequality from R. B. Ash and
W. P. Novinger, *Complex Variables* (2004),
[Theorem 4.8.3 and Lemma 4.8.4, printed pp.33--36](https://people.math.sc.edu/girardi/m7034/book/AshComplexVariablesWithHyperlinks.pdf#page=94),
with the unit-mass Poisson kernel from Corollary 4.7.4, printed p.27,
PDF p.88. For a nonzero function analytic near the closed unit disk,
its logarithm at a nonzero interior value is at most the Poisson
integral of its boundary logarithm. The inspected boundary factors
include zeros on the circle and their multiplicities. Below a rotation
reduces the evaluation point to the real radius 1/2. These named
theorems are imported, not reproved.

L683's absolute remainder and L686's sparse clearing estimate do not
provide the relative norm needed here. L702's endpoint-extension stop
forbids discarding the signed interior in an unsupported global
expansion. L706 supplies a paid arc, not the complementary estimate.
These are comparisons; no further claims from them are proof inputs.

### 2. Transfer, including the zero and constant cases

Fix u and write P(z)=G_n(u,z), with actual degree d_P. It is nonzero
by L706, so all its positive-radius maxima are positive. Its boundary
logarithm is integrable, including boundary zeros. Write L_r=log S_(n,r)
and m=mean_(|z|=1)log|P|. Three-circles at 1/2,1,s gives

    (log s+log 2)*L_1<=log s*L_(1/2)+log 2*L_s,
    L_1-L_(1/2)<=(log 2/log s)*(L_s-L_1).                 (6)

For a nonconstant P choose a maximizing point z_0 on |z|=1/2.
Its value has modulus S_(n,1/2)>0. Rotate P so that z_0 is the
positive real point 1/2; all maxima and circle logarithmic means
are unchanged. The unit-disk Poisson kernel there is

    K(theta)=(1-1/4)/|exp(i*theta)-1/2|^2>=1/3,
    mean K=1.

The imported boundary inequality, and log|P|<=L_1, therefore imply

    L_(1/2)<=mean K*log|P|
       <=m/3+(2/3)*L_1,
    L_1-m<=3*(L_1-L_(1/2)).                              (7)

The subtraction of the constant 1/3 is legitimate because K-1/3>=0
and the logarithm is integrable. Interior zeros at other points and
boundary zeros do not affect this argument. If P is a nonzero
constant, both sides of (6)--(7) vanish directly. Combining them
proves Delta_n(u)<=3*log 2*b_n(u)/log s in every case. No division by
b_n(u) is used, including when b_n(u)=0.

For fixed n, every S_(n,r) is positive and continuous on the compact
angular circle, by L706's coefficient continuity and nonzero slices.
Thus b_n is bounded. The logarithmic integrability already supplied
by L706 permits integration of (7) and proves (1).

### 3. Enlarged spatial radius and exact finite remainder

Every actual node has |a|^2<d^2+Y^2=353/200, with d=5/4, and the
anchor satisfies the same non-strict bound. Hence |p_a|<=rho<1.
Direct rational arithmetic gives

    (65/64)^2*(2824/3025)=59657/61952<1.

Thus all denominators 1-p_a*z are nonzero on |z|<=s and bounded
below in modulus by 1-v. The finite geometric identity with exactly
M terms proves G_n=F_n-T_n, without any infinite-sum interchange.
Bounding only this explicit error by absolute values proves (2).
Both signed sums remain in the exact F_n and T_n identities. In
particular an absolute decay rate tau_s does not by itself give a
relative estimate for G_n.

### 4. A coefficient cutoff with an explicit cancellation payment

For each 0<=k<M, integration of the finite polynomial on |z|=1 gives

    c_k=mean_theta P(exp(i*theta))*exp(-i*k*theta),
    |c_k|<=S_(n,1),             |c_k|<=A_n*rho^k.          (8)

Set C=C_n(u) and K=ceil(C/alpha), so exp(C)*rho^K<=1. If K<M,
use the first bound in (8) for k<K and the second for k>=K.
If K>=M, use only the first bound. In either case, extending only
nonnegative bounding sums gives

    S_(n,s)/S_(n,1)
       <=s^K*[(s-1)^(-1)+(1-v)^(-1)].                    (9)

For K=0 the initial sum is empty and the same estimate holds;
A_n/S_(n,1)<=exp(C) also covers ratios smaller than one.
Since K<=C/alpha+1, the second pointwise bound in (3) follows.
This cutoff is an estimate on the unchanged full polynomial; no
moments have been deleted from the family.

For the other bound let d_P be the actual degree and consider the
polynomial w^d_P*P(1/w). Its maximum on |w|<=1 is at most S_(n,1).
Evaluation on |w|=1/s and the maximum-modulus principle for P show

    S_(n,s)<=s^d_P*S_(n,1)<=s^(M-1)*S_(n,1).

This includes constants and degree drops. Integrating the second
bound in (3) proves its averaged version. The bound is useful only
if the actual signed family pays Cbar_n; no such payment is inferred
from the positivity of A_n.

### 5. Test the full-moment interpolation payment

Order the M distinct nodes p_0,...,p_N by imaginary part, N=M-1.
Two consecutive nonanchor ordinates are separated by at least
3A/(4n). The nearest nonanchor ordinate on each side of the anchor
has distance at least 3A/(8n). After division by R, every consecutive
node gap is at least

    delta_n=3A/(8Rn)=81/(110n).

All nodes have the same real part. Consequently
|p_i-p_j|>=delta_n*|i-j|, including pairs straddling the anchor.
For the degree-N Lagrange polynomial

    ell_i(z)=product_(j!=i)(z-p_j)/(p_i-p_j)
            =sum_(k=0)^N ell_(i,k)*z^k,

the exact full moment equations imply

    W_(a_i)/R=sum_(k=0)^N ell_(i,k)*c_k.

There is no inversion of a possibly vanishing coefficient: all M
equations are used and the distinct nodes make these interpolation
polynomials well-defined. The sum of coefficient moduli of a product
is at most the product of the corresponding sums. Therefore

    sum_k |ell_(i,k)|
       <=(1+rho)^N/[delta_n^N*i!*(N-i)!],
    A_n<=S_(n,1)*(1+rho)^N*delta_n^(-N)
                              *sum_(i=0)^N 1/[i!*(N-i)!]
        =S_(n,1)*Lambda_n.                              (10)

Here the last sum is 2^N/N!. Zeros of individual weights or a drop
in the actual spatial degree are permitted. Combining (10) with
(2) gives (4) for precisely the original family.

For completeness the factorial rate requires no unproved asymptotic
interchange: monotonicity of log t gives

    integral_1^N log t dt<=log(N!)
                         <=integral_1^N log t dt+log N.

Thus log(N!)=N*log N-N+O(log N). Since N/n->1/3 and
2*(1+rho)/delta_n=(220/81)*(1+rho)*n, substitution proves the
limit lambda_* in (5). Its logarithm has argument greater than one,
so lambda_*>1/3. Also log(1+t)<t for t>0 gives

    0<tau_s<(1/6)*(2295/59657)<1/100.

The last rational inequality is 229500<357942. Hence the limiting
rate of E_n is lambda_*-tau_s>1/3-1/100=97/300. This proves the
failure of this numerical upper certificate to tend to zero.
It proves no lower bound for the quantity it majorizes. In particular,
neither Cbar_n=o(n) nor its negation follows from (10).

This completes one bounded attempt: the standard transfer is valid,
the enlarged-radius error is explicit, and the tested interpolation
fallback fails to pay it. The full B_sp asymptotic remains open. The
sufficient averaged cancellation budget in (3) is a possible refined
target requiring its own source/obstruction comparison before research.

## Mathlib

Full matching Mathlib coverage for (1), the fixed-family B_sp limit,
or the averaged cancellation-budget test has not been checked. The
parent assessment's Mahler-measure support is not a matching theorem
for these assertions. No absence or formal verification is claimed.
The cited three-circles and boundary-Poisson theorems are informal
standard inputs; the family estimates above remain unaudited.
