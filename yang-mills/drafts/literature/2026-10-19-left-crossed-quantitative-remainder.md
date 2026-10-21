# Left crossed trace — quantitative source comparison

TARGET: Establish an O(N^(5/2) log(eN)^2) bound for L100's complete left crossed trace R_L for both actual probes.
CHECKED: 2026-10-19
DECISION: EXPLORE
SEARCH_EVIDENCE: Read full L100, L093 through its actual trace bound, L088's alternating/heat formulas, L089's split and spectrum, L090's derivative/collar/mass passages, the original left-crossed draft/history and ATTEMPTS/029--032; compared ready quantitative source assessments and L225--L229's stated scopes. Six bounded external queries below found no inspected matching complete-rate theorem.
SOURCE_EVIDENCE: Reinspected Benzi--Simoncini 1501.07376v1 section 3 (3.1)--(3.2), Theorems 4.1--4.2 with both proof regimes, Theorem 4.4 (4.1) and section 5, printed pp. 5--8 and 11--12; reused the recorded Lawler--Limic scalar Green, Adams--Lee one-loop and flow/Ward primary comparisons, with their limitations below.
COMPARISON: L100 proves only a^3 R_L -> 0: its O_epsilon(N^(5/2)) prefix error and fixed-mass projection/localization constants give no joint finite-N rate. Existing co-closed-sector estimates involve different projected factors and generator placement. Known scalar and sparse-matrix tools support a bounded test, but no inspected source supplies the requested R_L bound.
GAP: Establish uniform finite mass/projection errors, control the complete prefix-commutator trace and transfer the local odd cancellation through ordered localization, coefficient freezing and relative boundaries, with the entire heat sum. These are mathematical specialization obligations, not proved estimates or essential inaccessible sources.
REASON: Target-specific source comparison is complete for one later bounded attempt at exactly TARGET. EXPLORE approves scope only; no rate, parameter schedule, new lemma or novelty claim is established in this literature turn. The new assessment requires separate supervisor approval before research.
LITERATURE_REASON: The quantitative R_L conclusion was REVIEW_REQUIRED and lies outside the qualitative other/other and accepted H-axial coverage; reusable ready source assessments are retained instead of repeating their broad searches.
SCOPE: Relative all-face pinned SU(2) cube, straight lower-rooted direction-1 forest, sufficiently large admitted even N, a=8/N, tau=1/16, stored coordinates, bare-first coefficient, actual probes 3 and 6 and complete exterior heat sum.

## Completed comparison

This is one LITERATURE / NOVELTY_UNCHECKED / EXPLORATION step. No
lemma, mathematical script, proof assembly or DAG is changed. The
original registration is preserved below as a superseded scope record.
The main gap remains the interacting reflected error <=c_box/2 and the
continuum/infrared construction with finite positive mass. This one
component rate could support a quantitative L011 assembly; other
component rates and the interacting remainder remain independent gaps.
There is no complete-solution candidate or progress beyond the sources
checked. Reuse foundations/01-target-and-scope.md's Jaffe--Witten target
version; no new construction route is selected.

### Exact local comparison and duplicates

L100(1) fixes the trace with two K factors, the gh adjoint on the left,
the actual A=H_g K_a I_T in the middle and hh on the right. L093(2)--(3)
keeps it distinct from R_R and R_Q; neither is part of TARGET. L088(3)--(5)
fixes the entire skew alternating map and polynomially summable actual
heat coefficients. L089(1), (5)--(6) and L090(6)--(11) supply precisely
the exterior-circulation split, relative inverse-square spectrum and
staggered derivative/collar inputs used by L100. These are imports,
not a recursive audit of upstream results.

The following are **existing** estimates, not improvements made here:

| L100 passage | Existing scope | Unresolved obligation for TARGET |
| --- | --- | --- |
| (4)--(6) | Low-spectrum mass removal for both Omega K factors, including beta_N before the limsup | Retain finite-N errors and quantify mass dependence in every later step. |
| (7)--(9) | Exact local/prefix split; complete normalized prefix commutator has HS norm O(N^(3/2)); its trace is O_epsilon(N^(5/2)) at fixed mass | Control the trace uniformly in the regime actually used; the fixed-mass coefficient is not a uniform constant. |
| (11)--(13) | Projection regularization in normalized HS norm after covariance mass, with a constant depending on epsilon | Bound every P and Q replacement in this ordered product, including P inside A_loc. |
| (14)--(16), proof section 4 | Exact frozen odd-symbol cancellation and collar/freezing errors at fixed polynomial degrees | Bound localization, coefficient errors and relative boundary transfer jointly, without assuming prefix locality. |
| (3), proof section 5 | Full polynomial heat envelope and successive removal of parameters | Obtain a single finite-N bound with summable modal constants, rather than substituting varying masses into successive limits. |

