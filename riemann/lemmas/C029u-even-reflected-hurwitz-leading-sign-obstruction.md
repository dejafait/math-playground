# C029u — Infinitely many even reflected members fail the first Hurwitz sign

## Hypotheses

Use the exact full family of C029m, with every odd coefficient retained:

    T_N(t)=sum_(k=0)^N w_(N,k) beta_k p_k(t),
    w_(N,k)=N!/((N-k)!N^k),
    p_(-1)=0, p_0=1,
    (k+1)p_(k+1)=t p_k-(k+1/2)p_(k-1).

The real beta_k are the finite Bernoulli formulas (4)/(13) of
A. Kuznetsov, *Expansion of the Riemann Xi Function in Meixner-Pollaczek
Polynomials*, Canad. Math. Bull. 51(4) (2008), 561–569,
[original publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/FD79D70DF68748CCEC70097E3FB9F2FA/S0008439500012492a.pdf/expansion-of-the-riemann-function-in-meixnerpollaczek-polynomials.pdf),
[DOI](https://doi.org/10.4153/CMB-2008-055-0).

Import the identification of these coefficients with the auxiliary
integrals in that paper: (11), printed p564, for n>=2, and the exact
rotated representation (15), p566. This retains C029m's qualification:
the source's upstream [9] has not been independently audited here.
The result below is relative to this named analytic input. We do not
claim an independent derivation of that identification from (13).
No weighted compact-convergence claim, zero location, degree hypothesis
for all large N, or RH assumption is used.

## Conclusion

For arbitrarily large even integers N, beta_N and beta_(N-1) are both
nonzero and have the same sign. For each such N, T_N has actual degree
N and its monic reflection

    Q_N(t)=(N^N/beta_N) T_N(-t)

satisfies

    Delta_1(Q_N)=-N^2 beta_(N-1)/beta_N < 0.             (1)

Consequently the monic T_N cannot eventually all belong to Tyaglov's
generalized-Hurwitz type-II class. This eliminates that stronger
sufficient class, subject to the cited analytic input; it does not
refute eventual bare exclusion of nonreal zeros in Re(t)<0, the
eventual index premise of C029m, or RH. It says nothing about degree
drops outside the constructed subsequence. Conceptual audit2041
independently checked the transformed-error argument and application;
the named analytic-input qualification remains in force.

## Proof

### 1. Exact coefficient and criterion reduction

Induction in the recurrence gives deg(p_k)=k, leading coefficient
1/k!, and p_k(-t)=(-1)^k p_k(t). In particular p_N has no t^(N-1)
term. Terms of smaller degree than N-1 cannot contribute to either
of the top two coefficients. Therefore

    [t^N]T_N=beta_N/N^N,
    [t^(N-1)]T_N=N^2 beta_(N-1)/N^N.

If N is even and beta_N!=0, reflection preserves the first coefficient
and reverses the second. Monic normalization gives (1), including its
factor N^2. No sign assumption about the original leading coefficient
enters the normalization.

Import M. Tyaglov, *Sign patterns of the Schwarz matrices and generalized
Hurwitz polynomials*, Electronic Journal of Linear Algebra 24 (2012),
215–236, [primary PDF](https://emis.de/ft/34015), (2.1)/(2.5), p217,
Definitions 4.1–4.2 and Theorem 4.3, pp224–225. For a monic real
polynomial of actual degree N, type I requires
Delta_(N-1), Delta_(N-3), ... >0. For even N this list includes Delta_1,
the next-to-leading monomial coefficient. Type II means that its
reflection, with the monic convention, is type I. Thus (1)<0 excludes
type II. No converse from bare nonreal half-plane exclusion is used:
the definitions impose extra real-root and parity restrictions.

The required coefficient signs are proved next. The cited criterion
is not reproved, and isolated numerical degrees play no role.

### 2. Combine the full transformation before estimating

Write c=2 sqrt(pi), q=c(1+i),

    K_n=sqrt(pi)/(2 Gamma(n+3/2)),
    z_n=i(-i)^n exp(i pi/8),
    F_n=K_n integral_0^infinity exp(-x)x^n/(1+exp(q sqrt(x))) dx.

Square roots of nonnegative real numbers are nonnegative. The change
of variable x=nv in the source's (15), with its theta=-q, gives
exactly a_n=Im(z_n F_n) for n>=1. Only n>=3 will be used in the
three-term transformation. This change of variable, including the
factor n in dx, cancels the source's n^(n+1) exp(-n) prefactor.

Explicitly, the source's real prefactor is
(-1)^n K_n n^(n+1) exp(-n-c sqrt(n)), and its complex phase is
i^(n+1) exp(i pi/8-i c sqrt(n)). Its integral becomes

    exp(n+q sqrt(n)) n^(-n-1)
      integral_0^infinity exp(-x)x^n/(1+exp(q sqrt(x))) dx.

Both exponential factors and all powers of n cancel as stated, and
(-1)^n i^(n+1)=i(-i)^n. This checks the phase and Jacobian against
the exact imported (15), without using its later asymptotic expansion.

For n>=2, source (11) is

    beta_n=4n(n-1)a_(n-2)+(8n^2+12n+7)a_n
             +(2n+3)(2n+5)a_(n+2).

For n>=3 use z_(n-2)=z_(n+2)=-z_n and the Gamma recurrence:

    K_(n-2)/K_n=(n-1/2)(n+1/2),
    K_(n+2)/K_n=1/((n+3/2)(n+5/2)).

It follows, without discarding any term, that

    beta_n=Im[z_n K_n integral_0^infinity
                 exp(-x)x^n P_n(x)/(1+exp(q sqrt(x))) dx],       (2)
    P_n(x)=8n^2+12n+7-4x^2
              -4n(n-1)(n^2-1/4)/x^2.

These integrals converge absolutely. At zero their most singular
power is x^(n-2); at infinity exp(-x) controls every polynomial
factor. Thus combining three integrals uses no unproved limiting
interchange. The cancellation of the nominal n^2 contribution is
retained exactly in P_n, rather than inferred from separately
estimated oscillatory terms.

Put x=n+sqrt(n)u=nv, h(v)=log(v)-v+1, and

    D(x)=1/(1+exp(-q sqrt(x))),
    H_n(u)=n h(1+u/sqrt(n))
               -q sqrt(n)(sqrt(1+u/sqrt(n))-1),
    J_n=integral_(-sqrt(n))^infinity
          exp(H_n(u)) D(n+sqrt(n)u) P_n(n+sqrt(n)u)/n du.

Then (2) becomes the exact identity

    beta_n=Im[z_n K_n n^(n+3/2) exp(-n-q sqrt(n)) J_n].         (3)

We will prove the absolute complex estimate

    J_n=32 pi i sqrt(2pi)+O(n^(-1/2)).                         (4)

All O constants below are independent of n; q is fixed. No assertion
of a relative error at a zero of a sine is made.

### 3. Global control for the combined integral

First |D(x)|<=2 for x>=0. Indeed, if c sqrt(x)<=1 then
cos(c sqrt(x))>0, so the real part of 1+exp(-q sqrt(x)) is at least
1. If c sqrt(x)>=1, the triangle inequality gives modulus at least
1-exp(-1)>1/2. The endpoint x=0 gives D(0)=1/2. Also

    |D(x)-1|<=2 exp(-c sqrt(x)).                               (5)

These bounds include small x, where simply replacing D by 1 would
not be uniformly justified.

On 1/2<=v<=2, h(1)=h'(1)=0 and h''(v)=-1/v^2<=-1/4. Taylor's
integral formula consequently gives h(v)<=-(v-1)^2/8. Since
sqrt(n)(sqrt(v)-1)=u/(sqrt(v)+1),

    Re H_n(u)<=-u^2/8+c|u|.                                  (6)

The explicit formula for P_n gives |P_n(nv)/n|<=C n on this interval.
Thus the part with |u|>n^(1/12) has absolute value at most

    C n integral_(|u|>n^(1/12)) exp(-u^2/8+c|u|) du,

which is smaller than every fixed negative power of n. To see this
without an unproved tail interchange, for |u|>=16c the exponent is
at most -u^2/16, and the elementary Gaussian tail estimate follows
by comparing |u| with its lower endpoint in the integral of
|u| exp(-u^2/16). Its exponential factor dominates every power of n.

For 0<v<=1/2, |P_n(nv)/n|<=C n v^(-2) and
Re H_n<=n h(v)+c sqrt(n). Changing back from u to v shows that this
tail has absolute value at most

    C n^(3/2) exp(c sqrt(n)) integral_0^(1/2) v^(-2) exp(n h(v)) dv.

For n>=3, h is increasing on (0,1) and h(1/2)=1/2-log(2)<0.
Crucially the apparent singularity is absorbed exactly:

    v^(-2) exp(n h(v))
      =exp(2(1-v)) exp((n-2)h(v))
      <=exp(2) exp((n-2)h(1/2)).

After integration the tail is exponentially small in n, even with
the displayed exp(c sqrt(n)) and polynomial factors. This pays the
small-x endpoint in the transformed, not just the auxiliary, integral.

For v>=2, |P_n(nv)/n|<=C n(1+v^2), the real square-root term in
H_n is nonpositive, and

    h(v)<=h(2)-(v-2)/2,    h(2)=log(2)-1<0.

Hence the upper tail is bounded by

    C n^(3/2) exp(n h(2))
       integral_2^infinity (1+v^2) exp(-n(v-2)/2) dv.

For n>=3 the last integral is bounded by its value with n=1 and is
finite, so this tail too is exponentially small. These three estimates
cover the entire complement of |u|<=n^(1/12).

### 4. Central expansion with an integrable absolute error

On |u|<=n^(1/12), put y=u/sqrt(n); eventually |y|<=1/2.
Taylor's theorem on that fixed interval gives, with constants
independent of u and n,

    H_n(u)=-u^2/2-q u/2+R_n(u),
    |R_n(u)|<=C n^(-1/2)(u^2+|u|^3).                         (7)

In particular the supremum of |R_n| on this region tends to zero.
For the polynomial multiplier, its exact rescaled form is

    P_n(n+sqrt(n)u)/n
      =8n+12+7/n-4n(1+y)^2
          -4(n-1)(1-1/(4n^2))(1+y)^(-2).

Use (1+y)^(-2)=1-2y+3y^2+O(|y|^3), whose remainder is bounded
uniformly on |y|<=1/2. The order-n and order-sqrt(n) terms cancel,
leaving

    P_n(n+sqrt(n)u)/n=16(1-u^2)+E_n(u),
    |E_n(u)|<=C n^(-1/2)(1+|u|^3).                         (8)

For clarity, the terms left before the cubic Taylor remainder are
16-16u^2+8/n-1/n^2-8u/sqrt(n)
-2u/n^(3/2)+2u/n^(5/2)
+12u^2/n+3u^2/n^2-3u^2/n^3; these obey (8) on the stated region.

Eventually |R_n|<=1, so |exp(R_n)-1|<=e|R_n|. Combining (5),
(7), and (8), the difference of the central integrand and

    16(1-u^2) exp(-u^2/2-q u/2)

is bounded in absolute value by

    C [n^(-1/2)(1+|u|^5)
       +exp(-c sqrt(n/2))(1+|u|^3)]
       exp(-u^2/2+c|u|/2).                                (9)

One explicit justification, avoiding a product of unbounded remainders,
is to write A(u)=-u^2/2-q u/2 and L(u)=16(1-u^2). After factoring
exp(A), the difference is exactly

    exp(R_n) D E_n + L (exp(R_n)-1)D + L(D-1).

The first two terms use |D|<=2 and |exp(R_n)|<=e; the last uses
x=n+sqrt(n)u>=n/2 and (5). The powers required are at most five,
and all constants depend only on the fixed q. This proves (9) with
a common n-independent constant, rather than pointwise domination.

Each displayed Gaussian times polynomial has finite integral on R.
For example, beyond |u|>=2c its exponent is at most -u^2/4.
Integrating (9) therefore gives O(n^(-1/2)). Extending the limiting
integrand from the central region to R costs a Gaussian tail, also
o(n^(-1/2)). Together with Section 3 this proves

    J_n=16 integral_R (1-u^2) exp(-u^2/2-q u/2) du
            +O(n^(-1/2)).                                 (10)

This argument supplies the uniform and tail justification missing
from a merely pointwise saddle expansion. It does not require
uncorrelated remainder bounds for three neighboring a coefficients.

The standard Gaussian integral and its second derivative give

    integral_R exp(-u^2/2+z u) du=sqrt(2pi) exp(z^2/2),
    integral_R u^2 exp(-u^2/2+z u) du
        =(1+z^2)sqrt(2pi) exp(z^2/2),

also for complex z. One justification is the real Gaussian formula,
analytic continuation, and differentiation dominated on every compact
z-set by exp(-u^2/2+M|u|) times the relevant polynomial. Set z=-q/2.
Since q^2=8pi i and exp(q^2/8)=-1, the integral in (10) equals

    -4q^2 sqrt(2pi) exp(q^2/8)=32 pi i sqrt(2pi).

This proves (4), with a nonzero leading constant after cancellation.

### 5. Final beta scale and an infinite even-degree subsequence

Define the strictly positive, exact scale

    B_n=32 pi sqrt(2pi) K_n n^(n+3/2) exp(-n-c sqrt(n))
       =16 sqrt(2) pi^2 n^(n+3/2) exp(-n-c sqrt(n))/Gamma(n+3/2).

Equations (3)–(4), including z_n=i(-i)^n exp(i pi/8), imply

    beta_n=B_n [sin(n pi/2+c sqrt(n)-pi/8)+epsilon_n],
    |epsilon_n|<=C n^(-1/2).                              (11)

The error in beta_n is thus absolutely at most C B_n/sqrt(n), not
relative to the possibly vanishing sine. Explicitly, the leading
phase in (3) is the imaginary part of
-(-i)^n exp(i pi/8-i c sqrt(n)), which is the sine in (11).
The scale B_n is exact, so no Gamma asymptotic or effective numerical
onset is needed for the sign argument.

Let theta_n=c sqrt(n)-pi/8. The sequence theta_(2m) is strictly
increasing and unbounded, with successive increments

    theta_(2m+2)-theta_(2m)=2c/(sqrt(2m+2)+sqrt(2m)) ->0.

For every sufficiently large integer j, choose m_j minimal with
theta_(2m_j)>=2pi j+3pi/4, and put N_j=2m_j. Minimality and the
vanishing preceding increment give, once that increment is <pi/12,

    2pi j+3pi/4 <= theta_(N_j) < 2pi j+5pi/6.             (12)

These N_j are unbounded (and eventually distinct). Also
theta_N-theta_(N-1)=c/(sqrt(N)+sqrt(N-1))->0, so once it is <=pi/12,

    2pi j+2pi/3 <= theta_(N_j-1) < 2pi j+5pi/6.           (13)

On (12), sin(theta_(N_j))>=1/2; on (13),
cos(theta_(N_j-1))<=-1/2. Writing N_j=2m_j, the two sine terms
in (11) are respectively

    (-1)^m_j sin(theta_(N_j)),
    (-1)^(m_j+1) cos(theta_(N_j-1)).

Both have sign (-1)^m_j and absolute value at least 1/2. For all
sufficiently large j, both errors in (11) are at most 1/4. Consequently

    (-1)^m_j beta_(N_j) >= B_(N_j)/4 >0,
    (-1)^m_j beta_(N_j-1) >= B_(N_j-1)/4 >0.

This certifies actual degree N_j and a strict negative first minor,
with no reliance on phase points close to a zero. Substituting into
(1) even gives

    Delta_1(Q_(N_j)) <= -(N_j^2/5) B_(N_j-1)/B_(N_j) <0,

because |beta_(N_j)|<=5 B_(N_j)/4. The required sign was positive;
there are arbitrarily large strict violations. Higher determinants
cannot repair failure of this necessary condition.

### Qualifications and relevance

The new local result is the cancellation-safe actual-coefficient
asymptotic and its uniform obstruction to this selected sufficient
class. The imported general criterion and integral representation
remain known inputs. The source's own auxiliary expansion is neither
called a new result nor used without its missing transformed-error
justification. Literature assessment2037 did not establish a matching
prior actual-family sign theorem; this is not a claim of originality.

This proof establishes no actual nonreal zero, no statement about all
large actual degrees, and no failure of bare one-sided exclusion.
The analytic identification's upstream[9] qualification remains; the
weighted compact limit, its one-sided symmetry interface, and the
main all-degree mixed-positivity gap are not paid by this obstruction.

**Conceptual audit2041 (completed 21 November 2026).** The exact top-coefficient
ratio and even reflection were independently replayed. Primary (11)
and (15) were checked at printed pp564/566; Tyaglov's (2.1)/(2.5)
and Definitions4.1-4.2/Theorem4.3 were checked at pp217/224-225,
reusing the approved proof-case comparison rather than asserting an
audit of its upstream R-function theorems. The published necessary
criterion needs neither every Hurwitz determinant nonzero nor a
nonzero constant term. Only even actual degrees are applied here.

The replay checks the n^(n+3/2) prefactor in (3), both Gamma ratios,
all central polynomial terms, and each of the three tail regions.
The lower tail decays with rate (n-2)(1/2-log(2))+c sqrt(n);
the upper tail has rate n(log(2)-1); the remaining middle tail has
Gaussian decay beyond n^(1/12). Each is o(n^(-1/2)) after its
displayed polynomial factor. Equations (7)-(9) have constants uniform
on their entire expanding central interval. The complex Gaussian
calculation uses q^2=8pi i and exp(q^2/8)=-1; its leading sign,
the positive exact B_n, and the absolute error in (11) all agree.
The phase intervals have margins >=1/2 against errors <=1/4,
certify actual degree N and the strict negative minor, and prove
an unbounded subsequence rather than a sampled or all-degree claim.

No mathematical defect was found and no conclusion was strengthened.
This audit makes the qualified sufficient-class stop available for
route selection; it does not newly establish a result beyond the
existing C029u proof, remove upstream[9], or prove any Xi zero location.
The source's auxiliary asymptotic is not substituted for the combined
integral estimate. No numerical computation is used as verification.

## Mathlib

The full actual-family asymptotic, generalized-Hurwitz specialization
and integral identification have not been checked in Mathlib. Standard
Gaussian integration and Gamma recurrence are supporting mathematical
inputs, not evidence of a matching formal theorem. No absence claim
or formal verification claim is made. No numerical certificate or
mathematical script is needed for the analytic estimates above.
