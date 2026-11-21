# Step947 working record — approved center-normalization audit

Target: nomination945/review946's unchanged cubic-phase test.
Main gap: L030-L032/C032a actual-Xi all-degree positivity.
Test: establish generic feasibility, or an exact obstruction; a generic
positive jet parks this discriminator. Global integration and Xi transfer
remain independent. Existing stops927/932/941 and C466p are comparisons.

Work saved before completing the audit: for a symmetric holomorphic
coefficient G(w), G(0)=g>0, write w=v+t(1,1,1), sum v=0. Define
F(T,v)=integral_0^T G(v+s(1,1,1)) ds. The inspected holomorphic implicit
theorem applies to F(T,v)=g t at the origin since F_T(0,0)=g.
Candidate map: z_j=1+i(v_j+T(t,v)). Uniqueness should give permutation
equivariance. Differences are exactly i(u_j-u_i), so all collision
division is exact, including triple collisions. The full Jacobian
should be T_t, hence the divided coefficient is exactly g.

Still to write and verify in the canonical proof: parameter primitive,
first derivative, uniqueness on common invariant neighborhoods, both
linear-coordinate Jacobians and orientation, and the differentiated
Taylor remainder for degree-four truncation. No global inverse,
integrability or contour homology is asserted. Actual specialization
uses G(w)=product_j A_x(1+iw_j), not the stronger C466p certificates.
Completion: all listed checks are now proved in C466k's scope audit947,
including differentiated degree-five remainder before collision division.
The divided full germ is constant g; the degree-four truncation is
g+O(||u||^4). Test945 is generic and parked. This is an informative
negative control via a standard implicit-function specialization, not
a new sign theorem. The canonical home is existing C466k; no lemma
identifier is created merely for generic local feasibility. The earlier
tentative lines above are preserved as the pre-completion checkpoint.
