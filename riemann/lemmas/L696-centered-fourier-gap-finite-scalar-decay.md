# Lemma 696: a centered anchored gap gives exponential finite scalar decay

## Hypotheses

Use L666's exact product, with d=5/4, x=-d, R=11/8, U=121/64,
A=27/10, n=12q+3, q>=1, h=A/n and t_j=j/n, 0<=j<n. In particular
the denominator angle is 1/u and the j=0 factor is retained. Define

    f(t)=1/(d+t)-t/(U+d*t),
    omega_*=A*integral_0^1 f(t)dt.

For the transfer assertion, fix real e=(e_m) in l1(Z) with
sup |e_m|<=1/8, and put E=sum |e_m| and

    mu=delta_0+sum_(m in Z) delta_(m+1/2+e_m).

Assume its angular Fourier transform, with exponent -i*omega*s,
vanishes distributionally on I=(omega_*-g,omega_*+g), where g>0 is
fixed and I is contained in (0,2*pi). This is an infinite counting
measure with one fixed anchor and unit masses, not a finite-sum
vanishing assumption. The finite response is exactly

    c_(0,n)(1)=R^(-1)*[1+sum_(-2q<=m<2q)
                            W_(x+i*h*(m+1/2+e_m))(1)].          (1)

## Conclusion

Such a fixed sequence and g exist by the prescribed-center
specialization of L694 proved below. For every fixed sequence and gap
satisfying the hypotheses there are C,c>0 and N, independent of n,
such that

    |c_(0,n)(1)|<=C*exp(-c*n),       n=12q+3>=N.                 (2)

All finite endpoints, the anchor, original unit masses and j=0 factor
are retained. The proof gives an explicit endpoint error

    9*n^2*kappa^(n-2)+70*E*kappa^(n-1),
    kappa=sqrt(99/100)<1.                                      (3)

This is a family-specific transfer using known probability and Fourier
inputs, not a new general concentration or Poisson theorem. The prior
bounded source search found no matching finite scalar assertion; this
does not certify originality. The separate conceptual audit of
3 November 2026 (step 119), recorded below, accepts the stated bound.
It gives no angular interval, higher spatial-moment
bound, complete logarithmic inequality, H/support conclusion, actual-Xi
realization or RH result. In particular it does not contradict L690's
common-displacement result or resolve the signed problem left by L695.

## Proof

### 1. Scope and precise imported inputs

