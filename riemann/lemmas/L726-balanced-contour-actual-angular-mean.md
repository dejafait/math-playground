# Lemma 726: a balanced contour pays the actual constant angular mean

## Hypotheses

Fix one actual L703 profile, with all cutoffs, constants and the Picard
solution T fixed before n varies, as in L708. Retain L666's full family:

    d=5/4, x=-d, R=11/8, U=R^2, A=27/10, Y=9/20,
    n=12q+3, q>=1, h=A/n, M=n/3, t_j=j/n,
    s_m=m+1/2, y_m=h*(s_m+e_m), -2q<=m<2q,
    Z_n={x} union {x+i*y_m: -2q<=m<2q},
    W_a(u)=(x/a)*product_(j=1)^(n-1)
        [(x-t_j*u)/(a-t_j*u)]*[(U*u-t_j*a)/(U*u-t_j*x)],
    c_0(u)=R^(-1)*sum_(a in Z_n)W_a(u),
    mu_n=mean_(|u|=1)c_0(u), E_0=mean_(|u|=1)|c_0(u)|^2,
    D=mean_(|u|=1)sum_(a in Z_n)|W_a(u)|^2/(U-|a|^2).

All means are normalized. The original masses are one, W_x=1,
the j=0 factor x/a and the inverse denominator angle are retained.
No ordinate symmetry is assumed. In particular the inherited data give

    E=sum_m|e_m|<infinity, r=sup_m|e_m|<=1/8,
    Q2=sum_m e_m^2<=r*E<=1/(16*pi^2),
    T(t)=sum_m e_m*exp(2*pi*i*m*t),
    supp(T) subset [-7/16,7/16] in the principal period.

Use the exact L694/L703 equation T+R(e)=Q_w, with Phi=1 on
[-3/8,3/8], Q_w(t)=-exp(-pi*i*t)*chi_w(t)/(2*pi*i*t)
on its support and zero elsewhere. Here chi_w has its two disjoint
bumps, 0<=chi_w<=1, centered at +/-c_*, c_*=omega_*/(2*pi),

    omega_*=A*integral_0^1[1/(d+t)-t/(U+d*t)]dt,
    w<=3/81920.

The width bound is the audited L708 (4), for these actual selections.
No bound 0<=Phi<=1 outside its plateau is imposed.

## Conclusion

The complete signed mean has a limit L, depending on the fixed profile,
and satisfies

    |R*L-1|<=299/320,
    Re(mu_n)>=21/(640*R)>0                              (1)

for every sufficiently large allowed n. Consequently the approved
target |mu_n|>=exp(-n/100) holds eventually, hence on an unbounded
subsequence. The onset is not effective or uniform over profile choices.

With the original D and L661's envelope this also implies, eventually,

    E_0/D >= n^2*exp(-n/16).                            (2)

This pays L666's sufficient scalar E_0/D comparison for this fixed
family, not a universal family bound. The separate downstream audit in
Section 8 accepts the following consequence for the full original
G(u,zeta)=sum_(0<=k<M)c_k(u)*zeta^k. For every sufficiently large
allowed n there is one connected angular arc I_n with normalized
length n^(-2) such that

    log mu_arc(I_n)+2 mean_(I_n x T) log|G|
                       >=log D-n/16-32*pi^2/9.          (3)

Here c_k=R^(-1)sum_a W_a(u)(a/R)^k. The onset may depend on the
fixed profile and remains ineffective; the arc can vary with n.
Global angular charge, general support, matching detector upper bounds,
Xi realization and actual-Xi all-degree mixed signs remain unresolved.
The separate conceptual audit of 3 November 2026, step 216, accepts
(1)--(2) with this fixed-profile quantifier. It does not audit that
downstream assembly, resolve RH or certify originality.

## Proof

### 1. Approved scope, standard inputs and complete signed residues

