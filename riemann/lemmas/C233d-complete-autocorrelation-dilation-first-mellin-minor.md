# Corollary 233d: one necessary Mellin minor for complete theta dilation mixtures

## Hypotheses

Use exactly L019's K on [0,infinity), k(u)=K(|u|), and L233's complete
associated kernel, with a separate name H for the unweighted autocorrelation:

\[
 A(t)=\int_{\mathbb R}s^2k(s+t)k(s-t)\,ds,\qquad
 H(t)=\int_{\mathbb R}k(s+t)k(s-t)\,ds.
\]

H here denotes no heat-flow contract. Set a(t)=A(t)/A(0) and
h(t)=H(t)/H(0). The proposed representation, not an established hypothesis
about actual theta, is

\[
 a(t)=\int_{(0,\infty)}h(bt)\,d\mu(b)\quad(t\in\mathbb R),       \tag{1}
\]

where mu is a positive Borel probability measure. All b are finite and
strictly positive; arbitrary atoms, unbounded support and accumulation at
either missing endpoint are allowed. No inverse moments are assumed.
Define, using complete integrals,

\[
 I_A(r)=\int_0^\infty t^{r-1}a(t)\,dt,\quad
 I_H(r)=\int_0^\infty t^{r-1}h(t)\,dt,\quad
 q_r=I_A(r)/I_H(r)\quad(r=1,2,3).
\]

## Conclusion

All these normalizations and integrals are finite and strictly positive.
If (1) holds, then

\[
 q_r=\int_{(0,\infty)}b^{-r}\,d\mu(b)\quad(r=1,2,3),\qquad
 D=q_1q_3-q_2^2\ge0.                                      \tag{2}
\]

The single validated-integration attempt758 below gives, for the actual
complete theta kernel,

\[
 0.001519<D<0.004990.                                      \tag{11}
\]

In particular this necessary condition passes strictly. It supplies no
exclusion of the proposed dilation-mixture class.
This is only a finite necessary test: even D>0 neither constructs mu nor
proves the first associated Fourier sign. Higher/mixed positivity and RH
remain open. This corollary is a local specialization and computation of
known moment necessity, without a claim of originality. Independent audit760 below validates
this finite pass under the same software arithmetic qualification.

## Proof

### Normalization, complete integrals, and the measure endpoints

L019 gives continuity, strict positivity and, for every B>0, a constant
C_B with k(u)<=C_B exp(-B|u|). C233c has already proved 0<A(0)<infinity.
The same bound gives H(0)=integral k(s)^2 ds<infinity; continuity and
positivity on [1,2] give H(0)>0. Both A(t) and H(t) are finite and positive
for each t: use |s+t|+|s-t|>=2|s| and integrate, with the extra s^2 for A.
Continuity follows by dominated convergence on compact t intervals, as
in L233. In particular the integrands in (1) are Borel measurable.

Put M_j=integral_R u^j k(u)du for even j=0,2,4, and write B_A(r),B_H(r)
for the corresponding unnormalized Mellin integrals. The substitution
u=s+t, v=s-t has absolute Jacobian 1/2, t=(u-v)/2 and s=(u+v)/2.
The half-plane t>0 is u>v. Exchanging u,v preserves the nonnegative
integrands and divides the whole-plane integral equally between the two
half-planes, the diagonal having measure zero. Therefore

\[
\begin{aligned}
 B_H(r)&=2^{-r-1}\iint_{\mathbb R^2}|u-v|^{r-1}k(u)k(v)\,du\,dv,\\
 B_A(r)&=2^{-r-3}\iint_{\mathbb R^2}|u-v|^{r-1}(u+v)^2k(u)k(v)\,du\,dv.
\end{aligned}                                                   \tag{3}
\]

For r=1 the factor |u-v|^0 is 1, including on the irrelevant diagonal.
Each integral is finite by the rapid decay and a polynomial majorant
of total degree at most four. It is positive, since its integrand is
strictly positive on an open rectangle away from its polynomial zero set.
Consequently the I's are finite and positive before any division.

