# Corollary C028e: reciprocal Jensen degree-uniform exterior log tail

## Hypotheses

Use the unchanged actual entire function and monic polynomials of C028a:

    b_j=gamma_j/gamma_0,  gamma_j=j! M_(2j)/(2j)!,
    F(u)=sum_(j>=0) b_j u^j/j!,  b_0=1,  b_j>0,
    P_d(x)=sum_(j=0)^d binom(d,j)b_j x^(d-j).

Here gamma_0=M_0>0 and d>=3 is an integer. Use C028d's centering
and combined logarithm, with y real:

    Q_d(y)=P_d(y-b_1),
    f_d(y)=log|Q_d(y)|-d log|y|.

This is C028d's Q_d, not the scaled ordinary Jensen polynomial called
Q_d in C028b. No RH, root reality, simplicity, global logarithm or
degree-uniform root bound is assumed. Define fixed actual-family constants

    M=exp(b_1) F(1),    A_0=2 sqrt(M),    C=8M.

The positive entire series gives 1<=M<infinity. These constants do not
depend on d or on the real cutoff parameter A.

## Conclusion

For every integer d>=3 and every real A>=A_0,

    integral_(|y|>A d) |f_d(y)| dy <= 8M d/A.

In particular the exterior integral is an ordinary absolutely convergent
Lebesgue integral and

    |integral_(|y|>A d) f_d(y) dy| <= C d/A.

There are no real zeros of Q_d in this exterior region. More precisely,
for every real |y|>=A_0 d,

    |Q_d(y)/y^d-1| <= 2M d^2/y^2 <= 1/2,
    |f_d(y)| <= 4M d^2/y^2.

This meets the degree-uniform exterior target. It gives no bound for
the central signed integral and does not prove C028b's RH-equivalent
H_d=o(d). C028d's full-line identity is not a premise of this result.

## Proof

### Known method and the quantitative specialization

