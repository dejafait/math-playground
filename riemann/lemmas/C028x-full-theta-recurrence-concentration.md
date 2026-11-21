# Corollary C028x: full-theta recurrence is diffuse

## Hypotheses

Use the complete positive kernel K of L019 and M_0 from L021. Put

    dmu_0(x)=K(|x|)dx/(2*M_0), x in R.

Let p_j be its monic orthogonal polynomials, k_j=integral p_j^2 dmu_0,
and beta_j=k_j/k_(j-1) for j>=1. All degrees are integers. These are
the unscaled, untilted base coefficients used in C028o/p/w. No atoms
are added. Positivity and finite moments follow from L019/L021.
No recurrence asymptotic, monotonicity, RH, actual-root reality or
moment-determinacy hypothesis is assumed. Log denotes the natural log.

## Conclusion

There exist constants 0<b<=B<infinity, independent of j, such that

    b*log(j+1)^2 <= beta_j <= B*log(j+1)^2, j>=1.          (1)

Consequently, with T_n=sum_(j=1)^n beta_j,

    0 < max_(1<=j<=n) beta_j/T_n <= 8*B/(b*n), n>=2,      (2)

and the exact requested maximum-to-sum limit is zero. Constants and
the onset used to absorb finitely many indices are not evaluated.
No leading constant or actual beta_j asymptotic equivalence is claimed.

This is a local specialization of known exponential-weight recurrence
theory and the minimum monic norm principle. It supplies a diffuse-base
input potentially useful for C028w, not a two-moving-atom shape theorem,
a retained-cost floor, a small full cost, or C028b's H_d=o(d).
Conceptual audit1936 accepts (1)-(2) under the named theorem imports;
its checks and limits are recorded below. No stronger conclusion follows.

## Proof

### Imported results and scope of the specialization

