# L494 — Frozen-cutoff reflection and Cauchy bound on the finite exterior band

## Hypotheses

Use the exact normalization of D. H. J. Polymath, *Effective approximation
of heat flow evolution of the Riemann xi function, and a new upper bound
for the de Bruijn–Newman constant*, Research in the Mathematical Sciences
**6** (2019), article 31,
[arXiv:1904.12438v2, 4 August 2019](https://arxiv.org/html/1904.12438v2),
equations (3)–(11) and Theorem 1.3. Thus

    H_t(w)=integral_0^infinity exp(t*v^2)*Phi(v)*cos(w*v) dv,
    Phi(v)=sum_(k>=1) (2*pi^2*k^4*exp(9v)-3*pi*k^2*exp(5v))
                          *exp(-pi*k^2*exp(4v)),
    M_0(s)=(sqrt(2*pi)/16)*s*(s-1)*pi^(-s/2)
                  *exp((s/2-1/2)*Log(s/2)-s/2),
    alpha(s)=1/(2s)+1/(s-1)+(1/2)*Log(s/(2*pi)),
    M_t(s)=exp(t*alpha(s)^2/4)*M_0(s).

Log is the principal branch; the prefactors are holomorphic and nonzero
on C minus (-infinity,1]. Theorem 1.3, including its explicit constants,
is imported. Its underlying Riemann–Siegel/saddle proof is not audited
here. The integral gives an entire H_t satisfying
H_t(conj(w))=conj(H_t(w)) for real t, as in the source introduction.

Let t,x be real, with the closed conditions

    .16836<=t<=.1718,  x>=6000284561421.5,
    t*log(x/(4*pi))<=5.17.

Put r=.14142 and freeze N=floor(sqrt(x/(4*pi)+t/16)). For any fixed
nonnegative integer k define, on a neighborhood of |w-x|<=r,

    u=(1-i*w)/2,  B(w)=M_t(u),  gamma(w)=M_t(1-u)/M_t(u),
    b_n=exp(t*log(n)^2/4),
    F_k(s)=sum_(1<=n<=k) b_n*exp(-(s+t*alpha(s)/2)*log(n)),
    f_k(w)=F_k(u)+gamma(w)*F_k(1-u),
    R_k(w)=H_t(w)/B(w)-f_k(w).

The derivative R_N' is the complex spatial derivative at fixed t,N.
All finite decimals in this lemma denote exact rational numbers.

## Conclusion

For every such centre and every fixed k the exact identity is

    R_k(conj(w))=conj(R_k(w))/conj(gamma(w)).                 (1)

There is a uniform upper-half-disk bound for the *local* index
k(w)=floor(sqrt(Re(w)/(4*pi)+t/16)):

    |R_(k(w))(w)| < E = 6*10^(-7)  (Im(w)>=0).              (2)

At most one cutoff transition meets the disk. Its unmollified entering
pair has a real-axis triangle bound P=1.3*10^(-6), and its growth on the
full disk is bounded by the single factor G=8.770232. Consequently

    |R_N(x)| < E,
    sup_(|w-x|<=r) |R_N(w)| < (E+P)*G,
    |R_N'(x)| < (E+P)*G/r < 1.18*10^(-4).                  (3)

More generally (3)'s first two bounds and its Cauchy bound hold with
any nonnegative E_global that uniformly bounds the local-index error
on the upper half disk, using non-strict inequalities where appropriate.
This validates the form (E_global+P)*G/r, including cutoff equality and
crossings in either direction. It does not validate a program's claimed
E_global unless that value has the stated uniform property.

This is a reproduction/specialization of Michel Planat,
*Collective Contraction in the de Bruijn–Newman Heat Flow: Off-Zero
Logarithmic Derivatives and Certified Barrier Refinements*,
[arXiv:2609.37164v2, 7 October 2026, Section 6.7, pp.26–28](https://arxiv.org/html/2609.37164v2),
specifically the subsection “Frozen cutoff, reflection and Cauchy's
derivative bound” after Lemma 6.10. It checks that analytic interface
with a standalone envelope; it imports no numerical ledger, phase
floor, coefficient reserve, separator hypothesis or global endpoint.
No collision exclusion or new conclusion about RH follows. The first
independent critical audit on 2026-10-30 accepted this local reduction
and its complete scalar certificate; Section 7 specifies the evidence
and retained source limitations. No constant or domain was enlarged.

## Proof

### 1. Elementary bounds and the meaning of the certificate

Write w=xi+i*y. Introduce the rational constants

    X=6*10^12,  t0=.16836,  t1=.1718,  l=26.89,
    U=5.17/t0+10^(-12),  delta=10^(-12).

Throughout the disk, xi>X, |y|<=r, and, writing L=log(xi/(4*pi)),

    l<L<U,  t*L<5.17+delta,
    690000<=k(w)<4700000,
    log k(w)<=L/2+delta,  log 4700000<15.37.                (4)

Here xi>=x-r>X and
|log(xi/x)|<=r/(x-r)<r/X<delta. The centre's t*log(x/(4*pi))<=5.17
and t<=t1<1 imply the upper log and tL bounds. The classical
Archimedean bounds 3<pi<22/7 and the rational exponential comparison
exp(l)<X/(4*(22/7)) prove the lower log bound. The lower index follows
from (690000)^2<X/(4*(22/7)). The upper follows from
exp(U)+t1/16<(4700000)^2. Finally

    log k(w)<=L/2+(1/2)*log(1+t/(16*exp(L)))
              <=L/2+t1/(32*exp(L))<L/2+delta.

All nontrivial scalar numerical comparisons used below are certified
by `scripts/heat/frozen-cutoff-cauchy-certificate.py`, with exact inputs
and rational bounds in `scripts/heat/frozen-cutoff-cauchy-certificate.json`.
Reproduction command from this notebook:

    python3 scripts/heat/frozen-cutoff-cauchy-certificate.py

The script uses Fraction arithmetic, not floating-point verification.
For a nonnegative rational argument a it sums exp(a) through degree
180, rounding each positive recurrence term outward on the 10^(-50)
rational grid. The remaining series is bounded by

    upper_term_180*(a/181)/(1-a/182).

All arguments are less than 182. The successive omitted term ratios
are at most a/182, proving the geometric tail bound. Lower sums omit
the positive tail. Negative arguments use reciprocals of the positive
enclosure, with outward rounding. The artifact records inputs, last
terms, sums, tails and endpoints, all 24 comparisons, and failures.
It checks scalar inequalities; the analytic reductions are proved here.

### 2. Holomorphy and exact reflection

The real parts of u and 1-u lie in [(1-r)/2,(1+r)/2], inside (0,1),
and their imaginary parts have magnitude xi/2>X/2. They avoid the
prefactor cut on a neighborhood of the closed disk. M_t is nonzero
there by its explicit formula; hence R_k is holomorphic for fixed k.
Principal Log commutes with conjugation off its cut, so alpha, M_t
and F_k commute with conjugation for real t. In particular

    u(conj(w))=1-conj(u(w)),
    gamma(conj(w))=1/conj(gamma(w)).

Thus f_k(conj(w))=conj(f_k(w))/conj(gamma(w)). The same transformation
holds for H_t/B: its denominator at conj(w) is conj(M_t(1-u(w))).
Subtracting proves (1). This identity always holds with one fixed
integer k; it does not assert holomorphy of the variable-index model.

### 3. A uniform upper-half-disk local error

For 0<=y<=r and xi>X, the exact hypotheses of Polymath Theorem 1.3
hold: 0<t<=1/2, xi>=200 and 0<=y<=1. Set k=k(w),

    s_*=u+(t/2)*alpha(u),
    kappa=(t/2)*(alpha(1-u)-alpha(conj(u))).

The theorem's second finite sum is F_k(1-u), since
conj(s_*)+kappa-y=1-u+(t/2)*alpha(1-u). Hence its f_t equals our f_k.
Its equations (20)–(24) give

    |gamma|<=exp(.02*y-y*L/2),
    Re(s_*)>=(1+y)/2+t*L/4
                   -t*(1-3*y+4*y*(1+y)/xi^2)_+/(2*xi^2),
    |kappa|<=t*y/(2*(xi-6)),
    e_A+e_B<=sum_(n<=k) (1+|gamma|*k^|kappa|*n^y)
       *b_n*n^(-Re(s_*))
       *[exp(((t^2/16)*(L-2*log n)^2+.626)/(xi-6.66))-1],
    e_C0<=exp(-(1+y)*L/4-t*L^2/16
        +1.24*(3^y+3^(-y))/(k-.125)
        +(3*sqrt(L^2+pi^2/4)+10.44)/(xi-12)),
    |R_k(w)|<=e_A+e_B+e_C0.                                (5)

We use Theorem 1.3(21)'s literal 4y(1+y), not a different version of
the real-part bound elsewhere in the source. On 0<=y<=r the positive
part in (5) is less than 2. Its total correction is less than
t1/X^2<10^(-24). Since .5+t0*l/4=1.6318001, this proves

    Re(s_*)>=1.6318+y/2.                                  (6)

After extracting b_n*n^(-1.6318), the two positive coefficient
multipliers in the Gaussian sum are bounded by

    n^(-y/2)<=1,
    |gamma|*k^|kappa|*n^(y/2)
       <=exp(y*(.02-L/2+(.5+t1/(2*(X-6)))*(L/2+delta)))
       <=exp(y*(.02-L/4+delta))<=1.                        (7)

The penultimate bound uses
delta/2+t1*(U/2+delta)/(2*(X-6))<delta; the last uses l>26.
It is (7), after extracting the y/2 power, that supplies the factor
two. No assertion that |gamma|*k^|kappa|*n^y<=1 is needed.

For every legal n, t*log(n)/4<=5.17/8+delta by (4) and t1<1.
Put a=1.6318-5.17/8-delta=.985549999999. Then

    sum_(n<=k) b_n*n^(-1.6318)<=sum_(n<=k) n^(-a)
       <=1+((4700000)^(1-a)-1)/(1-a)
       <1+(exp((1-a)*15.37)-1)/(1-a)<20.                  (8)

For the integral comparison a>0. Since
-2*delta<=L-2*log n<=L and L>2*delta, its absolute value is at most L.
Consequently, with

    d0=((5.17+delta)^2/16+.626)/(X-6.66),

the Gaussian factor is at most exp(d0)-1<=d0/(1-d0). Equations
(7),(8) give

    e_A+e_B<=40*d0/(1-d0)<1.6*10^(-11).                   (9)

For fixed xi,t,k, the logarithmic derivative in y of the right side
of (5)'s C-error envelope is

    -L/4+1.24*log(3)*(3^y-3^(-y))/(k-.125)<0.

Indeed log 3<2, 3^y-3^(-y)<3 and
1.24*6/(690000-.125)<l/4. Its maximum is therefore at y=0,
including endpoints. Also sqrt(L^2+pi^2/4)<U+1. It follows that

    e_C0<=exp(-l/4-t0*l^2/16+2.48/(690000-.125)
                +(3*(U+1)+10.44)/(X-12))
         <5.972*10^(-7).                                 (10)

The rational certificate bounds the sum in (9),(10) by
5.972100511*10^(-7), which is less than E=6*10^(-7). This proves (2)
for the full upper half disk, including points on cutoff lines. It
does not rely on any companion error producer or a real-centre-only
bound. The exact source theorem applies separately with each local k.

### 4. Reciprocal reflection growth

For s=A0 +/- i*xi/2 with (1-r)/2<=A0<=(1+r)/2, put

    c=3/X+(1+r)^2/(4*X^2),
    d=(t1*U/4+3.21)/(X-6),  A=U/2+d.

The explicit rational terms and |arg(s)|<pi/2 imply

    |Re(alpha(s))-L/2|<=c,
    |alpha(s)|<=L/2+pi/4+c,
    |alpha'(s)|<=1/xi+6/xi^2<1/(xi-6)<=1/(X-6).           (11)

For the first two bounds use
(1/2)*log(|s|/(xi/2))=(1/4)*log(1+4*A0^2/xi^2)
<=A0^2/xi^2 and |1/(2s)|+|1/(s-1)|<=3/xi. For the last,
differentiate the exact alpha to get
alpha'=-1/(2s^2)-1/(s-1)^2+1/(2s), and apply |s|,|s-1|>=xi/2.

Let q_t=M_t'/M_t=alpha+(t/2)*alpha*alpha'. By (11),

    |Re(q_t(s))-L/2|
       <=c+(t1/2)*(U/2+pi/4+c)/(X-6)<=d.                 (12)

The last comparison follows from
c*(X-6)+t1*(22/7)/8+t1*c/2<3.21, recorded in the certificate.
This also checks conjugate prefactors without extending an
upper-half-plane argument across a branch cut.

For fixed xi, differentiate vertically:

    d/dy log|gamma(xi+i*y)|
       =-(Re(q_t(1-u))+Re(q_t(u)))/2.

At y=0, |gamma|=1. Equation (12) bounds the absolute value of this
derivative by A, so for 0<=y<=r,

    1/|gamma(xi+i*y)|<=exp(y*A)<=exp(r*A)<8.770232=G.       (13)

All vertical segments used stay inside the disk when their endpoint
does: at fixed xi, their height is no greater than the endpoint's.
For y<0 use (1) with the *fixed integer* k(w). Since k(w) depends only
on xi, it is the same integer at conj(w). Thus (2),(13) yield

    |R_(k(w))(w)|<=E_global*G                             (14)

on the whole disk whenever E_global is an upper-half-disk local-error
bound. No holomorphy of this variable-index expression is being used.

### 5. The entering pair, including both cutoff directions

Transitions occur at a_m=4*pi*(m^2-t/16). Consecutive transitions
are separated by 4*pi*(2m+1)>12>2r for m>=1. Our disk meets at most
one. If k(w) differs from N, the difference is exactly one index m,
and |xi-a_m|<=2r. Equality at a transition uses floor(m)=m; one of
the two models may then agree exactly, otherwise the same one-index
description applies. This covers transitions to the left or right of
the centre, centres on a transition, and transitions at disk endpoints.
More explicitly, if N=m-1 and k(w)=m the difference f_(k(w))-f_N
is the entering pair; if N=m and k(w)=m-1 it is its negative.
At equality k(w)=m, so the same alternatives or zero apply.

Let h=log m and epsilon_h=h-L/2. Since

    |m^2-exp(L)|<=t1/16+2r/(4*pi)<t1/16+2r/12,

we have |m^2/exp(L)-1|<=eta, where
eta=(t1/16+2r/12)/(X/(4*(22/7)))<1. The inequality
|log(1+v)|<=|v|/(1-|v|) for real |v|<1 gives

    |epsilon_h|<=eta/(2*(1-eta))<delta.                   (15)

This estimate permits the entering index even when it is not legal
for the local sum on one side of the transition.

At the real point xi the moduli of its two chirality terms agree,
since |gamma(xi)|=1 and the exponents are conjugates. With
e_alpha=Re(alpha((1-i*xi)/2))-L/2, their individual log modulus is

    t*h^2/4-(.5+t*L/4+t*e_alpha/2)*h
      =-L/4-t*L^2/16-epsilon_h/2
                       +t*epsilon_h^2/4-t*e_alpha*h/2.

By (11),(15), the last three terms are bounded above by
delta/2+t1*delta^2/4+t1*c*(U/2+delta)/2<10^(-10). The real-axis
triangle size is therefore at most

    P0=2*exp(-l/4-t0*l^2/16+10^(-10))
       <1.194386*10^(-6)<P=1.3*10^(-6).                  (16)

The real comparison point xi need not itself satisfy the original
centre lower bound or t*log(xi/(4*pi))<=5.17. Only the enlarged disk
bounds xi>X, l<L<U and (15) are used in (16); they have already been
proved for every such xi. Thus no endpoint is lost by the vertical
comparison.

We need a full-disk bound, not merely (16). For the two nonzero
chirality terms

    T1(y)=b_m*exp(-h*(u+t*alpha(u)/2)),
    T2(y)=gamma(xi+i*y)*b_m
                         *exp(-h*(1-u+t*alpha(1-u)/2)),

their real logarithmic derivatives are exactly

    (log|T1|)'=-h/2*Re(1+(t/2)*alpha'(u)),
    (log|T2|)'=-(Re(q_t(u))+Re(q_t(1-u)))/2
                         +h/2*Re(1+(t/2)*alpha'(1-u)).

Since h=L/2+epsilon_h, equations (11),(12),(15) bound the absolute
value of each by

    U/4+delta/2+d+t1*(U/2+delta)/(4*(X-6))<A.              (17)

For T2 the leading terms combine as -L/2+h/2=-L/4+epsilon_h/2;
bounding them separately before combining would lose this estimate.
Integrating (17) from zero to any positive or negative y, and then
adding the two moduli, proves

    |T1(y)+T2(y)|<=P0*exp(|y|*A)<P*G.                    (18)

This is an estimate directly on both faces of the disk. We do not
reflect an upper-face jump that has already incurred G. The actual
signed difference f_(k(w))-f_N is either zero or plus/minus this
entering pair, so (18) covers every cutoff case.

### 6. Cauchy's estimate and scope

The identity

    R_N(w)=R_(k(w))(w)+f_(k(w))(w)-f_N(w)

and (14),(18) give |R_N(w)|<=(E_global+P)*G throughout the disk.
At w=x the indices coincide, hence |R_N(x)|<=E_global. R_N itself
is holomorphic on a neighborhood of the closed disk by Section 2,
regardless of the jumps in the pointwise comparison. Cauchy's integral
formula, with this fixed N, therefore gives

    |R_N'(x)|<=(E_global+P)*G/r.

Taking E_global=E and using the strict verified bounds proves (3):
the rational expression (1.9*10^(-6))*8.770232/.14142 is less than
0.000117829449866, hence less than 1.18*10^(-4).

Only this true-function error interface has been checked. In particular
the coefficient majorant, positive mollified phase denominator and
strict reserve required to apply Planat Lemma 6.10 are not established.
Even a successful local application would leave interior collisions,
other times and zero-time control unresolved. L491 was consulted only
for overlap of exact prefactor formulas: its much larger-height
conclusion is not an input to this argument. No RH, separator
nonvanishing or global real-zero assumption was used.

### 7. First independent critical audit (2026-10-30)

The audit checked Sections 1–6 against the cited primary Theorem 1.3,
equations (5)–(24) and its fixed-cutoff warning, and against Planat
Section 6.7's fixed-cutoff subsection. The normalization in Section 3,
upper-face y/2 extraction, fixed-index reflection, signed cutoff cases
and full-disk two-chirality derivatives survive. In particular (17)
uses the combined leading terms for T2 before taking absolute values;
(18) bounds the jump on the lower face directly. Applying reflection
only to the local error, followed by Cauchy only for the fixed R_N,
justifies the single factor G in (3). No additional premise is needed.

The independent consumer

    python3 scripts/heat/l494-certificate-audit.py

reads the complete original JSON certificate and checks every stored
scalar comparison. For each of its seven exponentials it computes
unrounded rational Taylor terms through degree 220. With a the
absolute argument, the positive tail is at most

    term_220*(a/221)/(1-a/222).

The term ratios after the first omitted term are at most a/222<1.
For a negative argument it inverts the positive endpoints. Outward
rounding to the 10^(-70) grid gives a rigorous independent enclosure
contained in the stored enclosure. It also checks the stored degree-180
sums, final terms, tails and signed endpoint construction against exact
unrounded values, and replays the producer byte for byte. The complete
audit certificate is `scripts/heat/l494-certificate-audit.json`.

All 78 consumer checks passed, including the original 24 comparisons,
with no failures. The certified upper values include
E_actual<5.972100511*10^(-7), G_actual<8.770231039995,
P0<1.194385188495*10^(-6), and the charged derivative bound
<0.000117829449866. These are below the required E, G, P and
0.000118 respectively. This verifies existing constants, not an
improved collision bound or progress beyond the checked sources.
The imported saddle proof, numerical coefficient/phase producers,
Planat's true-double-zero application and global assembly are outside
this audit. No new lemma input or DAG edge was introduced.

## Mathlib

Full matching coverage was not checked and is unknown. This proof
uses the standard Cauchy integral derivative estimate, conjugation of
holomorphic finite sums, real integral comparison and elementary
logarithm/exponential inequalities. No particular Mathlib theorem is
claimed to formalize the imported Polymath approximation or this
explicit cutoff/reflection interface. The rational certificate is not
a formalization of the analytic proof.
