# Scale-adapted band cost: proposed mathematical continuation

TARGET: Calculate the L471 band majorant with cells h=u/log T, disk radius 6h and area collar h, and test its costs against dyadically summable decay in u.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed exact/stronger-result and narrow local duplicate comparison in 2026-10-28-scale-adapted-complementary-mass-coverage.md; no additional search or novelty claim for this continuation.
SOURCE_EVIDENCE: Titchmarsh--Heath-Brown (1986) Theorem 7.2(A) p. 141 https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=75, functional equation (2.1.9)--(2.1.10) p. 16 and chi asymptotic (4.12.3) p. 78/Section 5.1 p. 95; NIST DLMF 5.11.1--2/5.11.9 https://dlmf.nist.gov/5.11; Broughan II (2017) Theorem 3.3 proof (1),(4) pp. 26--27 https://api.pageplace.de/preview/DT0400.9781108195430_A31720577/preview-9781108195430_A31720577.pdf#page=48, reused through L474. Exact primary passages, applicability and Bettin's limitation are recorded in the completed comparison; direct URLs rechecked in this recovery review.
COMPARISON: Known finite factorization, submean area control, uniform continuous mean squares and sector Stirling cover the tools for this concrete rescaling. L474 supplies only the microscopic application; neither its bounded completion ratio nor Bettin's microscopic real-shift range may be reused on the larger disks.
GAP: Calculate the combined u-dependent band envelope, with single-pair cells and multiplicities, and determine whether it has summable dyadic tails or requires a new independently testable constraint. No useful envelope or complementary saving has been derived.
REASON: One bounded established-tool specialization can distinguish compensation from growth without an unproved occupancy/density assumption. Separate literature approval and direct-source-URL repair are now complete; the next turn may calculate within this exact scope.
LITERATURE_REASON: Supervisor recovery requires direct source URLs in the ready assessment; this turn repairs that omission and verifies access, without repeating discovery or deriving a bound.
SCOPE: L471 actual-Xi pairs, full m_j, one-pair quotient F_j, clipped J_j(T); T large, L=log T, 1<=u<L/16 and u<d_j L<=min(2u,L/16); no RH, simplicity, separation, density, selected-energy saving or external half-plane premise.

## Direct-source recovery review (2026-10-28)

The three direct URLs in SOURCE_EVIDENCE were opened successfully.
Titchmarsh's PDF image page 75 contains printed pp. 140--141;
Theorem 7.2(A) and its proof explicitly give uniformity for
1/2<=sigma<=2, unlike the fixed-sigma asymptotic immediately above.
Its proof treats sigma near 1/2 and sigma>=1 separately. The
functional equation and chi references remain reused from the
completed comparison, rather than claimed newly audited here.

DLMF 5.11.9 explicitly covers both signs of the imaginary part and
bounded real parts; 5.11.1--2 retain their closed-sector condition.
Broughan's Theorem 3.3 proof (1), printed p. 26, states the finite
quotient supremum bound and repeats zeros according to multiplicity;
part (4), p. 27, handles zeros at the origin. Only these finite-factor
passages are needed; this review does not import the intervening
infinite-product claims or audit them. The future rescaling still
owes every normalization, denominator and area-norm check listed below.

The prior comparison remains adequate and its duplicate/failure
decisions are unchanged. This is a process repair, not new source
scope or mathematical progress. No lemma or mathematical script was
changed. Full matching Mathlib coverage remains not checked.

## Preserved calculation obligations

The main unresolved estimate is L471's full B(T)=o(T L^3), which
would give a mean negative-first-sign saving but would still leave
individual signs and higher mixed positivity open. This test concerns
only its displayed complementary bands, not the full estimate.

Use width-h half-open cells, centers c_k, radius 6h disks and radius
7h disks for area control. Keep all assigned conjugate factors and
their multiplicities before removing exactly one copy of pair j.
Calculate the residual-factor contraction, the q_j scaling, the
normalization relative to A(c_k) and A(t), and the continuous area
norm with its overlap. At every stage retain the u dependence and
both signs of Im z. Use the inspected uniform bound on the right
of 1/2 and reflection with its chi cost on the left; there is no
zero-selected moment import. These are proposed proof obligations,
not assertions already proved in this assessment.

State an actual envelope K(u), if available, in units of T L^3,
uniformly for the stated T,u range. Test whether the dyadic sum of
K(u) over u>=U tends to zero as U grows; this is a large-u tail
test and would not settle any fixed-u annulus. Explicitly evaluate
what this method offers for a cell with one simple selected pair;
do not silently substitute a growing cluster occupancy. If extra
compensation is needed, state it as an unresolved condition, not an
input. Do not optimize a different geometry or import an all-zero
selection theorem under this target without a new source gate.

Continue only for summable tail decay or a precise additional
constraint with a plausible independent test. Otherwise preserve the
failed upper-bound comparison and park this implementation. A failure
of its envelope supplies no lower bound for actual B(T) and cannot
disprove the target. Leave the fixed microscopic annulus, d_j>1/16,
full mass saving and individual/higher signs explicit.

Essential local inputs: L471 definitions and majorant; L474 finite
factor/continuous-norm template; L018's high-strip normalization;
L465's sector gamma control. No cross-notebook input. Full matching
Mathlib coverage is not checked. The proposed work is a reproduction
and specialization, not a certified new mechanism. A creative route
would need a materially different cancellation or selection input,
which this source review has not identified.
