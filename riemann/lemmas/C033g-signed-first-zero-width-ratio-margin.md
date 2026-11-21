# Corollary C033g: signed first-zero width-ratio margin

## Hypotheses

Use C032j/m/n's full positive-ordinate divisor, with multiplicities,
conjugation symmetry, gamma>14 and |delta|<1/2, and precisely

    z_rho=gamma_rho-i*delta_rho,
    G_s(z)=exp(-z^2/(4*s))/sqrt(4*pi*s),
    p_s(z)=(1/2)*sum_rho [G_s(z-z_rho)+G_s(z+z_rho)],
    R_s(w)=integral_0^infinity (p_s(x)-p_s(i*w))/(x^2+w^2) dx,
    E_s(w)=4*integral_0^w t*R_s(t) dt,
    A_s(y)=2*pi*integral_0^y p_s(x) dx,
    e_s(y)=E_s(i*y), k_s(y)=exp(-e_s(y))*sin(A_s(y)).

The removable values in R are included. Put a=1/8, b=1/4,
f(s)=k_s(a), g(s)=k_s(b), W=f*dot g-g*dot f, where dot denotes
width differentiation, and let 1<=s<=2. Retain the fixed-v1 and
finite-height qualifications of C032j/m/n and C033f, including
V(3*10^12); this result does not reverify the external sources.

In addition use the source-qualified low-zero input: exactly one
simple positive-ordinate zero has ordinate below or equal to20; it
is on the line, with r in (14,15). Every other positive-ordinate
member has gamma>20. Use the corrected inclusive Bellotti--Wong v2
count stated in section1. These inputs are cited precisely below.
Neither RH nor reality of the remaining divisor is assumed.

## Conclusion

Uniformly on the closed width interval,

    W(s)/f(s)^2 < -1/2000.                                  (1)

Both f and g are positive. Consequently, for 1<=s<t<=2,

    f(s)*g(t)-g(s)*f(t) < -(t-s)*f(s)*f(t)/2000 < 0.          (2)

This pays only C032n(19)'s two-point sign premise. It neither
excludes arbitrary signed annihilating measures nor proves
constant-span completeness, positive output, moments, unsmoothed
Xi realization or L030-L032/C032a all-degree positivity. The first
proof attempt1728 was unaudited; conceptual audit1730 below confirms
this qualified estimate without changing its hypotheses or bound.

## Proof

### 1. Source imports, scope and elementary counting consequences

The approved assessment1726 and separate approval1727 cover exactly
this signed first-zero comparison, including relative errors and E.
Comparison1709 and stops1711/1725 exclude automatic total positivity
and phase-only completion. No matching signed theorem was found in
the recorded bounded screen; no claim of originality follows.
C033f already pays f>0 with its stated source qualifications. We
need a quantitative relative comparison, which its absolute phase
bound does not supply. C032m/n supply uniform analyticity and width
differentiation; no Gaussian heat-flow theorem is reproved here.

