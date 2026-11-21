# Independent review of the combined-origin proof1624

TARGET: Critically audit C048b's fixed-height straight-ray identity and full-sector bound |E_o(p)|/|S(p)|<10^9 L^(5/2) sqrt(r) exp(-r/32)<10^-4 L^(9/2)/r, checking meromorphic continuation, complete-mode constants, negative real parts, all junctions, reflection and zero height; validate the proof or identify a specific gap without expanding to other saddle terms.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse unchanged component coverage1623 and its exact-target, duplicate and failure comparisons; step1624 narrowly searched existing Mellin assessments/stops and compared C048a/L804/audit538. No fresh discovery search or novelty claim. The changed proof uses standard Cauchy deformation and Taylor continuation already within that approved scope.
SOURCE_EVIDENCE: Kawano, Preprints.org202611.0383v1, posted4November2026, https://www.preprints.org/manuscript/202611.0383/v1 , (25)-(26), (28), AppendixB origin cases and AppendixC combined-origin allowance; exact cases were inspected in1623 and the relevant primary paragraphs rechecked in1624. C048a supplies fixed-height contour continuation and branch facts; Cauchy coefficient formula DLMF1.9.30-31 and the Gaussian integral support the elementary estimates. No supplement premise is used.
COMPARISON: C048b reproduces the source allowance with a straight-ray representation of the combined contribution, a relaxed cos V>1/(4L) clearance, only the first coefficient bound, and an explicitly stronger prefactor. L804's differently normalized endpoint inequality is not imported. The intended review checks the full new implementation, not a repeated source search or automatic transfer of its bound.
GAP: Independent verification of C048b's changed contour and uniform constants remains pending; other saddle terms, full (29), zero counts, inversion and the actual-Xi sign bridge remain outside scope and unresolved.
REASON: A conceptual audit is justified by the new meromorphic path representation and its use across negative real parts and zero height. Prior essential source coverage is adequate; the nomination is ready for the supervisor's separate next-turn approval, not an additional mathematical attempt in1624.
SCOPE: Separate literature approval completed in step1625; exactly TARGET and C048b's stated sector, kernel, E_o and S are ready for RESEARCH / proof_audit / conceptual_audit / REPRODUCTION. C048a is the sole direct mathematical input; L804 is comparison and method history only. Full matching Mathlib coverage remains unchecked/unknown.

The exact intended allowance is already in the inspected primary source.
The review must check the complete canonical proof rather than treat
its scratch derivation or its stronger displayed prefactor as verified.
In particular, fix the height before the identity theorem, keep the
original finite vertical segment inside the path equality, and verify
the signs of both real-part phase comparisons. The small-height case
uses an integrable power rather than a singular pointwise bound.

Continue on a complete proof or a specific correctable defect; if the
proof fails, distinguish a failed sufficient estimate from a false
actual contribution bound. Do not reopen the stopped global import
without its independent analytic and signed hypotheses. No independently
specified central signed mechanism follows from this paid component;
that is the blocker to creative routing, not a ban on future discovery.


## Separate coverage approval — step1625, 18 November 2026

This is a literature-only approval of the unchanged exact target. Reused
assessment1623 and its complete source extraction; read C048a and the
complete C048b solely to identify essential source coverage and scope,
without auditing their inequalities or deriving a new result. Checked
history538 and the global-remainder import stop: L804's endpoint
normalization differs, and the global uniform saddle/sign obstacles
remain independent. Neither is a reason to reject this component review.

LITERATURE_REASON: The supervisor requires separate approval of the newly written assessment1624; this step checks coverage for its changed straight-ray implementation, without reopening discovery or repeating the prior mathematical attempt.

Primary spot checks used the same v1 URL (which redirects to the
unversioned page still labeled Version 1), Appendix C opening hypotheses
and its two combined-origin paragraphs immediately before C.1.
They match the sector and allocation extracted in source-notes1623.
The preprint remains a claim under review, not independent proof of
C048b or the rest of its conclusions. No archive/supplement is essential
for the independent proof now written; none was retrieved.

For the changed contour, additionally inspected
[NIST DLMF 1.9(iii), (1.9.29)-(1.9.31)](https://dlmf.nist.gov/1.9#iii).
Cauchy's theorem requires analyticity inside the closed contour and
continuity on it; the coefficient formula additionally uses positive
orientation and an interior evaluation point. Thus it applies only
after removing the zero vertex and checking the selected logarithm
branch. C048b must verify the vanishing removed arc initially for
Re(p)>0, then continue at fixed height, retaining the entire original
finite vertical segment. Standard continuation coverage is reused from
assessment1623 and its inspected endpoint-scope534 comparison (Zagier,
Mellin appendix Section 1, and DLMF 1.10.18-19); no moving-height
analyticity is supplied by those theorems. These are audit obligations,
not conclusions reached here.

The full proof is available for the next turn: C048b sections 1-2
contain geometry and complete-kernel bounds, section 3 the new path
identity, sections 4-5 normalization and signed phase comparisons with
all junctions, and section 6 the allocation. No essential unread source
case was identified within this unchanged scope. The exact SPECIALIZE
assessment is approved for one independent conceptual audit; this
approval does not verify C048b or advance the actual-Xi sign gap.
Full matching Mathlib coverage remains unknown.

Outcome STALLED: approval adds no new mathematical or route-changing
source evidence to the already adequate assessment. This is one required
literature gate completion, not an advance or a renewed exploration
budget. Next is the saved mathematical audit, with no further literature
turn needed unless its assumptions change. Continue on a complete audit
or an explicit defect, distinguishing an estimate failure from a false
allowance. The absence of an independently specified central signed
mechanism still blocks creative routing here; no new mechanism is
invented for scheduling purposes. No lemmas or mathematical scripts
were changed. Existing unfinished reasoning is preserved.
