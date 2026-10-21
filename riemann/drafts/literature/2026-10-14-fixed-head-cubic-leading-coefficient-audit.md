# Fixed-head cubic leading-coefficient audit: completed source coverage

TARGET: Audit L408's positive fixed-N cubic coefficient, including combined poles, analytic weights, sharp endpoints and the complete signed assembly at scale H(log H)^2.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step-112 rational-additive/shifted-Estermann search and step-111 carrier audit; read full L408 and targeted L407/L391 ranges, recent step-112/113 history and repeated-source stop evidence; narrowly retrieved the cited primary formulas for this new proof-audit scope, with no broad discovery sweep or coefficient verification.
SOURCE_EVIDENCE: Fazzari arXiv:2306.15553v1 (27 June 2023), (1.3), Lemma 3.2 and (3.5) p. 10, https://arxiv.org/html/2306.15553v1#S3; DLMF https://dlmf.nist.gov/25.11#i / https://dlmf.nist.gov/25.11.E5 / https://dlmf.nist.gov/2.5.E2 / https://dlmf.nist.gov/5.11.E2 and 5.11(ii); audited L407 (4), (8), (9) and L391 ordinary-jet/polygamma tools.
COMPARISON: Exact finite progression decomposition, sole Hurwitz pole, positive-half-plane continuation formula, smooth Mellin inversion and sector-qualified digamma expansion cover the standard tools; combined poles, derivative disks, absolute boundary estimates, uniform weights and signed normalization are local audit obligations, not conclusions imported from a cubic-moment theorem.
GAP: L408 correctness and its complete certificate evidence remain unaudited; no essential source is inaccessible for this fixed-N audit. Full-response passage, growing N and clipping remain outside coverage.
REASON: Approve a separate bounded critical audit using the inspected primary tools and ready carrier coverage; this literature turn proves no new lemma and does not validate beta_N or the sharp asymptotic.
LITERATURE_REASON: The newly written L408 combines coalesced differentiated poles with uniform analytic weights and sequential endpoint limits; its exact application needs a separate coverage comparison, particularly the principal-log sector and complex digamma remainder, before critical audit.
COVERED_TARGET: Audit L408's positive fixed-N cubic coefficient, including combined poles, analytic weights, sharp endpoints and the complete signed assembly at scale H(log H)^2.
SCOPE: Fixed positive integer N independent of real H; L408 (1)-(12) and its finite certificate, with audited L407/L391 reused. No full-response limit, clipping, regulator choice, total pencil margin or RH claim.

## Completed comparison — step 114

The saved action was: Assess primary-source coverage for a critical audit of L408's positive fixed-N cubic coefficient, including combined poles, analytic weights and sharp endpoints.
This literature-only step completes that comparison and prepares the
exact TARGET above for a separately invoked mathematical audit. ADVANCE
means new completed applicability coverage for that audit, not a new
mathematical result or a correctness verdict on L408.

The main gap remains global actual-theta mixed positivity. Essential
local inputs are L408, audited L407 and L391. The intermediate target
is an independent correctness audit of the claimed fixed-N positive
coefficient; its plausible use is a reliable finite-head benchmark for
later full-response work. A successful local audit may leave all those
independent downstream gaps open.

### Primary hypotheses and source limits

Reuse the [step-112 assessment](2026-10-14-fixed-head-cubic-leading-coefficient.md)
for discovery and the [step-111 assessment](2026-10-14-fixed-head-cubic-critical-audit.md)
for the carrier reduction. No matching published evaluation of this
complete local statistic was established by those searches; that is not
a novelty claim. This step read L408 completely, L407's definitions and
coefficient bounds, L391's ordinary-jet formulas and L407's corresponding
audited coefficient passage. The new certificate was not executed or
read as mathematical verification in this literature turn.

