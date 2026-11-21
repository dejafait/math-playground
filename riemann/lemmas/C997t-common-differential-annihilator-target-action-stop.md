# Corollary 997t: common constant-coefficient differential densities lose the target action

## Hypotheses

Use the complete kernel of audited C997c(1),(4)-(6) and C997s(2):

    k_n(c,z)=-2 exp(-cn/4) [integral_(cn)^(c(n+2)) g_n(t)exp(izt)dt
                             -integral_n^(n+2) g_n(t)exp(izt)dt],
    g_n(t)=K_(n+2)(t)exp(-t/2)cosh(3t/8),
    K_(n+2)(t)=(L_(n+1)^(2)(t)-1)/(n+1).

Here n>=2 is an integer, I=[7/4,9/4], E=[15/8,17/8],
z_star=1+i/8, and gamma_j=15/8+j/(4n), 0<=j<=n.
All polynomial zeros, both beta terms, both windows, the constant
subtraction and closed endpoints are retained.

Let A_n be a nonzero polynomial with complex constant coefficients such
that, with D=ordinary differentiation in c,

    A_n(D) k_n(c,gamma_j)=0 on (7/4,9/4), for every j.       (1)

Let phi_n be complex-valued and in C_c^infinity((7/4,9/4)). Suppose
v_n=A_n(-D)phi_n is not identically zero, and normalize by the ACTUAL norm:

    w_n=v_n/||v_n||_L1(I).

The conclusion also supplies an explicit family meeting these hypotheses.
No Haar property, nonvanishing of g_n, zero simplicity, actual-Xi input,
or estimate on the original minimax optimum is assumed.

## Conclusion

Every complete band action vanishes exactly and ||w_n||_1=1. Set

    M_n=4(n+1)(n+2),
    F_n=4(2^(n+3)+1)(2^(n+2)-1)/(n+1)
                     * exp(65n/4)*2^(-M_n).

Uniformly over ALL A_n and phi_n satisfying the hypotheses,

    |integral_I w_n(c) k_n(c,z_star)dc|
        <= F_n + 8 exp(1/2)(n+2)exp(-3n/16).               (2)

For every integer n>=12 this implies

    exp(n/64)|integral_I w_n(c) k_n(c,z_star)dc|
        <= exp(-n^2)+8 exp(1/2)(n+2)exp(-11n/64) -> 0.     (3)

If X+n/4 divides A_n(X), the second term in (2)-(3) is exactly absent.
In particular the explicit full endpoint annihilator and Boman cutoff
family below have scaled target action at most exp(-n^2) for n>=12.

Thus this entire common CONSTANT-COEFFICIENT differential-annihilator
mechanism cannot yield a target action whose exp(n/64) multiple is
unbounded on any unbounded integer subsequence. This is an UPPER bound
on its actual normalized action, not an upper bound on a denominator
being mistaken for a failure test. The original coefficient cap
exp(sqrt(n)) charges zero because all band actions are exactly zero.

This does NOT bound C997s's optimal E_n from above or below at the
required asymptotic rate. It does not exclude arbitrary densities
satisfying only the n+1 band-pairing equations, general measures,
variable-coefficient operators, approximate annihilation with paid
leakage, or a different construction. None of the actual-Xi, signed
forcing, selected-response, reconstruction or regulator gaps is closed.

Step376, 11 November2026: RESEARCH / POTENTIALLY_NEW / NEGATIVE under
the unchanged EXPLORE review374, separately approved at step375.
The source search did not identify this complete-kernel normalized
bound; POTENTIALLY_NEW is not a claim of certified originality. This
new proof awaits independent conceptual audit. It is a scoped route
obstruction, not an RH candidate or a verified resolution of E_n.

## Proof

### Imported inputs and the complete endpoint representation

