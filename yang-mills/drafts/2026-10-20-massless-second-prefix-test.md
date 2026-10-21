# Massless second-prefix test — saved working record

Gate-approved target: the massless second-prefix COVERED_TARGET in
`literature/2026-10-20-smooth-action-branch-quantitative-remainder.md`.
Main gap: interacting reflected-error control <=c_box/2, continuum
axioms and finite positive infrared mass. Intermediate use: replace the
second prefix before attempting quantitative ordered static comparison
with L179's coefficient; that independent comparison remains unproved.

Inputs read: L028's consistency statement, L156 sections 2--3, L159
sections 3--4, L175 sections 1--2, and the full L176/L177 proofs.
The saved source assessment and ATTEMPTS/030,038,045 are reused. L177
has only the left-mass-dependent bound; no matching massless result was
found in the scoped duplicate search. No external refresh is needed.

Candidate finite estimate: set Y=M tensor G and Z=F^0-F. L177(8)
gives Z Delta Z^T<=I tensor G^2. After L159's massless multiplier
bound, the remaining positive energy trace is bounded by
Tr M times Tr[G J_j G^2 J_j^T]. Keep the two G^(1/2) factors around
C=J_j G^(1/2), whose operator norm is <=2 on the full pinned space.
The weighted HS inequality proved after L159(16), specialized to G,
gives ||G^(1/2) C G^(1/2)||_HS^2<=4 Tr G^2<=C N^4.
Thus the rough factor is O(p(l)), the supported factor O(p(k)N^(3/2))
and the generator O(N), reaching the requested N^(5/2) count.

Before acceptance: write the diagonal-basis inequality completely,
check the rectangular trace order, retain all end rows and the constant
axial mode in the exact identity, and sum the polynomial mode envelope.
Continue if those checks close; abandon this factorization if they
require a covariance/multiplier commutation or leave a higher count.
This draft is the preserved initial reasoning, not a separate assessment.

Completed in [L256](../lemmas/L256-massless-second-prefix-quantitative-comparison.md):
the full weighted HS proof, ordered factorization and entire heat sum
close at N^(5/2). The canonical proof retains the pinned ends and
constant mode through L177's exact identity. Its separate critical
audit and the independent ordered static comparison remain pending;
this completion does not approve a new target.
