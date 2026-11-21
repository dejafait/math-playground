# Lemma 964: a supplied negative Li margin gives an explicit mixed witness

## Hypotheses

Use the actual Xi function of L018, its paired zeros alpha_j from L024,
and beta_j=alpha_j^(-2), with multiplicities. Thus L026 gives
|Re alpha_j|>4 and |Im alpha_j|<1/2. Let n>=1 be an integer and
let epsilon,A>0 be supplied finite real numbers such that

    lambda_n <= -epsilon,             sum_j |beta_j| <= A.       (1)

Here lambda_n is the ordinary real zeta Li coefficient in the normalization
of Lagarias, Theorem 3.1, cited below. In particular the first inequality
is a hypothesis, not an asserted fact about zeta. Define L030's form

    Q(q)=sum_j beta_j^2 q(beta_j)^2

for real polynomials q; all squares in this statement are algebraic.

## Conclusion

The following entirely explicit constants use only n,epsilon,A:

    c = 1/16,                 M = 3^n,                 C = 8 M^2,
    eta = min{c, epsilon/(8 C A)},
    B = M sqrt(2/eta),         R = c + eta/2,           theta = c/R,
    tau = min{1, epsilon/(8 c A (2B+1))},
    D = ceil(log(B/((1-theta)tau))/log(1/theta)).                 (2)

Logs are natural. Here 0<theta<1, tau>0, and D is a positive integer.
There is an explicit real polynomial q_D of degree at most D satisfying

    Q(q_D) < lambda_n + epsilon/4 <= -3 epsilon/4 < 0.           (3)

In particular L030's H_D has a negative quadratic direction. No zero
locations, separations, simplicity hypothesis, finite head, or extra
tail modulus enter D or q_D. The coefficient sizes are not asserted to
be small, and this bound is not claimed sharp or computationally practical.

This conditional quantitative bridge was written in step160 and passed
an independent conceptual audit in step161 on 10 November 2026, with
the statement and constants unchanged. It supplies neither a negative actual Li coefficient
nor an actual off-line zero, and proves no actual mixed-positivity sign.
Deriving the supplied data from a height/deviation bound is separate.

## Proof

### Imported identity and the exact paired observable

