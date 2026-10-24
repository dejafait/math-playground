# Complete transverse-H remainder — source comparison

TARGET: Determine whether the complete transverse-H remainder relative to a^(-3)[K_(i,f)+K_(i,V)+K_(i,sc)+K_(i,en)] is O(N^(5/2)log(eN)^2) for both actual probes.
CHECKED: 2026-10-23
DECISION: EXPLORE
SEARCH_EVIDENCE: Searched notebook literature, selected compression/placement drafts and histories for L110--L123, eta_N, q_j(N), compression rates and duplicates; inspected L110/L116 in full and the exact rate-relevant ranges listed below. Four bounded external queries are recorded below; no inspected theorem supplies the complete requested remainder.
SOURCE_EVIDENCE: Reused the 2026-10-10 other/other, 2026-10-17 complete-coefficient and E-static-continuum assessments; rechecked Lawler--Limic's author-hosted 289-page text, section 1.1 printed pp. 9--11, Theorem 4.3.1 pp. 81--83 including its bipartite and transient proof cases, and Corollary 4.3.3 p. 84. Precise applicability and limitations follow.
COMPARISON: L112/L114 already bound two comparison errors within the requested budget, and L118 annihilates only R_inf. L116's compression tail and L119--L123's four coefficient comparisons remain qualitative in essential places. Scalar Green estimates are usable inputs for a narrower compression-tail test, not a complete transverse-H rate theorem.
GAP: First quantify exactly L116's complete finite-compression difference; independently quantify the exterior-circulation and generator/scalar/energy coefficient remainders before assembling the complete target. No new estimate is established in this review.
REASON: The completed source comparison supplies an independently testable compression-tail continuation with accessible scalar inputs; it neither imports the full rate nor repeats a blocked source request. The newly written narrower assessment requires separate continuation approval.
SCOPE: Relative SU(2) cube, admitted sufficiently fine even N, a=8/N, tau=1/16, lower-rooted direction-1 forest, bare-first expansion, stored full-link coordinates, complete displacement, probes i=3,6, both residual insertion forms, two coefficient levels, upper jump, all source/end rows, constant modes and full heat sums; all imported analytic and unresolved audit premises remain.
LITERATURE_REASON: The changed quantitative transverse-H target was REVIEW_REQUIRED at invocation start and is outside L266's joint cubic-probe assembly audit; qualitative other/other coverage alone does not cover the changed rate.

## Relevance and exact comparison

The main gap remains interacting continuum existence, a nonzero physical
sector, the continuum axioms and finite positive infinite-volume mass.
This proposed component rate could support later quantitative L011
bookkeeping. It does not supply an interacting perturbative remainder,
reflection positivity or any construction conclusion.

The essential starting results remain L110--L116 and L118--L124;
L109 is a failure contrast. L124 proof section 2, (7)--(10), fixes
the exact finite telescope, with every retained difference positive:

    R_H,tr = E^f + R_pin + Delta_V + Delta_sc + Delta_P
                            + Delta_en + Delta_C + R_inf.

Here Delta_C is precisely R_prod-R_inf in L116, not a different
projection comparison. The outside factor 3 belongs to the later
other/other assembly. Subtracting the requested four coefficients
leaves all four coefficient remainders and all three comparison errors.
This is the imported bookkeeping, not a new remainder theorem.

## Inspected local coverage

| Part | Inspected evidence | Remaining scope |
| --- | --- | --- |
| R_pin | L112 hypotheses/conclusion and proof sections 2--5: O(N^(5/2)log N), retaining every boundary input | Already inside the proposed budget; no new audit claimed. |
| Delta_P | L114 hypotheses/conclusion and proof sections 2--5: O(N^(5/2)(log N)^(3/4)) | Already inside the proposed budget; distinct from compression. |
| Delta_C | Full L116, especially (9)--(15): at most C_i N^3 eta_N, eta_N=sum_j q_j(N), q_j(N)^2=sum_(|z|>=cN)|z|^2||e_j(z)||_F^2 | Dominated tail removal states no N-dependent rate. Both omitted-output selectors must remain. |
| R_inf | L118 hypotheses/conclusion and full-grid formula (1)--(3) | Exactly zero; it does not remove Delta_C or earlier placements. |
| Delta_V | L119 (7)--(16), L120 hypotheses/conclusion and proof sections 1--4 | L119's eta(a) tends to zero by dominated convergence; L120 next fixes offsets before projection comparison and Riemann limits. These are additional rate obligations. |
| Delta_sc, Delta_en | L121 proof sections 4--6 and L122 sections 2--4, with their definitions/conclusions | Joint first moments are summable, but Theta(J0,R) and fixed-offset derivative convergence have no stated combined quantitative modulus. Both coefficient levels remain. |
| E^f | L123 hypotheses/conclusion and proof sections 1--5 | The f,f term is O(N^2); covariance-mass removal costs C_i N^3 sqrt(epsilon). Subsequent axial, projection, polynomial and freezing bounds depend on fixed parameters; their complete uniform quantitative comparison remains missing. |

