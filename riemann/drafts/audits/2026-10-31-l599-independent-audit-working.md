# L599 independent fixed-pair audit — 31 October 2026

Target: Audit L599's inverse-transform hypotheses, odd-periodization normalization, reconstruction constant and complete-tail certificate.

Coverage reused: `drafts/literature/2026-10-31-l599-independent-audit-scope.md`, SPECIALIZE, supplied at invocation start. Mathematical inputs: L233 and only L598's convergence/endpoint argument. The primary Fourier and class-definition coverage is already ready; no renewed browsing or wider comparison is needed.

Main gap: actual-Xi all-degree positivity at unbounded heights. This audit can validate a generic obstruction to the stronger pointwise reflected sufficient condition, without supplying an actual-Xi sign or deciding the sine-weighted condition. Accept only if all transform factors, interchanges, endpoint constants and the entire odd tail preserve the strict negative value. Otherwise correct the canonical proof and route stop.

Checkpoint before replay: read the complete L599 proof, relevant L233 identity and L598 convergence/endpoint argument, the exact rational script and the two applicable route stops. The forward Gaussian differentiation, L233 factor 1/4, alternating-periodization sign and factor 2/pi check by hand. The endpoint cancellation fixes the constant at zero. The complete-tail comparison has a geometrically summable envelope starting at n=5. Certificate replay and independent inspection of all load-bearing values remain pending; no final audit verdict yet.

## Completed audit

PASS for the exact target. The canonical proof and audit qualification are in [L599](../../lemmas/L599-real-zero-reflected-majorant-countermodel.md). No new lemma, mathematical script or wider parameter test was needed. The primary source coverage is reused, rather than independently certifying the entire source manuscripts.

The polynomial-Gaussian form implies every derivative and moment is integrable, all spatial derivatives vanish at infinity, and the complex transform is uniformly dominated on compact sets. Its finite canonical factors cancel their linear exponentials; the Gaussian parameter is nonnegative. The associated kernel is a finite Gaussian-moment polynomial times exp(-t^2/4), so applying Schwartz periodization to A is legitimate. The full-line change of variables contributes 1/8 before the two diagonal and two cross terms, hence the final 1/4 in L233. That explicit check is now in L599.

Absolute uniform convergence of S_h and the endpoint cancellation give D_h(0)=0. Uniform convergence of the differentiated A sums justifies differentiation. For negative index m=-j-1, evenness gives the required minus sign. Period 2h contributes 1/(2h), odd-mode selection contributes 2, and pairing opposite frequencies contributes 2; integration contributes h/(n*pi). These give exactly 2/pi in L599, with no free constant. All these are analytic checks, beyond what the rational script verifies.

The tail envelope applies to every odd n>=5, not a finite cutoff. Its consecutive ratio is strictly below 2^(-89)<1/2. The full envelope sum is strictly below 156250 exp(-100), and its ratio to the negative n=3 magnitude is below 100/2^64=25/4611686018427387904<1/2. Replay of `python3 scripts/reflected-majorant/fixed_pair.py` passed all eight checks, with no failures. Inspected complete selected values using the prescribed JSON inspector: all five derivative polynomials, inverse polynomial, spectral polynomial, checks, failures, main contribution, complete-tail bound, relative prefactor 234375/2368, relative bound and threshold. The inspector's initial unsupported `--max-items` invocation failed without changing evidence; the successful selected-value inspections used `--pointer` and `--full`.

The negative conclusion survives unchanged. The bibliography now uses Csordas's exact title. This validates only the generic-implication stop; it supplies no actual-Xi sign, sine-weighted counterexample or all-degree advance. L598's other claims remain unaudited. No original mathematical discovery or full Mathlib matching theorem is claimed.
