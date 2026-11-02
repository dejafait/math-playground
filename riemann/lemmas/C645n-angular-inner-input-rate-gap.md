# Corollary 645n: an angular inner-function test and its exponent deficit

## Hypotheses

Fix n>=5, d=5/4, x=-d, R=11/8, U=R^2, eta=1/100, and
t_j=j/n for 0<=j<n. Let Z be a finite set of distinct points with
Re(a)=x and |a|<=R-eta, containing x. Assign positive integer
original simple-pole residues r_a and set M=sum_a r_a<=n/3.
The set and residues are the same for every theta. Define

    B_theta(v)=product_j R*(v-i*exp(i*theta)*t_j)
                           /(R^2+i*exp(-i*theta)*t_j*v),
    q_theta(zeta)=sum_a [r_a*B_theta(x)/(R*B_theta(a))]
                            /(zeta-a/R).

Use C645g's normalized circle measure, Hardy space H^2 with
nonnegative modes, H^2_- with strictly negative modes, and
H_q f=P_-(q*f). All operator norms below are largest norms.
There is no pole separation or ordinate symmetry hypothesis.
The stated line avoids every rotated grid, since |a|>=d>1>t_j.

Put

    A_n=(mean_theta ||H_q_theta||^2)^(1/2),
    f_theta(zeta)=B_theta(R*zeta),
    J_n=(mean_theta ||H_q_theta f_theta||_2^2)^(1/2),
    E_n=(mean_theta |B_theta(x)|^2)^(1/2),
    rho=(R-eta)/R=273/275,
    S(zeta)=sum_a r_a/(zeta-a/R).

## Conclusion

The exact inner-function test gives

    ||f_theta||_2=1,
    H_q_theta f_theta=(B_theta(x)/R)*S,
    A_n >= J_n = (||S||_2/R)*E_n,                         (1)
    M <= ||S||_2 <= M/sqrt(1-rho^2).

Define the evaluated rate

    lambda=log(11/10)+(201/80)*log(201/121)
                         -(9/4)*log(9/5).

It satisfies the rigorous bounds

    47/1000 < lambda < 49/1000,
    lambda-1/32 > 63/4000 > 0,                           (2)

with decimal preview lambda=0.04792001946... . Uniformly for all n>=5,

    (335/363)*exp(-1/4)/(sqrt(pi)*n^(1/4))*exp(-lambda*n)
        <= E_n <= exp(-lambda*n).                        (3)

Consequently this supplies the genuine, weaker angular lower bound

    A_n >= c_* M n^(-1/4) exp(-lambda*n),
    c_*=(8/11)*(335/363)*exp(-1/4)/sqrt(pi)>0.             (4)

But the response of this particular input also satisfies

    exp(n/32)*J_n
       <= n/[3R*sqrt(1-rho^2)]
                         *exp(-(lambda-1/32)*n) -> 0,    (5)

uniformly over the admissible families. Thus the full inner-function
test, including its complete output rather than just one coefficient,
cannot supply the proposed uniform c*exp(-n/32) lower bound.
Equation (5) is NOT an upper bound on A_n. The angular operator target
is neither proved nor refuted. The result is unaudited local progress
and a method limit; no RH advance, actual-Xi realization, or certified
novelty is asserted.

## Proof

### Source scope and reason for the calculation

The unchanged invocation-start
[angular assessment](../drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md)
is EXPLORE for this exact angular target, family, Fourier conventions,
and threshold. The primary sources and scoped duplicate/failure checks
there are reused. C645g supplies the normalization and symbol, not an
angular estimate at this census. C645l's fixed-angle counterfamily and
C645m's failed ellipse envelope are contrasts, not premises here.

