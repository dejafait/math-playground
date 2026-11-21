# Corollary C032t: compact weighted heat sign from the explicit formula

## Hypotheses

Use C032j's actual-zero normalization and C032s's hypotheses and
qualifications. Thus Z+ is the multiset of nontrivial zeta zeros
rho=beta+i*gamma with gamma>0, including multiplicity,

    z_rho=gamma-i*(beta-1/2),  |beta-1/2|<1/2,
    H(u)=sum_(rho in Z+) exp(-u*z_rho^2),
    K(u)=sqrt(u)*H(u),
    u_sigma(t)=t/(1+4*sigma*t),
    D(t)=ell_2(t)-ell_1(t).

Retain the cited zero-counting and zero-ordinate exclusion. The final
assembly also retains C032s's finite-zero, heat and fixed-v1 external
preprint inputs. Their source-wide correctness and finite zero data
are not independently verified here. No RH, positivity of p_sigma,
full cancellation J_eta=0, or unsmoothed realization is assumed.

## Conclusion

On the whole closed interval, not merely at sampled points,

    K'(u)<-1/(40*u),  1/10000<=u<=1/200.                    (1)

Consequently C032s's adjoining sign ranges and finite-mass conclusion
give

    D(t)>0 for every t>0,
    0<integral_0^infinity D(t) dt<infinity.                 (2)

This closes the remaining sign hypothesis for the fixed-width finite
positive Levy difference, subject to the retained inputs. It does not
construct a signed positive output, prove a compound-Poisson law
comparison, impose J_eta=0, or prove actual-Xi positivity or RH.
This local specialization passed critical audit1558 under its stated
external-input qualifications; it is not a claim of novelty beyond
all literature or an independent certification of those inputs.

## Proof

### Exact imported formula and normalization

