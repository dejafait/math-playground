# Printed staircase inequality: bounded audit nomination

TARGET: Audit Planat202604.1239v2 Lemma11's staircase sum bound uniformly in integer d>=2 and 0<tau<1, determining whether this printed input can support its growing-degree error estimate.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step559's three-source comparison; a narrow filename check found no Planat/staircase/finite-strip assessment or stop. No novelty inference or theorem import.
SOURCE_EVIDENCE: Planat Preprints202604.1239v2, Section3.3 Theorem3.2 complete bulk/edge proof and embedded Lemma11 statement/proof, https://www.preprints.org/manuscript/202604.1239 ; exact inequality below. Published version unread after failed access.
COMPARISON: This audit tests a printed elementary inequality without accepting the source's family normalization or RH claims. Exact variables, quantifiers and proof are accessible; no additional analytic theorem is essential to this bounded check.
GAP: Mathematical validity and endpoint behavior remain unchecked; this nomination performs no evaluation or counterexample construction.
REASON: A direct quantifier/arithmetic audit is independently testable after the bulk import failed; retain the bound at its exact scope or identify a rigorous failure before downstream use.
SCOPE: Only the printed inequality and its use as a uniform input; no repair of the source theorem, coefficient identification, numerical sweep, root-stability reproof or actual-Xi sign conclusion. Newly written readiness requires separate approval next turn.
LITERATURE_REASON: Step559 exposed an explicit, previously unassessed source claim; reuse its inspected statement and full proof rather than browse again.

The printed claim is an absolute C, independent of both variables, with

\[
 \sum_{k=0}^{d-2}\binom dk\tau^{(d-2-k)/2-1}
 \le C d^{10/3}\qquad(d\ge2,\quad0<\tau<1).
\]

Check individual endpoint summands before the longer proof. An exact
admissible violating family rejects this quantification; acceptance
requires an absolute C on the entire domain. A relation restricting tau
and d would be a different assertion requiring its own comparison.
No value or limit is evaluated in this literature nomination.

Main gap: actual-Xi all-degree mixed positivity. Downstream use:
prevent an unsupported uniform input from being mistaken for a bulk
sign estimate. Even a valid bound leaves actual normalization, shift
zero, barriers and arcs unresolved. This is a conventional source audit,
not a creative mechanism or an RH candidate. Intended classification:
REPRODUCTION; proof_audit/routine_audit, standard/high.

Essential input: the printed claim and quantifiers. L019/L021/L795
motivate relevance but are not premises for this elementary check.
No cross-notebook result or numerical certificate is needed. Mathlib
coverage is unchecked. Preserve any failure with its narrow consequence;
a source failure does not refute RH.
