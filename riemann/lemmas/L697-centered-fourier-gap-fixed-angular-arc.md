# Lemma 697: centered-gap decay on a fixed angular arc

## Hypotheses

Use L666's exact product and L696's centered-gap hypotheses. Explicitly,
d=5/4, x=-d, R=11/8, U=121/64, A=27/10, n=12q+3 with integer
q>=1, h=A/n and t_j=j/n for 0<=j<n. Fix one real sequence
e in l1(Z), with sup |e_m|<=1/8, before varying n, and put E=sum |e_m|.
With the negative-exponent angular Fourier convention, assume

    mu=delta_0+sum_(m in Z) delta_(m+1/2+e_m)

has a distributional Fourier gap I=(omega_*-g,omega_*+g), where

    f(t)=1/(d+t)-t/(U+d*t),
    omega_*=A*integral_0^1 f(t)dt,
    g>0,  I subset (0,2*pi).

L696 supplies existence of such a fixed profile and gap through its
prescribed-center specialization of L694. The transfer below applies
to every fixed profile satisfying these hypotheses. Keep the original
unit masses, anchor and finite scalar

    B_u(v)=product_(j=0)^(n-1) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    c_(0,n)(u)=R^(-1)*[1+sum_(-2q<=m<2q)
                              W_(x+i*h*(m+1/2+e_m))(u)].       (1)

The denominator uses 1/u and the j=0 factor is included.

## Conclusion

There are fixed delta,c>0 and finite C,N, independent of n, such that

    |c_(0,n)(exp(i*theta))|<=C*exp(-c*n)
       for |theta|<=delta and n=12q+3>=N.                       (2)

Constants may depend on the fixed profile and gap. Both finite
endpoints are retained. The proof gives the explicit bound (24) below,
with an existential but fixed arc width. No numerical gap width, arc
width or onset is claimed.

This is a local extension of L696 using known complex-measure,
concentration and Fourier inputs. The separate conceptual audit of
3 November 2026 (step 122), recorded below, accepts (2) and (24).
The bounded prior source comparison
found no matching finite fixed-arc theorem; this does not certify
originality. No spatial-moment, complete-logarithmic, full-circle,
H/support, actual-Xi or RH conclusion is asserted. In particular an
upper bound for this scalar on one arc does not decide the joint norm
or L666's signed lower-bound problem.

## Proof

### 1. Source scope and imported results

