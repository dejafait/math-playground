# All smaller auxiliaries — ready calculation scope

TARGET: Test whether all subfields of MN of degree less than 36 jointly support a generalized norm relation for L96, certifying exhaustive subgroup coverage and the complete rational map-image rank.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed enlarged-scope comparison in drafts/literature/2026-10-11-ninety-six-all-smaller-auxiliaries.md, including exact-group queries, duplicate/failure comparison and primary finite-group algorithm inspection.
SOURCE_EVIDENCE: Etienne https://arxiv.org/pdf/2411.13124v2 Proposition 2.7 pp.12-15 and assessed orbital-map correspondence; GAP https://gap-system.github.io/gap/doc/ref/chap39_mj.html Sections 39.19-5,6 and https://github.com/gap-system/gap/blob/v4.15.1/lib/grplatt.gi#L2979-L2994; Hulpke https://arxiv.org/pdf/2012.01595v1 Sections 4,4.1 pp.15-17 and 3.2 pp.8-9 (reused inspected coverage).
COMPARISON: Known results provide a complete bounded-index procedure and arbitrary-copy relation criterion; the precise audited field group's qualifying subgroups and resulting rank have not been computed.
GAP: Certify all subgroup classes with index at most 35 and every rational equivariant map into Q[G/H]; runtime/backend availability, enumeration completeness and the actual rank remain unresolved.
REASON: A separate finite specialization can decide feasibility of smaller-field reduction before expensive arithmetic; no branch exclusion follows from relation existence alone.
SCOPE: Exactly TARGET over L055's MN, with arbitrary multiplicities and conjugate composita; no auxiliary class/unit computation, saturation/transfer, torsion lift, descent image or integer-emptiness claim.

Approved in the separate 2026-10-11 source-URL recovery turn (step 154).
No research calculation is invoked in this source-review turn.

The main gap is unconditional emptiness of L032's 96a1 branch, within a
much larger unresolved Beal target. The intermediate target is complete
algebraic auxiliary coverage. A positive test identifies fixed fields
for later arithmetic review; a complete negative test parks smaller
auxiliaries in this particular overfield, while preserving the pair stop.

Inputs: L051's exact L96=K96F of degree 36; L055's audited M,N, sign
fiber-product group of order 3960 and stabilizer H on the 36-pair set;
the cited Etienne criterion. L052-L054 and ATTEMPTS/018-022 remain
obstruction context, with no new cross-notebook input or GRH premise.

Use the primary `LowIndexSubgroups(G,35)` contract and complete rational
orbital-map test assessed in the completed source comparison. An
equivalent reproduction must prove its enumeration completeness; omit
neither perfect subgroups nor necessary construction stages. Neither
GAP nor Sage was found on PATH during assessment, so the actual execution
method must be established. Partial output or a backend error is an
unfinished attempt, not proof of nonexistence. Save unfinished work if
execution cannot complete within the bounded attempt.

Save complete subgroup generators/indices, backend/version and coverage
evidence, every map or equivalent constituent certificate, exact rank,
required rank 36 and all failures. With full coverage, rank 36 continues
to separate field/arithmetic review; a smaller rank stops only this
auxiliary set. All other global certificate and descent gaps remain.
The general theorems are imported by citation; only this exact
specialization needs reproduction. Mathlib coverage is not checked.

## Separate source-URL repair and approval — 2026-10-11

LITERATURE_REASON: The supervisor requires direct source URLs in the
ready assessment. The mathematical target and assumptions are unchanged;
this review repairs source traceability rather than repeating discovery.

Opened the primary Etienne v2 PDF and read Proposition 2.7's finite-group,
subgroup H and nontrivial auxiliary-subgroup hypotheses, arbitrary-copy
surjection and invariant-coverage clauses (printed p.12), and the relevant
implications in its proof (pp.12-14). The existing full assessment is
reused, including the orbital-map interface; no general theorem is reproved.

Opened the primary GAP manual's Sections 39.19-5,6 and read the entire
pinned v4.15.1 finite-group method at lines 2979-2994 through
https://raw.githubusercontent.com/gap-system/gap/v4.15.1/lib/grplatt.gi.
The documented bounded-index contract and implementation match the saved
procedure. Hulpke's previously inspected cases and qualifications are
reused from the completed enlarged-scope assessment, not claimed as
newly reread. The URLs above identify the actual primary sources.

Compared history/153 and ATTEMPTS/022: the rank-14 pair stop remains
valid evidence and is not reopened. The enlarged target has existing
source coverage but no computed answer. Approval permits precisely the
saved finite specialization. Backend success, exhaustive enumeration
and complete map rank still require certificates in the research turn.
This is a process repair with no new mathematical evidence, no claim
beyond the checked sources, and no change to Mathlib coverage.
