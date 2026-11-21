# Corollary 997y: origin extraction succeeds, but the fixed-disk scalar certificate misses the rate

## Hypotheses

Use C997c's COMPLETE kernel and C997s's original objective, for integer n>=2:

    I=[7/4,9/4], z_star=1+i/8, gamma_j=15/8+j/(4n), 0<=j<=n,
    K(t)=(L_(n+1)^(2)(t)-1)/(n+1),
    g(t)=K(t) exp(-t/2) cosh(3t/8),
    k_n(c,z)=-2 exp(-nc/4) [integral_(cn)^(c(n+2)) g(t)exp(izt)dt
                           -integral_n^(n+2) g(t)exp(izt)dt],
    h(t)=exp(i z_star t)-sum_j A_j exp(i gamma_j t),
    R(c)=k_n(c,z_star)-sum_j A_j k_n(c,gamma_j),
    sum_j |A_j|<=exp(sqrt(n)), epsilon=||R||_C(I),
    E_n=inf_(admissible A) epsilon.

Coefficients are complex. Put m=ceil(sqrt(n)), d=z_star-2,

    Q(z)=((z-2)/d)^m,
    M=Q(z_star)-sum_j A_j Q(gamma_j),
    Omega={c:|c-1|<3/2}, delta= max_(|c|=1/n)|R(c)|,
    T_n=4 exp(1/4)(m+1)m! [8(n+3)]^m,
    U_n=448 exp(20)/(n+1) * exp((81/8+log(2))*n+sqrt(n)).

The complex extension of k_n is defined by its entire antiderivative,
equivalently the fixed-parameter integral proved below. No global
nonvanishing of g, prescribed interpolation jets, positivity, actual-Xi
input, or replacement of the complete residual by pointwise spectral
approximation is assumed. Natural logarithms are used.

## Conclusion

For every admissible A and n>=2, there is an exact finite linear extractor
from the positive-order germ of exp(nc/4)R(c) such that

    1/2 < |M| <= T_n delta,                 log T_n=o(n).       (1)

The original lower-window integral is eliminated exactly, and inversion
of g occurs only in the disk |t|<=1/(8(n+3)), where nonvanishing is proved.
For n>=8 a fully paid, contour-uniform propagation estimate gives

    delta <= U_n^(1-alpha) epsilon^alpha,    alpha=2^(-17),      (2)
    E_n >= (2T_n)^(-131072) U_n^(-131071).                      (3)

In particular (3) has exponential cost

    Lambda=131071*(81/8+log(2)),
    E_n >= exp(-Lambda*n-O(sqrt(n)*log n)).                     (4)

This is a much weaker lower bound than exp(-(1/64-eta)n), eta>0.
It neither disproves nor proves E_n=O(exp(-n/64)).

There is a rigorous limitation on improving (2) while using only a
uniform scalar bound for the ORIGINAL R on this fixed Omega and a
generic analytic power-propagation inequality. Every such scalar bound
V_n valid for all admissible coefficients satisfies, for n>=20,

    V_n >= 7(n+4)/32 * exp(5n/8).                              (5)

For n>=8, every exponent theta_n>0 in a bound

    max_(|c|=1/n)|f(c)| <= C_n ||f||_C(I)^theta_n

valid for ALL analytic f on Omega with sup_Omega|f|<=1, with finite C_n
independent of f, satisfies

    theta_n <= theta_star=log(5/4)/log(10) < 1/10.              (6)

Combining this type of bound with the extractor estimate (1) has a
scalar-prior cost of at least

    (5/8)*(1/theta_star-1) >45/8>1/64                          (7)

per n, even before its other nonnegative losses. This is a limitation
of that certificate, NOT an upper bound on E_n, an instability lower
bound for a residual-specific inverse, or an obstruction for all band
measures. Data-conditioned global bounds, use of further residual-range
structure, changed gauges or other geometries are not excluded.

