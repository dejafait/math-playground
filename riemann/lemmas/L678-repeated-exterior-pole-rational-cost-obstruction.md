# Lemma 678: repeated exterior-pole rational separators exceed the angular budget

## Hypotheses

Let q>=1 be an integer, n=12q+3, J=n-1 and tau=J/n. Keep the
complete product and normalized angular measure from L666:

    x=-d=-5/4, R=11/8, U=R^2=121/64, t_j=j/n,
    B_u(a)=product_(0<=j<n) R*(a-t_j*u)/(U-t_j*a/u),
    W_a(u)=B_u(x)/B_u(a), |u|=1,
    A(a)=mean_u conjugate(psi(u))*W_a(u), |a|>tau,
    mean_u G=(1/(2*pi))*integral_(-pi)^pi G(exp(i*theta)) dtheta.

Use the rational continuation of W at removable singularities of the
quotient. Let psi be any complex L2 function for this normalized
measure. Suppose a real number r and a real polynomial N satisfy

    0<r<4*tau/5, deg N<=n, P(w)=N(w)/(1-r*w)^n,
    A(a)=P(x/a) for every finite |a|>tau,
    P(0)=0, P(1)=1, P(10/11)=0,
    Re P(x/(x+i*y))>=0 for every real |y|<=9/20.

The pole is outside |w|<d/tau. Cancellation of any or all denominator
factors is allowed. No nonvanishing Taylor coefficient, chosen inverse,
restriction on free Fourier modes, or positivity on an open domain is
assumed. No displacement vector or original-residue sum is a hypothesis.

## Conclusion

Put

    gamma=94502611/8000000000=0.011812826375,
    B=19680067/8000000=2.460008375.

The full original product obeys the auxiliary uniform estimate

    |W_(x+i*y)(u)| <= exp(B-gamma*n)
                   for |y|>=9/20 and |u|=1.                 (1)

Every pair (P,psi) in the hypotheses therefore satisfies

    ||psi||_2 >= exp(gamma*n-B)/(300*(2*n+3)),                (2)
    gamma-1/100=14502611/8000000000>0.                       (3)

For every fixed real C, the ratio of the right side of (2) to
exp(n/100)*n^C tends to infinity along n=12q+3. The bound is uniform
over all allowed r, numerators, cancellations and preimages. Thus the
approved repeated-pole rational family cannot meet the required
rate-1/100 inverse budget for all sufficiently large allowed n.

This is an audited local class obstruction, not a verified RH result
or a claim of certified originality. The independent conceptual audit
in Section 7 verifies the stated bound and its uniform scope. It does
not exclude arbitrary analytic
segment-positive actions, changed pole/degree configurations or actions
without the prescribed zero. The general cone, original unit-residue H,
support, realization and actual-Xi mixed signs remain open. The proof
does not solve the rational range problem; a necessary bound applying
to every existing preimage suffices for this negative answer.

## Proof

### 1. Scope, sources and strategy

