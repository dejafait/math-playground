# Corollary 997z: the exact centered-moment representing norm has exponential cost

## Hypotheses

Retain the COMPLETE kernel of C997c and C997s, for integer n>=2:

    I=[7/4,9/4], z_star=1+i/8, gamma_j=15/8+j/(4n),
    K(t)=(L_(n+1)^(2)(t)-1)/(n+1),
    g(t)=K(t)exp(-t/2)cosh(3t/8),
    k_n(c,z)=-2exp(-nc/4)[integral_(cn)^(c(n+2)) g(t)exp(izt)dt
                            -integral_n^(n+2) g(t)exp(izt)dt].

The extension in c is entire, using the fixed-parameter definition in
C997y(8). Let S_n be the complex span of the target column and the
n+1 band columns, restricted to I. Let m=ceil(sqrt(n)), d=z_star-2,
and define the COMPLEX-LINEAR functional from C997y(13):

    D_f(c)=-exp(nc/4)f(c)/2,
    b_k=((n+2)^(k+1)-n^(k+1))/(k+1),
    v(t)=exp(-2it)/g(t)=sum_(j>=0) v_j t^j near zero,
    M_n(f)=m!/(i^m d^m) sum_(k=0)^m v_(m-k)[c^(k+1)]D_f/b_k. (1)

Here g(0)=(n+4)/2 is nonzero. C997y supplies the justified local reciprocal.
Restriction to I determines the entire function by the identity theorem,
so (1) is well defined even without a unique column representation.

An exact representing measure means a finite complex Borel measure nu
on I satisfying the BILINEAR equality integral_I f dnu=M_n(f) for every
f in S_n. The norm is actual complex total variation. No coefficient cap
is imposed when taking the norm of a functional on this linear span.
C997s's separate residual objective retains its cap exp(sqrt(n)).

## Conclusion

Put

    C_0=18exp(27/16)+8exp(3/4),
    rho=log(8sin(1/4))+1/16 > 7/16 > 1/64.

For every integer n>=64 there is an explicit BAND-ONLY f_n in S_n,
with coefficient sum of moduli exactly one, such that

    |M_n(f_n)| >= (1/2) sin(1/4)^n 4^(-m) >0,             (2)
    ||f_n||_C(I) <= C_0(n+2) exp(-n/16)8^(-n).            (3)

Consequently

    ||M_n||_(S_n,C(I))
       >= exp(rho*n)/(2C_0(n+2)4^m),
    liminf_(n->infinity) log||M_n||/n >= rho >7/16.        (4)

Every exact representing nu satisfies the same lower bound as (4).
Thus no constants C<infinity and 0<eta<1/64 can give
||nu_n||_TV<=C exp((1/64-eta)n) for all sufficiently large n. Indeed
this obstruction already occurs on the band subspace alone.

Step398, 11 November 2026: RESEARCH / POTENTIALLY_NEW / NEGATIVE under
the unchanged pre-invocation EXPLORE review396, separately approved in
step397. This is an actual-span lower bound, not merely a failure of an
upper estimate or an independently adjustable endpoint model. The
operator-specific bound was not supplied by the checked sources;
originality beyond those sources is not asserted. The proof was
unaudited at step398. The independent conceptual audit in step400 below
accepts (2)-(4) for every integer n>=64, with unchanged bounds and scope.

This stops the requested exact centered-moment norm target. It does
NOT bound the capped E_n from above, refute its desired lower bound,
or exclude approximate moment representation with paid leakage.
Neither actual-Xi positivity, forcing, nor any RH claim is established.

## Proof

### Reused inputs, duplicate checks and the needed new calculation