E. Levin and D. S. Lubinsky, *On recurrence coefficients for rapidly
decreasing exponential weights*, J. Approx. Theory 144 (2007), 260-281,
DOI [10.1016/j.jat.2006.06.004](https://doi.org/10.1016/j.jat.2006.06.004),
[author manuscript, 16 April 2006](https://lubinsky.math.gatech.edu/Research%20papers/LevLub05Apr06.pdf),
Definition 1.2(a)-(e) and Theorem 1.3, pp.4-5, gives
A_n/delta_n=1/2+O(n^(-c)), some c>0, for W in F(C^2).
The recurrence is x*r_n=A_n*r_(n+1)+B_n*r_n+A_(n-1)*r_(n-1)
for polynomials orthonormal against W^2 dx. For even Q=-log W,
delta_n=a_n, with the defining integral on manuscript p.3 used below.
The hypotheses are checked explicitly for the model in this proof;
Definition 1.2(f) and finite-interval corollaries are not used.

G. Szego, *Orthogonal Polynomials*, 4th ed. (1975), AMS Colloquium
Publications 23, Theorem 3.1.2, p.39, with Section 3.1A, p.38
([inspected book text](https://djvu.online/file/Nk6YlVBVuENXs)),
identifies the monic orthogonal polynomial as the unique minimum-norm
monic polynomial of its degree for a positive measure with infinite
support and finite moments. Infinite intervals are allowed.

Assessment1933 and source-notes1934 cover these imports. Only their
theta/model applicability, scale bounds and norm transfer are proved
here; neither source theorem is reproved. In particular the recurrence
theorem is not applied directly to -log K, whose class membership has
not been established. The earlier C028o cumulative-divergence proof and
C028p/w cost formulas are context, not mathematical inputs to this proof.

### A degree-independent comparison using the entire theta series

For u>=0 define

    E(u)=exp(9*u/2-pi*exp(2*u)),
    S=sum_(m>=1) m^4*exp(-pi*(m^2-1)),
    d_0=1-3/(2*pi)>0.

S is finite: m^2-1>=m-1 for m>=1, and the series
sum m^4*exp(-pi*(m-1)) converges by its ratio limit exp(-pi)<1.
Factoring the full positive series in L019 gives, exactly,

    K(u)/E(u)
      =8*pi^2*sum_(m>=1) m^4*(1-3/(2*pi*m^2*exp(2*u)))
                            *exp(-pi*(m^2-1)*exp(2*u)).

Every bracket is positive and at most 1. Keeping m=1 for the lower
bound, and using exp(2*u)>=1 in every summand for the upper bound,
yields the global inequalities

    8*pi^2*d_0*E(u) <= K(u) <= 8*pi^2*S*E(u), u>=0.      (3)

Thus no tail is discarded, and these constants do not depend on u
or polynomial degree. Now use exactly the approved model

    Q(x)=pi*(cosh(2*x)-1)-(9/4)*log(cosh x),
    W(x)=exp(-Q(x)), w(x)=W(x)^2.

For u>=0, direct algebra, retaining the linear exponential prefactor,
gives

    w(u)/E(u)
      =exp(2*pi-pi*exp(-2*u))*((1+exp(-2*u))/2)^(9/2).

Since 0<exp(-2*u)<=1,

    exp(pi)*2^(-9/2) <= w(u)/E(u) <= exp(2*pi).

Combine with (3) and evenness to obtain, for every real x,

    c_K*w(x) <= K(|x|) <= C_K*w(x),                     (4)
    c_K=8*pi^2*d_0*exp(-2*pi),
    C_K=8*pi^2*S*2^(9/2)*exp(-pi).

These bounds include x=0 and the entire central interval; no compact
interval is omitted or handled by an assumed tail asymptotic. Division
by the fixed positive finite 2*M_0 from L021 gives

    c_* w(x)dx <= dmu_0(x) <= C_* w(x)dx,                (5)
    c_*=c_K/(2*M_0), C_*=C_K/(2*M_0).

### Verification of every model weight hypothesis

Write a=9/4, alpha=1-a/(4*pi)=1-9/(16*pi), and
Q_0(x)=2*pi*sinh(x)^2=pi*(cosh(2*x)-1).
In particular 0<alpha<1 and 2*alpha>1, using pi>3.
For x>=0,

    0<=log(cosh x)<=sinh(x)^2/2.

Indeed both sides vanish at zero, and
tanh x<=sinh x*cosh x gives the upper inequality after integration.
Also tanh x/(sinh x*cosh x)=1/cosh(x)^2<=1 for x>0.
Consequently

    alpha*Q_0(x)<=Q(x)<=Q_0(x),
    alpha*Q_0'(x)<=Q'(x)<=Q_0'(x), x>0.                 (6)

Q is smooth and even, Q(0)=0, Q(x)>0 off zero, and (6) implies
Q tends to infinity at both endpoints of R. Moreover

    Q'(x)=2*pi*sinh(2*x)-a*tanh x,
    Q''(x)=4*pi*cosh(2*x)-a*sech(x)^2
           >=4*pi-a>0.                                 (7)

Thus the continuity, nonnegativity and strict convexity requirements
hold. The model has all absolute moments, since (6) bounds Q below
by a fixed positive multiple of exp(2*|x|) when |x|>=1.

For the growth condition let T_Q(x)=x*Q'(x)/Q(x) off zero and
T_0(x)=2*x*coth x for x>0. Equation (6) gives

    alpha*T_0(x)<=T_Q(x)<=alpha^(-1)*T_0(x).             (8)

T_0(x)>=2 because tanh x<=x. It is increasing: the derivative of
x*coth x has numerator sinh x*cosh x-x, whose derivative is
2*sinh(x)^2>=0 and whose limit at zero is 0. For 0<s<t,

    1<2*alpha<=T_Q(s)<=alpha^(-2)*T_Q(t).

T_Q is even, so this also proves the source condition whenever
0<s/t<1 with s,t negative. Thus Lambda=2*alpha and C_1=alpha^(-2)
are valid global constants.

Finally (7) implies Q''<=Q_0'', and (6) gives for x>0

    Q(x)*Q''(x)/Q'(x)^2
      <=alpha^(-2)*Q_0(x)*Q_0''(x)/Q_0'(x)^2
      =alpha^(-2)*cosh(2*x)/(2*cosh(x)^2)
      <=alpha^(-2).                                    (9)

Evenness proves (9) for negative x as well. This is precisely
Q''/|Q'|<=C_2*|Q'|/Q with C_2=alpha^(-2), everywhere off zero.
At zero, Q(x)=(2*pi-9/8)*x^2+O(x^4), so T_Q tends to 2 and
Q*Q''/Q'^2 tends to 1/2. No singularity at zero has been used as
a source hypothesis. All Definition 1.2(a)-(e) conditions hold for W.

### The model MRS scale

For y>0 put

    F(y)=(2/pi)*integral_0^1 y*t*Q'(y*t)/sqrt(1-t^2) dt.

It is continuous, strictly increasing, tends to 0 at zero, and tends
to infinity. For continuity and the zero limit on bounded y ranges,
the numerator is uniformly bounded and 1/sqrt(1-t^2) is integrable;
for strict increase use (x*Q'(x))'=Q'(x)+x*Q''(x)>0 for x>0.
The lower bound below proves divergence. Evenness in the source MRS
definition therefore gives its unique a_n>0 by F(a_n)=n, n>=1.

For y>=1, monotonicity of x*Q'(x) and (6) give

    F(y)<=y*Q'(y)<=2*pi*y*sinh(2*y)<=pi*y*exp(2*y).

On t in [1/2,1], y*t>=y/2, Q'(y*t)>=2*alpha*pi*sinh y,
and 1/sqrt(1-t^2)>=1. Integrating this interval gives

    F(y)>=alpha*y*sinh y>=c_0*y*exp y,
    c_0=alpha*(1-exp(-2))/2>0.                           (10)

In particular a_n tends to infinity. For all sufficiently large n,
a_n>=1; using a_n<=exp(a_n) in the upper bound gives

    (log n-log pi)/3 <= a_n <= log n-log c_0.             (11)

The right bound uses c_0*a_n*exp(a_n)>=c_0*exp(a_n).
It follows that a_n is bounded above and below by fixed positive
multiples of log(n+1) for all sufficiently large n. No precise MRS
asymptotic is needed or asserted.

### The recurrence coefficient and minimum-norm transfers

Let k_j^* be the minimum squared norm of a monic degree-j polynomial
for w(x)dx, and beta_j^*=k_j^*/k_(j-1)^*. Both measures in (5)
are strictly positive on R, have infinite support and all moments.
Their finite polynomial Gram matrices are positive definite, so these
norms exist and are strictly positive in every degree.

For the source's orthonormal polynomials the positive leading
coefficient is 1/sqrt(k_j^*). Comparing leading coefficients in
its recurrence yields

    A_j=sqrt(k_(j+1)^*/k_j^*), beta_j^*=A_(j-1)^2.        (12)

Theorem 1.3, now applicable by (6)-(9), gives A_n/a_n->1/2.
Combining this with (11) and (12) bounds beta_j^* above and below
by positive multiples of log(j+1)^2 for all sufficiently large j.
The shift causes no loss: for j>=2, log j and log(j+1) are within
a fixed factor. Absorbing finitely many strictly positive ratios,
including beta_1^*, gives constants 0<b_*<=B_*<infinity such that

    b_*log(j+1)^2<=beta_j^*<=B_*log(j+1)^2, j>=1.

For every monic degree-j polynomial f, (5) compares its two squared
norms. Taking the infimum over the same set of monic polynomials and
using Szego's minimum principle separately in the two measures gives

    c_* k_j^*<=k_j<=C_* k_j^*, j>=0.

The constants are the same for every degree. Divide a lower bound
for the numerator by an upper bound for the denominator, and vice
versa, to obtain

    (c_*/C_*) beta_j^*<=beta_j<=(C_*/c_*) beta_j^*, j>=1.

This proves (1), with b=(c_*/C_*)b_* and B=(C_*/c_*)B_*.
It does not compare coefficients of different minimizing polynomials
term by term, and it does not transfer a model asymptotic equivalence.

### The exact maximum-to-sum bound

For n>=2, (1) gives max_(j<=n) beta_j<=B*log(n+1)^2.
There are at least n/2 integers from ceil(n/2) to n. For each,
j+1>=n/2+1>=sqrt(n+1), since (n/2+1)^2>=n+1. Therefore

    T_n>=b*(n/2)*(log(n+1)/2)^2
        =(b*n/8)*log(n+1)^2.

Dividing proves (2) and hence the requested limit. Only finite sums
and pointwise inequalities are involved. No degree/site interchange,
unproved actual asymptotic, numerical evidence or positivity criterion
equivalent to RH enters this argument.

### Independent conceptual audit1936 (20 November 2026)

The audit replayed the full argument above, starting from the exact
kernel in L019 and the normalization in L021, and accepts (1)-(2).
The imported theorems remain external inputs, not independently proved
here. This verifies a known-theorem specialization locally; it claims
neither a new general theorem nor an improvement beyond the sources.
The following records the load-bearing checks rather than a new proof.

The same Levin--Lubinsky manuscript was reopened at pp.1-5. Its
Theorem1.3 assumes F(C^2), defined by (a)-(e), on an interval whose
endpoints may be infinite. Condition (f), the smaller class E(C^2)
and the finite-interval corollaries are not needed. Its orthogonality
uses W^2, and the positive coefficient A_n joins degrees n and n+1.
The even-case MRS equation is the displayed equation on p.3, not one
with Q replaced by 2Q. Szego's Theorem3.1.2 and Sections3.1A/2.2A
were also reopened: finite moments and infinite support suffice on an
infinite interval. No completeness or moment-determinacy premise is
imported from the distinct closure theorem. These are verification
reads of coverage1934, not a fresh literature assessment or reproof.

For (3)-(5), dividing the second term of each theta summand by its
first gives exactly 3/(2*pi*m^2*exp(2u)). All summands are positive,
and the upper tail is bounded by the single finite series S independent
of u. The ratio test used for S applies to its stated geometric-series
majorant. Direct expansion of -2Q(u)-(9u/2-pi*exp(2u)) gives
2*pi-pi*exp(-2u)+(9/2)*log((1+exp(-2u))/2). Hence both comparison
constants include the central interval and have no hidden degree
dependence. Division by 2*M_0 preserves their positivity and finiteness.

For (6)-(9), the derivative of sinh(x)^2/2-log(cosh x) is
sinh(x)*cosh(x)-tanh x>=0 on x>=0. Both Q and Q' therefore have
the same lower factor alpha=1-9/(16*pi) relative to Q_0 and Q_0'.
The computed Q'' is everywhere positive. The derivative numerator
sinh(x)*cosh(x)-x is nonnegative, proving T_0 increases. Thus
T_Q(s)<=alpha^(-1)*T_0(s)<=alpha^(-1)*T_0(t)
<=alpha^(-2)*T_Q(t) for 0<s<t, with T_Q>=2*alpha>1.
Evenness handles negative s,t: 0<s/t<1 means |s|<|t|.
The positive quotients in (9) are legitimate off zero, since Q>0
and Q' has the sign of x. The displayed origin limits are consistent
with the Taylor coefficient 2*pi-9/8>0; the source ratios are only
required off zero. The exponential lower growth of Q supplies
all model moments. Every model class condition is therefore checked.

For (10), the restricted interval has length1/2, its numerator is
at least alpha*pi*y*sinh y, and the outside factor is 2/pi.
Their product is alpha*y*sinh y, with no missing factor2.
For the upper estimate, (2/pi)*integral_0^1(1-t^2)^(-1/2)dt=1.
Continuity uses an integrable majorant on every bounded y interval;
strict increase and divergence justify F(a_n)=n and a_n->infinity.
For a_n>=1 the bounds give c_0*exp(a_n)<=n<=pi*exp(3*a_n),
which has exactly the logarithmic directions in (11). No endpoint
Laplace estimate or sharper MRS asymptotic is being assumed.

For (12), the leading coefficient of the model orthonormal polynomial
is (k_j^*)^(-1/2). Thus A_j=sqrt(k_(j+1)^*/k_j^*) and the needed
coefficient is beta_j^*=A_(j-1)^2. The model limit applies eventually;
all omitted indices, including j=1, are absorbed using strictly
positive finite monic norms. The two minimizing polynomials need not
agree: taking infima in (5) over the same monic degree-j class yields
c_*k_j^*<=k_j<=C_*k_j^*. Taking ratios of adjacent degrees gives
exactly c_*/C_* and C_*/c_*, not powers depending on degree.

Finally the upper half of the indices gives the stated lower bound
(b*n/8)*log(n+1)^2 for T_n, including n=2. Its comparison with
B*log(n+1)^2 proves the actual required zero limit. Neither the source
model's asymptotic constant nor monotonicity is transferred to theta.
No correction to the mathematical argument or DAG inputs was required.
C028w's independent audit, moving-site shape restriction, weighted
residual rates and all omitted costs remain outside this audit.

## Mathlib

Full matching coverage is not checked. Availability of formal versions
of the cited general recurrence theorem, its model specialization and
the final theta bound is unknown. The named classical results are
imported as informal mathematical inputs; no formal verification or
absence from Mathlib is claimed. This does not audit C028w or establish
its missing moving-site separation and norm-weighted residual rates.