For constant-coefficient ODEs we import the repeated-root
exponential-polynomial basis in J. M. Aldaz, O. Kounchev and H. Render,
*Bernstein operators for exponential polynomials*,
[arXiv:0805.1618v1](https://arxiv.org/pdf/0805.1618v1), pp1-3,
section1(1),(3) and section2's repeated-root paragraph. For distinct
complex roots lambda of multiplicity m_lambda the functions
c^r exp(lambda*c), 0<=r<m_lambda, form a solution basis and in
particular are linearly independent. No positivity, conjugacy, real-root
or Haar assertion from that paper is imported. The elementary
multiplicity specialization to our exact columns is given below.

The compact-support bilinear adjoint is the distributional derivative
identity in R. Melrose, *Chapter3: Distributions*, MIT18.155 Fall2016,
[author notes](https://math.mit.edu/~rbm/18.155-F16/Chapter3.pdf),
printed pp44,53, (1.4),(2.13)-(2.15). We use ordinary D, not the
author's 1/i derivative convention, and do not conjugate coefficients.
All boundary traces vanish because phi_n is compactly supported in
the open interval. The cutoff input is cited and specialized below.
These primary contracts were inspected in review373 and are reused.
The maximum modulus principle and Cauchy integral formula are standard
named complex-analysis inputs; their entire-function hypotheses are
checked explicitly below. No asymptotic ODE or Laguerre theorem is used.

Write d=n+1 and a_b(z)=b+iz for b=-1/8,-7/8. The EXACT polynomial
coefficients, including the subtraction from the constant term, are

    K_(n+2)(t)=sum_(s=0)^d p_s t^s,
    p_s=(-1)^s binomial(n+3,d-s)/(d s!)-1_{s=0}/d.          (4)

For all band and target z used here Im(a_b(z)) is positive. Thus
a_b(z)!=0. Define the degree-d polynomial Q_(b,z)(t)=sum q_r t^r by

    q_r=sum_(s=r)^d (-1)^(s-r) s! p_s /
                                    (r! a_b(z)^(s-r+1)). (5)

This is the unrolled recursion in C997s(2). Direct substitution gives
Q'+a_b(z)Q=K_(n+2); its leading coefficient is p_d/a_b(z)!=0.
Consequently the finite primitive exp(a_b(z)t)Q_(b,z)(t) gives

    lambda_(b,alpha)(z)=-n/4+alpha*a_b(z), alpha=n,n+2,
    ell_n(z)=sum_b [exp(a_b(z)(n+2))Q_(b,z)(n+2)
                              -exp(a_b(z)n)Q_(b,z)(n)],
    k_n(c,z)=-sum_b [exp(lambda_(b,n+2)(z)c)Q_(b,z)((n+2)c)
                         -exp(lambda_(b,n)(z)c)Q_(b,z)(nc)]
                           +exp(-nc/4)ell_n(z).           (6)

Expanding 2cosh(3t/8) gives precisely the two b values and the factor
-1 in (6). The lower window is the final term, not an omitted error.
This verifies the needed specialization of C997s(2) for every n and
every endpoint, rather than relying on a finite numerical evaluation.

### The mandatory roots and the full annihilator

Let lambda_(b,alpha,j)=lambda_(b,alpha)(gamma_j). The four real parts,
in strictly decreasing order for n>=2, are

    -3n/8, -3n/8-1/4, -9n/8, -9n/8-7/4.                 (7)

The middle inequality follows from 3n/4>1/4. Within each real-part
family, the n+1 imaginary parts alpha*gamma_j are distinct. They are
positive, so none equals the separate real exponent -n/4. There are
therefore exactly 4(n+1) distinct upper endpoint exponents. Every
associated polynomial in (6) has degree d with nonzero leading
coefficient, including at the closed grid endpoints j=0,n.

For a polynomial A, A(D)(exp(lambda*c)Q(c)) equals
exp(lambda*c)A(lambda+D)Q(c). If A has a root of multiplicity h<=d at
lambda, the leading surviving derivative of Q is of order h, with
nonzero coefficient A^(h)(lambda)/h!, and has degree d-h. All higher
derivatives have smaller degree; thus this expression is nonzero.
Here h=0 also covers A(lambda)!=0. Linear independence of the distinct
exponential-polynomial families in (6), as in the cited basis theorem,
then shows that (1) requires multiplicity at least d+1=n+2 at EVERY
upper exponent. No lower-window nonvanishing is needed for this claim.
Hence the monic polynomial

    G_n(X)=product_(b in {-1/8,-7/8}, alpha in {n,n+2}, 0<=j<=n)
                               (X-lambda_(b,alpha,j))^(n+2)             (8)

has degree M_n and divides every A_n satisfying (1). All expressions
are entire in c, so an identity on the specified open interval suffices;
equivalently apply the standard identity theorem before the basis result.

The full explicit choice

    P_n(X)=(X+n/4)G_n(X), m_n=M_n+1                         (9)

annihilates every complete band column. Each endpoint polynomial is
annihilated by its factor of order d+1, and X+n/4 annihilates the
lower-window term even when its coefficient happens to vanish.
No claim that the final factor is mandatory is needed.

### A supported cutoff, all coefficients and an actual nonzero norm

The existence and finite-order derivative contract are the construction
of J. Boman, *On the propagation of analyticity of solutions of
differential equations with constant coefficients*, Ark. Mat.5(1964),
271-279, [primary paper](https://archive.ymsc.tsinghua.edu.cn/pacm_download/116/7017-11512_2007_Article_BF02591127.pdf),
Lemma1, pp272-273, (2.1),(2.2') and its finite convolution proof.
Only this inspected finite-order construction is used. Its fixed
support margins and derivative scaling are specialized as follows,
so no unspecified cutoff constant is treated as a paid target rate.

Fix the standard nonnegative unit-mass smooth bump

    eta(x)=c_eta exp(-1/(1-x^2)) for |x|<1, and 0 otherwise,
    eta_h(x)=eta(x/h)/h,
    Psi=1_[2-3/32,2+3/32] * eta_(1/64),
    phi_n=Psi * (eta_(1/(128m_n)))^(*m_n),                 (10)

where * denotes convolution on the real line and c_eta normalizes the
finite positive integral. This is Boman's fixed Psi with m_n rescaled
unit-mass factors. It has 0<=phi_n<=1, integral 3/16, and support in
[2-15/128,2+15/128], strictly inside (15/8,17/8) and hence I.
The radius of the smoothing kernels together is 1/64+1/128=3/128;
the indicator half-width is 3/32=12/128. Thus phi_n=1 on
[2-9/128,2+9/128], in particular on [2-1/16,2+1/16].

In the cited proof allocate at most one derivative to each of the
m_n small convolution factors. Their first-derivative L1 norms are
128m_n||eta'||_1. With the FIXED finite constant
C=max{1,128||eta'||_1}, Boman's bound specializes to

    ||phi_n^(r)||_infinity <= (C m_n)^r, 0<=r<=m_n.        (11)

No estimate beyond order m_n is asserted or needed. The support has
length 15/64<1/4, so the L1 bound for each derivative is at most one
quarter of the displayed right side.

Since n+2<=2n, every root in (8) satisfies

    |lambda|^2 <= (2n)^2+(17n/4)^2
                =353n^2/16 <25n^2.                      (12)

The extra root -n/4 obeys the same bound. If P_n(X)=sum_(r=0)^m u_r X^r,
m=m_n, its elementary symmetric coefficients therefore satisfy
|u_r|<=binomial(m,r)(5n)^(m-r). The binomial theorem and (11) pay ALL
coefficients in the finite norm estimate

    ||P_n(-D)phi_n||_1 <= (C m+5n)^m/4.                   (13)

For nonzero normalization we use an actual lower bound, not (13).
All positive-order derivatives integrate to zero. Every upper root
has modulus at least its imaginary part, which is >=15n/8. Therefore

    |integral_I P_n(-D)phi_n|
       =|P_n(0)| integral_I phi_n
       >= (n/32)(15n/8)^(m-1)>0.                        (14)

We used the weaker mass lower bound 1/8; the exact mass is 3/16.
The same quantity is a lower bound on the actual L1 norm. Equations
(10)-(14) specify one legitimate order-dependent family, including
support, coefficients and a nonzero actual denominator. We normalize
by the actual norm, not by either bound. Crucially, the failure estimate
below is uniform in phi and A and does not infer failure from (13).

### Exact cancellation and the normalized transform bound

For the general hypotheses, finite integration by parts gives

    integral_I w_n(c)k_n(c,gamma_j)dc
       = integral_I phi_n(c) A_n(D)k_n(c,gamma_j)dc/||v_n||_1=0.         (15)

The pairing is bilinear: the coefficients of A_n are unchanged.
Define the entire Laplace transforms

    W(zeta)=integral_I w_n(c)exp(zeta*c)dc,
    V(zeta)=exp(-2zeta)W(zeta)
           =integral_I w_n(c)exp(zeta*(c-2))dc.

Compact support and L1 integrability justify every derivative locally
uniformly in zeta. The same integration by parts gives

    W(zeta)=A_n(zeta) integral_I phi_n(c)exp(zeta*c)dc/||v_n||_1.        (16)

Since exp(-2zeta) is nonzero, (8) and (16) show that V/G_n is entire,
with removable singularities at all listed roots, retaining their full
multiplicities. Also, because |c-2|<=1/4 and ||w_n||_1=1,

    |V(zeta)|<=exp(|zeta|/4).                            (17)

On |zeta|=25n each factor in G_n has modulus >=20n by (12).
The maximum modulus principle applied to the ENTIRE quotient gives

    |V(zeta)/G_n(zeta)| <= exp(25n/4)/(20n)^M_n
                                        for |zeta|<=25n.

On |zeta|<=5n each factor in G_n has modulus <=10n. Multiplication
therefore yields

    |V(zeta)|<=exp(25n/4)2^(-M_n),
    |W(zeta)|<=exp(65n/4)2^(-M_n), for |zeta|<=5n.        (18)

No positivity or absence of zeros of the kernel or the density is used.
This is where the quadratic count of forced zeros controls the ACTUAL
normalized transform. Additional roots or coefficients of A_n can only
preserve these inequalities; no order bound on A_n is assumed.

### The complete target action, including the surviving lower window

At z_star the two a_b values are -1/4+i and -1+i. Thus |a_b|>=1 and
every target endpoint exponent lambda_star=lambda_(b,alpha)(z_star)
satisfies

    |lambda_star|^2 <= (9n/4)^2+(2n)^2
                      =145n^2/16 <16n^2.                (19)

The radius-n circle centered at any lambda_star lies inside |zeta|<=5n.
Cauchy's integral formula and (18) give, for all nonnegative integers r,

    |W^(r)(lambda_star)|
       <= r! n^(-r) exp(65n/4)2^(-M_n).                 (20)

Formula(4) gives sum_(s=0)^d s!|p_s| <= (2^(n+3)+1)/(n+1): bound
the binomial partial sum by its complete sum and retain the subtracted
constant by the triangle inequality. Consequently (5), using |a_b|>=1,
gives for every target primitive coefficient

    r!|q_r| <= C_n, C_n=(2^(n+3)+1)/(n+1), 0<=r<=d.      (21)

Pair one endpoint term in (6) with w_n. Since
W^(r)(lambda)=integral_I c^r exp(lambda*c)w_n(c)dc, equations(20)-(21)
give the bound

    |sum_(r=0)^d q_r alpha^r W^(r)(lambda_star)|
       <= C_n exp(65n/4)2^(-M_n) sum_(r=0)^d (alpha/n)^r
       <= C_n exp(65n/4)2^(-M_n)(2^(n+2)-1).             (22)

The four endpoint terms together are at most F_n. This calculation
uses the full primitives, including K's -1, with no asymptotic
replacement of the Laguerre polynomial and no division by g_n.

If A_n has the extra root -n/4, (16) makes the last term of (6)
pair to zero. Without that assumption it is still explicitly paid.
C997c's audited proof gives |g_n(t)|<=2(n+2)exp(3t/8), t>=0.
Since |exp(iz_star*t)|=exp(-t/8),

    |ell_n(z_star)|
       =|2 integral_n^(n+2) g_n(t)exp(iz_star*t)dt|
       <=8(n+2)exp(n/4+1/2).

The actual norm bound gives |W(-n/4)|<=exp(-7n/16). Their product
is <=8 exp(1/2)(n+2)exp(-3n/16), proving (2) in full.

### Comparison with the required threshold and scope of the stop

The explicit finite factors in F_n obey

    F_n <= 2^(2n+8)/(n+1) * exp(65n/4)*2^(-M_n).

Using M_n=4n^2+12n+8 and log(2)>=1/2 (integrate 1/t on [1,2]),

    log(exp(n/64)F_n)
       <=(-4n^2-10n)log(2)+(1041/64)n-log(n+1)
       <=-2n^2+(721/64)n <=-n^2, n>=12.                 (23)

The second term of (2), multiplied by exp(n/64), is exactly bounded
by the second term of (3), which tends to zero. This proves (3) along
the full integer sequence and hence along every unbounded subsequence.
For the explicit P_n family the lower window is zero, so (23) alone
suffices. Exact band annihilation removes, rather than suppresses or
rescales, the exp(sqrt(n)) leakage deduction in the weak certificate.

For any coefficient vector of original complex l1 norm at most
exp(sqrt(n)), (15) and ||w_n||_1=1 give
|integral w_n k_n(c,z_star)dc| <= ||complete residual||_C(I).
This is the smooth-density specialization of C997s's weak certificate.
Our result bounds this PARTICULAR CLASS of certificates from above.
It does not bound the optimum over all measures. The ODE identity(1)
forces M_n transform zeros; the original n+1 pairing constraints alone
do not assert those multiplicities. Thus it would be invalid to extend
this stop to all compactly supported band-orthogonal densities or to
the fixed-budget point bridge itself. No progress on actual-Xi signs
is inferred from eliminating this witness mechanism.

### Step378: independent conceptual audit of (1)-(23)

11 November 2026. RESEARCH / REPRODUCTION / ADVANCE, proof_audit /
conceptual_audit, under unchanged pre-invocation EXPLORE review376,
separately approved at step377. The conclusion (2)-(3) is accepted
without changing any hypothesis, constant or threshold. ADVANCE means
completion of local verification of the existing obstruction; this
audit proves no stronger statement and claims no discovery beyond
the sources checked. Step376's original audit-pending record is retained.

**Complete primitive and mandatory multiplicities.** In (4), p_d is
(-1)^d/(d*d!), hence nonzero; subtracting 1/d affects only p_0.
In (5), a_b q_r+(r+1)q_(r+1)=p_r, with q_(d+1)=0, by cancellation
of the finite sums. Thus every coefficient, including r=0 and r=d,
is checked. The four primitives in (6) have leading coefficient
alpha^d p_d/a_b, which is nonzero for alpha=n,n+2. The imaginary
part of a_b is gamma_j>0 on the band and 1 at the target, so no
primitive denominator vanishes. Expanding the cosh accounts for
the factor -1 and both b values; the separate lower-window term is
exactly 2 exp(-nc/4) times its original integral.

For n>=2, the separation between the middle real parts in (7) is
3n/4-1/4>0. Within any one family, the imaginary increment is
alpha/(4n)>0. These observations verify all pairwise distinctions
across the grid, including j=0,n. No upper exponent equals -n/4.
For one column, apply A(D) to (6). Distinct exponential-polynomial
terms remain independent by the cited ODE basis; one cannot cancel
an upper term with a different upper exponent or the lower term.
If the multiplicity h of A at a listed exponent is <=d, then
A(lambda+D)Q has leading term (A^(h)(lambda)/h!)Q^(h), of degree
d-h and nonzero leading coefficient. Higher derivatives cannot
cancel it. Consequently the root multiplicity is at least d+1
in every column, and their distinct union forces (8), of degree
4(n+1)(n+2). The argument covers h=0 and does not presume any
nonzero lower-window coefficient. Entire dependence on c makes
the open-interval identities sufficient. The extra factor in (9)
is sufficient, without any claim that it is necessary.

**Explicit cutoff and the denominator.** The convolutions in (10)
have total smoothing radius 1/64+1/128=3/128. Adding this to the
indicator half-width 12/128 gives support radius 15/128; subtracting
it gives plateau radius 9/128. In particular 15/128<1/8, so the
support is strictly inside E and I, and 9/128>1/16 pays the claimed
plateau. Nonnegativity, unit mollifier masses and the indicator
height give 0<=phi<=1 and integral 3/16. Differentiating r distinct
small factors, for r<=m, costs (128m||eta'||_1)^r and leaves all
other convolution factors of unit L1 mass; Psi has sup norm <=1.
This verifies the exact finite-order specialization of Boman used
in (11), without an assertion about derivatives beyond m.

For n>=2 the largest absolute real part of a band root is
9n/8+7/4<=2n, while its imaginary part is <=17n/4. Thus
353/16<25 verifies (12). Counting the elementary symmetric terms
gives the displayed bound for EVERY coefficient u_r, including
u_0 and the leading coefficient. All derivatives stay supported
in an interval of length 15/64<1/4, so their L1 bounds and the
binomial sum prove (13). The integral of each positive derivative
is zero because of compact support. Since every upper root has
imaginary part at least 15n/8 and the additional root has modulus
n/4, the exact integral of the explicit v is nonzero; using mass
3/16>=1/8 gives (14). This proves that the example really can be
normalized. It does not replace its actual norm by either bound,
and no denominator estimate from this example enters the uniform
action estimate for arbitrary A and phi.

**Bilinear adjoint, quotient and derivative disks.** Integration
by parts for a term u_r(-D)^r phi transfers its r derivatives
with a second factor (-1)^r; the resulting coefficient is u_r,
not its complex conjugate. All boundary terms vanish. This proves
(15)-(16) with the ordinary derivative convention in the hypotheses.
For every compact zeta set, compact support gives an integrable
bound for w(c)c^r exp(zeta*c), for each finite r; hence W and V
are entire and their derivatives may be taken under the integral.
The factorization (16), G|A, and the nonvanishing exponential
prove removability of V/G at every forced root with its full
multiplicity. There is no division by w, g_n or a kernel value.

Actual normalization gives |V(zeta)|<=exp(|zeta|/4). On the circle
of radius 25n, the reverse triangle inequality and |lambda|<5n
give |G|>=(20n)^M. Apply maximum modulus to the holomorphic
quotient on that entire closed disk. On the inner disk of radius
5n, |G|<=(10n)^M, so the ratio is exactly 2^(-M). Finally
|exp(2zeta)|<=exp(10n) there, yielding 25n/4+10n=65n/4
in (18). These estimates hold regardless of any extra roots,
operator order or cancellation inside v.

At z_star, a_b=-1/4+i or -1+i. The largest absolute real part
of a target exponent is 5n/4+2<=9n/4, and its imaginary part
is at most 2n. Since 145/16<16, every target center lies strictly
inside radius 4n. Its complete radius-n derivative circle is
inside radius 5n. Cauchy's formula therefore proves (20) for
all r used in the degree-d primitives. No boundary point or
endpoint polynomial term is lost in this disk argument.

**All target coefficients, surviving window and threshold.** The
sum of s! times the absolute polynomial coefficients is bounded
by the full binomial sum plus 1, all divided by n+1; this retains
K's constant subtraction. Since |a_b|>=1 at z_star, the unrolled
coefficient formula yields (21) for every r. In each term of the
target pairing, the r! from Cauchy's estimate cancels the 1/r!
in that bound, leaving (alpha/n)^r. Here 1<=alpha/n<=2, so the
sum over r=0,...,n+1 is <=2^(n+2)-1. There are exactly four
endpoint terms, each paid this way, producing F_n without a
leading-term approximation or a positivity assumption.

For the last term, the audited C997c bound and the target's
imaginary part give |g_n(t)exp(i z_star t)|<=2(n+2)exp(t/4).
Multiplication by 2 and integration over the length-two lower
window give 8(n+2)exp((n+2)/4). Meanwhile c>=7/4 implies
|W(-n/4)|<=exp(-7n/16), so their product has the exact exponent
-3n/16 and prefactor in (2). If X+n/4 divides A, (16) instead
makes this contribution zero. This includes the explicit P_n.

For the threshold, 2^(n+3)+1<=2^(n+4) and
2^(n+2)-1<=2^(n+2) give the preliminary bound for F_n.
Subtracting M=4n^2+12n+8 from 2n+8 gives -4n^2-10n.
Since this coefficient is negative, log(2)>=1/2 has the upper-
bound direction used in (23). Also 65/4+1/64=1041/64, and
1041/64-5=721/64. For n>=12, n-721/64>=47/64>0;
hence -2n^2+(721/64)n<=-n^2. The lower-window exponent
after scaling is -3n/16+n/64=-11n/64. A fixed linear polynomial
times this decaying exponential tends to zero. This proves the
uniform bound along every unbounded integer subsequence.

**Scope and input audit.** The density has L1 norm one and exact
zero band actions, so it is a legitimate weak certificate at the
original complex coefficient cap. Bounding its target action from
above excludes only this certificate class. The n+1 original
pairing equations do not impose the ODE identities (1); no step
here bounds the supremum over all weak witnesses or E_n itself.
The direct local inputs remain C997c (complete kernel and audited
g_n bound) and C997s (exact primitive and certificate convention).
The named external contracts are cited above and were reused from
the approved assessment; no new source theorem or cross-notebook
input was needed. The original argument and DAG edges are unchanged.
The proof is analytic for all n>=2 with the stated n>=12 comparison;
no numerical sample, mathematical script or finite replay is evidence
for its all-n conclusion. All actual-Xi and transfer gaps remain open.

## Mathlib

Full matching coverage for this complete-kernel normalized obstruction,
the specific finite-order cutoff and its support payment has not been
checked and remains unknown. Supporting standard facts are the named
constant-coefficient ODE basis, distributional derivative identity,
maximum modulus principle, Cauchy integral formula and binomial theorem.
No Mathlib result is asserted to prove the full statement, and no
availability or absence claim is inferred from not searching Mathlib.
