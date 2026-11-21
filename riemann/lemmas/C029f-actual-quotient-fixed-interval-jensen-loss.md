# Corollary C029f: actual quotient fixed-interval Jensen loss

## Hypotheses

Use the unchanged actual family of C028d/e/f/g:

    F(u)=sum_(j>=0) b_j u^j/j!,  b_0=1,  b_j>0,
    P_d(x)=sum_(j=0)^d binom(d,j)b_j x^(d-j),
    Q_d(y)=P_d(y-b_1),  f_d(y)=log|Q_d(y)|-d log|y|,
    H_d=sum_(P_d(z)=0)|Im z|.

Integers d>=3 tend to infinity; all roots have their algebraic
multiplicities. Null-set values of f_d may be assigned arbitrarily.
C028d gives f_d in L1(R) and integral_R f_d=pi H_d. With the fixed
M=exp(b_1)F(1)>=1, C028e gives

    |integral_(|y|>Ad) f_d(y)dy|<=8Md/A,  A>=2sqrt(M).

C028f supplies a fixed finite K>=1 such that log F(r)<=K r^(3/4)
for r>=1. C028g supplies H_d/d->S_F<infinity. No value zero for
S_F, RH, real roots, simple roots, or nonvanishing at y=0 is assumed.
For each fixed real A>=max(1,2sqrt(M)), let nu be uniform probability
on [-Ad,Ad] and set

    Z_(d,A)=integral |Q_d(y)/y^d|^(1/(2d)) dnu(y),
    D_(d,A)=4Ad log Z_(d,A)-(1/d)integral_(-Ad)^(Ad) f_d(y)dy.

The moment integrand is defined off zero; any value at zero is harmless.
This is the actual quotient observable of assessment1962, not C029e's
numerator-only comparison.

## Conclusion

The moment Z_(d,A) is finite and strictly positive, its logarithmic
potential is integrable, and D_(d,A)>=0 for every stated d,A. Define
the fixed actual-family constants

    lambda=(1/2)log(1+b_1/2)>0,
    r=exp(-lambda/2)-1+lambda/2>0.

For every fixed allowed A, all sufficiently large d satisfy

    D_(d,A)>=4Ad log(1+r/(2Ad)).                         (1)

Consequently

    liminf_(A->infinity) liminf_(d->infinity) D_(d,A)>=2r>0, (2)
    liminf_(A->infinity) liminf_(d->infinity)
                       4Ad log Z_(d,A)>=2r>0.           (3)

Thus the proposed sufficient upper payment
limsup_A limsup_d 4Ad log Z_(d,A)<=0 is impossible for this fixed
q=1/2 normalization. This is an obstruction to that comparison, not
a positive lower bound for H_d/d and not a disproof of RH. The
signed central integral can still have an unpaid independent estimate.
The result is a known-method specialization; it passed the separate
conceptual audit1965 below under the stated C028d/e/f/g contracts.

## Proof

### Source scope and reason for the application

