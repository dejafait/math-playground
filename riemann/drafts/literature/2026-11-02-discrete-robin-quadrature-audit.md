# Robin-residue partial quadrature — independent audit nomination

TARGET: Audit L681's bounded Robin-residue positive quadrature on L673's exact nodes, including the unit anchor, positive weights, all contour edges, continuous certificate and finite-n transfer at rate 3/500.
CHECKED: 2026-11-02
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: Reuse the unchanged primary prescribed-node comparison in drafts/literature/2026-11-02-discrete-parameter-positive-quadrature.md and the recorded fixed-gauge, finite-polar and continuum stops. This nomination adds no search or approval of the newly written proof-audit target.
SOURCE_EVIDENCE: The standard Cauchy residue theorem is the named import; L672 Sections 3--4 supply audited series/derivative costs, L673 Sections 1/6 the exact nodes, and L680 Sections 3/6 the audited parameter attenuation. L681 and its complete new certificate require separate independent reading and verification.
COMPARISON: The derived rate 3/500 improves the recorded positive rate 1/200 but is below 1/100. No inspected general quadrature theorem supplies its particular residues or costs; the audit must verify the family-specific specialization without presuming originality or arbitrary-weight optimality.
GAP: Independently verify the nodal census, residue signs and anchor, complete finite contour, every continuous-bound cost, the n-dependent top height and the final normalized L2 statement. Neither the strict-rate target nor original H/support/realization/Xi signs is proved.
REASON: This exact audit continuation is newly nominated after the mathematical attempt and is not approved in that same invocation. Separate next-turn approval is required; ready primary coverage should be reused rather than refreshed without a specific reason.

The bounded audit concerns only L681 as written for n=12q+3, q>=1,
x=-5/4, R=11/8, L673's exact implicit nodes, the full L666 W, and
normalized continuous angular L2. Do not change nodes, drop the j=0
factor or denominator angle, or infer constant-function exactness or
original unit-residue control from auxiliary weights.

Check the exact kernel D_n(z)=z*cosh(lambda*z)+rho*sinh(lambda*z)
and K_n in L681, including all its imaginary roots inside the rectangle
and the absence of others. Check both signs of the vertical kernel
bound, the exact horizontal phase at Y=2*q*h, positivity of every
residue, and the fixed unit residue at zero. Verify the extension of
the existing analytic derivative bounds to the actual compact domain.

The complete arithmetic is stored in
`scripts/one-sided-hankel/discrete-robin-quadrature-certificate.json`;
its generator is the neighboring `.py`. Check all relevant evidence,
the preserved-helper boundary, rational rounding and tails, both circle
charts, every interpolation cell (especially s=0), and the maximum.
The floating design screen is not evidence for the theorem. Check the
height cost 27/(20*n), full left-cell product including j=0, left-edge
exterior-disk estimate, parameter-point error, constants and q=1 onset.

Essential mathematical inputs are L666 (6), L672 Sections 3--4, L673's
exact nodes and L680's point attenuation; only those scoped claims
are used. No segment positivity or L679 mass hypothesis enters L681.
Continue on an independently verified partial estimate or a repaired
mathematical defect. If a load-bearing step fails, preserve the formula
and certificate and report the actual surviving bound. The rate-1/100
question remains unresolved even if this audit passes. Full matching
Mathlib coverage is unchecked; supporting formal facts are not a gate.
