# Lemma 677: the closed-segment polynomial separator exceeds the angular cost budget

## Hypotheses

Let q>=1 be an integer, n=12q+3, J=n-1 and tau=J/n. Retain
L675's complete product and normalized angular measure, explicitly

    x=-5/4, R=11/8, U=R^2, t_j=j/n,
    B_u(a)=product_(0<=j<n) R*(a-t_j*u)/(U-t_j*a/u),
    W_a(u)=B_u(x)/B_u(a), |u|=1,
    A(a)=mean_u conjugate(psi(u))*W_a(u), |a|>tau,
    mean_u G=(1/(2*pi))*integral_(-pi)^pi G(exp(i*theta)) dtheta.

Here psi is any complex L2 function for this normalized measure.
Use the rational continuation of W at removable singularities; retain
j=0 and the denominator angle 1/u. Suppose P is a real-coefficient
polynomial of degree at most n satisfying

    A(a)=P(x/a) for every |a|>tau,
    P(0)=0, P(1)=1, P(10/11)=0,
    Re P(x/(x+i*y))>=0 for every real |y|<=9/20.

No restriction on the free Fourier modes of psi is imposed. In
particular, nonvanishing of the Taylor coefficients in L675 and the
minimum-norm subclass restriction in L676 are NOT hypotheses.

## Conclusion

Set kappa=23*sqrt(706)/605. Every such pair (P,psi) obeys

    ||psi||_2 >= 9*kappa^(n-1)/(2500*(2*n+3)),                 (1)
    log kappa > 7449/739499
              = 1/100 + 5401/73949900 > 1/100.              (2)

Consequently no absolute real C and onset can provide such pairs for
every sufficiently large n=12q+3 with ||psi||_2<=exp(n/100)*n^C.
Indeed this cost fails eventually for every pair satisfying the stated
hypotheses, for each fixed C. The obstruction covers the entire
degree-at-most-n class, not just degrees at most 3n/7 or the two-value
minimizer.

This does not exclude finite-n feasibility: L675's cubic has the values,
segment signs and exact action, at a larger cost. Nor does it exclude
nonpolynomial actions, higher-degree actions, actions without the exact
zero at 10/11, or other separators for the positive cone. It supplies
no original unit-residue H bound, support or Xi realization, or RH
conclusion. The independent conceptual audit in Section 7 verifies this
obstruction and the portions of L675 Sections 2--3 used here. It does
not audit L675's later low-degree and cubic conclusions or any broader
separator claim.

## Proof

### 1. Scope, input and all-preimage coefficient bound

Use the unchanged ready assessment
`drafts/literature/2026-11-02-inverse-parameter-polynomial-separator.md`.
The tested difference is precisely its degree-constrained polynomial
action with both values, closed-segment signs and paid angular inverse.
The unfinished proposal in
`drafts/2026-11-02-inverse-polynomial-arc-cost-working.md` is completed
here, rather than counted as a second result. L674's open-domain stop
and L676's finite sign failures are comparisons, not mathematical inputs.

Import normalized Fourier orthogonality and Parseval from A. Levitt,
*Analyse de Fourier et applications*,
[author PDF](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf),
version retrieved 2 November 2026, Theorem 1.3/Exercise 1.2 and
Theorem 1.11/Corollary 1.12, printed pp.6,8 (PDF pp.12,14), with
the completeness proof on printed p.53. This is the source already
inspected for the assessment and L675. Dividing measure by 2*pi gives
orthonormal monomials. The finite-polynomial kernel calculation below
uses this input directly; no general representation or positivity
theorem is reproved. The Yang--Xie arc characterization supplies no
paid inverse bound and is not needed for this obstruction.

In L675's notation put

    s_j=t_j/R, lambda=R/x=-11/10, s=|lambda|=11/10,
    b(v)=product_(j=1)^J (v-s_j)/(1-s_j*v)=sum_(k>=0) beta_k*v^k,
    F(u)=b(lambda*u), f(u)=conjugate(psi(u))/F(u),
    m_k=mean_u f(u)*u^k.

L675 Sections 2--3 prove, with the full product,

    W_a(u)=(x/a)*b(R*u/a)/F(u),
    |F(u)|>=(23/22)^J on |u|=1,
    p_(k+1)=beta_k*lambda^k*m_k for 0<=k<=J,                (3)

where P(w)=sum_(k=0)^J p_(k+1)*w^(k+1). For k>J the full action
also requires beta_k*m_k=0; none of those free or forced moments is
discarded in deriving the norm bound. In particular f is in L2 and

    sum_(k=0)^J |m_k|^2 <= ||f||_2^2
                        <= (22/23)^(2*J)*||psi||_2^2.       (4)

