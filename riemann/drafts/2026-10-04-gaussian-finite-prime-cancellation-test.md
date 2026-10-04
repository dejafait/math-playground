# Gaussian finite-prime cancellation test — 2026-10-04

This is saved reasoning for the single large-frequency sign target
already approved by the SPECIALIZE assessment in
[the first-spectrum review](literature/2026-10-03-gaussian-regulated-first-spectrum.md).
The target and regulator quantifier are unchanged. No further source
search is needed for the covered scalar gamma integral and the
elementary finite-prime summation test.

The main gap remains actual-theta mixed positivity. A global first
sign for every sufficiently small regulated approximant could pass
to actual theta through L357, while leaving higher signs unresolved.
L359's cancellation criterion is a possible way to disprove this
particular certificate by constructing negatives with ε tending to
zero. Its six finite examples are not that construction.

The concrete attempt starts with a completely multiplicative phase
χ, varying χ(p) on a fixed finite prime set P and setting χ(p)=1
on every other prime. This respects prime-power and product phase
relations. Test whether its Gaussian-weighted value can be small
as ε tends to zero. Continue this construction only if it admits
such cancellation, then address the derivative condition and
realization at actual frequencies. A uniform nonzero leading term
would stop this fixed-support, +1-background implementation; it
would not stop other phase backgrounds or growing support.

For b multiplicative with b(p^k)=(χ(p)−1)χ(p)^(k−1) on P,
and zero on prime powers outside P, the exact convolution is
χ(n)=Σ_(d|n)b(d). It gives a sum of rescaled ordinary Gaussian
sums H(εd²). The covered gamma integral supplies
H(a)=C a^(−1/4)+O(1), uniformly for a>0, with
C=Γ(1/4)/(2π^(1/4)); monotonicity bounds the error by two.
The prospective leading factor is therefore
Σ b(d)/d=∏_(p∈P)(1−1/p)/(1−χ(p)/p).
Its minimum modulus is at least ∏_(p∈P)(p−1)/(p+1)>0.

The remaining proof obligations at that checkpoint were absolute
interchange, a phase-uniform error bound, and comparison with the
actual shrinking cancellation requirement.

## Completed test

The full proof is
[L360](../lemmas/L360-gaussian-finite-prime-completions-retain-nonzero-main-term.md).
The convolution is absolutely summable, and its error is bounded
uniformly over the phases by twice
K_P=∏_(p∈P)(√p+1)/(√p−1). Thus for each fixed P all sufficiently
small regulators have a value bounded below by
(c_0ρ_P/2)ε^(−1/4), with ρ_P=∏_(p∈P)(p−1)/(p+1)>0.
It cannot be a zero-valued template or meet L359's shrinking-value
necessity at arbitrarily high frequencies with ε held fixed.

The explicit error also permits changing supports contained in the
primes at most y. Elementary integer comparisons give
log(K_P/ρ_P)≤18√y and ρ_P≥2/[y(y+1)]. Consequently if
y=o(log²(1/ε)), the modulus has the uniform divergent lower bound
c_0 ε^(−1/4)/[y(y+1)]. No prime-number theorem, generic recurrence
theorem, complex small-damping expansion, or numerical experiment
is needed for this statement.

This is informative NEGATIVE evidence against the fixed-support,
+1-background zero-template mechanism, not against the regulator
family itself. The proof reproduces the assessed scalar gamma
input with elementary divisor and geometric-series calculations;
no originality beyond the checked literature is claimed. L337's
endpoint positive completion is a related historical obstruction,
but has different weights and is not a mathematical input here.

The comparison must retain its qualifications: nonzero values do
not rule out negative signs in a coupled finite-frequency regime;
C_ε and L359's onset remain regulator-dependent. Actual prime
phases also range over infinitely many primes, so this is not a
lower bound for S_ε at every frequency. No six-regulator certificate
was recomputed, and no actual-zeta sign range is extended.

Park this implementation and retain the prior covered spectral
target for a prime shell growing at scale ε^(−1/2). A useful test
must retain the actual Gaussian coefficients, derivative and
rotated-phase conditions, and the required frequency-realization
scale; a phase-template cancellation alone will not establish a
negative family. The current Next action remains solely in
PROGRESS.md.