The original draft and history/126 explicitly stop at qualitative cubic
vanishing; they give no hidden quantitative continuation. Narrow searches
of the quantitative assessments and the left-crossed draft/history found
no duplicate rate. The broad complete-coefficient assessment licenses
only separately assessed components. This is a scoped duplicate check,
not an assertion of global absence or originality.

L225(1) is a reusable scalar resolvent-difference energy inequality for
the same Delta_E. Its completed trace estimate is for T_hh, not R_L.
L226(5) similarly counts the same transverse projection spectrum;
its generator placement and gradient-annihilation argument must not be
transferred without checking this product. L227's squared-moment estimate
is for Q_delta Omega Q_delta^2/(h+epsilon), with the complete co-closed
factor on both sides. It does not cover the gh factor and P-containing
A_loc by identification. L228's ordered bulk bound and L229's two-sided
boundary comparison concern their specified T_hh product. L229's scalar
Chebyshev residual and polynomial-path principle are supporting tools;
neither its product identity nor its final bound is imported for R_L.
The accepted H-axial rate concerns another kernel and supplies no R_L
estimate. This review derives none of these missing transfers.

### Primary tools and applicability

Benzi--Simoncini, [*Decay bounds for functions of matrices with banded
or Kronecker structure*](https://arxiv.org/pdf/1501.07376v1), v1,
29 January 2015, printed pp. 5--8 and 11--12: Theorem 4.2 assumes
Hermitian positive semidefinite banded M with spectrum in [0,4rho].
Its two heat-decay regimes follow from finite polynomial propagation
and the corresponding Krylov error estimates in Theorem 4.1. Theorem
4.4 requires positive definite M and a Laplace--Stieltjes function;
its three time ranges retain lambda_min. Section 5 replaces band
distance by graph distance; disconnected component blocks are treated
separately. Uniform infinite/finite-section bounds require a bounded
spectrum and no function singularity near it. Section 3 records
condition-dependent inverse decay. These tools apply to each massive
scalar relative component Laplacian with its actual end rows. They do
not give a uniform massless bound, a prefix-commutator estimate, or the
signed trace rate. The incidence factors, variable coefficients and
projection placements need separate estimates. No reproof of the
general theorem is needed. No original Demko or Benzi--Razouk theorem
is imported from its citation or abstract.

Reuse the primary scalar comparison in
`2026-10-18-h-curvature-static-continuum-rate.md` and the axial assessment:
Lawler--Limic, [*Random Walk: A Modern Introduction*](https://www.math.uchicago.edu/~lawler/srwbook.pdf),
Cambridge (2010), Theorem 4.3.1 and Corollary 4.3.3, pp. 81--84,
and Theorem 6.3.8(a), p. 131, including its harmonic-measure proof.
The former assumes transient symmetric finite-range irreducible walks;
the latter bounds interior differences of signed harmonic functions.
For the nearest-neighbor three-dimensional transverse scalar operator,
Delta=6(I-P_walk), so the Green normalization is G_walk/6. These
sources support the already assessed scalar/energy-cutoff methods.
Relative vector projection columns, noncompact prefix output and this
ordered R_L trace remain local obligations; scalar Dirichlet conditions
cannot be assigned to all vector components. L224's E and L234's H
conclusions are not transferred to R_L. No scalar theorem is reproved.

Reuse the complete-coefficient assessment's inspected Adams--Lee,
[*Structure of logarithmically divergent one-loop lattice Feynman
integrals*](https://arxiv.org/pdf/0709.0781v3), v3, 5 December 2007,
section II (7)--(15) and Appendix A (A1), (A11)--(A18). Its smooth
translation-invariant Brillouin-zone numerator/denominator hypotheses,
negative lattice degree and infrared finiteness do not identify this
pinned, position-dependent trace or give uniform exterior heat summation.
Its rate cannot be imported here. Reuse the original other/other
assessment's Del Debbio--Patella--Rago 1306.1173v1 section 6,
(6.1)--(6.17), and Luscher--Weisz 1101.0963v2 sections 7.2--7.4 and
8.2: full renormalized flowed Ward identities and flow finiteness do not
bound an isolated bare forest trace. Their detailed primary hypotheses
and essential cases remain recorded in the ready assessments; they were
not browsed again. These unchanged scope comparisons require no reproof.

### Search scope, failures and bounded test

External queries on 2026-10-19:

- `"lattice" "left crossed" "trace" Yang Mills`
- `"lattice perturbation" "finite volume" "boundary" "power counting" theorem`
- `Benzi Simoncini decay bounds functions matrices banded Kronecker 1501.07376 theorem 4.2`
- `"lattice gauge" "trace" "variable coefficients" "remainder"`
- `"lattice" "Hodge projection" "commutator" estimates resolvent`
- `"lattice perturbation" "finite volume" "power counting" boundary theorem`

No inspected matching or stronger complete-rate theorem was located.
General lattice-perturbation reviews, twisted-periodic finite-volume
calculations and numerical Hodge leads were not read at theorem level
and supply no coverage. The primary matrix-localization result above
was retrieved and its relevant proof cases inspected. Optional unread
original decay papers are not essential premises; no essential source
blocker remains. Failure to locate a match establishes no novelty.

ATTEMPTS/029--032 were read in full. Preserve their obstructions:
individual transport multipliers need not have small projection
commutators; a fixed-mass limit cannot receive a varying mass by
substitution; the complete symmetric generator need not be bounded;
separate projected alternating factors need not have finite first
absolute moments. These are failed sufficient mechanisms, not trace
lower bounds or global bans. L100's exact prefix split, joint weighted
estimates and ordered finite-boundary comparison remain a different,
independently testable quantitative mechanism.

After separate approval, one attempt at exactly TARGET should first
expose finite-N mass errors and the complete prefix-commutator trace
in L100's original order, then test the local part with quantitative
projection/localization and boundary estimates. Use only uniform finite
inequalities before choosing parameters. A useful proved partial input
may leave the other errors unresolved; label it accordingly. Continue
for a relevant uniform error within the stated final budget, or a new
obstruction that changes the route. Abandon a specific transfer if its
actual row/heat count cannot meet the budget or requires a stopped
commutation/moment premise; preserve the failed inequality. An excessive
upper bound is not signed growth or a disproof of TARGET.

Essential continuation inputs are L009 L028 L088 L089 L090 L093 L100
and their inherited finite contraction/spectral hypotheses. Supporting
L225--L229 scalar or polynomial tools require the applicability checks
above; no conclusion for their different trace is assumed. Keep all
source/end rows, constant indices, the complete prefix and actual
endpoint/clover filters, both actual probes, full heat sum, exact R_L
and bare-first order. Uniform prefix, projection, localization and
boundary rates remain unproved. Full matching and supporting Mathlib
coverage for this target are **not checked**; unknown is not absence.
No mathematical exploration turn is consumed by this source review.

## Original registration — superseded process record

The following text records what was registered before this comparison;
its REVIEW_REQUIRED process instruction is superseded by the decision
above, subject to separate supervisor approval.

The main gap remains the interacting reflected error <=c_box/2,
cutoff removal, continuum axioms, infrared control and finite positive
mass. The intermediate target is one missing component rate for a
quantitative L011 remainder. Other component rates and the complete
interacting comparison remain independent gaps. No full solution
candidate is proposed.

Essential inputs to assess are L009 L028 L088 L089 L090 L093 L100,
with their inherited finite contraction and spectral hypotheses.
Keep exactly R_L in L100(1), including both actual alternating blocks,
the ordered generator A=H_g K_a I_T and the two K occurrences.
Do not transfer a reverse crossed, H diagonal or co-closed diagonal
estimate to this orientation. All end rows, source rows, allowed
constant indices, actual generator filters and heat labels remain.
L093's separate curvature subtraction R_Q is not added to R_L.
The upstream results are imports, not recursively verified facts.

Reuse ready source notes first. Check the original L100 proof and
its recorded continuation for duplicates or a rate already proved.
Compare ATTEMPTS/029--032 before using commutation, mass schedules or
factorwise absolute moments. Primary theorem hypotheses and essential
proof cases must cover the actual uniform estimates; unanswered or
blocked leads are not coverage. Full and supporting Mathlib coverage
for this exact rate are not checked.

Continuation test: approve a mathematical attempt only if source scope
is adequate for an independently testable finite error bound leading
to the stated threshold. Otherwise identify the essential missing
source or select a different independently testable target. In later
mathematics, accept the requested bound only from uniform finite
inequalities with the entire heat sum; a qualitative limit at fixed
mass cannot be evaluated at varying mass. A failed upper-bound route
would not prove signed growth or refute the requested bound.

This is a future-target registration after a completed axial proof
audit. The next invocation is literature-only for exactly TARGET;
no new R_L mathematics has been performed or approved here.
