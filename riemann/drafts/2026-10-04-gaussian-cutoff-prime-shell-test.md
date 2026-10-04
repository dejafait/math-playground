# Gaussian cutoff prime-shell test — 2026-10-04

The saved SPECIALIZE assessment in
[the first-spectrum review](literature/2026-10-03-gaussian-regulated-first-spectrum.md)
already covers the unchanged large-frequency first-Laguerre target.
This invocation tests the proposed shell mechanism, without another
literature search or a standalone finite-regulator scan.

The main gap remains actual-theta mixed positivity and low-index signs
at unbounded height. A global first sign for every sufficiently small
regulated approximant could pass through L357; higher signs would
remain unresolved. L359 instead supplies a possible negative test,
but occurrence for arbitrarily small regulators is still missing.

Put R=ε^(−1/2). The concrete proposed template keeps arbitrary phases
on a fixed finite prime head P, assigns arbitrary unit phases to a
shell p>aR (a>0 fixed), and assigns +1 to every other prime. It
includes bounded shells at the Gaussian cutoff, and may even permit
arbitrary phases on every prime above aR. Continue this template only
if its value can approach zero, before addressing L359's derivative,
rotated-phase and actual-frequency conditions. A phase-uniform lower
bound of order √R would stop this implementation.

L360's finite-prime convolution bound is not effective at this shell
scale; simply inserting a larger support into it is not a new test.
Use the exact Gaussian coefficient mass of multiples of shell primes
instead. The change from the fixed-head template is at most
2Σ_(p>aR) p^(−1/2) H((p/R)²), where
H(t)=Σ_(m≥1)m^(−1/2)exp(−πtm²). For x≥a,
H(x²)≤exp(−πx²)/(1−exp(−3πa²)), by m²≥1+3(m−1).
An elementary central-binomial estimate should give at most
4x/log x primes in (x,2x], for x≥2. Dyadic summation would then
bound the shell perturbation by C_a√R/log(aR), uniformly over its
phases. L360 gives the fixed-head main term
c_0√R G_P with modulus at least c_0ρ_P√R and error at most 2K_P.

Remaining checks at this checkpoint: prove the real-endpoint prime
count, justify the union bound and infinite nonnegative interchange,
bound the dyadic constant, and retain every qualification when
comparing with L359's fixed-regulator cancellation necessity. No
shell bound, spectral sign or continuation decision is asserted yet.

## Completed test

The full proof is
[L361](../lemmas/L361-gaussian-cutoff-prime-shells-cannot-cancel-fixed-head.md).
The central-binomial argument proves the real-endpoint prime-count
bound; a nonnegative union bound and a convergent dyadic sum give
the phase-uniform shell error C_a√R/log(aR). Together with L360's
fixed-head estimate this leaves modulus at least c_0ρ_P√R/2 for
all sufficiently large R. The conclusion includes infinite support
above aR; it does not permit arbitrary phases below aR outside P.

This is new NEGATIVE evidence against the saved shell implementation,
rather than another use of L360's ineffective large-support error.
Its proposed larger support still cannot produce a zero-valued
template. The achieved perturbation is o(√R), below the retained
main term, whereas L359 requires a value shrinking to zero at fixed
ε as frequency grows. Neither the ε-dependent onset nor actual
frequency realization is improved. No spectral sign is inferred
from noncancellation in this restricted set of templates.

The result reproduces the assessed scalar tools and elementary
summation, with no originality claim. No numerical experiment was
needed: every bound follows from a displayed analytic inequality.
The finite negative regulators and all actual-theta sign/exclusion
ranges are unchanged. Park this shell construction and test phases
throughout the growing range below the Gaussian cutoff, together
with the weighted logarithmic derivative. This is a materially
different freedom: the intervening prime phases are no longer +1.
The prior assessment still covers the unchanged spectral target;
the current Next action is recorded only in PROGRESS.md.
