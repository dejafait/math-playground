# Adjoint heat transfer for the regular difference weight — review1846

TARGET: Review source coverage for transferring spatial derivatives onto C034c's regular difference weight Q_2-Q_1 to control its joint curvature against S4^3/5 on [1,2], including every origin boundary term.
CHECKED: 2026-11-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed source-notes1846 records exact adjoint, signed-covariance and Gaussian-rational searches, the full half-line boundary proof case, and local overlap/stops1839/1843. No matching quantitative joint-curvature theorem was located; no originality or impossibility claim.
SOURCE_EVIDENCE: Nonnenmacher, Introduction to Spectral Theory, September2021, Example3.1.12 and full proof p29, https://www.imo.universite-paris-saclay.fr/~nonnenma/enseign/Spectral%20Theory%202021%20chap1-4.pdf ; NIST DLMF1.2.8, 7.2.3, 7.7.1-2, 7.10.2-3 and 7.19.1-4, https://dlmf.nist.gov/7.7 and https://dlmf.nist.gov/7.19 . Reuse source-notes1842's Nolen/Haslinger/Ruzza/Zucca hypotheses rather than reprove them.
COMPARISON: Half-line selfadjointness requires H2 with Neumann trace and L2 pairings; those hypotheses are not established for the complete divisor profile. DLMF supplies Gaussian-rational identities and derivatives, not a signed two-copy bound. Existing C032n majorants support a later cutoff specialization; neither generic source nor integrated d_j>0 signs the joint curvature.
GAP: Derive and justify the specific adjoint transfer, preserve the normalization and all cutoff/origin terms, treat Q_1 only in its subtracted expression, and test an explicit joint estimate against C034c(20). No such specialization or estimate is derived in this review.
REASON: Missing comparison coverage for the changed adjoint mechanism is now supplied. One bounded full-divisor transfer test is justified as EXPLORE, not IMPORT; a newly written mathematical continuation is separately nominated in assessment1846 for approval next turn.
SCOPE: Literature-only completion of the saved review target. Sources cover the proposed analytic tools, not the desired inequality, complex-shift substitutions or finite-zero validity. No mathematical result is certified by the decision.

## Completed comparison1846

See [source-notes1846](2026-11-20-laplace-adjoint-difference-source-notes-1846.md)
for exact source statements, versions, proof cases, applicability limits,
queries and the bounded decision. The review completed source coverage;
it did not apply the sources to prove a new adjoint identity or sign.
The precise mathematical nomination is
[assessment1846](2026-11-20-laplace-adjoint-difference-attempt-1846.md).
Its separate approval belongs to the following invocation.

## Original nomination1845 (historical; preserved)

The main gap remains L030-L032/C032a actual-Xi all-degree positivity.
C034c's cubic payment is now audited but its sufficient curvature
threshold (20) is unpaid. The proposed intermediate target retains
that threshold and attempts to exploit the already explicit regular
difference weight before estimating the full determinant. An effective
bound could settle the final ECT prefix, supporting qualitative
mass-plus-two-observation interpolation. Conditioning, exact weights,
TV<=2, full observations, signed height, cancellation and actual-Xi
realization would remain independent.

The discriminating question for the source review is whether an adjoint
heat estimate has hypotheses compatible with this signed complex divisor,
the origin subtractions and both widths' endpoints, and supports an
explicit joint bound to compare with S4^3/5. Retrieve exact theorem
hypotheses and relevant proof cases first. A generic heat identity or
another unsigned independent jet bound alone is insufficient. If the
approach requires an unproved profile sign, an omitted boundary term or
the same unpaid correlation sign, document that obstruction and park it.
An absent matching theorem is not proof of impossibility or novelty.

This is independently testable through the adjoint rational weights and
their absolute full-divisor bounds. No such weights, their signs or
boundary identities were calculated during audit1845. Preserve the
pointwise stop1843 and full-prefix stop1839, together with the referenced
stops1746/1798/1823/1832/1837. Their restrictions do not rule out this
different estimate, and they are not being waived.

Essential inputs are C034c and C034b, with C032n's heat/interface
estimates and C032m's regularity. The probability interpretation retains
C033w through C033l/C032q: actual divisor, conjugation and multiplicity,
excluded ordinate zero, strict strip/gamma>14, count, verified through100,
retained real zero, reciprocal-square tail, heat positivity and separate
fixed-j errors, both fixed-v1 qualifications, zero drift and killing,
and Gaussian half-variance. No source-wide or finite-zero verification,
full matching Mathlib theorem, spatial positivity or score division is
available from this nomination. No cross-notebook input is proposed.

No source-supported new central signed-height or realization mechanism
is currently identified in the inspected continuation material. This is
a local curvature-source comparison, not a creative central-gap claim.
If its coverage becomes ready, nominate the precise mathematical test
for a later invocation; do not derive and approve it during the review.
