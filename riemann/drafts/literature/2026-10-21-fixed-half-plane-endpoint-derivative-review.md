# Changed source hypothesis: endpoint derivative comparison

TARGET: Compare the October 2026 fixed zero-free half-plane input with L330's moving-height logarithmic-derivative threshold and L331's disk criterion, identifying any applicable quantitative theorem before an endpoint proof attempt.
CHECKED: 2026-10-21
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: The family 003 overlap review found a fixed zero-free half-plane absent from L330/L331's tested inputs; searched fixed-half-plane logarithmic-derivative and Littlewood terminology, but did not establish a primary quantitative theorem meeting either precise criterion.
SOURCE_EVIDENCE: OpenAI Theorem 1.1 and Liu v2 Theorem 27.1 state fixed half-planes; read L330/L331 in full and the classical derivative inputs in foundations. The exact derivative/reciprocal consequences of the new region still require primary theorem inspection and applicability review.
COMPARISON: L330 needs a little-o bound uniformly on a shrinking height window near Re(s)=1; L331 needs analytic disk bounds relative to r*d. Neither is literally the external nonvanishing theorem. The old classical envelopes alone missed both criteria, but a fixed region changes the comparison and prevents recycling that failure as a verdict on the new input.
GAP: Locate and check quantitative logarithmic-derivative and reciprocal estimates under a fixed zero-free half-plane, including their uniformity as Re(s) tends to 1 and height tends to infinity on the prescribed coupled ray. Decide whether they imply either exact criterion; do not assume a small derivative merely from nonvanishing.
REASON: New relevant primary source changes the analytic hypothesis of a parked route. This is a separate literature comparison before any new calculation or lemma modification.
SCOPE: The exact L330/L331 criteria only; no assertion of an endpoint sign, all-index positivity, critical-line nonvanishing or full RH.

## Exact interfaces to compare

L330 fixes r=2n, a_n=sqrt(4*pi^2*exp(4r)-25), sigma=1+1/r,
V_r=log(r)/sqrt(r), and g=zeta'/zeta. Its sufficient target is

    sup_{|u|<=V_r}|g(sigma+i(a_n+u))|=o(sqrt(r)).

The conclusion must hold on this coupled sequence, uniformly in u.
The older available envelopes were O(r) and
O(r^(2/3)(log r)^(1/3)); failure of these envelopes is not a lower
bound on g. The required relative comparison is with B_r first,
not directly with the exponential final error E_r. A theorem about
zeros to the right of 7/8 does not itself state this derivative bound.

L331 centers at sigma_0=1+1/(2r), on the same height a_n.
For 0<d<=1/8, its sufficient criterion is analyticity of g on a
neighborhood of the closed disk of radius 2d and a disk supremum
M<=r*d/4. Its previous d was forced to shrink with the classical
region. Check both the available radius and the quantitative bound
under the new hypothesis; do not retain the old radius by default.

Even satisfying either interface would need a separate mathematical
application and review. A local saddle still requires higher-order
errors and complementary-contour control. A successful endpoint
margin would leave smaller indices and passage to all heights open.
No pure half-plane citation resolves these separate obligations.

The family 003 register's formal verification qualifications remain
in force. Reuse the existing external result rather than rerunning
its research proof; formal-artifact verification is a distinct task.
