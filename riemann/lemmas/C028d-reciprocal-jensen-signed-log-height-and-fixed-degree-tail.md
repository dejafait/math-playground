# Corollary C028d: reciprocal Jensen signed-log height and fixed-degree tail

## Hypotheses

Use exactly the actual reciprocal Jensen family of C028a and C028b:

    b_j=gamma_j/gamma_0,  gamma_j=j! M_(2j)/(2j)!,  b_0=1,
    P_d(x)=R_d(x)/gamma_0=sum_(j=0)^d binom(d,j)b_j x^(d-j),
    H_d=sum_(j=1)^d |Im z_j|,

where d>=3 is an integer and z_j are the roots of P_d with algebraic
multiplicity. The real normalization gamma_0 is positive. In particular
P_d is monic of degree d. C028a supplies

    S_2=b_1^2-b_2>0.

No RH, hyperbolicity, simplicity, or zero-free real axis is assumed.
Set

    Q_d(y)=P_d(y-b_1)=sum_(k=0)^d c_(d,k) y^(d-k),
    alpha_j=z_j+b_1,
    f_d(y)=log|Q_d(y)|-d log|y|.

The last function is initially defined away from the finite set consisting
of zero and the real roots of Q_d; any values may be assigned on that
null set. All integrals below are Lebesgue integrals. Define finite constants

    rho_d=max_j |alpha_j|,     A_(d,4)=sum_j |alpha_j|^4,
    c_(d,k)=binom(d,k) sum_(j=0)^k binom(k,j)b_j(-b_1)^(k-j),
    K_d=1+max_(1<=k<=d)|c_(d,k)|.

These constants depend on the specified degree and actual coefficients;
no bound uniform in d is a hypothesis or conclusion.

## Conclusion

The combined signed log belongs to L^1(R), including when P_d has
repeated real roots or a root at -b_1, and

    integral_R [log|P_d(x)|-d log|x+b_1|] dx
       = integral_R f_d(y) dy = pi H_d.                       (1)

For every T>rho_d the centered symmetric tail has the expansion

    integral_(|y|>T) f_d(y) dy
       = -d(d-1)S_2/T + E_d(T),
    |E_d(T)| <= A_(d,4)/[6 T^3 (1-(rho_d/T)^2)].              (2)

In particular rho_d<=K_d, so for every T>=2K_d,

    |E_d(T)| <= 2d K_d^4/(9T^3).                             (3)

Thus the first nonzero symmetric-tail term is the negative term displayed
in (2). Equivalently, for T>rho_d the central integral is

    integral_(-T)^T f_d(y)dy = pi H_d+d(d-1)S_2/T-E_d(T).      (4)

These are fixed-degree identities and bounds. They give no o(d) estimate
for the full integral and no uniform domination as d grows. C028b's
RH-equivalent height criterion remains unpaid.

## Proof

### Known method and the required specialization