Import the first-zero separation from FLINT's official
[zeta-zero API contract and complete example](https://flintlib.org/doc/acb_dirichlet/zeta-zeros.html),
version3.7.0-dev, generated17 November2026, build1d432c3bba.
The example starts at n=1 and gives the first two positive ordinates
14.1347251417346937904572519836 +/-3.76e-29 and
21.0220396387715549926284795939 +/-3.10e-30.
The consecutive-zero contract includes completeness, critical-line
location and simplicity, not just discovered sign changes. Thus it
implies exactly the coarse separation in the hypotheses. This is an
imported external certified computation, not a local replay or formal
verification. The page warns of LLM-generated documentation; retain
the checked fixed-commit
[low-index implementation](https://github.com/flintlib/flint/blob/1d432c3bba36d1a29f6453ebfaa00e43f58c278f/src/acb_dirichlet/isolate_hardy_z_zero.c),
constants and complete _separated_gram_list/_separated_list cases,
lines25-31,922-998 and create_gram_node lines163-213, as inspected in
source-working1726. That branch uses the historical first126 Gram-law
input, not Turing's large-height inequality at height20. Algorithm
background: Arias de Reyna, *Programs for Riemann's zeta function*,
CWI (2012), Section2, pp104-106, Theorem2.1,
[final primary PDF](https://ir.cwi.nl/pub/19724/19724D.pdf).
The external-computation qualification remains essential.

Import Bellotti--Wong, *Improved estimates for the argument and
zero-counting function of the Riemann zeta-function*,
[arXiv:2412.15470v2, 7 July2025](https://arxiv.org/pdf/2412.15470v2),
Theorem1.1 p1 and Section5 pp23-24. For every t>=e, counting all
positive ordinates <=t inclusively and with multiplicity,

    N(t)<=t/(2*pi)*log(t/(2*pi*e))
               +0.11200*log t+0.12567*log log t+3.77417.     (3)

These are the corrected source constants assessed in notes1721.
C032y's older displayed constant and its numerical consequences are
not inputs here. For t>=14, the main term is at most t*log t/6:
if its logarithm is negative use zero as upper bound, and otherwise
use 2*pi>6 and log(t/(2*pi*e))<log t. The remaining terms are less
than (log t)/4+4. Since log t>2,

    (t/6-1/4)*log t >=(14/6-1/4)*2=25/6>4.

It follows that

    N(t)<t*log t/3 <=t^2/6 <t^2, t>=14.                    (4)

Here log t<=t/2 follows by differentiation from t=2. Tonelli applied
to gamma^(-q)=integral_gamma^infinity q*t^(-q-1)dt, with gamma>14,
gives, without a cutoff omission,

    S2=sum_rho gamma^(-2)<4/21,
    S4=sum_rho gamma^(-4)<40/(27*14^3).                      (5)

Indeed the bounds are (2/3)*(log14+1)/14 and
(4/3)*(log14/3+1/9)/14^3, respectively; use log14<3.
All sums here and below retain every multiplicity and off-line member.

For the elementary constants use 3<pi<4, 8/3<e<3. The latter bounds
follow from the exponential series (its first five terms exceed8/3,
and the factorial tail is bounded by a geometric series). In
particular log14 lies in (2,3), since e^2<9<14 and e^3>(8/3)^3>14.
Also exp(1/16)<=16/15 and exp(3)>16 by the first five terms.

### 2. Complete Gaussian sums and the noncompact spatial bounds

Write Q=3/8 and c0=exp(1/16)/sqrt(4*pi)<16/45. Set

    T32=sum_rho exp(-gamma^2/32),
    T8 =sum_rho exp(-gamma^2/8).

The unique first member contributes less than exp(-196/32)<Q^6
to T32. Place every other ordinate in its unique shell [n,n+1),
n>=20. By (4) its multiplicity count is at most (n+1)^2/6.
Successive shell majorants have ratio at most

    (22/21)^2*exp(-41/32) < 1/2;

use exp(41/32)>1+41/32=73/32 and 2*484*32<441*73.
Thus the entire infinite tail, not a finite preview, satisfies

    T32 < Q^6+147*Q^12 <1/250,
    T8  < T32/100.                                         (6)

For the second bound, exp(-3*gamma^2/32)<exp(-18)<1/100.
An ordinate on an integer shell boundary belongs to the next shell;
the inclusive count may overcount but never deletes it.

For real x, the exact complex Gaussian modulus bounds a single
divisor member's contribution by

    exp(1/16)/2 *[G_s(x-gamma)+G_s(x+gamma)].                (7)

For q=2 or4, split its positive-center integral over x>=1 at
x=gamma/2. On the lower part, G_s(x-gamma)<=
exp(-gamma^2/32)/sqrt(4*pi); use integral_1^infinity x^(-q)dx
=1/(q-1). On the upper part x^(-q)<=2^q/gamma^q and the full
real Gaussian integral is1. The negative-center integral has the
bound exp(-gamma^2/8)/((q-1)*sqrt(4*pi)) on the whole half-line.
Tonelli therefore proves the absolutely convergent estimates

    J2:=integral_1^infinity |p_s(x)|/x^2 dx
       <=(c0/2)*(T32+T8)+2*exp(1/16)*S2 <5/12,
    J4:=integral_1^infinity |p_s(x)|/x^4 dx
       <=(c0/6)*(T32+T8)+8*exp(1/16)*S4 <1/200.            (8)

The rational upper bounds before the last simplifications are

    (16/45)*(101/100)/(2*250)+(32/15)*(4/21),
    (16/45)*(101/100)/(6*250)+(128/15)*40/(27*14^3).

To control the removable compact part, for |z|<=2 use the same
modulus calculation as C032m, retaining the imaginary displacement:

    |p_s(z)|<=c2*sum_rho exp(-(gamma-2)^2/8),
    c2=exp(25/16)/sqrt(4*pi)<3.

The first member is bounded by exp(-18). For the remaining members
use the coarser shell count (n+1)^2 and n>=20. The shell ratio is
less than (5/4)*exp(-3)<1/8, so that

    sup_(s in[1,2], |z|<=2)|p_s(z)|
       <M:=3*(Q^18+504*Q^40)<10^(-6).                      (9)

The first tail exponent is (20-2)^2/8=40.5>40. These bounds are
valid for the entire complex divisor, not just real centers.

### 3. Effective E correction, including its removable part

Write the even entire series p_s(z)=sum_(k>=0) h_k*z^(2k).
By (9) and Cauchy's coefficient estimate, |h_k|<=M/4^k,
uniformly in width. Split the spatial integral defining R at x=1,
and write R_s(w)=sum_(j>=0) r_j*w^(2j), initially for |w|<1.
For the compact part, polynomial division gives exactly

    (x^(2k)-(-w^2)^k)/(x^2+w^2)
       =sum_(j=0)^(k-1) x^(2(k-1-j))*(-w^2)^j.

This identity includes the removable locus. Absolute convergence
of the h_k series on x<=1 and compact subdisks of |w|<1 justifies
integration and collection of coefficients, yielding

    |r_j^(near)|<=M/(3*4^j), j>=0.                         (10)

On x>=1 expand 1/(x^2+w^2) in its geometric series. The J2 bound
and compact geometric domination justify integration. Subtracting
p_s(i*w) times the same integral gives exactly

    r_j^(far)=(-1)^j*[ integral_1^infinity p_s(x)/x^(2j+2)dx
                           -sum_(k=0)^j h_k/(2*(j-k)+1)].

For j>=1 this implies

    |r_j^(far)|<=J4+4*M/3.                                (11)

This retains the full subtraction term, including its constant;
no principal value, uncorrected resolvent or tail asymptotic is used.
It also proves locally normal convergence of the differentiated
series used next. The general entire and width-differentiability
statements are already supplied by C032m/n.

By the zero-normalized primitive,

    e_s(y)=-4*sum_(j>=0) (-1)^j*r_j*y^(2j+2)/(2j+2),
    e_s,yy(y)=-4*sum_(j>=0) (-1)^j*(2j+1)*r_j*y^(2j).

The j=0 term cancels in e_yy(b)-e_yy(a). Put Delta=b^2-a^2=3/64
and S(t)=sum_(j>=1) j*(2j+1)*t^(j-1)=(3+t)/(1-t)^3.
Using b^(2j)-a^(2j)<=j*Delta*b^(2j-2), (10)-(11) imply

    |e_yy(b)-e_yy(a)|
      <=4*Delta*[(M/12)*S(1/64)+(J4+4*M/3)*S(1/16)]
      <(7/10)*J4+2*M
      <7/2000+2/10^6 <1/280.                              (12)

For completeness, 4*Delta*S(1/16)=2352/3375<7/10;
the remaining coefficient of M in the preceding line is <2.

We also need a lower normalization for the final ratio. For
0<=y<=b, (10) bounds the near part of R_s(i*y) by M/2.
The far denominator obeys x^2-y^2>=(15/16)*x^2, hence

    |R_s(i*y)| <= M/2+(16/15)*(J2+M)<1/2.

Therefore

    |e_s(b)-e_s(a)| <=4*integral_a^b y*|R_s(i*y)|dy
                    <b^2-a^2=3/64.                       (13)

### 4. The signed first core

The simple first zero contributes exactly

    p0_s(x)=[G_s(x-r)+G_s(x+r)]/2=c_s*h_s(x),
    c_s=G_s(r),
    h_s(x)=exp(-x^2/(4*s))*cosh(r*x/(2*s)).

There is one such positive-ordinate member; neither its translates
nor conjugate off-line members receive an additional factor1/2.
Let I_y=integral_0^y h_s(x)dx, A0_s(y)=2*pi*c_s*I_y, and

    u=r*x/(2*s),
    q_s(x)=partial_s log h_s(x)
          =x^2/(4*s^2)-r*x*tanh(u)/(2*s^2).

On 0<=x<=b, 0<=u<=15/8. From exp(2u)>=1+2u follows
tanh(u)>=u/(1+u)>=8u/23. Consequently h_s is increasing,
h_s(0)=1, and

    q_s'(x)=x/(2*s^2)
             -r/(2*s^2)*[tanh(u)+u*sech(u)^2]
       <=x/(2*s^2)*[1-4*r^2/(23*s)]
       <=-(369/184)*x <=-2*x.                             (14)

To check the last uniform step, r^2>196, s<=2 imply that the
bracket is at most -369/23, and 1/(2*s^2)>=1/8. The negative
sign reverses the direction when that latter lower bound is used.

Let <v>_y denote the h_s-weighted mean on [0,y]. Since q_s+x^2
is decreasing, <q_s+x^2>_b<=<q_s+x^2>_a: the additional portion
[a,b] has no larger values than the first portion. Since h_s is
increasing, <x^2>_b>=b^2/3. Explicitly the double integral of
(x^2-t^2)*(h_s(x)-h_s(t)) over [0,b]^2 is nonnegative; expanding
it yields precisely this comparison with the uniform mean.
Also <x^2>_a<=a^2. Thus

    dot A0(b)/A0(b)-dot A0(a)/A0(a)
       =<q_s>_b-<q_s>_a
       <=-(b^2/3-a^2)=-1/192.                             (15)

The common c_s'/c_s cancels exactly. This is a signed bound, not
an estimate on the modulus of a Wronskian. We will also use
|dot A0(y)/A0(y)|<60: each real translated Gaussian has width
log derivative -1/(2*s)+(x+/-r)^2/(4*s^2), of absolute value
at most 1/2+(15+1/4)^2/4<60, and integration preserves the bound.

### 5. Relative errors for every remaining divisor member

For 0<=x<=b and any remaining member gamma>20, divide its exact
Gaussian modulus by the same positive c_s, before estimating width:

    |G_s(x+/-z_rho)|/c_s
      <=exp(1/16)*exp(-[(gamma-b)^2-225]/8).

Here the difference in square brackets is positive, so s<=2 gives
the displayed direction; r<15 and |delta|<1/2 were retained.
Direct width differentiation, rather than differentiating an error
estimate, gives

    |partial_s G_s(x+/-z_rho)|
       <=[(1/2)+((gamma+b)^2+1/4)/4]*|G_s(x+/-z_rho)|
       <=((gamma+1)^2/2)*|G_s(x+/-z_rho)|.

In shell [n,n+1) use (n+1)^2/6 members and gamma+1<=n+2.
The first exponential is exp(-[(20-1/4)^2-225]/8)<Q^20.
For both the profile and derivative majorants the successive ratio
is at most (23/21)^2*exp(-81/16)<(5/4)/16<1/8.
Summing every shell gives

    |p_s(x)-p0_s(x)| <=c_s*epsilon,
    |dot p_s(x)-dot p0_s(x)| <=c_s*eta,
    epsilon:=(16/15)*(8/7)*(441/6)*Q^20 <10^(-6),
    eta:=epsilon*(484/2)<10^(-4).                          (16)

The factor1/2 in each paired profile cancels the two equal modulus
bounds, including for every conjugate member. No high complex
center was replaced by a real one in an identity. C032m/n justify
the derivatives and integrals; these estimates also give an explicit
uniform summable majorant for the portions used here.

Because h_s>=1, A0_s(y)>=2*pi*c_s*y for y>0. Integrating (16),
and using the analogous bound for the width derivative, yields

    |A(y)-A0(y)|<=epsilon*A0(y),
    |dot A(y)-dot A0(y)|<=eta*A0(y),
    |dot A(y)/A(y)-dot A0(y)/A0(y)|
         <=(eta+60*epsilon)/(1-epsilon).                   (17)

In particular p_s(x)>=c_s*(1-epsilon)>0 on this real segment,
so A(b)>A(a)>0. By (9), A(b)<=2*pi*b*M<2*10^(-6)<10^(-5).
Both sine phases are therefore positive and increasing between
these arguments. Equations (15)-(17) imply

    dot A(b)/A(b)-dot A(a)/A(a) < -1/192+1/3000,
    |dot A(y)/A(y)|<61, y=a,b.                             (18)

Indeed 2*(10^(-4)+60*10^(-6))/(1-10^(-6))<1/3000.
This pays relative errors even though both A values are tiny.

### 6. Sine correction, normalization and the complete bound

For 0<v<10^(-5), the integral identity
sin v-v*cos v=integral_0^v t*sin t dt and sin v>=v/2 give
0<=1-v*cot v<=v^2. Thus replacing dot A/A by dot A*cot A
in the difference in (18) costs at most

    2*61*10^(-10)<10^(-6).                                (19)

Check C032n's evolution at the actual imaginary argument:
O_s(i*y)=i*A_s(y), dot A=2*pi*p_s'(y), and
dot e=e_yy+a_s, with a_s=E_s''(0). The latter follows from
dot E=-E''+a_s and e_yy=-E''(i*y). Therefore

    (g/f)'=(g/f)*B_s,
    B_s=dot A(b)*cot A(b)-dot A(a)*cot A(a)
                           -(e_yy(b)-e_yy(a)).

This verifies the signs in C032n(16)-(17); a_s cancels and has
not been omitted from either individual derivative. Combining
(12),(18),(19) proves the full, uniform signed bound

    B_s < -1/192+1/3000+1/10^6+1/280 < -1/1000.            (20)

By phase monotonicity and (13),

    g/f=exp(-e(b)+e(a))*sin(A(b))/sin(A(a))
        >=exp(-3/64)>1/2.

The last inequality follows, for example, from
exp(3/64)<=1/(1-3/64)=64/61<2. Multiplying the negative bound
(20) by this positive lower bound gives (1), with the direction
of the inequality retained. C032n's endpoint regularity includes
both width endpoints. Integrating (g/f)' on [s,t] and multiplying
by f(s)f(t)>0 gives (2), including arbitrarily close distinct widths.

### 7. Verification and limits

All transcendental comparisons were reduced above to elementary
inequalities and exact rational comparisons. Reproduce the latter:

    python3 scripts/signed_first_zero/check_margin.py

The complete rational certificate, with actual/required values and
pass/fail for every encoded check, is written to
`scripts/signed_first_zero/margin-1728.json`. The script checks the
arithmetic, not source correctness or the analytic proof. At attempt1728
the source applications and analytic exchanges still required critical
review; the subsequent bounded audit is recorded below.
There is no finite-zero replacement, width grid, computed RH claim,
erfc asymptotic, all-degree inference or new external theorem here.
The achieved upper bound -1/2000 passes the required threshold0
for this one minor only. No general sign-regularity or Chebyshev
application is inferred from a two-point result.

### 8. Conceptual audit1730, 19 November 2026

Verdict: (1)-(2) pass this independent audit of the local argument,
conditional on exactly the external inputs stated above. No numerical
constant, divisor assumption or conclusion has been strengthened.
Reuse the source evidence in source-working1726 and source-notes1721
under assessment1728/approval1729. In particular the first-two-zero
balls alone are insufficient: the FLINT consecutive-zero/completeness
contract and its historical low-index qualification are retained.
The fixed-v1 inputs and V(3*10^12) are not upgraded to source-wide
verification. The corrected inclusive count (3), rather than C032y's
older count or a primed endpoint convention, is the input to (4)-(5).

Here are the load-bearing analytic checks, beyond the rational replay.

* Count and tails: for t>=14, log log t<log t and
  0.11200+0.12567<1/4 justify the error bound used in (4).
  Integrating q*t^(-q-1) against the inclusive count from14 accounts
  for every ordinate; it yields exactly the two pre-simplification
  expressions in (5). The shell counts in (6), (9) and (16) are upper
  bounds on all multiplicities, not counts of just real centers.
  The first tail exponents are respectively 400/32>12,
  324/8>40 and 2641/128>20. Their successive majorants have the
  stated uniform ratios; thus every displayed tail includes the
  entire infinite remainder. For example the differentiated relative
  majorant has ratio at most ((n+3)/(n+1))^2*exp(-(2*n+1/2)/8),
  bounded by (23/21)^2*exp(-81/16) at n=20.
* Normalization and weighted integrals: the unique real first member
  contributes (G(x-r)+G(x+r))/2=G(r)*h(x). The two translated
  modulus bounds cancel this factor1/2; distinct conjugate members
  remain separate. In (8), the upper spatial portion contributes
  2^(q-1)*exp(1/16)*S_q, since the real Gaussian integral is1.
  Its lower and negative-center portions give exactly the c0 terms.
  Tonelli is applied to nonnegative majorants, not to p itself.
* Removable quotient and E: on the near interval the exact coefficient
  is (-1)^j*sum_(k>=j+1) h_k/(2*(k-1-j)+1). Cauchy's M/4^k bound
  gives (10) and absolute uniform convergence on every |w|<=r<1,
  including x=|Im w|. On the far interval the geometric expansion is
  dominated by (|p(x)|+C_r)/(x^2*(1-r^2)); (8) makes it integrable.
  The h_k convolution in (11) therefore cannot be discarded.
  For j>=1, x^(-2j-2)<=x^(-4). These bounds also make the resulting
  twice differentiated e series normally convergent at |y|<=1/4.
  Its constant second-derivative term j=0 cancels in the difference.
  The exact coefficients in (12) are 784/1125 for J4 and
  30586496/31255875 for M, respectively below7/10 and2.
* Signed core and relative errors: h is increasing because
  partial_x log h=-x/(2*s)+r*tanh(u)/(2*s) and the same
  tanh lower bound used in (14) makes this nonnegative. The uniform
  slope bound q'<=-369*x/184 implies q+x^2 is decreasing.
  Extending a weighted interval lowers the mean of that decreasing
  function, while the increasing h gives <x^2>_b>=b^2/3.
  These are signed comparisons and give (15), with c_s'/c_s canceled.
  In (16) the derivative of each Gaussian is bounded directly, before
  division by c_s; no derivative of an error inequality is taken.
  Hence (17) includes the required 60*epsilon term. The sum of the
  two logarithmic errors is bounded by 320/999999<1/3000.
* Width exchanges and signs: the portions of C032m/n used here were
  checked, including C032n(8)-(14), not its unrelated coefficient-span
  claims. On [1/2,3], all fixed Gaussian derivatives have a common
  polynomial-times-Gaussian majorant. Its weighted spatial integral
  is finite by sum gamma^(-2)<infinity. The h_sigma difference-quotient
  formula covers the removable locus for both the profile and width
  derivative. At spatial infinity the integration-by-parts boundary
  terms are O(log(x)/x) and O(log(x)/x^2), tending to zero; at zero
  evenness kills both terms. Thus dot E=-E''+4R(0), and substituting
  w=i*y gives dot e=e_yy+4R(0), with a plus sign. This constant
  cancels only after subtracting the two logarithmic derivatives.
  The neighborhood (1/2,3) includes both width endpoints of this test.

The sine correction follows from sin v>=v/2 and
integral_0^v t*sin(t)dt<=v^3/3, so the looser v^2 bound used in (19)
is valid. Reality follows from conjugation symmetry and evenness.
Equations (16)-(17) make both phases positive and ordered on [a,b];
(9) keeps them below10^(-5). Together with (13) this gives g/f>1/2.
The audited exact bracket is

    -1/192+1/3000+1/10^6+1/280 = -4559/3500000 < -1/1000.

Multiplication by g/f>1/2 preserves the strict upper conclusion
W/f^2<-1/2000 because the bracket is negative. Integration over each
[s,t] gives (2), including pairs arbitrarily near the diagonal; no
positive minimum separation or width grid is used.

Replayed `python3 scripts/signed_first_zero/check_margin.py`:23/23
exact rational comparisons passed, failures empty. Inspected complete
selected certificate values with the shared JSON inspector, including
the conclusion, T32, M, J4, both E coefficients, relative epsilon/eta
and logarithmic error. The original certificate's analytic_audit=PENDING
is attempt1728 provenance; this section supplies the analytic verdict.
The script does not verify FLINT, the count theorem or any preprint.
This audit establishes the local input for use, not a new theorem
beyond C033g, general annihilator exclusion, or an RH candidate.

## Mathlib

Full matching coverage is unchecked and unknown. No Mathlib result
is used as a substitute for the external zero computation, the cited
count, the full complex-divisor estimates or the signed conclusion.
Gaussian differentiation, Cauchy coefficient estimates and dominated
integration are supporting mathematics, not a matching formal theorem.
