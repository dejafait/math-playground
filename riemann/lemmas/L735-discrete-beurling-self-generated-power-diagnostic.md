# Lemma 735: a discrete Beurling power defect with its own coarse kernel bound

## Hypotheses

Set b=3/4. Use the continuous-template case of F. Broucke and J. Vindas,
*A new generalized prime random approximation procedure and some of its
applications*, Math. Z. 307 (2024), Article 62,
[arXiv:2102.08478v2](https://arxiv.org/pdf/2102.08478v2), Theorem 1.2,
printed p. 2. Its hypotheses on F:[1,infinity)->R are: nondecreasing,
right-continuous, unbounded, F(1)=0 and F(x)<<x/log x. If F is
continuous, its conclusion includes strictly increasing primes
1<p_1<p_2<... tending to infinity with

    |pi_P(x)-F(x)|<=1                 for every real x>=1.       (1)

Only this conclusion is used; the theorem's simultaneous Fourier
estimate is not needed. The source's continuous-construction proof
case is Section 2, printed pp. 4–6. The construction is imported,
not reproved.

The generalized integers are the free commutative semigroup on the
prime indices. An element g is a finitely supported vector of
nonnegative integers (a_j), with |g|=product_j p_j^(a_j). Distinct
vectors remain distinct even if their norms coincide. Define
Lambda_P(g)=log p_j when g is a positive formal power of generator j,
and Lambda_P(g)=0 otherwise, including the unit. These are the
conventions of Sz. Gy. Revesz, *Oscillation of the remainder term in
the prime number theorem of Beurling, caused by a given zeta-zero*,
[arXiv:2202.01837v3](https://arxiv.org/pdf/2202.01837v3), Section 1,
(1)–(7), printed pp. 1–3. No theorem about the associated integer
counting function or zeta continuation is assumed.

## Conclusion

There exists such a discrete system P for which, at every real x
tending to infinity,

    psi_P(x)=sum_(|g|<=x) Lambda_P(g)
            =x-x^(3/4)+O(sqrt(x) log x)
            =x-x^(3/4)+o(x^(3/4)).                            (2)

In particular the negative power term has coefficient exactly 1.
Put R_P(x)=psi_P(x)-x for x>=1. One constant works at all real x>=1:

    |R_P(x)log x+sum_(|g|<=x) Lambda_P(g)R_P(x/|g|)|<=B x.    (3)

All sums retain multiplicities and include atoms at equality. The
system is locally finite. The implied constants may depend on the
chosen system, and no effective asymptotic onset is asserted.

This is a specialization of a known construction, not a claim of
novelty. It shows that this coarse same-system bound and free-semigroup
arithmetic permit the tested power defect. It makes no assertion about
ordinary primes, an integer-density estimate, a zeta zero, continuation
through b, the full L733 increment envelope, growing prefix energy or
actual-Xi mixed signs. It is not an RH candidate. Independent audit of
this specialization passed on 2026-11-04 (step 253), within precisely
these qualifications.

## Proof

### Template admissibility and the imported construction

Use exactly the approved template

    F(x)=0,                                           1<=x<=2,
    F(x)=integral_2^x (1-b u^(b-1))/log u du,           x>2.    (4)

For u>=2, 0<b u^(b-1)<=b<1. Thus the integrand is positive,
continuous and between (1-b)/log u and 1/log u. Formula (4) is
continuous on [1,infinity), nondecreasing and zero at 1.
For x>=4 its integral over [x/2,x] gives

    F(x)>=(1-b)x/(2 log x)=x/(8 log x),

so F is unbounded. For the upper bound split the integral at sqrt(x):

    F(x)<=sqrt(x)/log 2+2x/log x,                     x>=4.

The first summand is O(x/log x), since log x/sqrt(x) is bounded
(indeed at most 2/e for x>=1). This verifies the required Chebyshev
upper bound. The initial interval is harmless because F is bounded
there. All hypotheses of Theorem 1.2 therefore hold. Choose a prime
sequence supplied by its continuous case, satisfying (1). No choice
of noninteger zero multiplicities or rescaling of psi is involved.

### Local finiteness and weighted prime counting

Write a=log p_1>0. For any real x>=1 only finitely many generators
have p_j<=x. Every g of norm at most x uses only these generators,
and each exponent is at most floor(log x/a). Consequently only
finitely many such exponent vectors exist. At x=1 the unit is the
only one. This proves local finiteness without identifying colliding
norms or assuming an estimate for their number.

Define theta_P(x)=sum_(p_j<=x) log p_j. Finite summation of
log p_j=log x-integral_(p_j)^x dt/t gives the exact identity

    theta_P(x)=pi_P(x)log x-integral_1^x pi_P(t)dt/t.          (5)

At a prime endpoint its atom is included in the first term and its
integral is zero. Also pi_P(1)=0. Put E(t)=pi_P(t)-F(t), so |E(t)|<=1.
The analogous integration by parts for the continuous F yields,
for x>=2 and c_0=2-2^b>0,

    F(x)log x-integral_1^x F(t)dt/t
      =integral_2^x (1-b t^(b-1))dt
      =x-x^b-c_0.

Subtracting from (5), including the endpoint x=2, gives

    |theta_P(x)-(x-x^b-c_0)|<=2 log x,                 x>=2. (6)

For 1<=y<=2, (1) and F(y)=0 imply pi_P(y)<=1, hence
theta_P(y)<=log y<=y. For y>=2, (6) gives
theta_P(y)<=y+2 log y<=3y. We may therefore use the global bound

    0<=theta_P(y)<=3y,                                y>=1. (7)

### Finite prime-power cutoff and its error

For x>=1 set K(x)=floor(log x/a). Any contributing power p_j^k<=x
has k<=K(x). By the formal-semigroup definition of Lambda_P,

    psi_P(x)=sum_(1<=k<=K(x)) theta_P(x^(1/k)).                (8)

This is a finite identity and counts distinct formal powers separately
even at coincident norms. If K(x)=0 both sides and theta_P(x) vanish.
Using (7) for k>=2, with an empty sum if K(x)<2, gives

    0<=psi_P(x)-theta_P(x)
      <=3sqrt(x) K(x)
      <=(3/a)sqrt(x)log x.                                  (9)

Thus (6) and (9) imply the complete error bound

    |psi_P(x)-(x-x^b)|
      <=c_0+2log x+(3/a)sqrt(x)log x,                 x>=2. (10)

Since log x/x^(1/4) tends to zero, (10) proves both assertions in
(2). In particular the higher powers do not alter the coefficient
of x^(3/4). No ordinary-integer prime-power cutoff is substituted
for the actual a=log p_1.

### Uniform bounds including the initial interval

Equation (2) implies R_P(t)/t^b tends to -1, so there is a real X_0>=2
such that |R_P(t)|<=2t^b for all real t>=X_0. Local finiteness shows
psi_P(X_0)<infinity. For 1<=t<=X_0, monotonicity gives

    |R_P(t)|<=psi_P(X_0)+X_0.

Consequently the finite constant

    C=max{2,psi_P(X_0)+X_0}

satisfies |R_P(t)|<=C t^b for every t>=1. In particular this covers
R_P(1)=-1 and every initial atom. Since t^b<=t on this domain, we also
have, with A=1+C,

    0<=psi_P(t)<=A t                         for every t>=1. (11)

These estimates use no regularity of the generalized-integer count.

### The convolution with the same system's Lambda

Fix an arbitrary real x>=1. For every g with |g|<=x the exact identity

    |g|^(-b)=x^(-b)+b integral_(|g|)^x t^(-b-1)dt

can be multiplied by Lambda_P(g) and summed. Local finiteness permits
interchanging the finite sum and integral; at almost every t its
coefficient is psi_P(t). Therefore

    S_b(x):=sum_(|g|<=x) Lambda_P(g)|g|^(-b)
      =psi_P(x)x^(-b)+b integral_1^x psi_P(t)t^(-b-1)dt
      <=A x^(1-b)+(b A/(1-b))(x^(1-b)-1)
       =4A x^(1/4)-3A.                                    (12)

The unit has zero weight; there is no lower endpoint term. A prime
power at x contributes to psi_P(x)x^(-b), with zero associated
integral. Thus (12) holds at every real x, including coincident
atoms and x=1, with no limiting-endpoint assumption.

For every summand the argument x/|g| is at least 1. Using the global
bound for R_P, nonnegativity of Lambda_P and (12),

    |sum_(|g|<=x) Lambda_P(g)R_P(x/|g|)|
      <=C x^b S_b(x)<=4ACx.                                (13)

Finally, if u=log x>=0 then x^(b-1)log x=u exp(-u/4).
Its derivative is exp(-u/4)(1-u/4), so its maximum is 4/e.
It follows that

    |R_P(x)log x|<=(4C/e)x.                                (14)

Combining (13)–(14) proves (3) with B=4C(A+1/e). The bound pays both
terms in absolute value; it assumes neither cancellation nor an
unproved generalized Selberg identity. R_P and Lambda_P throughout
(8)–(14) are produced by the single prime system chosen in (4).

### Independent audit of the specialization — step 253

The audit reuses the inspected versioned source statement and its
continuous-construction case recorded in
`drafts/literature/2026-11-04-self-consistent-generalized-prime-diagnostic.md`;
no stronger conclusion of that source is imported. All five template
hypotheses are verified in (4): continuity includes the join at 2,
positivity includes the whole integration interval, the lower bound
uses [x/2,x] only when x>=4, and the upper split has sqrt(x)>=2.
The bounded initial interval extends the asymptotic Chebyshev bound.
Thus the continuous-case counting error 1 and p_1>1 are applicable.

The weighted conversion (5) includes equality at a prime. At x=2 the
continuous weighted count is zero and 2-2^b-c_0=0, so the boundary
constant in (6) has the stated sign and value. The two error terms
are bounded by log x each. On [1,2], pi_P<=1 gives (7) without
assuming p_1>=2. Local finiteness follows from finitely many available
generators and the actual positive a=log p_1; it does not require
distinct real norms for distinct formal integers.

For (8), a formal positive power has one unique generator and exponent;
coincident real norms do not merge those formal elements. K(x)=0
means x<p_1, so both psi_P(x) and theta_P(x) vanish. Otherwise the k=1
term is theta_P(x), and every k>=2 term has x^(1/k)<=sqrt(x).
The global bound (7) therefore proves (9), including K(x)=1 and atoms
at equality. The actual error in (10), divided by x^(3/4), tends to
zero, which is exactly the required threshold for retaining coefficient
1; no claimed power tail of smaller order is being assumed.

The passage from eventual to global control uses the finite value
psi_P(X_0) and t^b>=1 on the compact initial interval. It covers t=1,
where R_P(1)=-1, and yields nonnegative psi_P(t)<=At everywhere.
In (12) the finite sum permits the integral interchange, Lambda_P of
the unit is zero, and an upper-endpoint atom has zero integral but
retains its first-term weight. The power integral is
integral_1^x t^(-b)dt=(x^(1-b)-1)/(1-b), yielding exactly
4A x^(1/4)-3A; at x=1 the identity has left side zero and the upper
bound is A. Hence there is no missing lower or upper boundary term.
Equations (13) and (14) bound the two requested terms separately by
4ACx and 4Cx/e. Their sum is Bx with B=4C(A+1/e), for this single
system at every real x>=1. No cancellation, integer-density estimate
or continuation is used. The audit finds no mathematical repair needed.

This verifies the written known-construction specialization, without
claiming a result beyond the sources checked. It closes the coarse
self-generated-kernel diagnostic at its stated strength: such a bound
alone cannot exclude this system's power defect. It does not establish
the omitted increment, prefix, ordinary-prime or Xi properties.

### Scope and known traps

L734's ordinary-kernel calculation is comparison context only and is
not a mathematical input here. The present argument verifies the
missing self-generated-kernel feature, but does not transfer any of
L733's other profile constraints to this step function. It likewise
does not identify this defect with a zero of a meromorphic zeta
function. Revesz's prescribed-zero coefficient 1/rho is not imported
as coefficient 1. The construction theorem, weighted conversion,
finite power tail and absolute convolution estimates are exactly
the approved specialization. Actual-prime upper norms, scalar anchors,
complementary residuals and mixed positivity remain open.

## Mathlib

Full matching construction and specialization not checked; availability
unknown. Supporting mathematics used here consists of finite sums,
integration by parts, power integration and elementary real calculus.
No exact Mathlib declaration or absence claim is asserted. All source
hypotheses and specializations are stated above; the imported random
discretization proof is not a local reproof.
