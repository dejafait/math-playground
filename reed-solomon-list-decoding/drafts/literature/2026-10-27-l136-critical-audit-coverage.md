# L136 specialization audit — source coverage ready

TARGET: Critically audit L136's triple-direction cubic containment, including cyclic relabeling, source hypotheses, scalar extension, all collinear and reducible cases, and descent of a nonzero cubic to K.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the pre-invocation cyclic-cubic assessment and its exact-statement/source-following search; the step-531 local search of lemmas, audit records and relevant histories found no prior completed L136 specialization or audit. No fresh external search or originality claim.
SOURCE_EVIDENCE: Direct primary URLs https://arxiv.org/pdf/1710.00172v1 and https://arxiv.org/pdf/1104.4439v3 were accessed on 2026-10-28; Definition 2.1, Section 4 setup and Proposition 4.5 in the former, and standing assumptions and Proposition 6.1 in the latter were checked against the reused coverage. The reused assessment inspected Korchmaros–Nagy arXiv:1710.00172v1 Definition 2.1 and Proposition 4.5 with Section 4 setup/degenerate cases, and Korchmaros–Nagy–Pace arXiv:1104.4439v3 p. 3 standing assumptions and Propositions 2.3/6.1 with propagation cases; L135's hypotheses, dualization and accepted audit status were read in step 531.
COMPARISON: The cyclic theorem supplies cubic containment once the light-multinet conditions hold; L136 adds the explicit auxiliary relabeling, extension-preservation argument and elementary matrix-rank descent. The audit checks this specialization, not an original classification or a stronger containment statement.
GAP: Independently check every local applicability argument and the exact imported conclusion; no separate audit of L136 has yet been performed. Common-cubic gluing, span-two collapse, span three, deletion robustness and RS transfer are outside this target.
REASON: This separate literature-only turn confirms adequate reused coverage and supplies the missing direct primary URLs; the unchanged audit target is ready for a research turn. No essential unread source or new mathematical target was identified.
LITERATURE_REASON: The supervisor required a literature-only approval because the saved ready assessment lacked a direct source URL; this bounded access/scope check repairs that field without reopening discovery.
SCOPE: Only L136 under the stated L135 hypotheses: K=E or F, characteristic 65537, arbitrary actual labels, repeated messages, coefficient-difference span exactly two, and any three of L135's six or seven complete retained directions; no ordinary-net or noncollinearity assumption and no factor descent.

## Reused evidence and audit boundary

The precise citations, version distinctions, inspected proof cases and
source-access qualifications remain in
[the cyclic-cubic assessment](2026-10-27-l135-cyclic-cubic-containment.md).
L136 states them in its canonical proof. This audit can rely on the
audited L135 separation theorem; it need not rerun the 126 orbit cases.

Check the coefficients lambda=(b-c)/(b-a), mu=(c-a)/(b-a), their
nonzero denominators and the labeling of all ordered pairs in additive
F_137. Confirm that these are index permutations only. Check that the
actual 411 dual vectors lie in K, are distinct, and retain all required
incidences after extension, including repeated coefficient points.
Verify the all-collinear line-cube branch and the use of the full
Proposition 4.5 in every other case, retaining p=65537>n=137.
Check the 411-by-10 evaluation matrix, extension-invariant rank,
nonzero kernel and nonzero formal cubic over K. Neither factorization
nor uniqueness nor a single cubic for several triples follows.

The bounded pass test is a complete independent applicability and
descent check with no extra assumptions. A failed identity, missing
source hypothesis, zero form or unhandled allowed degeneration requires
a canonical correction or a narrowed conclusion. This is an ordinary
hypothesis/algebra audit, not a candidate audit of the main problem.
No new mathematical result has been derived or audited in this coverage
file. No creative collapse target is covered here.

## Separate source-gate review — 2026-10-28

Accessed the versioned [2017 primary PDF](https://arxiv.org/pdf/1710.00172v1)
and [2011 primary PDF](https://arxiv.org/pdf/1104.4439v3). Checked the former's
Definition 2.1 (printed p. 3), algebraically closed introduction,
Section 4 setup (p. 8) and full Proposition 4.5 proof (p. 10).
The setup excludes the wholly collinear case, so the proposed audit must
retain L136's separate line-cube branch. The proposition covers cyclic
light multinets; its proof retains the small-index degeneration branches
and checks distinct construction lines for the higher-index propagation.
No classification theorem with a long-line-nine hypothesis is imported.

Checked the latter's standing characteristic conditions (p. 3) and
Proposition 6.1 statement and initial pencil construction (p. 17).
Reuse the previously inspected complete propagation and Lamé cases
recorded in the linked cyclic-cubic assessment; they were not rederived
or re-audited here. The 2011 theorem is for ordinary dual 3-nets, not
itself the light-multinet import. The 2017 proposition supplies that
extension. The published Proposition 18 text remains unread; the
explicitly versioned arXiv proof remains the inspected reference.

The narrow local duplicate search found step 531's specialization and
no completed L136 audit in drafts/audits. ATTEMPTS/031–032 and 109 were
checked for route boundaries: fixed-core caps and unresolved residual
rank do not certify this audit or invalidate its separate source scope.
No stopped calculation is reopened. Mathlib coverage remains unchecked.

Decision: retain SPECIALIZE for exactly the saved target. This is a
source-link/process repair and repeated coverage confirmation, honestly
STALLED under the shared outcome rule, not a mathematical advance or a
fresh literature discovery. The separate approval is complete; the next
turn should perform the audit, with its algebra, projective extension,
collinear/reducible cases and rank descent still unverified. No lemma,
script, DAG edge or argument overview changed.
