# Lemma 651: uniform cost of the joint full-grid polynomial dual

## Hypotheses

Retain n>=5, x=-5/4, R=11/8, U=R^2, eta=1/100 and t_j=j/n.
The common finite set Z consists of distinct points with Re(a)=x,
|a|<=R-eta and x in Z. Its original simple-pole residues r_a are
positive integers, and M=sum_a r_a<=n/3. The same poles and residues
are used for every |u|=1. No separation, symmetry or integrality of
polynomial coefficients is assumed. Set

    P(z)=product_a (z-a)^(r_a),  L(z)=P'(z)/P(z),
    B_u(z)=product_(0<=j<n) R*(z-t_j*u)/(U-t_j*z/u),
    b_u(zeta)=B_u(R*zeta)=sum_(ell>=0) beta_ell(u)*zeta^ell,
    W_a(u)=B_u(x)/B_u(a),
    q_u(zeta)=sum_a r_a*W_a(u)/(R*zeta-a).

Use normalized circle means, H^2 with nonnegative modes, strictly
negative H^2_-, and <f,g>=mean f*conjugate(g), linear in the first
variable. C645y's full analytic component F_u satisfies

    b_u*q_u=B_u(x)*L(R*zeta)-F_u.

In L649's notation put, for k>=0,

    c_k(u)=R^(-1)*sum_a r_a*W_a(u)*(a/R)^k,
    h_k=R^(-1)*sum_a r_a*(a/R)^k,
    D_single,n=sum_a r_a^2*mean_u |W_a(u)|^2/(U-|a|^2).

Define Js=zeta^(-1)*conjugate(s) on the boundary. For 0<=k<M put

    e_(k,u)=P_-(b_u*zeta^(-k-1)),
    d_(k,u)=P_+(b_u*zeta^(-k-1)),
    D_(u,M)=span_C{d_(k,u):0<=k<M},
    y_k(u)=<F_u,d_(k,u)>,
    G_(jk)(u)=<d_(k,u),d_(j,u)>.

The span is exactly {P_+(b_u Js):deg s<M}; the anti-linearity of J
does not restrict the allowed complex combinations. All n grid factors
are retained. Let

    delta=log(26/19)-(log 2)/3,
    epsilon_n=exp(-delta*n),
    sigma=sqrt(U-(R-eta)^2)=sqrt(137/5000),
    tau_n=(M/sigma)*epsilon_n,
    J_n=mean_u ||Proj_(D_(u,M)) F_u||_2^2,
    S_n=mean_u sum_(0<=k<M)|c_k(u)|^2.

## Conclusion

The full joint Gram matrix is uniformly well conditioned:

    delta>643/8788>1/16,
    (1-epsilon_n^2)*I <= G_u <= I,
    (5/13)*I <= G_u <= I.                                  (1)

These inequalities are uniform in the angle, the admissible family and
all pole separations. In particular the joint image has dimension M.
With E_u the M by M matrix

    (E_u)_(jk)=beta_(k-j)(u) if k>=j, and 0 otherwise,

its complete response and cost are

    G_u=I-E_u^*E_u,       ||E_u||<=epsilon_n,
    y_u=B_u(x)*E_u^*h^(M)-c^(M)(u),
    ||Proj_D F_u||_2^2=y_u^*G_u^(-1)y_u,
    ||y_u||^2 <= ||Proj_D F_u||_2^2
                  <=(1-epsilon_n^2)^(-1)||y_u||^2.          (2)

Here h^(M),c^(M) are the first M spatial coefficient vectors;
stars in matrix expressions mean conjugate transposes. The cost in
(2) is evaluated, rather than left as an unevaluated Gram minimum.
It follows that

    max(0,sqrt(S_n)-tau_n)^2 <= J_n
                      <=(sqrt(S_n)+tau_n)^2/(1-epsilon_n^2). (3)

