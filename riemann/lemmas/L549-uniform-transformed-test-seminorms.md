# L549 — Uniform transformed-test seminorms

## Hypotheses

Use the analytic test class and kernel normalization of L548 (6).
Precisely, V is a complex-valued C^infinity function on (0,infinity).
Writing D=x d/dx, for every integer r>=0 and every N>0,
D^r V(x)=O_(r,N)(x^N) as x decreases to zero and
D^r V(x)=O_(r,N)(x^(-N)) as x tends to infinity. Put

\[
 \widehat V(z)=\int_0^\infty V(x)x^z\frac{dx}{x},\qquad
 K=(2\pi)^4/27,\qquad
 R(t)=\prod_{a\in\{5/6,7/6\}}
               \frac{\Gamma(a+t)}{\Gamma(a-t)},
 \qquad
 V^\sharp(x)=\frac1{2\pi i}\int_{(0)}
                   \widehat V(-t)R(t)(Kx)^{-t}\,dt.       \tag{1}
\]

The quotient uses the entire reciprocal denominator gamma factors.
For real A>=0 and an integer B>=0 define

\[
 \begin{split}
 \mathfrak M_{A,B}(V)
  &=\sup_{-A\le\eta\le1/4}\int_{\mathbb R}
                    (1+|u|)^B|\widehat V(\eta+iu)|\,du,\\
 w_A(x)&=1+x^{-A}+x^{1/4},\qquad
 m_A(x)=\min\{x^{1/4},(1+x)^{-A}\}.
 \end{split}
\]

The nonnegative integers j,J and the cutoff chi in C_c^infinity(0,infinity)
are fixed when asserting the respective uniform estimates. No arithmetic
hypothesis of L548 is required for this analytic kernel result. Those
hypotheses remain necessary for its arithmetic reflection identity.

## Conclusion

The integral (1) is absolutely convergent, defines a smooth function,
and is unchanged if its line is replaced by any sigma>=-1/4. For x,Y>0,

\[
 |D^j V^\sharp(x)|\le C_{A,j}\,m_A(x)
                    \mathfrak M_{A,\lceil4A\rceil+j+2}(V),       \tag{2}
\]

\[
 \int_{\mathbb R}(1+|u|)^J
   \left|\int_0^\infty\chi(y)V^\sharp(Yy)y^{-iu}\frac{dy}{y}\right|du
 \le C_{A,J,\chi}\,m_A(Y)
                    \mathfrak M_{A,\lceil4A\rceil+J+4}(V).      \tag{3}
\]

These input seminorms are finite, with

\[
 \mathfrak M_{A,B}(V)\le C_{A,B}
       \int_0^\infty w_A(x)
          \bigl(|V(x)|+|D^{B+2}V(x)|\bigr)\frac{dx}{x}.          \tag{4}
\]

For real u_0, V_(u_0)(x)=x^(iu_0)V(x) belongs to the same test class and

\[
 \mathfrak M_{A,B}(V_{u_0})
       \le(1+|u_0|)^B\mathfrak M_{A,B}(V).                      \tag{5}
\]

All constants are independent of V, x,Y,u_0 and the arithmetic labels
in L548/L541; dependence on V and u_0 is displayed. They may depend on
the fixed orders and cutoff specified in (2)–(4); K is the fixed number
in (1). In particular A=0 is included. A moving family of V still needs
bounds for the displayed norms. No bound uniform in all derivative
orders, in a moving cutoff or in A is asserted.

This verifies the kernel portion of L541 Hypothesis 1, and its bound
for C_A in (12). It does not verify L541's joint common-profile estimate,
common-density Minkowski application, lattice-tail summation, marked
expansion, arithmetic estimates or global closure, and gives no Xi sign.

## Proof

### Citation and purpose

