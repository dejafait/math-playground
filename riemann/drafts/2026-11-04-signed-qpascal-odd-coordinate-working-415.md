# Signed q-Pascal odd-coordinate attempt — step415

Gate: the supplied SPECIALIZE assessment
`literature/2026-11-04-signed-qpascal-odd-coordinate-test.md`.
Only its e_1 test at k=d=r-1 is attempted. Main gap: actual-Xi
all-degree mixed positivity. Desired threshold is Q_r>0; eventual
Q_r<=0 abandons this strict-accretivity interface, not determinant
positivity or RH. Existing unfinished work is preserved.

## Checkpoint before completing the proof

Row1 of L^(-1) is (-1,1,0,...), and |D_1|=1-q. Preliminary
algebra gives

    Q_r = [2 exp(h_(k-1))-exp(h_k)-q exp(h_(k-2))]/(1-q).

This requires checking the constant terms and J_11=-1. The surviving
coefficient indices are k-1,k,k+1,2k,2k-1,2k-2, all large as
k tends to infinity. Thus the index0 endpoint of the full matrix does
not enter this coordinate.

For s=k,k-1 the exact adjacent defect is

    h_s-h_(s-1) = f(k+s)-f(k+s-1)-f(k+1)+f(k)+tau*(s-1).

Use audited L765's finite-value expansion f(n)=G(n)+epsilon_n,
|epsilon_n|=O(log(n)^2/n^2), and its explicit U'' and B0'
estimates. The amplified error in this adjacent expression is
O(k log(k)^2/k^2)=o(1), rather than the O(log(k)^2) error for
each individual h. Expected limit of both adjacent defects is
b=2-2log(2)>0; the normalized Q numerator would tend to
2-exp(b)-exp(-b)<0. This remains provisional until the canonical
proof checks every identity, finite-value error and normalization.

No full matrix scan, altered preconditioner, new uniform sign claim,
or mathematical script is authorized or needed.

## Completed disposition

The identities, finite-value error budget and strictly negative limit
are proved in canonical L774. The error for each adjacent defect is
O(log(k)^2/k)=o(1); K=2 suffices. The exact coordinate normalization
is positive, so the limit proves eventual Q_r<0 without controlling
the separate large exponentials or an effective onset. The finite
determinant-transfer signs are checked there as well. The provisional
calculation above is resolved; the new specialization awaits a separate
critical audit. No actual minor sign or RH conclusion follows.
