# L091 remaining gates and closure audit — source comparison

TARGET: Critically audit L091's first/second gate formulas and complete seven-seed single-label closure certificate, retaining all finite-label denominators.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read full L091, L089 definitions/gates and relevant step-226 audit ranges, both closure-program interfaces, history/228 and ATTEMPTS/032–034; reused the ready fixed-H and involution assessments; searched Horn forward chaining/least fixed point and exact cyclic single-label RS terminology on October 15.
SOURCE_EVIDENCE: Reused Nguyen (2021), Section 2 and Proposition 1, as assessed in the L090 review; newly read Dowling–Gallier (1984), Definition 1, Algorithm 1 and recurrence (pp. 269–271), Theorems 2–3 with all proof cases and least-assignment corollary (pp. 272–273), in the author-hosted journal PDF.
COMPARISON: Standard projective and definite-Horn machinery covers unique fractional-linear recovery and least closure in principle; neither inspected source supplies the cyclic F/S identities, their exact rule templates, or the maximum-nine certificate, which require the separate local audit.
GAP: L091 correctness and all 11,440 closure cases remain unaudited; uniform rank R>=3, rank-27 existence, arbitrary-family coverage and challenge qualifications remain unresolved.
REASON: Essential general machinery and exact artifact scope are now covered; audit the saved specialization and full certificate next, without new gates, rules or elimination. No essential unread source was identified.
SCOPE: Entire saved L091 under fixed F_(97^20), order-sixteen H in F_97^*, bijective h and hypothetical nonzero full alternating kernel; first/second gates, their stated single-label rules and all seven-index closures only.
LITERATURE_REASON: The saved audit target was REVIEW_REQUIRED; the L090 comparison did not cover L091's remaining gates or closure machinery, so this separate source comparison was essential.

## Original proposal — step 240, historical

The following records the proposal before this separate review. The
completed decision above and comparison below govern continuation.

The next invocation is literature-only source comparison for exactly
TARGET. Reuse the ready kernel and involution comparisons where their
hypotheses match; do not repeat source discovery on unchanged inputs.
Read L091 to extract its precise claims, proof scope and certificate
paths before deciding what primary coverage is essential. Do not execute
its mathematical audit or replay during that source-comparison step.

The main gap remains uniform cyclic rank R>=3, within the unresolved
sixteen-count problem. The intermediate target is correctness of the
saved remaining gates and of the diagnostic limiting the specified
single-label propagation method. Downstream use is trustworthy necessary
equations and a verified limit on that method, without claiming a new
route to uniform rank or repeating a stopped calculation as research.

Essential proposed inputs are L089 and L090, under the same fixed
F_(97^20), H and arbitrary bijection; the nonzero kernel is hypothetical.
Use L091's full stated hypotheses when assessing the diagnostic. No
L092–L096 result, rank-27 labeling, or sufficient moment condition is
assumed. Full matching Mathlib coverage is not checked.

The eventual audit acceptance test is correctness of both gate formulas
with all nonzero denominators, faithful translation to the specified
single-label rules, and complete independent replay of the recorded
seven-seed closure cases and claimed maximum nine against sixteen.
Reject or narrow the corresponding claim if an identity, case omission
or replay failure is found. No H-label sweep, rank sample, new closure
rule, gate elimination or improved seed bound is proposed. Preserve
ATTEMPTS/020,032–034 and unfinished work. The existing stop applies to
the propagation mechanism, not to a separate check of its certificate.

## Completed source comparison — step 241

This literature-only step identifies audit obligations and source scope.
It does not check the gate identities, execute either program, verify
the saved certificate or derive a new mathematical result. No lemma,
mathematical script, DAG edge or argument overview is changed.

### Exact scope and reused inputs

Read L091 in full. Its conclusions separate two circuit specializations,
unique single-unknown deductions and a finite abstract-index obstruction.
The F rule excludes x; the S rules exclude q,e; D uses L090. The
whole-index templates have respectively ten, nine and six indices.
These are statements to check, not additional deductions this turn.

