# Lemma 710: the full signed spatial residue and centered bump reduction

## Hypotheses

Fix exactly one actual L703 profile e, with its cutoffs and width fixed
before n. Use the full L666 family and L709's notation:

    d=5/4, R=11/8, U=121/64, A=27/10, Y=9/20,
    n=12q+3, q>=1, M=n/3, h=A/n, a(y)=-d+i*y,
    y_m=h*(m+1/2+e_m), m in Z, a_-=-d-iY,
    Z_n={-d} union {a(y_m): -2q<=m<2q},
    W_n(u,y)=product_(j=0)^(n-1) Q_(j/n)(u,y),
    Q_t(u,y)=r_t+(1-r_t)*lambda_t/(lambda_t-i*y),
    lambda_t=d+t*u, r_t=t*(d+t*u)/(U*u+d*t),
    F_n(u,z)=sum_(a in Z_n) W_a(u)/(R-a*z),
    T_n(u,z)=sum_(a in Z_n) W_a(u)*(a*z/R)^M/(R-a*z),
    G_n(u,z)=F_n(u,z)-T_n(u,z), s=65/64,
    S_(n,r)(u)=max_(|z|<=r)|G_n(u,z)|,
    B_sp(n)=mean_(|u|=1/2) log(S_(n,s)(u)/S_(n,1)(u)).

Here W_a=W_n(u,Im a), including W_x=1. All unit masses, the
inverse angular variable, j=0, both finite endpoints, signed interior
and all M spatial moments remain. The product identity, summability
of e and exact real-frequency identity are those of L708. The phase
bounds, D_-(u) and endpoint normalization are those of L709; L709
is accepted by its separate step-171 conceptual audit.
For the B_sp continuation use L706's nonzero spatial slices and
finite-n logarithmic integrability, with normalized angular measure.

Use chi_w and omega_* from L703, with its actual fixed width w.
The symbol y_z below is a spatial-resolvent pole, not this width:

    y_z=-i*(d+R/z)=X+i*c,
    K={X+i*c: -2/5<=X<=-9/25, 1/25<=c<=2/25},
    z(y_z)=-R/(d+c-i*X),
    K_s={y_z in K: |z(y_z)|<=s}.

For complex y define the entire centered bump transform

    E_n(y)=integral_0^infinity chi_w(v/(2*pi))
                              *exp(-i*y*(v-omega_*)/h)dv.

This integral is over real frequencies and compact positive bump
support. It is not an analytic continuation of S_e.

## Conclusion

There is a fixed closed positive-measure angular arc I about i/2,
contained in L709's arc, on which, uniformly for y_z in K_s,

    G_n(u,z)/W_n(u,-Y)
       = A_n(u,z)*E_n(y_z) - K_-(u,z) + epsilon_n(u,z),    (1)
    sup_(u in I, y_z in K_s)|epsilon_n(u,z)| -> 0,

where

    A_n(u,z)=W_n(u,y_z)*exp(-i*y_z*omega_*/h)
                                      /[h*z*W_n(u,-Y)],
    K_-(u,z)=1/[(R-a_-*z)*(1-exp(-A*D_-(u)))].           (2)

The finite coefficient K_- is uniformly bounded and nonzero. The
full infinite anchored resolvent, before subtracting either physical
tail, satisfies the stronger remainder estimate

    H_n(u,z)=W_n(u,y_z)*exp(-i*y_z*omega_*/h)*E_n(y_z)/(h*z)
                                      +O(n*exp(29*n/1500)),           (3)
    H_n(u,z)=1/(R+d*z)+sum_(m in Z)W_n(u,y_m)/(R-a(y_m)*z),

uniformly for y_z in K, including spatial points outside K_s.

Set y_*= -19/50+i/20 and z_*=z(y_*). Then 1<|z_*|<s.
There is a fixed closed disk D_* about y_*, with positive radius,
contained in the interior of K_s and with |z(y)|>1 throughout,
such that, after possibly shrinking I, for all sufficiently large
allowed n,

    inf_(u in I, y_z in D_*) |A_n(u,z)| >= exp(n/5000).   (4)

This is growth of the coefficient multiplying E_n, not a lower
bound for that product, G_n, S_(n,s)/S_(n,1), or B_sp. No lower
bound for E_n on D_* and no matching upper bound for the complete
unit-disk maximum have been proved. In particular (4) does not stop
the sublinear B_sp mechanism or prove a positive B_sp/n limit.