Moreover D_single,n>=64/21, and, uniformly over the admissible families,

    tau_n/[exp(-n/32)*sqrt(D_single,n)]
       <=sqrt(21)/(24*sigma)*n*exp(-(delta-1/32)*n) -> 0.    (4)

Consequently the existence of uniform positive constants and onsets
in J_n>=c*exp(-n/16)*D_single,n is equivalent to their existence in
S_n>=c'*exp(-n/16)*D_single,n. Constants may change; neither inequality
is established here. This is a quantitative removal of the joint norm
cost, not a uniform lower bound on the correlated response.

For L650's close pair x,a=x+i*2^(-n), n>=6, the joint construction
retains exactly

    d_(x,u)+d_(a,u)=d_(0,u)=b_u/zeta,
    ||d_(0,u)||=1,  <F_u,d_(0,u)>=-(1+W_a(u))/R.             (5)

The subscripts x,a on the left denote L650's pole-isolating duals;
the subscript 0 denotes the monomial dual defined here. Thus its
separate-column obstruction has not been imported into this joint span.

The rate-1/16 response bound, matching detector upper bounds, Xi
realization and all-degree signs remain unresolved. This specialization
has not received a separate critical audit. The checked literature did
not supply this exact quantitative bound; no certified novelty or RH
resolution candidate is claimed.

## Proof

### 1. Source scope, normalization and the remaining cost

The unchanged invocation-start assessment
`drafts/literature/2026-11-02-joint-full-grid-polynomial-dual.md`
has decision EXPLORE and covers this entire joint space, its complete
Gram cost and finite polynomial/Fourier algebra. Its primary comparison
is reused. The scoped duplicate check included the C645 family,
L646--L650, the full-grid assessments and the relevant recorded stops.
C645y's grid-prefix stop and L650's separately normalized columns are
distinct from this image of spatial polynomials. They are limitations
of other certificates, not premises giving a sign here.

