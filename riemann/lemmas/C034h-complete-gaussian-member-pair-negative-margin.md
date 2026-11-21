# Corollary C034h: a negative margin for complete Gaussian member pairs

## Hypotheses

Let z=gamma-i*delta and w=eta-i*epsilon be independent parameters, with
gamma,eta>14, |delta|,|epsilon|<1/2, and displacement zero whenever its
ordinate is <=100. Let 1<=sigma<=2 be Gaussian half-variance. Define

    G(v)=exp(-v^2/(4*sigma))/sqrt(4*pi*sigma),
    h_z(x)=Re([G(x-z)+G(x+z)]/2),
    Q_j(x)=4*j*(3*x^2+j)/(x^2*(x^2+j)^2), j=1,2,
    D_j(z)=int_0^infinity (h_z(x)-h_z(0))*Q_j(x) dx,
    E_j(z)=int_0^infinity (h_z''(x)-h_z''(0))*Q_j(x) dx,
    P(z,w)=[D_1(z)E_2(w)+D_1(w)E_2(z)
                       -D_2(z)E_1(w)-D_2(w)E_1(z)]/2.

Both subtractions are inside ordinary integrals. Both translates and
both displacement signs are retained. The parameters may coincide;
they need not be actual zero ordinates or conjugate to one another.

## Conclusion

Uniformly over the stated domain,

    P(z,w)<-25*(gamma^-4*eta^-8+gamma^-8*eta^-4)<0.       (1)

This intermediate sign result of attempt1864 passes conceptual
audit1866 below on exactly the stated domain. It is not a complete RH
candidate. The constants are deliberately conservative.

The possible downstream application is C034c(20) and C034b's final
width prefix. No total-divisor assembly or final-prefix conclusion is
asserted here. Such use retains C034c(21), the actual divisor with all
multiplicities/conjugates, ordinate0 exclusion, strict strip, count,
through100 and retained-real-zero qualifications, reciprocal-square
tail, heat positivity/separate fixed-j errors, both fixed-v1 inputs,
zero drift/killing and Gaussian half-variance. Source-wide/finite-zero
validity, conditioning, entries/m, exact weights, TV<=2, observations,
signed-height cancellation and actual-Xi realization remain unresolved.

## Proof

### Scope, sources and the exact complete-member decomposition

Use the pre-invocation EXPLORE assessment1862, separately approved1863,
`drafts/literature/2026-11-20-laplace-paired-member-sign-attempt-1862.md`.
Its comparison found no applicable complete-pair sign theorem; this
does not certify originality. The work below supplies the missing
signed estimate, rather than redoing the existing representation.

