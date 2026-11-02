# Lemma 639: vanishing microscopic-bump projection onto growing Hardy jets

## Hypotheses

Use exactly L637's fixed nonnegative w in C_c^infinity((0,1)),
integral w=1, fixed u0 with w(u0)>0, and

    L=log T, T<=X<=2T, a=X+u0*T, w_XT(t)=w((t-X)/T),
    psi(x)=exp(-1/(1-4x^2)) for |x|<1/2, zero otherwise,
    g_(T,X)(t)=psi(L(t-a))/||psi(L(.-a))||_T,
    <f,h>_T=integral w_XT(t) f(t) conjugate(h(t)) dt.

The norm is in the complex Hilbert space L2(w_XT dt). Z is the actual
analytic Hardy function fixed in L465/L622, real on the real axis;
ordinary derivatives are used. Define

    n=floor(L^(1/3)), N=n+1,
    V_(T,X)=span_C{L^(-j) Z^(j):0<=j<=n},
    Pi_(T,X)=the orthogonal projection onto V_(T,X),
    A_n=sqrt(2) N 10^n n!.

All onsets below are existential and uniform in X. No RH, simplicity,
nonvanishing at a, or exact bandlimitation is assumed.

Named imports, reused from the prior assessment:

- Sandro Bettin, *The second moment of the Riemann zeta function with
  unbounded shifts*, Int. J. Number Theory 6 (2010), 1933--1944,
  [arXiv:1111.0925v1, Theorem 1, p. 2; small-shift proof cases,
  pp. 9--10](https://arxiv.org/pdf/1111.0925v1#page=2),
  DOI 10.1142/S1793042110003861. With Re alpha, Re beta=O(1/log Y)
  and c=alpha-beta, the primitive has main integrand
  zeta(1+c)+zeta(1-c)chi(1/2+alpha+it)chi(1/2-beta-it),
  and error O((sqrt(Y)+sqrt(|Im alpha|)+sqrt(|Im beta|))log^2 Y).
  At c=0 the complete bracket is continued. Only fixed scaled complex
  shifts alpha=ir/L, beta=is/L, |r|,|s|<=2, and endpoints Y in [T,3T]
  occur here. The arithmetic theorem is imported, not reproved.
- Legendre orthogonality and normalization, [DLMF Table
  18.3.1](https://dlmf.nist.gov/18.3#T1), and the finite Jacobi formula
  [DLMF 18.5.8](https://dlmf.nist.gov/18.5#E8) at alpha=beta=0.
  The degree-dependent consequences actually needed are proved below.
- The Laurent expansion [DLMF 25.2.4](https://dlmf.nist.gov/25.2#E4):
  J(c)=zeta(1+c)-1/c is holomorphic at zero. It is holomorphic on a
  neighborhood of |c|<=1, since zeta has no other finite pole.
- Classical strip convexity (Phragmen--Lindelof), the zeta functional
  equation and sector Stirling, with the uniform-strip argument in
  L465 Section 4. Precise sources there are Titchmarsh, revised by
  Heath-Brown, *The Theory of the Riemann Zeta-Function*, 2nd ed.
  (1986), Section 5.1, (5.1.1)--(5.1.5), pp. 95--96, and DLMF
  5.11.1--2. The prior assessment also inspected Tao's
  [254A Supplement 3 (2014), (35)--(38)](https://terrytao.wordpress.com/2014/12/15/254a-supplement-3-the-gamma-function-and-the-functional-equation-optional/).
  Compact-strip uniformity is justified in Section 4 below, rather
  than inferred from pointwise constants depending on sigma.

L638 Section 1 supplies the smooth-window analytic conversion before
its fixed-order O(T) simplification; L465/L622 supply the local gamma
phase bounds. The invocation-start EXPLORE assessment is
drafts/literature/2026-11-01-growing-jet-localization-projection-test.md.
The new work is quantitative specialization to this growing space, not
a reproof of the arithmetic theorem. No fourth-moment result is used.

## Conclusion

For each fixed epsilon>0 and all sufficiently large T, uniformly in X,

    ||Pi_(T,X) g_(T,X)||_T^2
       <= C_(epsilon,w,u0,psi) T^(-1/2+2epsilon) A_n^2/L^2.     (1)

Since log A_n=O(n log(n+2))=o(log T), this tends to zero by choosing
epsilon<1/4. In particular, for every fixed eta>0 the squared projection
is O_(eta,w,u0,psi)(T^(-1/2+eta)). The actual weighted Gram, not just
the leading sine kernel, is used.

Consequently the squared distance of the unit bump from V_(T,X) is
1-o(1), uniformly in X. This rules out this particular microscopic
realization within the approved degree range. It does not rule out
larger degrees, arbitrary finite translates, other dictionaries, or
other observers. Signed |W|-weighted approximation, useful signed
main-term margins, actual-Xi initial signs and all-degree mixed
positivity remain unresolved. No RH resolution candidate is claimed.

The separate conceptual application audit in Section 6 passed on
1 November 2026 under the named imports, without changing any bound
or hypothesis. The bounded literature search identified no matching
projection theorem; that does not establish originality beyond the
sources checked. The arithmetic source proof remains an import.

## Proof

### 1. Retain the complete arithmetic second main term

For independent complex |r|,|s|<=2 put

    B(r,s)=integral w_XT(t) Z(t+r/L) Z(t+s/L) dt,
    c=i(r-s)/L, lambda_t=log(t/(2pi)), q_t=lambda_t/L,
    h(t;r,s)=exp(i[theta(t+r/L)-theta(t+s/L)]).

All functions are holomorphic on a neighborhood of this polydisc.
The exact Hardy conversion in L638 Section 1 gives the zeta product
multiplied by h, and its two-chi factor is h^(-2). Here |h|=O(1) and
|partial_t h|=O(1/(TL)). At every primitive endpoint Y the same physical
shifts ir/L,is/L are used, and log Y=L+O(1). Bettin's residual is thus
O(sqrt(T)L^2) uniformly throughout [T,3T]. Integrating by parts against
w_XT*h has zero boundary terms and total derivative integral O_w(1).
It follows that

    B(r,s)=integral w_XT(t)
                 [h zeta(1+c)+h^(-1)zeta(1-c)] dt
                 +O_w(sqrt(T)L^2).                           (2)

This imports the primitive estimate; it does not differentiate its
pointwise error. Compact t support and local holomorphy justify later
holomorphic differentiation of B.

The analytic gamma estimates in L465/L622 imply

    theta'(t)=lambda_t/2+O(1/T),
    theta''(t+z/L)=O(1/T) for bounded complex z.

Integrating on the segment between the shifted arguments therefore
gives h=exp(c lambda_t/2)+c O(1/T), uniformly and holomorphically.
Indeed the difference of the exponents is c times a holomorphic
O(1/T) function, including at r=s. Both h and its inverse are bounded.
Replacing h by exp(c lambda_t/2) in the full bracket of (2) costs
O(1/T): the difference is divisible by c before multiplication by
the pole 1/c. The integrated cost is O_w(1).

Write J(c)=sum_(m>=0) a_m c^m and
M=max_(|c|=1)|J(c)|. Cauchy's coefficient estimate gives |a_m|<=M.
With the singularities already canceled, the resulting main bracket is

    L integral_(-q_t/2)^(q_t/2) exp(i(r-s)x) dx
      + exp(i(r-s)q_t/2) J(c)
      + exp(-i(r-s)q_t/2) J(-c).                            (3)

For example, the first term is 2 sinh(c lambda_t/2)/c with its
continued value at c=0. Thus (2)--(3) yield an exact identity for B
with a holomorphic error E satisfying

    sup_(|r|,|s|<=2)|E(r,s)|<=C_w sqrt(T)L^2.                (4)

The full regular part J has been retained. In particular the O(T)
error obtained by dropping it in a fixed-order calculation is not used.

### 2. Polynomial endpoint and coefficient estimates

For any q in [1/2,2], set I_q=[-q/2,q/2]. Write ||P||_(I_q) for
the unweighted L2 norm of a complex polynomial P on that interval.
If deg P<=n, the normalized Legendre basis is

    e_k(x)=sqrt((2k+1)/q) P_k(2x/q), 0<=k<=n,

where P_k is the ordinary Legendre polynomial. Orthogonality makes
the squared norm of P the sum of squared coefficients in this basis.
The finite Jacobi formula at alpha=beta=0 reads

    P_k(y)=2^(-k) sum_(h=0)^k binom(k,h)^2
                              (y-1)^h (y+1)^(k-h).          (5)

For 0<=j<=k its coefficient of (y-1)^j is
2^(-j) binom(k,j) binom(k+j,j). To verify this from (5), the sum
before the factor 2^(-j) is

    sum_(h=0)^j binom(k,h)^2 binom(k-h,j-h)
      =binom(k,j) sum_(h=0)^j binom(k,h)binom(j,h)
      =binom(k,j)binom(k+j,j).

The last equality is the coefficient convolution for (1+z)^(k+j).
It follows that

    P_k^(j)(1)=(k+j)!/[2^j j! (k-j)!].                      (6)

Parity from (5) gives the same absolute value at -1. After rescaling,
using q>=1/2 and (k+j)!/(k-j)!<=(2N)^(2j), Cauchy--Schwarz in
the orthonormal basis gives, for every j>=0,

    |P^(j)(+-q/2)|
       <=sqrt(2) N (8N^2)^j/j! * ||P||_(I_q).              (7)

For j>n the left side is zero. The factor sqrt(2)N follows from
sum_(k=0)^n(2k+1)/q=N^2/q<=2N^2. This is an explicit estimate
for arbitrary complex polynomial coefficients.

Let F(x)=P(x) conjugate(P(x)) for real x; algebraically the second
factor is the polynomial with conjugate coefficients. Leibniz and (7)
give

    |F^(m)(+-q/2)|
       <=2N^2 (32N^2)^m/m! * ||P||_(I_q)^2.                (8)

In fact the intermediate sum is
sum_(j=0)^m binom(m,j)/(j!(m-j)!)=binom(2m,m)/m!<=4^m/m!.
Zero derivatives cause no problem when an index exceeds n.

We also need a coefficient estimate insensitive to arbitrary
T-dependent coefficients. Write P(x)=sum_(j=0)^n p_j x^j.
The sum of absolute monomial coefficients of each factor 2x/q+-1
is at most 5. Formula (5) and sum binom(k,h)^2=binom(2k,k)<=4^k
bound that sum for P_k(2x/q) by 10^k. Cauchy--Schwarz in the same
orthonormal basis therefore yields

    sum_(j=0)^n |p_j| j!
       <=n! sum_(j=0)^n |p_j|
       <=sqrt(2) N 10^n n! ||P||_(I_q)
       = A_n ||P||_(I_q).                                  (9)

All constants in (7)--(9) are uniform for q in the displayed interval.

### 3. Coercivity of the actual weighted Gram

Associate to P the function

    U_P(t)=sum_(j=0)^n p_j i^(-j) L^(-j) Z^(j)(t),
    D_P^(r)=sum_(j=0)^n p_j i^(-j) partial_r^j,
    Dbar_P^(s)=sum_(j=0)^n conjugate(p_j) i^j partial_s^j.

At r=s=0, applying D_P^(r) Dbar_P^(s) to B gives exactly ||U_P||_T^2,
because all real-axis derivatives of Z are real. Applied to
exp(i(r-s)x), it gives F(x)=|P(x)|^2. Further,

    c^m exp(i(r-s)x)=L^(-m) partial_x^m exp(i(r-s)x).

Consequently contracting the last two terms of (3) gives precisely

    R_t(P)=sum_(m=0)^(2n) a_m L^(-m)
       [F^(m)(q_t/2)+(-1)^m F^(m)(-q_t/2)].                (10)

There is no infinite derivative-order approximation here: all m>2n
terms vanish at r=s=0 under an operator of total order at most 2n.
The original power series is uniformly convergent on the fixed scaled
polydisc for large T, so this termwise extraction is legitimate.

On [T,3T], q_t=1+O(1/L) lies in [1/2,2]. Equations (8) and (10)
give the relative bound

    |R_t(P)|<=4 M N^2 exp(32N^2/L) ||P||_(I_(q_t))^2.     (11)

Since N^2/L->0, its coefficient divided by L tends to zero. Beyond
one onset it is at most L/2. Thus the complete main form in (3),
including its regular arithmetic terms, has real part at least
(L/2)||P||_(I_(q_t))^2 after contraction.

For the remaining analytic error use radius-one Cauchy circles about
r=s=0 inside (4). They give

    |D_P^(r) Dbar_P^(s) E(0,0)|
       <=C_w sqrt(T)L^2 (sum |p_j| j!)^2.                  (12)

Let q_-=(L-log(2pi))/L. For large T it belongs to [1/2,2], and
I_(q_-) is contained in every I_(q_t) on [T,3T]. Applying (9) with
q=q_-, integrating the main-form lower bound against w_XT>=0, and
using integral w_XT=T proves

    ||U_P||_T^2
       >=[TL/2-C_w sqrt(T)L^2 A_n^2] ||P||_(I_(q_-))^2.

Here log A_n=O(n log(n+2)), for example from n!<=max(1,n^n).
Because n=floor(L^(1/3)),

    T^(-1/2) L A_n^2 ->0.

It follows, after an X-uniform onset, that

    ||U_P||_T^2 >= (TL/4) ||P||_(I_(q_-))^2.              (13)

This proves actual-Gram coercivity for every polynomial, with no
restriction on its complex coefficients. It also shows that U_P is
nonzero whenever P is nonzero, so the indicated derivative functions
are linearly independent for sufficiently large T.

### 4. Bump correlations with all growing-order costs included

For every fixed epsilon>0, uniformly for t in [T,3T] and |z|<=1,

    |Z(t+z/L)|<=C_epsilon T^(1/4+epsilon).                 (14)

Here is the required compact-strip argument. Choose a fixed
0<delta<min(1/4,2epsilon). On the strip -delta<=sigma<=1+delta,
apply the classical strip theorem to (s-1)zeta(s)/(s+2), removing
zeta's pole without adding one. The Dirichlet-series bound on the
right boundary and the functional equation plus sector Stirling on
the left boundary have powers 0 and 1/2+delta respectively.
Interpolation gives exponent (1+delta-sigma)/2, uniformly in the
central compact substrip 1/4<=sigma<=3/4. The finite-order growth
hypothesis is the same classical input used in L465 Section 4.
Removing the rational factor at large height only changes constants.
For s=1/2+i(t+z/L), sigma=1/2-Im(z)/L and height comparable to T;
the exponent is at most 1/4+delta/2+1/(2L). This proves the zeta
part of (14), with the prescribed epsilon. Finally theta(t) is real
and theta'=O(L) on this complex neighborhood, so the modulus of
exp(i theta(t+z/L)) is bounded. This proves (14) for the analytic Z,
including points below as well as above sigma=1/2.

Cauchy's formula in z on the unit circle and (14) imply

    |L^(-j)Z^(j)(t)|<=C_epsilon j! T^(1/4+epsilon).

This keeps every factorial explicitly; it does not use a fixed-order
constant as if it were uniform, and does not differentiate the
real Riemann--Siegel remainder. Combining with (9) gives

    sup_(t in [T,3T]) |U_P(t)|
       <=C_epsilon T^(1/4+epsilon) A_n ||P||_(I_(q_-)).    (15)

For the normalized bump put

    J_T=integral psi(x)^2 w(u0+x/(TL)) dx.

It tends to w(u0)||psi||_2^2>0, independently of X, and the
unnormalized bump's squared norm is J_T/L. Its support is contained
in [T,3T] for large T. Direct change of variables therefore gives

    integral w_XT |g_(T,X)| dt
       = [integral psi(x) w(u0+x/(TL)) dx]/sqrt(L J_T)
       <=C_(w,u0,psi)/sqrt(L).                            (16)

Equations (15)--(16) yield

    |<g_(T,X),U_P>_T|^2
       <=C_(epsilon,w,u0,psi) T^(1/2+2epsilon) A_n^2
                                      ||P||_(I_(q_-))^2/L. (17)

### 5. Actual orthogonal projection and scope

The complex polynomials of degree at most n parametrize V_(T,X)
exactly via U_P. For a finite-dimensional subspace the Hilbert-space
projection identity is

    ||Pi g||_T^2 = sup_(0!=U in V) |<g,U>_T|^2/||U||_T^2.

It follows directly by orthogonality and Cauchy--Schwarz, with equality
at U=Pi g when this is nonzero. Dividing (17) by (13) proves (1).
For fixed eta>0 choose epsilon=eta/4 and use A_n^2/L^2<=T^(eta/2)
beyond an onset to obtain the asserted O(T^(-1/2+eta)) bound.
Take, for example, eta=1/4 to conclude uniform convergence to zero.
Pythagoras gives dist(g,V)^2=1-||Pi g||^2 because ||g||=1.

This calculation uses the retained arithmetic second main term,
its charged analytic error and the actual norm. The older TV envelope
stop does not enter the proof. There is no inference about arbitrary
translate density, actual signed remainders or pointwise Xi signs.
The separate application audit below checks this proof and the named
input hypotheses; it does not audit the arithmetic source manuscript.

### 6. Separate conceptual application audit — 1 November 2026

This is a reproduction of the quantitative specialization, using the
invocation-start SPECIALIZE coverage in
drafts/literature/2026-11-01-l639-projection-audit.md. The audit verifies
(1) and (13) with unchanged quantifiers and arbitrary T,X-dependent
complex coefficients. It supplies no stronger degree range or new
arithmetic theorem. All source statements are used with the qualifications
in the hypotheses; no unread theorem or fourth-moment input is needed.

**Analytic generator and its full remainder.** Put
s_r=1/2+i(t+r/L). The phase in L465/L622 gives
chi(s_r)=exp(-2i theta(t+r/L)) and
chi(1-s_s)=exp(2i theta(t+s/L)), with compatible analytic branches.
Applying the functional equation to the second Hardy factor therefore
gives exactly

    Z(t+r/L) Z(t+s/L)
       = h zeta(s_r) zeta(1-s_s),
    chi(s_r) chi(1-s_s)=h^(-2).

Thus Bettin's a=ir/L,b=is/L have the required signs, even for independent
complex r,s. Their real parts are bounded by 2/L on the stated polydisc;
log Y=L+O(1) throughout the primitive endpoints. Holding these physical
shifts fixed when varying Y is essential. The imported residual is
uniformly O(sqrt(T)L^2). For p=w_XT h, compact support kills both
boundary terms, and

    integral |p'| <= sup|h| integral|w'|
                     + T sup|partial_t h| integral w = O_w(1).

This verifies (2) without differentiating the residual in height.
The t support stays in [T,3T], independent of X. Only fixed-order
phase bounds are used before the later analytic Cauchy extraction.

Write e=exp(c lambda_t/2). The segment formula for theta gives
h-e=c d(r,s,t) with d holomorphic and O(1/T), including on r=s.
Since h and e and their inverses are bounded,
h^(-1)-e^(-1)=-c d/(he). Splitting the two zeta factors into their
poles and J proves that replacing h by e costs O(1/T) in the
complete bracket. Its integrated O(1) cost is absorbed in (4).
In particular no separate 1/c estimate or fixed-order O(T) remainder
is substituted. B, the canceled main expression and hence their
difference E are holomorphic on a neighborhood of the closed polydisc.
Their uniform bounds permit mixed Cauchy derivatives of every order.

**Regular-term contraction and degree constants.** For j<=k, the
coefficient convolution in (5) gives

    (2/q)^j |P_k^(j)(1)|
       = q^(-j) (k+j)!/[j!(k-j)!]
       <= (8N^2)^j/j!.

For j>k the derivative is zero. The sum of squared Legendre
normalizations is N^2/q<=2N^2. This proves (7) for complex
coefficients. Leibniz applied to the polynomial
F=P conjugate(P), with coefficientwise conjugation, then yields
(8), because sum_j binom(m,j)/(j!(m-j)!)=binom(2m,m)/m!.
The finite formula also bounds the monomial coefficient sum of
P_k(2x/q) by 10^k, so Cauchy--Schwarz proves (9), including n=0.
No coefficient sign or T-independence is required.

The conjugate differential operator in s has i^j, not i^(-j).
Consequently its contraction with exp(i(r-s)x) is exactly |P(x)|^2.
Commuting the polynomial differential operators with partial_x^m
shows that c^m contributes L^(-m)F^(m)(x). The sign (-1)^m
in the second endpoint comes from J(-c); it is not a conjugation
choice. Terms m>2n vanish by total derivative order, while uniform
convergence of J's series on the fixed polydisc justifies extraction.
This independently verifies the full regular form (10).

Cauchy's estimate for J on |c|=1 and (8) give the exact relative
loss used in (11). Relative to L||P||_(I_(q_t))^2 it is at most

    rho_n(T)=(4M N^2/L) exp(32N^2/L) ->0.

Here N^2/L=O(L^(-1/3)); no fixed derivative-order assertion is
being extended without a bound. Taking real parts is legitimate
even without first proving each displayed main summand is real.

**Actual Gram and conditioning.** Radius-one Cauchy estimates in the
two independent variables bound partial_r^j partial_s^k E(0,0)
by C_w sqrt(T)L^2 j! k!, which gives (12). For all t in [T,3T],
q_t>=q_->=1/2 eventually, so interval containment compares every
main-form norm with the same ||P||_(I_(q_-)). The nonnegative weight
has mass T. The remaining loss relative to TL is at most

    C_w T^(-1/2) L A_n^2 ->0,
    log(T^(-1/2) L A_n^2)
       = -L/2 + O(L^(1/3) log(L+2)) + O(log L) -> -infinity.

Choose one onset with rho_n<=1/2 and this second loss <=1/4.
This gives exactly (13), uniformly in X and in every complex P.
It is a lower bound on the actual integral, not an inversion of its
leading sine-kernel approximation. It also proves injectivity of the
parametrization P -> U_P in the weighted Hilbert space.

**Pointwise bound, normalization and projection.** On the closed strip
[-delta,1+delta], the factor (s-1)/(s+2) removes the sole zeta pole
and adds no pole. The imported strip theorem with the stated growth
hypothesis interpolates boundary powers 1/2+delta and 0 to
(1+delta-sigma)/2. Its constant is uniform on [1/4,3/4].
For the radius-one scaled Cauchy circles,
sigma=1/2-Im(z)/L lies in that compact interval eventually.
With delta/2<epsilon, the extra height factor from 1/(2L) is
bounded, and removal of the rational factor is uniform at height
comparable to T. The analytic theta increment is O(L|z|/L)=O(1)
from its real-axis value. This verifies (14) on the entire complex
circle, not just at real shifts. Ordinary Cauchy differentiation
then costs j! exactly, as charged by (9) and (15).

For the bump, the substitution t=a+x/L gives squared norm J_T/L
exactly; J_T tends to the fixed positive w(u0)||psi||_2^2 uniformly
in X. Its support lies in [T,3T] for large T. The same substitution
gives (16), with absolute values harmless because w,psi>=0.
The correlation estimate (17) follows by the supremum bound (15)
and is valid for arbitrary complex U_P. Dividing it by (13) yields
T^(-1/2+2epsilon) A_n^2/L^2, with the factor 4 absorbed in C.
The exact complex Hilbert-space variational identity then proves
(1), including the zero-projection case. The choice epsilon=eta/4
and log(A_n)=o(L) proves its stated O(T^(-1/2+eta)) consequence;
Pythagoras gives the distance assertion.

All onsets may depend on the fixed w,u0,psi and epsilon (or eta),
but not X, P or their coefficients. The same L465/L622/L637/L638
input uses remain sufficient; no dependency edge changes. This audit
confirms only the stated microscopic-bump obstruction. Arbitrary
translates, larger dictionaries, signed approximation and initial or
all-degree Xi signs are not inferred. No numerical preview is used
as evidence, and no source-manuscript or formal-proof audit is claimed.

## Mathlib

Full matching coverage was not checked. Legendre orthogonality,
holomorphic Cauchy estimates, finite-dimensional orthogonal projection
and Pythagoras are supporting mathematical tools, not an asserted
Mathlib formalization of the growing actual-Hardy Gram or this bound.
No Lean certificate or absence claim is supplied. The precise external
theorem and formula citations used here are given in the hypotheses.
