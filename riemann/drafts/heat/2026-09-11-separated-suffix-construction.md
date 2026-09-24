# Separated suffix construction checkpoint — 2026-09-11

DRAFT, not yet promoted. Set N_k=2^(4k²), d_k=sqrt(N_k), k≥1,
and prescribe S={1} union {N_k+j d_k: 0≤j<d_k}. At s in S put
x_s=s^(3/4). Between consecutive s<t in S put
x_n=sqrt(n) t^(1/4)(1+(t−n)/(4t)). This should give exactly S as
suffix minima: a_n decreases on gap interiors to a_t, whereas prescribed
a_s=s^(1/4) increases. The continuous gap formula is increasing and
its value at s exceeds x_s. Also x_n≥n^(3/4), giving summability.
Each active block contributes at least 1/sqrt(2) to suffix weights,
M=d, A²=d, spacing d, so T=1+H_(d−1)/d≤2.
Only dyadic blocks N_k and N_k/2 meet each cluster; the latter contains
no cluster index because its right endpoint is excluded (thus only N_k
actually meets it). For arbitrary [N,2N), at most one cluster occurs
apart from a finite prefix. Need audit M≤C sqrt(N), giving R≥c log N,
and dyadic R at N_k equals 2+log d_k, whose inverses sum over k.
Resume: audit all endpoints, exact S, arbitrary-block lower bound and
then store a full lemma. No universal near-sum claim or RH result.

Completed: the endpoint and arbitrary-block audits are proved in
`lemmas/L093-separated-suffix-blocks-realize-the-spacing-criterion.md`.
All requested conditions are compatible. No unfinished claim from this
construction is used as an input.
