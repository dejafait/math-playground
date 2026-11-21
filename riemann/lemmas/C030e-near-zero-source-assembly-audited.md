# Corollary C030e: audit of the near-zero source assembly

## Hypotheses

Let N>=1 be an integer, epsilon in {0,1}, and p(X)=sum_(i=0)^(N-1)
v_i X^i with real coefficients, allowing p=0. Set q(x)=x^epsilon p(x^2),
so deg(q)<=2N-1, and use the unnormalized norm
||q||_G^2=integral_R e^(-x^2)|q(x)|^2 dx. Let 0<t<=log(2)/180.
Spectral and complex polynomial squares mean algebraic squares.

Use the actual nontrivial zeta zeros with multiplicity. Put
gamma_rho=-i(rho-1/2), a_k=gamma_rho^2 for one representative of each
reflection pair {rho,1-rho}. Import the unconditional Guinand-Weil
explicit formula from E. Carneiro and M. B. Milinovich,
*On Littlewood's Estimate for the Modulus of the Zeta Function on the
Critical Line*, Constructive Theory of Functions, Lozenets2023,
Professor Marin Drinov Publishing House of BAS, Sofia,2024, pp1-16,
[Section2.2, Lemma2.2, p7; Fourier convention Section2.1, p5](https://www.math.bas.bg/mathmod/Proceedings_CTF/CTF-2023/files_CTF-2023/05-Carneiro-Milinovich.pdf#page=7).
The same theorem is [arXiv:2403.17803v1, 26March2024, Lemma4,
p5](https://arxiv.org/pdf/2403.17803v1#page=5).

Precisely, h is holomorphic on a strip |Im z|<1/2+eta for some
eta>0 and satisfies uniform horizontal decay
O((1+|z|)^(-1-delta)) there for some delta>0. With
hhat(y)=integral_R h(r)e^(-2*pi*i*r*y)dr, the theorem states

    sum_rho h((rho-1/2)/i)
      = h(1/(2i))+h(-1/(2i)) - hhat(0)log(pi)/(2*pi)
        + integral_R h(r)Re psi(1/4+ir/2)dr/(2*pi)
        - sum_(n>=2) Lambda(n)n^(-1/2)
            [hhat(log(n)/(2*pi))+hhat(-log(n)/(2*pi))]/(2*pi).

The zero sum uses the standard multiplicity convention: sum over all
nontrivial zeros, including off-line zeros, with each occurrence counted.
It is not a sum over distinct real ordinates. The displayed source
statement does not separately spell out multiplicity; the zero-sum
notation has this usual convention. No RH, simplicity or bandlimitedness
hypothesis is imposed by this lemma. Its later RH-dependent applications
are not imported. Its proof cites Iwaniec-Kowalski, *Analytic Number
Theory* (2004), Theorem5.12; that book chapter/number and an independent
contour proof have not been checked here. The precise accessible theorem
above is the standard input, rather than a certified book-number correction.

The original assembly used Nicholas G. Polson, *On Hilbert's 8th
Problem*, arXiv:1708.02653v24, 11September2026, Section4.3/(3), p8,
for this identity, and Definition5.1/(4) and Lemma5.2, pp8-9, for
W(t)=sum_k e^(-a_k t)=(1/2)sum_rho e^(-gamma_rho^2 t), its absolute
locally uniform convergence on Re t>0, differentiation and reality.
The latter properties are supplied locally by C030g below. No
large-time/first-zero assertion is imported.

The third original source input, Lemma6.1's bounds m(r)>=-6 on R
and m(r)>1 for |r|>=20, is now independently proved in C030f,
including its series/Binet constants (audit1188). Use that local
result together with the explicit formula and heat-series audit below.

The heat series' convergence, differentiation, reality and half-spectrum convention
are now independently checked in C030g (audit1190), using the unconditional
multiplicity-weighted zero count and Weierstrass theorem. Use that local
result in place of the corresponding Polson source-proof import; its
large-time and endpoint assertions remain excluded. The explicit formula
is a named standard import, not an independent contour-proof certification.
No critical-line assumption enters the spectral identity. C030d supplies the already
audited Gaussian bounds (23)-(25).

Define c_j(t)=(-1)^j W^(j)(t) and the source's equation(22) form

\[
 Q_{N,t}^{\epsilon}(p)=4\pi t^{\epsilon+1/2}
 \sum_{i,j=0}^{N-1}v_i v_j t^{i+j}c_{i+j+\epsilon}(t).
\]

This is the source heat form, not the local Q of L030. Put
r_N=1-1/(2N), C_N=r_N^(-(2N-1))/(sqrt(pi)*sqrt(1-r_N^2));
C030d gives 0<C_N<2sqrt(N).

## Conclusion

Relative to these imports, Polson v24
[Lemma7.7/(26), printed pp19-20](https://arxiv.org/pdf/1708.02653v24#page=19)
passes the assembly audit:

\[
 Q_{N,t}^{\epsilon}(p)\ge\eta_N(t)\|q\|_G^2,\qquad
 \eta_N(t)=1-280C_N\sqrt t-4\pi C_N\sqrt t\,e^{(4N-1)t/4}
              -\frac{4^N}{48}e^{-(\log2)^2/(24t)}.       \tag{26}
\]

The displayed eta_N is strictly decreasing for t>0. With
tau_N=1/(4000000N),

\[
 \eta_N(\tau_N)>0.706>0.7\quad(N\ge1),\qquad
 \eta_3(10^{-6})>0.2558>1/4.
\]

Both times are in the required domain. These decimals only spell out
the slack in the source's error thresholds; no improved-source claim
is made. The estimates cover all coefficients and both parities,
without finite zero verification. For p nonzero the source heat form
is positive throughout the corresponding near-zero intervals.
The intervals depend on N: this is neither all-degree positivity at
a fixed positive time nor the full criterion L030-L032/C032a or RH.
The far-time argument and the transfer in C030a/C030b are not premises
or audited conclusions here.

## Proof

The assembly is REPRODUCTION for reliability of C030b's near-zero source
input, not a new arithmetic sign mechanism. Assessment1184 approved that
scope before the audit. The citation/applicability repair1192 is
KNOWN_IMPORTED under assessment1190's covered target; it changes neither
the identity nor the bounds. C030d is reused without reproof.

### Admissibility, reality and normalization

Set h(r)=q(sqrt(t)r)^2 e^(-tr^2). It is entire and even because
q(-z)=(-1)^epsilon q(z). For fixed q,t there is a B such that

\[
 |h(u+iv)|\le B(1+|u|)^{4N-2}e^{-tu^2+t}\quad(|v|\le1).
\]

The Gaussian dominates every inverse power in u; |u+iv| and |u|
are comparable on this strip. Thus the standard theorem applies, for
example on |Im r|<3/4 with eta=1/4 and decay exponent delta=1.
The entire h is holomorphic in a neighborhood of the larger closed
strip |Im r|<=1. This also verifies the original source's stronger decay.
There is no requirement of a uniform admissibility constant over
coefficients, N, or t down to zero.

C030g gives c_j(t)=sum_k a_k^j e^(-a_k t) by termwise differentiation.
Expanding the finite polynomial square gives

\[
 Q_{N,t}^{\epsilon}(p)
 =4\pi\sqrt t\sum_k (ta_k)^\epsilon p(ta_k)^2e^{-ta_k}
 =2\pi\sqrt t\sum_\rho h(\gamma_\rho).                \tag{A}
\]

The square q(sqrt(ta_k))^2=(ta_k)^epsilon p(ta_k)^2 is independent
of the square-root choice. Reflection sends gamma to -gamma, giving
the factor two with multiplicities preserved. The form is real by
reality of W and its derivatives, also consistent with conjugate pairing.
No spectral algebraic square is replaced by a modulus square.

In the standard theorem, put
g(b)=(2*pi)^(-1)integral_R h(r)e^(-irb)dr. Then
hhat(b/(2*pi))=2*pi*g(b). Evenness of h gives g(-b)=g(b), so the
two prime frequencies together give -2 sum Lambda(n)n^(-1/2)g(log n).
Also hhat(0)=integral_R h(r)dr, so its log(pi) term combines with
the gamma integral to give (2*pi)^(-1)integral_R h(r)m(r)dr, where
m(r)=Re psi(1/4+ir/2)-log pi. The polar arguments 1/(2i) and
-1/(2i) are respectively -i/2 and i/2. Thus all terms of the original
even-test formula, including both polar evaluations, follow with their
stated coefficients. C030g supplies absolute convergence of its spectral
sum for this fixed Gaussian-polynomial test, with all multiplicities.

Let F_q(y)=integral_R q(x)^2e^(-x^2)e^(-iyx)dx. The change of variable
x=sqrt(t)r gives g(b)=F_q(b/sqrt(t))/(2*pi*sqrt(t)). Multiplying
the imported identity by 2*pi*sqrt(t) yields exactly

\[
 \begin{split}
 Q_{N,t}^{\epsilon}(p)={}&\int_{\mathbb R}q(x)^2e^{-x^2}m(x/\sqrt t)\,dx\\
 &+4\pi\sqrt t\,e^{t/4}q(i\sqrt t/2)^2
 -2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}F_q(\log n/\sqrt t).
                                                        \tag{B}
 \end{split}
\]

Evenness equates the two polar evaluations. F_q is real on R because
the imaginary integrand is odd. Also
q(i sqrt(t)/2)^2=(-1)^epsilon(t/4)^epsilon p(-t/4)^2 is real,
possibly negative. The terms in(B) therefore admit real lower bounds.
The prime series' absolute convergence is also checked below; the
other integrals and spectral identity use the verified applicability
and retained source imports.

### The three errors

Write w(x)=q(x)^2e^(-x^2)>=0 on R. The pointwise bounds of C030f give
m(x/sqrt(t))>=1-7*1_{|x|<=20sqrt(t)}. C030d/(24) then gives

\[
 \int w(x)m(x/\sqrt t)\,dx
 \ge\|q\|_G^2-7\int_{|x|\le20\sqrt t}w(x)\,dx
 \ge(1-280C_N\sqrt t)\|q\|_G^2.                     \tag{C}
\]

The constant280 is 7 times the full interval length40sqrt(t).
For the polar term, apply C030d/(23) at z=i sqrt(t)/2, r=r_N.
Since (1+r_N)/(1-r_N)=4N-1 and -Re(z^2)=t/4,

\[
 e^{t/4}|q(i\sqrt t/2)|^2
 \le C_N e^{(4N-1)t/4}\|q\|_G^2.                    \tag{D}
\]

Use |q(z)^2|=|q(z)|^2 only to bound the error: the polar term in(B)
is at least minus 4*pi*sqrt(t) times(D). This handles both parities
without asserting positivity at an imaginary point.

For b=log n>=ell=log2, the factorization
b^2-ell*b/2-ell^2/2=(b-ell)(b+ell/2)>=0 implies
e^(-b^2/(12t))<=e^(-ell^2/(24t))n^(-ell/(24t)). Since
t<=ell/180 gives ell/(24t)>=15/2, and
0<=Lambda(n)<=log n<=n from its definition,

\[
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}e^{-(\log n)^2/(12t)}
 \le e^{-\ell^2/(24t)}\sum_{n\ge2}n^{-7}
 \le\frac1{96}e^{-\ell^2/(24t)}.                     \tag{E}
\]

Here sum_(n>=2)n^(-7)<=2^(-7)+integral_2^infinity x^(-7)dx
=1/128+1/384=1/96 by monotonicity of x^(-7). C030d/(25) gives
|F_q(b/sqrt(t))|<=4^N e^(-b^2/(12t))||q||_G^2. Thus the absolute
value of the prime term in(B) is at most
(4^N/48)e^(-ell^2/(24t))||q||_G^2, and it is absolutely summable.
Combining(C)-(E) proves(26), without unproved prime cancellation or
distributional point evaluation.

### Monotonicity and scalar bounds

For alpha=(4N-1)/4>0 and beta=(log2)^2/24>0, the derivatives of
sqrt(t), sqrt(t)e^(alpha*t), and e^(-beta/t) are respectively
1/(2sqrt(t)), e^(alpha*t)(1/(2sqrt(t))+alpha*sqrt(t)), and
(beta/t^2)e^(-beta/t). They are positive on t>0, including N=1.
All their coefficients in1-eta_N are positive, proving strict decrease.

The following elementary enclosures suffice:

\[
 3141/1000<\pi<22/7,\quad \log2>693/1000,\quad\beta>1/50,
 \quad e^u<(1-u)^{-1}\ (0<u<1),\quad e^v>1+v\ (v>0).   \tag{F}
\]

To verify the pi enclosures without a decimal oracle, put
a=arctan(1/5), b=arctan(1/239). Double-angle formulas give
tan(4a)=120/119 and tan(4a-b)=1. The angle 4a-b lies in(0,4/5)
and hence in(0,pi/2), so pi=16a-4b. Positivity follows from
a>1/5-1/(3*5^3) and b<1/239; pi/2>1 follows from
arctan(1)=integral_0^1(1+x^2)^(-1)dx>1/2.
Alternating integral expansions for arctan give

\[
 \pi>16\left(\frac15-\frac1{3\cdot5^3}
 +\frac1{5\cdot5^5}-\frac1{7\cdot5^7}\right)-\frac4{239}
 =\frac{1231847548}{392109375}>\frac{3141}{1000},
\]
\[
 \pi<16\left(\frac15-\frac1{3\cdot5^3}+\frac1{5\cdot5^5}\right)
 -4\left(\frac1{239}-\frac1{3\cdot239^3}\right)
 =\frac{670143059704}{213311234375}<\frac{22}{7}.
\]

Integrating the positive geometric series for (1-u^2)^(-1) on[0,1/3]
gives log2=2 sum_(j>=0)1/((2j+1)3^(2j+1))
>2(1/3+1/81+1/1215)=842/1215>693/1000. Squaring gives
beta>160083/8000000>1/50. The exponential bounds in(F) follow
from the power series, comparing1/j! with1 for the first and retaining
the strictly positive quadratic and higher terms for the second.
Both tested times are admissible since tau_N<=1/4000000<10^-6
<(693/1000)/180<log2/180.

### Strict endpoint margins

At t=tau_N, C_N<2sqrt(N) makes the first error less than
560sqrt(N)/(2000sqrt(N))=0.28. Also
alpha*tau_N=(4N-1)/(16000000N)<1/4000000. The second error is
strictly below

\[
 \frac\pi{250}e^{1/4000000}
 <\frac{22}{7\cdot250}\frac{4000000}{3999999}
 =\frac{352000}{27999993}<\frac{13}{1000}.             \tag{G}
\]

Since beta/tau_N>80000N, the third error is less than
(4e^(-80000))^N/48. By e^80000>80001 this base is less than
4/80001<1, so for N>=1 the error is less than
1/(12*80001)=1/960012<0.001. Thus eta_N(tau_N)
>1-0.28-0.013-0.001=0.706>0.7 for every N>=1.

For N=3, r_3=5/6, so

\[
 C_3^2=\frac{6^{12}}{5^{10}\,11\pi}
 <\frac{6^{12}\,1000}{5^{10}\,11\cdot3141}
 =\frac{1934917632}{299921875}
 <\frac{16129}{2500}=\left(\frac{127}{50}\right)^2.
\]

Hence C_3<2.54. At t=10^-6 the first error is less than
280*(127/50)/1000=0.7112. Using alpha*t=11/4000000, the second is
less than

\[
 4\frac{22}{7}\frac{127}{50}\frac1{1000}
 \frac{4000000}{3999989}
 =\frac{894080}{27999923}<\frac4{125}=0.032.            \tag{H}
\]

Finally beta/t>20000 bounds the third error by
(64/48)e^(-20000)<4/(3*20001)=4/60003<0.001. Therefore
eta_3(10^-6)>1-0.7112-0.032-0.001=0.2558>1/4.

The twelve scalar-enclosure and endpoint comparisons were checked exactly with
`python3 scripts/near-zero-assembly/scalar_margins_1186.py`.
The complete supplementary certificate is
`scripts/near-zero-assembly/scalar-margins-1186.json`: 12 checks,
no failures. It checks rational arithmetic only; the analytic proof
and named imports remain separate. No source AppendixA or zero
computation was replayed.

If p=0 both the form and norm vanish, so the non-strict inequality
is immediate. If p is nonzero its real Gaussian norm is positive.
Monotonicity extends each margin toward zero with N fixed; no limit
interchanging N and t is used. All coefficients, N=1 and both
parities are included. No source inequality failed this audit.

## Mathlib

Full matching Mathlib coverage for this assembly, its constants and
imported zeta theorems is unchecked, not asserted absent. C030d
records the Gaussian component's coverage. The standard explicit-formula
import, its full strip/decay interface and its unperformed independent
contour audit are explicit in Hypotheses and Proof; C030g records the
heat-series audit. No matching Mathlib Guinand-Weil theorem is asserted.
The rational script is not a formal verification of the theorem.
Independent contour-proof, far-time, all-degree signing and realization
gaps remain unresolved.
