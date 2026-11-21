# Corollary C032y: Gaussian resolvent pairs and a uniform spectral tail

## Hypotheses

Retain C032m's actual positive-ordinate divisor Z+, with multiplicity,
and its normalization

    a_rho=gamma_rho-i*delta_rho, gamma_rho>14, |delta_rho|<1/2,
    G_sigma(z)=exp(-z^2/(4*sigma))/sqrt(4*pi*sigma),
    f_(sigma,a)(z)=[G_sigma(z-a)+G_sigma(z+a)]/2,
    p_sigma(z)=sum_(rho in Z+) f_(sigma,a_rho)(z),
    R_sigma(w)=integral_0^infinity
                  [p_sigma(x)-p_sigma(i*w)]/(x^2+w^2) dx,
    E_sigma(w)=4*integral_0^w t*R_sigma(t) dt.

Every quotient has its continuous removable value, including x=w=0
and w=+/-i*x. Throughout, sigma is real and 1<=sigma<=2. No RH,
reality of a_rho, profile sign or finite-coordinate availability is
assumed. A pair of off-line zeros with the same positive ordinate
remains two members of Z+, with their own multiplicities; the displayed
factor1/2 is not applied again to that pair.

Import the explicit count of Hasanalizade-Shen-Wong, *Counting zeros
of the Riemann zeta function*, arXiv:2107.06506v1 (14 July2021),
[Corollary1.2/(1.5), p.2, proof p.15](https://arxiv.org/pdf/2107.06506v1):

    |N(T)-T/(2*pi)*log(T/(2*pi*e))|
      <=0.1038*log(T)+0.2573*log(log(T))+9.3675, T>=e,       (1)
    N(T)=#{rho in Z+ : gamma_rho<=T}.

The count includes multiplicity and the upper endpoint. This is a
named source input, not a fresh verification of its proof or finite
database. Its corollary proof uses Theorem1.1/Table2 above
30,610,046,000 and the cited finite S(T) verification below that height.
The statement and complete corollary proof were inspected in
source-notes1577 and recovery1578. They provide no individual coordinates.

C032j/m's zero-ordinate exclusion, strip/counting and fixed-v1 source
qualifications are retained. Their through100/first-zero and heat
inputs remain qualified when this interface is used with C032q's
probability laws. Heat positivity and those probability claims are
not needed for the analytic estimates proved here. No independent
audit of the external preprints or finite-zero data is asserted.

## Conclusion

Write W_F(z)=exp(-z^2)*erfc(-i*z), D_F(z)=W_F(z)-exp(-z^2), and
k_sigma=2*sqrt(sigma). For one divisor member a define the entire
function

    B_(sigma,a)(w)=D_F((i*w-a)/k_sigma)
                     +D_F((i*w+a)/k_sigma).

The exact paired, subtracted resolvent and its primitive are

    r_(sigma,a)(w)=sqrt(pi)/(8*sqrt(sigma))
                            * B_(sigma,a)(w)/w,             (2)
    r_(sigma,a)(0)=i*sqrt(pi)/(8*sigma)
                            *D_F'(a/k_sigma),
    e_(sigma,a)(w)=sqrt(pi)/(2*sqrt(sigma))
                            *integral_0^w B_(sigma,a)(t) dt. (3)

In (2), the quotient has its entire removable extension. These
functions equal respectively the integral of
[f_(sigma,a)(x)-f_(sigma,a)(i*w)]/(x^2+w^2) over x>=0 and its
primitive 4*integral_0^w t*r_(sigma,a)(t)dt. Both are even in w.
They agree on the whole complex plane, including the imaginary-axis
removable cases, rather than only as boundary or principal values.

The series R_sigma=sum_rho r_(sigma,a_rho) and
E_sigma=sum_rho e_(sigma,a_rho) converge absolutely and uniformly
on [1,2] times {|w|<=2}. Here is an explicit tail certificate. Put

    c_Y=exp((Y+1/2)^2/4)/sqrt(4*pi), d=sqrt(26),
    A=5*c_d+(4/15)*(c_0+c_2),
    B=(8/3)*c_0*sqrt(8*pi).

For every real H>=16, retain every member with gamma_rho<=H and set
E_(sigma,H)=sum_(gamma_rho<=H) e_(sigma,a_rho). Then

    sup_(sigma in[1,2], |w|<=2) |E_sigma(w)-E_(sigma,H)(w)|
      <= T_E(H)
       :=16*(log(H)+1)/H * [B+A*H^2*exp(-H^2/32)].          (4)

The analogous R error is at most T_E(H)/8. The stated upper bound
is decreasing for H>=16 and tends to zero, with order log(H)/H.
The finite-divisor and arithmetic interface is specified in section6.
No finite coordinates, implemented evaluator, feasible cost estimate,
kernel table, cone certificate or residual below1/2 is supplied.

This is a specialization of known transform and counting inputs,
recorded 18 November2026 under the prior SPECIALIZE assessment1577.
Critical audit1581 below validates this analytic interface under its
stated source qualifications. Actual-Xi all-degree
positivity, full odd cancellation, arbitrary variation and unsmoothed
realization remain open; there is no complete RH candidate.

## Proof

### 1. Precise imported transforms and scope of the specialization

NIST DLMF Version1.2.8, [equation7.7.2](https://dlmf.nist.gov/7.7.E2),
states

    integral_R exp(-u^2)/(u-z) du=pi*i*W_F(z), Im(z)>0.     (5)

[Definition7.2.3](https://dlmf.nist.gov/7.2.E3) and Section7.2(i)
give the definition and entireness of W_F and erfc.
[Reflection7.4.3](https://dlmf.nist.gov/7.4.E3) gives
W_F(-z)=2*exp(-z^2)-W_F(z); hence D_F is entire and odd.
These are imported identities, not reproved here. The primary domains
and the contour warning in Ivanov-Adkins (2023), Section3.1/Figure2,
p.10, [doi:10.1017/S0022377823000077](https://doi.org/10.1017/S0022377823000077),
were inspected in notes1577. We do not apply (5) unchanged in the lower
half-plane or use an erfc asymptotic outside its remainder domain.
DLMF7.7.6 is covered by the assessment but is not needed for this proof.

For compactly dominated holomorphic integration use Haslinger,
*Complex Analysis*, Section2.7,
[Theorem2.39, pp.67-68](https://www.mat.univie.ac.at/~has/scriptneu.pdf),
with the coverage and verified hypotheses in C032m. Its role below
is to identify the entire removable quotient; it supplies no effective
spectral tail. The general transform and holomorphic integration
theorems already exist. What must be checked here is the normalization,
complex centre, subtraction, removable extension, and explicit
infinite-divisor error for this particular family.

### 2. Safe-domain computation, including both pole terms

Fix a=gamma-i*delta and sigma. Initially take Re(w)>1/2, so that
Re(w)>|Im(a)| and w is nonzero. Define

    T_a(z)=integral_R G_sigma(x-a)/(x-z) dx.

For z=+i*w and z=-i*w these integrals are absolutely convergent and
their poles are off the real x-axis. On substituting x=a+k_sigma*u,
the u contour is the horizontal line with height -Im(a)/k_sigma,
and the prefactor is 1/(k_sigma*sqrt(pi)). The pole is
zeta=(z-a)/k_sigma. For z=i*w it lies strictly above both this line
and the real u-axis; for z=-i*w it lies strictly below both. Indeed
their imaginary parts are respectively
(Re(w)-Im(a))/k_sigma>0 and (-Re(w)-Im(a))/k_sigma<0,
and their displacements from the original contour are
+Re(w)/k_sigma and -Re(w)/k_sigma.

Move each contour to the real u-axis. No pole is crossed. On the
two vertical sides at real part +/-L, the modulus of exp(-u^2)
is at most exp(-L^2+Y^2), where Y bounds the fixed heights, while
the denominator is bounded below by L-|Re(zeta)| for large L.
The side integrals therefore tend to zero. This justifies the
shift even though the centre a is complex.

Apply (5) to the upper pole. For a lower pole zeta, substituting
u=-v first gives

    integral_R exp(-u^2)/(u-zeta) du
      =-integral_R exp(-v^2)/(v-(-zeta)) dv
      =-pi*i*W_F(-zeta).

Thus in the safe domain

    T_a(i*w)= i*sqrt(pi)/k_sigma *W_F((i*w-a)/k_sigma),
    T_a(-i*w)=-i*sqrt(pi)/k_sigma *W_F((i*w+a)/k_sigma).

Evenness of the denominator and x -> -x give exactly

    integral_0^infinity f_(sigma,a)(x)/(x^2+w^2) dx
      =(1/2)*integral_R G_sigma(x-a)/(x^2+w^2) dx
      =sqrt(pi)/(8*sqrt(sigma)*w)
          *[W_F((i*w-a)/k_sigma)+W_F((i*w+a)/k_sigma)].       (6)

The last equality uses
1/(x^2+w^2)=[1/(x-i*w)-1/(x+i*w)]/(2*i*w).
In particular the factor1/2 from the even pair has been retained.

For Re(w)>0, integral_0^infinity dx/(x^2+w^2)=pi/(2*w).
For positive real w this is the elementary arctangent integral;
both sides are holomorphic on Re(w)>0 by compact domination, giving
the stated domain. Moreover

    f_(sigma,a)(i*w)=1/(4*sqrt(pi*sigma))
       *[exp(-((i*w-a)/k_sigma)^2)+exp(-((i*w+a)/k_sigma)^2)].

Multiplying this by pi/(2*w) and subtracting from (6) proves (2)
in the safe domain. The exponential subtraction has exactly the
same prefactor as the two W_F terms. No separated integral here
is being evaluated at a real spatial pole or at w=0.

### 3. Identification with the entire removable integral

For one pair f=f_(sigma,a), write f(z)=h(z^2), with h entire.
The continuous quotient is

    q_(sigma,a)(x,w)
      =integral_0^1 h'((1-v)*(-w^2)+v*x^2) dv.              (7)

This is the ordinary difference quotient off x^2+w^2=0, equals
h'(x^2) at either w=+/-i*x, and equals h'(0)=f''(0)/2 at
x=w=0. It is entire in w. On any fixed w disk, split the x integral
at 2*radius+1. Cauchy's bound for h' bounds (7) on the compact
portion, and the Gaussian real-axis bound and x^(-2) denominator
bound dominate the remaining portion. This is C032m's proof applied
to a single pair (no counting input is needed for that finite case).
It verifies Haslinger2.39's measurable sections, holomorphy and
integrable compact dominator, so the integral of q is entire.

Since D_F is odd, B_(sigma,a) is odd in w and B_(sigma,a)(0)=0.
Consequently B_(sigma,a)(w)/w is entire and even, and its value at
zero is (2*i/k_sigma)*D_F'(a/k_sigma). This proves the stated
origin value in (2). The entire integral of (7) and the entire
right side of (2) agree on Re(w)>1/2, hence everywhere by the
identity theorem. This includes both imaginary-axis removable
locations in the spatial integrand and their coincident origin.
The result is equality with the original combined integral, not
an uncorrected lower-half-plane Cauchy integral or a principal value.

Multiplying (2) by4w removes its apparent division. The entire
primitive normalized to zero at w=0 is (3), and it is even because
B_(sigma,a) is odd. One convenient equivalent expression, involving
only a compact integration interval, is

    e_(sigma,a)(w)=sqrt(pi)*w/(2*sqrt(sigma))
                         *integral_0^1 B_(sigma,a)(v*w) dv. (8)

### 4. A common summable spatial dominator for all exchanges

We now give the effective bounds on the closed disk |w|<=2.
For |z|<=Y, C032m's Gaussian modulus estimate, applied to one pair,
gives

    |f_(sigma,a)(z)|<=c_Y*exp(-(gamma-Y)_+^2/8).

For h as in (7), |h(u)| is bounded by the preceding expression
with Y=sqrt(U) on |u|<=U: choose any square root pointwise just
for the bound. Cauchy's radius-one derivative estimate gives

    |h'(u)|<=c_sqrt(U+1)*exp(-(gamma-sqrt(U+1))_+^2/8)
                                             for |u|<=U.

For 0<=x<=5 and |w|<=2, the segment in (7) lies in |u|<=25.
Thus its absolute value is at most
c_d*exp(-(gamma-d)^2/8), d=sqrt(26). For x>=5,
|x^2+w^2|>=3*x^2/4. A common nonnegative dominator for q is

    d_(gamma)(x)=c_d*exp(-(gamma-d)^2/8),             0<=x<5,
    d_(gamma)(x)=4/(3*x^2) *
      { (c_0/2)*[exp(-(x-gamma)^2/8)+exp(-(x+gamma)^2/8)]
                    +c_2*exp(-(gamma-2)^2/8) },          x>=5. (9)

These bounds are uniform in both sigma and |delta|<1/2. Since
gamma>14>2*d, all displayed exponent differences are positive.
Splitting the first spatial Gaussian at x=gamma/2 gives

    integral_5^infinity exp(-(x-gamma)^2/8)/x^2 dx
      <=exp(-gamma^2/32)/5+4*sqrt(8*pi)/gamma^2.

On the portion below gamma/2 use exp(-(x-gamma)^2/8)<=
exp(-gamma^2/32) and integrate x^(-2); on the remaining portion
use x^(-2)<=4/gamma^2 and the whole-line Gaussian integral.
The second spatial Gaussian contributes at most exp(-gamma^2/8)/5,
which is no greater than exp(-gamma^2/32)/5. Also

    exp(-(gamma-d)^2/8), exp(-(gamma-2)^2/8)
      <=exp(-gamma^2/32),

because gamma>=2*d and gamma>=4, respectively. Integrating (9)
therefore yields the explicit per-pair estimate

    integral_0^infinity d_(gamma)(x) dx
      <= A*exp(-gamma^2/32)+B/gamma^2.                    (10)

The constants A,B are exactly those in the conclusion. The two
translated Gaussians with their factor1/2 contribute
(4/3)*c_0*[exp(-gamma^2/32)/5+2*sqrt(8*pi)/gamma^2];
the constant subtraction contributes (4/15)*c_2*exp(-gamma^2/32).
The compact portion contributes5*c_d*exp(-gamma^2/32).
This verifies every coefficient in (10).

Both series in the right side of (10) are summable by the counting
input (or by the quantitative estimates in section5). Tonelli on
the nonnegative d_(gamma) therefore gives a single integrable
spatial dominator sum_rho d_(gamma_rho) for the sum of absolute
pair quotients, independent of sigma and w in the disk. For each
fixed x the sum of the quotients equals the full p quotient: off
the removable locus this follows from the locally uniformly
convergent profile series; on the locus, C032m's normal convergence
and Cauchy derivative bounds give the same assertion for h'.
Dominated integration now proves R_sigma=sum_rho r_(sigma,a_rho),
with uniform absolute convergence. No conditionally convergent
spectral or spatial sum is exchanged.

For the straight primitive path t=v*w, 0<=v<=1, the same bounds
apply, since |t|<=2. Termwise compact integration is justified by
the uniform summable bound; hence E_sigma=sum_rho e_(sigma,a_rho).
For any subset of omitted pairs, an R bound M on the disk gives
an E bound

    4*|w|^2*integral_0^1 v*M dv <=8*M.                    (11)

This controls the complete primitive path including its origin,
not merely the values at its endpoints.

### 5. Explicit spectral summation and cutoff endpoints

For t>=14, (1) implies the convenient coarse bound N(t)<=t*log(t).
Here log(log(t))<=log(t), 2*pi>6 and log(t)>=2 give

    N(t)<= t*log(t)/6 + 2*log(t)+10
         <=(1/6+1/7+5/14)*t*log(t)
          =(2/3)*t*log(t) <=t*log(t).

Only this specialization of the imported count is needed; it is
not claimed to improve that source. For any H>=16, Tonelli applied
to gamma^(-2)=integral_gamma^infinity 2*t^(-3)dt gives exactly

    sum_(gamma_rho>H) gamma_rho^(-2)
      =2*integral_H^infinity [N(t)-N(H)]/t^3 dt
      <=2*(log(H)+1)/H.                                  (12)

The N(H) subtraction includes every zero at the cutoff. Point values
of N at integration endpoints have no effect on the Lebesgue
integral. The finite part, however, must include gamma=H with its
full multiplicity; it cannot silently discard a boundary zero.

For u>=H>=16 the function u^2*exp(-u^2/32) is decreasing, since
its logarithmic derivative is 2/u-u/16<0. Consequently

    sum_(gamma_rho>H) exp(-gamma_rho^2/32)
      <=H^2*exp(-H^2/32)
                         *sum_(gamma_rho>H) gamma_rho^(-2). (13)

Equations (10)-(13) prove (4). The inverse-square part is
proportional to (log(H)+1)/H, whose derivative is -log(H)/H^2.
The Gaussian part is proportional to H*(log(H)+1)*exp(-H^2/32);
its logarithmic derivative is

    1/H+1/[H*(log(H)+1)]-H/16 < 2/H-H/16 <0

for H>=16. Both decrease to zero. Thus the error is explicitly
vanishing, unlike a spatial-tail estimate retaining the full fixed
sum of inverse squares. No sectorial special-function asymptotic,
RH or local zero-density estimate enters this bound.

### 6. What certified finite input and arithmetic would be required

To use (4) numerically one must supply a certified complete multiset
of all positive-ordinate zeros with gamma<=H, including multiplicities,
and certified enclosures of both gamma and delta for every member.
The verification must identify the actual zeros and prove completeness;
a list of numerical approximations or a statement of verification
through100 is not that input. Off-line conjugate members must not be
merged or set to delta=0 without a separate certificate. Choose a
cutoff certified not to split any coordinate enclosure, or explicitly
certify and include the boundary zeros. The retained first-zero
interval and the counting theorem alone do not provide this multiset.

For each finite member use (8), or an equivalent certified evaluation
of its entire primitive, over the required width and w parameter set.
The error allowance must enclose coordinate uncertainty, evaluation
of sqrt(sigma), exp and W_F, the compact v integral, cancellation of
the two terms and all rounding. Uniformity in sigma must be proved
by interval enclosures or explicit derivative bounds over the width
cells; sampling widths is insufficient. If (2) is used at zero,
its removable value or a certified analytic enclosure is necessary.
Formula (8) itself has no division by w. Complex-width differentiation
is not required or asserted.

Concretely, if a distinct certified zero with multiplicity m_j has
an approximation to e_(sigma,a_j) with uniform absolute error
epsilon_j, and summing those approximations adds error epsilon_sum,
then the full E error is at most

    T_E(H)+sum_j m_j*epsilon_j+epsilon_sum.                (14)

Each finite error in (14) must include all the preceding input and
arithmetic obligations; no values for them are supplied here. Further
propagation through exp(-E)*sinh(O), coefficient amplification and
uniform residual validation are additional obligations of the later
dictionary test. An O enclosure is also necessary for that test.
This analytic interface therefore does not claim its feasibility or
restart the stopped calculations1571/1576. C032q and C032w/x are
downstream context and comparisons, not mathematical inputs to (2)-(4).

### Critical audit1581 — 18 November 2026

The paired identities, removable continuation, full-divisor exchanges,
uniform tail (4) and conditional finite-input interface pass this
conceptual audit. No correction of (2)-(14) is required. The audit
reuses assessment1579, source-notes1577 and C032m's audited compact
domination. It does not audit the external counting theorem's database,
the fixed-v1 preprints, or the probability-law conclusions. This is
verification of a local specialization of known tools, not a new
transform theorem or a numerical certificate.

**Normalization and contours.** With k=2*sqrt(sigma), substitution
in T_a contributes 1/(k*sqrt(pi)), not 1/sqrt(pi): the factor k from
dx cancels the factor k in x-z, leaving the Gaussian prefactor.
For Re(w)>1/2>|Im(a)|, the upper pole is above both horizontal
contours and the lower pole below both. The vertical-side estimate
exp(-L^2+Y^2)/(L-|Re(zeta)|), multiplied by a fixed side length,
tends to zero. The real part of a only translates the infinite
horizontal line and causes no endpoint contribution. Thus the shift
is justified for each fixed a,w, without assuming real a.
Reflection u=-v at the lower pole reverses the sign of the Cauchy
denominator and gives -pi*i*W_F(-zeta). Both T_a formulas in section2
therefore have the correct signs.

If I is the full-real-line integral of G_sigma(x-a)/(x^2+w^2),
the corresponding integral of G_sigma(x+a) is also I. The even pair
has full-line integral I and half-line integral I/2. Partial fractions
then give sqrt(pi)/(4*k*w)=sqrt(pi)/(8*sqrt(sigma)*w), as in (6).
The subtraction has coefficient
pi/(2*w)/(4*sqrt(pi*sigma))=sqrt(pi)/(8*sqrt(sigma)*w).
No factor is lost for two distinct positive-ordinate off-line zeros;
the half factor belongs to each reflected pair, not that conjugate
pair in Z+. The elementary constant-kernel integral is used only on
Re(w)>0, where compact subsets stay away from real spatial poles.

**Entire equality, including the origin.** For every finite disk
|w|<=M, use X=2*M+1 in the single-pair version of C032m's argument.
On x<=X the segment in (7) stays in |u|<=X^2 and a Cauchy bound on
|u|<=X^2+1 bounds h'. On x>=X, the numerator is bounded by the
two translated real-axis Gaussians plus the finite disk supremum
of f(i*w); the denominator is at least3*x^2/4. This is an integrable
majorant for each M. The x-sections are measurable and the w-sections
entire by (7), so Haslinger2.39 applies on every compact disk, not
merely the disk of radius2. At w=+/-i*x the value is h'(x^2), and
at x=w=0 it is h'(0)=f''(0)/2. No principal-value prescription enters.

Oddness of D_F makes B odd in w. Its derivative at zero is
(i/k)*(D_F'(-a/k)+D_F'(a/k))=(2*i/k)*D_F'(a/k), since D_F' is even.
Multiplication by sqrt(pi)/(8*sqrt(sigma)) gives precisely the
origin value i*sqrt(pi)*D_F'(a/k)/(8*sigma). Both sides of (2) are
entire and agree on the nonempty open safe domain, so the identity
theorem proves equality on C. The primitive has derivative4*w*r(w)
and value zero at zero. Oddness of B makes that primitive even and
gives (3)/(8) with the stated constants.

**Summable domination.** In (9), the compact segment is in |u|<=25;
the radius-one Cauchy circle requires |z|<=sqrt(26)=d. The Gaussian
bound there is uniform for every width and allowed displacement.
On x>=5 the denominator bound and the two Gaussian terms retain
their factor1/2. Splitting the positive translate at gamma/2 gives
exp(-gamma^2/32)/5+4*sqrt(8*pi)/gamma^2; the negative translate
contributes at most exp(-gamma^2/32)/5. Multiplying their sum by
(4/3)*(c_0/2) gives (4*c_0/15)*exp(-gamma^2/32) and
(8*c_0/3)*sqrt(8*pi)/gamma^2. The subtracted constant contributes
(4*c_2/15)*exp(-gamma^2/32). The compact part contributes
5*c_d*exp(-gamma^2/32), because gamma>14>2*d. These are exactly A
and B in (10). No cancellation is used in the bound.

The count implies summability of both positive sequences in (10).
Tonelli gives an integrable sum of the nonnegative spatial majorants;
the Weierstrass bound gives absolute uniform convergence of the
integrated series on [1,2] times the closed w disk. On the removable
locus, normal convergence of the even profiles on larger disks gives
normal convergence of their h derivatives by Cauchy's formula. Thus
the pointwise summed quotient is the full profile quotient even there.
Dominated integration proves the asserted R equality. For t=v*w,
termwise integration is justified by that same uniform bound, and
4*|w|^2*integral_0^1 v dv=2*|w|^2<=8. The entire path, including
zero and imaginary-axis points, is covered. This proves the E equality
and the factor8 in the error; endpoint values alone would not suffice.

**Count, cutoff and decrease.** For t>=14 the imported error in (1)
is at most2*log(t)+10. The leading term is at most t*log(t)/6.
Since t>=14 and log(t)>=2, the remaining ratios are at most1/7
and5/14, whose sum with1/6 is2/3. The coarse N(t)<=t*log(t) is
therefore valid. In (12), each omitted occurrence contributes
integral_gamma^infinity 2*t^(-3)dt=gamma^(-2). Counting occurrences
with multiplicity gives N(t)-N(H), with all gamma=H retained. Tonelli
and integral_H^infinity log(t)/t^2 dt=(log(H)+1)/H yield (12),
without any continuity assumption on N or a zero-free cutoff.

For gamma>H>=16, monotonicity of u^2*exp(-u^2/32) gives (13).
Combining (10), (12), (13) and the factor8 yields exactly the
factor16 and bracket in (4). Both positive summands decrease: their
derivative signs are -log(H)/H^2 and
1/H+1/[H*(log(H)+1)]-H/16<0, respectively. Their limits are zero;
the positive constant B supplies the stated order log(H)/H.
The same calculation before multiplication by8 proves the R bound.

**Finite-input limit.** Formula (14) is a triangle inequality for
uniform absolute per-member errors with multiplicities, followed by
the analytic omitted-divisor bound. It requires a complete certified
finite multiset; neither the global count nor first-zero/through100
information supplies that multiset. A cutoff intersecting a coordinate
box needs separate resolution. Rounding, uncertain gamma and delta,
special-function cancellation, compact integration and width-cell
coverage must all be included in the finite errors. No such errors
or data are supplied. In particular, decreasing T_E(H) alone cannot
certify any value of E or the dictionary residual. The additional O,
exponential/sinh and coefficient-amplification bounds remain necessary.
Stops1571/1576 remain valid for their respective enclosure schemes.
Full cancellation, positive output, unrestricted variation and the
actual-Xi positivity/unsmoothed-realization gaps are unchanged.

## Mathlib

Full matching coverage is unchecked and unknown. No Mathlib theorem
is used here. Gaussian integration, holomorphic integration, Cauchy
bounds and measure summation have supporting general infrastructure,
but no formalized match for this paired subtraction, Faddeeva
continuation, qualified actual divisor and effective spectral tail
has been checked. The local result specializes the cited known tools;
it is not a claim of a new general transform or a result beyond the
sources checked.
