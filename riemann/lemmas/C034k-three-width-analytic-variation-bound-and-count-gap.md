# Corollary C034k: audited three-width analytic variation cap

## Hypotheses

Retain all hypotheses of C034j, C034b/audit1841, C034i/audit1870 and
C033w, with exactly C033m's compact excision. In particular Z+ is the
full labeled positive-ordinate zero multiset, including conjugates and
every multiplicity; z_rho=gamma_rho-i*delta_rho, gamma_rho>14,
|delta_rho|<1/2, and N(T)=O(T log(T+2)). There is no ordinate-zero
member. Displacements vanish through ordinate100; a real member r in
(14,15) is retained; sum_(gamma>100) gamma^-2<1 is qualified input.
Heat positivity, the separate fixed-j=0,1 heat-error inputs, both
fixed-v1 preprint qualifications, zero drift and killing, and Gaussian
half-variance are unchanged. Source-wide and finite-zero validity are
not independently verified here. No numerical count through100 is
assumed in the main bound below.

For sigma in [1,2], use the exact normalized primitives b_sigma of
C034b/j and probability transforms

    k_j(sigma)=exp(-b_sigma(sqrt(j))), j=1,2,
    d_j(sigma)=partial_sigma b_sigma(sqrt(j)),
    S=S_4=sum_rho gamma_rho^-4, S_8=sum_rho gamma_rho^-8,
    A=50*S*S_8+S^3/5, alpha=1/(5*10^12).

The real C^2 width regularity holds on (1/2,3); only [1,2] is used
for signs and estimates. The exact residual transform is

    m(j)=k_j(1)*exp(P_j),
    P_j=int_1^(3/2) (1-exp(-j*t))*ell_1(t) dt,
    ell_1(t)=sqrt(pi)*t^(-3/2)*p_(a(t))(0),
    a(t)=1+1/(4*t) in [7/6,5/4].

These are C033m(1),(3), not a modified residual or Levy restriction.
The ell_1 is nonnegative by the qualified law input; spatial profiles
are not assumed nonnegative. Let a=(a_0,a_1,a_2) be C034j's unique
real solution M^T a=(1,m(1),m(2))^T at widths (1,3/2,2).

## Conclusion

Without evaluating any scalar transform or zero ordinate, one has

    S*j/2 < d_j(sigma) < 20*j*S,                         (1)
    0 <= P_j < alpha*S, j=1,2.                          (2)

Normalize the two nonconstant columns of M by k_1(1),k_2(1), and
call the resulting matrix M_0. Then

    det M_0 < 0,
    |det M_0| > exp(-100*S)*A/512000,                    (3)
    |det M|=k_1(1)*k_2(1)*|det M_0|.

The exact weights obey the unconditional, qualified bound

    sum_i |a_i|
      < 1 + 92160000*alpha*S*exp((100+alpha)*S)
                                      /(50*S_8+S^2/5).  (4)

In particular the additional numerical condition S<=1/100 implies

    sum_i |a_i| < 1+1458/3125 < 3/2 < 2.                (5)

Audit1879 below verifies (1)-(5),(11) and specializes the imported
Hasanalizade–Shen–Wong count theorem to give, with the inclusive endpoint
and all positive-ordinate multiplicities,

    N(100)<283519/3000<100,
    S<64901/24010000<1/100,
    sum_i |a_i|<4583/3125=1.46656<3/2<2.

Thus the exact three-atom measure belongs to C033w's A_2 and
d_{ {1,2} }=0 under all the retained qualifications. No full-interval
match follows. The count input missing in attempt1876 is now paid;
its original stopping record is preserved below and in ATTEMPTS.

This is an audited local quantitative specialization of classical
interpolation tools and a cited counting theorem, not a claim of
originality or an RH candidate. Full observations, signed height,
cancellation, source-wide validity and actual-Xi realization remain open.

## Proof

### Source scope and the quantitative task

Use the pre-invocation SPECIALIZE assessment1875 and its inspected
source-notes1875, reusing1797/1838/1745. Import Carl de Boor,
*Divided Differences*, Surveys in Approximation Theory1 (2005),46-69,
author PDF dated21 December2004, printed pp60-61, Proposition43 and
complete Rolle/interlacing proof, Corollary(44), and determinant
formula(45), [primary PDF](https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf).
For a real C^2 function on an interval containing three distinct ordered
nodes, its second divided difference is f''(xi)/2 at an intermediate
point. Its evaluation determinant with columns (1,x,f) is the node
Vandermonde product times that divided difference. The change of
coordinate below verifies why these polynomial-column statements apply.
Also import the standard real inverse function theorem and Cramer's
rule. None of these general theorems is reproved. The family-specific
upper derivative, residual, spacing and cofactor estimates are the
unpaid application work addressed here. C034j's qualitative ECT
application and the stopped scalar evaluator1798 are not repeated.

