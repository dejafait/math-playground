# C759f: Normalized integration lowers the complete form on the two-sine slice

## Hypotheses

Use C759a's complete unneutralized real closed form Q on functions
supported in[-1,1], extended by zero, with its logarithmic Fourier domain:

\[
 F_f(t)=\int f(x)e^{-itx}\,dx,\quad
 m(t)=\Re\psi(1/4+it/2)-\log\pi,
\]
\[
 Q(f)=\int_{\mathbb R}m(t)|F_f(t)|^2\frac{dt}{2\pi}
 +2F_f(i/2)F_f(-i/2)
 -2\sum_{n\in\{2,3,4,5,7\}}\frac{\Lambda(n)}{\sqrt n}C_f(\log n),
 \qquad C_f(y)=\int f(x+y)f(x)\,dx.
 \tag{1}
\]

Here Lambda(p^r)=log p, including Lambda(4)=log2. The source
realization/domain is Suzuki, *Weil's quadratic form via the screw
function*, [arXiv:2606.09096v2](https://arxiv.org/html/2606.09096v2#S2.SS4),
Theorem1.1, (1.8), Section2.4/(2.7), Lemma3.1 and Section3.2,
as specialized and audited in C759a. The full-line multiplier identity
is L741(13),(16)-(17), from the digamma integral
[NIST DLMF5.9.13](https://dlmf.nist.gov/5.9.E13), with real part1/4>0.
C759e's regularized difference calculation is reused, with a new tail.
No small-window positivity, RH or source numerical certificate is used.

Let s_j(x)=sin(j*pi*x), j=1,2, and f=c_1 s_1+c_2 s_2 with real
coefficients, not both zero. Put Pf(x)=integral_(-1)^x f(u)du on
[-1,1], zero outside. The requested sublevel is ||f||_2=1,
Q(f)<=1/250. C759d's audited first-sine cap proves it is nonempty.

## Conclusion

For every such nonzero two-sine vector, in particular every vector
on the requested unit sublevel (including its boundary),

\[
 \frac{Q(Pf)}{\|Pf\|_2^2}<\frac{Q(f)}{\|f\|_2^2}.            \tag{2}
\]

This is a finite-slice partial result, classified REPRODUCTION under
assessment813's standard-method specialization. It establishes no
new general theorem beyond the checked sources. It neither refutes
nor establishes the comparison on the remaining odd domain. Actual
parity infima, ground-state sign/simplicity, other windows, Xi
realization and RH remain open. The separate conceptual and complete
arithmetic audit in Section5 accepts this finite-slice conclusion under
the stated software trust assumptions; no mathematical correction was needed.

## Proof

### 1. Primitive, metric, domain and phase

Direct integration gives

\[
 Ps_j=\frac{(-1)^j-\cos(j\pi x)}{j\pi}.
\]

Write g_1=-1-cos(pi*x), g_2=(1-cos(2*pi*x))/2 and
g=c_1 g_1+c_2 g_2, so Pf=g/pi. These functions are real even and
zero at both endpoints; f is odd with zero integral and zero traces.
Their continuous zero extensions are piecewise C1 with L2 weak
derivatives, since integration by parts on the pieces has no boundary
jump. They belong to H1(R) and H_0^1(-1,1). Plancherel's derivative
identity implies the logarithmic form norm and squared-logarithm
multiplier norm are finite, paying applicability of the full-line
identities. Direct sine/cosine orthogonality gives

\[
 \|f\|^2=c^T I c=:n,\quad
 \|g\|^2=c^T Hc=:h,\quad
 H=\begin{pmatrix}3&-1\\-1&3/4\end{pmatrix},\qquad \det H=5/4>0.
 \tag{3}
\]

Thus n,h>0 and ||Pf||^2=h/pi^2; this actual norm is never replaced
by ||f||. Also ||s_1'||=pi, ||s_2'||=2pi, and
||g_1'||=||g_2'||=pi. The source's D=i*d/dx convention would give
D^(-1)f=-i Pf on this mean-zero slice. We evaluate the real Pf
in(1) directly, without importing an energy-order assertion or
silently identifying it with D^(-1)f. Its norm is the same as that
of -i Pf. No inverse spectral theorem is reproved.

### 2. A regularized relative matrix, with all terms

Let q_1=Q(s_1). Define real symmetric matrices by polarization:

\[
 A_{ij}=Q(s_i,s_j)-\delta_{ij}q_1,\qquad
 B_{ij}=Q(g_i,g_j)-H_{ij}q_1.                              \tag{4}
\]

Then A_11=0 exactly. The common scalar q_1 cancels from the defect:

\[
 \frac{Q(Pf)}{\|Pf\|^2}-\frac{Q(f)}{\|f\|^2}
 =\frac{c^T Bc}{h}-\frac{c^T Ac}{n}.                      \tag{5}
\]

For two real tests u,v define the symmetric correlation
C_uv(y)=(C_(u+v)(y)-C_u(y)-C_v(y))/2, so C_uv(0)=<u,v>.
For the corresponding metric entry h_uv put
R_uv(y)=C_uv(y)-h_uv C_(s_1)(y). Thus R_uv(0)=0.
L741's full-line identity, with
k(y)=2e^(-y/2)/(1-e^(-2y)) and integrable
r(y)=k(y)-e^(-y)/y, gives exactly as in C759e Section2:

\[
 Q_m(u,v)-h_{uv}Q_m(s_1)
       =-\int_0^2 k(y)R_{uv}(y)dy
       =-2\sum_{j\ge0}\int_0^2 e^{-b_jy}R_{uv}(y)dy,
 \quad b_j=2j+1/2.                                      \tag{6}
\]

The scalar and regularizing subtraction cancel because the relative
inner product at0 is zero. The L2 multiplier limit is valid by the
squared-logarithm bounds above. The r convolution pairing is absolutely
integrable. Absolute interchange for the last series, including y=0,
follows from the explicit bound in Section3; it does not require R>=0.
No exterior correction or gamma constant is lost: the cancelled
scalar multiplies the same norm/inner product in the two terms of(4).

The relative pole is retained with its sign. If U_+=F_u(i/2),
U_-=F_u(-i/2) and similarly for v, it is

\[
 U_+V_-+V_+U_--2h_{uv}F_{s_1}(i/2)F_{s_1}(-i/2).          \tag{7}
\]

The relative prime contribution is
-2 sum_n (Lambda(n)/sqrt n) R_uv(log n), over precisely2,3,4,5,7.
All larger prime powers have delay>=log8>2 and zero correlation;
6 is not a prime power. These terms, (6), and(7) give every entry(4).

### 3. Elementary correlations, exact Laplace terms and a new full tail

The following finite algebra specifies every entry without quadrature.
For u(x)=sum_a z_a exp(i*a*pi*x), with a in{-2,-1,0,1,2}, direct
integration over x in[-1,1-y], 0<=y<=2, gives its autocorrelation:

\[
 C_u(y)=\sum_{a,b}z_a z_b
 \begin{cases}
 (2-y)e^{ia\pi y},&a+b=0,\\
 \dfrac{(-1)^{a+b}(e^{-ib\pi y}-e^{ia\pi y})}
                   {i(a+b)\pi},&a+b\ne0.
 \end{cases}                                             \tag{8}
\]

There is no conjugate in this physical product because u is real.
Its coefficients obey z_(-a)=conjugate(z_a). For s_j use
z_j=-i/2,z_(-j)=i/2. For g_1 use z_0=-1,z_(+/-1)=-1/2;
for g_2 use z_0=1/2,z_(+/-2)=-1/4. Polarizing(8) gives C_uv.
Collect R(y)=sum_(a=-2)^2 (U_a+V_a y)e^(ia*pi*y), with conjugate
paired coefficients. With z=b-i*a*pi and E=e^(-2b), its exact
term integral is

\[
 L_b(R)=\sum_{a=-2}^2\left[
 U_a\frac{1-E}{z}+V_a\left(\frac{1-E}{z^2}-\frac{2E}{z}\right)
 \right].                                                \tag{9}
\]

This follows by elementary integration; e^(2ia*pi)=1, and all
 denominators have real part b>0. At y=0 and2 these formulas are
continuous; at2 the integral interval in(8) has zero length.
For(7), direct exponential integration gives

\[
 F_u(\pm i/2)=\sum_a z_a
 \frac{2(-1)^a\sinh(\pm1/2)}{\pm1/2+ia\pi}.              \tag{10}
\]

For a rigorous tail use zero-extended translations T_y on R. Polarizing
||T_yu-u||^2=2||u||^2-2C_u(y) gives

\[
 C_{uv}(y)-\langle u,v\rangle
       =-\tfrac12\langle T_yu-u,T_yv-v\rangle.
\]

The fundamental theorem on each piece, or its L2 weak-derivative
version, gives ||T_yu-u||<=y||u'||. Hence, for all y>=0,

\[
 |R_{uv}(y)|\le\tfrac12
 (\|u'\|\|v'\|+|h_{uv}|\pi^2)y^2.                       \tag{11}
\]

This proves absolute integrability in(6). It also bounds each omitted
Laplace term by (||u'|| ||v'||+|h_uv|pi^2)/b_j^3, using
integral_0^infinity y^2 e^(-by)dy=2/b^3. Retain j=0,...,8191.
For b_*=16384.5 the entire remainder of(6) lies in a symmetric
interval of radius

\[
 2(\|u'\|\|v'\|+|h_{uv}|\pi^2)R_3,\qquad
 R_3=b_*^{-3}+\frac1{4b_*^2},                              \tag{12}
\]

by the decreasing sum-integral comparison at spacing2. In the order
A12,A22,B11,B12,B22, these radii are
(4,10,8,4,7/2)*pi^2*R_3, each less than10^(-7).
This is a new full-tail bound for the primitive correlations;
C759e's fixed-modulus numerical tail is not reused.

### 4. Interval matrix and a continuum sign certificate

Run from this notebook:

    python3 scripts/spectral-triples/two-sine-primitive-814.py

The full certificate is
`scripts/spectral-triples/two-sine-primitive-814.json`. Every one of
8192 relative Laplace terms for all five entries is retained, along
with coefficients(8), complete tails(12), signed pole values, all five
prime terms and trigonometric errors, matrix entries and final checks.
It uses copied C759d/e 60-digit outward Decimal arithmetic: basic
operations have explicit floor/ceiling contexts; negation is context
independent; divisors exclude0. Correctly rounded ln/exp/sqrt are
expanded by adjacent representable endpoints, as specified in the
[Python Decimal documentation](https://docs.python.org/3/library/decimal.html).
Pi uses Machin's identity and60 alternating arctangent terms with the
next-term radius. Prime-delay sine/cosine arguments are reduced by
integer multiples of2*pi, verified in modulus below4, then enclosed
by60 Taylor terms and twice the absolute next term; subsequent ratios
are below1/2. All numerical inputs except these enclosed constants are
exact integers or decimal rationals. No source numerical result or
uncertified diagnostic enters the matrix. Python/Decimal correctness
is a software trust assumption, not a formal verification claim.

For orientation, outward-coarsened entry bounds are

\[
 \begin{array}{c|rr}
 A_{12}&-0.006188067&-0.006187992\\
 A_{22}&0.011738308&0.011738493\\
 B_{11}&-0.007875443&-0.007875295\\
 B_{12}&0.002390640&0.002390714\\
 B_{22}&-0.001354786&-0.001354721
 \end{array}                                             \tag{13}
\]

The sign uses the full stored intervals, not these coarsenings.
For c_1!=0 set t=c_2/c_1 and write A(t)=2A12*t+A22*t^2,
B(t)=B11+2B12*t+B22*t^2. The numerator of(5), divided by c_1^4, is

\[
 q(t)=B(t)(1+t^2)-A(t)(3-2t+3t^2/4).
 \tag{14}
\]

Its coefficients from degree0 through4 are exactly
B11; 2B12-6A12; B11+B22+4A12-3A22;
2B12-(3/2)A12+2A22; B22-(3/4)A22.
Put u=t-43/100 and -q(t)=sum_(j=0)^4 a_j u^j.
The full intervals in the certificate imply

\[
 a_4>0.01015845,\quad
 K:=a_2-\frac{a_3^2}{4a_4}>0.02212839,\quad
 M:=a_0-\frac{a_1^2}{4K}>0.00001114243>0.                \tag{15}
\]

For the actual enclosed coefficients, two exact square completions give

\[
 -q(t)=a_4\left(u^2+\frac{a_3}{2a_4}u\right)^2
       +K\left(u+\frac{a_1}{2K}\right)^2+M>0.
 \tag{16}
\]

Interval dependency overestimation only weakens(15), and its positive
lower endpoints prove the sign for every real t, with no sampling
or untested parameter cells. If c_1=0, the numerator in(5) is
(B22-(3/4)A22)c_2^4=-a_4*c_2^4<0, covering the omitted projective
direction. Positivity of n,h from(3) now proves(2), including every
eligible cap endpoint. The input cap is only a restriction of the
proved slice; no output cap is assumed. No normalization can vanish.

All7 final certificate checks pass with no failures. The diagnostic
scripts/certificates named `two-sine-primitive-*-diagnostic-814` and
`two-sine-primitive-diagnostic-814` contain floating direction choices
only; they do not certify the near-zero maximum or establish(2).
The first interval execution hit a Python operand-dispatch TypeError
before producing a certificate; multiplication order was corrected.
No failed mathematical sign or tail bound was suppressed. The final
certificate and script hash refer to the successful version.

### 5. Separate conceptual and complete arithmetic audit — 13 November2026, step816

The invocation-start SPECIALIZE assessment814 covers this exact audit,
classified REPRODUCTION. The complete statement, proof and generator,
C759a's domain/full form, C759d's audited cap, C759e's regularization,
and L741(7),(13),(16)-(17) were inspected. The primary source coverage
in assessment813/review812 and assessment814 is reused without enlarging
the window, mode set, cap or assertion. This is local verification of
a specialization, not a new general source theorem or a resolution of RH.

**Metric, domain and cancellation.** The endpoint values of each s_j
and g_j vanish; integration by parts on their finitely many smooth
pieces gives no delta masses in the weak first derivative. Their zero
extensions are H1, and the elementary bound
(1+log(1+t²))² <= C(1+t²) pays the multiplier domain in L741(7).
The actual primitive is g/pi. Integrating the constant and cosine
products gives H11=3, H12=-1, H22=3/4, with determinant5/4.
Thus both Rayleigh denominators in(5) are strictly positive, and their
pi factors cancel exactly. D=i*d/dx gives D^(-1)f=-i Pf; only the
real Pf is inserted into(1), so no phase convention imports a sign.

To check(6) directly, polarize the real quadratic pairing of B_epsilon
in L741(7). Its value on u,v is
integral_epsilon^infinity e^(-y)/y [C_uv(y)-<u,v>]dy.
Subtract h_uv times the same expression for s1. Since ||s1||²=1,
the subtractions cancel exactly, leaving R_uv(y). The scalar cI
cancels for the same reason; the r pairing leaves integral r(y)R_uv(y)dy.
The real symbol of B+cI+r* is -m, so the remaining sign is precisely
minus the integral of kR. For y>2 both correlations vanish. This
also explains why no scalar, exterior or Euler constant is missing.

Polarizing the full-line translation norm identity gives
2h_uv-2C_uv(y)=<T_yu-u,T_yv-v>. Cauchy--Schwarz and the H1
translation bound prove(11) for either sign of h_uv or R_uv.
Hence k(y)|R_uv(y)|=O(y) near0, and the sum of the absolute Laplace
integrals is finite. Absolute Fubini, not a positivity assumption,
justifies the exponential series. The omitted series is bounded by
2D sum_(j>=8192)b_j^(-3), D=||u'|| ||v'||+|h_uv|pi².
The first omitted term plus the integral at spacing2 gives(12), with
the five radii exactly (4,10,8,4,7/2)pi²R3. This is a bound on the
whole signed remainder, not a numerical sample of it.

**Finite factors and continuum sign.** Integration of
exp(i(a+b)pi*x) over[-1,1-y], including the separate a+b=0 case,
gives(8). Integrating 1 and y against exp(-(b-ia*pi)y), with
exp(2ia*pi)=1 and Re(b-ia*pi)>0, gives(9). These formulas are
continuous at both overlap endpoints. Independent real integration
checks(10): writing S=sinh(1/2), d1=pi²+1/4, d2=4pi²+1/4,
the positive imaginary pole values for s1,s2,g1,g2 are respectively
2pi*S/d1, -4pi*S/d2, -4S+S/d1, 2S-S/(2d2).
At the negative pole the odd values reverse sign and the even values
agree. Inserting both factors reproduces(7). All five prime-power
terms are retained, with the squared-prime weight log2/sqrt4.
The certified log7<2<log8 excludes every further overlap.

Expanding n(c^T Bc)-h(c^T Ac) gives exactly the five coefficients
after(14). Substituting t=u+43/100 gives the displayed a_j.
Expanding the two squares in(16) yields coefficients a4,a3,a2,a1,a0
in order, since K=a2-a3²/(4a4) and M=a0-a1²/(4K).
Their positive denominators and positive remainder prove the sign
for every finite real t. For c1=0, its homogeneous numerator is
-a4*c2^4<0. No direction, cap boundary or normalization zero is omitted.

**Complete independent arithmetic.** Run from the notebook:

    python3 scripts/spectral-triples/two-sine-primitive-audit-816.py

The original step814 generator and certificate are preserved byte-for-byte.
An exact-byte generator copy is replayed under ambient Decimal precision7
in `scripts/spectral-triples/audit-816/`; every parsed certificate field
matches the original. The observed runtime is Python3.15.2/libmpdec4.0.1.
The explicit 60-digit contexts have Emin=-999999, Emax=999999 and no
InvalidOperation, DivisionByZero, Overflow, Underflow, Subnormal or
Clamped flags. Ordinary inexact/rounded flags are expected.

Every basic endpoint operation is explicitly directed. Negation uses
copy_negate; reciprocals exclude zero; integer powers use repeated
multiplication, not the generic Decimal power contract. Monotone
ln/exp/sqrt endpoints are enlarged by adjacent representables, using
the primary Python Decimal contracts cited above. Machin's alternating
arctangent remainders pay the pi enclosure. Any integer argument shift
preserves periodicity; the entire reduced interval is used, with |x|<4.
After the original 60 sine/cosine terms the subsequent term ratios are
less than1/2, so twice the absolute next term pays the complete tail.

The independent calculation uses Fraction endpoints rounded outwards
by integer floor/ceiling division to at least100 significant digits;
only monotone transcendental endpoints use120-digit Decimal. It forms
the symmetric correlations from direct bilinear integrals, rather than
polarizing (u+v)^2. Complex reciprocals and integration by parts compute
every Laplace integral at all five frequencies, including the negative
ones; they do not copy the original expanded real formulas. Poles use
the independent real formulas above. Prime-delay trigonometry uses
unreduced |x|<13 and120 terms: subsequent ratios are below
169/(240*241)<1/2, so twice the next term pays both tails. Pi uses80
exact rational Machin terms with their next-term errors.

Each of the8192 saved exponentials is enclosed separately at120 digits.
When its independent upper endpoint is below10^(-150), only its use
inside the new Laplace calculation is replaced by[0,10^(-150)]; this
avoids enormous rational denominators and remains an outward bound.
The exponential itself is still checked against its complete stored
interval. Every resulting Laplace enclosure lies inside the original.

The full audit certificate is
`scripts/spectral-triples/two-sine-primitive-audit-816.json`.
All57770 stored numerical intervals are independently checked: correlation
coefficients, every series row, constants, tails, poles, all25 signed
prime rows, trigonometry, matrices and the continuum certificate.
Coverage has no missing or extra intervals. All66207 checks pass with
no failures. The independent enclosures give

\[
 a_4>0.0101584523316948164294,\qquad
 K>0.0221283934419461299495,\qquad
 M>0.0000111424328405781504>0.
\]

These preserve every published bound in(13),(15) and certify the
projective endpoint. C759d's separately audited first-sine upper bound
remains the explicit nonemptiness input for the cap; it is not inferred
from a success flag or recomputed under different assumptions.

Python integer/Decimal/libmpdec correctness remains trusted; this is
not a formal verification. No arithmetic or analytic failure was found,
and the mathematical argument is unchanged. The fixed test is complete.
The full capped odd domain, parity infima, ground-state simplicity/sign,
other windows, actual-Xi realization and the main mixed-positivity gap
remain unresolved. No automatic mode enlargement is authorized by this pass.

## Mathlib

Full matching coverage of the complete Weil form, this two-mode
primitive comparison and its numerical certificate is unchecked.
Plancherel, the Fourier derivative identity, H1 translations,
finite exponential integrals and elementary square completion are
supporting inputs only. Unknown coverage is not evidence of absence.
