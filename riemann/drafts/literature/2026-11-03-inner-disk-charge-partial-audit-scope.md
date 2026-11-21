# Source scope for the partial inner-disk charge audit

TARGET: Critically audit L704's eventual Z_n^(1/2)(e)>=n/4000 bound, including the full spatial limit, complete divisor accounting and Poisson comparison.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 149 reuses step 147's exact inner-disk search and duplicate/obstruction comparison; new queries on Poisson--Jensen, disk Blaschke factors and boundary logarithms locate Ash--Novinger Theorem 4.8.3. Read L704 in full to delimit the audit; no matching theorem for its profile-specific lower charge was found or claimed.
SOURCE_EVIDENCE: New primary reading: Ash--Novinger, Complex Variables, hyperlinked web text, Theorems 4.8.1/4.8.3, Corollaries 4.7.4/4.8.2 and Lemma 4.8.4 with proofs, printed pp.27,32--36 (PDF pp.88,93--97), https://people.math.sc.edu/girardi/m7034/book/AshComplexVariablesWithHyperlinks.pdf. Reinspected Tao Notes 1 Theorem 2/proof, Mathews--Howell 8.1.5/8.1.7 statements and residue-theorem proof, and Miller Section 6 (6.1)--(6.2); reuse prior complete contour, Fourier and root-integrability reading records below.
COMPARISON: The primary Poisson--Jensen theorem covers the analytic disk application including boundary zeros, conditional on L704's claimed pole clearance and nonzero evaluation. Known contour/Fourier/root-integrability tools cover the remaining interfaces; none supplies the full-spatial limit, complete weighted lower charge or required o(n) deficit. Their local applications require a separate conceptual audit.
GAP: Verify L704's full moving contour, same-profile off-support Fourier use, uniform spatial summation, whole-boundary upper estimate, complete cancelled divisors and center/boundary cases, automorphism weight and inequality direction. The source comparison does not discharge those proof obligations or verify the constant certificate.
REASON: Essential source coverage is adequate for this exact bounded audit; the newly inspected boundary-zero theorem closes the source-scope question without deriving or approving L704. The partial result is preserved and remains unaudited; no lemma or mathematical script was changed.
LITERATURE_REASON: The saved audit target was REVIEW_REQUIRED; its changed positive-radius and disk-automorphism applications required this separate source comparison, especially the boundary-zero logarithmic case.
SCOPE: Only TARGET, for one actual L703 profile fixed before n=12q+3, retaining L657's complete K,Q and L666's anchor, unit masses, inverse angle, j=0, both endpoints and every M=n/3 moment. Audit or repair an error within this claimed bound; no constant optimization, stronger compensation claim or new profile selection.

## Exact scope and continuation conditions

The proposed audit concerns [L704](../../lemmas/L704-inner-disk-complete-charge-partial-payment.md)
for one actual fixed L703 profile, with all choices preceding
n=12q+3. Keep L666's unit masses, anchor, j=0 factor, inverse angle,
endpoints -2q and 2q-1, and all M=n/3 spatial moments. Use L657's
complete K,Q, including cancelled factors, multiplicities, finite
center-zero exceptions and radius-1/2 boundary factors.

The claimed bound is eventual and its onset may depend on the fixed
profile. The proof obtains a uniform full-spatial limit at s=1/10000,
uses an upper bound (7/4)n+O(log n) on the entire radius-1/2 boundary,
and obtains liminf Z_n/n>=2267057/7998400000>1/4000. The separate
pole charge is P_n/n->121/160. No o(n) deficit, complete compensation,
sign, H/support or Xi-realization conclusion is asserted.

Reuse the unchanged [inner-disk source comparison](2026-11-03-gevrey-inner-disk-complete-charge-scope.md)
and the primary source interfaces recorded in L704. Compare the
changed positive-radius residue application and Jensen after a disk
automorphism against their exact source hypotheses. Check that the
translated-comb input is only the standard distributional identity;
the summable-difference and expanding-endpoint limits must be justified
locally. Do not import L690's unit-circle conclusion at radius s.

The later audit must inspect the entire relevant proof and the exact
certificate at `scripts/one-sided-hankel/inner-disk-charge-148.json`.
That certificate checks 16 rational inequalities only. It neither
approximates the actual infinite Picard profile nor verifies an
analytic zero census. Existing L700/L701, L702, L695 and C703a stops
remain within their original scopes.

