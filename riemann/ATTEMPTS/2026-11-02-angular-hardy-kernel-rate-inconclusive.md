# Optimized Hardy kernels — rate test inconclusive

The bounded attempt used the ready angular scope on the r=27/50,
odd m>=5, n=3m unit-residue Chebyshev family. The exact full-response
identities and polynomial comparison are canonical in
[C645u](../lemmas/C645u-hardy-kernel-full-symbol-rate-comparison.md).
The attempted c exp(-n/32) lower bound and a faster-decay upper bound
both remain unproved. Outcome: EXPLORATION.

WHY IT FAILS: Optimizing the argument of a kernel with radius 1-1/n
changes the complete constant-input response by at most polynomial
factors. The required exponential estimate for that response is still
missing. The saved finite screen is unenclosed, and the optional
high-precision checks were not run because mpmath was unavailable.
Its large oblique negative-grid samples therefore prove neither a
lower bound nor an asymptotic. They nominate a different signed
finite-node test: isolate the first Chebyshev alias near 13*pi/16,
including the entire higher-alias remainder and a fixed angular
sector. The earlier endpoint and inner-input stops do not decide it.

The full diagnostic and unfinished continuation are in
`scripts/one-sided-hankel/angular-hardy-kernel-screen.json` and
[the working record](../drafts/2026-11-02-angular-hardy-kernel-working.md).
No assertion about general pole families, Xi signs or RH follows.