The source assessment1509, approved separately in review1510, covers
the classical coefficient method used here. Cormac O'Sullivan,
*Zeros of Jensen polynomials and asymptotics for the Riemann xi function*,
arXiv:2007.13582v2, 9 December 2020,
[Section 3.2, Lemma 3.4, (3.3)-(3.4)](https://arxiv.org/html/2007.13582v2#S3.SS2),
gives the formal product identities for reciprocal Jensen polynomials.
Thomas Craven and George Csordas, *Jensen polynomials and the Turan and
Laguerre inequalities*, Pacific J. Math. **136**(2) (1989), 241-260,
[Lemma 2.2 and proof, pp.244-245](https://msp.org/pjm/1989/136-2/pjm-v136-n2-p03-s.pdf),
give arbitrary-entire Jensen compact approximation using Cauchy
coefficient estimates. Neither result requires real zeros for these
purposes. Their general approximation theorem is not reproved or used
as an unproved integrable majorant.

We import the standard Cauchy coefficient inequality: if G is holomorphic
on a neighborhood of the closed disk |u|<=R and G(u)=sum h_k u^k,
then |h_k|<=R^(-k) max_(|u|=R)|G(u)|. The required application below
uses R=1 and an entire G. The finite product specialization, constants
and logarithmic integration are supplied explicitly because no inspected
source states this exact tail bound. This is reproduction/specialization
of known methods, with no claim of progress beyond the sources checked.

### Centered coefficients with all factorials retained

Put

    G(u)=exp(-b_1 u)F(u)=sum_(k>=0) h_k u^k.

Both factors are entire, so the coefficient convolution is valid on
every compact disk. For each k it is the finite identity

    h_k=sum_(j=0)^k b_j (-b_1)^(k-j)/(j!(k-j)!).             (1)

In particular h_0=1 and h_1=b_1-b_1=0. C028d's finite binomial
coefficient formula, specialized to (1), gives

    c_(d,k)=[y^(d-k)]Q_d(y)
           =binom(d,k) sum_(j=0)^k binom(k,j)b_j(-b_1)^(k-j)
           =binom(d,k) k! h_k=(d)_k h_k,                   (2)

where (d)_0=1 and (d)_k=d(d-1)...(d-k+1) for 1<=k<=d.
Thus, exactly and without a limit in d,

    Q_d(y)/y^d=sum_(k=0)^d (d)_k h_k/y^k     (y!=0).        (3)

This checks that exponential centering produces precisely the original
translation P_d(y-b_1); it does not replace the polynomial by another
family. The only coefficient cancellation used here is h_1=0, from
the specified centering.

### One coefficient constant for every degree

For complex |u|=1 the positivity and entire convergence of the actual
F series give

    |G(u)|=|exp(-b_1 u)F(u)|
           <=exp(b_1) sum_(j>=0) b_j/j!=M.

Here b_1 is real and positive, so |exp(-b_1 u)|<=exp(b_1).
Cauchy's coefficient inequality therefore gives |h_k|<=M for every
k>=0. This is a bound for the fixed entire function G, not for a
degree-dependent function. Also (d)_k<=d^k for every 0<=k<=d.

For |y|>=A_0 d set r=d/|y|. Since M>=1, A_0>=2, so 0<r<=1/2.
Writing (3) as 1+E_d(y), its constant and linear coefficients give

    |E_d(y)| <= sum_(k=2)^d (d)_k |h_k|/|y|^k
              <= M sum_(k=2)^infinity r^k
              =M r^2/(1-r)<=2M r^2<=1/2.                 (4)

The last inequality uses r<=1/(2 sqrt(M)). Every bound applies to
each finite d>=3 directly; no eventual degree threshold or untreated
small-degree cases occur. In particular 1+E_d(y) cannot vanish.

### Local logarithm and the unbounded exterior integral

For any complex E with |E|<=1/2, the absolutely convergent Taylor
series of log(1+E), normalized to be zero at E=0, has real part
log|1+E|. Hence

    |log|1+E|| <= sum_(n>=1) |E|^n/n
                 <= |E|/(1-|E|)<=2|E|.                  (5)

For real y in (4), |y^d|=|y|^d and Q_d(y) is nonzero, so

    f_d(y)=log|Q_d(y)/y^d|=log|1+E_d(y)|.

Applying (4)-(5) proves |f_d(y)|<=4M d^2/y^2. This local logarithm
is taken only in the disk |(1+E)-1|<=1/2. No logarithm is continued
through any central zero, and the argument applies equally to positive
and negative y and to odd and even degrees.

For A>=A_0 the pointwise majorant is integrable on both rays, and

    integral_(|y|>A d) |f_d(y)| dy
       <=4M d^2 (integral_(A d)^infinity y^(-2)dy
                  +integral_(-infinity)^(-A d) y^(-2)dy)
       =4M d^2 * 2/(A d)=8M d/A.

The triangle inequality now gives the requested signed-tail bound.
There is no exchange of a degree limit with an integral, infinite root
sum, or principal-value cancellation. Boundary points do not affect
the integral, and (4)-(5) also hold at |y|=A_0 d.

The exterior contribution divided by d is thus uniformly at most
8M/A and can be made small by choosing A large. This does not control
the contribution from |y|<=A d. The earlier positive-reference budget
stops in C028a/C028c remain intact; they are comparisons, not premises
of this estimate. The independent central payment remains unresolved.

### Independent conceptual audit1514 (2026-11-18)

The complete argument was replayed under assessment1511, with no
mathematical correction. The inputs used are C028a's actual positive
entire series and C028d's finite centered coefficients; neither the
full-line integral nor root reality is needed for the exterior bound.

In (1), h_k is an ordinary power-series coefficient. Multiplying it
by k! gives the inner binomial sum in (2), and multiplying again by
binom(d,k) gives precisely (d)_k h_k. Thus no exponential-series
factorial has been lost. The shift is the same fixed real b_1 in every
degree, and h_1=0 exactly. The actual coefficients are positive, so
the entire sum F(1) is finite and bounds |F(u)| on |u|=1. Together
with b_1>0 this verifies the single Cauchy constant M=exp(b_1)F(1)>=1
for every h_k; it is independent of d and A.

At the smallest allowed radius, r<=1/(2sqrt(M))<=1/2. Hence
M r^2/(1-r)<=2M r^2<=1/2, including equality in either estimate.
The ratio Q_d(y)/y^d lies in the closed disk of radius 1/2 about one,
which excludes zero and stays strictly inside the domain of its
normalized logarithm. The log-series bound at |E|=1/2 is valid and
gives 2|E|. Negative y and odd d cause no sign change in the modulus
identity because |y^d|=|y|^d. These checks establish the pointwise
4M d^2/y^2 bound on both rays, including |y|=A_0 d.

Each ray contributes 1/(Ad) to the integral of y^(-2), so the total
is 8M d/A, with no missing factor of two. The finite estimate
(d)_k<=d^k holds for every k<=d; no small-degree exception, eventual
threshold or interchange of a degree limit occurs. The audit therefore
passes for all stated d>=3 and A>=A_0. It verifies a known-method
specialization only. Neither the region |y|<=Ad nor the RH-equivalent
condition H_d=o(d) is controlled by this estimate.

## Mathlib

Not checked. Full matching coverage for the actual reciprocal-Jensen
degree-uniform exterior integral is unknown; no absence or formal
verification is claimed. Cauchy's coefficient inequality and the local
logarithm series are standard named analytic inputs. The full
specialization and its integration justification are written above.
The informal proof passed the separate conceptual audit1514 above;
this does not claim formal verification or new Mathlib coverage.