Accept only if all full-boundary and full-spatial applications, limit
orders, exceptional sets and signs are valid. Otherwise identify and
repair a specific error or withdraw only the unsupported conclusion,
preserving its derivation. Improving the small constant is not this
audit's target. Full matching Mathlib coverage is unchecked; L657's
supporting Mahler module remains a supporting reference only.

The preceding nomination is retained as its original scope. Step 149
completes source approval for that same audit; it does not perform the
mathematical audit or certify L704.

## Completed source comparison — 3 November 2026, step 149

### Local scope, duplicates and recorded failures

Read the full canonical L704, L657's hypotheses/conclusions, L666's
family and rational continuation through Section 2, and L703's statement,
Section 5 and the closing actual-data check in its separate Section 6
audit. L703's displayed identity is on the entire interval (-3/8,3/8),
not only the positive plateau where its measure has a gap. The later
auditor must check L704's use of the complementary neighborhood of zero
with the same actual profile and Fourier convention. No new identity
has been derived in this source review.

Reuse the exact-target search and primary-theorem comparison in
[step 147](2026-11-03-gevrey-inner-disk-complete-charge-scope.md),
the [step-93 root-integrability record](2026-11-03-spatially-averaged-angular-zero-charge.md),
the [step-118 Schwartz-Poisson record](2026-11-03-centered-gap-scalar-audit-scope.md),
the [step-89 contour record](2026-11-03-unit-residue-robin-contour-audit.md)
and the [step-143 same-profile scope](2026-11-03-centered-gap-gevrey-picard-audit-scope.md).
Their unchanged general tools need no fresh derivation.

Read the three short ATTEMPTS records for the common-sign residue,
middle-bulk microscopic pairing and Gevrey paired-tail absolute-variation
stops. L700/L701 concern particular scalar sufficient mechanisms;
L695/C703a concern absolute-cost certificates. These do not contradict
or establish the aggregate full-spatial partial charge. L702's retained
interior stops an endpoint-only extension. L690's common-shift unit-circle
conclusion and L691's two constant halves do not verify L704's varying
profile at positive radius. These comparisons are not new premises or
global bans. No stopped route is reopened by this audit.

### New primary Poisson--Jensen input

