# Corollary 645y: retained-grid energy and the initial-prefix obstruction

## Hypotheses

Retain n>=5, x=-d=-5/4, R=11/8, U=R^2, eta=1/100,
t_j=j/n, and a common finite set Z of distinct poles with Re(a)=x,
|a|<=R-eta and x in Z. The original simple-pole residues r_a are
positive integers, with M=sum r_a<=n/3. They do not depend on the angle.
There is no separation, ordinate symmetry or coefficient-integrality
assumption. Put

    P(z)=product_a (z-a)^(r_a),    L(z)=P'(z)/P(z)=sum_a r_a/(z-a),
    b_j=t_j*u,    |u|=1,
    B_{K},u(z)=product_(0<=j<K) R*(z-b_j)/(U-conjugate(b_j)*z),
    B_u=B_{n},u,    B_{0},u=1,
    Q^{K}_u(z)=B_u(x)*sum_a r_a/[B_{K},u(a)*(z-a)],
    q^{K}_u(zeta)=Q^{K}_u(R*zeta).

Thus q^{n}_u is the approved symbol, and q^{0}_u=B_u(x)*L(R*zeta).
The denominator retains the conjugated rotation. Use C645g's normalized
circle measure, H^2, strictly negative H^2_-, and H_q f=P_-(q*f).
Operator norms always mean largest norms. Define

    R_j(u)=sum_a r_a/[B_{j},u(a)*(a-b_j)],
    v_j=1-t_j^2/U>0,    E_n=(mean_u |B_u(x)|^2)^(1/2),
    lambda=log(11/10)+(201/80)*log(201/121)-(9/4)*log(9/5).

Every zero of P with multiplicity r_a still gives a simple pole of L.
The degree of P is M; its generally complex coefficients need not be
integers.

## Conclusion

There is an exact, nonnegative energy decomposition for every angle
and every integer 0<=K<=n:

    ||q^{K}_u||_2^2
      = |B_u(x)|^2 * [ ||L(R*zeta)||_2^2
                         + sum_(0<=j<K) v_j*|R_j(u)|^2 ].       (1)

All grid residues are retained at K=n. There is no cancellation
between the displayed squares, but the sums inside R_j are complex
and need not have a positive real part. Moreover q^{K}_u is the full
response of H_{q^{n}_u} to the unit inner input

    f^{K}_u(zeta)=product_(K<=j<n)
                    (zeta-b_j/R)/(1-conjugate(b_j)*zeta/R).   (2)

For the full grid let ell_j(u)=L(b_j) and

    C_(jk)=1/(1-t_j*t_k/U),   0<=j,k<n.

The matrix C is positive definite and independent of u. The retained
grid energy also equals

    |B_u(x)|^2*sum_(j<n) v_j*|R_j(u)|^2
       = |B_u(x)|^2 * ell(u)^* C^(-1) ell(u).                (3)

This inverse Gram factor cannot be replaced by a polynomial-size
multiple of the raw sample norm in a successful lower-bound test:
with c_0=10000/223729 and

    D_n^2=mean_u |B_u(x)|^2*sum_(j<n)|ell_j(u)|^2,

one has

    c_0*M*sqrt(n)*E_n <= D_n <=4*M*sqrt(n)*E_n.             (4)

C645n gives E_n<=exp(-lambda*n), lambda>47/1000>1/32.
Consequently n^A D_n=o(exp(-n/32)), uniformly over these families,
for every fixed real A. This limits raw sample-size certificates;
it does not upper-bound (3), the full symbol, or the operator norm.

There is also an actual admissible obstruction to keeping only an
initial grid prefix. For the C645t family

    m>=5 odd, n=3m, r=27/50,
    a_k=x+i*r*cos((2k-1)*pi/(2m)), 1<=k<=m, r_(a_k)=1,

put K_*=ceil(n/2). Uniformly in u and in every 0<=K<=K_*,

    ||q^{K}_u||_2 <=22000*m*exp(-7*n/200).                 (5)

This includes K=M=m and permits angle-dependent choices among these
prefixes. After multiplication by exp(n/32), the bound tends to zero.
Thus a degree-M argument using only the first M retained-grid
coefficients cannot establish the target. The same restriction holds
through the entire first K_* coefficients. No upper bound on the
remaining coefficients or on q^{n} follows.

