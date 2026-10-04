# Lemma 360: Gaussian finite-prime completions retain a nonzero main term

**Hypotheses.** Use the damped coefficients of S_ε in L358, with
0<ε≤1. Let P be a finite set of primes and let χ be completely
multiplicative, with |χ(p)|=1 on P and χ(p)=1 on every prime outside
P. These are test assignments of the prime phases, not asserted
assignments at actual real frequencies. Define

\[
 T_{\varepsilon,P}(\chi)
   =\sum_{n\ge1}\chi(n)n^{-1/2}e^{-\pi\varepsilon n^2},\qquad
 c_0=\frac{\Gamma(1/4)}{2\pi^{1/4}},
\]

\[
 G_P(\chi)=\prod_{p\in P}\frac{1-1/p}{1-\chi(p)/p},\qquad
 \rho_P=\prod_{p\in P}\frac{p-1}{p+1},\qquad
 K_P=\prod_{p\in P}\frac{\sqrt p+1}{\sqrt p-1}.
\]

Empty products are one. In the fixed-support assertions P is held
fixed; the subsequent growing-support bound explicitly allows it
to depend on ε. In the final comparison, ω, C_ε and X_ε are exactly
the gamma-phase derivative, constant and fixed-regulator onset in
L359.

**Conclusion.** Uniformly over all the permitted unit phases,

\[
 \left|T_{\varepsilon,P}(\chi)
            -c_0\varepsilon^{-1/4}G_P(\chi)\right|\le2K_P,
 \qquad
 |T_{\varepsilon,P}(\chi)|
       \ge c_0\rho_P\varepsilon^{-1/4}-2K_P.       \tag{1}
\]

In particular, if

\[
 0<\varepsilon\le
        \min\left(1,\left(\frac{c_0\rho_P}{4K_P}\right)^4\right),
 \quad\text{then}\quad
 |T_{\varepsilon,P}(\chi)|
       \ge\tfrac12c_0\rho_P\varepsilon^{-1/4}>0. \tag{2}
\]

There is also a uniform growing-support obstruction. Put
L=log(1/ε). If P_ε is contained in the primes at most y_ε, where
y_ε≥2 and y_ε=o(L²) as ε tends to zero, then eventually

\[
 \inf_\chi|T_{\varepsilon,P_\varepsilon}(\chi)|
        \ge\frac{c_0\varepsilon^{-1/4}}{y_\varepsilon(y_\varepsilon+1)}
        \longrightarrow\infty.                 \tag{3}
\]

Thus a construction that sets every prime outside such a support
to +1 cannot produce a zero-valued phase template for arbitrarily
small regulators. For a fixed P and any ε satisfying (2), it also
cannot meet L359's necessary small-value condition at ξ≥X_ε with
ω(ξ)>2C_ε ε^(1/4)/(c_0ρ_P). This is a comparison of template
values with a necessary condition, not an assertion that the test
assignment occurs at an actual frequency. It does not exclude
negative signs at coupled finite frequencies, larger supports, or
nontrivial phases on the remaining primes. No negative family with
ε tending to zero and no actual-theta sign is proved.

**Proof.** First consider the ordinary positive Gaussian sum

\[
 H(a)=\sum_{n\ge1}n^{-1/2}e^{-\pi a n^2},\qquad a>0.
\]

The function f_a(x)=x^(−1/2)e^(−πax²) is positive and decreasing
on (0,∞), and its singularity at zero is integrable. Integral
comparison on [1,∞) gives

\[
 \int_1^\infty f_a(x)\,dx
       \le H(a)\le f_a(1)+\int_1^\infty f_a(x)\,dx.
\]

