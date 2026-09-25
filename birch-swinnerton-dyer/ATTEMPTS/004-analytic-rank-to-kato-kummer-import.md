# Importing a strict Kummer class from analytic rank through nonvanishing

Date: 2026-09-25. Outcome: informative negative for the proposed direct
use of Castella--Hsieh's 2022 theorem from m(E) = 2 alone.

## WHY IT FAILS

The [published-source audit](../foundations/07-castella-hsieh-nonvanishing.md)
shows that Theorem A compares nonzero generalised Kato classes with
Selmer dimension two, with nonzero localization needed for its stated
converse. It supplies neither from complex analytic order two alone.
Theorem B instead assumes positive rational rank and an anticyclotomic
theta order; Section 5.7 adds finite p-primary Sha before identifying
the class with a rational-point regulator. Importing that identification
without its premise would erase precisely the unresolved Kummer defect.
[L006](../lemmas/L006-generalised-kato-kummer-certificate.md) retains the
useful upper bound and proves that Kummer membership would close it
without a cyclotomic coefficient. Even after Theorem B's point premise,
the resulting bound 1 <= r <= 2 still misses r >= 2. This rejects the
inference, not the paper's theorem or the possibility of proving
Kummer membership by a different geometric mechanism.
