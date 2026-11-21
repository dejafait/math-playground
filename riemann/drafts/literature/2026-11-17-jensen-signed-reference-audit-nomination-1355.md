# C019f signed-reference audit: reused coverage nomination1355

TARGET: Critically audit C019f's uniform limit I_3/M_d -> 4^(1/3) Ai(-16*4^(1/3)*x/pi^2) on [1,4], including signed normalization, finite-tail completion, exact rational sign certificate and the same-sign endpoint obstruction, without changing q_e, radius, scale or arc orientation.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse completed assessment1354's exact finite-cubic/Airy search, local C019c/C019d/C019e comparison and stop1345; no new target hypotheses, general-theorem search or novelty claim. New C019f is the result to audit, not an independently verified source.
SOURCE_EVIDENCE: Direct primary URLs rechecked in recovery1356: https://arxiv.org/html/2610.38870v1 (28 October 2026), Lemma7/(3.11) and uniform implicit-function proof, Lemma12/(4.2)-(4.3) and exact gamma remainder, Lemma13 half-plane proof; https://dlmf.nist.gov/9.5.E1 ; https://dlmf.nist.gov/9.2.E1 ; https://dlmf.nist.gov/9.2.E3 ; https://dlmf.nist.gov/9.2.E4 ; https://dlmf.nist.gov/9.4.E1 ; https://dlmf.nist.gov/5.2.E1 . Applicability and qualifications below; parent assessment1354 retained.
COMPARISON: The new audit remains inside1354's exact hypotheses and approved coefficient/prefactor/tail/sign obligations. Standard Airy identities are imported; the finite degree-dependent specialization and rational implementation require independent replay. No matching source is asserted to prove C019f automatically.
GAP: C019f's new proof and script have not received a separate critical audit; check the two-stage uniform limit, growing positive quadratic term, signed prefactor, rational remainders and both orientations. This assessment supplies coverage only, not validation of their conclusions.
REASON: Recovery1356 repairs the reported missing-direct-URL process issue and completes separate literature approval for this unchanged conceptual-audit target. Parent coverage1354 is reused; no completed mathematics is rejected or newly validated. The next turn should perform the audit, subject to the supervisor gate.
SCOPE: C019f and its exact rational certificate on the unchanged x-window only; REPRODUCTION under SPECIALIZE. No changed endpoints, actual-polynomial uniqueness/simplicity, global hyperbolicity, foundational manuscript audit or RH claim.

## Applicability and bounded review

The essential notebook inputs are C019c and C019e, with C019d retained
upstream. The source expansion must be used for q-q_e(d), rather than
replacing the slowly varying edge by its limit. Inspect C019f's exact
coefficient formulas and the constant exponent against those inputs.
The finite cubic has a nonnegative quadratic real coefficient; an infinite
integral of that degree-dependent cubic is not a permitted shortcut.
The proposed proof uses a fixed-cutoff comparison and finite integration
by parts before taking the cutoff to infinity. Check each uniformity and
endpoint in that order.

For the signs, use `scripts/jensen-edge/signed_reference_1355.py` and its
full certificate. Replay the Gamma integral, its finite Taylor remainder
and positive tail, the Airy-series recurrence and geometric tails, and
outward rational interval operations. No decimal zero table or floating
approximation is an input. C019f's same-sign endpoint conclusion and two
interior simple reference zeros remain claims for this audit; they do
not establish simple or unique actual-polynomial roots.

Retain the limit and endpoint obstruction only if this complete audit
survives; repair a real error or preserve a failure if it does not. The
source evidence is sufficient for this test without new generic Airy
browsing. Source foundational validity, formal artifacts, effective onset,
full Mathlib coverage and global root transfer remain outside the result.
The original nomination is retained; recovery1356 supplies its separate source-coverage approval, not a mathematical audit.


## Recovery1356: direct-source verification and approval

This literature-only step responds to the supervisor's precise report,
“Ready assessments need a direct source URL.” The parent assessment1354
already contains those links. They are now explicit in this assessment's
SOURCE_EVIDENCE rather than only reachable by reference. No new theorem
search is needed for unchanged hypotheses.

On 2026-11-17 the primary Ono HTML was opened directly. The inspected
passages were Lemma7 and its near-edge analytic-parameter proof through
(3.11), Lemma12 and its exact remainder proof, and Lemma13 including the
Euler-product and logarithmic-derivative cases. These are the same inputs
as1354, with the same large-parameter, sector and local-interval
restrictions. Lemma13's local C1 conclusion must not automatically be
extended to the wider cubic arcs: the audit must check the actual
half-plane estimates used there. The manuscript's global claims and
formal artifacts have not been audited.

The DLMF pages were opened directly: 9.5.1 for the real improper
oscillatory integral; 9.2.1 and the entire-solution statement, 9.2.3–4
for exact initial values; 9.4.1 for the complex-variable series; 5.2.1
for Euler's integral with Re(z)>0. The NIST attributions to Olver1997
p53, p392 and p54 are reused; no direct book-page inspection is claimed.
Displayed decimal approximations do not supply interval certificates.
The prior DLMF release identification is inherited from1354 rather than
independently reverified here.

The inspected identities provide tools, not the finite perturbed cubic
limit, its signed prefactor, or its rational endpoint enclosures. The
needed specialization is still exactly the pending C019f audit, under
SPECIALIZE/REPRODUCTION. The growing real quadratic exponential forbids
a shortcut through an infinite degree-dependent cubic integral.
The duplicate and failure comparison remains1354's local comparison
with C019c/C019d/C019e and stop1345; no stopped automatic Airy import is
reopened. No new lemma, calculation, certificate replay or proof audit
was performed in this step.

Decision: coverage is sufficient for the unchanged saved audit, with
all original hypotheses and exclusions retained. Continue only with
claims surviving coefficient, signed-prefactor, finite-tail and exact
certificate scrutiny; preserve any failed bound. Mathematical validity
of C019f remains unresolved.
