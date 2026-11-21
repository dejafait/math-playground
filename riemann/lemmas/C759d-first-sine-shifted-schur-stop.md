# C759d: The first retained sine stops the fixed shifted Schur test

## Hypotheses

Use C759a's complete real closed Weil form Q on zero-extended
L2(-1,1), with Fourier transform F_f(t)=integral f(x)e^(-itx)dx
and Fourier measure dt/(2*pi). Its domain is the supported logarithmic
Fourier domain, with norm squared integral
(1+log(1+t^2)/2)|F_f(t)|^2 dt/(2*pi). Thus

\[
 Q(f)=\int m(t)|F_f(t)|^2\frac{dt}{2\pi}
       +2F_f(i/2)F_f(-i/2)-2\sum_{n\in\{2,3,4,5,7\}}a_n C_f(\log n),
 \quad m(t)=\Re\psi(1/4+it/2)-\log\pi,
 \quad a_n=\Lambda(n)/\sqrt n.
 \tag{1}
\]

Retain V=span{s_j(x)=sin(pi*j*x):1<=j<=120} in the real odd
space, and its complete L2 orthogonal complement W. Each s_j has
norm1. Put tau=11/200, d=2859/10000, and q_tau=Q-tau||.||^2.
C759c supplies q_tau(w)>=d||w||^2 on the full complementary form
domain. Let A be q_tau's matrix on V. Define the complete cross
representers h_j and their Gram matrix K in the proof below; the
approved scalar-floor sufficient matrix is S_d=A-K/d.

