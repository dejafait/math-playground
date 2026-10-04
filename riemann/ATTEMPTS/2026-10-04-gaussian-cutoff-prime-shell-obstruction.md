# Gaussian cutoff prime-shell obstruction — 2026-10-04

The prior SPECIALIZE assessment covered this invocation's unchanged
large-frequency spectral target. The proposed phase template added
a growing shell at R=ε^(−1/2) to an arbitrary fixed prime head,
with +1 on every intervening prime. The result is
[L361](../lemmas/L361-gaussian-cutoff-prime-shells-cannot-cancel-fixed-head.md).

WHY IT FAILS: even arbitrary phases on every prime above a fixed
multiple of R change the Gaussian sum by only O(√R/log R), uniformly
in those phases. The fixed head retains a nonzero main term of
order √R. Thus the shell cannot produce the zero-valued template
needed for the proposed arbitrarily high-frequency cancellation
construction. This obstruction differs from L360's small-support
convolution bound and does not control arbitrary phases on the
growing intermediate primes. It does not exclude coupled finite
frequency negative signs, decide the regulator quantifier, or imply
an actual-theta sign. The next mechanism allows phases throughout
the growing range below the cutoff and retains L359's derivative,
rotated-phase and actual-frequency requirements.
