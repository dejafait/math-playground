# Actual-theta compensation after one spatial integration: source comparison

TARGET: Assess whether C604b's actual-theta layer contribution plus L604's remainder integrated in b can be nonnegative for every a and x, and cover a bounded negative-witness test.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Exact and stronger Stein/Fourier/Laguerre/theta searches and scoped duplicate/failure checks completed below; no matching sign theorem for this allocation found in the inspected sources. Reused the ready base Stein and theta assessments; this is not a novelty or absence claim.
SOURCE_EVIDENCE: Csordas https://arxiv.org/pdf/1309.0055v2 Theorems 4.5-4.6 and Open Problem 4.7, pp.11-12; Dimitrov--Xu https://arxiv.org/pdf/1606.05011v1 Theorems 2.5-2.6 and relevant proof, pp.5-6; Johansson https://arxiv.org/pdf/1802.07942v1 Sections 2-2.1, pp.2-3; Johansson https://arxiv.org/pdf/1806.06725v1 Section 1.2, p.4, and Section 1.4.2 (1.18)-(1.20), pp.12-13. Essential hypotheses/cases and local inputs are recorded below.
COMPARISON: Spatial concavity, a positive-definite Fourier Wronskian and the existing total identities do not state G_x(a)>=0. L604's pointwise remainder stop and C604b's negative total R do not decide G, which retains both the b integral and its positive layer allocation. L607 stops a generic implication, not this exact theta test. Numerical methods supply inclusion/error machinery, not a sign or a certificate for G.
GAP: All-frequency/all-a G positivity is unresolved, and no bounded witness has been calculated. The next covered experiment must establish explicit theta, derivative, weighted-tail, normalization and quadrature enclosures and check allocation admissibility; higher signs and effective global compensation remain independent.
REASON: The nomination lacked exact source comparison and certificate coverage. This first review now supports one bounded actual-theta negative-witness attempt; neither an identity nor a sign has been derived or approved in this literature-only step.
SCOPE: Source comparison of the unchanged proposed allocation and coverage for one bounded rational negative-witness calculation, as specified in the separate continuation assessment. No generic density search, whole-sign proof, higher-sign result or separate modular-block revival.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED target changed the signed allocation from C604b's applicability question; the old ready assessments did not cover this allocation or its numerical error requirements.

## Completed comparison, 1 November 2026

The main gap remains actual-Xi all-degree signs at unbounded heights.
The intermediate target is the proposed G below, for exactly C604b's
full-line density. A future sufficient first-sign argument could use
an admissible positive allocation; that assembly must itself be checked
in mathematics. Even a global first-sign success leaves independent
higher signs unresolved. This review proves no new allocation identity.

**Known results and their limits.** Reuse the inspected Stein identity,
weighted variance and hazard comparisons in
`2026-10-31-theta-stein-monotonicity-transfer-review.md` and the
actual-density application assessment
`2026-11-01-c604a-actual-theta-specialization.md`.
Their hypotheses have not changed. Saumard's Section 2 (5)-(6) requires
connected density support, finite first absolute moment, integrable
Stein tests and vanishing endpoint products; its Theorem 6 bounds a
variance, not this frequency-local allocation. No reproof is needed.

Reopened Csordas, *Fourier transforms of positive definite kernels and
the Riemann xi-function*, arXiv:1309.0055v2, 21 February 2014,
Theorems 4.5-4.6 and Open Problem 4.7, printed pp.11-12.
For his admissible theta kernel, associated kernels remain admissible;
all-degree positive definiteness is an equivalence, not a supplied
sign estimate. His 2014 first-Laguerre question concerns the total
transform. It is historical context, not evidence about the current
state of that question or this allocation. C604b/L605 retain the
coordinate k(u)=4 Phi(u/2), full-line normalization and imported
strict-tail/source-proof qualifications. No auxiliary squared-law
density can be substituted.

