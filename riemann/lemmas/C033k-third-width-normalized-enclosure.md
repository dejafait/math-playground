# Corollary C033k: inconclusive normalized third-width enclosure

## Hypotheses

Retain exactly C032j/m/n and C033g's full actual positive-ordinate
divisor, counted with multiplicity and conjugation. In particular
z_rho=gamma_rho-i*delta_rho, gamma_rho>14, |delta_rho|<1/2. There
is one simple real first center r in (14,15); every other ordinate
exceeds20. Retain the qualified external first-zero computation,
the corrected inclusive Bellotti--Wong v2 count, fixed-v1 inputs and
V(3*10^12). No external computation or preprint is reverified here.

Use Gaussian half-variance s, G_s(z)=exp(-z^2/(4s))/sqrt(4*pi*s),
p_s(z)=(1/2)sum_rho[G_s(z-z_rho)+G_s(z+z_rho)], and

    R_s(w)=integral_0^infinity (p_s(x)-p_s(i*w))/(x^2+w^2) dx,
    E_s(w)=4*integral_0^w u*R_s(u) du,
    e_s(y)=E_s(i*y), A_s(y)=2*pi*integral_0^y p_s(x) dx,
    k_s(y)=exp(-e_s(y))*sin(A_s(y)).

Removable quotient values and zero-normalized primitives are included.
Set a=1/8, b=3/16, c=1/4, f(s)=k_s(a), r_2(s)=k_s(b)/f(s),
r_3(s)=k_s(c)/f(s), for 1<=s<=2. These are real functions. The
positivity arguments of C033g apply to every y in [a,c], so f and
both other test values are strictly positive. RH is not assumed.

## Conclusion

The functions above are C^2 in width on a neighborhood of [1,2],
with the mixed complex derivatives and spatial-integral exchanges
specified below. On distinct ordered widths put

    Delta_3(s1,s2,s3)
      =det[(1,r_2(si),r_3(si))_(i=1,2,3)]
                       /[(s2-s1)*(s3-s1)*(s3-s2)].          (1)

It extends continuously to 1<=s1<=s2<=s3<=2. The single rational
interval calculation specified below proves the qualified enclosure

    -3 <= Delta_3 <= 3                                    (2)

on this entire closed simplex, including both kinds of double
collision, the triple collision and the endpoints. The intended
strict sign has NOT been established. Both the signed first-core
Wronskian enclosure and the full-divisor enclosure contain zero.
This is not a counterexample or a rigorous actual zero of Delta_3.

Attempt1746 is EXPLORATION and is parked without refining the cover.
No Chebyshev exclusion, variation bound, unrestricted odd cancellation,
output positivity, moment or actual-Xi realization claim follows.
The new analytic/computational write-up has not had an independent
critical audit; its arithmetic certificate alone is not such an audit.

## Proof

### 1. Coverage, imports and second width regularity

Assessment1745 predates this attempt and covers this exact test.
Source-notes1745 screens the local duplicates and stops1711/1725,
and distinguishes Sra's fixed-kernel Hankel positivity from width
positivity. C033g's proof and audit1730 supply the already justified
first-order bounds; none is differentiated as an inequality.

