# Corollary C032n: normalized Gaussian-width evolution of the odd kernel

## Hypotheses

Retain C032j/k/m's actual divisor, multiplicities and fixed-v1 source
qualifications. In particular z_rho=gamma_rho-i*delta_rho,
gamma_rho>14, |delta_rho|<1/2, and N(T)=O(T log(T+2)), counting
multiplicity. The divisor is invariant under conjugation. Use exactly

    G_sigma(z)=(4*pi*sigma)^(-1/2)*exp(-z^2/(4*sigma)),
    p_sigma(z)=(1/2)*sum_rho [G_sigma(z-z_rho)+G_sigma(z+z_rho)],
    R_sigma(w)=integral_0^infinity
                   (p_sigma(x)-p_sigma(i*w))/(x^2+w^2) dx,
    E_sigma(w)=4*integral_0^w t*R_sigma(t) dt,
    O_sigma(w)=2*pi*integral_0^w p_sigma(i*t) dt,
    b_sigma=E_sigma+O_sigma,
    K_sigma=exp(-E_sigma)*sinh(O_sigma).

The spatial quotient takes its continuous removable values, and the
primitives vanish at zero. Width sigma is Gaussian half-variance, not
standard deviation. Conclusions concern sigma in [1,2], with derivatives
defined on the positive-width neighborhood (1/2,3). A prime denotes
complex differentiation in w, except p',p'' denote differentiation in
its own complex argument. No RH, pointwise profile positivity, or
coefficient-span completeness is assumed. The inherited source inputs
are not independently reverified here; their heat positivity and
probability interpretation are not used in the calculation.

## Conclusion

All the displayed functions are continuously differentiable in sigma
and entire in their complex argument on this neighborhood, with joint
continuity and bounds uniform on [1/2,3] times each complex disk.
The same statements hold for every fixed complex derivative of the
functions and of their first sigma derivatives. The differentiated
spatial integral has an integrable common majorant on each disk.
In particular both width endpoints 1 and 2 are interior points of the
justified parameter interval. Put a_sigma=E_sigma''(0)=4*R_sigma(0).
Then

    partial_sigma p_sigma(z)=p_sigma''(z),                       (1)
    partial_sigma b_sigma(w)=-b_sigma''(w)+a_sigma,
    partial_sigma E_sigma(w)=-E_sigma''(w)+a_sigma,
    partial_sigma O_sigma(w)=-O_sigma''(w).                      (2)

If C_sigma=exp(-E_sigma)*cosh(O_sigma), the full odd evolution is

    partial_sigma K=-K''+((E')^2+(O')^2-a_sigma)*K
                          -2*E'*O'*C.                          (3)

The companion term can be eliminated without division or singularities:

    partial_sigma K=-K''-2*E'*K'+V_sigma*K,
    V_sigma=(O')^2-(E')^2-a_sigma.                              (4)

Thus a linear PDE with prescribed variable coefficients is obtained.
It must not be reported as either a constant-coefficient heat equation
for K or a proof that no linear evolution exists.

More explicitly write the convergent entire Taylor expansions

    E_sigma(w)=sum_(j>=1) e_j(sigma)*w^(2j),
    O_sigma(w)=sum_(j>=0) o_j(sigma)*w^(2j+1),
    K_sigma(w)=sum_(n>=0) phi_n(sigma)*w^(2n+1),
    V_sigma(w)=sum_(k>=0) v_k(sigma)*w^(2k).

All coefficients are real and C^1 in sigma. With an empty sum equal to
zero and delta_(k0) the Kronecker symbol,

    v_k=sum_(r,s>=0; r+s=k) (2r+1)*(2s+1)*o_r*o_s
          -4*sum_(r,s>=1; r+s=k+1) r*s*e_r*e_s
          -2*e_1*delta_(k0),                                  (5)

    d phi_n/d sigma=-(2n+3)*(2n+2)*phi_(n+1)
       -4*sum_(j=1)^(n+1) j*e_j*(2*(n+1-j)+1)*phi_(n+1-j)
       +sum_(k=0)^n v_k*phi_(n-k).                             (6)

