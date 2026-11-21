# Corollary C028q: tilted-theta finite spectral skewness first variation

## Hypotheses

Use the full positive kernel K of L019 and, for real theta, the probability
measure on R

    dmu_theta(u)=exp(theta*u)*K(|u|)du/Z(theta),
    Z(theta)=integral_R exp(theta*u)*K(|u|)du.

Let p_n(u;theta) be its monic orthogonal polynomials, with recurrence

    u*p_n=p_(n+1)+A_n(theta)*p_n+B_n(theta)*p_(n-1),
    p_(-1)=0, p_0=1, B_0=0, B_n>0 for n>=1.

For each fixed integer d>=3 let J_d(theta) be the principal Jacobi block
on indices 0,...,d-1: diagonal A_n and off-diagonal sqrt(B_n) on edge
(n-1,n), 1<=n<d. The full recurrence has B_d(theta)>0 outside this
block. Put

    m_d=tr(J_d)/d, C_d=J_d-m_d*I,
    M_r(d,theta)=tr(C_d^r)/d, g_d(theta)=M_3/M_2^(3/2),
    beta_n=B_n(0), T_d=sum_(n=1)^(d-1) beta_n, V_d=2*T_d/d.

Here M_r are empirical spectral moments, not the probability moments
of mu_theta or Gauss quadrature moments. For the actual cubic comparison
use the centered monic polynomial Q_d and constants S_2,S_3>0 of C028h.
No RH, actual-root reality, simplicity, moment determinacy, recurrence
asymptotic or uniform-in-degree estimate is assumed.

## Conclusion

For every fixed d>=3, the exact first-response identity is

    g_d(0)=0,
    g_d'(0)=3*beta_d*(beta_(d-1)-V_d)/(d*V_d^(3/2)).       (1)

Thus its sign is exactly the sign of beta_(d-1)-2*T_d/d, with zero
response if and only if equality holds. Positivity of the individual
recurrence coefficients alone does not choose a sign for this difference.
This statement makes no nonvanishing claim for every degree.

For this full theta measure the degree-three response is strictly negative:

    g_3'(0)=beta_3*(beta_2-2*beta_1)/(3*V_3^(3/2))
           =-4*beta_3*S_2/(mu_2*V_3^(3/2))<0,           (2)
    mu_2=integral_R u^2 dmu_0(u)>0.

Consequently small positive tilts give negative g_3 and small negative
tilts give positive g_3. This is a locally adjustable cubic direction.

The actual formal centered root moments are

    M_2^actual=(d-1)*S_2,
    M_3^actual=-(d-1)*(d-2)*S_3,
    gamma_d=-(d-2)*S_3/(sqrt(d-1)*S_2^(3/2)).           (3)

At any fixed theta, a real affine change u->a+sigma*u, sigma!=0,
matches Q_d's mean and quadratic coefficient precisely when

    a=-sigma*m_d, |sigma|=sqrt((d-1)*S_2/M_2(d,theta)).

With these choices it also matches the cubic coefficient if and only if

    sign(sigma)*g_d(theta)=gamma_d.                    (4)

In particular gamma_3=-S_3/(sqrt(2)*S_2^(3/2)) is a fixed nonzero
target. Equation (2) does not show that this magnitude is attained.
No nonlinear three-match feasibility, control of lower coefficients,
uniform remainder, sublinear companion cost or RH conclusion follows.

## Proof

### Imported deformation and its applicability