Reuse the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-centered-gap-fixed-angular-arc.md`.
The earlier C672a auxiliary-multiplier stop, L688's growing Taylor
filter and L695's absolute-tail stop concern different hypotheses;
none is a mathematical premise here. The parked step-105 screen is
not used. The required differences from L696 are the complex factor
law, its paid positive majorant and the actual signed endpoint pairing.

Import finite complex-measure integration and convolution from Jan
Kallsen and Paul Kruehner, *On uniqueness of solutions to martingale
problems — counterexamples and sufficient criteria*,
[arXiv:1607.02998v1](https://arxiv.org/pdf/1607.02998v1),
11 July 2016, Appendix A, Lemma A.1(6),(9)--(11),(14), pp.29--30.
In particular |nu_1*nu_2|<=|nu_1|*|nu_2|, integration is bounded
by variation, and positive-exponent Fourier transforms multiply.
Francesco Paolo Maiale, *Analysis of Sublaplacians on Lie Groups*,
notes for Fulvio Ricci's course, updated 28 May 2019,
[pp.8--9, Definition 1.5 and Proposition 1.7 with proof](https://poisson.phc.dm.unipi.it/~fpmaiale/notes/HAoLG.pdf),
provides the inspected convolution norm proof. These are finite-measure
inputs, not a theorem about pairing an infinite counting measure.

The complex exponential integral below is within the convergence
hypotheses of [NIST DLMF 1.14(iii), (1.14.17)--(1.14.18)](https://dlmf.nist.gov/1.14.iii),
version 1.2.8 (15 September 2026): the complex decay parameter has
strictly positive real part. Its elementary evaluation identifies the
actual factors; no general Laplace theorem is reproved.

Import non-identically-distributed Bernstein concentration from Roman
Vershynin, *High-Dimensional Probability*, first-edition author version,
20 May 2024, Definition 2.7.5, p.33, Theorem 2.8.1 and proof,
pp.36--37 ([author PDF](https://webapps.math.uci.edu/~rvershyn/papers/HDP-book/HDP-1.pdf)).
For independent centered real sub-exponential Y_j it gives

    P(|sum Y_j|>=z)
      <=2 exp[-c_B*min(z^2/sum ||Y_j||_(psi1)^2,
                            z/max ||Y_j||_(psi1))],           (3)

where c_B>0 is absolute. We apply this only to normalized positive
majorants constructed below, not to complex measures.

Import Schwartz Poisson summation and Fourier duality from Stephen
D. Miller, *Some notes on distributions*, 15 January 2006,
Theorems 4.1--4.2 and Section 6, pp.7--9
([author notes](https://sites.math.rutgers.edu/~sdmiller/musagei/distributions.pdf)).
The non-Schwartz limiting argument is proved for this kernel in
Section 5. L696 supplies the real signed-interval identity and the
scalar contraction at theta=0; their changed complex uses are checked
explicitly. Its prescribed-center existence is imported without a
second construction.

### 2. Exact complex factors and a fixed neighborhood

For u=exp(i*theta), t in [0,1], define

    lambda=d+t*u,  a=Re(lambda),
    alpha=t/(U*u+d*t),  r=alpha*lambda.

Direct division in (1), including t=0, gives

    W_(x+i*y)(u)=product_(j=0)^(n-1) Q_(t_j,theta)(y),
    Q_(t,theta)(y)=(1-i*alpha*y)/(1-i*y/lambda)
                 =r+(1-r)*lambda/(lambda-i*y).                (4)

Indeed the second ratio in each original factor is
(U*u+d*t-i*t*y)/(U*u+d*t), while the first is
(d+t*u)/(d+t*u-i*y). Thus no angular conjugation was changed.
For cos(theta)>=0, a>=d. The denominator U*u+d*t never vanishes
on the unit circle, since its modulus is at least U-d=41/64.
The finite complex measure

    nu_(t,theta)=r*delta_0+
              (1-r)*lambda*exp(-lambda*v)*1_(v>=0)dv          (5)

has algebraic mass one and positive-exponent Fourier transform (4),
because integral_0^infinity exp[-(lambda-i*y)*v]dv
=1/(lambda-i*y). In particular nu_(0,theta) is the real exponential
law of rate d, independent of theta.

Its variation is the positive measure

    M_(t,theta)=|r|*delta_0+
              |1-r|*|lambda|*exp(-a*v)*1_(v>=0)dv.

Set

    z(t,theta)=M_(t,theta)([0,infinity))=|r|+|1-r|*|lambda|/a,
    P_(t,theta)=M_(t,theta)/z(t,theta),
    m(t,theta)=integral v dP_(t,theta)(v)
             =|1-r|*|lambda|/(a^2*z(t,theta)).                (6)

Here z>=1 by the mass-one triangle inequality. The law P is a
zero/exponential mixture of rate a, so its mean is at most 1/d and
its second moment at most 2/d^2. At theta=0, L696's factor calculation
gives 0<=r<=48/67, z=1 and m(t,0)=f(t). All functions in (6) are
continuous jointly on compact neighborhoods of [0,1] times {0},
including t=0; their denominators are bounded away from zero.

Put

    b=c_B*min(g^2/(64*A^2),g/(8*A))>0,
    epsilon=min(b/4,1/40)>0,
    rho_1=4/5,
    kappa=sqrt(99/100),  kappa_1=(1+kappa)/2<1.                (7)

Choose delta>0 sufficiently small that, uniformly for t in [0,1]
and |theta|<=delta,

    cos(theta)>=0,  |sin(theta)|<=1/10,
    |r|<=rho_1,  log z<=epsilon,
    |m(t,theta)-f(t)|<=g/(4*A),
    |Q_(t,theta)(y)|<=kappa_1  for every real |y|>=2/5.        (8)

The first four conditions follow from the preceding compact continuity
and the strict margins at zero. For the last one, L696 Section 6
establishes |Q_(t,0)(y)|<=kappa for all t in [0,1], |y|>=2/5.
Formula (4) extends jointly continuously to y=+infinity and -infinity,
with value r: its remainder (1-r)*lambda/(lambda-i*y) tends uniformly
to zero, as all numerator parameters are bounded and a>=d. On each
bounded y interval there is no real pole. Compact continuity on these
two compactified half-lines, with kappa<kappa_1, therefore gives the
last condition on a fixed neighborhood. At infinity r(t,0)<=48/67
already has the required strict margin. Taking the minimum of these
finitely many positive neighborhood widths proves the simultaneous
choice (8); delta does not depend on n.

### 3. Concentration after paying variation growth

Let nu_(n,theta) be the pushforward under v=h*sum_j v_j of the
product of the n complex measures (5). Let X_j be independent real
variables with laws P_(t_j,theta), and V=h*sum_j X_j, with law P_n.
Finite complex-measure convolution and positive domination give

    K_n(s,theta):=W_(x+i*h*s)(u)
                =integral exp(i*s*v) dnu_(n,theta)(v),
    nu_(n,theta)([0,infinity))=1,
    |nu_(n,theta)|<=Z_n*P_n,
    Z_n=product_j z(t_j,theta)<=exp(epsilon*n).                (9)

The variables X_j and their independence are constructed for the
majorant. No independence of the fixed shifts e_m is assumed.

By (8) and L696's decreasing-integrand Riemann-sum bound,

    |E V-omega_*|<=g/4+A/(d*n)<=g/2
                         if n>=4*A/(d*g).                    (10)

For Y_j=X_j-E X_j, the exponential-mixture formula and a>=d give

    E exp(|Y_j|/4)
      <=exp(1/(4*d))*E exp(X_j/4)
      <=exp(1/5)/(1-1/5)<=25/16<2.

Thus ||Y_j||_(psi1)<=4 in the cited definition. Exiting I requires
|V-E V|>=g/2. Substitution z=g*n/(2*A) in (3) gives

    P_n(I^c)<=2*exp(-b*n).                                    (11)

Moreover, by independence and the moment bounds after (6),

    E V^2 <= (A/d)^2+2*A^2/(d^2*n)<16  (n>=15).               (12)

Although nu_(n,theta) has algebraic mass one, its variation cost in
(9) has not been dropped. It will multiply (11)'s square-root bound.

### 4. The density at every comb sample

The j=0 factor in both the complex law and its positive majorant is
the exponential law of rate lambda_0=d/h. Hence nu_(n,theta) has a
complex density p(v), zero for v<0, continuous for v>0. To see these
assertions directly, the convolution of factors j>=1 is a finite
mixture of an atom at zero and integrable exponential convolutions.
It has no other atoms. Convolving it with
lambda_0*exp(-lambda_0*v)*1_(v>=0) gives continuity at every v>0
by dominated convergence against its finite variation. It gives

    p(0+)=lambda_0*product_(j=1)^(n-1) r(t_j,theta),
    |p(0+)|<=lambda_0*rho_1^(n-1).                            (13)

The same assertions hold for the positive density p^+ of P_n. The
domination (9), initially an almost-everywhere density inequality,
and continuity give |p(v)|<=Z_n*p^+(v) at every v>0.

For an explicit positive-comb bound, write S=h*sum_(j>=1) X_j.
Then

    p^+(v)=E[lambda_0*exp(-lambda_0*(v-S))*1_(S<=v)].

Take tau=n/20<lambda_0. Since tau*h/a<=A/(20*d)=27/250,
each positive mixture has E exp(tau*h*X_j)<=250/223. Also
log(250/223)<=27/223<1/8. Consequently

    p^+(v)<=lambda_0*exp(n/8-n*v/20),  v>0,
    |p(v)|<=lambda_0*exp[(epsilon+1/8)*n-n*v/20].              (14)

Using pi>3, the geometric series at the positive comb samples and
n>=15 give

    sum_(k>=1) |p(2*pi*k)|
       <=2*lambda_0*exp[-(7/40-epsilon)*n].                    (15)

The zero half-density in (13) is a separate term, not a consequence
of a probability tail estimate.

### 5. Signed pairing and the justified infinite identity

First establish a summable even part without assuming any conjugacy
at the same nonreal u. For |y|>=2/5, (8) implies
|Im lambda|<=1/10, hence |lambda-i*y|>=3*|y|/4. Also
|(1-r)*lambda|<=(1+4/5)*(d+1)=81/20. Therefore

    |Q_(t,theta)(y)-r|<=6/|y|,
    |Q'_(t,theta)(y)|<=8/y^2.                                (16)

The derivative is i*(1-r)*lambda/(lambda-i*y)^2. Write W(y,u)
for W_(x+i*y)(u). Telescope the product of factors j>=1 around
product r_j, keeping Q_0(y)=d/(d-i*y) outside. The remainder has
n-1 terms, each bounded by
(5/4)*6*kappa_1^(n-2)/y^2. Since

    Q_0(y)+Q_0(-y)=2*d^2/(d^2+y^2),

the actual paired sum, using the same r_j at y and -y, satisfies

    |W(y,u)+W(-y,u)|
      <=[(25/8)*rho_1^(n-1)+15*(n-1)*kappa_1^(n-2)]/y^2
      <=19*n*kappa_1^(n-2)/y^2.                              (17)

Differentiating the n-factor product also gives

    |partial_y W(y,u)|<=8*n*kappa_1^(n-1)/y^2.                (18)

These estimates are independent of the gap and of Poisson summation.
In particular the half-lattice paired series converges absolutely.

For fixed n,theta, apply the cited Schwartz Poisson formula to
K_n(s,theta)*exp(-eta*s^2), eta>0. The rational K_n has no real
poles, and its derivatives have polynomial bounds, so this is indeed
Schwartz. Fubini against the finite complex measure in (9) gives its
angular Fourier transform 2*pi*(p*G_eta), where

    G_eta(v)=(4*pi*eta)^(-1/2)*exp(-v^2/(4*eta)).

On the lattice side, pair s=m+1/2 with -s. The Gaussian weights are
equal, and (17) permits dominated convergence as eta decreases to zero.
On the Fourier side, (13)--(14) and the even Gaussian give the limits
p(2*pi*k) for k!=0, and p(0+)/2 for k=0. These are valid for complex
p by applying the approximate-identity argument to its real and
imaginary parts. The negative nonzero samples have limit zero.

For completeness, the entire comb limit is dominated: for fixed n,
(14) gives |p(v)|<=C_n*exp(-a_n*v) for v>=0, where a_n=n/20.
For 0<eta<=1 the inequality |x|<=v+|x-v| gives

    |(p*G_eta)(x)|
       <=2*C_n*exp(a_n^2)*exp(-a_n*|x|).

This bound is summable at x=2*pi*k. No uniform exchange of the eta
limit with n is required. The translated-lattice phase is (-1)^k;
therefore

    B_n(theta):=lim_(L->infinity) sum_(-L<=m<L) K_n(m+1/2,theta)
       =pi*p(0+)+2*pi*sum_(k>=1) (-1)^k*p(2*pi*k),
    |B_n(theta)|<=pi*lambda_0*rho_1^(n-1)
           +4*pi*lambda_0*exp[-(7/40-epsilon)*n].             (19)

Now let F be L696's real oriented-interval primitive: it is the
sum of the signed indicators from m+1/2 to m+1/2+e_m. It converges
in L1, ||F||1<=E, and

    F'=sum_m delta_(m+1/2)-sum_m delta_(m+1/2+e_m).

With the negative-exponent Fourier transform, the distributional gap
and the absence of comb atoms inside I give
1-i*v*F-hat(v)=0 on I. This is pointwise because F-hat is continuous.
Since F is real, the reflected multiplier

    H(v)=1+i*v*F-hat(-v)

vanishes on I and obeys |H(v)|<=1+E*v for v>=0. This reflection
uses only reality of F, not reality of nu_(n,theta) or of its density.

By (9) and (12), integral v d|nu_(n,theta)|(v) is finite. Thus
K_n is continuously differentiable with derivative the integral of
i*v*exp(i*s*v), and ||K_n'||infinity<=integral v d|nu|. The
fundamental theorem of calculus, absolute summation of interval
corrections and Fubini are justified by
||F||1*integral v d|nu|<infinity. They yield

    sum_m [K_n(m+1/2+e_m,theta)-K_n(m+1/2,theta)]
       =integral F(s)*K_n'(s,theta)ds
       =integral i*v*F-hat(-v) dnu_(n,theta)(v).

Since nu_(n,theta) has algebraic mass one, the anchored symmetric
sum is exactly

    T_n(theta):=1+lim_(L->infinity)
                       sum_(-L<=m<L) K_n(m+1/2+e_m,theta)
       =B_n(theta)+integral H(v) dnu_(n,theta)(v).             (20)

Equations (9),(11),(12), Cauchy--Schwarz for the positive P_n, and
H=0 on I give the paid estimate

    |integral H dnu_(n,theta)|
       <=exp(epsilon*n)*sqrt(2+32*E^2)*sqrt(2*exp(-b*n))
       <=sqrt(4+64*E^2)*exp(-b*n/4).                          (21)

This is a justified L1 pairing with a bounded-growth multiplier, not
a direct rational test of an arbitrary tempered distribution.

### 6. Both finite endpoints and a surviving rate

The finite set -2q<=m<2q consists of complete unshifted pairs
m,-m-1. Its first omitted positive point has
h*(2q+1/2)=A/6=9/20. For n>=15, all segments from an omitted
unshifted point to its displaced point satisfy

    |y|>=9/20-h/8>=9/20-27/1200>2/5.

Thus (17)--(18) apply to the entire omitted tails. Since
sum_(m>=2q)(m+1/2)^(-2)<=1/(2q-1/2) and 2q-1/2>=n/10,
(17) gives

    sum_(m>=2q) |W(h*(m+1/2),u)+W(-h*(m+1/2),u)|
       <=19*n*kappa_1^(n-2)*h^(-2)/(2q-1/2)
       <=27*n^2*kappa_1^(n-2).                               (22)

The last numerical bound uses 190/A^2<27. The displaced corrections
in both omitted tails have total segment length at most h*E. From
(18) and 1/y^2<=25/4 their total absolute cost is at most

    h*E*8*n*kappa_1^(n-1)*(25/4)
       =135*E*kappa_1^(n-1).                                 (23)

No symmetry or tail decay rate for the fixed l1 profile is required.
Subtract these two fully paid tails from (20). For every |theta|<=delta
and allowed n>=max(15,4*A/(d*g)), (19),(21)--(23) give

    R*|c_(0,n)(u)|
      <=sqrt(4+64*E^2)*exp(-b*n/4)
        +pi*(d*n/A)*rho_1^(n-1)
        +4*pi*(d*n/A)*exp[-(7/40-epsilon)*n]
        +27*n^2*kappa_1^(n-2)+135*E*kappa_1^(n-1).            (24)

All rates are strictly positive: epsilon<=1/40 leaves at least 3/20
in the comb term, rho_1=4/5<1 and kappa_1<1. For example, take

    c=min(b/8,3/40,log(5/4)/2,-log(kappa_1)/2)>0.

Each polynomial factor in (24) is absorbed by the remaining positive
margin in its exponent, with one finite C independent of theta,n.
This proves (2). The fixed delta was chosen before n and the original
finite response, including the anchor and both endpoints, has been
used throughout.

### Independent conceptual audit — 3 November 2026, step 122

The unchanged invocation-start EXPLORE assessment covers exactly the
fixed-arc target and its complex-measure interfaces. This audit reuses
its inspected source statements, checks L666's defining ratio and finite
indices, and imports L696's already audited prescribed-center existence,
real contraction and signed-interval convention. It does not independently
audit the complete cited manuscripts or reconstruct L694/L693. L695's
absolute-tail stop, C672a's changed coefficients and L688's growing
Taylor filter remain comparisons, not inputs or counterexamples here.
The following verifies the existing proof without extending its scope.

**Exact factors and uniform arc.** Dividing B_u(x) by B_u(x+i*y)
in L666 gives, factor by factor,

    [(d+t*u)/(d+t*u-i*y)]*
    [(U*u+d*t-i*t*y)/(U*u+d*t)].

This is exactly (4); the denominator angle remains 1/u. The first
denominator has real part a>=d on the chosen arc, and
|U*u+d*t|>=U-d=41/64, so no real-y pole is introduced. At t=0
the atom vanishes and the measure is the real rate-d exponential.
For every other t, direct integration of the complex density gives
mass 1-r and transform (1-r)*lambda/(lambda-i*y). Atom and density
are mutually singular, so M in (6) is exactly the variation of that
factor, not an assumed probability measure. In particular z>=1.

At theta=0, r=t*(d+t)/(U+d*t) lies in [0,48/67], z=1, and
m=(1-r)/(d+t)=f(t). Their continuous formulas include t=0, with
denominators bounded away from zero. Compactness therefore gives the
first four requirements in (8) simultaneously for any fixed positive
epsilon and g. For the last requirement, on |y|>=2/5 the rational
remainder Q-r tends uniformly to zero at each infinity. On finite
closed y intervals its denominator cannot vanish. L696's real bound
|Q|<=kappa<kappa_1, including the strictly smaller limits r, extends
by compact continuity to one fixed arc, uniformly over t and both
unbounded y half-lines. This justifies a single delta>0 before n is
chosen; it is stronger than pointwise continuity in n or y.

**Positive normalization and concentration.** Variation domination of
the finite product and its pushforward gives |nu|<=Z_n*P_n, with
Z_n<=exp(epsilon*n); no mass-one identity for nu removes that cost.
Each normalized factor is a zero/exponential mixture of rate a>=d.
Thus EX_j<=1/d, EX_j^2<=2/d^2 and

    E exp(|X_j-EX_j|/4)
      <=exp(1/5)/(1-1/5)<=25/16<2.

The cited psi1 norm is consequently at most 4. The mean shift relative
to the real law is at most h*n*g/(4*A)=g/4. L696's Riemann-sum
error is at most A/(d*n), hence the stated onset puts the mean at
distance at least g/2 from I's complement. Bernstein at
z=g*n/(2*A) gives precisely the two constants in b in (7).
Independence here belongs to the constructed positive variables only.
The variance bound gives

    EV^2 <= (A/d)^2+2*A^2/(d^2*n)<16,  n>=15.

Since |H|<=1+E*v and H vanishes on I, Cauchy--Schwarz against P_n
therefore gives the first term of (24), with exponent
epsilon-b/2<=-b/4 and coefficient sqrt(4+64*E^2). Thus the
complex variation growth is fully paid by the fixed concentration
margin. No Bernstein assertion for a complex measure is used.

**Pointwise densities and the whole Fourier comb.** The convolution
of factors j>=1 is a finite sum of an atom at zero and absolutely
continuous exponential convolutions. After convolution with the j=0
rate-lambda_0 exponential, its density is continuous at every v>0.
For example, dominated convergence in that convolution uses the
absence of an atom at the moving point v>0 and the bounded kernel;
the right limit at zero retains only the atom at zero. This proves
p(0+)=lambda_0*product_(j>=1)r_j. The same argument applies to
p^+. The measure domination consequently upgrades from almost
everywhere to |p(v)|<=Z_n*p^+(v) at every positive comb sample.

With S=h*sum_(j>=1)X_j and tau=n/20, tau<lambda_0 and
tau*h/a<=27/250. Each normalized mixture has exponential moment
at most 250/223. For S<=v the conditional density kernel is bounded
by lambda_0*exp[-tau*(v-S)], and dropping the restriction only
increases this positive bound. It follows that

    |p(v)|<=lambda_0*exp[(epsilon+1/8)*n-n*v/20].

At v=2*pi*k, pi>3 gives the geometric ratio at most exp(-3*n/10).
For n>=15 its denominator exceeds 1/2. The first positive term has
exponent at most -(7/40-epsilon)*n, yielding (15); zero is accounted
for separately by (13). Density samples have not been inferred from
the probability tail.

For each fixed n,theta the rational K_n has no real pole, so its
Gaussian regularization is Schwartz. Fourier Fubini is justified by
finite variation and the integrable Gaussian and gives exactly
2*pi*(p*G_eta). Independently of Poisson, (17) makes the paired
half-lattice sum absolutely convergent; equal Gaussian weights on
opposite points permit its limit. For the entire Fourier side set
C_n=lambda_0*exp[(epsilon+1/8)*n], a_n=n/20. Then

    |(p*G_eta)(x)|
      <=C_n*exp(-a_n*|x|)*integral_R exp(a_n*|z|)*G_eta(z)dz
      <=2*C_n*exp(a_n^2)*exp(-a_n*|x|),  0<eta<=1.

This is summable at every x=2*pi*k. Continuity at positive samples,
the zero negative-side density and the two one-sided limits at zero
give exactly pi*p(0+) plus the signed positive comb in (19).
The phase is (-1)^k for the half-lattice. The regularization limit is
only taken at fixed n; its domination need not be uniform in n.

**Reflected identity and complex Fubini.** For b_m=m+1/2, the
oriented interval has derivative delta_(b_m)-delta_(b_m+e_m).
Summability gives ||F||1<=E. There is no comb atom in I, so the
distributional gap gives 1-i*v*F-hat(v)=0 there; continuity makes
it pointwise. Because F is real, conjugating this equality gives
H(v)=1+i*v*F-hat(-v)=0. This argument does not conjugate nu or
assume W(-y,u)=conjugate(W(y,u)) for nonreal u.

The bound integral v d|nu|<=Z_n*EV<infinity justifies differentiating
K_n, the sum of all interval corrections and Fourier Fubini:
their common absolute majorant is E*integral v d|nu|. The exponent
in K_n is positive, which explains F-hat(-v) in (20). Adding the
anchor uses the algebraic identity integral dnu=1, giving exactly
T_n=B_n+integral H dnu. This retains the anchor and does not test an
arbitrary tempered distribution against an unsupported rational test.

**Both tails and the five positive rates.** On |y|>=2/5, the arc
has |Im lambda|<=1/10, so |lambda-i*y|>=3|y|/4. Also
|(1-r)*lambda|<=81/20. Thus the sharper intermediate constants
27/5 and 36/5 imply the 6 and 8 in (16). In the telescoping
product, |Q_0|<=d/|y|, every remaining Q has modulus at most
kappa_1 and every r has modulus at most rho_1<kappa_1. Each
remainder is therefore at most (15/2)*kappa_1^(n-2)/y^2.
The two remainders contribute 15*(n-1), while
Q_0(y)+Q_0(-y)=2*d^2/(d^2+y^2) contributes 25/8 times
rho_1^(n-1). Their sum is at most 19*n*kappa_1^(n-2)/y^2.
The leading 1/y terms cancel algebraically at the same u. Product
differentiation gives (18) with n contracted terms. Both estimates are
independent of the gap and the previously discussed Poisson limit.

The retained set is invariant under m->-m-1. Its first omitted
unshifted ordinate is A/6=9/20. All displacement segments in both
tails stay above 9/20-27/1200>2/5 in absolute value, so the preceding
estimates cover the complete tails. The integral comparison gives
sum_(m>=2q)(m+1/2)^(-2)<=1/(2q-1/2), and
2q-1/2>=n/10 for every q>=1. Hence (22)'s coefficient is
190/A^2<27. The total length of all displaced tail segments is at
most h*E; with 1/y^2<=25/4 their derivative cost is exactly
A*8*(25/4)*E*kappa_1^(n-1)=135*E*kappa_1^(n-1).
No symmetry or quantitative tail rate for e has been assumed.

Combining these checks gives all five terms of (24) at its stated
onset. The rates are at least b/4, log(5/4), 3/20 and
-log(kappa_1), with only fixed-degree polynomial prefactors. The
proposed c is at most half of each relevant rate, so one finite C
absorbs those prefactors uniformly in theta and n. The audit accepts
(2) and (24) with no substantive repair. This establishes reliability
of the local input, not a new theorem beyond the previous derivation,
certified originality, a numerical onset, a full-spatial estimate or an
RH candidate.

## Mathlib

Full coverage of this family-specific complex-measure transfer and
fixed-arc estimate has not been checked. Supporting finite-measure
convolution, Fourier integration, probability concentration and
dominated-convergence mathematics are cited above; no matching Mathlib
theorem name is asserted. Unknown coverage is not evidence of absence.
The independent informal conceptual audit above is not formal
verification or an audit of the complete source manuscripts.
