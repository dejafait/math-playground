# Single-quartet transform: independent detector nomination

TARGET: Test L994's two-component transform on the rational principal parts of one hypothetical off-line zero quartet, retaining both shifted branches, and identify a reachable nonremovable singularity or a concrete cancellation obstructing this detector.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse step285's bounded moving-band/Laguerre/Hadamard/Lagrange searches and exact local pole-response duplicate comparison in 2026-11-10-moving-band-finite-cluster-review-284.md; no inspected theorem states this two-component quartet detector. No novelty claim; newly prepared scope requires separate approval before research.
SOURCE_EVIDENCE: Step285 inspected DLMF1.10(iv),(vii),(viii) https://dlmf.nist.gov/1.10 ; Gessel1609.05988v1 Theorem2.1.1/(2.1.4), Theorem4.1.1 and residue proof pp1-3,22-23 https://arxiv.org/pdf/1609.05988v1 ; L994's cited DLMF18.12.13 supplies the unchanged Laguerre coefficient tool. Full citations and essential theorem cases are in review284's completed step285 section.
COMPARISON: Residue calculus, formal Lagrange inversion and local analytic inversion cover tools for a finite rational-input assay, with their hypotheses checked in the future specialization. They give no two-component noncancellation theorem, reachable singularity, actual-zero extraction or holomorphic actual complement. General Hadamard formulas are comparisons only, since a product identification is absent.
GAP: Establish the rational-input height limit and exact complete-quartet response, then exhibit a continuation path and local singular certificate surviving both contour integrations, or a precise cancellation/loss defeating the proposed detector. No response identity, candidate point or singularity is established here.
REASON: The full actual-cluster route has unpaid complementary-holomorphy hypotheses. A single finite rational principal-part input tests the proposed transform without those hypotheses; success could justify later work on the actual complement, while a cancellation would stop this detector. This is a target definition and pending nomination, not a derivation or approval in step285.
SCOPE: L994(4) with exactly its rho=1/4 w circle, Re(s)=1, n>=2, r=1,2, S branches and symmetric H limit; replace F simultaneously in both shifted branches by the rational function specified below. One symmetry quartet with positive integral multiplicity, no rightmost-zero, simple-zero, nonresonance or actual-complement assumption. General inversion theorems are imported without reproof.

## Exact target definitions, not asserted identities

Let eta=beta+i*gamma, 1/2<beta<1, gamma>0, and let m be a positive
integer. Define the four distinct points

    Q_eta={eta, conjugate(eta), 1-eta, 1-conjugate(eta)},
    P_eta(u)=-m*sum_(omega in Q_eta) 1/(u-omega).

These parameters describe a hypothetical off-line zeta symmetry
quartet. Their existence as actual zeta zeros is not assumed or
claimed. The negative residue -m matches a logarithmic derivative's
principal part at a zero of multiplicity m. The problem asks about
the response for this parameter class; exceptional values must be
stated and tested, rather than excluded as nonresonant.

Define I_eta,r,H by replacing only F with P_eta in BOTH occurrences
in L994(4), keeping its H_r, 1/s, w factors, orientation and contours
exactly. Seek the symmetric locally uniform limit near zero and call
it Z_eta,r only after proving existence. These definitions assert no
convergence, resummation, analytic continuation or decomposition of
the actual G pair. They prescribe no spectral cutoff or source-error
estimate. Actual J_r and -C_r remain in the actual problem; they are
not represented by a rational-input response or silently discarded.

## One bounded mathematical test after separate approval

First obtain the finite-input response with full multiplicities,
both shifted branches and every endpoint combination already encoded
in H_r. Use the inspected coefficient/inversion tools, checking
analytic convergence separately from formal coefficient equality.
Do not reprove the general residue or Lagrange theorems.

Test whether the PAIR (Z_eta,1,Z_eta,2) has at least one reachable
nonremovable singularity. A positive certificate must identify the
point, a path from the initial germ and a cut/punctured neighborhood,
with nonzero monodromy or a polar singular part for the complete
quartet sum in one component. Treat coincident contributions and
parameter exceptions explicitly. A singularity in an integrand,
an unselected inverse branch or an isolated summand is insufficient.
An informative negative must exhibit a concrete cancellation or
failed detector condition; failure of a crude bound proves no
impossibility. Save partial reasoning before lengthy work.

This is the creative part of the prospective mechanism: does joint
observation at r=1,2 prevent the transform from hiding a full symmetric
pole cluster? Merely evaluating the known inversion formula is a
specialization and must be reported as such. A genuinely new
noncancellation result would be only potentially new relative to
the sources checked, never an originality certificate.

Main gap: L030-L032/C032a positivity and L966/L968 signed forcing.
Plausible downstream use: a surviving finite-pole signal could guide
one later, separately covered actual-complement test. Even success
gives no singularity of actual G, no signed arithmetic estimate,
no L993 recovery, no L984(H) or RH consequence. Continuation,
other zeros, all jumps/compensators and height limits for the actual
complement remain unpaid; importing them requires another assessment.

Essential inputs: audited L994's exact kernel/contour definitions;
L985 only for its finite K identity; L989 only for endpoint conventions
if comparing coefficients with the actual problem. L990/C990a/L993
are downstream context, not premises. No cross-notebook input is used.
Preserve stop214's sign warning and stop284's closed approval loop.
Full matching Mathlib coverage is unchecked and unknown.

Recommended after separate approval: proof_attempt/creative,
deep_research/max. The obstruction is cancellation of an off-line
quartet after both integrations, which could make the proposed
actual signed detector blind. The bounded decisive test is the
complete-quartet local singular certificate, including exceptions,
or an explicit obstruction. This nomination leaves the actual
complement unresolved and does not approve its extraction.
