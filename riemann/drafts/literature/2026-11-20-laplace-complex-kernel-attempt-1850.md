# Complex rational bulk kernel — bounded test nomination1850

TARGET: Test C034d(29)'s sign Re K(z,w)<0 for Re z,Re w>=13 and |Im z|,|Im w|<=1/2, using an exact whole-domain certificate or a certified violating pair.
CHECKED: 2026-11-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1850 completed assessment1849; twelve exact-formula, complex-sign, Gaussian-contour and certificate queries and narrow duplicate/failure comparison are recorded in drafts/literature/2026-11-20-laplace-complex-kernel-source-notes-1850.md. No matching sign theorem was found; novelty remains unclaimed.
SOURCE_EVIDENCE: Hamadneh et al., arXiv:1906.03472v1, Section2(1)-(6), pp2-3 and Section4(17)-(18), p8, https://arxiv.org/pdf/1906.03472v1 ; Haslinger Theorem2.5/Corollary2.6 with proof cases, pp45-48, https://www.mat.univie.ac.at/~has/scriptneu.pdf ; DLMF7.7.2, https://dlmf.nist.gov/7.7#E2 ; unchanged local tools reuse source-notes1848/1846/1842.
COMPARISON: Exact polynomial/rational certificate tools are known; K's complex-domain inequality is not imported. C034d's real ordering proof has no complex ordering premise. The contour and scalar Gaussian formulas supply neither this sign nor automatic endpoint cancellation.
GAP: Certify this precise rational sign on the full unbounded product strip, including independent imaginary signs and all finite edges, or certify a violating pair; no such result or algebraic reduction is asserted by this nomination.
REASON: A true complex sign could support Gaussian contour transfer on retained divisor cores while avoiding assumed spatial profile positivity. This is one separately testable local development target. The newly written ready assessment requires separate approval next turn.
SCOPE: Exactly C034d(29)'s same rational K and the displayed domain, with ordinary complex derivatives of its Q_j. No changed cutoff identity, finite-zero data, assumed nonnegative profile, contour transfer, source-wide validation or full curvature claim.

The main gap is L030-L032/C032a actual-Xi all-degree positivity.
The downstream use is only a possible conjugate-paired Gaussian
contour transfer. A sign alone neither pays C034d's exact R nor
proves C034c(20), the final ECT prefix or actual-Xi realization.

Keep both real coordinates unbounded above and both imaginary
coordinates independent in [-1/2,1/2]. Prove denominator nonvanishing
where needed. No restriction to w=conjugate(z), a diagonal, a finite
sample or real arguments decides this claim. Known exact certificate
methods may be imported by the cited equations; justify any actual
polynomial/rational encoding and all domain changes locally. A finite
box certificate requires rigorous completion outside the box.
Compactification, if used, must handle its limiting faces; the target
asks strict negativity at finite points, not a uniform constant.

Continue with a complete rigorous sign certificate or a certified
pair in the stated domain with Re K>=0. Distinguish an exact zero
from a positive violation. Negative Bernstein coefficients, enclosure
failure and sampling alone are inconclusive. If one bounded attempt
cannot decide the claim, save its actual partial reasoning and the
precise certificate obstruction; do not label failure as a disproof
or repeat an exhausted method without materially new input.

Any later contour work remains separately scoped: retain endpoint
connectors, tails, origin subtractions, possible pole contributions
and every justified divisor exchange. No such identity is licensed
as already proved. Preserve stops1847/1843/1839 and their cited
earlier evidence. This sign test does not reopen closure by transfer
alone; the signed threshold <=S4^3/5 on [1,2] is still unpaid.

Essential inputs and unresolved assumptions: C034d/c/b and C032n;
C032m and C033w through C033l/C032q for the qualified probability
context. Retain actual divisor/conjugation/multiplicity, ordinate0
exclusion, strict strip/gamma>14, count/through100/retained real zero,
reciprocal-square tail, heat positivity/separate fixed-j errors, both
fixed-v1 inputs, zero drift/killing and Gaussian half-variance. These
inherited qualifications matter to downstream use; this standalone
rational sign test must not assume RH. Source-wide/finite-zero
validity, global Sobolev membership and full matching Mathlib coverage
remain unverified. Conditioning, entries/m, exact weights, TV<=2,
full observations, signed height, cancellation and Xi realization
remain independent. No source supports a new central creative
mechanism here; this is established-route development.
