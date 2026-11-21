# Corollary C034g: joint origin and connector finite-part contours

## Hypotheses

Use C034f's exact functions, divisor, cutoff and qualifications. In
particular, with Gaussian half-variance sigma in [1,2] and uniform
estimates on I=[1/2,3], put

    G_sigma(z)=exp(-z^2/(4*sigma))/sqrt(4*pi*sigma),
    z_rho=gamma_rho-i*delta_rho,
    p(z)=(1/2)*sum_rho[G_sigma(z-z_rho)+G_sigma(z+z_rho)],
    Q_j(z)=4*j*(3*z^2+j)/(z^2*(z^2+j)^2), j=1,2,
    a=13, h=3/4.

The actual positive-ordinate divisor is nonempty, includes every
multiplicity and conjugate, has gamma_rho>14, |delta_rho|<1/2 and
N(T)=O(T log(T+2)). Retain the excluded ordinate zero, verified zeros
through100, retained real zero in (14,15), reciprocal-square tail,
heat positivity/separate fixed-j errors, both fixed-v1 qualifications,
zero drift/killing and C033w's probability interpretation through
C034b. Source-wide and finite-zero validity remain unverified here.
Only the explicit divisor assumptions, C032n's Gaussian estimates,
C034d's rational/transfer formulas and C034f's exact definitions enter
this representation. No RH, profile positivity or global Sobolev
membership is assumed. Primes below are spatial derivatives.

Keep the original ordinary quantities, without redefining them:

    alpha_j=int_0^a (p-p(0))*Q_j-p(0)*int_a^infinity Q_j,
    beta_j=int_0^a (p''-p''(0))*Q_j-p''(0)*int_a^infinity Q_j
                                  -p'(a)*Q_j(a)+p(a)*Q_j'(a).

For BOTH translates nu=(rho,epsilon), epsilon=+1,-1, define

    c_nu=epsilon*gamma_rho, b_nu=-epsilon*delta_rho,
    g_nu(z)=G_sigma(z-c_nu-i*b_nu),
    P_nu[F]=int_(a to a+i*b_nu) g_nu(z)*F(z) dz,
    N_nu[F]=int_(-a to -a+i*b_nu) g_nu(z)*F(z) dz,
    V[F]=(1/2)*sum_nu P_nu[F].

Every vertical segment is oriented as indicated, including negative
b_nu; for b_nu=0 it is zero. This V is precisely C034f's V.

## Conclusion

For s=+1,-1, let Gamma_nu^s be the three-segment path

    -a+i*b_nu -> -a+i*s*h -> a+i*s*h -> a+i*b_nu,
    I_nu^s[F]=int_(Gamma_nu^s) g_nu(z)*F(z) dz.

