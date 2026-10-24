# Proposed critical audit of L108

TARGET: Critically audit L108's equilateral-triangle nonseparation proof, including exact source-orbit coverage, invariant averaging and full unordered demand pairing.
CHECKED: 2026-10-22
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step 401's discovery and failure comparison; step 404 opened its four exact primary URLs and located Theorem 2.1, Section 2.3, equations (62)–(65), the finite averaging paragraph and conditional-cardinality passage; no new discovery search or mathematical audit.
SOURCE_EVIDENCE: Dukes–Garaschuk https://arxiv.org/pdf/1608.06017v1 Sections 1.1,2.1 Theorem 2.1,2.2–2.3 pp.1,3–5; Schrijver https://homepages.cwi.nl/~lex/files/codes.pdf III.B (62)–(65) p.7; Polak https://arxiv.org/pdf/1703.05171v1 Section 1.2 p.3; Raghavendra–Tan https://arxiv.org/pdf/1110.1064v1 Section 3 Definitions 3.1,3.3 p.7 and conditional-cardinality passage pp.8–9; direct passages rechecked in step 404, with earlier coverage retained in foundations/04,12,13.
COMPARISON: The original SPECIALIZE assessment covers the completed test; the new target is a separate critical audit of its symbolic certificate, not a new optimization or a request to repeat the original discovery search.
GAP: Source coverage is sufficient; the separate mathematical audit must independently check all hypotheses, exact (i,i,i,0) realizability, repetitions, zero-demand edges, action preservation, unordered multiplicities and the limitations of the Farkas conclusion.
REASON: Step 404 repairs missing direct source URLs and confirms access and cited scope for the unchanged audit; it neither verifies L108 nor supplies a new mathematical result. No essential unread source was identified.

Inputs are L021,L098,L107,L108, foundations/04,12,13 and
`drafts/literature/2026-10-21-distance-dependent-triangle-dual.md`.
The main gap is still arbitrary-center 68/67 safety; a successful audit
would retain only the stop on the uncapacitated cone, and an error must
be repaired or explicitly invalidate that stop. Check N>2, nonnegativity
of all c_i, removal of exactly the two distinct repeated third supports,
and every i=1,...,68, including null edges. Independently verify the
four-region orbit ranges and positive binomial(956-i,i), and confirm
that averaging preserves the entire triangle set and the strict pairing.
No capacity, t-s lift, PSD or realization follows from finite cone membership.
Preserve all numerical-run stops and the exhausted translated-pole route.

## Completed audit-source comparison — step 403

LITERATURE_REASON: The newly proposed critical audit was outside the prior assessment's exact TARGET; this gate comparison checks its source scope without repeating external discovery.
SCOPE: Independent proof audit of L108 as written, using L021,L098,L107,L108 and foundations/04,12,13; no new cone optimization, source completion or capacity theorem.

The precise external imports and version qualifications are retained in
[the prior assessment](2026-10-21-distance-dependent-triangle-dual.md).
In particular Dukes–Garaschuk Theorem 2.1 is the arbitrary finite
nonnegative-system alternative, not a unit-demand decomposition theorem.
Sections 1.1 and 2.2 retain complete-graph edges of weight zero; Section
2.3 covers invariant dual tests. Polak's finite averaging passage requires
preservation of constraints. Schrijver's actual set-difference indices
retain t-s. The cardinality source does not itself prove the local
homogeneous conversion: L098 and L107 remain mathematical inputs to be
checked, with zero-probability and repeated-index cases retained.
These known inputs suffice to audit the existing specialization; none
asserts the specific equilateral or demand verdict. No general theorem
needs a reproof. The local geometry and normalization require independent
checking rather than a citation presented as their proof.

The audit should follow L108's existing proof in four bounded parts:
check the exact pair prescription against L021/L098 and the homogeneous
contraction; check the removal of exactly two repetitions against L107;
check the full coordinate action and the claimed actual equal-side
orbits against foundations/04; check every unordered class multiplicity,
the strict separator convention and the finite Farkas inference. The
nonseparation direction can be audited from a sufficient subset of
triangle inequalities, whereas a separating vector would need all
actual triangles. This distinction must not be mistaken for permission
to merge primal source variables with different t-s. No calculation or
verification of these claims was performed in this literature turn.

The main gap is arbitrary-center 68/67 safety. Retaining L108 after an
independent audit would make its limited stop reliable and route future
work toward constraints absent from the uncapacitated cone. Continue
only with this exact audit; retain the stop if every load-bearing claim
checks, or identify and repair/invalidate a specific faulty claim.
Neither decision authorizes a new uncapacitated solve. Capacities,
Boolean lower rows, full source lift, PSD and realization remain open.

The duplicate/failure comparison uses ATTEMPTS/081–082,088–091 and
histories/401–402. Their fixed-control, stopped numerical, independent-row,
restricted-support and sufficient-theorem outcomes are not substitutes
for the audit; ATTEMPTS/091 is precisely the conclusion under review.
No source blocker, changed hypothesis or source-level contradiction was
identified. This is a bounded coverage comparison, not a mathematical
advance or a novelty determination. No lemma, script, DAG or argument
was changed. Mathlib matching and supporting coverage remain not checked;
unknown availability supplies no evidence of absence.

## Direct-source repair — step 404

LITERATURE_REASON: Supervisor recovery identified missing direct source URLs in this assessment; inspect and attach those exact sources without broadening the mathematical target.

The four URLs in SOURCE_EVIDENCE were opened successfully on 2026-10-22.
The [Dukes–Garaschuk v1 PDF](https://arxiv.org/pdf/1608.06017v1)
states the finite nonnegative-system alternative in Theorem 2.1 (p.3),
defines the complete edge/triangle incidence matrix in Section 2.2
(p.4), and describes stabilizer averaging in Section 2.3 (p.5).
Section 1.1 keeps zero-weight edges. Its arXiv v1 header dates to
22 August 2016 while its title page prints 20 February 2020; retain
this observed qualification. The theorem concerns arbitrary real demands;
the simple-graph illustration is not the only available theorem scope.

[Schrijver's author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.B p.7, defines ordered triples through actual set differences in
(62)–(63); (65)(iii) retains t-s and permutes the three half-distances.
The explanatory paragraph following (65) was read too. No use is made
of the qualified complement prefactor (61).
[Polak v1](https://arxiv.org/pdf/1703.05171v1), Section 1.2 p.3,
checks action preservation and convexity before finite averaging.
This supports the method; the proposed S_1024 action and preservation
of L108's strict pairing remain local audit obligations.

[Raghavendra–Tan v1](https://arxiv.org/pdf/1110.1064v1), Section 3,
the conditional-cardinality passage p.8 and its continuation p.9,
gives consistent local distributions and the conditional marginal
constraint, while explicitly warning that a global distribution need
not exist. The text extraction corrupts the display's expectation
symbol; reuse foundations/13's earlier inspected formula rather than
claim a fresh formula transcription. L098's homogeneous conversion,
zero-probability cases and removal of repetitions are local proof
obligations, not conclusions imported from this paper.

This is a process repair, outcome STALLED: source accessibility and
citation completeness are improved, but the prior SPECIALIZE decision
is unchanged and no new mathematical evidence is claimed. Existing
duplicate/failure comparisons above are reused. The intermediate target
remains the exact L108 critical audit, whose downstream use is a reliable
stop on this limited cone diagnostic. Retain the stop only after every
load-bearing local claim checks; repair or invalidate it upon a specific
failure. Capacities, the full source lift, PSD and RS realization remain
unresolved. No lemma, mathematical script, argument or DAG is changed.
