# Corollary 997x: prescribed Hermite jets exceed the original coefficient cap

## Hypotheses

Use exactly C997w's degree-at-most-n polynomial p_n(y)=sum_(j=0)^n
A_(j,n)y^j, for integer n>=3, and its definitions

    m=min{n,ceil(2n/log n)}, ell=n+1-m,
    theta=(n+1)/(2n), b=exp(i theta), alpha=(-7/2+i/2)n,
    f_n(y)=exp(alpha Log_n(y)),
    Log_n(y)=Log(b^(-1)y)+i theta.

The branch has domain Re(b^(-1)y)>0; Log on the right half-plane
has argument in (-pi/2,pi/2). The interpolant matches f_n's derivatives
at b through order ell-1. Retain C997s's original complex coefficient
norm and cap B_n=exp(sqrt(n)), with no scalar renormalization.

## Conclusion

For every integer n>=4096,

    sum_(j=0)^n |A_(j,n)| > exp(n/4-9/4) > exp(sqrt(n)).   (1)

Thus this particular successful uncapped family is eventually
inadmissible for C997s's capped objective. This gives no lower bound
on that objective, excludes no other coefficients, and does not
invalidate C997w's uncapped residual theorem or settle Xi positivity.

Step389, 11 November2026: RESEARCH / REPRODUCTION / NEGATIVE under
unchanged pre-invocation SPECIALIZE review387. This is a local
specialization of known derivative tools, not a claim of originality.
The independent audit in step390 below accepts (1) with its stated scope.

## Proof

### Imported finite-degree inputs

