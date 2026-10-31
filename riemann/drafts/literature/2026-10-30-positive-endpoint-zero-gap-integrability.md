# Positive-endpoint zero-gap integrability — source comparison

TARGET: Review Csordas–Smith–Varga's zero dynamics and Rodgers–Tao's localized interaction estimates for an inverse-square gap integrability bound up to a positive collision time in the actual theta heat flow.
CHECKED: 2026-10-30
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Queried Csordas Smith Varga 1994 zero dynamics, Lemmas 2.1/2.2/2.4, coalescence and Lehmer-pair PDFs; checked the exact local heat-route failures. Located the cited 23-page paper and author-uploaded mirror, but neither yielded inspectable text or images. Search excerpts are leads only. Detailed access and comparison evidence: drafts/heat/2026-10-30-positive-endpoint-source-comparison.md.
SOURCE_EVIDENCE: Read Rodgers–Tao arXiv:1801.05914v3 Theorem 4.1 and citation to CSV Lemmas 2.1/2.4, Lemma 4.2 including its convergence and finite Hamiltonian proof, Proposition 5.1/Lemma 5.2 and Proposition 6.1 with proof; read Section 7 definitions (62)–(69), Lemma 7.1 and Theorem 7.2 statement. CSV Constr. Approx. 10 (1994), 107–129, DOI 10.1007/BF01205170 is identified, but its essential collision proof remains unread.
COMPARISON: Rodgers–Tao gives integrated inverse-square control only away from Lambda under Lambda<0. Proposition 6.1 uses the lower-endpoint Hamiltonian bound from Proposition 5.1; the finite identity retains exterior interactions. Section 7 renormalizes the energy but keeps the time margin. These inspected results do not supply the requested positive-endpoint bound. Indexed CSV passages suggest dynamics for all t>Lambda, including positive t, but do not establish endpoint control and are not imported.
GAP: Essential CSV collision/simplicity and convergence cases cannot be inspected in this interface. Even the fully inspected Rodgers–Tao Proposition 6.1 does not license a uniform lower-endpoint limit or positive-time extension. No actual-theta remainder meeting the proposed integrability threshold was identified.
REASON: Park direct source application: newly inspected proof shows an explicit lower-endpoint gap/Hamiltonian dependence, while the older essential proof remains inaccessible. This is source-level negative evidence, not a disproof of the requested bound or an RH advance. Continue with an independent high-height positive-time source question, not repeated scan-access attempts.
SCOPE: Source review only for actual theta heat flow, an isolated finite-height neighboring real-zero pair on a one-sided interval above a putative positive endpoint, and integrability as that endpoint is approached. No derivation, all-height collision exclusion, RH assumption, strengthened zero-free premise or new generic energy comparison is authorized.
LITERATURE_REASON: Essential primary zero-dynamics proof coverage was explicitly left unread; positive-time endpoint control of inverse-square zero gaps is outside the previous finite-polynomial and negative-energy assessments.

## Named gap and bounded source test

The main gap is actual-Xi all-degree positivity. A possible independent
intermediate input is quantitative control of an approaching real-zero
pair in the actual theta heat family. If source-supported estimates
distinguish that family from generic colliding heat polynomials, they
could motivate a later collision-exclusion test. This nomination proves
no such distinction and does not turn a finite-height assertion into RH.

Use L058's exact heat convention after reading its hypotheses, and L018
for its relation to actual Xi. Write g(lambda)>0 for the separation of
a selected neighboring real simple pair for lambda in
(lambda_*,lambda_*+delta], where lambda_*>0 and delta>0. The proposed
threshold to compare with sources is

    sup_(0<epsilon<delta)
        integral_(lambda_*+epsilon)^(lambda_*+delta)
            g(lambda)^(-2) d lambda < infinity.

This is a requested bound, not an asserted estimate or an established
collision criterion. Simplicity at lambda_* may not be assumed. If
a source uses a different normalization or a weighted/renormalized
energy, retain its exact formula and determine whether it controls
this particular unweighted pair term. A source asserting only bounds
on closed subintervals separated from lambda_* does not meet the test.

Start with the exact Csordas--Smith--Varga reference behind
[Rodgers--Tao v3, Theorem 4.1](https://arxiv.org/html/1801.05914v3).
Read the primary theorem's hypotheses and essential convergence and
collision cases before larger extracts. Reuse the
[existing source comparison](2026-10-30-backward-heat-negative-energy-coverage.md)
for the already inspected conventions and the fact that the displayed
Rodgers--Tao time interval does not include a positive endpoint.
Inspect whichever localized interaction estimate actually controls
the proposed quantity; do not replace a cutoff identity by the formal
untruncated sum. Check exact-statement and stronger-result coverage
and recorded obstructions before approving any mathematical attempt.

Continue only if the primary results provide an applicable bound or
identify a concrete, independently testable actual-theta remainder
whose control could reach the displayed threshold. Otherwise record
the time-domain, separation or nonintegrable-endpoint loss and park
this direct source application. Do not manufacture an endpoint
extension from real-simple-zero evolution in an open interval.

L487's generic bounded backward negative-D_1 comparison remains
obstructed. The
[heat-route stop](../../ATTEMPTS/2026-09-20-heat-fourier-relevance-audit.md)
also retains L126/L128's local-to-global limitation: finite-height
motion cannot control a whole-plane zero-height supremum. Even an
applicable pair estimate leaves simultaneous/higher collisions,
escape to infinity, uniform height bounds and all initial signs
unresolved. These are limitations, not assumptions to suppress.

The preceding nomination is preserved as the exact test reviewed. The
completed review does not approve mathematical work on it. See the
source-comparison note for the inspected endpoint dependence and access
failures. Full matching Mathlib coverage is unchecked. No theorem was
imported, no collision estimate was derived, and no lemma/script changed.
