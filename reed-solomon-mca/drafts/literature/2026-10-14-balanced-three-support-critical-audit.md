# Proposed critical audit of L084

TARGET: Critically audit L084's balanced three-support extraction, including the nonlinear bridge, finite component girth and Ellis–Linial bound specialization.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact searches and duplicate/obstruction comparison in 2026-10-14-balanced-three-support-nine-union-extraction.md; compared that coverage with L084 and the exact proposed audit scope. No broader discovery search was needed.
SOURCE_EVIDENCE: Reopened Ellis–Linial arXiv:1302.5090v5 (12 July 2017), Section 1 printed pp. 3–4 and Section 2 Lemma 1 equations (5)–(6), printed pp. 5–6, including its complete two-case proof; reused the prior exact-target comparison.
COMPARISON: The same finite regular Berge-girth theorem covers the external input of the proposed audit; L084 adds only the previously identified nonlinear/triangle and component bridges. The audit changes no incidence hypotheses and needs no new external theorem.
GAP: Source coverage is ready; correctness of the written bridges, component regularity and specialization remains for a separate critical proof audit. RS completion and challenge qualifications are outside this approval.
REASON: This separate source-scope comparison approves the unchanged critical-audit target for a later REPRODUCTION research turn; it neither audits nor adds mathematics.

Essential input is L084, an abstract theorem with no local lemma inputs.
Reuse the prior extraction source evidence and its explicit versions and
proof-case coverage when approving this scope. L010 is only the prospective
RS applicability context; L032/L041 are not inputs. No cross-notebook
result is proposed. This source-checking approval turn has read the essential evidence and
has not performed the proof audit itself.

A later audit should accept the scoped theorem only if every short-cycle
case, finite girth argument and Moore-bound hypothesis holds, or record
and repair a specific defect. The theorem supplies a cluster only; moment
compatibility, completion of the triangle row, arbitrary-family assembly
and challenge qualifications remain unresolved. No complete candidate is
asserted. Mathlib coverage remains not checked.


## Completed source-scope review — 2026-10-14

LITERATURE_REASON: The new critical-audit target required its own source-scope approval; the prior extraction assessment is reused rather than repeating discovery searches.
SCOPE: Audit only L084 under its stated simple sixteen-edge, sixteen-vertex, four-uniform, degree-four hypotheses, using the cited Berge-girth Moore bound; no RS applicability theorem is approved here.

The versioned primary PDF was retrieved directly at
https://arxiv.org/pdf/1302.5090v5. Read the cycle definition on printed
p. 4, and the complete Lemma 1 statement and proof on printed pp. 5–6.
Its hypotheses are finite uniformity and regularity with d>=2 and
r,g>=3. Both parity formulas and the vertex-centered versus edge-centered
proof cases are available. No connectivity or asymptotic hypothesis is
imposed. This matches the external theorem L084 invokes. The source does
not itself establish L084's nonlinear or triangle bridges, nor the
existence of a finite-girth component; those remain audit obligations.

Read L084 only to identify its statement, cited input and bridge scope,
not to certify those arguments. The prior extraction assessment's
Shangguan comparison and its exact search record remain adequate:
no changed target requires refreshing that broader search. Reviewed
history/204 and history/205 and searched ATTEMPTS/016,017,027 for the
relevant stopped conclusions. They concern disjoint triples, six-edge
small unions or useful additional pairs, not this audit. No historical
stop is overturned, and no second extraction result is sought.

SPECIALIZE permits a later REPRODUCTION proof audit of exactly TARGET.
Accept only if every bridge and theorem hypothesis survives that audit;
otherwise record a precise defect and its effect on the scoped theorem.
There is no source blocker, new result, complete candidate or global
count improvement in this review. Mathlib coverage remains not checked.
