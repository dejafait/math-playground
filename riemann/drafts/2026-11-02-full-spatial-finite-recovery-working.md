# Full spatial finite-recovery test — working record

Approved target and source gate: the unchanged EXPLORE assessment
`drafts/literature/2026-11-02-displaced-full-spatial-fixed-angle.md`.
Test the full fixed-angle bound m(-1)>=-n/100-C log n for L666's
independent displacements. Main gap: actual-Xi mixed positivity and
unbounded-height signs. A successful bound could feed L658 using
L661's audited diagonal envelope. General support and realization remain
independent gaps. Reuse the inspected Gautschi and Akhtari--Vaaler
sources; no new theorem-dependent mechanism is being approved.

Inspected L649's definitions and ambient stop, L666's family and its
admissibility proof, L657's nonzero-slice interpolation argument,
L658's threshold, L661's general envelope, L664's complete-root bridge,
and the recorded L660/L665/scalar-route stops. The finite inverse cost
test is different from their ambient, monomial and scalar mechanisms.

Partial calculation, not yet a result: put N=M-1=4q, z_a=a/R,
w_a=W_a(-1), and let ell_a(z)=prod_(b!=a)(z-z_b)/(z_a-z_b).
Then w_a=R sum_(k=0)^N ell_(a,k)c_k. Applying the inspected
degree-indexed coefficient/Mahler bound to all coefficients gives the
certified lower value |w_a|/[R sum_k |ell_(a,k)| binom(N,k)].
The constant coefficient of ell_a has modulus prod_(b!=a)|b|/|a-b|.
All |b|>=5/4 while |a-b|<9/10, suggesting a uniform cost at least
(25/18)^N for every row. At the anchor the gap bound improves to
9/20. Need verify |w_a|<=1 at u=-1, handle actual degree drops,
and distinguish the small certified lower value from the true Mahler
measure. This is a test of this triangle transfer only.

Continuation/stop test: retain exact finite row sums and every spatial
moment, with all normalization and binomial costs. A verified linear
loss exceeding 1/100 stops this transfer; it does not refute the target,
H, or RH. No numerical screen is proposed. Save a canonical proof only
after completing the sign and degree qualifications.

Completed: L667 is the canonical proof. Every individual row, even
using the actual spatial degree, has an exact triangle/Mahler cost
at least (25/18)^(M-1), whereas every |W_a(-1)|<=1. The best certified
logarithmic lower value is therefore at most -7n/75+O(1). This is
new quantitative negative evidence about this transfer, not an upper
bound on the actual mean. No numerical computation was needed.

The individual-row transfer is stopped. A different possible functional
combines rows with the actual inverse weights before taking absolute
values. Its signed cancellations have not been estimated or approved;
the exact proposed cost test is nominated separately with REVIEW_REQUIRED
in `drafts/literature/2026-11-02-signed-finite-deweighting-cost.md`.
The prior paragraphs preserve the partial reasoning, not pending work.
