# Starting theorems and definitions

For Re(s)>1, define ζ(s)=Σ_{n≥1} n^{-s}, where n^{-s}=exp(-s log n) with the real logarithm. Use the standard meromorphic continuation theorem for the Riemann zeta function: this extends to C with its only pole a simple pole at 1. Use Riemann's functional equation

ζ(s)=2(2π)^{s-1} sin(πs/2) Γ(1-s) ζ(1-s).

Reference: the standard named Riemann functional equation, also [NIST DLMF 25.4.2](https://dlmf.nist.gov/25.4.E2). Other starting tools are the identity theorem for meromorphic functions, the fundamental theorem of arithmetic, absolute convergence and rearrangement of series, and the standard theorem that Γ is holomorphic and nonzero on Re(s)>0. Further named inputs used below are the Weierstrass theorem for locally uniform holomorphic limits, the fundamental theorem of algebra, the Gaussian integral, Poisson summation for Schwartz functions, and Euler’s gamma integral Γ(z)=∫_0^∞e^{-u}u^{z-1}du for Re(z)>0. The standard named Hadamard factorization theorem is used in Lemma 24 only after proving its finite-order hypothesis. No RH-equivalent result is an input.

File paths in lemma text and reproduction commands are relative to the repository root. Run certificate commands from that root. Lemma numbers are stable identifiers; locate their files through the root DAG.

For vertical-strip gamma estimates, use the standard named complex Stirling formula, [NIST DLMF 5.11.3](https://dlmf.nist.gov/5.11.E3), uniformly in closed sectors away from the negative real axis. In particular, for real a in a fixed compact subinterval of (0,∞), |Γ(a+ib)| is bounded above and below by positive constant multiples of |b|^(a−1/2)exp(−π|b|/2), uniformly for |b|≥1. This follows by taking moduli in that formula, using arg(a+ib)=sgn(b)π/2−a/b+O(|b|^−3); the remaining bounded range follows by continuity and nonvanishing. No zero-distribution hypothesis is involved.

For separated real frequencies, use the standard named Montgomery--Vaughan generalized Hilbert inequality: if the distinct real numbers λ_j have nearest-neighbor gaps δ_j=min_(h≠j)|λ_j−λ_h|, then the off-diagonal kernel (λ_j−λ_h)^(−1) defines a bilinear form bounded, up to an absolute constant, by the product of the two norms (Σ_j |x_j|²/δ_j)^(1/2) and (Σ_j |y_j|²/δ_j)^(1/2). The finite-sequence statement is used; infinite applications are obtained by convergence in these weighted ℓ² norms.

For finite exponential sums use the standard named van der Corput second-
and third-derivative tests. With e(v)=exp(2πiv), f real C^k on an
interval containing M consecutive integers, and
0<λ≤|f^(k)(x)|≤Aλ, their bounds (constants depending only on A) are
O(M λ^(1/2)+λ^(−1/2)) for k=2 and
O(M λ^(1/6)+M^(1/2)λ^(−1/6)) for k=3.
Empty and singleton sums are handled separately. See Olivier Robert,
[On van der Corput's k-th derivative test for exponential sums](https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf),
Theorems 1 and 2, pages 5 and 8, including the third-derivative derivation
immediately before Theorem 2. The derivative in the third test is f''';
the extracted PDF statement's apparent double prime is not the hypothesis
used in that derivation. These are unconditional finite-sum inputs.

For the van der Corput B-process use the C^4 transform with bounded-variation
amplitude, in J. Vandehey, [Error term improvements for van der Corput
transforms](https://arxiv.org/pdf/1205.0090), Theorem 1.1 (pp. 2–3),
which records Huxley's *Area, Lattice Points, and Exponential Sums*,
Lemma 5.5.3. If f'' is positive and comparable to Q/M², the next two
derivatives are O(Q/M³) and O(Q/M⁴), and M≥b−a, then the sum of
g(n)e(f(n)) over [a,b] equals the stationary sum over f'([a,b]), with
amplitude g(x_r)/sqrt(f''(x_r)), phase f(x_r)−rx_r+1/8, and error
O((Var(g)+|g(a)|)(M/sqrt(Q)+log(2+f'(b)−f'(a)))).
Here f'(x_r)=r and e(v)=exp(2πiv). Negative curvature follows by
conjugation. This uniform bound imposes no separation of endpoint slopes
from integers; changing endpoint half-weight conventions costs at most
the corresponding endpoint amplitudes.

For continuous periodic functions use the standard named Fejér theorem:
the Cesàro means of the Fourier partial sums converge uniformly to the
function. In particular, if its Fourier coefficients are absolutely
summable, their uniformly convergent Fourier series equals the function.
