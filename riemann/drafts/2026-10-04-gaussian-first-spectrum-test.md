# Regulated first-spectrum calculation — 2026-10-04

Saved reasoning for the single target approved in
[the prior assessment](literature/2026-10-03-gaussian-regulated-first-spectrum.md).
This records the initial reasoning and the completed bounded test;
the full proof is now in
[L358](../lemmas/L358-regulated-mellin-spectrum-and-fixed-regulator-negative-signs.md).
It is not a global sign certificate.

At fixed ε>0, put s=1/4+iξ/2 and
S_ε(ξ)=Σ_(n≥1)n^(−1/2)exp(−πεn²−iξlog n). The separate
generators a_ε and z_ε now have integrable whole-line tails, unlike
their ε=0 counterparts. Substituting x=exp(2u), the covered gamma
and beta integrals give

\[
 F_\varepsilon(\xi)=-(\xi^2+1/4)\operatorname{Re}\left[
 \Gamma(s)\pi^{-s}S_\varepsilon(\xi)
 -\frac{\varepsilon^{s-1/2}}{2\sqrt\pi}
       \Gamma(s)\Gamma(1/2-s)\right].
\]

L358 supplies absolute integrability with two
logarithmic weights, summation of the damped Gaussian terms, and
vanishing boundary terms before applying P. On this real-frequency
line Γ(1/2−s)=conj Γ(s), so the subtracted term retains a real
cosine with amplitude proportional to |Γ(s)|². The leading term
is a real projection of Γ(s)S_ε, not a modulus square.

For ξ→+∞ at fixed ε, the gamma factor has decay exp(−πξ/4),
while the beta term has decay exp(−πξ/2). Its gamma phase derivative
grows like (1/2)log(ξ/(2π)). A lower bound on |S_ε| would make
the squared phase term dominant, but such a lower bound is not
available for all sufficiently small ε. Near small values of S_ε,
the cross term with S_ε′ must be retained. The completed sign test
uses the differentiated exact expression and normalizes by the
positive gamma envelope to avoid floating-point underflow.

Discovery used an ordinary NumPy/Stirling scan on 40≤ξ<20000
with step 1/10 and regulators 1/10, 3/100, 1/100, 3/1000 and
1/1000. No negatives appeared in the first two sampled scans;
this supplies no sign theorem. Selected samples from the last
three scans proposed exact rational frequencies. The separate
standard-library interval certificate then enclosed the exact
values, with geometric infinite-series tails, a sector-controlled
log-gamma remainder and Cauchy bounds for its derivatives. Its
output is saved under `scripts/gaussian-zero-mode/`.

The three negative signs are rigorous under L037's stated arithmetic
contracts and require any common threshold to be below 1/1000.
No ε-uniform asymptotic, shrinking-target recurrence, or sequence
of negative values with ε→0 has been established. That regulator
quantifier is the remaining part of this mechanism, not a conclusion
from the finite scan. The conditional fixed-regulator positive-tail
test also requires an unproved uniform lower bound on |S_ε|.

The downstream aim is a global first-sign transfer via L357.
Negative values for arbitrarily small ε would stop that certificate;
a fixed-regulator positive tail alone would leave the complementary
frequencies, the common regulator threshold and all higher signs.
