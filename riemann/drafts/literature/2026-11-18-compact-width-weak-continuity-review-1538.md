# Compact-width laws: continuity source review completed1539

TARGET: Review whether C032m's continuous positive-ray Laplace transforms imply weak continuity of sigma -> nu_sigma on [1,2] and Borel measurability of sigma -> nu_sigma(A) for every Borel A in [0,infinity), using a probability Laplace-continuity theorem.
CHECKED: 2026-11-18
DECISION: IMPORT
SEARCH_EVIDENCE: Fresh primary-source search and scoped duplicate/failure comparison completed in step1539; queries and access outcomes are in drafts/literature/2026-11-18-compact-width-weak-continuity-sources-1539.md. No novelty claim is made.
SOURCE_EVIDENCE: Inspected Mimica2015 Corollary2.2/proof p13 and Theorem2.1/proof pp11-13; Tropp2024 Theorem17.22/p260 and Theorem17.39/proof p268; Fritz-Perrone-Rezagholi1910.03752v3 Definitions4.1/4.6 and Propositions4.7/4.10 with proofs pp41-43. Notes1539 give complete citations, qualifications and read/unread boundaries; C032j/k/m coverage is reused.
COMPARISON: The required general probability and Borel evaluation tools are known and cover this contract subject to ordinary local applicability checks. They supply the previously missing interface; Haslinger's scalar integration theorem alone did not.
GAP: No family-specific application is performed here. Check probability/support qualifications, zero normalization, limiting-law identification, sequential transform convergence including width endpoints, the half-line topology and the evaluation theorem's space hypotheses in a later audit.
REASON: Missing essential source coverage is resolved through inspected primary alternatives; the broader signed-cancellation problem is untouched. A new ready applicability nomination is saved for separate next-turn approval, without deriving and approving it in this turn.
SCOPE: sigma in [1,2]; C032j's probability measures nu_sigma on [0,infinity), with all fixed-v1 qualifications; Laplace transforms exp(-B_sigma(s))=exp(-b_sigma(sqrt(s))) for real s>0; arbitrary Borel A. No density, RH, signed-mixture nonnegativity or exponential moments are assumed.

## Completed source review1539

The inspected results and essential proof cases are recorded in
[notes1539](2026-11-18-compact-width-weak-continuity-sources-1539.md).
Their general conclusions need no new proof; the qualified family
still needs the applicability audit nominated in assessment1539.
This is local source progress, not progress beyond those theorems or
toward an actual-Xi sign. PROOF/DAG and all lemma files are unchanged.

## Historical source nomination1538 (preserved)

The following text records the previous missing-coverage state and
its discriminator; its source-review request is completed above.

Retrieve a primary statement and essential proof of the probability
Laplace-continuity theorem on [0,infinity), including its normalization
at zero and tightness hypotheses, then the weak-topology Borel
evaluation theorem or its standard measure-theoretic proof. A named
unread theorem, search snippet or a repeated attempt to fetch the
oversized MIT book is insufficient coverage. Check relevant duplicates
within the already named compact-width/smoothed-law paths.

The proposed discriminator is whether these statements cover C032j's
probability laws and C032m's continuous positive-ray transforms for
every convergent width sequence, including both endpoints. If they do,
import the matching theorem and approve only the necessary applicability
argument. If they need an unavailable extra moment, density or stronger
uniformity, record that exact gap and park this target. Do not derive
the application during the source review.

This is materially different from the stopped direct transform test:
it concerns weak convergence of already existing positive laws, rather
than representing the nonlinear odd kernel as a compact-distribution
transform or extracting an endpoint from signed cancellation. The
broader kernel question was recorded in1527/1528; the new input is
C032m's completed and audited continuity, and the proposed tool is
probability Laplace continuity, not the previously inaccessible source.

Plausible downstream use: a verified Borel kernel would permit defining
finite signed width mixtures as measures before asking about their
positivity and moments. It does not settle mass-one cancellation of
J_eta, construct a positive mixture, identify an unsmoothed actual-Xi
law or pay L030-L032/C032a's all-degree positivity. Those are independent
gaps. C032o and finite stop1302 are contrasts, not mathematical premises.

No creative central-sign mechanism is justified by this audit alone:
neither an estimate for Q(q) nor a sublinear reciprocal-Jensen height
bound has emerged. Do not label this standard continuity specialization
creative to satisfy routing aims. Full Mathlib matching coverage remains
unknown. This nomination approves no mathematics; the next turn is
literature-only because the essential theorem coverage is missing.
