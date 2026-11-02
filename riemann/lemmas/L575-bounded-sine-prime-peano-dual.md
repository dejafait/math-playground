# Lemma 575: bounded sine prime Peano dual for the complete residual

## Hypotheses

Use L477's actual-theta residual R=U+V on [T,2T], for arbitrary
sufficiently large real T, with L=log T, h=1/L and the fixed integer
M=floor(sqrt(T/(2pi))). Use C481a and L574 with exactly

    J=[T+h,2T-h], F(t)=|sum_(n<=M)n^(-1/2-it)|^2,
    D(t)=F(t+h)-2F(t)+F(t-h),
    Q(t)=F(t+h)+2F(t)+F(t-h)+L,
    B(t)=sum_(T^(1/16)<p<=T^(1/8), p prime)p^(-1/2-it),
    P(t)=-Re B(t), K(u)=(h-|u|)_+.

In particular U=-F'', and all pairs in

    V(x)=sum_(n,m<=M) a_nm cos(2theta(x)-x log(nm)),
    a_nm=log(n/m)^2/sqrt(nm)

are ordered. The diagonal coefficients vanish. Retain L316 (7)'s
uniform actual phase expansion and its logarithm convention. No RH,
independent phases, disjoint prime supports, moving cutoff, omitted
stationary terms or conjectural cancellation is assumed.

Import the arbitrary-coefficient finite mean-square and real-endpoint
Mertens theorems through L574. Import Gonek's endpoint-uniform
logarithmic stationary-phase lemma as stated below. These source proofs
are not independently audited here. The invocation-start EXPLORE
assessment is drafts/literature/2026-10-31-bounded-sine-prime-peano-dual.md,
whose COVERED_TARGET is the first-order implementation proved here.

## Conclusion

There exist fixed epsilon,a>0 and an existential T_0 such that every
real T>=T_0 satisfies, with b(t)=sin(epsilon P(t)) and

    psi(x)=-h^(-2) integral_J K(x-t)b(t)dt,

both approved budgets

    integral_J D(t)b(t)dt >= a T L,                         (1)
    |integral_T^(2T) V(x)psi(x)dx| <= (a/2)T L^3.           (2)

The real multiplier has support [T,2T], |psi|<=1, and exactly

    integral_T^(2T) U(x)psi(x)dx
                     =L^2 integral_J D(t)b(t)dt.           (3)

Consequently

    integral_T^(2T)|R(x)|dx >= (a/2)T L^3,
    E(T)>= (a/4)T L^3                                     (4)

eventually, where E is precisely L477's fixed-square absolute defect.
Thus that particular little-o fixed-square defect route fails. This
says nothing about a different square, negative-mass saving, a Xi sign,
or RH. Its local specialization is critically audited in Section 7, with
the named analytic theorems imported; it is not an RH candidate. The checked
sources did not supply this exact specialization; originality beyond
those sources is not certified. Constants and onset are not numerical.

## Proof

### 1. Imported finite tools and two positive constants

