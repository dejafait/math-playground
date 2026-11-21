# Formal half-factor: first Hermite-block detector retires

The approved asymptotic test has an informative negative outcome for
the detector. [C795a](../lemmas/C795a-formal-half-factor-eventual-hermite-block-positivity.md)
proves that the first 3-by-3 Hermite block of the formal centered
actual-theta additive half-factor is positive definite eventually,
using fixed coefficient order K=4. No degree sweep was performed.
The normalized determinant tends to 1/8; every principal minor has a
strictly positive limit. The analytic proof awaits separate audit.

**WHY IT FAILS.** An eventual negative minor of this proper block
cannot obstruct the all-degree half-factor proposal: the exact
fourth-moment cancellation leaves a positive margin, with controlled
vanishing error. Positivity of this block does not establish full-factor
hyperbolicity, nor handle finite exceptional degrees, shifted/mixed
positivity or RH. The uniform proposal itself is neither proved nor
refuted. L825's common-symbol stop remains a different obstruction.

Retire this fixed detector after its conceptual audit. Do not increase
the matrix size or asymptotic order automatically. A later central
mechanism requires a distinct test and its own source coverage.

Step767 completed that conceptual audit; its proof details and corrected
derivative recursion are recorded in C795a. The earlier pending status
above is historical: the eventual positive-definiteness claim passes,
and this fixed detector is now retired. Its scope exclusions remain.
