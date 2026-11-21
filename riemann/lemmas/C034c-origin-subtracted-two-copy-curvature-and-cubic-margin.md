# Corollary C034c: two-copy curvature and a negative cubic margin

## Hypotheses

Use C034b's exact functions and all its qualifications. In particular,
sigma is Gaussian half-variance, 1<=sigma<=2, with differentiation
on (1/2,3), and

    G_sigma(z)=exp(-z^2/(4*sigma))/sqrt(4*pi*sigma),
    p_sigma(z)=(1/2)sum_rho[G_sigma(z-z_rho)+G_sigma(z+z_rho)],
    z_rho=gamma_rho-i*delta_rho,
    Q_j(x)=4*j*(3*x^2+j)/(x^2*(x^2+j)^2), j=1,2,
    d_j=partial_sigma b_sigma(sqrt(j)),
    e_j=partial_sigma^2 b_sigma(sqrt(j)),
    S4=sum_rho gamma_rho^(-4),
    T=d_1*d_2*(d_1-d_2)+d_1*e_2-d_2*e_1.

The actual positive-ordinate divisor counts all multiplicities, is
conjugation invariant, has gamma_rho>14, |delta_rho|<1/2, and obeys
N(T)=O(T log(T+2)). Retain the excluded ordinate zero, verified zeros
through100, retained real zero in (14,15), reciprocal-square-tail,
heat-positivity and separate fixed-j error qualifications, both fixed-v1
preprint qualifications, and zero drift and killing. C033w's identification
with the probability transform is inherited through C034b; no new
probability assertion or independent source-wide/finite-zero validation
is made here. Use C032n's Gaussian heat identity and full spatial
majorants. No RH, nonnegative p_sigma, nonnegative p_sigma-p_sigma(0),
or monotone spatial score is assumed.

## Conclusion

For x>0 define, at the same width throughout,

    A(x)=p_sigma(x)-p_sigma(0),
    B(x)=p_sigma''(x)-p_sigma''(0),
    f(x)=A(x)/x^2, g(x)=B(x)/x^2,
    dmu(x)=x^2*Q_1(x) dx,
    r(x)=Q_2(x)/Q_1(x), h=d_2-d_1.

The primes on p denote spatial derivatives. The functions f,g extend
continuously to zero. The positive measure mu has mass4*pi, 0<r<2,
and f,g,rf,rg are absolutely integrable. Uniformly on the closed width
interval, all the following integrals and indicated divisor exchanges
are absolutely convergent:

    d_1=int f dmu, d_2=int rf dmu,
    e_1=int g dmu, e_2=int rg dmu,                         (16)
    C:=d_1*e_2-d_2*e_1
      =(1/2)int int [f(x)g(y)-g(x)f(y)]
                        *[r(y)-r(x)] dmu(x)dmu(y),       (17)
    T=(1/2)int int F_sigma(x,y) dmu(x)dmu(y),
    F_sigma(x,y)=[f(x)g(y)-g(x)f(y)]*[r(y)-r(x)]
                    -h*f(x)f(y)*[r(x)+r(y)].             (18)

Here and below an unmarked integral is over (0,infinity). Moreover,

    h>(2/5)*S4>0,
    -h*d_1*d_2<-(1/5)*S4^3,
    T<C-(1/5)*S4^3.                                     (19)

Thus the concrete joint inequality

    (1/2)int int [f(x)g(y)-g(x)f(y)]*[r(y)-r(x)]
                  dmu(x)dmu(y) <= (1/5)*S4^3             (20)

at every sigma in [1,2] would suffice for T<0 throughout that interval.
Inequality (20) is NOT proved. The ratio r is not monotone in x;
the first product in (18) has no established sign. For every width
F_sigma is strictly negative on some open subset of (0,infinity)^2,
but its global sign and integral sign remain unresolved.

This is a partial result of attempt1843, passing conceptual audit1845
below under unchanged hypotheses.
It pays the joint cubic term and gives an absolutely convergent
correlation formula; it does not establish final-prefix nonvanishing,
ECT, fixed-site nonsingularity, conditioning, exact weights, TV<=2,
full observation matching, signed-height cancellation or Xi realization.

## Proof

### Source scope

