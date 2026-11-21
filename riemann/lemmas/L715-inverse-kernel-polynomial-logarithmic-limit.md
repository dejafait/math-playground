# Lemma 715: normalized logarithmic limit of the exact inverse-kernel polynomial

## Hypotheses

Use L714's exact polynomial, with U=121/64, n=12q+3, q>=1,
N=n-1 and

    H_n(zeta)=sum_(j=0)^N b_(n,j)*zeta^j,
    b_(n,j)=(-1)^j*n^N/[j!*(N-j)!]
                         *product_(k=1)^N (U-j*k/n^2).

In particular H_n(0)=n^N*U^N/N!>0. L714 Section 3 establishes
that all its N roots rho_(n,k), counted with multiplicity, are
real and strictly greater than one. Only the coefficients and that
root argument from L714 are used here, not its contour estimates
or signed-remainder assertions.

Let ell_n be the analytic logarithm of H_n(zeta)/H_n(0) on
|zeta|<1 with ell_n(0)=0. The original fixed actual bump and all
finite-family parameters in L714 are unchanged; this statement
does not require or supply an analytic continuation of that bump.

## Conclusion

There is a single holomorphic function F on |zeta|<1 such that

    ell_n(zeta)/n -> F(zeta) locally uniformly,        (1)
    F(0)=0.

The following explicit real inverse identifies this function uniquely.
For 0<t<1 set

    g(t)=-t*log(t)-(1-t)*log(1-t)
                        +integral_0^1 log(1-t*s/U)ds,
    J(t)=integral_0^1 s/(U-t*s)ds,
    X(t)=t/(1-t)*exp(J(t)).                           (2)

X is a strictly increasing bijection from (0,1) onto (0,infinity).
Write t(x)=X^(-1)(x). For every 0<x<1,

    F(-x)=g(t(x))+t(x)*log(x)
         =-log(1-t(x))
            +integral_0^1 [log(1-t(x)*s/U)
                           +t(x)*s/(U-t(x)*s)]ds.    (3)

Thus (3) together with holomorphy specifies one analytic limit,
not an unspecified subsequential limit. A measure representation
valid everywhere in the disk is given in the proof. In particular
F'(0)=-exp(-1/(2U))=-exp(-32/121).

This is a specialization of a known coefficient-profile theorem,
not a new general zero-limit theorem or a claim of originality.
The local specialization passed the separate conceptual audit in
Section 5 (step 179, 3 November 2026), including its L714 root input.
It supplies only the polynomial component of the inverse kernel's
exponential scale. No rate or nonvanishing assertion for p_n, K_n
or R_n, no relative asymptotic for their integrals, no boundary
limit at |zeta|=1, and no RH candidate follows. The resolvent and
fixed signed bump cancellation, other frequencies/comb/tails/moments,
angular persistence, complementary defect, amplitude/full charge,
H/support and Xi realization remain open.

## Proof