Here ∫_0^1 f_a≤2 and f_a(1)≤1. Subtracting the full integral
therefore shows |H(a)−∫_0^∞f_a|≤2 for every a>0. Import the
covered scalar gamma integral
[DLMF 5.9.1](https://dlmf.nist.gov/5.9#E1), with positive real
parameter 1/4. The substitution t=πax² gives

\[
 \int_0^\infty f_a(x)\,dx
       =\tfrac12(\pi a)^{-1/4}\Gamma(1/4)
       =c_0a^{-1/4}.
 \quad\text{Hence}\quad
 |H(a)-c_0a^{-1/4}|\le2.                         \tag{4}
\]

No complex small-damping theorem is being invoked.

Define b multiplicatively by b(1)=1,
b(p^k)=(χ(p)−1)χ(p)^(k−1) for p∈P and k≥1, and
b(p^k)=0 for p outside P. The finite telescoping sum on each
prime power is
1+Σ_(j=1)^k(χ(p)^j−χ(p)^(j−1))=χ(p)^k.
Multiplication over the prime factors of n proves the exact divisor
identity χ(n)=Σ_(d|n)b(d). The support of b consists of integers
whose prime factors all belong to P. Moreover,

\[
 \sum_{d\ge1}\frac{|b(d)|}{\sqrt d}
   =\prod_{p\in P}\left(1+
                     \frac{|\chi(p)-1|}{\sqrt p-1}\right)
   \le\prod_{p\in P}\left(1+\frac2{\sqrt p-1}\right)=K_P<\infty.
                                                        \tag{5}
\]

This is an absolutely convergent product of finitely many geometric
series; no conditionally convergent Euler product is used. The
double sum after the divisor identity has absolute value sum at most
H(ε)Σ_d|b(d)|/√d, because H(εd²)≤H(ε). It is finite by (5),
so rearrangement is justified and gives exactly

\[
 T_{\varepsilon,P}(\chi)
        =\sum_{d\ge1}\frac{b(d)}{\sqrt d}\,H(\varepsilon d^2).
                                                        \tag{6}
\]

Substitute (4) into (6). Its total error has modulus at most 2K_P.
The absolutely convergent leading coefficient is

\[
 \sum_{d\ge1}\frac{b(d)}d
   =\prod_{p\in P}\left(1+\frac{\chi(p)-1}{p-\chi(p)}\right)
   =\prod_{p\in P}\frac{p-1}{p-\chi(p)}=G_P(\chi).   \tag{7}
\]

Since |p−χ(p)|≤p+1, its modulus is at least ρ_P. This proves
(1). The inequality ε^(1/4)≤c_0ρ_P/(4K_P) makes the error in
(1) at most half the leading lower bound, proving (2).

For growing support, the relevant ratio has the exact simplification

\[
 \frac{K_P}{\rho_P}
       =\prod_{p\in P}\frac{p+1}{(\sqrt p-1)^2}.      \tag{8}
\]

Write x=p^(−1/2)≤1/√2<3/4. Using log(1+x²)≤x²≤x and
−log(1−x)≤x/(1−x)≤4x, each logarithm in (8) is at most
9/√p. If P consists only of primes at most y≥2, comparison with
all integers and the decreasing integral gives

\[
 \log(K_P/\rho_P)
       \le9\sum_{2\le n\le y}n^{-1/2}\le18\sqrt y.  \tag{9}
\]

If m=floor y, adding all the nonprime factors, each smaller than
one, also proves

\[
 \rho_P\ge\prod_{n=2}^m\frac{n-1}{n+1}
            =\frac2{m(m+1)}\ge\frac2{y(y+1)}.       \tag{10}
\]

For y=o(L²), (9) implies
ε^(1/4)K_P/ρ_P≤exp(−L/4+18√y)→0, uniformly in P and χ.
Thus (2)'s error comparison eventually holds even for these changing
supports. Equations (2) and (10) give (3). Since y≤L² eventually,
the lower bound in (3) tends to infinity by exponential versus
polynomial growth. No estimate for the number of primes is needed.

Finally, L359's necessary condition at sufficiently high ξ is
|S_ε(ξ)|≤C_ε/ω(ξ). The uniform template lower bound in (2)
is strictly larger than this threshold when
ω(ξ)>2C_ε ε^(1/4)/(c_0ρ_P), giving the stated incompatibility.
The onset from L359 must also be respected. This comparison holds
ε fixed and uses its ε-dependent C_ε; it gives no ε-uniform
onset and no frequency-realization theorem. ∎

This is a **REPRODUCTION** of the covered scalar Gaussian/gamma
tool, with an elementary finite-prime divisor convolution supplying
the needed phase-uniform error. The closest screened smoothed-series
source is Paris, *The asymptotic expansion of a generalisation of the
Euler-Jacobi series*, [arXiv:1503.07329v1](https://arxiv.org/pdf/1503.07329v1),
§2; its Theorem 1's even-integer exponent hypotheses do not supply
this 1/2-exponent, phase-uniform bound. Only its assessed comparison
is reused, not a theorem outside its domain. L337's different
endpoint-weighted positive completion supplies useful historical
contrast; its weights and conclusions are not used in this proof.
The explicit estimate here is the needed specialization for L358's
Gaussian coefficients, not a new claim of arithmetic signing or
originality beyond the sources checked.

**Mathlib.** Full phase-uniform Gaussian estimate, growing-support
obstruction, and cancellation comparison: **not checked**. Supporting
gamma-integral, divisor-convolution and geometric-series coverage is
also **not checked** here. DLMF 5.9.1 above is a supporting scalar
input, not a match for the full statement. No full matching theorem
or library absence is asserted; general documentation is
[Mathlib](https://leanprover-community.github.io/mathlib4_docs/).