Put A_j=alpha_j+V[Q_j], B_j=beta_j+V[Q_j'']. For F=Q_j or Q_j'',
let J[F] denote A_j or B_j, respectively. Then

    r_nu[Q_j]=4*g_nu'(0),
    r_nu[Q_j'']=4*g_nu'''(0),                         (61)
    J[F]=(1/4)*sum_nu (I_nu^s[F]+s*i*pi*r_nu[F])
         =(1/4)*sum_nu I_nu^s[F]
         =(1/8)*sum_nu (I_nu^+[F]+I_nu^-[F]).        (62)

All contour integrals, residue series and displayed series converge
absolutely, uniformly on I, with one width-independent summable
divisor majorant specified below. No individual residue is assumed
zero. Cancellation in the second equality uses each original member's
two translates; every multiplicity remains. Both endpoint connectors
are incorporated into Gamma, including b_nu=0 and either displacement
sign. The values J[F] are real and continuous in sigma.

The finite normalizations matching the ordinary definitions are
explicit. Define the rational primitive

    L_j(z)=-4*j/(z*(z^2+j)), L_j'=Q_j,
    M_j(a)=a^2*Q_j'(a)-2*a*Q_j(a)+2*L_j(a),
    E_j(a)=p'(a)*Q_j(a)-p(a)*Q_j'(a),
    V_0(x)=p(x)-p(0)-p''(0)*x^2/2.

Using the symmetric finite-part prescription at the INTERIOR point0,

    alpha_j=(1/2)*FP int_-a^a p Q_j
            =int_0^a (p-p(0))*Q_j+p(0)*L_j(a),       (63)
    beta_j=(1/2)*FP int_-a^a p Q_j''
           =int_0^a V_0*Q_j''+p(0)*Q_j'(a)
                                      +(p''(0)/2)*M_j(a)
           =(1/2)*FP int_-a^a p'' Q_j-E_j(a).        (64)

Thus the normalization constants and the original finite derivative
trace are accounted for; they were not set to zero by convention.
This is a qualified representation from attempt1859, passing
conceptual audit1861 below. It does not bound C034f's Omega or the
full curvature C at C034c(20)'s S4^3/5 threshold. Final-prefix signs,
conditioning, entries/m, exact weights, TV<=2, full observations,
signed height/cancellation and actual-Xi realization remain unresolved.
There is no complete RH candidate and no originality claim.

## Proof

### Imported theorem and the scope of this specialization

Reuse the pre-invocation SPECIALIZE assessment1858 and its inspected
source record `drafts/literature/2026-11-20-laplace-combined-correction-source-notes-1858.md`.
Import Eric A. Galapon, *The Cauchy Principal Value and the Hadamard
Finite Part Integral as Values of Absolutely Convergent Integrals*,
[arXiv:1512.01323v3](https://arxiv.org/pdf/1512.01323v3), Section2,
Definition1/Lemma1, (7)-(10), pp3-4; Proposition2, (18)-(22), p6;
Theorem1, p7, with boundary formulas (25)-(28), pp7-8.
For an analytic numerator on a neighborhood of a finite interval
with an interior pole of order n+1, n>=1, the specified symmetric
Hadamard finite part equals the upper bypass integral plus i*pi
times its residue, or the lower bypass integral minus that term.
The paths must be in the stated pole-avoiding homotopy classes.
The source's counterterms, not a principal value for a higher pole,
are used below. No endpoint version of its theorem is assumed.

For finite contour homotopy use Friedrich Haslinger, *Complex
Analysis*, Section2.2, Theorem2.5/Corollary2.6, pp45-48,
[primary notes](https://www.mat.univie.ac.at/~has/scriptneu.pdf).
For absolute series/integrals and limits use John K. Hunter,
*Measure Theory*, Section5.6, Theorem5.18/Example5.19,
[p61](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch5.pdf),
and Section4.5, Theorem4.24 plus Section4.6's complex extension,
[pp49-50](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf).
Their inspected coverage in source-notes1854 is reused. The general
theorems are imported; the new work is matching these particular
ordinary subtractions and endpoint connectors, and supplying uniform
divisor bounds. No scalar special-function evaluation is needed.

### Exact finite-part prescription and ordinary normalization

C034d(31)/(34) give the rational kernels. At zero they have expansions

    Q_j(z)=4/z^2+4/j+O(z^2),
    Q_j'(z)=-8/z^3+O(z),
    Q_j''(z)=24/z^4+O(1),
    L_j(z)=-4/z+4*z/j+O(z^3).                         (65)

For any analytic g, Galapon's symmetric prescription specializes to

    FP int_-a^a g Q_j
      =lim_(epsilon->0+) [int_([-a,-epsilon] U [epsilon,a]) g Q_j
                                                     -8*g(0)/epsilon],
    FP int_-a^a g Q_j''
      =lim_(epsilon->0+) [int_([-a,-epsilon] U [epsilon,a]) g Q_j''
                    -16*g(0)/epsilon^3-24*g''(0)/epsilon]. (66)

For the first application the analytic numerator is z^2*g(z)*Q_j(z)
and n=1. For the second it is z^4*g(z)*Q_j''(z) and n=3. Their
Taylor coefficients and (65) give exactly (66): odd singular powers
cancel only in the symmetric truncated integral; the coefficient of
z^-1 is retained as a residue in the contour theorem. In particular
those residues are exactly (61), for every j. All finite parts here
are at an interior point of [-a,a]. Half-interval notation below means
one HALF of (66) for an even integrand, not a new endpoint theorem.

Since L_j'=Q_j and L_j(infinity)=0,

    int_a^infinity Q_j=-L_j(a),
    (1/2)*FP int_-a^a Q_j=L_j(a).                    (67)

The second equality follows by integrating on [epsilon,a], subtracting
4/epsilon and using L_j(epsilon)=-4/epsilon+O(epsilon).
The even function p-p(0)=O(x^2) gives an ordinary convergent
integral against Q_j. Splitting off p(0) in (66) and using (67)
proves (63), exactly matching the original negative tail constant.

For the fourth-order kernel, integration of Q_j'' gives

    (1/2)*FP int_-a^a Q_j''=Q_j'(a),
    (1/2)*FP int_-a^a x^2*Q_j''(x) dx=M_j(a).         (68)

Indeed Q_j'(epsilon)=-8/epsilon^3+O(epsilon). A primitive of
x^2 Q_j'' is x^2 Q_j'-2x Q_j+2L_j, whose expansion at epsilon
is -24/epsilon+O(epsilon). These are respectively the half-interval
counterterms 8/epsilon^3 and 24/epsilon in (66), with no unrecorded
finite lower constant. Since p is even, V_0=O(x^4) and V_0 Q_j''
is ordinarily integrable. Splitting p into V_0+p(0)+p''(0)x^2/2
now gives the middle expression of (64), including both finite
normalization constants. This retains C034d's quadratic subtraction.

To match the ORIGINAL beta rather than define a replacement, integrate
by parts twice on [epsilon,a]:

    int_epsilon^a p'' Q_j=E_j(a)-E_j(epsilon)
                                      +int_epsilon^a p Q_j'',
    E_j(epsilon)=8*p(0)/epsilon^3+8*p''(0)/epsilon
                                                    +O(epsilon). (69)

The expansion follows from p=p(0)+p''(0)x^2/2+O(x^4) and (65).
The half finite-part subtraction on the left is 4*p''(0)/epsilon;
that on the last integral is 8*p(0)/epsilon^3+12*p''(0)/epsilon.
Consequently every divergent term in (69) cancels with these precise
coefficients and leaves

    (1/2)*FP int_-a^a p'' Q_j
            =E_j(a)+(1/2)*FP int_-a^a p Q_j''.

Applying (63)'s normalization argument to the even function p''
identifies its left side with
int_0^a(p''-p''(0))Q_j-p''(0)int_a^infinity Q_j.
Subtract E_j(a). This proves (64) with both signs of the original
trace -p'(a)Q_j(a)+p(a)Q_j'(a). No boundary term was discarded.

The rational algebra, all principal Laurent coefficients, both residue
orders, the symmetric counterterms and the p(0)/p''(0) trace coefficients
are reproduced with exact Fraction arithmetic by
`python3 scripts/smoothed-law/laplace_joint_contour_check_1859.py`.
All52 checks pass; the full certificate is
`scripts/smoothed-law/laplace_joint_contour_check_1859.json`.
Its complete `/checks` value was inspected with the shared JSON
inspector. These are algebra checks only, not verification of the
analytic contour theorem, divisor limits or a quantitative sign.

### Finite contours, residues, and both endpoint connectors

Begin with a finite divisor sum, keeping both translates of every
member. On the convex rectangle |Re z|<14, |Im z|<7/8, the two
analytic numerators used in (66) are holomorphic. The other rational
poles +/-i*sqrt(j) are outside this rectangle. The only pole of
g_nu F inside is zero. Let C^s be the path

    -a -> -a+i*s*h -> a+i*s*h -> a.

It is in the upper (s=+) or lower (s=-) bypass class within this
rectangle minus0, without extra winding. For example its horizontal
side can be continuously lowered to a small upper semicircle and
the two real segments without meeting another pole. Galapon therefore
gives, for each individual translate,

    FP int_-a^a g_nu F=int_(C^s) g_nu F+s*i*pi*r_nu[F]. (70)

The sign agrees with the clockwise upper semicircle from -epsilon
to epsilon, whose residue contribution is -i*pi*r_nu. The theorem
accounts for the higher-pole divergent terms through (66); they
cannot be discarded as if only a simple pole were present.

Concatenation and cancellation of oriented vertical segments give

    I_nu^s[F]=-N_nu[F]+int_(C^s)g_nu F+P_nu[F].       (71)

This is valid for b_nu of either sign, including zero, since all
vertical paths lie at Re z=+/-a, away from every pole. In explicit
real parameters, with t(u)=b_nu+(s*h-b_nu)*u and
q(u)=s*h+(b_nu-s*h)*u, the three terms in I are

    i*(s*h-b_nu)*int_0^1 g_nu(-a+i*t(u))*F(-a+i*t(u)) du,
    int_-a^a g_nu(x+i*s*h)*F(x+i*s*h) dx,
    i*(b_nu-s*h)*int_0^1 g_nu(a+i*q(u))*F(a+i*q(u)) du. (72)

Thus neither cutoff endpoint is implicit in a dropped side.

Let nu*=(rho,-epsilon), so c_nu*=-c_nu, b_nu*=-b_nu and
g_nu*(-z)=g_nu(z). Both F are even. Substitution z=-w, including
its minus sign, gives

    N_nu[F]=-P_nu*[F],
    r_nu*[F]=-r_nu[F].                               (73)

The second identity follows either from odd derivatives at0 in (61)
or by transforming the Laurent expansion. No conjugate-only pairing
or removal of multiplicity is involved.

For the finite sum, (63)-(64) and p=(1/2)sum_nu g_nu give

    alpha_j or beta_j=(1/4)*sum_nu FP int_-a^a g_nu F.

Add V[F]=(1/2)sum_nu P_nu[F], apply (70), and use
sum_nu(P_nu-N_nu)=2*sum_nu P_nu from (73). Equation (71)
then gives the first equality of (62), including its factor1/4.
The residue sum is zero by (73), proving the second equality.
Averaging the independently justified upper and lower formulas gives
the factor1/8 in the third equality. Residues were displayed before
being paired. The step never separately integrates an origin-subtracted
single translate on [0,a].

### A common absolute divisor majorant and the infinite limit

Set

    w_rho=exp(-(gamma_rho-a)^2/24),
    E={x+i*s*h: -a<=x<=a, s=+1,-1}
                     U {+/-a+i*y: -h<=y<=h}.

By C032n(8), for k=0,1,2,3,4 there are constants C_k independent
of sigma in I, rho, epsilon and b_nu such that

    sup_(|Re z|<=a, |Im z|<=h)|g_nu^(k)(z)|<=C_k*w_rho. (74)

Indeed the imaginary part of z-c_nu-i*b_nu has modulus <=5/4;
its real part has modulus >=gamma_rho-a. Use C032n(8) with Y=5/4.
The zero count makes W=sum_rho w_rho finite: beyond gamma>2a,
w_rho<=exp(-gamma^2/96), which is summable by that count, and
only finitely many smaller ordinates occur. This is a width-independent
summable function of the original divisor, not memberwise convergence.

For each of the four F, the explicit rational denominators do not
vanish on compact E. Thus M_F=sup_E |F| is finite, independent of
sigma and all divisor members. Every Gamma has length at most
2a+4h=29, and lies in E. Equations (61), (72), (74) give

    int_(Gamma_nu^s) |g_nu F| |dz|<=29*M_F*C_0*w_rho,
    |r_nu[F]|<=4*C_k*w_rho, k=1 for Q_j, k=3 for Q_j'',
    |P_nu[F]|+|N_nu[F]|<=M_F*C_0*w_rho.              (75)

Taking the maximum of these finitely many constants supplies one
majorant for both j, both s, all four kernels, their residues and
all connectors, uniform on I. Counting the two translates only
multiplies its finite sum by2. All integrands are continuous in the
path parameters and sigma. Counting measure and the finite real
parameter intervals are sigma-finite, so the cited complex Fubini
and dominated-convergence theorems apply with (75). No far endpoint
is sent to infinity in this new contour construction; C034f's tail
identities and their proved uniform far-side bounds are reused.

It remains to identify the limit with the original ordinary alpha
and beta, not merely a new contour sum. At the origin keep the even
member t_rho=(g_(rho,+)+g_(rho,-))/2. Equation (74) implies

    |t_rho(x)-t_rho(0)|<=C_2*w_rho*x^2/2,
    |t_rho''(x)-t_rho''(0)|<=C_4*w_rho*x^2/2,
    |t_rho(x)-t_rho(0)-t_rho''(0)*x^2/2|
                                      <=C_4*w_rho*x^4/24, (76)

for 0<=x<=a. Since x^2 Q_j and x^4 Q_j'' are bounded there,
(76) is an integrable, summable majorant for each ordinary subtracted
integral in (63)-(64). Origin values and derivatives at a have (74),
and the tail constants int_a^infinity Q_j are fixed finite numbers
by (67). Therefore the finite-divisor alpha and beta converge to
exactly their original definitions, uniformly on I. This also verifies
all finite normalization and trace series absolutely. It avoids any
unjustified exchange of divergent individual origin integrals.

Take finite divisor truncations gamma<=R retaining translates and
conjugates, then R->infinity. Bounds (74)-(76) justify every limit
in (62)-(73) and the residue cancellation. Continuity in sigma and
uniformity at both widths1 and2 follow from the same majorants.
The inherited conjugation involution sends b to -b with c fixed,
and conjugates g_nu. It sends Gamma_nu^+ to Gamma_bar(nu)^-.
Consequently the averaged expression in (62) is real, consistent
with the original real alpha, beta and V. It imposes no sign.

### Scope of the result

This completes the approved linear representation test. It combines
each origin correction with its connector before estimation and
retains all normalization/residue/endpoint terms. The bounds (75)
prove convergence only: their constants are not small relative to
S4^3/5, and the Gaussian weights on these common-height paths have
complex phases. No nonnegative-weight or negative-kernel argument
has been applied to this correction. The existing negative retained
core in C034f remains available, but estimating its joint contribution
with (62) is a separate, uncovered target. No independent product
estimate, scalar-evaluation project or closure claim is made here.

### Conceptual audit1861 — 20 November 2026

The four linear identities (61)-(76) pass under assessment1859's
unchanged SPECIALIZE scope, separately approved1860. This verdict
validates the existing specialization; it imports no quantitative sign
and makes no originality claim. Reuse the inspected Galapon, Haslinger
and Hunter statements cited above and source-notes1858/1854. Their
hypotheses are checked here, without reproving the general theorems.

**Ordinary quantities and finite normalization.** Directly expand the
rational Q_j at zero. Its only negative Laurent term is 4/z^2;
differentiating twice gives 24/z^4 with no z^-2 term. Thus g Q_j has
residue 4g'(0), and g Q_j'' has residue 4g'''(0). For the latter,
the even singular terms are 24g(0)/x^4 and 12g''(0)/x^2.
Integrating symmetrically outside (-epsilon,epsilon) gives precisely
16g(0)/epsilon^3+24g''(0)/epsilon. The odd x^-3 and x^-1 terms
cancel on these symmetric truncated intervals; this does not remove
their role in the bypass formula. For Q_j the counterterm is
8g(0)/epsilon. These are Galapon's n=3 and n=1 prescriptions for
the analytic numerators z^4 g Q_j'' and z^2 g Q_j, respectively.