### 1. Source import and exact coefficient profile

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-03-signed-bump-polynomial-zero-limit.md`.
The imported result is J. Jalowy, Z. Kabluchko and A. Marynych,
*Zeros and exponential profiles of polynomials I: Limit distributions,
finite free convolutions and repeated differentiation*,
[arXiv:2504.11593v1](https://arxiv.org/pdf/2504.11593v1),
15 April 2025, Definitions 1.1--1.2, p.3, and Theorem 2.2(a),(b),(e),
pp.5--6. For nonnegative-coefficient polynomials of degree at most n,
an exponential profile on an open interval (a,b) and eventually
nonpositive roots give weak convergence of the zero measures on
[-infinity,0], counting any missing degree at infinity. The limiting
Cauchy transform satisfies x*G(x)=(exp(-g'))^(-1)(x) for x>0;
the masses at zero and infinity are a and 1-b. General convergence
and uniqueness are imported. We verify this array's hypotheses
and its bounded complex logarithm below.

To handle the theorem's integer indexing, use the displayed formula
for H_n for every integer n>=2 as an auxiliary array. It agrees
exactly with the required array whenever n=12q+3. L714's Section 3
root argument applies to these additional integer indices as well:
its only relevant inequality is

    (k/n^2)*N <= (n-1)^2/n^2 < 1 < U,    1<=k<=N.

Its N Euler factors each reduce the multiplicity at 1 by one and
preserve the degree. New roots lie in the gaps between distinct
existing roots and to the right of the largest root, hence strictly
above 1. Therefore all N roots lie strictly above one after all
factors, for every n>=2. This checks
the applicability of the existing proof, without importing other
finite-family assertions at these auxiliary indices. Set H_1=1;
this single initial polynomial does not affect any limit.

Define the reflected normalized polynomial

    A_n(x)=H_n(-x)/H_n(0)=sum_(j=0)^n a_(n,j)*x^j,
    a_(n,j)=binom(n-1,j)
                *product_(k=1)^(n-1) (1-j*k/(U*n^2)), 0<=j<n,
    a_(n,n)=0.                                      (4)

All coefficients in the stated range j<n are strictly positive,
since j*k/n^2<1<U. Its degree is n-1 and its roots are -rho_(n,k)<-1.

Fix 0<t<1 and put j=floor(n*t). For sufficiently large n, j<n.
The standard Stirling expansion
[DLMF 5.11.1](https://dlmf.nist.gov/5.11#E1), applied to the three
factorials in binom(n,j), gives, uniformly for j/n in any compact
subinterval of (0,1),

    log binom(n,j)/n
       =-(j/n)*log(j/n)-(1-j/n)*log(1-j/n)+O(log(n)/n).

The exact relation binom(n-1,j)=(1-j/n)*binom(n,j) changes this
by O(1/n) on such a subinterval. This is the necessary factorial
specialization; no special-function asymptotic for H_n is assumed.

For 0<=a,s<=1 the function f_a(s)=log(1-a*s/U) is continuous,
and its s-derivative has absolute value at most 1/(U-1).
Also |f_a(s)|<=-log(1-1/U). The right Riemann sum with its last
term removed consequently satisfies the uniform bound

    |(1/n)*sum_(k=1)^(n-1) f_a(k/n)-integral_0^1 f_a(s)ds|
       <=[-log(1-1/U)+1/(U-1)]/n.                    (5)

Taking a=j/n and then j/n->t proves from (4) that

    lim_(n->infinity) log(a_(n,floor(n*t)))/n=g(t).   (6)

This verifies Definition 1.2 with the profile interval (0,1).
The condition outside its closure is empty; that definition imposes
no endpoint value. In particular a_(n,n)=0 is allowed, and is not
mistaken for a finite profile value at t=1. Neither n-1 nor q is
used as the normalization in (6).

Differentiating the integral in (2) is legitimate since U-t*s>=U-1>0.
It gives

    g'(t)=log((1-t)/t)-J(t),
    g''(t)=-1/t-1/(1-t)-integral_0^1 s^2/(U-t*s)^2 ds <0. (7)

J is bounded on [0,1], so g'(0+)=+infinity and g'(1-)=-infinity.
Consequently X=exp(-g') has precisely the bijection property in (2).

### 2. Imported zero convergence with the actual degree normalization

The cited theorem now applies to A_n. Let

    mu_n=(1/n)*sum_(k=1)^(n-1) delta_(-rho_(n,k))
                                  +(1/n)*delta_(-infinity).

It gives mu_n -> mu weakly on the one-sided compactification
[-infinity,0], for one probability measure mu, not just along
subsequences. The closed support constraint gives
supp(mu) contained in [-infinity,-1]. Part (e), with a=0,b=1,
also gives mu({-infinity})=0. Its Cauchy transform, using value
zero at the point at infinity, satisfies

    G_mu(x)=integral 1/(x-y) mu(dy),
    x*G_mu(x)=t(x),                      x>0.         (8)

The missing degree is exactly the mass 1/n used above. Restricting
this full sequence to n=12q+3 preserves its limit and uses exactly
the requested normalization n^(-1). The auxiliary extension has
not changed any original polynomial or selected a subsequential law.

### 3. Uniform complex logarithm, including escaping roots

Push mu_n and mu forward by the continuous map on [-infinity,-1]

    y -> -1/y, with -1/(-infinity)=0,

to obtain probabilities kappa_n and kappa on [0,1]. Thus

    kappa_n=(1/n)*sum_(k=1)^(n-1) delta_(1/rho_(n,k))
                                        +(1/n)*delta_0,
    kappa_n -> kappa weakly.                         (9)

For |zeta|<1 and 0<=a<=1 use the logarithm

    K(zeta,a)=log(1-zeta*a)
            =-sum_(m=1)^infinity zeta^m*a^m/m.

For every fixed r<1 this series converges uniformly on
|zeta|<=r, 0<=a<=1 and has absolute bound -log(1-r).
In particular K(zeta,0)=0: roots escaping to infinity cause no
unbounded logarithmic-potential term. The factorization in L714
and the normalization at zero give the exact identity

    ell_n(zeta)/n=integral K(zeta,a) kappa_n(da).      (10)

Indeed both sides, after multiplication by n and exponentiation,
give H_n(zeta)/H_n(0), and both vanish at zero. The zero-free
disk fixes this analytic branch uniquely.

Define

    F(zeta)=integral_0^1 K(zeta,a) kappa(da)
           =-sum_(m=1)^infinity zeta^m/m
                                     *integral_0^1 a^m kappa(da). (11)

Weak convergence in (9) gives convergence of every moment in (11).
For a cutoff M the difference of the finite series converges
uniformly on |zeta|<=r; the sum of both tails is at most
2*sum_(m>M) r^m/m, which tends to zero. This proves (1), uniformly
on every such disk. The same series shows that F is holomorphic
and F(0)=0. No unnormalized integral of log|y| is used or needed.

### 4. Identification and normalization check

For 0<x<1, differentiation of (11), or bounded differentiation
under its integral, yields

    d/dx F(-x)=integral a/(1+x*a) kappa(da)
              =G_mu(x)=t(x)/x.                      (12)

The middle equality is exactly the reciprocal change of variables
in (9); both kernels vanish at infinity. Now set
E(x)=g(t(x))+t(x)*log(x). The inverse in (2) is differentiable
with positive derivative, by (7). Since g'(t(x))+log(x)=0,
differentiation gives E'(x)=t(x)/x. As x decreases to zero,
t(x) decreases to zero, g(t(x)) tends to zero, and

    t(x)*log(x)=-t(x)*g'(t(x)) ->0

by (7), boundedness of J, and t*log(t)->0. Also F(-x)->F(0)=0.
Thus (12) determines the same integration constant and proves
the first equality of (3). Substituting (7) into g(t)-t*g'(t)
gives the second equality, including its plus sign before t*s/(U-t*s).
An analytic function on the connected unit disk is uniquely
determined by its values on (-1,0), so (3) identifies all of (11).

For a direct check of sign and degree normalization, (2) gives
t(x)/x -> exp(-J(0))=exp(-1/(2U)) as x decreases to zero.
Equation (12) therefore yields the asserted F'(0). Independently,
the exact first coefficient in (4) gives

    ell_n'(0)/n
       =-(n-1)/n*product_(k=1)^(n-1) (1-k/(U*n^2)).

The logarithm of the product is
-n*(n-1)/(2U*n^2)+O(1/n), because the sum of squared factors
k^2/(U^2*n^4) is O(1/n). Restoring the negative prefactor gives
ell_n'(0)/n -> -exp(-1/(2U)), in agreement with (12),
and checks both the reflection sign and the normalization by n.

All assertions concern the exact polynomial logarithm. Uniformity
on compact subdisks does not justify a limit at the boundary,
an interchange with a noncompact resolvent integral, or a lower
bound for a complex signed bump integral. L714's earlier reduction
and the recorded absolute-contour and positive-blend stops retain
their stated qualifications.

### 5. Separate conceptual audit — 3 November 2026, step 179

**Verdict: accepted within the stated open-disk scope.** The audit used
the invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-03-polynomial-log-limit-audit.md`.
No conclusion, formula or direct mathematical input needed correction.
This validates a specialization of the cited theorem; it is not a new
zero-distribution theorem or a signed-rate result.

