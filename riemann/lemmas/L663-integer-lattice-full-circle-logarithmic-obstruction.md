# Lemma 663: a unit-residue lattice obstructs full-circle logarithmic averaging

## Hypotheses

Retain the L649 family and its full grid, with x=-d=-5/4, R=11/8,
U=R^2=121/64 and eta=1/100. Specialize to integers n=6q+3, q>=1,
and put

    Y=9/20, h=27/(10n), a_l=x+i*l*h, -q<=l<=q,
    Z_n={a_l:-q<=l<=q}, r_(a_l)=1, M=N=2q+1=n/3.

The same distinct poles and original integer residues are used at every
angular u. In particular x=a_0 is included. Define, with t_j=j/n,

    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    c_k(u)=R^(-1) sum_(l=-q)^q W_(a_l)(u)*(a_l/R)^k,
    G(u,zeta)=sum_(0<=k<M)c_k(u)*zeta^k,
    D=sum_(l=-q)^q mean_u |W_(a_l)(u)|^2/(U-|a_l|^2),
    m(u)=mean_zeta log|G(u,zeta)|, A_n=mean_u m(u).

Both circle means are normalized probability means. The denominator
uses 1/u=conjugate(u) on the angular circle. All n grid factors and
all M spatial moments are retained. All logarithms are natural.
Use L657's actual cleared numerator K, denominator Q, and complete
charges m_0,Z_n^zero,P_n; the superscript distinguishes its zero charge
from the pole set Z_n just defined. Z_n^zero counts zeros with their
multiplicities, including cancellations with Q.

## Conclusion

This is an admissible sequence in the original integer family. With

    lambda=20*pi/27, L_Gamma=221/100,
    C_*=L_Gamma*lambda*exp(8)/(3*pi*R),

the complete two-circle logarithmic mean obeys, for every such n,

    A_n=m_0+Z_n^zero-P_n
        <=-33n/1000+2log n+log C_*.                       (1)

In particular the zero compensation itself satisfies

    Z_n^zero-P_n <=-33n/1000+log n
                      +log(3R*(R-eta)^2*C_*/d^2).        (2)

The full circle fails the approved paid-arc inequality asymptotically:

    log D-n/16-2A_n
       >=7n/2000-4log n+log(64/21)-2log C_* -> infinity. (3)

The stronger sufficient route proposed at invocation also fails:

    (log D)/2-n/32+log n-A_n
       >=7n/4000-log n+(log(64/21))/2-log C_* -> infinity. (4)

Thus no absolute constant and onset make either full-circle lower
bound hold uniformly in the original family. This does **not** exclude
a family-dependent connected angular arc. It gives no upper bound
on every allowed arc or on H=max m at the rate needed for such an
exclusion. The localized criterion, L651's joint comparison, actual-Xi
realization and all-degree signs remain unresolved. The family is an
ordinary evenly spaced unit-residue lattice, not L661's half-turn
phase census or C645x's fractional mixture.

The conceptual audit in section 7 validates this result, its analytic
use of the certificate, and the inherited inputs actually used. It
reuses the named source theorems and the original interval backend;
neither their manuscripts nor an independent arithmetic backend are
audited here. This is a local route obstruction under the unchanged
EXPLORE assessment, not an RH candidate or certified novelty.

## Proof

### 1. Scope, standard inputs and admissibility

Reuse the invocation-start assessment
`drafts/literature/2026-11-02-localized-logarithmic-joint-moment.md`.
It covers the exact localized criterion and admissible asymptotic
obstructions, including complete rational divisor and spatial costs.
This attempt tests its stronger full-circle subroute. The searches
recorded there and the local zero-evaluation, fractional-lattice,
deweighting, finite-screen and half-turn stops were compared. They do
not give (1)--(4). L649 supplies the original conventions, and L657
supplies absolute logarithmic integrability and the exact charge
identity. L658/L651 are downstream context, not premises. L661's
diagonal envelope motivated the test but is not used to prove it.

Import the residue theorem, simple-pole rule and contour absolute-value
bound from R. W. Howell and J. H. Mathews, *Complex Analysis*, online
edition with front matter updated 22 August 2025,
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html),
and [Section 6.2, Theorems 6.2.18--6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html).
These are the already inspected imports recorded in C645x/L661; no
new source or independent source audit is claimed. The finite contour
and error bounds below are necessary specializations, not a reproof
of the general residue theorem.