The estimate is already stated in OpenAI, *The Quasi-Riemann Hypothesis*,
30 September 2026, Proposition `prop:completed-reflection`, equations
`eq:reflection-kernel`, `eq:reflection-annular-fourier` and
`eq:reflection-test-seminorm`,
[build/paper.tex at commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
The precise statement is at lines 1727–1755; its proof is at 2261–2314.
The test hypotheses and transform are at 1600–1629. The saved SPECIALIZE
assessment covers exactly this interface. This proof checks a retained
local contract, reproducing the known bound rather than claiming a new
transform or stronger estimate.

Import the analytic properties of gamma and reciprocal gamma from
NIST DLMF [5.2(i), paragraph after 5.2.1](https://dlmf.nist.gov/5.2#i),
and the modulus asymptotic
[5.11.9](https://dlmf.nist.gov/5.11.E9), including its uniformity for
bounded real parts and both signs of the imaginary part. The assessment
records DLMF 1.2.8; these statements were also retrieved in this audit.
No theta, coefficient, Gauss or arithmetic bound enters the proof below.

### Mellin control with finite input orders

For eta in [-A,1/4], x^eta<=w_A(x). The two-endpoint hypotheses imply
that every integral of w_A(x)|D^r V(x)| dx/x is finite, and that
x^eta D^r V(x) tends to zero at both endpoints, uniformly on this eta
interval. This follows by using decay exponents greater than A+1 at
zero and greater than 5/4 at infinity. Inserting any fixed power of
|log x| remains integrable, by increasing the decay exponent if needed.
Dominated differentiation in z on each compact set therefore makes
Vhat entire.

For z=eta+iu!=0, integration by parts with D and measure dx/x gives,
for every positive integer N,

\[
 \widehat V(z)=(-z)^{-N}
                 \int_0^\infty D^N V(x)x^z\frac{dx}{x}.         \tag{6}
\]

Every boundary term just described vanishes. For |u|>=1, (6) and
|eta+iu|>=|u| bound Vhat by
|u|^(-N) integral w_A|D^N V| dx/x, uniformly in eta. For |u|<=1 the
defining integral is bounded by integral w_A|V| dx/x, without dividing
by z. Taking N=B+2 proves (4), since

\[
 \int_{|u|\ge1}(1+|u|)^B|u|^{-B-2}\,du<\infty.
\]

This also proves pointwise rapid decay on the entire Mellin strip,
with a finite weighted input integral for each requested decay order.
The special point z=0 causes no loss. The argument applies on any
compact real strip by replacing w_A by the corresponding endpoint
weights.

### Gamma quotient and justified contour operations

The numerator poles are t=-5/6-n and t=-7/6-n, n>=0. Thus R is
holomorphic on Re(t)>-5/6. A pole of a denominator gamma factor is a
zero of its reciprocal, not a pole of R. For -1/4<=sigma<=A and large
|u|, DLMF 5.11.9 gives, uniformly in sigma,

\[
 |\Gamma(a+\sigma+iu)|\asymp_A
 |u|^{a+\sigma-1/2}e^{-\pi|u|/2},\qquad
 |\Gamma(a-\sigma-iu)|\asymp_A
 |u|^{a-\sigma-1/2}e^{-\pi|u|/2}.
\]

The real parts lie in bounded intervals even when A exceeds a.
Each quotient has power 2sigma and the product has power 4sigma.
On the remaining compact rectangle, the function
|R(sigma+iu)|(1+|u|)^(-4sigma) is continuous and bounded, including
all zeros of reciprocal gamma. Consequently

\[
 |R(\sigma+iu)|\le C_A(1+|u|)^{4\sigma}
          \quad(-1/4\le\sigma\le A, u\in\mathbb R).          \tag{7}
\]

For fixed j, the differentiated integrand has factor (-t)^j.
On this strip its absolute value is bounded by a constant times
(Kx)^(-sigma)(1+|u|)^(4A+j)|Vhat(-sigma-iu)|.
The preceding pointwise Mellin estimate makes this integrable,
locally uniformly in x>0. It also dominates the next x derivative
on each compact x interval by choosing a larger finite N. Thus
dominated differentiation proves smoothness and the formula with
(-t)^j for every fixed j.

For contour joins at heights +/-H, H>=1, choose N>4A+j+1 in (6).
The joined segment has bounded length; its integrand is
O_(A,j,x,V)(H^(4A+j-N)), uniformly along the segment. Here x can
range in any fixed compact subset of (0,infinity). The joins tend
to zero. Cauchy's theorem, with no enclosed pole, then identifies
the integrals on any two lines in [-1/4,A]. Letting A be any fixed
number containing the desired lines proves the asserted line
independence, including the original line zero. In checking the
joins and the jth differentiation, N=ceil(4A)+j+4 already suffices;
this is B+2 for the norm in (2). Hence these operations do not require
an unrecorded uniform higher-derivative cost.

### Endpoint bounds, including A=0

Set B=ceil(4A)+j+2. For sigma=-1/4,0,A, (7) and
|sigma+iu|^j<=C_(A,j)(1+|u|)^j imply

\[
 |D^j V^\sharp(x)|
 \le C_{A,j}x^{-\sigma}
    \int_{\mathbb R}(1+|u|)^B
                       |\widehat V(-\sigma-iu)|\,du
 \le C_{A,j}x^{-\sigma}\mathfrak M_{A,B}(V).             \tag{8}
\]

The real arguments -sigma belong to [-A,1/4], and reversal of u does
not change its absolute weight. K^(-sigma) is absorbed into the fixed
constant. Combining the three estimates gives the factor
min{x^(1/4),1,x^(-A)}. For x<=1, 1<=(2/(1+x))^A; for x>=1,
x^(-A)<=2^A(1+x)^(-A). Thus the combined factor is at most
2^A m_A(x), proving (2). When A=0 the two nonnegative lines coincide
and this proof gives exactly min{x^(1/4),1}; no positive A or division
by A was used.

### Annular Fourier bound

If chi is zero, (3) is immediate. Otherwise choose 0<a<b<infinity
containing its support and put f_Y(v)=chi(e^v)Vsharp(Ye^v).
This is smooth and supported in the fixed interval [log a,log b].
With F_Y(u)=integral f_Y(v)e^(-iuv) dv, the change y=e^v identifies
F_Y with the inner integral of (3). For |u|<=1 use
|F_Y(u)|<=||f_Y||_1. For |u|>=1, integrate J+2 times by parts;
compact support eliminates boundary terms and gives
|F_Y(u)|<=|u|^(-J-2)||f_Y^(J+2)||_1. Therefore

\[
 \int_{\mathbb R}(1+|u|)^J|F_Y(u)|\,du
       \le C_J\bigl(\|f_Y\|_1+\|f_Y^{(J+2)}\|_1\bigr).       \tag{9}
\]

Leibniz's rule expresses each derivative on the right using
(D^r chi)(e^v) and (D^k Vsharp)(Ye^v), with k<=J+2.
For a<=e^v<=b,

\[
 m_A(Ye^v)\le
       \max\{b^{1/4},\min(1,a)^{-A}\}\,m_A(Y),                \tag{10}
\]

because each of the two terms defining the first minimum is bounded
by the corresponding term defining the second, with these constants.
Also M_(A,B) is nondecreasing in the integer B. Apply (2) to each
Leibniz term with the common order B=ceil(4A)+J+4, integrate over the
fixed interval and use (9). This proves (3). Only finitely many cutoff
derivatives, up to J+2, are used; they are part of C_(A,J,chi).

### Pure twists, constant dependencies and application limit

The identity D^r(x^(iu_0)V)=x^(iu_0)(D+iu_0)^r V shows admissibility
for each real u_0. Directly in the absolutely convergent Mellin integral,

\[
 \widehat {V_{u_0}}(\eta+iu)=\widehat V(\eta+i(u+u_0)).
\]

Substitute v=u+u_0 and use
1+|v-u_0|<=(1+|u_0|)(1+|v|) before taking the eta supremum.
This proves (5), including B=0. It yields polynomial twist costs of
orders ceil(4A)+j+2 and ceil(4A)+J+4 respectively in (2) and (3).
Using (5) directly avoids introducing the larger derivative cost that
would result from first applying (4) to the twisted input.

All steps used only the fixed analytic parameters, the displayed
seminorms and the fixed cutoff. For j=0 and x>=1, (2) supplies
|Vsharp(x)|<=C_A M_(A,ceil(4A)+2)(V)x^(-A), precisely the kernel
premise accompanying L541 (12). For A=0 it supplies the scalar
min{x^(1/4),1} used in that lemma's retained-dyad analysis. Passing
from this one-variable statement to a joint profile and a common
row measure remains a separate proof obligation. Nor does shifting
an individual kernel authorize a dual-series/integral interchange on
Re(t)=0; L548 justifies that exchange on Re(t)>1/2. There is no
all-height or signed-Xi conclusion.

## Mathlib

Full matching coverage has not been checked. The imported gamma facts
are the precise DLMF statements above. No claim that Mathlib contains
or lacks this full transform theorem is made.