The equation is linear in the phi functions with coefficients determined
by E and O. It does not establish closure of their real scalar linear
span under multiplication by these coefficient functions or under
sigma differentiation. For example, c=o_0=phi_0 and e=e_1 give

    d c/d sigma=-6*phi_1+c^3-6*e*c.                            (7)

No uniform approximation of 1 on [1,2], existence or exclusion of a
mass-one signed annihilator, positive mixture, exponential moment,
unsmoothed Xi realization or actual-Xi sign is concluded. Formula (6)
leaves the specified direct approximation mechanism unresolved.

## Proof

### 1. Imported identity and the additional estimates required here

Import the one-dimensional Gaussian identity partial_sigma G=G''
from James Nolen, *Partial Differential Equations and Diffusion
Processes*, Stanford Math227 notes, Section 2.3, (3.17), P0-P1,
[printed pp.14-15](https://math.stanford.edu/~ryzhik/STANFORD/STANF227-10/notes227-09.pdf).
The Gaussian has variance 2*sigma, matching our convention. For each
positive real sigma the identity extends from real to complex arguments
by the identity theorem, since both sides are entire in that argument.
The source statement and the differentiation discussion on pp.16-17
were inspected in source assessment1532 and approval1533. The general
convolution theorem there is not applied to a complex zero divisor.
The following estimates supply precisely the needed infinite-sum,
spatial-integral and normalization checks, rather than reproving that
Gaussian identity.

For compact complex integration use Haslinger, *Complex Analysis*,
Section 2.7, [Theorem 2.39, pp.67-68](https://www.mat.univie.ac.at/~has/scriptneu.pdf),
with the coverage reused in C032m. It requires measurable sections,
holomorphy in the complex variable and an integrable dominator on each
compact disk. Real parameter differentiation below follows from
dominated difference quotients with the explicit first-derivative
majorants, not from an assertion that the complex theorem automatically
differentiates the width.

Let I=[1/2,3]. For a=0,1 and each fixed integer k>=0, differentiation
of the Gaussian formula expresses partial_sigma^a partial_z^k G_sigma(z)
as G_sigma(z) times a polynomial in z whose coefficients are bounded
on I. This polynomial claim follows inductively: a z derivative changes
P to P'-z*P/(2*sigma), and a sigma derivative changes P to
partial_sigma P+(-1/(2*sigma)+z^2/(4*sigma^2))*P. There is no negative
power of sigma unbounded on I. If z=u+i*v, |v|<=Y, the Gaussian modulus
is bounded by a constant depending on Y times exp(-u^2/12).
Absorb each fixed polynomial in u into half of that Gaussian decay.
There are therefore finite constants C_(a,k,Y) such that

    |partial_sigma^a partial_z^k G_sigma(u+i*v)|
          <=C_(a,k,Y)*exp(-u^2/24),   sigma in I, |v|<=Y.       (8)

For translates by either z_rho, replace Y by Y+1/2 and u by
u-gamma_rho or u+gamma_rho. On |z|<=M the resulting sum is bounded
by a constant times

    sum_rho exp(-(gamma_rho-M)_+^2/24)<infinity.

Indeed beyond gamma_rho>2M it is bounded by sum exp(-gamma_rho^2/96),
which converges by the stated zero count; finitely many smaller terms
cause no problem. Uniform convergence of both the Gaussian series and
its first sigma derivative justifies real parameter differentiation on
the interior of I. For example, apply the fundamental theorem of
calculus to each summand between sigma and sigma+h, and dominate the
resulting averaged derivatives by (8). Uniform convergence of the
complex derivatives, or Cauchy's formula on a larger disk, justifies
their exchanges as well. The finite Gaussian identity now sums to (1).

### 2. The differentiated spatial integral and its removable values

For x>=0 define

    P(x)=sum_rho [exp(-(x-gamma_rho)^2/24)
                    +exp(-(x+gamma_rho)^2/24)].

Equation (8) bounds p_sigma(x), p_sigma'(x), p_sigma''(x) and
partial_sigma p_sigma(x), in absolute value, by respective constant
multiples of P(x), uniformly on I. The factor 1/2 in p is absorbed
in these constants, not in the divisor or multiplicities. For X>=1,
splitting the positive-center Gaussian at x=gamma_rho/2 gives

    integral_X^infinity P(x)/x^2 dx
      <=(2/X)*sum_rho exp(-gamma_rho^2/96)
                       +4*sqrt(24*pi)*sum_rho gamma_rho^(-2)
      <infinity.                                               (9)

On X<=x<gamma/2 use exp(-(x-gamma)^2/24)<=exp(-gamma^2/96)
and integral_X^infinity x^-2 dx=1/X. On the remaining region use
x^-2<=4/gamma^2 and the full Gaussian integral sqrt(24*pi).
The negative-center translate is at most exp(-gamma^2/24)/X after
integration against x^-2. Tonelli applies to the nonnegative
majorants. Both sums in (9) converge by N(T)=O(T log(T+2)); on
dyadic intervals the inverse-square contributions are O((n+1)2^-n).
This proves an integrable envelope, not a small numerical tail bound.

Write p_sigma(z)=h_sigma(z^2). The even Taylor series and the compact
normal convergence proved above show that h_sigma and its first sigma
derivative are jointly continuous and entire in their second argument.
For detail, choose a z circle of radius r with r^2>U on |u|<=U.
Cauchy's formula bounds both sets of even Taylor coefficients by a
common constant times r^(-2n); their u series and parameter derivative
series converge uniformly geometrically. Cauchy's formula in u gives
the same properties for h_sigma'. Put dot h=partial_sigma h; then
dot h(z^2)=p_sigma''(z) by (1).

The extended spatial quotient q has the identity

    q_sigma(x,w)=integral_0^1
                   h_sigma'(-(1-v)*w^2+v*x^2) dv.              (10)

Its sigma derivative is this same integral with h replaced by dot h.
The compact v integral can be differentiated by uniform continuity
and the just-proved compact derivative bounds. In particular (10)
and its differentiated expression cover both w=+i*x and w=-i*x.
At those points their values are h_sigma'(x^2) and dot h_sigma'(x^2).
At x=w=0 these are p_sigma''(0)/2 and p_sigma''''(0)/2.
Thus no principal value or omitted origin term is present.

On |w|<=M choose X=2M+1. For 0<=x<=X, the arguments of h' and
dot h' in (10) lie in the compact disk |u|<=X^2, so both integrands
have one finite bound B_M uniform in sigma,x,w. For x>=X use
|x^2+w^2|>=3*x^2/4, (8), (9) and compact bounds for p_sigma(i*w)
and p_sigma''(i*w). With suitable finite constants A_M,D_M,

    |q_sigma(x,w)|+|partial_sigma q_sigma(x,w)|
        <=B_M,                              0<=x<X,
        <=D_M*(P(x)+A_M)/x^2,               x>=X.              (11)

This is a single integrable majorant, uniform on I and the disk.
Measurability and joint continuity follow from (10) and the normally
convergent profiles. Dominated convergence, the fundamental theorem
of calculus in sigma, and (11) therefore give

    partial_sigma R_sigma(w)=integral_0^infinity
            (p_sigma''(x)-p_sigma''(i*w))/(x^2+w^2) dx,         (12)

with the just-specified removable values. Both R and its width
derivative are entire by the cited holomorphic integration theorem.
Cauchy's formula on a larger disk gives joint continuity, uniform
bounds and interchange for every fixed complex derivative. The compact
straight-segment formulas for E and O in C032m similarly justify their
width derivatives, entire dependence, bounds and mixed derivatives.
Their normalization at zero remains exact for every width.

### 3. Spatial integration by parts and the primitive constant

The boundary terms needed next vanish uniformly on I. To see this
without assuming a uniform logarithmic-growth theorem, for x>=1 split
P(x) at gamma_rho<=2x+2. There are O((x+1)log(x+2)) such terms,
each at most one per translate. For gamma_rho>2x+2, gamma_rho-x>
gamma_rho/2 and both translated Gaussians are at most
exp(-gamma_rho^2/96). The remaining sum is bounded independently
of x. Hence

    |p_sigma(x)|+|p_sigma'(x)|
                     =O((x+1)*log(x+2))                      (13)

uniformly on I. This crude pointwise bound is used only for boundary
terms; (9), not (13), justifies the original weighted integrals.

For real w>0 put f_w(x)=w/(x^2+w^2). The definition of R and the
elementary integral integral_0^infinity dx/(x^2+w^2)=pi/(2w) give

    b_sigma'(w)=4*integral_0^infinity p_sigma(x)*f_w(x) dx.     (14)

The subtraction of p_sigma(i*w) cancels precisely with O_sigma'.
Equations (8)-(9) justify sigma differentiation of (14). On each
compact positive real w interval, f_w and its first two w derivatives
are bounded on bounded x intervals and are O(x^-2) at infinity.
Thus (9) also justifies two w derivatives under this integral.

Twice integrating by parts on a finite spatial interval, then taking
its endpoint to infinity, gives

    integral_0^infinity p_sigma''(x)*f_w(x) dx
                    =integral_0^infinity p_sigma(x)*f_w''(x) dx.

Here the primes on f_w in this display denote x derivatives.
At zero p_sigma'(0)=0 by evenness and partial_x f_w(0)=0. At
infinity (13), f_w=O(x^-2) and partial_x f_w=O(x^-3) imply
p_sigma'*f_w ->0 and p_sigma*partial_x f_w ->0. The integrals
are absolutely convergent by (8)-(9); intermediate integrals with
p_sigma' partial_x f_w also converge by those bounds. Direct
differentiation of this rational function gives

    partial_x^2 f_w(x)=(6*w*x^2-2*w^3)/(x^2+w^2)^3
                       =-partial_w^2 f_w(x).

Consequently partial_sigma b_sigma'(w)=-b_sigma'''(w) on w>0.
Both sides are entire by the preceding work, so the identity theorem
extends the equality to C. Integrating in w shows that
partial_sigma b_sigma+b_sigma'' is constant in w. Since b_sigma(0)=0
for every width, that constant is b_sigma''(0). E is even and O odd,
so O''(0)=0 and b''(0)=E''(0)=4R(0). Taking even and odd parts gives
all of (2). No arbitrary primitive constant has been discarded.

### 4. Kernel evolution, coefficient extraction and the bounded test

Suppress sigma in this paragraph. Ordinary product and chain rules
give

    K''=((E')^2+(O')^2-E'')*K+(O''-2*E'*O')*C,
    partial_sigma K=(E''-a_sigma)*K-O''*C.

Their difference proves (3). The first derivative identity
K'=-E'*K+O'*C implies E'*O'*C=E'*K'+(E')^2*K everywhere, including
zeros of O'. Substitution gives (4), with no division by O' or K.
The coefficients E' and V are prescribed entire functions, odd and
even respectively. This is genuine variable-coefficient linearity
in K even though these coefficients arise from the original nonlinear
construction.

Conjugation invariance of the actual divisor and the real Gaussian
formula make p_sigma real on the real axis. Evenness then makes
p_sigma(i*t) real for real t. The extended quotient is real for
real w,x; hence R,E,O and K have real Taylor coefficients. Joint
sigma differentiability and compact complex bounds allow coefficient
extraction and sigma differentiation to commute by Cauchy's formula.
The locally uniformly convergent entire power series permit the usual
finite convolution for each coefficient. Extracting w^(2k) from V
gives (5), and w^(2n+1) from (4) gives (6): in the E'K' product the
indices satisfy j+(n+1-j)=n+1. In particular a=2e_1,
v_0=o_0^2-2e_1 and phi_0=o_0, proving (7).

An independent low-order consistency check within the same identity is
available from the primitives. Their Taylor series give
c=2*pi*p_sigma(0), e=2*R_sigma(0),
o_1=-pi*p_sigma''(0)/3, and
phi_1=o_1+c^3/6-e*c. Equation (1) gives c'=2*pi*p_sigma''(0);
substituting the displayed phi_1 proves exactly (7), with the same
signs and origin constant. No numerical truncation is used here.

For the approximation test let S be the uniform closure in real
C([1,2]) of the real scalar span of the phi_n. The coefficients in
a linear combination defining that span are real constants, independent
of sigma. Equations (5)-(6) supply functions e_j*phi_m, v_k*phi_m and
sigma derivatives of phi_n. No established input says these operations
map S to S. Already (7) retains c^3 and e*c as well as c'; being real
continuous functions is not a membership proof for S. Conversely,
their appearance is not a proof that they lie outside S. An annihilator
of the phi_n cannot simply be differentiated in sigma or assumed to
annihilate their variable-coefficient products. An arbitrary finite
signed Borel measure need not have a differentiable density, and no
integration by parts in width has been invoked.

Thus the achieved result is (4)-(6), with every analytic exchange and
normalization retained. The required output for the proposed downstream
use would instead be finite sums sum_n alpha_n*phi_n tending uniformly
to 1. No such sequence or bound is supplied by this calculation.
The direct recursion is parked at that precise missing implication.
This is an inconclusive completeness test, not a nonclosure theorem,
nor a counterexample to RH. The source search1532 did not identify a
matching theorem for this exact nonlinear family; that is not a novelty
claim. This local identity has not received a later independent audit.

### Ordered two-point minor attempt1711, 19 November 2026 (inconclusive)

This is an attempted application of the width regularity already proved
above, under unchanged EXPLORE assessment1709 and approval1710. It does
not assert a sign theorem. Retain the full actual divisor, its
multiplicities, conjugation symmetry and all source qualifications.
Put a=1/8, b=1/4 and, for real y in [0,b], define

    A_sigma(y)=2*pi*integral_0^y p_sigma(x) dx,
    e_sigma(y)=E_sigma(i*y),
    k_sigma(y)=Im(K_sigma(i*y)),
    f(sigma)=k_sigma(a), g(sigma)=k_sigma(b).

The functions A and e are real. For A this follows from reality of p on
R; for e it follows from the real even Taylor series of E. The straight
primitive path and evenness of p give

    O_sigma(i*y)=2*pi*i*integral_0^y p_sigma(-x) dx=i*A_sigma(y),
    k_sigma(y)=exp(-e_sigma(y))*sin(A_sigma(y)).                (15)

Thus no imaginary part has been replaced by an absolute value. In
particular exp(-e)>0, but positivity of sin(A) at either specified
argument is not a consequence of (15) alone.

All width derivatives below are justified on the positive-width
neighborhood in the Hypotheses, so both endpoints 1 and 2 are included.
The heat identity (1), differentiation of the compact real integral,
and p_sigma'(0)=0 give

    partial_sigma A_sigma(y)=2*pi*p_sigma'(y).

Since partial_y^2 e_sigma(y)=-E_sigma''(i*y), (2) gives

    partial_sigma e_sigma(y)=partial_y^2 e_sigma(y)+a_sigma.

Here a_sigma=4*R_sigma(0) is the normalization constant from (2), not
the fixed argument a=1/8. Write dot for the width derivative and e_yy
for two derivatives in y. Differentiating (15) gives the exact identity

    dot k_sigma(y)=exp(-e_sigma(y))*[
        2*pi*p_sigma'(y)*cos(A_sigma(y))
        -(e_sigma,yy(y)+a_sigma)*sin(A_sigma(y))].             (16)

For the target D(s,t)=f(s)g(t)-g(s)f(t), define the diagonal quantity
W(sigma)=f(sigma)*dot g(sigma)-g(sigma)*dot f(sigma). Substitution of
(16) cancels a_sigma, without dividing by either sine. Suppressing
sigma on the right gives

    W(sigma)=exp(-e(a)-e(b))*{
        2*pi*[sin(A(a))*cos(A(b))*p'(b)
              -sin(A(b))*cos(A(a))*p'(a)]
        -(e_yy(b)-e_yy(a))*sin(A(a))*sin(A(b))}.                (17)

For s<t, the fundamental theorem of calculus, applied to f and g on
[s,t], also gives the division-free formula

    D(s,t)/(t-s)=integral_0^1 [
        f(s)*dot g(s+v*(t-s))-g(s)*dot f(s+v*(t-s))] dv.       (18)

Joint continuity of these functions proves that this expression
extends continuously to 1<=s<=t<=2, taking the value W(s) when t=s.
This is an exact identity for the complete divisor, not a truncated
or sampled approximation. It retains a factor t-s even arbitrarily
near the diagonal. A zero of W alone need not refute strictness at
strictly ordered pairs; no such inference is made.

One sufficient route to the desired sign would be to prove f never
vanishes and W<0 on [1,2]. Under those explicitly unpaid premises,
f has a constant sign by continuity and

    D(s,t)=f(s)*f(t)*integral_s^t W(u)/f(u)^2 du<0.            (19)

Indeed (g/f)'=W/f^2; integration proves the equality, and f(s)f(t)>0
proves the strict inequality. The analogous positive-W assertion is
valid. These are sufficient tests, not necessary conditions or verified
premises for this kernel. In particular p_sigma(0)>0 by the qualified
heat input only supplies positivity in a neighborhood of y=0. Even a
width-uniform neighborhood obtained by compactness has no established
radius reaching a or b.

Here is what the available modulus bounds actually yield in this test.
Use C032m's positive finite constants A_M and B_M, with
|p_sigma(z)|<=A_M and |R_sigma(w)|<=B_M on the corresponding disks.
Write

    U_y=min(1,2*pi*y*A_b),
    P=A_(b+1),
    Q=12*(b-a)*(b+1)^2*B_(b+1).

For y in [0,b], the compact integral gives |A_sigma(y)|<=2*pi*y*A_b,
so |sin(A_sigma(y))|<=U_y, while |cos(A_sigma(y))|<=1. Cauchy's
radius-one estimate for p yields |p_sigma'(y)|<=P. For the other
term, C032m gives |E_sigma(w)|<=2*(b+1)^2*B_(b+1) on |w|<=b+1.
Cauchy's estimate on the radius-one circle about i*y therefore gives

    |E_sigma'''(i*y)|<=12*(b+1)^2*B_(b+1).

Since d(e_yy)/dy=-i*E_sigma'''(i*y), integration from a to b proves
|e_sigma,yy(b)-e_sigma,yy(a)|<=Q. Finally
|e_sigma(y)|<=2*b^2*B_b. Thus (17) implies only

    |W(sigma)|<=exp(4*b^2*B_b)*[
        2*pi*P*(U_a+U_b)+Q*U_a*U_b].                         (20)

Every constant is finite and all bounds include width endpoints and
the full complex-divisor tail. However, the enclosure in (20) is
symmetric about zero; its right side is strictly positive. It does not
verify W<0, W>0, or nonvanishing of f. No finite bound here is being
treated as a signed lower margin. Similarly, an absolute error for D
that is independent of t-s would not settle the near-diagonal region.

The achieved calculation is (15)-(18) and the inconclusive estimate
(20); the required threshold is a common strict sign of D over all
1<=s<t<=2. That threshold is neither proved nor refuted. No numerical
evaluator, grid, zero-coordinate truncation, all-order inference, or
Chebyshev application was made. The prospective Chebyshev restriction
on continuous densities remains separate, as do arbitrary signed
measures, positivity of the output law, moments and actual-Xi
realization. The source comparison1709 ruled out automatic Gaussian
and nonlinear total-positivity imports; it did not prove the sign.

No additional theorem is imported for this appendix: its only
mathematical inputs are the existing C032m bounds and the width
regularity/heat identities proved in this file, followed by elementary
chain rules, Cauchy estimates and the fundamental theorem of calculus.
The exact-sign attempt is parked after this unsuccessful modulus
comparison. Reopening needs a signed quantitative estimate for (17)
and nonvanishing control, or an independent full-divisor certificate;
repeating these identities or a finite grid would add no evidence.
This appendix has not received a later independent mathematical audit.

## Mathlib

Full matching coverage is unchecked and unknown. No Mathlib theorem is
used. Gaussian differentiation, Cauchy estimates, dominated integration
and elementary power-series products would support parts; coverage of
the full qualified divisor evolution or coefficient completeness is
not asserted.