Reuse the source coverage in review1555 for the approved target of
assessment1554. Import the unconditional explicit formula, not a
spectral interpretation assuming RH. A precise source in the Mellin
normalization used below is Alain Connes, *Heat Expansion and Zeta*,
[arXiv:2402.13082v1, 20 February 2024](https://alainconnes.org/wp-content/uploads/heat-zeta.pdf),
Section 2, equations (4)-(9), printed p.4. In particular (5) sums over
the complex nontrivial zeros, while (7) gives the archimedean
distribution and (6) includes every prime power. The Gaussian transform
is (13), p.5, and the archimedean change of variables is (15), p.5.
Neither Theorem 1.1 nor the real-spectrum version (11) is used.
The same unconditional zero-sum identity is stated with an additive
Fourier convention in Andres Chirre and Felipe Goncalves, *Bounding
the log-derivative of the zeta-function*, Math. Z. 300 (2022),
1041-1053, [Proposition 5](https://link.springer.com/article/10.1007/s00209-021-02820-9);
it is not necessary to import the RH-dependent estimates elsewhere
in that article. No general explicit formula is reproved here.

For each real u>0 set

    F_u(v)=exp(-(log v)^2/(4*u))/(2*sqrt(pi*u)),
    f_u(v)=v^(-1/2)*F_u(v),                 v>0,
    B(x)=exp(x/2)/(exp(x)-exp(-x)),         x>0,
    c=log(4*pi)+gamma_E.

Here B is an archimedean kernel, not C032j's exponent B_sigma.
The functions f_u are smooth and decay faster than every prescribed
power at both endpoints after the displayed v^(-1/2) factor; hence
they satisfy the source's Mellin hypotheses with any fixed delta>0.
The same is true of all derivatives required by the explicit formula.
Indeed, on setting x=log v these statements reduce to Gaussian decay
times a polynomial and a fixed exponential in x. Also
f_u^sharp(v)=v^(-1)*f_u(v^(-1))=f_u(v).
The cited Gaussian transform gives

    tilde(f_u)(s)=exp(u*(s-1/2)^2).

The identity holds for complex s as well: the defining integral is
dominated on every compact s set by a Gaussian times exp(C*|x|).
At a zero rho the transform is exp(-u*z_rho^2); at s=0,1 it
equals exp(u/4). Pairing rho with 1-rho, preserving multiplicity,
and using the exclusion of ordinate zero gives an all-zero sum of
2*H(u). Both positive-ordinate zeros in an off-line conjugate pair
remain separate terms; they receive no further factor of one half.

Thus equations (5)-(7), with the change of variables in (15), give

    H(u)=exp(u/4)-W(u)/2-P(u),                             (3)
    W(u)=c/(2*sqrt(pi*u))
       +1/sqrt(pi*u)*integral_0^infinity
          [exp(-x^2/(4*u))-exp(-x/2)]*B(x) dx,
    P(u)=1/(2*sqrt(pi*u))*sum_(n>=2)
          Lambda(n)*n^(-1/2)*exp(-(log n)^2/(4*u)).

Lambda is the von Mangoldt function, zero except at prime powers
and equal to log p at p^m. The coefficient of P follows because
the two terms of (6) agree and the all-zero formula is divided by
two. The term exp(u/4) retains both pole evaluations before that
division. Trivial zeros are already accounted for by W; no extra
trivial-zero sum is added. Equation (3) is an exact identity, not
an asymptotic expansion. The subtraction inside W stays inside
its integral until differentiation; its separate pieces need not
be integrable at zero.

### Uniform differentiability and the weighted identity

All required differentiations are justified on the larger compact
real interval [a,b]=[1/20000,1/100], whose interior contains the
target interval. We use differentiation under a sum or integral
via dominated convergence for its difference quotients, as detailed
below. No asymptotic remainder is differentiated.

First, for delta=beta-1/2 and a<=u<=b,

    |exp(-u*z_rho^2)|<=exp(b/4)*exp(-a*gamma^2),
    |z_rho^2|=gamma^2+delta^2<=gamma^2+1/4.

The counting input N(T)=O(T*log(T+2)) therefore makes the sums of
these bounds and their products with gamma^2+1/4 finite. For example,
grouping gamma in [j,j+1) bounds the tail by a constant times
sum_(j>=1) (j+1)^3*log(j+3)*exp(-a*j^2), which converges.
There are finitely many initial zeros. This proves uniform
convergence of H and its first derivative and justifies the
zero-side differentiability, including all complex ordinates.
Conjugate symmetry makes H and K real on this interval.

Write g_u(x)=exp(-x^2/(4*u)). For 0<x<=1,

    0<B(x)<=exp(1/2)/(2*x),
    |g_u(x)-exp(-x/2)|<=x^2/(4*a)+x/2,
    |partial_u g_u(x)|<=x^2/(4*a^2).

The first bound follows from sinh(x)>=x. Thus the subtracted
integrand defining sqrt(u)*W(u) and its u derivative are bounded
near zero by constant multiples of 1+x and x, respectively.
For x>=1 put C_B=(1-exp(-2))^(-1). Then

    B(x)<=C_B*exp(-x/2),
    |g_u(x)-exp(-x/2)|<=exp(-x^2/(4*b))+exp(-x/2),
    |partial_u g_u(x)|
          <=x^2*exp(-x^2/(4*b))/(4*a^2).

After multiplication by B these are integrable common majorants.
The real mean-value theorem bounds difference quotients on a
neighborhood of each interior u by the same derivative envelope.
Dominated convergence therefore differentiates the subtracted
integral without separating its divergent pieces. In particular,

    (sqrt(u)*W(u))'
       =1/(4*sqrt(pi)*u^2)*integral_0^infinity
                            x^2*B(x)*exp(-x^2/(4*u)) dx.  (4)

For the prime sum, 0<=Lambda(n)<=log n. The summands of
sqrt(u)*P(u) and their derivatives are bounded, up to fixed
constants, by

    [(log n)+(log n)^3]*n^(-1/2)
                         *exp(-(log n)^2/(4*b)).

Here 1/(4*b)=25. For n>=3, log n>1, so the exponential is at
most n^(-25); the displayed sequence is summable. The n=2 term
is finite. Uniform domination justifies differentiation and gives

    (sqrt(u)*P(u))'
       =1/(8*sqrt(pi)*u^2)*sum_(n>=2)
          Lambda(n)*(log n)^2*n^(-1/2)
                         *exp(-(log n)^2/(4*u)) >=0.      (5)

The constant term in sqrt(u)*W(u) has zero derivative. Combining
(3)-(5) now proves the exact identity

    K'(u)=exp(u/4)*(1/(2*sqrt(u))+sqrt(u)/4)
       -1/(8*sqrt(pi)*u^2)*integral_0^infinity
                            x^2*B(x)*exp(-x^2/(4*u)) dx
       -(sqrt(u)*P(u))'.                                 (6)

In particular the entire weighted prime contribution is nonpositive;
discarding it gives a rigorous upper bound. No effective estimate
from a heat asymptotic or a preprint derivative remainder is needed.

### Explicit archimedean margin against the pole term

For 0<x<=1 the absolutely convergent power series for sinh gives

    sinh(x)/x
       =1+sum_(k>=1) x^(2*k)/(2*k+1)!
       <=1+x^2*(sinh(1)-1)
       <1+x^2/2<=1+x/2<=exp(x/2).

Indeed e<3 implies sinh(1)<3/2. The elementary inequality e<3
follows by comparing 1/n!, n>=2, with 1/2^(n-1), with strict
inequality for n>=3. Consequently

    B(x)>1/(2*x),                  0<x<=1.

Positivity of B outside this interval and direct Gaussian integration
give

    integral_0^infinity x^2*B(x)*exp(-x^2/(4*u)) dx
       > (1/2)*integral_0^1 x*exp(-x^2/(4*u)) dx
        =u*(1-exp(-1/(4*u))).                             (7)

On the target interval u<=1/200, so exp(-1/(4*u))<=exp(-50)<1/100:
e>2 and 2^50>100 suffice. Since pi<4, (7) shows that the
archimedean contribution in u times (6) is strictly less than

    -99/(800*sqrt(pi)) < -99/1600.                        (8)

For the positive pole contribution use sqrt(u)<1/14,
1/2+u/4<=401/800, and

    exp(u/4)<=exp(1/800)<800/799.

The last inequality follows termwise from exp(v)<1/(1-v) for
0<v<1. Therefore the pole contribution in u times (6) satisfies

    exp(u/4)*sqrt(u)*(1/2+u/4)
       <401/11186 <59/1600.                              (9)

The final comparison is exact: 401*1600=641600 is less than
59*11186=659974. Combining (5), (8), and (9) proves

    u*K'(u)<59/1600-99/1600=-1/40,

uniformly throughout the closed target interval. This proves (1)
without a numerical grid, omitted prime powers, or an RH assumption.
The source identities are imported; (7)-(9) are precisely the
effective specialization not supplied by the assessed sources.

### Assembly with the established endpoint ranges

C032s proves K'<0 on (0,1/10000] and on [1/200,1/4], with
the input qualifications stated there. Equation (1) covers the
entire intervening closed interval. Hence K'<0 on (0,1/4].
For every t>0 one has 0<u_2(t)<u_1(t)<1/4, and C032s's
exact Gaussian identity is

    D(t)=t^(-3/2)*integral_(u_2(t))^(u_1(t)) -K'(u) du.

The integrand is continuous and strictly positive, and the interval
has positive length, so D(t)>0. The finite absolute mass already
proved in C032s gives finiteness of its integral. Its strict
positivity follows, for example, by integrating the continuous
positive function D over any nondegenerate compact subinterval
of (0,infinity). This proves (2).

C032s's failure of its absolute counting envelope is unchanged;
the explicit formula supplies different cancellation information.
The reverse ordering is still excluded. Positivity and finite mass
are the inputs for a later compound-Poisson comparison, not such a
comparison itself. Full cancellation, output positivity for a signed
width input, and actual-Xi realization remain separate. ∎

### Critical audit1558 — 18 November 2026

The complete proof and C032s's complete endpoint and mass arguments
were independently checked in this invocation under the unchanged
SPECIALIZE assessment1556. No mathematical defect or missing local
hypothesis was found. This accepts (1)-(2) with the stated external
qualifications; it introduces no stronger conclusion.

The primary Connes formulas (4)-(7), (9), (13), and (15) were checked
directly at the cited version. The Gaussian satisfies the Mellin
endpoint hypotheses for every fixed positive decay exponent. The
all-zero formula pairs rho with 1-rho, so division by two applies
once, to both pole evaluations, the archimedean distribution and
the doubled prime-power sum. The positive-ordinate off-line pair
is retained with both multiplicities. Formula (11)'s RH assumption
is not used. Changing the integration variable to log(v) in (7)
gives exactly B(x) and the subtraction exp(-x/2) in (3).

On [1/20000,1/100], the zero majorants include the factor
gamma^2+1/4 for the derivative. Counting makes their shell sums
finite. At the archimedean endpoint x=0, the original subtracted
integrand is O(1+x) and its derivative is O(x), uniformly; the
two separate un-subtracted integrals are never differentiated.
The displayed common integrable majorants at infinity and the
summable prime envelopes justify every real derivative in (4)-(6)
on an open neighborhood of the entire target interval. The prime
derivative is nonnegative before its minus sign in (6), including
every prime power. No limiting heat expansion is differentiated.

The strict kernel comparison in (7) holds on a positive-length
interval and therefore yields a strict integral inequality. The
audit checked the exact margins after multiplying by u: the
archimedean magnitude exceeds 99/1600, while the pole contribution
is less than 401/11186<59/1600. Their difference exceeds 1/40;
discarding the favorable prime term cannot weaken this conclusion.
All estimates include both endpoints of the target interval.

C032s's separately audited small-time range is (0,1/10000], and
its high-zero comparison covers [1/200,1/4]. These join the compact
range without a gap. For each finite t>0, u_2(t)<u_1(t)<1/4 and
u_2(t)>0, so C032s(3) integrates a continuous strictly positive
function over an interval of positive length. Its zero-endpoint
majorant is O(t^(-1/2)+log(1/t)); its infinity majorant is
O(t^(-3/2)). Continuity covers the intervening compact intervals.
This verifies strict positive total mass and finite absolute mass,
without requiring positivity of p_sigma or either individual
Levy density for this particular difference argument.

The audit directly checked the fixed-v1 Gaussian formula and the
separate j=0,1 heat-error cases used in C032s, together with the
stated counting and finite-zero inputs. It did not independently
verify the finite-zero data, Bellotti-Wong's theorem, or the whole
preprints. No compound-Poisson comparison is proved in this audit.

## Mathlib

Full matching coverage has not been checked and is unknown. No
Mathlib theorem is substituted for the explicit formula or the
external zero and heat inputs. Supporting dominated-convergence,
Gaussian-integration and exponential-series APIs have not been
assessed for this informal specialization. The proof uses exact
inequalities and no machine-computation certificate.