The full coefficient identity follows by uniform Taylor convergence
on compact subsets of |w|<|x|/tau, as justified in L675. It includes
w=0 by analytic extension. Every point used below has |w|<=1, so
lies strictly inside that disk; there is no boundary continuation
assumption about the exterior action.

Each s_j lies in (0,8/11). Thus b is analytic on a disk of radius
greater than one, and |b(v)|=1 for |v|=1: for real s_j the squared
moduli of v-s_j and 1-s_j*v coincide there. Its Taylor series
converges uniformly on the circle. The cited Parseval theorem gives

    sum_(k>=0) |beta_k|^2 = 1.                              (5)

Define rho=25/sqrt(706). It satisfies 0<rho<1 and s*rho>1.
For any |w|<=rho, (3), finite Cauchy--Schwarz and (4)--(5) yield

    |P(w)|
      <= |w|*(sum_(k=0)^J |beta_k|^2*(s*|w|)^(2*k))^(1/2)
                   *(sum_(k=0)^J |m_k|^2)^(1/2)
      <= rho*(s*rho)^J*(22/23)^J*||psi||_2
       = rho*kappa^(-J)*||psi||_2.                         (6)

The middle inequality uses (s*|w|)^k<=(s*rho)^J for all 0<=k<=J;
it holds even when s*|w|<1, since s*rho>1. No beta_k was divided
out, and no inverse-minimization assertion was used. Thus (6) holds
for every allowed preimage, including those outside L676's subclass.

### 2. The segment and its complementary circle arc

Let

    theta0=2*arctan(9/25), sigma=sin(theta0/2)=9/sqrt(706),
    w(theta)=(1+exp(i*theta))/2, -pi<=theta<=pi,
    Q(z)=P((1+z)/2), h(theta)=Re Q(exp(i*theta)).

For |theta|<pi the identity

    w(theta)=1/(1-i*tan(theta/2))

shows that w(theta)=x/(x+i*y) with y=(5/4)*tan(theta/2).
This is a bijection from [-theta0,theta0] to [-9/20,9/20].
Accordingly h>=0 on the whole closed central arc and h(0)=1.
On the complementary arcs theta0<=|theta|<=pi,

    |w(theta)|=cos(theta/2)<=cos(theta0/2)=rho.

At theta=+-pi, w=0 and P(0)=0, so the same bound applies there.
Equation (6) proves

    |h(theta)|<=rho*kappa^(-J)*||psi||_2
                         whenever theta0<=|theta|<=pi.    (7)

The coefficients of Q are real. Thus h is a real even trigonometric
polynomial of degree at most n. There is a real polynomial S of
degree at most n with h(theta)=S(cos theta): express each
cos(k*theta) through the recurrence T_0=1, T_1=t,
T_(k+1)=2*t*T_k-T_(k-1). This does not require any global sign for h.

### 3. A lower bound for the mass on the positive arc

Put L=1-cos(theta0)=2*sigma^2 and define

    H(phi)=S(1-L/2+(L/2)*cos phi),
    K(phi)=(1+cos phi)*H(phi).

As phi varies, the argument of S lies in [cos(theta0),1], where
S is nonnegative. Hence K is nonnegative on the full circle. It is
an even real trigonometric polynomial of degree at most n+1, and
K(0)=2. Write K=sum_(|j|<=n+1) k_j*exp(i*j*phi). Orthogonality
and nonnegativity imply

    |k_j|=|mean_phi K(phi)*exp(-i*j*phi)|<=mean_phi K=k_0.

Therefore 2=K(0)<=sum |k_j|<=(2*n+3)*k_0. In particular

    integral_0^pi K(phi) dphi=pi*k_0>=2*pi/(2*n+3).        (8)

To relate this to the required arc, use the monotone substitution

    theta(phi)=2*arcsin(sigma*sin(phi/2)), 0<=phi<=pi.

It maps [0,pi] onto [0,theta0], and
cos theta(phi)=1-L/2+(L/2)*cos phi. Since 0<sigma<1,

    theta'(phi)=sigma*cos(phi/2)/sqrt(1-sigma^2*sin(phi/2)^2)
                >=sigma*cos(phi/2)
                >=(sigma/2)*(1+cos phi).                  (9)

All denominators are strictly positive even at the endpoints. The
derivative is continuous, positive for 0<=phi<pi, and zero at phi=pi,
so the usual substitution is valid. Multiply
(9) by H(phi)>=0 and use (8):

    integral_0^theta0 h(theta) dtheta
      =integral_0^pi H(phi)*theta'(phi) dphi
      >=(sigma/2)*integral_0^pi K(phi) dphi
      >=pi*sigma/(2*n+3).