Use the invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-actual-angular-mean.md`. It covers this
fixed-profile complete constant-mode contour test. The negative-mode
coordinates and continued-origin stops are contrasts, not inputs.
C645o/C645p remain unaudited; no assertion is imported wholesale from
them. The finite scalar pole computation below is verified directly.

Import the residue theorem and simple-pole rule from R. W. Howell and
J. H. Mathews, *Complex Analysis*, online edition, front matter updated
22 August 2025, [Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html).
Import scalar Fourier orthogonality/Parseval and the constant-mode
projection from A. Levitt, *Analyse de Fourier et applications*, version
retrieved 2 November 2026, Theorem 1.3/Exercise 1.2 and Theorem
1.11/Corollary 1.12, printed pp.6,8 ([author PDF](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf)).
Their statements/proofs were inspected in the reused assessments.
These general theorems are not reproved. The necessary new work is
control of this product and its complete signed actual spatial sum.
No saddle theorem or uniform asymptotic for analytic powers is assumed.

Put p_j=t_j*x/U, 1<=j<n. For a!=x define

    r_(j,a)=(x/a)*(x-t_j*p_j)/(a-t_j*p_j)*t_j*(x-a)/U
       *product_(k!=j,1<=k<n)
          [(x-t_k*p_j)/(a-t_k*p_j)]
          *[(U*p_j-t_k*a)/(U*p_j-t_k*x)].

This is Res_(u=p_j)W_a(u), with zero allowed if cancellation occurs.
The p_j are distinct nonzero real points with |p_j|<d/U<1.
All other possible poles a/t_j have modulus >d>1. All are simple
within a single summand, and a sum can only cancel them. The anchor
is identically one. Zero is regular and W_a(0)=x/a. Thus the exact
signed residue formula is

    R*mu_n=1+sum_(a!=x)[x/a+sum_(j=1)^(n-1)r_(j,a)/p_j]. (3)

It includes the origin residue of W_a/u and every common interior
pole, with no pole on the contour. No positivity of its summands is
claimed, and its continued-origin part is not substituted for mu_n.

### 2. Balanced contour, exact contraction and central frequency

Deform the angular circle to |u|=d/R=10/11. No pole of W_a/u lies
in the closed intervening annulus: |p_j|<d/U<d/R and
|a/t_j|>d>1. Hence its normalized integral is unchanged. Set
u=(d/R)z, |z|=1, b=1-i*y/d, k_j=t_j/R, and F_n(y,z)=W_(x+i*y)(u).
Direct substitution, including j=0, gives

    F_n(y,z)=b^(-1)*product_(j=1)^(n-1)
         [(1+k_j*z)/(b+k_j*z)]*[(z+k_j*b)/(z+k_j)].       (4)

For real |y|<=1/2, |b|<11/10, 0<k_j<8/11. No factor vanishes
or has a pole: |b+k_j*z|>=3/11, |z+k_j*b|>1/5, and
|1+k_j*z|=|z+k_j|>=3/11. On the circle,

    |b+k_j*z|^2-|z+k_j*b|^2
                 =(|b|^2-1)*(1-k_j^2)=(y/d)^2*(1-k_j^2).

Also |b+k_j*z|<2. Therefore each factor's squared modulus is at
most exp[-57*(y/d)^2/484]. Since n>=15, n-1>=14*n/15 and |b|>=1,

    |F_n(y,z)|<=exp(-n*y^2/32), |y|<=1/2.              (5)

The coefficient before n*y^2 from this calculation is at least
57*14/(968*15*d^2)>1/32. This estimate uses no absolute spatial sum
as a replacement for the signed mean.

Choose the logarithm ell_n(y,z) continuously along the real interval
from ell_n(0,z)=0. Uniform nonvanishing of all factors in (4) shows
|partial_y^j ell_n|<=C_j*n for j=1,2 there, with constants independent
of n,z. Differentiating the original product at y=0 gives

    ell_n'(0,z)=i*n*omega_n(theta)/A,
    omega_n(theta)=(A/(n*d))*sum_(j=0)^(n-1)
          (1-k_j^2)/(1+2*k_j*cos(theta)+k_j^2), z=exp(i*theta).

Indeed 1/(d+t*u)-t/(U*u+d*t) equals
(1-k^2)/(d*|1+k*z|^2) on this contour; the zero-grid term is 1/d.
Uniform Riemann-sum convergence, with denominators >=(3/11)^2,
yields omega_n->omega uniformly, where

    omega(theta)=(A/d)*integral_0^1
         (1-(t/R)^2)/(1+2*(t/R)*cos(theta)+(t/R)^2)dt.    (6)

It is even and strictly increasing on (0,pi). Its endpoint values are

    omega(0)=(54/25)*[-1+(11/4)*log(19/11)]>126/125>1,
    omega(pi)=(54/25)*[-1+(11/4)*log(11/3)]<28/5<2*pi. (7)

The first non-strict lower bound 126/125 follows from
log(v)>=2*(v-1)/(v+1), v>=1, and is strict here. For the second,
log(11/3)<13/10 gives the stronger upper bound 2781/500.
For example the exponential Taylor polynomial through degree eight
at 13/10 is already >11/3. These are elementary scalar bounds.

### 3. The complete finite unshifted comb tends to zero

This step verifies cancellation, rather than interchanging an infinite
comb and an n-dependent contour kernel. Fix a smooth real cutoff kappa
equal to one on |y|<=delta/2 and zero on |y|>=delta, with a fixed
0<delta<Y/2. Put

    V_n(y,z)=F_n(y,z)*exp[-i*n*omega_n(theta)*y/A],
    f_n(y,z)=kappa(y)*V_n(y,z),

extended by zero outside the cutoff. The oscillatory exponential has
modulus one on real y. The derivative bounds above give

    |ell_n'(y,z)-ell_n'(0,z)|<=C*n*|y|,
    |V_n''(y,z)|<=C*(n+n^2*y^2)*exp(-n*y^2/32).

Together with (5), the analogous first-derivative bound and cutoff
derivatives imply

    integral_R |f_n''(y,z)|dy <= C*sqrt(n)              (8)

uniformly in z. Cutoff-derivative terms are exponentially small or
bounded by the same Gaussian integrals. All constants here may depend
on the fixed cutoff, which is sufficient.

For a_m=f_n(h*(m+1/2),z), the double integral for a second difference
and the tiling of R by the h-intervals give

    sum_m |a_(m+2)-2*a_(m+1)+a_m|
       <=h*integral_R|f_n''(y,z)|dy=O(n^(-1/2)).        (9)

Explicitly, the difference is the integral over 0<=s,t<=h of
f_n''(h*(m+1/2)+s+t,z). For each fixed s, summation of the t
integrals covers R once, proving (9). These sequences have finite
support. Shifting their finite Fourier sums twice therefore yields

    |sum_m a_m*exp(i*omega_n*m)|
       <= |1-exp(i*omega_n)|^(-2)*sum_m|Delta^2 a_m|
       =O(n^(-1/2)).                                  (10)

The denominator is uniformly bounded away from zero by (7) and
uniform convergence of omega_n. Since
F_n(h*(m+1/2),z)=exp(i*omega_n*(m+1/2))*V_n(h*(m+1/2),z),
(10) controls the cutoff version of the unshifted sum. For large n
its support lies entirely in -2q<=m<2q. Every omitted finite term
has |h*(m+1/2)|>=delta/2 and <=Y, so (5) bounds the total omission
by O(n*exp(-n*delta^2/128)). Both finite endpoints are retained in
this error. Consequently, uniformly in z,

    sum_(-2q<=m<2q)F_n(h*(m+1/2),z) -> 0.             (11)

### 4. The actual shifted correction and the limiting signed mean

All interpolated ordinates between h*s_m and h*(s_m+e_m) lie in
[-1/2,1/2]. From (4)--(5) and |ell_n'|<=C*n,

    |F_n(h*(s_m+e_m),z)-F_n(h*s_m,z)|<=C*|e_m|.        (12)

For each fixed real v, Taylor's formula at zero and (6) give, uniformly
in z, F_n(h*v,z)->exp(i*omega(theta)*v). Since E<infinity, (12)
allows dominated convergence of the shifted-minus-unshifted finite
sum: first truncate m to a fixed finite interval, then bound both
tails by C*sum|e_m|. Both moving endpoints tend to infinity.
Together with (11), this proves the uniform limit

    R*c_0((d/R)*exp(i*theta)) -> 1+S_e(omega(theta)),
    S_e(v)=sum_(m in Z) exp(i*v*(m+1/2))
                                      *(exp(i*v*e_m)-1). (13)

The series for S_e is locally uniformly absolutely convergent since
its summand magnitude is <=|v*e_m|. Thus contour integration and
the uniform limit, not an unsupported infinite-comb interchange, give

    R*mu_n -> 1+mean_theta S_e(omega(theta)).            (14)

In particular the anchor in (14) has survived unchanged. The remaining
task is a quantitative bound for this entire signed correction.

### 5. Paying the limiting correction without a global Phi bound

Write

    N(v)=sum_m exp(i*v*m)*(exp(i*v*e_m)-1-i*v*e_m),
    |N(v)|<=v^2*Q2/2,
    S_e(v)=exp(i*v/2)*[i*v*T(v/(2*pi))+N(v)].           (15)

The Taylor remainder inequality holds for real v*e_m and the sums
are absolutely convergent. On |v|<=3*pi/4 the exact fixed-point
equation, including its removable zero value, gives

    i*v*T(v/(2*pi))+N(v)
                  =-exp(-i*v/2)*chi_w(v/(2*pi)),
    S_e(v)=-chi_w(v/(2*pi)).                           (16)

This uses Phi=1 only on its recorded plateau. Outside the two data
bumps Q_w is zero there. It does not assert a global Fourier gap.

For 5*pi/4<=v<=omega(pi), put v0=v-2*pi, so
-3*pi/4<=v0<0. Periodicity of T and (16) express (15) as a bump
term of magnitude (v/|v0|)*chi_w(v0/(2*pi)), plus a remainder of
magnitude at most

    (v*|v0|+v^2)*Q2/2=pi*v*Q2<7/60.                 (17)

For the central band 3*pi/4<=v<=5*pi/4, keep the linear T term
in (15); its nonlinear remainder is at most 25/512<7/60. For the
low band (16) has no remainder. Thus the mean of all these remainder
costs is <7/60, not a separate cost for each band.

We next bound the linear central-band cost. The pushforward of
normalized angular measure under omega has density

    p(v)=1/(pi*omega'(theta)), 0<theta<pi, v=omega(theta).

Differentiating (6), with k=t/R, gives

    omega'(theta)=(A/d)*sin(theta)*integral_0^1
                 2*k*(1-k^2)/(1+2*k*cos(theta)+k^2)^2 dt.

The exact ancillary bounds in Section 6 give

    omega(arccos(-1/2))<9/4<3*pi/4,
    omega(arccos(-12/13))>4>5*pi/4.

Hence throughout the central frequency band,
2*pi/3<theta<arccos(-12/13), sin(theta)>=5/13 and
1+2*k*cos(theta)+k^2<=1-k+k^2<=1. Therefore

    omega'(theta)>=C*(5/13)=38448/86515,
    C=(A/d)*(1/R-1/(2*R^3))=38448/33275,
    p(v)<=3/4.                                        (18)

Here the classical Archimedean bounds 223/71<pi<22/7 in particular
give pi>25/8, and (25/8)*(38448/86515)>4/3.

The support of T means that in the central band T(v/(2*pi)) can
be nonzero only on [3*pi/4,7*pi/8] union [9*pi/8,5*pi/4], of
total length pi/4. Scalar Parseval gives

    integral_(central band)|T(v/(2*pi))|^2 dv
                <=2*pi*sum_m e_m^2<=1/(8*pi).

Cauchy--Schwarz and (18) now pay the whole linear central term:

    integral_(central band) v*|T(v/(2*pi))|*p(v)dv
       <=(5*pi/4)*(3/4)*sqrt(pi/4)*sqrt(1/(8*pi))
       =15*pi/(64*sqrt(2))<8/15.                       (19)

This is why no unprovided global sup bound for Phi or T is necessary.

It remains to bound the two bump costs. Globally the derivative formula
and 1+2*k*cos(theta)+k^2<=(1+8/11)^2 give

    omega'(theta)>sin(theta)/8,

because C/(1+8/11)^4=422928/3258025>1/8. For any frequency
interval of width delta, its preimage in [0,pi] has length ell with
delta>=(cos(alpha)-cos(alpha+ell))/8>=ell^2/(4*pi^2).
The last inequality follows from sin(ell/2)>=ell/pi and the minimum
cosine difference at an endpoint. Thus its normalized angular mass
is <=2*sqrt(delta). Each relevant bump interval has width

    delta=4*pi*w<=3*pi/20480,
    2*sqrt(delta)<7/160.                               (20)

Both its lower frequency omega_*-2*pi*w and the corresponding
|v0| exceed one. Indeed the pointwise comparison with omega(0) gives

    omega_* >=126/125-A*(d-R)^2/(2*d^2*R^2)
             =15138/15125>1+1/2000,

and 2*pi*w<3*pi/40960<1/2000. To check the comparison, subtract
f_1(t)=(U-t^2)/[(d+t)*(U+d*t)] from
f_bal(t)=(R-t)/[d*(R+t)]; their difference is
(R-t)*(d-R)^2*t/[d*(R+t)*(d+t)*(U+d*t)], bounded above by
(d-R)^2*t/(d^2*R^2). Integrate and multiply by A.
On the high bump v/|v0|=2*pi/|v0|-1<11/2. Since chi_w<=1,
the sum of low and high bump costs is therefore <

    (1+11/2)*(7/160)=91/320.                           (21)

Combining (17), (19) and (21), with the triangle inequality applied
to the complete correction rather than individual residues, proves

    |mean_theta S_e(omega(theta))|
       <=mean_theta|S_e(omega(theta))|
       <8/15+91/320+7/60=299/320.                      (22)

Equations (14) and (22) imply (1). In particular the positive distance
from zero is a proved cancellation budget, not reality or mere
nonvanishing of a rational function.

### 6. Exact ancillary certificate and original-D threshold

The two non-elementary-looking scalar integrals used in (18) have
fully rational bounds. For c=-1/2 and c=-12/13, partition [0,1]
into 128 equal intervals and put k_lo=j/(128*R),
k_hi=(j+1)/(128*R). The numerator 1-k^2 lies between its endpoint
values. For the positive quadratic 1+2*c*k+k^2 its maximum is at
an endpoint; its minimum is at an endpoint or at k=-c if that point
belongs to the interval. Divide these bounds with positive denominators,
multiply by A/(128*d), and add. The full rational certificate records
every cell, its exact raw contribution, outward rounding to 10^(-8),
and the total. It proves

    omega(arccos(-1/2)) <=219083311/100000000<9/4,
    omega(arccos(-12/13))>=1004189/250000>4.

Reproduce with
`python3 scripts/one-sided-hankel/actual-angular-mean-bounds-214.py`.
The complete certificate is
`scripts/one-sided-hankel/actual-angular-mean-bounds-214.json`.
The bound algorithm and all checks, constants and these exact totals
were inspected; this is exact rational ancillary verification, not a
finite-n numerical mean or evidence for an unbounded subsequence.
Other rational comparisons in the proof are recorded by the same
script. The limit argument in Sections 3--4 is analytic, not certified
by a numerical preview.

Finally constant-mode projection gives E_0>=|mu_n|^2. All original
unit masses and squared diagonal terms remain in L661's envelope:

    D<=n*exp(2*kappa*n+6)/(3*sigma^2),
    kappa=91/5000, sigma^2=137/5000.

Writing a0=21/(640*R), (1) gives

    E_0/D >=3*sigma^2*exp(-6)*a0^2*n^(-1)*exp(-2*kappa*n).

Its ratio to n^2*exp(-n/16) tends to infinity, since
1/16-2*kappa=261/10000>0. This proves (2), with all polynomial
factors paid, and gives the stated L666 interface. No change of D,
pole weights, finite endpoints or spatial moments has been made.
Neither this special family nor a paid scalar bridge establishes
the independent global charges or transfers it to Xi.

### 7. Separate conceptual audit — 3 November 2026, step 216

Use the prior EXPLORE assessment
`drafts/literature/2026-11-03-balanced-angular-mean-audit.md` for exactly
this limit, correction budget and original-D specialization. The named
residue and Fourier theorems in Section 1 are reused with their stated
hypotheses, not reproved. L694's exact equation, L703's ordered choices
and smallness, L708's constructed width, and L661's general envelope
are the local inputs checked here. L661's special census is not assumed.
L666's quadrature and spatial Jensen conclusions are not premises of
the proof of (1)--(2).

**Poles, deformation and real-ordinate bounds.** At p_j the residue
of (U*u-t_j*a)/(U*u-t_j*x) is t_j*(x-a)/U; the other factors
are regular there. This proves the displayed r_(j,a), including zero
when cancelled. At zero the nonzero-grid ratios cancel in pairs and
W_a(0)=x/a. Both circles and their annulus avoid all p_j, since
d/U=80/121<10/11, and all a/t_j, since |a/t_j|>d>1. The residue
theorem therefore preserves the normalized integral of W_a/u. It
does not require W_a to be analytic inside either circle.

For |y|<=1/2, |b|<=sqrt(29/25)<11/10, so |b+k_j*z|>3/11
and |z+k_j*b|>1/5. The squared-modulus identity in Section 2 holds
for complex b: both cross terms have equal real parts. Dividing it by
|b+k_j*z|^2<4 bounds the squared-factor decrement below by
57*(y/d)^2/484. Taking square roots, multiplying n-1 factors and
using |b|^(-1)<=1 gives coefficient 57*14/(968*15*d^2)>1/32
in (5). Define the logarithm for each z by integrating F_n'/F_n
along the real y interval from zero. Uniform denominator clearances
give the stated derivative bounds without a jointly defined logarithm
in an annulus in z. Direct differentiation yields

    ell_n'(0,z)=(i/d)*sum_(j=0)^(n-1)
                       (1-k_j^2)/|1+k_j*z|^2.

The j=0 term is the derivative of b^(-1). The integrand and its t
derivative are bounded uniformly on [0,1] times the circle, justifying
uniform left Riemann-sum convergence. The endpoint antiderivatives give
(7); the lower logarithm bound gives 126/125 and the upper Taylor
check gives 2781/500<28/5. Thus omega_n stays a fixed positive
distance from 2*pi*Z uniformly for all sufficiently large n.

**Finite-comb cancellation and actual shifts.** Subtracting the linear
phase gives V_n'=V_n*(ell_n'(y)-ell_n'(0)) and

    V_n''=V_n*((ell_n'(y)-ell_n'(0))^2+ell_n''(y)).

The Gaussian integrals give bounded L1 first derivative and O(sqrt(n))
L1 second derivative; cutoff derivatives obey the same bound. For each
fixed s in [0,h], the intervals h*(m+1/2)+s+[0,h] tile the real line
up to endpoints. Integrating |f_n''| first in these intervals and then
in s gives exactly the factor h in (9), without sampling derivatives.
The cutoff sequence is finite, so shifting its Fourier sum twice has
no boundary terms. Both retained ordinate endpoints tend to +/-Y and
contain the cutoff support for large n. The at most 4q terms outside
the plateau are exponentially small by (5). This proves uniform (11)
without summing the original rational kernel on an infinite half-lattice.

At every interpolated ordinate, |F_n'|<=C*n by the same derivative
and Gaussian bounds. Multiplication by h*|e_m| proves (12). On a
fixed finite set of indices, Taylor's remainder for ell_n(h*v,z) is
O(v^2/n) uniformly in z. The remaining shifted-minus-unshifted terms
are bounded by C*sum_tail |e_m| independently of n. Both moving
endpoints eventually contain the fixed finite set. This order of limits
proves uniform (13), permitting the contour mean in (14). This is a
constant integral on the balanced circle, not an identification of the
original E_0 with an L2 norm on that circle.

**Prescription, periodic fold and normalized density.** Real e_m give
the absolutely convergent N(v) and |N(v)|<=v^2*Q2/2. On the plateau
the exact fixed-point equation, multiplied by i*v, is

    i*v*T(v/(2*pi))+N(v)=i*v*Q_w(v/(2*pi)).

L703 (10), including the reflected data sign, gives (16) at positive
and negative v. At zero this has removable value 0=0, and the original
equation gives T(0)=Q_w(0)=0. For the high band v0=v-2*pi lies
in [-3*pi/4,0). Periodicity of T gives explicitly

    S_e(v)=(v/v0)*chi_w(v0/(2*pi))
          +exp(i*v/2)*(N(v)-(v/v0)*N(v0)).

The high bump remains signed; its absolute value is used only after
this identity. The remainder bound is
(v^2+v*|v0|)*Q2/2=pi*v*Q2<7/60, using v<28/5 and pi>3.
The central remainder is <=25/512<7/60; the low band has none.
These bands partition the angular measure space, up to zero-measure
endpoints. Their combined remainder mean is <7/60, not three times
that cost. No ordinate symmetry is assumed.

Strict monotonicity of omega on (0,pi), its evenness and normalized
circle measure give p(v)=1/(pi*omega'(theta)). The exact replay
below places the whole central band between theta=2*pi/3 and
theta=arccos(-12/13). Here sin(theta)>=5/13 and
1+2*k*cos(theta)+k^2<=1 because 0<=k<=8/11<1. Integrating
2*k*(1-k^2) over t gives C in (18), hence p<=3/4. The periodic
support restricts T on this band to the two intervals before (19).
Their images in one period are disjoint, so Parseval bounds their
total squared integral by 2*pi*Q2. Cauchy--Schwarz then gives (19).

For a bump interval of width delta, truncate its preimage at a frequency
endpoint if needed. On its preimage [alpha,alpha+ell], integration
of omega'>sin(theta)/8 gives

    delta >= (cos(alpha)-cos(alpha+ell))/8
          >= (1-cos(ell))/8 >= ell^2/(4*pi^2).

Thus its normalized full-circle mass, including the reflected angular
preimage, is ell/pi<=2*sqrt(delta). Both the low positive bump and
the high folded negative bump have delta<=4*pi*w. The comparison of
f_bal and f_1 gives omega_*>=15138/15125, so the low frequency
and |v0| on the high bump exceed one. Their combined cost is therefore
<(1+11/2)*(7/160)=91/320. These checks prove (22), without any
bound on Phi off its plateau. Uniform convergence in (14) now gives
the eventual real-part margin in (1).

**Complete rational replay and original-D quantifiers.** The producer
`scripts/one-sided-hankel/actual-angular-mean-bounds-214.py` was read
in full. An independent replay uses the quadratic's vertex form to
verify every denominator extremum, positive numerator, raw ratio,
outward-rounded contribution, contiguous cell index and both sums in
all 256 stored cells. It recomputes all constants and all 12 checks
instead of trusting stored booleans. Two check names say "below" but
encode equalities (the residual budget and budget total); these are
arithmetic identities, with the strict inequalities justified analytically
above. All six extra arithmetic/clearance checks pass. Full exact replay:
`scripts/one-sided-hankel/balanced-angular-mean-audit-216.json`;
reproduce with
`python3 scripts/one-sided-hankel/balanced-angular-mean-audit-216.py`.
The replay verifies ancillary rational bounds only; the analytic limits,
fold and measure argument are checked above.

Successive nonanchor ordinates have gaps at least 3*h/4, distance
from the anchor at least 3*h/8, and absolute value <Y. There are
exactly 4q+1=M=n/3 distinct unit mass poles with
|a|^2<353/200<(R-1/100)^2. These verify every family hypothesis
of L661's general envelope. In particular sum_a r_a^2=M and its
diagonal is exactly the original D. The rational c_0 is continuous on
the original circle, so normalized L2 constant projection gives
E_0>=|mu_n|^2. Dividing the resulting bound by n^2*exp(-n/16)
gives

    3*sigma^2*exp(-6)*a0^2 * exp(261*n/10000)/n^3 -> infinity.

This proves (2) for every sufficiently large allowed n for one fixed
profile. It supplies neither a uniform onset for all L666 displacement
families nor an effective onset, the general paid-arc criterion, or an
independently audited quadrature/Jensen assembly. The audit accepts the
existing local derivation: reproduction and validation, not a result
beyond L726, certified originality or a complete RH candidate.

### 8. Separate downstream assembly audit — 3 November 2026, step 218

The invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-03-fixed-profile-jensen-assembly-audit.md`
covers exactly this audit. Take (2), already accepted in Section 7,
as input; its contour and Picard proof is not repeated. The present
specialization checks L666's observation/Jensen application and L658's
localization for this fixed profile. It does not use L664's two-offset
symmetry or uniform onset. The parked general signed-flow estimate in
L666 Section 6 remains unresolved. The new input distinguishing this
application from that stop is (2), with its fixed-profile quantifier.

