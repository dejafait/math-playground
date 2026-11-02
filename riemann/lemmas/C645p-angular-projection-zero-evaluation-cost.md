# Corollary 645p: nonpositive angular energy and the sharp zero-evaluation cost

## Hypotheses

Fix n>=5, d=5/4, x=-d, R=11/8, U=R^2, eta=1/100 and t_j=j/n.
Let Z contain x and consist of distinct points a with Re(a)=x and
|a|<=R-eta. Give each a a positive integer original simple-pole residue
r_a, with M=sum_a r_a<=n/3. The same Z and residues are used for all
angles, without separation or ordinate symmetry. Set u=i exp(i theta),
and retain the conjugated angle in

    B_theta(v)=product_(j=0)^(n-1)
        R*(v-i*exp(i*theta)*t_j)/(U+i*exp(-i*theta)*t_j*v).

In C645g's normalized circle spaces, H_q f=P_-(q f), where H^2 has
nonnegative modes and H^2_- strictly negative modes, put

    W_a(u)=B_theta(x)/B_theta(a)
          =(x/a)*product_(j=1)^(n-1)
            [(x-t_j*u)/(a-t_j*u)]*[(U*u-t_j*a)/(U*u-t_j*x)],
    q(u,zeta)=sum_a r_a*W_a(u)/(R*zeta-a),
    A_n=(mean_u ||H_q(u,.)||^2)^(1/2).

Write p_j=t_j*x/U for 1<=j<n. These are distinct nonzero real
numbers in (-80/121,0). Let R_j(a) be the residue of W_a at p_j,
with value zero for a cancelled pole, in particular R_j(x)=0.
Let mu_a=mean_u W_a(u)=I(a,x) in C645o. Let P^u_(<=0) denote the
orthogonal projection in the angular variable onto modes of exponent
at most zero, and define G=P^u_(<=0)q. All two-circle norms below use
normalized measure in each variable. The point u=0 below refers to
rational continuation, not boundary evaluation of an L2 function.

## Conclusion

The exact projection and its complete signed energy are

    V_a(u):=P^u_(<=0)W_a(u)
            =mu_a+sum_j R_j(a)/(u-p_j),
    G(u,zeta)=sum_a r_a*V_a(u)/(R*zeta-a),                     (1)
    A_n >= ||q||_(L2(u,zeta)) >= ||G||_(L2(u,zeta)),
    ||G||^2=sum_(a,b) r_a*r_b/(U-a*conjugate(b)) *
       [mu_a*conjugate(mu_b)
        +sum_(j,k) R_j(a)*conjugate(R_k(b))/(1-p_j*p_k)].      (2)

Every term, including the zeroth angular mode and signed cross terms,
is retained. Define

    pi_n=(80/121)^(n-1)*(n-1)!/n^(n-1),
    rho=(R-eta)/R=273/275.

Evaluation at angular zero gives a noncancelling quantity, but only the
following transfer bound:

    G(0,zeta)=sum_a r_a*(x/a)/(R*zeta-a),
    ||G|| >= pi_n*||G(0,.)||_2,                              (3)
    M*d^2/[R*(R-eta)^2] <= ||G(0,.)||_2
                                      <= M/[R*sqrt(1-rho^2)]. (4)

The constant pi_n in (3) is exactly optimal on the ambient rational
space span{1,(u-p_1)^(-1),...,(u-p_(n-1))^(-1)}, also with spatial
Hilbert-space coefficients. Its rate is

    -log(pi_n)/n -> 1+log(121/80) > 1/32.                    (5)

Consequently the *lower estimate supplied by this evaluation* satisfies

    e^(n/32)*pi_n*||G(0,.)||_2 -> 0                         (6)

uniformly over the stated families. This stops an argument based only
on this continued value and the ambient rational-space norm. It does
not upper-bound ||G|| or A_n: the ambient extremizer below is not shown
to come from the prescribed positive integer residues. Neither the
projection nor the full angular target is refuted. No useful improvement
over the previously recorded angular lower bound, actual-Xi realization,
RH result or certified novelty is asserted. This result is unaudited.

## Proof

### Source scope and why the calculation is needed

The unchanged ready
[EXPLORE assessment](../drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md)
covers this Fourier/residue test on the exact approved family. C645g
supplies the spaces and normalization; C645o supplies the product,
residues and exact mean identity. Its negative-entry witness is a
contrast, not an assumption used here. C645o remains independently
unaudited; the specialization uses only its analytic identities, whose
pole and constant-term cases are also justified below. The scoped
duplicate search found the earlier suggestion that cancellation of
common poles could be costly, but no evaluated sharp transfer factor.