Newly inspected Dimitrov--Xu, *Wronskians of Fourier and Laplace
Transforms*, the PDF served at arXiv:1606.05011v1 (arXiv header
16 June 2016; manuscript footer 21 November 2021), Theorem 2.5,
its determinant/Fourier proof and Theorem 2.6, printed pp.5-6.
Theorem 2.5 requires f and t^(2n-2)f in L1 on the transform domain.
Theorem 2.6 states a positive-definite Fourier-Wronskian conclusion
for an even nonnegative measure with moments through 2n-1.
Those hypotheses fit smooth rapidly decaying densities, but the
conclusion is positive definiteness, not pointwise nonnegativity.
Neither theorem allocates a Stein layer at fixed a. No use of their
strict-positive-definiteness wording, general normalization constants,
or a new Wronskian specialization is made here. This was an unread
lead in the older layer assessment; it is now inspected for this
specific distinction, not imported as a sign theorem.

**Certified numerical support.** Johansson, *Numerical integration in
arbitrary-precision ball arithmetic*, arXiv:1802.07942v1,
22 February 2018, Sections 2-2.1, printed pp.2-3: the callback must
enclose the integrand on its entire input ball. The direct box rule
provides an inclusion on a finite real interval without an analyticity
claim. The faster Gaussian branch requires analyticity and a finite
bound throughout its complex ellipse. All regularity flags, poles and
branch cuts must be handled honestly. Requested tolerance is a goal;
the final radius is the evidence, including when evaluation limits
are reached. Neither branch supplies an omitted infinite tail.
This supports real interval subdivisions for both finite integrals
in G, with rigorous enclosures for their inputs; it does not guarantee
an efficient or successful certificate. No complex ellipse is needed
if only the direct box rule is used.

Johansson, *Numerical Evaluation of Elliptic Functions, Elliptic
Integrals and Modular Forms*, arXiv:1806.06725v1, 18 June 2018,
Section 1.2, printed p.4, describes ball propagation plus explicit
series truncation bounds. Section 1.4.2, (1.18)-(1.20) and Algorithm 1,
printed pp.12-13, bounds theta-series and z-derivative tails by a
geometric majorant, only when its denominator is positive. These
are supporting methods. Its z derivatives are not u derivatives
of k(u); a future implementation must either justify its coordinate
conversion or differentiate L019's summands and certify their tails
directly. No automatic derivative or truncation bound is imported
for k, h or tau. Reproof of the general numerical methods is unnecessary;
the exact local error/normalization specialization is still required.

For this specialization the narrowly read local inputs are L016's
uniform differentiated theta series, L019's exact positive summands,
and the complete-kernel Gaussian envelope in L564's proof (section
"A numerical envelope for the complete kernel"). L564 states the
relation of its Phi_R to L019's K; carry that factor before bounding
normalization and weighted spatial tails. No Hermite expansion is
needed. These provide existing convergence/envelope inputs, not yet
an evaluated error budget for G. Explicit finite-sum derivative and
tail constants remain work for the covered calculation. No new bound
is derived here.

The current FLINT and legacy Arb acb_calc documentation URLs returned
403. They are not evidence. The accessible primary integration paper
contains the necessary inclusion and analytic-branch cases, so this
does not block a direct-real-interval implementation. No installed
library, API availability or executable certificate was checked here.

## Search, duplicates and failures

Queries actually issued included:

- `"Stein kernel" "Laguerre" Fourier positivity theta`
- `"Riemann" "kernel" "integrated" "Laguerre inequalities" Csordas`
- `"theta" "Stein kernel" "layer"`
- `"Stein kernel" "Laguerre inequality"`
- `"Riemann" "Laguerre" "integrated" "kernel" positivity`
- `"Wronskians of Fourier and Laplace Transforms" Dimitrov Xu`
- `"theta" "Stein" "compensation"`
- `"Stein kernel" "partially integrated"`
- `"Stein kernel" "truncated Fourier" positivity`
- `Johansson rigorous arbitrary precision numerical integration 2018 algorithm analytic bounds`

No exact G theorem was located in this bounded search. Most exact Stein
allocation queries gave unrelated material. Growing-order and filtered
Hardy-positivity hits do not state a fixed-spatial-layer sign; their
theorems were not inspected in this review. They and other search
snippets supply no new mathematical input. No originality is inferred.