C034d supplies the real cutoff identities and real-quadrant rational
sign. C034e supplies its exact polynomial identity (38)-(39) and angle
method; their needed domain extension and stronger core constants are
justified below. C034f(47)/(59) supplies the finite-contour shift with
its connector and the original origin/trace corrections. Its standard
inputs are Haslinger, *Complex Analysis*, Section2.2,
Theorem2.5/Corollary2.6, pp45-48,
[primary notes](https://www.mat.univie.ac.at/~has/scriptneu.pdf), and
Hunter, *Measure Theory*, Section5.6, Theorem5.18/Example5.19, p61,
[primary notes](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch5.pdf).
The inspected source coverage is reused; neither theorem supplies (1).
Only the finite-member specialization is used, not an infinite divisor
exchange or an assumed positive spatial profile. The Gaussian integral
int_R G=1 and its scaling identity are used with their usual real,
positive variance hypotheses.

Put R=2Q_1-Q_2. Write D_R=2D_1-D_2 and E_R=2E_1-E_2, so exactly

    P=[D_R(z)E_1(w)+D_R(w)E_1(z)
                            -D_1(z)E_R(w)-D_1(w)E_R(z)]/2. (2)

For a member with ordinate g and displacement d choose a=1 if d=0,
and a=13 otherwise. In the latter case g>100 is an essential hypothesis.
For e,t in {+1,-1} set c_e=e*g and b_et=-e*t*d. The real even member
is (1/4)sum_(e,t) G(x-c_e-i*b_et), also when d=0. For a rational F set

    H_z[F]=(1/4)sum_(e,t) int_a^infinity G(x-c_e)*F(x+i*b_et) dx,
    V_z[F]=(1/4)sum_(e,t) int_(a to a+i*b_et)
                                      G(v-c_e-i*b_et)*F(v) dv.

The t pairing makes these quantities real; it does not restrict the
independent pair of member parameters. The connector is oriented as
written for either sign of b_et. It vanishes for a real member.
For F=Q_1,R define the complete corrections

    alpha_F=int_0^a (h_z-h_z(0))*F-h_z(0)*int_a^infinity F,
    beta_F=int_0^a (h_z''-h_z''(0))*F
                 -h_z''(0)*int_a^infinity F-h_z'(a)*F(a)+h_z(a)*F'(a),
    A_F=alpha_F+V_z[F], B_F=beta_F+V_z[F''].

The real cutoff identity and C034f's shift therefore give

    D_F=H_z[F]+A_F, E_F=H_z[F'']+B_F.                 (3)

For a=1 this is C034d's unshifted identity. For a=13 it is C034f's
identity applied to the four terms above. The shift occurs only in
Re v>=13, which contains no rational pole. The far connectors tend
to zero uniformly for sigma in I=[1/2,3]: for each fixed member all
Gaussian derivatives there are bounded by a polynomial times
exp(-(x-g)^2/12). Near0, evenness bounds both subtracted numerators
by O(x^2), uniformly on I; the corresponding derivatives are bounded
on compact intervals. These bounds justify the ordinary integrals,
finite sums, products and Fubini applications used here uniformly on
I. The sign constants below need only sigma in [1,2]. No infinite
member sum or global Sobolev assertion is used.

In particular no raw integral of Q_j at0 is split out. The original
h_z''-h_z''(0) is retained on [0,a]; if transferred through0 instead,
C034d's quadratic subtraction would still be required. This proof
uses no origin bypass contour, so no residue is silently discarded.

### Bounds for positive Gaussian weighted integrals

For p=4,6, g>=14 and 1<=sigma<=2 define

    I_p(g)=(1/2)int_1^infinity [G(x-g)+G(x+g)]*x^-p dx.

We shall use the uniform bounds

    I_4(g)<(3/2)g^-4, I_6(g)<(15/4)g^-6.             (4)

Here G has real argument. On x>=g/2, put t=x/g. For t>=1 the
quantity t^-p exp(-g^2(t-1)^2/16) is <=1. For 1/2<=t<=1 put v=1-t.
The inequality -log(1-v)<=v+v^2 follows by differentiating the
difference, whose derivative is v(1-2v)/(1-v)>=0. Consequently

    log[t^-p exp(-g^2(t-1)^2/16)]
       <=p*v-(49/4-p)*v^2<=p^2/(49-4p).

For p=4 this last value is16/33<1/2, giving a bound2 for the
exponential; for p=6 it is36/25<3/2, giving a bound5. The latter
uses e<11/4, sqrt(e)<5/3, hence e^(3/2)<55/12<5.
Use half of the Gaussian exponential in this bound and integrate the
other half over the whole line. The Gaussian scaling integral is
sqrt(2), so the positive-center contributions on x>=g/2 are at most
sqrt(2)*g^-4 and (5/2)*sqrt(2)*g^-6, respectively, including their1/2.

On 1<=x<=g/2, G(x-g)<(5/24)exp(-(g-x)^2/8). Indeed the Gaussian
increases with sigma up to2 for |g-x|>=7, and
1/sqrt(8*pi)<5/24. For
f(x)=p*log(g/x)-(g-x)^2/8, its derivative has numerator
-x^2+g*x-4p. Its larger root is >g/2 for g>=14 and p<=6; thus on
this interval the maximum is at an endpoint. The normalized integral
is at most

    (5*g/96)*max{g^p exp(-(g-1)^2/8), 2^p exp(-g^2/32)}. (5)

Both expressions including the prefactor decrease with g>=14,
as logarithmic differentiation verifies. Since e^3>20>16,
exp(169/8)>16^7 and exp(49/8)>400. At g=14 the two quantities
in (5) are each <3/100 for p=4 and <3/25 for p=6.

The negative-center contribution is at most

    [5/(48*(p-1))]*exp(-(g+1)^2/8).

After multiplication by g^p this decreases for g>=14. At14,
exp(225/8)>16^8 shows that it is <1/1000 for each p. Finally
sqrt(2)<10/7, and
10/7+3/100+1/1000<3/2,
25/7+3/25+1/1000<15/4. This proves (4).
The scalar series and rational comparisons are certified below.

### Uniform absolute horizontal bounds

For real x>=1, direct multiplication of positive denominators gives

    Q_1(x)<=12x^-4, R(x)<=40x^-6,
    Q_1''(x)<=240x^-6, Q_2''(x)<=480x^-6.             (6)

For example, with t=x^2,
R=8(5t^2+9t+2)/[t(t+1)^2(t+2)^2]>0, and
(t+1)^2(t+2)^2=t^4+6t^3+13t^2+12t+4.
The bound for R follows by subtracting 8t^2(5t^2+9t+2) from
40(t+1)^2(t+2)^2; every remaining coefficient is positive.
The derivative formula is C034d(34):

    Q_j''=24j(10t^3+5j*t^2+4j^2*t+j^3)/[t^2(t+j)^4].

The difference between 10(t+j)^4 and
t(10t^3+5j*t^2+4j^2*t+j^3) has positive coefficients,
proving the last two bounds in (6). The Q_1 bound follows directly
from its displayed rational formula.

For v=x+i*b, x>=13, |b|<=1/2, put t=v^2. Then |t|>=x^2 and
|t+j|>=|t| because Re t>0. The same rational formulas yield

    |Q_1(v)|<13x^-4, |R(v)|<45x^-6,
    |Q_1''(v)|<260x^-6, |Q_2''(v)|<520x^-6.          (7)

For the four constants it suffices to substitute |t|>=169 into
4(3+1/|t|), 8(5+9/|t|+2/|t|^2),
24(10+5/|t|+4/|t|^2+1/|t|^3), and
48(10+10/|t|+16/|t|^2+8/|t|^3). Each is below the stated constant.
The bounds (7) also cover (6). The four positive horizontal weights
sum to the two-center weights in (4); increasing the cutoff to13
only reduces their integrals. Consequently, writing H_F=H_z[F]
and W_F=H_z[F''], we have

    |H_1|<20g^-4, |H_R|<200g^-6,
    |W_1|<1000g^-6, |W_2|<2000g^-6,
    |W_R|<=2|W_1|+|W_2|<4000g^-6.                  (8)

### Complete real-member origin corrections

For a real member a=1, so A_F=alpha_F and B_F=beta_F. For u>=13
put n=5/24 and

    F_0(u)=n*exp(-u^2/8),
    F_1(u)=n*(u/4)*exp(-u^2/8),
    F_2(u)=n*(u^2/16+1/4)*exp(-u^2/8),
    F_4(u)=n*(u^4/256+3u^2/32+3/16)*exp(-u^2/8),
    M_k(g)=[F_k(g-1)+F_k(g)]/2.

These bound the absolute Gaussian derivatives of order k=0,1,2,4
uniformly in sigma[1,2]. Each positive term in the derivative bound
is a constant times sigma^-q exp(-u^2/(4*sigma)), with q<=9/2;
its sigma derivative is positive since u^2>4*q*sigma. Thus its
maximum is at sigma2, where the displayed polynomial coefficients
are exactly the absolute derivative bounds. Each F_k decreases for
u>=13. It follows that sup_[0,1]|h_z^(k)|<=M_k(g), and
|h_z^(k)(0)|<=F_k(g). Evenness gives the Taylor bounds with
factors x^2*M_2/2 and x^2*M_4/2 for the two subtractions.

On [0,1], x^2 Q_1<=9/2 and x^2 R<=5. The first inequality reduces
to (3t-1)^2>=0. The second reduces to

    5t^4+30t^3+25t^2-12t+4>0,

where 25t^2-12t+4 has negative discriminant and positive leading
coefficient. The exact tails and endpoint data are

    int_1^infinity Q_1=2, int_1^infinity R=4/3,
    Q_1(1)=4, Q_1'(1)=-10,
    R(1)=32/9, R'(1)=-284/27.

The primitive -4j/[x(x^2+j)] verifies the tail values. Keeping every
term of (3) now gives

    |A_1| <=(9/4)M_2+2F_0(g),
    |A_R| <=(5/2)M_2+(4/3)F_0(g),
    |B_1| <=(9/4)M_4+2F_2(g)+4M_1+10M_0,
    |B_R| <=(5/2)M_4+(4/3)F_2(g)+(32/9)M_1+(284/27)M_0. (9)

After multiplying the first two by g^6 and the last two by g^8,
every positive summand decreases for g>=14. For a typical summand
g^k(g-1)^m exp(-(g-1)^2/8), logarithmic differentiation gives
k/g+m/(g-1)-(g-1)/4<0, since k+m<=12 and (g-1)^2>=169>48.
The unshifted case is even simpler. At g=14, the exact lower series
bounds exp(169/8)>1490000000 and exp(49/2)>43000000000 give the
following rational upper bounds for (9), in the same order:

    205928221289/15376800000000 <1/50,
    342465768239/23065200000000 <1/50,
    689176200513801/20502400000000 <40,
    680837992347401/18452160000000 <40.

Therefore the complete real corrections satisfy

    |A_1|,|A_R|<(1/50)g^-6,
    |B_1|,|B_R|<40g^-8.                              (10)

### Nonreal-member origin and connector corrections

Here g>100 and a=13. Put L=exp(-(g-13)^2/8). For real u>=g-13>87,
|b|<=1/2 and k=0,1,2,4, the explicit Gaussian derivatives give

    |G^(k)(u+i*b)|<=u^k exp(-u^2/8).

For example, |G|<=(16/45)exp(-u^2/8), and for k=4 the multiplier
before16/45 is at most
(u+1/2)^4/16+3(u+1/2)^2/4+3/4<u^4*(45/16).
The corresponding k=1,2 inequalities follow directly from
(u+1/2)/2 and (u+1/2)^2/4+1/2. The bound16/45 uses
pi>3 and exp(1/16)<=16/15. Since u^k exp(-u^2/8) decreases here,
both translates imply sup_[0,13]|h_z^(k)|<=g^k L.

The bounds x^2 Q_1<=9/2 and x^2 R<=5 hold on the entire positive
axis by the same polynomials used above. Also each tail integral
from13 is <1, and |F(13)|,|F'(13)|<1 for F=Q_1,R. For the
derivative check use the partial-fraction expression
Q_j=4/x^2-4/(x^2+j)+8j/(x^2+j)^2:
|Q_j'|<=16/x^3+32j/x^5 and
|R'|<=48/x^3+128/x^5, each <1 at13.
Taylor's theorem in the complete subtractions and the two endpoint
traces thus give |alpha_F|<=34g^2 L, |beta_F|<=36g^4 L.

On each connector the real distance from the center is >=g-13 and
the imaginary difference from it has modulus <=1/2. Thus |G|<=L.
Its length is <=1/2. By (7), |Q_1|,|R|,|Q_1''|,|R''|<1 there;
for the last use |R''|<=2|Q_1''|+|Q_2''|<1040/13^6<1.
The averaging weights sum to1. In particular each V has modulus
<=L, so |A_F|<=35g^2 L and |B_F|<=37g^4 L.

The functions g^8 L and g^12 L decrease for g>=100 by logarithmic
differentiation. At100, (g-13)^2/8=7569/8>900, and e^3>16 gives

    35*100^8/16^300<1/50, 37*100^12/16^300<40.

This proves (10) also for nonreal members. Both the complex phase
and all lower connectors have been paid, not suppressed by positivity.

### The negative horizontal kernel, including mixed cutoffs

Use C034d's symmetric kernel

    K(v,u)=[Q_1(v)Q_2''(u)+Q_1(u)Q_2''(v)
                          -Q_2(v)Q_1''(u)-Q_2(u)Q_1''(v)]/2.

It is negative on two real coordinates>=1 by C034d(35), and has
negative real part on two coordinates in Re>=13, |Im|<=1/2 by C034e.
One additional case is needed: a real coordinate x>=1 paired with
a complex-strip coordinate. In C034e(38)-(39), put T=x^2-1>=0 and
U=u^2-1. All coefficients outside the block

    105T^8 U^6+105T^6 U^8-100T^7 U^7

are nonnegative, with positive constant coefficient. The real factor
T^i/H(T+1) contributes zero argument, where
H(t)=t^2(t+1)^4(t+2)^4. The other factor has argument of magnitude
<=(10-j)*52/671<1 for every exponent0<=j<=8, by C034e(40)-(42).
Every nonzero term outside the block therefore has positive real part.
In the block j=6,7,8; the positive terms have cosine>7/8.
The same arithmetic-geometric mean step as C034e(44) pays the negative
term. For T=0 the block vanishes and the remaining i=0 terms have
positive real part. This proves Re K<0 also in the mixed-cutoff case.
This extension is a specialization of the displayed polynomial identity,
not an assumption of the original complex-strip domain at x=1.

There is a stronger quantitative bound on the retained positive-center
cores |x-g|<=3, |y-eta|<=3. A real coordinate is >=11; a nonreal
coordinate is >97. A nonreal T has |arg T|<1/96 because
x/(x^2-5/4)<1/96 for x>=97. A real T has argument zero. The factor
argument bounds from C034e then put EVERY rational monomial's total
argument below20/96<1/4. Its cosine is >31/32. For the special block,
the two positive terms minus the possible absolute size of its negative
term therefore give

    -Re K(v,u)>
      4965*(|T|^8|U|^6+|T|^6|U|^8)/(|H(v^2)H(u^2)|). (11)

Here 4965=96*(105*31/32-50); the subtraction50 uses
2|T|^7|U|^7<=|T|^8|U|^6+|T|^6|U|^8. The remaining polynomial
terms have nonnegative real part. Independent arguments and moduli
are used throughout; no conjugacy relation between v and u is required.

For either core coordinate, x=Re v>=11, |Im v|<=1/2. Thus
|T|>=x^2-5/4 and

    |H(v^2)|<=(x^2+1/4)^2(x^2+5/4)^4(x^2+9/4)^4.

The normalized denominator is a product of ten factors1+a_i with
sum a_i=29/(2x^2)<1. Its reciprocal is >=1-sum a_i: use
1+a_i<=1/(1-a_i) and product(1-a_i)>=1-sum a_i.
Bernoulli's inequality gives (1-5/(4x^2))^k>=1-10/x^2 for k=6,8.
Consequently

    |T|^8/|H(v^2)|>(4/5)x^-4,
    |T|^6/|H(v^2)|>(4/5)x^-8,

since (1-10/121)*(1-29/242)=23643/29282>4/5. Inserting these
bounds in (11), and using4965*16/25=15888/5>3100, yields

    Re K(v,u)<-3100*(x^-4*y^-8+x^-8*y^-4)            (12)

on every such core, for either displacement sign in either member.

### Integrating the core and paying all corrections

The Gaussian mass on [-3,3] is >4/5 uniformly in sigma[1,2]. Indeed
the two tails are at most (4*sigma/3)G_sigma(3), an increasing
function of sigma, hence less than
(8/3)*(5/24)*exp(-9/8)<5/27.
The last inequality follows from e>8/3 and exp(1/8)>9/8, so
exp(9/8)>3. The core mass is therefore >22/27>4/5.
For p>0, convexity and symmetry give

    int_(g-3)^(g+3) G(x-g)*x^-p dx
                   >=g^-p int_-3^3 G(v) dv>(4/5)g^-p.

The two displacement signs for the positive-center translate have
total averaging weight1/2. Thus each retained core contributes more
than (2/5)g^-p. All other horizontal kernel contributions have
negative real part by the preceding section and positive Gaussian
weights. Applying (12) on the two positive-center cores therefore
bounds the full horizontal determinant by

    P_H<-496*S, S=g^-4*eta^-8+g^-8*eta^-4,            (13)

where496=3100*(2/5)^2. This includes the negative-center translates,
the independent conjugate averages, diagonal and unequal pairs.

Expand (2) using (3). For each orientation (z,w), its correction
before the factor1/2 is exactly

    A_R(z)W_1(w)+H_R(z)B_1(w)+A_R(z)B_1(w)
       -A_1(z)W_R(w)-H_1(z)B_R(w)-A_1(z)B_R(w).

Equations (8) and (10) bound its absolute value by

    100*g^-6*eta^-6
      +(8000+8/5)*g^-6*eta^-8+800*g^-4*eta^-8.

Include the other orientation and divide by2. Since g,eta>=14 and
2g^-6*eta^-6<=S, the entire correction has absolute value at most

    [50+400+(8000+8/5)/392]*S=(115251/245)*S<471*S. (14)

Combining (13)-(14) gives P<-(6269/245)S<-25S. This proves (1)
with every origin, trace, connector and mixed correction retained.
No sign assumption was placed on any individual correction.

### Exact checks and limitations of verification

Run `python3 scripts/smoothed-law/laplace_paired_member_bounds_1864.py`.
The full certificate is
`scripts/smoothed-law/laplace_paired_member_bounds_1864.json`.
All32 exact rational/integer checks pass. Exponential lower bounds
use sums through degree8 at3 and degree100 at169/8 and49/2; their
complete rational sums are stored. The degree8 sum is89641/4480>20;
the latter sums have floors1494414009 and43673179097. The upper
bound e<11/4 uses its sum65/24 through degree4 and tail<=1/100.
The certificate checks the scalar thresholds, not the analytic proof.

The first arithmetic run compared the floor of the degree8 sum to20
using a strict inequality, and reported that check as false. The exact
sum is strictly greater than20 although its floor equals20. The check
was corrected to compare the complete rational sum; the first output
is preserved as `scripts/smoothed-law/laplace_paired_member_bounds_1864_first_pass.json`.
No failed mathematical inequality was hidden or repaired by rounding.

The floating diagnostic
`scripts/smoothed-law/laplace_paired_member_diagnostic_1864.json`
contains135 nonpositive sampled pairs. It is explicitly nonrigorous
and is not an input to this proof. No sample or refinement difference
is used to certify (1). Attempt1864 left the analytic argument pending
independent review, especially its mixed-cutoff domain, complex
averaging, Gaussian derivative bounds and all correction constants;
audit1866 below checks those obligations.
Neither this result nor its arithmetic checks verify the actual zero
data, the source-wide assumptions or any RH-equivalent realization.

### Conceptual audit1866 — 20 November 2026

**Verdict and scope.** Equations (1)-(14) pass on the full stated
finite-member domain, including coincident pairs, independent unequal
pairs, both displacement signs and both width endpoints. This audit
uses the pre-invocation SPECIALIZE assessment1865. It reproduces and
validates the existing local input; it claims neither a new sign theorem
beyond that result nor originality. The through100 condition is used
separately for each nonreal member. Uniformity on [1/2,3] is used only
for convergence and integral operations, not for the constants in (1).
No actual-divisor assembly is performed.

**Four terms, contours and subtractions.** Expanding the real part in
the definition of h_z gives the four terms of weight1/4, because G has
real coefficients on real sigma. If d=0 the duplicate terms retain
their weights and reduce to the two real translates of weight1/2.
Changing t to -t conjugates each horizontal term and its lower
connector, including the connector's differential. Thus H,V,A,B are
real after averaging; neither w=conjugate(z) nor z=w is assumed.

For nonzero b the oriented rectangle gives real+far-horizontal-lower=0,
so the lower connector has the plus sign in (3), for b<0 as well as
b>0. It lies in Re v>=13; all poles of Q_j and their derivatives are
on Re v=0. C034f(51)'s application of Haslinger Theorem2.5/Corollary2.6
therefore applies term by term. The real member has no contour shift.
Integrating h_z''F twice only over [a,M] gives the lower pairing
-h_z'(a)F(a)+h_z(a)F'(a). Splitting the ORIGINAL subtracted integrals
at a leaves precisely the two constants in alpha_F and beta_F. The
far trace vanishes. This independently checks (3) and both finite
traces without forming a divergent integral of F through zero.

For each fixed member, every required Gaussian derivative on these
paths, uniformly for sigma in [1/2,3], is bounded by a constant times
(1+x)^m exp(-(x-g)^2/12), for an appropriate finite m. The constant
may depend on the fixed member; there is no assertion of a dominator
uniform over an infinite divisor. This bounds all horizontal tails and
the far connectors, with the latter tending uniformly to zero. Near
zero the COMPLETE h_z is even; Taylor's theorem gives the uniform
x^2 bounds for both subtracted numerators. Hence origin tails have
uniformly vanishing integrals as well. Products of the resulting
one-variable absolute majorants are integrable. Finite counting measure
on the four terms and Lebesgue measure are sigma-finite, and every
integrand is measurable. Hunter Theorem5.18 therefore applies to these
complex products. The limiting input is Hunter, *Measure Theory*,
Section4.5 Theorem4.24 and Section4.6, pp49-50,
[primary notes](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf).
Uniform convergence follows from the uniform absolute tail bounds just
given, rather than from pointwise dominated convergence alone. No
single-translate origin subtraction or global Sobolev assumption is used.

**Gaussian integral envelopes.** The classical Gaussian integral
int_R exp(-t^2) dt=sqrt(pi), with real positive scaling, gives both
int_R G_sigma=1 and the sqrt(2) factor after halving its exponent.
On x>=g/2 the inequality in (4) uses half of that exponent and
1/(8*sigma)>=1/16. For v in [0,1/2], the derivative of
v+v^2+log(1-v) is v(1-2v)/(1-v)>=0. Maximizing
p*v-(49/4-p)*v^2 gives exactly p^2/(49-4p), since p=4,6<49/4.
The remaining half Gaussian integrates to sqrt(2); including the
positive-center weight1/2 gives the two stated leading constants.

For the low interval, the larger root of -x^2+g*x-4p exceeds g/2
because g^2>16p. Its derivative is first negative then positive
on that interval, with no interior maximum. The two endpoint bounds
in (5) therefore suffice. Their logarithmic derivatives, including
the g prefactor, are (p+1)/g-(g-1)/4 and 1/g-g/16. Both are negative
for g>=14, p<=6. The normalized negative-center bound has derivative
p/g-(g+1)/4<0. At14 the displayed exponential lower bounds give
the strict low-interval and negative-center bounds used in (4).
The estimate e<11/4 follows from the sum through degree4 and the
tail <=(1/120)/(1-1/6)=1/100; it implies all square-root exponential
bounds used there. No Gaussian probability or sign is assigned to a
complex translate: these envelopes concern the REAL horizontal weights.

**Real corrections.** At sigma=2 the absolute Gaussian derivative
polynomials of orders0,1,2,4 are exactly F_k as displayed, with the
normalizing constant replaced by the larger 5/24. Each constituent
sigma^-q exp(-u^2/(4*sigma)), q<=9/2, increases in sigma on [1,2]
because u>=13 gives u^2>4*q*sigma. Each monomial u^m exp(-u^2/8)
decreases for u>=13 and m<=4. Thus the positive translate on [0,1]
is bounded at g-1, and the negative translate at g, proving M_k.
At zero the sharper F_k(g) applies. The subtractions use Taylor
factors1/2 with M_2 and M_4, respectively.

Multiplying positive denominators verifies the two x^2F bounds.
For R, 25t^2-12t+4 has discriminant -256<0; the remaining terms
are nonnegative. This also proves the bound for all t>=0, as required
later. Differentiating the rational functions and their primitive
checks all six tail/endpoint data in (9). The signs of the two traces
have already been checked before their absolute values are taken.
Every scaled summand in (9) has k+m<=12. Its logarithmic derivative
is at most12/(g-1)-(g-1)/4<0; unshifted terms obey the stronger
bound12/g-g/4<0. Thus evaluation at14 is valid for the entire
unbounded domain. The four full rational endpoint values in (9)
were inspected and satisfy their respective 1/50,1/50,40,40 thresholds.

**Nonreal corrections and horizontal bounds.** For u>=87, put
r=1/(2u)<=1/174. The absolute Gaussian prefactor is at most16/45,
using sigma>=1, pi>3 and exp(1/16)<=16/15. After division by u^k,
the derivative polynomials for k=1,2,4 are bounded respectively by
(1+r)/2, (1+r)^2/4+1/(2u^2), and
(1+r)^4/16+3*(1+r)^2/(4u^2)+3/(4u^4).
For instance 1+r<3/2 and u>2 bound these by3/4,11/16,201/256;
each is less than45/16. Together with k=0 this verifies the claimed
bound |G^(k)(u+ib)|<=u^k exp(-u^2/8). Its right side decreases
here; the minimum real distance g-13 therefore gives g^k L on
[0,13], including both translates.

The integral of x^2|F| over [0,13] is <=65. Consequently
|alpha_F|<=(65/2)g^2 L+L<34g^2 L, and
|beta_F|<=(65/2)g^4 L+g^2 L+g L+L<36g^4 L.
The tail bounds and endpoint values used here are <1: integrate (6)
for the tails and use the displayed partial-fraction derivative bounds
for the endpoints. On each lower connector the real distance is still
at least g-13, and the imaginary difference has modulus <=1/2.
Its length is <=1/2. Equation (7) bounds both F and F'' by1 there,
including |R''|<=1040/13^6<1. Thus every connector has modulus <=L
after averaging, proving the constants35,37 without a sign assumption.
For k=8,12, the logarithmic derivative k/g-(g-13)/4 is negative
for g>=100; the test at100 and e^3>16 prove (10).

The rational formulas in (6)-(7) have no hidden phase estimate:
Re(v^2)>0 implies |v^2+j|>=|v^2|>=x^2. Bounding their numerators
by absolute coefficients gives exactly the four constants in (7).
These constants also dominate the real bounds (6). Their products
with (4) are <20,<200,<1000,<2000, giving (8). This use of (4)
extends the real integration domain down to1 only for an upper bound;
it never applies the complex rational bounds below13.

**Mixed domains and the stronger core.** C034e(38)-(39)'s audited
polynomial identity is used unchanged. For one real T>=0, its
nonzero monomial factors have zero argument. For the strip coordinate
the largest remaining angle is10*52/671<1. Outside the exceptional
block all coefficients are nonnegative with a positive constant, so
cos(theta)>=1-theta^2/2 gives positive real part. Inside the block
the largest angle is4*52/671<1/2. Its positive terms have cosine
>7/8, and 105*(7/8)>50 pays half of the negative coefficient100
by the arithmetic-geometric mean inequality. At T=0 the block
vanishes; the positive constant survives. This covers the previously
unlisted mixed domain without enlarging the asserted theorem's domain.

On the positive-center cores, real x>11 and nonreal x>97. Only
nonreal coordinates need an argument estimate. Since
x^2-96x-5/4>0 for x>=97, their |arg T|<1/96. C034e's lower bound
for the denominator arguments remains valid on this smaller strip.
Each rational monomial therefore has total argument <20/96<1/4,
even for opposite displacement signs. Its cosine is >31/32. Paying
the exceptional negative term by its absolute value gives the exact
coefficient96*(105*31/32-50)=4965 in (11); the other terms are
nonnegative and may be dropped. Real-coordinate factors have argument
zero even where x<13, so no strip hypothesis is misapplied there.

There are ten positive denominator factors after normalization,
with total increment29/(2*x^2). Each increment is <1 and their
sum is <1 for x>=11. Thus the stated reciprocal product estimate
and Bernoulli's inequality apply, giving23643/29282>4/5 for both
required powers. This verifies (12) uniformly on the full cores.

**Mass, pair expansion and decisive threshold.** For a real Gaussian,
int_3^infinity G <=(1/3)int_3^infinity xG=(2*sigma/3)G(3).
Both tails are therefore <=(4*sigma/3)G(3). This expression is
increasing in sigma and its value at2 is <5/27, using exp(9/8)>3.
The core mass exceeds22/27>4/5. Symmetry and convexity of x^-p
on the positive interval [g-3,g+3] then give the lower bound in
(13); the positive-center weights total1/2 even when d=0. Both
cores lie strictly above their respective cutoffs. The four-term
averages in both variables represent independent choices, so their
product has all16 terms. Every complementary horizontal term has
negative real kernel by the real, mixed or two-strip case, and a
positive real Gaussian weight. Keeping only the two positive-center
cores consequently gives P_H<-3100*(2/5)^2*S=-496*S.

Substituting D_2=2D_1-D_R and E_2=2E_1-E_R verifies (2).
Expanding (3) in (2) gives exactly the six displayed correction
products for each orientation. Equations (8),(10) give coefficients
100,8000+8/5,800 before the orientation average. The comparisons
2*g^-6*eta^-6<=S and
g^-6*eta^-8+g^-8*eta^-6<=S/196 follow respectively by a square
and by g,eta>=14. They give the exact correction coefficient
115251/245<471. Hence 496-115251/245=6269/245>25. No diagonal
exception, omitted mixed product or sign assumption on a correction
is needed. This establishes the stated strict inequality (1).

**Arithmetic evidence and limitations.** Replayed
`python3 scripts/smoothed-law/laplace_paired_member_bounds_1864.py`:
all32 exact checks pass. The complete program was inspected, along
with the full rational exponential series at3,169/8,49/2, the four
scaled real corrections and the correction/margin fields, using the
shared JSON inspector. The series are positive lower sums; comparison
of their full values, not their floors, justifies the strict bounds.
The preserved first-pass certificate still reports the exp3 floor-test
failure; it is not a failure of exp(3)>20. The regenerated certificate
retains its historical pending-audit label and is scalar evidence only;
the analytic verdict is this section. The floating135-pair diagnostic
is unused. No assertion about the actual zero data, infinite divisor
assembly, C034c(20), final prefix, signed height or Xi realization is
certified by this audit. Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage was not checked; no absence or formalization is
asserted. C034d/e/f's supporting source qualifications are retained.
The elementary Gaussian, contour, rational and integral results used
here are stated explicitly, but the complete uniform paired-member
inequality and this analytic/certificate combination have not been
matched to Mathlib. Its availability is not a premise of the proof.
