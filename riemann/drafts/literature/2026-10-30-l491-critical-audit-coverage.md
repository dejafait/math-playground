# L491 explicit gamma-log certificate: proposed audit coverage

TARGET: Critically audit L491's source-branch center expansion, conjugation and uniform gamma-log bound on the full stated domain.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Separate approval completed 2026-10-30; reuse drafts/literature/2026-10-30-explicit-gamma-log-linearization.md and drafts/heat/2026-10-30-explicit-gamma-phase-source-review.md for the same explicit-model scope and local duplicate/failure checks; no broader search or originality claim is made for a proof audit.
SOURCE_EVIDENCE: Directly rechecked Polymath arXiv:1904.12438v2 (4 August 2019), https://arxiv.org/html/1904.12438v2 , (7),(9),(10),(42),(43),(75)–(76),(100), Lemma 9.2 and its proof inspected; source (76)'s constant conflicts with (9), so L491 uses independently derived elementary bounds instead.
COMPARISON: The source supplies the exact logarithm/derivative identities and qualitative phase/variation model; L491 makes the constant effective with a full-domain elementary proof, and an audit must replay it rather than import the invalid (76) or unspecified O-constant.
GAP: Independent verification of L491, including its rational countercheck of source (76), the exact branch constant, center/time normalization, lower-half-plane conjugation, disk derivative and unbounded-height comparison.
REASON: This bounded audit is needed before relying on the new numerical component in a strict contour comparison; it supplies neither a new model nor a real/simple tail by itself.
SCOPE: Approved for the exact TARGET after this separate literature turn. Only L491 and its explicit-formula/rational inputs; no source saddle audit, residual reflection, zero count, exhaustion, collision exclusion or zero-time transfer is covered. Newly written continuation requires separate approval next turn.

## Inputs and bounded test

Read the canonical L491 proof, with its definitions and full closed
domain. Replay the formula-(7) branch at (1+iX)/2, including the
identity Im(Log(s)+Log(s-1))=pi and the real 1/4 leading logarithm
correction. Check the source-(9) discrepancy by exact fractions and
check the replacement alpha bound for every 0<=sigma<=1, x>=200.
Verify both disk images, conjugation, the signs in G_t', the time
factor, segment integration and monotonicity through all X in the
domain. Inspect the complete relevant arithmetic certificate; it
checks rational arithmetic only and cannot certify analyticity.

Essential external inputs are source identities (7),(9),(10),(42),(100)
and elementary principal-logarithm facts; no other local lemma is a
mathematical premise. L488 and L490 are downstream context only.
The arithmetic certificate is reproduced with
`python3 scripts/heat/l491-arithmetic-certificate.py`.
An independent audit must accept or identify a failing inequality
in the bound (log(X/(4*pi))+20)/X<5010/10^12<1/100 on the full domain;
samples cannot pass. On failure, retain the failing step before
changing the claimed bound. Success still leaves strict counting,
normalization of the reflected residual, exhaustion, edge transfer,
collision exclusion and zero-time control unresolved.

This assessment approves a routine proof replay with unchanged
explicit-model hypotheses; the mathematical audit is not completed. The source
discrepancy is new evidence requiring this refreshed comparison and
separate approval, now completed; the old assessment is retained as evidence of the
completed calculation's gate. Full matching Mathlib coverage unchecked.

## Separate source-coverage approval, 2026-10-30

The exact target is retained. Direct primary-source inspection checked
(7)–(10), (42)–(43), the proof immediately preceding (75)–(76),
and all of Lemma 9.2's proof through (101), at the linked v2 above.
The domain of (7) is C minus (-infinity,1]; (43) requires Im(s)>3.
Lemma 9.2 assumes 0<t<=1/2, a sufficiently large positive center and
bounded displacement; both its conclusions retain unspecified error
constants. It therefore supplies the model, not L491's numerical bound.
Its proof treats local variation and center phase separately. These
are both essential cases for the audit, with the fixed branch (7).

The printed (76) and its preceding estimate were located directly;
the conflict reported in L491 is not an artifact of the local source
notes. No independent rational or analytic replay was performed here.
The audit must check that conflict and the replacement estimates from
(9); it must not silently import (76). The definitions and derivative
identities are accessible without any saddle theorem. Reading the
entire canonical L491 for scope found no additional essential external
input beyond those listed here and elementary logarithm facts.

The prior search/overlap assessment and its recorded queries remain
adequate for this unchanged audit. Local scope comparison additionally
read history/2026-10-30-explicit-gamma-log-linearization.md and
ATTEMPTS/2026-10-30-direct-numerical-tail-extraction.md and
ATTEMPTS/2026-10-30-tail-approval-loop-recovery.md. These distinguish the
new constant check from the stopped direct extraction of an unspecified
tail cutoff and from repeated audits with no remaining target. L491's
first independent audit is still outstanding. No claim of novelty or
new mathematical result follows from this approval.

Disposition: SPECIALIZE is ready for the exact TARGET next turn.
Accept only a full-domain analytic replay plus complete relevant
arithmetic evidence; otherwise preserve the exact failure before any
repair. No additional approval loop is needed for unchanged coverage.
Mathlib coverage remains unchecked. Counting, exhaustion and collisions
are excluded from this approval and remain unresolved.