Read C604a/C604b and L605 completely; read L604's full hypotheses,
conclusions, layer/triangle assembly and absolute-convergence range.
Reused its already completed identity audit, without repeating it.
Read L607's hypotheses/conclusion and the generic and pointwise Stein
ATTEMPTS records; L607 is only a contrast, not a proof input for G.
Read the prior post-L607 three-candidate screen and layer assessment.
Scoped exact G/partially-integrated/allocation searches of November 1
literature/history and the relevant Stein stops found the nomination,
not an earlier calculation. The signed-allocation finite-grid script
did not match these Stein terms; it is not a certificate for G.
Initial broad outputs were truncated; only subsequent targeted reads
and the supplied snapshot are used as evidence.

The existing stops remain: L604 excludes a separate pointwise remainder
sign; C604b forces cancellation of total M and R; L607 refutes the
generic monotone-Stein implication. None evaluates the proposed sum at
fixed a for this p. This distinction licenses a bounded test, not a
claim to have overcome those mathematical obstructions. In particular
a different name for R_-<=M+R_+ would not provide a controlled estimate.

## Decision and continuation

EXPLORE covers a single negative-witness experiment, not global
positivity. Its exact target and certificate obligations are in
`2026-11-01-theta-integrated-layer-negative-witness-test.md`.
A rigorously negative enclosure rejects this allocation only; an
unsuccessful finite search establishes no global sign and does not
authorize a larger sweep without a refined mechanism. A failed error
budget must be reported as such. Preserve the floor in any assembly.

No lemma, mathematical script, DAG or PROOF edit was made. Full matching
and supporting Mathlib coverage for G and the numerical specialization
remain unchecked; L016 retains its existing supporting links. No
cross-notebook input is used. A bounded calculation is justified;
a creative first-sign proof attempt remains blocked by the absence of
an independently controlled signed theta estimate. The newly written
ready continuation is subject to separate next-turn approval.

## Original nomination (historical; review requirement discharged above)

## Proposed mathematical target, not an approved calculation

Use the exact full-line normalized p, h and tau of C604b. Retain
C604a's notation q=-tau', J_a, ell, M and L604's Delta and K_x.
The proposed quantity to investigate is

\[
 G_x(a)=q(a)J_a(x)^2+
        2p(a)\int_0^a[\tau(b)-\tau(a)]p(b)K_x(a,b)\,db.
\]

This formula only specifies the candidate test. No new integral
identity, bound, sign or counterexample is established by writing
it here. The intended allocation combines the two existing
representations before seeking a sign; source comparison must verify
its admissibility and usefulness. The possible floor ell F^2 must be
retained in any future assembly. Do not replace p by the auxiliary
density Phi(sqrt(s))/J, or discard any sine/cosine term of K_x.

One bounded discriminator to cover is a rigorously negative value
G_x(a)<0 at rational 1<=x<=64 and 1/16<=a<=4 for this exact p.
The box is a proposed search domain, not a mathematical assumption,
a certified threshold or a claim that a witness exists. If coverage
approves numerical work, a witness needs analytic or interval error
bounds for the theta sum, derivatives, weighted tail and b integral;
a floating-point preview is not evidence. No witness in that box
would leave the global sign unresolved and would not authorize
repeated searches without a refined mechanism.

The question differs from the previously recorded negative individual
K_x values: the smaller-variable integration and the allocated
nonnegative layer term are both retained. Conversely eventual R<0
alone does not decide the sign of their proposed sum at each a.
Compare these exact distinctions rather than rename the already
uncontrolled total inequality R_-<=M+R_+.

Main gap: actual-Xi all-degree signs at unbounded heights. This is
only a prospective sufficient mechanism for the first sign. Even
success would leave independent higher signs unresolved. Continue
to mathematics only after exact source/duplicate/obstruction coverage
is ready for this target; reject this allocation if a rigorous
negative witness is found. Full and supporting Mathlib coverage is
unchecked. No cross-notebook input is proposed. No new lemma or
script for this target was written during the C604b application.

The next turn is literature_comparison. A protected creative proof
attempt is not yet justified by an independently controlled signed
theta estimate; this nomination supplies a concrete test for an
allocation, not such an estimate. Missing coverage must be prepared
before choosing a mathematical task type or claiming a new mechanism.
