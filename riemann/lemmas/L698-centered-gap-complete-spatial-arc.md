# Lemma 698: centered-gap decay of the complete spatial polynomial on an arc

## Hypotheses

Use exactly L666's family and L697's fixed centered-gap hypotheses.
Thus d=5/4, x=-d, R=11/8, U=121/64, A=27/10, n=12q+3,
q>=1 is an integer, h=A/n, M=n/3, and t_j=j/n, 0<=j<n.
Fix one real sequence e in l1(Z), with sup_m |e_m|<=1/8, before
varying n. Put E=sum_m |e_m|. With the negative-exponent angular
Fourier convention, suppose

    mu=delta_0+sum_(m in Z) delta_(m+1/2+e_m)

has a distributional Fourier gap I=(omega_*-g,omega_*+g), where

    f(t)=1/(d+t)-t/(U+d*t),
    omega_*=A*integral_0^1 f(t)dt,
    g>0,  I subset (0,2*pi).

L696, through L694/L693, supplies existence of such a fixed profile;
this assertion applies to every fixed profile with these hypotheses.
Keep the original unit masses and anchor, and set

    Z_n={x} union {x+i*h*(m+1/2+e_m): -2q<=m<2q},
    B_u(v)=product_(j=0)^(n-1) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    G_n(u,z)=R^(-1)*sum_(a in Z_n) W_a(u)
                                      *sum_(k=0)^(M-1)(a*z/R)^k.

The denominator angle is 1/u and the j=0 factor is included. No
symmetry of e, finite-variation hypothesis on mu, or spatial-moment
truncation below M is imposed.

## Conclusion

There are fixed delta,c>0 and finite C,N, depending at most on the
fixed profile and its gap, such that

    sup_(|theta|<=delta, |z|=1) |G_n(exp(i*theta),z)|
                           <=C*exp(-c*n),  n=12q+3>=N.        (1)

Both finite endpoints and all M spatial moments are retained. The
positive rates in the proof are existential; no numerical gap width,
arc width or onset is asserted. This is a new local derivation under
the prior EXPLORE assessment, not certified originality or a theorem
claimed beyond the sources checked. The separate conceptual audit of
3 November 2026 (step 125), recorded below, accepts (1) without a
substantive repair. It is not an RH candidate. The angular complement,
complete logarithmic estimates, norm comparison, H/support, actual-Xi
realization and all-degree mixed positivity remain open.

## Proof

### 1. Source scope and the two finite spatial expressions

The unchanged invocation-start assessment is
`drafts/literature/2026-11-03-centered-gap-full-spatial-arc.md`.
It licenses the exact target with a signed resolvent or retained
finite-polynomial treatment. Reuse L697's audited complex factors,
positive majorants, reflected interval identity and Fourier conventions.
The differences requiring proof here are one additional resolvent
factor, its uniform comb and endpoint costs, a finite spatial analytic
continuation with a paid maximum-modulus bound, and the complete
geometric remainder. L695's absolute-tail stop, L682's highest-moment
stop and C645p's angular origin-evaluation stop are comparisons only.
No auxiliary residue weights or angular origin normalization are used.

The standard inputs are imported, not reproved:

