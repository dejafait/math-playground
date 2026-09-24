# Starting theorems and definitions

For Re(s)>1, define ζ(s)=Σ_{n≥1} n^{-s}, where n^{-s}=exp(-s log n) with the real logarithm. Use the standard meromorphic continuation theorem for the Riemann zeta function: this extends to C with its only pole a simple pole at 1. Use Riemann's functional equation

ζ(s)=2(2π)^{s-1} sin(πs/2) Γ(1-s) ζ(1-s).

Reference: the standard named Riemann functional equation, also [NIST DLMF 25.4.2](https://dlmf.nist.gov/25.4.E2). Other starting tools are the identity theorem for meromorphic functions, the fundamental theorem of arithmetic, absolute convergence and rearrangement of series, and the standard theorem that Γ is holomorphic and nonzero on Re(s)>0. Further named inputs used below are the Weierstrass theorem for locally uniform holomorphic limits, the fundamental theorem of algebra, the Gaussian integral, Poisson summation for Schwartz functions, and Euler’s gamma integral Γ(z)=∫_0^∞e^{-u}u^{z-1}du for Re(z)>0. The standard named Hadamard factorization theorem is used in Lemma 24 only after proving its finite-order hypothesis. No RH-equivalent result is an input.

File paths in lemma text and reproduction commands are relative to the repository root. Run certificate commands from that root. Lemma numbers are stable identifiers; locate their files through the root DAG.

For vertical-strip gamma estimates, use the standard named complex Stirling formula, [NIST DLMF 5.11.3](https://dlmf.nist.gov/5.11.E3), uniformly in closed sectors away from the negative real axis. In particular, for real a in a fixed compact subinterval of (0,∞), |Γ(a+ib)| is bounded above and below by positive constant multiples of |b|^(a−1/2)exp(−π|b|/2), uniformly for |b|≥1. This follows by taking moduli in that formula, using arg(a+ib)=sgn(b)π/2−a/b+O(|b|^−3); the remaining bounded range follows by continuity and nonvanishing. No zero-distribution hypothesis is involved.

The logarithmic version of complex Stirling is log Γ(w)=(w−1/2)Log w−w+(log(2π))/2+O(1/|w|), with compatible analytic logarithms, uniformly on every closed sector |arg w|≤π−δ. See [NIST DLMF 5.11.1](https://dlmf.nist.gov/5.11.E1) and its [complex remainder bounds](https://dlmf.nist.gov/5.11#ii). On disks of radius comparable to |w| contained in a slightly larger such sector, the remainder is analytic and Cauchy's estimates bound its jth derivative by O(|w|^(−1−j)). This supporting gamma estimate supplies no sign of a zeta derivative expression.

For exact gamma moduli, use Euler's reflection formula Γ(z)Γ(1−z)=π/sin(πz) for noninteger z, [NIST DLMF 5.5.3](https://dlmf.nist.gov/5.5.E3). Together with Γ(z+1)=zΓ(z), obtained by integration by parts in Euler's integral on Re z>0 and then continuation, it gives |Γ(1+it)|²=πt/sinh(πt) for real t≠0. The equivalent formula for |Γ(it)| is [NIST DLMF 5.4.3](https://dlmf.nist.gov/5.4.E3); the value at t=0 follows by continuity. These are standard identities, not zero-location inputs.

For the Hardy–Littlewood approximate functional equation use E. C. Titchmarsh, *The Theory of the Riemann Zeta-function*, second edition revised by D. R. Heath-Brown (1986), [Theorem 4.15 and equation (4.12.4), pp. 79, 81–84](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=44). For s=σ+it, t>0, 2πxy=t and x,y bounded below by a fixed positive constant,

ζ(s)=Σ_(n≤x)n^(−s)+χ(s)Σ_(n≤y)n^(s−1)+O(x^(−σ))+O(t^(1/2−σ)y^(σ−1)),
χ(s)=2(2π)^(s−1)sin(πs/2)Γ(1−s).

The error constants are uniform for σ in a fixed closed subinterval of (0,1). This unconditional approximation supplies no positive lower bound. To estimate derivatives, first realize the difference with fixed finite sums as an analytic function on a complex neighborhood and bound it there; a real-variable error term cannot simply be differentiated.

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

For a fixed derivative order d≥2, the classical extension is
O_d,A(M λ^(1/(2^d−2))+M^(1−2^(2−d))λ^(−1/(2^d−2))).
The hypothesis is 0<λ≤|f^(d)|≤Aλ on the interval. See Robert's Theorem 3,
equation (17), p. 8, and the explicit kth-derivative restatement (30)–(31),
p. 18, at the same link. D. R. Heath-Brown, *A New k-th Derivative Estimate
for Exponential Sums via Vinogradov's Mean Value*,
[equation (1), p. 1](https://arxiv.org/pdf/1601.04493#page=1), also states
this bound with an explicit kth-derivative hypothesis. His
[Theorem 1, p. 3](https://arxiv.org/pdf/1601.04493#page=3), for fixed d≥3
and ε>0, gives
O_d,A,ε(M^(1+ε)[λ^(1/(d(d−1)))+M^(−1/(d(d−1)))
+M^(−2/(d(d−1)))λ^(−2/(d²(d−1)))]).
Translate the interval and, for negative f^(d), conjugate the sum.
All terms of either bound must be retained; neither result asserts a sign.

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

For the zero-free-region bounds on ζ′/ζ, use Titchmarsh's *The Theory of
the Riemann Zeta-function*, second edition (1986), [Theorem 3.11,
equation (3.11.7), p. 60](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=35),
and [Section 6.19, p. 135](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=72).
For Re s≥1 and sufficiently large |Im s| these give, respectively,
|ζ′(s)/ζ(s)|=O(log |Im s|) and
O((log |Im s|)^(2/3)(log log |Im s|)^(1/3)), uniformly in Re s.
These unconditional bounds are supporting inputs only; they do not
assert slow variation on every shrinking window or sign a Mellin integral.
The same Section 6.19 gives nonvanishing and the latter derivative
bound throughout Re s≥1−A/Q(t), for a fixed A>0 and
Q(t)=(log |t|)^(2/3)(log log |t|)^(1/3). A smaller fixed region
permits Cauchy disks of radius comparable to 1/Q(t) near Re s=1;
the resulting first derivative bound for ζ′/ζ is O(Q(t)²).

For finite prime products use the standard named Mertens third
theorem: ∏_(p≤x)(1−1/p)^(−1)∼exp(γ)log x as real x→∞,
where γ is Euler's constant. See Ross G. Pinsky, *Probabilistic
Proofs of Some Generalized Mertens' Formulas Via Generalized Dickman
Distributions* (2018), [equation (1.1), p. 2](https://arxiv.org/pdf/1809.04888#page=2).
This unconditional main term is the only part used here; no
RH-dependent bound on its error or on oscillations is imported.