**Admissibility and unchanged objects.** For every q>=1, n=12q+3>=15,
there are M=4q+1=n/3 distinct poles, all with original mass one.
The nonanchor gaps are at least 3h/4, the distance to the anchor is
at least 3h/8, and |y_m|<9/20. Thus

    |a|^2<353/200<(273/200)^2=(R-eta)^2<U.

This checks L658's hypotheses with N=M, positive integer residues
and the same x,R,U,eta. In particular D>0 is finite and is exactly
the diagonal in L658 and L666: no mass, weight or denominator has
changed. The finite index range -2q<=m<2q retains both endpoints.
All products use j=0,...,n-1 and the inverse angular factor; the
j=0 quotient is x/a. Every one of the M prescribed spatial moments
remains in G, even when its actual polynomial degree is smaller.

**Observation, signs and normalized energy.** The rational continuation
of W_a is exactly that displayed in the hypotheses. Its possible finite
poles are p_j=t_j*x/U and a/t_j (1<=j<n); each is simple. For a=x
they cancel. For a!=x, p_j are interior real points, a/t_j are exterior,
and both W_a(0) and W_a(infinity) equal x/a. Therefore c_0 and every
W_a satisfy the ordinary order <=1 and combined zero/infinity order
0<=1 requirements of Danchenko--Semin,
[arXiv:1503.06476v1, Section 1.1, Theorem 2, pp.1--2](https://arxiv.org/pdf/1503.06476v1),
with r=s=1. Pole cancellations cannot increase orders.

The common interior set is L666's S: zero, the p_j and
t_j/conjugate(a) for a!=x. The latter are nonreal. Equality of two
such points forces the same j and a by comparing real parts after
cross multiplication, since Re(a)=x!=0. Thus S has
K=1+M(n-1) distinct points, all of modulus <4/5. Its reflected
completion contains every possible pole; unused completion points
are allowed. The boundary argument of Bcal has strictly positive
derivative mu=sum_(z in S)(1-|z|^2)/|u-z|^2 and total increase
2pi K. Hence Bcal^2=e^(i phi) has 2K distinct boundary nodes.

Dividing the cited quadrature formula by the original circle length
2pi gives w_l=1/(2mu(u_l)). Applying it to 1 gives sum_l w_l=1;
applying it to c_0 and separately to each W_a gives exactly L666
(1)--(2). In the former, the full signed sum is formed before its
modulus square. These are observation weights, not changed spatial
masses. The z=0 Poisson term is 1 and every other term lies between
1/9 and 9, giving L666 (3) as well. No coercivity is inferred from
the positive weights; (2) above is the independent scalar premise.

The rational c_0 is nonzero because
Re c_0(infinity)=R^(-1)sum_a d^2/(d^2+y_a^2)>0. It has no boundary
pole, so E_0>0. The exact positive quadrature therefore supplies a
node u_l with |c_0(u_l)|>=sqrt(E_0)>0. All these statements concern
the original angular circle, not the balanced contour used earlier.

**Full spatial roots and logarithmic integrability.** Import the complex
root-mean formula, including boundary roots, from Brunault--Zudilin,
*Many Variations of Mahler Measures*, ISBN 9781108794459,
[Propositions 1.4--1.5, pp.6--7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf).
For P=G(u_l,.) the constant coefficient is nonzero. Its actual
factorization has nonzero roots alpha and gives

    mean log|P|=log|lead(P)|+sum_alpha log max(1,|alpha|)
              >=log|lead(P)|+sum_alpha log|alpha|
              =log|c_0(u_l)|.

A constant P uses empty sums. This is precisely L664 Section 5's
polynomial specialization, with a possibly complex constant coefficient;
no conjugate-pair argument is needed. It retains the leading factor,
all roots and actual degree drops. Consequently L666 (4) gives

    H>=log|c_0(u_l)|> -infinity,
    H>=(log E_0)/2.                                    (A1)

The other slices required for localization were also checked. In L657's
clearing G=K/Q, Q=C_x product_(a!=x)A_a has no angular boundary zero
and angular degree N(n-1); K has angular degree at most N(n-1).
For fixed boundary u, all W_a(u) are nonzero. If the first M moments
vanished, Lagrange interpolation at the N<=M distinct nodes a/R would
force each W_a(u)=0. Thus every spatial polynomial slice is nonzero.
For fixed boundary zeta, each nonanchor a supplies a unique uncancelled
exterior pole a/t_j of W_a. Comparing real parts after cross multiplication
excludes a pole shared with another W_b: Re(a)=Re(b)=x
forces t_j=t_k and a=b. Its coefficient in G is
R^(-1)sum_(k=0)^(M-1)(a*zeta/R)^k, which is nonzero since |a/R|<1.
The numerator factors at that pole are nonzero: A_x would require
a=x and C_a would require U=t_j*t_k<1, both impossible.
Hence no angular slice is identically zero either.

In particular the full K is a nonzero complex polynomial. Import
Issa--Lalin,
[arXiv:1203.5379v1, Remark 3.8 and Theorem 4.1/proof, printed p.7](https://arxiv.org/pdf/1203.5379v1),
with s=1: log|K| is absolutely integrable on the product torus.
Subtracting the bounded continuous log|Q| proves the same for log|G|,
also on every positive-length arc. Fubini is valid. At each fixed n
the nonzero spatial slices have finite root means. Since G is bounded
on the torus, Fatou applied to a common upper bound minus log|G|
makes m(theta)=mean_zeta log|G(e^(i theta),zeta)| upper semicontinuous.
It attains a finite maximum H. Neither a zero-free torus nor a bound
uniform in n for absolute logarithmic integrability is assumed.

**Localization with all denominator costs.** The inherited L658 argument
and L662/L664 scoped audits apply to these exact slices. Its disk
substitution w=(s+v)/(1+s*v), 0<s<1, has inverse angular Jacobian
P_s and yields the root mean log|1-s*gamma*u_0| for |gamma|<=1.
The identity

    |1-s*gamma*u_0|^2-s*|1-gamma*u_0|^2
                         =(1-s)(1-s*|gamma|^2)>=0

charges each numerator root by at worst (log s)/2. Actual angular
degrees are <=d_ang=N(n-1); since log s<0 this upper degree bound
has the correct direction. Each of Q's roots has reflected modulus
<4/5 and costs at most 4(1-s), by integrating
|gamma|/(1-v|gamma|)<=4 for s<=v<=1. All d_ang denominator factors
are kept, including common factors of K and Q. Absolute integrability
and bounded P_s justify the product integration. Therefore

    P_s*m >= m+(d_ang/2)log s-4d_ang(1-s).             (A2)

Choose a maximizer theta_m, h_arc=pi/n^2 and s=1-h_arc.
Here h_arc<1/4 and -log s<=4h_arc/3. Thus
P_s*(H-m)(theta_m)<=(14/3)d_ang*h_arc. On |t|<=h_arc,
P_s(t)>=7/(8h_arc). Since H-m>=0 on the entire circle, restriction
to the centered arc I_n of normalized length h_arc/pi=n^(-2) gives

    [7/(8pi)] mean_(I_n)(H-m)<=(14/3)d_ang*h_arc,
    mean_(I_n)m>=H-16pi^2/9,

using d_ang=N(n-1)<=n^2/3. This verifies L658's normalization and
constant. The maximizer is of m itself; no maximum is moved through
a spatial integral or identified with a diagonal-maximizing angle.

**Paid comparison and quantifiers.** For this fixed profile, (2) and
(A1) give H>=(log D)/2+log n-n/32 for all sufficiently large allowed n.
Substitute this in the last arc inequality and use log mu_arc(I_n)=-2log n:

    log mu_arc(I_n)+2 mean_(I_n x T)log|G|
      >=-2log n+2H-32pi^2/9
      >=log D-n/16-32pi^2/9.

This proves (3) with the same possible profile dependence and
ineffectiveness of the onset as (2). Localization itself has no further
asymptotic threshold. Both angular and spatial means are normalized;
mu_arc is arc length, not the quadrature function mu. No limiting
interchange in n, infinite extension of the finite poles, or deletion
of endpoints is used in this assembly.

The audit accepts this fixed-profile paid-arc input, not the general
displacement inequality, global angular charge, arbitrary support or
Xi signs. It is a reproduction and validation of the written implication
using named inputs and the already-audited scalar bound, not certified
originality or an RH candidate. No numerical diagnostic supplies a premise.

## Mathlib

Full matching coverage for this fixed-profile angular mean and finite-
comb limit was not checked. General complex contour integration,
Fourier/Parseval and dominated-convergence support would not by itself
establish the product-specific contraction, correction budget or (2).
No absence claim is made. Standard imported theorems and their precise
citations are separated from the above specialization. Section 7 is an
informal conceptual audit, not a formal verification or an independent
audit of the complete source manuscripts.
For Section 8, the inspected univariate supporting results remain
`Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`,
`Polynomial.intervalIntegrable_mahlerMeasure` and
`Polynomial.mahlerMeasure_mul` in
[Mathlib.Analysis.Polynomial.MahlerMeasure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html).
Full matching coverage for the rational observation, two-variable
localization and fixed-profile assembly has not been checked; no
absence or formal-verification claim is made.
