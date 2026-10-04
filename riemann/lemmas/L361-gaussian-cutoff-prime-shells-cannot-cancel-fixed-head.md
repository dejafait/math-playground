# Lemma 361: Gaussian cutoff prime shells cannot cancel a fixed head

**Hypotheses.** Fix a>0 and a finite set P of primes. Let R≥1
satisfy aR≥2 and p≤aR for every p∈P, and put ε=R^(−2).
Let χ be completely multiplicative with |χ(p)|=1 on every prime,
χ(p)=1 for every p≤aR outside P, and arbitrary unit phases for
p>aR. These are phase templates, not asserted phases at actual
real frequencies. Thus any selected shell (aR,bR], b>a fixed,
with +1 elsewhere outside P is included, as is arbitrary support
on all primes above aR. Define

\[
 T_R(\chi)=\sum_{n\ge1}\chi(n)n^{-1/2}e^{-\pi(n/R)^2},
 \qquad c_0=\frac{\Gamma(1/4)}{2\pi^{1/4}},
\]

\[
 G_P=\prod_{p\in P}\frac{1-1/p}{1-\chi(p)/p},\quad
 \rho_P=\prod_{p\in P}\frac{p-1}{p+1},\quad
 K_P=\prod_{p\in P}\frac{\sqrt p+1}{\sqrt p-1},
\]

with empty products equal to one. Put

\[
 C_a=\frac{8}{1-e^{-3\pi a^2}}
       \sum_{k\ge0}\sqrt{2^ka}\,e^{-\pi4^ka^2}<\infty.
                                                        \tag{1}
\]

The inequalities below hold pointwise even if P depends on R;
only the stated fixed-head asymptotic holds P fixed.

**Conclusion.** Uniformly in every allowed phase assignment,

\[
 |T_R(\chi)-c_0\sqrt R\,G_P|
       \le 2K_P+\frac{C_a\sqrt R}{\log(aR)},
 \quad
 |T_R(\chi)|\ge c_0\rho_P\sqrt R-2K_P
                         -\frac{C_a\sqrt R}{\log(aR)}.       \tag{2}
\]

In particular, if

\[
 \log(aR)\ge\frac{4C_a}{c_0\rho_P},\qquad
 \sqrt R\ge\frac{8K_P}{c_0\rho_P},                 \tag{3}
\]

then |T_R(χ)|≥c_0ρ_P√R/2>0. For fixed a and P this holds
eventually, so the infimum of |T_R| over all allowed phases tends
to infinity as ε tends to zero. A shell at the Gaussian cutoff,
even together with an arbitrary fixed prime head and arbitrary
phases on every larger prime, cannot furnish a zero-valued template
for L359's arbitrarily high-frequency shrinking cancellation test.

This is not a lower bound for S_ε at all actual frequencies.
It leaves phases on the growing intermediate range below aR
uncontrolled, and does not rule out negative spectral signs at
coupled finite frequencies. It establishes neither the required
derivative/rotated-phase occurrence nor failure for arbitrarily
small regulators. No actual-theta sign or RH conclusion follows.

**Proof.** The damped series is absolutely convergent for every R.
Define ν completely multiplicatively by ν(p)=χ(p) on P and ν(p)=1
elsewhere. If n has no prime divisor exceeding aR, χ(n)=ν(n).
Since both have modulus one,

\[
 |\chi(n)-\nu(n)|\le
       2\sum_{\substack{p>aR\\p\mid n}}1.
\]

Consequently the nonnegative union bound, followed by summation over
multiples of each prime, gives

\[
 |T_R(\chi)-T_R(\nu)|
 \le2\sum_{p>aR}p^{-1/2}H((p/R)^2),\qquad
 H(t)=\sum_{m\ge1}m^{-1/2}e^{-\pi tm^2}.            \tag{4}
\]

Tonelli's theorem permits this nonnegative interchange, including
infinite prime support. The following bound also proves its finiteness.
For x≥a, use m^(−1/2)≤1 and m²≥1+3(m−1) to obtain

\[
 H(x^2)\le\frac{e^{-\pi x^2}}{1-e^{-3\pi x^2}}
          \le\frac{e^{-\pi x^2}}{1-e^{-3\pi a^2}}. \tag{5}
\]