This is a local specialization and method restriction, not a solution
of the angular target or progress beyond the checked literature. The
full-grid degree constraint is still unexploited. The corollary has not
received a separate conceptual audit; no RH candidate is proposed.

## Proof

### Source scope and purpose

The unchanged invocation-start
[angular EXPLORE assessment](../drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md)
covers the same family, threshold and Fourier/residue calculation.
Reuse its source comparisons and C645g's normalization. C645n supplies
the finite analytic-input projection identity and the evaluated
anchor-product rate; C645t supplies its audited counterfamily bound.
C645o's negative cross entry and C645x's fractional dual stop are
contrasts, not premises for the identities here. The scoped duplicate
search found the earlier scalar/Gram/prefix-response calculations,
but not the full retained-grid decomposition below; no originality
claim follows.

Import the projection convention from L. Baratchart, S. Chevillard
and T. Qian, *Minimax principle and lower bounds in H2-rational
approximation*, J. Approx. Theory 206 (2016), 17--47, preprint v2,
24 March 2015, [Section 4, (17)--(19)](https://arxiv.org/pdf/1501.01161v2),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004). Import scalar Fourier
orthogonality/Parseval from A. Levitt, *Analyse de Fourier et
applications*, [author PDF](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf),
version retrieved 2 November 2026, Theorem 1.3/Exercise 1.2 and
Theorem 1.11/Corollary 1.12, printed pp.6,8 (PDF pp.12,14).
The normalized exponentials have norm one.

Import the residue theorem and simple-pole rule from R. W. Howell
and J. H. Mathews, *Complex Analysis*, online edition, front matter
updated 22 August 2025,
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html).
These primary inputs were inspected in the reused assessment chain.
No Nehari, Parseval or residue theorem is reproved. The finite rational
basis calculation is included to verify the exact constants, ordering
of prefixes and correspondence with C645t; an unevaluated general
model-space assertion would not provide those identifications.

### 1. Complete residue decomposition, including the zero grid point

All grid points have modulus less than one, whereas every a has
|a|>=d>1. The factors' denominators are nonzero in |z|<=R, since
U-|b_j|R>0. The grid zeros are distinct and simple. For K>=1 put

    T^{K}_u(z)=B_u(x)*L(z)/B_{K},u(z),
    s^{K}_j(u)=B_u(x)*L(b_j)/B'_{K},u(b_j),   0<=j<K,
    G^{K}_u(z)=sum_(j<K) s^{K}_j(u)/(z-b_j).                (6)

At a, the residue of T is r_a B_u(x)/B_{K},u(a). At b_j it
is s^{K}_j, including j=0. Polynomial multiplicities in P do not
alter either simple-pole rule. There are no other finite poles:
the exterior poles of B_{K} are zeros of its reciprocal.

Because the factor at zero is z/R and every other grid factor
approaches a nonzero constant at infinity, B_{K}(z) grows linearly
there. Also L(z)=M/z+O(z^(-2)). Thus T^{K}(z)=O(z^(-2)).
After subtracting Q^{K} and G^{K}, the rational difference has no
finite poles and tends to zero at infinity, hence vanishes identically:

    T^{K}=Q^{K}+G^{K}.                                      (7)

In particular there is no omitted polynomial part. For K=0, (7)
holds with G^{0}=0 and T^{0}=Q^{0}=B_u(x)L.

On the spatial circle set b^{K}(zeta)=B_{K}(R*zeta),
g^{K}(zeta)=G^{K}(R*zeta) and F^{K}=b^{K}g^{K}. The function
b^{K} is inner and F^{K} is holomorphic near the closed disk:
its grid poles have all been cancelled. Multiplying (7) by b^{K}
gives

    b^{K} q^{K}=B_u(x)L(R*zeta)-F^{K}.                     (8)

The first term has strictly negative Fourier modes; F^{K} has
nonnegative modes. Orthogonality and |b^{K}|=1 therefore give

    ||q^{K}||_2^2=|B_u(x)|^2||L(R*zeta)||_2^2+||F^{K}||_2^2. (9)

These are finite rational functions with poles a fixed positive
distance from the spatial circle for each family. Their geometric
Fourier expansions converge absolutely and uniformly. Their angular
dependence is continuous on the compact circle. Thus the integrations
used here and below introduce no interchange requiring a bound uniform
in n or in the pole separation.

