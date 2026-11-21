# Lemma 714: exact finite reduction of the signed positive-bump remainder

## Hypotheses

Retain L713's fixed actual L703 profile, including the same even
nonnegative Gevrey plateau and width selected before n. Use its
positive-frequency bump chi, supported in
[omega-delta,omega+delta], equal to one on
[omega-delta/2,omega+delta/2], with 0<delta<1/3000 as in L708.
The complete L666 family still has unit masses, its anchor, inverse
denominator angle, j=0 factor, both physical endpoints and all M=n/3
moments. No estimate of its other response terms is asserted here.

Use the exact constants and transform convention of L713:

    n=12q+3, q>=1, N=n-1, h=A/n, A=27/10,
    d=5/4, U=121/64, u=(3+4i)/10, c_0=1/8, c=3/20,
    lambda_j=d+u*j/n,                     0<=j<=N,
    W_n(u,y)=product_(j=0)^N
       (d+u*j/n)*(U*u+(d-i*y)*j/n)
       /[(U*u+d*j/n)*(d+u*j/n-i*y)].

The j=0 factor is d/(d-i*y). R_n(c), P_n and the inverse density
p_n are exactly L713's quantities, with no modulus inserted into
either integral defining R_n. All limits below use n=12q+3.

Define the nonzero complex constant, real coefficients and polynomial

    D_n=d*product_(k=1)^N (d+u*k/n)/(U*u+d*k/n),
    b_(n,j)=(-1)^j*n^N/[j!*(N-j)!]
                         *product_(k=1)^N (U-j*k/n^2),
    H_n(zeta)=sum_(j=0)^N b_(n,j)*zeta^j,
    B_n(a)=integral_0^infinity chi(v)*exp(-a*v/h)dv,
    v_+=sup{v>0: chi(v)>0}.

B_n is entire in a; its integral is over the unchanged compact bump.
The symbol D_n here is a scalar prefactor, not L666's squared-residue
diagonal D. The b_(n,j) are auxiliary partial-fraction coefficients,
not replacements for the original unit spatial masses.

## Conclusion

The following identities are exact for every permitted n:

    W_n(u,i*z)=D_n*sum_(j=0)^N b_(n,j)/(z+lambda_j),       (1)
    p_n(v)=D_n/h*sum_(j=0)^N b_(n,j)
                      *exp(-lambda_j*v/h)/(lambda_j+c_0),
                                                       v>=0, (2)
    R_n(3/20)=D_n/h*sum_(j=0)^N b_(n,j)/(lambda_j+c_0)
                              *[B_n(lambda_j)-B_n(-c_0)]
             =P_n+K_n,
    K_n=D_n/h*sum_(j=0)^N b_(n,j)*B_n(lambda_j)
                                               /(lambda_j+c_0).
                                                               (3)

The same formula for R_n holds for every fixed c>c_0. In particular,
changing that horizontal height does not change this signed observable.
No absolute value is taken before the finite sum or bump integral.

All N roots rho_(n,k) of H_n are real and strictly greater than one,
counted with multiplicity. Consequently

    H_n(zeta)/H_n(0)=product_(k=1)^N (1-zeta/rho_(n,k)),
    H_n(0)=n^N*U^N/N!,                                (4)

and the inverse density of W_n itself, on v>=0, is

    g_n(v)=D_n/h*exp(-d*v/h)*H_n(exp(-u*v/A)).          (5)

This density is nonzero for v>=0. This is NOT a nonvanishing
assertion for p_n, K_n or R_n, which involve further integration.

The actual residue has the full, profile-dependent rate

    lim log|P_n|/n
      = integral_0^1 log|Q_t(u,i*c_0)|dt+c_0*v_+/A.     (6)

In particular its upper bound <1/5000 is inherited from L713,
with that lemma's unaudited numerical/analytic qualifications.
The new identity (6) itself does not require its numerical certificate.

