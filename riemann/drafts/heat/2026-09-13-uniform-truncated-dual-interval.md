# Uniform truncated dual intervals — 2026-09-13

Checkpoint: existing L175 and L176 are complete and preserved. For fixed
N≤y≤2N, apply the same C^4 transform on [N,y] with M=N, Q=a;
the standard input requires M≥y−N, not equality. Handle y=N separately.
Define D_y over [a/y,a/N] and Q_y over [2N²/y,2N], retaining sqrt(a)/k.
With δ=2N²−a, the correction strips are [a/y,2N²/y) and
(a/N,2N]. Their widths are at most δ/N=O(sqrt(N)). They can
overlap when y is close to N: prove the signed indicator identity
without an overlap assumption. For each fixed y the pair supports in t
are intervals, so L176's harmonic square estimate is uniform in y.
Resume with endpoint bookkeeping and constants before promoting any claim.
The sought full-sum first-moment decay is still unproved.

## Completed

L177 proves the uniform transform and boundary replacement. The signed
indicator identity handles overlapping strips and the degenerate endpoint;
the mean-square bound has constants independent of y. Uniform first-moment
decay remains unproved. The assertion concerns sup_y E_B, not E_B sup_y.
