# Corollary 645z: polynomial cost from one rotation to the angular mean

## Hypotheses

Retain n>=5, x=-d=-5/4, R=11/8, U=R^2, eta=1/100,
t_j=j/n, and a common finite set Z of distinct poles with Re(a)=x,
|a|<=R-eta and x in Z. Their original simple-pole residues r_a are
positive integers, m=|Z|, and M=sum r_a<=n/3. The same Z and residues
serve every angle; there is no separation or symmetry assumption.
For |u|=1 put

    B_{j,u}(v)=product_(0<=k<j) R*(v-t_k*u)/(U-t_k*v/u),
    B_u=B_{n,u}, B_{0,u}=1,
    W_a(u)=B_u(x)/B_u(a),
    q_u(zeta)=sum_a r_a*W_a(u)/(R*zeta-a),
    H_u f=P_-(q_u*f).

The denominator angle is conjugated since 1/u=conjugate(u).
Use C645g's normalized circle measures, H^2, strictly negative H^2_-
and largest operator norm. Define the later coefficients from C645y:

    K=ceil(n/2), v_j=1-t_j^2/U,
    C_j(u)=B_u(x)*sum_a r_a/[B_{j,u}(a)*(a-t_j*u)],
    T(u)=sum_(K<=j<n) v_j*|C_j(u)|^2,
    A_n=(mean_u ||H_u||^2)^(1/2),
    Q_n=(mean_u ||q_u||_2^2)^(1/2),
    T_n=(mean_u T(u))^(1/2),
    D_n=1+(n-1)*(201/41+9*m).

Here T_n is an amplitude, not a squared energy. The common polynomial
P(v)=product_a(v-a)^(r_a) has degree M, with generally complex
coefficients; polynomial multiplicities still give simple poles in P'/P.

## Conclusion

Uniformly in the entire stated family,

    max_u ||H_u|| <= sqrt(D_n)*A_n <= 2*n*A_n,            (1)
    max_u ||q_u||_2 <= sqrt(D_n)*Q_n <= 2*n*Q_n,          (2)
    max_u sqrt(T(u)) <= sqrt(D_n)*T_n <= 2*n*T_n.         (3)

The reverse inequalities A_n<=max ||H_u||, Q_n<=max ||q_u||_2
and T_n<=max sqrt(T(u)) are immediate. All maxima exist. Thus passage
from a large angle to the angular root mean square costs at most 2n,
uniformly even for arbitrarily close poles and growing m. It does not
require an exponentially small arc estimated from an absolute derivative.

In particular, proving for each family that some u satisfies

    sqrt(T(u)) >= c*n*exp(-n/32)                          (4)

with one uniform c>0 and onset would suffice for the approved angular
operator lower bound. A bound c*n^p*exp(-gamma*n) for any fixed real p
and fixed gamma<1/32 would also suffice, beyond another uniform onset.
The same sufficient tests apply directly to ||q_u||_2 or ||H_u||.

No such large-angle lower bound is proved here. The common degree-M
polynomial has not yet controlled cancellation in C_j. This result is
a local quantitative reduction obtained by specialization of finite
rational Hardy-space evaluation, not a new general evaluation theorem,
an admissible countersequence, or an RH resolution. It has not received
a separate conceptual audit. Actual-Xi realization and signs remain open.

## Proof

### 1. Reused coverage and the finite evaluation calculation

The unchanged invocation-start
[angular assessment](../drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md)
covers this Fourier/residue test on the same family and threshold.
The assessed finite rational/model-space comparison and C645y's
orthogonal-basis calculation are reused. The scoped duplicate search
also checked C645p/q/u: continued evaluation at zero, angular versus
Hilbert--Schmidt energy, and spatial Hardy-kernel optimization are
different operations. None of those results is used as a lower bound
for the present later coefficients.