These results reduce the approved signed-rate question to (3); they
do not determine the exponential rate of R_n, its nonvanishing or
its comparison with P_n. No limiting root distribution in (4),
relative asymptotic for K_n, or absence of cancellation is proved.
The complete spatial Jensen defect, other frequency and finite-family
terms, angular persistence, amplitude/full charge, H/support and Xi
realization remain unresolved. The coefficient definition, (4), (9)
and Section 3 root argument passed the L715 input audit (step 179);
the finite inverse and signed identities (1)--(3), (5), (8) passed
the separate conceptual audit in Section 5 (step 185). The residue
rate (6) and L713's envelope estimates are outside that audit.
This is not an RH candidate.

## Proof

### 1. Reused source scope and the finite rational identity

The original step-175 derivation used the EXPLORE assessment
`drafts/literature/2026-11-03-signed-bump-remainder-rate.md`.
Its target permits a signed analysis in the rational variable with
the bump variable real. No analytic extension or endpoint law for
eta is used. The earlier absolute-contour obstruction in L713 and
the positive-blend obstruction concern different estimates.

The standard finite-complex-measure transform/inversion inputs are
those already inspected and stated in L708/L713: J. Kallsen and
P. Kruehner, *On uniqueness of solutions to martingale problems —
counterexamples and sufficient criteria*,
[arXiv:1607.02998v1](https://arxiv.org/pdf/1607.02998v1), Appendix A,
Lemma A.1(6),(9)--(11),(14), pp.29--30, and the Laplace convention in
[DLMF 1.14(iii), (1.14.17)--(1.14.19)](https://dlmf.nist.gov/1.14.iii).
The latter defines the transform and its domain; it does not state
the exponential pair previously attributed to (17)--(18). Section 2
evaluates the needed elementary integrals explicitly. Pointwise
inversion is imported from
[DLMF 1.14(i), (1.14.1), (1.14.3)](https://dlmf.nist.gov/1.14.i),
under its L1 and local bounded-variation hypotheses, and the finite
rectangle residue theorem from
[DLMF 1.10(iv), (1.10.8)](https://dlmf.nist.gov/1.10.iv).
These general theorems are not reproved. Their precise applicability
was source-assessed in
`drafts/literature/2026-11-03-signed-bump-inversion-audit.md` before
the step-185 audit. The elementary partial fractions, scaled integrals
and contour checks below verify this particular finite family;
they make no new general inversion or root-preservation claim.

Directly factor the product to obtain

    W_n(u,i*z)=D_n
       *product_(k=1)^N [U*u+(d+z)*k/n]
       /product_(j=0)^N (z+lambda_j).                  (7)

It is strictly proper, with distinct simple poles -lambda_j since
u!=0. At the j-th pole the numerator factor is
u*(U-j*k/n^2). The product of the other denominator factors is

    (u/n)^N*(-1)^j*j!*(N-j)!.

Thus the residue is exactly D_n*b_(n,j). Subtract the right side
of (1) from (7). The difference is a rational function without
finite poles and tending to zero at infinity; it is zero. None
of the residues vanishes because U-j*k/n^2>U-1>0. All factors
in D_n are nonzero, as their real parts are strictly positive.

### 2. Inversion, signs and the real bump integral

For v>=0 define g_n by (5), using the finite sum for H_n, and
set g_n(v)=0 for v<0. For fixed n put
C_g=|D_n|*sum_j |b_(n,j)|/h, which is finite. Then

    |g_n(v)|<=C_g*exp(-d*v/h),                          v>=0,
    ||g_n||_1<=C_g*h/d,
    integral_R |v*g_n(v)|dv<=C_g*h^2/d^2.

Since Re(lambda_j)>=d>0, direct evaluation at the two endpoints gives

    (1/h)*integral_0^infinity exp(-(lambda_j-i*y)*v/h)dv
                  =1/(lambda_j-i*y),                  y real.

Consequently the positive-exponent transform, with physical scale h, is

    integral_R exp(i*y*v/h)*g_n(v)dv
       =D_n*sum_j b_(n,j)/(lambda_j-i*y)=W_n(u,y),

by (1). This identification includes the j=0 factor d/(d-i*y).
To compare with L713's actual measure, let t=j/n, lambda_t=d+t*u and
r_t=t*(d+t*u)/(U*u+d*t). Direct algebra gives

    Q_t(u,y)=r_t+(1-r_t)*lambda_t/(lambda_t-i*y).

The scaled factor measure is therefore

    mu_t=r_t*delta_0+(1-r_t)*(lambda_t/h)
                          *exp(-lambda_t*v/h)*1_(v>=0)dv.

The denominators defining r_t have positive real part. Each mu_t
has finite variation, bounded by
|r_t|+|1-r_t|*|lambda_t|/Re(lambda_t), and finite first absolute
moment, bounded by |1-r_t|*h*|lambda_t|/Re(lambda_t)^2.
The imported complex-measure convolution bounds and |s+t|<=|s|+|t|
give the same finiteness for their finite convolution mu_n. Its
transform is W_n, by the imported multiplication theorem.
The t=0 measure has density (d/h)exp(-d*v/h)1_(v>=0), so mu_n
has a density and no atom at zero. Injectivity in Kallsen--Kruehner
Lemma A.1(14) identifies mu_n with g_n(v)dv: as y ranges over R,
y/h ranges over every real frequency. No positivity of mu_n or
g_n is assumed. The value chosen for g_n at zero does not affect
the measure.

For q(v)=exp(c_0*v/h)*1_(v<=0)/h, direct integration on the
negative half-line gives the transform 1/(c_0+i*y). Here
||q||_1=1/c_0 and integral |v*q(v)|dv=h/c_0^2.
Let p_n=g_n*q, the resolvent convolution used in L713. Absolute
Fubini follows from

    integral_R integral_R |g_n(s)*q(v-s)|ds dv
                       =||g_n||_1*||q||_1<infinity.

Its first absolute moment is at most
(integral |s*g_n(s)|ds)||q||_1+||g_n||_1 integral |t*q(t)|dt,
also finite. For each real v the convolution is absolutely
convergent by the displayed exponential bound. For v>=0 it gives

    p_n(v)=exp(c_0*v/h)/h
                         *integral_v^infinity exp(-c_0*s/h)*g_n(s)ds.

Substituting the finite exponential sum and integrating each term
gives (2), with the denominator lambda_j+c_0 and prefactor D_n/h.
For v<0 the lower integration endpoint is instead zero, giving
p_n(v)=W_n(u,i*c_0)*exp(c_0*v/h)/h. Both one-sided values at
zero equal W_n(u,i*c_0)/h, using (1) at z=c_0.
These finite exponential formulas are smooth on each open half-line
with bounded one-sided derivatives at zero. Their continuous gluing
is locally absolutely continuous, hence locally of bounded variation.
For example, off zero its derivative is

    p_n'(v)=(c_0/h)*p_n(v)-g_n(v)/h,      v>0,
    p_n'(v)=(c_0/h)*p_n(v),               v<0.

The finite one-sided derivatives and matching value verify the local
claim also across zero; no delta mass is introduced there.

The convolution theorem identifies its transform as
k_n(y)=W_n(u,y)/(c_0+i*y). This rational function has no real poles
and is O(|y|^-2): (7) has numerator degree N and denominator degree
N+1, and the resolvent adds one denominator degree. Thus k_n is L1.
To apply the cited symmetric DLMF convention, set f(x)=h*p_n(h*x).
Then f is L1 and locally of bounded variation, its normalized
Fourier transform is k_n(y)/sqrt(2*pi), and the mean of its one-sided
limits equals f(x) at every x. DLMF (1.14.3) therefore gives

    p_n(v)=(2*pi*h)^(-1)*integral_R k_n(y)*exp(-i*y*v/h)dy.

The integral is absolutely convergent. This proves pointwise identity
with L713's continuous inverse, including zero, rather than relying
on equality of densities only almost everywhere.

Verify also the particular signed contour identity used from L713.
The poles of W_n are

    y=j*Im(u)/n-i*(d+j*Re(u)/n),             0<=j<=N,

all strictly below the real axis. In the strip 0<=Im(y)<=c, with
any fixed c>c_0, the only pole of k_n is y=i*c_0. It is simple
and W_n(u,i*c_0) is nonzero by the positive real parts of the
product factors there. On y=+/-T+i*s, 0<=s<=c, the rational part
is O_(n,c)(T^-2), uniformly in s as T tends to infinity. For v in
any fixed compact real set |v|<=V the exponential factor has
modulus at most exp(c*V/h). The sum of the absolute vertical
integrals is therefore O_(n,c,V)(T^-2) and tends to zero uniformly
on that compact set. Both horizontal integrals converge absolutely
by the same degree bound and the absence of poles on their lines.

Take the positively oriented rectangle with bottom traversed from
-T to T and top from T+i*c to -T+i*c. The residue of
k_n(y)exp(-i*y*v/h) at i*c_0 is
-i*W_n(u,i*c_0)exp(c_0*v/h). The bottom integral minus the
left-to-right top integral therefore tends to
2*pi*W_n(u,i*c_0)exp(c_0*v/h). Division by 2*pi*h yields

    p_n^c(v)=p_n(v)-W_n(u,i*c_0)*exp(c_0*v/h)/h.

Equivalently, for v>=0,

    p_n^c(v)=-exp(c_0*v/h)/h
                            *integral_0^v exp(-c_0*s/h)*g_n(s)ds. (8)

The minus sign and the interval [0,v] are essential, and (8) also
holds at zero. All exchanges with the actual real bump are absolute:
integral chi(v)|p_n(v)|dv<=||chi||_infinity*||p_n||_1, and for the
shifted contour the double absolute integral is bounded by

    (2*pi*h)^(-1)*[integral_0^infinity chi(v)*exp(c*v/h)dv]
                  *integral_R |k_n(X+i*c)|dX < infinity.

The first factor is finite by compact support and the second by the
horizontal-line bound. Each finite exponential term in (2) is also
integrable against chi. Thus absolute Fubini and finite summation
are legitimate for every fixed n,c; no bound uniform in n is being
claimed. Finally (1) at z=c_0 gives

    W_n(u,i*c_0)=D_n*sum_j b_(n,j)/(lambda_j+c_0).

Integrating the formula for p_n^c against chi and using (2) and the
definitions of P_n and B_n gives exactly (3), with R_n=P_n+K_n.
The contour height disappears through an exact identity, not an
asymptotic. The bump has not been extended to nonreal arguments or
replaced at either support endpoint.

### 3. The real-root calculation and its limitation

Let E=zeta*d/dzeta. Coefficientwise calculation gives

    H_n(zeta)=n^N/N!
              *{product_(k=1)^N (U-(k/n^2)*E)}(1-zeta)^N. (9)

Here the factors commute, but apply them successively for the root
argument. Suppose a real degree-N polynomial f has distinct positive
roots r_1<...<r_s, with multiplicities m_1,...,m_s, and take alpha>0
with U/alpha>N. For x away from those roots, the new-root equation
for (U-alpha*E)f is

    x*f'(x)/f(x)=sum_(i=1)^s m_i*x/(x-r_i)=U/alpha.     (10)

The left side has derivative
-sum_i m_i*r_i/(x-r_i)^2<0 on every complementary interval.
On (r_i,r_(i+1)) it decreases from +infinity to -infinity, and
on (r_s,infinity) it decreases from +infinity to N. Thus (10)
has exactly one root in each of these s intervals. At r_i the
new polynomial has multiplicity exactly m_i-1: after removing
(x-r_i)^(m_i-1), its value is -alpha*r_i*m_i times the nonzero
remaining factor. Its degree is still N because U-alpha*N!=0.
The inherited N-s roots and the s roots just found account for
its full degree, so there are no other roots.

In (9), alpha=k/n^2 and alpha*N<=N^2/n^2<1<U. Start from
(1-zeta)^N. After each operation all roots remain >=1, every new
root is >1, and the multiplicity at 1 decreases by exactly one
until it disappears at the N-th operation. This proves (4),
including strictness. Since |exp(-u*v/A)|<=1 for v>=0, with
strict inequality for v>0, (4) proves nonvanishing in (5).

The conclusion is deliberately limited to g_n. For complex u the
numbers g_n(v) have no established common phase. The convolution
in (2), incomplete convolution in (8), and final integration against
chi can cancel. In particular positivity of the roots in (4) is
not positivity of any of these complex integrals. Taking absolute
values termwise in (3) would lose precisely the cancellation whose
rate is the approved target.

### 4. Exact residue rate and the unresolved comparison

At y=i*c_0, the numerator and denominator affine factors in Q_t
have strictly positive real parts for 0<=t<=1. Thus
log|Q_t(u,i*c_0)| is continuously differentiable there with a
bounded derivative. Its left Riemann sum gives

    log|W_n(u,i*c_0)|
           =n*integral_0^1 log|Q_t(u,i*c_0)|dt+O(1).     (11)

For the bump integral B_n(-c_0)>0, compact support gives an upper
bound C*exp(n*c_0*v_+/A), with C independent of n. For each
epsilon>0, the definition of v_+ and continuity/nonnegativity of
chi give an interval of positive length contained in
(v_+-epsilon,v_+] on which chi is bounded below by a positive
constant. Consequently

    lim log B_n(-c_0)/n=c_0*v_+/A.                     (12)

No regularity or positivity at the endpoint itself is needed.
The prefactor 1/h costs only O(log n); (11)--(12) prove (6).

Equation (3) leaves two explicit unpaid cancellations: among its
alternating finite coefficients and within the complex transforms
B_n(lambda_j). Neither the compact Gevrey hypothesis nor (4)
by itself supplies a lower bound for their combined sum. The
separately proved residue rate therefore does not imply a rate
for R_n. In particular no full limit, nonvanishing or exceptional-
subsequence exclusion is asserted, and log(0)=-infinity remains
the convention for any future signed comparison.

### 5. Conceptual audit of the finite inverse — 3 November 2026

Step 185 accepts (1)--(3), (5) and (8) under the unchanged
hypotheses. Section 2 now supplies the explicit variation/first-moment
bounds, scaled finite-measure identification, local bounded variation
and continuous value at zero, normalized pointwise inversion, signed
finite rectangle and compact-bump Fubini bounds. The elementary
exponential pair has been evaluated rather than misattributed to
DLMF's transform definition. No numerical test or asymptotic theorem
is needed for these identities.

This is a verification and completion of an existing specialization,
not a new signed-rate result. The original unit spatial masses,
anchor, inverse angle, j=0 factor, physical endpoints -2q and 2q-1,
and all M=n/3 moments are unchanged. Only L713's continuous inverse,
P_n and R_n(c) are identified here; its complete-family equation (4)
and the sizes of the retained endpoint/comb/tail/moment terms have
not been audited or estimated by this step. Section 4's residue rate
and L713's absolute-envelope estimates also remain outside this audit.
Nonvanishing of p_n, K_n or R_n does not follow from the accepted
finite identities. No additional mathematical input edge is required.

## Mathlib

Full matching coverage is not checked. No formalization is claimed
for (1)--(12), the growing polynomial, the actual fixed bump or its
signed rate. Polynomial factorization, finite rational partial
fractions, elementary exponential integration and Riemann sums are
supporting tools, not a matching theorem for R_n. No root-distribution
or signed-asymptotic theorem is imported without a source assessment.
