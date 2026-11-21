# Lemma 709: phase-sensitive normalization on an imaginary angular arc

## Hypotheses

Fix one actual L703 profile e before n varies, including its prescribed
cutoffs and width. Use L666's complete family, with

    d=5/4, x=-d, R=11/8, U=121/64, A=27/10, Y=9/20,
    n=12q+3, q>=1, M=n/3, h=A/n, t_j=j/n,
    a(y)=-d+i*y, y_m=h*(m+1/2+e_m), m in Z,
    Z_n={x} union {a(y_m): -2q<=m<2q},
    W_n(u,y)=(x/a(y))*product_(j=1)^(n-1)
       [(x-t_j*u)/(a(y)-t_j*u)]*[(U*u-t_j*a(y))/(U*u-t_j*x)],
    G_n(u,z)=R^(-1)*sum_(a in Z_n) W_a(u)
                                      *sum_(k=0)^(M-1)(a*z/R)^k.

Here W_a=W_n(u,Im a), including W_x=1. The inverse angular factor,
j=0, unit masses, both finite endpoints, signed interior and all M
moments are retained. In particular E=sum_m|e_m|<infinity and
|e_m|<=1/8. The virtual endpoint a_-=-d-iY is used for normalization;
it is not an additional atom. Put

    s=65/64, rho=sqrt(2824/3025), v=s*rho,
    S_(n,r)(u)=max_(|z|<=r)|G_n(u,z)|,
    F_n(u,z)=sum_(a in Z_n) W_a(u)/(R-a*z),
    T_n(u,z)=sum_(a in Z_n) W_a(u)*(a*z/R)^M/(R-a*z).

Thus G_n=F_n-T_n exactly. Every retained node has |a|/R<rho and
v^2=59657/61952<1. No absolute-envelope cancellation premise is used.

## Conclusion

There are a fixed closed positive-measure arc I_0 of |u|=1/2 about
i/2, constants C,N, and a continuous function D_-(u) with
Re D_-(u)>1/25, such that, uniformly on I_0 along every allowed n,

    G_n(u,1/2)/W_n(u,-Y)
      -> -1/[(R-a_-/2)*(1-exp(-A*D_-(u)))],                (1)
    S_(n,1)(u)>=exp(n/50),                       n>=N,    (2)
    max_(|z|<=s)|T_n(u,z)|/S_(n,1)(u)
                         <=C*exp(-n/500),        n>=N.    (3)

In (1),

    D_-(u)=integral_0^1 i*[1/(d+t*u+iY)
                              -t/(U*u+d*t+i*t*Y)]dt.

The limiting coefficient in (1) is nonzero. The new input pays an
actual normalization and the relative finite-moment remainder on a
previously unpaid arc. It does NOT bound max_(|z|<=s)|F_n|/S_(n,1),
prove B_sp=o(n), give a positive lower limiting B_sp/n, or settle the
complementary Jensen defect. Full angular amplitude/charge, H/support,
Xi realization and actual-Xi positivity remain independent.

The constants and onset are existential and may depend on the fixed
profile. The separate conceptual audit in Section 8 accepts (1)--(3).
This is not certified originality or an RH candidate. The
arithmetic certificate below is rigorous auxiliary evidence; it does
not independently verify the analytic proof.

## Proof

### 1. Scope and imported identities

Reuse the unchanged invocation-start assessment
`drafts/literature/2026-11-03-spatial-doubling-growth-attempt-scope.md`.
The attempt addresses its full-family B_sp observable by paying its
actual denominator and finite tail on a new arc. L707's stopped
interpolation certificate, L708's absolute-envelope obstruction, and
C708a's two local growth arcs are comparisons, not premises here.

