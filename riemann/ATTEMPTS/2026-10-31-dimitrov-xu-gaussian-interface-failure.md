# Printed Fourier/correlation interface: fixed-Gaussian failure

The approved source audit is proved in
[L563](../lemmas/L563-dimitrov-xu-fixed-gaussian-phase-audit.md).
It uses the source's negative Fourier phase, y=1 and the explicitly
displayed one-dimensional correlation normalization. It is a reproduction
of Gaussian/Fourier algebra, not a new Xi positivity result.

**WHY IT FAILS.** The odd sinh-weighted kernel has transform i times
the real imaginary part. Quadratic Wronskian scaling therefore changes
the correlation sum to a difference; the explicit integral also requires
a factor 1/2. In the Gaussian diagnostic the printed combination gives
the opposite sign to the actual Wronskian sum at x=pi. Fixing only a
constant or the sign of the sine integral cannot remove that disagreement.
The canonical proof retains the corrected fixed-Gaussian identity and
the valid spatial sum identity. This rejects the tested printed interface,
not Theorem 3.2 under all its hypotheses: the Gaussian lacks its required
zero-product factorization. It provides no actual-theta sign or L1
approximation. Constructive use remains parked pending independent
error control, and the earlier source-construction stop is preserved.