Import the Hardy projection convention from L. Baratchart, S. Chevillard
and T. Qian, *Minimax principle and lower bounds in H2-rational
approximation*, J. Approx. Theory 206 (2016), 17--47, preprint v2,
24 March 2015, [Section 4, (17)--(19)](https://arxiv.org/pdf/1501.01161v2),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004).
Import scalar Fourier orthogonality and Parseval from A. Levitt,
*Analyse de Fourier et applications*, version retrieved 2 November
2026, [Theorem 1.3/Exercise 1.2 and Theorem 1.11/Corollary 1.12,
printed pp.6,8](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf).
These primary inputs were inspected in the reused assessment chain;
no new source retrieval or independent source audit is claimed.

No general approximation theorem is reproved. The explicit grid and
M<=n/3 permit the coefficient estimate below, which is needed to
evaluate the otherwise unspecified joint norm cost. L650's arbitrary
polynomial response formula (10), together with C645y's full component
identity and L649's coefficient normalization, supplies the exact
response used below. None of their claimed target bounds is assumed.

Each b_u is holomorphic on a neighborhood of the closed unit disk and
has boundary modulus one. Indeed its grid zeros are t_j*u/R, of
modulus less than 1/R, and the denominator uses their conjugates.
Also beta_0=0 because t_0=0. Poles a/R have modulus at most
273/275<1 and avoid every grid zero. All fixed-family Fourier
expansions in use converge absolutely and uniformly on the spatial
circle, and depend continuously on u. The forthcoming bounds themselves
are uniform; the exact identities do not require a uniform separation.

### 2. A small-circle bound for the entire grid product

For 0<=alpha<1 and |zeta|=r<1, an elementary disk-factor calculation
gives

    |(zeta-alpha*u)/(1-alpha*conjugate(u)*zeta)|
                        <=(r+alpha)/(1+r*alpha).

For r*alpha>0, square the ratio and put cos(theta)=Re(zeta/u)/r.
The squared ratio is
(r^2+alpha^2-2*r*alpha*cos(theta))/(1+r^2*alpha^2-2*r*alpha*cos(theta)).
Its derivative with respect to cos(theta) is nonpositive, since its
numerator after differentiation is -2*r*alpha*(1-r^2)*(1-alpha^2).
The maximum is therefore at cos(theta)=-1. The zero cases follow
directly. Denominators stay positive.

Set r=1/2 and alpha=t/R. The right side is

    f(t)=(11+16*t)/(22+8*t).

For 0<=t<=1, g(t)=log f(t) has g'(t)>0 and g''(t)<0:
16/(11+16*t)>8/(22+8*t)>0, which proves both signs.
The tangent inequality, obtained by integrating the decreasing
derivative on either side of 1/2, is

    g(t)<=g(1/2)+g'(1/2)*(t-1/2).

Since sum_(j<n)(t_j-1/2)=-1/2 and f(1/2)=19/26, it follows that

    max_(|zeta|=1/2)|b_u(zeta)| <= (19/26)^n.              (6)

This estimates the full product, with no grid factors omitted.
Applying scalar Fourier orthogonality to its uniformly convergent
Taylor series on this smaller circle gives, for every ell>=0,

    beta_ell=2^ell*mean_theta b_u(e^(i*theta)/2)*e^(-i*ell*theta),
    |beta_ell|<=2^ell*(19/26)^n.                          (7)

Thus no additional coefficient theorem or uncontrolled contour limit
is required.

### 3. Full joint Gram cost

The negative part of b_u*zeta^(-k-1) has coefficient beta_(k-j)
at zeta^(-j-1) for 0<=j<=k, and zero otherwise. It has no other
negative coefficients. Hence E_u is exactly its coefficient matrix.
If s=sum_(k<M)s_k*zeta^k, the negative coefficient vector of b_u Js
is E_u*conjugate(s). This explicitly accounts for J's anti-linearity.

Write E_u=sum_(ell=0)^(M-1) beta_ell*S^ell, where S is the
M-dimensional backward shift (ones on the superdiagonal). Each S^ell
has operator norm at most one. Formula (7) and beta_0=0 give

    ||E_u|| <= sum_(ell=0)^(M-1)|beta_ell|
             <=(2^M-1)*(19/26)^n
             <=2^(n/3)*(19/26)^n=epsilon_n.              (8)

This includes M=1, for which E_u=0 exactly. Unitarity of multiplication
by b_u and orthogonality of its negative and nonnegative parts now give
G_u=I-E_u^*E_u, with the index convention in the hypotheses.
This proves the first operator bounds in (1)--(2).

For the explicit exponent comparison,

    3*delta=log(8788/6859)
             >(8788-6859)/8788=1929/8788.

The strict inequality follows by integrating 1/t from 1 to 8788/6859
and comparing it with the constant 6859/8788. Thus
delta>643/8788>1/16; the last comparison is 10288>8788.
For n>=5,

    1-epsilon_n^2 >= 1-exp(-n/8)
                      >= 1-exp(-5/8) >= 1-8/13=5/13,

where exp(5/8)>=1+5/8. The Gram matrix is therefore invertible
with the stated uniform bounds. For any analytic F, its response
vector y_k=<F,d_k> has projection coefficient vector G_u^(-1)y.
Taking its squared norm proves the projection formula and both
inequalities in (2). This retains the cross terms and all allowable
family- and angle-dependent combinations.

### 4. Correlated response and its explicit correction

L650's full polynomial formula, used with s=zeta^k, reads

    <F_u,d_(k,u)>=B_u(x)<L(R*zeta),e_(k,u)>-c_k(u).

The negative Fourier coefficients of L(R*zeta) are h_j. Because
e_(k,u) has only the coefficients already enumerated,

    <L(R*zeta),e_(k,u)>
          =sum_(j=0)^k h_j*conjugate(beta_(k-j))
          =(E_u^*h^(M))_k.

This proves the response formula, including all conjugations and
the normalization 1/R. Each grid factor of B_u(x) has modulus at
most one, since |x|<R and |t_j*u|<R. Thus |B_u(x)|<=1.
The geometric-series norm of 1/(R*zeta-a) is
1/sqrt(U-|a|^2)<=1/sigma. The triangle inequality in H^2_-
therefore gives ||h^(M)||<=||h||<=M/sigma. Consequently

    ||y_u+c^(M)(u)||<=tau_n                              (9)

at every angle. This costs the entire correction without assuming a
sign or reusing an insufficient lower bound for the recovered response.

All functions involved are continuous in u; G_u^(-1) is continuous
and uniformly bounded by (1). Apply the triangle inequality in the
Hilbert space L2(du;C^M) to (9), then the integrated inequalities in
(2). This gives exactly (3). No maximum is interchanged with a mean,
and the spatial moments c_0,...,c_(M-1) are not the first M grid
coefficients in C645y.

The anchor a=x has W_x=1 and r_x>=1. Its single diagonal contribution
is at least 1/(U-x^2)=64/21. Using M<=n/3 in tau_n now proves (4).
The comparison is uniform because its right side depends only on n.
For completeness, if S_n>=c'*exp(-n/16)*D_single,n uniformly beyond
an onset, (4) makes tau_n at most half its guaranteed square-root
lower bound beyond another uniform onset. The lower inequality (3)
then yields J_n>=c'/4*exp(-n/16)*D_single,n.
Conversely, (3) gives

    sqrt(S_n)>=sqrt(1-epsilon_n^2)*sqrt(J_n)-tau_n.

If J_n has the asserted uniform bound with constant c, use (1) and
(4) to obtain S_n>=5*c/52*exp(-n/16)*D_single,n beyond a uniform
onset. This proves the qualified equivalence, not either premise.

### 5. Close-pair normalization and verification limits

For the admissible pair in L650, its two polynomials are
(R*zeta-a)/(x-a) and (R*zeta-x)/(a-x). They add to 1.
Additivity of s -> P_+(b_u Js) therefore gives d_x+d_a=d_0.
Because beta_0=0, b_u/zeta is analytic and has boundary norm one;
its negative part is zero. Formula (2) gives y_0=-c_0, which is
exactly -(1+W_a)/R on this pair. This verifies (5) with the same
angle and spatial normalization. It does not infer a general lower
bound from this example.

The exact finite check
`python3 scripts/one-sided-hankel/joint-polynomial-gram-check.py`
saves its full certificate to
`scripts/one-sided-hankel/joint-polynomial-gram-check.json`.
It reconstructs every d_k and F from their values on all n grid
points using C645y's complete inverse grid Gram matrix, independently
of the low-coefficient Gram and response formulas above. Six admissible
Gaussian-rational cases cover n=5,6,9,10,12, degrees M=1,2,3,4,
repeated original residues, nonsymmetric pole sets, the close pair
and real, imaginary and oblique rotations. All 102 exact checks passed:
every Gram/response difference and full-energy difference is zero,
and the stated finite norm comparisons hold. All six complete
verification objects were inspected, not only a preview or aggregate
success flag. These checks test normalization and conjugation; the
uniform inequalities follow from the proof, not from the finite cases.

The new quantitative input is the uniform cost (1) and negligible
correction (4). Neither a pointwise nor angular lower bound for S_n
relative to D_single,n has been proved. Discarding phases, appealing
only to dimension or nonvanishing, or substituting a grid prefix would
not supply it. L650 identifies ||F_u||=||kappa_u||, so a successful
lower bound for J_n would have the intended sufficient-detector use;
actual-Xi realization and signs are still independent. Separate
critical audits of this result and its previously unaudited inputs
remain outstanding.

## Mathlib

Full matching coverage for this explicit grid, joint Gram bound and
uniform response comparison has not been checked. Supporting
Fourier/Parseval and finite-dimensional orthogonal-projection facts
are the cited standard inputs. Unknown Mathlib coverage is not evidence
of absence. No formal theorem asserting the open response estimate or
actual-Xi positivity is assumed.