Reuse the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-fourier-gap-positive-convolution-transfer.md`.
Its scope includes the prescribed center, rational pairing and finite
endpoints. L690/L695 and the parked step-105 screen are comparisons,
not mathematical premises of this proof.

Import the characteristic-function mixture, scaling and independent
product rules, and the exponential characteristic function, from
Rick Durrett, *Probability: Theory and Examples*, version 5,
11 January 2019, Theorems 3.3.1--3.3.2, p.126, Example 3.3.8 and
Lemma 3.3.9, p.128 ([author PDF](https://math.duke.edu/~rtd/PTE/PTE5_011119.pdf)).
The convention in these rules is E exp(i*y*X). No general rule is
reproved; the actual ratios are checked in Section 3.

Import non-identically-distributed Bernstein concentration from Roman
Vershynin, *High-Dimensional Probability*, first-edition author version,
20 May 2024, Theorem 2.8.1, pp.36--37, using Definition 2.7.5, p.33
([author PDF](https://webapps.math.uci.edu/~rvershyn/papers/HDP-book/HDP-1.pdf)).
For independent mean-zero sub-exponential Y_j, and z>=0, it states

    P(|sum Y_j|>=z)
      <=2 exp[-c_B*min(z^2/sum ||Y_j||_(psi1)^2,
                            z/max ||Y_j||_(psi1))],             (4)

with an absolute c_B>0. The centered norms needed here are bounded
directly below; no unproved application of a centering exercise is used.

Import only Schwartz Poisson summation and Fourier duality from Stephen
D. Miller, *Some notes on distributions*, 15 January 2006, Theorems
4.1--4.2 and Section 6, pp.7--9
([author notes](https://sites.math.rutgers.edu/~sdmiller/musagei/distributions.pdf)).
Section 5 below justifies the non-Schwartz limit for this rational
kernel; the notes are not cited as supplying that extension.

The center construction uses L694's audited two-norm Picard argument.
Its primary coefficient input is Nir Lev, *An example concerning
Fourier analytic criteria for translational tiling*, Rev. Mat. Iberoam.
38 (2022), 1975--1991, Lemma 4.3, p.1984, equation (4.6), and the
prescription in Theorem 4.8 and Section 4.10, p.1988 onward
([DOI](https://doi.org/10.4171/RMI/1318),
[arXiv:2007.09930v3, Sections 4.3--4.10](https://arxiv.org/html/2007.09930v3#S4.SS3)).
Absolute summability is the local specialization in L694, not a
conclusion silently attributed to Lev's theorem statement.

### 2. Placing the gap at the required center

The integrand f is positive, since

    f(t)=(U-t^2)/[(d+t)*(U+d*t)]>0,       0<=t<=1.

Cauchy--Schwarz applied to d+t and its reciprocal gives
integral_0^1 1/(d+t)dt>=1/(d+1/2)=4/7. Also
integral_0^1 t/(U+d*t)dt<=1/(2U)=32/121. Consequently

    omega_*>=702/847>pi/4,
    omega_*<=A/d=54/25<3*pi/4.                                 (5)

For the strict comparisons one may use 3<pi<22/7. Thus the new
center c_*=omega_*/(2*pi) lies in L694's original annulus
(a,b)=(1/8,3/8). Keep its l=7/16, Phi, coefficient constant C_Lev,
K, r=min(1/8,1/(4*C_Lev*K)), Psi and M=max(1,||Psi||infinity).
Those constants are chosen before the cutoff width. Replace only its
c=1/4 and width by

    c=c_*,
    w=min((c_*-a)/2,(b-c_*)/2,r/(8*M))>0,
    chi(t)=eta((t-c_*)/w)+eta((t+c_*)/w),
    S(t)=-exp(pi*i*t)*chi(t),  P=Psi*S,  Q(t)=P(-t).             (6)

The support intervals are disjoint and strictly inside the same two
annuli. Hermitian symmetry, smooth periodic extension and support in
[-l,l] are unchanged. In particular Q belongs to the same A intersect Y
space, and its coefficient-sup norm is at most 4*M*w<=r/2. L694's
estimates (2)--(9), with these unchanged kernel constants, apply to
this Q. They give real alpha in l1, ||alpha||infinity<=r, for the
same Picard solution; no small A norm or width-uniform A bound is
required. Its equations (12)--(14), whose proof uses precisely these
support and symmetry conditions, give

    F_(2pi) mu=1+delta_0-chi       on (-b,b),       e_m=alpha_m.

Hence mu has an angular gap centered at omega_* of radius g=pi*w.
The anchor and masses remain unchanged and cap 1/8 prevents collisions.
This checks every changed hypothesis; it does not assume that L694's
originally stated existential interval already had this center.

The remaining proof applies to any fixed e and gap in the hypotheses,
not only the profile selected by (6).

### 3. Exact positive convolution and concentration

Write W_n(y)=W_(x+i*y)(1). Direct division of all n factors in L666
gives

    W_n(y)=product_(j=0)^(n-1) Q_j(y),
    Q_j(y)=(1-i*alpha_j*y)/(1-i*beta_j*y),
    alpha_j=t_j/(U+d*t_j),  beta_j=1/(d+t_j),
    r_j=alpha_j/beta_j=t_j*(d+t_j)/(U+d*t_j),
    Q_j(y)=r_j+(1-r_j)/(1-i*beta_j*y).                           (7)

Here 4/9<=beta_j<=4/5, r_0=0, and 0<=r_j<=rho=48/67<3/4.
For the latter bound, t*(d+t)/(U+d*t) is increasing on [0,1]:
the derivative numerator is U*d+2*U*t+d*t^2>0. Its endpoint value
is (d+1)/(U+d)=48/67. In particular these are positive mixtures.
Take independent X_j equal to zero with probability r_j and otherwise
exponential with mean beta_j. The cited rules give

    W_n(y)=E exp(i*y*sum X_j),
    F_n(s):=W_n(h*s)=E exp(i*s*V_n),  V_n=h*sum X_j.              (8)

The new notation F_n is a scalar kernel, not the signed-interval
primitive used below. The anchor contribution is F_n(0)=1.

The mean is m_n=h*sum f(j/n). Since
f'(t)=-(d+t)^(-2)-U*(U+d*t)^(-2)<0, the left Riemann sum gives

    0<=m_n-omega_*<=A*(f(0)-f(1))/n<=A*(4/5)/n.                (9)

For Y_j=X_j-E X_j, use E X_j<=4/5 and the mixture MGF to obtain

    E exp(|Y_j|/4)
      <=exp(1/5)*E exp(X_j/4)
      <=exp(1/5)/(1-1/5)<=25/16<2.

The last bound uses exp(z)<=1/(1-z) for 0<=z<1. Thus
||Y_j||_(psi1)<=4 in the source's norm. For n>=2*A*(4/5)/g,
leaving I implies |V_n-m_n|>=g/2. Applying (4) at z=g*n/(2*A)
gives

    P(V_n not in I)<=2 exp(-b*n),
    b=c_B*min(g^2/(64*A^2),g/(8*A))>0.                         (10)

Also E X_j^2<=2*(4/5)^2, so

    E V_n^2<=(A*4/5)^2+2*A^2*(4/5)^2/n<16.                   (11)

These are uniform in n. They concern mass and a moment, not yet a
distributional pairing.

### 4. Density at the Fourier-comb samples, including zero

The j=0 variable h*X_0 is exponential with rate lambda_0=d/h.
Let Z=h*sum_(j>=1) X_j. Then V_n has density, on v>0,

    p_n(v)=E[lambda_0*exp(-lambda_0*(v-Z))*1_(Z<=v)].            (12)

Set p_n=0 on v<0. The finite mixture defining Z has an atom only
at zero; conditional on any nonempty set of exponential choices its
law is continuous. Thus (12) is continuous on (0,infinity) and

    p_n(0+)=lambda_0*product_(j=1)^(n-1) r_j
            <=lambda_0*rho^(n-1).                             (13)

The density is bounded by lambda_0. For tau=n/20<lambda_0,
the integrand in (12) is at most lambda_0 exp[-tau*(v-Z)]. Since
tau*h*beta_j<=27/250,

    E exp(tau*Z)<=(250/223)^(n-1)<=exp(n/8),
    p_n(v)<=lambda_0*exp(n/8-n*v/20),       v>0.                (14)

Indeed log(250/223)<=27/223<1/8. Therefore, using pi>3 and n>=15,

    sum_(k>=1) p_n(2*pi*k)
      <=lambda_0*exp(-7*n/40)/(1-exp(-3*n/10))
      <=2*lambda_0*exp(-7*n/40).                               (15)

The zero value cannot be discarded just because the mean lies inside
the gap. Its exponentially small half-density term is retained next.

### 5. A justified infinite pairing

For fixed n, symmetric summation on the unshifted half-lattice obeys

    B_n:=lim_(L->infinity) sum_(-L<=m<L) F_n(m+1/2)
       =pi*p_n(0+)+2*pi*sum_(k>=1) (-1)^k*p_n(2*pi*k).          (16)

Here is a non-Schwartz justification. The rational kernel has real
coefficients in i*y, so F_n(-s)=conjugate(F_n(s)). Moreover
Re F_n(s)=O_n((1+s^2)^(-1)); this follows from the telescoping identity
proved in Section 6, or directly by separating its purely imaginary
leading 1/s term. Thus its symmetric real series converges absolutely.
For epsilon>0, F_n(s)*exp(-epsilon*s^2) is Schwartz. Apply the cited
Poisson formula for the translated lattice to this test. Its angular
Fourier transform is 2*pi*(p_n*G_epsilon), where

    G_epsilon(v)=(4*pi*epsilon)^(-1/2)*exp(-v^2/(4*epsilon)).

This transform identity follows from (8) by Fubini, since the Gaussian
is integrable and p_n is a probability density. The left side of
Poisson converges to B_n by pairing m with -m-1 and dominated
convergence of the real series. On the right, approximate-identity
convergence gives p_n(2*pi*k) for k!=0 and p_n(0+)/2 for k=0.
The latter follows by splitting the even Gaussian at zero and using
the two one-sided limits 0 and p_n(0+).

The sum over k also admits dominated convergence: for fixed n, (14)
gives p_n(v)<=C_n exp(-a_n*v), v>=0, for some a_n>0. For
0<epsilon<=1, the triangle inequality |x|<=v+|x-v| yields

    (p_n*G_epsilon)(x)
      <=2*C_n*exp(a_n^2)*exp(-a_n*|x|).

This is summable at x=2*pi*k and proves (16), with no uniform-in-n
regularization assumption. Equations (13)--(16) imply

    |B_n|<=pi*lambda_0*rho^(n-1)
                      +4*pi*lambda_0*exp(-7*n/40).             (17)

Now define F to be the sum of the real signed interval indicators
from m+1/2 to m+1/2+e_m, with the orientation sign as in L694.
It converges in L1, ||F||1<=E, and

    F'=sum_m delta_(m+1/2)-sum_m delta_(m+1/2+e_m).

For every n, ||F_n'||infinity<=E V_n<infinity. The fundamental
theorem of calculus gives, by absolute convergence and L1 summation,

    sum_m [F_n(m+1/2+e_m)-F_n(m+1/2)]
       =integral F(s)*F_n'(s) ds
       =integral_0^infinity i*v*F-hat(-v)*p_n(v)dv.             (18)

The last Fubini step is justified by ||F||1*E V_n<infinity, with
F-hat using the angular negative-exponent convention. In particular
this is a direct integration-by-parts extension, not an unsupported
test of a tempered distribution on a rational function.

As tempered distributions the same signed-interval identity and
Poisson for the half-lattice give

    mu-hat(omega)=1+2*pi*sum_k (-1)^k*delta_(2*pi*k)
                                      -i*omega*F-hat(omega).

There is no comb atom on I. Since F-hat is continuous, the assumed
distributional gap implies pointwise 1-i*v*F-hat(v)=0 on I.
Reality of F then implies

    H(v):=1+i*v*F-hat(-v)=0 on I,    |H(v)|<=1+E*v (v>=0).

Combining (16) and (18), the shifted anchored symmetric sum is exactly

    T_n:=1+lim_(L->infinity) sum_(-L<=m<L) F_n(m+1/2+e_m)
        =B_n+E H(V_n).                                        (19)

Using (10)--(11) and Cauchy--Schwarz,

    |E H(V_n)|
       <=sqrt(2+32*E^2)*sqrt(2)*exp(-b*n/2).                   (20)

Thus (17),(20) give an exponential bound for the justified infinite
sum, with the nonzero Fourier-comb samples and the half-density term
both paid. Tail probability by itself was not used as a bound on an
arbitrary distribution.

### 6. Paying both finite endpoints

For |y|>=2/5, (7) gives

    |Q_j(y)|^2=1-(1-r_j^2)*beta_j^2*y^2/(1+beta_j^2*y^2)
       <=1-(7/81)*y^2/(1+(16/25)*y^2)
       <=1-700/55809<99/100=kappa^2.                          (21)

The real limits r_j<=rho<kappa also obey this contraction. The finite
telescoping identity for product_(j>=1)Q_j minus product_(j>=1)r_j,
multiplied by Q_0, has terms

    Q_0*(Q_k-r_k)*product_(1<=j<k)Q_j*product_(k<j<n)r_j.

Here |Q_0|<=1/(beta_0*|y|), |Q_k-r_k|<=1/(beta_k*|y|),
and Re Q_0=1/(1+beta_0^2*y^2). Since beta_0=4/5 and
beta_k>=4/9, this proves

    |Re W_n(y)|
      <=[(25/16)*rho^(n-1)+(45/16)*(n-1)*kappa^(n-2)]/y^2
      <=3*n*kappa^(n-2)/y^2.                                 (22)

This establishes the real-series convergence used in Section 5.
Also Q_j'(y)=i*(beta_j-alpha_j)/(1-i*beta_j*y)^2 gives

    |W_n'(y)|<=(81/20)*n*kappa^(n-1)/y^2.                      (23)

The exact finite index set in (1) is invariant under m -> -m-1.
Its omitted unshifted pairs start at m=2q and -2q-1; their absolute
ordinate is at least h*(2q+1/2)=A/6=9/20. Along every displacement
segment in the omitted tail it stays at least
9/20-h/8>=9/20-27/1200>2/5, since n>=15.

For the unshifted omitted pairs, (22) and the decreasing-function
integral bound give

    sum_(m>=2q) 2*|Re W_n(h*(m+1/2))|
      <=6*n*kappa^(n-2)*h^(-2)*sum_(m>=2q)(m+1/2)^(-2)
      <=6*n*kappa^(n-2)*h^(-2)/(2q-1/2)
      <=9*n^2*kappa^(n-2).                                   (24)

Indeed 2q-1/2>=n/10 and 60/A^2<9. Apply (23) along the shifted
segments and sum the absolute differences in both tails. Their sum is
at most

    h*E*(81/20)*n*kappa^(n-1)*(25/4)
       <=70*E*kappa^(n-1).                                   (25)

Equations (24)--(25) prove exactly (3). No rate of decay for the l1
tail of e was needed, and the entire omitted tail, rather than a
fixed-index preview, has been bounded.

Finally, combine (17),(19),(20),(24),(25) and multiply by 1/R.
This gives the explicit bound

    R*|c_(0,n)(1)|
      <=sqrt(4+64*E^2)*exp(-b*n/2)
        +pi*(d*n/A)*rho^(n-1)+4*pi*(d*n/A)*exp(-7*n/40)
        +9*n^2*kappa^(n-2)+70*E*kappa^(n-1).                   (26)

It holds for n>=max(15,2*A*(4/5)/g) in the prescribed progression.
All constants are independent of n for the fixed profile and gap.
Since kappa<=exp(-1/200), rho<3/4 and b>0, polynomial factors
can be absorbed, for example with c=min(b/4,1/1000)>0 and a finite
C depending on E,g and the imported absolute c_B. This proves (2).
No effective numerical gap width, onset or Bernstein constant is claimed.

### Independent conceptual audit — 3 November 2026, step 119

This audit uses the unchanged SPECIALIZE assessment
`drafts/literature/2026-11-03-centered-gap-scalar-audit-scope.md`.
Its TARGET matches the invocation-start Next action exactly. The
step-116 source statements and step-118 interface checks are reused;
no broader probability, Poisson or rational-test theorem is imported.
L666's defining product and finite indices and all of L694's construction
and completed audit were checked against the applications here. L693's
cutoff convention is inherited through L694. L695's absolute-tail stop
is a comparison, not an input or a refutation of this signed scalar bound.
The following checks validate the existing argument, without extending
its conclusion or certifying originality.

**Prescribed center and the same fixed point.** The lower bound in (5)
is exactly A*(4/7-32/121)=702/847. Since pi/4<11/14<702/847 and
54/25<9/4<3*pi/4, c_* is strictly in (a,b). The choice of w places
both closed support intervals strictly within the original annuli;
their distance from zero is positive. The smooth real even chi gives
the same Hermitian symmetry for S, P and Q. In particular reflection
preserves the real-coefficient condition in Y. Directly,

    ||Q||Y<=||P||L1<=4*M*w<=r/2,

while two integrations by parts give finite ||Q||A. No small or
width-uniform A norm is required. Phi, the coefficient constant, K,
r, Psi and M are unchanged, so L694's two-norm iteration and its
limit identification apply to this very Q. On the positive plateau
J=(c_*-w/2,c_*+w/2), its identity (14) is zero. The angular interval
2*pi*J has center omega_* and radius pi*w, exactly as stated. Thus
one fixed admissible profile and g are obtained before n varies;
the conditional transfer below still applies to every fixed profile
and g satisfying the hypotheses, without a uniform bound over profiles.

**Exact law, mean and concentration.** In L666 at u=1, one product
ratio at a=x+i*y is

    [(x-t_j)/(x+i*y-t_j)]*
    [(U-t_j*(x+i*y))/(U-t_j*x)]
      =(1-i*t_j*y/(U+d*t_j))/(1-i*y/(d+t_j)).

This checks (7), including j=0, with no additional normalization.
The derivative of r(t) has positive numerator U*d+2*U*t+d*t^2,
so r_j<=r(1)=48/67<3/4. Every mixture weight is nonnegative and
r_0=0, so the cited characteristic-function rules apply and V_n
has no atom at zero. Its mean is h*sum(beta_j-alpha_j), giving (9)
by the decreasing integrand's left Riemann sum. Independence concerns
the constructed X_j; it is not an assumption on the shifts e_m.

For each centered Y_j, E exp(|Y_j|/4) is at most
exp(1/5)/(1-1/5)<=25/16<2. Thus the exact psi1 definition used by
Bernstein gives norm at most 4. Substituting z=g*n/(2*A) into (4)
gives the two exponents n*g^2/(64*A^2) and n*g/(8*A). The onset
n>=2*A*(4/5)/g makes the distance from the mean to the complement
of I at least g/2. Also

    E V_n^2 <= (54/25)^2+2*A^2*(4/5)^2/n <16

for every n>=15 here. The fixed positive b in (10) and the moment
used later are therefore justified. No density estimate is inferred
from Bernstein alone.

**Density, comb and Gaussian limit.** Conditioning on Z in (12)
is legitimate because h*X_0 is an independent exponential of rate
lambda_0=d*n/A. Every nonempty exponential component of Z is
continuous; its only possible atom is at zero, of weight product r_j.
Consequently p_n is continuous at each positive comb sample, zero
on the negative half-line, and has right limit (13) at zero. The
choice tau=n/20 satisfies tau<lambda_0 and tau*h*beta_j<=27/250.
The mixture MGF is at most 250/223 for every j>=1, and
log(250/223)<=27/223<1/8. This proves (14) directly. At positive
comb samples it gives

    sum_(k>=1) p_n(2*pi*k)
      <=lambda_0*exp(-7*n/40)/(1-exp(-3*n/10)),

whose denominator exceeds 1/2 for n>=15. The atom of Z and the
one-sided density at zero have not been discarded.

For each fixed n, (22) gives summable real parts on the half-lattice
outside a finite set. Its proof below uses only the finite product,
not (16) or the gap, so there is no circular use. Pairing m with
-m-1 cancels the imaginary parts exactly. The rational F_n has no
real poles and its derivatives have polynomial bounds, so multiplying
by exp(-epsilon*s^2) really gives a Schwartz function. Fourier Fubini
then gives 2*pi*(p_n*G_epsilon), with the normalization in Section 5.

For fixed n put a_n=n/20 and C_n=lambda_0*exp(n/8). On v>=0,
p_n(v)<=C_n*exp(-a_n*v). Since |x|<=v+|x-v|, integrating the
Gaussian gives

    (p_n*G_epsilon)(x)
      <=C_n*exp(-a_n*|x|)*integral exp(a_n*|z|)*G_epsilon(z)dz
      <=2*C_n*exp(a_n^2)*exp(-a_n*|x|),  0<epsilon<=1.

This dominates the whole two-sided comb series, including negative k.
Approximate-identity convergence at zero gives p_n(0+)/2 because
the Gaussian is even and the two one-sided limits are 0 and p_n(0+).
Poisson's translated-lattice phase is (-1)^k. Dominated convergence
on both sides therefore yields exactly (16), including the coefficient
pi of its zero half-density. These limits are taken for each fixed n;
no uniform exchange with n tending to infinity is needed for (17).

**L1 pairing and reflected sign.** The oriented interval from b_m=m+1/2
to b_m+e_m has derivative delta_(b_m)-delta_(b_m+e_m). Its integral
against F_n' is F_n(b_m+e_m)-F_n(b_m). Since ||F||1<=E and
||F_n'||infinity<=E V_n, both the infinite correction and Fourier
Fubini in (18) converge absolutely. The exponent in the characteristic
function is positive, hence the transform in that integral is F-hat(-v).
The distributional derivative has transform i*v*F-hat(v); consequently
the gap gives 1-i*v*F-hat(v)=0, with no comb atom inside I.
Continuity of F-hat upgrades that equality to a pointwise equality on I.
Reality of F conjugates it to 1+i*v*F-hat(-v)=0. This establishes the
sign of H and the exact anchored identity (19). Finally,

    E |H(V_n)|^2 <= 2+2*E^2*E V_n^2 <= 2+32*E^2,

so Cauchy--Schwarz with (10) proves (20). This is a bounded-growth
multiplier paired with a density, not a rational test of an arbitrary
tempered distribution or an estimate from concentration alone.

**Both endpoints and the positive rate.** For |y|>=2/5, using
1-r_j^2>=7/16 and beta_j>=4/9 in the exact factor modulus gives
the deficit at least 700/55809>1/100 in (21). In the telescoping
identity, the separate Q_0*product r_j term has real part at most
(25/16)*rho^(n-1)/y^2. Each of the other n-1 terms has modulus
at most (45/16)*kappa^(n-2)/y^2. Their combined coefficient is
at most 3*n*kappa^(n-2), proving (22). This also supplies the
independent real-series justification used above. Differentiating
the finite product gives n terms, with

    |Q_j'(y)| <= (4/5)*(81/16)/y^2=(81/20)/y^2

and n-1 contracted factors in each term, proving (23).

The retained indices -2q<=m<2q form complete m,-m-1 pairs. The first
omitted pair has |h*(m+1/2)|=A/6=9/20, and every omitted displacement
segment has |y|>=9/20-h/8>=9/20-27/1200>2/5. Further,
2q-1/2>=n/10 for q>=1. The integral comparison in (24) therefore
has coefficient 60/A^2<9 after inserting h=A/n. For (25), summing
segment lengths in both tails costs at most h*E, and the remaining
constant is A*(81/20)*(25/4)=68.34375<70. These are bounds on
the entire omitted tails. They do not require symmetry of e, a decay
rate for its l1 tail, or an unpaired absolutely convergent rational sum.

All terms in (26) are now justified at its stated onset. Since
kappa<=exp(-1/200), rho<3/4 and b>0, each polynomial prefactor is
absorbed into C*exp(-c*n) with c=min(b/4,1/1000)>0. Constants and
onset may depend on the fixed profile and gap, never on n. The audit
accepts (2), (3) and (26) without a substantive repair or stronger
conclusion. It validates this local source-based specialization only;
angular, spatial-moment, complete-logarithmic, H/support and actual-Xi
transfers remain unresolved. No RH candidate has been obtained.

## Mathlib

Full matching coverage of this finite scalar transfer and L694's
summable prescribed-center construction has not been checked. The
probability, Schwartz Poisson and elementary convergence inputs are
cited or justified above; no matching Mathlib theorem names are
asserted. Unknown coverage is not evidence of absence. The informal
independent audit above is not formal verification or an audit of the
complete source manuscripts.
