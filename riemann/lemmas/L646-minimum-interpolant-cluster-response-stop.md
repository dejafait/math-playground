# Lemma 646: the minimum exact-recovery input still loses the angular rate

## Hypotheses

Retain the approved family: n>=5, x=-d=-5/4, R=11/8, eta=1/100,
t_k=k/n, and a common finite set Z of distinct poles with Re(a)=x,
|a|<=R-eta and x in Z. The original simple-pole residues r_a are
positive integers, with M=sum r_a<=n/3. For |u|=1 set

    B_u(v)=product_(k<n) R*(v-t_k*u)/(R^2-t_k*v/u),
    b_u(zeta)=B_u(R*zeta),
    q_u(zeta)=sum_a r_a*B_u(x)/[B_u(a)*(R*zeta-a)],
    L(z)=sum_a r_a/(z-a).

Use C645g's normalized circle measure, H^2, strictly negative H^2_-,
and largest Hankel norm H_u f=P_-(q_u*f). The same poles and residues
serve every u. No separation or ordinate symmetry is assumed. Put

    b_alpha(zeta)=(zeta-alpha)/(1-conjugate(alpha)*zeta),
    C(zeta)=product_(a in Z) b_(a/R)(zeta),
    K_C=H^2 orthogonal to C*H^2,
    E_u=P_(K_C) b_u,
    J_u=|B_u(x)|*||L(R*zeta)||_2/||E_u||_2.              (1)

The product C counts distinct poles, not residue multiplicities. The
common polynomial product_a(z-a)^(r_a) still has degree M; no condition
on its coefficients is imposed. E_u is nonzero because E_u(x/R)=B_u(x).

## Conclusion

E_u is the minimum-H^2-norm function satisfying f(a/R)=B_u(a) at
every pole. Its complete Hankel output is

    H_u E_u=B_u(x)*L(R*zeta),
    ||H_u||>=J_u.                                       (2)

Thus J_u is the best normalized response among all inputs with these
exact interpolation values. Allowing a common nonzero scalar multiple
of the values gives the same normalized optimum.

Nevertheless this input does not prove the approved angular threshold.
For every n>=5 let

    m=floor(n/3), epsilon_n=exp(-n^2),
    a_j=x+i*j*epsilon_n, 0<=j<m, r_(a_j)=1,
    N=(50400000)^2,
    lambda=log(11/10)+(201/80)*log(201/121)-(9/4)*log(9/5).

These are admissible distinct-pole families. For all n>=N and all |u|=1,

    ||E_u||_2>=1/63000,
    J_u<=63000*n*exp(-lambda*n),
    lambda>47/1000>1/32.                                 (3)

Consequently exp(n/32)*max_u J_u tends to zero, as does the same
scaled angular root mean square. Angle selection and optimal
interpolation normalization cannot repair this particular input.

This is not an operator countersequence. On the very same family,
for every n>=5 and every u,

    ||q_u||_2>=m, hence ||H_u||>=m.                       (4)

The result is a local obstruction to an exact-recovery input, obtained
by a finite Hardy-space/Fourier specialization. It does not stop the
full common-polynomial or later-grid mechanisms, settle the arbitrary
family detector, or supply an Xi realization or sign theorem. The new
argument passed a separate conceptual audit on 2 November 2026,
recorded in Proof Section 8. No originality or RH resolution is claimed.

## Proof

### 1. Coverage, exact recovery, and the interpolation minimizer

Reuse the unchanged invocation-start
[angular EXPLORE assessment](../drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md),
including its finite rational/model-space comparison and scalar
Fourier scope. The scoped duplicate search checked the C645 angular
lemmas and the common-polynomial, projection and fractional-lattice
failure records. C645n stops the unnormalized full inner input; the
question here is whether the minimum-norm input with the same values
repairs that loss. C645y/z motivate retaining the full response, but
are not mathematical premises for the estimates below. Their later
grid sum is not bounded above here.

