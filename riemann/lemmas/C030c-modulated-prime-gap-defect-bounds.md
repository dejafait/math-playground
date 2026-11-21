# Corollary C030c: uniform quantitative detection of a finite arithmetic defect

## Hypotheses

Set a=4/5, b=9/10 and define the fixed mass-one bump

\[
 Z=\int_a^b\exp\!\left(-\frac1{(x-a)(b-x)}\right)dx,\qquad
 \chi(x)=\begin{cases}
 Z^{-1}\exp\!\left(-\frac1{(x-a)(b-x)}\right),&a<x<b,\\
 0,&\text{otherwise}.
 \end{cases}
\]

Let A,B be real, 0<=B-A<=2, and g=(A+B)/2. Put

\[
 K(x)=2\cosh(x/4)\cos(gx)-\cos(Ax)-\cos(Bx),\qquad
 \eta_g(x)=\chi(|x|)\cos(gx),
\]
\[
 h_g(r)=\int_{\mathbb R}\eta_g(x)e^{irx}dx,\qquad
 \phi_g(z)=h_g(\sqrt z).
\]

The last expression is defined by the entire even power series of h_g,
not by a choice of square-root branch. Write

\[
 N_j=\int_a^b|\chi^{(j)}(x)|dx\quad(0\le j\le3),\qquad N_0=1,
\]
\[
 m=\cosh(1/5)-1,\qquad
 M=(\cosh(9/40)+1)N_1+\tfrac14\sinh(9/40)+1,
\]
\[
 c_\chi=\frac m2,\qquad
 G_\chi=\max\{1000,\lceil M/m\rceil\},\qquad
 C_\chi=2e^{27/40}(11/4)^{9/4}(N_0+3N_1+3N_2+N_3).
 \tag{1}
\]

For interpreting K as a genuine spectral surgery, assume additionally
that iA,-iA and iB,-iB are the exact line-zero occurrences removed
from the normalized function xi(1/2+s)/xi(1/2). If A=B, two occurrences
at each of iA and -iA are required. Insert the quartet s=+-1/4+-ig, with multiplicities.
These extra assumptions are unnecessary for the displayed integral
and norm estimates. No existence of such zero occurrences at every
height is asserted.

## Conclusion

For every such A,B with g>=G_chi,

\[
 I_g:=\int_0^\infty\eta_g(x)K(x)dx\ \ge c_\chi>0,\qquad
 \|h_g\|_{1/4}:=
 \sup_{|\operatorname{Im}r|\le3/4}(1+|r|)^{9/4}|h_g(r)|
 \ \le C_\chi(1+g)^3.
 \tag{2}
\]

All constants are explicit in finitely many specified derivative L1
norms of the prescribed bump and are independent of A,B,g. In fact
c_chi>=1/100. Both h_g and phi_g are entire, h_g is even, and phi_g
belongs to Polson's test class T with delta=1/4. Its inverse transform
in that source's convention is exactly eta_g.

Under the extra zero-occurrence assumptions, the change in the full
zero sum tested against h_g is 4 I_g, and the change in the
reflection-paired half sum tested against phi_g is 2 I_g. The signed
arithmetic measure changes by -2K(x)dx on x>0. This measure's pairing
against eta_g is -2 I_g, while the pairing against any locally finite measure
supported on {log n:n>=2} is zero. Thus the fixed probes quantitatively
distinguish the finite surgery with the stated polynomial norm cost.

This is a quantitative specialization of a known qualitative support
defect. It is neither a positivity result for the actual Xi mixed form
of L030 nor a polynomial-square representation. It gives no exclusion
of infinite coordinated perturbations and no common-graph realization.
It does not assert that the original A,B in (1000,2000] meet (1).

## Proof

### Source inputs and reason for the calculation