The projection convention is that of L. Baratchart, S. Chevillard and
T. Qian, *Minimax principle and lower bounds in H2-rational approximation*,
J. Approx. Theory 206 (2016), 17--47, author preprint v2 (24 March 2015),
[Section 4, (17)--(19)](https://arxiv.org/pdf/1501.01161v2),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004).
Scalar Fourier orthogonality and Parseval are imported in their usual
form from A. Levitt, *Analyse de Fourier et applications*,
[author PDF](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf),
version retrieved 2 November 2026, Theorem 1.3/Exercise 1.2,
Theorem 1.11/Corollary 1.12, printed pp.6,8 (PDF pp.12,14), as inspected
in the assessment. Dividing Lebesgue measure by 2*pi makes the constant
and every circle exponential have norm one. Parseval is used for a
scalar H^2_- function, not for an operator norm as a Hilbert norm.

The elementary negative-part identity in (1) is a direct specialization
to these finitely many poles. It is not a new Hankel theorem or a reproof
of Nehari/AAK. Its evaluated angular exponent, needed to compare this
test to 1/32, is not supplied by the inspected general identities.

### 1. Exact action of the inner input

For |v|<=R, every factor denominator has modulus at least
R^2-t_j*R>0. On |zeta|=1, the j-th factor of f_theta is

    (zeta-alpha_j)/(1-conjugate(alpha_j)*zeta),
    alpha_j=i*exp(i*theta)*t_j/R,

and has modulus one. Therefore f_theta is holomorphic near the closed
unit disk and has norm one. All B_theta(a) are nonzero by grid avoidance.
Every q_theta is a continuous strictly negative Fourier symbol, since
its poles lie in |zeta|<=rho<1. Its operator is bounded.

For any function f holomorphic near the closed disk and |alpha|<1,

    f(zeta)/(zeta-alpha)
      = f(alpha)/(zeta-alpha)
         +(f(zeta)-f(alpha))/(zeta-alpha).

The second term has a removable singularity and belongs to H^2;
the first has only strictly negative Fourier modes. Applying P_- to
this identity with alpha=a/R and f=f_theta proves (1), since
f_theta(a/R)=B_theta(a). This calculation keeps the denominator's
conjugated angle; no angular pole or complex phase is discarded in an
average. The inverse factors cancel before that average is taken.

The series

    S(zeta)=sum_(k>=0) (sum_a r_a*(a/R)^k)*zeta^(-k-1)

converges absolutely and uniformly on the circle. Its first coefficient
is M, so Parseval gives ||S||_2>=M. The geometric-series norm of an
individual kernel is (1-|a/R|^2)^(-1/2); the triangle inequality gives
the upper bound in (1). In particular 1-rho^2=1096/75625>0.
All sums here are finite over a, and there is no limiting interchange
over n or Z. The angular integrands are continuous and finite for each
family, since all factors avoid zero on the compact parameter circle.

### 2. Maximum angular product and its exact exponential rate

For a single t in [0,1], direct evaluation at x=-d gives

    |b_theta,t(x)|^2
      = U*(d^2+t^2-2*d*t*sin(theta))
                  /(U^2+d^2*t^2-2*U*d*t*sin(theta)).       (6)

Its denominator is positive. Its derivative with respect to
sin(theta) has the sign of

    -2*d*t*U*(U-d^2)*(U-t^2),

which is nonpositive, and negative for t>0. Therefore every factor,
and hence the product, is maximized at theta=-pi/2, where the grid
lies on the positive real axis. Set

    L(t)=log((U+d*t)/(R*(d+t))),
    b_n=|B_(-pi/2)(x)|=exp(-sum_(j=0)^(n-1) L(j/n)).

The argument of the logarithm exceeds one, since its numerator minus
its denominator equals (R-d)*(R-t)>0. Also

    L'(t)=(d^2-U)/((U+d*t)*(d+t))<0.

The decreasing left and right Riemann sums give the finite-n bounds

    n*integral_0^1 L(t)dt <= sum_j L(j/n)
       <= n*integral_0^1 L(t)dt + L(0)-L(1).              (7)

Evaluation of the elementary integrals yields exactly

    integral_0^1 L(t)dt
      = log(R/d)+(1+U/d)*log(1+d/U)
                          -(1+d)*log(1+1/d) = lambda,
    exp(-(L(0)-L(1)))
      = d*(U+d)/(U*(d+1))=335/363.

It follows that

    (335/363)*exp(-lambda*n) <= b_n <= exp(-lambda*n),    (8)

and E_n<=b_n. This is an exact product estimate with a bounded
endpoint correction, not a limiting Riemann-sum assumption.

### 3. A sufficiently wide arc near the angular maximum

Write theta=-pi/2+phi with |phi|<=n^(-1/2). Let h=1-cos(phi),
and for each t put

    A_t=2*d*t/(d+t)^2,
    C_t=2*U*d*t/(U+d*t)^2.

Both are nonnegative and at most 1/2, by (p-q)^2>=0. Formula (6) gives

    |b_theta,t(x)|^2/|b_(-pi/2),t(x)|^2
        =(1-A_t*h)/(1-C_t*h).                            (9)

Since h<=phi^2/2, one has 0<=A_t*h<=1/(4n)<=1/20.
The elementary bound -log(1-u)<=2u for 0<=u<=1/2 follows
by integrating 1/(1-u)<=2. Therefore

    log(|b_theta,t(x)|/|b_(-pi/2),t(x)|)
      = (1/2)*log(1-A_t*h)-(1/2)*log(1-C_t*h)
      >= (1/2)*log(1-A_t*h)
      >= -A_t*h >= -phi^2/4.

Multiplying the n bounds yields

    |B_theta(x)| >= b_n*exp(-n*phi^2/4)
                   >= b_n*exp(-1/4).                    (10)

The arc has angular length 2/sqrt(n), including wraparound modulo
2*pi. Integrating its square against normalized measure gives

    E_n^2 >= b_n^2*exp(-1/2)/(pi*sqrt(n)).

Together with (8) this is (3). It also proves that the particular
response has exponential rate lambda, up to the displayed polynomial
factors and the census factor M. No asymptotic saddle theorem or
unjustified uniform angular sample is used.

### 4. Exact comparison with the required rate

For q>1 and u=(q-1)/(q+1), integration of the finite geometric series
for 1/(1-u^2) gives

    2*sum_(k=0)^15 u^(2*k+1)/(2*k+1)
      < log(q)
      <= 2*sum_(k=0)^15 u^(2*k+1)/(2*k+1)
                 +2*u^33/(33*(1-u^2)).                  (11)

All numbers in (11) are rational when q is rational. Applying (11)
gives the following enclosures, with common denominator 10^12:

| logarithm | lower numerator | upper numerator |
| --- | ---: | ---: |
| log(11/10) | 95310179804 | 95310179805 |
| log(201/121) | 507514362462 | 507514362463 |
| log(9/5) | 587786664902 | 587786664903 |

Insert the two lower endpoints and the third upper endpoint for a
lower bound on lambda; reverse the choices for an upper bound.
Rational comparison proves (2). The complete exact series, remainder
bounds, endpoint correction, clearance and comparisons are saved in
`scripts/one-sided-hankel/angular-inner-input-rate-check.json`.
Reproduce with
`python3 scripts/one-sided-hankel/angular-inner-input-rate-check.py`.
The selected full `/readable_log_bounds` and `/checks` fields were
inspected. The decimal preview is not used in the proof.

Finally (1), (3), M<=n/3 and lambda>1/32 prove (4)--(5).
The exponential in (5) dominates its linear factor. Its upper bound is
uniform because all remaining constants depend only on fixed R,eta.
An operator can be much larger on another input; reversing A_n>=J_n
would be a mathematical error. In particular (5) supplies no
countersequence for A_n and does not settle the approved target.

## Mathlib

Full matching coverage has not been checked. Supporting finite
Blaschke, Hardy projection and Parseval identities are standard and
are imported or specialized as identified above; no Mathlib absence
claim is made. No numerical experiment is a substitute for the
uniform estimates (7)--(10) or the exact rational comparisons (11).
