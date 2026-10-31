# L566 independent audit working checkpoint

Approved exact target: audit L566's four-coefficient construction for all
N>=3, actual N=2 obstruction, singular cases and entire certificate.
Assessment: literature/2026-10-31-l566-banded-leading-test-audit.md
(SPECIALIZE, supplied at invocation start). Main gap: actual-Xi
all-degree positivity. This audit changes confidence in the diagnostic,
not its scope or the unresolved full restricted-Gram/Xi-transfer gaps.

Initial paper check: monomial cross coefficient is i+j-(i-j)^2;
all four d_k and the visible-diagonal/off-diagonal lists agree. At N=2
y_2 is absent; at N>=3 x_4 exists and remains free. Completing the
m>0 square yields the stated singular 2-by-2 PSD alternatives; the
chosen x_2,x_3,x_4 give the exact positive square completions. Diagonal
congruence uses A^2 E^-1 C E^-1, hence preserves sparsity and PSD.
At N=2, A=16b_4 and D(P_2)(sqrt(a/2))=16aQ agree algebraically.
These preliminary checks are not yet final audit acceptance.

Remaining work within this audit: replay original exact interval
certificate, inspect complete relevant evidence programmatically,
independently verify every panel and its summation, exp/Taylor and
Machin bounds, both omitted tails, exact sign and boundary bookkeeping.
Then record the qualified result in L566 and concise history/checkpoint.
No source search, new mechanism, full Gram matching or RH sign authorized
within this step. Existing files and unfinished work are preserved.

Completed audit: no mathematical repair. Canonical full audit and command
are in L566; `scripts/hermite-gram/l566-certificate-audit.json` records
all 3072 panels, interval-primitive checks, 22744 independent exponential
enclosures, 20236 analytic clipped calls, both tails and exact Q<0.
The original certificate is byte-identical on replay. The independent
harness initially needed the exp(0)=1 singleton handled exactly; that
was corrected without changing the original implementation or evidence.
All remaining mathematical limitations above remain. The separate
proposed full-polynomial global dual target is REVIEW_REQUIRED; it was
not derived, approved or attempted here. This working checkpoint is
closed; current routing and Next action are solely in PROGRESS.md.
