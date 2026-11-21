# Corollary 997u: the complete-column determinant density exists, but its rate is unpaid

## Hypotheses

Use the COMPLETE kernel of audited C997c(1),(4)–(6) and C997s(2):

    k_n(c,z)=-2 exp(-cn/4) [integral_(cn)^(c(n+2)) g_n(t)exp(izt)dt
                             -integral_n^(n+2) g_n(t)exp(izt)dt],
    g_n(t)=K_(n+2)(t)exp(-t/2)cosh(3t/8),
    K_(n+2)(t)=(L_(n+1)^(2)(t)-1)/(n+1).

Here n>=2 is an integer, m=n+1, I=[7/4,9/4], E=[15/8,17/8],
z_star=1+i/8, and gamma_j=15/8+j/(4n), 0<=j<=n. Set
f_j(c)=k_n(c,gamma_j) and h(c)=k_n(c,z_star). Keep both beta terms,
both windows, K's constant subtraction, all zeros and both closed
endpoints. No Haar property, zero simplicity or actual-Xi input is assumed.

Fix the cutoff independently of the subsequent estimates. Let eta be
the nonnegative unit-mass normalization of exp(-1/(1-x^2)) on |x|<1,
extended by zero, and eta_a(x)=eta(x/a)/a. With real-line convolution,

    Psi=1_[2-3/16,2+3/16] * eta_(1/64),
    chi_m=Psi * (eta_(1/(64m)))^(*m).

Use ordinary derivatives, and fix the determinant orientation by

    P u=W(f_0,...,f_n,u)=det[D^r f_0 ... D^r f_n D^r u]_(r=0,...,m),
    a_r=(-1)^(r+m) det[D^k f_j]_(k in {0,...,m}\{r}, j=0,...,n),
    P=sum_(r=0)^m a_r D^r,
    A=P h, phi=chi_m conjugate(A),
    v=P^t phi=sum_(r=0)^m (-1)^r D^r(a_r phi).             (1)

Rows in each minor retain increasing order. The transpose is bilinear;
its coefficients are not conjugated. No division by a Wronskian or g_n
occurs. These definitions use all n+1 band columns, without rank reduction.

## Conclusion

For EVERY fixed n>=2 the band columns, together with h, are linearly
independent over C. The leading Wronskian and A are entire and not
identically zero; their pointwise zeros need not be absent. The density
v is smooth, supported strictly inside I, and nonzero. In particular,

    N_n=integral_I chi_m(c)|A(c)|^2 dc >0,
    integral_I v f_j=0 for every j,
    integral_I v h=N_n,
    w_n=v/||v||_1,  ||w_n||_1=1.                         (2)

This gives the fixed-n complete-kernel weak certificate

    E_n >= N_n/||v||_1 >0,                               (3)

where E_n has C997s's original complex coefficient cap exp(sqrt(n)).
The band leakage is exactly zero, so no budget is omitted from (3).

The explicit finite upper bound U_n in (11) below pays every coefficient,
cofactor derivative and cutoff derivative in ||v||_1. It does NOT prove
the required asymptotic statement. This attempt establishes neither
unboundedness nor boundedness of

    R_n=exp(n/64) N_n/||v||_1.                            (4)

There is no useful uniform lower bound for N_n in relation to U_n and
no useful lower bound for the actual norm in relation to N_n. The
family is therefore parked under review379's bounded-attempt test.
This is an INCONCLUSIVE attempt, not a degeneracy or impossibility result.

Step381, 11 November 2026: RESEARCH / REPRODUCTION / EXPLORATION,
proof_attempt, under the unchanged pre-invocation EXPLORE review379,
separately approved at step380. The construction specializes known
determinant, analytic-independence and transpose results; no mathematical
discovery beyond the checked sources is claimed. The present proof has
not received an independent conceptual audit. Fixed-n admissibility is
not the quantitative gate's success criterion and is not reported as an
asymptotic advance. No RH candidate or bound on optimal E_n at the
required rate is established.

## Proof

### Imported contracts and their roles

