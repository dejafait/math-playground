# Proposed hierarchical finite-cell square contraction

TARGET: Assess a hierarchical separable finite-cell K_0 approximation for the frozen C998a square matrix, with coefficient contraction before quadrature, entry error at most 1e-10, and at most 20000000 scalar operations.
CHECKED: 2026-11-12
DECISION: EXPLORE
SEARCH_EVIDENCE: Review673 searched hierarchical asymptotically smooth Galerkin kernels, Carleman/logarithmic divided-difference low rank and hierarchical singular quadrature; inspected Borm--Grasedyck--Hackbusch2003 and Meszmer2010 as detailed below. Compared local657/660/662 stops, C998a, C998e(6)-(8), and complete C998g. No ready local hierarchical assessment or turnkey finite certificate was identified; no novelty inference.
SOURCE_EVIDENCE: Borm--Grasedyck--Hackbusch, EABE27(2003),405-422, Sections1.2,2.1-2.3,3.1-3.2,4/4.1,5.1-5.2, equations(2),(5),(7)-(8),(14), https://people.math.ethz.ch/~hiptmair/Seminars/HMAT/ST04/Papers/BGH03.pdf ; Meszmer, MiS preprint5/2010 revised July2010, Definitions2.1-2.6, Sections3.4,5-7.1 through equations(37)-(38), https://webdoc.sub.gwdg.de/ebook/serien/e/MPI_Math_Nat/preprint2010_5.pdf . Precise inspected scope and unread leads follow; predecessor coverage670/655 is reused only for the independent next audit.
COMPARISON: Separated Galerkin factors and contraction-before-evaluation are standard. Their inspected guarantees do not directly cover this K_0's axis blocks, global cosine support or finite-end correction, and supply no certified scalar-work constant for the six frozen densities. Near-field entries and factor construction are not free. The source comparison changes the route: park the full hierarchy proposal, rather than treating an asymptotic rate as affordable ranks.
GAP: No inspected result currently permits one justified full-block hierarchy/rank prescription at entry error<=1e-10 and work<=20000000. Missing items are integrated axis/corner error, finite-end treatment, localized coefficient moments and a complete finite scalar ledger. This EXPLORE assessment records bounded discovery and does not approve a dependent hierarchy calculation; independent audit continuation673 has separate ready coverage.
REASON: New, concrete source-scope restrictions make a black-box hierarchical import inadequate. Stop this source-to-prescription route without declaring hierarchical methods impossible; preserve672. Review an independently testable existing transform/error/work claim next, with no new quadrature prescription or renewed source-access loop.

The original nomination sought finite-cell, integrable-kernel error
control for a hierarchical sum of separated terms and an explicit
coefficient contraction, not just asymptotic convergence, sampled ranks
or function-evaluation counts. State all hypotheses at s=0,u=0 and
s=u. The full K_0 includes its finite upper-end correction. The square
uses the six exact finite cosine densities, both parities, all column
products and1/4. No half-line replacement or retuned trial is proposed.

Original discriminator (completed below): identify an inspected result permitting ONE explicit
hierarchy/rank prescription with a provable integrated entry-error
bound and a full scalar-operation ledger under the TARGET; otherwise
record the precise missing hypothesis or obstruction and nominate a
materially different independently testable target. No general rate
implies affordable ranks. Do not treat432945540 as a lower bound for
all square methods. Do not run a parameter sweep or another direct
point service under this nomination.

Essential inputs: C998a/audit655 and complete654/655, C999q exact Z,
frozen652 SHA2562b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6;
C998e(6)-(8) scoped audit672; C998g's new transformation, ellipse
ledger and cost proof remain separately unaudited. Use that last result
as proposed evidence to check, not an already critically reviewed
numerical certificate. C998f/audit669's<=10000000 diagonal reserve is
separate. C999/audit650 and C999y/audit642 are downstream interpretation.
C744v/w/z,C999k,C999z/audit646 and original analytic/arithmetic/source-to-Xi/
whole-core/c_* contracts remain unreplayed. No cross-notebook input.

Main gap is L030-L032/C032a actual-Xi positivity and signed S3 coupling.
A paid square contribution could help a later correlated residual-Gram
ledger, but A-square, both mixed terms, moments/projection, residual
size, inverse debt, full100000000 work, signs, higher/mixed endpoints,
C744q/H2, non-neutral coverage and global assembly remain open. Full
matching Mathlib coverage is unchecked. No specified new signed S3
mechanism is available for a justified creative attempt; this possible
numerical specialization must not be labeled creative.

## Completed source comparison673

This is one LITERATURE-only step. The original discriminator above was
not met. No hierarchy, rank, new estimate, lemma or mathematical script
was derived. EXPLORE records the search decision, not readiness of a new
full-block algorithm. The numerical target and all prior stops survive.

