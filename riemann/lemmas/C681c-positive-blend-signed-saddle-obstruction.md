# Corollary 681c: the two positive constructions cannot cancel their real saddle

## Hypotheses

Use L666's complete rational angular kernel W, L673's exact nodes and
positive finite-product coefficients b_a, and L681's Robin coefficients
w_a. Thus n=12q+3, q>=1, x=-d=-5/4, R=11/8, U=121/64,
h=27/(10n), rho=h/10, c=10*pi/27, r=9/20, and
a=x+-i*y_k, y_k=h*s_k, 0<=k<2q, with exactly the roots specified
in L673 (1). For any theta in [0,1], independent of the angle u, put

    v_a=(1-theta)*b_a+theta*w_a,
    T_(n,theta)(u)=W_(-R)(u)-1-sum_(a!=x) v_a*W_a(u).

The anchor remains one. The norm is continuous normalized circle L2.
Theta may depend arbitrarily on n. All factors and angular modes are
retained. Original residues in H are still one and are not replaced.

## Conclusion

There is an absolute Q such that, for every q>=Q and every theta in [0,1],

    ||T_(n,theta)||_2 >= exp(-19*n/2000).                    (1)

In particular no convex blend of these two specified constructions
has a bound n^kappa*exp(-(1/100+epsilon)*n) for all sufficiently large q,
with fixed kappa>=0 and epsilon>0. This stops this blend, including
n-dependent blend parameters; it does not exclude arbitrary positive
weights, different multipliers or different constructions. Q is
existential, not numerically evaluated.

This is a family-specific obstruction under the unchanged EXPLORE
assessment `drafts/literature/2026-11-02-discrete-parameter-positive-quadrature.md`.
It extends the preserved unfinished step-71 calculation. The separate
conceptual audit in Section 7 verifies this family-specific bound.
No originality beyond the
checked sources, original-H bound, support/realization bridge, Xi sign
or RH resolution is asserted.

## Proof

### 1. Exact contours and source scope

Write W(z)=W_(x+z)(-1). Exact substitution into L666 (6), including j=0,
gives, with t_j=j/n,

    W(z)=product_(0<=j<n)
         [(d-t_j)/(d-z-t_j)]*[(U-t_j*(d-z))/(U-t_j*d)].       (2)

This is positive for real -1/8<=z<=1/10, and has no parameter pole
on Re z<1/4. In particular W_(-R)(-1)=W(-1/8)>0.
Put P(z)=product_(0<=k<2q)(z^2+y_k^2), gamma=3/5, and

    H_b(z)=(1-z/rho)*exp(-cnz-gamma*n*z^2)*W(z)*P(0)/(z*P(z)),
    H_w(z)=K_n(z)*W(z),
    K_n(z)=C_n*(rho-z)*exp(-cnz)/[z*cosh(cnz)+rho*sinh(cnz)],
    C_n=(1+rho*cn)/rho.

The finite identities L673 (6) and L681 (5) say that
S_b=1+sum b_a W_a(-1) and S_w=1+sum w_a W_a(-1) are their respective
contour integrals divided by 2*pi*i. They remain valid with left edge
-1/8 and any right edge in (1/20,1/10). For b use height 1/2: all
P roots are inside, there are no other kernel poles, and (2) has none.
For w use Y_n=2qh=r-27/(20n): L681's imaginary-root census and exact
integer boundary phase give precisely the required poles. No other
Robin roots are added. Both contours are counterclockwise; their right
edges are traversed upwards. Conjugation makes S_b,S_w real.

