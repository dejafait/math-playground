# Coverage: subendpoint theta-sector reduction

TARGET: Attempt a uniform whole-plane theta-sector reduction to L454's S_{r,m} on 31/32≤m/r≤63/64 with normalized error O((1+r)^K exp(−κr)) for fixed K,κ>0.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded exact-terminology searches for Riemann Xi generalized Laguerre inequalities, saddle/stationary phase, logarithmic orders and theta/Riesz reductions found no inspected matching uniform-band theorem. Reused the rounded-endpoint comparison and October overlap review; compared the named local sector proofs and L323/L327 failures. Queries and inspected/unread distinctions appear below; no novelty or exhaustive-search claim.
SOURCE_EVIDENCE: Csordas, arXiv:1309.0055v2 (21 February 2014), Theorem 3.5, Lemma 3.6 and Theorem 3.7 with proofs; NIST DLMF 2.3(iv), hypotheses (a)–(d), 2.3.21–2.3.23, and 7.2.6–7.2.9. Inspected L269, C294b and L324–L326 in full, L453 Sections 1–6 and corresponding audit passages, and the L454 arithmetic interface; reused the existing shifted-class/coefficient comparison and fixed-half-plane assessments.
COMPARISON: The sources supply representation and stationary-phase mechanisms, not this whole-plane uniform error theorem. C294b covers the mixed-sector h range; L324–L326 retain growing mass and r/20 strips at one fixed proportional exponent, while L453 proves only bounded exponent offsets from r. Their explicit arguments support a uniform specialization attempt but their stated conclusions cannot be substituted for its proof.
GAP: Uniformly control the exact finite-weight mass and cutoff tails, all clipped stationary patches, moving-domain complements and both same-sign strips; then assemble the exact positive normalization with one error bound and onset over the full band. No new sector estimate or Laguerre sign is established by this review.
REASON: The separate changed-band comparison is now complete at source/mechanism level. Reuse the audited arithmetic input; a local proof must still supply parameter uniformity not stated in the inspected theorems. No reproof of the external zero-free theorem or additional Mellin research is needed.
SCOPE: One bounded uniform-sector specialization attempt on the specified band, using the smaller-strip mechanism and retaining L454's original signed sum. No arbitrary-phase signing, fixed-r all-height positivity, smaller-index completion, new zero-free region or RH claim.
LITERATURE_REASON: The changed proportional exponent is outside L453's bounded-offset sector estimates and the completed arithmetic assessments; essential uniform-sector source comparison was missing at invocation start.

## Completed review and relevance

The saved action at turn start was: “Assess source coverage for a uniform
whole-plane theta-sector reduction to L454's S_{r,m} on
31/32≤m/r≤63/64 with exponentially decaying normalized error.” This
literature-only step completes that comparison and records the exact
mathematical continuation above. The newly completed assessment requires
the supervisor's separate approval on the next turn before research.

The main gap remains global mixed positivity and the initial low-index
segment. The intermediate target is a whole-plane reduction to precisely
L454's full finite sum, retaining exact positive factorial and reflection
normalization, with remainder at most C(1+r)^K exp(−κr), for fixed
C,K,κ>0. Its downstream use is comparison with L454's separately audited
arithmetic margin. Neither that reduction nor its sign consequence is
proved here. The outcome is source exploration, not a new mathematical
input or progress beyond the checked sources.

Retain positive even m, real r tending to infinity,
31/32≤m/r≤63/64, h=9/2+m/(2r),
a²=4π²exp(4r)−h² and a>0. The arithmetic input is audited L454
with the precise pinned external premise and its unaudited manuscript/
import closure. The prospective Laguerre level is m/2. Do not infer
uniformity in this proportional band from L453's bounded exponent
offset or from L326's single fixed below-five value.

## Primary sources and reuse