L_j'=Q_j and L_j(infinity)=0 give the actual tail constant -L_j(a).
Since L_j(epsilon)=-4/epsilon+O(epsilon), the half finite part of
Q_j is L_j(a), with no finite lower constant. Similarly, the lower
expansions of the primitives Q_j' and x^2 Q_j'-2x Q_j+2L_j are
-8/epsilon^3+O(epsilon) and -24/epsilon+O(epsilon). The half finite
parts of Q_j'' and x^2 Q_j'' are therefore Q_j'(a) and M_j(a).
Consequently the two even Taylor
coefficients of p give exactly the constants p(0)Q_j'(a) and
p''(0)M_j(a)/2 in (64); they are not optional normalizations.

For an independent check against the original beta, write
p(x)=p0+p2*x^2/2+O(x^4). Direct multiplication gives

    p'(epsilon)Q_j(epsilon)-p(epsilon)Q_j'(epsilon)
        =8*p0/epsilon^3+8*p2/epsilon+O(epsilon).

Twice integrating by parts on [epsilon,a] therefore yields

    int_epsilon^a p'' Q_j-4*p2/epsilon
      =E_j(a)+[int_epsilon^a p Q_j''
                     -8*p0/epsilon^3-12*p2/epsilon]+O(epsilon).

Both limits exist by even Taylor subtraction. Subtracting E_j(a)
recovers precisely C034f's beta, including -p'(a)Q_j(a)+p(a)Q_j'(a)
and the tail constant -p2*int_a^infinity Q_j. The alpha comparison
uses p-p0=O(x^2) and the same L_j(a) normalization. Thus (63)-(64)
reach the ordinary definitions, rather than redefining them by a
contour integral. Only half of a symmetric interior finite part is
used; no endpoint-pole theorem is invoked.