Import the Hardy projection convention from L. Baratchart,
S. Chevillard and T. Qian, *Minimax principle and lower bounds in
H2-rational approximation*, J. Approx. Theory 206 (2016), 17--47,
[arXiv:1501.01161v2](https://arxiv.org/pdf/1501.01161v2), 24 March 2015,
Section 4, (17)--(19), and the Section 5.2 finite-space comparison;
[DOI](https://doi.org/10.1016/j.jat.2015.03.004). Import scalar Fourier
orthogonality and Parseval from A. Levitt, *Analyse de Fourier et
applications*, [author PDF](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf),
version retrieved 2 November 2026, Theorem 1.3/Exercise 1.2 and
Theorem 1.11/Corollary 1.12, printed pp.6,8. These inspected sources are
reused; no Nehari, AAK or general interpolation theorem is reproved.
The elementary projection, change of variables and one integration by
parts below check the constants and the actual confluent limit needed
for this family. No general stationary-phase theorem is invoked.

Multiplication by a finite Blaschke product is an isometry of H^2,
so the projection onto K_C is

    P_(K_C) f=f-C*P_+(conjugate(C)*f).                    (5)

The functions in C*H^2 are exactly the H^2 functions vanishing at the
distinct zeros of C. Indeed division by one b_alpha cancels the zero
and preserves boundary norm. Membership in H^2 follows from the identity
(f(z)-f(alpha))/(z-alpha)=sum_(j>=0) alpha^j*(S^*)^(j+1)f, converging
in H^2 with norm at most ||f||/(1-|alpha|); S^* removes the constant
coefficient and shifts the others down. Multiply this quotient by
1-conjugate(alpha)*z. Iteration proves the assertion. Therefore E_u has the
specified values, and any other interpolant is E_u+C*h. Orthogonality
gives norm squared ||E_u||^2+||h||^2, proving minimality.

For each pole alpha=a/R, subtraction of f(alpha) gives

    P_-[f(zeta)/(zeta-alpha)]=f(alpha)/(zeta-alpha).

For rational f analytic near the closed disk this follows directly
from the removable singularity. For general H^2 inputs it follows
by polynomial approximation, bounded point evaluation and boundedness
of the fixed rational-symbol Hankel operator. Applying it at the
interpolation values proves (2), with the physical factor 1/R retained.
Conversely, uniqueness of partial fractions at distinct poles and
r_a*B_u(x)/B_u(a) nonzero shows that this output requires exactly those
values. Thus no input with the same complete recovered output is omitted
by the minimization.

### 2. The confluent model and the direction of the unitary map

First replace C by C_0=b_alpha^m, where alpha=x/R=-10/11 is real,
m=floor(n/3), and keep b_u unchanged. This is an auxiliary interpolation
space with repeated zeros; it is not an assertion that the approved
logarithmic derivative has a higher-order pole. Write

    phi(w)=(w+alpha)/(1+alpha*w),
    kappa(w)=sqrt(1-alpha^2)/(1+alpha*w),
    (U_alpha f)(w)=kappa(w)*f(phi(w)),
    F_u=U_alpha b_u.

On the unit circle |kappa|^2 is the derivative of the angular change
of variables induced by phi. That change is an orientation-preserving
bijection, so U_alpha is unitary on H^2, with inverse obtained from
the inverse disk map. Also b_alpha(phi(w))=w. It follows that U_alpha
maps C_0*H^2 onto w^m*H^2 and hence

    ||P_(K_(C_0)) b_u||_2=||P_(0<=k<m) F_u||_2,
    ||F_u||_2=1,  |F_u(e^(i*s))|^2=|kappa(e^(i*s))|^2.  (6)

This orientation is essential: the transformed object includes the
factor kappa, not just composition by phi.

Put beta_k=t_k*u/R and A=10/11=-alpha. Composition of each inner
factor with phi has, up to a unimodular constant, the zero

    gamma_k=(beta_k+A)/(1+A*beta_k).

Every gamma_k is in the disk and has positive real part. For r=|beta_k|
<=8/11<A, the real numerator after multiplying by 1+A*conjugate(beta_k)
is at least

    A*(1+r^2)-(1+A^2)*r=(A-r)*(1-A*r)>0.

On the arc I={s: |s-pi|<=h}, h=1/100, write the product of these
inner factors as exp(i*S_u(s)), choosing any continuous local phase.
The derivative of one factor's phase is its Poisson kernel

    P_gamma(e^(i*s))=(1-|gamma|^2)/|e^(i*s)-gamma|^2.

At w=-1 the angular derivative of phi is 1/21. The chain rule gives

    P_(gamma_k)(-1)=P_(beta_k)(-1)/21
       <=(1/21)*(1+8/11)/(1-8/11)=19/63.

Since Re(gamma_k)>0, |-1-gamma_k|>=1. Also |e^(i*s)+1|<=h on I.
Consequently

    0<=S_u'(s)<=n*(19/63)*(100/99)^2 < (5/16)*n,
    |S_u''(s)|<=2*n/(1-h)^4 <3*n.                       (7)

For the first inequality, compare the two Poisson denominators;
their ratio is at most (1-h)^(-2). For the second, differentiate the
kernel: the derivative of its squared denominator has magnitude at
most 2|gamma_k|, while that denominator has magnitude at least
(1-h)^2. These bounds are uniform in n, k and u. The strict rational
comparison in (7) is 3040000<3087315.

### 3. A fixed arc forces a nonzero low-frequency mass

Define the real nonnegative C^1 cutoff

    psi(s)=(1-((s-pi)/h)^2)^2 on I, and zero outside I,
    g_u(e^(i*s))=psi(s)*F_u(e^(i*s)).

It is understood periodically; I does not meet the integration endpoints.
We have ||g_u||_2<=1. Throughout the circle |kappa|^2>=1/21. Since
integral psi(s) ds=16h/15, normalized measure gives

    <F_u,g_u>=mean_s psi(s)*|kappa(e^(i*s))|^2
       >=8/(31500*pi)>1/15750=:c_0.                     (8)

Here the inner product is linear in its first variable, and pi<4
suffices for the last comparison. This positive overlap is independent
of the grid rotation.

To control high frequencies, put a(s)=psi(s)*kappa(e^(i*s)), so that
g_u=a*exp(i*S_u). The harmless unimodular constant in the latter
product can be included in S_u. Direct differentiation gives

    |kappa|<=sqrt(21)<5, |d kappa/ds|<=10*sqrt(21)<50,
    integral |psi'| ds=2,
    integral |a'| ds<11, integral |a| ds<1/10.           (9)

For an integer k>=m let Delta_k=k-5*n/16. If n>=96, then
Delta_m>=n/48-1>=n/96>=1. The phase S_u(s)-k*s has derivative
of magnitude at least Delta_k on I. One integration by parts, with
zero endpoint term because a vanishes there, and (7)--(9) imply

    |(g_u)_k|
      <=(1/(2*pi))*(11/Delta_k+(3*n/10)/Delta_k^2)
      <=11/Delta_k+n/Delta_k^2.                         (10)

For clarity, the differentiated amplitude is
a'/(i*(S_u'-k))-a*S_u''/(i*(S_u'-k)^2). Thus no bound on a
global phase or an interchange with an asymptotic expansion is used.

For any Delta>=1, monotone integral comparison gives

    sum_(j>=0) (Delta+j)^(-2)<=2/Delta,
    sum_(j>=0) (Delta+j)^(-4)<=4/(3*Delta^3).

Squaring (10) with (p+q)^2<=2p^2+2q^2 and summing yields

    ||P_(k>=m) g_u||_2^2
       <=[242*192+(8/3)*96^3]/n
       =2405760/n <1600^2/n.                            (11)

Only scalar Fourier coefficients and Parseval are used. F_u has no
negative modes. Splitting the inner product in (8) at m and applying
Cauchy--Schwarz, with ||F_u||=1 and ||g_u||<=1, gives

    ||P_(0<=k<m) F_u||_2>=c_0-1600/sqrt(n).

For n>=N=(3200*15750)^2=(50400000)^2 this is at least 1/31500.
By (6), this proves a uniform lower bound for the confluent projection.
The very large onset is an explicit sufficient value, not an optimized
constant and not an effective RH height assertion.

### 4. Distinct admissible poles and a uniform projection perturbation

Return to a_j=x+i*j*epsilon_n, 0<=j<m, with residues one. The elementary
series bound exp(n^2)>=n^4/2 gives

    |a_j-x|<=n*exp(-n^2)<=2/n^3<=2/125<1/16,
    |a_j|<=21/16<R-eta=273/200,
    |a_j/R|<=21/22.                                    (12)

These poles are distinct, lie on the required line, include x, and avoid
every rotated grid because |a_j|>=d>1. Their total residue is m<=n/3.

For |zeta|=1, |beta|<=21/22 and alpha=-10/11, subtraction of the
two Blaschke fractions gives

    |b_beta(zeta)-b_alpha(zeta)|<=1000*|beta-alpha|.

Indeed their denominator product is at least (1/22)*(1/11)=1/242,
and the combined numerator is at most 4|beta-alpha|. Telescoping
products of unit-modulus boundary factors now gives

    ||C-C_0||_infinity<=1000*n^2*exp(-n^2).              (13)

Formula (5), the L2 contraction of P_+, and ||b_u||=1 imply

    ||P_(K_C)b_u-P_(K_(C_0))b_u||_2
       <=2*||C-C_0||_infinity
       <=2000*n^2*exp(-n^2).                            (14)

This argument avoids an ill-conditioned limiting inverse Gram matrix
and is uniform in u. The bound exp(n^2)>=n^6/6 makes the last term
at most 12000/n^4, which is <=1/63000 for n>=200. Combining (14) with
the preceding lower bound at n>=N proves ||E_u||>=1/63000.

### 5. The actual and required exponents

On this family, each physical resolvent has norm

    ||1/(R*zeta-a_j)||_2=1/sqrt(R^2-|a_j|^2)
       <=16/sqrt(43)<3.

Hence ||L(R*zeta)||<=3m<=n. C645n's pointwise maximum calculation,
Proof Section 2, (6)--(8), gives |B_u(x)|<=exp(-lambda*n) for every
rotation, with lambda>47/1000 from its exact logarithm bounds.
Inserting these facts in (1) proves (3). In particular

    exp(n/32)*max_u J_u
       <=63000*n*exp(-(lambda-1/32)*n) ->0,
    lambda-1/32>63/4000.

The same upper bound applies to the angular root mean square of J_u.
It is an upper bound on the best response within the exact-recovery
input class, never an upper bound on ||H_u||.

### 6. The full constant-input response stays large

We verify (4) to distinguish this method obstruction from a counterexample
to the angular target. On each segment from x to a_j, |z|<=21/16 and
|z|>=d. The logarithmic derivative of a grid factor satisfies

    |1/(z-t_k*u)+(t_k/u)/(R^2-t_k*z/u)|
       <=4+64/37<6.

No factor vanishes on these segments. Integrating its logarithmic
derivative along the segment therefore shows, for W_j=B_u(x)/B_u(a_j),

    W_j=exp(v_j), |v_j|<=6*n^2*exp(-n^2)=:delta_n<1/2,
    |W_j-1|<=2*delta_n<=12*n^2*exp(-n^2).               (15)

The estimate delta_n<1/2 follows already from
exp(n^2)>=n^8/24 for n>=5. The exponential estimate for |v|<=1/2
follows from its absolutely convergent power series.

On |zeta|=1, the two resolvent denominators have moduli at least
1/16 and 1/8. Subtracting them and using (15) yields

    |W_j/(R*zeta-a_j)-1/(R*zeta-x)|
       <=192*n^2*exp(-n^2)+128*n*exp(-n^2)
       <=220*n^2*exp(-n^2).

Sum over j and use the triangle inequality in L2. Since
||1/(R*zeta-x)||_2=8/sqrt(21), we obtain

    ||q_u||_2>=m*(8/sqrt(21)-220*n^2*exp(-n^2))>m.

For the last strict inequality, exp(n^2)>=n^10/120 gives
220*n^2*exp(-n^2)<=26400/n^8<=26400/390625<1/2,
while 8/sqrt(21)>3/2. Finally H_u 1=q_u and ||1||=1. This proves
(4) uniformly over the entire angular circle. All poles remain simple;
the confluent model was used only to estimate interpolation norms.

### 7. Verification and scope of the stop

The reproducible exact-arithmetic check is
`python3 scripts/one-sided-hankel/minimum-interpolant-cluster-check.py`.
It writes its full rational comparisons and their margins to
`scripts/one-sided-hankel/minimum-interpolant-cluster-check.json`.
It checks the explicit constants in (7)--(15), the onset arithmetic,
admissibility margins, and the final resolvent error comparisons.
The uniform Fourier argument and projection continuity are proved
above; finite arithmetic checks do not independently certify them.

The test optimized here imposes all exact pole values before choosing
an input. Near a cluster those conditions encode derivative information
and keep the minimum norm large. The actual positive-residue symbol
needs none of those interpolation conditions and is large by (4).
Therefore a continuation must use the actual full response or later
grid coefficients, or explicitly exploit clustering without imposing
exact recovery at every node. The arbitrary-family lower bound and
all Xi bridges remain unresolved. The original derivation was an
author-checked local specialization; the separate audit below covers
this lemma and only its needed pointwise rate input from C645n.

### 8. Separate conceptual audit, 2 November 2026

This audit checked the complete proof, not only the rational certificate.
No mathematical correction to (1)--(15), the family, or the onset was
needed. The following are the load-bearing logical checks; they do not
extend the result to the full angular operator or all of C645n.

**Exact-output class and normalization.** For every H^2 input the
negative-part identity in Section 1 holds by bounded polynomial
approximation. Equality of its output with B_u(x)*L(R*zeta) forces
equality of every simple-pole coefficient: a rational function with
distinct poles and zero boundary values has all coefficients zero.
The coefficients B_u(x)*r_a/B_u(a) are nonzero. Thus the exact-output
constraint really is f(a/R)=B_u(a), including all close nodes. The
vanishing subspace is C*H^2, so orthogonal projection minimizes over
the entire input class, not merely polynomials or a chosen basis.
The physical denominator R*zeta-a retains the necessary 1/R.

**Unitary and auxiliary multiplicity.** The inverse coordinate map is
chi(z)=(z-alpha)/(1-alpha*z). The inverse operator is

    (V_alpha g)(z)=sqrt(1-alpha^2)/(1-alpha*z)*g(chi(z)).

Indeed 1+alpha*chi(z)=(1-alpha^2)/(1-alpha*z), so the two weights
cancel. For polynomials the boundary change of variables gives the
isometry directly; density gives its H^2 extension and the displayed
inverse. Moreover U_alpha(b_alpha^m*h)=w^m*U_alpha(h).
This verifies both surjectivity and the direction of the projection
identity (6). Repeated nodes enter only C_0; the final q_u always has
distinct simple poles. Omitting kappa would invalidate the argument.

**Phase and Fourier cutoff.** The real numerator for gamma_k is
A*(1+|beta_k|^2)+(1+A^2)*Re(beta_k), bounded below by
(A-|beta_k|)*(1-A*|beta_k|)>0. The map phi fixes -1 and has angular
derivative 1/21 there. On I, the reverse triangle inequality gives
|e^(i*s)-gamma_k|>=|1+gamma_k|-h and |1+gamma_k|>=1.
This proves the relative denominator comparison in (7), uniformly
over every rotation. The phase S_u is only needed on I, where a
continuous smooth lift exists; no joint branch in u is required.
Its derivative excludes the phase of kappa, which is instead retained
in a(s). The estimates on both a and a' therefore apply to the actual
F_u, not an unweighted substitute.

For k>=m and n>=96, Delta_k>=n/96+(k-m)>0. Differentiation of
a/[i*(S_u'-k)] gives exactly the two terms displayed after (10).
The cutoff vanishes at both arc endpoints, so no boundary term remains.
The squared-tail sum is bounded by 2405760/n<1600^2/n, with normalized
Fourier measure throughout. Although g_u has negative modes, F_u has
none. Consequently the exact orthogonal splitting is

    <F_u,g_u>=<P_(0<=k<m)F_u,P_(0<=k<m)g_u>
                  +<P_(k>=m)F_u,P_(k>=m)g_u>.

There is no discarded nonzero negative-mode contribution. Combining
this identity with the positive overlap (8) proves the stated low-mode
norm lower bound and its explicit onset. No uniform-in-n limit or
operator-valued Parseval identity is assumed.

**Transfer to distinct poles.** The bounds |a_j|<=21/16 and
|a_j/R|<=21/22 retain the original clearance and grid avoidance.
Subtracting the two Blaschke fractions gives constant 968<=1000;
telescoping their boundary products needs no pole separation. More
explicitly, the difference in (5) is the sum

    (C_0-C)*P_+(conjugate(C)*b_u)
           +C_0*P_+((conjugate(C_0)-conjugate(C))*b_u).

Its norm is at most 2*||C-C_0||_infinity because both multiplication
by an inner function and P_+ have norm at most one on the relevant
L2 spaces. This avoids any conditioning assumption about interpolation
matrices. Since ||b_u||=1 for every u, the resulting perturbation is
uniform over the whole angular circle, not merely pointwise convergence
as the poles coalesce.

**Imported exponent and full response.** The audit checked C645n
Section 2's common maximizing direction, decreasing left Riemann sum,
and exact integral for lambda, as well as Section 4's logarithm series
and remainder. They give the pointwise |B_u(x)|<=exp(-lambda*n) and
lambda>47/1000 used here. No lower angular estimate from C645n is
needed. The three complete rational logarithm enclosures and all seven
checks in its certificate were replayed and inspected. The 31 checks
for this lemma also passed, and their complete /checks field was read.
These arithmetic replays support, rather than replace, the preceding
analytic checks; no scripts or numerical screens were added.

On each segment from x to a_j the logarithmic derivative is holomorphic
and bounded by 6n. Integrating along that segment defines v_j without
requiring a global logarithm or angular branch. The resulting
|W_j-1|<=12*n^2*exp(-n^2), the two physical denominator lower bounds
1/16 and 1/8, and 8/sqrt(21)>3/2 give (4) with the stated strict
margin for every n>=5. Thus the same family demonstrably has a large
constant-input response. The inequality ||H_u||>=J_u is never reversed.

**Decision and limits.** Accept this uniform exact-recovery method
obstruction, with N=2540160000000000 and rate gap >63/4000. This is
independent verification of a local specialization, not a new theorem
beyond the checked sources. The arbitrary-family angular detector,
other input classes, the later-grid mechanism and actual-Xi realization
remain open. C645y's and C645z's separate proofs were not audited here.

## Mathlib

Full matching coverage for this cluster obstruction and its uniform
Fourier estimate has not been checked; no absence claim is made.
Supporting ingredients are orthogonal projection, finite Blaschke
products, a unitary disk change of variables, scalar Fourier Parseval,
one integration by parts and elementary rational inequalities. No
matching Mathlib theorem or actual-Xi realization is assumed.