L657's logarithmic inputs are Z. Issa and M. Lalin,
*A generalization of a theorem of Boyd and Lawton*,
[arXiv:1203.5379v1, Remark 3.8 and Theorem 4.1, printed p.7](https://arxiv.org/pdf/1203.5379v1),
24 March 2012, with s=1; and F. Brunault and W. Zudilin,
*Many Variations of Mahler Measures*, ISBN 9781108794459,
[Proposition 1.4, pp.6--7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf).
The latter includes boundary roots. We use L657's verified nonzero
numerator and integrability specialization; we do not assume G is
nonzero everywhere on the torus or discard roots of any slice.

Since q*h<Y and

    d^2+Y^2=353/200 < (273/200)^2=(R-eta)^2,

all poles are permitted. They are distinct, include x, and have total
integer mass M=n/3. This also verifies the hypotheses for L657's
identity A_n=m_0+Z_n^zero-P_n and its bounds for m_0. The exact anchor
term in D gives D>=1/(U-d^2)=64/21, with no substitution of an
unsquared-residue diagonal.

### 2. Finite contour with all spatial moments and poles retained

In the complex y-plane take the positively oriented rectangle Gamma
whose real part is in [-Y,Y] and imaginary part in [-b,c], where

    b=2/25, c=1/8, e_0=d-b=117/100,
    K_n(y)=i*lambda*n/(exp(i*lambda*n*y)-1).

The only poles of K_n in this rectangle are the simple y=l*h,
-q<=l<=q. Each residue is one, since lambda*n*h=2*pi and
Y/h=n/6=q+1/2. No pole is on the boundary. In the full rectangle,
a=x+i*y has real part between -R and -e_0, so a cannot equal any
t_j*u, whose modulus is below one. Moreover

    |a|<=sqrt(R^2+Y^2)<29/20<U.

Thus W_a(u), as a function of y, is holomorphic and nonzero there:
its possible numerator zeros also require |a|=U/t_j>=U. The fixed
anchor denominators are nonzero. These facts justify every finite
contour application uniformly for |u|=1; there is no limiting contour.

For T_M(w)=sum_(0<=k<M)w^k the residue theorem gives exactly

    G(u,zeta)=(1/(2*pi*i*R)) integral_Gamma
               W_(x+i*y)(u)*K_n(y)*T_M((x+i*y)*zeta/R) dy. (5)

At a horizontal edge y=s+i*v, the denominator of K_n has modulus
at least |1-exp(-lambda*n*v)|. Since n>=9 and
lambda*5*b>log 2, both horizontal edges satisfy

    |K_n(s+i*v)|<=2*lambda*n*exp(-lambda*n*(-v)_+).       (6)

On a vertical edge exp(i*lambda*n*s)=-1, because s=+/-Y and n=6q+3.
Its denominator is 1+exp(-lambda*n*v), so (6) holds there as well,
even without its factor 2. This counts both endpoints and every edge.

For |zeta|=1 the full spatial polynomial satisfies

    |T_M(a*zeta/R)|<=M*max(1,|a|/R)^(M-1)
                  <=M*exp(n*beta(a)),
    beta(a)=(1/3)log max(1,|a|/R).                       (7)

The top-edge spatial cost is positive and is retained below. In
particular (7) is not an assertion that |a|<R on the whole contour.

### 3. Uniform product and quadrature bounds

For u=exp(i theta) and a in this rectangle set

    f(t,u,a)=log|(x-t*u)/(a-t*u)|
                 +log|(U*u-t*a)/(U*u-t*x)|,
    F(theta,s,v)=integral_0^1 f(t,u,x-v+i*s) dt
                    -lambda*(-v)_++beta(x-v+i*s),
    B(theta)=max_((s,v) in boundary Gamma) F(theta,s,v).

Let A=29/20. The uniform clearances d-1, e_0-1, U-A and U-d
are strictly positive. Differentiating the four logarithms yields

    |partial_t f| <=1/(d-1)+1/(e_0-1)+A/(U-A)+d/(U-d)<16,
    |partial_t^2 f| <=1/(d-1)^2+1/(e_0-1)^2
                                +A^2/(U-A)^2+d^2/(U-d)^2<70,
    |partial_theta^2 f| <=d/(d-1)^2+A/(e_0-1)^2
                                +U*A/(U-A)^2+U*d/(U-d)^2<100. (8)

For example, the angular second derivative of log|a-t*u| has
modulus at most |a|*t/|a-t*u|^2; the numerator factor gives
U*t*|a|/|U*u-t*a|^2. These prove the last line with t<=1.
All rational comparisons in (8) are checked exactly in the certificate.

The first bound gives the left Riemann-sum estimate

    sum_(j<n) f(t_j,u,a)<=n*integral_0^1 f(t,u,a)dt+8.   (9)

Indeed on each interval of length 1/n the integral of
16*(t-j/n) is 8/n^2, and multiplication by n and summation gives 8.
There is no replacement of the finite grid by an uncontrolled limit.

Combining (5)--(9), the contour length L_Gamma=221/100 and M=n/3,

    sup_(|zeta|=1)|G(u,zeta)|<=C_* n^2 exp(n*B(theta)).   (10)

Thus m(u)<=log C_*+2log n+n*B(theta). Its integral exists by L657.
This upper bound controls the actual complete polynomial; no spatial
root or signed residue has been removed in passing to it.

We will prove mean_theta B<=-33/1000. Two elementary interpolation
facts justify the finite certificate. If g''>=-C on an interval of
length delta, then g is bounded above by its chord plus
(C/2)*(t-left)*(right-t). This follows by adding C*t^2/2 and using
convexity. Integration gives the trapezoidal upper error C*delta^2/12.
A maximum of functions with the same lower second-derivative bound
has the same chord bound, because their convex modifications have
a convex maximum. Compact maxima, rather than only finite maxima,
are allowed by this argument. These facts apply to f in t and to B
in theta by (8). They require no differentiability of the maximizer.

### 4. Bounds for the four edges

Write a=-e+i*s, u=C+i*S with C=cos theta, S=sin theta. In this
section C is a cosine, not a free constant. On either vertical side
s=+/-Y, direct differentiation gives

    partial_e integral_0^1 f dt=integral_0^1
      [-(e+t*C)/((e+t*C)^2+(s-t*S)^2)
       +t*(U*C+e*t)/((U*C+e*t)^2+(U*S-t*s)^2)] dt.      (11)

The exact interval certificate described in section 5 proves

    integral (11) <=-3/10 for d<=e<=R,
    integral (11) >=-9/4 for e_0<=e<=d,                (12)

for both s signs and every theta in [0,pi]. Conjugation covers the
remaining half circle. For e>=d the spatial correction has derivative
either zero or e/[3(e^2+Y^2)]<=4/15<3/10. For e<=d it vanishes,
since e^2+Y^2<=d^2+Y^2<U; the kernel correction is lambda*(e-d),
whose derivative exceeds 9/4. Consequently each side's full exponent
F has its maximum at e=d, equivalently v=0. This treats the spatial
kink by monotonicity on its two pieces. The two side upper bounds are
therefore exactly integral_0^1 f(t,u,x+i*Y)dt and the same with -Y.

On the top edge e=R. The identity

    U*|a-t*u|^2-|U*u-t*a|^2=(U-t^2)(|a|^2-U)>=0

shows that every reciprocal Blaschke factor at a has modulus at most
one. The top bound is

    integral_0^1 (1/2)log[U*N_0/D_0] dt+beta_top,
    N_0=d^2+t^2+2*d*t*C,
    D_0=U^2+d^2*t^2+2*U*d*t*C,
    beta_top=(1/6)log[(U+Y^2)/U].                       (13)

On the bottom edge e=e_0, maximize one factor over the entire real
line of ordinates s. With e+t*C>0, the reciprocal
1/(a-t*u) describes a circle with center -1/[2(e+t*C)] and radius
1/[2(e+t*C)]. Since

    (U*u-t*a)/(a-t*u)=-t+(U-t^2)*u/(a-t*u),

the exact supremum of its modulus is

    [sqrt((2*e*t+(U+t^2)*C)^2+(U-t^2)^2*S^2)+U-t^2]
                                                       /[2(e+t*C)].

Multiplication by sqrt(N_0/D_0) gives a positive number V(t,C,S).
The bottom edge's f is at most log V for every allowed s. Its spatial
cost is zero and its kernel cost is -lambda*b. Hence a trapezoidal
sum of log V, plus the error 70/(12*128^2) and minus lambda*b,
is a bottom upper bound. The error is justified using the actual f
with |s|<=Y and (8): bound each chord endpoint by log V, then
integrate the chord inequality. No derivative bound for a maximizer
at an arbitrarily large s is being assumed.

Likewise, 128 uniform t intervals give upper bounds for both sides
and (13), each with error 70/(12*128^2). For the top integrand this
is more than the bound needed for its two anchor logarithms. Take
the maximum of these four bounds at each theta_k=k*pi/512,
0<=k<=512. It bounds B(theta_k). Because B is even by simultaneous
conjugation u->conjugate(u), s->-s, its full-circle mean is its mean
on [0,pi]. The chord inequality for B gives the additional error

    E_theta=100*pi^2/(12*512^2).                         (14)

Thus the normalized trapezoidal mean of these 513 maxima plus (14)
is an upper bound on the continuous full-circle mean of B. This
controls the continuum, not merely the sampled angles.

### 5. Complete arithmetic certificate and its scope

The producer is `scripts/one-sided-hankel/full-circle-root-compensation.py`.
Run from the notebook:

    python3 scripts/one-sided-hankel/full-circle-root-compensation.py
    python3 scripts/one-sided-hankel/full-circle-root-compensation.py --inspect-certificate

The complete producer certificate is
`scripts/one-sided-hankel/full-circle-root-compensation-certificate.json`;
the separate complete terminal-value/coverage inspection is
`scripts/one-sided-hankel/full-circle-root-compensation-inspection.json`.
Both passed with empty failure lists. The exploratory floating-point
diagnostic is separate and supplies no premise of this proof.

Every arithmetic interval is [lo/S_0,hi/S_0], S_0=2^72,
with signed integer endpoints. Basic operations round outward using
integer division. Square roots use integer isqrt with the upper endpoint
rounded up. Logarithms use binary range reduction and the positive
series 2*sum_(k=0)^23 z^(2k+1)/(2k+1), 0<=z<=1/3, with remainder
at most 2*z^49/[49*(1-z^2)]. The same formula encloses log 2.
Pi is enclosed by Machin's identity
16 atan(1/5)-4 atan(1/239), using respectively 32 and 12 alternating
terms with their next-term error bounds. The tangent addition formula
gives tangent one for 4 atan(1/5)-atan(1/239), which lies in (0,pi/2)
and is therefore pi/4.
Cosines and sines are reflected to [0,pi/2] and use 20 Taylor terms;
both remainder magnitudes are below (11/7)^40/40!<10^(-35).
The certificate checks this last comparison with exact integers and
also checks pi<22/7. Rounded transcendental library calls are not
used as premises. Floating values printed for convenience are not
used in any test.

For (12), each of its two e ranges is divided into 16 intervals and
[0,pi] into 128 intervals. For each side sign and every box, direct
interval integration of (11) on 256 t intervals yields the stored
`integral_interval`. All 8192 boxes pass the appropriate threshold.
The inspection reads every interval and verifies its threshold, the
complete disjoint covers of both e ranges and both side signs, and
the common t partition. It does not infer coverage from a preview.

For (13)--(14) and the other edges, `angular_rows` stores all 513
angles, all four rate upper bounds and each maximum. The inspection
checks every stored maximum and recomputes the complete weighted mean
and both quadrature error charges. It replays the global rational
arithmetic in (8). This is an inspection of all terminal evidence and
coverage; it is not an independent replay of every interval operation
or an independent conceptual audit of (5)--(14).

The complete selected comparison is

    mean B <= -160478178277610331367/4722366482869645213696
            < -33/1000.                                (15)

The displayed rational already includes the t error, the angular
error, both vertical sides, bottom kernel decay, and the top spatial
cost. It is approximately -0.0339825760791; the exact integer
comparison is the premise. No effective onset is needed for (15).

### 6. Divisor compensation and the route decision

Integrating (10) and applying (15) proves the upper bound in (1).
L657's absolutely integrable, exact two-circle identity proves its
equality with m_0+Z_n^zero-P_n. Its bound
m_0>=log[M*d^2/(R*(R-eta)^2)] and M=n/3 then give (2).
Thus the complete zero compensation is quantitatively bounded; it
has not been left as an unevaluated sum or replaced by its sign.
All cancellations in K/Q remain counted by L657's identity.

Finally D>=64/21 and 33/1000-1/32=7/4000 give (3)--(4).
For every fixed additive constant, their positive linear terms
eventually exceed their logarithmic terms. This proves failure of
the full-circle sufficient mechanism on an admissible subsequence.
It does not prove failure of the supremum over localized arcs:
an angular maximum can substantially exceed its mean. The construction
therefore parks full-circle averaging while preserving the original
localized target and every independent Xi/sign gap.

### 7. Conceptual audit — 2 November 2026

The audit accepts (1)--(4) without a mathematical correction. It read
the full proof and producer, L649's definitions and convergence
conventions, and L657's complete clearing, nonzero-slice, integrability
and divisor arguments used here. It checks these applications of the
named residue and logarithmic-integrability/root theorems, rather than
independently auditing their source manuscripts. L657's other local
estimates and L649's deweighting conclusions are not premises of this
result and are not promoted by this audit.

**Contour, census and normalization.** Since Y/h=q+1/2, the rectangle
contains exactly 2q+1 kernel poles. The derivative of its exponential
denominator at each is i*lambda*n, giving residue one with the stated
positive orientation. The continued a=x+i*y has Re(a)<=-117/100,
so a=t_j*u is impossible; its modulus is below 29/20<U, so
U*u=t_j*a is also impossible. Consequently the contour contains no
unrecorded singularity of W or T_M. The spatial polynomial has exactly
M terms, and its bound uses M*max(1,|a|/R)^(M-1), including the
top edge where |a| can exceed R. The factor 1/R in (5), the kernel
factor 2*lambda*n, M=n/3 and the perimeter 221/100 give exactly
C_* n^2, with the exp(8) grid error. Nothing depends on sampling
the spatial circle. At the anchor W_x=1 and r_x=1, so D>=64/21
uses the actual squared-residue diagonal.

**Vertical and horizontal edges.** Differentiating with respect to
e in a=-e+i*s gives precisely (11): the numerator derivative has
the plus sign t*(U*C+e*t), and the denominator contributes
-(e+t*C). On e<=d the derivative of the kernel correction is
+lambda, not -lambda. Hence (12) implies an increasing full
exponent there, since lambda>9/4. On e>=d the spatial derivative
is at most 1/(3e)<=4/15<3/10, so the exponent decreases, including
across the spatial kink by continuity. Both vertical maxima are
therefore at e=d. For the top edge, the displayed Blaschke identity
gives |U*u-t*a|/|a-t*u|<=R; multiplication by the anchor ratio
gives exactly (13). On the bottom, writing A=e+t*C>0 makes
1/(a-t*u) range over the circle of center -1/(2A) and radius
1/(2A), up to its limiting point. Translating and multiplying as
in section 4 gives exactly V. Taking this supremum factor by factor
can only enlarge the actual edge bound. The bottom spatial cost is
zero because e_0^2+Y^2<U.

**Continuum and maximum.** For each fixed contour point, the four
logarithms have denominators bounded away from zero. The t and theta
second derivatives are bounded by (8), uniformly in that point.
If g''>=-C, convexity of g(t)+C*t^2/2 gives

    g(t)<=chord_g(t)+(C/2)*(t-left)*(right-t).

For each fixed bottom s, this applies to its actual f. Its endpoint
values are at most log V, so the same integrated upper chord bound
holds using those larger endpoints. No derivative estimate for log V
or for its maximizing s is needed. The top anchor-only integrand
also satisfies the 70 bound. This justifies all four t quadratures.
For angular integration, F(theta,s,v)+50*theta^2 is convex for each
fixed boundary point; beta and the kernel correction are independent
of theta. The maximum over the compact boundary is finite, and a
supremum of convex functions is convex. Thus B+50*theta^2 is convex
on [0,pi], even where the maximizing edge changes. Its normalized
trapezoidal upper error is exactly 100*pi^2/(12*512^2). Conjugation
sends (theta,s,v) to (-theta,-s,v), preserving the boundary and all
costs, so the half-circle calculation is the full-circle mean.

**Outward arithmetic.** Every operation in the producer was read.
For intervals with positive denominator, the extrema of a quotient
over the rectangle occur at its corners; floor/ceiling of the four
scaled quotients enclose them. Negative denominators are reduced to
that case by simultaneous sign reversal. Products use the same
corner rule; squares treat intervals crossing zero separately.
The integer square-root floor and ceiling enclose both endpoints.
For a positive scaled integer v, binary reduction chooses an exact
power-of-two den with den<=v<2den; hence z=(v-den)/(v+den) is in
[0,1/3). The positive artanh series and its geometric tail enclose
log(v/den); the same series at z=1/3 encloses log 2. Negative binary
exponents are handled by interval multiplication, which reverses
endpoints as required. Therefore log_hi is a valid monotone upper
bound even when the logarithm is negative.

Machin's formula uses alternating atan series with a symmetric bound
by the next omitted term. The branch is fixed by
0<4*atan(1/5)-atan(1/239)<4/5<pi/2 and its tangent being one.
The reflected sine/cosine Taylor intervals use |z|<11/7, with
(11/7)^40/40!<10^(-35); the sine remainder of order 41 is smaller
still. Endpoint cosine monotonicity and the single sine maximum on
[0,pi] justify trig_box. All intermediate interval operations round
outward. The stored derivative boxes integrate interval enclosures
over complete t subintervals; they do not use point quadrature.
The angular rows instead use point intervals with the separately
proved quadrature error. Ceiling division remains an upper rounding
operation for negative numerators as well as positive ones. The
bottom subtraction uses the lower bound for lambda*b, preserving
the upper direction. No floating-point diagnostic is a premise.

**Full replay and its limits.** The audit command is

    python3 scripts/one-sided-hankel/full-circle-root-compensation-audit.py

Its complete output is
`scripts/one-sided-hankel/full-circle-root-compensation-audit.json`.
It preserves the original producer and certificate, recomputes all
8192 derivative intervals and all 513 four-edge angular rows, and
compares every value with the originals. It checks the complete
disjoint covers, every derivative threshold and maximum, all global
values, both quadrature charges, and the aggregation using exact
rational arithmetic. All values reproduce and the failure list is
empty. The all-box derivative extrema are recorded in that artifact;
the least favorable top upper endpoint is
-189060661796807590901/590295810358705651712<-3/10,
and the least favorable bottom lower endpoint is
-9861207077654893068171/4722366482869645213696>-9/4.
The continuous mean upper bound is exactly (15), with positive margin

    (-33/1000)-upper
      =580010542864004914379/590295810358705651712000.

The replay uses the same interval backend after the operation-level
audit above; it is not an independently implemented interval proof or
a Lean certificate. Complete terminal evidence was processed, not
inferred from a JSON preview.

**Divisors and stopping scope.** L657's K is nonzero; its nonzero
center slice follows from Re c_0(0)>0, and Q has no unit-circle zero.
The one-variable root formula handles individual nonzero slices;
product integrability justifies Fubini and restriction to positive-
measure arcs despite zeros. Factoring K for almost
every spatial slice and subtracting Q counts all cancelled interior
zeros and poles, including zero charges at boundary roots. Thus the
mean controlled by (10) is the same m_0+Z_n^zero-P_n in (1),
not a selected subset of roots. Subtraction of the actual lower m_0
bound gives (2). The exact differences
33/1000-1/32=7/4000 and 66/1000-1/16=7/2000 then give
(3)--(4); positive linear terms dominate their stated logarithmic
costs on the admissible subsequence. This validates the full-circle
stop. A negative full-circle mean supplies no upper bound on every
arc or on H. The localized criterion and Xi/sign gaps remain open.

## Mathlib

The reused source assessment inspected
[Mathlib.Analysis.Polynomial.MahlerMeasure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html).
Supporting results include `Polynomial.intervalIntegrable_mahlerMeasure`,
`Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`
and `Polynomial.mahlerMeasure_mul`; analytic nonzero hypotheses and
boundary-root qualifications remain those in L657. Full coverage of
this finite-lattice contour bound and its certificate has not been
checked. No absence claim about Mathlib as a whole is made, and this
is not a Lean verification of the interval program or the argument.