Import the Hardy projection convention from L. Baratchart, S. Chevillard
and T. Qian, *Minimax principle and lower bounds in H2-rational
approximation*, J. Approx. Theory 206 (2016), 17--47, preprint v2,
24 March 2015, [Section 4, (17)--(19), and Section 5.2](https://arxiv.org/pdf/1501.01161v2),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004). That finite-space
description alone does not provide the constants for our angular poles.
Import scalar Fourier orthogonality and Parseval from A. Levitt,
*Analyse de Fourier et applications*,
[author PDF](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf),
version retrieved 2 November 2026, Theorem 1.3/Exercise 1.2 and
Theorem 1.11/Corollary 1.12, printed pp.6,8. Normalized measure makes
every circle exponential have norm one. These primary inputs were
inspected in the reused assessment chain.

We spell out the finite basis specialization to include repeated zeros
at zero, the polynomial part at infinity, and both sides of the angular
circle. This checks the actual rational class and constants; it is not
a claim to reprove or improve Nehari/AAK or a general evaluation theorem.

Let beta_1,...,beta_N lie strictly in the disk, allowing repetitions.
Consider rational functions with denominator
prod_l(1-conjugate(beta_l)*u) and numerator degree <=N-1.
Their normalized orthonormal basis is

    e_l(u)=sqrt(1-|beta_l|^2)/(1-conjugate(beta_l)*u)
               *product_(h<l) (u-beta_h)/(1-conjugate(beta_h)*u). (5)

For clarity, the geometric Fourier series gives
<f,(1-conjugate(beta)*u)^(-1)>=f(beta), with inner product linear
in the first variable. Each normalized kernel has norm one, and
multiplication by an inner factor preserves circle norm. For l<k,
cancel their common inner prefix in the inner product; the remaining
analytic function from e_k vanishes at beta_l. The reproducing identity
makes the inner product zero, even when beta_k=beta_l. Each e_l lies
in the displayed N-dimensional rational space, so they are a basis.
This is C645y's finite calculation with repeated zeros permitted.

At |u|=1 all inner factors in (5) have modulus one. Finite
Cauchy--Schwarz and Parseval therefore give

    |f(u)|^2 <= k_beta(u)*||f||_2^2,
    k_beta(u)=sum_l (1-|beta_l|^2)/|1-conjugate(beta_l)*u|^2
              <=sum_l (1+|beta_l|)/(1-|beta_l|).         (6)

For a rational function with simple interior poles p_h and no other
interior singularities, its interior principal parts form a strictly
negative Fourier function f_-. The map

    J f_-(u)=conjugate(u*f_-(u)),  |u|=1,

preserves its norm and pointwise modulus. It takes 1/(u-p_h) to
1/(1-conjugate(p_h)*u), hence maps this space into the rational space
in (5) with zeros p_h. The remaining part f_+ is analytic in the disk.
These two spaces are orthogonal. Combining their orthonormal bases
gives an evaluation bound whose constant is the sum of their two
constants in (6), not their product.

The same bound holds for functions taking values in any complex Hilbert
space and having this finite angular expansion. Indeed write
F(u)=sum_l phi_l(u) h_l in the combined orthonormal scalar basis.
Then ||F(u)||^2 <= (sum_l |phi_l(u)|^2)(sum_l ||h_l||^2),
while finite orthogonality gives mean ||F||^2=sum_l ||h_l||^2.
Only finite sums are involved. This does not regard an operator norm
as a Hilbert-space norm.

### 2. Full symbol: all angular poles and the constant at infinity

Algebra, retaining 1/u in the original denominator, gives

    W_a(u)=(x/a)*product_(k=1)^(n-1)
                 [(x-t_k*u)/(a-t_k*u)]
                 *[(U*u-t_k*a)/(U*u-t_k*x)].             (7)

This rational continuation has possible interior poles
p_k=t_k*x/U, 1<=k<n, and possible exterior poles a/t_k.
They are all simple before cancellations. Exterior poles are distinct:
equality a/t_k=a'/t_h forces x/t_k=x/t_h by taking real parts,
then k=h and a=a'. Interior poles are distinct and separate from
the exterior ones. Adding over a does not increase the common
interior pole multiplicities. Cancellations, including W_x=1, only
reduce the space. There is no pole at u=0. At infinity every factor
ratio in (7) tends to one, so W_a tends to x/a: the polynomial part
has degree at most zero.

The angular interior pole moduli and reflected exterior pole moduli
obey, respectively,

    |p_k|<d/U=80/121,
    |1/conjugate(a/t_k)|=t_k/|a|<1/d=4/5.               (8)

After subtracting all interior principal parts, the analytic rational
part has at most m(n-1) simple exterior poles and a constant polynomial
part. It belongs to (5) with those reflected exterior poles and one
additional zero beta=0. The latter zero includes the constant part:
the common numerator has degree at most m(n-1), and the space has
dimension m(n-1)+1. The negative part has at most n-1 poles p_k.
Since

    (1+80/121)/(1-80/121)=201/41,
    (1+4/5)/(1-4/5)=9,

the combined evaluation bound is exactly at most D_n.

For every fixed polynomial f(zeta), the finite projection identity gives

    H_u f=sum_a r_a*W_a(u)*f(a/R)/(R*zeta-a).             (9)

To check it, subtract f(a/R) from f(zeta) in each term; the quotient
has a removable singularity and is analytic. The remaining simple
pole has only negative spatial Fourier modes. Thus (9) is a Hilbert-
valued angular function in precisely the finite rational class above,
with values in H^2_-. Applying (6) at any angle u_0 yields

    ||H_(u_0) f||_2^2 <= D_n*mean_u ||H_u f||_2^2
                         <= D_n*A_n^2*||f||_2^2.        (10)

Each H_u is bounded since q_u is a bounded circle symbol. Taking the
supremum over unit polynomials, which are dense in H^2, proves (1)
with sqrt(D_n). Taking f=1 in the first inequality of (10) proves (2).
The angular weights are continuous, with denominators nonzero on the
circle. Finite-rank representation (9), or the finite sum of bounded
evaluation operators, implies operator-norm continuity in u. All
maxima in (1)--(2) therefore exist. No interchange of an angular
integral with an optimizing angle-dependent input has been made.

### 3. Later grid coefficients: the polynomial part must be retained

For 1<=j<n and each pole a, the contribution to C_j is

    r_a*(x/a)*R^(n-j)*u^(n-j)
       *product_(k=1)^(n-1)(x-t_k*u)
       *product_(k=1)^(j-1)(U*u-t_k*a)
       /[product_(k=1)^(n-1)(U*u-t_k*x)
          *product_(k=1)^j(a-t_k*u)].                    (11)

The factor t_0=0 was separated in deriving this expression. In
particular it creates no missing zero pole in the angular variable.
The numerator degree is 2n-2; the denominator degree is n+j-1.
All denominator leading coefficients are nonzero. Thus each summand,
and their sum, has polynomial part of degree at most n-j-1.
Its possible interior poles are the same n-1 points p_k; its possible
exterior poles are a/t_k with 1<=k<=j, at most m*j distinct points.

After subtracting the interior principal parts, use (5) with the m*j
reflected exterior poles and n-j repeated zeros at zero. This includes
the entire polynomial part: its common numerator degree is at most
m*j+n-j-1. Equations (6) and (8) now give

    |C_j(u_0)|^2 <= D_(n,j)*mean_u |C_j(u)|^2,
    D_(n,j)=(201/41)(n-1)+9*m*j+n-j <= D_n.             (12)

The last inequality follows because the coefficient of j is 9m-1>0
and its maximum occurs at j=n-1. Multiply by v_j>0 and sum for
K<=j<n to obtain (3). C645y's exact orthogonal grid identity supplies

    ||q_u||_2^2 >= T(u).                                (13)

This is the only energy-decomposition input required here; the present
point-evaluation calculation does not certify the other claims or
audits in C645y. Continuity also gives the maximum in (3).

### 4. Explicit loss, threshold and limitations

The census implies m<=n/3. Since 201/41<5,

    D_n < 1+(n-1)*(5+3n)=3n^2+2n-4 < 4n^2,

where 4n^2-(3n^2+2n-4)=(n-1)^2+3>0. This proves the
displayed 2n bounds without a numerical or asymptotic estimate.
Combining (3), (13) and A_n>=Q_n gives the sufficient condition (4).
With a strict rate gamma<1/32, the remaining factor
n^(p-1)*exp((1/32-gamma)*n) tends to infinity, so a uniform constant
and onset follow if the pointwise hypothesis has uniform constants.

The proof of the evaluation bound itself uses only the number and
location of poles, not their positive integer residues. Those stronger
hypotheses remain essential candidates for the still-unproved
large-angle estimate. This result does not evade C645x's fractional
dual obstruction or the C645t/y prefix obstruction. It neither changes
the common-pole family nor permits a different pole set at each angle.
Finite exact directional values could now give certified lower bounds
for their individual angular means, but cannot establish uniformity
over unbounded n or over arbitrary families.

All algebra and constants above are exact. No quadrature, floating-point
screen, asymptotic certificate or mathematical script was needed for
this step. The saved working note records the still-missing common-P
lower estimate rather than treating the reduction as its solution.

## Mathlib

Full matching coverage for these angular pole counts and the explicit
2n comparison has not been checked; no absence claim is made. Supporting
ingredients are normalized Fourier orthogonality, geometric Hardy
kernels, finite orthonormal bases and rational partial fractions.
Neither the uniform large-angle lower bound nor actual-Xi realization
is assumed to be present in Mathlib.