Use L574 (7)--(8), importing Michael J. Curran, *Correlations of the
Riemann zeta function*, arXiv:2303.10123v2 (15 May 2024),
[Section 2, Lemma 2.3](https://arxiv.org/html/2303.10123v2#S2).
For fixed finite coefficients supported on n<=N the interval-translated
mean-square formula on J is

    integral_J |sum c_n n^(-it)|^2 dt
                  =|J| sum |c_n|^2+O(N sum |c_n|^2).       (5)

On [T,2T] it has T in place of |J|. Constants are uniform in the
coefficients, including their dependence on T and on bounded shifts.
Equal products must be grouped before computing the squared coefficient
norm. No variable coefficient vector is inserted into (5).

Use Mertens' second theorem with the precise real-endpoint version in
Mark B. Villarino, *Mertens' Proof of Mertens' Theorem*,
math/0504289v3 (17 May 2005),
[Theorem 6, printed p. 7, (2.3.4)--(2.3.5)](https://arxiv.org/pdf/math/0504289v3#page=7),
already imported in L574. Put x_0=T^(1/16), y=T^(1/8), and S=sum_p 1/p
on the entire block x_0<p<=y. Then S=log 2+O(1/L)<=1 eventually.
For k=2,3 finite partial summation of A(z)=sum_(p<=z)1/p gives

    sum_(x_0<p<=y)(log p)^k/p
       =L^k ((1/8)^k-(1/16)^k)/k+O(L^(k-1)).              (6)

Indeed the exact endpoint formula is f(y)A(y)-f(x_0)A(x_0)
minus integral_(x_0)^y A(z)f'(z)dz, with f(z)=(log z)^k.
The constant part of A cancels; its log log z part integrates f(z)
against dz/(z log z). Its O(1/log z) error contributes O(L^(k-1))
in the two endpoints and the integral. This retains primes at both
real endpoints with the strict/weak conventions stated above.

Let J_0=integral_J D P. L574 (2) supplies exactly

    J_0=4|J| sum_p sin(log p/(2L))^2 H_floor(M/p)/p
                                                   +O(T^(5/8)L). (7)

We need a sharper lower constant than L574's convenient c_1.
For 0<=z<=1/16, Taylor's theorem gives sin z>=z-z^3/6, whence
sin(z)^2>=(99/100)z^2. Also M>=sqrt(T/(2pi))/2 eventually, so
H_floor(M/p)>=log(M/p)>=(3/8)L-C for an absolute C. Applying
(6) with k=2 to (7) therefore yields

    liminf_(T->infinity) J_0/(T L) >= 891/409600 > 1/512.

All inequalities hold at floor and prime-block transitions. Set

    A=1/512.  Then J_0>=A T L eventually.                  (8)

### 2. Complete grouped moments for both cubic remainders

This section establishes constants C_D,C_V>0 independent of T such that

    integral_J Q(t)|B(t)|^3 dt <= C_D T L,                 (9)
    sup_(|u|<=h) integral_T^(2T)|V(x)||B(x-u)|^3 dx
                                             <= C_V T L^3. (10)

Here and below unspecified constants are fixed, finite and independent
of all sufficiently large real T. No smallness is claimed for them.

Write A_sigma(t)=sum_(n<=M)n^(-1/2-i sigma-it), sigma=-h,0,h.
The product A_sigma B^3 has support at integers k<=M y^3<=T^(7/8).
Every such integer has fewer than 14 block prime factors counted with
multiplicity, since each is >T^(1/16). Its number r(k) of ordered
representations k=n p_1 p_2 p_3 with n<=M is at most 14^3. This upper
bound includes repeated primes and all equal products. After grouping,
Cauchy--Schwarz for the r(k) summands gives

    ||A_sigma B^3||_coeff^2
        <=14^3 sum_(n<=M,p_1,p_2,p_3)1/(n p_1 p_2 p_3)
        =14^3 H_M S^3 <=14^3 L.                          (11)

There is no restriction excluding block primes from n. Applying (5),
with the actual product length T^(7/8), proves
integral_J |A_sigma|^2 |B|^6<=C T L. Likewise integral_J |A_sigma|^2
<=C T L. Weighted Cauchy--Schwarz gives
integral_J |A_sigma|^2 |B|^3<=C T L. For B^3 alone the same grouping
has length y^3 and squared coefficient norm <=14^3 S^3, so
integral_J |B|^6<=C T. Consequently integral_J |B|^3<=C T.
Adding the three densities with weights 1,2,1 and the additive L
in Q proves (9). These are actual-density weighted estimates, not
unweighted prime moments substituted for them.

For (10), denote L477's finite jets by

    P_j(x)=sum_(n<=M)(lambda(x)-log n)^j n^(-1/2-ix),
    lambda(x)=log(x/(2pi))/2, j=0,1,2.

To handle variable lambda correctly define fixed-coefficient polynomials

    E_r(x)=sum_(n<=M)(L/2-log n)^r n^(-1/2-ix), r<=2,
    q(x)=lambda(x)-L/2.

Here q is bounded on [T,2T] by an absolute constant, and
P_j=sum_(r=0)^j binomial(j,r) q(x)^(j-r) E_r(x). Thus
|P_j(x)|^2<=C_j sum_(r<=j)|E_r(x)|^2. The grouped coefficients of
E_r(x) B(x-u)^3 have precisely the same representations as (11).
The factors p_i^(iu) have modulus one, and
0<=L/2-log n<=L/2. Their length is <=T^(7/8) and squared norm
<=14^3 L^(2r) H_M S^3<=14^3 L^(2r+1), uniformly for every real u.
Apply (5) on [T,2T] to these fixed vectors, and also to E_r alone.
The preceding pointwise inequality then gives, uniformly in u,

    integral |P_j|^2<=C_j T L^(2j+1),
    integral |P_j(x)|^2 |B(x-u)|^6 dx<=C_j T L^(2j+1).

Cauchy--Schwarz between these two measures proves

    integral |P_j(x)|^2 |B(x-u)|^3 dx<=C_j T L^(2j+1).     (12)

L477's exact product form gives |V|<=2(|P_0 P_2|+|P_1|^2).
A further weighted Cauchy--Schwarz using (12) for j=0,2 bounds
the first product by C T L^3; j=1 bounds the second. This proves
(10), in fact uniformly for all u. There are no bad sets or discarded
mass. All higher norms used here have been grouped and paid; no
product beyond three block primes is needed.

### 3. The exact linear convolution and all boundary strips

Let psi_P=-h^(-2) integral_J K(x-t)P(t)dt. If the t integral is
extended to the whole line, direct integration of the triangle gives

    phi(x)=sum_p s_p p^(-1/2) cos(x log p),
    s_p=(sin(log p/(2L))/(log p/(2L)))^2, 0<=s_p<=1.        (13)

For x in [T+2h,2T-2h] the extension adds no terms. On the two
remaining strips, total length 4h, the pointwise difference is at
most sum_p p^(-1/2)<=2sqrt(y). C574a (10)'s complete ordered
coefficient bound is sum a_nm<=64M, and hence |V|<=64M. Therefore

    |integral_T^(2T) V(psi_P-phi)|<=512h M sqrt(y).         (14)

This explicitly pays both strips; their pairing is not declared zero.
The bound is o(T L^3), since M sqrt(y)=O(T^(9/16)).

### 4. Complete stationary main term and uniform endpoint errors

L316 (7), taking the imaginary part on the real interval, gives

    2theta(x)=x log(x/(2pi e))-pi/4+O(1/T)

uniformly on [T,2T], with its specified analytic logarithm. Replacing
this phase in the finite V phi integral costs O(M sqrt(y)): the
phase error is O(1/T), the interval length is T, and the full absolute
coefficient sum is <=128 M sqrt(y). This accounts for the full phase
error without differentiating a real big-O term.

Import S. M. Gonek, *Mean values of the Riemann zeta-function and its
derivatives*, Inventiones Mathematicae 75 (1984), 123--141,
[Lemma 2, pp. 129--130](https://sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf#page=7).
Its fixed sigma=1/2 specialization, for every r>0 and large real T,
is

    integral_T^(2T) exp(ix log(x/(r e)))dx
      =sqrt(2pi r) exp(-ir+i pi/4) 1_(T,2T](r)
       +O(1+T/(|T-r|+sqrt(T))
                         +2T/(|2T-r|+sqrt(2T))).          (15)

This is the imported endpoint-uniform theorem, including exterior
saddles and equality at an endpoint. Its primary statement and
central/outer/endpoint proof cases were inspected in the assessment;
its proof and supporting references remain unaudited here.
For a readable precise statement also import William Banks,
*Shifting the ordinates of zeros of the Riemann zeta function*,
[arXiv:2405.11084v1, Lemma 2.8](https://arxiv.org/html/2405.11084v1#S2.SS4),
which attributes the formula to Gonek's Lemmas 2--3. Its hypotheses
are 10a>=b>a>=10, sigma in [1/10,10], m in {0,1}, and positive
saddle parameter. Take a=T, b=2T, sigma=1/2, m=0 and conjugate
its negative-phase formula. The amplitude (x/(2pi))^(sigma-1/2)
is then one, its logarithmic weight is one, and its coefficient is
sqrt(2pi r); its error is exactly the one in (15). This unconditional
auxiliary lemma, rather than Banks's RH-dependent main theorems, is
the input. The original Gonek formula has imperfect OCR in the accessed
copy; no visual verification of that copy is claimed. The readable
Banks statement supplies the exact formula used here.

Expanding cos(f_nm)cos(x log p) retains both signs with coefficient
s_p a_nm/(2sqrt(p)). The plus sign in f_nm+x log p has logarithmic
parameter r=2pi nm/p, and derivative log(x/r)>=log p>=L/16.
Its second derivative is 1/x>0, so finite integration by parts bounds
the entire integral by 2/log p. Indeed the two boundary terms and
the integral of f''/f'^2 together equal at most 2/f'(T).
Its complete coefficient sum is O(M sqrt(y)), so the whole plus
branch is O(M sqrt(y)/L). No rational-frequency main term is omitted.

For the minus sign the parameter is exactly r=2pi nmp. In (15)
the external phase exp(-i pi/4) cancels exp(i pi/4), and
exp(-2pi i nmp)=1. Its real main term is consequently the positive
complete finite sum

    H_T=pi sum_p s_p sum_(n,m<=M, T<2pi nmp<=2T)
                                                  log(n/m)^2. (16)

This includes all repeated products, both orders and all block primes.
There is no arithmetic cancellation in (16). Diagonal coefficients
remain zero. Endpoint choices are exactly those in (15).

Here is a uniform bound for the sum of *all* errors in (15).
Put k=nmp, K_0=floor(M^2 y)<=T^(9/8). Each k has fewer than 18
block prime factors counted with multiplicity. The number of distinct
choices p in the block dividing k is therefore at most 18, and for
each p the ordered pairs n,m number at most d(k/p)<=d(k). Since
|log(n/m)|<=L and s_p<=1, the grouped weight before k^(-1/2)
is <=18 L^2 d(k). For delta=1/16 the elementary divisor inequality

    d(k)<=C_delta k^delta                                 (17)

has a fixed finite constant: for primes q>=2^(1/delta),
alpha+1<=2^alpha<=q^(delta alpha); for each of the finitely many
smaller primes the supremum of (alpha+1)q^(-delta alpha) is finite.
Multiplication over the prime factors proves (17), including k=1.
This short elementary estimate is supplied here because the complete
endpoint sum needs uniform multiplicities, not a prime-only moment.

Thus the total absolute error is at most a fixed constant times

    L^2 sum_(k<=K_0) k^(-1/2+delta)
      [1+T/(|T-2pi k|+sqrt(T))
                         +2T/(|2T-2pi k|+sqrt(2T))].      (18)

The term 1 sums to O(K_0^(1/2+delta)). For either endpoint a=T,2T,
restrict first to a/(4pi)<=k<=a/pi. Here k is comparable to T,
and the spacing 2pi implies, uniformly for real a,

    sum_(a/(4pi)<=k<=a/pi)1/(|a-2pi k|+sqrt(T))<=C log T.

For example partition distances into intervals of length 2pi; each
contains at most two integers and the resulting harmonic sum has
initial denominator sqrt(T). Hence this portion of the endpoint
term is O(T^(1/2+delta) log T). Outside that range
|a-2pi k|>=c(T+k), and splitting at k=T bounds its contribution by

    C T sum_(k<=K_0)k^(-1/2+delta)/(T+k)
                                                <=C T^(1/2+delta).

These bounds include exact endpoint hits and every exterior mode.
With delta=1/16, (18) is

    O(T^(81/128)L^2+T^(9/16)L^3)=o(T L^3).                (19)

Together with (14), the exact-theta cost and the plus branch this proves

    integral_T^(2T) V psi_P=H_T+o(T L^3).                 (20)

All errors are uniform for sufficiently large real T, including cutoff,
prime-block and saddle endpoint transitions. In particular a preview
of stationary terms has not been substituted for their complete sum.

### 5. Upper budget for the surviving stationary mass

Put X=sqrt(T/(2pi)), z=X^2/p. On the range in (16), nm>z and
n,m<=M<=X. Thus |log(n/m)|<=log(M^2/z)<=log p, and necessarily
n>z/M. Eventually z/M>=X/p>=T^(3/8)/sqrt(2pi)>1. For each such n,
the number of allowed m in (z/n,2z/n], even after ignoring m<=M,
is at most z/n+1. Integral comparison gives

    sum_(z/M<n<=M)1/n<=log(M^2/z)+M/z<=log p+M/z.

Thus the number of ordered pairs is at most z log p+2M. This is an
upper bound with every pair counted, not an asymptotic lattice claim.
Using 0<=s_p<=1 in (16) yields

    0<=H_T<=(T/2)sum_p(log p)^3/p+2pi M sum_p(log p)^2.

The second term is O(M y L^2)=O(T^(5/8)L^2). By (6),

    limsup H_T/(T L^3)<=7/24576 < 1/2048=A/4.

The positive gap absorbs all the errors in (20), so eventually

    |integral_T^(2T)V psi_P|<=(A/4)T L^3.                 (21)

Stationary mass survives, but fits this fixed budget. Neither a
little-o assertion for the linear chirp nor independence was used.

### 6. Both weighted Taylor costs and compatible fixed constants

Taylor's theorem with Lagrange remainder at zero, using |sin'''|<=1,
gives |sin z-z|<=|z|^3/6 for every real z. Since |D|<=Q and |P|<=|B|,
(9) and (8) imply

    integral_J D sin(epsilon P)
             >=epsilon J_0-(epsilon^3 C_D/6)T L.          (22)

For the chirp remainder, finite Fubini and positivity of K imply

    |integral V(psi-epsilon psi_P)|
      <=(epsilon^3/6)h^(-2) integral_(-h)^h K(u)
          integral_(t in J)|V(t+u)||B(t)|^3 dt du
      <=(epsilon^3 C_V/6)T L^3.                          (23)

The last inequality follows from (10) after setting x=t+u, enlarging
only the nonnegative inner integral to [T,2T], and using integral K=h^2.
There is no extra h^(-2) loss, unweighted error substitution or removed
boundary mass. All t+u belong to [T,2T].

Choose once and for all any epsilon>0 such that

    epsilon<=1, epsilon^2 C_D/6<=A/4,
                epsilon^2 C_V/6<=A/8.

Such a positive choice exists because both constants are fixed and
finite. Put a=3epsilon A/4. Equation (22) proves (1), and (21),(23)
give (2), since epsilon A/4+epsilon A/8=a/2. These are compatible
fixed constants independent of every sufficiently large real T.

Finally |sin(epsilon P)|<=1 and integral K=h^2 show |psi|<=1;
its support is J+[-h,h]=[T,2T]. All integrands are continuous on the
compact two-variable integration region. C481a's imported Peano
identity says D(t)=-integral K(x-t)U(x)dx. Multiplying by b(t),
using finite Fubini and the minus sign in psi proves exactly (3),
including both boundary strips and normalization h^(-2)=L^2.
Then integral R psi>=a T L^3-(a/2)T L^3. Since |psi|<=1, this
proves the first assertion of (4). L477's error O(T L^(5/2)) is
o(T L^3), which proves its second assertion after enlarging T_0.
No conclusion about negative mass follows from a lower bound on E.

### 7. Independent conceptual audit, 31 October 2026

The audit target was both budgets (1)--(2), for the entire prime block,
full J and arbitrary sufficiently large real T. The saved assessment
`drafts/literature/2026-10-31-l575-independent-audit.md` approved this
specialization. Named source theorems are retained as inputs, not
independently reproved. All six preceding sections were checked; no
mathematical correction to their inequalities was needed. The readable
endpoint citation above makes the source interface explicit. Here are
the load-bearing checks, including the constants and complete sum.

**Moments and shifts.** An integer k<=M y^3<=T^(7/8) has fewer
than 14 prime factors from the block, counted with multiplicity.
Choosing ordered factors p_1,p_2,p_3 among those occurrences gives
at most 14^3 representations, and n is then fixed. Repeated factors
and primes dividing n are included. If c_k is a grouped coefficient,
|c_k|^2<=r(k) times the sum of squared summands gives (11).
For E_r B(x-u)^3 each summand acquires a unit-modulus shift and a
factor bounded by L^r. Thus its squared norm is O(L^(2r+1)),
uniformly in u; its length is unchanged. The mean-square error is
O(T^(7/8)L^(2r+1))=o(T L^(2r+1)). Only fixed vectors enter
that theorem. Bounded q(x) is removed by the finite binomial and
pointwise square inequalities before integration. Weighted
Cauchy--Schwarz consequently bounds the j-th jet's cubic-weighted
square by O(T L^(2j+1)); pairing j=0 and j=2 costs T L^3,
as does j=1 squared. This verifies (9)--(10), including every shift
used in (23), without a variable-coefficient mean-square theorem.

**Signs, phase and all endpoints.** The minus sign in psi_P cancels
P=-Re B. The full triangle transform has integral h^2 and gives
exactly the nonnegative s_p of (13). Its truncated convolution
differs only on two strips of total length 4h, each paid in (14).
The complete ordered coefficient sum 64M in C574a applies here.
L316 (7) gives the constant phase -pi/4 in 2theta; it cancels the
+pi/4 of the positive saddle. At r=2pi nmp the remaining phase is
exp(-2pi i nmp)=1 and the coefficient is

    (log(n/m)^2/(2 sqrt(nmp))) sqrt(2pi*2pi nmp)
       =pi log(n/m)^2.

The other branch has r<=T/p and derivative at least log p, hence
no stationary main term. The actual-theta error and both branch
coefficient sums are paid before taking limits.

For the complete minus-branch error, k=nmp<=T^(9/8) has fewer than
18 block prime factors. There are at most 18 choices for p and at
most d(k) ordered pairs for each, so (18) retains every representation.
The fixed delta=1/16 divisor bound applies uniformly. For a=T or 2T,
on a/(4pi)<=k<=a/pi the weight is O(T^(-1/2+delta)).
The distance bins of width 2pi contain a bounded number of integers,
including exact endpoint hits; their reciprocal-denominator sum is
O(1/sqrt(T)+log(1+T/sqrt(T)))=O(L). Multiplication by a
gives O(T^(1/2+delta)L). Outside this range the denominator
is at least c(T+k); the portions k<=T and k>T are each
O(T^(1/2+delta)) by comparison with the two convergent power
integrals at their respective ends. The unweighted part is
O(K_0^(1/2+delta)). Thus the whole error, after the L^2
coefficient factor, has precisely (19)'s exponents 81/128 and 9/16.
Both are strictly below one. This proves a uniform little-o error,
not merely a modewise asymptotic or a preview of the stationary sum.
The indicator convention at either endpoint is harmless only because
these complete error bounds include that endpoint.

**Lattice and fixed margins.** With z=X^2/p and alpha=z/M>1,
the reciprocal sum satisfies

    sum_(alpha<n<=M)1/n<=log(M/alpha)+1/alpha.

Indeed, if the sum is nonempty, separate its first summand, which
is at most 1/alpha; bound all later summands by the integral of
1/x from the first integer to M, then enlarge it to [alpha,M].
There are at most z/n+1 possible m in the open/closed interval
(z/n,2z/n]. Hence the full count is at most
z log(M^2/z)+2M<=z log p+2M. For every such pair,
|log(n/m)|<=log(M^2/z)<=log p. These inequalities hold for
nonintegral alpha and for exact product equalities, with the same
strict lower endpoint as (16). Partial summation (6) therefore
gives the exact limiting upper coefficient

    (1/2)*((1/8)^3-(1/16)^3)/3=7/24576
       <1/2048,
    1/2048-7/24576=5/24576>0.

Independently, the density lower coefficient is

    (99/100)*(3/8)*((1/8)^2-(1/16)^2)/2
       =891/409600>1/512,
    891/409600-1/512=91/409600>0.

Thus the two strict gaps absorb their respective uniform errors
at one existential onset. This does not assert an effective height.

**Signed transfer.** One fixed choice

    0<epsilon<=min(1,sqrt(3A/(2C_D)),sqrt(3A/(4C_V)))

meets both cubic budgets. Equation (22) is at least
(3epsilon A/4)T L, whereas (21),(23) give at most
(3epsilon A/8)T L^3. The constants are compatible without
knowing numerical C_D,C_V. All shifts t+u in (23) remain in
[T,2T]; its nonnegative enlargement and integral K=h^2 remove
the normalization loss exactly. Finally U=-F'', C481a's sign,
and the minus sign in psi give (3) with factor h^(-2)=L^2.
Consequently integral R psi>=(3epsilon A/8)T L^3. Its real
bounded multiplier proves the absolute-norm bound; L477 (4)'s
O(T L^(5/2)) transfer leaves the stated strictly smaller bound
for E(T). No implication for negative W, pointwise signs or RH is
made. This audit validates only the fixed-square route obstruction
conditional on the precisely named standard analytic inputs.

## Mathlib

Full matching theorem and supporting Mathlib coverage are unchecked;
unknown availability is not evidence of absence. Supporting analytic
imports are the precisely cited Curran/Montgomery--Vaughan finite
mean-square formula, Mertens' second theorem, the Gonek/Banks endpoint formula, and
L316's complex-Stirling expansion. C481a carries the de Boor Peano
input with its hypotheses. This proof specializes those inputs using
finite grouping, partial summation, Taylor's theorem and compact Fubini.
Source proofs remain unaudited. Section 7 critically reviews the local
specialization; it does not certify novelty beyond the sources checked.
