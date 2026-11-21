# Lemma 708: a fixed inner arc obstructs the absolute-envelope budget

## Hypotheses

Fix one actual L703 profile e before n varies, including its choices
of cutoffs and constants in (8)--(9). In particular its width w is
the width constructed there, not an arbitrary gap width. Use the full
L666 family, with

    d=5/4, x=-d, R=11/8, U=R^2=121/64, A=27/10, Y=9/20,
    n=12q+3, q>=1, M=n/3, h=A/n, t_j=j/n,
    a(y)=-d+i*y, y_m=h*(m+1/2+e_m), -2q<=m<2q,
    Z_n={x} union {a(y_m): -2q<=m<2q},
    W_a(u)=(x/a)*product_(j=1)^(n-1)
        [(x-t_j*u)/(a-t_j*u)]*[(U*u-t_j*a)/(U*u-t_j*x)],
    G_n(u,z)=R^(-1)*sum_(a in Z_n) W_a(u)
                                     *sum_(k=0)^(M-1)(a*z/R)^k,
    S_(n,1)(u)=max_(|z|<=1)|G_n(u,z)|,
    A_n(u)=R^(-1)*sum_(a in Z_n)|W_a(u)|,
    Cbar_n=mean_(|u|=1/2) log^+(A_n(u)/S_(n,1)(u)).

Means use normalized full-circle measure mu. Keep unit original
masses, W_x=1, the inverse denominator angle, the j=0 factor x/a,
both finite endpoints, the complete interior and all M moments.
L703 supplies E=sum_m|e_m|<infinity, |e_m|<=1/8 and its exact
Fourier prescription. L706 supplies nonzero slices and continuity
on |u|=1/2, so the ratios and finite-n means above are well-defined.
The auxiliary A_n does not replace the original squared diagonal D.

## Conclusion

There exist a fixed closed arc I of |u|=1/2, mu(I)>0, and fixed
epsilon>0 and N<infinity such that, for every allowed n>=N,

    S_(n,1)(u)<=A_n(u)*exp(-epsilon*n),       u in I,       (1)
    Cbar_n>=mu(I)*epsilon*n.                              (2)

All constants are independent of n and u in I; no effective arc,
rate or onset is asserted. Thus L707's stronger sufficient premise
Cbar_n=o(n) fails for this same actual fixed profile. This does not
refute B_sp=o(n), J_sp=o(n), or RH, and does not use L707's unaudited
transfer as a premise. Amplitude, full angular charge, H/support,
Xi realization and actual-Xi all-degree positivity remain unresolved.

A load-bearing estimate proved below is that on a fixed complex
neighborhood V of u=1/2, for some c,C>0,

    sup_(u in V, |z|<=1)|G_n(u,z)-1/(R+d*z)|
                                      <=C*exp(-c*n).      (3)

Only a subarc inside V is used in (1). This is a local mathematical
obstruction under the prior EXPLORE assessment, not a claim of
certified originality or a complete RH candidate. The separate conceptual
audit in Section 9 accepts (1)--(3) with these hypotheses and quantifiers.

## Proof

### 1. Source scope and reused analytic tools

The invocation-start assessment is
`drafts/literature/2026-11-03-spatial-cancellation-arc-attempt-scope.md`,
separately approved in step 162. Its parent compares inversion,
sampling and the prescribed vector, and preserves the existing stops.
The finite convolution/Fourier treatment used in L698 is reused with
a different center and a zero correction, not its radius-one theorem.
The ready primary reading record for those tools is
`drafts/literature/2026-11-03-centered-gap-full-spatial-arc.md`,
Section "Reused standard inputs", and its cited scalar assessments.
The following known results are imported, not reproved as new results:

