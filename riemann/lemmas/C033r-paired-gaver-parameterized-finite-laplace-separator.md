# Corollary C033r: a parameterized paired-Gaver finite Laplace separator

## Hypotheses

Retain the exact laws, signed remainders and external qualifications of
C033i/j/l/p/q. The positive-ordinate nontrivial zeta divisor counts
multiplicity, z_rho=gamma_rho-i*(beta_rho-1/2), with conjugate pairing,
excluded ordinate zero, |beta_rho-1/2|<1/2, gamma_rho>14,
N(T)=O(T log(T+2)), the verified real zeros through height 100,
the retained real zero in (14,15), reciprocal-square tail, heat
positivity and separate fixed-j heat errors through j=2. Both fixed-v1
preprints and finite-zero data remain qualified external inputs, not
independently certified here. Sigma is Gaussian half-variance.

On X=[0,infinity), W=[1,2], retain C033l's probabilities nu_sigma,
their transforms k_sigma(s)=exp(-B_sigma(s)), and the real signed
mixtures nu_eta for

    A_2={eta real finite signed Borel on W:
                      eta(W)=1, |eta|(W)<=2}.

All atoms, singular parts and infinite support of eta are allowed.
C033j supplies, on every Borel set,

    nu_sigma=nu_1*R_sigma,
    R_sigma=exp(-M_sigma)*delta_0+r_sigma(t)dt,
    R_eta=integral_W R_sigma deta,  nu_eta=nu_1*R_eta.

Set I_0=[3/4,5/4]. Fix finite nonnegative constants B,L,V satisfying

    |r_sigma(t)|<=B,  |r_sigma(t)-r_sigma(u)|<=L*|t-u|,
                          t,u in I_0, sigma in W,
    ||R_sigma||_TV<=V,                    sigma in W.       (1)

C033j provides B,V and C033p provides L; these are generally
nonnumerical. The densities are the specified continuous representatives.

Use exactly C033i's P, the restriction of ell_1(t)dt to [1,3/2], m=P(X)>0,
lambda=exp(m)*sum_(j>=0)(-1)^j P^{*j}/j!, and probability
mu=nu_1*lambda. Write d(s)=exp(-B_1(s))>0, s>0. C033i/j give

    ||lambda||_TV<=V_lambda:=exp(2*m),
    lambda({0})=exp(m),
    lambda(dt)=0                   on (1/2,1),
    lambda(dt)=-g(t)dt              on (1,3/2),
    g(t)=exp(m)*ell_1(t),  J=g(1)>0.                         (2)

The function g is continuous and positive. On J_0=[1,5/4] define

    D=max_(t in J_0) g(t),
    omega(h)=sup{|g(t)-g(u)|: t,u in J_0, |t-u|<=h}, h>=0. (3)

Thus D is finite, omega is nondecreasing and omega(h)->0 as h->0.
No Lipschitz bound across lambda's jump is imposed. No global bounded
density, positivity of R_sigma, moments, full cancellation, bounded
inverse-convolution operator or actual-Xi realization is assumed.

## Conclusion

Choose parameters in this order:

    0<delta<1/8,     omega(delta)+4*L*delta<=J/4;
    rho=delta/2;
    0<tau<=rho,      omega(tau)<=J/8.                       (4)

Such choices exist by (3). Define x_-=1-delta, x_+=1+delta,
a_x=log(2)/x, A=log(2)/(1-delta), and

    h(v)=4*2^(-v)*(1-2^(-v)),
    q=max{h(1-rho/(1+delta)),h(1+rho/(1+delta))}, 0<q<1,
    c_n=(2n)!/[n!*(n-1)!],
    b_n=(1+delta)*sqrt(n+2)/(n*log(2)),
    E_n=L*b_n+B*b_n^2/rho^2+A*V*n*q^n,
    T_n=4*E_n+2*D*b_n^2/tau^2+D*b_n^2/rho^2
                                      +2*A*V_lambda*n*q^n. (5)

