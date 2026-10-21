# Entire-map reduction at thirteen — working attempt

Approved target: certify good reduction at thirteen of L034's entire
degree-twelve modular map, including both x=16 charts and O. Reuse
`drafts/literature/2026-10-14-modular-map-thirteen-good-reduction.md`
(SPECIALIZE); no new source review or global point enumeration.

Initial reasoning saved before verification: write N=a+by and
N'=a-b-by. L034 gives NN'=-(x-16)^11 h^3. On the affine curve use
j=N/d where d is invertible, j=-h^3/N' near 2T, and 1/j=d/N near
3T. The two constants at x=16 must be checked as thirteen-adic units.
At O set t=-x/y and w=-1/y; the projective equation gives
w U=t^3, U=1+t^2+(10t-1)w+20w^2. On U invertible put V=1/U,
so w=t^3 V. Clearing the numerator should give j=Q/[t H],
H=(1-16t^2 V)^11 and Q(O)=-1. These chart identities, coverage,
special-fiber pole orders 11 and 1, and separability still require
complete verification. No result is asserted at this checkpoint.

Completed result: [L066](../lemmas/L066-modular-map-thirteen-good-reduction.md)
supplies all integral charts, gluing, the full reduced pole divisor
O+11(3T), separable degree twelve and entire unramified base change.
All 20 exact checks pass in
`scripts/modular-map-thirteen/reduction-certificate.json`; complete
origin chart polynomials, x=16 evaluations and residuals were inspected.
The approved continuation test succeeds. No matching-fiber shortcut,
new global point theorem or novelty claim is used.

Keep thirteen as a map-reduction candidate, subject to independent
critical audit. Rank/index, translated coverings, coset zero tests
and global primitive power lifting remain unresolved. The next
assessment is a separate coverage gate for this audit, not an
approval derived from the completed mathematical calculation.