Assessment1962, saved before this attempt, covers precisely this test.
We import Jensen's inequality for the exponential in its integrable
case: for a probability measure and integrable real T with exp(T)
integrable, exp(E T)<=E exp(T). The inspected classical source is
Cover and Thomas, *Elements of Information Theory*, first edition
(1991), Theorems 2.6.1-2.6.2, printed pp.24-26,
[chapter scan](https://sites.stat.columbia.edu/liam/teaching/neurostat-spr11/papers/EM/Cover%26Thomas-Ch2.pdf).
The actual growth and finite-height statements are imported from
C028f/g with their precise source qualifications; their entire-order,
zero-convergence and summability proofs are not repeated here.

Strict Jensen alone supplies no degree-uniform gap. The specialization
below is necessary to check the singular quotient, moving probability
space, exact factor 4Ad, and the prescribed order of limits. The
elementary exponential remainder retains the mass of one fixed
interval; it does not import an unavailable uniform strictness theorem.
No claim of progress beyond the inspected standard methods is made.

### All singularities and the exact Jensen normalization

Fix d,A. Near y=0 factor Q_d(y)=y^k V(y), where 0<=k<=d and
V(0)!=0. On a sufficiently small punctured real neighborhood,

    |Q_d(y)/y^d|^(1/(2d))
       =|y|^((k-d)/(2d)) |V(y)|^(1/(2d)).

Here (k-d)/(2d)>=-1/2>-1, and V is bounded, so the expression is
locally integrable, including a common numerator/reference zero of
any multiplicity. At any other real root a of multiplicity k, the
denominator stays away from zero locally, and the numerator contributes
|y-a|^(k/(2d)), a nonnegative power. Away from these finite points
the integrand is continuous. Hence its integral on the compact window
is finite. It is strictly positive except at finitely many points,
so Z_(d,A)>0. The potential

    t_d(y)=f_d(y)/(2d)

is integrable by C028d, and the moment integrand equals exp(t_d)
almost everywhere. No L1-to-exponential-integrability implication is
being assumed: the preceding local factorization proved the latter.
Put

    m_(d,A)=E_nu t_d=(1/(4Ad^2))integral_(-Ad)^(Ad) f_d,
    v_(d,A)=t_d-m_(d,A).

Then v is integrable with mean zero and exp(v) is integrable. Jensen
applies with every hypothesis verified. More precisely,

    D_(d,A)=4Ad[log Z_(d,A)-m_(d,A)]
           =4Ad log E_nu exp(v_(d,A)).                    (4)

Jensen proves D>=0, but the quantitative argument below is stronger.

### The full-window mean tends to zero with A fixed

Write T_(d,A)=integral_(|y|>Ad) f_d. The ordinary integrable identity
from C028d, followed by C028e, gives

    integral_(-Ad)^(Ad) f_d=pi H_d-T_(d,A),
    |T_(d,A)|/d<=8M/A.                                  (5)

Since H_d/d->S_F<infinity and H_d>=0, for all sufficiently large d,

    |m_(d,A)|<= [pi(S_F+1)+8M/A]/(4Ad)->0.              (6)

Only an eventual bound is needed; no effective degree onset or
simultaneous uniformity in A is claimed. This step does not assume
S_F=0 or use signs of f_d pointwise.

### A fixed positive-real interval remains below that mean

For 1<=x<=2 and d>=3, positivity of the coefficients and
binom(d,j)=(d)_j/j!<=d^j/j! give

    1<=P_d(x)/x^d
      =sum_(j=0)^d binom(d,j)b_j x^(-j)<=F(d/x).

The argument d/x>=1 permits C028f's growth bound. Therefore, uniformly
on this interval,

    0<=epsilon_d(x):=(1/d)log(P_d(x)/x^d)
        <=K d^(-1/4) x^(-3/4)<=K d^(-1/4).              (7)

There are no zeros of P_d here, since its constant coefficient is
positive and all terms are positive. Translating by precisely the
original b_1, with y=x+b_1>0, gives

    t_d(x+b_1)=(1/2)log(x/(x+b_1))+epsilon_d(x)/2
              <=-lambda+(K/2)d^(-1/4).                 (8)

Indeed log(x/(x+b_1)) is increasing in x>0 and is largest at x=2.
For sufficiently large d the last error is <=lambda/4. Equation (6)
also gives |m_(d,A)|<=lambda/4 for sufficiently large d at each fixed
A. The fixed interval I=[b_1+1,b_1+2] lies inside [-Ad,Ad] for all
sufficiently large d. On all of I at those degrees,

    v_(d,A)<=-3lambda/4+lambda/4=-lambda/2.              (9)

No statement about the sign of t_d on the complement has been made.

### Nonnegative remainder and both limits

For real v let R(v)=exp(v)-1-v. Convexity of the exponential gives
R(v)>=0 everywhere, and R'(v)=exp(v)-1<0 for v<0. Hence (9) gives
R(v_(d,A))>=R(-lambda/2)=r>0 on I. Strict positivity follows from
strict convexity at the nonzero point -lambda/2. Since exp(v) and
v are integrable, R(v) is integrable, and E v=0 yields the exact identity

    E_nu exp(v)=1+E_nu R(v)
       >=1+r nu(I)=1+r/(2Ad).                           (10)

Only the nonnegative remainder is restricted to I. In particular no
signed contribution on the complement is discarded. Equations
(4) and (10) prove (1). For each fixed A, elementary real calculus
gives 4Ad log(1+r/(2Ad))->2r. Thus liminf_d D_(d,A)>=2r for
every allowed A, and taking the outer liminf proves (2). This uses
the degree limit first and no interchange of a limit and an integral.

Finally (5) and H_d>=0 imply, at every degree,

    (1/d)integral_(-Ad)^(Ad) f_d>=-8M/A.

Adding this inequality to (1) and using the definition of D gives

    liminf_(d->infinity)4Ad log Z_(d,A)>=2r-8M/A.

Taking the outer liminf proves (3). A fortiori the proposed ordered
limsup upper threshold cannot be <=0. The argument would remain
consistent with H_d/d->0: the positive cost comes from the exponential
comparison, not from an established nonreal root. Neither alternate
shrinking-q choices nor a direct signed-log upper estimate is analyzed.

### Separate conceptual audit1965 (2026-11-20)

The full proof was independently replayed under unchanged SPECIALIZE
assessment1963, approved in1964. Equations (1)-(3) pass without a
correction, stronger conclusion or new mathematical dependency. The
four direct input contracts were checked against their canonical
statements and existing audits: C028d supplies the ordinary L1 identity,
C028e the degree-uniform exterior bound, C028f the actual positive-series
growth bound, and C028g the finite height limit. Multiplication of R_d
by the positive constant 1/gamma_0 and the real shift by b_1 preserve
the height and all multiplicities. The upstream Xi proofs are not
recertified by this local audit. In particular no conditional
hyperbolicity theorem is imported.

At the origin, factorization with every k in {0,...,d} gives exactly
the power (k-d)/(2d), which is at least -1/2. The analytic factor is
bounded on a small closed neighborhood; this proves local moment
integrability independently of the logarithmic L1 input. At every
other real root the power is k/(2d)>=0 and the denominator is bounded
away from zero. Complex roots produce no additional real singularity;
endpoint roots obey the same one-sided bounds. The monic polynomial
is nonzero, so the integrand is positive almost everywhere. All null-set
choices can therefore be made finite without changing either integral.
This validates both Z>0 and the uses of log Z and exp(v).

The interval probability density is exactly 1/(2Ad). Dividing f_d
by 2d consequently gives mean integral f_d/(4Ad^2), and multiplying
log Z-m by 4Ad subtracts integral f_d/d, exactly as in (4).
For fixed A, the full-line identity and the exterior absolute bound
give |integral_central f_d|<=pi H_d+8Md/A. The finite limit H_d/d
then proves (6), with S_F+1 as an eventual bound. This is an absolute
mean estimate, not an assumed upper sign or a claim that S_F=0.

For x in [1,2], positivity and (d)_j<=d^j bound the finite series
by F(d/x), including the j=0 term. Since d>=3, the growth estimate
is applied within its domain r>=1. Division by d leaves precisely
K d^(-1/4)x^(-3/4). The real logarithm is legitimate because P_d(x)>0.
The translation uses y=x+b_1, not x-b_1; monotonicity of
log(x/(x+b_1)) makes x=2 the upper endpoint and yields the stated
lambda. The growth error and the absolute mean can each be made
at most lambda/4, while the fixed interval fits inside [-Ad,Ad].
All three conditions can be imposed at one degree onset for this
fixed A. Uniformity of that onset in A is neither used nor proved.

The sign check in (10) concerns R(v)=exp(v)-1-v only. It is
nonnegative on the entire probability space and decreasing on the
negative half-line, so v<=-lambda/2 implies R(v)>=r on the fixed
interval. Its integrability follows from that of exp(v), v and 1.
The identity E exp(v)=1+E R(v) uses the zero mean exactly; it loses
no potentially negative complement. The length-one interval has mass
1/(2Ad). Thus (1) has exactly the stated factor and, at fixed A,
its right side tends to 2r, not to zero. Strict convexity gives r>0
because b_1>0. The same constant is independent of A, permitting the
outer liminf without exchanging any limits or integrals.

Finally the central signed integral divided by d is bounded below
by -8M/A because H_d>=0. Adding this bound to (1), taking d first,
and then A proves (3). Each inner limsup dominates the corresponding
liminf, so the proposed ordered limsup upper threshold <=0 is indeed
excluded. The proof does not subtract the two lower bounds to infer
a positive height. It remains valid if S_F=0; the excess is a cost
of this comparison. The local audit therefore accepts the fixed-q
payment stop only. It does not settle the central signed estimate,
other observables or RH, and claims no new theorem beyond this
checked specialization of the cited methods.

## Mathlib

Not checked. Full matching coverage for this actual-family ordered-limit
quotient obstruction is unknown. Standard convexity, integrability and
finite polynomial factorization are supporting inputs, not a claimed
formalization of the full result. No absence or formal verification is
claimed. Audit1965 validates the informal specialization under its input
contracts; it adds no formal coverage. The RH-equivalent gap is unchanged.
