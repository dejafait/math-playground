# Lemma 355: a positive Fourier kernel with the counting law, exact gaps and a negative first sign

**Hypotheses.** Use the counting convention and first Laguerre form
of L354: N_F(T) counts zeros with 0<Re z≤T, including multiplicity,
and D_1(F;x)=F'(x)²−F(x)F''(x). The finite interval calculation below
uses L037's arithmetic contracts. No assertion about actual Ξ is
assumed.

**Conclusion.** There exists a real even canonical product F of
order exactly one satisfying every conclusion of L354, including
F(0)=1, only simple zeros, exactly one nonreal quartet ±(A±ib),
A>40, 0<b<1/4, all other zeros real with absolute value greater
than 4, and

\[
 N_F(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(1),
 \qquad
 t_{n+1}-t_n\le\frac{2\pi}{\log(t_n/(2\pi))}\quad(n\ge1).
\]

Here t_n lists all positive real zeros in increasing order. Moreover
F(A)≠0 and D_1(F;A)/F(A)²<−31, while

\[
 F(z)=\int_{\mathbb R}K(u)e^{izu}\,du,
 \quad K\in C^\infty(\mathbb R),\quad K(-u)=K(u)>0,
 \quad \int_{\mathbb R}K(u)e^{c|u|}\,du<\infty\quad(c>0).
\]

Thus even these joint conditions do not imply the first Laguerre
inequality. This is a counterexample to a proposed sufficient
condition, not to RH, and supplies neither an actual-theta identity
nor an Euler product.

**Proof.** The background and first-sign mechanisms are imported;
the work here checks the simultaneous kernel and exact-gap
requirements left open by the prior SPECIALIZE assessment.

### 1. Background, normalization and counting

Put q=2π, k(u)=exp(−q cosh(2u)) and B=∫_R k(u)du>0. The standard
Bessel integral [DLMF 10.32.9](https://dlmf.nist.gov/10.32.E9) gives

\[
 H(z)=\frac{K_{iz/2}(q)}{K_0(q)}
     =\frac1B\int_{\mathbb R}k(u)e^{izu}\,du,
 \qquad B=K_0(q).
\]

The change of variable is t=2u, including both halves of the real
line. Every exponential moment of k and of each derivative exists;
in particular the integral is entire, real on R, even, and H(0)=1.

Import Lagarias, *The Schrödinger Operator with Morse Potential
on the Right Half Line*,
[arXiv:0712.3238v6, Theorems 2.1 and 4.1, (4.7)](https://arxiv.org/pdf/0712.3238v6).
At κ=0, W_(0,μ)(e^u₀) has order one, only simple nonzero imaginary
zeros, and two-sided zero count
2U log U/π+2(2log2−1−u₀)U/π+O(1).
The identity K_μ(q)=sqrt(π/(2q)) W_(0,μ)(2q) applies with
u₀=log(4π). Halving that count and putting U=T/2 gives

\[
 N_H(T)=\frac{T}{2\pi}
   [\log(T/2)+2\log2-1-\log(4\pi)] +O(1)=M(T)+O(1).
\]

All zeros of H are therefore simple and real. They also obey
|z|>2q=4π>4: a positive order zero ν of K_(iν)(q) gives the
Dirichlet eigenfunction w(t)=K_(iν)(q e^t) on t≥0 in the cited
spectral correspondence. Its equation and energy identity are

\[
 -w''+q^2e^{2t}w=\nu^2w,
 \qquad
 \nu^2\int_0^\infty |w|^2
  =\int_0^\infty(|w'|^2+q^2e^{2t}|w|^2)
  >q^2\int_0^\infty|w|^2.
\]

The decaying eigenfunction has the required square integrability
and vanishing boundary term, and it is nonzero. Thus ν>q and
z=2ν>2q. Hadamard's factorization theorem for finite-order entire
functions now gives

\[
 H(z)=\prod_{n\ge1}(1-z^2/t_n^2).
\]

Indeed the count implies Σt_n^(−2)<∞, pairing the genus-one factors
is locally absolutely convergent, and the possible exponential
factor is exp(az+b). Evenness forces a=0, and H(0)=1 removes the
constant. This imports the named factorization theorem; it does
not infer canonical normalization from the zero set alone.

### 2. An exact gap bound above order parameter 100

Write ν_n=t_n/2. We must prove
ν_(n+1)−ν_n≤π/log(ν_n/π), including the initial range. Set χ=π² and

\[
 S(\nu)=\sum_{j\ge0}\frac{\chi^j}{j!(1+i\nu)_j},\qquad
 \theta(\nu)=\operatorname{Im}\log\Gamma(1+i\nu)
             -\nu\log\pi-\arg S(\nu).
\]

Use Paris, [arXiv:2204.09306v1, (1.2), (2.1)](https://arxiv.org/pdf/2204.09306v1):
I_(iν)(q)=π^(iν) S(ν)/Γ(1+iν) and
K_(iν)(q)=πi(I_(iν)(q)−I_(-iν)(q))/(2sinh(πν)).
Consequently, wherever S≠0,

\[
 K_{i\nu}(q)
  =\frac{\pi |S(\nu)|}{\sinh(\pi\nu)|\Gamma(1+i\nu)|}
     \sin\theta(\nu).                                      \tag{1}
\]

For ν≥100, the absolutely and locally uniformly convergent series
and its derivative satisfy

\[
 |S-1|\le e^{\chi/\nu}-1,\qquad
 |S'|\le\frac{\chi e^{\chi/\nu}}{\nu^2}.
\]

For the derivative, each j-th term acquires a sum of j reciprocals
of modulus at most 1/ν. Since χ<10 and exp(1/10)<10/9,
|S|>8/9 and |S'/S|<25/(2ν²). In particular a continuous argument
is available throughout this tail.

The explicit complex remainder in
[DLMF 5.11.2 and §5.11(ii)](https://dlmf.nist.gov/5.11#ii),
with no Bernoulli term retained, gives for z=1+iν

\[
 \psi(z)=\log z-\frac1{2z}+R(z),\qquad
 |R(z)|\le\frac{\sec^3(\arg z/2)}{12|z|^2}<\frac1{4\nu^2}.
\]

Also Re(log z−1/(2z))≥log ν: with x=ν^(−2), this is the
elementary inequality log(1+x)≥x/(1+x). Hence

\[
 \theta'(\nu)\ge\log(\nu/\pi)-\frac{14}{\nu^2}.             \tag{2}
\]

For h=π/log(ν/π), integrate (2), using
log(1+s/ν)≥s/(ν+h) for 0≤s≤h, to obtain

\[
 \theta(\nu+h)-\theta(\nu)
 \ge\pi+\frac{h^2}{2(\nu+h)}-\frac{14h}{\nu^2}>\pi.        \tag{3}
\]

The strict inequality is uniform for ν≥100. To check it explicitly,
h<2, and νh is increasing here with νh>75 at ν=100 because
3<π<4 and log(100/π)<4. Thus
hν²/(ν+h)>75/(1+2/100)>28. These elementary bounds can use
e<3 and e^4>100/3, the latter from the first five exponential terms.
Equation (1) and continuity then place a zero strictly between ν
and ν+h whenever ν is a zero, and give the desired tail gap bound.
No adjacent leading asymptotics have been subtracted.

### 3. The whole finite range, with a reproducible certificate

The finite computation is

```sh
python3 scripts/laguerre/certify_bessel_gaps.py
```

Its saved output is `scripts/laguerre/bessel-gap-certificate.json`.
It uses only L037's outward basic arithmetic and rational enclosure
of π. Logarithms and arctangents use the power series below with
explicit tails; no new transcendental implementation is assumed.

For n=1,…,80 it produces disjoint rational intervals [l_n,r_n]
of width 1/25000, all lying in (9,102), such that

\[
 -\pi<\theta(l_n)-n\pi<0<\theta(r_n)-n\pi<\pi,\qquad
 \frac{\pi}{\log(l_n/\pi)}-(r_{n+1}-l_n)>\frac8{10000}.
                                                               \tag{4}
\]

The second assertion is for n<80. The smallest enclosed phase-sign
margin exceeds 19/10^6 and the smallest gap surplus exceeds
8/10000. The first interval ends at 976879/100000<10; the last is
[2025391/20000,10126959/100000], with left endpoint above 100.
The endpoints' signs in (1) are opposite, so every interval contains
a zero. Uniqueness within these brackets is unnecessary.

Here are the analytic errors used to certify (4). Shift the gamma
argument to w=33+iν and use its recurrence 32 times. Stirling's
formula through 1/(12w), with
[DLMF 5.11.1 and §5.11(ii)](https://dlmf.nist.gov/5.11#ii), gives

\[
 \begin{split}
 \operatorname{Im}\log\Gamma(1+i\nu)
 ={}&\frac{65}{2}\arctan(\nu/33)
   +\frac\nu2\log(33^2+\nu^2)-\nu
   -\frac{\nu}{12(33^2+\nu^2)}\\
 &-\sum_{j=1}^{32}\arctan(\nu/j)+\varepsilon,
 \qquad |\varepsilon|\le\frac1{90\cdot33^3}.
 \end{split}                                                  \tag{5}
\]

The bound follows from sec^4(arg w/2)<4 and |w|≥33. The branch is
the analytic logarithm of Γ on Re w>0 agreeing with its real value
on the positive axis. The series for S is kept through j=64. For
ν≥9 its complex tail has modulus at most
(50/49)(10/9)^65/65!: the first omitted term has that factorial
majorant without 50/49, and subsequent ratios are below 1/50.
This disk is enclosed by a rectangle. Its real part is checked
positive at each endpoint, so arg S=arctan(Im S/Re S) there.

Range reduction puts each logarithm into
log x=m log2+2Σ_(j≥0) y^(2j+1)/(2j+1), with |y|≤1/2.
Each arctangent is reduced by its reciprocal and addition formulas
to |y|≤1/2. After 96 terms, the absolute tails are bounded by
2|y|^193/[193(1−|y|²)] for log and half that for arctan. All
range conditions and denominator signs are checked. Floating-point
phase values propose rational brackets only; (4) is accepted solely
by interval evaluations with (5) and these tails. Induction over
the enclosed operations, as in L037, therefore certifies the saved
strict rational inequalities under its implementation contracts.

To see why witness brackets cover *all* gaps, put
g(v)=v+π/log(v/π). The same rational interval calculation gives

\[
 \frac\pi{\log(7/\pi)}-(10-2\pi)>\frac15,\quad
 g(7)>10,\quad g'(7)>\frac3{10}.
\]

The formula g'(v)=1−π/[v log²(v/π)] then shows g increasing for
v≥7. Any zero v between q and l_1 has a later witness below 10:
for q<v≤7 use the first displayed inequality, and for 7≤v<l_1
use g(v)≥g(7)>10. For l_n≤v<l_(n+1), (4) gives a later witness
at most r_(n+1)<g(l_n)≤g(v). This covers every v<100 because
l_80>100. Zeros with v≥100 use (3). Additional zeros between, or
inside, the brackets cannot invalidate these upper bounds for the
next zero. Rescaling by two proves the literal gap inequality for
every pair of consecutive positive real zeros of H.

### 4. Uniform positivity of the modified density

For arbitrary A>40 and 0<b<1/4 define L354's normalized quartet
factor and its inverse Fourier density by

\[
 P_b(z)=\frac{((z-A)^2+b^2)((z+A)^2+b^2)}{(A^2+b^2)^2},
 \qquad
 K(u)=\frac{k''''(u)+2(A^2-b^2)k''(u)+(A^2+b^2)^2k(u)}
             {B(A^2+b^2)^2}.                                \tag{6}
\]

To prove positivity on the entire line, put v=q cosh(2u) and y=v−q≥0.
Direct differentiation, using v'=2q sinh(2u), gives

\[
 \frac{k''}{k}=4(v^2-v-q^2)\ge-4q>-28,
\]

\[
 \begin{split}
 \frac{k''''}{16k}
 &=v^4-6v^3+(7-2q^2)v^2+(6q^2-1)v+q^4-4q^2\\
 &=y^4+(4q-6)y^3+(4q^2-18q+7)y^2
       +(-12q^2+14q-1)y+3q^2-q.
 \end{split}
\]

Since 6<q<7, the quartic, cubic and constant terms on the last
line are nonnegative, the quadratic coefficient is at least 43,
and the linear coefficient is at least −589. Completing a square
therefore gives

\[
 \frac{k''''}{k}\ge-\frac{16\cdot589^2}{4\cdot43}>-33000.
\]

As A²−b²>0, the numerator in (6), divided by k, exceeds
A⁴−56A²−33000. At A=40 this is 2437400, and it increases for
A≥40. Thus K(u)>0 for every real u, uniformly over this whole
parameter range. This bound avoids a continuity argument on an
unbounded interval.

The independent integer-polynomial recurrence in
`python3 scripts/laguerre/check_bessel_kernel.py` checks both
displayed derivative identities, the shift v=q+y and the rational
coefficient bounds. It uses no sampled value of u or π.

Every derivative in (6) is a polynomial in sinh(2u), cosh(2u)
times k. Hence K is smooth and even, and has every exponential
moment. Four integrations by parts are valid for every complex z;
all boundary terms vanish by the superexponential decay. They give
∫K(u)e^(izu)du=P_b(z)H(z), with the signs in (6) coming from
the Fourier multiplier −z² for a second derivative. In particular
∫K=1.

### 5. Choose the quartet and retain the negative sign

Choose the midpoint A>40 of any consecutive real zeros of H above
40. Then H(A)≠0 and the sum

\[
 S_A=\sum_n\big((A-t_n)^{-2}+(A+t_n)^{-2}\big)
\]

is positive and finite. Its convergence follows from Σt_n^(−2)<∞;
the finitely many small denominators are nonzero. Choose
b=(S_A+16)^(−1/2), so 0<b<1/4, and set F=P_bH.
The count changes by precisely 2 times the indicator of T≥A.
The real zeros and all their gaps remain unchanged; the inserted
quartet is simple and disjoint from them. The paired factors
(1−z²/(A+ib)²)(1−z²/(A−ib)²) show that F itself is the canonical
product with F(0)=1. Its order remains exactly one.

Use the reciprocal-square identity of Csordás,
[arXiv:1309.0055v2, Proposition 2.2, (2.3)](https://arxiv.org/pdf/1309.0055v2),
with the symmetric reflected-pair bound checked in L354. It gives

\[
 \frac{D_1(F;A)}{F(A)^2}
 =S_A-\frac2{b^2}+R_b=-S_A-32+R_b<-31,
 \qquad
 0<R_b=\frac{2(4A^2-b^2)}{(4A^2+b^2)^2}<\frac1{2A^2}<1.
\]

Here P_b(A)>0 and H(A)≠0. The reflected contribution is bounded
uniformly as b varies; it has not been treated as a fixed factor.
Section 4 applies to precisely this choice of A,b. This verifies
all of the required conditions together. ∎

This specializes known Bessel, Fourier-differentiation and
Laguerre-sign mechanisms. The checked literature did not supply
their full conjunction with these exact gaps; no originality is
claimed. The finite gap portion retains L037's implementation
qualification. The required generic sign is nonnegativity, whereas
the constructed normalized value is below −31. No actual-zeta sign,
zero-exclusion interval, endpoint margin or RH candidate follows.

**Mathlib.** Full statement: **not checked**. Supporting
Bessel/Whittaker zero classification, Hadamard factorization,
Fourier differentiation, special-function remainder and first
Laguerre coverage: **not checked**. The named theorems and direct
links above are mathematical sources, not asserted Mathlib matches.