Walter Van Assche, *Orthogonal polynomials, Toda lattices and Painleve
equations*, arXiv:2202.11017v1, 22 February 2022,
[Section 1.1, (1.1)-(1.4), and Section 2.1, Lemma 2.1 and (2.1)-(2.4),
printed pp.4-6](https://arxiv.org/pdf/2202.11017v1), supplies the
exponential-deformation equations. With t=theta, b_n=A_n and a_n^2=B_n,
they are

    A_n'=B_(n+1)-B_n,
    B_n'=B_n*(A_n-A_(n-1)), n>=1.                     (5)

These known equations are imported, not reproved. In particular the
finite terminal-zero system discussed there is not the principal block
of the present infinite-support measure.

For every fixed R and nonnegative integer r, L019 provides an integrable
majorant for |u|^r*exp(R*|u|)*K(|u|): choose its exponential decay rate
larger than R and absorb the fixed polynomial in the remaining decay.
This proves positivity and finiteness of Z(theta), all absolute moments
and compact-tilt differentiation of each moment. Every nonzero polynomial
has positive squared integral, since the density is positive on every
interval. Each finite Gram matrix is therefore positive definite. The
finite Gram linear equations defining p_n have smooth coefficients and
nonzero determinant, so their coefficients and norm ratios are smooth
in theta. The source deformation is applicable at every fixed degree.
Scalar normalization by Z(theta) changes neither monic polynomials nor
norm ratios, so (5) is unchanged by using probability measures.

The monic recurrence and even parity are also the standard inputs in
[DLMF 18.2(iv), (18.2.10)-(18.2.11)](https://dlmf.nist.gov/18.2#iv)
and [18.2.21](https://dlmf.nist.gov/18.2.E21). At theta=0 even parity
gives A_n(0)=0 for every n. Hence (5) gives

    A_n'(0)=beta_(n+1)-beta_n, B_n'(0)=0, beta_0=0.    (6)

No uniqueness statement for an unbounded moment problem is used.

### Centered trace and the exterior boundary

Write J=J_d(0). It has zero diagonal, and J_d'(0)=D is diagonal with
D_nn=beta_(n+1)-beta_n. Differentiating each positive sqrt(B_n) gives
zero by (6). Thus m_d(0)=0 and the telescope gives

    m_d'(0)=sum_(n=0)^(d-1)(beta_(n+1)-beta_n)/d=beta_d/d.

Set w_n=(J^2)_nn. Within this finite block,

    w_n=beta_n+beta_(n+1), 0<=n<=d-2,
    w_(d-1)=beta_(d-1).

In particular tr(J^2)=2*T_d and M_2(d,0)=V_d>0. There is no closed
three-edge walk on a path, so tr(J^3)=0. Also
M_2'(d,0)=2*tr(J*(D-m_d'(0)*I))/d=0, since the second factor is
diagonal and J has zero diagonal. Cyclicity of the finite trace gives

    M_3'(d,0)=(3/d)*tr(J^2*(D-(beta_d/d)*I)).

The uncentered weighted diagonal sum is exactly

    sum_(n=0)^(d-1) w_n*(beta_(n+1)-beta_n)
      =sum_(n=0)^(d-2)(beta_(n+1)^2-beta_n^2)
                              +beta_(d-1)*(beta_d-beta_(d-1))
      =beta_(d-1)*beta_d.

Subtracting the mean derivative therefore yields

    M_3'(d,0)=(3*beta_d/d)*(beta_(d-1)-2*T_d/d).

Differentiate g_d=M_3*M_2^(-3/2). Its normalization derivative is
-(3/2)*M_3*M_2^(-5/2)*M_2', which vanishes at zero because M_3=0.
Dividing the remaining term by V_d^(3/2) proves (1). All differentiations
here are finite matrix operations; beta_d has not been set to zero.

### Independent degree-three endpoint check and the strict theta sign

For d=3 let alpha_i=A_i(theta), c_i=alpha_i-m_3(theta). Direct expansion
of det(xI-J_3) gives

    (x-alpha_0)*(x-alpha_1)*(x-alpha_2)
               -B_1*(x-alpha_2)-B_2*(x-alpha_0).

After x=y+m_3, its constant coefficient is
-c_0*c_1*c_2+B_1*c_2+B_2*c_0. At zero each c_i=0, and

    c_0'=beta_1-beta_3/3,
    c_2'=beta_3-beta_2-beta_3/3.

The derivative of that constant coefficient is therefore

    beta_1*(2*beta_3/3-beta_2)
                  +beta_2*(beta_1-beta_3/3)
      =beta_3*(2*beta_1-beta_2)/3.

For a centered monic cubic, Newton's identity makes the third root-power
sum minus three times its constant coefficient. Division by d=3 gives
M_3'(3,0)=beta_3*(beta_2-2*beta_1)/3, independently checking the endpoint
and empirical factors in (2).

Let mu_4=integral_R u^4 dmu_0. L021 gives mu_2=M_2/M_0 and
mu_4=M_4/M_0 in its half-line moment notation. Orthogonality at zero
gives p_1=u and p_2=u^2-mu_2, hence h_0=1, h_1=mu_2 and
h_2=mu_4-mu_2^2. The monic norm ratios give

    beta_1=mu_2, beta_2=mu_4/mu_2-mu_2.

The already established L025 identity and L027 strict sign give
mu_4-3*mu_2^2=-12*S_2<0. It follows that
beta_2-2*beta_1=-12*S_2/mu_2<0. Positivity of beta_3 and V_3 proves
(2). The first derivative definition, with g_3(0)=0, gives the stated
opposite signs for sufficiently small positive and negative theta.
This uses an existing strict fourth-moment input, not a new recurrence
estimate or a numerical tilt grid. No higher derivative is calculated.

### Actual cubic normalization and both affine signs

C028h supplies the top coefficients

    Q_d(x)=x^d-binom(d,2)*S_2*x^(d-2)
                          +2*binom(d,3)*S_3*x^(d-3)+... .

The coefficient of x^(d-1) is zero. Newton's identities through order
three give centered formal sums r_1=0,
r_2=2*binom(d,2)*S_2=d*(d-1)*S_2 and
r_3=-6*binom(d,3)*S_3=-d*(d-1)*(d-2)*S_3.
These identities hold also at d=3 and do not assume actual roots real.
Dividing each sum by d proves (3). This agrees with the actual sums
in C028k; its classical-family feasibility restriction is not an input
here.

The characteristic polynomial of J_d is p_d, as follows by the finite
determinant recurrence. Under u->a+sigma*u it becomes the monic
polynomial sigma^d*p_d((x-a)/sigma), for either sign of sigma. Its mean
is a+sigma*m_d; its centered empirical moments of orders two and three
are sigma^2*M_2 and sigma^3*M_3. Equality of the first three subleading
coefficients of two monic degree-d polynomials is equivalent, by
Newton's identities, to equality of their first three formal power
sums. Thus the mean and variance conditions fix a and |sigma| as
stated, and the standardized cubic becomes sign(sigma)*g_d(theta).
This proves (4), including reflection. If matching the uncentered P_d
instead, add its mean to a; neither centered moment changes.

Strict first response supplies only arbitrarily small nonzero cubic
values near zero. It gives no certified neighborhood large enough to
contain gamma_3, and no nonvanishing or size bound for arbitrary d.
Even successful three-coefficient matching would leave all lower
residuals and the full height-majorant payment unresolved. The floors
for the even families in C028o/p remain valid in their original scope;
this local response does not reverse any upper bound for actual H_d.

### Independent finite audit1720 — 19 November 2026

Accepted without correction under assessment1718, separately approved1719.
This audits the fixed-degree specialization of the cited Toda equations;
it supplies no stronger theorem or claim of progress beyond checked
sources. No new recurrence estimate or global-tilt assertion is used.

L019's decay supplies domination for each fixed polynomial moment on
every compact tilt interval, on both halves of R. Positive density
makes every finite polynomial Gram matrix strictly positive definite.
Thus the imported deformation applies to the monic recurrence, including
the exterior B_d=h_d/h_(d-1)>0. Probability normalization cancels from
each norm ratio; it does not add a term to either equation (5).
Smooth finite matrices suffice throughout; no derivative of an individual
eigenvalue, simple-root hypothesis or determinate moment problem is used.

The derivative matrix at zero is diagonal. Its trace is beta_d, whereas
its contraction with J^2 is beta_(d-1)*beta_d: the inner terms telescope
to beta_(d-1)^2 and the last term is
beta_(d-1)*(beta_d-beta_(d-1)). Centering subtracts
(beta_d/d)*tr(J^2)=2*beta_d*T_d/d. Multiplication by 3/d and division
by V_d^(3/2) give exactly (1), with the exterior coefficient retained.
The derivative of M_2 vanishes by its zero-diagonal trace contraction.
Independently, the normalization term in g_d' vanishes because M_3=0;
no nonzero response has been presumed in differentiating this quotient.

At d=3, the centered determinant has constant coefficient
-c_0*c_1*c_2+B_1*c_2+B_2*c_0. Its derivative is
beta_3*(2*beta_1-beta_2)/3. Newton's identity gives the third
power sum as minus three times that coefficient, and the empirical
division by three leaves its negative. Hence
M_3'=beta_3*(beta_2-2*beta_1)/3, agreeing with the general formula.
The norm-ratio calculation gives beta_2=mu_4/mu_2-mu_2, so the L025
identity is used with its exact factor12:
beta_2-2*beta_1=(mu_4-3*mu_2^2)/mu_2=-12*S_2/mu_2.
C028h's S_2 is this same actual constant, not a raw variance or a
rescaled fourth cumulant. L027 supplies strict positivity of S_2
unconditionally. Positive beta_3 and V_3 prove precisely (2).

For every d>=3 the centered actual coefficients are -binom(d,2)*S_2
and +2*binom(d,3)*S_3. Newton's second and third sums are therefore
d*(d-1)*S_2 and -d*(d-1)*(d-2)*S_3. Dividing by d before
standardizing proves (3), including the constant coefficient when d=3.
For either nonzero real sigma, sigma^d*p_d((x-a)/sigma) remains monic;
its centered moments are sigma^2*M_2 and sigma^3*M_3. Since M_2>0,
the quadratic match fixes |sigma|, while sigma^3/|sigma|^3 is
sign(sigma). This verifies (4) for both affine signs. Returning to
uncentered P_d adds its mean -b_1 to a and changes neither moment.

The continuation test for this audit passes. No correction to the direct
mathematical inputs is needed. Local first response remains distinct
from achieving gamma_3: no size of a suitable tilt neighborhood is
certified, and no general-degree response, nonlinear matching, lower
residual payment or actual-Xi positivity follows. Stops1695/1713 and
the parked global1716 question retain their scopes.

## Mathlib

Not checked. No full matching Mathlib theorem for the tilted-theta
finite-block response or its strict degree-three specialization is
claimed. The external Toda, recurrence and parity inputs are cited
above; finite trace identities and the stated specialization are proved
here. This is REPRODUCTION/SPECIALIZE under assessment1716, not a claim
of progress beyond the literature checked. Independent audit1720 accepts
the unchanged calculation under assessment1718/approval1719.
