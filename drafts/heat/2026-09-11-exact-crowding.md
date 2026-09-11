# Exact crowding checkpoint — 2026-09-11

Draft, unproved pending audit. Define C_N=max_{N≤r<4N} sum_{n in B_N,n≤r}
1/(r-n+1), V_N=N C_N/(M_N A_N²). Lemma 92's finite expansion gives
average Q≤32 V_N D_N. The same height budget gives bounded-V and
divergent dyadic inverse-V criteria.

Construction candidate: U_k=2^(4k²), d_k=sqrt(U_k), use prescribed
indices U_k+j d_k and U_k+j d_k+1 for 0≤j<d_k, plus 1.
Use the interpolation of Lemma 93 with x_s=s^(3/4). Two grids imply
C_(U_k)≤2(1+H_(d_k-1)/d_k)≤4, hence V≤2. Every contiguous
block intersection with at least three prescribed points contains an
adjacent pair, giving minimum spacing 1. With M≤2sqrt(U)<2sqrt(2N)
and A²<sqrt(2N), expect T≥(1+H_(M-1))sqrt(N/2)/M→∞
uniformly; use decreasing (1+H_(m-1))/m and integer ceiling.
For M≤2 use T≥sqrt(N/2)/2. Aligned dyadic T=(1+H_(2d-1))/2,
so inverse T sums converge since log d is proportional to k².

Resume: audit all-block lower bound using a split M≤N^(1/4) versus
M>N^(1/4), avoiding rounding. Then write criterion and construction
as separate proved lemmas, update DAG/history/progress and validate.

Completed: the criterion and construction were audited and stored in
`lemmas/L094-exact-crowding-height-budget-selection.md` and
`lemmas/L095-paired-suffix-blocks-realize-exact-crowding.md`.
The split by M versus N^(1/4) proves the uniform all-block limit.
No remaining draft claim is used as an established input.
