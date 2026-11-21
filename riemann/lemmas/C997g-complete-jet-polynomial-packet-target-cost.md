# Corollary 997g: complete data-jet cancellation also suppresses the target

## Hypotheses

Use the COMPLETE response H_n^+(z;mu) in C997c(1), with its original
K_(n+2)=(L_(n+1)^(2)-1)/(n+1), integer n>=2, and set

    J=[15/8,17/8], z_star=1+i/8,
    phi(c)=arccos(1-c/2)+sqrt(c*(4-c))/2.

The branches in phi are real on J. Fix kappa=1 and a curvature A in
C997e's sufficiently large range, before n. This keeps the construction
inside the approved polynomial-packet scope; the proof below uses only
A>0, not that range's analytic asymptotics. Let P_n be a nonzero complex
polynomial of degree at most n. Define the ORIGINAL normalization

    M_n=integral_J exp(-A*n*(c-2)^2)*|P_n(c)|dc,
    dmu_n(c)=M_n^(-1)*1_J(c)*exp(-A*n*(c-2)^2)*P_n(c)
                                      *exp(i*n*(phi(c)-c))dc.       (1)

Impose the n exact complex constraints on the COMPLETE response

    (d/dz)^j H_n^+(2;mu_n)=0, 0<=j<n.                            (2)

No constraint is imposed separately on an asymptotic branch. These are
finite hypothetical slope measures, not actual zeta-zero data. Both
beta terms, both short intervals, both slope cutoffs and K's -1 remain.

## Conclusion

For each n>=2 at least one nonzero P_n of degree<=n satisfies (2)
after (1), and its original total variation is one. There are absolute
constants C<infinity and n_0 such that EVERY choice satisfying (1)-(2)
obeys, for n>=n_0,

    sup_(gamma in J)|H_n^+(gamma;mu_n)|
                              <=C*(n+2)^2*exp(-n/16),             (3)
    |H_n^+(z_star;mu_n)|       <=C*(n+2)^2*exp(-3*n/16).           (4)

The constants are independent of the coefficients and of the fixed
admissible A. Thus (3) supplies the required band bound for any fixed
0<sigma<1/16 eventually, but (4) rules out target retention
|H_n^+(z_star)|>=exp(-a_n), a_n>=0, a_n/n->0, on every unbounded
integer subsequence. For a scalar multiple nu_n=s_n*mu_n meeting that
target threshold at a sufficiently large index, necessarily

    ||nu_n||_TV >= exp(3*n/16-a_n)/(C*(n+2)^2).                    (5)

If the unscaled target value is zero, scalar target normalization is
impossible. This stops the full n-jet cancellation design only. It does
not exclude polynomial packets with fewer or approximate constraints,
arbitrary multipliers, or other mechanisms for uniform suppression.

Step332, 10 November 2026: RESEARCH / POTENTIALLY_NEW, outcome NEGATIVE,
under unchanged pre-invocation EXPLORE review329. This is a local
subclass obstruction using standard finite-dimensional and complex
analysis tools; the assessment did not identify this exact normalized
response statement. No originality certification or RH advance is
asserted. The independent conceptual audit in step334 below accepts
(1)-(16), without changing the hypotheses or bounds.

## Proof

### Reused inputs and why a specialization is needed