Queries included `hierarchical matrices asymptotically smooth kernel
logarithmic singularity Galerkin error interpolation theorem Hackbusch
Borm pdf`, `Carleman kernel log x log y divided difference hierarchical
low rank approximation 1 x plus y exponential sums error theorem`,
`Hierarchical Quadrature Borm pdf`, and exact-title searches for the
two Borm papers. Search snippets and asymptotic abstracts were leads.

**Inspected interpolation and contraction.** Borm--Grasedyck--Hackbusch,
*Introduction to hierarchical matrices with applications*, Engineering
Analysis with Boundary Elements27(2003),405-422,
DOI10.1016/S0955-7997(02)00152-2,
[published PDF](https://people.math.ethz.ch/~hiptmair/Seminars/HMAT/ST04/Papers/BGH03.pdf).
Read pp406-409, Sections1.2,2,3.1: equation(2) assumes factorial
mixed-derivative control away from x=y, with positive constants C_as1,
C_as2. Equation(5) compares cluster-support diameter with separation.
Equations(7)-(8) interpolate one kernel variable and integrate against
basis functions to obtain separated Galerkin factors. Their exponential
estimate needs sufficiently small admissibility parameter and finite
block bounds. Read Section3.2's two-stage product, Section4/4.1's
unstructured non-admissible leaves, and Section5.1/5.2's forward,
coupling and backward transformations. These explicitly support moving
contraction before evaluation. Rank, tree sparsity and already constructed
factors enter the complexity estimates; they are not an absolute
operation certificate for factor construction or singular integration.

**Inspected singular reductions.** Meszmer, *Hierarchical quadrature for
multidimensional singular integrals*, MiS preprint5/2010, revised July2010,
[primary preprint archive](https://webdoc.sub.gwdg.de/ebook/serien/e/MPI_Math_Nat/preprint2010_5.pdf).
Read printed pp2-3, Definitions2.1-2.6: translation invariance,
homogeneity, factorial asymptotic smoothness and regular-grid domain
pairs are explicit assumptions. Read Section3.4's equivalence-class
system(20), and Section5, printed pp18-22, including the full polynomial
example: translated monomials introduce lower-degree cases via the
binomial formula. This is finite polynomial closure, not a finite-cosine
closure theorem. Section6 excludes specified hypersingular exponents.
Section7.1, printed pp22-23, equations(35)-(38), obtains exponential
regular-panel quadrature from derivative bounds and strictly positive
domain separation. Those cases do not eliminate the need to justify
the singular reduction's assumptions first. No generic singular-block
rank or scalar-cost theorem for the present K_0 was found here.

**Comparison to the exact notebook object.** C998e(6) and C998g Section1
already record divergent axes at tau=0, despite a removable positive
diagonal. Thus a separated positive rectangle touching an input axis
does not acquire a bounded kernel simply by staying away from s=u.
BGH's off-diagonal picture is not an axis-block certificate. The cosine
modes in C998a have full half-cell support, so clustering their indices
does not supply separated supports under equation(5). Spatial panel
localization would need its own moments and cost. Non-admissible blocks
still require integration; storing them densely is not a proof of their
entries. Meszmer's translation/homogeneity assumptions are not established
for the FINITE-end K_0. Dropping its a-dependent correction or replacing
the six densities by a polynomial would change the object without a
paid error. Neither source provides that payment. These are limitations
on the proposed imports, not impossibility claims about other hierarchies.

The known sources cover much of the proposed organization; independent
local bounds and certified factor construction would still be necessary.
Consequently neither an affordable rank nor an error floor is claimed.
The unchanged1e-10 and20000000 thresholds are unachieved by this review.
The432945540 stop remains specific to C998g's direct prescription.

**Access and unread leads.** Borm--Hackbusch, *Hierarchical quadrature
for singular integrals*, Computing74(2005),75-100,
DOI10.1007/s00607-004-0076-0, was located at the
[MiS50/2003 record](https://www.mis.mpg.de/publications/preprint-repository/article/2003/issue-50).
Only its abstract/record was accessible: the primary PDF returned an
unsupported-content-type error, the publisher PDF was inaccessible,
and local curl had no DNS access. It is an unread lead, not an input.
The BGH published PDF above did load through an academic mirror;
Meszmer is a distinct inspected primary source, not a silent substitute
for BH's unseen proof. No quoted BH theorem or source-block recurrence
is imported. This review parks the dependent hierarchy, rather than
repeating access attempts. BGH's references to dedicated approximation
papers and adaptive ranks are also unread leads, not certificates.

## Routing after the comparison

An independently testable target is the unaudited C998g transform and
ideal-node ledger, whose hypotheses and complete proof now exist. Its
source gate can reuse670 and655; it needs a conceptual audit, not new
hierarchy mathematics. Ready coverage is recorded separately in
[audit continuation673](2026-11-12-duffy-square-ledger-audit-review-673.md).
Newly written coverage receives separate supervisor approval next turn.
No signed S3 mechanism with a new discriminating central test emerged
from this review, so creative routing has no justified nomination here.
The audit must not reopen direct672 execution or tune degrees.