L089's definitions, gate statement and relevant step-226 audit passages
fix the unshifted circuit coefficients, normalization and three necessary
shared-coordinate equations. Reuse its audited L010/L087/L088 conventions.
Reuse `2026-10-14-cyclic-family-alternating-kernel.md` and
`2026-10-15-cyclic-six-label-critical-audit.md` for the unchanged fixed-H
and projective input comparisons. Nguyen's *Projective Line Revisited*,
J. Geometry and Graphics 25(2) (2021), Section 2, pp. 188–189, and
Proposition 1, p. 191, already cover the characteristic-not-two matrix,
affine and inversion cases. The ready assessment records the inspected
proof cases and primary URL; no repeated source retrieval is needed.
F_97 meets its field hypotheses. That comparison does not certify any
F/S formula, and the completed L090 audit covers only its saved claims.

### Primary closure comparison

Queries: `Horn clauses forward chaining least fixed point Dowling Gallier
1984 algorithm closure`; `"cyclic" "single-label" "Reed Solomon"
reconstruction gates`. No inspected exact cyclic theorem was identified;
this is not a novelty claim. Search snippets and secondary explanations
were screening material only.

William F. Dowling and Jean H. Gallier,
[*Linear-Time Algorithms for Testing the Satisfiability of Propositional
Horn Formulae*](https://www.seas.upenn.edu/~cis5110/Dowling-Gallier-Horn-sat.pdf),
Journal of Logic Programming (1984), 267–284, DOI
10.1016/0743-1066(84)90014-1; author-hosted journal scan, read
October 15, 2026. Read Definition 1 (p. 269), Algorithm 1 (p. 270),
the finite-set recurrence (p. 271), Theorems 2–3 and their proofs,
including unit, implication and negative-clause cases, and the
least-assignment corollary (pp. 272–273). These concern finite
propositional Horn clauses. The intended correspondence uses one
proposition per known index, seed facts, and each stated rule's
prerequisites implying its target. This definite-Horn case has no
negative constraints. The source covers propagation soundness and
least satisfying assignment, not the gate-to-rule translation or
maximum nine. Its linear-time refinement is unnecessary here.
Theorem 1's grammar equivalence uses Lemma I, whose proof the paper
omits; that equivalence is not needed as an independent input.

### Artifact obligations and continuation test

Read the complete short producer and verifier to identify interfaces
and update strategies, without auditing or executing them. The producer
uses sequential set updates; the verifier uses simultaneous bit masks.
Both share stated templates and Python, so implementation independence
is limited. The full result is
`scripts/cyclic-shared-gates/seed-reconstruction-result.json` and replay
report is `scripts/cyclic-shared-gates/seed-reconstruction-audit.json`.
Their qualification/scope fields were inspected with the shared JSON
inspector only as labeled previews; no numerical claim was verified.
The later audit must inspect every relevant case through full replay,
not infer correctness from that report or an attaining example.

The local history and ATTEMPTS/032 already record the nine-versus-sixteen
diagnostic; this is a correctness audit of that result, not a new failed
propagation attempt. ATTEMPTS/033–034 stop the separate expanded and
direct joint-elimination routes. No duplicate full L091 critical audit
was found in the targeted local comparisons. Nothing here restarts
those routes or the stopped positive-rank sampling. Matching Mathlib
coverage remains not checked, not absent.

Continue with exactly TARGET. Check the F/S reductions from L089,
wraparound windows, every finite-label denominator and all permitted
fractional-linear factors, then compare their whole/allowed templates
to both implementations. Reuse audited L090 for D. Independently replay
all 11,440 distinct seven-subsets and every terminal closure; confirm
the claimed maximum nine against sixteen, coverage, zero failures and
artifact identity, or record the first precise defect and narrow or
reject the affected claim. The abstract procedure's scope must retain
its stated rules; no inference about all possible reconstruction
algorithms is licensed. Do not add rules, eliminate gates, sample ranks
or sweep H-labelings. A new target would require separate assessment.

Decision SPECIALIZE licenses a later REPRODUCTION audit: general
machinery is known, but the saved circuit convention, denominators,
templates and finite cases require direct checking. That local checking
is needed for trust in existing inputs, not to claim a new general
closure theorem. This new bounded comparison is EXPLORATION with no
mathematical exploration usage and no progress beyond the sources
checked asserted. The exact approved target is retained for next turn.
