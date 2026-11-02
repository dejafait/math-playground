# Complete ratio coefficient certificate: stopped implementation

The gate-approved target applied Jaming--Saba v1 Theorem 4.2/(4.4) to
the entire grouped L481 ratio spectrum on [T,2T]. The ready assessment
is [the prior comparison](../drafts/literature/2026-10-31-grouped-ratio-nazarov-certificate.md).
The complete proof is [L572](../lemmas/L572-grouped-ratio-short-interval-certificate-stop.md).

WHY IT FAILS: the exact minimum gap makes the normalized interval
length exceed one by only Theta(T^(-1/2)), uniformly in the cutoff's
floor remainder. Keeping the theorem's excess-length loss and the
complete ascending-rank coefficient sum yields a certificate of size
Theta(T^(-3)(log T)^3). Its ratio to the required T(log T)^3 is
Theta(T^(-4)), so no unbounded sequence rescues this implementation.
Translations, subintervals and smaller common-gap normalizations do
not improve it. This bounds the certificate only, not the actual L1
norm. No block deletion, shifted rank or curved-phase theorem is used.

The exact ratio L1 norm and the independent full-residual cancellation
problem remain open, as do L477's defect thresholds, negative-mass
saving and actual-Xi all-degree positivity. The older Hardy/Haar,
sign-multiplier, stationary-involution and constructive-chirp stops
are preserved. Reopening this certificate requires a materially
stronger quantitative inequality or a different, fully justified
functional; repeating its normalization is not a new mechanism.