R. B. Ash and W. P. Novinger, *Complex Variables*, hyperlinked web
text, [Theorem 4.8.3, printed pp.33--34](https://people.math.sc.edu/girardi/m7034/book/AshComplexVariablesWithHyperlinks.pdf#page=94):
if f is analytic on a neighborhood of the closed disk of radius R0,
not identically zero, and f(z)!=0 at an interior point, then

    log|f(z)| = sum_j k_j log|R0*(z-a_j)/(R0^2-conj(a_j)*z)|
                 + mean_t P_(z/R0)(t)*log|f(R0*exp(i*t))|.

Here a_j are all interior zeros, with multiplicities k_j. Boundary zeros
are allowed; the integral exists as an improper Riemann integral.
Read Theorem 4.8.1 and its Blaschke proof (p.32), Corollary 4.8.2
(p.33), and the entire boundary-factor proof of 4.8.3 and Lemma 4.8.4
(pp.34--36): finite boundary factors, logarithmic endpoint integrability,
exterior-root approximation and split-interval convergence.
Corollary 4.7.4 (p.27) gives kernel mass one.
The p.35 proof uses P_z(-t)=P_z(t); do not import that assertion for
general complex z. L704 evaluates at real s, within that proof's
even-kernel case. The inspected file has no explicit revision date;
these are printed page and theorem numbers, not a claim about another
edition.

The intended specialization is f(u)=F_n(u,zeta), R0=r=1/2 and
z=s=1/10000. Source hypotheses require actual analytic pole removal
near the whole closed disk and nonzero evaluation for the relevant
spatial slices. Both remain audit obligations. The source directly
supplies the standard Poisson--Jensen interface, including its
nonpositive interior-zero terms. It does not supply L704's upper
boundary bound or the rearrangement involving kappa. In particular,
positivity of the Poisson kernel does not supply a lower bound for
an arbitrary signed boundary logarithm. Check the displayed
automorphism, its boundary measure, and the use of the upper bound
in L704 (24)--(28), rather than assuming their correctness from the
source name. No reproof of the general theorem is needed.

### Reused primary interfaces and application boundaries

T. Tao, *246B, Notes 1*, 23 December 2020,
[Theorem 2 and proof (3)--(5)](https://terrytao.wordpress.com/2020/12/23/246b-notes-1-zeroes-poles-and-factorisation-of-meromorphic-functions/)
were reinspected. The function must be meromorphic near the closed
disk with removable singularities removed and center neither zero nor
pole. Divisors are counted with multiplicity; boundary weights are zero.
The proof removes finite divisors by Blaschke factors, then uses a
holomorphic logarithm; its initial radius perturbation is not by itself
a quantitative uniform limiting estimate. The boundary-root coverage
above and the step-93 polynomial formula avoid relying on an unstated
dominated limit for the present logarithms.

Reuse Brunault--Zudilin, *Many Variations of Mahler Measures*,
[Propositions 1.4--1.5, pp.6--7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf),
and Issa--Lalin, [arXiv:1203.5379v1](https://arxiv.org/pdf/1203.5379v1),
Remark 3.8 and Theorem 4.1/proof p.7, s=1, exactly as inspected in
steps 93/147. Nonzero polynomial logarithms are absolutely integrable;
degree drops and circle roots are allowed. No n-uniform small-value
estimate is imported. The later audit must apply this to the actual
rescaled bivariate K and retain every cancelled Q factor, not merely
the reduced rational numerator. A finite exceptional center set does
not permit discarding other spatial sets or logarithmic costs.

Mathews--Howell, *Complex Analysis*, online
[Theorems 8.1.5/8.1.7](https://complexanalysis.org/web/sec_residue-thm.html):
reinspected both statements and the residue-theorem proof; reuse their
full proof record and [6.2.18--6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html)
from steps 89/123. The contour is simple, closed and positively oriented,
with no boundary singularities, only finitely many interior singularities,
and the requisite analytic domain. The contour bound needs a continuous
integrand on a finite piecewise smooth path. These theorems apply to
each finite n; they do not provide uniform moving-boundary decay.
For L704 Section 2 the pole census, all four edges, endpoint placement,
fixed v_0, uniform product Riemann error and spatial geometric bound
must therefore be audited locally. No strict Rouche comparison is
required or imported for that residue calculation.

S. D. Miller, *Some notes on distributions*, 15 January 2006,
[Theorems 4.1--4.2, Section 6 (6.1)--(6.2), pp.7--9](https://sites.math.rutgers.edu/~sdmiller/musagei/distributions.pdf):
reuse the full Schwartz-Poisson/duality proof reading in step 118;
reinspected Section 6's test restriction and comb formula. These cover
the standard translated comb, not pointwise evaluation of a general
distribution or an unregularized infinite exponential sum. L704's
summable-difference series, compact-frequency test pairing, convention
conversion and uniform finite-endpoint/spatial limits are local
application obligations. L703 supplies the exact prescribed data;
neither Miller nor a gap assigned to a truncated profile replaces them.

### Search record and bounded audit decision

New queries were `Poisson Jensen formula disk Blaschke zero subharmonic
boundary logarithm lecture notes` and `Robert Ash complex variables
4.8.3 Poisson Jensen formula second version author`. The primary
Ash--Novinger text was read as specified above. Search snippets,
secondary proof sites and other returned potential-theory papers were
not imported. The exact partial-charge comparison otherwise reuses
step 147; no stronger matching lower-charge theorem is asserted.
The web text was accessible. An optional shell PDF download failed
at DNS resolution and is not an essential blocker; no claim rests on
that failed download or on an uninspected passage.

Coverage is SPECIALIZE because the standard tools are available while
their family-specific applications, quantifiers and signs need audit.
The exact bounded test is the saved TARGET: inspect the entire L704
proof, relevant canonical inputs, and every relevant value/check in
`scripts/one-sided-hankel/inner-disk-charge-148.json`, using the scoped
JSON inspector. That certificate remains arithmetic evidence only;
this literature turn neither ran it nor verified its entries. Accept
the eventual n/4000 claim only if the analytic applications, complete
divisors, exceptions and inequality direction all pass. Otherwise
identify and repair a specific error or qualify the unsupported claim,
preserving its derivation. No stronger compensation target is approved.

No new Mathlib lookup was needed. Full matching coverage remains
unchecked; L657/L704's recorded Mahler-measure module is supporting
one-variable coverage only. This source approval establishes no new
lower charge and no progress beyond the cited general theorems.