[Fazzari v1](https://arxiv.org/html/2306.15553v1#S3), (1.3),
Lemma 3.2 and (3.5), p. 10, were retrieved narrowly. Three shifts are
independent complex parameters, and (3.5) sums every class from 1 to K.
For the proposed audit the modulus is u and numerator -v with (u,v)=1;
the zero class and nonunits must remain. Theorem 1.1 is smooth and its
coincident polar terms require combination. The inconsistent expanded
polar-factor display recorded in step 112 remains excluded; only the
exact progression identity is needed. No full Voronoi reproof is justified.

[DLMF 25.11(i)](https://dlmf.nist.gov/25.11#i) supplies the
series on Re s>1 and the unique simple pole with residue one.
[25.11.5](https://dlmf.nist.gov/25.11.E5), sourced to Apostol,
*Introduction to Analytic Number Theory* (1976), (25), p. 269,
requires a>0, Re s>0, s!=1 and integer cutoff >=0. The proposed
parameters a=class/u and cutoff zero meet this scope. It supplies an
integral representation, not an already differentiated twist asymptotic.
The growth and Cauchy-disk estimates remain audit checks.

[DLMF 2.5.2](https://dlmf.nist.gov/2.5.E2), with the introduction
and admissible inversion line in 2.5(i), is sufficient for the compact
smooth test functions used here. It does not approve using an indicator
in the source's smooth theorem. Absolute contour decay and boundary
transfer must be checked in L408; no sharp Perron input is needed.

[DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2) uses the principal
logarithm and the closed sector |arg z|<=pi-eta, eta>0. The complex
remainder bound in [5.11(ii)](https://dlmf.nist.gov/5.11#ii) was also
read. Both shifted gamma arguments fall within the proposed sector scope;
even a negative real component of one argument does not exclude it.
The sum of logarithms and derivative bounds must still be checked locally;
an O-term cannot simply be differentiated. L391 supplies the previously
audited polygamma bounds for that purpose.

DLMF citations refer to the online formulas retrieved on 2026-10-14;
the extraction did not expose a release number, so none is newly
certified here. The earlier assessment's release record is retained.
The precise numbered formulas above are the inspected evidence.

### Separate audit obligations and decision test

Compare the highest pole of all three ordinary derivatives,
the complete residue-class orthogonality (including nonunits), polynomial
growth on the shifted Mellin strip, absolute horizontal/vertical estimates,
unsigned endpoint majorants and the order of the two limits, uniform
analytic-weight coefficients with all Omega' terms, zero-carrier
resonances, rational-twist normalizations and all eight signed terms.
Check Cauchy bounds on the slightly enlarged fixed strip containing all
derivative disks, not just their centers. The fixed endpoint width must
precede the height limit; complex phases and weights need an absolute
unsigned majorant, including integer endpoints. Check both the source applicability and local algebra, without importing
the inconsistent expanded Fazzari polar factor or the excluded cubic
theorem. A fresh search is justified only by a specific uncovered
hypothesis or a discovered mismatch.

Coverage is adequate for one separate proof_audit under SPECIALIZE.
The sources do not state the claimed 17/20160 assembly or beta_N;
those remain verification targets. The exact local specialization is
needed to preserve logarithmic jets, rational twists and sharp weights;
no matching cubic theorem is imported or reproved.

Continue only if every load-bearing identity and the complete relevant
certificate values agree, and all errors total o_N(H(log H)^2).
Failure of a pole order, disk bound, branch, endpoint or signed factor
stops use of the claimed coefficient until the exact defect is recorded
and repaired. An essential input outside this fixed scope requires
REVIEW_REQUIRED before dependent work. No downstream premise may be
silently added. Mathlib full matching coverage remains unchecked.

The recent records contain the calculation and the L407 audit, not a
completed L408 audit. L394/L399/L400's different-weight stops and the
repeated-source-approval failure in ATTEMPTS remain intact: this is a
new concrete proof-audit scope, not permission for recurring literature
approval of unchanged tools. The next turn defaults to mathematics.

Unresolved assumptions outside the local result: its independent audit,
uniform full-response passage at H(log H)^2, clipping, regulator choice,
total L367 margin/remainder, actual common-zero upper counts and global
mixed positivity. No RH candidate.