The generic comparison is imported from Andrews, Connes and La Gatta,
*The uncertainty operator, the Weil ground state and the zeros of zeta*,
[arXiv:2611.13129v1](https://arxiv.org/html/2611.13129v1#S8.SS6),
Lemma8.16, and Hongmin Li, *Cutoff-free positivity of localized Weil
forms through the (log11)/2 threshold*,
[paper45/v2](https://rstation.ai/problems/riemann_hypothesis/papers/45),
Sections4-5, (4.7)-(5.5). Only the scalar lower-block comparison is
used. No exact inverse of the complementary operator, source numerical
certificate, RH, even minimizer or parity ordering is assumed.

## Conclusion

Every retained vector has a complete L2 cross representer on W;
K is a finite positive semidefinite Gram matrix. The full-form scalar
certificate gives, for s_1(x)=sin(pi*x),

\[
 0.00168053281301474<Q(s_1)<0.00364123566126519<0.004,
 \tag{2}
\]
\[
 e_1^T S_d e_1\le Q(s_1)-\frac{11}{200}
       <-0.05135876433873481<-0.051<0.
 \tag{3}
\]

Hence this fixed shifted Schur test is not positive semidefinite.
In fact the retained diagonal already disproves the proposed full odd
floor tau: inf_(odd f!=0) Q(f)/||f||^2 <= Q(s_1)<tau. This is not a
negative value of Q, not a disproof of actual even/odd ordering, and
not a statement about an off-line zeta zero. C759a's constant even
trial is only an upper bound on the even infimum, which may be much
smaller. Even simplicity/sign and Xi realization remain independent.

This is REPRODUCTION of the assessed entry and scalar-enclosure
methods, with a new local stopping certificate, not a claim of a new
general theorem beyond the checked sources. The separate conceptual
and complete scalar audit in Section5 accepts the certificate and
operator-domain argument under their stated hypotheses.

## Proof

### 1. Complete cross map, including the domain

Write E for zero extension and g(x)=sinh(x/2) on(-1,1). C759a(5)
implies |m(t)|<=M+log(1+t^2)/2 for some finite M. Direct integration
of the two exponentials in s_j gives, away from t=plus or minus j*pi,

\[
 F_{Es_j}(t)=\frac{2i(-1)^j j\pi\sin t}{j^2\pi^2-t^2}.
 \tag{4}
\]

Here (4) is justified for all nonsingular real t by that direct
integration; C759a's originally restricted use is not assumed to be
a global tail estimate. At the removable points use the defining
integral, which is continuous and bounded in modulus by sqrt2 by
Cauchy--Schwarz. For |t|>=2*j*pi, (4) gives
|F_(Es_j)(t)|<=8*j*pi/(3*t^2). Consequently m F_(Es_j) belongs
to full-line L2: on compact sets it is bounded; at infinity its
squared modulus is O((1+log|t|)^2/t^4), which is integrable.
This proves an operator-domain fact, not merely finite form norm.

By the Plancherel theorem let R_j be the restriction to(-1,1) of the
inverse Fourier transform of m F_(Es_j). Define the L2 function

\[
 r_j(x)=R_j(x)-\sum_n a_n\bigl[(Es_j)(x+\log n)
                                  +(Es_j)(x-\log n)\bigr]
                         -2\langle s_j,g\rangle g(x).
 \tag{5}
\]

Every term is in L2: the shifts followed by restriction are contractions,
the sum is finite, and g is in L2. Real-even m and the symmetric shift
pairs preserve real oddness, so r_j is real odd. Polarizing (1),
Plancherel and changes of variables in the finite shift integrals give

\[
 Q(s_j,w)=\langle r_j,w\rangle
 \tag{6}
\]

for every real odd w in the full form domain. The Fourier pairing is
absolutely convergent by Cauchy--Schwarz applied to m F_(Es_j) and
F_(Ew); it agrees with the polarized weighted-form integral. In the
odd sector the two poles are exactly -2< s_j,g >< w,g >, accounting
for the final term of (5). No passage from an unproved smooth-only
operator identity is required.

The exact projection is h_j=P_W r_j=r_j-sum_(k=1)^120<r_j,s_k>s_k.
Since <s_j,w>=0 on W, q_tau(s_j,w)=<h_j,w>. This identity holds on
the entire complementary form domain and extends the cross map as
an L2 functional. Put K_ij=<h_i,h_j>. For every real vector c,

\[
 c^T Kc=\left\|\sum_{j=1}^{120}c_jh_j\right\|_2^2\ge0.
 \tag{7}
\]

For completeness, sine completeness and Parseval also give
K_ij=sum_(k=121)^infinity Q(s_i,s_k)Q(s_j,s_k). These series converge
absolutely by Cauchy--Schwarz for the two square-summable coefficient
sequences. This is the full covariance, with all mixed component
terms included by (5), not a sum of separately estimated component
norms. For the negative direction below only (7) is needed. Thus
no infinite-frequency numerical remainder or covariance upper enclosure
is needed: every uncomputed contribution to K_11 is nonnegative.

C759a pays the closed-domain split and C759c pays the complementary
floor. These establish applicability of the cited sufficient Schur
comparison. Its generic proof is not repeated. Since d>0, (7) gives
e_1^T S_d e_1=A_11-K_11/d<=A_11=Q(s_1)-tau. A strict negative
upper bound for A_11 is therefore decisive for this exact fixed test,
regardless of the other119 retained directions. Failure of a matrix
upper enclosure is not being used as negative evidence.

### 2. Exact first-sine entry

Direct integration gives, for 0<=y<=2,

\[
 C_{s_1}(y)=(1-y/2)\cos(\pi y)+\frac{\sin(\pi y)}{2\pi},
 \qquad \langle s_1,g\rangle=
       \frac{2\pi\sinh(1/2)}{\pi^2+1/4}=:g_1.
 \tag{8}
\]

The prime contribution is consequently
-sum_n a_n[(2-log n)cos(pi log n)+sin(pi log n)/pi], with all five
prime powers. Its sign is not replaced by an absolute bound. The
pole contribution is -2g_1^2.

Use Connes, Consani and Moscovici, *Zeta Spectral Triples*,
[arXiv:2511.22755v1](https://arxiv.org/html/2511.22755v1),
Lemma2.3 and Section4, (4.2)-(4.4), at lambda=e and L=2, as in
C759a Section5 and L759's general entry reduction. The zero-extended
sine is precisely the unit odd combination of modes plus/minus1,
up to a unit complex phase and the shift of origin from(0,2).
Both preserve the quadratic form. In particular the correlation
input is omega(y)=2C_(s_1)(y), omega(0)=2. Equation(4.4) gives

\[
 W_{\mathbb R}=\gamma+\log(4\pi\tanh1)+
       \int_0^2\frac{e^{y/2}\omega(y)-2}{e^y-e^{-y}}\,dy,
 \quad Q_m(s_1)=-W_{\mathbb R}.
 \tag{9}
\]

This retains the exterior correction tanh1 and the source sign.
Set rho(y)=e^(y/2)/(2sinh y) and
S=integral_0^2 rho sin(pi y), C=integral_0^2 rho(cos(pi y)-1),
D=integral_0^2 y rho cos(pi y), B=integral_0^2 rho(1-e^(-y/2)).
Substitution of (8) into (9) gives exactly

\[
 Q(s_1)=-\gamma-\log(4\pi\tanh1)-2C+D-2B-S/\pi
       -2g_1^2-\sum_n a_n\left[(2-\log n)\cos(\pi\log n)
                                  +\sin(\pi\log n)/\pi\right].
 \tag{10}
\]

No different-window value from L759 is reused. The specializations
are necessary because neither its finite radius-log13 certificate
nor the cited unshifted positivity results give this shifted entry.

### 3. Finite sums with complete analytic tails

For b_k=2k+1/2 and E_k=e^(-2b_k), rho(y)=sum_(k>=0)e^(-b_k y).
The elementary term integrals, using pi*2=2pi, are

\[
 \begin{split}
 S&=\sum_{k\ge0}\frac{\pi(1-E_k)}{b_k^2+\pi^2},\\
 C&=-\sum_{k\ge0}\frac{\pi^2(1-E_k)}{b_k(b_k^2+\pi^2)},\\
 D&=\sum_{k\ge0}\left[
 \frac{(1-E_k)(b_k^2-\pi^2)}{(b_k^2+\pi^2)^2}
                  -\frac{2E_kb_k}{b_k^2+\pi^2}\right],\\
 B&=\sum_{k\ge0}\left[\frac{1-E_k}{b_k}
                   -\frac{1-E_ke^{-1}}{b_k+1/2}\right].
 \end{split} \tag{11}
\]

All interchanges are absolute, including at0: use |sin(pi y)|<=pi*y,
|cos(pi y)-1|<=pi^2*y^2/2, |y cos(pi y)|<=y, and
0<=1-e^(-y/2)<=y/2. Integrating these against e^(-b_k y) on
(0,infinity) produces summable multiples of b_k^-2 or b_k^-3.

Keep k=0,...,511. Write b_*=1024+1/2 and
R_2=b_*^-2+1/(2b_*), R_3=b_*^-3+1/(4b_*^2),
E_*=e^(-2b_*)/(1-e^-4). The decreasing sum-integral comparison gives
sum_(k>=512)b_k^-s <= b_*^-s+b_*^(1-s)/(2(s-1)), for s>1.
Every remainder in (11) is enclosed by

\[
 S_{tail}\in[0,\pi R_2],\quad
 C_{tail}\in[-\pi^2R_3,0],\quad
 |D_{tail}|\le R_2+2E_*/b_*,\quad
 B_{tail}\in[0,R_2/2]. \tag{12}
\]

The signs for S and C follow termwise from (11). For D use
|b^2-pi^2|/(b^2+pi^2)^2<=1/b^2, 0<1-E<1,
and b/(b^2+pi^2)<=1/b. Sum the remaining exponentials as an exact
geometric series of ratio e^-4. The B bound follows from its
nonnegative integrand and the preceding y/2 inequality. These are
full infinite tails, not numerical asymptotics.

### 4. Arithmetic certificate and limitations

Reproduce from the notebook with

    python3 scripts/spectral-triples/shifted-schur-stop-806.py

The complete certificate is
`scripts/spectral-triples/shifted-schur-stop-806.json`. It records
every term of the four512-term series, partial sums, all remainder
enclosures, constants, five signed prime contributions, components,
final intervals, checks, failures and source hash. All8 checks pass.
The final upper endpoint of Q(s_1) is
0.00364123566126518143532582655011590251559850355619035489241.
The script's full interval implies the outward decimal bounds (2)
and, subtracting the exact tau, (3).

Basic operations use60-digit Decimal floor/ceiling contexts. Monotone
ln, exp and sqrt endpoints are expanded by one adjacent representable
value, using the correctly rounded operations documented in the
[Python Decimal reference](https://docs.python.org/3/library/decimal.html).
Negation uses copy_negate, and division excludes zero. Pi uses the
60-term alternating arctangent sums in Machin's identity, with
next-term remainder. Gamma is enclosed by
H_128-log128-1/(2*128)+1/(12*128^2), with symmetric radius
1/(60*128^4), exactly the Euler--Maclaurin specialization justified
in C759a Section5-6 and L759 Section3; the named inputs are
[DLMF2.10.1](https://dlmf.nist.gov/2.10.E1) and
[DLMF24.8.1](https://dlmf.nist.gov/24.8.E1).

For each prime delay, reduce turns=(log n)/2 by an exactly selected
integer; retain the entire interval for x=2pi(turns-integer) and
verify |x|<4. Sum sine through degree119 and cosine through degree118.
Twice the absolute next-term bound pays the tails, since each
subsequent absolute term ratio is below16/(119*120)<1/2.
Thus the errors in every transcendental, finite sum and infinite
series enter (10) before the strict comparison. Python integer and
Decimal correctness remain software trust assumptions, not formal
verification of the interpreter.

The prior exploratory arrays in
`scripts/spectral-triples/shifted-schur-diagnostic-806.json` and the
derived direction summary are explicitly uncertified and are not
inputs to (2)-(3). They only selected s_1. No diagnostic eigenvalue,
unbounded quadrature, computed zero location, or finite-mode substitute
for the full complementary form enters the certificate. Neither a
complete matrix enclosure nor a full inverse-covariance computation
was carried out, because (3) already settles the approved negative
branch. C759c's complementary floor remains intact; the failure is
in a retained direction. A new shift or even trial would be a changed
target requiring its own source gate, not part of this attempt.

### 5. Independent conceptual and scalar audit — 13 November2026, step808

The unchanged SPECIALIZE assessment806, separately approved in step807,
covers this exact audit. Existing source coverage is reused; this is
REPRODUCTION, not a new theorem beyond the sources checked. No error
requiring a change to (1)-(12) was found.

**Operator domain and complete Gram.** The formula (4) follows by
integrating each exponential on [-1,1]. Since j is an integer, both
endpoint terms contain (-1)^j sin(t); the sign agrees with
F_s(t)=-it integral x s(x)dx+O(t^2) near0. At t=plus or minus j*pi
the defining integral is continuous, bounded by sqrt2, and removes
the quotient singularities. For |t|>=2j*pi the denominator modulus
is at least3t^2/4, giving the displayed8j*pi/(3t^2). C759a(5)'s
bounded symbol remainder makes the resulting mF_s square integrable
for every one of the120 fixed modes. This is the precise extra fact
needed for an L2 representer; the weaker form norm would not suffice.

The real-even multiplier preserves the Fourier conjugation symmetry
of a real odd function. Its inverse transform and restriction are
therefore real odd. For each finite prime shift, polarization of
-2a_n C_f(log n) gives exactly minus a_n times the two shift pairings
in (5). For real odd f, F_f(i/2)=<f,g> and F_f(-i/2)=-<f,g>,
so polarization of the pole product gives -2<s_j,g><w,g>.
Plancherel with measure dt/(2pi) justifies the remaining pairing
on the whole form domain, since mF_s and F_w are both in L2.
No smooth-core operator identity or unproved continuity extension
is used. C759a supplies the closed, dense complementary form domain.

Projection subtracts only the120 retained sine coefficients and
defines h_j in the full odd W, whether or not h_j itself has finite
form norm. Membership of h_j in the form domain is not required for
its L2 functional. Completeness of the integer sine basis follows
from the usual sine basis on(0,1) by odd extension. Parseval then
gives the entire covariance; Cauchy--Schwarz gives absolute convergence
of each mixed coefficient series. Thus K is exactly a nonnegative
Gram matrix, and d>0 yields the claimed upper bound in(3).
C759c's audited Q(w)>=0.3409||w||² gives the exact shifted
d=0.3409-0.055=0.2859. This pays the imported scalar-floor
comparison's complement hypothesis but cannot repair A_11<0.
The negative diagonal also defeats the odd floor directly, independent
of whether that sufficient comparison is used.

**Normalization and all analytic errors.** On0<=y<=2, integrate
sin(pi(x+y))sin(pi*x) over[-1,1-y] to obtain(8); the product-to-sum
boundary term is +sin(pi*y)/(2pi), not its negative. The endpoint
antiderivative of sin(pi*x)sinh(x/2) gives the stated positive g_1.
In the cited CCM basis at L=2, q_11=q_(-1,-1)=(2-y)cos(pi*y)
and q_(1,-1)=q_(-1,1)=-sin(pi*y)/pi. The normalized odd coefficient
vector, up to its unit complex phase, is(1,-1)/sqrt2. Its omega is
therefore q_11-q_(1,-1)=2C_s and omega(0)=2. This checks the
specialization of the defining(4.4) without invoking any source
special-function shorthand. The factor(exp(2)-1)/(exp(2)+1)=tanh1
and Q_m=-W_R are retained. Substitution gives exactly(10).

The finite support contains precisely the prime powers2,3,4,5,7;
Lambda(4)=log2. Both overlap directions have already supplied the
factor2 in(1). The scalar certificate keeps each resulting signed
term and -2g_1². Every finite term of(11) follows from elementary
exponential integration; in particular D is the negative b derivative
of b(1-exp(-2b))/(b²+pi²), producing its negative endpoint term.
The four absolute-integral majorants at y=0 given in Section3 are
summable, so the exchanges are valid even though rho itself is singular.
The decreasing sum-integral bound includes the k=512 term before its
integral. Its inverse-square and inverse-cube bounds, the geometric
exponential tail and all four signs/radii in(12) have been checked.
The gamma radius is the m=2 specialization of L759's cited
Euler--Maclaurin bound, with |B_4|=1/30; it does not assume a remainder
sign. No finite cutoff is substituted for any infinite integral.

**Complete independent arithmetic.** Run from the notebook:

    python3 scripts/spectral-triples/first-sine-schur-audit-808.py

The original generator and certificate are preserved byte-for-byte.
An exact-byte copy is replayed under ambient Decimal precision7 in
`scripts/spectral-triples/audit-808/`. Its parsed certificate equals
the original in every field. The generator's division domains,
monotone transcendental rounding, copy_negate, exact inputs, 60-term
Machin bounds and reduced Taylor error bounds were also inspected.
Any selected reduction integer preserves periodicity; the whole
reduced interval is retained. Decimal ambient rounding affects no
arithmetic endpoint.

The independent calculation uses Fraction interval arithmetic. Each
operation is rounded outwards on a rational decimal grid by integer
floor/ceiling division, retaining at least100 significant digits.
Only ln, exp and sqrt endpoints use120-digit Decimal contexts and
adjacent endpoint expansion. Machin sums use80 exact rational terms.
Sine and cosine use unreduced x=pi*log n, |x|<7, through degrees179
and178. Twice the absolute next term pays each remainder: all
subsequent ratios are less than49/(180*181)<1/2. For B the second
exponential is evaluated directly at -2(b+1/2), independently of the
generator's product of exponentials. These choices avoid simply
repeating the generator's reduced trigonometric implementation.

The audit compares independently enclosed values with every saved
constant, all512 four-integral rows including b and E, their sums,
every tail majorant and enclosure, all five complete prime rows,
all three Q components and the final published bounds. All3674
checks pass, with no failures. Complete check evidence and the
independent trigonometric errors are stored in
`scripts/spectral-triples/first-sine-schur-audit-808.json`. The
independent final enclosure is contained in the original one; its
upper endpoint is less than0.003641235661265182. Hence(2)-(3) pass
with their written strict endpoints. This is complete scalar
verification, not reliance on a preview, diagnostic or success flag.

Python integer arithmetic and Decimal/libmpdec correctness remain
software trust assumptions. The conclusion is an independently audited
local stop for this fixed tau and scalar-floor matrix, not a negative
value of unshifted Q. Actual parity, even simplicity/sign, Xi
realization with multiplicities and global mixed positivity remain
unproved. No new shift, basis or window was tested.

## Mathlib

Full matching coverage of the complete fixed-window representers and
the first-sine numerical stopping certificate has not been checked.
Plancherel, Parseval, sine completeness, Gram positivity and elementary
series integration are supporting named inputs, not a matching formal
certificate. No Mathlib absence or formal verification is claimed.
