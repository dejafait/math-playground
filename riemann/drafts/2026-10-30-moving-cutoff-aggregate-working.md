# Moving-cutoff aggregate calculation — saved reasoning

Approved target: the exact COVERED_TARGET in
`drafts/literature/2026-10-29-moving-cutoff-aggregate-coverage.md`.
Read L483 and L471 completely, L467 including its local audit, and the
moving-cutoff source notes. Existing unfinished files are preserved.

For each fixed sufficiently large real T, freeze
L=log T, l=log L and delta=100 l/L. Restrict the original pairs to
d_j>=delta. L483's finite nonnegative kernel argument, before its
fixed substitution, gives

    B_delta(T)^2 <= 18 delta^(-3) log(2T+2) H_delta(3T) Q_4(T),
    H_delta(U)=8.604 U^a log^3 U+9.461 log^2 U+167.8 log U,
    a=3(1/2-delta)/(3/2-delta)=1-4delta/(3-2delta).

The selected right-side zeros have beta>=1/2+delta. The assessed
inclusive corollary is uniform for delta in [0,1/8]. The padding is
still 3T, not a changed definition of delta. For T large enough,
0<delta<=1/8 and 3T>=3*10^12 simultaneously. No differentiation
with respect to T or limiting sum interchange is needed.

Candidate scale comparison being checked: 1-a>=4delta/3 and
(3T)^a=3T exp(-(1-a)log(3T))<=3T L^(-400/3).
Thus, retaining both additive terms,

    B_delta(T)^2 = O((T^2 L^(-367/3)+T L^10+T L^9)/l^3).

After division by T^2 L^6 this is
O((L^(-385/3)+T^(-1)L^4+T^(-1)L^3)/l^3), tending to zero.
All constants in these O terms must be independent of moving delta;
the explicit uniform density constants and fixed fourth-moment input
provide that property. Check the finite kernel proof, endpoint cases
and exponents before canonicalizing. No complementary-sector estimate
or full N(T) saving follows. This is known-tool specialization, not
a new density/moment theorem or a creative mechanism.

Completed: the full proof and precise imports are canonical in C483a.
Both additive density remainders survive in its explicit squared
bound, and the normalized squared bound tends to zero. No mathematical
script was needed. A separate critical application audit is pending;
the saved reasoning above is not a second canonical proof.
