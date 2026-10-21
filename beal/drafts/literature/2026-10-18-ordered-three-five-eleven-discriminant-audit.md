# Ordered (3,5,11) — discriminant application audit coverage

TARGET: Critically audit L094's coefficient-one maximal-discriminant application, retaining the entire algebra and every coordinate-divisor case.
CHECKED: 2026-10-18
DECISION: IMPORT
SEARCH_EVIDENCE: Reused exact-signature discovery and the discriminant-import assessment; inspected L094 and history/312–313 for duplication and scope, then reopened the narrowly relevant primary definitions, statement, table and proof.
SOURCE_EVIDENCE: Putz (2024), DOI 10.5463/thesis.832, version of record: Section 1.5.2/Proposition 1.16 p.22; equation (5.1) p.163; Section 5.2/Proposition 5.7 p.165; Table 5.8 and proof p.166; Remark 5.13 p.167, inspected on 2026-10-18.
COMPARISON: The existing source covers the proposed audit's exact scope: arbitrary nonzero pairwise coprime coefficients, nontrivial primitive coordinates and the discriminant of the entire maximal algebra; its unit-coefficient table does not require unit coordinates.
GAP: No essential source gap remains for this application audit; the source computation is imported without replay, and global algebra elimination and integer power lifting remain unresolved.
REASON: Approve the unchanged critical application audit using the existing citation; this turn resolves coverage only and does not complete the mathematical audit or derive a result.
LITERATURE_REASON: Separate approval of the newly proposed L094 critical audit was required by the startup gate; reuse prior discovery, with a focused primary-scope check rather than another literature search.
SCOPE: Citation-only critical audit of L094 under its stated positive primitive coefficient-one hypotheses, including all coordinate-divisor cases and every algebra component; no computational replay or field enumeration.

## Primary source scope

P. H. C. Putz, *Enumeration of local and global étale algebras applied to generalized Fermat equations*, VU Amsterdam doctoral thesis (2024), version of record, [DOI](https://doi.org/10.5463/thesis.832), [primary PDF](https://research.vu.nl/ws/portalfiles/portal/367784086/Thesis_CasperPutz.pdf). Printed pp.22,163,165–167 correspond to PDF indices 28,169,171–173.

Section 5.2 defines the source solution set by (5.1), with nonzero coordinates and gcd(ax,by,cz)=1, and the entire quotient algebra using parameter ax^5/(cz^11). Proposition 5.7 quantifies over nonzero pairwise coprime integer coefficients, rather than membership in Theorem 5.1's special nine-element set. The audit can therefore check coefficient one against this general statement without importing terminal exclusions for other coefficients.

Table 5.8 conditions on v_p(abc)=0 and records valuation sets {6,8,10}, {8,10}, {9,11} for p=3,5,11. Neither the proposition nor that table imposes v_p(xyz)=0. The source scope thus permits auditing cases where any coordinate has positive valuation, including the denominator coordinate. This observation concerns theorem coverage; the later audit must still verify L094's actual substitution and parameter identity.

Section 1.5.2 defines discriminants using an integral basis. Proposition 1.16 uses the integral closure and the product over every field component. It supplies exactly the maximal entire-algebra convention needed to check L094, without an irreducibility premise or polynomial-index identification.

The proof on p.166 invokes Algorithm 2.74 and ramification.m. Its additional transformations address nonunit-coefficient Table 5.11. No conditional hypothesis is stated for Proposition 5.7. No code has been inspected or executed here; the audit imports this computational theorem and must retain that qualification. Remark 5.13 explicitly warns about the coefficient-one degree-eleven Hunter workload. That warning remains evidence against merely launching that enumeration, rather than a ban on all algebra methods.

## Bounded decision and continuation

Coverage passes: every item on the proposed audit checklist lies within inspected source scope. The existing import assessment already supplies discovery and comparison; no uncovered mathematical subtarget is approved here. Mathlib coverage remains not checked. No new lemma, mathematical script, independent enumeration or result beyond Putz is produced.

Essential inputs for the next turn: L093, L094, this assessment and the cited source pages. Audit coefficients (1,1,1), coordinates (B,A,C), primitivity, the parameter and full algebra, the maximal discriminant convention, every coordinate-divisor case, table transcription and computational qualifications. Retain all components and source cases. No cross-notebook input is needed.

The main gap is still global elimination and integer power lifting for residual signatures. A passing audit would secure a necessary discriminant filter for later global-candidate elimination; it would not eliminate a candidate or establish a complete field list. Continue only if the actual L094 application meets all source hypotheses and retains the whole algebra; otherwise record the precise defect and park the unsupported restriction. The application audit itself remains pending for a separate research turn.
