# C750o: Complete signed compensation on the fixed phi115

## Hypotheses

Use C750m's unchanged complex H=L2((-b,b);C), zero extension,
L=log101, b=L/2, all35 prime-power coefficients c_n=2Lambda(n)/sqrt(n),
A=sum c_n, T=2pi exp(A+2), beta=2-1/T, P=P64 and Q=I-P.
The Fourier convention is F_f(t)=integral f(x)exp(-itx)dx.
Use exactly its complete forms E and R, with m(t)=Re psi(1/4+it/2)-log pi,
p(t)=sum c_n cos(t log n), and Psi=m-p. Set

    alpha=115pi/L, phi=phi_115=-cos(alpha x)/sqrt(b).

C750n Section2 supplies norm1, real even parity, Qphi=phi and phi in V.
C750m Sections1-2 supply the full complex form and comparison E>=R;
its(13),(16) give the transform and exact supported correlation.
L744(8) supplies |m(t)-log(|t|/(2pi))|<=2/t^2 for |t|>=1,
and its compact bound implies |m(t)|<11 on |t|<=1, as checked in
C750m Section5. C750m Section3 supplies T>100000 and 0<beta<2.

The prior SPECIALIZE assessment1169 is
[the fixed complete-energy scope](../drafts/literature/2026-11-16-signed-phi115-complete-energy-test-1169.md).
It reuses Xuefeng Zhu, *Weil positivity in compact windows: a finite
reduction, certified two-sided bounds, and a Landau-Widom decay law*,
[arXiv:2608.24827v2](https://arxiv.org/html/2608.24827v2),
Theorem1.1/(4), Lemma6.1 and Section11.1/(16), with the normalization,
closure and parity specialization audited in C750m. Section11.4/(17)
also permits geometric-side evaluation; we instead use the accepted
Fourier identity, so no compact archimedean formula is reproved here.

## Conclusion

The complete signed value satisfies

    61177/100000 < R(phi_115) < 62173/100000.             (1)

In particular the interval has width249/25000<1/50; its midpoint
absolute error is less than1/100. The sharper integer enclosure is
given below. This is RESEARCH/REPRODUCTION: a local quantitative
specialization, with no originality claim beyond the sources checked.
Independent conceptual audit1172 in Section6 accepts this enclosure.
It verifies the existing specialization, without claiming a stronger
bound or a discovery beyond the sources checked.

The positive energy compensates the previously proved clipped-symbol
loss on THIS unit vector. This is no lower spectral bound on QRQ or E,
no head/coupling certificate, no all-support sign and no Xi transfer.
A trial value bounds a spectral infimum from above, not below; see
Gerald Teschl, *Mathematical Methods in Quantum Mechanics*, GSM99,
[author version12February2009](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
Section4.3, Theorem4.10 and(4.27)-(4.32), pp118-119.
The main all-degree actual-Xi gap remains open. No RH conclusion follows.

## Proof

### 1. Full scalar identity and exact finite pieces

Put rho(t)=|F_phi(t)|^2/pi for t>=0. Evenness and Plancherel give
integral_0^infinity rho=1. With sinc(0)=1, C750m(13) gives

    F_phi(t)=-sqrt(b)[sinc(bt-115pi/2)+sinc(bt+115pi/2)].  (2)

All apparent poles are removable; sinc's Taylor enclosure is used
near them. For 0<=u<L, C750m(16) gives

    C_phi(u)=(1-u/L)cos(alpha u)+sin(alpha u)/(L alpha).  (3)

Let S=sum c_n C_phi(log n), including ALL35 terms below101. The delay
log101=L has measure-zero overlap and is zero. The odd moment vanishes
only for this even witness. Both original moments remain present in E.
Since sin(alpha b)=-1 and cos(alpha b)=0, direct integration gives

    M_+=M_-=2alpha cosh(b/2)/(sqrt(b)(alpha^2+1/4)),
    Z:=2M_+M_-=4alpha^2(cosh b+1)/(b(alpha^2+1/4)^2),
    cosh b=(sqrt101+1/sqrt101)/2.                        (4)

For example the antiderivative for cos(alpha x)cosh(x/2) has numerator
(1/2)sinh(x/2)cos(alpha x)+alpha cosh(x/2)sin(alpha x),
divided by alpha^2+1/4. This checks (4), including its sign and factor.
Thus the complete identity is

    E(phi)=Gamma-S+Z, Gamma=integral_0^infinity m(t)rho(t)dt. (5)

Only the finite correlations and pole are specialized; no new general
form identity is needed. All integrals are absolute: phi's transform
decays quadratically and m has logarithmic growth by L744(8).

### 2. Complete archimedean errors

The integer parameter enclosures below certify 2<b<5/2 and 2<alpha<80.
Away from t=alpha, (2) or C750m(13) gives

    |F_phi(t)|^2<=4alpha^2/[b(alpha^2-t^2)^2].           (6)

Consequently the ENTIRE interval [0,1] contributes an error bounded by

    e0=44alpha^2/[pi b(alpha^2-1)^2].                   (7)

This uses |m|<11 there and makes no log approximation at zero.
On [1,alpha/2], (6) bounds |F|^2 by64/(9b alpha^2).
Integrating the L744(8) error2/t^2 there, and using2/t^2<=8/alpha^2
and integral rho<=1 on [alpha/2,infinity), gives

    |integral_1^infinity [m(t)-log(t/(2pi))]rho(t)dt|
        <=e1:=128/(9pi b alpha^2)+8/alpha^2.            (8)

These regions cover the entire positive half-line above1, including
both the resonance and all frequencies beyond the integration cutoff.

Take B=512. Since alpha<B/2, (6) gives
rho(t)<=64alpha^2/(9pi b t^4) for every t>=B. The log is positive there,
so its complete tail lies in [0,eB], where exact integration gives

    eB=64alpha^2/(27pi b B^3)[log(B/(2pi))+1/3].         (9)

Thus Gamma is enclosed by the log integral on [1,B], a symmetric error
e0+e1, and the one-sided tail[0,eB]. No frequency region is deleted free.

### 3. Rigorous midpoint error, with no differentiating a digamma series

Let g(t)=log(t/(2pi))rho(t). It is C2 on [1,B], because the compact
Fourier integral is smooth, including its removable zeros/poles.
Plancherel applied to x phi and x^2 phi, and Cauchy--Schwarz, imply

    integral_0^infinity |rho'|<=2||x phi||<=2b,
    integral_0^infinity |rho''|
       <=2||x^2 phi||+2||x phi||^2<=4b^2.              (10)

To check the factors, rho'=2Re(F'conj F)/pi and
rho''=2Re(F''conj F)/pi+2|F'|^2/pi. The absolute expressions are
even for this real even phi, so positive-half integrals divided by pi
equal full-line integrals divided by2pi. Fourier differentiation is
valid since x^k phi is supported and L2; no derivative of the zero
extension is asserted in this argument.

On [1,512], |log(t/(2pi))|<7: pi between3 and4 gives log(2pi)<3,
while log512=9log2<63/10<7, using the accepted log2<7/10.
Using t>=1 and integral rho=1, the product derivative therefore gives

    integral_1^B |g''| <=1+4b+28b^2<186.               (11)

Import Douglas N. Arnold, *A Concise Introduction to Numerical Analysis*,
[author course copy, copyright1999-2001](https://www-users.cse.umn.edu/~arnold/597.00-01/nabook.pdf),
Chapter2 Section2, printed pp58-59, composite formulas(2.3)-(2.4)
and their midpoint example. Its C2 hypothesis was checked above.
For a cell [a,a+h] with midpoint c, the integral minus the midpoint
rule is exactly integral K(s)g''(s)ds,
where K(s)=(s-a)^2/2 on the left half and
K(s)=(a+h-s)^2/2 on the right. Therefore 0<=K<=h^2/8.
Summing cells, the composite midpoint error is at most
(h^2/8)integral|g''|. With h=1/100 and51100 adjacent cells this is

    eq=186/80000.                                     (12)

This application of the known remainder is necessary to pay the whole
mesh error; point intervals alone are not an integral proof.
It avoids a C4 Simpson premise and any new source-series truncation.

### 4. Full conversion from E to R

Plancherel in C750m(2) shows exactly

    E(phi)-R(phi)=integral_T^infinity [Psi(t)-beta]rho(t)dt>=0. (13)

The lower comparison is accepted from C750m; it is not reversed.
For t>=T>100000 and alpha<80, the same tail envelope as in(9) applies.
Since |p|<=A<34, |beta|<2 and L744(8) holds, the integrand's symbol
is at most log t+A+4. Put U=100000. Using b>2 and pi>3,

    E-R <= [64*6400/(9*2*3)]
             *[(log U+34+4)/3+1/9]/U^3
         < [409600/54]*(151/9)/10^15 < 1/10^8.         (14)

Here log U<12: e>8/3 implies e^12>(8/3)^12>100000.
The integrand majorant is nonnegative, so enlarging [T,infinity)
to [U,infinity) is legitimate. Both poles cancel exactly between
E and R, as does the finite-window part of the complete comb.
Equation(14), rather than E>=R alone, supplies the required lower
enclosure for R.

### 5. Complete integer evidence

Run `python3 scripts/sine64/signed_phi115_1170.py`.
The full certificate is `scripts/sine64/signed-phi115-1170.json`.
It imports the independently audited1166 interval primitives; no
floating-point elementary function or external library enters a bound.
The interval grid is10^-40; every add/product/division/square-root
rounds outwards using integers, with denominators checked away from0.
The source map and complete remainders for the reused logarithm,
Machin pi and trigonometric polynomials are in C750n Sections4-5.
They are standard Taylor specializations already audited, not new
general identities; the relevant DLMF references are4.6.4,4.19.1-2,
4.24.3 and4.24.15 with the branch check recorded there.

For sinc, the audited polynomial is used when its WHOLE input interval
is in [-4,4]; otherwise sin(u)/u is used after checking0 is excluded.
This covers BOTH terms in(2) on every one of51100 midpoints, including
the resonance. Each trig reduction verifies its reduced interval lies
in [-4,4]. Each log reduction verifies its real input lies in [1,2].
The code records every midpoint, G, log interval and contribution,
plus all35 coefficients, correlations and their signed contributions.
There is no support, mode or cutoff sweep.

The complete errors read from the certificate satisfy

    eq=0.002325,
    e0<0.000991, e1<0.001626, eB<0.000071,
    0<=E-R<0.00000001.

These displayed decimals are outward summaries only; the script uses
the full rational upper endpoints, not these rounded summaries.
At scale S0=10^40 the final R enclosure is exactly

    [6117701263735406801359882234168088995123,
     6217234740879311899215980072672266872718]/S0.       (15)

Its width is
19906695428781019571219567700835575519/(2*10^39)<1/50.
Exact integer comparison puts (15) strictly inside (1). All seven
certificate checks pass, with no domain failure. Full-cell assembly
inspection is in `scripts/sine64/signed-phi115-assembly-1170.json`;
it verifies all indices/midpoints, complete sums and final rational
comparisons. This is supporting finite arithmetic, not an independent
analytic or primitive audit. Section6 completes that separate audit.

The actual norm-loss obstruction of C750n is therefore compatible with
a positive complete value: it threw away the positive energy now paid
in(5)-(15). No property of any other complementary vector follows.

### 6. Independent conceptual and complete finite audit1172

This audit uses the prior SPECIALIZE assessment1170, separately approved
in1171. It accepts(1)-(15) for precisely the fixed hypotheses above.
The original1170 and1166 programs and certificates are unchanged.
No parameter, mode or cutoff search is performed. The known identities
are imported; verifying their hypotheses, the local error constants
and the unpublished scalar certificate is the necessary specialization.

**Normalization, support and complete pole.** C750m Section1 states the
complex closed form on V and the comparison E>=R; its Section3 checks
T>100000. C750n Section2 checks the unit norm, Q membership and endpoint
regularity for this particular phi. Its transform is real even, so
the full-line density dt/(2pi) becomes dt/pi on the positive half-line,
with total mass1. Neither the signed arithmetic nor the odd pole was
deleted from the parent form. The supported correlation in(3) has the
plus sine term, since sin(2*115*pi-alpha*u)=-sin(alpha*u). All35 shifts
have 0<log(n)<L; the endpoint log101 has zero overlap. The antiderivative
in Section1 at both endpoints uses sin(alpha*b)=-1 and cos(alpha*b)=0.
Thus each M is positive with the value in(4), and 2M^2 equals precisely
the displayed Z, using cosh(b/2)^2=(cosh b+1)/2. This checks the even
pole's factor and sign rather than inferring them from parity alone.

**Every analytic error region.** On[0,1], alpha>2 keeps the denominator
in(6) bounded below by(alpha^2-1)^2; length1 and |m|<11 give exactly(7).
On[1,alpha/2], integrate 2/t^2 with the bound64/(9b alpha^2) for |F|^2,
giving at most128/(9pi b alpha^2). On[alpha/2,infinity), use total rho
mass at most1 and 2/t^2<=8/alpha^2. This proves(8) over the entire
region, including the resonance and the tail beyond512. The positive
log tail uses alpha<80<512/2 and

    integral_B^infinity log(t/(2pi))/t^4 dt
       =[log(B/(2pi))+1/3]/(3B^3).

This verifies(9)'s sign, factor3 and complete integration range. Hence
the near-zero omission and symbol replacement are symmetric errors,
whereas only the log tail has a one-sided allowance. No unaccounted
gap or double assumption of frequency support enters Gamma.

**Differentiation and integrated quadrature bound.** For k=0,1,2,
x^k phi is in L1 and L2 by compact support. Dominated differentiation
gives F^(k)=Fourier[(-ix)^k phi]; Parseval then gives its squared
full-line norm divided by2pi as ||x^k phi||^2. This is the negative-sign,
unnormalized specialization of NIST DLMF
[1.14.1](https://dlmf.nist.gov/1.14.E1) and
[1.14.7_5-8](https://dlmf.nist.gov/1.14.E8), with the absolute and square
integrability hypotheses stated in Section1.14(i). Reflection of the
frequency variable changes the source positive sign without changing
these norms. Since |F'F|, |F''F| and |F'|^2 are even, the positive-half
integrals divided by pi equal the full-line integrals divided by2pi.
Cauchy--Schwarz in the two derivative identities in Section3 proves
exactly(10), including both factors2. It differentiates the compact
Fourier integral, not the zero extension in x or a digamma series.

Now g''=-rho/t^2+2rho'/t+log(t/(2pi))*rho''. The bound |log|<7,
t>=1, integral rho=1 and(10) give1+4b+28b^2<186, because b<5/2
and1+4*(5/2)+28*(5/2)^2=186. Smoothness of F makes g C2 even at
t=alpha. Apply Arnold's cited composite kernel directly: its supremum
is h^2/8, so51100 adjacent length1/100 cells incur at most186/80000.
There is no extra cell-count factor and no pointwise or C4 premise.

**Complete E-R conversion.** In the full Fourier expression for E,
replace the arithmetic correlations by their full cosine integrals,
as established in C750m Section1. Subtract R from C750m(2) and use
Plancherel. The finite band and both moments cancel, leaving exactly
(13), including the positive-half density. The accepted tail comparison
supplies its nonnegativity; no sign of E is used. For t>=T>U=100000,
L744(8), |p|<=A<34, |beta|<2 and alpha<80 imply the integrable positive
majorant used in(14). Extending only that majorant to[U,infinity) is
legitimate. The exact rational checks are

    (8/3)^12>100000,
    [409600/54]*(151/9)/10^15
       =151/1186523437500 < 1/100000000.

Thus log U<12 follows from e>8/3, and the allowance subtracts from the
LOWER endpoint of E, with the upper endpoint unchanged. This establishes
the required lower bound for R as well as the accepted upper comparison.

**Independent complete finite evidence.** Run
`python3 scripts/sine64/audit_signed_phi115_1172.py`.
Its full certificate is `scripts/sine64/signed-phi115-audit-1172.json`.
It imports only the independent audited1168 implementation, not1170
or1166. C750n Section5 gives that implementation's precise real-branch
Machin proof, 65/20-term arctangent bounds, 90-term monotone endpoint
logarithms, 50-term direct trigonometric recurrences on[-7,7] and
10^-70 outward integer arithmetic. The code was inspected again here:
its four endpoint products/ratios, exact root rounding and Taylor
remainders have the stated signs and domains. The sine/cosine/sinc
remainders are respectively7^101/101!,7^100/100!,7^100/101!. Sinc uses
its polynomial on a whole interval inside[-7,7]; otherwise its checked
nonzero denominator and reduced sine enclose the quotient.

The audit independently factors every integer2,...,100 and matches all
35(n,p) pairs, then encloses each coefficient, log shift, correlation
and signed product. Every finer interval is contained in its saved1170
interval by exact endpoint cross-multiplication. For EVERY one of51100
consecutive midpoints it independently encloses both sinc terms, their
sum G, the logarithm and the complete signed contribution. All saved
intervals contain these independent results. Full finer intervals and
per-record checks are saved, not replaced by a sample or decimal match.

In addition, separate rational endpoint arithmetic on the old10^-40
grid reconstructs each original signed product and the exact complete
sums, parameter assembly, pole, near-zero and asymptotic errors, and
Gamma/E/R assembly. The log-tail bound is independently enclosed on the
finer grid inside its saved interval; its saved upper endpoint is used
as the allowance, without guessing an unrecorded primitive. The audit
also reconstructs every original elementary call's input domain:
51173 log calls, 101923 trigonometric calls, 347 small-sinc calls and
101853 sinc divisions all satisfy their original asserted domains.
Both sides of the removable resonance are therefore covered.

The independently computed Gamma/E/R intervals, assembled with the same
saved analytic allowances, lie inside the original intervals. All32
global checks pass; all51100 cell checks and all35 term checks pass;
there are no failures. Selected complete `/checks`, `/domain_counts`,
`/independent_errors` and `/assembly` values were inspected using the
JSON inspector, as were the original `/errors`, `/parameters` and
`/full_R`. Verification uses all records, not those selected views.
The source certificate's hash is recorded and its bytes are unchanged.

The exact old endpoints remain(15), with width
19906695428781019571219567700835575519/(2*10^39)<1/50. Strict integer
comparison gives(1). This fills the independent-verification gap for
the existing scalar only. C750m/C750n's norm stops remain valid; the
present positive trial supplies no all-direction lower bound, head or
coupling control, all-support sign, actual-Xi transfer, or RH conclusion.

## Mathlib

Full matching coverage for this fixed signed scalar, complete cutoff
conversion and rational certificate is not checked. Plancherel,
Fourier differentiation, Cauchy--Schwarz, elementary Taylor remainders
and interval arithmetic are supporting standard inputs. No matching
Mathlib theorem or Lean verification is claimed; unknown coverage is
not evidence of absence.
