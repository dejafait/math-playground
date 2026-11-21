# Once-rounded normalized width: working record1830

Approved target: C033z one-time normalized-width conversion before eight
exact Newton steps, error<=2^-60, cost<=322 including clamps, every
iterate denominator bounded independently of the input denominator.
Prior gate: drafts/literature/2026-11-19-normalized-width-dyadic-review-1827.md,
SPECIALIZE, separately approved1829. This is numerical reproduction,
not a new central RH mechanism. Preserve all1823 execution artifacts.

Candidate saved before verification: retain1825 normalization a=W/4^k,
h=2^-k,0<=k<=15. Bisect [1/4,1]64 times by exact comparisons with a,
retaining the lower half on equality; take its final midpoint b.
Then b in[1/4,1], |a-b|<=3*2^-67, denominator(b) divides2^67.
Run x0=1, x_(n+1)=x_n*(3-b*x_n^2)/2 for eight steps.

Proposed proof bounds, not yet independently audited: reuse the1825
Brent-Zimmermann specialization for b, e8<2^-65. Since h*b^-1/2<=2,
Newton output error<2^-64. The derivative bound4 on[1/4,1] gives
coefficient error<=3*2^-65. Add1802 input error<2^-123; total
<5*2^-65+2^-123<2^-62<2^-60. Panel projection is nonexpansive.

Candidate complete ledger:94+64*3+2=288<=322. Dyadic induction:
d0=0,d_(n+1)=3*d_n+68, so d_n=34*(3^n-1), d8=223040.
denominator(x_n) divides2^d_n; rescaling adds k<=15 to the exponent.
Normalization/comparison may retain arbitrary input denominators.
No bit/runtime, changed global ledger, profile/scalar or RH claim.

Pending: write complete continuum/equality proof in canonical C033z;
check exact error arithmetic, all reduction ledgers, coefficient-grid
endpoints/equalities and samples, all iterate/intermediate denominator
divisibilities; save full certificate, then run scoped structure validation.

Completed1830: the candidate is now proved in canonical C033z extension1830,
including the exact (odd-numerator) denominator statement. All92 finite
checks pass in scripts/smoothed-law/width_dyadic_1830.json. Independent
application audit remains pending under the separate REVIEW_REQUIRED
assessment1830. This working snapshot is historical, not a second proof.