Under (1), Tonelli's theorem for the positive integrand t^(r-1)h(bt)
applies even if an inverse moment of mu were initially infinite. For
each fixed b in (0,infinity), y=bt gives

\[
 I_A(r)=\int b^{-r}I_H(r)\,d\mu(b).
\]

The already proved 0<I_H(r)<infinity and finite I_A(r) force precisely
(2)'s moment identity and the finiteness of these three inverse moments.
No support bound, density, derivative interchange or compactification
is used. Zero and infinity are not points of the specified measure
space; no atoms there have been admitted.

This is the positive-real local specialization of the Mellin scale-product
identity in Denis Belomestny, Ekaterina Morozova and Vladimir Panov,
*Statistical Inference for Scale Mixture Models via Mellin Transform
Approach*, arXiv:2211.01799v2 (22 January 2024), Sections 1-2, equations
(1)-(3), [primary text](https://arxiv.org/html/2211.01799v2). We use Tonelli
to justify the different point-normalization here; no inversion theorem,
complex transform or nonvanishing condition is imported.

For these finite inverse moments, the shifted moment-matrix necessity
of Konrad Schmudgen, *Ten Lectures on the Moment Problem*,
arXiv:2008.12698v1 (28 August 2020), Lecture 1, subsection 3, Theorem 3.2 and the
polynomial-square argument preceding it,
[primary text](https://arxiv.org/html/2008.12698v1), gives (2). Explicitly,
the 2 by 2 matrix with rows (q1,q2) and (q2,q3) has quadratic form
integral b^(-1)(alpha+beta b^(-1))^2 dmu>=0. All terms are integrable by
the three finite moments above. Equivalently apply Cauchy-Schwarz to
b^(-1/2) and b^(-3/2). This explains the finite specialization, rather
than assuming all moments or invoking the all-order Stieltjes converse.

### Exact reduction of the numerical integrals

Odd moments of k vanish by evenness. Expanding (3) at r=1 and r=3 gives

\[
\begin{array}{ll}
 B_H(1)=M_0^2/4,&B_A(1)=M_0M_2/8,\\
 B_H(3)=M_0M_2/8,&B_A(3)=(M_0M_4-M_2^2)/32.
\end{array}                                                    \tag{4}
\]

For r=2 split the (u,v)-plane into its four quadrants and interchange
x,y in half the positive quadrant. On x>=y>=0, the two absolute-value
combinations are

\[
 |x-y|+(x+y)=2x,\qquad
 |x-y|(x+y)^2+(x+y)(x-y)^2=2x(x^2-y^2).
\]

With F_j(x)=integral_0^x y^j K(y)dy this yields exactly

\[
\begin{aligned}
 B_H(2)&=\int_0^\infty xK(x)F_0(x)\,dx,\\
 B_A(2)&=\frac14\int_0^\infty xK(x)
                         [x^2F_0(x)-F_2(x)]\,dx.             \tag{5}
\end{aligned}
\]

The bracket is nonnegative, as follows also from its integral
integral_0^x (x^2-y^2)K(y)dy. Finally

\[
 H(0)=2\int_0^\infty K(x)^2dx,\quad
 A(0)=2\int_0^\infty x^2K(x)^2dx,\quad
 q_r=\frac{B_A(r)}{B_H(r)}\frac{H(0)}{A(0)}.                 \tag{6}
\]

### Uniform theta remainder and spatial tails

For x>=0, L019's n-th summand is

\[
 T_n(x)=4e^{x/2}v(2v-3)e^{-v}>0,\qquad v=\pi n^2e^{2x}\ge3.
\]

Since e^(x/2)<=v and 2v-3<=2v, T_n<=8v^3e^(-v). The maximum of
v^3e^(-v/2) for v>=0 is 216e^(-3)<11. Also n^2>=1+3(n-1) for n>=1.
Thus the geometric sum gives, for all x>=0,

\[
 K(x)\le\frac{88}{1-e^{-9/2}}e^{-(3/2)e^{2x}}
       <90e^{-(3/2)e^{2x}}.                                \tag{7}
\]

For n>=5, v>=75. The function v^3e^(-v/4) decreases for v>=75,
and 75^3<e^(75/4), so T_n<=8e^(-3v/4)<=8e^(-9n^2/4).
Since n^2>=25+11(n-5),

\[
 0\le K(x)-\sum_{n=1}^4T_n(x)
 \le\frac{8e^{-225/4}}{1-e^{-99/4}}<10^{-22}                \tag{8}
\]

uniformly on the entire half-line. These generous constants are
checked with outward arithmetic in the certificate; no asymptotic
notation or unspecified onset enters the numerical proof.

For x=2+z>=2, e^4>50 and e^(2z)>=1+2z give from (7)

\[
 K(2+z)<90e^{-75}e^{-150z}<10^{-29}e^{-z}.                 \tag{9}
\]

Define the explicit rational integer

\[
 T_j=\sum_{l=0}^j {j\choose l}2^{j-l}l!
     =\int_0^\infty (z+2)^j e^{-z}\,dz.
\]

Then the tail of integral x^j K(x)dx after 2 is at most 10^(-29)T_j,
and that of integral x^j K(x)^2dx is at most 10^(-58)T_j, since
exp(-2z)<=exp(-z). Only j<=4 is needed. Also integral_0^infinity K<181:
(7) bounds its integral on [0,2] by 180, and (9) bounds the rest by
10^(-29). The missing x>=2 portions in (5) are bounded respectively by
181*10^(-29)T_1 and (181/4)*10^(-29)T_3. Indeed F0(x)<181 and
0<=x^2F0(x)-F2(x)<=181x^2. These include the inner y-tail as well;
when x<=2 its entire inner interval is already inside [0,2].

### Validated cell integration and arithmetic contract

Reproduction command, relative to this notebook:

    python3 scripts/theta-dilation/mellin_minor_758.py

The complete output is
scripts/theta-dilation/mellin-minor-certificate-758.json. Divide [0,2]
into N=262144 equal cells [l,r], h=2/N. On each cell independently
enclose exp(2x), exp(x/2), v=pi*n^2*exp(2x), and exp(-v) by interval
arithmetic, then evaluate the displayed T_n for n=1,...,4 and add the
interval [0,10^(-22)] from (8). This gives K_i^-<=K(x)<=K_i^+ on the
whole cell. All bounds are nonnegative. Monotonicity of K itself is
neither assumed nor used; repeated-variable interval overestimation
is retained. Store both K endpoints for every cell in the certificate.

Write J_{j,i} for the interval K_i*(r^(j+1)-l^(j+1))/(j+1). Sum these
for the half-moments. For the two normalizations use K_i^2 with the
same exact cell moments. For the triangular integrals in (5), cells
j<i contribute J_{1,i}*sum_{j<i}J_{0,j} to B_H(2), and
[J_{3,i}*sum_{j<i}J_{0,j}-J_{1,i}*sum_{j<i}J_{2,j}]/4 to B_A(2).
The subtraction is carried out as an interval subtraction: it does
not assume independence or replace a signed bound by its midpoint.

The remaining same-cell triangular contributions are enclosed by K_i^2
times the exact nonnegative polynomial integrals

\[
\begin{aligned}
 \int_l^r\int_l^x x\,dy\,dx&=lh^2/2+h^3/3,\\
 \int_l^r\int_l^x x(x^2-y^2)\,dy\,dx
       &=l^2h^3/3+5lh^4/12+2h^5/15.
\end{aligned}                                                  \tag{10}
\]

Divide the second by four for B_A(2). Thus the diagonal cells have
not been omitted or estimated by a possibly negative rectangle.
The disjoint rectangles and diagonal triangles partition x>=y on
[0,2]^2 except boundaries of measure zero. Adding the explicit tails
from (9) gives the complete, rather than truncated, integrals. Equations
(4) and (6) then produce the three ratios and the one determinant.
No quadrature convergence heuristic is used: interval ranges and exact
polynomial cell integrals already bound every cell's integration error.

Each interval endpoint is an integer multiple of 10^(-40). Addition,
negation, multiplication and division use exact Python integers with
outward floor/ceiling after every operation; division asserts a positive
denominator. Fractions entering the computation are exact rational
numbers before outward conversion. Pi is enclosed using Machin's formula
pi=16*arctan(1/5)-4*arctan(1/239), with respectively 64 and 20 terms of
the alternating series and the signed next term as remainder bounds.
For exponentials use Python Decimal.exp at precision 60, whose documented
contract is correct rounding with ROUND_HALF_EVEN; expand each result
by one neighboring Decimal value before outward conversion to the fixed
grid. The input endpoints have exact terminating representations of
fewer than 60 significant digits, so that conversion is exact here.
This is a software-arithmetic qualification of the computational proof,
not a claim of formal verification of Python. No hardware float or
unvalidated numerical quadrature enters the certificate.

The initial program invocation failed on an integer/interval division
operator before any numerical conclusion; its failure certificate is
preserved. The corrected N=65536 enclosure straddled zero and is retained
at scripts/theta-dilation/mellin-minor-coarse-65536-758.json. One refinement
to N=262144 is the final bounded attempt; there is no higher-minor search.
The final certificate reports PASS with no failures. Its full selected
normalization, Mellin-integral, ratio, determinant and analytic-check fields
were inspected, rather than inferred from bounded previews. Coarsened
outward displays of the ratio intervals are

\[
 q_1\in[0.939550,0.940426],\quad
 q_2\in[0.887227,0.888199],\quad
 q_3\in[0.841270,0.842346].
\]

The determinant computed from the stored forty-place intervals, before
these coarsened displays, is enclosed by

\[
 [0.0015191986019618917235861701872361743975,
  0.0049894578087557010390368559257683951152].
\]

All stored H(0),A(0),B_H(r),B_A(r) lower bounds are strictly positive.
The saved certificate's program digest, all 262144 cell endpoints and
nonnegative ordered K bounds, analytic-check results and claimed decimal
coarsening were checked in full, with no failures. The concise persisted
integrity report is scripts/theta-dilation/mellin-minor-integrity-758.json;
it also records the installed Decimal.exp/next_minus/next_plus documentation
contracts. These are integrity checks, not an independent mathematical audit.
This proves (11), under the stated software arithmetic contract, and ends
the single test. The initial coarse failure to decide is not hidden; it
was solely an integration-range enclosure issue, not a sign conclusion.
No second determinant, tail-comparison mechanism, mixture existence or
actual Fourier sign was tested. The subsequent independent audit760 is recorded below; the main RH
gap remains unchanged.


### Independent audit760 — 13 November 2026

The complete proof above was checked, including positivity before division,
the Jacobian and half-plane factor in (3), both moment expansions in (4),
all quadrant factors in (5), and the normalization in (6). Tonelli proves
finite inverse moments under the hypothetical law even with unbounded
support or scales approaching zero. The shifted two-by-two square uses
only these moments; no all-order moment converse is imported. Equations
(7)-(9) bound the full theta and spatial tails, including the inner integral
in (5). Direct integration of x=l+v, y=l+w, 0<=w<=v<=h gives both
polynomials in (10). No sign or factor discrepancy was found.

Reproduce the audit, preserving the original758 output, by

    python3 scripts/theta-dilation/mellin_minor_audit_760.py

It imports the unmodified program758 with a separate output path and
instruments every exponential input. The replay certificate is
scripts/theta-dilation/mellin-minor-replay-760.json; its bytes equal the
original, whose SHA256 remains
f9b74f64effaae714a2bebdb33eb677695ea68b7ae2fb195b60e90be88cf4a1f.
The complete audit is scripts/theta-dilation/mellin-minor-audit-760.json.
All 1,572,873 exponential calls have input raw integers of at most 44
digits, hence exact conversion and division by S=10^40 at precision60.
Their arguments lie strictly between -10000 and 10000. The inherited
context has Emin=-999999, Emax=999999, clamp=0; the exponentials and their
neighbors are normal, finite and far from the exponent limits. Multiplying
by the exact power of ten S merely shifts the exponent and is exact at
precision60. Thus the neighboring correctly rounded exponentials followed
by floor/ceiling enclose the true values; neither subnormal rounding nor
inexact input conversion invalidates the stated contract. The integer
interval operations use all endpoint products, outward reciprocal bounds
for positive denominators, and correct signed floor/ceiling. The alternating
arctangent remainders and the negative coefficient of the second arctangent
in Machin's formula have the correct endpoint directions.

A second accumulator checks every saved cell endpoint and nonnegative K
bound, then integrates its lower and upper step functions with exact
integer sums and rational arithmetic, without program758's intermediate
grid rounding. For clarity, put d=N/2=131072, so cell i is
[i/d,(i+1)/d], and let k_i denote either sequence of raw lower or upper
K endpoints (actual step value k_i/S). Put
Delta_{j,i}=(i+1)^(j+1)-i^(j+1),
f_{0,i}=sum_{m<i}k_m and
f_{2,i}=sum_{m<i}k_m Delta_{2,m}.
The half-moments are exactly
sum_i k_i Delta_{j,i}/[S(j+1)d^(j+1)]; their squared-kernel analogues
replace k_i/S by k_i^2/S^2. For these same step functions the finite
triangular integrals in (5) are exactly

\[
\begin{aligned}
 B_{H,[0,2]}(2)&=
 \frac{\sum_i[3k_i(2i+1)f_{0,i}+k_i^2(3i+2)]}{6S^2d^3},\\
 B_{A,[0,2]}(2)&=
 \frac{\sum_i[15k_i\Delta_{3,i}f_{0,i}
 -10k_i(2i+1)f_{2,i}+k_i^2(20i^2+25i+8)]}{240S^2d^5}.
\end{aligned}
\]

These follow by substituting the exact cell monomial integrals and (10)
into the off-diagonal rectangles and diagonal triangles. Although the
second sum contains a subtraction, its underlying integrand
x(x^2-y^2)K(x)K(y)/4 is nonnegative on 0<=y<=x. Therefore evaluating
all lower step bounds gives a lower bound and all upper step bounds an
upper bound. This monotonicity justifies the independent accumulator;
it does not assume that separate signed interval terms are independent.
The same full tails (9) are then added to the upper endpoints. Equations
(4) and (6) are evaluated with exact rational interval arithmetic.

Every independent half-moment, normalization, Mellin integral and ratio
interval is contained in its original758 interval. All required lower
bounds are positive. The independent interval for this same D is

\[
[0.0016312243057720831734521591789581386715,
 0.0048776241765432137140145005044016300414],
\]

contained in the original interval. All analytic, partition, equality and
containment checks passed; there are no failures. The complete relevant
stored values and audit checks were inspected, not inferred from a preview.
This validates the existing finite pass (11) under the stated Python
arithmetic contract. The independent accumulation is a verification of
the same minor, not a second diagnostic or a mixture construction. No
formal verification of Python, actual Fourier sign, higher positivity,
or progress beyond the cited general moment mechanism is claimed.

## Mathlib

Full matching or supporting coverage has not been checked. No absence
or formalization is claimed. The Mellin and moment statements above
are cited mathematical inputs; the interval computation additionally
uses the stated Python arithmetic contract. General reference:
https://leanprover-community.github.io/mathlib4_docs/