This local signed reduction pays the contour remainder, both frequency
tails, all comb samples including zero, both physical tails and the
finite moment remainder. It leaves a specified bump-transform and
unit-maximum comparison. Constants and onsets depend on the fixed
profile and are existential. The separate conceptual audit in Section 7
accepts the result; its auxiliary arithmetic certificate alone does
not audit the analytic proof. Actual-Xi
positivity, amplitude/full charge, H/support and realization stay open.

## Proof

### 1. Scope, reused inputs and auxiliary rate bounds

Reuse the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-spatial-doubling-growth-attempt-scope.md`.
The present attempt retains the spatial pole that prevents L709's
pole-free scalar proof from extending to a full spatial disk.
The earlier interpolation, absolute-envelope and two-arc completion
stops are comparisons, not assumptions about this residue.

The standard Fourier inputs are the ones used and assessed in L708:
J. Kallsen and P. Kruehner, *On uniqueness of solutions to martingale
problems -- counterexamples and sufficient criteria*,
[arXiv:1607.02998v1](https://arxiv.org/pdf/1607.02998v1), Appendix A,
Lemma A.1(6),(9)--(11),(14), pp.29--30; S. D. Miller, *Some notes
on distributions*, 15 January 2006,
[Theorems 4.1--4.2 and Section 6, pp.7--9](https://sites.math.rutgers.edu/~sdmiller/musagei/distributions.pdf);
and the exponential transform in
[DLMF (1.14.17)--(1.14.18)](https://dlmf.nist.gov/1.14.iii).
Their source qualifications remain as recorded in L708. The negative
halfline transform needed here is obtained from the same absolutely
convergent exponential integral by reflection, as written below.
The standard Cauchy residue theorem is applied to a finite rectangle;
its only crossed pole and the vanishing vertical integrals are specified.
No nonreal-frequency gap, saddle-point theorem, entire-function
indicator theorem, or new general Fourier theorem is assumed.

At u=i/2 write Phi_c(X)=integral_0^1 log|Q_t(i/2,X+i*c)|dt.
L709's formula is

    |Q_t(i/2,X+i*c)|^2
      =[(d^2+t^2/4)*(t^2*(d+c)^2+(U/2-t*X)^2)]
          /[(d^2*t^2+U^2/4)*((d+c)^2+(t/2-X)^2)].      (5)

The exact auxiliary certificate for this lemma proves

    sup_(X+i*c in K) Phi_c(X)<1/100,
    Phi_0(-Y)<2053/100000,
    Phi_(1/20)(-19/50)+omega_*/(20*A)>207/10000,
    Phi_(1/20)(-19/50)+omega_*/(20*A)-Phi_0(-Y)>1/5000.  (6)

Here is the complete reduction to its finite checks. For t>0 put
a_t=U/(2t), b_t=t/2, D=d+c. The c-dependent logarithm in (5) is
half log[(D^2+(X-a_t)^2)/(D^2+(X-b_t)^2)]. For X<0, a_t>b_t>=0,
so its c derivative

    D*[1/(D^2+(X-a_t)^2)-1/(D^2+(X-b_t)^2)]

is negative. The t=0 derivative is -D/(D^2+X^2)<0. It therefore
suffices to bound Phi_(1/25) on [-2/5,-9/25]. Use 40 equal cells;
the midpoint enclosure plus its derivative enclosure times the
cell radius and radius^2/(d+1/25)^2 bounds the whole cell. This uses
the bound |partial_X^2 log|Q_t||<=2/(d+c)^2 from the two quadratic
factors. There is no untested interval or exterior reduction here.

All evaluations lie in L709's certified domain -1<=X<=Y,
-1/10<=c<=3/20. Reuse its explicit fourth t-derivative bounds 256
for log|Q_t| and 512 for its X derivative. The elementary cubic
Taylor error for 32-panel composite Simpson is K/(45*32^4).
Integer-directed rational-log enclosures at scale 2^100 use 40
terms and the full atanh-series remainder described in L709.
The center omega_* is enclosed from the exact formula

    omega_*=A*[log(9/5)-4/5+(121/100)*log(201/121)].

The script loads only those named arithmetic function definitions
from the existing step-166 script; it does not execute its old
top-level calculations or alter its certificate. It records their
source hash. Whole-cell, endpoint and point enclosures are saved.
The rigorous rounded weakenings are respectively: box upper below
0.005245; endpoint upper below 0.020522; centered outer coefficient
rate above 0.020757; and coefficient-minus-endpoint rate above
0.000236. None of those rounded previews decides a comparison.

The product factors and all denominators are nonzero on these compact
sets, including t=0. Uniform Riemann sums consequently give

    log|W_n(u,X+i*c)|
       =n*integral_0^1 log|Q_t(u,X+i*c)|dt+O(1).         (7)

Strictness, compact continuity and then a fixed sufficiently small
neighborhood V of i/2 preserve |W_n(u,y)|<=C*exp(n/100) on K.
Keep simultaneously L709's uniform bounds on the horizontal lines
Im y=3/20 and Im y=-1/10, its endpoint lower bound
|W_n(u,-Y)|>=C^(-1)exp(51*n/2500), its physical-tail bounds, and
its D_- with Re D_->1/25. All parameter choices precede n.

### 2. The bilateral density and the upper-halfplane spatial pole

For y_z=X+i*c in K put beta=d+R/z=i*y_z=-c+i*X. Its real part
is negative. The correct exponential measure for the resolvent is
therefore on the NEGATIVE halfline:

    1/(R-a(y)*z)=1/[z*(beta-i*y)]
       =-(1/z)*integral_(-infinity)^0 exp(-beta*t)*exp(i*y*t)dt. (8)

Absolute convergence follows from c>=1/25. This is not the positive
halfline measure used for the scalar z=1/2 in L709.

Let nu_W be the convolution of L708's n complex mass-one measures
for Q_(j/n), pushed forward by h. It is supported in [0,infinity),
has finite first absolute moment and has no atoms because Q_0
is an exponential density. Its Fourier transform at v/h is W_n(u,v).
Convolve nu_W with the scaled measure from (8), whose density is

    -(1/(h*z))*exp(-beta*v/h)*1_(v<=0).

The resulting finite complex measure has a continuous density p_z.
Indeed its convolution formula is an integral over t>=max(0,v);
the finite measure nu_W has no atoms, so moving this endpoint is
continuous, including at zero. Exponential decay supplies domination
locally in v. Inversion, with the same conventions as L708, is

    p_z(v)=(2*pi*h)^(-1)*integral_R
           W_n(u,y)/(R-a(y)*z)*exp(-i*y*v/h)dy.          (9)

The rational kernel is integrable: Q_0 and the resolvent each supply
a factor O(1/|y|). The convolution density is continuous, so the
Gaussian-regularized inversion proof used in L708 applies. For v<=0
the convolution can be evaluated directly, absolutely, giving

    p_z(v)=-W_n(u,y_z)*exp(-i*y_z*v/h)/(h*z).             (10)

In particular p_z(0) is generally NONZERO. The transform W_n(u,y_z)
is legitimate because exp(i*y_z*t/h) has modulus exp(-c*t/h) on
nu_W's positive support. No S_e value at a nonreal argument occurs.

Every pole of a Q_t lies below Im y=-1 on a sufficiently small V.
The only pole crossed by shifting (9) to Im y=3/20 is y_z. Its
residue before the factor 1/(2*pi*h) is

    i*W_n(u,y_z)*exp(-i*y_z*v/h)/z.

On a counterclockwise rectangle the real-line integral minus the
upper-line integral is 2*pi*i times this residue. Thus, for v>=0,

    p_z(v)=p_z^+(v)-W_n(u,y_z)*exp(-i*y_z*v/h)/(h*z),     (11)
    p_z^+(v)=(2*pi*h)^(-1)*integral_(R+3i/20)
              W_n(u,y)/(R-a(y)*z)*exp(-i*y*v/h)dy.

For fixed n and v, the vertical integrals vanish as their real
parts tend to infinity: the rational part is O(|Re y|^(-2))
uniformly across the finite strip, and the exponential is bounded
on it. The upper-line pole distance is at least 7/100. On the
lower line Im y=-1/10 it is at least 7/50, and shifting to that
line crosses no pole. The spatial z values lie in a fixed compact
annulus away from zero. The resolvent is consequently bounded by
C/(1+|Re y|) on each line. Together with L709's integrable product
bounds, this gives the uniform estimates

    |p_z^+(v)|<=C*n*exp[n*(-41/1000+v/18)],
    |p_z(v)|<=C*n*exp[n*(74/1000-v/27)],       v>=0,
    |p_z(v)|<=C*n*exp[n*(1/100-|v|/(25*A))],  v<=0.     (12)

The last line is (10) and the box bound. The first line is used only
on a bounded positive frequency interval; extending the separately
growing residue to all positive frequencies would be invalid.

### 3. Pair the full real-frequency correction and every comb sample

L708's exact identity and bound apply on the real line:

    S_e(v)=sum_m [exp(i*v*(m+1/2+e_m))-exp(i*v*(m+1/2))],
    |S_e(v)|<=E*|v|, E=sum_m|e_m|<infinity,
    S_e(v)=-chi_w(v/(2*pi)),                    |v|<3*pi/4. (13)

The actual positive bump ends before 543/500 and its width obeys
2*pi*w<1/3000, as proved for this fixed construction in L708--L709.
Set v_0=9/4<3*pi/4. On 0<=v<=v_0 insert (11) into the integral
of S_e*p_z. The positive bump gives exactly

    W_n(u,y_z)*exp(-i*y_z*omega_*/h)*E_n(y_z)/(h*z)
                - integral_0^infinity chi_w(v/(2*pi))*p_z^+(v)dv. (14)

By (12) the second term is O(n*exp(29*n/1500)), since
-41/1000+(543/500)/18=29/1500. On -v_0<=v<=0, (10),
0<=chi_w<=1 and its fixed support bound the entire contribution
by C*n*exp(n/100). It has not been identified with the positive
residue or omitted. On the two remaining half-lines use E*|v|
and (12). Their starting exponents are respectively

    74/1000-v_0/27 < -9/1000,
    1/100-v_0/(25*A)=-7/300 < -1/50.

Integrating the exponential tails changes only the prefactor. Thus
(14), with its stated error, describes the FULL real-frequency
pairing, not only the prescribed bump.

Write k(s)=W_n(u,h*s)/(R-a(h*s)*z). The signed lattice identities
are absolutely convergent because k(s)=O(s^(-2)), the shifted
points remain separated, and (12) gives integrable |v*p_z(v)|.
Termwise differences are justified by E*integral |v*p_z(v)|dv.
Gaussian-regularized Poisson, as in L708, gives

    sum_(m in Z) k(m+1/2)=2*pi*sum_(l in Z)(-1)^l*p_z(2*pi*l). (15)

For completeness the removal of the Gaussian includes all samples.
For each fixed n, (12) gives |p_z(v)|<=C_n*exp(-a_n*|v|)
with a_n>0 on both half-lines. Its Gaussian convolutions at
2*pi*l are dominated by a constant times exp(-a_n*|2*pi*l|),
as in L708's proof. Continuity gives the pointwise sample limits.
The zero sample is (10), not zero; negative samples do not vanish.
Their complete sum, including zero, can also be written exactly as

    2*pi*sum_(l<=0)(-1)^l*p_z(2*pi*l)
      =-2*pi*W_n(u,y_z)/[h*z*(1+exp(2*pi*i*y_z/h))].    (16)

Its modulus is O(n*exp(n/100)), because c>=1/25 and hence the
denominator is uniformly bounded away from zero for large n.
The positive samples in (15) are exponentially small by the second
line of (12) and 2*pi>6. This pays every comb sample separately.

The anchor equals k(0)=1/(R+d*z), uniformly bounded on the
compact spatial set since beta=i*y_z is bounded away from zero.
Combining (13)--(16) with the shifted-minus-unshifted identity yields

    H_n(u,z)=k(0)+sum_m k(m+1/2)+integral_R S_e(v)*p_z(v)dv.

All the nonleading terms are O(n*exp(29*n/1500)). This proves (3),
including its sign and normalization. The factor 1/h in the residue
and the zero-frequency comb term have both been retained.

### 4. Both physical tails and all finite spatial moments

Subtract both omitted physical tails from H_n to recover F_n.
L709's negative tail argument extends uniformly to every spatial
point under consideration. In detail, its first omitted ordinates
are -Y-h*k+h*e_m, k>=0. For each fixed k their W_n ratios to
W_n(u,-Y) tend uniformly to exp(-A*k*D_-(u)). On the near portion
the summable bound C*exp(-A*k/40) persists. Here the resolvent
is uniformly bounded and tends to 1/(R-a_-*z) at the endpoint.
Indeed for real y its denominator has modulus |z|*|y-y_z|,
with Im y_z>=1/25; at infinity it also supplies C/(1+|y|).
These facts make dominated convergence uniform in z on K.

The compact far portion of the negative tail has L709's positive
exponential gap below the endpoint, and its remaining infinite
portion is bounded by C*n*(9/10)^(n-1) with the integrable
Q_0/resolvent factors. The entire positive omitted tail is
O(n*exp(-n/10)), by L709's positive-halfline comparison and the
same resolvent bounds. Consequently

    sum_(m<=-2q-1) W_n(u,y_m)/(R-a(y_m)*z)
                      =W_n(u,-Y)*(K_-(u,z)+o(1)),
    sum_(m>=2q) W_n(u,y_m)/(R-a(y_m)*z)=o(W_n(u,-Y)),     (17)

uniformly. No symmetry of e is used. The geometric denominator in
K_- is nonzero since Re D_->1/25; all other denominators are
bounded away from zero on the compact parameter set. This also
proves the asserted bounds and nonvanishing of K_-.

The error in (3) divided by W_n(u,-Y) tends to zero exponentially:
51/2500-29/1500=4/3750>1/1000. On K_s, L709 Section 6's
ABSOLUTE finite-tail estimate, before its division by S_(n,1), is

    |T_n(u,z)|<=C*n*exp(24*n/1000)*v^(n/3),
    v^2=59657/61952<1.

It is o(W_n(u,-Y)), since log v<=(v^2-1)/2 and

    24/1000+(59657/61952-1)/6-51/2500 < -1/400.

Using only L709's relative T_n/S_(n,1) bound here would not suffice
without an upper bound for S_(n,1). The displayed absolute bound
avoids that circular step. Equations (3), (17) and G_n=F_n-T_n
now prove (1) uniformly on K_s, with the signed interior intact.

### 5. The coefficient margin and its precise limitation

At y_*=-19/50+i/20,

    |z_*|^2=U/[(d+1/20)^2+(19/50)^2],
    1<|z_*|^2<(65/64)^2.

By (7), at u=i/2 the limiting exponential rate of |A_n(u,z_*)|
is the last difference in (6). The prefactor 1/(h*z_*) contributes
only O(log n)/n to its normalized logarithm. All product factors
are nonzero on a neighborhood of this point. The strict rate
margin, the strict spatial-radius margins and compact continuity
therefore give a fixed disk D_* and a sufficiently small angular
arc I for which the same rate exceeds 1/5000 uniformly. The
uniform O(1) Riemann error and log n prefactor prove (4) at one
onset along the full allowed sequence.

Writing delta=2*pi*w, the still-uncontrolled factor is explicitly

    E_n(y)=integral_(-delta)^delta eta(t/delta)*exp(-i*y*t/h)dt,
    |E_n(X+i*c)|<=2*delta*exp(c*delta/h),       X+i*c in K. (18)

The first identity uses the actual even nonnegative bump; no
replacement of it is allowed. Equation (18) is only an upper
bound. Positivity of eta does not give a positive modulus lower
bound at the complex y in D_*. Exponential growth of A_n alone
therefore leaves open cancellation inside E_n and cancellation
between the residue and the endpoint term in (1).

For a concrete sufficient continuation threshold, if one could prove

    max_(y in D_*) |E_n(y)| >= exp(-n/10000),
    S_(n,1)(u)/|W_n(u,-Y)| <= exp(n/20000),    u in I,   (19)

eventually along every allowed n, then (1), bounded K_- and (4)
would imply log(S_(n,s)/S_(n,1))>=n/20000-log 2 on I for large n.
The integrand is nonnegative elsewhere because the disks are nested,
so liminf B_sp(n)/n>=mu(I)/20000>0. Neither inequality in (19)
has been established. In particular the endpoint rate in (6) is
not a bound for the full unit maximum. This conditional threshold
explains the downstream use and the remaining two obligations; it
is not an informative negative result about B_sp yet.

### 6. Reproduction and evidence limits

Run, from the active notebook,

    python3 scripts/one-sided-hankel/spatial-residue-rates-167.py

The full certificate is
`scripts/one-sided-hankel/spatial-residue-rates-167.json`.
All 13 exact comparisons pass; the full 40 cell enclosures and
endpoint/outer-point logarithmic intervals are retained. This
certifies (6), pole/radius margins and the displayed error-rate
comparisons using the analytic derivative bounds above. It does
not certify contour signs, interchanges, endpoint asymptotics,
uniformity, E_n lower bounds, or either maximum.

The separate `scripts/one-sided-hankel/spatial-residue-diagnostic-167.py`
and its JSON record retain the preliminary floating sample screen.
They are labeled nonrigorous and play no role in any proof here.

### 7. Separate conceptual audit — 3 November 2026, step 171

Use the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-fixed-profile-spatial-growth-stop-audit.md`.
This audit accepts (1)--(4), including their signs and uniformity, for
the same fixed L703 profile. L709's normalization and absolute moment
bound were checked in the same joined audit. No lower bound for E_n
or inference from a coefficient alone is part of this lemma.