George Csordas, [*Fourier transforms of positive definite kernels and the
Riemann ξ-Function*, arXiv:1309.0055v2, 21 February 2014](https://arxiv.org/html/1309.0055v2),
Theorem 3.5 assumes an admissible strictly logarithmically concave kernel
and proves admissibility of its associated kernels. Lemma 3.6 and
Theorem 3.7, equations (3.10)–(3.14), give the double-integral/coefficient
identity; their proofs retain the factor-two change of variables and
coefficient factorial. Theorem 3.7 still requires positive definiteness
at every level for the Laguerre–Pólya conclusion. These inspected
statements supply no signed high-height sector estimate. The admissible
kernel definition and its comparison with the local theta kernel are
already covered in the [rounded-endpoint assessment](2026-10-23-rounded-endpoint-height-coverage.md).
Reuse that comparison; do not import positive definiteness from kernel
positivity or identify the paper's whole-line F with Ξ without its factor.

[NIST DLMF §2.3(iv)](https://dlmf.nist.gov/2.3#iv), inspected
2026-10-23, hypotheses (a)–(d) and equations (2.3.21)–(2.3.23),
assumes smooth real phase/amplitude, positive phase derivative away from
the endpoint, differentiable endpoint expansions, and finite endpoint
limits or uniform convergence at infinity. Both finite endpoints
contribute. It provides a stationary-phase source mechanism, not
uniform constants for moving amplitudes, clipped domains or growing
theta-index sums. Its references to Olver (1974) and Lyness (1971)
were not read and are not imported error theorems. For this attempt the
explicit local phase change and rectangular-variation proof remain
available, so no unseen general error theorem is essential.

[DLMF §7.2(iii), equations (7.2.6)–(7.2.9)](https://dlmf.nist.gov/7.2#iii),
inspected the same day, defines the Fresnel integrals and gives both
real-axis limits C(+∞)=S(+∞)=1/2. This supplies the standard scalar
normalization only. Uniform amplitude and clipped-endpoint errors must
still be justified by the explicit local bounds; these limits alone
do not establish them. DLMF is cited by section/equation and access date;
no unobserved release number is assigned.

The [rounded-endpoint assessment](2026-10-23-rounded-endpoint-height-coverage.md)
already compares Wagner 2108.01827v2, Theorems 1.2/1.4 and the proof of
1.2, and the Wang–Yang institutional manuscript, equations (1.1)–(1.4)
and Theorem 1.3. Reuse its findings: high derivative shifts or Maclaurin
sequence inequalities do not give original-Ξ real-height sector control.
Wagner's landing text was reopened; no new theorem reading or stronger
claim is attributed to that reopening. The
[October overlap review](2026-10-21-openai-quasi-rh-overlap.md) and
[external-input register](../../foundations/2026-10-quasi-riemann-input.md)
were read and reused. The conditional L454 margin retains the pinned
September 30 Theorem 1.1 at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`, the strict 7/8 boundary,
allowed pole and unaudited external manuscript/import closure. None of
that source work must be repeated to attempt the sector reduction.

## Local theorem comparison and exact remaining work

L269's exact parameterwise contour shift and coefficient normalization
are available independently of its proportional-index asymptotic. The
latter's positivity conclusion is outside the present scope. Retain
`C₀=(8π²)²`, `τ=arctan(a/h)/2` and
`Φ_*=m log r+9r−h−2aτ`. The intended normalization is the existing
L326/L453 pattern `I_{m/2}/(C₀exp(Φ_*)π/a)`. A later proof must
show that its difference from S_{r,m} meets the target error. The
coefficient multiplier is exactly `2^(m−1)/m!`; doubling the reflected
same-sign interiors must occur once, with each positive-coordinate
Jacobian already included. These are existing formulas, not a new
changed-band assembly proved here.

C294b's stated interval 39/8≤h≤5 contains the proposed h-band. Its
entire-sector estimate includes termwise absolute integrability,
stationary indices, both finite-boundary primitives and infinite-edge
limits. It is reusable as a sector input after the elementary domain
and even-index applicability check. Its positive fixed decay rate does
not control the same-sign regions.

L453's proof domain is r−1≤m≤r+2. In particular its weight mass O(r),
translated index sum O(1+r), and subsequent strip estimate use that
bounded-offset condition. They cannot be quoted at a fixed fractional
deficit m/r<1. Extending only its compact h interval is insufficient:
the index weights also change. The new attempt must bound the complete
mass before multiplying any local error, rather than use L453 (9),
(16), (23) or (25) outside their proved domain.

L324 fixes m/r=3/4 and uses the smaller boundary min(u,v)≤r/20,
splitting at the other coordinate 101r/100. Its proof sums Gaussian
index weights first and retains polynomial derivatives through order
two on a low rectangle, with superexponential suppression above it.
L325 fixes the same exponent, controls its growing coefficient mass
and the complete log-index tail near 19r/20, and evaluates all full
and clipped stationary squares with uniform per-weight errors. Its
moving-domain nonstationary variation has explicit index cutoffs;
it never sums a divergent uncut power. L326 assembles those estimates
with the mixed sectors and the exact normalization. All three full
proofs were inspected. Their fixed-exponent conclusions are not
theorems on an interval of m/r.

These proofs provide a concrete specialization mechanism: retain the
r/20 split and all exact m-dependent powers, and recheck the mass,
tails, polynomial derivatives and translated-domain sums uniformly.
Use the same explicit fixed-square real phase change, retaining the
full relative amplitude derivatives on every nonempty clipped patch.
Compare the summed patch error, not merely each fixed-index error,
with the target. The first test is whether these *complete* masses and
tails can be paid for at a fixed exponential rate throughout the band.
No value of that rate or assertion that these inequalities hold on the
new band is derived in this review.

## Duplicates, recorded failures and stopping test

The targeted local comparison found no already stated uniform theorem
for this band. The explicit distinct scopes are m/r=3/4 in L326,
bounded m−r in L453, and arithmetic-only comparison in L454. This is
a scoped duplicate check, not a claim of originality. L303's endpoint
cutoff cannot be transplanted; L454 already defines the exact full sum
to be used, so no new Mellin inversion or arithmetic freezing is needed.

Read L323's hypotheses/conclusion, exact summands and proof summary,
and its [recorded failure](../../ATTEMPTS/2026-09-24-below-five-boundary-strip-test.md).
It stops the r/4 summed-modulus strip certificate at m/r=3/4 because
that strip contains a growing stationary family. It does not forbid
retaining those terms in the interior arithmetic sum with a smaller
strip. Neither its lower bound nor a corresponding obstruction on the
new band is inferred here. L327's exact hypotheses/conclusion and
[balanced-AFE failure](../../ATTEMPTS/2026-09-24-below-five-balanced-afe-test.md)
retain the same unsigned form and rule out its phase-uniform PSD
replacement at the stated fixed-band precision. That obstruction is
preserved without extrapolation; the present target retains the signed
sum and imports L454's actual coupled-height comparison separately.

Continue only after separate approval, and only if one proof accounts
for every sector and cutoff with fixed constants and one onset over
all admissible real r and even m. A complete normalized error
C(1+r)^K exp(−κr), κ>0 fixed, is the requested pass threshold. Its
later comparison must use L454's non-Euler lower margin, not L453's
right-of-one reciprocal-series bound. If a summed tail, derivative,
clipping or boundary budget does not decay exponentially, record the
specific failed bound and stop this implementation; do not infer a
negative coefficient or discard the uncontrolled region.

Essential continuation inputs are L269, C294b, L324–L326, L453's
explicit sector methods and audited L454 (with L303/L330/L452 retained
as its established inputs). The proposed changed-band uniform
same-sign estimates and complete assembly remain unproved. Initial
smaller indices, bounded exterior heights, global mixed positivity and
selected-law/regulator gaps remain independent even if it succeeds.
Full matching Mathlib coverage is not checked; no absence is asserted.
No lemma, mathematical script, DAG or main argument was changed.

## Search record and unread leads

New queries: `"Riemann Xi" "Laguerre" "saddle" uniform`;
`"generalized Laguerre" "Riemann" "logarithmic"`;
`site.dlmf.nist.gov/2.3 stationary phase parameter uniform`;
`"Riemann xi" "stationary phase" "Laguerre inequalities"`;
and `"theta" "Laguerre" "Riesz" zeta`.
The previous rounded-endpoint search/primary comparison is reused
rather than presented as a fresh exhaustive search. Results about
classical Laguerre polynomials, Riesz criteria or unverified RH claims
were not imported. A 2025 SIGMA parameter-dependent stationary-phase
result appeared as a search lead but was not read; it is not an input
or an essential source blocker because the explicit local method is
already covered. The working checkpoint is
[the source-comparison note](../2026-10-23-subendpoint-theta-sector-source-notes.md).