For completeness the exact polynomial constraint at K=n is as follows.
Let A_u(z)=product_(j<n)(z-b_j),
D_u(z)=product_(j<n)(U-conjugate(b_j)*z), h_u=A_u G^{n},
and V_u=P Q^{n}. The degrees of h_u and V_u are at most n-1
and M-1, respectively, even when P has repeated zeros. Since
B_u=R^n A_u/D_u, (7) gives the polynomial identity

    A_u V_u + P h_u = B_u(x)*R^(-n)*D_u P'.                (10)

All grid contributions are in h_u. The common degree-M polynomial
has not been replaced by separate polynomials for each angle.
Identity (10) alone is not a quantitative lower bound.

### 2. Orthogonal grid coefficients and the response of every prefix

Write beta_j=b_j/R and let

    e_j(zeta)=sqrt(1-|beta_j|^2)/(1-conjugate(beta_j)*zeta)
                  *product_(k<j)(zeta-beta_k)/(1-conjugate(beta_k)*zeta).

For j<K these functions form an orthonormal basis of the K-dimensional
space of rational functions with denominator
product_(1<=j<K)(1-conjugate(beta_j)*zeta) and numerator of degree
at most K-1. Here beta_0=0, so e_0=1. To verify the claim, the
geometric-series reproducing identity is

    <f, 1/(1-conjugate(beta)*zeta)>=f(beta),

with the inner product linear in its first entry. Each normalized
kernel has norm one; multiplication by the preceding inner factors
preserves it. For j<k, cancel the common inner prefix in the inner
product. The remaining function from e_k has a zero at beta_j,
so the reproducing identity makes the inner product zero. All K
functions have the displayed common denominator and numerator bound.
That rational space has dimension K, so orthonormality proves they
are a basis. F^{K} belongs to this space by (6) and cancellation of
its K grid poles.

Take its coefficient against e_j in (8). The negative Fourier term
is orthogonal to e_j. On |zeta|=1, cancellation of the prefix gives

    b^{K}(zeta)*conjugate(e_j(zeta))
       =sqrt(v_j)*zeta/(1-conjugate(beta_j)*zeta)
          *product_(j<k<K)(zeta-beta_k)/(1-conjugate(beta_k)*zeta).

For any f holomorphic near the closed disk, the residue rule is
mean_zeta [zeta*f(zeta)/(zeta-alpha)]=f(alpha). Apply it to each
simple pole of q^{K}. The factors with j<k<K cancel its inverse
grid weights. The factor with index j combines with
1-conjugate(beta_j)*alpha to give alpha-beta_j. Including the
1/R in the normalized symbol, the exact coefficient is

    <F^{K},e_j>=-sqrt(v_j)*B_u(x)*R_j(u),   j<K.            (11)

In particular this coefficient is independent of K once K>j.
Finite Parseval in this K-dimensional space proves (1) from (9).
No sign was assigned to the complex terms inside R_j.

Finally (2) is inner and has norm one. C645n's finite projection
identity P_-[f(zeta)/(zeta-alpha)]=f(alpha)/(zeta-alpha)
applies: f^{K}(a/R)=B_u(a)/B_{K},u(a). This proves that its
entire Hankel output is q^{K}, not a truncation of that output.
Equation (1) also proves the pointwise monotonicity

    ||q^{K}||_2 <= ||q^{K+1}||_2.                          (12)

### 3. Inverse Gram norm, raw-data rate, and the remaining threshold

The reproducing kernels at beta_j span the same rational space as
the e_j. Their Gram matrix is exactly C. They are linearly
independent: after multiplication by their common denominator,
evaluation at its distinct reciprocal roots eliminates every
nonconstant kernel coefficient, and then eliminates the constant
one. Thus C is positive definite. Formula (8), evaluated at beta_j
after the removable singularities have been filled in, gives

    F^{n}(beta_j)=B_u(x)*L(b_j).                           (13)

Solving the finite Gram interpolation system shows that the squared
norm is the data vector's quadratic form with C^(-1), proving (3).
Explicitly, if F=sum c_j k_(beta_j), its values are Cc, and
||F||_2^2=c^*Cc. This also fixes all conjugation conventions.