Evenness now gives the normalized positive-arc mass bound

    (1/(2*pi))*integral_(-theta0)^theta0 h(theta) dtheta
                         >=sigma/(2*n+3).                (10)

This mass estimate is uniform over all polynomials in the hypotheses.
It does not replace the sign condition with finitely many samples or
assume a norm bound for P on the positive arc.

### 4. The prescribed zero balances the two arcs

Let alpha=9/11. Then Q(alpha)=P(10/11)=0. The explicit kernel

    D_alpha(theta)=(1-alpha^2)/(1-2*alpha*cos theta+alpha^2)
                  =1+2*sum_(j>=1) alpha^j*cos(j*theta)

has an absolutely uniformly convergent Fourier series because alpha<1.
For this finite polynomial Q(z)=sum_(k=0)^n q_k*z^k with real q_k,
termwise integration and orthogonality give directly

    mean_theta D_alpha(theta)*h(theta)
       =sum_(k=0)^n q_k*alpha^k=Q(alpha)=0.                (11)

This is the finite-polynomial Poisson identity with all its interchanges
justified. The pointwise kernel bounds are

    1/10=(1-alpha)/(1+alpha)<=D_alpha(theta)
                                  <=(1+alpha)/(1-alpha)=10.

On the central arc h>=0. Equations (10)--(11) imply that its weighted
mass is at least sigma/(10*(2*n+3)), and is exactly the negative
of the complementary weighted mass. The latter has absolute value
at most 10*rho*kappa^(-J)*||psi||_2 by (7), since the complementary
arcs have normalized measure at most one. Consequently

    sigma/(10*(2*n+3))<=10*rho*kappa^(-J)*||psi||_2.

As sigma/rho=9/25, this is (1). In particular the zero forces enough
negative mass away from the positive arc to contradict a too-small
inverse norm. No sign was imposed on the complement.

### 5. Strict exponential margin and route consequence

The exact square of the base is

    kappa^2=373474/366025>1,
    z=(kappa^2-1)/(kappa^2+1)=7449/739499 in (0,1).

The elementary logarithm expansion used in L675 gives

    log kappa=(1/2)*log((1+z)/(1-z))
              =sum_(r>=0) z^(2*r+1)/(2*r+1)>z.

Subtracting 1/100 from z gives 5401/73949900>0, proving (2).
For any fixed real C, (1)--(2) imply

    log(||psi||_2/(exp(n/100)*n^C))
      >= log(9/2500)+(n-1)*log kappa-log(2*n+3)-n/100-C*log n
      > (5401/73949900)*n-C*log n-log(2*n+3)
                                      +log(9/2500)-log kappa
      -> infinity.

The limit holds along the allowed n=12q+3. It proves the claimed
uniform obstruction, without inferring asymptotics from finite tests.
The bound settles the approved degree/zero-constrained target negatively.
Changing the polynomial degree or abandoning the exact zero changes
the target and needs separate assessment; these possibilities are not
excluded by this proof. Historical disk and low-degree stops keep
their own narrower hypotheses.

### 6. Arithmetic evidence and verification limits

Run `python3 scripts/one-sided-hankel/polynomial-arc-cost-check.py`.
It saves exact rational checks for the arc endpoint, kernel bounds,
cost base, normalization prefactor and strict rate margin to
`scripts/one-sided-hankel/polynomial-arc-cost-check.json`. The complete
check list and selected rate evidence are inspected. These checks
support the constants; they do not establish the analytic proof of
(3)--(11), the uniform quantifiers or the input L675. Those essential
claims are separately checked in Section 7.
No numerical sampling or finite-degree experiment is used as proof
of a continuum sign or asymptotic claim.

### 7. Independent conceptual audit — 2 November 2026, step 54

The invocation-start approved assessment is
`drafts/literature/2026-11-02-polynomial-arc-cost-audit.md`.
This audit reconstructed the argument from the displayed full product,
L666 Section 2 and L675 Sections 2--3, rather than assuming the
construction's certificate verified its analysis. The primary Fourier
reading recorded in the assessment was reused; no new external theorem
or mathematical hypothesis is needed. The result is a verified local
class exclusion with the same bound, not a stronger bound or another
discovery of the obstruction.

