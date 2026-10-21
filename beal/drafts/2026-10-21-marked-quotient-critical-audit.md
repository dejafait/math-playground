# L111 critical audit — working record

2026-10-21. Approved target: Critically audit L111's marked twist,
degree-two genus-one quotient, rational origin and normalized lifting interface.
Prior SPECIALIZE coverage is
`literature/2026-10-20-marked-genus-one-quotient-critical-audit.md`.

Main gap: residual positive primitive integer exclusion, here the
rational-factor branch of ordered (3,5,11). The intermediate target
is independent verification of the existing L111, with no new lemma.
Its downstream use is a reliable genus-one necessary image for point
methods. Continue only if the exact twist, both field compositions,
geometric component, degree, proper charts, origin and all rational
fibers pass; repair or park a specific failed assertion otherwise.

Read L111 completely, audited L110 completely and the exact L109
definitions and normalized-unit proof. Reused the supplied primary-source
assessment; compared history/385 and ATTEMPTS/050. No duplicate quotient
is needed; the exhausted Jacobian rank detector and unfinished L108
remain preserved. No cross-notebook input is used.

Saved before arithmetic work: the written field and chart arguments
appear consistent. The finite model is finite free of rank two over
the quartic chart, including h=0; a ramified fiber must be recorded as
Spec(Q[h]/(h²)), not as two sign choices. Independent arithmetic replay
and complete certificate inspection are still pending. SymPy is not
installed; use an independent standard-library quotient-algebra checker,
without importing the producer or its nested arithmetic classes.

Independent gaps remain E(Q) completeness, degree-nine distinguished-root
recovery, remaining factors, both L095 systems and minus-eleven. An origin
at the original boundary gives none of those conclusions.

## Completed audit

The audit passes without changing the mathematical conclusion. Full
proof, qualifications and source citations are canonical in
[L111](../lemmas/L111-marked-pair-genus-one-quotient.md), under its
2026-10-21 independent-audit section. The finite-free chart proof
also makes the ramified fiber multiplicity explicit.

`python3 scripts/pair-genus-two/audit_marked_quotient.py` reports
94 passing checks, no failures, degree 2/2 and quotient genus 1/1.
The complete evidence is
`scripts/pair-genus-two/marked-quotient-audit-certificate.json`.
It independently compares the entire original certificate, using
four-dimensional quotient algebras and multiplication-matrix inversion,
with no producer imports. All sixteen full residuals, all check flags,
gcds and normalized boundary values were inspected. Both u,z are
preserved, hence so is every term of the complete original scalar H0;
no new scalar expansion or scalar descent is assumed. The original
certificate and producer are unchanged. No arithmetic or mathematical
failure occurred in this replay.

Outcome: RESEARCH / ADVANCE / REPRODUCTION; actual type proof_audit.
The advance is a verified local input, not a new theorem beyond the
inspected sources or an integer exclusion. Existing direct inputs
L109/L110 remain exact, so DAG.md needs no change. PROOF.md's argument
is unchanged; the canonical L111 and current checkpoint record the
completed audit. Preserve all earlier unfinished work and stops.

The proposed continuation is the rank-zero test for this elliptic
quotient, requiring a separate source review before mathematical work.
This is distinct from ATTEMPTS/050's exhausted bounded genus-two
Jacobian detector. Its assessment is newly REVIEW_REQUIRED; this
audit neither computes rank nor approves an uncovered rank method.