A. Bostan and P. Dumas, *Wronskians and linear independence*, American
Mathematical Monthly 117 (2010), 722–727,
[author manuscript](https://mathexp.eu/dumas/publications/Bostan_Dumas_2010_WLI.pdf),
Theorem 1, p1 (Theorem 2 and Lemmas 1–3, pp2–4, provide the formal-series
proof): independent analytic functions on a connected domain have a
Wronskian which is not identically zero. This is NOT a pointwise
nonvanishing or quantitative theorem.

A. Kasman, *Spectral difference equations satisfied by KP soliton
wavefunctions*, Inverse Problems 14 (1998), 1481–1487,
DOI 10.1088/0266-5611/14/6/008,
[published author PDF](https://kasmana.people.charleston.edu/spec-solitons.pdf),
p1484 equation (3), the following paragraph and Lemma 3.1: the augmented
Wronskian numerator has polynomial-exponential coefficients. We use only
the numerator construction, not its quotient by the leading Wronskian
or a quantitative consequence of the source's factorization.

S. Dyatlov, *Lecture notes for 18.155: distributions, elliptic regularity,
and applications to PDEs*, version 2 November 2026,
[author notes](https://math.mit.edu/~dyatlov/18.155/155-notes.pdf),
Definition 9.1 and (9.1)–(9.4), pp97–98, with Definition 7.12 and
Proposition 7.14, pp84–85: the smooth-coefficient bilinear transpose of
sum a_r D^r is sum (-1)^r D^r(a_r .), with support preservation and the
compact-test integration-by-parts identity. This uses ordinary D and
differs from the sesquilinear adjoint in Remark 7.13.

J. Boman, *On the propagation of analyticity of solutions of differential
equations with constant coefficients*, Arkiv för Matematik 5 (1964),
271–279, DOI 10.1007/BF02591127,
[primary paper](https://archive.ymsc.tsinghua.edu.cn/pacm_download/116/7017-11512_2007_Article_BF02591127.pdf),
Lemma 1, pp272–273, (2.1), (2.2') and its convolution proof: the
order-dependent cutoff has bounds (C m)^r through order m. The support
margins and a numerical C for the fixed choice above are checked below.

For the independence specialization we also reuse the standard
exponential-polynomial basis stated in J. M. Aldaz, O. Kounchev and
H. Render, *Bernstein operators for exponential polynomials*,
[arXiv:0805.1618v1](https://arxiv.org/pdf/0805.1618v1), pp1–3,
section 1(1),(3) and section 2's repeated-root paragraph. Distinct
complex exponents lambda with prescribed multiplicities have independent
basis functions c^r exp(lambda c) up to those multiplicities. No positive
Bernstein, real-root or interval Chebyshev hypothesis is imported.

These contracts were already inspected in reviews373/378/379. Their
generic proofs are not reproduced. What follows is the necessary exact
kernel specialization, zero handling and finite norm calculation. C997t
is a contrast: its constant-coefficient forced-root bound does not apply
to (1), and no conclusion from that stop is used as a premise here.

### Complete endpoint representation and nondegeneracy

By C997s(2), write K_(n+2)(t)=sum_(s=0)^m p_s t^s, where

    p_s=(-1)^s binomial(n+3,m-s)/(m s!)-1_{s=0}/m.

For b=-1/8,-7/8 and z in the band grid or at z_star, put a=b+iz and

    q_r(b,z)=sum_(s=r)^m (-1)^(s-r) s! p_s/(r! a^(s-r+1)),
    Q_(b,z)(t)=sum_(r=0)^m q_r(b,z)t^r,
    lambda_(b,alpha)(z)=-n/4+alpha(b+iz), alpha=n,n+2,
    ell(z)=sum_b [exp((b+iz)(n+2))Q_(b,z)(n+2)
                              -exp((b+iz)n)Q_(b,z)(n)].

All these a have positive imaginary part, hence are nonzero. The exact
primitive identity Q'+aQ=K gives

    k_n(c,z)=-sum_b [exp(lambda_(b,n+2)(z)c)Q_(b,z)((n+2)c)
                          -exp(lambda_(b,n)(z)c)Q_(b,z)(nc)]
                         +exp(-nc/4)ell(z).              (5)

Thus every column is entire in c. In particular (5) proves Kasman's
polynomial-exponential applicability without an asymptotic Laguerre
replacement. Explicitly, let Delta_(lambda,s) be the functional
F -> F^(s)(lambda) on entire functions of a variable w. Then
Delta_(lambda,s)[exp(cw)]=c^s exp(lambda c). The coefficients
of Q_(b,z)(alpha c), with the signs in (5), and ell(z) at (-n/4,0),
give a finite linear combination of these point-derivative evaluations
whose exponential image is exactly k_n(c,z).

The four real parts of the upper band exponents are, in descending order,

    -3n/8, -3n/8-1/4, -9n/8, -9n/8-7/4.

They are distinct for n>=2. Within each family the imaginary parts
alpha gamma_j are distinct, including j=0,n. They are positive, so
none equals the lower exponent -n/4. Each corresponding polynomial has
degree m and nonzero leading coefficient alpha^m p_m/(b+iz), since
p_m=(-1)^m/(m m!) is nonzero. In a linear combination of band columns,
the coefficient of an upper exponent unique to column j can therefore
vanish only if that column's multiplier is zero. Apply the cited
exponential-polynomial basis independence to the finite union of
exponents. This proves independence of all band columns; ell is allowed
to vanish and is never used to infer independence.

The target has a nonzero upper term with exponent -n/2+in (b=-1/8,
alpha=n). Its imaginary part n is smaller than every upper band
imaginary part, which is at least 15n/8. It is not the lower real
exponent, and the other target term of imaginary part n has different
real part -5n/4. The target's alpha=n+2 terms have imaginary part n+2.
Thus the same basis independence forces the target multiplier to vanish
in any linear relation among the band columns and h; the band
independence then finishes that relation.

Bostan–Dumas now applies on the connected complex plane, both to the
m band functions and to the m+1 functions including h. Consequently
a_m and A=W(f_0,...,f_n,h) are not identically zero. They may vanish
at individual real or complex points. Every a_r is entire and is kept
at all such points; no inverse is taken. The determinant with a repeated
column gives P f_j=0 identically. Expanding the last column gives
exactly the signs and ordinary-derivative order in (1).

### Fixed cutoff, transpose and actual normalization

The smoothing radii sum to 1/64+m/(64m)=1/32. Thus

    supp chi_m subset J=[2-7/32,2+7/32] subset interior(I),
    chi_m=1 on [2-5/32,2+5/32],
    0<=chi_m<=1,  integral chi_m=3/8.                    (6)

The plateau contains a neighborhood of the closed E. The mollifier is
smooth and unimodal, so ||eta'||_1=2 eta(0). Its normalizing denominator
is at least exp(-4/3), by integrating on [-1/2,1/2], of length one.
Hence ||eta'||_1<=2 exp(1/3)<4; for example the exponential series gives
exp(1/3)<=sum_(k>=0)(1/3)^k=3/2<2. Specializing Boman's derivative
allocation to the m small convolution factors gives the explicit bound

    ||chi_m^(r)||_infinity <= (256m)^r, 0<=r<=m.          (7)

The fixed seed has sup norm at most one. No estimate beyond order m is
needed. This verifies the source's support and constant hypotheses for
the specified cutoff, rather than optimizing its choice after a result.

Since A is analytic and chi_m is compactly supported in interior(I),
phi and v are smooth with support in J. Dyatlov's transpose identity
can be applied to f_j or h by first multiplying either by a smooth
function equal to one near J. Their derivatives there are unchanged.
All boundary traces at the endpoints of I vanish. Therefore

    integral_I v f_j=integral_I phi P f_j=0,
    integral_I v h=integral_I phi P h=integral_I chi_m |A|^2=N_n.

There is no coefficient conjugation in the integration by parts; the
only conjugation was intentionally put into phi. If A vanished on the
interior of E, the identity theorem would make it identically zero.
It does not, so continuity and (6) give N_n>0. This proves v is not
identically zero and its finite actual L1 norm is strictly positive.
It handles possible zeros of A, a_m and g_n without removing any point.

For any admissible complex coefficients B_j, pairing w_n with
h-sum B_j f_j gives N_n/||v||_1. Its modulus is at most the continuum
supremum because ||w_n||_1=1. Taking the infimum proves (3), the
absolutely continuous version of C997s's weak certificate. No strong
duality, continuum discretization or approximation to nullity is used.

### Explicit growing-order bound with all product derivatives retained

The following bounds are deliberately displayed with their full costs.
They are norm upper bounds, not an action upper bound. Set

    C_n=(2^(n+3)+1)/(n+1), H_n=8 C_n exp(9n/2), q=7n,
    S=m(m+1)/2, L=length(J)=7/16.

The coefficients above satisfy sum_(s=0)^m s!|p_s|<=C_n, including the
subtracted constant. For every z used here, |b+iz|>=1, whence
r!|q_r(b,z)|<=C_n. The polynomial derivative sum gives
|D^l Q_(b,z)(alpha c)|<=C_n alpha^l exp(alpha c), for c in I;
when l>m its left side is zero. All upper exponents have negative real
part and modulus <=5n: on the band the absolute real and imaginary
parts are at most 2n and 17n/4, whose squared sum is 353n^2/16<25n^2;
at the target they are at most 9n/4 and 2n, whose squared sum is
145n^2/16<16n^2. Also alpha<=2n. Leibniz's rule thus bounds each
upper endpoint term's r-th derivative on I by
C_n exp(9n/2)(7n)^r. The lower coefficient has
|ell(z)|<=4 C_n exp(2n), directly from (5), and its r-th derivative
contribution is at most 4 C_n exp(2n)(n/4)^r. Summing all four upper
terms and that lower term proves, for every r>=0,

    ||D^r k_n(.,z)||_(C(I)) <= H_n q^r.                 (8)

For a_r^(s), differentiate the minor by allocating the s derivatives
among its m columns. Each term has total derivative-row degree
S-r+s, determinant bound m! H_n^m q^(S-r+s), and multinomial
coefficients whose sum is m^s. Similarly A has m+1 columns. Therefore

    ||a_r^(s)||_infinity <= m! H_n^m q^(S-r)(mq)^s,
    ||A^(s)||_infinity <= (m+1)! H_n^(m+1) q^S ((m+1)q)^s.             (9)

These hold on I for all s>=0; only s<=m is used next. A derivative
of the conjugate along the real axis is the conjugate derivative and
has the same bound. In the full transpose one must use

    D^r(a_r chi_m conjugate(A))
      =sum_(s+t+u=r) r!/(s!t!u!)
                      a_r^(s) chi_m^(t) conjugate(A^(u)).            (10)

Combining (7),(9),(10) and the trinomial theorem, then integrating on
J, gives the explicit finite bound

    ||v||_1 <= U_n,
    U_n=L m!(m+1)! H_n^(2m+1) q^(2S)
                 *sum_(r=0)^m [2m+1+256m/q]^r.          (11)

Indeed the derivative factor before extracting q^r is
mq+256m+(m+1)q. The cofactor prefactor q^(S-r) cancels that extracted
q^r, leaving exactly q^(2S). No cofactor derivative has been suppressed
and no n-dependent constant is unnamed. The bound can be very wasteful;
it is not asserted to be the true norm's growth rate.

### What the bounded test did and did not establish

For comparison, C997c's audited |g_n(t)|<=2(n+2)exp(3t/8), together
with |exp(iz_star t)|=exp(-t/8), gives directly on I

    ||h||_infinity <= T_n,
    T_n=18(n+2)exp(9/8)
                 +8(n+2)exp(1/2)exp(-3n/16).            (12)

The upper-window estimate uses its length 2c and cancels exp(-cn/4)
against exp(cn/4); the lower-window estimate uses length two and
c>=7/4. Both windows and beta terms are still present. Equations
(2),(11),(12) give only

    exp(n/64) N_n/U_n <= R_n <= exp(n/64) T_n.           (13)

The right side does not yield a bounded scaled action. The left side
has no useful uniform lower estimate because N_n has only been proved
positive at each fixed n. An upper bound on N_n cannot be substituted
as a lower bound in (13). Nor does a large U_n imply a large actual
denominator, or that this family fails. Thus (13) proves neither side
of review379's required asymptotic discrimination.

The variable operator avoids the formal mandatory-root premise of
C997t, but (9)–(11) expose the still-uncontrolled relation between
cofactor growth and the positive response energy. Nonidentical
Wronskian vanishing, lower differential order and phase alignment alone
do not supply that relation. No fixed-n computation is presented as
an unbounded-n certificate. Under the approved stopping rule, park this
particular recipe; resuming it requires a new quantitative input, not
another derivation of (2) or a re-selection of the same cutoff.

The argument neither settles the original capped E_n nor rules out
other exact-null or paid-leakage witnesses. C997a(8), selected/both-sign
transfer, assay/reconstruction, complements/regulators, L993, L984(H),
L966/L968 signed forcing and actual-Xi signs remain unresolved.

## Mathlib

Full matching coverage for this complete-kernel determinant density and
its asymptotic action has not been checked and is unknown. No Mathlib
theorem is an input. The generic results are imported by the precise
primary citations above; the specialization is an informal proof,
not a Lean verification. No mathematical script or numerical certificate
is needed for the fixed-n identities or the finite bounds (5)–(13).