- Finite complex-measure variation domination and Fourier convolution:
  Jan Kallsen and Paul Kruehner, *On uniqueness of solutions to martingale
  problems — counterexamples and sufficient criteria*,
  [arXiv:1607.02998v1](https://arxiv.org/pdf/1607.02998v1),
  11 July 2016, Appendix A, Lemma A.1(6),(9)--(11),(14), pp.29--30;
  the supporting convolution norm proof is Francesco Paolo Maiale,
  *Analysis of Sublaplacians on Lie Groups*, 28 May 2019,
  [Definition 1.5 and Proposition 1.7, pp.8--9](https://poisson.phc.dm.unipi.it/~fpmaiale/notes/HAoLG.pdf).
- Real Bernstein concentration: Roman Vershynin, *High-Dimensional
  Probability*, first-edition author version, 20 May 2024,
  [Definition 2.7.5, p.33, and Theorem 2.8.1, pp.36--37](https://webapps.math.uci.edu/~rvershyn/papers/HDP-book/HDP-1.pdf).
  Write c_B>0 for its absolute constant. It applies only to the
  independent normalized positive variables constructed below.
- Schwartz Poisson summation and distributional Fourier duality:
  Stephen D. Miller, *Some notes on distributions*, 15 January 2006,
  [Theorems 4.1--4.2 and Section 6, pp.7--9](https://sites.math.rutgers.edu/~sdmiller/musagei/distributions.pdf).
  The actual non-Schwartz limit is justified below.
- The complex exponential integral in
  [NIST DLMF 1.14(iii), (1.14.17)--(1.14.18)](https://dlmf.nist.gov/1.14.iii)
  is used only with strictly positive real decay parameter.
- Hadamard's three-circles theorem, in its standard disk form: if F is
  holomorphic on a neighborhood of a closed disk centered at z_0 and
  0<r_1<r<r_2 are its radii, then

      M_F(r)<=M_F(r_1)^alpha*M_F(r_2)^(1-alpha),
      M_F(s)=max_(|z-z_0|=s)|F(z)|,
      alpha=log(r_2/r)/log(r_2/r_1).

  This named standard theorem needs no zero-free hypothesis on F; the
  identically zero case is immediate. We also use the maximum-modulus
  principle. Neither standard theorem is reproved. Their application
  is to the original finite rational function below, not to an
  unproved continuation of an infinite comb identity.

For each fixed n,u define the finite rational function and remainder

    F_n(u,z)=sum_(a in Z_n) W_a(u)/(R-a*z),
    T_n(u,z)=sum_(a in Z_n) W_a(u)*(a*z/R)^M/(R-a*z).

The exact finite identity from L683 (7) gives

    G_n(u,z)=F_n(u,z)-T_n(u,z).                              (2)

The same identity holds wherever the displayed denominators are
nonzero, simply by the finite geometric-sum identity. We only estimate
T_n on |z|=1, where every denominator is separated from zero. L666's
node geometry gives |Z_n|=M, |a|>=d, and

    |a|^2<K_0^2:=353/200,
    rho:=K_0/R=sqrt(2824/3025)<1,
    tau:=-(log rho)/3>0.                                   (3)

### 2. Choose all rate margins before the fixed angular arc

Set

    kappa_1=(1+sqrt(99/100))/2<1,
    b=c_B*min(g^2/(128*A^2),g/(8*A))>0,
    gamma=min(b/8,3/40,-log(kappa_1)/2)>0,
    alpha=log(301/300)/log(301/50) in (0,1).

Choose once and for all

    0<epsilon<=min(b/4,1/40,alpha*gamma/4,tau/4).            (4)

L697 Section 2's compact-continuity argument, with this possibly
smaller epsilon, gives a fixed delta>0 such that for |theta|<=delta,
u=exp(i*theta), t in [0,1], and all real |y|>=2/5:

    lambda=d+t*u,  a_t=Re(lambda)>=d,
    r=t*(d+t*u)/(U*u+d*t),
    Q_t(y)=r+(1-r)*lambda/(lambda-i*y),
    |Q_t(y)|<=kappa_1,
    z_t:=|r|+|1-r|*|lambda|/a_t<=exp(epsilon),
    |m_t-f(t)|<=g/(4*A),
    m_t=|1-r|*|lambda|/(a_t^2*z_t).                         (5)

The same delta may be made to satisfy cos(theta)>=0 and
|sin(theta)|<=1/10 as in L697. This continuity step is uniform in n.
At theta=0, z_t=1 and m_t=f(t), while the contraction
has the strict uniform margin sqrt(99/100)<kappa_1, including both
infinities. Thus choosing epsilon after alpha and gamma is legitimate;
it is not an n-dependent angular restriction.

Exactly as in L697, W_(x+i*y)(u)=product_j Q_(t_j)(y) is the
positive-exponent Fourier transform of the convolution of the complex
mass-one measures

    r_j*delta_0+(1-r_j)*lambda_j*exp(-lambda_j*v)*1_(v>=0)dv.

Their normalized variations are zero/exponential laws of rate a_j>=d,
with means m_j. Their product variation costs at most exp(epsilon*n).
In particular, for every real y,

    |W_(x+i*y)(u)|<=exp(epsilon*n).                          (6)

### 3. Add one resolvent factor on a fixed spatial disk

For this section restrict |z-1/2|<=1/4. Then

    |z|>=1/4,  |z|<=3/4,  Re z>=1/4,
    beta=d+R/z,  a_beta=Re beta>=67/36>d,
    |beta|<=27/4,  |beta|/a_beta<6,
    |R+d*z|>=27/16.                                       (7)

For example Re(1/z)=Re z/|z|^2>=4/9 proves the lower bound
for a_beta. No boundary Laplace prescription is needed here:

    beta/(beta-i*y)=integral_0^infinity
                            exp(i*y*v)*beta*exp(-beta*v)dv.

The complex measure on the right has mass one, variation mass
|beta|/a_beta<6, and normalized variation equal to an exponential
probability law of rate a_beta. Define

    J(y)=W_(x+i*y)(u)*beta/(beta-i*y),  k(s)=J(h*s).

The exact algebraic relation is

    W_(x+i*y)(u)/(R-(-d+i*y)*z)=J(y)/(R+d*z).                (8)

Let nu be the pushforward of the n base complex measures and this
one extra complex measure under v=h times the sum of their variables.
It has mass one and transform k(s)=integral exp(i*s*v)dnu(v).
For the corresponding independent normalized positive variables
X_0,...,X_(n-1),Y, put V=h*(sum X_j+Y) and let P be its law.
Complex variation domination gives

    |nu|<=6*exp(epsilon*n)*P.                               (9)

These positive variables, not nu, enter Bernstein. Each rate is at
least d; each variable has mean <=1/d, second moment <=2/d^2,
and centered psi1 norm <=4 by L697's calculation
exp(1/(4*d))/(1-1/(4*d))<=25/16<2. The extra exponential obeys
the same bounds. L696's decreasing-integrand Riemann-sum estimate,
(5), and the extra mean give

    |EV-omega_*|<=g/4+2*A/(d*n)<=g/2
                               when n>=8*A/(d*g).          (10)

There are n+1<=2n centered variables. Bernstein at threshold
g*n/(2*A), with sum of squared psi1 norms <=32n and maximum <=4,
therefore gives precisely

    P(V outside I)<=2*exp(-b*n).                            (11)

For n>=15, independence also gives

    EV^2<=(A/d)^2*((1+1/n)^2+2*(n+1)/n^2)
         <=(A/d)^2*(288/225)<6<16.                         (12)

### 4. Every comb sample and the anchored signed pairing

The j=0 base factor is the real rate-lambda_0 exponential after
scaling, where lambda_0=d/h=d*n/A. Convolving it with the other
factors gives a density p for nu, supported on [0,infinity). The
remaining factors include the extra exponential, so their convolution
has no atoms. Consequently p is continuous everywhere, including
p(0)=0: at v decreasing to zero its defining integral is over [0,v]
against an atom-free finite complex measure and tends to zero.
Continuity at positive v follows from dominated convergence with no
atom at the moving endpoint. The same facts hold for the positive
density p^+ of P. Thus (9) gives pointwise
|p(v)|<=6*exp(epsilon*n)*p^+(v), not merely almost everywhere.

Write V=h*X_0+S. The variable S contains n independent positive
factors. For the exponential tilt t=n/20<lambda_0, each factor has
exponential moment at most 250/223, since t*h/a<=27/250.
As log(250/223)<1/8, the conditioning argument of L697 gives

    p^+(v)<=lambda_0*exp(n/8-n*v/20),  v>0,
    |p(v)|<=6*lambda_0*exp[(epsilon+1/8)*n-n*v/20].           (13)

In particular, using pi>3 and n>=15,

    sum_(l>=1)|p(2*pi*l)|
          <=12*lambda_0*exp[-(7/40-epsilon)*n].              (14)

For fixed n,u,z the rational k is O((1+|s|)^(-2)) at infinity:
the j=0 factor and the additional resolvent each decay like 1/s,
while the other finitely many factors are bounded at infinity.
It has no real pole. Apply Schwartz Poisson to k(s)*exp(-eta*s^2)
for eta>0. Its Fourier transform is 2*pi*(p*G_eta), with
G_eta(v)=(4*pi*eta)^(-1/2)*exp(-v^2/(4*eta)), by finite-variation
Fubini. Absolute summability of k(m+1/2) gives the lattice limit.
For fixed n the exponential bound (13) implies, with a_n=n/20 and
C_n=6*lambda_0*exp[(epsilon+1/8)*n],

    |(p*G_eta)(w)|<=2*C_n*exp(a_n^2)*exp(-a_n*|w|),
                                                   0<eta<=1.

This is summable at all w=2*pi*l. Continuity of p, p(0)=0 and
its zero negative side justify the complete comb limit. Hence

    B:=sum_(m in Z)k(m+1/2)
       =2*pi*sum_(l>=1)(-1)^l*p(2*pi*l),
    |B|<=24*pi*lambda_0*exp[-(7/40-epsilon)*n].               (15)

The zero half-density is exactly zero here, because of the extra
continuous factor; it has not been inferred from a probability tail.
All positive samples and all zero negative samples are accounted for.

Reuse L697's real oriented-interval primitive Phi_e, with
||Phi_e||_1<=E and

    Phi_e'=sum_m delta_(m+1/2)-sum_m delta_(m+1/2+e_m).

The gap, the absence of comb atoms in I, and reality of Phi_e give

    H_e(v):=1+i*v*Phi_e-hat(-v)=0 on I,
    |H_e(v)|<=1+E*v,  v>=0.                                (16)

By (9),(12), integral v d|nu|(v)<infinity. Thus k is continuously
differentiable, interval corrections are absolutely summable, and
their Fubini majorant is E*integral v d|nu|<infinity. Exactly the
anchored signed identity of L697, now for the present kernel, yields

    S_infty:=1+sum_(m in Z)k(m+1/2+e_m)
             =B+integral H_e(v)dnu(v).                     (17)

Both lattice sums are absolutely convergent. The anchor is k(0)=1
because nu has algebraic mass one; its variation is still paid in
(9). By (11),(12),(16), Cauchy--Schwarz against the positive P gives

    |integral H_e dnu|
      <=6*sqrt(4+64*E^2)*exp[-(b/2-epsilon)*n]
      <=6*sqrt(4+64*E^2)*exp(-b*n/4).                        (18)

This is a justified L1 interval pairing. It does not apply a finite-
measure gap theorem to the infinite unit-mass counting measure.

### 5. Pay both endpoints on the small spatial disk

For |y|>=2/5, (5) and the exact j=0 factor give

    |W_(x+i*y)(u)|<=d*kappa_1^(n-1)/|y|.

From (7), |y|<=|beta-i*y|+|beta|<=7*|beta-i*y|, and so

    |beta/(beta-i*y)|<=48/|y|,
    |J(y)|<=60*kappa_1^(n-1)/y^2.                          (19)

The omitted unshifted points start at m=2q and m=-2q-1, with
|h*(m+1/2)|>=A/6=9/20. Their displaced points obey
|y|>=9/20-h/8>2/5 for n>=15, exactly as in L697. Moreover
|m+1/2+e_m|>=(3/4)|m+1/2|. Therefore both omitted tails together
have absolute sum at most

    60*kappa_1^(n-1)*(32/9)*h^(-2)/(2q-1/2)
      <=[19200/(9*A^2)]*n*kappa_1^(n-1)
      <300*n*kappa_1^(n-1).                                (20)

Here sum_(m>=2q)(m+1/2)^(-2)<=1/(2q-1/2), and
2q-1/2>=n/10. No shift symmetry, l1 tail rate, or displaced endpoint
is dropped. Absolute tails are affordable for this extra-decaying
kernel on this angular arc; L695's different full-angular absolute
perturbation cost is not being assumed small.

Subtracting these tails from (17), and using (7),(8),(15),(18),
gives uniformly on |z-1/2|<=1/4 and |theta|<=delta:

    |F_n(u,z)|<=(16/27)*[
       6*sqrt(4+64*E^2)*exp(-b*n/4)
       +24*pi*(d*n/A)*exp[-(7/40-epsilon)*n]
       +300*n*kappa_1^(n-1)].                              (21)

This holds for all allowed n>=max(15,8*A/(d*g)). By (4), the
second rate is at least 3/20. The definition of gamma leaves at
least half of each rate to absorb the polynomial prefactors.
Thus one finite constant C_0, independent of n,u,z, gives

    max_(|z-1/2|<=1/4)|F_n(u,z)|<=C_0*exp(-gamma*n).         (22)

### 6. Propagate the finite rational bound with all spatial poles paid

For each retained a, every possible spatial pole of F_n is R/a.
Cancellations can remove such poles but cannot introduce new ones.
Since Re a=-d,

    |R/a-1/2|^2=1/4+(U+R*d)/|a|^2
       >1/4+(U+R*d)/K_0^2=6481/2824>(151/100)^2.             (23)

In particular F_n is holomorphic on a neighborhood of the disk
|z-1/2|<=r_2:=301/200. On that disk the full denominator cost is

    |R-a*z|=|a|*|R/a-z|
       >d*(151/100-301/200)=1/160.

Equation (6) therefore gives the original finite function the
global disk bound

    max_(|z-1/2|<=r_2)|F_n(u,z)|
                            <=(160*n/3)*exp(epsilon*n).     (24)

Apply Hadamard's three-circles theorem about 1/2, with r_1=1/4,
r=3/2, and r_2=301/200. Its weight is exactly alpha from Section 2.
Equations (22),(24) imply

    M_F(3/2)<=C_0^alpha*(160*n/3)^(1-alpha)
                        *exp[-(alpha*gamma-(1-alpha)*epsilon)*n]
               <=C_0^alpha*(160*n/3)^(1-alpha)
                        *exp(-3*alpha*gamma*n/4).           (25)

Absorb the remaining power of n using one quarter of alpha*gamma.
The maximum-modulus principle, and |z-1/2|<=3/2 for |z|<=1, give

    sup_(|z|<=1)|F_n(u,z)|<=C_1*exp(-alpha*gamma*n/2).        (26)

All constants are fixed before n. The small positive distance between
3/2 and r_2 is sufficient; its small interpolation weight has been
paid in the prior choice of epsilon. No lower bound on F_n or
zero-free hypothesis about its numerator was used.

Only the finite rational F_n is continued across the spatial disk.
The infinite pairing (17) is used only on |z-1/2|<=1/4, where
Re beta>d. Thus no out-of-domain Laplace expression, crossed spatial
pole, missing residue or principal-value term is hidden in (25).
Every finite spatial pole is outside the stated larger disk by (23).
This differs from continuing the infinite split resolvent to a
boundary parameter, and from C645p's costly angular origin evaluation.

### 7. The complete finite geometric remainder

For |z|=1, (2),(3),(6) give directly, without any moment truncation,

    |T_n(u,z)|<=[n/(3*R*(1-rho))]
                                   *exp[-(tau-epsilon)*n]
              <=[n/(3*R*(1-rho))]*exp(-3*tau*n/4).

One fixed C_2 consequently bounds this by C_2*exp(-tau*n/2).
Together with (26), this proves (1), for example with

    c=min(alpha*gamma/2,tau/2)>0,
    C=C_1+C_2,

and one finite onset no smaller than max(15,8*A/(d*g)). The anchor,
the j=0 factor, both finite endpoints, the exact denominator angle
and all M=n/3 moments have been retained throughout. No conclusion
about the rest of the angular circle or about RH follows.

The elementary rational margins in (3),(7),(12),(20),(23),(24) are
checked exactly by
`python3 scripts/one-sided-hankel/centered-gap-full-spatial-124.py`.
Its certificate is
`scripts/one-sided-hankel/centered-gap-full-spatial-124.json`.
Those checks do not verify the analytic proof or supply an effective
gap, arc width or onset. The separate analytic audit is recorded next.

### Independent conceptual audit — 3 November 2026, step 125

This audit uses the unchanged invocation-start EXPLORE assessment for
the exact full-spatial fixed-arc target. It checks the complete proof
above against L666's definitions and node geometry, L683 (7), L697's
audited factors and pairing, and L696's Riemann-sum and prescribed-center
interfaces. L694/L693's construction is inherited through the existing
L696/L697 audits; it is not reconstructed here. The inspected source
statements are reused, and Hadamard's standard named theorem is applied
in its displayed disk form. This is an audit of the local application,
not of complete source manuscripts. No new general theorem is reproved.
The L695 absolute-tail, L682 highest-moment and C645p angular-origin
stops retain their recorded scopes and are not premises of this proof.

**Fixed parameters and positive domination.** Exact division of the
original product gives Q_t in (5), including Q_0=d/(d-i*y), with the
original denominator angle 1/u. L697's compact-continuity argument
allows any fixed positive epsilon, so (4) can be chosen after alpha,
gamma and tau, and before delta or n. Its contraction covers both
unbounded y half-lines. This ordering is essential: an arbitrary
previously chosen arc would not necessarily pay the interpolation loss.

On the entire closed small disk, z is nonzero and
Re(1/z)>=4/9. Hence Re beta>=67/36 and |beta|<=27/4. The extra
complex exponential has algebraic mass one and variation
|beta|/Re beta<=243/67<6. Its normalized variation is a real
exponential law; the other normalized variations are zero/exponential
laws of rates at least d. Product-measure pushforward domination yields
(9), with the full factor 6*exp(epsilon*n). Nothing identifies nu
with a positive probability law.

Each of the n+1 positive variables has mean <=1/d, second moment
<=2/d^2 and centered psi1 norm <=4, since
exp(1/5)/(1-1/5)<=25/16<2. The mean error has three charges:
g/4 from the changed base laws, A/(d*n) from L696's decreasing
left Riemann sum, and A/(d*n) from the extra variable. The onset
in (10) leaves distance g/2 to the complement of I. With n+1<=2n,
Bernstein's squared-norm sum is <=32n and largest norm <=4.
The threshold g*n/(2*A) gives exactly the b in Section 2.
The second-moment expression in (12) decreases with n and at n=15
is 93312/15625<6, in particular <16. This verifies every positive-law
input to (18), without a concentration claim for a complex measure.

**Density values and the entire comb limit.** After removing the j=0
exponential, the remaining convolution still contains the extra
absolutely continuous exponential factor. It therefore has no atoms.
Convolution with lambda_0*exp(-lambda_0*v)*1_(v>=0) is continuous
at every v>0 by dominated convergence against finite variation, and
its limit at zero is zero because the remaining measure has no atom
there. Both p and p^+ are continuous on the whole real line, with
value zero at zero and on the negative side. Their measure domination
thus gives the pointwise bound at every comb sample.

There are exactly n positive factors in S after removal of X_0.
For t=n/20, t*h/a<=27/250, so their product exponential moment is
at most (250/223)^n<exp(n/8). Conditioning on S<=v and using
t<lambda_0 proves (13). The first positive comb exponent is at most
-(7/40-epsilon)*n; the remaining geometric ratio is at most
exp(-3*n/10), whose denominator exceeds 1/2 for n>=15. This
proves (14) for every positive sample, independently of probability
tail bounds.

The j=0 and extra factors make k(s)=O(s^(-2)), with no real pole;
bounded shifts preserve absolute lattice summability. Gaussian
regularization is Schwartz and Fourier Fubini has finite-variation
domination. For each fixed n,u,z the exponential density bound gives
the displayed summable majorant
2*C_n*exp(a_n^2)*exp(-a_n*|w|) for every 0<eta<=1.
Thus both sides of Poisson pass to the limit, with phase (-1)^l,
zero contribution at l=0, and zero negative samples. There is no
exchange with n and no omitted half-density or principal-value term.

**Anchored sign and both endpoints.** The derivative of the oriented
interval is delta_(m+1/2)-delta_(m+1/2+e_m). The negative-exponent
gap gives 1-i*v*Phi_e-hat(v)=0 on I; reality of Phi_e gives (16)
by complex conjugation. This uses no symmetry of e and no conjugacy
of the complex kernel. The finite first variation moment justifies
differentiation, interval summation and Fubini with common majorant
E*integral v d|nu|. Adding k(0)=integral dnu=1 gives exactly (17).
Cauchy--Schwarz uses the positive P, and yields the coefficient
6*sqrt(4+64*E^2) and exponent epsilon-b/2<=-b/4 in (18).

For |y|>=2/5, Q_0 gives d/|y| and each remaining factor gives
kappa_1. Since |beta-i*y|>=Re beta and |beta|<6*Re beta,
|y|<=7*|beta-i*y| and the extra factor is <=48/|y|.
This verifies (19). Both omitted tails start at absolute unshifted
ordinate 9/20; their shifted ordinates remain >=171/400>2/5.
The cap implies |m+1/2+e_m|>=(3/4)|m+1/2|. Summing both
tails supplies 2*(16/9), and the integral comparison together with
2q-1/2>=n/10 gives exactly the coefficient
19200/(9*A^2)=640000/2187<300 in (20). All endpoints, not only
paired or symmetric shifts, are therefore covered.

**Finite poles, interpolation and complete remainder.** The only
possible spatial poles of the original finite F_n are R/a. From
Re a=-d, expansion of |R/a-1/2|^2 gives (23) exactly. Its lower
bound 6481/2824 exceeds (151/100)^2. Hence the closed outer disk
of radius 301/200 has a neighborhood free of every possible pole,
and each denominator exceeds d*(151/100-301/200)=1/160.
The outer bound (24) counts all M=n/3 nodes, including the anchor.
Hadamard's theorem concerns this finite holomorphic function. It
does not continue the infinite comb formula beyond the small disk.
The target radius 3/2 contains the entire spatial unit disk; the
strictly larger outer radius gives precisely the positive alpha stated.

The three rates in (21) are at least b/4, 3/20 and
-log(kappa_1), each at least 2*gamma. Thus (22) absorbs its
polynomial prefactors. Next
alpha*gamma-(1-alpha)*epsilon>=3*alpha*gamma/4, by (4).
Absorbing n^(1-alpha) leaves alpha*gamma/2 in (26).
Finally |a|/R<=rho<1, M=n/3 and
|R-a*z|>=R*(1-rho) on |z|=1 give the complete remainder
exponent tau-epsilon>=3*tau/4. Its factor n is absorbed leaving
tau/2. Their minimum is strictly positive, with constants fixed
before n. No effective value or uniformity over profiles is asserted.

The audit accepts (1) and (21)--(26) without changing the argument
or its direct inputs. The unchanged arithmetic script was replayed:
all 21 exact rational checks passed, including the endpoint coefficient,
pole separation and denominator margin. The full checks were inspected;
they support arithmetic only. This audit validates a local mathematical
input, not progress beyond the checked literature, formal verification,
full logarithmic control, or an RH candidate.

## Mathlib

Full matching coverage of this family-specific complete spatial estimate
has not been checked. The named three-circles and maximum-modulus
theorems and the cited convolution, concentration, Fourier and Laplace
results are standard supporting inputs; no matching Mathlib theorem
name or formal proof is asserted. Unknown coverage is not evidence of
absence. L697's existing audit is reused only for its stated factor,
gap and scalar interfaces. The separate informal conceptual audit above
validates the added spatial argument; it is not formal verification.