The finite-factor accounting is a specialization of the usual
log-modulus method, not a new general identity. Relevant inspected sources
are Min Ru, *Nevanlinna Theory*, undated author-hosted notes,
[Theorem A1.1.1 and proof, printed pp.1-2](https://www.math.uh.edu/~minru/log.pdf),
and Abbas Emami-Naeini and Dick de Roover, *Bode's Sensitivity Integral
Constraints: The Waterbed Effect Revisited*, arXiv:1902.11302v1,
[Theorem 1/(12), Corollary 3/(18), Appendix A/(23)-(27)](https://arxiv.org/html/1902.11302v1).
Assessment1507 and its source notes record the inspected hypotheses and
proof cases. Ru's result is a finite-disk Poisson-Jensen formula; the
Bode result uses a stable closed-loop control setting and its real
conjugate-factor structure. Neither theorem is applied under unverified
hypotheses here. In particular rotation does not supply stability, and a
formula with a nonzero boundary parameter does not settle real roots.

The short finite-factor calculation below is needed for the actual
normalization, arbitrary repeated boundary roots, and unweighted tails.
It uses the fundamental theorem of algebra, the ordinary Taylor series
for log(1-w) on |w|<1, elementary real integration, and Tonelli's theorem
for a nonnegative function. It does not reprove general Poisson-Jensen
or import the control theorem's conclusions outside their scope.

### Centering, coefficients, and an explicit exterior region

Expanding each (y-b_1)^(d-j) gives the displayed c_(d,k): the coefficient
of y^(d-k) uses the identity
binom(d,j)binom(d-j,k-j)=binom(d,k)binom(k,j). Consequently

    c_(d,0)=1,  c_(d,1)=0,
    c_(d,2)=binom(d,2)(b_2-b_1^2)=-binom(d,2)S_2.

Factoring Q_d(y)=product_(j=1)^d(y-alpha_j), with multiplicity, and
comparing its top coefficients now gives

    sum_j alpha_j=0,
    p_(d,2):=sum_j alpha_j^2
       =(sum_j alpha_j)^2-2sum_(i<j)alpha_i alpha_j
       =-2c_(d,2)=d(d-1)S_2>0.                              (5)

This is an algebraic square sum, not a sum of absolute squares; no root
reality is used. Since Q_d has real coefficients, its roots are closed
under conjugation with multiplicities, and all its power sums are real.

For completeness the coefficient bound used in (3) follows directly.
Write M=max_(1<=k<=d)|c_(d,k)|=K_d-1. If |y|=r>K_d, then

    |sum_(k=1)^d c_(d,k)y^(d-k)|
      <= M sum_(k=1)^d r^(d-k)
      = M(r^d-1)/(r-1) < r^d.

Here r>1 and r-1>M. Hence Q_d(y) cannot vanish there, so rho_d<=K_d
and A_(d,4)<=d K_d^4. This supplies a coefficient-only finite cutoff.

### Local singularities and absolute tail integrability

For a real root r!=0 of multiplicity m, write Q_d(y)=(y-r)^m U(y)
with U nonzero on a sufficiently small real interval about r. Then
f_d(y)=m log|y-r|+log|U(y)|-d log|y| there. The latter two terms
are bounded on a smaller interval, and log|y-r| is absolutely locally
integrable. At zero use the same factorization, allowing m=0:

    f_d(y)=(m-d)log|y|+log|U(y)|.

This treats a common zero of the numerator and reference and all
multiplicities. The elementary integral of |log|y|| near zero is finite.
Away from these finitely many points f_d is continuous, proving local
absolute integrability.

Put p_(d,n)=sum_j alpha_j^n. For |y|>rho_d the logarithm series in each
factor, normalized at alpha_j/y=0, gives

    f_d(y)=-Re sum_(n>=1) p_(d,n)/(n y^n).                    (6)

Only these exterior factor logarithms are used. There is no global
logarithm across the zeros. The series is absolutely convergent, and (5)
removes its n=1 term. With A_(d,2)=sum_j|alpha_j|^2, it follows that

    |f_d(y)| <= A_(d,2)/[2|y|^2(1-rho_d/|y|)].

Indeed, for n>=2, sum_j|alpha_j|^n<=A_(d,2)rho_d^(n-2) and 1/n<=1/2.
For |y|>=2K_d this is at most A_(d,2)/|y|^2. Along with local
integrability, this proves f_d in L^1(R). Translation y=x+b_1 proves
absolute integrability of the combined integrand in (1) as well.

### Finite-factor integral, with real and repeated roots

Fix one root alpha=a+ib, put B=|b|, and retain a symmetric finite
cutoff for

    g_alpha(y)=log|y-alpha|-log|y|.

Almost everywhere split it as

    g_alpha(y)=h_B(y-a)+log|y-a|-log|y|,
    h_B(u)=(1/2)log(1+B^2/u^2).

If B=0, h_B is zero almost everywhere. For B>0 and u!=0,

    h_B(u)=integral_0^B t/(u^2+t^2)dt.

The integrand is measurable and nonnegative, so Tonelli permits the
interchange with integration over all real u. For every t>0,
integral_R t/(u^2+t^2)du=pi, by the arctangent antiderivative. Thus

    integral_R h_B(u)du=pi B.                                (7)

The point u=0 and the parameter t=0 are null sets and do not affect this
calculation. In particular h_B is integrable, so its integral on the
increasing intervals [-T-a,T-a] tends to (7).

The translation difference must not be integrated as two divergent
one-sided integrals. Instead let Phi(u)=u log|u|-u for u!=0 and
Phi(0)=0. This is a continuous odd primitive of log|u|, with the
primitive identity valid across zero because the logarithm is locally
integrable. For T>|a| its finite symmetric integral is

    integral_(-T)^T [log|y-a|-log|y|]dy
       =Phi(T-a)+Phi(T+a)-2Phi(T).                           (8)

For positive u, Phi''(u)=1/u. Taylor's formula with integral remainder
at T, applied at T-a and T+a, cancels the linear terms and bounds the
absolute value of (8) by a^2/(T-|a|). It therefore tends to zero.
This includes a=0, when (8) is identically zero. Equations (7)-(8)
give the symmetric-cutoff limit pi|b| for this single factor. We have
not asserted that g_alpha alone is absolutely integrable.

The factorization of Q_d gives f_d=sum_j g_(alpha_j) almost everywhere.
There are only d terms, so for each finite T their locally integrable
functions may be summed under the integral. Taking the symmetric-cutoff
limit gives pi sum_j |Im alpha_j|. The combined f_d is already known
to be in L^1(R), so this limit is its ordinary full integral, not merely
a principal value. Since b_1 is real, Im alpha_j=Im z_j, with all
multiplicities unchanged. This proves (1), including all repeated real
root and common-zero cases.

### The first symmetric-tail term and its remainder

For y>rho_d, use (6) at y and -y. Odd powers cancel, giving

    f_d(y)+f_d(-y)=-sum_(k>=1) p_(d,2k)/(k y^(2k)).           (9)

For every T>rho_d termwise integration of (9) on [T,infinity) is
justified by absolute summability of the integrated series: its absolute
sum is bounded by

    sum_(k>=1) sum_j|alpha_j|^(2k)
                    /[k(2k-1)T^(2k-1)]
       <= A_(d,2)/[T(1-(rho_d/T)^2)] < infinity.

Since f_d is integrable, changing variables on its negative tail is
also legitimate. Thus

    integral_(|y|>T) f_d(y)dy
       =-sum_(k>=1) p_(d,2k)/[k(2k-1)T^(2k-1)].             (10)

By (5) its k=1 term is exactly -d(d-1)S_2/T, which is nonzero.
For k>=2 use sum_j|alpha_j|^(2k)<=A_(d,4)rho_d^(2k-4) and
k(2k-1)>=6. Summing the resulting geometric series proves (2).
For T>=2K_d, replace A_(d,4) by dK_d^4 and
1/(1-(rho_d/T)^2) by 4/3, obtaining (3). Subtracting (2) from (1)
gives (4). Every interchange here has been justified for the fixed
degree and the stated cutoff; none involves d tending to infinity.

The negative far tail does not give an upper bound for the central
integral, whose missing payment is explicit in (4). A large or growing
K_d in (3) cannot silently be replaced by a uniform constant. No
conclusion about actual nonreal zeros or all-degree positivity follows.

### Independent conceptual audit1514 (2026-11-18)

The full proof was replayed under the unchanged SPECIALIZE scope of
assessment1511. No correction to the hypotheses, formulas or constants
was needed. The following checks are part of the audit, not additional
claims about the central integral.

The top coefficient of P_d is one, its next coefficient is d b_1, and
the real shift therefore gives sum alpha_j=0 exactly. The binomial
convolution gives c_(d,2)=-d(d-1)S_2/2, so Newton's second identity
gives p_(d,2)=d(d-1)S_2, with no absolute-square substitution. C028a's
strict S_2 is an inherited actual-family input; this audit does not
reaudit its earlier zero-sum proof. Multiplication by gamma_0 and the
real translation preserve C028b's multiplicities and imaginary heights.

For each individual factor with alpha=a+ib, B=|b|=0 gives h_B=0
almost everywhere, including alpha=0. For B>0 Tonelli applies to a
nonnegative measurable integrand and produces pi B; it does not require
an integrable dominating function in the parameter. The two Taylor
remainders in (8) each have magnitude at most
a^2/[2(T-|a|)], including negative a by using |a| for the interval.
Thus the translation term vanishes in the symmetric limit. These
individual limits are used only after the combined sum has its
O_d(|y|^(-2)) absolute bound. Local factorization at every real root,
including zero and all multiplicities, gives only integrable logarithmic
singularities. Consequently the limiting sum is the ordinary L1
integral in (1), not a principal value or a subtraction of infinite
integrals. There is no boundary-root exception.

In (9) the factor two from the two rays cancels the 2 in the even
Taylor index 2k. Integration gives exactly k(2k-1) in (10); the first
term is -p_(d,2)/T. The remaining indices start at k=2, so the smallest
denominator is 6 and the geometric ratio is (rho_d/T)^2. The
coefficient cutoff ensures rho_d/T<=1/2 even at T=2K_d, making the
factor 1/[6(1-(rho_d/T)^2)] at most 2/9. This verifies both remainder
constants. The first asymptotic term is negative; the statement does
not assert that the whole tail is negative at every T>rho_d. All these
estimates keep d fixed. The central integral in (4) remains unpaid.

## Mathlib

Not checked. Availability of a full matching theorem for this actual
reciprocal-Jensen identity and fixed-degree tail is unknown; no absence
or formal verification is claimed. The analytic and algebraic steps are
proved above. The cited source formulas supply methodological coverage,
not a formally checked implementation or a missing uniform height bound.