The finite residue input is Howell--Mathews, *Complex Analysis*,
[Section 8.1, Theorems 8.1.5 and 8.1.7(1), with their proofs](https://complexanalysis.org/web/sec_residue-thm.html).
The assessed version requires a positively oriented simple contour,
finitely many isolated interior poles and none on the boundary. Here
the rectangles can be chosen with vertical sides beyond all poles;
all Q poles are below -1, and precisely y_z is crossed upward.
The spatial pole is simple, with residue i*W_n(u,y_z)*exp(-i*y_z*v/h)/z.
Thus 2*pi*i times the residue is negative, giving (11). The rational
O(X^-2) bound proves the vertical-edge limits for fixed n,v; the
finite residue theorem by itself would not prove these limits.

**Bilateral transform and every sample.** With beta=i*y_z and
Re beta=-c<0, direct integration over t<=0 gives (8), including
its minus sign. Convolution with the positive-supported finite
measure for W_n has density

    -(h*z)^(-1) exp(-beta*v/h)
       *integral_(t>=max(0,v)) exp(beta*t/h) dnu_W(t).

For v<=0 this is (10); the transform at y_z converges absolutely
because exp(-c*t/h)<=1. The measure nu_W is atom-free, and the
displayed moving-endpoint formula is continuous at every v, including
zero. This checks inversion at the zero sample as well as elsewhere.
The contour estimate for p_z^+ is used only on the compact positive
bump. For v>=9/4 the lower-contour bound is applied to p_z itself;
one cannot integrate its separated growing residue over that halfline.
The negative bump is bounded independently, and the complete negative
high-frequency exponent is -7/300<-1/50. The positive high-frequency
exponent is -7/750<-9/1000. These bounds pay both first absolute
moments, so the displacement Fubini step is justified.

At v=0 the density is -W_n(u,y_z)/(h*z), not zero. For l=-k<=0,
the factors in the comb are (-exp(2*pi*i*y_z/h))^k. Summing this
absolutely convergent geometric series gives exactly (16); its
denominator is separated from zero uniformly for c>=1/25. Positive
samples use the lower contour and 2*pi>6. Gaussian-regularized Poisson
has the same 2*pi normalization as L709. For fixed n its Gaussian
convolutions have a summable two-sided exponential majorant, and
continuity justifies all sample limits. The anchor is separately
k(0). Multiplying S_e=-chi_w by the negative residue in (11) gives
the positive leading term in (14), hence (3), with its factor 1/h.

**Physical tails, moments and rate margin.** On compact K the
resolvent is bounded by C/c on the physical line and C/(1+|y|)
at infinity. L709's summable endpoint ratios therefore give (17)
uniformly on K. This subtracts both omitted tails from the full
infinite anchored sum. The geometric endpoint factor is nonzero
since Re D_->1/25. On K_s the absolute M-moment remainder divided
by W_- has rate at most -199341/77440000<-1/400. This check uses
neither L711 nor an unproved upper bound on S_(n,1).

The full 40-cell rectangle certificate and all 13 comparisons were
replayed by `scripts/one-sided-hankel/spatial-growth-audit-171.py`.
They agree in full with the original, including the helper hash and
endpoint and outer-point enclosures; the replay is
`scripts/one-sided-hankel/spatial-residue-rates-167-replay-171.json`.
The exact coefficient-rate lower bound is

    21552503281937052214049741158477
      /91270843216432516907762630787072000 > 1/5000.

Also |z_*|^2=75625/73376 lies strictly between 1 and 4225/4096.
Nonvanishing and compact continuity give a positive-radius disk
strictly inside K_s and a fixed angular arc on which the strict
coefficient margin survives. The O(1) Riemann error and the 1/h
prefactor preserve the eventual lower bound. This is not pointwise
noncancellation of the bump transform. No substantive error was found.

## Mathlib

Full matching coverage of this fixed-profile signed-residue reduction,
the bilateral finite-convolution specialization, its uniform physical
tail asymptotic and B_sp has not been checked. No absence or formal
verification is claimed. The standard named Fourier/convolution
inputs retain their cited source qualifications. The arithmetic
certificate is auxiliary evidence; Section 7 supplies a separate informal
critical review, not formal verification or a new coverage claim.