Use the invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-repeated-exterior-pole-rational-separator.md`.
The exact rational target and all its uniform quantifiers are unchanged.
L677's polynomial exclusion is not applied to an infinite Taylor tail.
Instead, the full L666 product gives (1); a Mobius change of variable
removes the repeated pole and permits L677's positive-arc mass
calculation with a different endpoint. That endpoint specialization is
justified below. Neither the restricted inverse in L676 nor the
open-domain positivity conclusion in L674 is used.

Import normalized scalar Fourier orthogonality from A. Levitt,
*Analyse de Fourier et applications*,
[author PDF](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf),
version retrieved 2 November 2026, Theorem 1.3/Exercise 1.2, printed
p.6 (PDF p.12), as inspected in the reused assessment. The related
Parseval coverage is Theorem 1.11/Corollary 1.12, printed p.8, but
only orthogonality and elementary integral inequalities are needed
here. Finite polynomial algebra and one absolutely uniformly convergent
geometric Fourier series justify the uses below. No general Fourier,
rational coefficient or rational Bernstein theorem is reproved.
The assessed general coefficient and pole-sensitive norm results do
not provide these product-specific constants; this is the identified
specialization requiring proof.

### 2. A bound for each full product factor

Write y0=9/20 and Delta=U-d^2=21/64. L666 Section 2 gives

    W_a(u)=(x/a)*product_(j=1)^J V_(t_j)(a,u),
    V_t(a,u)=((x-t*u)/(a-t*u))*((U*u-t*a)/(U*u-t*x)).   (4)

This includes j=0 and the denominator angle 1/u. For a=-d+i*y,
|y|>=y0 and u=c+i*s, c^2+s^2=1, put

    A_t=d^2+t^2+2*d*t*c,
    B_t=U^2+d^2*t^2+2*U*d*t*c,
    D_t=A_t+y^2-2*t*y*s=|a-t*u|^2.

For 0<=t<=1 all denominators below are strictly positive:
|a|>=sqrt(d^2+y0^2)>1 and U>d. Direct squared-modulus algebra gives

    |V_t|^2=A_t*(B_t+t^2*y^2-2*U*t*y*s)/(B_t*D_t),
    1-|V_t|^2=(U-t^2)*y^2*L_t/(B_t*D_t),
    L_t=U+t^2+2*d*t*c-2*t*(Delta/y)*s.                (5)

These identities retain every factor and are valid for either sign
of y, including when the numerator of V_t vanishes.
Cauchy--Schwarz for the real pair (c,s) proves

    L_t >= U+t^2-2*t*sqrt(d^2+Delta^2/y^2)
        >= U+t^2-2*K*t =: g(t), K=29/20.              (6)

The latter upper choice of K is justified by the exact margins

    K^2-d^2-Delta^2/y0^2=479/57600>0,
    d^2+y0^2-(53/40)^2=3/320>0,
    (133/100)^2-d^2-y0^2=39/10000>0.                 (7)

Set a_-=53/40 and a_+=133/100. The function g is decreasing on
[0,1], since g'(t)=2*t-29/10<0. Suppose 0<=l<=t<=h<=1.
If g(h)>=0, all terms used as lower bounds in (5) are nonnegative.
The bounds B_t<=(U+d*t)^2 and D_t<=(sqrt(d^2+y^2)+t)^2,
together with (6), give

    1-|V_t|^2 >= y0^2*(U-h^2)*g(h)
                       /((U+d*h)^2*(a_++h)^2) =: d_(l,h). (8)

For clarity, z/(sqrt(d^2+z^2)+t) increases for z>0: its derivative
has numerator d^2/sqrt(d^2+z^2)+t>0. Consequently the factor
y^2/(sqrt(d^2+y^2)+t)^2 is bounded below by its value at |y|=y0.
Then sqrt(d^2+y0^2)<a_+ and t<=h bound its denominator from above.
Also U-t^2>=U-h^2 and g(t)>=g(h). These sign-preserving operations
prove (8) uniformly for the entire unbounded y range.

If g(h)<0, the following excess estimate suffices:

    |V_t|^2 <= 1+Delta*(U-l^2)*(-g(h))
                       /((U-d*h)^2*(a_--h)^2) =: 1+e_(l,h). (9)

To prove it, first consider y^2>=Delta. Then the square root in
(6), before replacing it by K, is at most sqrt(d^2+Delta)=R.
Thus L_t>=(R-t)^2>0 and |V_t|^2<=1. For y^2<Delta, if
L_t>=0 the same conclusion holds. Otherwise -L_t<=-g(t)<=-g(h),
U-t^2<=U-l^2, and y^2<Delta. The positive denominator in (5)
has the uniform lower bound

    B_t*D_t >= (U-d*t)^2*(|a|-t)^2
             >= (U-d*h)^2*(a_--h)^2>0.

This proves (9). No assertion of contraction for the final grid
points is hidden: their possible excess is explicitly paid.

### 3. Exact partition constants and the uniform n error

Partition (0,1] into m=200 intervals I_i=((i-1)/m,i/m]. Put
l_i=(i-1)/m and h_i=i/m, and use a fixed integer scale S=10^8.
For every i with g(h_i)>=0, define

    d_i=floor(S*d_(l_i,h_i))/S, e_i=0.

For every other i define

    d_i=0, e_i=ceil(S*e_(l_i,h_i))/S.

All quantities in these definitions are explicit rational numbers.
The exact arithmetic certificate verifies 0<=d_i<1, e_i>=0,
the indicated rounding directions, and the complete sums

    S*sum_i d_i=482257365,
    S*sum_i e_i=9744310.                              (10)

Its reproducible command is

    python3 scripts/one-sided-hankel/repeated-pole-rational-cost-check.py

The script uses Python's integer Fraction arithmetic, saves all 200
interval endpoints, exact unrounded constants and rounded integers to
`scripts/one-sided-hankel/repeated-pole-rational-cost-check.json`, and
checks each row before summing. Equation (10) is a finite rational
calculation, not an extrapolation or a floating quadrature. The full
algorithm and row data remain available for replay. Decimal output is
display-only; (7)--(10) and the strict comparison below are exact.

By (8)--(9), the elementary inequalities sqrt(1-v)<=exp(-v/2)
for 0<=v<1 and sqrt(1+v)<=exp(v/2) for v>=0 imply

    |V_t|<=exp((-d_i+e_i)/2) for t in I_i.            (11)

Let N_i count the actual points t_j=j/n, 1<=j<=n-1, in I_i.
For i<m it equals floor(n*i/m)-floor(n*(i-1)/m).
For i=m it equals n-1-floor(n*(m-1)/m). Hence, including the
last interval and for every n, even n<m,

    n/m-1 <= N_i <= n/m+1.                           (12)

The j=0 factor in (4) has modulus d/sqrt(d^2+y^2)<=1.
Multiplying (11) and using (12) with the correct signs yields

    |W_a(u)| <= exp((-sum_i d_i*N_i+sum_i e_i*N_i)/2)
              <= exp(B-gamma*n),
    gamma=(sum_i d_i-sum_i e_i)/(2*m),
    B=(sum_i d_i+sum_i e_i)/2.                        (13)

Substitution of (10) gives exactly the constants in the conclusion
and proves (1). Possible zero product factors still satisfy (11), so
no logarithm of a zero was taken. The argument covers every angle,
every allowed n and both unbounded complementary rays. It is not a
Taylor cutoff or an estimate on a selected subspace of preimages.

Normalized Cauchy--Schwarz now gives, for every psi in the hypotheses,

    |A(x+i*y)| <= ||psi||_2*exp(B-gamma*n), |y|>=y0.   (14)

### 4. Remove the rational pole without deleting the tail

Make the exact Mobius change

    v=(1-r)*w/(1-r*w), w=v/(1-r+r*v).

Writing N(w)=sum_(l=0)^n a_l*w^l with zero coefficients above its
actual degree gives the real polynomial

    T(v)=(1-r)^(-n)*sum_(l=0)^n a_l*v^l*(1-r+r*v)^(n-l). (15)

It has degree at most n. Where the substitution is defined,
T(v)=P(v/(1-r+r*v)); (15) extends it across any removable
substitution singularity. This identity holds with all cancellations
retained, even if the original pole cancels entirely. In particular

    T(0)=0, T(1)=1,
    T(v0)=0, v0=10*(1-r)/(11-10*r).                   (16)

For v(theta)=(1+exp(i*theta))/2 and |theta|<pi,

    v(theta)=1/(1-i*tan(theta/2)),
    w(theta)=v(theta)/(1-r+r*v(theta))
            =1/(1-i*(1-r)*tan(theta/2)),
    x/w(theta)=x+i*d*(1-r)*tan(theta/2).              (17)

The denominator 1-r+r*v on this circle has positive real part,
since r<4/5 and Re v>=0. Thus there is no boundary singularity.
Let

    theta_r=2*arctan(9/(25*(1-r))),
    sigma_r=sin(theta_r/2),
    Q(z)=T((1+z)/2), h(theta)=Re Q(exp(i*theta)).

Equation (17) maps the whole central arc |theta|<=theta_r to the
entire prescribed segment, including its endpoints. Accordingly
h>=0 there and h(0)=1. The complement theta_r<=|theta|<pi
maps to |y|>=y0. Its points have |a|>=d>tau, so the assumed exact
action and (14) give

    |h(theta)|<=||psi||_2*exp(B-gamma*n) on the complement. (18)

At theta=+-pi one has v=w=0 and T(0)=0; (18) holds there directly.
There is no assertion of an action at a finite forbidden parameter or
an unproved interchange at infinity. The infinite rational Taylor tail
has not been truncated: (15)--(18) are exact identities for P itself.

### 5. Positive mass and the prescribed-zero balance

Here h is an even real trigonometric polynomial of degree at most n.
L677 Section 3 supplies the finite Fourier mass calculation; the
following verifies it for the changed endpoint theta_r. Write
h(theta)=S_0(cos theta), with deg S_0<=n, and L=1-cos theta_r.
Define

    H(phi)=S_0(1-L/2+(L/2)*cos phi),
    K_0(phi)=(1+cos phi)*H(phi).

The polynomial K_0 is nonnegative on the full circle, is even, has
trigonometric degree at most n+1, and K_0(0)=2. Each Fourier
coefficient has modulus at most mean K_0 by nonnegativity and
orthogonality. Evaluating the finite Fourier sum at zero therefore
gives mean K_0>=2/(2*n+3).
The substitution theta(phi)=2*arcsin(sigma_r*sin(phi/2)) maps
[0,pi] onto [0,theta_r] and satisfies

    theta'(phi)=sigma_r*cos(phi/2)
                   /sqrt(1-sigma_r^2*sin(phi/2)^2)
                >=(sigma_r/2)*(1+cos phi).

Since 0<sigma_r<1, this derivative is continuous on the closed
interval, with strictly positive denominator. Multiplication by
H>=0 and ordinary substitution, followed by evenness, proves

    mean_theta 1_(|theta|<=theta_r)*h(theta)
                      >=sigma_r/(2*n+3).             (19)

No global positivity of h was assumed. Since 0<r<4/5,

    sigma_r>=9/sqrt(706)>1/3,
    alpha=2*v0-1=(9-10*r)/(11-10*r) in (1/3,9/11).    (20)

The first strict inequality follows from 729>706; the second range
follows by differentiating the displayed fractional linear function,
or direct cross multiplication with positive denominators.
By (16), Q(alpha)=0. The Poisson kernel

    D_alpha(theta)=(1-alpha^2)/(1-2*alpha*cos theta+alpha^2)
                 =1+2*sum_(k>=1) alpha^k*cos(k*theta)

has an absolutely uniformly convergent series and obeys
1/10<=D_alpha<=10 uniformly in every allowed r. Since Q is a
finite real-coefficient polynomial, the imported Fourier orthogonality
and this uniform convergence give exactly

    mean_theta D_alpha(theta)*h(theta)=Q(alpha)=0.    (21)

Thus the nonnegative central weighted mass is at least
sigma_r/(10*(2*n+3)) by (19), and equals the negative of the
complementary weighted mass. Equations (18) and (21) bound the
absolute value of the latter by 10*||psi||_2*exp(B-gamma*n).
Rearranging and using sigma_r>1/3 proves (2). All endpoint sets
have zero measure; their signs and pointwise bounds were nevertheless
included above. Every use of an infinite series was justified; no
Fourier coefficient of the angular inverse was divided out.

### 6. Quantifiers, evidence and remaining work

For every fixed real C, (2)--(3) give

    log(||psi||_2/(exp(n/100)*n^C))
      >= (14502611/8000000000)*n
                     -B-log 300-log(2*n+3)-C*log n -> infinity.

All constants are independent of r, N and psi. Hence this is the
class-wide alternative in the approved test, not a bound for a
particular construction or an n-fixed coefficient asymptotic.
No zero-beta exception or free Fourier mode can evade (14), which
uses the complete original kernel and arbitrary normalized L2 data.

The exact script checks all 200 interval constants and roundings,
the square margins, positive denominator bounds, totals, and the
actual-versus-required exponent. Its eight checks pass and its failure
list is empty. The complete aggregate, square-margin, check and failure
fields were inspected with the notebook JSON inspector. The script
does not establish the analytic steps (4)--(9) or (15)--(21), and
does not perform their independent critical review. That separate
analytic review is recorded in Section 7. The construction record remains at
`drafts/2026-11-02-repeated-pole-rational-working-56.md`.

The rational ansatz is parked under the audited hypotheses. The
negative answer does not certify an exact inverse for any
rational action, extend a finite fit to a continuum, or resolve the
general cone/H/support/Xi gaps. The argument is a family specialization
beyond what the inspected source statements supplied, not evidence of
priority or a resolution of RH.

### 7. Independent conceptual audit — 2 November 2026, step 57

Reuse the unchanged invocation-start EXPLORE assessment stated in
Section 1, including its primary Fourier coverage. This audit read
the full proof and reconstructed the factor algebra directly from
L666 Section 2. L677's positive-arc calculation and its previous audit
were compared at the new endpoint. No additional external theorem,
unproved inverse formula or positivity assumption was introduced.
This verifies the existing local exclusion; it neither improves the
bound nor constitutes another discovery of it.

**Full product and the two ray estimates.** The j=0 quotient is x/a.
Dividing every other factor with the denominator angle 1/u gives
exactly (4). On both rays, |a|>d>tau and U-t*d>=U-d>0,
so the angular function is continuous and all displayed denominators
are nonzero. In the notation of Section 2, direct cancellation gives

    B_t-t^2*A_t=(U-t^2)*(U+t^2+2*d*t*c),
    U*A_t-B_t=-Delta*(U-t^2),
    B_t*D_t-A_t*(B_t+t^2*y^2-2*U*t*y*s)
      =(U-t^2)*(y^2*(U+t^2+2*d*t*c)-2*Delta*t*y*s).

These identities prove (5) without a sign choice for y. The Euclidean
bound for (c,s) uses sqrt(d^2+Delta^2/y^2), so it covers both rays.
The positive margin in (7) permits its replacement by K. When g(h)>=0,
every numerator factor used in (8) is nonnegative; increasing positive
denominators gives a lower bound. For z=|y|, the derivative of
z/(sqrt(d^2+z^2)+t) has numerator d^2/sqrt(d^2+z^2)+t>0.
This establishes the comparison at y0 on the whole unbounded ray,
rather than just its endpoint.

When g(h)<0, split at y^2=Delta. Above that threshold,
L_t>=(R-t)^2>0 and the factor contracts. Below it, an excess can
occur only when L_t<0; then -L_t<=-g(t)<=-g(h), with
y^2<Delta and U-t^2<=U-l^2. The lower denominator bounds
U-d*h>0 and a_--h>0 are uniform for h<=1. This proves (9)
also for bins straddling the sign change of g. A vanishing numerator
factor is permitted and does not require taking its logarithm.

**Rounding, full counts and arithmetic replay.** The complete script
was inspected and replayed. Its exact Fraction loop visits every one
of the 200 intervals, computes the appropriate rational expression
in (8) or (9), and checks its directed rounding before aggregation.
The complete aggregate, square margins, eight checks and empty failure
list were inspected using the notebook JSON inspector at
`scripts/one-sided-hankel/repeated-pole-rational-cost-check.json`.
The sums in (10), gamma and B agree exactly with the displayed values.
There is no floating input in these calculations.

For i<200 the floor difference counts exactly the integers
n*(i-1)/200<j<=n*i/200. The final bin omits j=n, so its count
is ceil(n/200)-1. Thus (12) holds even when n<200 or a bin
endpoint is an actual grid point. Applying its lower bound to the
negative terms -d_i*N_i and its upper bound to the positive terms
e_i*N_i yields (13) with the stated signs and constant B. The j=0
modulus is at most one. Consequently (1) holds for every n in the
hypotheses, angle and complementary ordinate. Normalized
Cauchy--Schwarz proves (14) for every L2 preimage. Neither a zero
Taylor coefficient nor a free Fourier mode alters this inequality.

**Exact substitution and endpoint control.** For
w=v/(1-r+r*v), one has 1-r*w=(1-r)/(1-r+r*v).
Multiplying out gives (15) term by term even after pole cancellation.
Since 0<r<4*tau/5<4/5, its constant denominator is nonzero.
The boundary substitution denominator has real part at least 1-r>0.
Hence T is a real polynomial of degree at most n, with all three
values in (16). There is no loss of an infinite Taylor tail.

In (17) the ordinate is +d*(1-r)*tan(theta/2), with the sign
fixed by x=-d. This maps both halves of the central closed arc onto
the required segment and both open complementary arcs onto the rays.
Every finite image has |a|>=d>tau. At the two circle endpoints
theta=+-pi, T(0)=P(0)=0 supplies the bound directly, so no action
at infinity is assumed. The proof therefore establishes (18) on the
entire complement with its endpoints.

**Mass, zero and uniformity.** The real coefficients make h even.
Its representation as S_0(cos theta) has degree at most n.
The argument of S_0 defining H ranges over [cos theta_r,1],
so H and K_0 are nonnegative on the full circle. Orthogonality
and nonnegativity give |hat K_0(k)|<=mean K_0 for all k.
The at most 2*n+3 Fourier terms and K_0(0)=2 prove the
stated lower mean. In the substitution of Section 5,
cos(phi/2)>=cos(phi/2)^2 and the square-root denominator is
at most one. Thus its derivative is at least
sigma_r*(1+cos phi)/2. It is continuous up to both endpoints
and nonnegative, so substitution against H>=0 is valid.
Evenness and division by 2*pi give exactly (19), without an extra
factor of two. Uniformity does not require a bounded inverse derivative.

The parameter interval gives sigma_r>1/3 and 1/3<alpha<9/11.
Therefore the Poisson kernel lies between 1/10 and 10 on the
whole circle. Its geometric Fourier series is uniformly absolutely
convergent (indeed alpha<=9/11), and h has only finitely many
Fourier modes. Orthogonality gives Q(alpha)=0 in (21), retaining
the constant coefficient and the correct factors on the other terms.
The central weighted integral is at least
sigma_r/[10*(2*n+3)] and is the negative of the complementary
integral. Bounding the latter using (18) and normalized measure at
most one gives (2). No sign is imposed on the complement.

Finally gamma-1/100=14502611/8000000000 is strictly positive.
For every fixed real C its linear contribution in n dominates
C*log n, log(2*n+3) and the fixed constants in Section 6.
All constants are independent of r, N and psi, including when these
vary with n. This is the required eventual class-wide exclusion,
not a fixed-function asymptotic or a finite-degree extrapolation.

No failed implication was found in this audited chain. Only the exact
repeated-pole family is excluded. The general segment-positive action,
cone/H/support/Xi realization and all-degree mixed positivity remain
unresolved. Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage of this product-specific complementary-ray bound
and rational-class obstruction has not been checked. Fourier
orthogonality is imported from the precise inspected source above;
the remaining analytic ingredients are finite algebra, elementary
Cauchy--Schwarz and substitution, and an explicitly convergent geometric
series. The constant certificate uses exact integer rational arithmetic.
No unverified Mathlib identifier or claim of absence is made.