### A complete-member upper bound for the width derivative

C034b(6) and its absolute-summation proof give, for s=1,2,

    d_s=int_0^infinity (p_sigma(x)-p_sigma(0))*Q_s(x) dx,
    Q_s(x)=4*s*(3*x^2+s)/(x^2*(x^2+s)^2),
    h_rho(x)=Re([G_sigma(x-z_rho)+G_sigma(x+z_rho)]/2),
    G_sigma(v)=exp(-v^2/(4*sigma))/sqrt(4*pi*sigma).

The origin subtraction must be retained. First sharpen the elementary
weighted Gaussian estimate, for gamma>14, x>=1 and sigma in [1,2], to

    x^-4*exp(-(x-gamma)^2/(8*sigma)) < 2*gamma^-4.       (6)

It suffices to use denominator16 in the exponential. Write
F(x)=4*log(gamma/x)-(gamma-x)^2/16. For x>=gamma, F<=0.
For 3gamma/4<=x<=gamma, put y=gamma-x. Integration of 1/(1-u)
on [0,y/gamma] gives log(gamma/x)<=4y/(3gamma), whence

    F <= 16*y/(3*gamma)-y^2/16
       <=1024/(9*gamma^2)<2/3.

On [gamma/2,3gamma/4], F'=[x*(gamma-x)-32]/(8*x)>0,
because x*(gamma-x)>=3gamma^2/16>32. Its maximum is therefore
already bounded at 3gamma/4. On [1,gamma/2], this derivative can
change sign only from negative to positive, so the maximum occurs
at an endpoint. At gamma/2,

    F=4*log2-gamma^2/64<3-196/64<0.

At1, F decreases as gamma>=14 increases, since
4/gamma-(gamma-1)/8<0, and

    F(1)<4*log14-169/16<11-169/16=7/16<2/3.

Here log2<3/4 follows from the first four terms of exp(3/4), and
log14<11/4 from the first six terms of exp(11/4). Finally log2>2/3:
integrating 1/t >= 4/3-4*t/9 on [1,2] gives 2/3, strictly since
the difference is (2*t-3)^2/(9*t) and is not identically zero.
Thus F<log2, proving (6). The bound with x+gamma in place of
x-gamma follows from (x+gamma)^2>=(x-gamma)^2.

For each member, |G_sigma(u+i*delta)| is at most
(16/15)*exp(-u^2/(4*sigma))/sqrt(4*pi*sigma), since
delta^2/(4*sigma)<1/16 and exp(1/16)<=16/15. Apply (6) to
half this Gaussian exponential and Q_s<=12*s/x^4 on x>=1.
The sum of the remaining two translated Gaussian integrals, extended
from x>=1 to x>=0, equals sqrt(8*pi*sigma). Including the factor1/2
in h_rho therefore gives

    int_1^infinity |h_rho(x)|*Q_s(x) dx
      < (12*2*16/15)/sqrt(2) * s*gamma^-4
      < (96/5)*s*gamma^-4.                              (7)

For the last inequality use 1/sqrt(2)<3/4. C034b(12),(13), already
audited, bound the absolute origin-interval contribution by
(2/125)*s*gamma^-4 and the constant subtraction on [1,infinity)
by s/(10000*gamma^4). Consequently the absolute complete-member
integral is less than

    (96/5+2/125+1/10000)*s*gamma^-4 < 20*s*gamma^-4.

These are uniform summable bounds because S is finite. All labeled
members, both translates, conjugates and multiplicities remain.
C034b's justified absolute sum gives d_s<20*s*S. Its audited lower
bound d_s>s*S/2 proves (1). Neither the sign nor a bound for the
spatial profile itself was assumed.

### Reparametrization, reversed nodes and determinant magnitude

Put x(sigma)=k_1(sigma)/k_1(1) and y(sigma)=k_2(sigma)/k_2(1).
Integrating (1) from width1, and using x'=-x*d_1, y'=-y*d_2,
gives throughout [1,2]

    exp(-20*S)<=x<=1, exp(-40*S)<=y<=1,
    |x'|>exp(-20*S)*S/2,
    |x'|<20*S, |y'|<40*S.                              (8)