Import scalar Fourier orthogonality and Parseval from A. Levitt,
*Analyse de Fourier et applications*,
[author PDF](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf),
version retrieved 2 November 2026, Theorem 1.3/Exercise 1.2 and
Theorem 1.11/Corollary 1.12, printed pp.6,8 (PDF pp.12,14), as inspected
in the assessment. Dividing measure by 2*pi makes every exponential
have norm one. The Hankel convention and contractive projection are
those of L. Baratchart, S. Chevillard and T. Qian, *Minimax principle
and lower bounds in H2-rational approximation*, J. Approx. Theory 206
(2016), 17--47, author preprint v2 (24 March 2015),
[Section 4, (17)--(19)](https://arxiv.org/pdf/1501.01161v2),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004).

These are standard imported identities, not new operator theorems.
The finite-product specialization and its exact transfer cost are
written out because the cited identities do not evaluate that cost.
No general Nehari, AAK or model-space theorem is reproved or needed.

### 1. The projection, including all cancellation cases

For each a, the only possible poles of W_a inside the angular unit
disk are the simple p_j. All a/t_j lie outside, since |a|>=5/4>t_j.
Each p_j is distinct and nonzero. Subtract its principal parts:

    F_a(u)=W_a(u)-sum_j R_j(a)/(u-p_j).

This extends holomorphically to a neighborhood of the closed unit disk.
A cancelled pole has residue zero and causes no exception. When a=x,
W_x=1, all residues vanish and the same statement applies. For |u|=1,

    1/(u-p_j)=sum_(ell>=0) p_j^ell*u^(-ell-1)

converges absolutely and uniformly. Thus the strictly negative angular
modes are exactly these principal parts. The remaining nonpositive
mode is F_a(0)=mu_a. Direct evaluation of the product gives W_a(0)=x/a:
each nonzero-grid pair has cancelling ratios x/a and a/x. Hence

    mu_a=x/a+sum_j R_j(a)/p_j,
    V_a(0)=mu_a-sum_j R_j(a)/p_j=x/a.                         (7)

This also verifies the particular mean identity from C645o used here.
There is no holomorphic mean-value assertion for unmodified W_a.

The spatial series of 1/(R*zeta-a) converges uniformly because
|a|/R<=rho<1. All angular functions are continuous and bounded on the
unit circle, for each fixed n and finite family. The sums over a,j
are finite. These facts justify projecting term by term to obtain (1).
For each u, H_q 1=q and ||1||_2=1, because q has only strictly negative
spatial modes. Integrating that inequality and then using contractivity
of P^u_(<=0) proves the inequalities in (2).

Angular orthogonality gives

    mean_u V_a*conjugate(V_b)
      =mu_a*conjugate(mu_b)
        +sum_(j,k) R_j(a)*conjugate(R_k(b))/(1-p_j*p_k).

The constant and negative modes are orthogonal, and the last kernel is
sum_(ell>=0) p_j^ell*p_k^ell. Spatial orthogonality similarly gives

    mean_zeta 1/[(R*zeta-a)*conjugate(R*zeta-b)]
                                            =1/(U-a*conjugate(b)).

Combining the two identities proves the equality in (2). Absolute
uniform geometric bounds in both circle variables justify these
interchanges. Their bounding constants may depend on n and the finite
family; no uniform bound on them is claimed or needed for the identity.

### 2. An exact and sharp norm for continuation to zero

Set

    beta_n(u)=product_(j=1)^(n-1) (u-p_j)/(1-p_j*u).

This is holomorphic near the closed disk, has modulus one on its
boundary, and beta_n(0)=product_j(-p_j)=pi_n>0. The product beta_n G
has removable singularities at every p_j and is holomorphic near the
closed angular disk. It has the same two-circle norm as G. For each
spatial boundary point, its angular constant coefficient is
beta_n(0)G(0,zeta). The scalar constant-coefficient inequality, integrated
over zeta, proves (3). All integrands are continuous on the compact
boundary product, so the integration order is harmless. This argument
also applies to any member of the ambient rational space with spatial
coefficients.

For sharpness take V_*(u)=1/beta_n(u). Its denominator has exactly the
distinct roots p_j, and its numerator has the same degree n-1; partial
fractions place it in span{1,(u-p_j)^(-1)}. On the unit circle it has
modulus one, whereas V_*(0)=1/pi_n. Thus (3) is equality for V_*.
Tensoring it with any nonzero spatial function proves the asserted
Hilbert-space sharpness. This is an extremizer in the ambient space
only; no identification with an admissible q is made.

### 3. The noncancelling value and the inadequate rate

Equation (7) proves the first line of (3). Its first spatial Fourier
coefficient is c_0=(1/R)*sum_a r_a*x/a. Writing a=-d+iy gives

    Re(x/a)=d^2/(d^2+y^2)>=d^2/(R-eta)^2.

Positivity of the original residues and Parseval yield the lower bound
in (4). Also |x/a|<=1 and the spatial kernel norm is
1/[R*sqrt(1-|a|^2/R^2)], giving the upper bound by the triangle
inequality. This uses no positivity of the weighted complex amplitudes.

To verify (5) without a factorial asymptotic import, set k=n-1. The
monotonicity of log gives, for k>=1,

    k*log(k)-k+1 <= log(k!)
                          <= k*log(k)-k+1+log(k).

Divide log(pi_n)=k*log(80/121)+log(k!)-k*log(n) by n.
Since k/n->1, log(k/n)->0 and log(k)/n->0, these two bounds give (5).
In particular its limit exceeds one, and therefore exceeds 1/32.

There is also a direct finite bound sufficient for (6). Each j/n<1,
so pi_n<=(80/121)^(n-1). For y>=1, integrating 1/t on [1,y] gives
log y>=1-1/y. Hence log(121/80)>=41/121 and (4), M<=n/3 give

    e^(n/32)*pi_n*||G(0,.)||_2
       <= [121*n/(240*R*sqrt(1-rho^2))]
                           *exp(-(1191/3872)*n) -> 0.        (8)

The constant is independent of the family. Equation (8) bounds the
right side of the lower estimate (3), not its left side. Sharpness in
the ambient space explains why that generic transfer inequality cannot
be improved without using additional structure of V_a. Neither (2)
nor the admissibility constraints have been used to prove or disprove
the desired lower bound for the actual projection.

The exploratory script `scripts/one-sided-hankel/angular-projection-screen.py`
and its JSON record have no rounding, aliasing or spatial-tail enclosure
and play no role in this proof. No numerical certificate is required
by the elementary exact inequalities above.

## Mathlib

Full matching coverage of this product-specific projection and sharp
continuation-cost statement has not been checked; no absence claim is
made. Fourier orthogonality, contractive projection and finite Blaschke
factor identities are supporting mathematics, not a matching theorem
for the uniform angular target. The source citations above supply the
standard analytic inputs used here.
