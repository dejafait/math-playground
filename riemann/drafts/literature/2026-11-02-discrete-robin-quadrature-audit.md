# Robin-residue partial quadrature — independent audit nomination

TARGET: Audit L681's bounded Robin-residue positive quadrature on L673's exact nodes, including the unit anchor, positive weights, all contour edges, continuous certificate and finite-n transfer at rate 3/500.
CHECKED: 2026-11-02
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed prescribed-node search and primary comparisons in drafts/literature/2026-11-02-discrete-parameter-positive-quadrature.md; read L681 to identify its actual standard input and remaining audit cases. Directly retrieved NIST DLMF 1.10(iii)--(iv), especially 1.10.8 and its hypotheses. Checked the scoped fixed-gauge and finite-polar failure records; no repeated broad search or novelty claim.
SOURCE_EVIDENCE: NIST DLMF, online text retrieved 2026-11-02, Section 1.10(iii) Laurent residue definition and Section 1.10(iv), equation (1.10.8), complete statement and positive orientation clause; source notes cite Copson (1935), pp.117--120, not independently read. Reused the previously inspected quadrature theorems and local audited L672/L673/L680 inputs with their existing qualifications; no certificate replay or mathematical audit was performed.
COMPARISON: Cauchy's residue theorem supplies the finite contour identity conditional on its analytic and pole hypotheses. It does not supply the Robin zero census, weights, continuous exponent or uniform finite-n costs. The existing positive-discretization and sampling comparisons remain adequate; none is a matching import for L681. The audit checks this family-specific specialization, without re-proving standard contour theory or asserting originality.
GAP: Verify L681's claimed anchor, positive residues, complete contour, continuous arithmetic coverage, shifted top height and normalized L2 remainder for all q>=1. Its claimed rate 3/500 remains below 1/100 even if verified; arbitrary-weight strict-rate approximation, original H/support/realization and actual-Xi signs remain open.
REASON: Essential coverage is sufficient for the exact nominated audit; no source blocker remains. SPECIALIZE permits a later REPRODUCTION audit of the application and its implementation, not a new quadrature mechanism or approval of L681's truth. This completes only the separate literature gate; the supervisor approves execution next turn.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED nomination requires separate coverage approval of the newly written L681 audit. Reuse covers the unchanged quadrature search; the only additional source extraction is the precise finite residue-theorem input and its hypothesis boundary.
SCOPE: Exactly TARGET for n=12q+3, q>=1, x=-5/4, R=11/8, L673's exact nodes, the full L666 W and normalized continuous angular L2; verify or identify a defect in L681's existing claimed rate 3/500, without optimizing gauges, nodes, weights or rates.

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

## Completed source gate — 2 November 2026, step 67

### Standard import and application boundary

Read the primary reference text [NIST DLMF Section 1.10(iv),
equation (1.10.8)](https://dlmf.nist.gov/1.10#E8) and its full
hypothesis and orientation clauses, together with the Laurent residue
definition in Section 1.10(iii). The theorem concerns a simple closed
contour, an integrand analytic inside and continuous on the contour
and interior except for finitely many interior isolated singularities,
and positive traversal. Its normalized contour integral equals the
sum of interior residues. The source notes refer to E. T. Copson,
*An Introduction to the Theory of Functions of a Complex Variable*
(1935), pp.117--120; that book passage was not read. The online
statement, not an inaccessible book or search snippet, is the inspected
named-theorem input. The TeX endpoint failed to render, but the complete
HTML formula and conditions were available; no essential access gap
remains. No proof of the standard theorem is needed here.

For L681 the proposed integrand is its K_n(z) W_(x+z)(u), with u fixed
on the unit circle and a finite rectangular contour. A later audit must
check the complete singularity list, contour admissibility, orientation,
absence of boundary poles and regularity of W. It must check the claimed
simple-pole residues and unit anchor directly. The named theorem supplies
neither the sign of these residues nor any quantitative remainder. No
infinite partial-fraction expansion, spectral completeness theorem or
infinite sampling limit is an invoked premise. This is a statement of
audit obligations, not a verification of their satisfaction.

### Reuse, duplicate screen and exact remaining scope

Reused step 65's primary comparisons with Bayer--Teichmann Theorem 1
and Corollaries 1--2, Glaubitz Theorem 3.5 and Corollary 3.6,
Cala Rodriguez et al. Theorems 2.2--2.3, and Trefethen--Weideman
Theorem 5.1 and the qualified Theorem 9.1 reading. Their inspected
hypotheses, proof-reading limits and citations remain in
`drafts/literature/2026-11-02-discrete-parameter-positive-quadrature.md`.
The move from construction to auditing that construction introduces no
use of those unused general quadrature theorems or unread leads.
Repeated retrieval of those sources would not resolve the present gap.

Read L681's full statement and proof to delimit the audit, not to certify
it. Local comparison includes L672's audited series/derivative framework,
L673's exact nodes and its qualified fixed-gauge stop, L680's parameter
attenuation scope, and step 66's history. The narrow records
`ATTEMPTS/2026-11-02-fixed-gauge-contour-crossing-stop.md` and
`ATTEMPTS/2026-11-02-positive-cone-polar-finite-screen-inconclusive.md`
retain their restricted meanings: neither a stopped sufficient contour
estimate nor an uncertified finite polar screen excludes L681's proposed
partial formula. Conversely, its auxiliary weights cannot be substituted
for the original unit residues when interpreting H. L680's continuum-sign
contradiction is not a premise of this discrete-node audit.

The remaining work is the exact specialization and its full evidence:
L666 (6), L672 Sections 3--4, L673's exact nodes and L680 Sections 3/6
point attenuation; then L681 (1)--(11), the preserved-helper boundary,
all certificate rows and rational tails, both angular charts, interpolation
cells including s=0, the n-dependent top and the q=1 onset. The certificate
and its generator were not verified or replayed in this source turn.
Their recorded maxima and pass counts remain claims to check. No sampled
preview establishes continuous coverage. Full matching Mathlib coverage
remains unchecked; elementary supporting coverage is not a substitute
for the family-specific audit.

### Relevance and discriminator

The main gap is actual-Xi all-degree mixed positivity. The intermediate
target is verification or precise repair of this bounded positive-node
approximation, potentially useful for transferring discrete-node signs to
the paid parameter point -R. Success means a complete independent check
of the stated full residual bound for every q>=1; failure means locating
a load-bearing error and preserving the actual surviving estimate. Do not
repeat an unsuccessful audit without a corrected argument or new evidence.
No outcome here decides the strict exponent above 1/100: the claimed
3/500 is only partial, and original H, support and Xi realization remain
independent gaps. The exact TARGET stays unchanged. Source coverage is
ready for one conceptual audit, classified REPRODUCTION if undertaken;
this literature completion itself is NOVELTY_UNCHECKED and establishes
no new mathematical result or originality.