The primary version cited in Section 1 was inspected at Definitions
1.1–1.2, p.3, Theorem 2.2(a),(b),(e), pp.5–6, Theorem 5.2's statement,
p.20, and its uniqueness proof, pp.24–25, together with Section 5.2,
pp.25–27. The arbitrary-array, missing-degree and open-profile-interval
conventions agree with (4), (6) and (8). In particular, no value at
t=1 is required and no limiting measure is assumed before applying
the theorem. The source's proof of Theorem 2.2 first normalizes by
A_n(1); its inverse-transform relation depends on g', so it applies
to this unshifted coefficient profile as written. The normalization
at zeta=0 is separately fixed in Section 4. General convergence and
uniqueness remain cited inputs, not local reproofs. DLMF 5.11.1 was
checked on the positive real factorial arguments used in Section 1.

L714's coefficient definition, factorization (4), Euler identity (9)
and Section 3 were checked in full for this input. The Euler identity
acts diagonally on each monomial and reproduces b_(n,j) exactly. For
each positive-root polynomial, the derivative and endpoint values in
L714 (10) locate one new simple root in each indicated gap and one
above the largest root. At an existing root of multiplicity m_i,
the remaining factor is nonzero because alpha*r_i*m_i is nonzero.
The leading coefficient is multiplied by U-alpha*N>0; the inherited
N-s multiplicities and s new roots therefore exhaust the degree.
Starting at (1-zeta)^N removes the multiplicity at one after exactly
N operations. These checks use only n>=2 and U>1, not the congruence
or parity of n. Thus the auxiliary array and its restriction to
n=12q+3 are valid, and every normalization remains 1/n rather than
1/(n-1) or 1/q. This replay is needed to audit the root hypothesis;
L714's contour, inversion and residue assertions are not certified.

