# Coupled distance-shell lead — completed source review

TARGET: Assess Kim–Toan Theorem 17 for a coupled distance-shell exclusion test of L022's unchanged A(1024,10,68) extension.
CHECKED: 2026-10-06
DECISION: IMPORT
SEARCH_EVIDENCE: Scoped searches of foundations/04, selected/strengthened SDP assessments, ATTEMPTS/012–016 and history/042,050 found no earlier shell-coupling assessment; searched Kim Toan Theorem 17 constant weight distance distribution and constant weight distance distribution doubly constant upper bounds Agrell Vardy Zeger.
SOURCE_EVIDENCE: Read Kim–Toan arXiv:1212.3467v1 III.C.3 definitions (46)–(50), Proposition 15 (51)–(52), Lemma 16 (53)–(54), Theorem 17 (55) and complete proof (56)–(59), printed pp. 11–12; checked Theorem 19 prerequisites on p. 14 and the alpha<=0 alternative lead on pp. 16–17.
COMPARISON: The imported maximum-distance formula rules out every distinct eligible shell pair at (1024,10,68): m_ij>=22>10; Theorem 17 gives only singleton bounds and cannot supply the proposed coupling, regardless of coefficient precision.
GAP: This coupled mechanism is inapplicable; singleton shell feasibility, other strengthened inequalities, omitted PSD blocks, full-SDP feasibility and arbitrary-center safety remain unresolved.
REASON: Precise primary hypotheses settle the gate target negatively without a calculation; import only that applicability assessment and park Theorem 17 coupling at this instance.
LITERATURE_REASON: The saved target was uncovered; its exact primary hypotheses and proof cases were essential unread evidence beyond the ready Theorem 12 assessment.
SCOPE: Source-only review of Theorem 17 applicability to the unchanged L022/L023 instance; no coefficient computation, new lemma or mathematical script.

The main gap is arbitrary-center safety at 68 agreements, with
955<=t_star(m)<=957. The intermediate target was a coupled distance-shell
inequality excluding L022's unchanged above-threshold extension. A valid
exclusion could motivate stronger support bounds, transferred to tuple
lists using L001/C001a; exclusion of one assignment would not itself
prove safety. The continuation test was an eligible multi-shell set and
an applicable effective coefficient prescription. The abandonment test
was failure of its geometric prerequisite. The latter is now met.

The precise imported statement, proof coverage, specialization and
Mathlib qualification are canonical in
[foundations/05](../../foundations/05-distance-shell-source.md).
In source notation H={5,...,68}, v=956. Distinct shell indices have
11<=i+j<=135; (51) yields 2(i+j) below 68 and 136 otherwise.
The minimum is 22, while (55) requires each pair maximum below d=10.
All eligible H_1 are therefore singletons. The adjacent equality-case
Theorem 19 also requires i+j>=956 and cannot apply. No numerical
certificate, unknown exact T value or reproof is needed for this source
comparison. The conclusion is a route obstruction, not unsafety or a
new result beyond the sources checked.

This failure is different from L025's passing weakened four-block rows:
Theorem 17 has no coupled rows here even with exact Q_i. It is also
different from L021's optimized pair LP and L023's ordinary scalar pass.
No redundancy of the remaining individual-shell inequalities is claimed.
Preserve all stops, especially ATTEMPTS/016's cap and unchanged assignment.

## Unapproved continuation lead

Kim–Toan printed pp. 16–17 explicitly points to Theorem 21, citing
Agrell, Vardy and Zeger, *Upper bounds for constant-weight codes*, IEEE
Trans. Inform. Theory 46(7) (2000), 2373–2395, Proposition 17. Its
conditional doubly-bounded-weight coefficients T' differ from Theorem
17's mutual shell incompatibility. The restatement and definition of
T' were read, but the original Proposition 17 and proof were not.
The coefficient orientation, allowed replacements, ratio cases, and
effective strength for a fixed pair remain uncovered. A search also
returned a doubly-constant-weight LP paper
(DOI 10.1016/j.ffa.2018.08.009); its DOI fetch failed, and it is an unread
lead, not an essential input to this completed rejection.

The new proposed (67,68)-shell review is separately recorded as
REVIEW_REQUIRED. No applicability, conditional coefficient bound or
violation for that target is derived or approved here. It is a distinct
conditional mechanism, not a widened residual cap or retuned assignment.