**Bypass class, residues, connectors and factors.** The convex open
rectangle |Re z|<14, |Im z|<7/8 contains [-13,13] and both paths
C^s. The analytic numerators have no singularity there. All other
rational poles, at +/-i*sqrt(j), lie outside it. The upper path has
the upper bypass homotopy class without extra winding; the lower
path has the lower class. The clockwise upper small semicircle has
residue contribution -i*pi*r. Hence FP=int(C^+)+i*pi*r, whereas
FP=int(C^-)-i*pi*r. This checks (70)'s sign against the actual path,
not a displaced-pole boundary-value convention.

For either sign of b, decompose the left side of Gamma as the path
from -a+ib to -a followed by the left side of C^s. Decompose the
right side as the right side of C^s followed by a to a+ib. This is
the exact oriented identity I^s=-N+int(C^s)+P, also when b=0.
The parameterizations (72) have the corresponding factors i(sh-b)
and i(b-sh); no absolute value may replace either factor.

Under z=-w, the path -a to -a+ib becomes a to a-ib, with dz=-dw.
Evenness of F and g_nu(-w)=g_nu*(w) then give N_nu=-P_nu*.
Odd derivatives at zero change sign, so r_nu*=-r_nu. Pairing here
is each original divisor member's two translates, independently of
conjugation or whether b vanishes. For a finite divisor truncation,

    (1/4)*sum_nu(I_nu^s+s*i*pi*r_nu)
      =(1/4)*sum_nu FP int_-a^a g_nu F
                         +(1/4)*sum_nu(P_nu-N_nu)
      =(alpha_j or beta_j)+(1/2)*sum_nu P_nu.