Both functions are real C^2 on (1/2,3). The continuous x' is strictly
negative on [1,2], hence on a slightly larger open interval by compactness.
It is injective there. The real inverse function theorem gives a C^2
inverse psi on an open neighborhood of x([1,2]). Thus f=y composed
with psi is real C^2 there. Ordinary differentiation gives exactly

    f''(x(sigma))=(x'*y''-y'*x'')/(x')^3.

C034i gives x'*y''-y'*x''=x*y*T, T<-A. As x'=-x*d_1,

    f''= -y*T/(x^2*d_1^3)
         > exp(-40*S)*A/(8000*S^3)>0.                  (9)

All divisions are legitimate: S>0, x>0, d_1>S/2. The factors in
(9) use x<=1, y>=exp(-40*S), d_1<20*S; no inverse norm is assumed.

At widths sigma_0=1,sigma_1=3/2,sigma_2=2 the nodes satisfy
x_2<x_1<x_0=1. Integrating the lower bound in (8) gives

    x_0-x_1 > exp(-20*S)*S/4,
    x_1-x_2 > exp(-20*S)*S/4,
    x_0-x_2 > exp(-20*S)*S/2.

Apply de Boor(44)-(45) first in increasing x order. The determinant
is the positive Vandermonde product times f''(xi)/2. Reversing the
three rows to the prescribed increasing-width order swaps the first
and last rows and changes its sign. Its magnitude is therefore larger
than

    [exp(-60*S)*S^3/32]
         *[exp(-40*S)*A/(16000*S^3)]
      =exp(-100*S)*A/512000.

This proves (3), including its orientation and the column-normalization
factors. The regularity neighborhood justifies endpoint derivatives;
no sign outside [1,2] is used.

### Independent full-divisor compact-excision allowance

At zero, the two translates in p_a coincide, so
p_a(0)=sum_rho G_a(z_rho), with no extra factor1/2. On the complete
range a in [7/6,5/4],

    |p_a(0)| <= (16/15)/sqrt(4*pi*a)
                                  *sum_rho exp(-gamma_rho^2/5).

The actual ell_1 is nonnegative by the inherited Levy input. Using
t>=1, a>=1, length([1,3/2])=1/2, and 0<=1-exp(-j*t)<=1,
C033m's exact rescaling yields

    0<=P_j <= (4/15)*sum_rho exp(-gamma_rho^2/5).

For gamma>=14 the function gamma^4*exp(-gamma^2/5) is decreasing.
Moreover exp(3)>20: its series through degree8 is 806769/40320>20.
Since 196/5>39, it follows that

    sum_rho exp(-gamma_rho^2/5) < (14^4/20^13)*S,
    P_j < [4*14^4/(15*20^13)]*S < alpha*S.              (10)

The last rational comparison is
4*14^4*(5*10^12)=768320000000000000
<15*20^13=1228800000000000000. These bounds include the entire
tail and every nonreal member by modulus; the S majorant justifies
the absolute series uniformly in a. Reality follows by conjugation.
No zero coordinates, quadrature, spatial-profile positivity or residual
smallness were inserted as premises. This proves (2).

### Cofactors and the exact variation comparison

After column normalization, the system is

    M_0^T a=(1,exp(P_1),exp(P_2))^T.

Set r_j=exp(P_j)-1. By (10) and exp(v)-1<=v*exp(v) for v>=0,

    0<=r_j<R, R=alpha*S*exp(alpha*S).

Subtract the width-one column from the two observation equations and
use a_0=1-a_1-a_2. Writing u_i=x_i-1, v_i=y_i-1 for i=1,2 gives

    u_1*a_1+u_2*a_2=r_1,
    v_1*a_1+v_2*a_2=r_2,
    D=u_1*v_2-u_2*v_1=det M_0.

The upper derivative bounds (8) retain the actual half-width distances:

    |u_1|<=10*S, |u_2|<=20*S,
    |v_1|<=20*S, |v_2|<=40*S.

Cramer's rule, with D nonzero by (3), now gives

    |a_1|=|(r_1*v_2-u_2*r_2)/D| <=60*S*R/|D|,
    |a_2|=|(u_1*r_2-v_1*r_1)/D| <=30*S*R/|D|.

Since |a_0|<=1+|a_1|+|a_2|, the variation is bounded by
1+180*S*R/|D|. Substitution of (3) and A=S*(50*S_8+S^2/5)
proves (4), with 180*512000=92160000. This controls the exact
solution, not rounded weights or a conditional unverified linear solve.

The retained member r<15 gives S_8>15^-8. The arithmetic-geometric
mean inequality therefore gives

    50*S_8+S^2/5 >=2*S*sqrt(10*S_8)>6*S/15^4.

If S<=1/100, then (100+alpha)*S<21/20 and exp((100+alpha)*S)<3.
For an elementary check, e<11/4 and exp(1/20)<=20/19 give
exp(21/20)<55/19<3; e<11/4 follows from summing its series through
degree4 and bounding the remaining tail by1/100. Hence the excess
over1 in (4) is less than

    92160000*alpha*15^4/2=1458/3125<1/2.

This proves exactly (5) under its additional condition.

### Historical finite-count stopping point in attempt1876

Let N(100) count all positive-ordinate members with gamma<=100,
including every multiplicity and the endpoint. If N(100)<=100 were
available, the hypotheses gamma>14 and the retained reciprocal-square
tail would imply

    S < 100/14^4 + (1/10000)*sum_(gamma>100) gamma^-2
      < 100/14^4+1/10000 < 1/100.                       (11)

At attempt1876, the inspected inherited conditions said that displacements vanish
through100; that alone is not a bound on the number of members there.
The qualitative O(T log(T+2)) count also has no supplied numerical
constant at100. Neither is replaced by remembered zero data. No
primary rigorous count sufficient for (11) was imported in this turn.
That attempt stopped the cap claim at this precise input, preserving the quantitative
partial result (1)-(4) and sufficient comparison (5),(11).

If the missing count is later justified and this proof survives audit,
the distinct three atoms would have mass1, exact matching at1,2 and
variation<2, so their measure belongs to C033w's A_2. Nonnegativity
of the finite minimax value then yields d_{ {1,2} }=0. This conditional
consequence has no full-observation, signed-height, cancellation or
actual-Xi implication. Stops1798/1839/1843/1847/1866 remain valid in
their recorded scopes. No general impossibility or actual TV>2 follows
from the present missing input.

### Conceptual audit and count specialization1879 — 20 November 2026

**Verdict and source scope.** The proof of (1)-(5),(11) passes, retaining
all stated hypotheses. Use the unchanged pre-invocation SPECIALIZE
assessment1877 and reuse1875/1196. The de Boor, real inverse function
theorem and Cramer inputs are exactly those cited above. The new
fixed-height counting application below pays the specific missing input;
no scalar transform or zero ordinate is evaluated. This is local
reproduction and specialization, not a new counting theorem or a result
beyond the sources checked. The earlier count stop records what was
missing at1876, not a permanent obstruction.

**Complete-member derivative estimate.** For (6) the weakest Gaussian
decay is sigma=2. On [3gamma/4,gamma], the quadratic upper bound has
maximum 1024/(9gamma^2)<256/441<2/3. On [gamma/2,3gamma/4],
x(gamma-x)>=3gamma^2/16>32, so F is increasing. On [1,gamma/2]
the numerator of F' is increasing and can cross zero only from negative
to positive; hence both endpoints suffice. Their upper bounds are
-1/16 and 7/16, respectively. The finite exponential sums used for
log2<3/4 and log14<11/4 are 269/128>2 and
1805231/122880>14. The displayed integral of the tangent to 1/t is
strictly less than log2 and equals2/3. This verifies the constant2
uniformly for every member and both translates, including the unbounded
range gamma>14.

Splitting each Gaussian exponential in half, integrating the remaining
two translates on the positive half-line, and retaining the averaging
factor1/2 gives exactly the factor1/sqrt(2) in (7). Since
1/2<9/16, it is less than3/4. C034b(12)'s proof uses the pointwise
Taylor bound |h(x)-h(0)|<=x^2 sup|h''|/2 and positive Q_s; it therefore
bounds the integral of the absolute value, although its displayed
conclusion only encloses the absolute value of the integral. Together
with C034b(13), the absolute complete-member coefficient is at most
192161/10000<20. Summability of S and the inherited absolute Fubini
argument justify the full member sum, with conjugates and multiplicities.
The strict lower bound is the already audited C034b(2). No spatial
profile sign is needed for (1).

**Coordinate and determinant checks.** Real C^2 regularity holds on
(1/2,3). On [1,2], x'=-x*d_1<0 with a uniform strict lower bound for
|x'|. Continuity extends this sign to an open interval containing the
closed width interval, so x is one-to-one there and its inverse is C^2.
For f=y composed with x^{-1}, direct differentiation gives
f''=(x'y''-y'x'')/(x')^3=-y*T/(x^2*d_1^3). C034i's T<-A,
x<=1, y>=exp(-40S) and 0<d_1<20S yield (9), without replacing a
denominator by a lower bound in the wrong direction. The three positive
node spacings have product greater than exp(-60S)*S^3/32. de Boor's
second divided difference supplies the additional factor1/2, giving
32*16000=512000. Increasing widths correspond to decreasing x nodes;
reversing all three rows is a single swap. Thus the determinant is
negative and has precisely (3)'s magnitude bound. The positive column
normalization factors do not affect its sign. No sign outside [1,2]
or qualitative conditioning premise is used.

**Compact excision and cofactors.** C033m(1),(3) gives exactly the stated
P_j and a([1,3/2])=[7/6,5/4]. At zero the two even Gaussian translates
coincide, so p_a(0)=sum G_a(z_rho), with no additional factor1/2.
The complex-displacement modulus factor is at most16/15, the exponent
is at most -gamma^2/5, and sqrt(pi)/sqrt(4pi*a)<=1/2. The time interval
has length1/2. These factors give4/15 in (10). Only the qualified Levy
density sign is used to conclude P_j>=0. The function
gamma^4 exp(-gamma^2/5) has logarithmic derivative4/gamma-2gamma/5<0
on gamma>=14. The degree8 partial sum for exp(3) is
89641/4480>20, and 196/5>39. Therefore the strict allowance in (10)
is valid for the entire divisor and is less than alpha*S; the finite
coefficient comparison is 2401/19200000000000000<1/5000000000000.
This also gives the required uniform absolute-series majorant.

Column normalization in M means left multiplication by the corresponding
diagonal matrix in the transposed matching equations. Hence the right
side is exactly (1,exp(P_1),exp(P_2)), not its reciprocal. Eliminating
a_0 gives the displayed two-by-two system with determinant det M_0.
The mean-value allowances preserve the half-width distances. Cramer's
rule gives60*S*R and30*S*R, and the mass-one equation bounds variation
by1+180*S*R/|D|. Since180*512000=92160000, (4) follows. The retained
member r<15 gives S_8>15^-8; AM-GM and sqrt(10)>3 give the strict
denominator floor6*S/15^4. For S<=1/100 the exponent is below21/20.
The exponential tail after degree4 at1 is strictly less than
(1/120)/(1-1/6)=1/100, so e<1631/600<11/4; also
exp(1/20)<=20/19 by its geometric-series majorant. Thus the needed
exponential is less than55/19<3. The final excess is exactly bounded
by1458/3125<1/2. This checks (5) with strict margin.

**Primary count and endpoint application.** Import Elchin Hasanalizade,
Quanli Shen and Peng-Jie Wong, *Counting zeros of the Riemann zeta
function*, J. Number Theory235 (2022),219-241,
[arXiv:2107.06506v1, 14 July2021](https://arxiv.org/pdf/2107.06506v1),
Corollary1.2, equation(1.5), printed p2:

    |N(T)-F(T)|<=B(T), T>=e,
    F(T)=T/(2*pi)*log(T/(2*pi*e)),
    B(T)=0.1038*log T+0.2573*log log T+9.3675.

The count is over the full strict strip 0<Re rho<1 with
0<Im rho<=T. The definition on p1, argument-principle discussion
(2.1)-(2.3) on p3 and complete small-height proof (5.5)-(5.6) on p15
are covered by assessment1877/1196 and C030i. Multiplicities are
included. The imported small-height case covers e<=T<=30610046000;
its cited finite computation is an input to the theorem, not a
computation reproduced here. C030i's endpoint argument applies: the
entire nonzero completion has locally finitely many zeros in the strip,
so choose nonzero contour heights T_n decreasing to100 below the next
ordinate above100. Then N(T_n)=N(100), including all multiplicities at
100. Continuity of F and B passes the bound to that endpoint, even if
one initially states the argument-principle formula away from zeros.

The normalization agrees with Z+: each positive-ordinate occurrence
rho is one label z_rho, including its multiplicity. An off-line pair
at the same positive ordinate gives two labels in both counts; negative
ordinates do not add another factor. No RH or simplicity assumption is
used to import this upper count.

For explicit arithmetic, the exponential series gives e>8/3, since
its terms through degree3 sum to8/3 and all remaining terms are
positive. Also e<11/4<100 by the estimate above. Since
(8/3)^5=32768/243>100, one has log100<5. The elementary inequality
log u<u for u>0, applied to u=log100, gives
loglog100<log100<5. Archimedes' bound pi>3 and 2*pi*e>1 give

    F(100)<100/(2*pi)*log100<250/3,
    B(100)<5*(0.1038+0.2573)+9.3675=11173/1000,
    N(100)<=F(100)+B(100)<283519/3000<100.                (12)

This is a deliberately coarse rigorous specialization of the imported
theorem; it is not an evaluation of N(100). Its integral value is at
most94, but only the weaker bound100 is used. Splitting the full
divisor at the inclusive height100 and using gamma>14 and the retained
strict reciprocal-square-tail input gives exactly (11), namely

    S<100/14^4+1/10000=64901/24010000<1/100.              (13)

Every member at100 is in the finite part, and the tail uses gamma>100.
The actual count alone proves neither the separate low-zero reality
condition, the retained real zero, nor the qualified tail or heat laws.

**Finite consequence and limits.** Substitute (13) into (5). The exact
solution already has mass one and matches m(1),m(2), and its three
widths are distinct. Hence its variation is the sum of absolute weights,
which is strictly below4583/3125<2. It is therefore an admissible
member of the full class A_2, giving a zero objective at the two
observations. Since that objective is nonnegative, d_{ {1,2} }=0.
No sign of the individual weights, continuum equality, evaluated
full-interval minimax, signed-height payment, cancellation or Xi
realization is asserted. In particular all inherited C032m/n,
C033l/C032q, C034c/h/d/e/f, fixed-v1, finite-zero and heat qualifications
persist. C034g is unused; no global Sobolev premise is added.

Exact rational checks are reproducible by
`python3 scripts/smoothed-law/three_width_cap_audit_1879.py`; the full
certificate is `scripts/smoothed-law/three_width_cap_audit_1879.json`.
All 23 comparisons pass. These verify arithmetic only; the analytic
arguments, summability and source applicability are justified above.
The only additional direct mathematical input is C030i's imported
count and endpoint interface. Earlier analytic/evaluator stops remain
valid in their stated scopes and are preserved.

### Bounded third-difference attempt1904 — 20 November 2026

**Scope and result.** Under unchanged assessment1903, attempt only the
test f(u)=(1-exp(-u))^3 for the existing exact output
Q=sum_(i=0)^2 a_i*nu_(sigma_i), sigma=(1,3/2,2). All hypotheses above
remain, including the qualified probability laws of C032j. C032q
supplies bounded signed integration. This attempt does not certify a
negative value. The explicit enclosure below contains zero; the
sharper comparison is left unevaluated. Park this diagnostic, without
changing its order, spacing, widths or weights. This is an inconclusive
classical-criterion specialization, not a new sign theorem, a proof of
positive output or evidence against RH.

Import Persi Diaconis and David Freedman, *The Markov Moment Problem
and de Finetti's Theorem: Part I*, author version15June2003,
[equation(1), pp1-2, Lemma1(a) and its proof, p2](https://www.stat.berkeley.edu/~census/631.pdf),
as inspected in source review1903. With Delta t_j=t_(j+1)-t_j, the
n=3,j=0 case is t_0-3*t_1+3*t_2-t_3=int(1-x)^3 dP(x)>=0 for a
probability P on [0,1]. Only this necessary condition is imported;
neither the all-orders converse nor the density-constrained theorem
is needed. The elementary bounds below apply Cauchy--Schwarz to
bounded functions; no additional tail or moment theorem is invoked.

**The finite signed test and exact common numerator.** Write

    K_j(sigma)=exp(-B_sigma(j)), j=1,2,3,
    C_i=1-3*K_1(sigma_i)+3*K_2(sigma_i)-K_3(sigma_i).

C032j defines these transforms at every positive parameter. The
identification with the earlier k_j holds for j=1,2. Each nu_sigma
is a probability on [0,infinity), so 0<=C_i<=1. Moreover 0<=f<=1,
Q has finite variation at most sum|a_i|, and C032q gives its bounded
integral as the finite sum sum a_i*C_i. Thus no density, unbounded
moment, interchange of an infinite signed sum, or positive Q is used.
Expanding the finite polynomial and using only the already proved
mass and matches at1,2 gives exactly

    D_3=int f dQ=1-3*m(1)+3*m(2)-sum_i a_i*K_3(sigma_i).

A negative D_3 would contradict nonnegativity of Q, by the imported
necessary condition under x=exp(-u). The converse is not asserted.

Retain precisely the normalized x_i,y_i,u_i,v_i,r_j,D above and set

    t_j=K_j(1), j=1,2,3,
    A_1=r_1*v_2-u_2*r_2, A_2=u_1*r_2-v_1*r_1,
    h_i=K_3(sigma_i)-t_3, i=1,2,
    Delta=-D>0, N=A_1*h_1+A_2*h_2.

There is no approximation to the weights: a_1=A_1/D,
a_2=A_2/D, a_0=1-a_1-a_2. Hence the third coordinate of Q is
t_3+N/D and m(j)=t_j*(1+r_j) for j=1,2. Consequently

    D_3=C_0-3*t_1*r_1+3*t_2*r_2+N/Delta,               (14)
    Delta*D_3=Delta*(C_0-3*t_1*r_1+3*t_2*r_2)+N.        (15)

This retains the negative determinant's orientation and all cofactor
cancellations. The required comparison is that the right side of
(15) be at most -epsilon*Delta for some specified epsilon>0.
It is not enough to bound N alone: C_0 and the two residual terms
remain part of the same comparison. In particular no existing
quantitative j=1,2 estimate has been asserted at3.

**An analytic enclosure at3 from bounded component moments.** One can
bound each C_i without a scalar evaluator. For each fixed i, let
X=exp(-u) on the probability space nu_(sigma_i), and write

    p_i=K_1(sigma_i)=E X, q_i=K_2(sigma_i)=E X^2.

Here 0<p_i<1. Positivity follows from the finite positive-real
transform. Strict inequality from1 follows because C032j's qualified
heat positivity makes ell_sigma(t)>0 for every t>0, so
0<B_sigma(1)<infinity. Put Y=1-X. Cauchy--Schwarz applied to
Y^(1/2),Y^(3/2), and then to X^(1/2),X^(3/2), gives

    (E Y^2)^2 <= E Y * E Y^3,
    (E X^2)^2 <= E X * E X^3.

Every variable here is bounded by1; these are not moments of u.
Dividing only by the strictly positive denominators gives

    L_i=(1-2*p_i+q_i)^2/(1-p_i) <= C_i,
    C_i <= U_i=1-3*p_i+3*q_i-q_i^2/p_i.                (16)

For a_i^+=max(a_i,0), a_i^-=max(-a_i,0), finite signed summation
therefore yields the valid enclosure

    sum_i(a_i^+*L_i-a_i^-*U_i) <= D_3
                         <= sum_i(a_i^+*U_i-a_i^-*L_i). (17)

This is application work for the single approved third difference.
It neither assumes coefficient signs nor refits them. It reduces one
possible negative certificate to the upper expression in (17), but
the existing coarse allowances do not evaluate its actual p_i,q_i or
cofactor signs closely enough in this attempt. No claim is made that
(17) itself must contain zero for the exact divisor.

For a completely explicit enclosure using the paid bounds, the
cofactor argument above gives

    |a_1|+|a_2| <= 90*S*R/Delta < 729/3125.

Indeed twice this upper allowance is exactly the term bounded by
1458/3125 in the proof of(5); audit1879 pays its S<=1/100 condition.
Using mass one and 0<=C_i<=1, retain the width-one term:

    D_3=C_0+a_1*(C_1-C_0)+a_2*(C_2-C_0),
    |D_3-C_0| < 729/3125,
    -729/3125 < D_3 < 3854/3125.                        (18)

The upper bound3854/3125 is positive, whereas the target is an upper
bound -epsilon<0. Thus(18) supplies no negative certificate. This is
a failure of this bounded estimation attempt, not proof that no
stronger analytic estimate can work, and not an evaluation of D_3.
The exact unpaid comparison is(15), or the sufficient upper test(17).
No scalar quadrature, zero-data substitution, changed observation or
mathematical script was used. Stops1798/1894/1900 are not reopened.

All original qualifications persist: the complete actual divisor,
conjugation and multiplicity; no ordinate-zero member; strict strip
and gamma>14; counting; zero displacements through100 and the retained
real zero; the reciprocal-square tail; heat positivity and the
separate fixed-j heat-error contracts; zero drift and killing;
Gaussian half-variance; and both fixed-v1 preprints. The paid count
does not verify their remaining hypotheses. Positive output, uniform
accuracy, moments, full cancellation, signed height and actual-Xi
realization all remain unresolved.

### Bounded first-coefficient attempt1906 — 20 November 2026

**Scope and outcome.** Use the unchanged, pre-invocation SPECIALIZE
assessment1905 for the same three widths, exact coefficients and
C033i/l residual. Set q_i=p_(sigma_i)(0), sigma=(1,3/2,2), and
c=sum_i a_i*q_i. C032j gives q_i>0, with all its qualifications.
C032l's recorded origin derivative explains the choice of statistic;
its finite-family independence theorem is not used. The inspected
necessary Laplace signs are Ante Mimica, *Laplace transform*, Dresden
course27 April-1 May2015,
[Proposition1.4(i)-(ii), printed pp6-7](https://web.math.pmf.unizg.hr/~amimica/lt.pdf).
The individual Gaussian coefficient is also in Sra, *Some positivity
properties of Riemann Xi under smoothing*, fixed2611.00345v1,
[Theorem4.1 and AppendixA.7 PropositionA.8](https://hexagonmath.org/pdf/2611.00345v1),
as inspected in review1905. Neither result decides this signed c.
No general theorem or individual cusp is reproved here.

The enclosure below contains both signs. This is an inconclusive
application attempt, not a negative-output certificate, an evaluation
of c, or a positive-output theorem. The prescribed threshold
c<=-epsilon<0 is not attained. Accordingly no small-parameter witness
or analytic remainder calculation is undertaken. In particular no
finite moment at s=0 or signed-tail inversion is substituted for the
origin derivative. This calculation has not received a separate audit.

**Keep the exact common numerator.** Retain A_1,A_2,D and Delta=-D>0
from the cofactor section and attempt1904. Finite algebra, using
a_0=1-a_1-a_2, gives

    c=q_0-[A_1*(q_1-q_0)+A_2*(q_2-q_0)]/Delta,
    Delta*c=Delta*q_0-A_1*(q_1-q_0)-A_2*(q_2-q_0).    (19)

Thus the sought negative certificate would require

    A_1*(q_1-q_0)+A_2*(q_2-q_0)
                       >=Delta*(q_0+epsilon), epsilon>0.

No signs for A_1,A_2 or their weighted sum are assumed. The negative
determinant reverses the correction sign in (19); replacing D by its
modulus in the original weight formulas would lose this orientation.

**Complete-profile bounds for this comparison.** For 1<=sigma<=2,
the two translates coincide at zero and conjugation makes their
complete sum real. The Gaussian definition gives

    p_sigma(0)=sum_rho G_sigma(z_rho),
    |G_sigma(z_rho)|
      <=(16/15)*exp(-gamma_rho^2/(4*sigma))/sqrt(4*pi*sigma).

Here exp(delta_rho^2/(4*sigma))<exp(1/16)<=16/15. On gamma>=14,
gamma^4*exp(-gamma^2/(4*sigma)) is strictly decreasing: its
logarithmic derivative is 4/gamma-gamma/(2*sigma)<0 since
gamma^2>=196>8*sigma. Consequently, with the already paid (13),

    sum_rho exp(-gamma_rho^2/(4*sigma))
       <=14^4*S*exp(-49/sigma),
    14^4*S<64901/625.

The finite S majorant proves absolute summability of the full series;
no member, conjugate or multiplicity is dropped. Since pi>3 implies
sqrt(4*pi*sigma)>3 and 1038416/28125<40, C032j's positive origin
value therefore obeys

    0<p_sigma(0)<U_sigma:=40*exp(-49/sigma).             (20)

A retained-real-member lower bound is available at width1. All
members through the inclusive ordinate100 have zero displacement
and positive real Gaussian contribution. The retained r in (14,15)
contributes more than exp(-225/4)/sqrt(4*pi). The remaining possibly
nonreal members must not be discarded. On gamma>100,
gamma^2*exp(-gamma^2/4) is decreasing, and the qualified
reciprocal-square tail is less than1. Hence their total modulus is
less than

    (16/15)*10000*exp(-2500)/sqrt(4*pi).

This is less than exp(-225/4)/(2*sqrt(4*pi)). Indeed
2500-225/4=9775/4>12 and the already checked exp(3)>20 gives
exp(9775/4)>20^4=160000>320000/15. The finite real contributions
and the signed tail therefore give, using pi<4,

    q_0>exp(-225/4)/(2*sqrt(4*pi))
        >L_0:=exp(-225/4)/8>0.

This lower bound does not assert positivity of a spatial profile or
of each nonreal member. It pays the entire complex tail before
retaining the real contribution. The count used for (20) and the
separate low-zero reality and tail hypotheses have distinct roles.

**Achieved enclosure versus the required sign.** Write
U_0=40*exp(-49), U_1=40*exp(-98/3), U_2=40*exp(-49/2).
Then U_0<U_1<U_2. By (20), |q_i-q_0|<U_i for i=1,2.
With R=alpha*S*exp(alpha*S), the original exact cofactor bounds
first yield the more structured allowance

    |c-q_0|<(30*S*R/Delta)*(2*U_1+U_2).

It is an absolute allowance, not an evaluation of the signed numerator
in (19). Alternatively the paid bound
|a_1|+|a_2|<729/3125 gives |c-q_0|<(729/3125)*U_2. Combining it
with the preceding upper and lower bounds for q_0 yields the fully
explicit enclosure

    exp(-225/4)/8-(5832/625)*exp(-49/2) < c
      <40*exp(-49)+(5832/625)*exp(-49/2).              (21)

Its lower endpoint is negative: 225/4>49/2 and 1/8<5832/625.
Its upper endpoint is positive. Thus (21) does not supply the
required negative upper bound, or a nonnegative lower bound. The
exact comparison in (19) is unpaid; (21) does not show that a sharper
comparison is impossible or that the exact c lies on either side.
No scalar transform, zero ordinate, coefficient fit, parameter scan,
new width or mathematical script was evaluated. Park this diagnostic
without higher orders, refitting or another attempt on these bounds.

All hypotheses of this lemma remain in force: complete actual divisor,
conjugation and multiplicities; no ordinate zero; strict strip and
gamma>14; counting; displacement zero through100, retained real zero
and reciprocal-square tail; heat positivity and separate fixed-j
heat-error inputs; zero drift and killing; Gaussian half-variance;
and both fixed-v1 qualifications. Their independent validity, output
sign, accuracy, moments, full cancellation, signed height and actual-Xi
realization are not established by this calculation.

## Mathlib

Full matching coverage is unchecked and unknown. No formal theorem is
invoked or asserted absent. Real inverse differentiation, finite matrix
identities, Gaussian integration and divided differences are supporting
topics, but their exact APIs and a matching theorem for this qualified
actual-divisor comparison have not been verified. This is an informal
classical-tool specialization. Audit1879 verifies its quantitative
application and imports the count with explicit fixed-height arithmetic;
it does not change the unknown formalization status or certify the
other inherited external inputs. The bounded signed-moment and cofactor
specialization in attempt1904 has no checked full Mathlib match;
supporting Cauchy--Schwarz and finite-integration APIs were not inspected.
The complete-profile/cofactor enclosure in attempt1906 likewise has
no checked full matching Mathlib theorem; no absence claim is made.