Import J. C. Lagarias, *Li coefficients for automorphic L-functions*,
Ann. Inst. Fourier 57(5) (2007), 1689-1740,
[Theorem 3.1, equations (3.1)-(3.6), pp.1704-1706](https://www.numdam.org/article/AIF_2007__57_5_1689_0.pdf#page=17).
In its zeta specialization, G_n(s)=1-(1-1/s)^n satisfies

    sum_rho G_n(rho) conjugate(G_n(1-conjugate(rho)))
        = 2 Re(lambda_n) = 2 lambda_n.                         (4)

The sum is over all nontrivial zeros, with multiplicity, and is
absolutely convergent. The source's test class requires holomorphy in
the open critical strip and uniform O(1/|s|) decay outside |Im s|<=1;
G_n has these properties for each fixed positive integer n. Its only
pole is 0, and the reflected function's only pole is 1; neither is a
zero by L018. Reality of the zeta Li coefficients follows from the
real xi normalization; see also the source's (1.1)-(1.3), p.1690,
and Lemmas 2.2-2.3, pp.1701-1702. We use the absolute quadratic identity,
not a rearrangement of a conditionally convergent sum of linear terms.
No positivity of the Weil form is assumed.

The zeta specialization is explicitly included in the source: for the
trivial GL(1) representation, its completed entire function is 2*xi(s)
(p.1697). This has exactly the zeros and multiplicities of L018. The
constant factor does not change Li coefficients: in the derivative
definition (1.3), its contribution is the nth derivative of
s^(n-1)*log(2), which is zero for n>=1. In particular neither this
normalization nor the pairing below introduces an additional factor two.

Since G_n has real rational coefficients, the summand in (4) equals
G_n(rho)G_n(1-rho). For alpha with rho=1/2+i alpha, put
t=1/(2 alpha), beta=alpha^(-2), and w=(rho-1)/rho. Then

    w=(1+i t)/(1-i t),          t^2=beta/4,
    G_n(rho)G_n(1-rho)=2-w^n-w^(-n).

All denominators are nonzero. Define the real polynomial and the
analytic function

    P_n(z)=sum_{k=0}^{floor((n-1)/2)}
               (-1)^k binom(n,2k+1)(z/4)^k,
    a_n(z)=P_n(z)(1+z/4)^(-n/2),             |z|<4,              (5)

where the power is the analytic branch with value 1 at z=0.
The finite binomial identity

    (1+i t)^n-(1-i t)^n = 2 i t P_n(beta)

gives, without any critical-line assumption,

    2-w^n-w^(-n)
      = -((1+i t)^n-(1-i t)^n)^2/(1+t^2)^n
      = beta a_n(beta)^2.                                     (6)

The pair {alpha,-alpha} corresponds to {rho,1-rho}. Each member has
the same summand (6), and multiplicities agree by L018. Thus (4),
grouped only in pairs in an absolute sum, yields exactly

    lambda_n = sum_j beta_j a_n(beta_j)^2.                     (7)

Conjugation preserves the beta multiset, independently of the choice
of the alpha representatives. The sum in (7) is also directly absolute
by the uniform bound below and L024. In particular there is no missing
factor two and no replacement of the actual nodes by their ordinates.

### Fixed node disk and explicit analytic bounds

Write alpha=x+i y. L026 implies

    |beta|=1/(x^2+y^2)<c,
    Re(beta)/|beta|^2=x^2-y^2>63/4.

Consequently Re(beta)>0 and

    |beta-c|^2-c^2
      =|beta|^2-2c Re(beta)
      <(1-63/32)|beta|^2<0.                                  (8)

Every node therefore lies in the fixed disk |z-c|<c, including nodes
arbitrarily close to 0. Also sum_j |beta_j|^2 <= c A.

On |z|<=1/4, the odd binomial coefficients in (5) have total 2^(n-1),
and |z/4|<=1/16<=1. Therefore

    |P_n(z)| <= 2^(n-1),
    |a_n(z)| <= 2^(n-1)(16/15)^(n/2) <= 3^n=M.                (9)

The last inequality follows from 2 sqrt(16/15)<3. Put h(z)=a_n(z)^2;
then h(0)=n^2. The Cauchy coefficient bound on |z|=1/4, with
sup|h|<=M^2, gives, for |z|<=1/8,

    |h(z)-n^2|
      <= M^2 sum_{k>=1}(4|z|)^k
      <= 8 M^2 |z| = C |z|.                                 (10)

Here we import the standard Cauchy formulas and analytic Taylor theorem,
[NIST DLMF 1.9.30-31](https://dlmf.nist.gov/1.9.E31) and
[1.10.1](https://dlmf.nist.gov/1.10.E1), version 1.2.8, as assessed
before this attempt. All contours used here lie strictly within the
analytic domain. The explicit disks, suprema and remainder estimates
are the specialization needed for the present weighted node sum.

### One-sided regularization at the accumulation point

Define

    f_eta(z)=a_n(z)(z+eta)^(-1/2),                             (11)

using the branch positive for real z+eta>0. It is analytic on a
neighborhood of the closed disk |z-c|<=R: there
Re(z+eta)>=eta/2>0 and |z|<=2c+eta/2<=5/32<1/4.
In particular no node-specific clearance is used.

Define Q_eta=sum_j beta_j^2 f_eta(beta_j)^2. This sum is absolute:
|beta+eta|>=eta and (9) bound it in modulus by
(M^2/eta) sum_j |beta_j|^2. It is real by conjugation symmetry.
For a node z=beta, direct algebra gives

    z^2 f_eta(z)^2-z h(z)
      = -eta n^2 z/(z+eta) - eta z(h(z)-n^2)/(z+eta).          (12)

For Re z>0,

    Re(z/(z+eta))=(|z|^2+eta Re z)/|z+eta|^2>0,
    |z+eta|>=|z|.

The first term on the right of (12) has nonpositive real part.
By (10), the absolute value of its second term is at most
eta C |z|. Both separated series are absolutely convergent:
|z/(z+eta)|<=|z|/eta for the first, and the displayed mass bound
for the second. We may therefore sum real parts to get

    Q_eta-lambda_n <= eta C sum_j |beta_j|
                    <= eta C A <= epsilon/8.                 (13)

This is deliberately a one-sided estimate. The favorable n^2 term
need not tend uniformly to zero relative to |z| near z=0.
No uniform mass-tail modulus or sign of a complex algebraic square
has been assumed; the only sign used is the elementary real-part
identity above.

### Polynomial truncation and its complete-sum error

On |z-c|=R, (9) and Re(z+eta)>=eta/2 imply

    |f_eta(z)| <= M sqrt(2/eta)=B.                             (14)

Let b_k=f_eta^(k)(c)/k! and define

    q_D(z)=sum_{k=0}^D b_k (z-c)^k.                           (15)

The branches in (5) and (11) respect conjugation on this disk and
are real on its real segment. Thus every b_k, and every coefficient
of q_D in powers of z, is real. Cauchy's formula on this specified
circle gives |b_k|<=B R^(-k). Uniformly on |z-c|<=c,

    |q_D(z)-f_eta(z)| <= e_D:=B theta^(D+1)/(1-theta).          (16)

All constants in (2) are positive as asserted. Since eta<=1/16,
B>=3 sqrt(32)>1, whereas (1-theta)tau<1. Hence the logarithm
defining D is positive. The ceiling choice gives

    theta^D <= (1-theta)tau/B,
    e_D <= theta tau < tau <= 1.                              (17)

At every node, (9) and |beta+eta|>=eta give
|f_eta(beta)|<=M/sqrt(eta)<=B. The algebraic identity
u^2-v^2=(u-v)(u+v), used with absolute values only for the error,
therefore yields the full-sum estimate

    |Q(q_D)-Q_eta|
      <= sum_j |beta_j|^2 e_D(2B+e_D)
      <= c A e_D(2B+e_D)
      < c A tau(2B+1) <= epsilon/8.                          (18)

The sums defining Q(q_D) and Q_eta are absolute, and both are real.
Combining (13) and (18) proves (3). L030 identifies this negative
polynomial value with the corresponding real Hankel quadratic form.
In particular q_D is nonzero. Every node and every multiplicity was
included in the bounds; there is no discarded tail or limiting-degree
sign inference.

For an explicitly finite coefficient recipe, put p=floor((n-1)/2).
The binomial series at c gives

    b_m = (1+c/4)^(-n/2)(c+eta)^(-1/2)
          * sum_{h+k+l=m, 0<=h<=p, k,l>=0}
              [P_n^(h)(c)/h!]
              * binom(-n/2,k)/(4+c)^k
              * binom(-1/2,l)/(c+eta)^l.                      (19)

This uses the ordinary generalized binomial theorem,
[DLMF 4.6.7](https://dlmf.nist.gov/4.6.E7) and
[1.10.4](https://dlmf.nist.gov/1.10.E4). Its radii are valid because
R<c+eta and R<4+c. Formula (19) involves only the supplied inputs
and finite sums, not unknown derivatives or norms of Xi.

### Scope and comparison

Lagarias's identity is imported, not reproved. The additional work is
the actual-node rational factorization, the favorable regularization
term in (12), and a specified Taylor contour that turns it into an
explicit degree. L032 and L895 instead use a supplied finite head and
interpolation denominators; neither is a mathematical input here.
The pre-existing bounded literature assessment found no matching
D(n,epsilon,A); that search is not a claim of originality or absence
from the wider literature.

There is no proof of RH in this lemma: (1) supplies a negative Li
coefficient hypothetically. Proving actual mixed signs, obtaining
such data from height/deviation, and all-height/all-degree coverage
remain independent obligations. Numerical evaluations would not
establish (1), (7), (13), or (18); the present argument is analytic.

### Independent conceptual audit, step161

The audit checked Lagarias's zeta normalization on p.1697, the test class
and absolute convergence on p.1704, and Theorem 3.1 with its proof on
pp.1705-1706 against (4)-(7). Grouping the absolute quadratic sum into
two-element sign orbits preserves multiplicity. Conjugating these orbits
preserves the beta multiset, even when a sign orbit is fixed by
conjugation; no additional doubling is performed.

The analytic checks distinguish the node set from the larger contour.
At the nodes |beta|<1/16, so (10) applies, and (8)'s coefficient is
1-63/32=-31/32<0. The Taylor contour can cross Re(z)=0, but still has
Re(z+eta)>=eta/2 and |z|<=5/32<1/4. Thus (9) and (14), not a
positive-real-part claim for that entire contour, supply its bound.
Zeros of P_n cause no branch problem: f_eta uses a_n itself, not a
newly chosen square root of h. Both separated series in (12) are
absolute, which licenses taking their real parts before summing.

The minimum choices in (2) cover both capped and uncapped cases:
eta*C*A<=epsilon/8 and c*A*tau*(2B+1)<=epsilon/8. Since
theta<1, the ceiling gives e_D<=theta*tau<tau even if its argument
is an integer. Hence (18) is strictly less than epsilon/8, and the
total upper error is strictly less than epsilon/4. Formula (19) has
R<c+eta and R<4+c, and finite convolution gives exactly the Taylor
coefficients in (15). L030 uses indices 0 through D, so degree at
most D corresponds to H_D, with no missing index shift.

No defect or needed change to the degree bound was found. These checks
establish the stated conditional bridge within the cited informal
inputs; they do not certify originality or any actual negative sign.
The direct mathematical inputs remain L018/L024/L026/L030. L032,
C032a and L895 are comparisons only, and no finite Li-window theorem
or unverified count constant is used.

## Mathlib

Coverage of the full explicit Li-to-L030 conversion has not been checked;
availability is unknown, not asserted absent. No Mathlib theorem is
imported. General Taylor, Cauchy, binomial or finite-quadratic-form
support alone would not verify the normalization and one-sided
complete-sum comparison above.
