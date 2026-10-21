# Mixed product Weitzenböck result — critical-audit coverage

TARGET: Critically audit L143's product Weitzenböck projection, full cubic zero locus and exact wrong-sign witnesses.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the pre-invocation Weitzenböck and invariant-module searches and duplicate/failure comparisons; the proposed audit changes no hypothesis, source formula, module, functional or technique and needs no new source search.
SOURCE_EVIDENCE: Previously inspected inputs are Oliveira–Waldron arXiv:1812.10866v2 (4.6), section 4.1 and Proposition 4.1 with its full projection/integration proof, PDF pp. 10–13, and Fowdar CMP 405 (2024), 183, section 2 (2.6); reuse their precise coverage, not an uninspected theorem.
COMPARISON: L143 specializes the cited general identity and gives an explicit quaternionic matrix calculation; a separate audit must distinguish the actual global equation from the universal pointwise sign test.
GAP: Independent review of source conventions, all Riemann terms, mixed-form norm, both bracket signs and the exhaustive zero-fibre argument is pending; no stronger conclusion or global realization is claimed.
REASON: Separate literature approval completed in step 453 by comparing the saved primary-source evidence with L143 hypotheses and stated audit scope; reuse SPECIALIZE coverage for the unchanged next mathematical audit.
SCOPE: Only verification of L143's stated product identity and pointwise sign/zero-locus test under the identical L071/L131 assumptions and previously covered Oliveira–Waldron/Fowdar inputs; no additional identity, estimate, global realization, connection splitting or new mechanism is covered.
COVERED_TARGET: Critically audit L143's product Weitzenböck projection, full cubic zero locus and exact wrong-sign witnesses.

The proposed audit retains the exact hypotheses of L071 and L131,
including the hypothetical actual SU(2) connection at the identical
metric and the full ch_2=-14e_1-21e_2-tau_D. Its essential result to
review is L143, including the full certificate at
`scripts/mixed-weitzenbock/product_coupling_certificate.json` and the
proof's complete matrix derivation. L095's weaker harmonicity is a
contrast, not a substitute for Delta_A R=0 or a new dependency.

Reuse the ready evidence in
[the differential assessment](2026-10-21-equality-mixed-curvature-weitzenbock.md)
and [the invariant-module assessment](2026-10-20-mixed-calibration-quartic-feasibility.md).
Primary links are [Oliveira–Waldron v2](https://arxiv.org/pdf/1812.10866v2#page=11)
and [Fowdar's version of record](https://link.springer.com/article/10.1007/s00220-024-05060-0).
No new source search or completed audit is asserted here. This is a
newly registered ready continuation based on the unchanged coverage,
and receives separate supervisor approval next turn. The mathematical
audit should correct a substantive error if found;
otherwise retain the scoped stop without counting it as a second negative
result. No route is reopened by that verification.

The main gap remains universal primitive Hodge realization. The audit
could validate useful negative route evidence, but it constructs no F,
cycle or transport. Global curvature realization and every independent
universal-Hodge gap remain unresolved. Mathlib matching coverage is not
checked. No audit has been performed or independently approved in this
registration. If it reveals an essential source gap or changes scope,
register that uncovered target as REVIEW_REQUIRED before dependent work.

## Separate approval — step 453, 2026-10-21

The registration statements above describe step 452; this paragraph
supersedes their pending-approval status, without claiming a mathematical
audit. Read the complete differential assessment and its completed source
working record, the invariant-module assessment's separate source review,
L143's hypotheses/conclusion and imported identity, ATTEMPTS/083 and
history/452. No fresh external retrieval was necessary: the target,
source version, coefficient category and invariant domain are unchanged.
This is the supervisor-required approval of reused coverage, not additional
literature discovery. LITERATURE_REASON: the newly registered continuation
required a separate approval turn; no essential unread source was identified.

The comparison covers the smooth metric-connection identity in
Oliveira–Waldron v2, section 4.1 (4.6), with (4.7)–(4.11) fixing bracket
conventions; its Proposition 4.1 projection/integration proof supplies
method coverage only. L131's conditional actual SU(2) connection is the
recorded applicability bridge. Fowdar, section 2 (2.6), covers the invariant
form module independently of the su(2) coefficient factor. Neither source
is asserted to contain L143's product formula or cubic classification.
Checking those specialized claims, their normalization and the complete
certificate is precisely the subsequent REPRODUCTION audit, and requires
no separate source theorem about a globally realized witness.

ATTEMPTS/083 records the result to verify, not permission to repeat the
sign search. The quartic stop and charge/moduli stops are contrasts only;
no stopped mechanism is reopened. The audit must inspect the entire
relevant proof and certificate, including zero mixed curvature, commuting
coefficients and cancellation with both pure blocks, rather than treating
sample values as exhaustive verification. No calculation or substantive
proof audit was performed in this literature turn.

DECISION remains SPECIALIZE and the exact TARGET is unchanged. This
approval is STALLED / LITERATURE / REPRODUCTION: it adds no mathematical
or source-discovery evidence and does not count the prior negative twice.
The next turn defaults to the approved proof audit. Preserve the scoped
stop if it survives; repair any substantive error. Any essential newly
exposed source gap or changed target requires REVIEW_REQUIRED before
dependent work. Mathlib coverage remains unchecked.
