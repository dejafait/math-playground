# Outer-half inner input — complete-response stop

The fixed outer-half grid input has an admissible Chebyshev response
countersequence in
[C645t](../lemmas/C645t-outer-half-inner-input-chebyshev-response-stop.md),
with odd m>=5, n=3m, radius 27/50 and unit original residues. The proof
was independently audited on 2 November 2026 without correction; its
classification does not certify originality.

WHY IT FAILS: Cancelling only the outer half retains enough correlated
inverse-grid weights for the full response to be exponentially small.
The canonical proof bounds the complete spatial boundary uniformly
over every rotation by 22000*m*exp(-7*n/200). This beats the required
decay exponent 1/32 by 3/800; multiplying the response by exp(n/32)
therefore tends to zero. The arc estimate and exact finite-node error
are both included, as are all complex phases. The first-pass n=9
auxiliary failure is retained; the proved sequence starts at n=15.
This is an upper bound on one unit input's output, not on the operator
norm. It neither refutes the angular detector nor supplies an off-line
zeta zero. Other inputs and the Xi bridges remain open.

This stops the precise outer-half lower-bound mechanism without
materially new input. The originally nominated conceptual audit is now
complete: its independent exact replay checks all 6322 boxes and all
analytic uses in the canonical proof. The full angular operator route
is still open; this record imposes no ban on a different input.
