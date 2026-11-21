# Odd-kernel two-point sign regularity: completed source review1709

TARGET: Assess source coverage and relevance for a strict common sign of the two-point minor of Im(kappa_(i*y)(sigma)) at y=1/8,1/4 and 1<=sigma_1<sigma_2<=2, comparing Gaussian total positivity with the actual nonlinear divisor kernel.
CHECKED: 2026-11-19
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1709 searched the exact nonlinear kernel, Gaussian strict total positivity/composition, complex shifts, univariate and multivariate preservers, and Chebyshev orthogonality; targeted local duplicate/failure checks and queries are recorded in drafts/literature/2026-11-19-odd-kernel-sign-regularity-source-notes-1709.md. No matching theorem was located and no novelty is inferred.
SOURCE_EVIDENCE: Inspected BGKP arXiv2006.16213v5 Proposition6.2/proof pp24-25 and Theorem4.1/order-two proof pp14-16; Damase-Khare arXiv2411.03391v2 Definitions1.1-1.2, Theorem1.6(2), Proposition3.3/Theorem3.2 proofs and order-two sufficiency pp2-4,12-14,18; Musin arXiv0903.1908v2 Section2/Theorem1/proof pp2-4. Exact versions, links and hypotheses are in source-notes1709; existing Gaussian-heat and duality coverage1532 is reused.
COMPARISON: Real ordered Gaussian composition and universal positive-real entrywise preservation do not cover this complex-divisor nonlinear kernel. C032l finite independence, C032n/stop1534 and C032o do not decide its ordered minor. Musin supplies a prospective continuous-density Chebyshev use beyond finite independence, conditional on later verification of the system hypothesis; it does not cover arbitrary signed measures.
GAP: The strict common minor sign on all ordered widths, its near-diagonal control and the subsequent kernel-specific Chebyshev application remain unproved. All-order regularity, constant approximation, unrestricted signed cancellation, positive output and Xi realization remain independent gaps.
REASON: Reject the automatic Gaussian-preservation import and nominate one full-divisor minor attempt with a qualified continuous-density downstream use; no determinant calculation or kernel theorem was made in this literature turn. The newly written continuation assessment requires separate approval.
SCOPE: C032m's fixed actual positive-ordinate divisor with multiplicity, conjugation, strip/counting and first-ordinate hypotheses; full closed width interval[1,2]; exact imaginary arguments i/8 and i/4; finite real signed width measures. Keep finite-zero, heat and fixed-v1 qualifications for probability-law use. No changed divisor, finite truncation, width-zero limit, optimized coefficients or cross-notebook input.
LITERATURE_REASON: This is a changed target with essential unread total-positivity/strict-sign-regularity coverage, not additional literature on ready gamma application1706 or audit1708.

## Completed review1709

The canonical source ledger for this review is
[source-notes1709](2026-11-19-odd-kernel-sign-regularity-source-notes-1709.md).
The negative evidence concerns the proposed automatic import, not the
actual minor sign or RH. One bounded kernel-specific attempt is nominated
in [minor-test1709](2026-11-19-odd-kernel-two-point-minor-test-1709.md),
with separate approval next turn. No lemmas, mathematical scripts, DAG
or main proof were changed. Full matching Mathlib coverage is unknown.

## Original nomination1708, preserved

The original nomination below describes the pre-review state. Its
unread-source instructions are superseded by the completed fields and
source ledger above; its mathematical scope and cautions remain.

### Exact prospective test, not a derived result

Use only the already defined kernel of C032m/q. Put

    k_sigma(y)=Im(exp(-E_sigma(i*y))*sinh(O_sigma(i*y))),
    D(sigma_1,sigma_2)
      =k_(sigma_1)(1/8)*k_(sigma_2)(1/4)
         -k_(sigma_1)(1/4)*k_(sigma_2)(1/8).

The possible later mathematical target is that D has one strict sign
for every ordered pair 1<=sigma_1<sigma_2<=2, or an informative rigorous
counterexample to that proposed sign regularity. This nomination proves
neither. A proof must handle arbitrarily close distinct widths and the
width endpoints. Finite grids, a fixed truncated divisor and unsigned
errors larger than the minor cannot verify it. Im makes k real by
definition; merely posing the test requires no unstated profile positivity.

The next turn is solely source comparison: search this exact family,
strict total positivity/sign regularity and Chebyshev-kernel terminology,
stronger applicable results and failures of preservation. Inspect primary
theorem hypotheses and essential preservation/failure cases. Gaussian
total positivity for real ordered translates must not be silently applied
to complex shifted zeros, an infinite divisor sum, integration in w or
nonlinear exponentiation. Reuse the existing scalar coverage; full
matching Mathlib coverage is unknown, not known absent.

Continue only if the review identifies a matching theorem with verified
hypotheses or a concrete missing difference admitting a bounded relevant
test. A strict minor is merely a first diagnostic toward an all-order
Chebyshev/approximation route for C032q's signed annihilator problem.
It does not imply that1 belongs to the kernel span, control arbitrary
variation, give positive output or realize Xi. The review must name a
plausible further structural use before approving a calculation; abandon
if this supplies only already covered finite independence or no supported
path beyond that diagnostic. No minor sign or relevance theorem is assumed.

Compare at most three mechanisms: gamma certification parked1708, direct
width-recursion stop1534 and this ordered-minor mechanism. The first needs
independent enclosures and a positive margin; the second needs new scalar
closure information. Preserve all stops. This REVIEW_REQUIRED nomination
approves no mathematics; a later research turn needs a preexisting ready
assessment for its exact target. No protected creative attempt is justified
before the essential source comparison. Do not manufacture an all-order
claim from a finite test or relabel routine specialization creative.

Main gap remains actual-Xi all-degree positivity, H_d=o(d) and S_F=0.
Essential input IDs for this source review are C032m/q/n/l/o; C033d is
only a contrast with the parked route. All actual-divisor, multiplicity,
conjugation, strip/counting/first-ordinate and probability-law finite-zero,
heat and fixed-v1 qualifications remain. No cross-notebook input, new
lemma, determinant calculation, primary theorem import or mathematical
script was made in this nomination.
