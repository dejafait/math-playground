# Lemma 622: collective signed Xi transfer and the unscaled row-sum stop

## Hypotheses

Use the actual Xi of L018 and the normalization of L471:

    A(t)=(t^2+1/4) pi^(-1/4)|Gamma(1/4+it/2)|/2,
    Z(t)=-Xi(t)/A(t),
    W(t)=(Xi'(t)^2-Xi(t)Xi''(t))/A(t)^2.

All derivatives are ordinary derivatives. Fix a nonnegative
w in C_c^infinity((0,1)), with integral 1. Let T tend to infinity,
L=log T, T<=X<=2T, w_XT(t)=w((t-X)/T), and

    N=floor(T^(1/100)),
    M(t)=sum_(n<=N) a_n n^(-it),   sum_(n<=N)|a_n|^2=1,
    U_c(t)=c0 Z(t)+c1 Z'(t)/L,    c0^2+c1^2=1.

The a_n are complex, c0,c1 are real, and all these coefficients
may depend on T and X. There is one common observer c, not an
independently chosen observer at each frequency.

Import C. P. Hughes and M. P. Young, *The twisted fourth moment of
the Riemann zeta function*, J. reine angew. Math. 641 (2010),
203–236, [arXiv:0709.2345v2, Theorem 1.1, (11)–(17), printed
pp. 3–5](https://arxiv.org/pdf/0709.2345v2#page=3), including its
complete-sum holomorphy remark on p. 5. Its divisor estimates and
the cited CFKRS holomorphy argument are named imports, not audited
manuscript proofs. The local analytic gamma bounds use L465;
L619's audited H=T application supplies the untwisted absolute
fourth-moment and observer bounds. No new zero-free assumption,
RH, simplicity, lower zero spacing or pointwise sign is imposed.

## Conclusion

Define the exact six-term matrix K_c(T,X) in the proof below, using
every gcd-reduced pair with its original coefficient multiplicity,
the full prime-power factors, and the exact analytic Hardy phase.
It is Hermitian by the specified symmetrization. There is C_w,
independent of T,X,a,c, such that for all sufficiently large T,

    | integral w_XT(t) W(t)|M(t)|^2 U_c(t)^2 dt/(T L^6)
                       - a^* K_c(T,X) a |
       <= C_w [ T^(-17/80)/L^4 + T^(-199/100)/L^2 ].       (1)

Neither a frozen-phase O(1/L) error nor an entrywise leading-term
replacement is used in (1). The constants and onset are existential;
(1) is not a finite-height numerical sign certificate.

The elementary sufficient test of positive unscaled row diagonal
dominance fails: for every allowed common c, uniformly for X in
[T,2T], the first row satisfies, beyond one onset,

    (K_c)_(1,1) - sum_(n=2)^N |(K_c)_(1,n)| < 0.          (2)

This is a failure of that sufficient test, not a negative eigenvalue.
In fact the limiting normalized principal block on {1,2,3} is
strictly positive definite, as verified below. No sign or smallest
eigenvalue bound for the growing full matrix is proved.

This supplies a previously missing coefficient-uniform local
application of the imported moment theorem. It is reproduction /
specialization, not a new arithmetic theorem, a proof of positivity,
a negative Xi witness, or an RH candidate. Bound (1), with Sections
1–4, passed the separate conceptual application audit recorded below
on 1 November 2026, under the named imports. Section 5 and (2) were
outside that audit. Pointwise signs, the collective spectrum, and
all-degree mixed positivity remain unresolved.

## Proof

### 1. Exact source expression and the matrix being tested

For q=(alpha,beta,gamma,delta), put

    sigma_(u,v)(n)=sum_(d e=n) d^(-u) e^(-v),
    J(q)=zeta(1+alpha+gamma) zeta(1+alpha+delta)
         zeta(1+beta+gamma) zeta(1+beta+delta)
         /zeta(2+alpha+beta+gamma+delta).

For coprime h,k define B_hk(q) exactly as source (14) at s=0.
More explicitly, write

    D_p(q)=sum_(j>=0) sigma_(alpha,beta)(p^j)
                        sigma_(gamma,delta)(p^j) p^(-j).

For p^e||h the factor is

    [sum_(j>=0) sigma_(alpha,beta)(p^j)
                  sigma_(gamma,delta)(p^(j+e)) p^(-j)]/D_p(q);

for p^e||k increment the first divisor function instead. Multiply
these factors over the primes dividing hk, and set R_hk(q)=J(q)B_hk(q).
There is no omission of small primes or prime powers. With
ell=log(t/(2pi)), the six-term sum is

    S_hk(t;q)=R_hk(alpha,beta,gamma,delta)
      + exp(-ell(alpha+beta+gamma+delta))
                           R_hk(-gamma,-delta,-alpha,-beta)
      + exp(-ell(alpha+gamma)) R_hk(-gamma,beta,-alpha,delta)
      + exp(-ell(alpha+delta)) R_hk(-delta,beta,gamma,-alpha)
      + exp(-ell(beta+gamma)) R_hk(alpha,-gamma,-beta,delta)
      + exp(-ell(beta+delta)) R_hk(alpha,-delta,gamma,-beta).  (3)

Only the complete holomorphic value of this sum is used at shift
collisions. These are the six terms of the imported theorem, with
the same (h,k) orientation in each.

Use compatible analytic gamma logarithms as in L465 and L619:

    g(s)=log Gamma(s/2)-(s/2)log pi,
    theta(z)=[g(1/2+iz)-g(1/2-iz)]/(2i),
    q(b)=(i b1,i b2,-i b3,-i b4)/L,
    Phi(t,b)=exp(i[theta(t+b1/L)+theta(t+b2/L)
                      -theta(t+b3/L)-theta(t+b4/L)]).

For real t in the support and bounded complex b these functions
use branches on one neighborhood of [T,3T]. In particular the
analytic amplitude is

    A_an(z)=(z^2+1/4)/2
             * exp([g(1/2+iz)+g(1/2-iz)]/2).

It is nonzero on this neighborhood and equals A(t)>0 on the real
interval. Thus Z(z)=-Xi(z)/A_an(z) is holomorphic even at Xi zeros.
L018's functional equation and L465's analytic normalization give
the exact identity

    product_(j=1)^4 Z(t+bj/L)=Phi(t,b) F(t,b),              (4)

where F is the four-zeta product with shifts q(b), the first two
at height t and the last two at height -t. The two unshifted
positive phases and the two negative phases cancel exactly.

Set

    H_hk(b)=1/(T L^4 sqrt(hk))
                 integral w_XT(t) Phi(t,b) S_hk(t;q(b)) dt,
    Q=partial_1 partial_2-(partial_1^2+partial_2^2)/2,
    V_c=(c0+c1 partial_3)(c0+c1 partial_4),
    J_hk(c)=(Q V_c H_hk)(0).

Here H includes every term of (3) and the exact phase; none is
replaced by its leading asymptotic. For 1<=m,n<=N, g_mn=gcd(m,n),
define

    (K_c)_(m,n) = [ J_(n/g_mn,m/g_mn)(c)
                       + conjugate(J_(m/g_mn,n/g_mn)(c)) ]/2. (5)

Thus K_c is Hermitian and, with the ordinary convention a^* K_c a,

    a^* K_c a
      = Re sum_(m,n<=N) a_m conjugate(a_n)
                               J_(m/g_mn,n/g_mn)(c).        (6)

We do not need the unsymmetrized source approximation itself to
be exactly Hermitian. Taking its real part in (6) loses no actual
signed integral and cannot increase its absolute error.

### 2. Uniform admissibility of the exact complex phase weight

For b in a fixed polydisc, say |bj|<=2, sector digamma estimates
used in L465 give theta'(z)=O(L) on |z-t|<=2/L. For each integer
j>=1 they also give

    theta^(j+1)(z)=O_j(T^(-j)).                            (7)

To justify all derivative orders in (7), use the analytic digamma
expansion on disks of radius kappa T about 1/2+iz and 1/2-iz,
with small fixed kappa. These disks stay inside closed sectors
avoiding the gamma poles and the negative real axis. The analytic
O(1/T) digamma remainder and its jth derivatives are O_j(T^(-j-1))
by Cauchy's estimates; derivatives of the logarithmic leading term
of positive order are O_j(T^(-j)). The linear combinations defining
theta' have the same bounds. This is an all-fixed-orders use of
the sector expansion, not differentiation of a real-axis error.

Write E=log Phi using its displayed analytic exponent, and give
the four terms signs epsilon=(1,1,-1,-1). Since sum epsilon_j=0,

    partial_t^j E
      = i sum_(r=1)^4 epsilon_r (b_r/L)
                   integral_0^1 theta^(j+1)(t+s b_r/L) ds.

For j=0 this is O(1); for j>=1 it is O_j(T^(-j)/L).
The repeated product rule for exp E therefore yields

    |Phi|<=C,    |partial_t^j Phi|<=C_j T^(-j), j>=1.       (8)

Constants are uniform in T,X,b. Leibniz's rule now shows that
v_b(t)=w_XT(t)Phi(t,b) is supported in [T,3T] and has the source
weight derivative bounds with T0=T.

The source states its theorem for nonnegative weights. Here is
the necessary uniform extension, without assuming it for complex
weights. Fix a real C greater than the bound for |Phi| in (8).
All four smooth weights

    w_XT(C+Re Phi),  w_XT(C-Re Phi),
    w_XT(C+Im Phi),  w_XT(C-Im Phi)

are nonnegative and have uniform derivative bounds of every fixed
order. They extend smoothly by zero outside the phase neighborhood,
since w has compact support in (0,1). Half the difference of the
first pair, plus i/2 times the difference of the second pair, equals
v_b. Apply the source theorem to each weight and use its linearity.
Its four absolute error bounds
give the same order of error, with a uniform enlarged constant.
Although this decomposition is not holomorphic in b, it proves a
uniform bound at every complex b. Holomorphy of the resulting total
error will be proved separately before differentiation.

Take eta=1/100 in Hughes--Young. Each reduced twist obeys

    hk=mn/g_mn^2<=N^2<=T^(1/50)<T^(2/11-1/100).

The strict exponent margin is 167/1100. Also
T^(1/2+1/100)<<T0=T<<T, and q(b)=O(1/L). The theorem therefore
applies uniformly and, by (4), gives

    integral w_XT(t)(h/k)^(-it) product_j Z(t+bj/L) dt
       = T L^4 H_hk(b) + O_w(T^(3/4+1/100)(hk)^(7/8)).    (9)

The factor (hk)^(-1/2) is part of H_hk, not the error. In
particular, no growing amplifier is multiplied into a frozen-phase
O(1/L) remainder. The phase is retained inside the source weight.

### 3. Holomorphy, gcd multiplicities and Cauchy costs

The actual integral in (9) is holomorphic on a neighborhood of
the fixed closed shift polydisc: the t support is compact, the
shifted Hardy factors are holomorphic there, and on each compact
shift set their integrands and derivatives have an integrable
bound. For the main expression use the imported complete-sum
holomorphy. The arithmetic factors introduce no additional poles
in this domain. One direct check is the elementary local identity

    D_p(q)=(1-p^(-2-alpha-beta-gamma-delta))
       /[(1-p^(-1-alpha-gamma))(1-p^(-1-alpha-delta))
         (1-p^(-1-beta-gamma))(1-p^(-1-beta-delta))].        (10)

Indeed, write sigma_(alpha,beta)(p^j) as
(x^(j+1)-y^(j+1))/(x-y), with x=p^(-alpha), y=p^(-beta),
and write the analogous expression with u=p^(-gamma),v=p^(-delta).
Multiplication and summation of the four geometric series gives
(10); equality when x=y or u=v follows by analytic continuation.
The original series converge locally uniformly since the shifts
are O(1/L). For sufficiently large T the real parts of all four
denominator exponents in (10) and the numerator exponent are
strictly positive, so D_p has no zero or pole. Explicitly, on
|b_j|<=2 their real parts are at least 1-4/L and 2-8/L,
respectively; the same estimates hold for all six permuted tuples.
Also Re(2+alpha+beta+gamma+delta)>1 for large T, so the
reciprocal zeta factor in J is holomorphic by the absolutely
convergent Euler product. The incremented series also converge
locally uniformly for each finite exponent e.
This verifies the needed local analyticity for all primes dividing hk;
no uniform magnitude bound on B_hk is asserted or needed here.

Integrating Phi times the complete sum preserves holomorphy. It
follows that the error in (9), and any finite coefficient sum of
such errors, is holomorphic, despite the weight decomposition.
At collisions neither an isolated pole term nor its derivative
is evaluated. This use of holomorphy is part of the named import.

Expand the amplifier exactly:

    |M(t)|^2=sum_(m,n<=N) a_m conjugate(a_n)(m/n)^(-it).

Every pair is retained, including the N diagonal pairs reducing
to h=k=1. Applying (9), summing the errors absolutely, and using
finite Cauchy--Schwarz yields

    sum_(m,n<=N)|a_m a_n| (mn/g_mn^2)^(7/8)
      <= (sum_(n<=N)|a_n| n^(7/8))^2
      <= sum_(n<=N)n^(7/4) <= N^(11/4).

Thus on |bj|<=2 the normalized holomorphic error has supremum
at most

    C_w T^(-1/4+1/100) N^(11/4)/L^4
       <= C_w T^(-17/80)/L^4,                             (11)

because 3/4+1/100+11/400=63/80. This rechecks the elementary
coefficient accounting rather than importing L620's unaudited
summed application. It uses no coefficient-growth hypothesis on
sqrt(n)a_n.

The vectors a,c are fixed while differentiating in b, even if they
depend on T,X. Apply Q V_c at b=0. Cauchy's formula on the four
unit circles costs 1+1+1=3 for Q: the two factorials 2! cancel the factors
1/2. The cost for V_c is (|c0|+|c1|)^2<=2. Hence at most
six times the bound in (11) is lost. Exactly,

    Q V_c [ integral w_XT |M|^2 product_j Z(t+bj/L) dt
                                                 /(T L^4)]_(b=0)
      = integral w_XT |M|^2 (Z'^2-ZZ'') U_c^2 dt/(T L^6).

The powers L^(-1) from all ordinary derivatives are accounted
for in this identity. In particular Q contributes L^(-2),
while V_c gives precisely the already normalized observer.
No derivative is applied to an error known only for real shifts.

### 4. Curvature and the actual signed error threshold

L471 gives, including at real zeros of any multiplicity,

    W=Z'^2-ZZ''-(log A)'' Z^2,
    |(log A)''(t)|<=C T^(-2) on [T,3T].

The curvature bound includes the polynomial prefactor in A and
the paired-gamma cancellation from L465. The used H=T case of
L619 supplies

    integral w_XT Z^2 U_c^2 dt <= C_w T L^4

uniformly in the real unit observer. More explicitly, its holomorphic
comparison and unit-circle Cauchy bounds give both
integral w_XT Z^4=O_w(T L^4) and
integral w_XT Z^2(Z'/L)^2=O_w(T L^4). The pointwise inequality
U_c^2<=2c0^2 Z^2+2c1^2(Z'/L)^2 proves the displayed estimate,
using c0^2+c1^2=1. Also |M(t)|^2<=N by finite
Cauchy--Schwarz. Consequently the absolute curvature cost, divided
by T L^6, is at most

    C_w N/(T^2 L^2) <= C_w T^(-199/100)/L^2.               (12)

This coarse amplifier bound is harmless for the T^(-2) curvature
cost; it was not used to multiply a logarithmic phase error.
Take the real part of the main expression as in (6) and combine
(11) after extraction with (12). This proves (1).

The full absolute costs before normalization are bounded by
C_w T^(63/80)L^2 for the differentiated source error and
C_w T^(-99/100)L^4 for curvature. There is no other discarded
term. All six source main terms, prime-power factors, phase
increments, gcd multiplicities and conjugate orientations remain
in K_c. These estimates do not give a numerical value for C_w.

In particular a negative main direction must be separated below
zero by more than this complete absolute error. A positive lower
bound for every K_c must exceed it uniformly to stop this family.
A sufficient asymptotic comparison would be a bound of one sign
with magnitude at least d_w T^(-beta), d_w>0, beta<17/80.
No such signed bound is established here.

### Separate conceptual audit of (1) — 1 November 2026

The independent replay covered Sections 1–4 for exactly the stated
coefficient, window and common-observer family. The primary source
(11), (14), (16)–(17) and its printed p. 5 holomorphy remark were
matched to (3)–(4) and (9): the h side increments the negative-height
divisor function, the k side increments the positive-height one,
and all six permutations retain h,k in that order. The factor
(hk)^(-1/2) belongs only to the main term. In (5) the transposition
is necessary: if G_(m,n)=J_(m/g,n/g), then the unsymmetrized
ordinary quadratic-form matrix is G^T, and
K=(G^T+conjugate(G))/2. This gives (6) for every complex a,
not just real coefficients.

The analytic phase has uniformly bounded exponent and all fixed
t-derivative bounds in (7)–(8). The four nonnegative weights have
one set of derivative bounds, so the source error constant is uniform
in b,X and the reduced twist. The same arguments hold on a slightly
larger fixed polydisc, giving an open neighborhood of the Cauchy
contours. The total remainder is holomorphic as the difference of
the actual integral and the imported complete main sum; it is not
obtained by differentiating the nonholomorphic weight decomposition.
The explicit denominators above exclude additional arithmetic poles.

The finite gcd sum retains every original pair, including all diagonal
coefficients, and has bound N^(11/4) without an extra N factor.
The total Cauchy cost is at most 6. Replaying the normalization gives
raw errors O_w(T^(63/80)L^2) and O_w(T^(-99/100)L^4), hence exactly
the two powers asserted in (1) after division by T L^6. The L619
H=T absolute bounds, the direct product identity in L471 (7), and
L465 Sections 1–2 and 5 justify completion on the whole [T,3T],
including all real zeros. No logarithm of Xi or Z is used.

No bound, hypothesis or exponent required correction; the added
domain and normalization details make the audit explicit. This is
verification of a local specialization, not new mathematics beyond
the named sources. Their divisor estimates and complete-sum
holomorphy remain imports, not independently audited manuscript
proofs. Section 5, any signed spectral margin, effective constants
and pointwise initial signs remain outside this audit.

### 5. Bounded spectral test: why unscaled diagonal dominance fails

This last calculation concerns only fixed h,k as T tends to
infinity; it is not a leading approximation for growing h,k.
For fixed coprime h,k, source (14) and analyticity give
B_hk(q(b))=B_hk(0)+O_(h,k)(1/L), on every fixed shift polydisc.
All six permutations have the same value at zero. On separated
circles, for example |bj|=3,4,5,6, the four zeta pole factors
each have their uniform Laurent expansion. The exact phase is
exp(i(b1+b2-b3-b4)/2)(1+O(1/L)), uniformly in X. Thus the
L619 six-term germ calculation applies multiplied by

    kappa_hk=B_hk(0)/sqrt(hk).

Both complete expressions are holomorphic; the successive maximum
principle extends the O_(h,k,w)(1/L) normalized error to the inner
polydisc. The fixed Q V_c extraction then gives

    J_hk(c)=kappa_hk B(c)+O_(h,k,w)(1/L),
    B(c)=(28 c0^2+c1^2)/(840 pi^2),                        (13)

uniformly in the real unit c and in X. The enlarged fixed shift
circles remain within the same source hypotheses; the phase bounds
in Section 2 hold on any fixed bounded polydisc. This phase
approximation is used only for these finitely many entries, not
in (1) or through the growing coefficient sum.

At zero shifts sigma_(0,0)(p^j)=j+1. Put x=1/p. The denominator
local sum is (1+x)/(1-x)^3, and its increment-e numerator is
that denominator plus e/(1-x)^2. Hence

    kappa_hk=product_(p^e||hk)
           p^(-e/2) [1+e(p-1)/(p+1)].                    (14)

In particular, put r=2sqrt(2)/3 and s=sqrt(3)/2. On the index
set {1,2,3}, (13)–(14) give

    K_c/B(c) --> G = [ 1  r   s  ]
                    [ r  1   rs ]
                    [ s  rs  1  ],                       (15)

uniformly in c,X, since B(c)>=1/(840 pi^2). Now r+s>1, so
(K_c)_(1,1)-|(K_c)_(1,2)|-|(K_c)_(1,3)| is eventually
negative, uniformly in c,X. Adding the other absolute row entries
cannot increase it. Since N>=3 eventually, this proves (2).

For clarity the leading block G itself is positive definite:

    x^*G x=|x1+r x2+s x3|^2+(1-r^2)|x2|^2+(1-s^2)|x3|^2,
    1-r^2=1/9,   1-s^2=1/4,   det G=1/36.

Thus the negative row-sum lower bound is not a negative spectral
witness. Nor does positivity of this fixed block control the
growing matrix. The first unresolved quantity after the transfer
is the smallest eigenvalue of the full K_c, uniformly over c and
X, compared with (1). A refined attempt needs a representation
or inequality preserving collective arithmetic correlations;
repeating the unscaled row test, freezing the phase through the
amplifier, or enlarging a floating matrix will not settle it.

## Mathlib

Full matching coverage for Hughes--Young's twisted shifted moment,
its collision holomorphy, and this exact-phase coefficient-uniform
Xi transfer has not been checked and is unknown. The elementary
finite sums, Cauchy estimates, complex-weight decomposition and
fixed-block factorization above are informal proofs, not Lean
certificates. No numerical spectral computation is used as proof.