Step393, 11 November 2026: RESEARCH / POTENTIALLY_NEW / NEGATIVE under
pre-invocation EXPLORE review391, separately approved in step392. The
exact extractor and explicit losses are local mathematical work not
supplied by the inspected sources; originality is not asserted. The
negative outcome parks the specified scalar-prior certificate after
one attempt. Step395's independent conceptual audit below accepts (1)-(7)
with unchanged bounds and scope, and makes the rotated sign in (17)
explicit. C997w's uncapped
construction and C997x's prescribed-family stop remain unchanged.
Actual-Xi positivity, L966/L968 forcing and L984(H) remain open; no RH
candidate is proposed.

## Proof

### Sources and why the kernel-specific work is necessary

The finite Laguerre expansion is NIST DLMF
[18.5.12](https://dlmf.nist.gov/18.5.E12), with degree n+1 and alpha=2.
Analytic parameter integration on a fixed finite segment uses
[1.10(viii), equations 18-19](https://dlmf.nist.gov/1.10.viii);
Cauchy's coefficient estimate uses the derivative formula
[1.9.31](https://dlmf.nist.gov/1.9.E31). These contracts were inspected
in reviews390/391 and step392. Their standard theorems are imported.

For analytic propagation use L. N. Trefethen, *Quantifying the
ill-conditioning of analytic continuation*, BIT Numerical Mathematics
60 (2020), 901-915, DOI
[10.1007/s10543-020-00802-7](https://doi.org/10.1007/s10543-020-00802-7),
[author PDF](https://people.maths.ox.ac.uk/trefethen/trefethen_ac.pdf),
Lemma2.1/proof p904 and Theorems5.1-5.2/proof p908. The standard
maximum-principle comparison and bounded-strip three-lines estimate
are imported, not claimed as new. Below we give the explicit slit-disk
barrier and annular geometry needed for a uniform numerical exponent;
the source's existential pointwise exponent alone would not prove (2).
All functions here extend across the relevant closed disks and segment,
and are globally bounded there. No unbounded strip auxiliary function
is used. The germ inversion, original-cap envelope and their growing-n
costs are not conclusions imported from these sources.

### Entire extension and exact removal of the lower window

Set q(t)=g(t)h(t), an entire function, and

    F(c)=c integral_n^(n+2) q(cu)du,
    D(c)=-exp(nc/4)R(c)/2=F(c)-F(1).                         (8)

On the fixed finite u interval the integrand is jointly continuous
and entire in c. It is uniformly bounded on every compact c set, so
the cited parameter theorem makes F entire. Substitution for positive
real c proves the original kernel identity; entire continuation or
the antiderivative proves it for every complex c. Both windows and
both exponential terms of cosh remain in (8).

Writing q(t)=sum_(k>=0) q_k t^k, compact-uniform convergence permits
termwise integration on the fixed segment. Thus for every k>=0,

    [c^(k+1)]D=b_k q_k,
    b_k=((n+2)^(k+1)-n^(k+1))/(k+1)
       =integral_n^(n+2) u^k du >=2 n^k>0.                  (9)

The lower window F(1) is constant in c after the gauge in (8); it
contributes to none of these coefficients. No estimate discards it.
On |c|=1/n, |D(c)|<=exp(1/4)delta/2. Cauchy's formula, with the order
factorial canceled when passing to Taylor coefficients, gives

    |q_k| <= n exp(1/4)delta/4,      k>=0.                  (10)

Indeed the coefficient of c^(k+1) has bound
exp(1/4)delta*n^(k+1)/2, which is divided by b_k in (9).

### A justified local division and the centered extractor

Write K(t)=sum p_j t^j. DLMF18.5.12 gives, retaining the subtraction,

    p_0=(binomial(n+3,2)-1)/(n+1)=(n+4)/2,
    p_j=(-1)^j binomial(n+3,j+2)/((n+1)j!), 1<=j<=n+1.

For n>=2,

    binomial(n+3,2)/(binomial(n+3,2)-1)<=10/9,
    binomial(n+3,j+2)/binomial(n+3,2)
       =2*(n+1)(n)...(n+2-j)/(j+2)! <=(n+3)^j.

With r=1/(8(n+3)), therefore,

    max_(|t|<=r)|K(t)/p_0-1|
       <=(10/9)(exp(1/8)-1)<10/63<1/2.                    (11)

The strict bound follows from exp(x)<1/(1-x) for 0<x<1,
by comparing the positive power series. Also r<=1/40,
|cosh(3t/8)-1|<=exp(3r/8)-1<1/2, and
|exp((1/2-2i)t)|<=exp(5r/2)<2. Consequently

    v(t)=exp(-2it)/g(t)=exp((1/2-2i)t)/(K(t)cosh(3t/8))

is analytic on a neighborhood of the closed disk |t|<=r and has
modulus <=8/p_0=16/(n+4) there. If v(t)=sum v_j t^j, Cauchy gives

    |v_j|<=16 r^(-j)/(n+4).                                (12)

The centered moment is exactly the finite functional

    M=m!/(i^m d^m) [t^m]{v(t)q(t)}
     =m!/(i^m d^m) sum_(k=0)^m v_(m-k) [c^(k+1)]D/b_k.    (13)

This is an identity because vq=exp(-2it)h(t). Since
|d|=sqrt(65)/8>1, (10)-(12), r<1 and n/(n+4)<=1 yield

    |M|<=4 exp(1/4)(m+1)m! r^(-m) delta=T_n delta.

All factorials and scaling factors have been retained. Only a germ
inverse is used; zeros of K or cosh outside this disk are immaterial.
Since m<=sqrt(n)+1 and m!<=m^m, log T_n=O(sqrt(n)log n)=o(n).

On the other hand |gamma_j-2|<=1/8, so the original complex l1 cap gives

    |M-1|<=exp(sqrt(n))*65^(-m/2)
          <=(e/8)^sqrt(n)<3/8,

using m>=sqrt(n), sqrt(65)>8, e<3 and sqrt(n)>=1. This proves (1),
with the slightly stronger gap |M|>5/8. It is a necessary consequence
for every admissible vector; no jets have been prescribed to A.

### Entire original-cap envelope, with both windows

The same finite Laguerre formula and binomial(n+3,j+2)<=2^(n+3) give

    |K(t)|<=a_n exp(|t|),
    a_n=(2^(n+3)+1)/(n+1)<=2^(n+4)/(n+1).

The separate +1 pays K's subtraction. Since |z_star|<17/8 and
15/8<=gamma_j<=17/8,

    |g(t)|<=a_n exp(15|t|/8),
    |h(t)|<=(1+exp(sqrt(n))) exp(17|t|/8),
    |q(t)|<=a_n(1+exp(sqrt(n))) exp(4|t|).                  (14)

In the closed disk |c-1|<=3/2, |c|<=5/2 and Re(c)>=-1/2. The fixed
parameter formula bounds F(c) by 5a_n(1+exp(sqrt(n)))exp(10(n+2));
F(1) is bounded by 2a_n(1+exp(sqrt(n)))exp(4(n+2)). Returning to R
costs 2exp(n/8). Thus

    sup_(|c-1|<=3/2)|R(c)|
       <=14 a_n(1+exp(sqrt(n)))exp(10(n+2)+n/8)<=U_n.       (15)

The real-exponent cosh estimate in (14) retains both beta terms;
no real-t Laguerre estimate has been extended to complex t. The
original coefficient cap, target growth, lower window and gauge
have all been paid explicitly.

### Explicit contour-uniform propagation in the prescribed disk

Let f=R/U_n and p=epsilon/U_n. We have 0<p<=1: if epsilon=0,
analyticity through the interval gives R identically zero, contradicting
(1). If p=1 the desired propagation bound is immediate.

For 0<p<1, in the slit disk {|c-2|<1/2}\I put w=4(c-2) and

    G(c)=log|w+sqrt(w^2-1)|,

with the exterior branch characterized by |w+sqrt(w^2-1)|>1.
This is the usual harmonic Green function of [-1,1], composed with w;
it is continuous with value zero on the slit. The identity
w=(zeta+zeta^(-1))/2, |zeta|=exp(G), gives

    sinh(G)<=|w|<=cosh(G).

Hence on |c-2|=1/2, G>=arcosh(2)>1, since cosh(1)<2.
On |c-2|<=1/8, G<=arsinh(1/2)<1/2. Apply the standard logarithmic
maximum-principle comparison to log|f| and the harmonic majorant
(1-G)log p: on I the latter is log p, while on the circular boundary
it is nonnegative. The endpoint values are continuous and f is analytic
through them. Therefore

    sup_(|c-2|<=1/8)|f(c)|<=p^(1/2).                       (16)

Zeros of f cause no difficulty for the subharmonic log|f| comparison.

For j=0,...,16 let x_j=2-j/8. Each disk |c-x_j|<=1/2 lies in the
closed Omega, where |f|<=1. The three-circle consequence of the
bounded-strip three-lines theorem, on radii 1/8,1/4,1/2, says that
a bound p^a on the inner disk gives p^(a/2) on the middle disk.
Explicitly use c=x_j+exp(w) in the annulus; the analytic function is
bounded and periodic in Im(w), so the cited strip theorem applies,
with weight log(2)/log(4)=1/2. A zero inner maximum is handled by
the identity theorem. The next inner disk is contained in the current
middle disk because |x_(j+1)-x_j|=1/8.

Starting from (16) and applying this sixteen times proves

    sup_(|c|<=1/8)|f(c)|<=p^(2^(-17)).

For n>=8 this covers the complete circle |c|=1/n. It proves (2)
without an n-dependent hidden constant. Combining (1) and (2) proves
(3). In (15), log U_n=(81/8+log 2)n+O(sqrt(n)+log n), so (4) follows.
The explicit chain is deliberately just one valid geometry inside
the already prescribed Omega; no optimal propagation exponent is claimed.

### An unavoidable global cost for the original residual class

Take the admissible choice A_j=0 for all j. For u>=0, every coefficient
of K(-u) is nonnegative, and K(-u)>=p_0. At c=-1/2,

    F(-1/2)=-integral_(n/2)^(n/2+1)
                  K(-u)exp(5u/8)cosh(3u/8)exp(-iu)du.

For -exp(i(n+1)/2)F(-1/2), the integrand phase lies between -1/2
and 1/2. The real part of its unit phase factor is at least
cos(1/2)>=7/8, and
exp(5u/8)cosh(3u/8)>=exp(u)/2. Therefore

    |F(-1/2)|>=7(n+4)/32 * exp(n/2).                       (17)

C997c's audited real-t bound |g(t)|<=2(n+2)exp(3t/8), including the
subtraction, applies on [n,n+2]. The target contributes exp(-t/8), so

    |F(1)|<=4(n+2)exp((n+2)/4).

The ratio of this upper bound to the lower bound in (17) is at most
(128/7)exp(1/2-n/4). For n>=20 this is <1/2: exp(9/2)>256/7,
already implied by the first six terms of exp(4). Thus the reverse
triangle inequality in the COMPLETE (8) gives

    |R(-1/2)|>=exp(n/8)|F(-1/2)|
              >=7(n+4)/32 * exp(5n/8).

Although -1/2 is on the boundary of Omega, R is entire and continuous
there, so its value is a limit of values inside Omega. This proves (5)
for every scalar bound valid on the whole original residual class.
It is not a lower bound on the global norm of a minimizing residual.

### Why improving only the generic propagation exponent cannot pay

For a positive integer N take the bounded analytic test function

    f_N(c)=((c-2)/(5/2))^N.

Its supremum on Omega is 1, its data norm on I is 10^(-N), and
|f_N(0)|=(4/5)^N. The value at zero is at most its maximum on |c|=1/n
by the maximum-modulus principle (the circle and its interior lie in
Omega for n>=3; use n>=8 here). Any asserted generic estimate in (6)
therefore gives (4/5)^N<=C_n 10^(-N theta_n). Sending N to infinity
for FIXED n proves theta_n<=theta_star. This remains so even if
f(1)=0 is imposed: multiply the witnesses by 2(c-1)/3, bounded by one
on Omega; the additional fixed factors disappear on division by N.
Finally (5/4)^10<10, exactly 9765625<10485760, proves theta_star<1/10.

These test functions need not be residuals; they test precisely the
generic bounded-analytic inequality used for propagation. With such
an estimate applied to R/V_n, (1) can yield only the certificate

    epsilon >= (2T_n C_n)^(-1/theta_n)
                         V_n^(-(1-theta_n)/theta_n).        (18)

For the unrestricted analytic class C_n>=1 by the constant function;
T_n>1. For n>=20 the prefactor 7(n+4)/32 in (5) is >1. Thus the
right side of (18), whatever permitted V_n and theta_n are used, is
at most exp(-(5/8)(1/theta_star-1)n), which proves the scoped cost
statement (7). The comparison uses an upper bound on the strength
of THIS lower certificate, not an upper bound on epsilon or E_n.
Using a residual-specific propagation theorem instead would require
new information and is not covered by this stop. Nor has every
possible gauge/extractor norm been optimized or excluded.

### Verification and retained gaps

The proof is analytic and all-n; no finite sampling establishes (1)-(7).
The companion exact-arithmetic check in
`scripts/adaptive-slope/slope-origin-check-393.py` checks the germ
normalization on finite rational test vectors and selected exact scalar
inequalities, saving its complete certificate in
`scripts/adaptive-slope/slope-origin-check-393.json`. It is a diagnostic
check of the written formulas, not a separate conceptual audit.

The fixed-domain original-residual scalar-prior certificate is parked.
The lower rate (4) cannot decide C997s's capped bridge. C997a(8),
selected/both-sign transfer, assay/reconstruction, complements and
regulators, L993, L984(H), signed forcing and actual-Xi positivity
remain unpaid. This result neither changes the frequency grid/cap nor
imports a theorem from another notebook.

### Independent conceptual audit — step395, 11 November 2026

RESEARCH / REPRODUCTION under pre-invocation EXPLORE review393,
separately source-approved in step394. This audit accepts (1)-(7).
It establishes an audited local input, not a stronger rate, a new
discovery beyond the checked sources, or an RH candidate. The only
textual repair is to exhibit the minus sign in the positive rotated
quantity used in (17); the modulus conclusion and all constants stay
unchanged. The actual task is proof_audit / conceptual_audit.

**Input and source contracts.** Checked C997c's complete two-window
kernel and its real-t bound, including its retained Laguerre subtraction,
and C997s's exact grid, target, complex coefficient cap and objective.
Only these two local mathematical inputs are used. Reuse the inspected
DLMF and Trefethen contracts cited above and approved in review393;
there is no new source hypothesis or missing essential theorem here.
C997w/x are contrasts, not inputs. Full matching Mathlib coverage
remains unchecked; this audit is informal, not Lean verification.

**Germ and inverse.** On each compact c set the fixed u segment in
(8) gives compact-uniform analytic integration. Its positive-order
coefficients are b_k q_k with b_k>0 as in (9), independent of the
lower-window constant. On the full Cauchy circle Re(nc/4)<=1/4, division by
b_k>=2n^k indeed gives (10) for every k, with no missing factorial.
The exact p_0=(n+4)/2 uses the subtraction. The normalized polynomial
tail is bounded by (10/9)(exp(1/8)-1)<10/63. Thus |K|>p_0/2
on the closed inverse disk; |cosh(3t/8)|>1/2 there as well.
The numerator of v has modulus less than 2, giving 8/p_0 in (12).
Strict inequalities on this compact disk give a zero-free neighborhood,
as required for Cauchy. Multiplication by v changes q to exp(-2it)h
exactly, so (13) retains m!, i^m and d^m. Summing its m+1 terms
gives precisely T_n. Since |gamma_j-2|/|d|<=1/sqrt(65), the original
complex l1 cap gives |M-1|<3/8 and hence the stated strict gap.
The bound m<=sqrt(n)+1 proves the asserted sublinear logarithmic cost.

**Complex envelope and all contour points.** The finite polynomial
estimate includes a separate +1 for K's subtraction. In (14) the
exponents are 1+1/2+3/8=15/8 for g and at most 17/8 for h,
hence 4 for their product. On closed Omega, the upper integral costs
2|c|<=5, the lower one costs 2, and the gauge costs 2exp(n/8).
Using a_n<=2^(n+4)/(n+1) and 1+exp(sqrt(n))<=2exp(sqrt(n))
gives the factor 448 and exponent (81/8+log 2)n in U_n.
No real-t Laguerre inequality is used on a complex contour.

In the slit disk the exterior square-root branch has |zeta|>1,
and its Green function is harmonic off the slit and tends to zero
at both slit endpoints. The relations sinh G<=|w|<=cosh G give
G>1 on the outer circle and G<1/2 on the inner disk off the slit.
The majorant (1-G)log p is >=0 on the outer circle, and equals
log p on the slit; subharmonic comparison therefore has the stated
direction. On the slit itself the original data bound suffices.
All outer disks satisfy |x_j-1|+1/2<=3/2. Tangency to the boundary
is allowed because R is entire and (15) holds on the closed disk.
Apply the annular step for j=0,...,15, not an extra seventeenth step:
its middle disk contains the next inner disk. Starting at exponent
1/2 gives exponent 2^(-17) at x_16=0. The entire circle |c|=1/n
lies there for n>=8, including equality n=8. Thus no angular sector
or boundary point is omitted. Inverting the exponent gives 131072
and (1-alpha)/alpha=131071 in (3); the remainder in (4) follows
from log T_n=O(sqrt(n)log n) and log U_n=kappa*n+O(sqrt(n)+log n).

**Scalar prior and exact scope.** For A=0 the negative-t integral
has a leading minus sign. Taking the real part of
-exp(i(n+1)/2)F(-1/2) puts its unit phase in [-1/2,1/2].
The elementary cosine bound 1-(1/2)^2/2=7/8, K(-u)>=p_0,
and cosh(3u/8)>=exp(3u/8)/2 prove (17). The real-t input applies
only to F(1), giving its displayed upper bound. For n>=20 the ratio
is at most (128/7)exp(-9/2)<1/2, because
exp(9/2)>exp(4)>643/15>256/7. The factor 2 in R then cancels
this one-half loss. Continuity at -1/2 transfers its boundary value
to the supremum over open Omega. This proves a lower bound on any
single prior valid for ALL admissible residuals; it proves no such
growth for a minimizing residual.

The polynomials f_N have supremum 1 on open Omega (a supremum,
not an attained maximum), data norm 10^(-N), and value (4/5)^N
at zero. Maximum modulus on |c|<=1/n and then N->infinity with
n FIXED prove (6), even with finite n-dependent C_n. The remark
about f(1)=0 changes only fixed factors in this witness argument.
For the unrestricted analytic class in (6), the constant function
forces C_n>=1. Together with T_n>1, V_n>=exp(5n/8) for n>=20
and theta_n<=theta_star<1/10, this makes the right side of (18)
at most exp(-(5/8)(1/theta_star-1)n). This is an upper bound on
the numerical strength of the displayed LOWER certificate, not on
epsilon or E_n. Polynomial witnesses are not asserted to be residuals.
The restricted f(1)=0 remark alone is not used to assert C_n>=1.

**Evidence and decision.** Read and replayed the entire finite diagnostic
script cited above. All ten rational test cases at n=2,8,17,64,256
(zero and complex vectors), their germ identities and four scalar
checks pass; the certificate's failures array is empty. Inspected
the complete exact scalar values: alpha=1/131072, exponential partial
sum 643/15 versus 256/7, 9765625<10485760 and 45/8>1/64.
The artificial lower-window constant tests algebra only; these finite
checks neither evaluate the actual lower integral nor prove the
all-n contour or inverse assertions. Those are established by the
analytic arguments checked above. The weak rate and narrowly scoped
scalar-prior stop are retained. No optimization or second attempt
on the parked generic fixed-disk certificate is justified by this audit.

## Mathlib

Full matching coverage for the complete-kernel germ extractor and its
quantitative propagation/obstruction is unchecked and unknown. Cauchy,
finite polynomial expansion and maximum-principle facts above are
ordinary supporting mathematics, imported by the precise cited sources;
no Mathlib theorem is an input and no Lean verification is claimed.