Import V. K. Jain, *An improved inequality for k-th derivative of a
polynomial*, Glasnik Matematicki 35(55) (2000), 215-219, p215,
(1.1)-(1.2), [journal PDF](https://web.math.pmf.unizg.hr/glasnik/35.2/35(2)-03.pdf).
For a complex polynomial p of actual degree d, R>0 and integer
1<=k<=d, the cited bound is

    max_(|y|=R)|p^(k)(y)|
      <= d(d-1)...(d-k+1) R^(-k) max_(|y|=R)|p(y)|.      (2)

The inspected source obtains (2) by successive Bernstein inequalities
as the degree decreases. There is no root-location or fixed-order
hypothesis. Reuse review387/step388's source coverage, without
reproving (2). Also import NIST DLMF 4.7.11's exact complex-power
derivative formula, with branch conventions 4.2.28-30:
[derivatives](https://dlmf.nist.gov/4.7.E11),
[powers](https://dlmf.nist.gov/4.2.E28).
The branch specialization and original coefficient-norm comparison
below are the necessary family-specific work. No asymptotic theorem
or interpolation remainder estimate is required.

### Branch and available growing jet

Let n>=4096 and k=floor(n/2). Since
log2=integral_1^2 dx/x>1/2, log n>=12log2>6. Therefore

    ceil(2n/log n)<2n/log n+1<n/3+1<n.

The minimum in m is inactive, m<n/3+1, and consequently
ell=n+1-m>2n/3>k. Also 1<=k<=n. Hence this jet is indeed prescribed.

Near b write y=bx, with x near 1. The fixed branch gives exactly

    f_n(bx)=exp(i alpha theta) exp(alpha Log x).

Apply DLMF's local power derivative formula near x=1 and the linear
change y=bx. It follows that

    f_n^(k)(b)=b^(-k) exp(i alpha theta)
                          product_(r=0)^(k-1)(alpha-r).

Now |b|=1 and |exp(i alpha theta)|=exp(-n theta/2)
=exp(-(n+1)/4). The real part of alpha-r is -(7/2)n-r,
so |alpha-r|>=(7/2)n. By derivative matching,

    |p_n^(k)(b)|=|f_n^(k)(b)|
        >=exp(-(n+1)/4)((7/2)n)^k>0.                   (3)

This uses no incompatible global principal-power substitution and is
exact at every finite n and k.

### Actual degree, coefficient norm and effective threshold

Let d be p_n's actual degree. Nonvanishing in (3) forces d>=k,
so constants and all smaller-degree cases are excluded explicitly.
For M_n=sum_(j=0)^n |A_(j,n)| and |y|=1, the triangle inequality
gives |p_n(y)|<=sum |A_(j,n)||y|^j=M_n. Apply (2) at R=1 and b:

    |p_n^(k)(b)|<=d(d-1)...(d-k+1)M_n<=n^k M_n.

Combining with (3), M_n>0 and

    log M_n>=-(n+1)/4+k log(7/2).                      (4)

Here 1<log(7/2)<2 admits elementary strict bounds. For integers r>=2,
r!>=2^(r-1), strictly for r>=3. Thus the positive exponential series
gives exp(1)=2+sum_(r>=2)1/r!<2+sum_(r>=2)2^(-(r-1))=3<7/2.
Also exp(2)>1+2+2=5>7/2. Monotonicity proves both logarithm bounds.
Since k>=n/2-1 and n/2-1>0, (4) yields

    log M_n>=-(n+1)/4+(n/2-1)log(7/2)
            >-(n+1)/4+n/2-2=n/4-9/4.

Finally n>=4096 implies sqrt(n)<=n/8 and n/8>9/4, whence
n/4-9/4>n/8>=sqrt(n). Exponentiation proves (1), including its
effective onset and all ceiling/degree qualifications.

Cancellation between the Hermite summands cannot evade the prescribed
jet in (3). But different polynomials having small complete residual
need not have these jets. Thus the capped infimum E_n, alternative
capped constructions, paid leakage, selected/both-sign transfer,
assay/reconstruction, complements/regulators, L993, L984(H), L966/L968
forcing and L030-L032/C032a actual-Xi positivity remain unresolved.
No numerical experiment, infinite interchange or actual-Xi assumption
is involved. C997r's different Taylor family and the step372 finite
generator failures are contrasts only, not mathematical inputs.

### Independent audit — step390, 11 November 2026

The audit accepts (1), reusing unchanged SPECIALIZE review387. This is
verification of the existing specialization, not a further coefficient
obstruction or a new result beyond the cited tools and local proof.

The exact inputs needed from C997w are (1), (5), the definitions of
m, ell, alpha and b, and degree at most n. Its residual estimates are
not used to prove (1). At x=1, the branch Log x is holomorphic and
Log 1=0; the chain rule contributes precisely b^(-k). Since
Im(alpha)=n/2, the constant exponential has modulus
exp(-theta*n/2)=exp(-(n+1)/4). Each factor alpha-r has real part
-(7/2)n-r and hence modulus at least (7/2)n. The derivative is
nonzero; no cancellation or root-location premise is being assumed.

For every integer n>=4096, log n>6 makes the ceiling estimate strict:
m<n/3+1<n and ell>2n/3>floor(n/2). Thus the chosen positive derivative
order is available. Its nonvanishing separately proves d>=k before
Bernstein is used with actual degree d; d<=n then permits the weaker
factor n^k. The triangle bound uses the original complex monomial
coefficient norm, with no rescaling or change of basis.

All threshold comparisons are strict where required. In particular,
with q=n/2-1>0 and log(7/2)>1, q*log(7/2)>q>n/2-2, which independently
checks the relaxed lower estimate following (4). The proof's series
bounds justify its logarithm bounds without numerical rounding.
Finally sqrt(n)<=n/8 follows already from n>=64, and n/8>9/4 holds
throughout the claimed n>=4096 range. Thus (1) holds at the stated
endpoint as well as for all larger integers; no eventual threshold is
being inferred from finite samples.

The external inputs retain exactly their cited hypotheses: complex
polynomial, circle radius one, integer derivative order at most actual
degree, and a local holomorphic power branch. No additional theorem,
asymptotic estimate, mathematical script or numerical certificate is
needed. C997w supplies the degree and interpolation premises, while
C997s fixes the original cap. All-polynomial lower bounds for E_n and
every actual-Xi transfer remain outside this audit.

## Mathlib

Full matching coverage for this n-dependent Hermite coefficient-cap
specialization has not been checked; no absence claim is made.
Jain's cited complex-circle Bernstein bound and DLMF's branch-local
power derivative identity are the external inputs. Generic polynomial
support alone would not establish the branch and jet qualifications.
No Mathlib theorem is assumed.
