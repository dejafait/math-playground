# Actual-weight cubic feasibility: coefficient-uniform dual attempt

Work in progress, 30 October 2026. Invocation-start coverage is the
unchanged EXPLORE assessment
`literature/2026-10-29-saturation-weighted-cubic-feasibility.md`.
The exact E_3 infimum, including all T-dependent real cubics, is the
only mathematical target. No replacement by the p=1 error is allowed.

The main gap is actual-Xi all-degree positivity. The intermediate test
is a bounded functional annihilating 1,x,x^2,x^3 in
dmu_T=|R_T(t)|dt, x=|F_T(t)|^6, whose saturation pairing is at least
c T(log T)^3. Such a result would stop this particular polynomial
approximation implementation; successful approximation would still
need a separate positive signed correlation. Neither outcome would
settle the negative mass or higher signs.

Essential inputs are L477 (1)--(5), L481's exact F_T and retained
finite-interval estimates, and Houston--Roggendorf--van der Zee,
ESAIM M2AN 56 (2022), Section 2.1, Theorem 2.1 and Corollary 2.4,
pp. 185--186, as already inspected in the assessment. L482 and the
constant-candidate attempt are contrasts, not positive premises.
No Haar transfer, independent phases, weighted amplitude distribution,
coefficient bounds, RH, or discarded exceptional mass is available.

Proposed bounded test: use five ordered bounded amplitude ranges to
construct exact cubic-annihilating coefficients, retaining their
actual |R_T|-weighted masses. Then check whether the available
finite-polynomial interface proves the needed full-scale masses.
Do not infer such masses from ordinary high moments. Continue only
with a proved new weighted estimate or a decision of E_3. If the
construction merely exposes an uncontrolled mass, record the failure
and park this implementation without promoting a conditional formula
to a main-gap advance.

## Completed diagnostic calculation

This is the full calculation of an unsuccessful quantitative dual
test, not a new accepted lemma or an asymptotic decision of E_3.
The construction below uses classical finite interpolation to specify
an admissible dual; it does not reprove the general best-approximation
theorem. Its unproved actual-weight premise is kept explicit.

### 1. Weighted setting and the exact dual obligation

For a fixed sufficiently large real T put S_T=T(log T)^3 and

    x(t)=|F_T(t)|^6, f(x)=x/(1+x), dmu(t)=|R_T(t)|dt,
    nu(E)=integral_[T,2T] 1_(x(t) in E) dmu(t).

Use the complete real R_T of L477 (1), or equivalently L481's
U+Re(exp(2i theta)V). Both phases are inside the absolute value.
The functions are continuous on the compact time interval, x is
bounded for this fixed T, and L477 (5) gives nu([0,infinity))<=C S_T
with C independent of T. All polynomial moments used at fixed T
are therefore finite. This is not a uniform estimate for growing
weighted moments. If mu is zero, E_3=0 and a positive lower bound
is impossible; no division by its total mass is made below.

