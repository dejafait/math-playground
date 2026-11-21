# Corollary 919q: an order-one shifted-sinc model with positive inverses after every real-zero prefix

## Hypotheses

Use the angular convention T(f)(z)=integral_R f(u)exp(izu)du.
Set c=sqrt(2), a_j=1/(j+c) for integers j>=1, and sinc(w)=sin(w)/w,
with sinc(0)=1. Fix the single function

    G(z)=(2+cos z)/3 * product_(j>=1) sinc(a_j z).             (1)

The product's existence and the root enumeration used next are proved
below. Let r_1<r_2<... enumerate {pi*k/a_j:j,k>=1}. For each finite
integer N>=0 set

    R_N(z)=product_(ell=1)^N(1-z^2/r_ell^2),  R_0=1,
    G_N(z)=G(z)/R_N(z)                                     (2)

initially where R_N is nonzero. Import C919p's compact identity
(8)-(10) and second-moment calculation (16), and the named standard
inputs below. There is no zeta, Xi, numerical or cross-notebook premise.

## Conclusion

The product (1) is entire. Its complete real-zero set is
{+/-r_ell:ell>=1}, all simple. Every G_N extends to an entire function
whose real zeros are exactly {+/-r_ell:ell>N}, all simple. It is the
entire transform of a smooth even probability density f_N with
f_N(u)>0 for every real u. For all integers m,p>=0 and real B>=0,

    integral_R (1+|u|)^p exp(B|u|)|f_N^(m)(u)|du < infinity,
    exp(B|u|)f_N^(m)(u) -> 0 as u -> +/-infinity.             (3)

The second moments satisfy the exact formula and uniform bound

    integral_R u^2 f_N(u)du
      =1/3+(1/3)sum_(j>=1)a_j^2-2 sum_(ell=1)^N r_ell^(-2)
      <=(1+1/sqrt(2))/3 < 2/3.                             (4)

For every N the point

    z_*=pi+i log(2+sqrt(3))                                (5)

is a simple nonreal zero of G_N. Each G_N has order exactly one.
Writing M_N(r)=max_(|z|=r)|G_N(z)|, the following bounds suffice,
simultaneously for all N and r>=1:

    r-log(6) <= log M_N(r)
      <= r+r log((ceil(r)+c)/c)+r^2/(2(ceil(r)+c)).          (6)

Thus order one, all finite real-zero-prefix positive inverses, (3),
and a uniform second moment do not together force all zeros real.
This is a known-method REPRODUCTION specialization under the prior
SPECIALIZE2244 assessment, accepted by critical audit2248 below. It is
not a proof or disproof of RH. No actual-Xi transfer, theta identity,
correlation-kernel positivity, logarithmic concavity, finite type or
precise Xi growth asymptotic is asserted.

## Proof

### Imported inputs and scope

C919p(8)-(10) gives, for every integer n>=0,

    h_n(v)=c_n cos(pi*v/2)^(2n) on |v|<1, zero otherwise,
    c_n=4^n(n!)^2/[2(2n)!],
    H_n(w)=T(h_n)(w),
    H_n(w) product_(k=1)^n(1-w^2/(k*pi)^2)=sinc(w),
    H_n(+/-k*pi)=(n!)^2/[(n+k)!(n-k)!]  (0<=k<=n).        (7)

These are even probability densities, strictly positive on (-1,1);
h_0 is the uniform density there. Endpoint values do not matter.
C919p(16) also gives

    integral v^2 h_n(v)dv=1/3-2 sum_(k=1)^n(k*pi)^(-2).    (8)