The imported contour theorem is the finite Cauchy residue theorem,
NIST DLMF Section 1.10(iv), [equation (1.10.8)](https://dlmf.nist.gov/1.10#E8),
with the pole and boundary hypotheses just checked, reused from L681's
source assessment. Section 6 below uses the already inspected
Danchenko--Semin theorem. No new general quadrature or asymptotic theorem
is assumed. The family-specific signed limit is proved below because
an absolute contour estimate cannot settle cancellation.

### 2. The limiting exponents and certified scalar inequalities

On a neighborhood of -1/8<=Re z<=1/10, |Im z|<=1/2 define the analytic logarithm

    F(z)=integral_0^1 log([(d-t)/(d-z-t)]
                         *[(U-t*(d-z))/(U-td)]) dt,

real on the real interval, and write f(s)=F(s). Also put

    K(s+iy)=(10/27)*integral_(-r)^r
                       [log|t|-log|s+i*(y-t)|] dt,
    e_w(s)=f(s)-2cs,
    e_b(s)=f(s)-cs-gamma*s^2+K(s),       s>=0.

K(0)=0 by continuity. On Re z>0 its analytic counterpart is
(10/27)*integral_0^r [2*log t-log(z^2+t^2)]dt, using the analytic
logarithm real on the positive real axis; its real part is K(z).
This specifies the branches used in the derivative and Taylor estimates.
For s>0,

    K'(s)=-(20/27)*atan(r/s),
    K''(s)=(20/27)*r/(s^2+r^2),
    f'(s)=integral_0^1 [1/(A-t)+t/(U-At)]dt, A=d-s,
    f''(s)=integral_0^1 [1/(A-t)^2-t^2/(U-At)^2]dt.          (3)

On -1/8<=s<=1/10, f''>0: the integrand is positive since
U+t^2-2At>0 for A<=R and 0<=t<=1. On 0<=s<=1/10,

    13/5 < f''(s) < 6.                                    (4)

For the lower bound the first integral is at least
1/(d-1)-1/d=16/5, and the second is <3/5. For the upper bound
omit the second integral and use
1/(3/20)-1/(23/20)<6. The needed scalar bounds are

    23/20<c<5/4,  f'(0)<11/5,  f'(-1/8)>7/4,
    0<delta=2c-f'(0)<11/50,
    e_w'(1/20)<0<e_w'(1/10),
    e_b'(1/20)<0<e_b'(1/10),
    K(-1/8)<-1/8,  K(i/2)<-3/10.                          (5)

Here and below inequalities involving K use its real-valued definition.
All nontrivial scalar enclosures are certified by
`scripts/one-sided-hankel/positive-blend-saddle-certificate.py`, with
full output in the corresponding `.json` file. Reproduce from the
notebook directory with

    python3 scripts/one-sided-hankel/positive-blend-saddle-certificate.py

The certificate uses exact rational arithmetic. For clarity its
integration bounds used in (4) and Section 3 are

    integral_0^1 1/((11/8-t)^2+1/4)dt >11/10,
    integral_0^1 t^2/(U-(11/8)t)^2 dt <3/5,
    integral_0^1 1/((6/5-t)^2+1/4)dt >3/2,
    integral_0^1 t^2/(U-(5/4)t)^2 dt <1/2.                 (6)

Each integrand increases on [0,1]; its exact left and right sums on
256 equal cells enclose the integral. All summands, outward rounding,
actual bounds and required bounds are retained. The closed expression
for f' used by the code is

    log(A/(A-1))+(U/A^2)*log(U/(U-A))-1/A.

For K use the primitive
J(s,v)=(v/2)*log(s^2+v^2)-v+s*atan(v/s) for s>0, with its s=0
limit, so K(s+iy)=(10/27)*(2r*(log r-1)-J(|s|,y+r)+J(|s|,y-r)).
Logarithms use the 32-term atanh series after scaling into [1,2],
with tail 2*z^65/[65*(1-z^2)]. Arctangents reduce to |z|<=1/2
and use 60 alternating terms and error |z|^121/121; Machin's identity
encloses pi. These are the exact helpers already justified in L673
Section 4. No floating comparison or sampled residual is used.

The quantity K''(s)-6/5 is positive on [0,1/10], since its
minimum exceeds 0.368. Thus e_b''>=13/5, e_w''>=13/5, and
e_b'(0+)=e_w'(0)=-delta. Each has a unique stationary minimum
sigma_b,sigma_w in (1/20,1/10), by (5). Further,
e_b-e_w=cs-gamma*s^2+K(s) has value and right derivative zero
at zero and positive second derivative. Consequently e_b>=e_w.
Integrating the curvature lower bound in (4) yields

    e_w(s)>=-delta*s+(13/10)*s^2 >=-121/13000,
    e_b(s)>=-121/13000,             0<=s<=1/10.             (7)

This bound, rather than a fitted saddle value, is the rate discriminator.

### 3. Uniform vertical decay and complementary edges

For A=d-s and v=y^2, direct subtraction of the logarithms gives

    Re F(s+iy)-f(s)
      =(1/2)*integral_0^1
        [log(1+t^2*v/(U-At)^2)-log(1+v/(A-t)^2)]dt.

Differentiate in v. By (6), for -1/8<=s<=1/10, |y|<=1/2,
the derivative is less than (3/5-11/10)/2=-1/4.
For 1/20<=s<=1/10 it is less than (1/2-3/2)/2=-1/2.
Monotonicity in A and v justifies using those extremal integral bounds.
Therefore

    Re F(s+iy)<=f(s)-y^2/4                       (broad strip),
    Re F(s+iy)<=f(s)-y^2/2                       (right edges). (8)

For y>=0,

    K_y(s+iy)=-(5/27)*log[(s^2+(y+r)^2)/(s^2+(y-r)^2)].

On 1/20<=s<=1/10 and 0<=y<=1/2, use log(1+t)>=t/(1+t)
to obtain

    K(s+iy)-K(s)<=-(10/27)*r*y^2/(1/100+(19/20)^2).

Conjugation covers negative y. Combining with (8) and the quadratic
term proves

    Re F(s+iy)-cs-gamma*(s^2-y^2)+K(s+iy)
        <=e_b(s)-(2/25)*y^2,                             (9)

because 1/2+(10/27)*r/(1/100+(19/20)^2)-3/5>2/25.
For the Robin right edge, (8) gives e_w(s)-y^2/2.

For b, the left edge has s=-1/8. Since f' increases and
f'(-1/8)>7/4, f(-1/8)<-7/32. Also K(s+iy)<=K(s) for y>=0
and its negative counterpart, by the displayed derivative. Dropping
the favorable term -gamma*s^2, the whole left-edge exponent is less than

    -7/32+5/32-1/8+3/20=-3/80.                           (10)

On its top edge y=1/2, K(s+i/2)<=K(i/2)<-3/10: K decreases
with |s| there directly from the integral. For s>=0, (4)--(5) imply
f(s)-cs<=(21/20)*s+3*s^2. For s<=0, f(s)-cs<=0, since
f'(s)>7/4>c. Hence the top and bottom exponents are at most

    (21/20)*(1/10)+3/100+3/20-3/10=-3/200.              (11)

For w, the exact kernel estimates of L681 Section 2 still hold on
these altered contours with an absolute O(n) prefactor: on a right
edge s>0 use |(z-rho)/(z+rho)|<1, on the left use its reciprocal,
and on y=+-Y_n use cnY_n=2q*pi. Thus

    |K_n(z)|<=C*n*exp(-2cn*max(s,0))                    (12)

on every edge, with C independent of n. The horizontal estimate uses
Y_n>=9/25 and bounded |rho-z|/Y_n, exactly as in L681; it remains
uniform for s<=1/10. For n>=27, Y_n>=2/5. If s>=0, (4)--(5)
give e_w(s)<=-s/10+3s^2<=1/50 on [0,1/10]; if s<=0,
f(s)<=0. Equations (8) and (12) bound the top/bottom exponent by
1/50-(1/4)*(2/5)^2=-1/50. The left exponent is at most -7/32.
These bounds hold for the actual Y_n, with no limiting-height exchange.

### 4. Finite products and the signed local limit

Here are the uniform approximation details needed to turn the exponents
into signed integrals. On the fixed edges above and on a neighborhood
of each sigma, (2) is a full left Riemann sum of a smooth logarithm:

    log|W(z)|=n*Re F(z)+O(1).

On a sufficiently small complex neighborhood of each sigma the same
holds for the analytic logarithm and its first three z-derivatives.
Indeed all denominators are separated from zero (the nearest parameter
pole has real part at least 1/4), the numerator zeros are at real part
at most d-U<0, and the t-derivatives of these logarithms and their
first three z-derivatives are uniformly bounded on a compact set.
Summing the cell integration errors gives O(1). Constants are absolute.

For P, compare y_k with h*(k+1/2). The denominator logarithms and
their first three derivatives are smooth away from i[-r,r]; all used
edges have a fixed positive distance from that segment. Their midpoint
sum differs from h^(-1) times the segment integral by O(1), including
the two missing end intervals of length h/2. Shifting each node by
less than h/8 changes each such sum by O(1), because 4q*h is bounded.
For the numerator, cell comparison for log t on [0,2qh] gives an
O(log n) error: the first scaled cell contributes O(1), and the
remaining absolute cell errors are bounded by a constant times
sum_(1<=k<2q) 1/k. Appending the end intervals costs O(1).
Finally L673's root inequality e_k<=1/[10*pi*(k+1/2)] shows
sum log(y_k/[h*(k+1/2)])=O(1). These arguments give both bounds in

    log|P(0)/P(z)|=n*K(z)+O(log n),                     (13)

uniformly on all used edges. On a right neighborhood, the derivative
error in (13), interpreted as analytic logarithms, is O(1) through
order three; the numerator's O(log n) normalization is independent of z.
More precisely, differences between z and the real sigma have O(1)
error also in their real parts. This follows directly from the smooth
denominator sums just proved, without differentiating a modulus estimate.

For the Robin kernel, on a right neighborhood let r_n(z)=(z-rho)/(z+rho).
The exact identity

    K_n(z)=-2*C_n*r_n(z)*exp(-2cnz)
                              /(1+r_n(z)*exp(-2cnz))

shows that log(-K_n(z))=log(2C_n)-2cnz+O(1), with bounded
derivative errors through order three. Here r_n tends to one smoothly,
and each derivative of the exponentially small denominator correction
is bounded. Its modulus relative to its value at sigma is bounded
uniformly on the whole right edge. These facts, (8)--(9), and (13)
give for l=b,w, at the corresponding right edge sigma_l,

    H_l(sigma_l)<0                     (all sufficiently large n),
    log|H_l(sigma_l)|=n*e_l(sigma_l)+O(log n),
    |H_l(sigma_l+iy)/H_l(sigma_l)|<=C*exp(-a*n*y^2),          (14)

with one absolute C and some a>0. For b the remaining factors
(1-z/rho)/z have uniformly bounded ratios and bounded logarithmic
derivatives on the right neighborhood; their real value is negative
when sigma_b>rho. For w the same sign follows from the exact formula.
All other factors at the real point are positive.

Choose the analytic logarithm of -H_l near sigma_l, real there.
The derivative statements give

    (log(-H_l))'(sigma_l)=O(1),
    (log(-H_l))''(sigma_l)=n*e_l''(sigma_l)+O(1),
    (log(-H_l))'''=O(n)

on that neighborhood. Taylor's formula at z=sigma_l+i*v/sqrt(n)
therefore proves, uniformly for bounded real v,

    H_l(sigma_l+i*v/sqrt(n))/H_l(sigma_l)
              -> exp(-e_l''(sigma_l)*v^2/2).             (15)

The possibly nonzero finite-n linear phase tends to zero; it is not
silently dropped. By (14), the rescaled tails are bounded by
C*exp(-a*v^2). Their integrals tend uniformly to zero as the tail
cutoff tends to infinity. On each bounded v interval use (15), then
take that cutoff to infinity. Since the heights times sqrt(n) tend
to infinity, the entire right-edge contribution is

    H_l(sigma_l)/(2*pi*sqrt(n))
         *[sqrt(2*pi/e_l''(sigma_l))+o(1)].              (16)

The bracket is strictly positive eventually, and the leading sign
is negative. This proves the signed limit with all of the vertical
edge retained. It does not infer a lower bound from an absolute maximum.

By (10)--(13) and the finite-product errors, the other three edges
are O(n^C*exp(-3n/200)) for b and O(n^C*exp(-n/50)) for w.
By (7), their ratios to the magnitude in (16) tend to zero.
Thus there are absolute C_0,C_1>0 and an onset such that

    S_b<0, S_w<0,
    min(-S_b,-S_w)>=C_0*n^(-C_1)*exp(-121*n/13000).       (17)

The constants and onset can be shared because there are just two fixed
constructions. No claim of equal profiles or equal saddle locations is
needed. This supplies the uniform remainder needed for the sign decision.

### 5. Every convex blend retains the negative packet

At u=-1, the exact identity and W_(-R)(-1)>0 give, for all theta in [0,1],

    T_(n,theta)(-1)
      =W_(-R)(-1)-(1-theta)*S_b-theta*S_w
      >=min(-S_b,-S_w)>0.                              (18)

This is uniform even if theta depends on n. It is a statement about
the full combined function, not separate squared summands.

### 6. Point-to-continuous-norm transfer and rate comparison

Import V. I. Danchenko and L. A. Semin, *Sharp quadrature formulas
and Nikol'skii type inequalities for rational functions*,
[arXiv:1503.06476v1](https://arxiv.org/pdf/1503.06476v1), 22 March 2015,
Section 1.1, Theorem 2, PDF pp.1--2, proof pp.6--7, as inspected in
`drafts/literature/2026-11-02-displaced-signed-angular-sampling.md`
and used in L666. Theorem 1's underlying proof remains unaudited.
For a distinct finite interior pole set containing zero, its reflected
completion, ordinary pole orders <=1, and combined orders at zero and
infinity <=1, the normalized formula at radius one is

    ||T||_2^2=sum_(Bcal(u_l)^2=exp(i*phi))
                              |T(u_l)|^2/(2*mu(u_l)),
    mu(u)=sum_(z in S) (1-|z|^2)/|u-z|^2.                (19)

For the present T take the distinct union of zero, t_j*x/U,
t_j/conjugate(a) for all 4q nonanchor a, and -t_j/R,
1<=j<n. The last points account for W_(-R). Duplicates, if any,
are removed; they only reduce the count N_p. By L666 (6) each
individual term has only simple poles in this reflected completion,
and finite values at zero and infinity. Sums cannot increase pole order.
All interior moduli are <4/5, and

    N_p<=1+(4q+2)*(n-1)=n*(n+2)/3.

Thus every source hypothesis holds, including the added parameter -R.
Choose exp(i*phi)=Bcal(-1)^2, so one quadrature point is exactly -1.
Each Poisson term is <=9; hence mu(-1)<=9*N_p. Dropping the other
nonnegative terms from (19) gives

    ||T_(n,theta)||_2>=|T_(n,theta)(-1)|/sqrt(18*N_p).    (20)

In particular there is no unproved sampled-norm assumption. Equations
(17)--(20) bound the norm below by a polynomial factor times
exp(-121*n/13000), uniformly in theta. Since

    121/13000 < 19/2000 < 1/100,

the polynomial factor is absorbed into the first strict gap beyond
one absolute onset. This proves (1). For fixed epsilon>0 and kappa,
exp((1/100+epsilon-19/2000)*n)/n^kappa tends to infinity, which
contradicts the proposed upper bound. Independent H/support/Xi gaps
remain unaffected.

### 7. Separate conceptual audit — 2 November 2026, step 73

The invocation-start SPECIALIZE assessment was
`drafts/literature/2026-11-02-positive-blend-saddle-audit.md`.
This is a REPRODUCTION audit of (1), with existential onset and uniformity
over all n-dependent theta in [0,1]. It imports the named residue theorem
and the precise Danchenko--Semin formula in Sections 1 and 6; it does not
reprove their source manuscripts. The recorded Theorem 1 proof-audit
qualification remains. No new rate or arbitrary-weight result is asserted.

**Contours, branches and signs.** Direct substitution of u=-1 and
a=-d+z into L666 (6) gives (2), including its j=0 factor. For real s
in [-1/8,1/10], every denominator d-s-t and numerator U-td+ts is
positive. More generally their real parts are at least 3/20 and
U-R=33/64 throughout the closed rectangle. Hence one explicit branch
of the integrand defining F is

    log(d-t)-Log(d-z-t)+Log(U-td+tz)-log(U-td),

where both capitalized logarithms are principal in the right half-plane.
This branch is analytic on a neighborhood of the entire rectangle,
real on its real interval, and agrees with the full product at t_j.
The domain is this neighborhood, not the whole half-plane Re z<1/4,
which also contains numerator zeros farther left. This clarification
changes no estimate. In particular the shifted target -R corresponds
to z=-1/8 and has strictly positive W there.

For the finite product all +-i*y_k lie below r<1/2. For the Robin
kernel, the modulus contradiction for exp(2cnz)=(rho-z)/(rho+z)
excludes every nonimaginary zero, including direct checks of +-rho.
On the imaginary axis tan(pi*s)+10s has one simple root in each
(k+1/2,k+1), exactly L673's s_k, and no positive root in the other
half-intervals. The height Y_n/h=2q encloses exactly the required
2q pairs and zero, with no boundary root. W has no parameter pole
in either rectangle. The residues and positive orientation therefore
give S_b and S_w exactly. At a positive real saddle, P, W and the
real exponentials are positive; (1-s/rho)/s is negative eventually,
and the exact Robin formula is negative. The right contour runs upward,
so its contribution is +(1/(2*pi))*integral H(s+iy)dy. There is no
orientation sign reversal in (16).

**Curvature and every complementary edge.** Differentiating the explicit
branch gives (3). Positivity of f'' follows pointwise from
U+t^2-2At>0: for 0<=t<=1 and A<=R its minimum is at A=R,t=1
and equals (R-1)^2>0. The lower bound 13/5 uses 16/5 for the
first integral and the larger-A numerator bound <3/5. The upper
bound is 400/69<6. The minimum of K''-6/5 is 94/255>0.
Together with the checked derivative signs these give the two unique
real saddles and e_b>=e_w, with common lower barrier -121/13000.

For the vertical logarithmic difference, its v=y^2 derivative is
one half the integral of

    t^2/((U-At)^2+t^2*v)-1/((A-t)^2+v).

The first term is at most the certified numerator integral with the
largest permitted A and v=0. The subtracted integral is at least
the certified denominator integral with that largest A and v=1/4.
For right edges use A<=6/5 in the denominator and the looser A<=5/4
in the numerator. These monotone comparisons prove both parts of (8)
on the continuous strip. The four scalar integral functions increase
with t: their derivatives have signs of A-t and t*U respectively,
with positive denominators. Thus the saved left/right sums are valid
integral enclosures, not sampled monotonicity assumptions.

The derivative K_y has coefficient -5/27. The inequality
log(1+v)>=v/(1+v) bounds it above by
-(20/27)*r*y/[s^2+(y+r)^2]. Integrating and using
s^2+(y+r)^2<=1/100+(19/20)^2 gives (9); the resulting
vertical drop is 181/2190>2/25. On the left K decreases in |y|;
on the top K decreases in |s|. The complete b-edge exponents are
therefore <=-3/80 and <=-3/200. The Robin horizontal denominator
has imaginary part Y_n*cosh(cns), since cnY_n=2q*pi exactly.
This proves (12) with O(n) constants on the altered contour. For
n>=27, Y_n>=2/5, and its top/bottom and left exponents are
<=-1/50 and <-7/32. No passage from r to Y_n is left uncharged.

**Finite-product errors and the full signed limit.** For W, the explicit
branch and its first three z-derivatives have bounded t-derivatives
on the compact rectangle or a smaller right neighborhood as needed.
The error on each left Riemann cell is O(n^-2); multiplying the
integral by n and summing n cells gives O(1), also for those analytic
derivatives. This is stronger than mere convergence after division by n.

For the denominator of P, use

    L(z,t)=Log(z+i*t)+Log(z-i*t),        Re z>0.

On a neighborhood of either right edge this is analytic, agrees with
log(z^2+t^2) at positive real z, and has uniformly bounded mixed
t,z derivatives through the required orders. Midpoint cells cover
[0,2qh]; appending [2qh,r] costs O(1) after division by h because
r-2qh=h/2. Each node displacement is at most h/8, and the sum of
the resulting errors is O(qh)=O(1), again through three z-derivatives.
On the other fixed edges the same argument for real logarithms is
valid because their distance from i[-r,r] is bounded below.

For the numerator, the first scaled log cell has finite O(1) error;
the remaining errors sum to O(sum_(k<2q)1/(k+1/2))=O(log n).
The omitted end interval costs O(1). The relative node corrections
are bounded by a convergent multiple of sum (k+1/2)^(-2), using
L673's exact root inequality. This proves the two-sided normalization
error in (13). Crucially that entire numerator is independent of z.
For the vertical ratio it cancels exactly, leaving

    log|P(s)/P(s+iy)|
       =n*(K(s+iy)-K(s))+O(1),        |y|<=1/2,

with one uniform constant, not an O(log n) error. W's corresponding
ratio also has O(1) error. The b prefactor (1-z/rho)/z has bounded
ratio to its value at s and bounded local logarithmic derivatives once
rho<s/2. For w, r_n(z) tends smoothly to one on the right edge;
the denominator correction and its first three derivatives are bounded
by constants times n^j*exp(-2cn*s), which are bounded and tend to zero.
These observations prove every part of (14), with a constant independent
of n and without losing a polynomial in its Gaussian domination.

The local logarithm of -H_l is real at sigma_l. Its first derivative
is O(1), its second is n*e_l''+O(1), and its third is O(n).
Thus on bounded rescaled v-intervals the linear Taylor term is
O(v/sqrt(n)) and the cubic remainder is O(|v|^3/sqrt(n)). The
remaining term tends to -e_l''*v^2/2. Extend the rescaled integrand
by zero beyond the actual edge heights. Equation (14) dominates it
on the whole real line by C*exp(-a*v^2), an integrable function.
This proves (16) for the complete complex integral by dominated
convergence, with a positive real limit. Conjugate symmetry makes the
edge contribution real. The nonzero curvature and complementary-edge
gaps then give the negative signs and polynomial lower bounds in (17).
This verifies the analytic argument independently of the scalar replay.

**Uniform blends and rational norm transfer.** Equation (18) has two
negative packets with nonnegative blending coefficients. Taking their
minimum pays every theta in [0,1], including arbitrary dependence on n.
No common saddle, common profile or differentiability in theta is needed.
The separate onsets and polynomial constants can be combined because
there are only two fixed constructions.

The possible angular poles of each term are t_j*x/U and a/t_j.
For a=-R the new reflected interior points are -t_j/R, of modulus
<8/11<4/5. These may coincide with older real points; taking the
distinct union is essential and only reduces its size. Within each
individual rational term its interior and exterior poles are distinct
and simple, and addition cannot increase their order. Every term is
finite at zero and infinity; hence both pole orders there are zero.
Thus the exact source hypotheses of (19) hold for the completed set
containing zero, with order parameter one. The count is
1+(4q+2)(n-1)=n(n+2)/3. The Blaschke argument derivative mu is
positive, so selecting Bcal(-1)^2 includes -1 as a simple observation
point. Normalizing the cited integral by 2*pi gives 1/(2*mu), and
each Poisson term is at most 9. This proves (20) with no L2 bound
inferred from an arbitrary point evaluation. The final strict gap is
19/2000-121/13000=1/5200, which absorbs every fixed polynomial
loss; 1/100-19/2000=1/2000 remains for the required-rate comparison.

**Complete scalar evidence.** Reproduce with

    python3 scripts/one-sided-hankel/positive-blend-saddle-audit.py

The full artifacts are `scripts/one-sided-hankel/positive-blend-saddle-audit.json`
and `scripts/one-sided-hankel/positive-blend-saddle-audit-replay.json`.
The original artifact is preserved byte for byte and matches the complete
replay. All 43 audit checks pass: all 22 scalar inequalities, all four
256-cell integral enclosures and their 2048 outward-rounded contributions,
specifications, totals, replay and rate comparisons. The inherited helper
prefix was read in full. Its 32-term atanh tails, signed power-of-two
scaling, 60-term alternating arctangent tails, reciprocal/quarter-turn
reductions and Machin enclosure retain the stated rigorous errors.
No fixed-point complex-series mesh is executed by that prefix here.

No load-bearing defect was found. This verifies the stated bound for
the two specified constructions, with existential Q; it establishes no
effective onset, arbitrary-positive-weight obstruction, original-H bound,
support/realization bridge or Xi sign. The only branch-domain clarification
above makes explicit the compact domain already used by the proof.

## Mathlib

Full matching coverage for this two-construction obstruction, signed
asymptotic limit and rational norm specialization has not been checked.
The named residue theorem and Danchenko--Semin formula are cited above;
the latter's precise source qualifications are retained. Unknown
Mathlib coverage is not an absence claim. The scalar certificate
verifies constants only; Section 7 separately audits the analytic and
uniformity arguments. This is informal verification, not formalization.