After fixing delta and tau, choose any integer n>=1 with T_n<=J/8.
Such a finite n exists. There are 2(n+1) indexed positive nodes
(coincident nodes can be combined): for x=x_-,x_+ and 0<=k<=n put

    s_(x,k)=a_x*(n+k),
    v_(x,k)=epsilon_x*a_x*c_n*(-1)^k*binom(n,k),
    epsilon_(x_-)=1,   epsilon_(x_+)=-1,
    alpha_(x,k)=v_(x,k)/d(s_(x,k)),
    H_n(t)=sum_(x,k) alpha_(x,k)*exp(-s_(x,k)*t).          (6)

This finite bounded real test satisfies, for every eta in A_2,

    integral_X H_n dmu - integral_X H_n dnu_eta
       >= e_n:=J-omega(delta)-4*L*delta-omega(tau)-T_n
       >=J/2>0.                                         (7)

Consequently it is a parameterized witness for C033l's separation
inequality with epsilon=e_n. Its combined coefficient vector is nonzero.
One explicit finite coefficient allowance is

    sum_(x,k) |alpha_(x,k)|<=C_n,
    C_n=2*A*n*8^n*exp(B_1(2*n*A)).                        (8)

In particular H_n/C_n has supremum norm at most one and separation
gap at least J/(2*C_n)>0. This is not a uniform inverse bound.

For completeness, index (x,k) by i. Suppose real numerical data,
with bounded Borel width data, have uniform errors

    |ktilde_i(sigma)-k_sigma(s_i)|<=u_i  (sigma in W),
    |mutilde_i-muhat(s_i)|<=z_i,
    |dtilde_i-d_i|<=kappa_i<d_i,   d_i=d(s_i).

Then the error in the residual-minus-mixture test formed with
v_i/dtilde_i instead of v_i/d_i is, uniformly in eta in A_2, at most

    A_data=sum_i |v_i|*((z_i+2*u_i)/(d_i-kappa_i)
                         +3*kappa_i/[d_i*(d_i-kappa_i)]). (9)

Thus A_data<e_n preserves strict separation for these approximate
expressions. For exact divisors, the allowance reduces to
sum_i |alpha_i|*(z_i+2*u_i). All coefficients and strictly positive
error tolerances are finite after (4)-(5) are fixed. No numerical
values, certified evaluators or feasible runtime are asserted.

This is a local parameterized specialization of the known Gaver
mechanism. It passes the separate conceptual audit1777 below under
the stated qualifications. It is not a complete RH candidate or a claim of certified
originality. Unrestricted variation, moments, cancellation, signed
height estimates and actual-Xi positivity remain unpaid.

## Proof

### Source scope and the additional work