* J. Kallsen and P. Kruehner, *On uniqueness of solutions to martingale
  problems -- counterexamples and sufficient criteria*,
  [arXiv:1607.02998v1](https://arxiv.org/pdf/1607.02998v1),
  11 July 2016, Appendix A, Lemma A.1(6),(9)--(11),(14), pp.29--30:
  finite complex-measure convolution, variation domination and Fourier
  multiplication. The inspected convolution norm proof is F. P. Maiale,
  *Analysis of Sublaplacians on Lie Groups*, 28 May 2019,
  [Definition 1.5 and Proposition 1.7, pp.8--9](https://poisson.phc.dm.unipi.it/~fpmaiale/notes/HAoLG.pdf).
* R. Vershynin, *High-Dimensional Probability*, first-edition author
  version, 20 May 2024,
  [Definition 2.7.5, p.33, and Theorem 2.8.1/proof, pp.36--37](https://webapps.math.uci.edu/~rvershyn/papers/HDP-book/HDP-1.pdf):
  for independent centered real sub-exponential X_j,

      P(|sum X_j|>=t)<=2 exp[-c_B*min(
          t^2/sum ||X_j||psi1^2, t/max ||X_j||psi1)],

  where c_B>0 is absolute. It is applied only to positive probability
  laws below, never to a complex measure.
* S. D. Miller, *Some notes on distributions*, 15 January 2006,
  [Theorems 4.1--4.2 and Section 6, pp.7--9](https://sites.math.rutgers.edu/~sdmiller/musagei/distributions.pdf):
  Schwartz Poisson summation and distributional Fourier duality.
  The passage to the present rational kernel is justified in Section 5.
* [NIST DLMF 1.14(iii), (1.14.17)--(1.14.18)](https://dlmf.nist.gov/1.14.iii):
  the exponential Laplace integral, used only with strictly positive
  real decay parameter.
* Hadamard's three-circles theorem, K. Ramachandra, *On the Mean-Value
  and Omega-Theorems for the Riemann Zeta-Function*, TIFR Lectures 85
  (1995), [Theorem 1.5.2 and proof, printed p.27, PDF p.37](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr85.pdf#page=37).
  For a function analytic near the closed comparison annulus, its
  maximum at r lies below M(r_1)^alpha M(r_2)^(1-alpha), where
  alpha=log(r_2/r)/log(r_2/r_1). Zeros are allowed. The maximum-modulus
  principle identifies disk maxima here.

The work required at this radius is the actual profile's off-bump
frequency margin, a complete signed finite-sum estimate, and an
absolute-envelope lower bound on a common fixed arc. No n-dependent
profile, generic near-nullvector or unpaid perturbation is used.

### 2. A frequency interval where the actual correction vanishes

For real r>0 define

    f_r(t)=1/(d+r*t)-t/(U*r+d*t),
    omega_0=A*integral_0^1 f_(1/2)(t)dt,
    omega_*=A*integral_0^1 f_1(t)dt,
    g=1/1000, J=(omega_0-g,omega_0+g).

First bound the width of the actual L703 construction. There its
phi(t)=-exp(-pi*i*t)/(2*pi*i*t) on the two fixed annuli, so its
constant B_0 is at least 4/pi. The fixed eta equals one on [-1/2,1/2]
and is nonnegative, hence ||eta||L1>=1. L703's displayed constants give

    B>=5*A_0=10*B_0*||eta||L1>=40/pi,
    r_Picard<=3/(64*pi^2*B),   M_Psi>=4/pi,
    w<=r_Picard/(8*M_Psi)<=3/81920,
    2*pi*w<3/10240<1/3000.                               (4)

The bound on M_Psi follows from its prescribed values arbitrarily
close to t=1/8; it does not require a new choice of Psi or r_Picard.
Thus (4) holds for every actual construction specified in the hypotheses.

Direct subtraction, with all denominators positive, gives

    f_1(t)-f_(1/2)(t)
      =t*(d^2-U/2)*(U-t^2)
        /[2*(d+t)*(d+t/2)*(U+d*t)*(U/2+d*t)].              (5)

On 1/2<=t<=1 lower-bound t and U-t^2, and upper-bound each
denominator by its value at 1. Integration over this half interval gives

    omega_*-omega_0
      >=A*(d^2-U/2)*(U-1)
        /[8*(d+1)*(d+1/2)*(U+d)*(U/2+d)]
       =4503/658945>1/200.                               (6)

Also

    A*(U-1)/[2*(d+1/2)*(U/2+d)]<=omega_0<=A/d=54/25.

The lower bound exceeds g, and 54/25+g<9/4<3*pi/4.
Equations (4)--(6) show that J is inside (0,3*pi/4) and strictly
below the positive bump support; it meets neither bump.

Put s_m=m+1/2 and define the actual signed correction on real v by

    S_e(v)=sum_(m in Z) [exp(i*v*(s_m+e_m))-exp(i*v*s_m)].

The series is locally uniformly convergent and |S_e(v)|<=E*|v|.
Termwise pairing with a compact smooth frequency test is justified
by this bound and sum|e_m|<infinity. Thus it is the continuous
positive-exponent Fourier transform of the shifted-comb difference.
Subtract the translated-comb identity from L703's exact prescription
F_(2pi)mu=1+delta_0-chi_w on (-3/8,3/8). The anchor and the zero
frequency atom cancel in that difference. Since chi_w is even,

    S_e(v)=-chi_w(v/(2*pi))=0,                v in J.      (7)

This is not an assumed complex-frequency continuation of S_e.
Only real frequencies in J will be paired with a finite measure.

### 3. Complex factors and the order of uniform choices

For complex u near u_0=1/2 and real y, set

    lambda_t=d+t*u, a_t=Re lambda_t,
    r_t=t*(d+t*u)/(U*u+d*t),
    Q_t(u,y)=r_t+(1-r_t)*lambda_t/(lambda_t-i*y).

Exact division of L666's factors, including j=0, gives

    W_(a(y))(u)=product_(j=0)^(n-1) Q_(t_j)(u,y).          (8)

On a sufficiently small fixed closed disk about u_0, Re u>0 and
a_t>=d. All displayed parameter denominators stay nonzero. Each
Q_t is the positive-exponent transform of the complex mass-one measure

    r_t*delta_0+(1-r_t)*lambda_t*exp(-lambda_t*v)1_(v>=0)dv.

Its variation mass and its normalized positive-law mean are

    z_t=|r_t|+|1-r_t|*|lambda_t|/a_t,
    m_t=|1-r_t|*|lambda_t|/(a_t^2*z_t).                   (9)

At u_0, 0<=r_t<1, z_t=1 and m_t=f_(1/2)(t). Moreover

    |Q_t(u_0,y)|^2
      =[1+t^2*y^2/(U/2+d*t)^2]/[1+y^2/(d+t/2)^2]<1

for y!=0. The strict inequality follows from U>t^2. On the two
compactified ranges |y|>=2/5 this is a uniform strict inequality:
the limits at both infinities are r_t, whose maximum over [0,1]
is strictly less than one. Choose kappa_0<1 bounding these moduli,
and kappa_1=(1+kappa_0)/2<1. Joint continuity, including those
infinities, preserves |Q_t(u,y)|<=kappa_1 on a fixed small disk.

Before finally shrinking that disk choose

    rho=sqrt(2824/3025)<1, tau=-log(rho)/3,
    b=c_B*min(g^2/(128*A^2),g/(8*A))>0,
    gamma=min(b/8,3/40,-log(kappa_1)/2)>0,
    alpha=log(301/300)/log(301/50)>0,
    0<epsilon_0<=min(b/4,1/40,alpha*gamma/4,tau/4).

Uniform continuity in t allows a single closed disk V about u_0 on
which, simultaneously,

    a_t>=d, z_t<=exp(epsilon_0),
    |m_t-f_(1/2)(t)|<=g/(4*A),
    |Q_t(u,y)|<=kappa_1 for |y|>=2/5.                     (10)

The normalized positive laws in (9) are zero/exponential mixtures
with exponential rates >=d. Their means are <=1/d, second moments
<=2/d^2, and centered psi1 norms <=4, since

    E exp(|X-E X|/4)
      <=exp(1/(4*d))/(1-1/(4*d))<=25/16<2.               (11)

Every choice above is fixed before n. In particular the variation
cost is chosen after the spatial interpolation weight alpha.

### 4. The complete resolvent on a small spatial disk

For |z-1/2|<=1/4 set beta=d+R/z. Elementary disk bounds give

    Re beta>=67/36>d, |beta|<=27/4,
    |beta|/Re beta<6, |R+d*z|>=27/16.                    (12)

The extra factor beta/(beta-i*y) is the transform of the complex
mass-one exponential measure beta*exp(-beta*v)1_(v>=0)dv.
Its normalized variation is a positive exponential law of rate
Re beta. Convolve this extra measure with all n factors in (8),
then push forward by multiplication by h. The resulting finite
complex measure nu, with positive majorant law P, satisfies

    k(s):=W_(a(h*s))(u)*beta/(beta-i*h*s)
          =integral exp(i*s*v)dnu(v),
    nu([0,infinity))=1, |nu|<=6*exp(epsilon_0*n)*P.        (13)

P is the law of V_n=h*(sum_(j=0)^(n-1)X_j+X_beta) for independent
positive variables with the laws just described. No independence or
randomness of the fixed e_m is assumed. Since f_(1/2) is decreasing,
its left Riemann-sum error is at most 1/(d*n). Hence (10) and the
extra mean give, eventually,

    |E V_n-omega_0|<=g/4+2*A/(d*n)<=g/2.

For n>=8*A/(d*g), Bernstein with n+1<=2n variables and (11) gives

    P(V_n outside J)<=2*exp(-b*n),
    E V_n^2<=(A/d)^2*[(1+1/n)^2+2*(n+1)/n^2]<16.         (14)

The second inequality holds for n>=15. All estimates are uniform
on V and the small spatial disk. From (7), (13), (14), and
Cauchy--Schwarz against P,

    |integral S_e(v)dnu(v)|
      <=6*E*sqrt(32)*exp[-(b/2-epsilon_0)*n].             (15)

In particular integral v d|nu| is finite, a fact needed for the
signed infinite pairing below. No probability assertion is made
about the complex nu itself.

### 5. Comb samples and both finite tails

The j=0 factor is an exponential of scaled rate lambda_0=d*n/A.
After its removal the extra exponential is still present, so the
remaining convolution is atom-free. Thus nu has a continuous density
p on the real line, zero for v<0 and with p(0)=0. This follows
directly by convolving the j=0 exponential with that atom-free finite
measure; dominated convergence applies at every positive point and
at zero. The positive majorant P has the same continuity property.

Writing V_n=h*X_0+S and tilting S by n/20, each of its n factors
has exponential moment <=250/223, since A/(20*d)=27/250.
As log(250/223)<=27/223<1/8, conditioning on S yields

    |p(v)|<=6*lambda_0*exp[(epsilon_0+1/8)*n-n*v/20], v>0,
    sum_(l>=1)|p(2*pi*l)|
       <=12*lambda_0*exp[-(7/40-epsilon_0)*n].             (16)

For the latter geometric sum use pi>3 and n>=15. Variation
domination first gives a density inequality almost everywhere;
continuity extends it to every sample in (16).

For fixed n,u,z the rational k has no real pole and is O((1+|s|)^(-2)),
because its j=0 factor and extra resolvent each decay like 1/s.
Multiply it by exp(-eta*s^2), eta>0, and apply Schwartz Poisson.
Finite-variation Fubini identifies its transform as 2*pi*(p*G_eta),
where G_eta(v)=(4*pi*eta)^(-1/2)exp(-v^2/(4*eta)). The bound (16)
has the form |p(v)|<=C_n exp(-a_n*|v|), a_n=n/20, on all real v.
For 0<eta<=1 it implies

    |(p*G_eta)(w)|<=2*C_n*exp(a_n^2)*exp(-a_n*|w|).

This follows from |w|<=|v|+|w-v| and the Gaussian exponential
moment. It is summable at w=2*pi*l for fixed n. Continuity of p,
p(0)=0, and absolute summability of k(m+1/2) therefore justify
both limits in Poisson, including the zero and negative samples:

    B_n:=sum_(m in Z)k(s_m)
       =2*pi*sum_(l>=1)(-1)^l*p(2*pi*l),
    |B_n|<=24*pi*lambda_0*exp[-(7/40-epsilon_0)*n].         (17)

The shifted lattice sum is also absolutely convergent. Termwise
differences satisfy the integrable Fubini bound
sum_m |e_m|*integral v d|nu|. Consequently the exact anchored identity is

    1+sum_(m in Z)k(s_m+e_m)
           =1+B_n+integral S_e(v)dnu(v).                 (18)

The anchor equals k(0)=1. Equations (15)--(18) keep the signed
correction and every comb term; no finite-measure theorem has been
applied to the infinite unit-mass counting measure.

To truncate, (8), (10) and the exact j=0 factor give, for |y|>=2/5,

    |W_(a(y))(u)|<=d*kappa_1^(n-1)/|y|,
    |beta/(beta-i*y)|<=48/|y|,
    |W_(a(y))(u)*beta/(beta-i*y)|<=60*kappa_1^(n-1)/y^2.  (19)

For the middle bound, |y|<=|beta-i*y|+|beta|<=7|beta-i*y|
and (12) suffice. Both omitted tails start at |h*s_m|>=Y,
and |h*(s_m+e_m)|>=Y-h/8>2/5 for n>=15. Also
|s_m+e_m|>=(3/4)|s_m|. Summing both tails in (19) gives

    sum_(m>=2q or m<=-2q-1)|k(s_m+e_m)|
      <=60*kappa_1^(n-1)*(32/9)*h^(-2)/(2q-1/2)
      <=300*n*kappa_1^(n-1).                            (20)

Here 2q-1/2>=n/10 and the reciprocal-square sum is bounded by
its integral. No symmetry, truncated-profile Fourier gap or Gevrey
tail approximation enters this estimate.

Define the original finite rational resolvent

    F_n(u,z)=sum_(a in Z_n)W_a(u)/(R-a*z), H(z)=1/(R+d*z).

Its finite sum equals the truncated left side of (18) divided by
R+d*z, by the exact identity
W_(a(y))(u)/(R-a(y)*z)=W_(a(y))(u)*beta/[(beta-i*y)*(R+d*z)].
Using (12), (15), (17), (20), and the prior choices of gamma and
epsilon_0, absorbs all polynomial prefactors and proves

    sup_(u in V, |z-1/2|<=1/4)|F_n(u,z)-H(z)|
                                       <=C_0*exp(-gamma*n). (21)

### 6. Spatial continuation and all M moments

Every retained node satisfies |a|^2<353/200. Every possible spatial
pole R/a of F_n, including the anchor pole of H, obeys

    |R/a-1/2|^2=1/4+(U+R*d)/|a|^2
       >6481/2824>(151/100)^2.

Thus F_n-H is analytic near |z-1/2|<=301/200. On that disk
|R-a*z|>d*(151/100-301/200)=1/160. From (8)--(10), or directly
from the total variation of the n base factors, |W_a(u)|<=exp(epsilon_0*n).
Therefore

    sup_(|z-1/2|<=301/200)|F_n-H|<=C_1*n*exp(epsilon_0*n). (22)

Apply three-circles to the finite analytic function F_n-H, with
radii 1/4, 3/2 and 301/200. Its weight is exactly alpha chosen in
Section 3. Equations (21)--(22) give exponential rate at least
alpha*gamma-(1-alpha)*epsilon_0>=3*alpha*gamma/4. Absorbing
the remaining power of n, and using |z-1/2|<=3/2 when |z|<=1, gives

    sup_(u in V, |z|<=1)|F_n-H|<=C_2*exp(-alpha*gamma*n/2). (23)

Only the original finite rational function is continued. The infinite
Laplace pairing remains restricted to the small disk where Re beta>d;
no infinite resolvent is continued through an inadmissible parameter.

Finally the exact finite M-term identity is

    G_n=F_n-T_n,
    T_n(u,z)=sum_(a in Z_n)W_a(u)*(a*z/R)^M/(R-a*z).

All nodes have |a|/R<=rho<1. For |z|<=1 the complete remainder obeys

    |T_n(u,z)|<=n/[3*R*(1-rho)]*exp[-(tau-epsilon_0)*n]
                                         <=C_3*exp(-tau*n/2). (24)

Together (23)--(24) prove (3), with
c=min(alpha*gamma/2,tau/2)>0. In particular S_(n,1)(u)<=9 on
V for sufficiently large n, since max_(|z|<=1)|H(z)|=1/(R-d)=8.
Both endpoint sums and every finite spatial coefficient have been paid.

### 7. An exponential envelope on a fixed subarc

For u near u_0 and y near zero define

    Phi(u,y)=integral_0^1 log|Q_t(u,y)|dt,
    Omega(u)=A*integral_0^1 [1/(d+t*u)-t/(U*u+d*t)]dt.

The factors in this compact neighborhood are nonzero. Phi is smooth
in its real variables, Phi(u,0)=0, and Omega is holomorphic in u.
Differentiating (8)'s individual factor at y=0 gives

    partial_y Phi(u,0)=-Im Omega(u)/A.                    (25)

At real r=1/2,

    Omega'(r)=A*integral_0^1 t*
                    [U/(U*r+d*t)^2-1/(d+r*t)^2]dt>0.     (26)

For t>0 the integrand is positive because
R*(d+r*t)-(U*r+d*t)=(R-t)*(d-R*r)>0; R>1 and d-R/2=9/16.
Thus

    d/dtheta Im Omega((1/2)*exp(i*theta)) at theta=0
                                           =(1/2)*Omega'(1/2)>0.

Choose a fixed sufficiently small theta_1>0 with
u_1=(1/2)exp(i*theta_1) in the interior of V and Im Omega(u_1)>0.
By (25), some fixed y_* in (-Y,0), sufficiently close to zero,
satisfies Phi(u_1,y_*)>0. Continuity gives a closed positive-length
arc I about u_1, inside V on |u|=1/2, a small interval about y_*,
and eta_*>0 such that Phi(u,y)>=3*eta_* on their product.

Uniform Riemann comparison of the exact product (8), on this compact
set with no factor zeros, gives

    (1/n)*log|W_(a(y))(u)|=Phi(u,y)+o(1),

uniformly in u,y there. Choose an integer m_n nearest to
n*y_*/A-1/2. Then m_n lies in [-2q,2q) for all sufficiently large
n, and its actual displaced ordinate satisfies

    |y_(m_n)-y_*|<=5*A/(8*n).

The cap |e_(m_n)|<=1/8 alone proves this bound. It selects an
existing node, without changing the fixed profile or any mass.
The uniform Riemann estimate therefore gives, eventually on I,

    |W_(a(y_(m_n)))(u)|>=exp(2*eta_*n),
    A_n(u)>=R^(-1)*exp(2*eta_*n).

Combine this with S_(n,1)<=9 from Section 6. Increasing the single
onset to absorb 9R gives S_(n,1)/A_n<=exp(-eta_*n), proving (1)
with epsilon=eta_*. Nonnegativity of log^+ on the complement and
integration over I with full-circle normalized measure prove (2).

This is an actual prescribed-vector lower bound on the cancellation
budget, not the lower bound on a failed upper certificate in L707.
It stops only that stronger sufficient budget. The exponential
comparison uses a fixed tilted arc, not a point or a shrinking set.

### 8. Auxiliary arithmetic and verification limits

Run `python3 scripts/one-sided-hankel/spatial-cancellation-arc-163.py`.
Its full exact-rational certificate is
`scripts/one-sided-hankel/spatial-cancellation-arc-163.json`.
It checks the frequency and width separation, the frequency-domain
endpoints, spatial-pole margin, moment and two-tail constants: 15
checks, no failures. Bounds involving pi use only 3<pi<4.
No computed profile, sampled angle, numerical asymptotic, or finite
precision calculation is a premise. The certificate does not verify
the analytic proof, source hypotheses, existential constants or onset.
The separate conceptual audit below checks the analytic argument; the
arithmetic certificate alone does not supply that audit.

### 9. Separate conceptual audit — 3 November 2026, step 164

This audit reuses the unchanged invocation-start EXPLORE assessment in
Section 1. It checks the complete proof above and its direct interfaces
with L666, L703 and L706. The existing primary theorem assessments are
reused with their stated reading limits; no manuscript-wide source audit
or stronger external theorem is claimed. L707's definitions agree with
the present ones, but its unaudited transfer is not an input to (1)--(3).

**Actual width and real-frequency prescription.** L703's (8)--(9)
fix B, r_Picard and w in this order. On its annuli the supremum of
|phi| is 4/pi, and the prescribed values of Psi approach modulus
4/pi at the inner endpoint. Together with ||eta||_1>=1 these give
precisely (4), for any of the permitted fixed initial cutoffs. No
choice is enlarged after n is introduced. Subtracting the two rational
expressions for f gives (5); on [1/2,1] its numerator is bounded below
by (d^2-U/2)*(U-1)/2, before the displayed denominator factor 2.
The interval length 1/2 yields (6). The complete auxiliary check gives

    (omega_*-omega_0) - g - 2*pi*w
        > 186931441/33737984000 > 0.

The lower and upper bounds on omega_0 place all of J strictly inside
(0,3*pi/4). Subtracting the anchor and translated lattice from L703's
identity leaves -chi_w in the negative-exponent convention. Reflection
to the positive-exponent convention changes its argument's sign; chi_w
is even. The l1 bound on e gives local uniform convergence of S_e and
identifies this distribution with the continuous function in (7).
Thus S_e vanishes on J as a real-frequency identity, with no analytic
continuation of the displacement transform.

**Complex variation and probability normalization.** Direct multiplication
gives Q_t=(lambda_t-i*r_t*y)/(lambda_t-i*y), including Q_0=d/(d-i*y).
At u_0 every r_t is in [0,1), since U>t^2; hence z_t=1. The modulus
formula and its limits as y tends to either infinity give a uniform
kappa_0<1 on the compactified set in Section 3. Continuity permits
shrinking one disk after kappa_1, b, gamma, alpha and epsilon_0 have
been fixed. All denominators stay nonzero there. There is no circular
choice of the concentration rate or interpolation weight.

The normalized variation of each factor is exactly the probability
mixture used in (9). Its exponential part has real rate a_t>=d, so
its mean is at most 1/d and its second moment at most 2/d^2. The
inequality exp(1/5)<=5/4 verifies (11) and the centered psi1 bound 4.
The extra factor has Re beta>=67/36>d and variation at most 6.
Only these independent positive laws enter Bernstein. Their total
centered psi1-square sum is at most 32*n; with threshold n*g/(2*A),
the theorem gives exactly b in Section 3. Since f_(1/2) is decreasing,
its left Riemann-sum error is at most 1/(d*n). This proves the mean
margin in (14), including the extra exponential. Its second-moment
bound and Cauchy--Schwarz give (15), retaining exp(epsilon_0*n).

**Zero sample, smoothing, and both tails.** Removing Q_0 leaves the
extra exponential, so the remaining finite convolution is atom-free.
Convolution with Q_0's exponential density is continuous and zero at
zero: the only possible moving discontinuity is at the boundary of
the half-line, and an atom-free measure assigns that point mass zero.
This applies both to the complex density p and to its positive majorant.
No half-density term remains at the zero Poisson sample.

For the tail bound, write lambda_0=d*n/A and s=n/20<lambda_0. For
0<=S<=v,

    exp[-lambda_0*(v-S)]<=exp[-s*v+s*S].

Each of S's n factors has exponential moment at s bounded by 250/223.
This proves the pointwise density bound (16), after using continuity
to extend variation domination from almost everywhere. Its sample sum
has first exponent at least (3/10-1/8-epsilon_0)*n and geometric
denominator at least 1/2 for n>=15, giving the stated 7/40. The
Gaussian domination has a constant depending on fixed n, which is
sufficient: eta tends to zero for that n first. Absolute summability
of k(m+1/2) controls the other side of Poisson. The resulting uniform
bound in n is then (17), not a bound on the Gaussian constant.

The shifted differences are summable by E*integral v d|nu|, so Fubini
in (18) is legitimate. The first omitted unshifted ordinate has absolute
value exactly Y, on each side; its shifted absolute value is at least
171/400>2/5 for n>=15. The j=0 decay and extra resolvent give 1/y^2
in (19). Using |s_m+e_m|>=(3/4)|s_m| on both tails gives the constant
640000/2187<300 in (20). No absolute Gevrey-tail error is substituted
for this signed full-comb calculation.

**Spatial continuation and all moments.** The small disk has Re z>=1/4,
|z|<=3/4 and |z|>=1/4, which suffice for every bound in (12). Every
spatial pole, including H's, is farther than 151/100 from 1/2, whereas
the outer interpolation radius is 301/200. Thus the denominator bound
1/160 applies throughout that closed disk. Only the original finite
resolvent is continued; the infinite pairing is used solely in its
convergent small disk. Three-circles permits zeros, and an identically
zero difference is immediate. Its exact weight is
alpha=log(301/300)/log(301/50)>0, however small.

The three small-disk error rates before absorption are at least b/4,
3/20 and -log kappa_1. Each strictly exceeds gamma. After interpolation
the rate is at least 3*alpha*gamma/4, leaving alpha*gamma/2 after the
polynomial factor is absorbed. The exact M=n/3 remainder has rate
tau-epsilon_0>=3*tau/4, leaving tau/2 after its factor n. All choices
precede n and use a single final onset. This verifies (3) on the whole
spatial unit disk, rather than at selected moments or resolvent samples.

**The common fixed arc and the average.** The logarithmic derivative
of Q_t at y=0 is i*[1/(d+t*u)-t/(U*u+d*t)], giving the minus sign in
(25). The factorization (R-t)*(d-R/2)>0 verifies (26), so a small
positive angular tilt inside the already fixed V has Im Omega>0.
A fixed small negative y_* then gives positive Phi. Continuity and a
uniform Riemann-sum limit on a zero-free compact set provide one arc
and ordinate interval before selecting m_n. The cap 1/8 gives the
5*A/(8*n) approximation by an existing retained node. No profile or
mass changes with n. Consequently the lower envelope exponent and
S_(n,1)<=9 hold on the same fixed arc for all sufficiently large n.
The positive rate epsilon=eta_* survives absorption of 9R.

L706's nonzero-slice argument uses all M distinct nodes and W_x=1;
its pole exclusion on |u|=1/2 follows from j=121n/160 being impossible
for odd n. Hence A_n and S_(n,1) are positive continuous functions on
that circle for each n. The finite means exist, and integrating the
pointwise log^+ lower bound on I gives (2) without any n-limit/Fubini
interchange or assumption on the complementary arc.

The audit finds no substantive error or additional premise. All 15
auxiliary inequalities were replayed and their complete exact values
inspected in the step-163 certificate; they do not certify the analytic
steps above. This establishes the previously unaudited restricted input
locally, not a new mathematical result beyond L708. The stronger
Cbar_n=o(n) subroute is stopped. No conclusion about B_sp=o(n),
J_sp=o(n), effective constants/onset, full charge, amplitude, H/support
or Xi realization follows, and no RH candidate is asserted.

## Mathlib

Full matching coverage for (1)--(3), the actual profile and its
Fourier prescription has not been checked. No absence or formal
verification is claimed. The named convolution, Fourier, Bernstein
and three-circles imports are informal inputs with the precise source
references above. Their local specializations and this proof were checked
in Section 9; this is not a formal verification or a manuscript-wide
audit of those sources.