Use L708 Sections 2--5 and its separate audit for the exact factorization,
real-frequency prescription, complex finite-convolution construction
and Gaussian-regularized Poisson identity. Their standard inputs are
J. Kallsen and P. Kruehner, *On uniqueness of solutions to martingale
problems -- counterexamples and sufficient criteria*,
[arXiv:1607.02998v1](https://arxiv.org/pdf/1607.02998v1), Appendix A,
Lemma A.1(6),(9)--(11),(14), pp.29--30, and S. D. Miller,
*Some notes on distributions*, 15 January 2006,
[Theorems 4.1--4.2 and Section 6, pp.7--9](https://sites.math.rutgers.edu/~sdmiller/musagei/distributions.pdf).
The exponential transform is
[NIST DLMF (1.14.17)--(1.14.18)](https://dlmf.nist.gov/1.14.iii),
with strictly positive real decay parameter. Their source qualifications
are unchanged. The only contour theorem used is Cauchy's integral
theorem on a pole-free rectangle, with its vertical integrals explicitly
controlled below. No complex-saddle or nonreal-frequency gap theorem is
imported. The necessary changed rate estimates are proved here.

Write, including t=0,

    lambda_t=d+t*u, r_t=t*(d+t*u)/(U*u+d*t),
    Q_t(u,y)=r_t+(1-r_t)*lambda_t/(lambda_t-i*y),
    W_n(u,y)=product_(j=0)^(n-1)Q_(t_j)(u,y).             (4)

For u close to i/2, Re lambda_t>1 and U*u+d*t is bounded away from
zero uniformly in t. At t=0, Q_0=d/(d-i*y). These facts verify the
finite complex-measure hypotheses; no positive-law bound is substituted
for the phase of the convolution.

### 2. Complete rational certificates for the limiting product rates

At u=i/2, for real X,c and D=d+c, direct division in (4) gives

    |Q_t(i/2,X+i*c)|^2
      =[(d^2+t^2/4)*(t^2*D^2+(U/2-t*X)^2)]
         /[(d^2*t^2+U^2/4)*(D^2+(t/2-X)^2)].             (5)

Let Phi_c(X) be the integral from 0 to 1 of half the logarithm of
(5). Its X derivative is the integral of

    (t/2-X)/(D^2+(t/2-X)^2)
              -t*(U/2-t*X)/(t^2*D^2+(U/2-t*X)^2).      (6)

The exact certificate establishes

    sup_(X real) Phi_(3/20)(X)<-41/1000,
    sup_(X real) Phi_(-1/10)(X)<74/1000,
    sup_(X real) Phi_0(X)<24/1000,
    Phi_0(-Y)>51/2500,        Phi_0(Y)<-1/10,
    Phi'_0(X)>1/25,                   -1<=X<=-Y.        (7)

Here are the full reductions that make a finite certificate sufficient.
For t>0 put a_t=U/(2t), b_t=t/2. The X-dependent logarithm in (5)
is half log[(D^2+(X-a_t)^2)/(D^2+(X-b_t)^2)]. We have a_t>b_t,
a_t*b_t=U/4 and a_t+b_t>=R. Its derivative has the sign of
(X-a_t)*(X-b_t)-D^2. For X<=-1 this sign is positive, since
1+R+U/4>(7/5)^2>=D^2 for all three c in (7).
For X>=0 the logarithm first decreases and then increases toward
its value at infinity, which is smaller than its value at zero.
Indeed D^2>U/4 makes its first critical point negative, and
a_t^2>b_t^2 gives the latter comparison. Consequently each factor's
maximum over the real line occurs in [-1,0]. The t=0 factor obeys
the same bounds directly. This proves the reduction for the three
suprema, without a grid assertion outside the certified interval.
Also, for every X>=Y each factor is bounded by its value at Y:
the same single-minimum argument applies and a_t+b_t>=R>2Y makes
its value at Y exceed the limit at infinity.

For completeness the error bounds used inside the interval are as
follows. The logarithmic integrand is

    log|d+i*t/2|-log|d*t+i*U/2|
       +log|t*D+i*(U/2-t*X)|-log|D+i*(t/2-X)|.

For -1<=X<=Y and -1/10<=c<=3/20, the moduli of the four linear
factors are respectively at least d, U/2, 4/5 and 23/20. For the
third, negative X gives the stronger bound U/2; for nonnegative X
minimizing its squared modulus gives the bound
(U/2)^2*(23/20)^2/[(23/20)^2+Y^2]>(4/5)^2. Its slope modulus is
at most sqrt((7/5)^2+1)<7/4. The formula
(log L)^(4)=-6*(L'/L)^4 for a nonzero affine L therefore bounds
the absolute fourth t derivative of the real logarithmic integrand
by 256. Differentiating (6) four times in t bounds it by 512: the
two contributions are at most

    24*(U/2)*(7/4)^3/(4/5)^5
                       +24*(1/2)^4/(23/20)^5<512.

In X, the second derivative of the logarithmic integrand is at most
2/D^2 in absolute value, by the two real quadratic factors. These
are bounds on the complete integrands, not on sampled values.

Use composite Simpson sums with N_t=32 even panels. The elementary
cubic Taylor remainder on a pair of panels of half-width h_t bounds
the error by K*h_t^5*(1/60+1/36). Summing the N_t/2 pairs gives
K/(45*N_t^4). Thus no uninspected sharper quadrature theorem is needed.
On each of 200 X cells covering [-1,0], the midpoint rate enclosure,
the enclosed derivative times the cell radius, and radius^2/D^2 give
an upper bound on the ENTIRE cell. The derivative lower bound on
[-1,-Y] uses 200 cells and the Lipschitz constant 2/d^2 for (6).

All logarithms of positive rationals are enclosed with integer-directed
rounding at scale 2^100, using

    log r=2*sum_(k=0)^39 z^(2k+1)/(2k+1)+remainder,
    z=(r-1)/(r+1),             1<=r<=2.

The positive remainder is at most 8/[3*81*2^81], a deliberately
larger bound obtained from z<=1/2; reciprocation and powers of two
cover every positive rational. The script stores every cell enclosure.
Its final rigorous upper bounds for the first three lines are below
-0.0411628, 0.0735360 and 0.0236545, respectively; the negative
endpoint lower bound exceeds 0.0205105 and the derivative lower bound
exceeds 0.0448634. These displayed rounded weakenings are not used
as exact arithmetic. The exact rational values are in the certificate.
The positive endpoint upper bound is also below -1/10.

Reproduction command and full evidence:

    python3 scripts/one-sided-hankel/spatial-complex-phase-166.py
    scripts/one-sided-hankel/spatial-complex-phase-166.json

All 21 comparisons pass. The script and the derivative/halfline
arguments together prove (7); finite samples alone would not.

### 3. Uniform finite products and the two legitimate contour shifts

All inequalities in (7) are strict. On any fixed bounded X interval,
the factors in (5) are nonzero; continuity therefore preserves the
integral inequalities on a sufficiently small fixed closed complex
neighborhood V of i/2. Uniform bounded t derivatives there give the
finite-product Riemann comparison

    log|W_n(u,X+i*c)|
       =n*integral_0^1 log|Q_t(u,X+i*c)|dt+O(1).         (8)

There is no logarithm-branch choice in this real identity.
The assertions at large |X| also extend uniformly. Indeed Q_t tends
uniformly in t to r_t, and at the center

    |r_t|^2<=|r_1|^2=29696/40241<(9/10)^2.

Monotonicity of t^2*(d^2+t^2/4)/(d^2*t^2+U^2/4) follows by
differentiation; its numerator after clearing positive denominators
has positive coefficients. Choose a fixed large L and then shrink V
so |Q_t(u,X+i*c)|<=9/10 for |X|>=L and the three c in (7).
Retain Q_0 separately for a factor C/(1+|X|). Since log(9/10)<-1/10,
these tails are smaller than all three asserted global upper rates.
Together with (8) on [-L,L], this proves uniform product bounds with
the exact rates in (7) and one constant C. This step avoids assuming
uniform logarithmic differentiability at t=0, |X|=infinity.

Set beta=4 and

    k_n(u,y)=W_n(u,y)*4/(4-i*y).

This is the extra resolvent for z=1/2. Convolve the n complex
mass-one measures in (4) with 4*exp(-4v)1_(v>=0)dv and scale by h.
Its density p_(n,u) has positive-halfline support, is continuous, and
p_(n,u)(0)=0: Q_0 is one exponential density and the remaining
convolution is atom-free because of the extra exponential. Its first
absolute moment is finite. L708's Gaussian argument gives the exact
inversion formula

    p_(n,u)(v)=(2*pi*h)^(-1)
           *integral_R k_n(u,y)*exp(-i*y*v/h)dy.          (9)

Here k_n is integrable since Q_0 and the extra resolvent each decay
as 1/|y|. For fixed n and u, Gaussian removal in (9) uses that
integrability and continuity of p, precisely as in the cited argument.

Every pole of Q_t in y is t*Im u-i*(d+t*Re u), and the extra pole
is -4i. Shrink V so none lies between Im y=-1/10 and 3/20. Cauchy's
theorem on rectangles therefore moves (9) to either horizontal line.
The vertical integrals tend to zero: for fixed n and v the rational
integrand is O(|Re y|^(-2)), uniformly across this finite strip, and
the exponential factor is bounded there. On either horizontal line
the extra resolvent supplies a second 1/(1+|X|) factor at infinity.
The uniform product estimates just proved imply

    |p_(n,u)(v)|<=C*n*exp[n*(-41/1000+v/18)],
    |p_(n,u)(v)|<=C*n*exp[n*(74/1000-v/27)],     v>=0.   (10)

Both estimates are for the actual complex convolution. Absolute values
were taken after the product on the shifted line, not factorwise in
its convolution representation.

### 4. Pair the actual real-frequency correction and the full comb

For s_m=m+1/2, L708's exact real-frequency identity is

    S_e(v)=sum_m [exp(i*v*(s_m+e_m))-exp(i*v*s_m)]
          =-chi_w(v/(2*pi)),                  |v|<3*pi/4,
    |S_e(v)|<=E*|v|,                         v real.     (11)

No continuation of S_e to nonreal v is used. The same actual L703
width satisfies 2*pi*w<1/3000. Direct integration gives

    omega_*=A*[log(9/5)-4/5+(121/100)*log(201/121)]
                                            <10851/10000.

Thus the positive bump ends before 543/500; it lies below 9/4<3*pi/4.
The certificate verifies these comparisons with the same exact log
enclosures. Since 0<=chi_w<=1 on the positive halfline, (10)--(11)
give

    |integral_0^infinity S_e(v)*p_(n,u)(v)dv|
      <=C*n*exp(29*n/1500)+C*exp(-9*n/1000).            (12)

For the bump use -41/1000+(543/500)/18=29/1500. For v>=9/4
integrate E*v times the second bound in (10); its starting exponent
is 74/1000-1/12<-9/1000 and its integral prefactor is bounded.
The interval outside the bump and below 9/4 contributes zero exactly.

The second bound in (10) also makes the positive samples p(2*pi*l)
absolutely summable with an exponentially decaying bound, uniformly
in u. Negative samples and the zero sample vanish. For fixed n its
exponential tail, continuity, k_n(h*(m+1/2))=O(m^(-2)), and the same
Gaussian domination as L708 Section 5 justify Poisson and Gaussian
removal on both sides. Consequently

    B_n(u)=sum_(m in Z) k_n(u,h*s_m)
          =2*pi*sum_(l>=1)(-1)^l*p_(n,u)(2*pi*l).

It is exponentially small, since 2*pi>6 in the second bound in (10).
The shifted difference pairing is justified by
E*integral v d|nu|(v)<infinity. All shifted and unshifted lattice
sums are absolutely convergent, and the anchor is k_n(u,0)=1. Hence

    1+sum_(m in Z) k_n(u,h*(s_m+e_m))
          =1+B_n(u)+integral S_e(v)*p_(n,u)(v)dv
          =O(n*exp(29*n/1500)),                          (13)

uniformly on V. This is an upper estimate on the complete signed
infinite sum; no counting measure has been treated as a finite measure.

### 5. Both omitted tails and a nonzero scalar asymptotic

By (7)--(8), after shrinking V,

    |W_n(u,-Y)|>=C^(-1)*exp(51*n/2500),
    W'_n(u,y)/(n*W_n(u,y))
      ->integral_0^1 i*[1/(d+t*u-i*y)
                          -t/(U*u+d*t-i*t*y)]dt.        (14)

The latter convergence is uniform on a slightly enlarged interval
[-1,-Y]; its real part is at least 1/40 for large n. The limiting
real part on the original interval is strictly above 1/25. This
follows from the derivative certificate and uniform Riemann sums;
all factors are nonzero on the compact sets concerned.

The negative omitted indices are m=-2q-1-k, k>=0. Their ordinates
are -Y-h*k+h*e_m, because h*(2q+1/2)=Y exactly. For each fixed k,
e_m tends to zero and (14) therefore gives uniformly on V

    W_n(u,-Y-h*k+h*e_m)/W_n(u,-Y)
                                  ->exp(-A*k*D_-(u)).   (15)

For the portion with ordinates between -1 and -Y+h/8, (14) and
|e_m|<=1/8 bound these ratios by C*exp(-A*k/40). This supplies a
summable majorant independent of n, including the possible slight
inward shift of the first omitted node.

No infinite physical tail is omitted from that argument. At u=i/2,
the pointwise monotonicity proved after (7) bounds Phi_0(y) by
Phi_0(-1) for y<=-1, and
Phi_0(-Y)-Phi_0(-1)>(1-Y)/25. On a fixed compact remainder interval
this gives a uniform positive exponential gap after shrinking V.
For sufficiently large negative y use the 9/10 factor bound from
Section 3, retaining Q_0 and the resolvent for C/(1+y^2). These
bounds also hold on an overlap around -1. The shifted lattice has
spacing at least 3h/4; thus sums of the integrable majorant cost O(n).
It follows that the entire remaining negative tail divided by
W_n(u,-Y) is O(n*exp(-g*n)) for some fixed g>0.

For the positive omitted indices m=2q+k the ordinates are
Y+h*k+h*e_m. The pointwise positive-halfline comparison after (7),
the strict Phi_0(Y)<-1/10, compact continuity, and the same 9/10
far-tail bound give a complete positive-tail bound O(n*exp(-n/10)).
Allowing ordinates as low as Y-h/8 does not change it: the strict
endpoint margin holds on a fixed slightly enlarged interval before
n is chosen. Again the Q_0/resolvent factors make the far-tail sum
integrable. No symmetry of e is assumed.

Since 1/(R-a(y)/2) tends to 1/(R-a_-/2) at the negative endpoint,
(15), its summable majorant, and both tail bounds prove

    sum_(m<=-2q-1) W_n(u,y_m)/(R-a(y_m)/2)
      /W_n(u,-Y)
        ->1/[(R-a_-/2)*(1-exp(-A*D_-(u)))].              (16)

For the FULL infinite anchored resolvent at z=1/2, divide (13) by
R+d/2=2. Its exponential rate is strictly smaller than that of
W_n(u,-Y), since 51/2500-29/1500=4/3750>1/1000.
The finite F_n is this full sum minus BOTH omitted tails. Hence
(16) gives the negative of its displayed limit for F_n/W_n(u,-Y).
Re D_->1/25 guarantees that the geometric denominator is nonzero;
compactness gives a uniform nonzero lower bound for the modulus of
the limiting coefficient. The signed interior has been retained
through (13), not bounded away by an endpoint-modulus argument.

### 6. Pay every finite moment relative to the actual maximum

The third global bound in (7)--(8) gives |W_a(u)|<=C*exp(24*n/1000)
for every retained atom, including the anchor. For |z|<=s the exact
geometric remainder consequently satisfies

    |T_n(u,z)|<=C*n*exp(24*n/1000)*v^(n/3)/(R*(1-v)).    (17)

Using log v<= (v^2-1)/2, its exponential rate is at most

    24/1000+(59657/61952-1)/6 < 1/50-1/500.             (18)

The exact excess below the right side before the final 1/500
subtraction is recorded in the certificate; relative to 1/50 it is
-33673/15488000<-1/500. This strict margin absorbs the factor n.
In particular (17) is o(|W_n(u,-Y)|), even on the whole larger disk.
Thus G_n=F_n-T_n has the limit (1). Evaluating this limit at z=1/2
gives S_(n,1)>=c*|W_n(u,-Y)|. Absorbing its fixed positive constant
in the stronger rate 51/2500 proves (2) at one uniform onset.
Divide (17) by this ACTUAL lower bound (2) and use (18) to obtain
(3). Take any sufficiently small closed positive-measure arc I_0
inside V. All choices precede n and work along its full allowed sequence.

### 7. What the normalization does not pay

A full-disk upper estimate for F_n requires additional work. The
upper contour in Section 3 is legitimate for z=1/2, but the general
resolvent pole is

    y_z=-i*(d+R/z).

For example y_z=-2/5+7i/100 corresponds to
z=-R/(33/25+2i/5), whose squared modulus is
U/[(33/25)^2+(2/5)^2]<1. It lies between the real line and Im y=3/20.
At u=i/2, W_n(u,y_z) is nonzero. The residue of
W_n(u,y)*exp(-i*y*v/h)/(R-a(y)*z) there is

    i*W_n(u,y_z)*exp(-i*y_z*v/h)/z.

It must be retained in any such contour deformation. This exact pole
example prevents a pole-free extension of the scalar proof; it does
not estimate the residue after the signed v pairing, decide the full
resolvent maximum, or imply positive linear B_sp. L709's paid finite
tail and denominator leave precisely that signed comparison open.

### 8. Separate conceptual audit — 3 November 2026, step 171

The joined audit uses the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-fixed-profile-spatial-growth-stop-audit.md`.
It accepts (1)--(3); no substantive repair or new family is needed.
The named Fourier inputs are reused with that assessment's finite
variation, Schwartz-test and strict-halfplane qualifications, not as
a manuscript-wide audit. The following checks concern their local use.

**Family, rates and complete arithmetic.** Dividing the original
L666 weight factors gives (4), including Q_0=d/(d-i*y) and W_x=1.
The retained ordinates lie strictly between -Y and Y; there are
4q+1=M distinct nodes. For t>0, the derivative of the variable
logarithm in (5) has numerator
(a_t-b_t)*[(X-a_t)*(X-b_t)-D^2] over a positive denominator.
For X<=-1 this is positive by 1+R+U/4>D^2. Its two critical
points straddle zero since D^2>U/4. On X>=0 the sole critical
point is a minimum, and the limiting value at infinity is below
the value at zero. On X>=Y the same conclusion uses
a_t+b_t>=R>2Y. The t=0 factor is checked directly. Thus the
finite interval and both halfline reductions are valid.

The four affine-factor lower bounds and slope bounds in Section 2
give the displayed fourth-derivative constants. For either variable
derivative the only nonconstant terms are multiples of t/L(t) and
1/L(t), with (t/L)''''=-24*L(0)*L'^3/L^5. The logarithmic Hessian
bound follows by adding the norms of two log-distance Hessians.
For one Simpson pair [-h_t,h_t], Taylor expansion at its midpoint
gives integral and quadrature remainder bounds K*h_t^5/60 and
K*h_t^5/36; summing the pairs gives K/(45*N_t^4), as used.
The rational-log algorithm rounds each multiplication and addition
outwards. Its omitted atanh tail is bounded by
2*z^81/[81*(1-z^2)]<=8/(3*81*2^81). Reciprocal and power-of-two
reductions preserve both endpoints. None of these checks uses the
floating decimal previews.

The complete reviewed program was replayed without replacing the
original certificate. All 600 rate cells, 200 derivative cells,
both endpoint enclosures and all 21 exact comparisons reproduce
identically, including the full remainders. In particular the endpoint
rate is >51/2500, the complete correction rate is 29/1500, and their
gap is 2/1875>1/1000. The exact relative moment rate is
-33673/15488000<-1/500. The shared reproduction command is

    python3 scripts/one-sided-hankel/spatial-growth-audit-171.py

Full replay: `scripts/one-sided-hankel/spatial-complex-phase-166-replay-171.json`.
Complete comparison record: `scripts/one-sided-hankel/spatial-growth-audit-171.json`.

**Uniform products, Fourier pairing and tails.** Compact nonvanishing
of the factors gives uniform O(1) errors in the logarithmic Riemann
sums. At infinity Q_t-r_t=O(1/|X|) uniformly in t and nearby u.
The strict |r_t|<.9 margin makes the remaining product exponentially
small there; retaining Q_0 and the extra resolvent gives an integrable
C/(1+X^2) majorant. This avoids a false logarithmic bound at t=0,
X=infinity. Both horizontal shifts avoid every pole. For each fixed
n,v their vertical edges vanish by rational O(X^-2) decay.

The convolution is a finite complex measure with finite first absolute
moment. Its two exponential factors give a continuous density, including
p(0)=0; its negative samples vanish by positive support. Inversion is
scaled by 1/(2*pi*h). In the lattice variable s=y/h, its transform is
k(h*s), so the Poisson samples are 2*pi*l with multiplier 2*pi and
phase (-1)^l. Gaussian removal is taken for fixed n, using the complete
exponential sample majorant; its constants need not be uniform in n.
Fubini for displacement differences uses E*integral v d|nu|(v)<infinity.
The bump and v>=9/4 use different bounds in (10). The interval between
them vanishes by the real-frequency identity; no complex value of S_e
is used. The uniform estimates in n follow after these exact identities.

The negative omitted ordinates are exactly -Y-h*k+h*e_m, including
k=0. Summability implies e_m->0 at both ends. The complex logarithmic
derivative and Re D_->1/25 yield the ratio limit (15), dominated by
C*exp(-A*k/40). Compact uniform convergence plus this summable bound
justifies the endpoint series uniformly in u. Beyond -1 the strict
gap and the integrable .9-product bound pay the whole negative tail;
the positive tail uses its separate strict endpoint bound. Separated
lattice points make these sums O(n) times their exponential bounds.
Thus the sign in (1) is minus: the full anchored sum is negligible
and the negative omitted tail is subtracted. Its limiting coefficient
is uniformly nonzero on a smaller fixed arc. Finally |a|/R<rho and
M=n/3 give the exact all-moment remainder (17), establishing both
the scalar limit and the actual S_(n,1) normalization without a
presumed cancellation budget. All arc choices precede n.

## Mathlib

Full matching Mathlib coverage for this fixed-profile normalization,
complex-convolution estimates, uniform finite-tail limit and B_sp
observable has not been checked. No absence or formal verification
is claimed. The named Fourier/convolution inputs retain L708's source
qualifications. The exact certificate checks the stated rational and
logarithmic inequalities with complete interval remainders; it is not
a formal proof. Section 8 supplies a separate informal analytic audit;
it does not change the stated Mathlib coverage limitation.