Here an elementary local prime-count estimate suffices; no prime-number
theorem is used. For an integer m≥2 every prime in (m,2m] divides
the central binomial coefficient (2m choose m). The binomial theorem
gives (2m choose m)≤4^m. Taking logarithms shows that the number of
these primes is at most 2m log 2/log m. For real x≥2 put m=ceil x.
The interval (x,m] contains at most one integer, and (m,2x] is
contained in (m,2m]. Since m≤3x/2 and log m≥log x,

\[
 \#\{p:x<p\le2x\}
       \le1+\frac{3x\log2}{\log x}
       \le\frac{(1+3\log2)x}{\log x}
       <\frac{4x}{\log x}.                        \tag{6}
\]

The middle inequality uses log x≤x. This proves the needed
real-endpoint version directly, rather than assuming a source's
prime-count constants.

Partition p>aR into (x_k,2x_k] with x_k=2^kaR. By (6), monotonicity
of p^(−1/2)exp(−π(p/R)²), and log x_k≥log(aR),

\[
 \begin{aligned}
 \sum_{p>aR}p^{-1/2}e^{-\pi(p/R)^2}
 &\le\sum_{k\ge0}\frac{4\sqrt{x_k}}{\log x_k}
                            e^{-\pi(x_k/R)^2}\\
 &\le\frac{4\sqrt R}{\log(aR)}
                \sum_{k\ge0}\sqrt{2^ka}\,e^{-\pi4^ka^2}.
 \end{aligned}                                      \tag{7}
\]

The ratio of consecutive terms of the last series is
√2 exp(−3π4^ka²), eventually at most 1/2. This proves convergence
and, if desired, bounds the remaining tail by twice its first term.
Equations (4), (5) and (7) yield

\[
 |T_R(\chi)-T_R(\nu)|\le C_a\sqrt R/\log(aR).       \tag{8}
\]

Apply L360 only to the finite-head assignment ν, with ε=R^(−2).
It supplies
|T_R(ν)−c_0√R G_P|≤2K_P and |G_P|≥ρ_P. Its covered scalar
gamma integral, [DLMF 5.9.1](https://dlmf.nist.gov/5.9#E1), has
already been specialized there and is not rederived here. Combining
these bounds with (8) proves (2). The two conditions in (3) make
each of its error terms at most c_0ρ_P√R/4. This proves the
strict lower bound. With a,P fixed, both conditions hold for all
sufficiently large R, and the lower bound diverges.

For comparison with the proposed sign construction, fix one ε
satisfying (3). L359 requires |S_ε(ξ)|≤C_ε/ω(ξ) for any negative
sign at ξ≥X_ε, and ω(ξ) tends to infinity. Its right side eventually
falls below this positive template bound. Thus these templates
cannot supply zero values around which to realize shrinking
cancellation at arbitrarily high ξ. This comparison does not assert
that actual phases obey the head/intermediate-range restrictions;
it gives no regulator-uniform onset and no sign assertion in the
remaining frequency regime. ∎

This is a **REPRODUCTION** of covered Gaussian summation tools,
using a proved elementary central-binomial prime bound to supply
the shell error missing from L360's finite-support convolution.
The closest screened smoothed-series source remains Paris,
*The asymptotic expansion of a generalisation of the Euler-Jacobi
series*, [arXiv:1503.07329v1](https://arxiv.org/pdf/1503.07329v1),
§2 and Theorem 1. Its stated exponent hypotheses and small-damping
expansion do not give this arbitrary-prime-phase shell estimate.
No originality beyond the checked literature is claimed. The new
information is local to the proposed template: its cutoff-scale
shell has only O(√R/log R) influence against the O(√R) fixed-head
main term. This does not extend L360's obstruction to arbitrary
phases on every prime below aR.

**Mathlib.** Full Gaussian shell estimate and spectral-cancellation
comparison: **not checked**. Supporting binomial, prime-count,
Tonelli and gamma-integral coverage: **not checked** here. The named
DLMF formula above supports only the inherited scalar input, not the
full statement. No full matching theorem or library absence is
asserted; general documentation is
[Mathlib](https://leanprover-community.github.io/mathlib4_docs/).