The product in (4) has factors bounded below by 1-1/U>0. The
Riemann-sum bound (5), the compact-interior factorial estimate and
continuity in j/n prove the required profile. In (7), both the
negative sign of the integral in g'' and the positive sign of J in
X=exp(-g') are correct. Bounded J gives both endpoint limits of X.
The root measures have mass one with the explicit missing-degree
atom 1/n; their closed support passes to the limit. The reciprocal
map is continuous at minus infinity. For clarity, if
m_(n,k)=integral a^k kappa_n(da) and m_k=integral a^k kappa(da), then
for every integer M>=1 and 0<r<1 the exact proof in Section 3 gives

    sup_(|zeta|<=r) |ell_n(zeta)/n-F(zeta)|
      <= sum_(k=1)^M (r^k/k)*|m_(n,k)-m_k|
           +2*r^(M+1)/[(M+1)*(1-r)].

The finite sum tends to zero for fixed M, and the displayed tail
tends to zero as M increases. This verifies the order of limits and
uniformity on every closed subdisk. The kernel is zero at reciprocal
root zero, so the unbounded-potential issue in JKM Remark 5.4, p.26,
does not occur. Exponentiation and the common value zero at the origin
fix the logarithm without a hidden multiple of 2*pi*i.

Finally dF(-x)/dx is +G_mu(x), whereas F'(0) is negative. The
reciprocal substitution in (12), the cancellation of the t'(x) terms
in E'(x), and t(x)*log(x)->0 establish the same integration constant.
The integral formula (3) and the independent first-coefficient limit
both retain their signs. The identity theorem then identifies the
analytic function throughout the disk. No boundary passage,
noncompact convolution interchange, nonvanishing of p_n/R_n or
signed lower rate was used. All such independent gaps remain open,
with log(0)=-infinity retained for any later signed-rate comparison.

## Mathlib

Full matching coverage is not checked. No formalization is claimed
for the JKM profile theorem, this varying coefficient array, or (1)--(12).
Weak convergence against bounded continuous functions, power-series
uniform convergence, analytic logarithms, Stirling's formula and
the identity theorem are supporting ingredients, not an identified
Mathlib theorem for this exact limit. Unknown availability is not
evidence of absence.