Use SPECIALIZE assessment1773, separately approved1774 before this
attempt, and its source-notes1774. Import the base variable-center
Gaver finite formula and normalized kernel from A. Kuznetsov,
*On the convergence of the Gaver-Stehfest algorithm*, SIAM J. Numer.
Anal. 51(6) (2013), 2984-2998,
[arXiv:1305.0715v2, pp.2-3, (2)-(3)](https://arxiv.org/pdf/1305.0715v2)
(served manuscript header 29 October 2018), and J. Abate and W. Whitt,
*A Unified Framework for Numerically Inverting Laplace Transforms*,
INFORMS J. Computing 18(4) (2006), 408-421,
[p.414, (28)](https://www.columbia.edu/~ww2040/AbateUnified2006.pdf),
DOI 10.1287/ijoc.1050.0137. The exact kernel transform and cumulants
are in D. P. Gaver, Jr., *Observing Stochastic Processes, and Approximate
Transform Inversion*, Operations Research 14(3) (1966), 444-459,
[pp.448-451, (13)-(29), especially (17)-(20)](https://doi.org/10.1287/opre.14.3.444).
Their inspected proof cases are reused through notes1764/1769/1774.
No new source retrieval, accelerated convergence theorem or asymptotic
smooth-function expansion is used.

C033q checks the exact normalization, indexing and second moment for
this base kernel. Its stated two-point conclusion is not applied to
our moving centers. The additional proof below supplies neighborhood
and full-variation bounds at the new centers, separate estimates for
lambda's two sides, integration against signed widths, and finite
division/error accounting. These are the interfaces not supplied by
the cited inversion statements. The measure construction, local
regularity and exact finite-node transform identities are C033i/j/p;
C033l fixes the original laws and whole signed class being separated.

### Kernel estimates at either chosen center

For any x>0 and n>=1 set

    K_(n,x)(t)=a_x*c_n*exp(-n*a_x*t)*(1-exp(-a_x*t))^n.

For every finite real signed measure theta on X, finite binomial
expansion gives

    integral_X K_(n,x) dtheta
      =sum_(k=0)^n a_x*c_n*(-1)^k*binom(n,k)
                                  *thetahat(a_x*(n+k)). (10)

Each exponential is bounded by one and hence integrable against
|theta|; no infinite interchange is needed. Also K_(n,x)(0)=0.
This includes every zero atom exactly for exact samples.

The normalized kernel and moment identities in C033q(8)-(10), before
its final restriction to two x values, hold at every x>0. Explicitly,
its scaled positive density p_n(u)=c_n*exp(-n*u)*(1-exp(-u))^n has
Laplace transform product_(j=n)^(2n) j/(j+z), z>-n, mass one,
mean S_n=sum_(j=n)^(2n)1/j and variance U_n=sum_(j=n)^(2n)1/j^2.
The checked bounds are 0<=S_n-log(2)<=1/n and U_n<=(n+1)/n^2.
Rescaling u=a_x*t therefore gives

    integral_X K_(n,x)(t)dt=1,
    integral_X (t-x)^2*K_(n,x)(t)dt
      =(x/log(2))^2*(U_n+(S_n-log(2))^2)<=b_n^2          (11)

for both x=x_-,x_+, since x<=1+delta. In particular the first
absolute moment is at most b_n by Cauchy-Schwarz. For any r>0,

    integral_(|t-x|>r) K_(n,x)(t)dt<=b_n^2/r^2.         (12)

These are statements about the positive Lebesgue kernel only.

Let I_x=[x-rho,x+rho]. From delta<1/8 and rho=delta/2,
I_(x_-) lies in (3/4,1) and I_(x_+) in (1,5/4).
The function h is increasing for 0<=v<=1 and decreasing for v>=1;
h(v)=1-(2*2^(-v)-1)^2, so h(v)<1 except at v=1.
For t<x-rho,

    t/x<1-rho/x<=1-rho/(1+delta)<1;

for t>x+rho one has t/x>1+rho/x>=1+rho/(1+delta)>1.
Both endpoints defining q are strictly positive, one below and one
above 1; hence 0<q<1 and h(t/x)<=q outside I_x. Since
c_n=n*binom(2n,n)<=n*4^n and a_x<=A, it follows that

    sup_(t outside I_x) K_(n,x)(t)<=A*n*q^n.            (13)

For any finite signed theta this gives the different tail estimate

    |integral_(X\I_x) K_(n,x) dtheta|
                         <=||theta||_TV*A*n*q^n.       (14)

It controls the entire complement, including its unbounded tail and
all atoms, without a global density bound or any moments of theta.
We do not replace (14) by the kernel-probability estimate (12).

### Uniform width-family error and its signed integration

Write G_x(theta)=integral K_(n,x) dtheta. On I_x the measure
R_sigma has density r_sigma and no atom. Adding and subtracting
r_sigma(x)*integral_(I_x)K_(n,x)dt gives

    G_x(R_sigma)-r_sigma(x)
      =integral_(I_x) K_(n,x)(t)*(r_sigma(t)-r_sigma(x))dt
       +r_sigma(x)*(integral_(I_x)K_(n,x)(t)dt-1)
       +integral_(X\I_x)K_(n,x)dR_sigma.                (15)

The three absolute bounds, by (1) and (11)-(14), are L*b_n,
B*b_n^2/rho^2, and A*V*n*q^n. Thus (15) is at most E_n,
uniformly over both centers and all widths.

C033j's bounded-Borel mixture identity applies to K_(n,x), which
is bounded for each fixed n,x. It gives G_x(R_eta)=integral_W
G_x(R_sigma)deta. Fubini on the compact density interval, with bound
B*|eta|(W), likewise gives r_eta(t)=integral_W r_sigma(t)deta.
The error of this mixture at either center is at most 2*E_n.
Also |r_eta(x_-)-r_eta(x_+)|<=|eta|(W)*L*(2*delta)<=4*L*delta.
Consequently, for S_n(theta)=G_(x_-)(theta)-G_(x_+)(theta),

    S_n(R_eta)<=4*L*delta+4*E_n,             eta in A_2. (16)

There is no restriction to positive or atomic eta. In fact this
upper bound uses only its variation cap; its mass condition is
retained to match C033l's exact class.

### Separate residual-side bounds

On I_(x_-), lambda is zero by (2), so (14) gives

    |G_(x_-)(lambda)|<=A*V_lambda*n*q^n.                (17)

On I_(x_+), lambda has density -g. Subtract its value -g(x_+)
as in (15). Within |t-x_+|<=tau the density oscillation is at most
omega(tau). On the rest of I_(x_+) it is at most 2*D. Using (12)
at radius tau bounds the local error by
omega(tau)+2*D*b_n^2/tau^2. The normalization error is at most
D*b_n^2/rho^2 and the full signed tail at most A*V_lambda*n*q^n.
Thus

    |G_(x_+)(lambda)+g(x_+)|
       <=omega(tau)+2*D*b_n^2/tau^2+D*b_n^2/rho^2
                                        +A*V_lambda*n*q^n. (18)

All points used for the modulus are in J_0. No estimate applies
that modulus across 1, and no value assigned to the density at 1
affects an integral. The atom exp(m)*delta_0 is included in the
full-variation tail and has exact kernel value zero by (10).
Higher convolution powers and every distant signed component of
lambda remain included in V_lambda.

Since g(x_+)>=J-omega(delta), subtracting (16) from the lower bound
obtained from (17)-(18) proves

    S_n(lambda)-S_n(R_eta)>=e_n.                        (19)

Uniform continuity on J_0 proves the existence of delta in (4),
since omega(delta)+4*L*delta tends to zero as delta decreases to
zero. Having fixed that delta, choose tau in (4) by the same
continuity. Now q<1, rho and tau are fixed, b_n tends to zero,
and n*q^n tends to zero (its successive ratio tends to q<1).
Every term of T_n therefore tends to zero. A finite n with
T_n<=J/8 exists, and (4) gives e_n>=J-J/4-J/8-J/8=J/2.
This is an ordered finite parameter selection, not a simultaneous
shrinking-center limit or a numerical certificate for those choices.

### Return to the original positive-node transforms

For each of the finitely many s_i>0, C033i/j give the exact equalities

    lambdahat(s_i)=muhat(s_i)/d_i,
    Rhat_sigma(s_i)=k_sigma(s_i)/d_i,
    Rhat_eta(s_i)=nuhat_eta(s_i)/d_i.                   (20)

The convolution transform identities hold for finite signed measures;
d_i is finite and strictly positive. Apply (10) and finite linearity
to (20): the left side of (19) becomes exactly
sum_i alpha_i*(muhat(s_i)-nuhat_eta(s_i)), which is (7).
All integrals of H_n exist because it is a finite sum of bounded
exponentials. Taking the supremum over eta yields C033l's orientation.
The gap is strict, so H_n cannot be identically zero; in particular
merging coincident nodes cannot annihilate the whole coefficient vector.

Every s_i<=2*n*A. Since ell_1 is positive, its nonnegative exponent
integrand proves B_1(s_i)<=B_1(2*n*A)<infinity. The finite binomial
coefficient sums give

    sum_i |v_i|=(a_(x_-)+a_(x_+))*c_n*2^n
                      <=2*A*n*8^n.

Multiplying by exp(B_1(2*n*A)) proves (8). The bound can grow very
rapidly with n; no uniform inverse, stable inversion or usable
runtime follows. Dividing H_n by the positive C_n gives the stated
normalized gap and supremum bound.

### Data and division-factor errors

For any true numerator f with |f|<=1, an approximation ftilde with
|ftilde-f|<=e, and |dtilde-d|<=kappa<d, direct subtraction gives

    |ftilde/dtilde-f/d|
      <= e/(d-kappa)+kappa/[d*(d-kappa)].               (21)

Indeed |dtilde|>=d-kappa>0; write the difference as
(ftilde-f)/dtilde+f*(d-dtilde)/(d*dtilde).
The true numerators muhat(s_i), k_sigma(s_i) lie in [0,1], since
mu and every nu_sigma are probabilities. Apply (21) with error
z_i to muhat, and with uniform error u_i to k_sigma, then integrate
the latter bound against |eta|, of mass at most 2. Multiplication
by |v_i| and finite summation gives exactly (9), including the
factor 3 for the two divisor-error contributions. Correlations
between errors are irrelevant to this absolute bound.

The approximate numerator functions were assumed bounded Borel,
so their signed width integrals exist. For each eta, their resulting
approximate residual-minus-mixture expression differs from the exact
one by at most A_data. Equation (7) therefore leaves a gap at least
e_n-A_data. With finitely many d_i>0 one can first require
kappa_i<=d_i/2 and then choose all tolerances sufficiently small to
make A_data<e_n/2. This proves existence of a finite positive error
allowance, not availability of any such numerical enclosures. The
continuum width errors must still be uniform; a finite width grid
alone would not meet that requirement. No global inverse operator
or positivity of deconvolution is used. This completes the proof.

### Conceptual audit1777 — 19 November 2026

**Verdict.** Equations (4)-(21) pass for the entire real signed
mass-one TV<=2 class. No inequality, constant, parameter order or
mathematical premise requires correction. The numerical-data paragraph
now explicitly says real data, as required to compare approximate
expressions by an ordered inequality; its absolute error estimate
also holds for complex data, in which case the conclusion concerns
their real parts. This clarification does not restrict eta. This is
verification of the existing specialization, not a new bound or an
independent validation of the heat/zero sources.

The unchanged SPECIALIZE assessment1775, separately approved1776,
covers this audit. Source formulas and proof-case evidence are reused
from notes1774. Checked C033i's measure exponential and positive residual,
C033j's full-variation, continuous-density, setwise-mixture and jump
interfaces, C033l's precise class and separation orientation, C033p's
qualified uniform Lipschitz assertion, and C033q's kernel proof.
No upstream heat asymptotic or preprint is re-audited here.

1. **Fixed constants and neighborhoods.** The numbers B,L,V are common
   to all widths before any center or degree is selected. C033j's
   continuous representative makes point evaluation legitimate, with
   no hidden singular part on I_0. C033i/j give the full finite signed
   lambda, its zero atom and its exactly zero and negative-density
   restrictions on the two open sides. Continuity of ell_1 and its
   positive value at 1 give J>0, finite D and a genuine compact modulus
   omega. The closed neighborhoods have endpoints

       I_minus=[1-3*delta/2,1-delta/2],
       I_plus =[1+delta/2,1+3*delta/2].

   Since delta<1/8, they lie respectively in (3/4,1) and
   (1,5/4). Every use of g and its modulus is consequently on J_0;
   neither a density value at the jump nor a modulus across it is used.

2. **Kernel normalization and tails.** The beta-product calculation
   has exactly n+1 factors indexed n,...,2n, and c_n=n*binom(2n,n).
   Its mean is S_n and its variance is U_n; centering at log(2)
   leaves the nonnegative squared bias (S_n-log(2))^2. Thus
   U_n+(S_n-log(2))^2<=(n+2)/n^2, and x<=1+delta gives precisely
   b_n^2 in (11), including n=1. Scaling also preserves unit
   Lebesgue mass. The first absolute moment and the probability
   leakage follow from this unit mass and second moment.
   For t outside I_x, rho/x>=rho/(1+delta). Monotonicity of h
   on its two sides gives h(t/x)<=q<1. Therefore the bound
   A*n*q^n controls the entire complement pointwise. Integrating
   it against |theta| proves (14) without moments or a density
   bound there. The probability leakage (12) is never substituted
   for this signed-measure estimate. The exact atom contribution
   vanishes because n>=1 and K(0)=0, while its mass remains in V
   and V_lambda wherever those bounds are used.

3. **The full signed width class.** In (15) the local oscillation,
   missing Lebesgue normalization and signed complementary measure
   cost, respectively, L*b_n, B*b_n^2/rho^2 and A*V*n*q^n.
   C033j's bounded-Borel mixture identity applies because each
   fixed kernel is bounded. Joint measurability and the local
   bound B justify Fubini against dt times |eta|. Hence each center
   costs at most 2*E_n after mixing. The center difference is at
   most 2*L*(2*delta)=4*L*delta. Taking the upper bound for the
   left-minus-right functional gives (16), with total error 4*E_n.
   No sign, atom, support-size or density hypothesis on eta enters;
   eta(W)=1 is retained but not needed for these estimates.

4. **The residual has two separately paid sides.** Its left local
   integral is identically zero, leaving one full-variation tail.
   At the right center, subtract -g(x_plus). On the inner radius
   tau the error is at most omega(tau) times at most unit kernel
   mass. On the remainder of I_plus it is at most 2*D times
   b_n^2/tau^2. Subtracting the full constant also costs the
   normalization leakage D*b_n^2/rho^2. One further full-variation
   tail completes (18). The left side can be negative, so its
   absolute bound (17) must be subtracted, not discarded. This
   explains both copies of A*V_lambda*n*q^n in T_n. Since the
   right density is negative, left minus right yields +g(x_plus),
   and g(x_plus)>=J-omega(delta) gives exactly (19).

5. **Order and the actual threshold.** First continuity and finite L
   give delta with omega(delta)+4*L*delta<=J/4. Only then fix
   0<tau<=rho with omega(tau)<=J/8. Thus rho,tau and q<1 are
   fixed as n increases. Every term of T_n tends to zero, so some
   finite integer n has T_n<=J/8. The total allowance is at most
   J/4+J/8+J/8=J/2. There is no interchange of a shrinking
   neighborhood with a degree limit and no effective onset claim.

6. **Finite return to the original laws.** All nodes are positive;
   C033i/j's exact convolution identities and d_i>0 permit division
   at each one. Finite summation proves (20)'s use in (7), and
   the uniform bound over eta has C033l's required orientation.
   The class is nonempty (delta_1 belongs to it), so a positive
   gap rules out the zero test even after coincident nodes merge.
   The positive Levy measure makes B_1 nondecreasing and finite
   at each finite positive argument. Since s_i<=2*n*A and
   sum_i |v_i|<=(2*A)*n*8^n, (8) follows for the indexed vector;
   merging can only lower this absolute coefficient bound.
   C_n>0 is finite, so normalization gives the claimed supremum
   bound and strictly positive, possibly extremely small, gap.

7. **Every data and divisor error is counted.** For fixed i write
   f_i=muhat(s_i) and g_i(sigma)=k_sigma(s_i). Both lie in [0,1].
   The approximate difference is

       v_i*(ftilde_i-integral gtilde_i deta)/dtilde_i.

   The numerator error is at most z_i+2*u_i, while the true
   numerator has absolute value at most 1+2=3. Subtracting the
   exact quotient and using |dtilde_i|>=d_i-kappa_i>0 gives
   precisely the i-th summand in (9). Thus the factor 3 includes
   the residual and the entire signed mixture, with no presumed
   cancellation of their divisor errors. Summing absolute bounds
   proves the stated uniform allowance. Finitely many positive
   d_i allow kappa_i<=d_i/2 first, then sufficiently small positive
   tolerances with A_data<e_n/2. Uniform Borel width approximants
   are essential; pointwise accuracy or a grid would not suffice.

The audit therefore resolves this construction's pending verification,
not its effectivity. No numerical B,L,V,D,J,omega, nodes, certified
data/divisors or runtime has been supplied. The hypotheses remain
qualified by both fixed-v1 preprints, actual divisor and finite-zero
data, heat positivity and separate fixed-j errors through j=2.
Neither full cancellation nor positive unsmoothed Xi realization
follows. The direct mathematical uses remain exactly the C033r row
already in DAG.md; there is no new node or dependency.

## Mathlib

Full matching coverage for this signed paired-Gaver separator has
not been checked and is unknown. Supporting finite signed integration,
uniform continuity on compact intervals, binomial identities and
kernel moment APIs have not been separately assessed here. No formal
verification of this proof, either fixed-v1 preprint, or finite-zero
data is claimed. Conceptual audit1777 is informal verification of this
local construction under its stated qualifications, not formal coverage.
