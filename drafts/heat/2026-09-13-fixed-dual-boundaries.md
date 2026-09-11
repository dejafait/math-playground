# Fixed dual boundaries — 2026-09-13

Checkpoint: L175 is complete; preserve its stationary transform. Write
δ=2N²−a=(2T−t)/(2π)+1/4, so 1/4≤δ≤h/(2π)+1/4.
The moving range adds a lower strip below N and removes an upper strip
near 2N, each supported on O(h/N+1)=O(sqrt(N)) integers.
Proposed proof: expand each strip's square. Each pair of cutoff indicators
has interval support in t. Integrating a(t)/(kl) against the logarithmic
phase over that interval costs O(1/|log(k/l)|), since its supremum and
variation are bounded. Harmonic summation then gives square mean
O(K+NK log(2K)/h), hence first mean O(N^(1/4)).
Resume by checking strict/closed endpoints, both interval supports and the
amplitude variation before promoting the bound. No first-moment decay
for the complete sum is claimed.

## Completed

L176 proves the proposed estimate for both strips, with exact closed/strict
endpoint bookkeeping. Pair supports are intervals; coefficient supremum
and variation are O(1). The square mean is O(sqrt(N)), yielding the
claimed O(N^(1/4)) first-moment replacement. Complete-sum decay remains
unproved. No failed approach or numerical certificate arose in this step.