**Full action and arbitrary preimages.** Dividing the j=0 factors gives
x/a. For each remaining j, dividing the two factors of b at R*u/a
and R*u/x gives exactly
((x-t_j*u)/(a-t_j*u))*((U*u-t_j*a)/(U*u-t_j*x)).
Thus no reflected pole, denominator angle or factor has been removed.
The Taylor radius R/tau of b exceeds |lambda|. For a compact disk
|w|<=r<|x|/tau, one has |lambda|*r<R/tau, proving uniform
convergence jointly in w and u. Since f is L2 on a probability space,
it is L1, so coefficient extraction under the integral is justified.
The moment m_k is the Fourier coefficient at index -k. Bessel's
inequality applies to these distinct indices even if all the other
indices remain free. If beta_k=0 then p_(k+1)=0; no division by that
coefficient is required anywhere in this proof. The infinitely many
coefficient constraints above degree n are not replaced by finite
interpolation or by a minimum-norm assertion.

To check the bound making f square-integrable, set h=t_j/R and
s=11/10. Here 0<h<8/11<1/s. The squared modulus of each factor
has derivative with respect to cos(arg z) of the sign of
(s^2-1)*(1-h^2), hence its minimum occurs at z=-s. The logarithm
of that minimum is convex because
s*(s+h)>1+s*h. The average h is exactly
(J+1)/(2*n*R)=4/11. Finite convexity therefore gives the stated
pointwise lower bound (23/22)^J on F. This proves both the existence
of the L2 quotient and its norm inequality for every preimage.
These are the L675 input claims certified by this audit; its later
degree/cubic applications have not been separately audited here.

**Complementary arc and positive mass.** Every factor of b has modulus
one on the unit circle, and b is analytic past that circle. Normalized
Parseval therefore gives exactly sum |beta_k|^2=1. Since
(s*rho)^2=3025/2824>1, every weight with 0<=k<=n-1 is at most
(s*rho)^(n-1), including at w=0. Finite Cauchy--Schwarz proves (6)
uniformly for |w|<=rho. All these points belong to the open action
disk, because rho<1<|x|/tau.

The segment/circle identity uses y=(5/4)*tan(theta/2), with the
positive sign appropriate to x=-5/4. Thus neither endpoint nor either
half of the complement is lost. Real coefficients make h even; the
Chebyshev recurrence gives degree at most n for S, hence at most n+1
for K. Since K>=0 and K(0)=2, its 2*n+3 possible Fourier
coefficients yield mean K>=2/(2*n+3). On [0,pi] the substitution
has denominator at least sqrt(1-sigma^2)>0. Its derivative is
continuous and nonnegative, with only the far endpoint equal to zero;
the change of variables does not require a differentiable inverse
there. The inequality cos(phi/2)>=cos(phi/2)^2 gives precisely
theta'>=(sigma/2)*(1+cos phi). Nonnegativity of H permits
multiplication. Evenness and division by 2*pi then give
sigma/(2*n+3) in (10), with no omitted factor of two.

**Prescribed-zero balance and quantifiers.** At alpha=9/11 the circle
map has value 10/11. The absolutely uniformly convergent kernel series
can be integrated against the bounded finite polynomial h; orthogonality
gives q_0+sum_(k>=1)q_k*alpha^k, with no factor of two on the
nonconstant terms. This is Q(alpha)=0. The kernel bounds 1/10 and
10 apply on the entire circle. The central weighted integral is
nonnegative and at least sigma/(10*(2*n+3)); the complementary
integral is its negative, even though h may have either sign there.
Bounding the complement by its absolute supremum and normalized
measure at most one gives exactly (1), since sigma/rho=9/25.

The existing arithmetic script was replayed. All 15 checks, the empty
failure list and the complete cost-bound field were inspected in
`scripts/one-sided-hankel/polynomial-arc-cost-check.json`.
The exact rate lower bound is 7449/739499, exceeding 1/100 by
5401/73949900. The logarithm series is strictly greater than its
first term because its argument is positive. For every fixed real C,
the positive linear margin in n dominates both C*log n and
log(2*n+3); the prefactor and n-1 shift are fixed constants.
The lower bound is uniform over all eligible pairs for each n, so
the eventual exclusion is not merely a statement about one selected
sequence or about sampled degrees.

No invalid implication was found in the audited chain. Construction
under these exact constraints is parked. Rational/nonpolynomial
actions, changed degree or interpolation requirements, and the general
cone/H/support/Xi questions remain outside the conclusion. There is
no candidate proof or disproof of RH.

## Mathlib

Full matching coverage for this product-specific polynomial obstruction
and the displayed positive-arc mass estimate has not been checked.
Fourier orthogonality and Parseval are imported from the precise inspected
source above. The proof otherwise uses finite polynomial algebra,
Cauchy--Schwarz, an explicit differentiable substitution and absolutely
convergent scalar series. No unverified Mathlib identifier or claim
of absence is made. The bounded literature search did not establish
coverage of this combination; no priority or certified novelty is claimed.