Use C997c(4)-(6)'s real-t variation estimates and C997s's original
kernel/grid without changing their hypotheses. The underlying standard
Laguerre inequality is NIST DLMF [18.14.8](https://dlmf.nist.gov/18.14.E8),
already specialized with degree n+1, alpha=2 and the constant subtraction
in C997c. Specifically, that local input gives

    |g(t)|<=2(n+2)exp(3t/8), t>=0,
    T_U=18exp(27/16)(n+2)exp(9n/32),
    T_L=8exp(3/4)(n+2)exp(-n/16),                         (5)

as bounds for the upper and lower absolute density integrals at every
c in I. No complex-t Laguerre estimate is used in (5).

Reuse C997y(8)-(13)'s germ identity, whose fixed-parameter analytic
integration and positive Taylor coefficients were audited in step395.
For ANY finite spectral sum h(t)=sum a_z exp(izt), linearity gives

    f(c)=sum a_z k_n(c,z),
    F(c)=c integral_n^(n+2) g(cu)h(cu)du,
    D_f(c)=F(c)-F(1),
    M_n(f)=m!/(i^m d^m)[t^m]{exp(-2it)h(t)}.              (6)

The cap in C997y's conclusion is used only for its target-minus-band
gap; it is unnecessary for this finite identity. The finite sum makes
all exchanges immediate, and fixed compact u integration is the same
entire extension as in that input. In particular the lower window is
retained as F(1) and removed from the germ only by positive-order
coefficient extraction, not by dropping it from f.

Review396/step397 and the completed comparison in review395 are reused;
no additional theorem is imported. The elementary finite binomial and
Leibniz identities below require their explicit kernel specialization
and cancellation bound; generic Hahn--Banach/Riesz representation and
the inspected derivative inequalities provide neither. C997f's binomial
factor modulates a slope density, whereas the present binomial combines
band columns. C997w's uncapped target interpolant is also a different
object. Their proofs and conclusions are not mathematical inputs here.
The stops340/341, C997t's annihilator stop and C997y's scalar-prior stop
are preserved on their original scopes.

### Exact column membership and complete-window upper bound

For n>=64 choose

    h_n(t)=exp(2it) sin((t-2n)/(8n))^n,
    a_(j,n)=(2i)^(-n) binomial(n,j)(-1)^(n-j)
                                      exp(-i(2j-n)/4),
    f_n(c)=sum_(j=0)^n a_(j,n) k_n(c,gamma_j).            (7)

The binomial expansion of sin x=(exp(ix)-exp(-ix))/(2i) gives
h_n(t)=sum a_(j,n)exp(i gamma_j t): its frequency is
2+(2j-n)/(8n)=15/8+j/(4n). Also sum |a_(j,n)|=2^(-n)sum binomial(n,j)=1.
Thus f_n lies in the actual band span, with ALL endpoint coefficients
and the lower term coupled by the same a_(j,n). In particular C997t(6)
is respected automatically; it is not enlarged to free endpoint jets.

On the complete upper support [7n/4,9(n+2)/4],

    |(t-2n)/(8n)| <= 1/32+9/(16n) <=1/16.

On the complete lower support [n,n+2], the same absolute value is at
most 1/8. These bounds include both closed endpoints. Since t is real,
|exp(2it)|=1 and |sin x|<=|x|. Hence |h_n(t)|<=16^(-n) on the upper
support and <=8^(-n) on the lower support. The triangle inequality in
the COMPLETE response and (5) therefore imply

    ||f_n||_C(I)<=T_U 16^(-n)+T_L 8^(-n).                (8)

Now exp(11/32)<1/(1-11/32)=32/21<2, by the exponential and geometric
series. Thus exp(9n/32)16^(-n)<=exp(-n/16)8^(-n), proving (3).
All zeros and signs of g are permitted; both beta contributions and
K's subtraction are already included in (5). No asymptotic Laguerre
formula, unobserved half-line norm or sampling assertion is used.

### The centered derivative cannot cancel

Write a=1/4 and r=cot a. Elementary sine/cosine bounds give
cos a>=31/32, 0<sin a<=1/4 and r>=31/8>3. We claim

    (d/dx)^m sin(x)^n at x=a
       >=(1/2)(n)_m sin(a)^n r^m,                       (9)

where (n)_m=n(n-1)...(n-m+1). Here m=ceil(sqrt(n))<=n.

To prove the claim, label the m differentiations in the ordinary
Leibniz formula for a product of n identical sine factors. Group labels
which differentiate the same factor into nonempty blocks. A partition
pi of the m labels into b blocks can be assigned injectively to factors
in (n)_b ways. Its contribution is exactly

    (n)_b sin(a)^(n-b) product_(B in pi) sin^(|B|)(a).

This follows directly from the expanded product rule: the partition
and assignment specify the factor receiving each labeled derivative,
so no factorial or multiplicity is missing. The all-singleton partition
contributes the positive main term P=(n)_m sin(a)^n r^m.

Every derivative of sin at a, divided by sin(a), is one of +/-1,+/-r,
so its modulus is at most r. For b=m-j, j>=1, a single partition's
absolute contribution divided by P is therefore at most

    (n)_(m-j)/(n)_m * r^(-j)
       <= [r(n-m+1)]^(-j).                              (10)

There are at most binomial(m(m-1)/2,j) such partitions. To see this
without an asymptotic counting formula, join the least label in every
block to each other label of that block. The resulting set of j
unordered pairs determines the partition as its connected components,
including isolated labels. This is an injection into j-element subsets
of the m(m-1)/2 possible pairs.

Put N=m(m-1)/2 and u=1/(r(n-m+1)). The sum of the absolute ratios of
ALL nonsingleton contributions is at most

    sum_(j=1)^(m-1) binomial(N,j)u^j
       <=(1+u)^N-1 <=exp(Nu)-1.                         (11)

For n>=64, m<=sqrt(n)+1 and m-1<=sqrt(n), so

    Nu <=(n+sqrt(n))/(6(n-sqrt(n))) <=3/14.

Consequently the right side of (11) is at most
exp(3/14)-1 < 1/(1-3/14)-1 =3/11<1/2.
Subtracting this full absolute error from P proves (9), including
the sign. This is the noncancellation estimate needed for (2);
it is not inferred from a finite numerical derivative test.

### Functional value, true norm lower bound and required rate

By (6)-(7),

    exp(-2it)h_n(t)=(-1)^n sin(a-t/(8n))^n,
    |M_n(f_n)|=(8n|d|)^(-m) |(sin^n)^(m)(a)|.            (12)

The m! in (6) cancels the Taylor coefficient factorial exactly; i^m
has modulus one. From (9),

    |M_n(f_n)| >=(1/2) sin(a)^n (n)_m/n^m
                                      * [r/(8|d|)]^m.

Here (n)_m/n^m >=((n-m+1)/n)^m >=(7/8)^m, since n>=64.
Also |d|=sqrt(65)/8<9/8 and r>3. Thus the combined factor per m is
greater than 7/24>1/4, proving (2). In particular f_n is nonzero:
the zero function has zero germ functional.

Divide (2) by (3) to obtain the first inequality in (4). Because
m<=sqrt(n)+1, log(2C_0(n+2)4^m)/n tends to zero, proving the liminf.
For the stated numerical comparison,

    sin(1/4)>=1/4-(1/4)^3/6=95/384>1/5,
    log(8/5)=integral_1^(8/5) dx/x > (3/5)*(5/8)=3/8.

The sine bound follows by integrating cos x>=1-x^2/2 on [0,1/4].
Therefore rho>3/8+1/16=7/16, with a large strict margin above 1/64.

Finally an exact representing measure satisfies

    |M_n(f_n)|=|integral_I f_n dnu|<=||f_n||_C(I)||nu||_TV.

This is the defining total-variation inequality, valid for the bilinear
complex pairing. It proves the stated measure lower bound without
asserting an unproved quantitative extension theorem. The upper target
with rate 1/64-eta contradicts (4) as n tends to infinity, for any
fixed C and eta in the specified range.

### Scope and remaining gaps

The witness is a band-only function; it is NOT a residual with target
coefficient one. Its coefficient sum one does not change that fact.
Both its functional value and response are exponentially small; their
ratio obstructs EXACT moment reproduction. Approximate reproduction
could ignore such small band moments if its aggregate cap-weighted
error were separately paid, so (4) gives no stop for that different
question. No reopening of the unpaid spectral-tail route is asserted.

The argument neither proves E_n=O(exp(-n/64)) nor rules it out. It
provides no chosen-measure certificate for E_n. C997a(8), selected and
both-sign transfer, assay/reconstruction, complements/regulators, L993,
L984(H), L966/L968 forcing and actual-Xi signs remain open. This is
local route evidence, not a proof or disproof of RH.

### Independent conceptual audit — step400, 11 November 2026

RESEARCH / REPRODUCTION / ADVANCE under the unchanged pre-invocation
EXPLORE review398, separately source-approved in step399. Actual task:
proof_audit / conceptual_audit. This verifies the stated local input;
it proves no stronger bound and makes no claim of progress beyond the
sources checked or of certified originality. No repair to the
mathematical statement, proof constants or direct inputs was needed.

**Contracts and well-defined functional.** Read C997c(4)-(6), C997s's
original kernel/grid/cap, and C997y(8)-(13) with its step395 audit.
Reuse the approved real-t DLMF18.14.8 contract cited above: degree n+1,
alpha=2, real t>=0, with K's subtraction already paid. No new theorem
or complex-t extension is used. C997y gives g(0)=(n+4)/2 and a local
analytic reciprocal, sufficient for every coefficient in (1).

For a finite spectral sum h, compact-uniform analytic integration on
the fixed u segment gives D_f=F(c)-F(1). Its coefficient of c^(k+1)
is b_k[t^k]{gh}, with b_k>0. Multiplication of this finite Taylor jet
by v therefore recovers [t^m]{exp(-2it)h}. This checks (6), including
the gauge sign -1/2. The constant F(1) is eliminated only from positive
Taylor coefficients. It remains in f's complete response. The argument
uses no cap and applies to arbitrary finite complex column coefficients.
If two such entire functions have the same restriction to I, the
identity theorem makes their germs identical. Hence M_n is a
well-defined complex-linear functional on S_n regardless of column
relations. In particular a zero restriction has zero functional value.

**Actual frequencies, phases and complete norm.** The j-th term in
sin((t-2n)/(8n))^n has phase exp(-i(2j-n)/4), sign (-1)^(n-j),
and frequency (2j-n)/(8n). Multiplication by exp(2it) gives exactly
gamma_j, including j=0,n. The coefficient moduli sum to one.
Consequently the same vector combines both upper endpoints and the
lower window; there are no freely chosen endpoint data.

On the upper support, x=(t-2n)/(8n) lies in
[-1/32,1/32+9/(16n)], inside [-1/16,1/16] for all n>=64.
On [n,n+2], it lies in [-1/8,-1/8+1/(4n)], inside [-1/8,0].
Thus the two bounds on h in (8) include all closed endpoints.
For each fixed c, C997c's absolute-density bounds apply to the
COMPLETE integrand, not to just one cosh term. Explicitly their upper
and lower bounds before maximization over c are

    8c(n+2)exp(cn/8+3c/4),
    8(n+2)exp((3/8-c/4)n+3/4).

Their maxima are precisely the T_U and T_L in (5). Multiplication by
the two sup bounds on h gives (8), with the factor 2 in the original
kernel already included. The conversion of its first term to the
scale of its second uses exp(11/32)<32/21<2. This checks (3) with
the stated C_0, without any cancellation, zero exclusion or omitted
reflected beta contribution.

**All orders in the labeled derivative expansion.** Each sequence of
m labeled differentiations assigns every label to one of n factors.
Its nonempty fibers form a partition with b blocks; choosing distinct
factors for the blocks gives exactly (n)_b assignments. This justifies
the contribution written before (10), including its multiplicity.
For b=m-j, normalizing by P leaves at most

    [(n)_(m-j)/(n)_m] r^(-j)
       = r^(-j)/product_(q=1)^j (n-m+q)
       <= [r(n-m+1)]^(-j).

Here each normalized sine derivative has modulus either 1 or r, and
r>=31/8>3>1. The star-edge map has exactly sum_B(|B|-1)=j edges.
Connected components recover every original block, including singleton
blocks as isolated vertices. Thus it really is injective into the
j-edge subsets and bounds every nonsingleton partition.

For s=sqrt(n)>=8, m<=s+1 and m-1<=s give

    N/[r(n-m+1)] <= (s^2+s)/(6(s^2-s))
                      = (s+1)/(6(s-1)) <=3/14.

Every denominator is positive. Summing absolute values of ALL omitted
partitions gives at most exp(3/14)-1<3/11<1/2 of P. All terms are
real and P>0, so their signs cannot invalidate the lower bound (9).
This proves noncancellation uniformly, not merely at sampled n or for
fixed derivative order.

**Factorials and exponential rate.** The m-th derivative of
(-1)^n sin(a-t/(8n))^n at zero equals
(-1)^(n+m)(8n)^(-m)(sin^n)^(m)(a). Its Taylor coefficient is this
quantity divided by m!; precisely that factorial cancels the m! in
(6). Taking moduli leaves (12). Furthermore

    (n-m+1)/n >=1-1/sqrt(n)>=7/8,
    r/(8|d|)>3/9=1/3.

The product per derivative is greater than 7/24>1/4. Thus (2) follows
and also proves that the witness is nonzero on I, by well-definedness
of M_n. Dividing its positive functional value by the upper bound for
its actual C(I) norm is therefore legitimate and proves (4).
The denominator's logarithm is O(sqrt(n)+log n)=o(n). Finally
sin(1/4)>=95/384>1/5 and the strict integral estimate
log(8/5)>3/8 give rho>7/16. No decimal estimate or finite numerical
certificate is necessary for this all-n comparison.

**Measure implication and limits.** For every finite complex Borel
measure satisfying the stated bilinear representation, total variation
gives |M_n(f_n)|<=||f_n||_C(I)||nu_n||_TV. Conjugating the functional
or the coefficients is neither required nor allowed. This yields the
same finite lower bound and, for any sequence of such measures, the
same liminf. A bound C exp((1/64-eta)n), with fixed C and
0<eta<1/64, contradicts it. No existence or minimum-norm representation
theorem is needed for this implication.

The witness has target coefficient zero, whereas every residual in
C997s's E_n has target coefficient one. Its coefficient mass one does
not identify these two classes. Accordingly this audit accepts only
the exact-functional stop. It neither bounds E_n at the required rate
nor excludes approximate reproduction with paid errors. C997f/t/w and
the scalar393 and spectral-tail341 records are scope comparisons, not
mathematical inputs. No additional mathematical input is used.
All transfer, reconstruction, forcing, H and actual-Xi gaps listed
above remain unresolved. Full matching Mathlib coverage is unchecked.

## Mathlib

Full matching coverage for this coupled-span norm obstruction has not
been checked and is unknown. The finite binomial expansion, product
rule, elementary sine bounds and total-variation inequality are ordinary
supporting mathematics; the specialized proof is given above. The
Laguerre input is precisely cited in (5) and reused from audited C997c.
No Mathlib theorem is imported and no Lean verification is claimed.