The image of the real polynomials of degree at most three is a
finite-dimensional, hence closed, subspace of L1(mu), even if some
polynomials agree mu-almost everywhere. Thus the Banach-space
criterion in Houston--Roggendorf--van der Zee, Theorem 2.1, and its
L1 characterization in Corollary 2.4 apply in this weighted setting.
Their complete statement, including freedom on the zero-error set,
is retained; no assumption of a unique approximant or a null
zero-error set is needed. Precise source:
[ESAIM M2AN 56 (2022), pp. 185--186, Section 2.1](https://www.numdam.org/item/10.1051/m2an/2021086.pdf#page=9).

For the test only the following direct inequality is needed. If
g is real, measurable, |g|<=1 mu-almost everywhere, and

    integral g(t)x(t)^k dmu(t)=0, k=0,1,2,3,

then every admissible p, with arbitrary T-dependent coefficients,
satisfies

    integral |p(x(t))-f(x(t))|dmu(t)
        >= |integral g(t)(p(x(t))-f(x(t)))dmu(t)|
         = |integral g(t)f(x(t))dmu(t)|.                 (1)

Taking the infimum preserves (1). This uses the entire interval,
including its endpoints, and every real cubic, including constants
and zero. It does not bound E_3 below by one candidate's error.

### 2. An exact five-range construction

Choose five closed intervals I_i=[a_i,b_i], i=0,...,4, with

    0<=a_0<=b_0<a_1<=b_1<...<a_4<=b_4=B,
    delta=min_(i<4)(a_(i+1)-b_i)>0,
    m_i=nu(I_i)>0, m=min_i m_i, kappa=m delta^4.

These are conditional choices: no such positive masses, let alone
full-scale lower bounds for them, have been proved for actual F_T.
Let lambda_i be the probability measure nu restricted to I_i and
divided by m_i. For y_i in I_i put

    alpha_i(y_0,...,y_4)=1/product_(j!=i)(y_i-y_j).

The separation gives |alpha_i|<=delta^(-4). Finite Lagrange
interpolation, by comparing the coefficient of degree four in the
interpolant of y^k, gives

    sum_i alpha_i y_i^k=0, k=0,1,2,3.                  (2)

The elementary partial-fraction identity

    1/product_j(z-y_j)=sum_i alpha_i/(z-y_i)

follows by multiplying by the denominator and evaluating the two
degree-at-most-four numerators at each of the five distinct y_i.
Evaluate at z=-1, which is outside the nonnegative intervals, to
obtain sum_i alpha_i/(1+y_i)=1/product_j(1+y_j). Using (2) at
k=0 therefore gives the exact saturation identity

    sum_i alpha_i f(y_i)=-1/product_j(1+y_j).           (3)

Define a real measurable function h on the amplitude axis by zero
off the five intervals and, for x in I_i, by

    h(x)=-(kappa/m_i)
       integral [1/product_(j!=i)(x-y_j)]
                    product_(j!=i) dlambda_j(y_j).

The uniformly separated denominators justify these finite product
integrals and their interchange, and
|h(x)|<=kappa/(m_i delta^4)=m/m_i<=1. Put g(t)=h(x(t)).
Integration on I_i changes dnu to m_i dlambda_i, so (2) proves
all four annihilation conditions exactly. Equation (3) gives

    integral g f(x)dmu
       =kappa integral [1/product_j(1+y_j)]
                                  product_j dlambda_j(y_j)
       >= m delta^4/(1+B)^5.

Consequently the test yields the conditional bound

    E_3(T)>=delta^4 min_i nu(I_i)/(1+B)^5.              (4)

No coefficient bound, inverse moment matrix, density of the
pushforward measure, Haar law, or unweighted exceptional-set
estimate was used. Values outside the five ranges have not been
removed from the error norm; the dual is simply zero there. This
is also why (4) remains valid if nu has atoms. The endpoints of
the five disjoint ranges and of [T,2T] are retained.

For example, the fixed ranges [0,1],[2,3],[4,5],[6,7],[8,9]
would give E_3(T)>=10^(-5) min_i nu([2i,2i+1]). Thus proving
all five masses >=eta S_T for some fixed eta>0 on a sequence
would stop cubic approximation on that sequence. This statement
does not assert those mass inequalities. Different fixed ranges
would also work; the displayed ones are a discriminating test,
not a claim about the actual amplitude distribution.

### 3. Why the existing concentration certificate does not finish it

L481 supplies integral R_T x>=c T(log T)^18 and
integral x^(4/3)<=C T(log T)^16, together with its residual
moment obstruction. Neither assertion localizes the nonnegative
measure nu to the five bounded ranges in (4). The available
finite-polynomial interface L481 (3)--(4) evaluates finite
polynomial means with a length-dependent error; it is not an
estimate for |R_T| times an amplitude-range indicator. In particular,
the large signed moment cannot be turned into any of the five
positive lower bounds by taking its absolute value.

There is also a precise diagnostic limit on a dual placed only
where the amplitude grows. For any dual satisfying (1), if g=0
mu-almost everywhere on {x<a}, then the constant annihilation
condition and f=1-1/(1+x) give

    |integral g f(x)dmu|
      =|integral g/(1+x)dmu|
      <=nu([0,infinity))/(1+a)<=C S_T/(1+a).           (5)

Hence support restricted to x>=a(T) with a(T) tending to infinity
cannot give the sought fixed positive multiple of S_T. This is a
limitation of that dual support, not an upper bound for the whole
E_3 infimum and not a statement that actual weight escapes to
infinity. For an arbitrary dual, splitting only the right side of
this same inequality gives

    |integral g f(x)dmu|
      <=nu([0,a])+C S_T/(1+a).                         (6)

Thus a full-scale dual needs full-scale weighted mass at some
fixed bounded amplitudes. Equation (4) needs the further spread
over five separated ranges. No such bounded-amplitude mass or
spread follows from the inputs used in this attempt. Proving only
positivity of fixed-T masses would not meet the required scale.

These are elementary diagnostic checks, not a new distribution
theorem. The actual E_3 alternatives remain undecided. In particular,
failure of this constructed dual does not preclude another dual,
and no positive lower bound has been obtained even on a subsequence.
The p=1 calculation has not been repeated or silently substituted
for the cubic infimum.

## Outcome, stop and source scope

EXPLORATION / RESEARCH / REPRODUCTION; actual task proof_attempt.
The attempt makes the coefficient-uniform separation test explicit,
but supplies no new actual weighted estimate or main-gap advance.
After the earlier constant-candidate failure and this dual test,
park the E_3 implementation. Reopening requires a materially new
bounded-amplitude weighted mass estimate or another independently
testable mechanism; another ordinary-moment or duality rewrite is
not a continuation. Preserve the separate L481/L482 stops.

No new lemma, mathematical script, numerical certificate, DAG edge,
or argument-overview edit is warranted by this unsuccessful test.
The canonical inputs remain L477 and L481. The displayed conditional
calculation is retained here as failed-attempt evidence, not entered
as an established premise in the proof assembly. The imported
optimality theorem was reused, not reproved; finite interpolation
was written out only to check this specific candidate and all of
its missing quantitative hypotheses. Matching Mathlib coverage is
not checked; unknown availability is not absence. Full signed
correlation, either L1 defect threshold, negative mass, individual
signs and all-degree positivity remain unresolved.
