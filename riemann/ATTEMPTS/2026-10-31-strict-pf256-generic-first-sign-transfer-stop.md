# Strict PF256 alone does not transfer the first polynomial sign

The independent conceptual audit verifies the fixed-model obstruction in
[L562](../lemmas/L562-fixed-reciprocal-model-global-pf256-certificate.md),
using the retained density, transform, regularity and sign inputs in
[L561](../lemmas/L561-fixed-high-rank-reciprocal-density-partial-certificate.md).
The exact scalar replays passed 9/9 and 13/13 checks; the canonical analytic
audit verifies the uniform determinant argument that those scripts do not.

WHY IT FAILS: this positive even C^542 probability density is strictly PF256
at all real ordered tuples, but its reciprocal polynomial has a negative
first Laguerre sign at A=2^20. The transform identity is only asserted for
|Re z|<1; the offending point lies outside that strip. Therefore strict
PF256 and the stated reciprocal-transform identity do not imply an
all-real first sign. No actual-Xi counterexample follows. Xi-specific
growth, arithmetic structure, infinite-product restrictions or stronger
joint hypotheses remain distinct questions; reopening needs such an
explicit new input and a discriminating test.

The reviewed specialization is local progress, not certified novelty.
All earlier PF2, actual-theta Fourier-transfer and parity-block stops
remain preserved with their original scopes.