The factor1/4 is the half symmetric integral times the factor1/2
in p. The last sum is exactly V[F] in C034f. The residue sum then
vanishes, and averaging the two resulting equalities gives factor1/8.
Every multiplicity survives. A single translate generally has nonzero
residue, even if b=0; its omission before pairing would be invalid.

**Uniform full-divisor limit.** For every point of the complete
rectangle |Re z|<=a, |Im z|<=h, both signs of c obey

    |Re(z-c-ib)|>=gamma-a, |Im(z-c-ib)|<=h+1/2=5/4.

C032n(8), whose derivative-polynomial proof was checked, applies
for k=0,...,4 on the closed interval I=[1/2,3]. It gives (74)
with w_rho=exp(-(gamma-a)^2/24) and constants independent of
the member, translate and width. For gamma>2a,
w_rho<=exp(-gamma^2/96). Grouping ordinates in [n,n+1) bounds
their contribution by O((n+1)log(n+3))*exp(-n^2/96); this series
converges. Finitely many smaller ordinates cause no difficulty.
Thus sum w_rho is finite with the actual multiplicities.

Every horizontal segment stays a distance at least h from zero;
every vertical segment has real part +/-13. The compact set E
contains no pole of any of the four F, so a common finite maximum
of their moduli exists. The exact path length is 2a+2|sh-b|<28.5,
which is below the stated29. The total lengths of P and N are
2|b|<1, with both zero at b=0. These facts prove all of (75),
including its constants and both displacement signs. Taking a finite
maximum supplies a single constant times w_rho for every side,
residue and kernel. This is a summable majorant, not a small bound.