For every allowed a and b_j,

    Re(b_j-a)>=d-1=1/4,    |b_j-a|<=1+R-eta=473/200,
    |b_j-a|>=d-t_j>1/4.

Consequently each reciprocal has positive real part and

    c_0 M <= Re L(b_j) <= |L(b_j)| <=4M.

Summing squares and taking the angular mean proves (4). C645n's
exact rate estimate, proved there by finite Riemann sums and an
angular arc bound, also gives

    (335/363)*exp(-1/4)/(sqrt(pi)*n^(1/4))*exp(-lambda*n)
       <= E_n <= exp(-lambda*n),
    47/1000<lambda<49/1000,    lambda-1/32>63/4000.         (14)

Thus the raw data have precisely this insufficient exponential rate,
up to polynomial factors; M<=n/3 makes the upper comparison uniform.
This says nothing adverse about the inverse Gram amplification.
Indeed, for the admissible one-pole family Z={x}, r_x=1, (9) gives

    ||G^{n}(R*zeta)||_2^2=(1-|B_u(x)|^2)/(U-d^2).          (15)

It stays large although every datum in (13) is exponentially small.

Let Q_n^2=mean_u ||q^{n}_u||_2^2 and let G_n^2 be the mean of
either side of (3). By C645n's geometric bound on the unweighted
symbol, with rho=(R-eta)/R,

    Q_n^2=G_n^2+J_n^2,
    J_n^2=E_n^2*||L(R*zeta)||_2^2
         <= n^2/[9*R^2*(1-rho^2)]*exp(-2*lambda*n).        (16)

The last term is uniformly o(exp(-n/16)). Therefore the existence
of a uniform positive constant and onset for Q_n>=c exp(-n/32)
is equivalent, with possibly changed constants and onset, to the
same bound for G_n. One direction is immediate; for the other,
subtract J_n^2<=c^2 exp(-n/16)/2 beyond a uniform onset.
This equivalence concerns the sufficient constant-input route only.
The largest operator norm may succeed when this route does not.
Neither side of this still-unproved bound is established by (10).

### 4. Why the degree-M initial prefix cannot suffice

For the family in (5), C645t already verifies all admissibility
conditions and proves the pointwise bound for its full outer-half
inner input. Its B_low consists of indices 0 through (n-1)/2,
so that input is exactly f^{K_*} in (2), with K_*=ceil(n/2).
Its complete output is q^{K_*}. Apply (12) to obtain (5) for
every earlier prefix without redoing the Chebyshev contour proof.
The maximum over K<=K_* satisfies the same bound at each angle,
so angle-dependent selection cannot evade it.

The exact rate deficit is 7/200-1/32=3/800. In particular

    exp(n/32)*(mean_u ||q^{K(u)}_u||_2^2)^(1/2)
      <=22000*m*exp(-3*n/800) -> 0

for every measurable K(u)<=K_* on this admissible sequence.
Equation (1) also bounds the squared sum of the first K_* grid
coefficients by the square of (5). Since M=m<K_*, this explicitly
rules out the proposed simplification that the first M grid
coefficients should suffice merely because P has degree M.
It does not rule out use of the full polynomial identity with the
later coefficients, another selection of grid indices, or the full
angular operator target. All Xi realization and sign gaps remain.

### 5. Exact finite checks and their limits

The reproducible algebra check is
`python3 scripts/one-sided-hankel/common-polynomial-grid-certificate.py`.
Its full output is
`scripts/one-sided-hankel/common-polynomial-grid-certificate.json`.
It uses Gaussian rational arithmetic throughout. Five cases at n=6,9
include real, imaginary and oblique unit rotations, and repeated
polynomial zeros with original residues two and three. It computes
the complete Z and grid residues, both finite kernel norms, the
inverse Gram system, every coefficient of (10), and (1) for every
K=0,...,n. All 35 aggregate checks and all 41 prefix equalities
pass with exact difference zero. The full check fields were inspected.
These are normalization checks at finite parameters, not evidence
of a uniform angular lower bound or an independent proof audit.

## Mathlib

Full matching coverage for the retained-grid identities, their exact
prefix ordering and the quantitative stop has not been checked; no
absence claim is made. The supporting ingredients are finite rational
residue decomposition, Hardy kernels, Fourier orthogonality and finite
Gram interpolation. No Mathlib result about the missing uniform
angular bound or actual-Xi realization is assumed.