L110 in full identifies the exact full matrix kernel and its summable
quadratic first moment. That moment supports L116's qualitative tail;
it does not by itself state the desired rate for that tail. No estimate
from L266 or from a differently ordered co-closed trace is transferred.

The 2026-10-20 remaining-rate inventory already recorded these gaps.
This review adds primary-source applicability to a concrete compression
test; it does not count repeating that inventory as a mathematical advance.

## Primary source applicability

Lawler--Limic, *Random Walk: A Modern Introduction* (Cambridge, 2010),
[author-hosted text](https://www.math.uchicago.edu/~lawler/srwbook.pdf),
289-page version accessed 2026-10-23: section 1.1 defines P_d by
symmetric finite-range irreducible increments. Theorem 4.3.1, printed
pp. 81--83, assumes d>=3 and gives the anisotropic continuum Green
term with O(|x|^(-d)) error. Its proof includes bipartite walks and
controls short, intermediate and long time ranges. Corollary 4.3.3,
p. 84, gives first and repeated-coordinate second difference bounds.
Four-dimensional nearest-neighbor simple walk meets these hypotheses.
The unnormalized lattice Laplacian requires its factor 2d=8.
These scalar statements are imported by citation, without reproof.

For the proposed application, one must still identify every matrix
entry of L110's e_j with its correctly shifted scalar Green differences,
justify mixed differences rather than citing the repeated-coordinate
case alone, retain zero offset and all integer j, and estimate the
complete squared tail. These are obligations for later mathematics,
not conclusions of this review. No essential source is inaccessible.

Reuse the existing 2026-10-17 complete-coefficient comparison of
Adams--Lee 0709.0781v3, section II and Appendix A: its translation-
invariant Brillouin integral hypotheses have not been matched to this
pinned variable-coefficient trace. Reuse the 2026-10-10 assessment's
Del Debbio--Patella--Rago 1306.1173v1 section 6 and Luescher--Weisz
1101.0963v2 sections 7.2--7.4/8.2 comparison. Renormalized flowed Ward
finiteness does not assign a bare isolated forest block its quantitative
remainder. Those ready primary assessments need no repeated reading.
Gurevich 1504.02673v2 remains a whole-space parabolic supporting lead
with the scope recorded in the E-static-continuum assessment; no new
application or further proof reading is claimed.

Queries on 2026-10-23 were `Lawler Limic Random Walk Modern Introduction
Corollary 4.3.3 second differences Green function pdf`, `lattice Green
function second differences bound dimension four nearest neighbour
infinite lattice Gurevich asymptotics`, `"joint circulation" "energy"
"lattice" Green function`, and `"lattice Green function" "second
differences" "four"`. The first pair located the primary scalar source
and existing parabolic lead; the latter pair supplied no inspected
matching theorem. Unrelated search hits and the 1991 Lawler article
are unread, unused leads. This bounded search establishes no novelty
or global absence claim. Full matching Mathlib coverage is not checked.

## Duplicate/failure disposition and bounded continuation

Read history/142 and the original energy-compression draft: they prove
and record o(N^3), not a quantitative rate. Scoped searches found no
duplicate compression-rate assessment or theorem. L109's conclusion
and proof section 5 rule out a first absolute moment of a separate
alternating factor, not a squared tail of L110's circulated covariance.
ATTEMPTS/030 stops varying a mass inside a fixed-mass qualitative limit;
the proposed finite kernel-tail comparison needs no such substitution.
ATTEMPTS/043 concerns an insufficient full-residual norm, a different
mechanism. These stops and unfinished work are preserved.

The next independently testable target is exactly L116's complete
compression difference at the same N^(5/2)log(eN)^2 budget. Its source
assessment is `2026-10-23-transverse-h-compression-quantitative-rate.md`.
It tests a quantitative modulus for L116(10)'s all-offset squared tail,
then its existing complete finite trace estimate. No new scalar theorem
needs reproving. A later success would remove one obstruction to the
complete rate; it would leave four independent coefficient comparisons.

Continue only with a finite uniform bound within the requested budget
after both selectors, all levels and heat labels are restored. Reassess
this mechanism if only fixed-j convergence, an uncontrolled mixed entry,
or a larger allowance remains. Such failure would not prove signed
growth or disprove the complete target. The narrower assessment is new
and receives separate approval next turn. This completed LITERATURE /
NOVELTY_UNCHECKED step has outcome EXPLORATION and spends no mathematical
exploration turn. PROOF, DAG, lemmas and scripts are unchanged. All
upstream qualifications, quantitative L011 assembly and interacting,
continuum and infrared construction requirements remain unresolved.
