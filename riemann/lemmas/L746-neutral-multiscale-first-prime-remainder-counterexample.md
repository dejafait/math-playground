# L746: An exact-neutral smooth counterexample to the first-prime half-remainder budget

## Hypotheses

Put a=log2, b=2log3, L=2b=4log3, and c=sqrt(2)log2.
For a real or complex f in C_c^infinity(0,L), extend by zero and set
h(y)=f(y+b). The exact global constraints are

    integral_0^L exp(x/2)f(x) dx = integral_0^L exp(-x/2)f(x) dx = 0.

Use L743 (1)'s actual first-prime coefficient:

    Q_2(f) = c Re integral_R h(y-a) conjugate(h(y)) dy.

The literal, whole-line Beckner resource is

    R(h) = (1/4) integral_(R x R)
      |sqrt(|y|)h(y)-sqrt(|z|)h(z)|^2 /
                         (|y-z|sqrt(|yz|)) dy dz.                 (1)

Null sets at the singular coordinates are interpreted by the
nonnegative Lebesgue integral. In the target notation R_B(f)=R(h).
No exterior pairs are removed.

The only specialized external theorem is William Beckner,
*Pitt's inequality and the fractional Laplacian: sharp error estimates*,
[arXiv:math/0701939v6](https://arxiv.org/pdf/math/0701939v6#page=5),
31 July 2009, Theorem 4, equation (12), printed p.5; Fourier convention
on printed p.2. Its hypotheses are Schwartz functions on R^n, including
n=1 and complex functions. It gives (1), with coefficient 1/4, as its
logarithmic-uncertainty remainder. The source was assessed before this
attempt. We import the identity, not its endpoint differentiation proof.
The other analytic imports are the standard Plancherel theorem,
Tonelli's theorem for nonnegative integrands, and change of variables.

L744 (6) motivates the prospective downstream complete-energy use;
no conclusion of L744, L742 or L745 is used to prove this counterexample.
There is no RH, spectral endpoint, positivity-complement or limiting
singular-function hypothesis.

## Conclusion

There is an explicitly defined finite integer N_* below and a real
f_(N_*) in the stated smooth class with both exact moments zero and

    Q_2(f_(N_*)) - R_B(f_(N_*))/2 > 1.                            (2)

More precisely the constructed family satisfies

    Q_2(f_N)-R_B(f_N)/2 >= kappa H_N-C_R/2,
    H_N=sum_(j=1)^N 1/j,   kappa>0,   C_R<infinity,               (3)

with every constant defined by fixed smooth bumps below. Thus the
proposed half allocation fails at the exact stated window, even on
real tests. This is an analytic finite-N certificate, not a numerical
preview or the use of a nonsmooth limiting vector.

This local comparison was POTENTIALLY_NEW under the prior EXPLORE
assessment; originality is not certified. The separate conceptual
audit in step301 below accepts (2)-(3), with only support-notation
and a non-load-bearing strict-inequality correction. The conclusion stops this
allocation; it gives no negative complete Weil energy, off-line zero,
RH disproof, or sign for the other terms.

## Proof

### 1. Source normalization and disjoint supports

Write F_h(xi)=integral h(y)exp(-i xi y)dy. Beckner's Fourier variable
uses exp(+2pi i y xi). Changing variable xi to -xi/(2pi) in the
source identity, and applying Plancherel to the constant, gives

    R(h) = integral log|y| |h(y)|^2 dy
         + integral log|xi| |F_h(xi)|^2 dxi/(2pi)
         - (psi(1/4)+log2)||h||_2^2.                             (4)

Indeed its constant is D=psi(1/4)-log pi; the Fourier change subtracts
log(2pi)||h||_2^2. This proves the displayed scalar without changing
the source theorem. All uses below are C_c^infinity, hence Schwartz.
The logarithmic integrals are finite: the transform is bounded near
zero and rapidly decreasing at infinity. Set B=|psi(1/4)+log2|.
For any such u, log|xi|<=xi^2 and Plancherel give

    integral log|xi| |F_u(xi)|^2 dxi/(2pi) <= ||u'||_2^2.        (5)

If u,v are real smooth functions with disjoint compact supports at
positive distance, expansion of (1) gives exactly

    R(u+v)=R(u)+R(v)-I(u,v),
    I(u,v)=integral integral u(y)v(z)/|y-z| dy dz.                (6)

The two equal cross integrals cancel the factor 1/2 from polarization;
the sqrt(|yz|) weights cancel against sqrt(|y|)sqrt(|z|).
The separated-support integral is absolutely convergent. Equivalently,
one can polarize the finite weighted L2 difference integrals first.
For nonnegative u,v, I>=0. For a finite family of disjoint nonnegative
packets, (6) therefore implies that the resource of their sum is at
most the sum of their resources. When subtracting a nonnegative v,
the sign reverses: R(u-tv)=R(u)+t^2R(v)+t I(u,v), for t>=0.

### 2. A uniformly paid smooth center profile

Fix delta=a/16. Let eta be the nonnegative C_c^infinity(R)
function proportional to exp(-1/(1-4t^2)) on (-1/2,1/2), normalized
to have integral one, and zero elsewhere. Its support is
[-1/2,1/2]. For each integer N>=1 set

    A_N=log(delta)-N-1,   B_0=log(2delta),
    v_N=1_[A_N,B_0] * eta,
    h_0,N(y)=|y|^(-1/2) v_N(log|y|)  (y!=0),
    h_0,N(0)=0.                                                (7)

This is a real nonnegative even smooth function. For each finite N
it vanishes in a neighborhood of zero and outside

    |y| < rho=2delta exp(1/2)<a/4.

The last strict inequality follows from exp(1/2)<2. In particular its
zero extension is smooth. Also 0<=v_N<=1 and ||v_N'||_1<=2, since
v_N'=eta(.-A_N)-eta(.-B_0). The plateau v_N=1 on
[A_N+1/2,B_0-1/2] contains, for every 1<=j<=N,

    [log(delta)-j, log(2delta)-j].                              (8)

For completeness, evaluate (1) on a general even function of this
form using y=+/-exp(t), z=+/-exp(u). On same-sign pairs the measure
and kernel become 1/(2|sinh((t-u)/2)|); on opposite-sign pairs they
become 1/(2cosh((t-u)/2)). Both half-lines and every exterior pair
are included. Thus

    R(h_0,N)=(1/4) integral integral
                    |v_N(t)-v_N(u)|^2 k(t-u) dt du,
    k(s)=csch(|s|/2)+sech(s/2)
        =4 sum_(m>=0) exp(-(2m+1/2)|s|),  s!=0.                 (9)

These are nonnegative changes of variables. Since |v_N(t)-v_N(t-s)|
is at most one, the fundamental theorem of calculus and Tonelli give

    integral |v_N(t)-v_N(t-s)|^2 dt
      <= integral |v_N(t)-v_N(t-s)| dt <= 2|s|.

Consequently, again by Tonelli,

    R(h_0,N) <= (1/2) integral |s|k(s) ds
       =4 sum_(m>=0)(2m+1/2)^(-2) <=20.                       (10)

For the last bound, the m=0 summand is 4 and the remaining decreasing
series is at most integral_0^infinity(2x+1/2)^(-2)dx=1. This bound
is uniform in N. It does not assert a uniform L2 bound for h_0,N.

### 3. Translated smooth packets and their entire resource

Fix, explicitly,

    phi(v)=exp(-1/((v-1)(2-v))) for 1<v<2, and 0 otherwise.

Put

    A=integral_1^2 phi(v)/sqrt(v) dv>0,
    M=integral_1^2 phi(v)dv>0,
    d=integral_1^2 phi(v)^2dv>0,
    d_1=integral_1^2 phi'(v)^2dv<infinity,
    C_phi=d_1+(B+log18)d>0.

For u_j=delta exp(-j), define

    p_j^+(y)=u_j^(-1/2)phi((y-a)/u_j),
    p_j^-(y)=p_j^+(-y),
    w_N=sum_(j=1)^N (p_j^++p_j^-)/j.                           (11)

All packets are smooth and nonnegative. Their positive supports are
[a+u_j,a+2u_j], and 2u_(j+1)<u_j since exp(1)>2. Thus the packet
supports are pairwise disjoint, and disjoint from h_0,N. They lie in

    a<|y|<=a+2delta/e<a+2delta=9a/8.

Fourier scaling in (4) gives, exactly,

    integral log|xi| |F_(p_j^+)(xi)|^2 dxi/(2pi)
      = -log(u_j)d + integral log|xi| |F_phi(xi)|^2 dxi/(2pi).

Its spatial logarithm is at most log(a+2delta)d. By (5) and the
definition of B, since (a+2delta)/delta=18,

    R(p_j^+)=R(p_j^-) <= j d+C_phi.                            (12)

This estimate includes all pairs in (1) via the imported exact identity;
it is not a restriction of that integral to the packet supports.
For lambda>0 set r_N=h_0,N+lambda w_N. Applying (6), (10), (12), and
sum_(j>=1)j^(-2)<=2 yields

    R(r_N) <=20+2lambda^2 d H_N+4lambda^2 C_phi.               (13)

### 4. Exact arithmetic correlation

Neither h_0,N nor w_N has a self-correlation at displacement a.
The center support has diameter <a/2; each of the positive or negative
outer clusters has diameter <a/8; the two outer clusters are more
than 2a apart. The only nonzero cross terms in
integral r_N(y-a)r_N(y)dy are the positive outer packet with the
positive center, and the negative outer packet with the negative
center. By (8), h_0,N(u_j v)=(u_j v)^(-1/2) for v in supp(phi).
For each packet their respective integrals are both A/j. Therefore

    integral r_N(y-a)r_N(y)dy =2lambda A H_N.                   (14)

This is an equality, not an absolute upper bound for a signed term.

### 5. A uniformly paid exact moment correction

Define the fixed even nonnegative smooth function

    beta(y)=phi(4|y|/a-5).

Its support lies in 3a/2<=|y|<=7a/4, inside (-b,b); indeed
7log2/4<2log3, equivalently 2^7<3^8. It vanishes near zero, so the
absolute value in its definition causes no smoothness issue. Write

    V=||beta||_1=a M/2,
    m_beta=integral cosh(y/2)beta(y)dy
          =(a/2)integral_1^2 cosh(a(v+5)/8)phi(v)dv>0,
    C_beta=8d_1/a+(B+|log(7a/4)|)a d/2.

Equation (4), (5), and direct scaling give R(beta)<=C_beta, because
||beta||_2^2=a d/2 and ||beta'||_2^2=8d_1/a.

Set

    t_N=(integral cosh(y/2)r_N(y)dy)/m_beta,
    h_N=r_N-t_N beta,    f_N(x)=h_N(x-b).                       (15)

The function h_N is real, even, smooth and compactly supported in
(-b,b), and its cosh moment is exactly zero. Its sinh moment is zero
by parity. Therefore

    integral_0^L exp(+-x/2) f_N(x)dx
      =exp(+-b/2) integral exp(+-y/2)h_N(y)dy=0                (16)

for both signs, exactly.

All raw supports lie in |y|<a/4 or a<|y|<9a/8. The beta supports
have distance at least Delta=3a/8 from them. They have no difference
equal to a with any raw support: on the same positive half-line the
outer-to-beta differences lie strictly between 3a/8 and 3a/4, and
center-to-beta differences exceed 5a/4; opposite-sign differences
are also separated from a. The negative half-line is symmetric.
There is no beta-to-beta difference a either. Thus the correction
has no self or cross contribution to this delay, and (14) gives

    Q_2(f_N)=2c lambda A H_N.                                  (17)

It remains to bound its resource cost without using the growing
L2 norm of the center. From (7) and (11),

    ||r_N||_1 <= U:=2sqrt(a)+2lambda M sqrt(delta)/(sqrt(e)-1).

Here ||h_0,N||_1<=integral_(|y|<a/4)|y|^(-1/2)dy=2sqrt(a),
and sum exp(-j/2)/j<=1/(sqrt(e)-1). Since |y|<9a/8 on raw supports,

    0<=t_N<=D:=cosh(9a/16)U/m_beta.

Use the subtraction case of (6), the support distance Delta, and
the L1 bounds. This retains the sign of every correction term:

    R(h_N)=R(r_N)+t_N^2R(beta)+t_N I(r_N,beta)
       <=2lambda^2 d H_N+C_R,
    C_R:=20+4lambda^2 C_phi+D^2 C_beta+D U V/Delta.              (18)

Every constant on the last line is finite and independent of N.
The disjoint-support integral is bounded by U V/Delta; no singular
center estimate or uncontrolled norm comparison is needed here.

### 6. A specified finite witness and the stopping threshold

Now fix lambda=c A/d>0, using this value in U,D,C_R, and set

    kappa=c^2 A^2/d>0,
    N_*=ceil(exp((C_R/2+1)/kappa)).                             (19)

Combining (17) and (18) proves (3). The integral comparison
H_N>=log(N+1)>log N gives

    kappa H_(N_*)-C_R/2>1,

and proves (2). Formula (19), with the explicit bumps and integrals
above, specifies a finite integer and an actual finite sum of smooth
functions. It requires no effective small value of N and takes no
limit inside a form, moment or Fourier transform. In particular the
nonsmooth formal limit |y|^(-1/2) is never used as an admissible test.

The trial-space eigenvalues saved in `scripts/beckner-budget/` are
nonrigorous exploratory previews and are not inputs to this proof.
Their modest scale ranges do not certify the inequality or exclude
the family (15). The new evidence is the analytic lower bound (3)
and its finite threshold (19), not a numerical optimization.

### 7. Independent conceptual audit — step301, 4 November 2026

The separately source-approved audit accepts the exact finite smooth
witness (2). The following checks reproduce this local argument; they
are not an additional discovery or an audit of Beckner's theorem's
endpoint proof. The source identity is imported with its stated
Schwartz hypotheses. No numerical preview is an input.

**Normalization and polarization.** Write the source transform as
Fhat_B(t)=F_h(-2pi t). Substitution xi=-2pi t gives its logarithmic
Fourier integral as

    integral log|xi| |F_h(xi)|^2 dxi/(2pi)
                         -log(2pi)||h||_2^2.

Combining this with D=psi(1/4)-log pi gives precisely (4).
All spatial and Fourier logarithmic integrals are absolutely finite
for the finite smooth tests used here. L743 (1) contributes
2 Lambda(2)/sqrt(2)=c, so the coefficient of the real delay
correlation in (17) is correct. No assertion about L743's supremum
or any RH-conditional result is used.

For separated real u,v, the cross part of the modulus square in
(1), including its prefactor, is

    -(1/2) integral integral
           [u(y)v(z)+u(z)v(y)]/|y-z| dy dz = -I(u,v).

Products u(y)v(y) vanish. This computation can first be made by
polarizing the finite difference-form integrals; it does not split
divergent diagonal terms. The displayed cross integral is absolutely
convergent by separation and finite L1 norms. In particular subtracting
t beta contributes +t I, exactly as in (18); it is not discarded.

**The two cutoff edges and every sign quadrant.** The actual eta has
support [-1/2,1/2]. Thus v_N'=eta(.-A_N)-eta(.-B_0) has L1 norm
at most two, independently of the interval's length. The plateau
contains every interval in (8): its lower edge is
log(delta)-N-1/2 and its upper edge is log(2delta)-1/2.
All j in 1,...,N lie strictly within these bounds. For each fixed N
the center vanishes for |y| below exp(A_N-1/2), so smoothness at
zero is literal, not a limiting claim.

On each of the two same-sign quadrants the change-of-variables
kernel is 1/(2|sinh((t-u)/2)|); on each of the two opposite-sign
quadrants it is 1/(2cosh((t-u)/2)). Summing all four gives (9).
The transformed integral still extends over all t,u in R, including
the two exterior regions of the cutoff. Since 0<=v_N<=1,

    integral |v_N(t)-v_N(t-s)|^2 dt
       <= |s| ||v_N'||_1 <= 2|s|.

For s!=0, the sum csch(|s|/2)+sech(s/2) equals
4 sum_(m>=0) exp(-(2m+1/2)|s|); the odd-indexed exponential terms
cancel before this nonnegative series is integrated. Tonelli yields
4 sum_(m>=0)(2m+1/2)^(-2). Its m=0 contribution is 16, and its
tail is at most 4 integral_0^infinity(2x+1/2)^(-2)dx=4.
This proves the bound 20, without any uniform center L2 bound.

**Packet scaling and the signed delay.** The transform of p_j^+ is
sqrt(u_j) exp(-ia xi) F_phi(u_j xi); reflection gives p_j^-.
Substituting u_j xi into its complete Fourier integral contributes
-log(u_j)d, not -2log(u_j)d. The spatial upper bound and
log|xi|<=xi^2 then give (12), with
(a+2delta)/delta=18. Finite disjoint nonnegative packets have
nonpositive resource cross terms by (6). Their diagonal upper bound
is 2lambda^2 d H_N+2lambda^2 C_phi sum_(j=1)^N j^(-2),
at most 2lambda^2 d H_N+4lambda^2 C_phi as in (13).

Every positive packet is at y=a+u_j v with 1<=v<=2; the plateau
therefore gives h_0,N(y-a)=u_j^(-1/2)v^(-1/2). Its correlation
integral is A. Reflection gives a second copy, from the negative
packet to the negative center. The center diameter is below a/2,
each outer cluster diameter below a/8, and opposite outer clusters
are more than 2a apart. Hence these are all the delay-a terms,
and (14) is exact. At support endpoints phi vanishes; replacing
open nonzero sets by closed supports changes no integral.

**The separated correction and exact moments.** Use the enclosing
sets H=(-a/4,a/4), P+=(a,9a/8), P-=-P+, and
B+=[3a/2,7a/4], B-=-B+. Positive beta-to-outer distances lie
strictly between 3a/8 and 3a/4; beta-to-center distances exceed
5a/4; beta-to-opposite-outer distances exceed 5a/2. Distances
within either beta interval are at most a/4, while between the
two beta intervals they are at least 3a. These cases and their
reflections exclude every correction pair at delay a. They also
prove the separation Delta=3a/8 needed by (18). All these sets
lie strictly inside (-b,b), since 2^7<3^8.

Direct scaling verifies V=a M/2, ||beta||_2^2=a d/2,
||beta'||_2^2=8d_1/a and the displayed positive m_beta. The upper
bound for the spatial logarithm is at most |log(7a/4)| on this
support, so R(beta)<=C_beta follows from (4)-(5). The raw L1
bound uses

    integral_(|y|<a/4)|y|^(-1/2)dy=2sqrt(a),
    sum_(j>=1) exp(-j/2)/j <= 1/(sqrt(e)-1).

Consequently t_N<=D uniformly. The entire signed cross correction
is bounded by D U V/Delta, and its self cost by D^2 C_beta. This
establishes (18) without substituting the growing center L2 norm.
Parity cancels the sinh moment, the definition of t_N cancels the
cosh moment, and translation by b contributes only the nonzero
factors exp(+-b/2). Thus both global moments in (16) vanish exactly.

**Finite threshold and qualifications.** The fixed bumps give A,d,
m_beta>0 and all other constants finite. After fixing lambda=c A/d,
none of C_R, U or D depends on N. Subtraction of half of (18) from
(17) gives coefficient 2c lambda A-lambda^2 d=kappa>0. For the
finite integer N_* in (19),

    H_(N_*) >= log(N_*+1) > log N_*
                                  >= (C_R/2+1)/kappa.

The required strict gap exceeds one. No limiting test, numerical
quadrature, infinite sum inside the form, or effective small N is
needed. This confirms the exact stated obstruction only; all other
prime powers and the complete energy's remaining terms are unpaid.

Three minor corrections preserve the original defined functions and
all constants: the original label "C_c^infinity(-1/2,1/2)" for eta
has been replaced by C_c^infinity(R) with its actual closed support;
packet and beta supports now include their endpoints; and the original
strict comparison "a+2delta<9a/8" is an equality. The required strict
outer enclosure follows instead from j>=1, as now displayed. None
of these corrections changes the separation, plateau, estimates or
witness. The only local mathematical input remains L743's coefficient;
L744 is downstream context, and L742/L745 are not premises.

## Mathlib

Full matching Mathlib coverage of this constrained multiscale
counterexample is not checked. No absence or novelty inference is
made from that. Beckner's exact identity is a precisely cited external
input; standard Plancherel, Tonelli, smooth convolution, finite-sum
polarization and change of variables support the specialization.
No Lean verification or matching Mathlib theorem is claimed.
