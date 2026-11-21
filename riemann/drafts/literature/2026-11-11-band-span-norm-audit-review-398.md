# Nomination for critical audit of the coupled-span norm obstruction

TARGET: Critically audit C997z's exact band-span witness, centered-derivative noncancellation and complete-window norm lower bound, including its limited implication for representing measures.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Step399 reuses the completed exact-target searches and primary derivative/Remez comparisons in review395/step396 and review396/step397; narrowly inspected C997c(4)-(6), C997s hypotheses, C997y(8)-(13) and its step395 audit, the full proposed C997z proof, C997f/w contracts and stops340/341/393/398. No new exact-match search or novelty inference.
SOURCE_EVIDENCE: NIST DLMF https://dlmf.nist.gov/18.14.E8, equation18.14.8 and its real-x, alpha>=0 hypotheses, accessed 2026-11-11, with attribution to Koornwinder(1977), Remark4.1; reused audited C997c(4)-(6) and C997y(8)-(13). Primary derivative-theorem contracts/proof cases already read in review395 and recovered in review396/step397 are reused without importing them.
COMPARISON: Existing coverage suffices to audit this explicit actual-span lower-bound proof: the only special-function estimate is the unchanged real Laguerre input. Generic derivative/Remez upper estimates and Hahn-Banach/Riesz do not supply its noncancellation or rate. C997f/w concern different objects; the scalar, annihilator and spectral-tail stops do not settle this witness.
GAP: No essential source blocker remains for the nominated audit. C997z noncancellation, constants, exact column membership and the limited measure implication remain mathematically unverified; this literature approval verifies none of (2)-(4). Full matching Mathlib coverage remains unknown and unchecked.
REASON: Separate coverage approval for the unchanged nominated audit is complete in step399. EXPLORE authorizes one conceptual audit of the written proof, without treating the operator-specific result as a known theorem import or approving new mathematics in this literature turn.
SCOPE: Original n>=64, I=[7/4,9/4], z_star=1+i/8, gamma_j=15/8+j/(4n), m=ceil(sqrt(n)), C997y(13), both beta terms/windows, exact endpoint coupling and actual complex TV. No new positive construction, coefficient-cap replacement or RH claim.

The separate approval may reuse existing primary coverage because the
Laguerre bound and germ formula have unchanged hypotheses. First check
that this coverage and the elementary finite identities suffice; an
essential new source hypothesis would require explicit review. At nomination this
file was REVIEW_REQUIRED; the separate coverage approval below now
authorizes the nominated audit, without carrying it out.

For the nominated audit, essential local inputs are C997c, C997s and
C997y. Check C997z's binomial frequencies and phases, coefficient sum,
lower-window retention, all-slope upper bound, the labeled-derivative
partition injection, every falling-factorial factor, the m-dependent
absolute error and the cancellation of m! in the germ formula. Check
that the witness is nonzero, that the complex pairing is bilinear, and
that the rate is an actual norm lower bound, not a poor upper estimate.
The decisive test is whether (2)-(4) hold uniformly for all n>=64 and
contradict the original <1/64 upper rate without an enlarged span.

If a flaw defeats the rate, preserve the proof and identify the precise
repair needed; do not treat a failed upper certificate as an obstruction.
If the proof survives, retain only the exact-functional stop. The capped
E_n, approximate representation with paid leakage, C997a(8), selected/
both-sign transfer, assay/reconstruction, complements/regulators, L993,
L984(H), L966/L968 forcing and actual-Xi signs remain unresolved.
No cross-notebook input, new external theorem or mathematical script
is part of this nomination.

## Separate coverage approval — step399, 11 November 2026

This is LITERATURE / NOVELTY_UNCHECKED; actual task literature_comparison.
LITERATURE_REASON: Step398 nominated a new conceptual-audit target with
REVIEW_REQUIRED; this turn supplies its mandatory separate source gate,
rather than repeating literature on the prior ready construction target.

The main gap remains actual-Xi positivity and the unpaid forcing/H
bridges. The intermediate target is exactly the TARGET above. Its
plausible downstream use is to decide whether the exact centered-moment
measure route should remain parked; it would not settle the capped E_n.

Read the complete C997z proof to identify its source obligations, without
replaying or accepting its new finite partition estimate. Its external
special-function input is DLMF18.14.8: for nonnegative integer degree,
real x>=0 and alpha>=0, exp(-x/2)|L_degree^(alpha)(x)| is bounded by its
value at zero. The proposed application has degree n+1 and alpha=2,
with real nonnegative t on both windows, so its hypotheses have unchanged
scope. The constant subtraction is handled in the already audited local
C997c input; no complex-t extension of this inequality is authorized.
The DLMF statement and attribution were read; Koornwinder's complete
original proof was not newly retrieved. Import the named DLMF equation
through that local input, without reproving the Laguerre inequality.

C997y's fixed-parameter integral and reciprocal germ are already audited
in step395. Its exact formulas (8)-(13), rather than its stopped scalar
continuation rate, are the relevant contract. For the proposed audit,
finite linearity and the identity theorem must be checked where C997z
uses them on arbitrary band combinations. Neither a new global inverse
estimate nor a quantitative Hahn-Banach application is needed. The
measure conclusion uses the defining total-variation inequality only;
no existence or minimal-cost representation theorem is imported.

C997f's binomial modulates a slope density, and C997w interpolates a
target-minus-band residual without a cap. Their contracts do not cover
the present band-only witness. Stops340/341 leave a target spectral tail
unpaid; stop393 concerns a global scalar prior. They remain recorded
and do not supply the missing cancellation audit. Reuse the primary
comparison in reviews395/396; re-browsing those derivative papers would
not verify the new elementary calculation. No exact matching theorem
or originality claim is established by this scope review.

The finite binomial expansion, labeled Leibniz rule and elementary
sine/exponential estimates require proof replay, not a new literature
import. In the next turn independently test (2)-(4) for every n>=64:
check frequency phases and coefficient mass, the complete lower and
upper supports, the partition injection and falling factorials, the
uniform m-dependent error, and factorial cancellation in (12). Retain
the local stop only if this proves a true norm lower bound at the stated
rate. Otherwise preserve the derivation and identify the precise flaw
or required repair. Do not convert an insufficient upper estimate into
a norm obstruction or treat the band witness as a capped residual.

Essential inputs remain C997c, C997s and C997y; C997t/f/w are comparisons.
No cross-notebook input, new lemma, mathematical script or proof verdict
was produced. C997a(8), selected/both-sign transfer, assay/reconstruction,
complements/regulators, L993, L984(H), L966/L968 forcing and Xi signs
remain unresolved. Full matching Mathlib coverage is unknown, unchecked,
and not required to begin this informal conceptual audit.