Import C997c(4)-(6), including its step322 conceptual audit: the exact
finite complex spectral measures, their supports and total variations.
Its Laguerre estimate comes from L997(4), based on
[NIST DLMF18.14.8](https://dlmf.nist.gov/18.14.E8), with the original
constant subtraction retained. Its measure contracts are the standard
finite-complex-measure Fubini theorem, made precise in that audit by
Axler, *Measure, Integration & Real Analysis*, author version
12 June 2026, 9.10 pp260-261 and 9.41(b) p274, and Tao, *245A, Notes6*,
30 October 2010, Theorem43. Those general inputs are not reproved here.

Also use the standard named rank-nullity theorem and Cauchy's integral
formula for Taylor coefficients. The necessary new specialization is
a degree<n polynomial approximating the target exponential on the
upper spectral interval while remaining small on the lower interval.
A plain upper-center Taylor polynomial does not pay its lower-interval
growth. The extra factor below does. No weighted Bernstein-Markov
estimate, saddle expansion, whole-line Gaussian replacement or
unproved polynomial condition number is needed.

### Exact constraints exist, with the original normalization

For fixed n consider the (n+1)-dimensional complex vector space of
polynomials of degree<=n. Insert its elements in the UNNORMALIZED
density in (1). Each of the n derivatives in (2) is a complex-linear
functional of that polynomial. Indeed all integrations are over compact
sets, and differentiation in z is justified by uniform domination on
compact z sets. Rank-nullity supplies a nonzero element in their common
kernel, without any assertion that the functionals are independent.

A nonzero polynomial has only finitely many zeros on J. The weight is
positive and continuous, so 0<M_n<infinity. Dividing by M_n preserves
the homogeneous constraints, and the real phase in (1) has modulus one.
Consequently ||mu_n||_TV=1 exactly. This is existence, not a numerical
interpolation solve or a bound on coefficients. The following estimates
apply to every exact solution, so coefficient conditioning is irrelevant
to this obstruction.

### The complete response and its two spectral intervals

For the measure (1), C997c gives H(z)=H_n^+(z;mu_n) in the exact form

    H(z)=integral exp(izt)d(nu_U+nu_L)(t),
    supp(nu_U) subset [15*n/8,17*(n+2)/8],
    supp(nu_L) subset [n,n+2],
    ||nu_U||_TV<=U*(n+2)*exp(9*n/32), U=18*exp(27/16),
    ||nu_L||_TV<=L*(n+2)*exp(-n/16), L=8*exp(3/4).          (6)

The narrower upper support follows directly from cn<=t<=c(n+2) and
c in J; the deliberately coarser variation bounds are unchanged from
C997c(5) on I. The signed lower density has its original plus sign.
The identity holds for complex z: both finite compactly supported
Fourier integrals are entire, by dominated differentiation. In
particular, with nu=nu_U+nu_L, (2) implies

    integral exp(2it)*Q(t)dnu(t)=0, deg(Q)<=n-1,             (7)

since H^(j)(2)=i^j integral t^j exp(2it)dnu(t). Only the SUM of
the two spectral measures satisfies these moment identities.

### A polynomial that pays both spectral intervals

Define the upper center b, lower center a and their separation d by

    b=2*n+17/8, a=n+1, d=b-a=n+9/8,
    r=(n+17)/8, x=(t-b)/d,
    ell=ceil(3*n/log(d)), N=n-1-ell.                       (8)

Here log denotes the natural logarithm. For all sufficiently large n,
N>=0 and

    r/d<=1/6, ell*log(7)<=5*n/32, d^(-ell)<=exp(-3*n).      (9)

The first inequality holds for n>=47, since
6(n+17)<=8n+9. The second and N>=0 follow from ell/n->0;
the last follows from ell>=3n/log(d). Fix one n_0 large enough
for all these statements, independently of A and P_n.

For z in J union {z_star} put s=i(z-2). On |x|<1 the function

    f(x)=exp(s*d*x)*(1+x)^(-ell)

is holomorphic. Write T_N(x) for its degree-N Taylor polynomial at zero.
On |x|=1/2, Cauchy's formula gives the coefficient bound

    |[x^j]f|<=B*2^j, B=exp(|s|*d/2)*2^ell.                (10)

Set the following auxiliary polynomial IN THE SPECTRAL VARIABLE t:

    Q_(n,z)(t)=exp(s*b)*(1+x)^ell*T_N(x).                  (11)

It has degree at most ell+N=n-1. This Q is not P_n and does not
replace M_n or the original slope measure in any norm estimate.

On the upper support |x|<=r/d<=1/6. The full geometric bound for the
Taylor tail in (10) is

    |f(x)-T_N(x)|<=B*(2*|x|)^(N+1)/(1-2*|x|)
                          <=(3/2)*B*3^(-(n-ell)).

Multiplying by |exp(s*b)*(1+x)^ell|, with |1+x|<=7/6, gives

    sup_upper |exp(s*t)-Q_(n,z)(t)|
       <=(3/2)*exp(Re(s)*b+|s|*d/2)*7^ell*3^(-n).         (12)

Every endpoint is included. On the lower support, |1+x|<=1/d and
|x|<=1+1/d. The finite polynomial, with (10), is bounded by

    |T_N(x)|<=B*(N+1)*[2*(1+1/d)]^N.

Use N+1<=n, N/d<1, (1+1/d)^N<=exp(N/d)<=e, and
2^ell*2^N=2^(n-1). Equations (9)-(11) yield

    sup_lower |Q_(n,z)(t)|
       <=(e/2)*n*exp(Re(s)*b+|s|*d/2+n*log(2)-3*n).       (13)

This pays the lower interval by its actual fixed width. Treating its
support as a broad interval about b would not give (13). All estimates
are finite inequalities; no interchange of asymptotic expansions or
assumption of separate upper-band moment cancellation was used.

### Uniform band suppression and target cost

By (7), subtract (11) in the COMPLETE integral before separating it:

    H(z)=integral exp(2it)*(exp(s*t)-Q_(n,z)(t))dnu(t).     (14)

On the real support |exp(2it)|=1. Bound the upper part by (12) and
(6), and the lower part by (13), the original exponential itself,
and (6). The scalar estimates log(3)>1 and log(2)<1 follow from
2<e<3. For real z in J, Re(s)=0 and |s|<=1/8. Hence

    Re(s)*b+|s|*d/2<=n/16+9/128.

Using (9), the upper exponential rate is at most
9/32+1/16+5/32-1=-1/2. The lower Q rate is strictly less than
-1/16+1/16+1-3=-2. The lower original exponential has modulus one.
These uniform bounds give

    |H(z)| <= (3/2)*U*exp(9/128)*(n+2)*exp(-n/2)
              +L*(n+2)*exp(-n/16)
              +(e/2)*L*exp(9/128)*n*(n+2)*exp(-2*n),
                                                   z in J.       (15)

At z=z_star, s=-1/8-i and |s|=sqrt(65)/8<9/8. Consequently

    Re(s)*b+|s|*d/2<=5*n/16+47/128.

Now the upper rate is at most
9/32+5/16+5/32-1=-1/4. The lower Q rate is strictly less than
-1/16+5/16+1-3=-7/4. On the lower support
|exp(s*t)|=exp(-t/8)<=exp(-n/8). Thus

    |H(z_star)| <= (3/2)*U*exp(47/128)*(n+2)*exp(-n/4)
                   +L*(n+2)*exp(-3*n/16)
                   +(e/2)*L*exp(47/128)*n*(n+2)*exp(-7*n/4).
                                                                  (16)

For example C=(3/2)*U*exp(47/128)+L+(e/2)*L*exp(47/128) works in
both (3) and (4). All constants are independent of the original
polynomial. Polynomial factors are exp(o(n)), so (4) contradicts the
target threshold on any unbounded subsequence. Complex linearity of H
and ||s_n*mu_n||_TV=|s_n| prove (5). This completes the specified stop.

### Qualifications and unresolved uses

The proof is an exact-response obstruction, not failure of an upper
estimate to prove suppression: (3) actually gives suppression, and
(4) actually gives an incompatible target cost. Existence of the null
polynomial alone would have supplied neither bound. The cutoff points
enter the closed upper support in (6); no analytic extension of the
indicator or omission of endpoint contributions occurs. Both analytic
Laguerre branches are already contained in the exact spectral measures,
as are both beta terms and K's -1. No sign or positivity is imposed.

Only the full n-jet subclass of the approved kappa=1 polynomial family
is stopped. Approximate or fewer jet constraints and arbitrary packet
designs remain undecided. No data derivative norm is asserted for an
experimental reconstruction. The point bridge, selected/both-sign
transfer, C997a(8), original assay, actual reconstruction, signed
recovery, infinite-zero complements, regulator uniformity, L993 and
L984(H) remain unresolved. No RH candidate or infinite-zero argument
is obtained. The analytic estimates above, rather than a sampled
calculation or numerical certificate, supply the proof. The independent
conceptual audit below verifies this specified subclass result.

### Independent conceptual audit — step334, 10 November 2026

RESEARCH / REPRODUCTION under pre-existing SPECIALIZE review332,
completed in step333. The audit accepts (1)-(16), including existence
for every n>=2 and the uniform eventual bounds, without a correction.
This is local verification of a previously unaudited obstruction, not
a stronger theorem, a result beyond the checked sources or an RH claim.

**Contracts and specialization.** Reuse the primary source statements
inspected in review332: Sheldon Axler,
[*Null Spaces and Ranges*](https://linear.axler.net/NullRange.pdf),
author-hosted slide set retrieved 10 November 2026, PDF pp17-24,
the Fundamental Theorem of Linear Maps and its lower-dimensional-map
consequence (rank-nullity); NIST DLMF
[1.9.30-31](https://dlmf.nist.gov/1.9#iii), Cauchy's integral and
derivative formulas, and [1.10.1](https://dlmf.nist.gov/1.10#i),
Taylor expansion on a holomorphic disk. These general theorems are
imported, not reproved. Reuse C997c(4)-(6) and its step322 audit for
the finite complex measures, the original signs and the TV estimates;
its Axler 9.10/9.41(b), Tao Theorem43 and DLMF18.14.8 citations above
retain their original qualifications. No new source hypothesis is needed.
The verification below is necessary because these contracts alone do
not supply the two-band approximation or its original-TV rates.

**Existence, normalization and moments.** Before dividing by M_n,
the density depends complex-linearly on the n+1 polynomial coefficients.
For each fixed n all c and t domains are compact. Equivalently, in the
spectral representation, let T=17(n+2)/8. For |z|<=R the j-th derivative
of exp(izt) is bounded by T^j exp(RT) on either support, an integrable
constant against the finite variation measure. Difference quotients
are dominated as well: for |h|<=1,
|(exp(iht)-1)/h|<=t exp(t). Dominated differentiation, iterated at each
fixed order, proves entire dependence and the derivative formula used
in (7). No uniformity in n is needed for this differentiation.
Thus the n unnormalized constraints form a linear map C^(n+1)->C^n,
whose kernel is nonzero even if some constraints are dependent.

A nonzero polynomial has finitely many real zeros. The positive
continuous weight on the nondegenerate compact J therefore gives
0<M_n<infinity. The phase is real on J, so the absolute density in
(1) integrates to precisely one. Division by the positive scalar M_n
preserves every zero derivative. Conversely, for every normalized
solution, H^(j)(2)=i^j integral t^j exp(2it)d(nu_U+nu_L) gives (7)
for every complex polynomial of degree<n. This does not give separate
moments for nu_U and nu_L, nor any bound on the coefficients of P_n.

**Closed supports and the degree budget.** With c in J, the two extreme
upper endpoints are 15n/8 and 17(n+2)/8, whose midpoint and half-width
are exactly b=2n+17/8 and r=(n+17)/8. The lower interval has midpoint
a=n+1 and half-width one. Hence d=b-a=n+9/8>1; throughout the lower
interval |1+x|<=1/d and |x|<=1+1/d. Throughout the upper interval
|x|<=r/d<=1/6 for n>=47, since 6n+102<=8n+9 there.

The ceiling in (8) gives 0<ell/n<=3/log(d)+1/n->0 and
ell log(d)>=3n. Consequently a single absolute n_0 makes N>=0,
ell log(7)<=5n/32 and all of (9) hold for every n>=n_0. The onset
is eventual, not a statement about the small indices. It depends on
neither A nor a null polynomial. In (11) the total degree is at most
ell+N=n-1, so the very same combined moment identity annihilates it.

**Upper and lower approximations.** The only possible singularity of
f in the closed unit disk is at x=-1, outside the Cauchy circle of
radius 1/2. On that circle |1+x|>=1/2 and
|exp(sdx)|<=exp(|s|d/2), proving (10). Summing the complete Taylor
tail on |x|<=1/6 gives (3/2)B*3^(-(N+1)). Multiplication by
|exp(sb)|(7/6)^ell gives (12), because N+1=n-ell and
2^ell*(7/6)^ell*3^ell=7^ell. This includes both closed endpoints.

On the lower interval every one of the N+1 Taylor terms is at most
B[2(1+1/d)]^N in modulus. Since N<=n-1<d,
(1+1/d)^N<=exp(N/d)<=e and N+1<=n. The factor (1+x)^ell contributes
d^(-ell)<=exp(-3n), including at both endpoints (and vanishes at a).
Finally 2^(ell+N)=2^(n-1), giving exactly the coefficient (e/2)n
and exponent in (13). No Taylor convergence at the lower interval
was assumed: only the finite polynomial is evaluated there.

**Subtraction, rates and quantifiers.** Subtract Q under the combined
integral first. The factor exp(2it) has modulus one for real t, so
(14) may then be estimated separately using (6). For real z in J,
s=i(z-2) has Re(s)=0 and |s|<=1/8, giving the constant 9/128 in
(15). At z_star, s=-1/8-i, and sqrt(65)<9 gives

    -b/8+(9/16)d = 5n/16+47/128.

Using log(3)>1 and log(2)<1, the upper exponents per n are
9/32+1/16+5/32-1=-1/2 on J and
9/32+5/16+5/32-1=-1/4 at the target. The lower-polynomial exponents
are -1/16+1/16+1-3=-2 and -1/16+5/16+1-3=-7/4, respectively.
The untouched lower exponential is bounded by 1 on J and exp(-n/8)
at the target; together with (6) it contributes rates -1/16 and
-3/16. These are precisely all three terms of each of (15)-(16).

Each factor n+2 or n(n+2) is at most (n+2)^2, and every other rate
is at least as negative as the required one. The displayed C following
(16) therefore works simultaneously in (3)-(4). Its constants and the
single n_0 are independent of A and all coefficients. C997e's role is
only to specify the inherited admissible fixed-A scope; none of its
saddle expansions or onsets is used to obtain this uniformity.
No A_n extension is asserted by this audit.

For every fixed 0<sigma<1/16, log(C(n+2)^2)=o(n) proves the stated
eventual band threshold. If a_n/n->0, the logarithm of the target
upper bound divided by exp(-a_n), namely
log C+2log(n+2)-3n/16+a_n, tends to minus infinity. This also holds
on any unbounded integer subsequence. Complex linearity and TV=1
then prove (5); a zero target cannot be made nonzero by scalar scaling.
No numerical sampling, coefficient solve, asymptotic branch deletion,
positivity assumption or infinite-zero interchange enters this audit.

The direct recorded inputs remain C997c and C997e, with the latter's
scope-only role as just specified. C997f, stopped certificates and
unpaid selected-response identities were not used as premises. The
full-jet subclass stop is accepted; every independent gap listed in
the qualifications above remains open.

## Mathlib

Full matching coverage for this polynomial-Gaussian jet-cost statement
has not been checked and is unknown. Rank-nullity and Cauchy's formula
are standard mathematical inputs; no particular Mathlib theorem name
or full formalization is claimed. The Laguerre and complex-measure
inputs retain C997c's coverage qualifications.