The finite identity is already proved using NIST DLMF
[5.12.5](https://dlmf.nist.gov/5.12.E5),
[5.12.1](https://dlmf.nist.gov/5.12.E1),
[5.5.1/5.5.3](https://dlmf.nist.gov/5.5) and
[5.2(i)](https://dlmf.nist.gov/5.2.i), including the initial beta
parameter restrictions, entire extension and every removable value.
It is reused, not reproved here; no Gaussian assertion from C919p is used.

Rick Durrett, *Probability: Theory and Examples*, version5,
11 January2019, [author PDF](https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf),
Theorem2.5.6, printed pp84-85, gives almost sure convergence of a series
of independent centered variables with summable variances. Theorem3.3.14,
printed p130, gives the bounded continuous inverse probability density
when the characteristic function is integrable, with factor1/(2pi)
and inverse exponential exp(-ixu) in this convention. The hypotheses
are checked below. Standard L2 completeness, Tonelli/Fubini and
dominated convergence are used with the stated bounds.

Wassily Hoeffding, *Probability Inequalities for Sums of Bounded Random
Variables*, UNC Institute of Statistics Mimeo326, May1962,
[primary manuscript](https://repository.lib.ncsu.edu/bitstreams/d0e6ed15-3e1c-432f-8419-e55ffb6f3171/download),
Theorem2, printed p6, (2.10), and its proof pp12-13, (3.11)-(3.17),
provides the bounded-variable input

    E exp(t(X-E X))<=exp(t^2(b-a)^2/8),  a<=X<=b, t real. (9)

We import this bound, with constant variables omitted if necessary,
and explicitly use Fatou at infinite limits. Source notes2244 inspected
the theorem and proof; the damaged web transcription of (3.16) is
resolved there by (3.12),(3.15),(3.17). The later URL-recovery turn saw
a bot block, not a new manuscript extraction. This proof reuses the
prior coverage and does not claim renewed source access.

[DLMF1.10(ix), (1.10.20)-(1.10.21) and the following conclusion](https://dlmf.nist.gov/1.10.ix)
supplies the locally uniform analytic-product test and the fact that a
convergent product under that test has no zeros except its factors'
zeros. The compact majorant and local multiplicities are checked below.
Order means limsup_(r->infinity) log log M(r)/log r; see A. Eremenko,
*Zeros and coefficients*, 28 October2015, [p2, item3](https://www.math.purdue.edu/~eremenko/dvi/legendre2new.pdf).
Only this definition is needed, not a type theorem.

B. Schmuland, *Random Harmonic Series*, *American Mathematical Monthly*
110(5) (2003),407-416, DOI10.1080/00029890.2003.11919978,
[manuscript sections2,4-5, pp2,4-7](https://web.williams.edu/Mathematics/sjmiller/public_html/105Sp11/addcomments/Schmuland_RandomHarmonicSeries.pdf),
provides the standard finite-head smoothing and support method being
specialized. Its uniform widths differ and it has no asserted global
zero-prefix conclusion, so its full conclusion is not imported for (1).
The method, the atomic cosine factor and (7) are not claimed original.
The source comparison found no matching full theorem, which does not
certify novelty. The new work here is the fixed-model assembly.

### Entire product, root inventory and ordered removal

Monotone integral comparison gives

    sum_(j>=1)a_j^2 <= integral_0^infinity (x+c)^(-2)dx=1/c,
    sum_(j=1)^J a_j <= log((J+c)/c),
    sum_(j>J)a_j^2 <= 1/(J+c),
    sum_(j>K)a_j=infinity for every finite K.              (10)

For the last claim, the partial sums dominate the corresponding
integral from K+1 to the next integer, which diverges. For |z|<=R,
the sinc power series yields

    |sinc(a_j z)-1|
      <= a_j^2 R^2 sum_(l>=1) R^(2l-2)/(2l+1)!,            (11)

because 0<a_j<1. The sum on the right is a finite constant for each
R (with its limiting interpretation at R=0). Thus (10)-(11) satisfy
the cited analytic-product test on every compact disk. The product
in (1) is entire and nonzero wherever no sinc factor is zero.

The complex sine definition gives precisely the simple sinc zeros
w=+/-k*pi for k>=1, with nonzero derivative there. If
k(j+c)=k'(j'+c), then (k-k')sqrt(2)=k'j'-kj. Irrationality of sqrt(2)
forces k=k', hence j=j'. Thus no two factors share a zero. In any
bounded interval there are finitely many positive candidate zeros:
pi*k*(j+c)<=R bounds both positive integers j and k. The set is
unbounded and infinite, so the stated increasing enumeration exists.
For real x, 2+cos x>=1; it adds no real zeros. At each sinc zero,
the product of the other factors is analytic and nonzero by the same
test. This proves the exhaustive simple real-root claim for G.

For N>=1 let n_j be the number of positive integers k with
pi*k/a_j<=r_N; for N=0 put every n_j=0. Only finitely many n_j are
nonzero, sum_j n_j=N, and the roots removed from factor j are exactly
k=1,...,n_j. This follows from the global increasing order and the
strict order within each factor; there is no reordering of an infinite
conditionally convergent product. Therefore

    R_N(z)=product_j product_(k=1)^(n_j)(1-(a_j z)^2/(k*pi)^2),
    G_N(z)=(2+cos z)/3 * product_(j>=1) H_(n_j)(a_j z).      (12)

Only finitely many factors differ from (1), so (12) is entire and
equals the quotient away from R_N=0 by (7). At a removed zero belonging
to factor j and k<=n_j, that factor has the strictly positive value
in (7); every other factor is nonzero there. Equation (7) also shows
that H_n has exactly the remaining sinc zeros, all simple: off the
removed points this follows by division; at the removed points the
displayed values exclude a zero. Thus (12) proves all removability
and remaining-real-zero assertions, including N=0.

### One probability law for each prefix of the same entire function

On a product probability space choose independent variables Y_j with
densities

    rho_j(u)=a_j^(-1) h_(n_j)(u/a_j).                       (13)

The substitution u=a_j v in the compact Fourier integral gives
T(rho_j)(z)=H_(n_j)(a_j z), including complex z. The variables are
centered and even, with |Y_j|<=a_j. Independently choose A with law

    mu=(2/3)delta_0+(1/6)delta_-1+(1/6)delta_1.             (14)

Its transform is (2+cos z)/3, its mean is zero and E A^2=1/3.
Since sum_j Var(Y_j)<=sum_j a_j^2<infinity, Durrett2.5.6 applies:
S=sum_j Y_j exists almost surely. It also exists in L2: the L2 norm
squared of a difference of partial sums is the sum of their variances
by independence and centering, hence tends to zero. L2 completeness
gives a limit in probability; uniqueness of limits in probability
identifies it with the almost sure limit S. In particular S is centered
and E S^2=sum_j Var(Y_j). The distribution of S is even, since every
finite partial sum is even and bounded continuous expectations pass
to the almost sure limit. The same holds for A+S.

For real x, bounded convergence applied to exp(ix sum_(j<=L)Y_j)
identifies the characteristic function of S with the infinite product
in (12). Independence of A then identifies G_N on the real axis as
the characteristic function of A+S. The random variables depend on N,
as they must after division; the underlying G in (1) never changes.

For any subseries sum_(j>K)Y_j, apply (9) to its finite partial sums.
Independence gives the bound exp(t^2 sum_(j>K)^L a_j^2/2), for every
real t. Fatou along the almost sure limit gives

    E exp(t sum_(j>K)Y_j) <= exp((t^2/2)sum_(j>K)a_j^2).    (15)

For T_K=A+sum_(j>K)Y_j, independence of A and (9) give

    E exp(t T_K)<=exp(V_K t^2/2),
    V_K=1+sum_(j>K)a_j^2<=1+1/c<2.                         (16)

Markov's inequality at t=r/V_K and at -t, for r>0, yields

    P(|T_K|>=r)<=2 exp(-r^2/(2V_K)).                       (17)

The right side2 also bounds the probability at r=0. No expectation
is interchanged with an unbounded exponential limit without (15).

### Full support and pointwise strict positivity

Fix N and let J_N=max{j:n_j>0}, or J_N=0 if the set is empty. When
K>=J_N, all variables Y_j for j>K are genuine uniform variables on
[-a_j,a_j]. Their sum has full support R. Here is the needed check.
Given x in R and epsilon>0, choose L>K so large that

    sum_(j=K+1)^L a_j>|x|,
    Var(sum_(j>L)Y_j)<epsilon^2/8.                         (18)

The first choice is possible by (10), and the second by summable
variances; enlarging L preserves the first. A finite convolution of
the interval densities is strictly positive in the interior of its
support interval, so

    P(|sum_(j=K+1)^L Y_j-x|<epsilon/2)>0.                  (19)

For completeness, this finite positivity uses only an elementary
integration fact: for |x|<b+d, the intervals (-b,b) and (x-d,x+d)
have an open intersection, on which the two positive densities have
positive product. Their convolution is therefore positive at x.
Induction applies this to all the finitely many factors. For one factor
the assertion is direct. Thus (19) follows even if the displayed
epsilon-neighborhood extends outside the support interval.

Chebyshev and (18) give probability greater than1/2 that the infinite
remaining sum has absolute value less than epsilon/2. This remaining
sum is independent of the finite block: it is the almost sure limit
of random variables measurable with respect to the disjoint tail
coordinates. Combining these two events proves positive probability
in (x-epsilon,x+epsilon). Since P(A=0)=2/3, the law nu_K of T_K also
has full support. This proves a measure-support assertion first;
strict positivity of the desired density will use a separate finite head.

### Finite-head smoothness and every derivative tail

Fix m>=0 and choose K>=J_N+m+3. Let Q_K=sum_(j=1)^K Y_j and
L_K=sum_(j=1)^K a_j. Every factor in its characteristic function has
modulus at most1 on R. Among them at least m+3 are unaffected uniforms.
For those factors

    |sinc(a_j x)|<=min(1,1/(a_j|x|))  (x nonzero).

Consequently, with a finite constant C depending on the chosen head,

    |E exp(ix Q_K)|<=C(1+|x|)^(-m-3).                     (20)

Thus x^l times this characteristic function is integrable for all
0<=l<=m+1. Durrett3.3.14 supplies a bounded continuous probability
density q_K. Differentiation under its absolutely convergent inverse
Fourier integral, dominated by these integrable functions, gives
q_K in C^(m+1)(R), with bounded derivatives through order m+1.
The probability law is supported in [-L_K,L_K], so its continuous
density, and all these derivatives outside that interval, vanish.
Continuity also supplies the endpoint values and makes the derivatives
compactly supported. In particular C_(K,m)=sup_R |q_K^(m)| is finite.

This density is positive for |u|<L_K. Indeed the finite convolution
of (13) has this interior positivity by the same elementary argument
used above; each factor is bounded, integrable, supported in its
interval, and positive in its interior. The convolution of two such
factors is continuous: translate one factor in L1 and bound the other
in L-infinity. Convolving further preserves continuity and the
positivity argument. Here K>=3, so this continuous representative
agrees everywhere with q_K, since the two are equal almost everywhere.

Define the continuous probability density

    f_(N,K)(u)=integral_R q_K(u-v)dnu_K(v).                 (21)

Tonelli gives its mass1; evenness follows from evenness of both laws.
It is a density for A+S by independence. All choices of K as above
give the same function pointwise: they are continuous densities of
the same law and hence agree almost everywhere, then everywhere.
Call this function f_N. Since q_K is positive on a neighborhood of0
and nu_K assigns positive mass to every open interval, (21) gives
f_N(u)>0 at every u. More explicitly, q_K has a positive minimum on
some compact neighborhood of0; integrating over its translate about
u gives a strictly positive lower bound. This argument does not infer
strict positivity merely from full support or from a positive limit.

Bounded derivatives of q_K justify successive differentiation of
(21) by dominated convergence; for derivatives through order m one
may use the bound on the next derivative for difference quotients.
Thus

    f_N^(m)(u)=integral_R q_K^(m)(u-v)dnu_K(v),
    |f_N^(m)(u)|
      <=2 C_(K,m) exp(-((|u|-L_K)_+)^2/4).                 (22)

To obtain the last line, a nonzero integrand requires |v|>=|u|-L_K;
use (17) with r=(|u|-L_K)_+ and V_K<2. This also bounds the case
r=0. Since such a head can be chosen for every m, the common f_N is
C-infinity. No uniformity of C_(K,m) or L_K in N,m is asserted.

To check (3) explicitly, put r=|u|. For
r>=max(2L_K,32B), the exponent in (22) after multiplication by exp(Br)
is at most -r^2/16+Br<=-r^2/32. This Gaussian majorant times any
(1+r)^p is integrable and tends to zero; on the remaining compact
interval all derivatives are continuous and bounded. This proves both
weighted conclusions separately, for every p,B and each derivative.

In particular the transform integral of f_N extends to an entire
function: on |z|<=R, its lth differentiated integrand is bounded by
|u|^l exp(R|u|) f_N(u), integrable by (3). It agrees with (12) on R
by the characteristic-function argument and hence on C by the identity
theorem. Finally, applying (20) for m=0 to the full characteristic
function (the remaining characteristic factor has modulus at most1)
shows G_N is integrable on R. Durrett inversion therefore also gives

    f_N(u)=(1/(2pi))integral_R G_N(x)exp(-ixu)dx.           (23)

### Uniform second moment

Scaling (8) in (13) gives

    Var(Y_j)=a_j^2/3-2a_j^2 sum_(k=1)^(n_j)(k*pi)^(-2).

These are actual nonnegative variances of the already constructed
probability laws. The L2 convergence proved above, centering and
independence of A give E(A+S)^2=1/3+sum_j Var(Y_j). Only finitely
many inner sums are nonempty, and their roots are exactly r_1,...,r_N
by the prefix grouping. This proves the equality in (4). Dropping the
nonnegative subtracted term and using (10) proves its bound. There is
no differentiation of an unjustified infinite product, and no passage
N->infinity is used or needed.

### Retained nonreal zero and exact growth order

Let b=log(2+sqrt(3)), so cosh b=2 and sinh b=sqrt(3). Then
cos(pi+ib)=-2 and sin(pi+ib)=-i sqrt(3). The factor (2+cos z)/3
has a simple zero at z_* with derivative i sqrt(3)/3. Every sinc
factor is nonzero at z_*, since its zeros are real; the analytic-product
test excludes an additional zero from their infinite product. R_N(z_*)
is nonzero. Thus the simple nonreal zero persists in every G_N.

For every n, the compact law h_n is centered and supported on [-1,1].
Its scaled transform obeys both bounds, for |z|=r,

    |H_n(a_j z)|<=exp(a_j r),
    |H_n(a_j z)|<=exp(a_j^2 r^2/2).                        (24)

The first uses the support bound inside the integral. For the second,
take absolute values inside the same integral and apply (9) with
t=-Im(z) to the centered variable of range [-a_j,a_j]. Also
|(2+cos z)/3|<=exp(r) from the probability law (14). Use the first
bound of (24) for j<=J=ceil(r), the second for j>J, and pass through
the locally convergent product (12). This gives

    log M_N(r)<=r+r sum_(j<=J)a_j+(r^2/2)sum_(j>J)a_j^2,

and (10) proves the upper half of (6). It holds even when J<J_N,
because both bounds (24) hold for all n, including modified factors.
Its right side is r log r+O(r) as r->infinity.

For the lower bound, evenness of each compact law gives

    H_n(i a_j r)=integral h_n(v)cosh(a_j r v)dv>=1.

The convergent product of these positive factors is at least1.
Therefore G_N(ir)>0 and

    M_N(r)>=G_N(ir)>=(2+cosh r)/3>=exp(r)/6.

This proves the other half of (6). For r large enough that r-log6>0,
taking log of the two bounds for log M_N(r), then dividing by log r,
gives lower limit at least1 and upper limit at most1. Thus the order
is exactly1 for every finite N. Only order is concluded; these bounds
do not assert finite exponential type or an asymptotic for log M_N.

The single fixed model meets every nominated requirement and retains
the detecting nonreal zero. It therefore supplies a scoped obstruction
to a generic order-one sufficiency inference. The actual-Xi inverse
iteration, existence of all needed real roots, and L030-L032/C032a's
mixed positivity remain independent unresolved questions. In particular
pointwise positivity of (21) is not the positive definiteness of every
weighted correlation kernel in Csordas1309.0055v2 Theorem3.7; no such
identification or extra strict-log-concavity hypothesis is claimed.

### Critical audit2248: all finite prefixes, with the same fixed G

21 November2026. Independent conceptual audit under SPECIALIZE2246,
separately approved2247. The complete proof above and the exact compact
input C919p(8)-(10),(16) were checked. Source notes2239/2244 supply the
previously inspected primary statements and proof cases; this audit
does not claim fresh access to Hoeffding or independent recertification
of the classical theorems. Every nominated obligation passes. The
following records the load-bearing checks, rather than finite samples.

**Product and enumeration.** The decreasing function (x+c)^(-2)
dominates its value at each right integer endpoint, giving the first
and third bounds in (10) on the stated integration intervals. The
same comparison for (x+c)^(-1) gives the finite head bound; its divergent
integral gives the divergent sum of widths. In (11), factoring
a_j^2 R^2 from each nonconstant sinc term leaves a_j^(2l-2)<=1.
Thus the majorant is summable in j on every disk. The cited product
test applies to a nonvanishing tail after any finite set of factors
is excluded. It rules out both extra zeros and extra multiplicity.
Irrationality of c forces equality of j and k at any coincident
candidate roots. Bounded candidate roots bound both integers, so
the enumeration is locally finite. These checks justify the global
increasing prefix, not merely a convenient enumeration of factors.

**Removal at every apparent pole.** For a fixed finite N, a root
pi*k/a_j below the cutoff brings all the smaller k from that factor
with it. Exactly N distinct positive roots are removed and only
finitely many factors change. C919p's compact formula has mass one
and value (n!)^2/[(n+k)!(n-k)!]>0 at every removed k, including its
n=0 normalization. Substitution w=a_j z proves (12). At an affected
root the other factors and (2+cos z)/3 are nonzero; each unaffected
sinc root is simple. This proves entire removability and the remaining
real-root inventory for arbitrary N without an infinite rearrangement.

**Probability limit and exponentials.** The independent even compact
variables are centered and have variances at most a_j^2. The hypotheses
of Durrett2.5.6 therefore hold. The L2 Cauchy calculation uses centering
to eliminate every cross term. Its L2 limit equals the almost sure
limit by uniqueness in probability, so its mean and variance pass in
L2, not through an unjustified weak-limit moment assertion. Bounded
convergence for exp(ix sum Y_j), for real x, identifies the characteristic
product. Applying Hoeffding's moment bound to finite sums uses ranges
of length 2a_j and yields exactly t^2 sum a_j^2/2. Fatou for their
nonnegative exponentials proves (15) for each real t. Independence
from A, whose range length is 2, gives (16) with V_K=1+sum_(j>K)a_j^2.
Markov at t=+/-r/V_K gives both sides of (17). No complex-frequency
expectation or unbounded exponential is passed through a limit here.

**Support and strictness are separate.** With K>=J_N the remaining
variables are uniforms. Their divergent total widths permit a finite
block with x strictly inside its support interval, while the variance
of its remaining infinite tail can simultaneously be made less than
epsilon^2/8. The block's interior positivity follows by integrating
over an open intersection of two positive-density intervals, inductively.
Chebyshev then gives tail probability greater than 1/2 within
epsilon/2. Independence proves positive mass in each epsilon-neighborhood
of x. The atom A=0 transfers this to nu_K. This establishes full support
of the remainder, not yet positivity of a density. That latter claim
uses the continuous finite-head density: its positive value at zero
gives a positive minimum on a sufficiently small closed interval.
Full support of nu_K gives positive mass in the interior of its translate
about each u, and (21) is consequently strictly positive at that u.

**Changing heads and all derivative tails.** Choosing K>=J_N+m+3
leaves at least m+3 uniform factors in the head. All other characteristic
factors have modulus at most one, and the uniform factors give (20).
The largest required multiplier, |x|^(m+1), leaves O(|x|^(-2)) at
infinity and is integrable also near zero. Durrett3.3.14 and dominated
Fourier differentiation therefore give a C^(m+1) head density with
bounded derivatives. Its continuous representative agrees everywhere
with the positive finite convolution, since K>=3 and that convolution
is continuous. Its support and derivative supports lie in [-L_K,L_K];
continuity handles the endpoints. Convolution with nu_K gives a
continuous density of the same fixed law A+S for every eligible head.
Equality almost everywhere of these continuous functions implies
equality everywhere. Thus increasing K proves smoothness of one f_N,
not a succession of possibly different representatives.

Bounded derivatives through m+1 dominate the successive difference
quotients in (21). If its mth derivative integrand is nonzero, then
|v|>=(|u|-L_K)_+. Apply (17), using V_K<=1+1/c<2, to obtain exactly
the bound (22); for the zero cutoff its factor 2 remains a valid upper
bound. For r>=2L_K its exponent is at most -r^2/16; for r>=32B,
adding Br gives at most -r^2/32. This proves every weighted L1 statement
and every weighted pointwise limit in (3). Constants may depend on
N and m. The same bounds justify all complex transform derivatives
locally uniformly. The identity theorem then identifies that transform
with (12). Real-axis integrability for (23) follows from one m=0 head
and the modulus-at-most-one remainder; the inverse factor and sign
match the angular convention. These are full infinite-tail arguments.

**Moment and retained zero.** C919p(16), after scaling, gives the
displayed actual variances. L2 convergence and independence add them
to E A^2=1/3. The finitely many subtracted terms are precisely the
N removed reciprocal squares, by the grouping already checked.
This proves the equality in (4). Dropping them gives
(1+1/c)/3<2/3 because c=sqrt(2)>1, uniformly for all N. There is no
N-limit assertion. At z_*, cos z_*=-2 and sin z_*=-i sqrt(3), so
the atomic factor has nonzero derivative i sqrt(3)/3. No sinc factor
or divisor vanishes there, and the product test makes their infinite
product nonzero. The nonreal zero therefore survives simply.

**Exact order and uniformity.** Both bounds in (24) apply to every
compact law h_n, including modified factors. The first is its support
bound; the second is Hoeffding at t=-Im z. Splitting at J=ceil(r)
thus remains valid even when J<J_N. Taking finite products and then
their convergent limit gives the upper bound (6), of size
r log r+O(r), with no N-dependent constant. On the imaginary axis
each factor is the expectation of a cosh and is at least one. The
convergent positive product and (2+cosh r)/3>=exp(r)/6 give the lower
bound. Consequently log log M_N(r)/log r has liminf at least one
and limsup at most one for each N. Both estimates, not the order
upper bound alone, are used. Finite exponential type and an exact
Xi-scale growth asymptotic do not follow and are not claimed.

**Verdict and scope.** Accept C919q as a checkable generic order-one
countermodel with all the stated quantifiers. No correction to its
mathematical argument was necessary. Its sole direct local mathematical
input is C919p's compact identity and moment formula; the DAG row
requires no change. This acceptance adds a verified local obstruction,
not a new result beyond the assessed literature, an actual-Xi input,
or a resolution of L030-L032/C032a. Positivity of these direct inverse
densities is still distinct from Csordas's correlation-kernel criterion.
Repeating unchanged approval or audit cannot supply the missing bridge.

## Mathlib

Full matching coverage and supporting theorem names have not been
checked. No absence claim or formal verification is made. The named
classical inputs and the complete specialization above supply the
informal argument, critically checked in audit2248 above. No numerical
or mathematical-script certificate or formal verification is used.