The general integration input is Haslinger, *Complex Analysis*,
Section2.7, [Theorem2.39, pp67-68](https://www.mat.univie.ac.at/~has/scriptneu.pdf),
under the measurable-section, holomorphic-section and compact
integrable-majorant hypotheses checked here. The heat identity and
its normalized E evolution are used from C032n, not reproved. The
full-divisor and low-zero inputs are those precisely cited in C033g:
Bellotti--Wong [arXiv:2412.15470v2](https://arxiv.org/pdf/2412.15470v2),
Theorem1.1/Section5, pp1,23-24; the qualified
[FLINT consecutive-zero contract/example](https://flintlib.org/doc/acb_dirichlet/zeta-zeros.html)
and fixed commit1d432c3bba36d1a29f6453ebfaa00e43f58c278f's low-index
implementation and historical first126 Gram-law input. Their exact
applicability and source limitations in C033g remain unchanged.

Here is the needed extension beyond C032n's C^1 assertion. For
s in I=[1/2,3], each a=0,1,2 and each fixed k>=0,
partial_s^a partial_z^k G_s(z)=P_(a,k,s)(z)G_s(z), where P is a
polynomial with coefficients bounded on I. Indeed a z derivative
replaces P by P'-zP/(2s); a width derivative replaces it by
partial_s P+(-1/(2s)+z^2/(4s^2))P. This proves the assertion also
for a=2 by induction. For |Im z|<=Y, absorbing any fixed polynomial
into half of the Gaussian gives

    |partial_s^a partial_z^k G_s(u+i*v)|
        <=C_(a,k,Y) exp(-u^2/24).                          (3)

The constants are finite and independent of s. The displacement
|delta|<1/2 merely replaces Y by Y+1/2. On each complex disk
the resulting majorant is a constant times
sum_rho exp(-(gamma_rho-M)_+^2/24), finite by the inclusive zero
count. The Gaussian series through width order2, and every fixed
complex derivative of it, thus converge uniformly on compact disks.
Apply the fundamental theorem of calculus to each term, then the
same summable bound to its averaged derivative, twice. This justifies
C^2 width dependence and joint continuity, without differentiating
an estimate. The open interior (1/2,3) contains both width endpoints.

For the noncompact spatial integral use

    P(x)=sum_rho[exp(-(x-gamma_rho)^2/24)
                    +exp(-(x+gamma_rho)^2/24)].

All width orders0,1,2 and fixed complex derivatives are bounded
by constants times P(x) on the real axis. For X>=1, splitting at
x=gamma/2, as in C032n(9), gives the complete majorant

    integral_X^infinity P(x)/x^2 dx
      <=(2/X)sum exp(-gamma^2/96)
                    +4*sqrt(24*pi)sum gamma^(-2)<infinity. (4)

Write p_s(z)=h_s(z^2). Cauchy's coefficient formula on a larger
z disk, with (3), gives joint C^2 width dependence of h_s and all
its complex derivatives, uniformly on compact disks. The exact
removable quotient is

    (p_s(x)-p_s(i*w))/(x^2+w^2)
      =integral_0^1 h_s'(-(1-v)*w^2+v*x^2) dv.             (5)

Its first and second width derivatives have the same expression
with partial_s h_s and partial_s^2 h_s. For |w|<=M and
0<=x<=X=2M+1, compact bounds on these functions dominate all three
integrands by one constant. For x>=X, |x^2+w^2|>=3x^2/4 gives a
bound D_M(P(x)+A_M)/x^2. Equations (4)-(5) provide an integrable
common majorant, including w=+/-i*x and the origin. Dominated
difference quotients and the cited integration theorem prove the
claimed C^2 and entire dependence for R. Compact segment integration
then proves it for E and A; Cauchy's formula permits the fixed mixed
complex derivatives. Products, sine and division by positive f
prove the assertions for the two ratios.

In particular C032n's exact identity partial_s e=e_yy+a_s may
now be differentiated again with its mixed derivatives. For
d_y(s)=e_s(y)-e_s(a), constants cancel only after subtraction:

    d_y'=e_yy(y)-e_yy(a),
    d_y''=e_yyyy(y)-e_yyyy(a).                            (6)

No origin or primitive constant is silently dropped.

### 2. Relative divisor errors through inverse-width order2

Put t=1/s, v=r^2, c_s=G_s(r), and

    h(t,x)=exp(-t*x^2/4)cosh(r*t*x/2),
    J_y(t)=y^(-1)integral_0^y h(t,x)dx,
    H_y(t)=A_s(y)/(2*pi*c_s*y).

The domain is t in [1/2,1], v in [196,225]. C033g's increasing
first-core argument gives h>=1 on 0<=x<=c. Define

    Q=3/8, epsilon=(16/15)*(8/7)*(441/6)*Q^20,
    C20=4433/64, epsilon_k=epsilon*C20^k, k=0,1,2.

For every fixed y in [a,c], differentiating the exact normalized
Gaussian, before any estimate, yields

    |partial_t^k(H_y-J_y)|<=epsilon_k.                     (7)

To verify the full tail, a translated Gaussian divided by c_s is
exp(-t*B), where B=((x+/-z_rho)^2-r^2)/4. Its kth t derivative
is (-B)^k exp(-tB), without a prefactor derivative. For a remaining
member gamma>20 and 0<=x<=1/4,

    |exp(-tB)|<=exp(1/16)*exp(-[(gamma-1/4)^2-225]/8),
    |B|<=[(gamma+3/4)^2-196]/4.

The latter uses (gamma-x)^2-r^2>0, |delta|<1/2 and the triangle
inequality on the real and imaginary parts of the square. In the
shell [n,n+1), C033g's inclusive count bounds multiplicity by
(n+1)^2/6 and |B| by C_n=[(n+7/4)^2-196]/4. Its first exponential
is less than Q^20. Since

    C_(n+1)/C_n
      =(1+1/(n-49/4))*(1+1/(n+63/4))
      <=(35/31)*(147/143),

the ratio of successive majorants, for any k<=2, is at most

    (22/21)^2*((35/31)*(147/143))^2/16
      =60025/649636 <1/8.

Here the Gaussian exponent increment is at least81/16>3 and
exp(3)>16. Summing all shells gives (7), using exp(1/16)<=16/15.
The paired profile's factor1/2 cancels the two translate bounds;
conjugate divisor members and multiplicities remain separate.
Integration divided by y preserves these bounds. In particular

    epsilon_0<10^-6, epsilon_1<10^-4, epsilon_2<2/1000,
    epsilon_2=479643537111361623/368934881474191032320,
    H_y>=1-epsilon_0>0.                                  (8)

Thus the common tiny Gaussian was removed before the second-order
comparison. No derivative of C033g's first-order error is used.

### 3. The full E correction through order2

Use the exact C033g bounds

    M=3*(Q^18+504*Q^40),
    J4_bound=(16/45)*(101/100)/(6*250)
                              +(128/15)*40/(27*14^3).

Here |p_s(z)|<=M on |z|<=2, and the second expression bounds
integral_1^infinity |p_s(x)|/x^4 dx. One further moment is needed.
From C033g's N(u)<u log(u)/3 for u>=14, Tonelli gives

    sum gamma^-6 <=2*14^-5*(log(14)/5+1/25)
                       <32/(25*14^5).

The same positive-center split at gamma/2, retaining the negative
center and its Gaussian tail, gives

    integral_1^infinity |p_s(x)|/x^6 dx <=J6_bound,
    J6_bound=(16/45)*(101/100)/(10*250)
                            +(512/15)*32/(25*14^5)<1/4000. (9)

For clarity, the general bound used here is
c0*(T32+T8)/(2(q-1))+2^(q-1)*exp(1/16)*sum gamma^-q,
with c0<16/45, T32<1/250 and T8<T32/100 from C033g. It follows
by integrating the lower and negative-center Gaussian bounds against
x^-q, and using x^-q<=2^q/gamma^q on the upper portion. Thus (9)
does not assume real remaining centers or delete any spatial tail.

Write p_s(z)=sum h_k z^(2k), R_s(w)=sum r_j w^(2j).
C033g's exact removable-division and far-geometric expansions give

    |r_j^(near)|<=M/(3*4^j),
    |r_j^(far)|<=J4_bound+4M/3, j>=1,
    |r_j^(far)|<=J6_bound+4M/3, j>=2.                      (10)

The last inequality follows from the same exact coefficient
(-1)^j[integral_1^infinity p(x)x^(-2j-2)dx
 -sum_(k=0)^j h_k/(2(j-k)+1)]; j>=2 permits x^-6. The subtraction
and the removable part are retained. The coefficients also give
normally convergent differentiated series on |y|<=1/4.

Set Delta_y=y^2-a^2 and define the positive rational functions

    S2(z)=(3+z)/(1-z)^3,
    S4(z)=8z(1+11z+11z^2+z^3)/(1-z)^5
             +56z(1+4z+z^2)/(1-z)^4
             +142z(1+z)/(1-z)^3+154z/(1-z)^2+60/(1-z).

The latter sums (n+1)(2n+3)(2n+4)(2n+5)z^n for n>=0;
expand that polynomial as 8n^4+56n^3+142n^2+154n+60 and differentiate
the geometric series. Equation (10) and the zero-normalized E series
give, for a<=y<=c,

    |d_y|<=Delta_y,
    |d_y'|<=D2(y)
      :=4Delta_y[(M/12)S2(y^2/4)+(J4_bound+4M/3)S2(y^2)],
    |d_y''|<=D4(y)
      :=4Delta_y[(M/48)S4(y^2/4)+(J6_bound+4M/3)S4(y^2)]. (11)

The first line uses C033g's |R_s(i*y)|<1/2 and its integral
formula for e. For the second line the constant j=0 cancels in
e_yy(y)-e_yy(a). For the third, the constant j=1 cancels in
e_yyyy(y)-e_yyyy(a), leaving coefficients
4(2j+1)(2j)(2j-1)|r_j| and the difference of powers
y^(2j-2)-a^(2j-2)<=Delta_y*(j-1)y^(2j-4), j>=2.
This proves both displayed series bounds, including the factors12
and48. In inverse width they imply

    |partial_t d_y|<=D2(y)/t^2,
    |partial_t^2 d_y|<=D4(y)/t^4+2D2(y)/t^3.              (12)

### 4. Explicit core and sine enclosures

The fixed certificate uses 16 equal t intervals covering [1/2,1]
and 16 equal v intervals covering [196,225]. No smaller cover is
tried after its outcome. Each rectangle encloses a continuum, not
a set of sampled values. Arithmetic uses exact rational endpoints.

For N=20 define

    m_n(y,v)=(-1)^n sum_(j=0)^floor(n/2)
       binom(n,2j) v^j y^(2n-2j)/[4^(n-j)*(2n-2j+1)].

For k=0,1,2 use the polynomial and error

    partial_t^k J_y(t)
       in sum_(n=k)^N m_n(y,v)*t^(n-k)/(n-k)! + [-T_k,T_k],
    T_k=9*2^(N+1)/(N+1-k)!.                              (13)

This is the integrated exponential Taylor series, not a numerical
quadrature. In fact h=(exp(t*alpha_+)+exp(t*alpha_-))/2 with
alpha_+/-=-x^2/4+/-r*x/2. Expanding their nth powers and cancelling
odd r powers gives m_n exactly. Since |alpha_+/-|<=121/64<2,
the Taylor remainder after differentiating k times is bounded by
exp(2)*2^(N+1)/(N+1-k)!; exp(2)<9. Integration divided by y proves
(13), simultaneously for every point in each rectangle. The interval
for J_y is intersected with [1,9], justified by h>=1 and h<=exp(2).
Add the errors (7) to obtain full H_y jets, intersecting H_y's lower
bound with 1-epsilon_0. No denominator can meet zero.

Keep the small sine term explicitly. C033g's compact profile bound
gives 0<A_s(y)<10^-5 for these three y. With c_s=sqrt(t/(4pi))
exp(-r^2*t/4), |c_t/c|<57 and |c_tt/c|<57^2+2. The same
exponential representation gives |J_t|<=18, |J_tt|<=36. Equations
(7)-(8) therefore give |H_t/H|<19, |H_tt/H|<37, and

    |A_t/A|<80, |A_tt/A|<5500.

For 0<u<10^-5 set phi(u)=log(sin(u)/u). The elementary integral
sin(u)-u*cos(u)=integral_0^u x*sin(x)dx, together with sin(u)>=u/2,
gives |phi'(u)|<=u. Also
|phi''(u)|=(u^2-sin(u)^2)/(u^2*sin(u)^2)<=4/3<2:
use u-sin(u)<=u^3/6 and sin(u)>=u/2. Thus differences between
the two log-sinc terms have first t derivative at most16/10^9,
and second t derivative at most
2*(2*80^2+5500)/10^10<4/10^6. Their undifferentiated ratio belongs
to [1-10^-10,1/(1-10^-10)]. These bounds are used separately;
the sine correction is never set to zero.

For y=b,c form the exact ratio r_y=k_s(y)/k_s(a) and denote
B_y=partial_t log r_y, C_y=partial_t^2 log r_y. On each rectangle,
the certificate encloses them by the identities

    r_y=(y/a)*(H_y/H_a)*exp(-d_y)*sinc(A_y)/sinc(A_a),
    B_y=H_y'/H_y-H_a'/H_a-partial_t d_y
                                  +partial_t(phi(A_y)-phi(A_a)),
    C_y=H_y''/H_y-(H_y'/H_y)^2-H_a''/H_a+(H_a'/H_a)^2
                     -partial_t^2 d_y
                                  +partial_t^2(phi(A_y)-phi(A_a)). (14)

Here primes on H denote t derivatives. For exp(-d_y), (11) allows
the rational interval [1-Delta_y,1/(1-Delta_y)]. Equations (7),
(11)-(14) enclose the complete divisor, normalization and corrections.

The signed differential test is calculated, not assumed:

    W_t=r_2'*r_3''-r_3'*r_2''
       =r_2*r_3[B_b*C_c-B_c*C_b+B_b*B_c*(B_c-B_b)].        (15)

The script also evaluates the first-core version of (15), using J
without tail/E/sine corrections. Both aggregate enclosures contain
zero. Therefore the first-core interval calculation itself fails to
pay a strict sign; blaming only the added corrections would be wrong.
The s-coordinate identities are
r_s'=-t^2 r_t', r_s''=t^4 r_tt''+2t^3 r_t', W_s=-t^6 W_t.
For r_3' only, intersect its enclosure with C033g's already audited
upper bound -1/2000. No analogous r_2 sign or higher Wronskian is
assumed.

### 5. Normalized determinant and every collision

Import the C^2 divided-difference extension and Genocchi--Hermite
formula from Carl de Boor, *Divided Differences*, Surveys in
Approximation Theory1 (2005),46-69,
[Proposition35/Definition37, pp58-59, formula(52), pp63-64](https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf).
The k=2 simplex has volume1/2. No general ECT theorem is needed,
since its nonvanishing premise was not established here.

For distinct s1<s2<s3, subtract the first row from the second
and third in (1), then form their Newton divided differences.
The first column becomes (1,0,0); the row scaling determinant is
exactly the width Vandermonde. This gives the specialization for
two general ratio columns, rather than applying de Boor's
polynomial-column determinant formula outside its scope:

    Delta_3=r_2[s1,s2]*r_3[s1,s2,s3]
                          -r_3[s1,s2]*r_2[s1,s2,s3].      (16)

If global intervals U_j and V_j enclose r_j' and r_j'', respectively,
the cited integral formula gives

    Delta_3 in (U_2*V_3-U_3*V_2)/2.                       (17)

It applies also to repeated sites because the ratios are C^2 on
a neighborhood of the full interval. Explicitly, at (s,s,t) the
first divided differences become r_j'(s) and the second ones are
[r_j(t)-r_j(s)-(t-s)r_j'(s)]/(t-s)^2. At (s,t,t) the first ones
are [r_j(t)-r_j(s)]/(t-s) and the second ones are
[r_j(s)-r_j(t)+(t-s)r_j'(t)]/(t-s)^2. At (s,s,s), (16) equals
[r_2'(s)r_3''(s)-r_3'(s)r_2''(s)]/2. The Hermite integral formula
ensures these are the continuous joint limits even when all gaps
tend to zero at different rates. Widths1 and2 cause no issue by
the neighborhood regularity already proved. Thus an automatic raw
determinant zero at a collision has not been mistaken for a test.

### 6. Exact certificate, outcome and qualifications

Reproduce the one fixed enclosure with

    python3 scripts/signed_first_zero/third_width_1746.py

The full exact certificate is `scripts/signed_first_zero/third-width-1746.json`.
It records every parameter rectangle, its first-core and full
Wronskian interval, all complete global derivative hulls, the exact
interval (17), constants and actual/required side bounds. The ten
rational side checks pass. The exact interval (17) is contained in
[-3,3] and contains zero, establishing (2) with no strict margin.
Its first-core W_t enclosure has decimal preview
[-0.451668350732,1.06976278594]; the full one has preview
[-0.546603470026,1.21364797905]. These decimals are explanatory
previews, not the certificate endpoints or a sign-change proof.

All 256 exact rectangles were checked for coverage of the two
parameter intervals; their three Wronskian hulls match the stored
global hulls. The exact rational determinant interval was checked
to lie in [-3,3] and to contain zero. The complete rational side
checks and the integer enclosure were inspected with the shared
JSON inspector. This validates the recorded arithmetic and coverage,
not the analytic argument, external zero verification or source-wide
correctness. No finite divisor truncation or floating-point sign
claim enters the result.

WHY THE ATTEMPT DOES NOT CLOSE ITS TARGET: separate interval
enclosures of the two ratio jets lose the correlation in (15),
already for the first core; (17) additionally decouples slopes and
curvatures. The full second-order divisor and E errors are paid
only as bounds and cannot supply the missing signed correlation.
The enclosing interval therefore gives neither orientation with
a positive margin. Its failure does not prove that a sharper
signed method is impossible. This particular bounded attempt is
parked; no refinement or extra grid was performed. The main
actual-Xi all-degree gap remains entirely unresolved.

## Mathlib

Full matching coverage is unchecked and unknown. No Mathlib result
is used to replace the external zero/count inputs, relative-error
proof, divided-difference specialization or exact interval program.
Gaussian differentiation, dominated integration and interpolation
are supporting mathematics, not a matching formal theorem.