Nicholas G. Polson, *On Hilbert's 8th Problem*,
[arXiv:1708.02653v24, September 2026](https://arxiv.org/pdf/1708.02653v24),
Definition 9.1 and Proposition 9.3, printed pp30-31, specify the even
strip-holomorphic test class and the norm used in (2). Theorem 12.2(vi),
equation (53), printed p37, and its Fourier/support proof on p38 give
the finite-surgery defect -2K dx and its qualitative detection by
compactly supported tests in logarithmic gaps. We import that source
interpretation with exact removed zero occurrences; we do not reprove
its heat-trace stability claims. The calculation below adds the
explicit constants and height-uniform estimates for the fixed family,
which that qualitative detection argument does not supply.

Fourier inversion is the standard Schwartz inversion theorem, e.g.
Terence Tao, [*245C, Notes 2: The Fourier transform*, 6 April 2009](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/),
Section 3, equation (11), with compact-support smoothness/decay as in
Example 33 and Exercise 38. That source uses a 2pi exponent; our
inversion is eta(x)=(2pi)^(-1) integral h(r) exp(-irx) dr.
The strip estimates below are proved directly, since real-axis
Schwartz decay alone would not bound the source norm.

### Smoothness and support

The integral Z is finite and strictly positive. The function chi is
C_c^infinity(R), nonnegative and of integral one. To check smoothness
at an endpoint, differentiation on (a,b) produces finitely many
products of powers of (x-a)^(-1), (b-x)^(-1) and the same exponential.
For every nonnegative integer k, t^(-k)e^(-1/t) tends to zero as
t decreases to zero. Since (x-a)(b-x) vanishes linearly at each
endpoint, every one-sided derivative tends to zero. Extension by
zero therefore has all derivatives zero at the endpoints. In
particular all N_j in (1) are finite and all integrations by parts
below have zero boundary terms.

The support [a,b] lies strictly in (log2,log3):
e^(4/5)>1+4/5+(4/5)^2/2>2, while e^(9/10)<e<3. The last inequality
follows from the exponential series and n!>=2^(n-1) for n>=2, with
strict inequality for n>=3. Consequently eta_g vanishes at every
log n, n>=2. Its even extension is smooth at zero since it vanishes
on a neighborhood of zero.

### Uniform positive signal

Let d=(B-A)/2, so 0<=d<=1 and A=g-d, B=g+d. The cosine addition
identity gives, for every real x,

\[
 K(x)=2[\cosh(x/4)-\cos(dx)]\cos(gx).
\]

Define W_d(x)=chi(x)[cosh(x/4)-cos(dx)] on the real line. On [a,b]
the bracket is at least cosh(a/4)-1=m>0. Hence

\[
 \int_a^bW_d(x)dx\ge m.
 \tag{3}
\]

The product rule, |cos(dx)|<=1, d<=1 and N_0=1 give

\[
 \begin{split}
 \|W_d'\|_1
 &\le(\cosh(b/4)+1)N_1
       +(\tfrac14\sinh(b/4)+1)N_0=M.
 \end{split}
 \tag{4}
\]

For g>0, a single integration by parts yields the uniform estimate

\[
 \left|\int_a^bW_d(x)\cos(2gx)dx\right|
 \le\frac{\|W_d'\|_1}{2g}\le\frac M{2g}.
 \tag{5}
\]

Using 2cos^2(gx)=1+cos(2gx), (3)-(5) imply

\[
 I_g=\int_a^b W_d(x)[1+\cos(2gx)]dx
 \ge m-\frac M{2g}\ge\frac m2
 \quad(g\ge G_\chi).
\]

There is no existential Riemann-Lebesgue onset in this estimate.
Since cosh t>=1+t^2/2, m>=1/50 and c_chi>=1/100.
The coincident-occurrence case d=0 is included throughout.

### Entire extension and the fixed strip norm

Set E(x)=chi(|x|). For 0<=j<=3 its derivative L1 norm on R is
2N_j; reflection changes only a derivative's sign. The compact
support implies that the integral defining h_g is entire, by
uniform domination of every differentiated integrand on compact
sets of r. Evenness follows by replacing x with -x. More explicitly,

\[
 h_g(r)=2\sum_{k=0}^\infty\frac{(-1)^k r^{2k}}{(2k)!}
          \int_a^b\chi(x)\cos(gx)x^{2k}dx.
 \tag{6}
\]

The coefficient integrals have absolute value at most b^(2k).
Thus (6) converges locally uniformly, and replacing r^(2k) by z^k
also gives an entire function. This defines phi_g unambiguously.

Put s_0=3/4, write r=t+iy with |y|<=s_0, and set
f_(g,y)(x)=exp(-yx)E(x)cos(gx). For every integer k>=0,

\[
 \left|\frac{d^k}{dx^k}(e^{-yx}\cos(gx))\right|
 \le e^{-yx}(g+|y|)^k
 \le e^{s_0 b}(1+g)^k
\]

on the support of E, since g>=0 and s_0<1. This follows by taking
the real part of (-y+ig)^k exp((-y+ig)x). The product rule gives

\[
 \|f_{g,y}^{(3)}\|_1
 \le2e^{s_0b}\sum_{j=0}^3\binom3j N_j(1+g)^{3-j}
 \le D_\chi(1+g)^3,
\]
\[
 D_\chi=2e^{27/40}(N_0+3N_1+3N_2+N_3).
 \tag{7}
\]

Also ||f_(g,y)||_1<=2e^(27/40)N_0<=D_chi. Since
h_g(t+iy)=integral f_(g,y)(x) exp(itx) dx, three integrations by
parts show

\[
 |h_g(t+iy)|\le D_\chi(1+g)^3|t|^{-3}\quad(t\ne0).
 \tag{8}
\]

For |t|<=1, the direct integral bound and
1+|t+iy|<=1+|t|+|y|<=11/4 give (2). For |t|>1,

\[
 1+|t+iy|\le(11/4)|t|,
\]

so (8) bounds the weighted quantity in (2) by
D_chi(11/4)^(9/4)(1+g)^3 |t|^(-3/4), at most the stated constant.
This proves the supremum estimate on the closed strip, not just its
real axis. It also proves the O((1+|r|)^(-9/4)) strip decay, for each
fixed g, required by Definition 9.1 with delta=1/4. Entire h_g gives
holomorphicity on an open neighborhood of that strip.

The same compact-support argument with arbitrary derivative order
gives real-axis Schwartz decay of h_g and its derivatives; alternatively
this is the standard transform of the Schwartz function eta_g.
Schwartz Fourier inversion in the convention stated above proves
that the source inverse transform is exactly eta_g: in Tao's notation,
h_g(r)=hat(eta_g)(-r/(2pi)), and substituting r=-2pi*xi in our inverse
integral gives his equation (11). Compact support
also makes every displayed defect pairing absolutely convergent.

### The normalization factors and arithmetic detection

In the r variable, the inserted quartet is
{g+i/4, g-i/4, -g+i/4, -g-i/4}; the removed occurrences are
{A,-A,B,-B}. Their full test-sum difference is

\[
 \Delta_{\rm full}
 =2h_g(g+i/4)+2h_g(g-i/4)-2h_g(A)-2h_g(B).
\]

From the even integral h_g(r)=2 integral_0^infinity eta_g(x)cos(rx)dx
and cos(u+iv)+cos(u-iv)=2cos(u)cosh(v), this is exactly

\[
 \Delta_{\rm full}=4\int_0^\infty\eta_g(x)K(x)dx=4I_g.
 \tag{9}
\]

Each reflection pair has a single squared exponent. Its sum against
phi_g is half the even full sum, so Delta_pair=2I_g. This counts a
repeated removed zero twice when A=B and requires the multiplicities
stated in the hypotheses. When the admissible source zero sums are
used, their absolute convergence follows from the source's zero count
N(T)=O(T log T) and the closed-strip decay: the shell 2^k<=|Re r|<2^(k+1)
contributes O((k+1)2^(-5k/4)) for fixed g. Finite surgery preserves
that convergence. Unchanged occurrences cancel and give precisely this finite
difference; no change of summation convention or limiting exchange
is used to obtain (9).

The source full explicit formula has arithmetic term
-2 integral_0^infinity eta_g dmu; the half formula has coefficient
-1. Therefore mu_F-mu=-2K dx produces respectively 4I_g and 2I_g,
as required. The measure change itself pairs to -2I_g, with that
negative sign. A logarithm-supported measure pairs to zero because
eta_g vanishes on its support. This comparison does not require
positivity of the signed eta_g or any sign of the full arithmetic
functional. The quantitative separation is at least 2c_chi at the
measure level and 4c_chi at the full-sum level, with the cost (2).

For completeness, the source's construction applies to the ordinates
in this statement by setting w=1/4+ig and

\[
 F(s)=\frac{\xi(1/2+s)}{\xi(1/2)}
 \frac{(1-s^2/w^2)(1-s^2/\bar w^2)}
      {(1+s^2/A^2)(1+s^2/B^2)}.
\]

Here A=g-d>=999 and B=g+d>0. At every denominator root the assumed
zero occurrence cancels the corresponding factor; if A=B the
denominator has order two at each root and the stated multiplicity
cancels both. Thus every apparent pole is removable and F is entire.
The numerator inserts exactly the stated quartet. The finite spectral
difference (9) and its arithmetic interpretation therefore remain
valid without an upper bound of 2000 on A,B. This extends only the
finite-divisor construction and its formula; no heat-stability claim
from the source's original height interval is being imported.

The zero-occurrence hypotheses are essential only for realizing this
finite change by the entire function F. The estimates (1)-(8)
are valid for every real A,B in the specified parameter domain. No
claim of an unconditional surgery at every g>=G_chi, or of stability
of any heat block at those heights, is part of this corollary.

### Audit1120 — 16 November 2026

The independent replay accepts (1)-(9) with the stated constants.
Endpoint flatness makes all boundary terms zero. The signal uses
g>=ceil(M/m), hence M/(2g)<=m/2, including d=0. For the strip,
s_0 b=27/40, g+|y|<=1+g and the binomial coefficients in (7) are
1,3,3,1. The direct bound covers |t|<=1; for |t|>1 the remaining
power is |t|^(-3/4)<=1. The entire power series and the Fourier
rescaling above give the required test class with delta=1/4.
The quartet contributes four evaluations with multiplicity, the two
removed reflection pairs contribute four, and halving the full sum
gives exactly 2I_g. The measure defect pairs to -2I_g, with no sign
change suppressed. These checks accept the quantitative specialization,
not a new qualitative support obstruction or an actual-Xi sign theorem.
The audit corrects the source page references (equation (53) on p37,
support proof on p38) and makes arbitrary-height quotient cancellation
explicit. No inequality, threshold, or parameter domain is weakened.

## Mathlib

Matching coverage for the full quantitative statement, the source's
surgery formula and its test class has not been checked; availability
is unknown. Supporting real/complex Fourier, smooth bump and entire
power-series results are also not checked here. No formalization or
absence claim is made. Reference:
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