Use the pre-invocation EXPLORE assessment1842 for exactly C034b's
origin-subtracted d_j,e_j,T, including the cubic. The general bilinear
determinant identity is imported from Giulio Ruzza, *Introduction to
Random Matrix Theory, Riemann-Hilbert problems, and Universality*,
notes updated4May2022, Lemma3.1.1, (3.1.1)-(3.1.9), printed pp27-28,
[primary notes](https://webpages.ciencias.ulisboa.pt/~gruzza/introRMT.pdf).
It permits complex measurable factors when every cross-product is L1.
The statement and complete proof were inspected in source-notes1842.
Forrester, *Meet Andreief, Bordeaux1886, and Andreev, Kharkov1882-83*,
[arXiv:1806.10411v1](https://arxiv.org/pdf/1806.10411v1), (1.7) p2
and Section2.2 p4, supplies the same identity. Neither gives a sign.
No reproof of that identity is needed; the checks below justify its
specialization. C032n supplies the previously justified Gaussian heat
and differentiation inputs; C034b supplies the memberwise signed core
and complete error bounds. C033g/k's odd kernel is not used.

### Origin subtraction and all absolute convergence checks

C034b(6) gives d_j=int A*Q_j. C032n's heat identity gives
partial_sigma A=B, with BOTH origin values retained. On [0,1],
evenness and the compact bounds for p'' and p'''' imply, uniformly
on [1/2,3],

    |A(x)|<=c*x^2, |B(x)|<=c'*x^2.

This also gives f(0)=p''(0)/2 and g(0)=p''''(0)/2. Since
Q_j=O(x^-2) at zero, both A*Q_j and B*Q_j are bounded there.
For x>=1, C032n(8)-(9) bound |p_sigma(x)| and |p_sigma''(x)|
by constants times its fixed nonnegative P(x), with
int_1^infinity P(x)/x^2 dx finite. The origin values are uniformly
bounded, while Q_j<=12*j/x^4. Consequently both products admit
a single integrable majorant on the full spatial domain, uniformly
on the parameter neighborhood. The fundamental theorem of calculus
in sigma followed by dominated convergence therefore differentiates
d_j=int A*Q_j and proves e_j=int B*Q_j, including widths1 and2.
There is no differentiation of a sign inequality or principal value.

For completeness the same domination holds absolutely before divisor
summation. Write

    h_rho(x)=Re([G_sigma(x-z_rho)+G_sigma(x+z_rho)]/2),
    A_rho=h_rho-h_rho(0), B_rho=h_rho''-h_rho''(0).

Normal convergence and conjugation give A=sum A_rho, B=sum B_rho,
with multiplicity unchanged. On [0,1], the sums of the suprema of
|h_rho''| and |h_rho''''| are finite uniformly in width, by C032n(8)
and the counting hypothesis. Taylor's theorem gives a summable x^2
majorant for each of A_rho and B_rho. On x>=1, the sums of the
absolute Gaussian derivatives are bounded by constant multiples of
P(x); the sums of |h_rho(0)| and |h_rho''(0)| are finite. Hence

    sum_rho int (|A_rho|+|B_rho|)*Q_j dx < infinity,     (21)

with a common uniform bound. Tonelli applies first to these nonnegative
majorants; Fubini then justifies every displayed signed divisor sum.

The density of mu is 4*(3*x^2+1)/(x^2+1)^2, which is bounded at
zero and O(x^-2) at infinity. Its mass is4*pi, using
int_0^infinity dx/(1+x^2)=pi/2 and
int_0^infinity dx/(1+x^2)^2=pi/4. To check r, write t=x^2 and

    R(t)=2*(3*t+2)*(t+1)^2/((t+2)^2*(3*t+1)).           (22)

All factors are positive, and
(t+2)^2*(3*t+1)-(3*t+2)*(t+1)^2=5*t^2+9*t+2>0.
Thus 0<r(x)=R(x^2)<2. Formula (21) proves f,g in L1(mu),
and this bound for r proves rf,rg in L1(mu), including absolute
memberwise sums. Equation (16) follows.

Apply Ruzza's n=2 identity with row factors f,g and column factors
1,r on the measure space ((0,infinity),mu). The four cross-products
are precisely f,rf,g,rg; their integrals form the matrix with rows
(d_1,d_2) and (e_1,e_2). This gives (17) with factor1/2.
For example, the absolute integral of f(x)g(y)r(y) is at most
2*||f||_1*||g||_1. Each expanded determinant term has the same
kind of bound. Before summing over rho,tau it is bounded by
2*(sum_rho||f_rho||_1)*(sum_tau||g_tau||_1), which is finite
by (21). Thus the two-copy formula has no hidden divisor exchange.
We use the finite measure directly, not an unnormalized covariance
formula missing its mass factor, and never divide by f or A.

Fubini also gives
(1/2)int int f(x)f(y)*(r(x)+r(y)) dmu(x)dmu(y)=d_1*d_2.
Its absolute integral is at most2*||f||_1^2. Multiplication by the
finite scalar h and C034b's identity for T give (18). The scalar
h itself is an absolutely convergent divisor sum by (21) and
|Q_2-Q_1|<=Q_1, proved below. If the cubic is expanded as a triple
divisor sum, the corresponding absolute bound is a constant times
(sum_rho||f_rho||_1)^3, so that expansion is legitimate as well.
All bounds are uniform in width, and dominated convergence gives
continuity of these integrals on the entire closed interval.

### A joint signed difference pays the cubic

Let D=Q_2-Q_1. The bound 0<r<2 proves |D|<=Q_1 on x>0.
Directly combining the rational functions gives

    D(x)=4*(3*t^2+3*t-2)/((t+1)^2*(t+2)^2), t=x^2.     (23)

In particular D>0 on x>=1. On a member's positive core
x in [gamma-1,gamma+1], we have x>13 and t>169. By (22),

    r(x)>2*((t+1)/(t+2))^2
         >2-4/(t+2)>2-4/171,
    r(x)-1>167/171>9/10.                               (24)

Thus D>(9/10)Q_1 on every such core. This is a comparison of the
two observation weights BEFORE integration; it is not a subtraction
of the two independent lower bounds for d_j.

For a fixed divisor member use exactly C034b's complete decomposition
in (8)-(13) with s=1. Its positive-center core, including the averaging
factor1/2, contributes more than (31/32)*gamma^(-4) against Q_1.
Equation (24) gives more than (279/320)*gamma^(-4) against D.
On x>=1 the weight D is positive and at most Q_1, so all other
positive-phase contributions may be discarded and both negative-phase
tails together cost less than (9/20)*gamma^(-4), as in C034b(10).
No favorable phase is assumed for the other translate, even inside
the selected core; its possible negative part is included in that cost.
On [0,1], |D|<=Q_1 lets C034b(12) bound the entire subtracted
integrand by (2/125)*gamma^(-4). On [1,infinity), the constant
subtraction h_rho(0) costs less than gamma^(-4)/10000, by C034b(13)
and D<=Q_1. All four regions/terms are therefore paid, yielding

    int (h_rho(x)-h_rho(0))*D(x) dx
       >[279/320-9/20-2/125-1/10000]*gamma^(-4)
       =(16231/40000)*gamma^(-4)
       >(2/5)*gamma^(-4).                              (25)

Equation (21) and |D|<=Q_1 justify summing (25). The count makes
S4 finite, and the nonempty actual divisor makes it positive. Hence
h>(2/5)S4. C034b gives d_1>S4/2 and d_2>S4; multiplication proves
h*d_1*d_2>S4^3/5. This proves (19) and the sufficiency of (20).
No individual ordinate, multiplicity or off-line member is omitted.

### Bounded sign test and the remaining obstruction

The joint expression (17) preserves precisely the correlation lost
by independent jet bounds. It has no automatic covariance sign.
Indeed logarithmic differentiation of (22) gives

    R'(t)/R(t)
      =(15*t^2+9*t-2)/((t+1)*(t+2)*(3*t+1)*(3*t+2)).    (26)

The numerator is negative on
0<t<(sqrt(201)-9)/30 and positive above that number. Thus r(y)-r(x)
has both signs on open subsets of the ordered region 0<x<y.
Even a strictly monotone spatial score would not, by its ordering
in x alone, give one sign to the determinant product in (17).
In fact f>=0 and any monotone score g/f have not been proved, and
division by f could be undefined. The correlation condition in Fabio
Zucca, *An inequality for correlated measurable functions*, Definition2.1
and Lemma3.3 (3.6)-(3.7), pp2,5 of the
[author version inspected20November2026](https://zucca.faculty.polimi.it/papers/inequality/inequality.pdf),
cannot simply be presumed. Its identity includes the measure's mass;
we do not apply its sign criterion here.

The concrete pointwise sufficient test for T<0 from (18) would be
F_sigma(x,y)<=0 everywhere, with strictness on a set of positive
product measure, at every width. Strictness alone is available:
d_1=int f dmu>0 and continuity imply f(x_0)>0 at some x_0>0.
Then F_sigma(x_0,x_0)=-2*h*f(x_0)^2*r(x_0)<0 by (19).
Continuity and the strictly positive density of mu extend this to
an open rectangle of positive product measure. This excludes a
pointwise nonnegative F_sigma proof for this representation; it
does NOT exclude a positive total integral. No control of F_sigma
away from that rectangle is established. The negative cubic likewise
does not bound the positive part of the curvature determinant.

End the bounded attempt here. The global pointwise sign test is
unpaid, and (20) remains an explicit sufficient threshold, not an
asserted estimate or a claimed zero. Preserve the convergent formula
and cubic margin as a partial input; park automatic monotonicity-based
closure. A later full-prefix attempt needs a new estimate of the
JOINT curvature integral, with separate source coverage if its
mechanism changes. Old stops1839/1746/1798/1823/1832/1837 remain intact.
The current result changes no actual-Xi all-degree sign conclusion.
The inspected sources supply the general identity, not (25) or (20);
the local partial calculation is not a certification of originality.

### Conceptual audit1845 — 20 November 2026

The partial conclusions (16)-(19), (21)-(26) and the negative open
patch pass the unchanged EXPLORE assessment1843, separately approved1844.
This verifies the existing estimate, with no stronger bound or corrected
mathematical conclusion. The primary identity and integration coverage
above is reused. Inequality (20), the sign of T and source-wide validity
are outside the verdict.

**Analytic interface and both origins.** C032n(8) bounds each fixed
spatial derivative and its first width derivative on I=[1/2,3], before
divisor summation. On [0,1] it gives, for k=0,2,4,

    sum_rho sup_(sigma in I, 0<=x<=1)|h_rho^(k)(x)|
       <=K_k*sum_rho exp(-(gamma_rho-1)^2/24)<infinity.

The last sum converges by the counting hypothesis. Each h_rho is even,
including a nonreal divisor member: the two translates exchange under
x -> -x because G is even. Taylor's formula applied to h_rho and
h_rho'' therefore gives |A_rho|<=x^2 sup|h_rho''|/2 and
|B_rho|<=x^2 sup|h_rho''''|/2. On x>=1, C032n(8)-(9) bounds
the sum of absolute translates and second derivatives by K*P(x),
with integral P(x)/x^2 finite; the summed origin values are finite.
Together with Q_j<=12j/x^4 this proves (21) using one dominator
independent of width. It proves the stronger domination of the sum
of absolute memberwise integrands, not just a bound on the signed sum.

Normal convergence gives partial_sigma p=p'' and
partial_sigma p(0)=p''(0). Hence partial_sigma A=B exactly.
The preceding dominator and the fundamental theorem of calculus give
e_j=int B Q_j on (1/2,3), so neither endpoint is a one-sided
differentiation problem. It also gives the continuous origin limits
f(0)=p''(0)/2 and g(0)=p''''(0)/2. No standalone integral of
p(0)Q_j or p''(0)Q_j is taken at zero. Conjugation justifies the
real-member convention while retaining every conjugate and multiplicity.

**Product integrals and constants.** The density decomposes as
12/(1+x^2)-8/(1+x^2)^2, so its mass is 4*pi. Expanding the positive
denominator comparison in (22) gives precisely 5t^2+9t+2, proving
0<r<2. Put a=sum_rho ||f_rho||_(L1(mu)) and
b=sum_rho ||g_rho||_(L1(mu)); (21) makes both finite, uniformly in
width, and the preceding pointwise dominators also dominate the sums.
For each expanded mixed product the summed absolute double integral
is at most 2ab. Tonelli on these majorants permits both independent
divisor sums, and Fubini permits their spatial integrations. Ruzza's
row factors (f,g) and column factors (1,r) meet all four L1 hypotheses.
Their determinants have product
(f(x)g(y)-g(x)f(y))*(r(y)-r(x)), giving the sign and factor 1/2
in (17). This uses the measure directly, without a probability
normalization or an extra mass factor.

The cubic integral in (18) has absolute bound 2a^2 before multiplication
by h. Since |Q_2-Q_1|<=Q_1, the sum of absolute member contributions
to h is at most a. Thus even its triple-divisor expansion has bound
2a^3. For the two-copy expression h is a uniformly bounded scalar;
the pointwise majorants already proved give dominated convergence in
width for all displayed integrals. No diagonal divisor terms, cross
terms or origin constants are excluded from these checks.

**Sign-changing difference weight.** Rational subtraction verifies
(23). For t>=1 its numerator 3t^2+3t-2 is positive. On the selected
core t>169, the factor (3t+2)/(3t+1)>1 in (22), and
((t+1)/(t+2))^2=1-2/(t+2)+1/(t+2)^2. Thus (24) gives
D>(9/10)Q_1 there. The factor 1/2 in each translate remains present:
the positive core contributes more than (9/10)*(31/32)=279/320
in units gamma^(-4). On all x>=1, 0<D<Q_1, so both complete
negative-phase bounds from C034b apply, totaling less than 9/20.
The second translate's possible negative part inside the core is
included. Discarding the remaining positive phases is therefore valid.

There is a useful distinction in the origin payment: the display
C034b(12) bounds the absolute value of an integral, but its proof
actually proves the following stronger intermediate estimate:

    integral_0^1 |h_rho(x)-h_rho(0)| Q_1(x) dx
       <=6*sup_[0,1]|h_rho''|
       <=(8/15)*gamma^2*exp(-(gamma-1)^2/8)
       <(2/125)*gamma^(-4).

Indeed the pointwise Taylor bound above and x^2 Q_1<=12 give the
first inequality before integration. This is the bound used with
|D|<=Q_1 on [0,1]; it needs no sign of D or of the subtracted profile.
On [1,infinity), C034b(13) pays the full constant subtraction by
less than gamma^(-4)/10000. Hence the exact memberwise residual is

    279/320-9/20-2/125-1/10000
       =16231/40000=2/5+231/40000.

The positive excess is uniform in width and member. Absolute summation,
the finite S4 and its strict positivity therefore give h>(2/5)S4.
Multiplying with the audited d_1>S4/2 and d_2>S4 proves
h*d_1*d_2>S4^3/5, with strictness intact. This establishes (19)
without subtracting independently estimated d_j or differentiating
an inequality.

**Limited sign conclusion.** Logarithmic differentiation of (22)
gives 2/((t+1)(t+2))-3/((3t+1)(3t+2)), whose numerator is
15t^2+9t-2. Its only positive zero is (sqrt(201)-9)/30, so the
nonmonotonicity claim is exact. With d_1>0, continuous f is positive
at some x_0>0. Equation (18) on the diagonal gives exactly
-2h f(x_0)^2 r(x_0)<0; continuity gives an open rectangle, and the
strictly positive measure density makes its product measure positive.
This proves only a negative patch. No sign on its complement or
upper bound for the full curvature integral follows. In particular
(20) would imply T<0, but remains an unproved sufficient condition.

The analytic verdict needs no probability positivity; the probability
interpretation retains C034b's complete C033w/C033l/C032q interface,
including positive-real arguments sqrt(j), both fixed-v1 inputs,
finite-zero and heat-error qualifications, and zero drift and killing.
Their wider validity is not audited here. The strict numerical ordinate
floor is inherited; no new zero data is used. The existing direct
mathematical inputs C032n and C034b suffice, so the DAG is unchanged.
The final ECT prefix, quantitative inverse and weights, full observations,
signed height, cancellation and Xi realization all remain open.

## Mathlib

Full matching coverage is unchecked and unknown. No Mathlib theorem
is used or asserted absent. Supporting integration, Gaussian and
finite determinant results may exist, but no matching theorem for
this qualified full-divisor specialization, its joint cubic margin
or the unproved bound (20) has been verified. Conceptual audit1845
verifies the informal local partial proof; external preprints and
finite-zero data keep their inherited qualifications.