At the real origin the even t_rho has t_rho'(0)=t_rho'''(0)=0.
Taylor's integral remainders, with (74) on [0,a], give exactly the
three estimates (76). The functions x^2 Q_j and x^4 Q_j'' extend
continuously to zero and are bounded on [0,a]. Their products with
the remainders are therefore dominated by a fixed integrable function
times w_rho. The cutoff traces and origin constants have the same
summable bounds. This proves uniform convergence of the original
ordinary alpha and beta, including their quadratic normalization.
For a single g_nu in a symmetric finite part, its even part
(g_nu(x)+g_nu(-x))/2 satisfies the same Taylor estimates. Its odd
part integrates to zero on every symmetric truncated interval.
Thus the regularized finite-part series itself is absolutely summable;
no separate divergent half-interval integral is interchanged with a sum.

Take gamma<=R with both translates and all conjugates before R tends
to infinity. Counting measure on this countable divisor and Lebesgue
measure on each parameter interval are sigma-finite; the integrands
are measurable and continuous in width. The preceding absolute
majorants verify Hunter's hypotheses and bound every omitted tail
uniformly by a constant times sum_(gamma>R) w_rho. Therefore all
linear contour sums, finite normalizations and residue cancellations
pass to the limit uniformly on I. No new infinite path or far-side
limit is introduced. Finally conjugation fixes c, negates b and
interchanges the upper/lower paths; the averaged formula is real
and continuous, including sigma=1,2. Reality supplies no sign.

The exact algebra script1859 was inspected and replayed: all52
required checks passed with no failures. The complete `/checks`
value in `scripts/smoothed-law/laplace_joint_contour_check_1859.json`
was read using `python3 ../scripts/loop/inspect_json.py
scripts/smoothed-law/laplace_joint_contour_check_1859.json --pointer
/checks --full`. This evidence checks rational primitives, residues,
counterterms and traces; the analytic audit above is separate.
No formula or direct mathematical dependency needed correction.

The verdict remains conditional on the explicit divisor and inherited
source qualifications. It does not validate those external inputs,
global Sobolev membership or full Mathlib matching. In particular it
neither bounds Omega nor proves C034c(20), final-prefix nonvanishing,
conditioning, observation matching, signed-height cancellation or
actual-Xi realization. Stops1839/1843/1847 remain intact.

## Mathlib

Full matching coverage is unchecked and unknown. No Mathlib theorem
is used or claimed absent. General contour integration, Taylor
estimates and dominated-convergence support are distinct from a
matching theorem for (61)-(76), with its prescribed finite parts,
ordinary normalizations, member-dependent endpoints and full divisor
limits. Conceptual audit1861 validates the qualified representation;
the inherited source qualifications remain unverified here. No formal
verification is claimed.
