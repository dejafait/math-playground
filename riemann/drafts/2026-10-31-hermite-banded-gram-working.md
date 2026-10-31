# Hermite bandwidth-two leading-block attempt

Approved target and source gate: the unchanged EXPLORE assessment
`literature/2026-10-31-hermite-banded-gram-diagnostic.md`. Main gap:
actual-Xi all-degree positivity. This attempt tests only the highest
four even coefficients of D(P_N) against the proposed sparse PSD Gram
matrix. L564 supplies actual coefficients; audited L565 and its cone
stop are retained. No manuscript audit, full Gram construction or Xi
sign is claimed.

Working normalization: m=2N, q=m-1, A=(-1)^N 2^m b_m,
p=P_N/A, h_j=H_j/2^j. Seek D(p)=h^T C h, with C PSD and zeros
between opposite parities and outside distance two. Positive diagonal
congruence converts between C and the specified original Gram matrix.
The four coefficients see diagonals x_i=C_(q-i,q-i), i=0,...,3,
and off-diagonals y_i=C_(q-i,q-i-2), i=0,...,2, except y_2 is
absent at N=2. For N>=3 the endpoint x_4 is below their degrees but
must be retained in the necessary PSD test.

Partial reasoning, not yet a verified result: the affine system is
triangular, with x_0=m and successive new terms x_1+2y_0,
x_2+2y_1, x_3+2y_2. One can try x_1=1, choose y_0 from the first
equation, x_2=y_0^2/m+1, choose y_1 from the second, x_3=y_1^2+1,
choose y_2 from the third, and x_4=y_2^2+1. The affected parity
blocks would then be positive definite by direct square completion.
If this survives complete coefficient bookkeeping, the diagnostic
is non-discriminating at every N>=3, including all L564 cutoffs.

At N=2, p=t^4-a t^2+c, a=3+b_2/(4b_4),
c=3/4+b_2/(8b_4)+b_0/(16b_4). All four coefficients are present;
the actual condition and any rigorous coefficient bounds remain to
be checked. Do not transfer a finite-cutoff failure to unbounded N.

Next within this attempt: write all four complete-discriminant and
Hermite-product coefficient equations, prove or reject the proposed
blocks including singular alternatives, and resolve or explicitly
retain the N=2 actual-coefficient condition. Any completed proof
belongs in a canonical lemma; this file preserves interruption state.

Completed within the approved scope: L566 contains the complete four
equations and all contributing entries, including the unconstrained
x_4. The displayed construction works for every N>=3 and has explicit
positive-definite supported blocks. For actual N=2, the rational
certificate in `scripts/hermite-gram/leading-block-boundary-certificate.json`
establishes Q<0 and excludes every PSD representation, singular or not.
The finite exception does not reach any L564 cutoff. Outcome: NEGATIVE
for this diagnostic's ability to discriminate at unbounded cutoffs;
the full bandwidth-two certificate is not abandoned. Canonical proof
and certificate await an independent audit; no RH sign follows.
