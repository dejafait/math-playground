# Step 344 — conditional L094 audit, working record

Main gap: arbitrary-center 67/68-agreement safety; bracket 955–957.
Approved intermediate target: Critically audit L094's two-mixed-row subsystem witness and saved Phase I trace without new optimization or omitted-mode tests.
Reuse the supplied SPECIALIZE assessment `literature/2026-10-19-two-mixed-row-witness-critical-audit.md` unchanged. Downstream use is a reliable necessary-subsystem input for a separately assessed stronger test. Continue only if full original/raw reconstruction, both singular blocks and all 317 saved pivots agree; preserve any first discrepancy, separating trace provenance from independent feasibility.

Inputs: L021,L053,L073,L075,L076,L078,L082,L083,L084,L086,L090,L091,L092,L093,L094. Freeze rho,p8,pairs,seven RREF/completion,L086 columns,t78=s and all L094 moments. Retain 85 domain rows,90 kernel equations,500 types/3000 presentations,36 forced entries,28 equalities,43 zero-old-block modes,rows23=(2,5)/31=(3,4),45 signs,full anchor,whole singular ranges and positive raw scales. Foundations/04,09,10,12 ancestral PSD,uniqueness,whole-kernel and normalization remain conditional; no recursive ancestral review is attempted.

L092's existing audit is a method reference, not evidence for L094's different witness. L093's rejection concerns the old L092 assignment. ATTEMPTS/071 and /077 retain the capped full-system and two-row nonexclusion decisions. L094's verifier explicitly does not replay pivots. Planned audit reconstructs all relevant coefficients with the existing independent source audit (its residual evaluations concern the OLD L086 witness only), then independently checks L094's retained system and saved trace. No optimizer or constructor is called. The new script and complete certificates will be under `scripts/finite-support/two-mixed-row-critical-*`.

Other 28 modes,scalar upper rows,other anchors/columns/base/pairs,global moments,representing measures,RS realization and exact boundary remain unresolved. This step is RESEARCH / REPRODUCTION / proof_audit; no new lemma or novelty claim is intended. Historical elapsed time cannot be independently observed by replay.

## Completed audit

The sole invocation of `critical_audit_two_mixed_row.py` completed without
mathematical or trace discrepancies. Its independent source reconstruction
passed 7993 checks; the fresh original/raw verifier passed 426; the new
audit passed 2725, including all 317 saved pivots, both complete tableaux
and final transform, both equality-lift directions, all retained residuals,
and both four-by-four block congruences and all 30 principal minors.
Canonical proof,citations,qualifications and full evidence paths are in
L094. The original construction and trace files were not changed.

All 56 original/raw equality residuals vanish. Retained mode signs are
14 positive/31 zero; moment signs are 33 positive/12 zero. Row23 is tight;
row31's normalized remainder is in [153320960,153320961). Actual minimum
original/raw inequality values are 0, meeting the required bound 0.
No L094 omitted-mode evaluation or optimizer/constructor invocation
occurred. Historical time and the single-run claim are not independently
observed. All ancestral assumptions remain conditional.

Tooling note: the first bounded inspector calls failed at Python's default
4300-digit JSON integer limit (a tableau integer has 4331 digits).
Repeating only those read-only inspections with PYTHONINTMAXSTRDIGITS=0
succeeded for the complete /summary and /failures fields; the certificate
and mathematics were unchanged. No mathematical rerun was needed.

Outcome ADVANCE / RESEARCH / REPRODUCTION / proof_audit establishes a
reviewed conditional local input, without progress beyond assessed methods
or an RS boundary improvement. Mathematical exploration usage remains 0/3.
PROOF.md and DAG.md remain unchanged because the assembled argument and
mathematical inputs did not change. The sole proposed continuation is
the exact 28-complementary-mode residual test in the new REVIEW_REQUIRED
assessment; it is neither performed nor approved in this turn.

### Old-block classification correction

A final selected determinant inspection exposed imprecise scope wording:
the two added OLD blocks are not both singular. The complete determinant
of B23 is positive, while det(B31)=0. The executed audit had checked all
minors,whole range equations and congruences without assuming either
invertibility or singularity, so no arithmetic verdict changes. The
executed script's historical comment is preserved with its certificate
hash; this note and canonical L094 supersede that comment and the initial
working shorthand. The four-check supplement
`inspect_two_mixed_row_block_ranks.py` independently recomputes both full
determinants from the complete audited matrices and confirms their saved
values and signs, with no failures. Full evidence is
`scripts/finite-support/two-mixed-row-critical-block-classification.json`.
No omitted mode or optimizer was invoked. This is a real qualification
repair, not a new theorem or boundary improvement.
