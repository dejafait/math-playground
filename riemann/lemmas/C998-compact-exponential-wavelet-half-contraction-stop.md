# C998: A rejecting pair for the fixed compact exponential-wavelet half estimate

## Hypotheses

Use L744(6)'s complete Weil form Q, Fourier convention
F_f(t)=integral f(x)exp(-itx)dx, and measure dt/(2*pi).
Its Hermitian polarization H is linear in its first argument.
Set L=4log(3), I=(0,L), T_0=log(3)/16, T_1=T_0/2.
Use the compact, causal exponential-spline construction with physical
roots (-1/2,-1/2,1/2,1/2), no zeros, free filter1 and source origin0.
For each T retain every lattice-2T translate with closed support in I;
U_j is its full complex span. No RH hypothesis or positivity on this
window is assumed.

Construction input: Khalidov–Unser, *From Differential Equations to the
Construction of New Wavelet-Like Bases*, IEEE TSP54(4),1256–1267(2006),
DOI10.1109/TSP.2006.870544,
[published author PDF](https://bigwww.epfl.ch/publications/khalidov0601.pdf),
III.A/IV.A–B/V.A–B, pp1259–1262, (3)–(9), Proposition2 and Property2.
Use its compact filter G=-z H_i^*(-z^-1) A_i(-z), not its dual branch.
The repeated real-root scaling-function Riesz/reproduction inputs are
Unser–Blu, *Cardinal Exponential Splines: Part I—Theory and Filtering
Algorithms*, IEEE TSP53(4),1425–1438(2005), III.C, Theorem1 and
III.C2/Proposition2, pp1430–1432,
[author PDF](https://bigwww.epfl.ch/publications/unser0503.pdf).
These source statements and essential real-root proof cases were
assessed before this calculation in assessment855, approved856.

Also use Plancherel, supported Sobolev mollification, Cauchy's derivative
estimate (Cauchy's integral formula; Purdue MA425/525, Fall2026,
[Lecture7, Theorem9](https://www.math.purdue.edu/~qi117/MA425_Fall26/webs/lecture7_accessible.html)),
and the real Gauss quadrature remainder in
[NIST DLMF3.5(v), (3.5.18)–(3.5.21)](https://dlmf.nist.gov/3.5#v),
specialized to Legendre weight1 on[-1,1].
The only digamma remainder used is the first-order DLMF5.11.2/5.11(ii)
bound already imported and specialized in L744(8). No source numerical
certificate, Schur sign theorem or new wavelet-basis theorem is asserted.

## Conclusion

The prescribed spaces have dimensions24 and56. There are explicit real
u in U_0 and v in U_1 with

    0.04111 < Q(u) < 0.04516,
    10.3564 < Q(v) < 10.3967,
    0.66574 < H(u,v) < 0.66825,
    |H(u,v)| / sqrt(Q(u)Q(v)) > 0.97 > 1/2.

Thus positive definiteness of both metrics together with strict
half-contraction on the full spaces cannot hold. The pair alone rejects
the universal half estimate; this does not require proving either full
metric positive. If both are positive, their beta is greater than0.97.
Full metric positivity is not certified here. In particular no negative
Q value, failure of Weil positivity, or RH conclusion follows.

This is a REPRODUCTION/specialization of known construction and scalar
verification machinery, not a claimed discovery beyond checked sources.
The separate conceptual audit859 below accepts this fixed stop after
checking the analytic reduction, complete replay and exact rational
verification. It supplies no stronger estimate or full-metric sign.

## Proof

### 1. The specified source specialization

Put a=T/2. In the coordinate y=x/T define

    b_a = (exp(-ay)1_[0,1]) * (exp(-ay)1_[0,1])
          * (exp(ay)1_[0,1]) * (exp(ay)1_[0,1]).

This is positive inside(0,4), has closed support[0,4], is symmetric
about2, and is C2 and piecewise exponential-polynomial. Define

    R_k = integral b_a(y)b_a(y-k)dy,   A_k=R_k/R_0,
    A(z)=sum_(k=-3)^3 A_|k| z^(-k),
    Hraw(z)=product_(alpha=-1/2,-1/2,1/2,1/2)(1+exp(T alpha)z^-1),
    Graw(z)=-z Hraw(-z^-1) A(-z)=sum_k g_k z^-k,
    psi_T(x)=sum_k g_k b_a(x/T-k).

This raw generator differs from the prescribed source-normalized
generator only by a positive scalar: the normalized scaling function
is b_a(x/T)/sqrt(T R_0), and the source H_i has a positive constant
prefactor multiplying Hraw. Consequently the finite spaces, supports
and cross ratio are identical. This explicit scalar simplification
avoids computing an irrelevant normalization; it changes no origin.
To match the source's unit dyadic ladder, first set q=x/T_0 and roots
alpha'=T_0 alpha, and use source spacings1 and1/2. Returning to x gives
exactly these T-dependent factors, rather than fixed-wavelet dilates.
All roots are real and repeated roots are permitted; free filter1 is
bounded and nonvanishing. The cited Riesz theorem applies.

Graw has extreme indices-8 and2. Both extreme coefficients are A_3>0,
since the extreme Hraw coefficients equal1. On each outermost nonzero
piece only the extreme spline contributes. Thus psi_T has precisely
closed support[-8T,6T], and psi_T(.-2rT) has support
[(2r-8)T,(2r+6)T]. Strict interior selection gives r=5,...,28 at T_0
and r=5,...,60 at T_1. Finite subsets of the cited Riesz sequences are
independent, proving the dimensions and completeness of this selection.

For z=Tt, direct Fourier transformation of the four compact factors gives

    F_bphysical(t)=4T exp(-2iz)(cosh(a)-cos(z))^2/(a^2+z^2)^2,
    F_psi(t)=-16T exp(iz)(cosh(a)-cos(z))^4
             * Aalt(z)/(a^2+z^2)^2,
    Aalt(z)=A_0-2A_1 cos(z)+2A_2 cos(2z)-2A_3 cos(3z).       (1)

The apparent singularities at z=±ia are removable. The numerator in
the second formula has a zero of order4 and the denominator order2
there, so F_psi has zeros of at least order2 at t=±i/2. Translation
preserves these zeros. In particular both exponential pole moments
vanish exactly for every vector in both spaces. This also checks the
source Property2 specialization directly, without selecting a dual or
adding moment corrections.

All these zero extensions belong to H2(R), with support strictly inside
I. Mollification within that support approximates them in H2 by smooth
compact tests. L744(8)'s logarithmic symbol bound makes the Fourier
quadratic form continuous under this approximation. Every delay is
bounded on L2; the two finite-interval exponential moment functionals
are continuous on L2. Hence L744(6), and its polarization, pass to
these functions. No closed-domain or positivity assertion of L741 is
extended to this longer interval.

### 2. Exact pair and complete signed integrals

Write c=(c_first,reverse(c_first))/1000 and
d=(d_first,reverse(d_first))/1000, where

    c_first=(274,-403,56,268,-373,559,-483,32,603,-1000,732,-180),
    d_first=(-3,-37,191,-489,833,-974,709,-151,-325,429,-221,-24,
             131,-217,461,-723,652,-228,-117,-10,476,-681,208,602,
             -1000,734,-258,27).

Set u=sum_(r=5)^28 c_(r-5) psi_(T_0)(.-2rT_0) and
v=sum_(r=5)^60 d_(r-5) psi_(T_1)(.-2rT_1).
These exact rationals were selected once by rounding a diagnostic
singular pair of the fixed full blocks. The diagnostic, which includes
all80 directions, is not a certificate and is not a proof input.

The two palindromic trains are centered at L/2. For length n=24 or56,
put S(z)=2sum_(j=0)^(n/2-1) e_j cos((n-1-2j)z), with e_j=c_j or d_j.
Then F_u(t)=exp(-itL/2)P_0(t), F_v(t)=exp(-itL/2)P_1(t), where

    P_j(t)=-16T_j (cosh(T_j/2)-cos(T_j t))^4
            * Aalt_j(T_j t) S_j(T_j t)
            / ((T_j/2)^2+(T_j t)^2)^2.                       (2)

For real t these P_j are real and even. With every prime power retained,

    M(t)=Re digamma(1/4+it/2)-log(pi)
         -2sum_(2<=n<81) Lambda(n)/sqrt(n) cos(t log n),
    Q(u)=pi^-1 integral_0^infinity M(t)P_0(t)^2 dt,
    Q(v)=pi^-1 integral_0^infinity M(t)P_1(t)^2 dt,
    H(u,v)=pi^-1 integral_0^infinity M(t)P_0(t)P_1(t) dt.      (3)

The active prime powers are exactly
2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,37,41,43,47,49,
53,59,61,64,67,71,73,79. The endpoint81 has zero delay overlap.
Equation(3) combines the signed arithmetic and archimedean parts before
integration; neither is replaced by an arithmetic or differential norm.
The pole block is zero because of the exact moments, not an approximation.

### 3. Complete scalar verification and all errors

Reproduction command, from this notebook:

    OPENBLAS_NUM_THREADS=1 python3 scripts/exponential-wavelet/two-scale-certificate-857.py

Full evidence is `scripts/exponential-wavelet/two-scale-certificate-857.json`;
the exact coefficient input is `scripts/exponential-wavelet/witness-857.json`.
The script stores node brackets, panel contributions, constants, bounds,
all checks, failures and hashes. Its printed result is only a summary.
Here is the mathematical justification of its enclosures.

First, symmetry gives R_k=(b_a*b_a)(k+4). The bilateral Laplace transform
of this convolution is (1-2cosh(a)exp(-s)+exp(-2s))^4/(s^2-a^2)^4.
Writing its finite numerator coefficients as p_l gives

    R_k=sum_(l=0)^(k+4) p_l h(k+4-l),
    h(t)=sum_(m>=0) binomial(m+3,3) a^(2m) t^(2m+7)/(2m+7)!.

The code retains m=0,...,15. For 0<a<0.04 and 0<=t<=7 the positive
subsequent-term ratios are below1/2, so twice the first omitted term
encloses the entire tail. All additions, subtractions and divisions
use directed60-digit Decimal intervals. Signed cancellation in the
finite numerator sum is retained. The computed R_0 and R_3 intervals
are strictly positive; all R_k are also positive by their defining
integrals. This pays every A_k error in(1)–(3).

Second, the quadrature is Gauss–Legendre24 on16 panels of length1/8
covering[0,2], and510 panels of length1 covering[2,512]. Each reference
node is enclosed by100 bisections starting from a checked sign-changing
interval for the degree24 Legendre polynomial. The24 brackets are
disjoint, so exhaust its roots. Weights are enclosed by
2/((1-x^2)P_24'(x)^2). NumPy supplies seeds only; sign checks, polynomial
recurrences and interval weights make seed accuracy immaterial.

All trigonometric arguments are reduced by an integer multiple of an
interval for2pi. Sine/cosine series through degrees87/86 have remainders
at most twice the next term, since reduced arguments have modulus<4.
Pi uses Machin's formula with alternating arctangent tails. Arithmetic
cosines advance by exact angle-addition recurrences between adjacent
integer panels, retaining intervals and restarting every16 panels.
Natural interval widths and every endpoint operation remain included.
Decimal exp/log/sqrt endpoints are expanded by one adjacent representable
number around the correctly rounded elementary-function result.

At each real node shift the digamma argument by20 to w=81/4+it/2.
Use the exact recurrence subtracting sum_(k=0)^19
(k+1/4)/((k+1/4)^2+t^2/4), and approximate digamma(w) by
log(w)-1/(2w). L744's imported bound gives absolute error at most
sqrt(2)/(6|w|^2), which is included at every node. No higher asymptotic
expansion or inferred roundoff tolerance is used.

For the quadrature truncation error, analytically continue m to

    mhol(z)=(digamma(1/4+iz/2)+digamma(1/4-iz/2))/2-log(pi).

Use Cauchy disks of radius1/4 at points of[0,2] and radius1 at points
of[2,512]. There are no digamma poles in these disks: on the first
family the two arguments have real part>=1/8; in the second family
their imaginary parts have modulus>=1/2. Shifting each argument by2
then puts its real part>=7/4. The first-order DLMF bound, its principal
logarithm and the two recurrence terms give
|mhol|<100+log(1034) throughout; these loose bounds also cover the
first disk family. The arithmetic holomorphic factor is bounded by
Cprime exp(L)<100*82. The certificate verifies Cprime<100, exp(L)<82,
and ||u||_1,||v||_1<100. The latter follow from

    ||b_a(./T)||_1 <= T exp(T),
    sum |g_k| <= (2+2cosh(a))^2 (A_0+2A_1+2A_2+2A_3)

and the exact coefficient l1 norms9.926 and21.822. On all disks the
absolute value of each analytic integrand before division by pi is
therefore bounded by

    Mstar=10000*82^2*(100+log(1034)+100*82) < 10^14.

Indeed |F_f(z)|<=exp(L|Im z|)||f||_1. The common-center formula in(2)
continues the products in(3) as F_f(z)F_g(-z), with no leftover phase.
For n=24 Cauchy's estimate and the Gauss error theorem give on a panel
of length h and disk radius r the error at most

    h Mstar C_n (h/r)^(2n),
    C_n=(n!)^4/((2n+1)((2n)!)^2).

Here h/r<=1. Summing panel lengths gives total error at most
512 Mstar C_24 < 5.613e-15, before division by pi. Point enclosures
already include all digamma, root, arithmetic and roundoff uncertainties;
this additional estimate controls the exact, rather than approximate,
analytic integrand between the quadrature nodes.

Finally let ell_j be the coefficient l1 norm and

    C_j=16(cosh(T_j/2)+1)^4
         (A_0+2A_1+2A_2+2A_3) ell_j / T_j^3.

Equation(2) gives |P_j(t)|<=C_j/t^4 for real t>0. Put R=512 and let
A=2+8sqrt(2)/3+log(4pi), exactly as in L744(8). Since
log(2+t)<=log(3R)+log(t/R) for t>=R, the absolute tail of the j,k
integral, before division by pi, is bounded by

    C_j C_k R^-7 [(A+Cprime+log(3R))/7+1/49].                (4)

The three computed tail bounds are respectively less than
0.000193473,0.059743907,0.003399825. Thus every infinite-frequency
remainder, every active arithmetic term and every pole qualification
has been accounted for; a frequency cutoff is not being treated as exact.

The full final intervals imply the displayed conclusion. For instance
the computed interval for 4H(u,v)^2-Q(u)Q(v) is strictly positive, while
both pair Q values are positive. Direct interval division gives a lower
ratio exceeding0.9716, which implies the stated conservative bound0.97.
The certificate's upper ratio exceeds1 and proves no upper contraction
bound. It is not evidence for a ratio greater than1 or a negative Q value.

### 4. Separate conceptual audit — 13 November2026, step859

This audit reuses assessment857, separately approved858, and the exact
source formulas/real-root cases assessed855/856. Its task is to validate
the fixed pair, not to reprove the general wavelet or quadrature theorems.
The source-to-physical map in Section1 uses q=x/T_0 and roots T_0 alpha:
the two source spacings are1 and1/2. At physical spacing T the causal
four-factor spline is a positive scalar multiple of b_(T/2)(x/T).
Its L2 normalization and the positive prefactor in H_i only multiply
Graw by a positive scalar. No phase, origin, filter branch or lattice
is changed. For real coefficients the source star conjugates nothing.
The constant free filter1 meets Proposition2's bounded/nonvanishing
hypothesis. The purely imaginary alias exception in the scaling Riesz
theorem does not concern these repeated, nonzero real roots.

The finite Laurent product has powers z^8 through z^-2 with extreme
coefficients A_3>0. Only that extreme spline contributes on each outer
unit interval. Thus the stated supports are exact, and the strict
inequalities 2r-8>0 and 2r+6<64 (respectively128) give precisely the
24 and56 retained translates. The source Riesz property applies to
each whole lattice; restricting it to these finite sets proves their
independence. It is not a positivity theorem for Q.

For the Fourier calculation, each pair of opposite exponential factors
has transform 2exp(-iz)(cosh(a)-cos(z))/(a²+z²). Squaring and multiplying
by Graw(exp(iz)) gives(1), including its phase exp(iz). At z=±ia,
cosh(a)-cos(z) has a simple zero because a>0. The fourth power in(1)
divided by the double denominator leaves a zero of order at least2.
Consequently F_f(±i/2)=0 exactly, as well as its first derivatives there;
only the zeroth moments are needed for the pole block. The palindromic
trains give the phase exp(-i(2*5+n-2)Tt), whose center is32T_0=64T_1=L/2.
This verifies both signs of the pole moments and the common center in(2).

Compact C2 piecewise smooth zero extensions have their first two weak
derivatives in L2 and no boundary delta terms. Supported mollification
converges in H2; the symbol bound |m(t)|<=A+log(2+|t|) is dominated by
a constant times1+t²+t⁴. Cauchy–Schwarz and Plancherel therefore give
continuity of its polarized integral on H2. Finite shifts are bounded
on L2, and each exponential moment is L2-continuous on this fixed
support. The approximants need not themselves be neutral: their pole
products converge to zero. Also L744's elementary generator-domain
argument works directly for these compact C2 functions, since f' is
bounded and log is locally integrable. No extension of the short-window
closed-domain or sign theorem is involved. The same complete Q thus
applies, with the negative arithmetic multiplier in(3).

The prime-power enumeration was independently checked by factoring
every integer2,...,80. It gives exactly the31 pairs (n,p) in the full
certificate, with Lambda(n)=log(p). The endpoint is exactly81 because
exp(4log3)=81; the original numerical endpoint check is only a
consistency check, not a proof of that identity. A delay at least L
has zero overlap for these zero extensions. Translation Plancherel
gives -2 Lambda(n)/sqrt(n) cos(t log n), with measure dt/(2pi).
Realness and the common center reduce the full-line pairing to(3).

Here is a uniform check of every Cauchy disk, rather than a test at
quadrature nodes. Write z=x+iy. On the radius1/4 disks centered in[0,2],
each zeta_±=1/4±iz/2 has Re(zeta_±)>=1/8. On the radius1 disks centered
in[2,512], x>=1, so |Im(zeta_±)|>=1/2. These facts exclude every
nonpositive-integer digamma pole, with strict margins also in a
neighborhood of each closed disk. After adding2, w=zeta_±+2 obeys
Re(w)>=7/4 and 7/4<=|w|<259 throughout both families. Principal log
therefore satisfies |log w|<=log259+pi/2. The exact recurrence gives

    psi(zeta_±)=log(w)-1/(2w)+R(w)-1/zeta_±-1/(zeta_±+1),
    |R(w)|<=sqrt(2)/(6(7/4)^2).

The last two reciprocal terms have total modulus at most16 in the
first family (each denominator has real part at least1/8), and at
most4 in the second (each imaginary part has modulus at least1/2).
Thus on all disks

    |mhol(z)| <= log259+pi/2+2/7+sqrt(2)/(6(7/4)^2)+16+log(pi)
              < 100+log1034.

Pole locations and recurrence are precisely
[DLMF5.2(i), after(5.2.2)](https://dlmf.nist.gov/5.2#i) and
[DLMF5.5.2](https://dlmf.nist.gov/5.5.E2); the complex remainder is
the same first-order right-half-plane bound as L744(8), not a
nodewise approximation used away from its hypotheses.

The certified L1 majorants are below24.379 and25.883, hence below100.
For |y|<=1, |F_f(z)|<=exp(L|y|)||f||_1, and the common-center identity
gives P_j(z)P_k(z)=F_j(z)F_k(-z). The entire arithmetic part has
modulus at most Cprime exp(L|y|)<100*82. These bounds justify the
single Mstar in Section3 on every disk, including those meeting the
ends of the integration interval. The exact integrands are real on
the real axis. The real Gauss remainder therefore applies to their
48th derivatives; no complex mean-value theorem is used. Under an
affine panel change, its factor is
h^49(24!)^4/(49(48!)^3). Multiplying by Cauchy's 48!Mstar/r^48 gives
exactly h Mstar C_24(h/r)^48. Every panel has h/r<=1 and their total
length is512. This verifies the bound before division by pi.

For the spline correlation series the ratio from term m to m+1 is
a²t²(m+4)/((m+1)(2m+8)(2m+9)). For m>=16, a<.04 and t<=7 it is
less than1/2. Twice the first omitted term is a valid positive tail
bound even after the signed finite numerator cancellation, because
each h-value is first enclosed separately. The trigonometric code
retains sine through degree87 and cosine through degree86; on the
verified |y|<4 reductions, the remaining absolute-series ratios are
less than1/2. Its doubled next terms bound both tails. Between integer
panels each fixed Gauss node advances by exactly1, so the arithmetic
rotation recurrence uses the exact increment log(n); restarting it
every16 panels does not omit error or a delay. Low panels restart
individually. All intermediate operations retain intervals.

For arithmetic guarantees the audit uses the implementation-specific
[Python3.15 Decimal specification](https://docs.python.org/3.15/library/decimal.html)
for correctly rounded exp/ln/sqrt and adjacent representable numbers,
as read in approval858. These functions use half-even, independently
of the directed Context used for elementary arithmetic. One adjacent
number on each side encloses the exact endpoint function value.
The [General Decimal Arithmetic1.70 square-root rule](https://speleotrove.com/decimal/daops.html#refsqrt)
confirms that sqrt ignores a requested directed mode; its weaker
general exp/ln guarantee is not substituted for Python's guarantee.
The program uses60-digit directed contexts for every endpoint addition,
subtraction, multiplication and division. copy_negate/copy_abs and
integer/decimal-string conversions are exact. No uncontrolled default
context calculation contributes an endpoint: rounding used to select
an argument-reduction integer is followed by a verified |y|<4 bound,
and the inactive negative-H ratio branch is not used. NumPy seeds are
only starting points for the fully checked root brackets.

Independent audit command, preserving every857 artifact:

    python3 scripts/exponential-wavelet/two-scale-audit-859.py --replay

It saves the complete replay to
`scripts/exponential-wavelet/two-scale-replay-859.json` and full audit
evidence to `scripts/exponential-wavelet/two-scale-audit-859.json`.
The sole replay change is its output path; source and witness hashes
are checked. The original and replay JSON values agree in full,
including every root/weight, all31 delay records, all526 panel records,
correlations, constants, tails and final intervals. An independent
Fraction calculation uses the explicit Legendre polynomial coefficients
to check all endpoint signs; it also checks interval weights, exact
panel coverage/sums, Machin bounds, the final error ledger and the
ratio endpoints by exact squaring. Full records are evaluated, not
accepted from previews. The recorded runtime/context checks and all
arithmetic conditions must pass for the audit script to report PASS.
The recorded Python3.15.2 run passes all648 checks. Both Decimal
contexts have only the expected Inexact/Rounded flags; InvalidOperation,
FloatOperation, DivisionByZero, Overflow, Underflow, Subnormal and
Clamped are all false. Their exponent limits are ±999999.

The analytic tail(4) is independently justified by |P_j(t)|<=C_j t^-4,
|M(t)|<=A+log(2+t)+Cprime, and
integral_R^infinity t^-8 log(t/R)dt=R^-7/49. The already stated tails
are before division by pi; both signs are included in each final
interval. The Gauss error is below5.612390e-15 before division by pi.
The complete enclosures give

    4H²-Q(u)Q(v) > 1.3034390052,
    |H|/sqrt(Q(u)Q(v)) > .9716769027,

with both Q values positive. Thus the provisional fixed half-budget
stop is accepted. The ratio's upper endpoint1.02406083... crosses1;
it is not a lower bound and supplies no negative Q direction. The
audit gives no stronger bound, no claim beyond the checked known
machinery, and no resolution of the full metrics, remaining scales,
coarse/non-neutral directions, uniform assembly or actual-Xi gap.

## Mathlib

Matching Mathlib coverage for this complete Weil-form wavelet certificate
was not checked. Supporting standard Fourier, Sobolev, quadrature and
finite-dimensional facts are not asserted to constitute a matching
formal theorem. No formal verification or absence claim is made.
